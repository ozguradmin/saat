#!/usr/bin/env python3
"""ozgur kadran üreteci.

Kadranı tek bir geometriden iki üretim yoluna hazırlar:

  * Lazer: 1:1 DXF (siyah-altın lazer alüminyumu için; KESIM + ALTIN katmanları)
  * PCB:   Gerber + Excellon delik dosyaları (0.4 mm FR4, ENIG altın, siyah/mavi/yeşil maske)
  * Önizleme PNG/SVG'leri ve 3D önizleme sayfası için maske dokusu

Üç stil var (PARAM["stil"]):
  klasik  -> ince çubuk saat işaretleri, 12'de çift çubuk
  rakamli -> 12, 3, 6, 9'da rakamlar, diğer saatlerde çubuk
  sektor  -> eş merkezli halkalar, 1-12 rakamlı saat halkası, ince artı çizgisi

Katmanların anlamı (üstten bakınca):
  altın -> lehim maskesi açılmış bakır = ENIG altın görünür (lazerde: kaplaması yakılan alan)
  gölge -> maskenin altında kalan bakır = ton-sür-ton ışınsal doku (yalnız PCB'de görünür)

Kullanım:  python3 kadran.py stil=klasik tarih_penceresi=false
Bütün ölçüler milimetre.
"""

import json
import math
import sys
import zipfile
from pathlib import Path

import numpy as np
from shapely import affinity
from shapely.geometry import LineString, MultiPolygon, Point, Polygon, box
from shapely.ops import unary_union

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.font_manager import FontProperties  # noqa: E402
from matplotlib.path import Path as MplPath  # noqa: E402
from matplotlib.patches import PathPatch  # noqa: E402
from matplotlib.textpath import TextPath  # noqa: E402

BURASI = Path(__file__).resolve().parent
FONT_DIR = BURASI / "fontlar"

PARAM = {
    # --- kart ---
    "stil": "klasik",         # klasik | rakamli | sektor
    "cap": 28.5,              # Seiko föyü: Ø28.50 ±0.05 (NH35/36/38/39 ortak)
    "kalinlik": 0.4,          # PCB kalınlığı (sipariş formunda seçilir; NH35 standardı ~0.4 mm)
    "merkez_delik": 2.10,     # Seiko föyü: Ø2.05 — üretim toleransı için +0.05
    "kenar_payi": 0.35,       # bakırın kart kenarından en az uzaklığı
    "tarih_penceresi": False, # NH35/NH36 kullanılırsa True: saat 3'te pencere açılır
    "ayak_delikleri": False,  # True: resmî kadran ayağı konumlarına Ø0.70 pim delikleri (PCB + tarihli için önerilir)
    "tarih_pencere_r": 10.55, # Seiko föyü: pencere merkezi 10.55 mm, saat 3 yönü
    "tarih_pencere_g": 2.90,  # pencere genişliği (radyal)
    "tarih_pencere_y": 2.00,  # pencere yüksekliği (teğetsel)
    # --- logo ---
    "logo": None,             # None -> stilin kendi yazımı (OZGUR / ozgur); istenirse "özgür" vb.
    # --- dakika halkası (ortak) ---
    "dakika_ic": 12.70,
    "dakika_dis": 13.30,
    "dakika_gen": 0.15,       # PCB ve asit için en az 0.15
    "bes_dakika_gen": 0.24,
    # --- maske/bakır payları ---
    "bakir_tasma": 0.05,      # altın alanların bakırı maske açıklığından bu kadar taşar
    "isinsal_doku": True,     # PCB'de maske altı ışınsal (sunburst) çizgiler
}

STILLER = {
    "klasik": {"logo": "OZGUR", "font": "Marcellus-Regular.ttf", "boy": 1.15, "aralik": 0.42, "olcu": "H", "logo_y": 6.15},
    "rakamli": {"logo": "ozgur", "font": "Jost-Medium.ttf", "boy": 1.25, "aralik": 0.06, "olcu": "x", "logo_y": 5.75},
    "sektor": {"logo": "OZGUR", "font": "Jost-Regular.ttf", "boy": 0.95, "aralik": 0.45, "olcu": "H", "logo_y": 4.40},
}

RENKLER = {
    "gece": {     # siyah maske + ENIG
        "maske": (0.035, 0.037, 0.042),
        "maske_kabartma": (0.075, 0.078, 0.086),
        "altin": (0.93, 0.76, 0.42),
    },
    "iznik": {    # mavi maske + ENIG
        "maske": (0.03, 0.12, 0.36),
        "maske_kabartma": (0.06, 0.20, 0.50),
        "altin": (0.93, 0.76, 0.42),
    },
    "zumrut": {   # yeşil maske + ENIG
        "maske": (0.02, 0.20, 0.13),
        "maske_kabartma": (0.04, 0.30, 0.20),
        "altin": (0.93, 0.76, 0.42),
    },
}


# ----------------------------------------------------------------------------
# yardımcılar
# ----------------------------------------------------------------------------

def kutup(r, aci_derece):
    """Saat yönünde, 12'den başlayan açı -> (x, y). 12 = +y."""
    a = math.radians(90.0 - aci_derece)
    return (r * math.cos(a), r * math.sin(a))


def cizgi(p, q, gen):
    return LineString([p, q]).buffer(gen / 2.0, cap_style=2, join_style=2)


def halka(r, gen, seg=720):
    return Point(0, 0).buffer(r + gen / 2, seg).difference(Point(0, 0).buffer(r - gen / 2, seg))


def yazi(metin, boy, font, aralik=0.0, olcu="H"):
    """Metni shapely çokgenine çevirir; (0,0) taban çizgisinin ortası.

    boy: `olcu` harfinin yüksekliği (büyük harf için "H", küçük harf için "x").
    aralik: harfler arasına eklenen boşluk, boy'un katı olarak.
    """
    fp = FontProperties(fname=str(FONT_DIR / font))
    ref = TextPath((0, 0), olcu, size=1.0, prop=fp).get_extents()
    em = boy / ref.height
    parcalar = []
    x = 0.0
    for harf in metin:
        if harf == " ":
            x += em * 0.3 + aralik * boy
            continue
        tp = TextPath((0, 0), harf, size=em, prop=fp)
        geo = None
        for h in tp.to_polygons():
            if len(h) < 3:
                continue
            pg = Polygon(h).buffer(0)
            geo = pg if geo is None else geo.symmetric_difference(pg)
        if geo is None:
            continue
        minx, _, maxx, _ = geo.bounds
        parcalar.append(affinity.translate(geo, x - minx, 0))
        x += (maxx - minx) + aralik * boy
    toplam = unary_union(parcalar)
    minx, _, maxx, _ = toplam.bounds
    return affinity.translate(toplam, -(minx + maxx) / 2.0, 0.0)


def ortala(g, x, y):
    """Geometrinin sınır kutusunun merkezini (x, y)'ye taşır."""
    minx, miny, maxx, maxy = g.bounds
    return affinity.translate(g, x - (minx + maxx) / 2, y - (miny + maxy) / 2)


def cubuk(r0, r1, gen, aci, kaydir=0.0):
    """Saat yönünde `aci` derecede, r0..r1 arasında dikdörtgen çubuk."""
    pg = box(-gen / 2 + kaydir, r0, gen / 2 + kaydir, r1)
    return affinity.rotate(pg, -aci, origin=(0, 0))


# ----------------------------------------------------------------------------
# stiller
# ----------------------------------------------------------------------------

def dakika_halkasi(P, r_ic=None, r_dis=None, besli_uzun=0.12):
    r_ic = P["dakika_ic"] if r_ic is None else r_ic
    r_dis = P["dakika_dis"] if r_dis is None else r_dis
    out = []
    for m in range(60):
        if m % 5 == 0:
            out.append(cizgi(kutup(r_ic - besli_uzun, 6 * m), kutup(r_dis, 6 * m), P["bes_dakika_gen"]))
        else:
            out.append(cizgi(kutup(r_ic, 6 * m), kutup(r_dis, 6 * m), P["dakika_gen"]))
    return out


def stil_klasik(P):
    altin = dakika_halkasi(P)
    for h in range(12):
        if h == 3 and P["tarih_penceresi"]:
            continue
        if h == 0:
            altin += [cubuk(9.65, 12.15, 0.50, 0, -0.42), cubuk(9.65, 12.15, 0.50, 0, 0.42)]
        else:
            altin.append(cubuk(9.95, 12.15, 0.62, 30 * h))
    return altin, []


def stil_rakamli(P):
    altin = dakika_halkasi(P)
    rakam_r = {0: 10.55, 3: 10.75, 6: 10.55, 9: 10.75}
    for h in range(12):
        if h in rakam_r:
            if h == 3 and P["tarih_penceresi"]:
                continue
            g = yazi(str(12 if h == 0 else h), 2.25, "Jost-Medium.ttf", aralik=0.04)
            altin.append(ortala(g, *kutup(rakam_r[h], 30 * h)))
        else:
            altin.append(cubuk(10.25, 12.15, 0.52, 30 * h))
    return altin, []


def stil_sektor(P):
    altin = []
    # dış dakika halkası: iki ince çember arasında çentikler
    altin += [halka(12.05, 0.13), halka(13.30, 0.13)]
    for m in range(60):
        gen = P["bes_dakika_gen"] if m % 5 == 0 else P["dakika_gen"]
        r0 = 12.05 if m % 5 == 0 else 12.55
        altin.append(cizgi(kutup(r0, 6 * m), kutup(13.30, 6 * m), gen))
    # saat halkası: 1-12 rakamları
    altin.append(halka(9.05, 0.13))
    for h in range(1, 13):
        if h == 3 and P["tarih_penceresi"]:
            continue
        g = yazi(str(h), 1.25, "Jost-Medium.ttf", aralik=0.02)
        altin.append(ortala(g, *kutup(10.55, 30 * h)))
    # iç disk: ince artı çizgisi
    for a in (0, 90, 180, 270):
        altin.append(cizgi(kutup(1.75, a), kutup(9.05, a), 0.13))
    # dokular: saat halkasında eş merkezli, iç diskte ışınsal (yalnız PCB)
    golge = [halka(r, 0.07, 360) for r in np.arange(9.35, 11.95, 0.16)]
    return altin, golge


STIL_FONK = {"klasik": stil_klasik, "rakamli": stil_rakamli, "sektor": stil_sektor}


# ----------------------------------------------------------------------------
# geometri
# ----------------------------------------------------------------------------

def geometri(P):
    R = P["cap"] / 2.0
    S = STILLER[P["stil"]]
    altin, golge = STIL_FONK[P["stil"]](P)

    logo = yazi(P["logo"] or S["logo"], S["boy"], S["font"], aralik=S["aralik"], olcu=S["olcu"])
    logo = ortala(logo, 0, S["logo_y"])
    yazilar = [logo]
    # diğer altın öğeler (ör. sektör stilindeki artı çizgisi) logoya 0.35 mm'den fazla yaklaşmasın
    temiz = unary_union([y.buffer(0.35) for y in yazilar])
    altin = unary_union(altin).difference(temiz).union(logo)

    # ışınsal doku (PCB'de maske altı bakır): çizgiler merkeze yakın sıklaşmasın diye kademeli başlar
    if P["isinsal_doku"]:
        ic_sinir = 9.05 if P["stil"] == "sektor" else P["dakika_ic"] - 0.45
        for k in range(240):
            r0 = 2.2 + ((k * 0.6180339887) % 1.0) * 3.4   # düzensiz başlangıç: halka izi oluşmaz
            golge.append(cizgi(kutup(r0, 1.5 * k), kutup(ic_sinir - 0.2, 1.5 * k), 0.09))
    golge = unary_union(golge) if golge else Polygon()

    # --- kesimler ---
    kart = Point(0, 0).buffer(R, 1440)
    delikler = [Point(0, 0).buffer(P["merkez_delik"] / 2.0, 256)]
    if P["ayak_delikleri"]:
        # Seiko/TMI föyü: F1 (+9.672, +8.667), F2 (-9.466, -8.930), ayak Ø0.64 (kurma kolu saat 3'te)
        for x, y in ((9.672, 8.667), (-9.466, -8.930)):
            delikler.append(Point(x, y).buffer(0.35, 64))
    kesim = []
    if P["tarih_penceresi"]:
        c = (P["tarih_pencere_r"], 0.0)
        pen = box(c[0] - P["tarih_pencere_g"] / 2, -P["tarih_pencere_y"] / 2,
                  c[0] + P["tarih_pencere_g"] / 2, P["tarih_pencere_y"] / 2)
        pen = pen.buffer(-0.35, join_style=1).buffer(0.35, join_style=1)  # freze yarıçapı
        kesim.append(pen)
        cerceve = pen.buffer(0.36, join_style=1).difference(pen.buffer(0.22, join_style=1))
        altin = altin.difference(pen.buffer(0.58)).union(cerceve)
    kesim_hepsi = unary_union(delikler + kesim)

    # bakır serbest bölge: kenar payı, merkez delik ve diğer deliklerin çevresi
    bakir_sinir = Point(0, 0).buffer(R - P["kenar_payi"], 1440).difference(
        Point(0, 0).buffer(P["merkez_delik"] / 2.0 + 0.25, 256))
    for k in kesim + delikler[1:]:
        bakir_sinir = bakir_sinir.difference(k.buffer(0.25))
    altin = altin.intersection(bakir_sinir)
    golge = golge.difference(altin.buffer(0.18)).intersection(bakir_sinir)

    bakir = unary_union([altin.buffer(P["bakir_tasma"], join_style=2), golge]).intersection(bakir_sinir)
    maske_acik = altin

    return {
        "kart": kart,
        "delikler": delikler,
        "kesimler": kesim,
        "kesim_hepsi": kesim_hepsi,
        "altin": altin,
        "golge": golge,
        "bakir": bakir,
        "maske_acik": maske_acik,
        "R": R,
        "yazi_sinirlari": [[round(v, 2) for v in y.bounds] for y in yazilar],
    }


# ----------------------------------------------------------------------------
# Gerber RS-274X yazıcı
# ----------------------------------------------------------------------------

def _poligonlar(g):
    if g.is_empty:
        return []
    if isinstance(g, Polygon):
        return [g]
    if isinstance(g, MultiPolygon):
        return list(g.geoms)
    out = []
    for p in getattr(g, "geoms", []):
        out += _poligonlar(p)
    return out


def _koord(v):
    return int(round(v * 1_000_000))


def gerber_bolgeler(geo, ad, dosya_fonksiyonu):
    s = [
        "G04 ozgur kadran - {}*".format(ad),
        "%FSLAX46Y46*%",
        "%MOMM*%",
        "%TF.FileFunction,{}*%".format(dosya_fonksiyonu),
        "%LPD*%",
        "G01*",
    ]
    # Sıralama dış kabuk alanına göre: bir deliğin içindeki adacık, delik temizlendikten
    # SONRA çizilmeli (ince halka çokgenlerinin deliği koca bir disktir).
    pgs = sorted(_poligonlar(geo), key=lambda p: -Polygon(p.exterior).area)
    for pg in pgs:
        s.append("%LPD*%")
        s += _halka(pg.exterior.coords)
        if pg.interiors:
            s.append("%LPC*%")
            for ic in pg.interiors:
                s += _halka(ic.coords)
    s.append("%LPD*%")
    s.append("M02*")
    return "\n".join(s) + "\n"


def _halka(coords):
    pts = list(coords)
    out = ["G36*"]
    x, y = pts[0]
    out.append("X{}Y{}D02*".format(_koord(x), _koord(y)))
    for x, y in pts[1:]:
        out.append("X{}Y{}D01*".format(_koord(x), _koord(y)))
    out.append("G37*")
    return out


def gerber_cizgi(halkalar, ad, dosya_fonksiyonu, gen=0.10):
    s = [
        "G04 ozgur kadran - {}*".format(ad),
        "%FSLAX46Y46*%",
        "%MOMM*%",
        "%TF.FileFunction,{}*%".format(dosya_fonksiyonu),
        "%ADD10C,{:.3f}*%".format(gen),
        "%LPD*%",
        "G01*",
        "D10*",
    ]
    for coords in halkalar:
        pts = list(coords)
        x, y = pts[0]
        s.append("X{}Y{}D02*".format(_koord(x), _koord(y)))
        for x, y in pts[1:]:
            s.append("X{}Y{}D01*".format(_koord(x), _koord(y)))
    s.append("M02*")
    return "\n".join(s) + "\n"


def excellon(delikler):
    s = ["M48", "METRIC,TZ", "FMAT,2", ";TYPE=NON_PLATED"]
    caplar = sorted({round(d, 3) for d, _ in delikler})
    for i, d in enumerate(caplar, 1):
        s.append("T{}C{:.3f}".format(i, d))
    s.append("%")
    s.append("G90")
    s.append("G05")
    for i, d in enumerate(caplar, 1):
        s.append("T{}".format(i))
        for dd, (x, y) in delikler:
            if round(dd, 3) == d:
                s.append("X{:.3f}Y{:.3f}".format(x, y))
    s.append("T0")
    s.append("M30")
    return "\n".join(s) + "\n"


def gerber_paketi(G, P, hedef_zip):
    R = G["R"]
    # kart merkezi (0,0) -> Gerber'de pozitif koordinata kaydır (bazı üreticiler bunu tercih eder)
    k = R + 1.0

    def tas(g):
        return affinity.translate(g, k, k)

    dosyalar = {}
    dosyalar["OZGUR-F_Cu.gtl"] = gerber_bolgeler(tas(G["bakir"]), "ust bakir", "Copper,L1,Top")
    dosyalar["OZGUR-F_Mask.gts"] = gerber_bolgeler(tas(G["maske_acik"]), "ust maske acikliklari", "Soldermask,Top")
    dosyalar["OZGUR-F_Silkscreen.gto"] = gerber_bolgeler(Polygon(), "ust serigrafi (bos)", "Legend,Top")
    dosyalar["OZGUR-B_Cu.gbl"] = gerber_bolgeler(Polygon(), "alt bakir (bos)", "Copper,L2,Bot")
    dosyalar["OZGUR-B_Mask.gbs"] = gerber_bolgeler(Polygon(), "alt maske (tam kapali)", "Soldermask,Bot")
    # alt serigrafi: imza + JLC sipariş numarasının basılacağı yer (ön yüze basılmasın diye)
    arka = unary_union([
        affinity.translate(yazi("JLCJLCJLCJLC", 1.0, "Inter-Bold.otf", 0.05), 0, 4.0),
        affinity.translate(yazi((P["logo"] or STILLER[P["stil"]]["logo"]).upper(), 1.2, "Inter-Bold.otf", 0.3), 0, -1.0),
        affinity.translate(yazi("No 001  2026", 1.0, "Inter-Bold.otf", 0.12), 0, -3.2),
    ])
    arka = affinity.scale(arka, xfact=-1, origin=(0, 0))  # alttan bakıldığında okunur olsun
    dosyalar["OZGUR-B_Silkscreen.gbo"] = gerber_bolgeler(tas(arka), "alt serigrafi", "Legend,Bot")
    # dış hat + kesimler
    halkalar = [tas(G["kart"]).exterior.coords]
    for kes in G["kesimler"]:
        halkalar.append(tas(kes).exterior.coords)
    dosyalar["OZGUR-Edge_Cuts.gko"] = gerber_cizgi(halkalar, "kart dis hatti", "Profile,NP", 0.10)
    delik = [(round(2 * d.exterior.distance(d.centroid), 3), (d.centroid.x + k, d.centroid.y + k))
             for d in G["delikler"]]
    dosyalar["OZGUR-NPTH.drl"] = excellon(delik)

    with zipfile.ZipFile(hedef_zip, "w", zipfile.ZIP_DEFLATED) as z:
        for ad, icerik in dosyalar.items():
            z.writestr(ad, icerik)
    return dosyalar


# ----------------------------------------------------------------------------
# rasterleştirme ve önizleme
# ----------------------------------------------------------------------------

def _mpl_yol(g):
    verts, codes = [], []
    for pg in _poligonlar(g):
        for halka in [pg.exterior] + list(pg.interiors):
            c = list(halka.coords)
            verts += c
            codes += [MplPath.MOVETO] + [MplPath.LINETO] * (len(c) - 2) + [MplPath.CLOSEPOLY]
    if not verts:
        return None
    return MplPath(verts, codes)


def maske(g, px, kapsam):
    """Geometriyi [0,1] alfa dizisine çevirir (kenar yumuşatmalı)."""
    fig = plt.figure(figsize=(px / 100, px / 100), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(-kapsam, kapsam)
    ax.set_ylim(-kapsam, kapsam)
    ax.axis("off")
    fig.patch.set_facecolor("black")
    ax.set_facecolor("black")
    yol = _mpl_yol(g)
    if yol is not None:
        ax.add_patch(PathPatch(yol, facecolor="white", edgecolor="none", antialiased=True))
    fig.canvas.draw()
    arr = np.asarray(fig.canvas.buffer_rgba())[:, :, 0].astype(np.float32) / 255.0
    plt.close(fig)
    return arr


def onizleme(G, P, renk, px=2048, kapsam=None):
    """Gerçekçi önizleme RGB'si + 3D doku haritaları."""
    R = G["R"]
    kapsam = kapsam or R
    kart = maske(G["kart"].difference(G["kesim_hepsi"]), px, kapsam)
    altin = maske(G["altin"], px, kapsam)
    golge = maske(G["golge"], px, kapsam)
    C = RENKLER[renk]

    yy, xx = np.mgrid[0:px, 0:px].astype(np.float32)
    u = (xx / (px - 1)) * 2 - 1
    v = 1 - (yy / (px - 1)) * 2
    r = np.sqrt(u * u + v * v)
    aci = np.arctan2(v, u)

    maske_renk = np.array(C["maske"])[None, None, :] * np.ones((px, px, 1))
    kab = np.array(C["maske_kabartma"])[None, None, :]
    rgb = maske_renk * (1 - golge[..., None]) + kab * golge[..., None]
    # ENIG: sıcak altın, hafif yön bağımlı parlama
    parlama = 0.85 + 0.15 * np.cos(2 * aci - 0.8)
    altin_rgb = np.array(C["altin"])[None, None, :] * parlama[..., None]
    rgb = rgb * (1 - altin[..., None]) + altin_rgb * altin[..., None]
    # dış gölge (kasa bileziğinin yaptığı karanlık halka)
    vinyet = np.clip((r - 0.86) / 0.14, 0, 1) ** 2
    rgb *= (1 - 0.35 * vinyet)[..., None]
    rgba = np.concatenate([rgb, kart[..., None]], axis=2)

    haritalar = {
        "renk": rgba,
        "metalik": np.clip(altin, 0, 1),
        "puruzluluk": np.clip(0.55 - 0.33 * altin - 0.10 * golge, 0, 1),
        "kabartma": np.clip(0.35 * golge + 0.9 * altin, 0, 1),
        "alfa": kart,
    }
    return haritalar


def png_kaydet(arr, yol):
    from PIL import Image

    a = np.clip(arr, 0, 1)
    if a.ndim == 2:
        img = Image.fromarray((a * 255).astype(np.uint8), "L")
    elif a.shape[2] == 4:
        img = Image.fromarray((a * 255).astype(np.uint8), "RGBA")
    else:
        img = Image.fromarray((a * 255).astype(np.uint8), "RGB")
    img.save(yol, optimize=True)


def svg_kaydet(G, P, renk, yol):
    C = RENKLER[renk]
    R = G["R"]

    def hex_(c):
        return "#{:02x}{:02x}{:02x}".format(*[int(round(v * 255)) for v in c])

    def d(g):
        parca = []
        for pg in _poligonlar(g):
            for halka in [pg.exterior] + list(pg.interiors):
                c = list(halka.coords)
                parca.append("M" + " L".join("{:.3f},{:.3f}".format(x, -y) for x, y in c) + " Z")
        return " ".join(parca)

    kart = G["kart"].difference(G["kesim_hepsi"])
    svg = [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="{0} {0} {1} {1}" width="{2}mm" height="{2}mm">'.format(
            -R - 0.5, 2 * R + 1, 2 * R + 1),
        '<path fill-rule="evenodd" fill="{}" d="{}"/>'.format(hex_(C["maske"]), d(kart)),
        '<path fill-rule="evenodd" fill="{}" d="{}"/>'.format(hex_(C["maske_kabartma"]), d(G["golge"])),
        '<path fill-rule="evenodd" fill="{}" d="{}"/>'.format(hex_(C["altin"]), d(G["altin"])),
        "</svg>",
    ]
    Path(yol).write_text("\n".join(svg))


def dxf_kaydet(G, yol):
    """Lazer atölyeleri için DXF: KESIM (dış hat + delikler) ve ALTIN (lazerle açılacak alanlar).

    Ton-sür-ton GOLGE katmanı bilerek yok: siyah-altın levhada her lazer izi altını açar.
    """
    import ezdxf

    doc = ezdxf.new("R2010", setup=True)
    doc.units = ezdxf.units.MM
    msp = doc.modelspace()
    doc.layers.add("KESIM", color=1)
    doc.layers.add("ALTIN", color=2)

    def halkalar(g, katman):
        for pg in _poligonlar(g):
            for h in [pg.exterior] + list(pg.interiors):
                msp.add_lwpolyline([(round(x, 4), round(y, 4)) for x, y in h.coords[:-1]],
                                   close=True, dxfattribs={"layer": katman})

    msp.add_circle((0, 0), G["R"], dxfattribs={"layer": "KESIM"})
    for d in G["delikler"]:
        c = d.centroid
        msp.add_circle((c.x, c.y), d.exterior.distance(c), dxfattribs={"layer": "KESIM"})
    for k in G["kesimler"]:
        halkalar(k, "KESIM")
    halkalar(G["altin"], "ALTIN")
    doc.saveas(yol)


def main():
    cikti = BURASI / "cikti"
    cikti.mkdir(exist_ok=True)
    P = dict(PARAM)
    for arg in sys.argv[1:]:
        k, v = arg.split("=", 1)
        if isinstance(PARAM[k], bool):
            P[k] = v.lower() in ("1", "true", "evet")
        elif PARAM[k] is None or isinstance(PARAM[k], str):
            P[k] = v
        else:
            P[k] = type(PARAM[k])(v)
    G = geometri(P)
    ek = "_" + P["stil"] + ("_tarihli" if P["tarih_penceresi"] else "") + ("_ayakli" if P["ayak_delikleri"] else "")
    gerber_paketi(G, P, cikti / "ozgur_kadran{}_gerber.zip".format(ek))
    dxf_kaydet(G, cikti / "ozgur_kadran{}_lazer.dxf".format(ek))
    svg_kaydet(G, P, "gece", cikti / "kadran_gece{}.svg".format(ek))
    # 3D önizleme için paketlenmiş maske: R = altın, G = maske altı bakır, B = kart
    from PIL import Image
    kapsam = G["R"]
    kanal = [maske(G["altin"], 2048, kapsam), maske(G["golge"], 2048, kapsam),
             maske(G["kart"].difference(G["kesim_hepsi"]), 2048, kapsam)]
    Image.fromarray((np.stack(kanal, axis=2) * 255).astype(np.uint8), "RGB").save(
        cikti / "doku_maskeler{}.png".format(ek), optimize=True)
    for renk in RENKLER:
        H = onizleme(G, P, renk, px=1600)
        png_kaydet(H["renk"], cikti / "kadran_{}{}.png".format(renk, ek))
    ozet = {
        "stil": P["stil"],
        "cap_mm": P["cap"],
        "yazi_sinirlari": G["yazi_sinirlari"],
        "altin_alan_mm2": round(G["altin"].area, 2),
        "golge_alan_mm2": round(G["golge"].area, 2),
        "tarih_penceresi": P["tarih_penceresi"],
    }
    (cikti / "ozet{}.json".format(ek)).write_text(json.dumps(ozet, ensure_ascii=False, indent=2))
    print(json.dumps(ozet, ensure_ascii=False))


if __name__ == "__main__":
    main()
