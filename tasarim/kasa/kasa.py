#!/usr/bin/env python3
"""ozgur 12 köşeli ("Kümbet") kasa — parametrik CAD (CadQuery).

Kayseri Döner Kümbet'in on iki yüzlü gövdesinden ve konik külahından esinlenen
12 yüzlü orta kasa + yüzeyli bezel, ön yüzden takılan safir cam, 4 vidalı
şeffaf arka kapak ve NH35/NH38 için mekanizma ara halkası.

Çıktılar (cikti/):
  orta_kasa.step / .stl     -> CNC (316L) veya SLM metal baskı teklifi için
  arka_kapak.step / .stl
  mekanizma_halkasi.step / .stl -> reçine/naylon baskı (JLC3DP) — 1-2 $
  montaj.glb                -> 3D önizleme sayfası için

Z ekseni: 0 = kadranın üst yüzü. Bütün ölçüler mm.
NOT: Mekanizma ölçüleri (kurma mili yüksekliği vb.) Seiko NH35A teknik föyüne göre
doğrulanmadan metal sipariş verilmemeli; değerler PARAM'da tek yerde toplanmıştır.
"""

import math
from pathlib import Path

import cadquery as cq

BURASI = Path(__file__).resolve().parent
CIKTI = BURASI / "cikti"

PARAM = {
    # --- mekanizma (Seiko NH35A / NH38A) ---
    "mek_cap": 27.40,          # mekanizma çapı
    "mek_yuk": 5.32,           # mekanizma yüksekliği
    "kadran_cap": 28.50,
    "kadran_kal": 0.40,
    "mil_z": -2.32,            # Seiko föyü: mil ekseni kadran oturma yüzeyinin 1.92 mm altında
    "mil_tup_cap": 2.50,       # kurma tüpü dış çapı (standart 2.5 mm tüp)
    # --- cam ---
    "cam_cap": 30.00,          # düz safir cam çapı
    "cam_kal": 2.00,
    "cam_conta": 0.45,         # I-tipi cam contası et kalınlığı (çap farkı = 2x)
    "ibre_boslugu": 2.36,      # Seiko föyü (M tipi ibre): kadran üstü -> cam altı 2.36 mm
    # --- gövde ---
    "govde_r": 19.50,          # 12 köşeli gövdenin köşe yarıçapı (≈ Ø39)
    "bezel_ust_r": 16.55,      # bezel çatısının iç kenar yarıçapı
    "bezel_yuk": 1.25,         # çatı yüksekliği
    "kasa_alt_z": -6.55,       # orta kasanın alt yüzü
    "rehaut_ic": 27.30,        # kadranın görünen çapı (iç bileziğin alt ağzı)
    # --- kulplar ---
    "kordon_gen": 20.0,
    "kulp_kal": 2.30,
    "kulp_uc_y": 23.30,        # kulp ucu (lug-to-lug ≈ 46.6)
    "pim_delik": 1.05,         # yay pimi deliği (Ø1.0 pim + boşluk)
    "pim_y": 21.35,
    "pim_z": -4.30,
    # --- arka kapak ---
    "kapak_cap": 34.00,
    "kapak_kal": 1.60,
    "kapak_ic_z": -6.12,       # Seiko föyü: kadran üstü -> arka kapak iç yüzü 6.12 mm
    "pencere_cap": 23.0,       # arka safir pencere
    "pencere_kal": 1.00,
    "vida_r": 16.10,           # M1.6 vida çemberi
    "vida_delik": 1.25,        # M1.6 kılavuz deliği (orta kasada)
    "vida_gecis": 1.75,        # kapakta geçiş deliği
    # --- mekanizma halkası ---
    "halka_dis": 29.30,        # Seiko föyü: standart plastik ara halka yuvası Ø29.30 ±0.03
    "halka_ic": 27.45,
}


def poligon12(r, z=0.0, faz=15.0):
    """Köşeleri faz+30k derecede olan 12'gen (yüzler 12/3/6/9 yönlerine bakar)."""
    return [(r * math.cos(math.radians(faz + 30 * k)), r * math.sin(math.radians(faz + 30 * k)))
            for k in range(12)]


def orta_kasa(P):
    z_cam_alt = P["ibre_boslugu"]
    z_cam_ust = z_cam_alt + P["cam_kal"]
    z_govde_ust = z_cam_ust - P["bezel_yuk"] - 0.10   # cam bezelden 0.1 mm taşar
    z_alt = P["kasa_alt_z"]

    # 12 yüzlü gövde
    govde = (cq.Workplane("XY").workplane(offset=z_alt)
             .polyline(poligon12(P["govde_r"])).close()
             .extrude(z_govde_ust - z_alt))
    # konik "kümbet çatısı": iki 12'gen arasında loft -> düzlemsel yüzeyler
    cati = (cq.Workplane("XY").workplane(offset=z_govde_ust)
            .polyline(poligon12(P["govde_r"])).close()
            .workplane(offset=P["bezel_yuk"])
            .polyline(poligon12(P["bezel_ust_r"] / math.cos(math.radians(15)))).close()
            .loft(ruled=True))
    kasa = govde.union(cati)

    # kulplar (yan profil YZ düzleminde çizilip X boyunca uzatılır)
    yi = P["govde_r"] * math.cos(math.radians(15)) - 1.2
    profil = [
        (yi, z_govde_ust - 0.2),
        (P["kulp_uc_y"] - 1.2, z_govde_ust - 2.0),
        (P["kulp_uc_y"], z_govde_ust - 2.6),
        (P["kulp_uc_y"], z_alt + 1.05),
        (P["kulp_uc_y"] - 1.0, z_alt + 0.55),
        (yi, z_alt + 0.35),
    ]
    x0 = P["kordon_gen"] / 2
    k = P["kulp_kal"]
    uc = P["kulp_uc_y"]
    for sx in (1, -1):
        for sy in (1, -1):
            # yan profil (YZ) ile üstten görünüş (XY) kesişimi: uca doğru incelen, ucu yuvarlak kulp
            yan = (cq.Workplane("YZ").workplane(offset=-30)
                   .polyline([(y * sy, z) for y, z in profil]).close().extrude(60))
            plan = [(x0, yi), (x0 + k, yi), (x0 + k - 0.30, uc), (x0, uc)]
            ust = (cq.Workplane("XY").workplane(offset=z_alt - 1)
                   .polyline([(x * sx, y * sy) for x, y in plan]).close().extrude(20))
            try:
                ust = ust.edges("|Z").edges(">Y" if sy > 0 else "<Y").fillet(0.75)
            except Exception:
                pass
            kulp = yan.intersect(ust)
            try:
                kulp = kulp.edges("not |Z").fillet(0.22)
            except Exception:
                pass
            kasa = kasa.union(kulp)

    # iç boşluklar: döndürülmüş kesit (r, z)
    cam_yuva_r = (P["cam_cap"] + 2 * P["cam_conta"]) / 2
    ic = [
        (0, z_cam_ust + 1.0),
        (cam_yuva_r, z_cam_ust + 1.0),
        (cam_yuva_r, z_cam_alt - 0.05),             # cam + conta yuvası
        (P["cam_cap"] / 2 - 0.55, z_cam_alt - 0.05),  # cam oturma basamağı
        (P["rehaut_ic"] / 2, 0.05),                 # eğimli iç bilezik (rehaut)
        (P["rehaut_ic"] / 2, 0.0),
        ((P["kadran_cap"] + 0.20) / 2, 0.0),        # kadran yuvası
        ((P["kadran_cap"] + 0.20) / 2, -P["kadran_kal"] - 0.05),
        (P["halka_dis"] / 2 + 0.05, -P["kadran_kal"] - 0.05),  # mekanizma halkası odası
        (P["halka_dis"] / 2 + 0.05, P["kapak_ic_z"]),
        (P["kapak_cap"] / 2 + 0.05, P["kapak_ic_z"]),  # arka kapak yuvası
        (P["kapak_cap"] / 2 + 0.05, z_alt - 1.0),
        (0, z_alt - 1.0),
    ]
    bosluk = cq.Workplane("XZ").polyline(ic).close().revolve(360, (0, 0, 0), (0, 1, 0))
    kasa = kasa.cut(bosluk)

    # kurma tüpü deliği (saat 3 = +X)
    tup = (cq.Workplane("YZ").workplane(offset=P["halka_dis"] / 2 - 1.0)
           .center(0, P["mil_z"]).circle(P["mil_tup_cap"] / 2 + 0.01).extrude(10))
    kasa = kasa.cut(tup)
    # kurma kolu oyuğu (iç tarafta, tüpe giden kanal)
    kasa = kasa.cut(cq.Workplane("XY").box(6, 3.4, 3.0).translate((P["halka_dis"] / 2 + 1.2, 0, P["mil_z"])))

    # yay pimi delikleri (boydan boya)
    for sy in (1, -1):
        pim = (cq.Workplane("YZ").workplane(offset=-15).center(P["pim_y"] * sy, P["pim_z"])
               .circle(P["pim_delik"] / 2).extrude(30))
        kasa = kasa.cut(pim)

    # arka kapak vida delikleri (M1.6, 3.2 mm derin)
    for k in range(4):
        a = math.radians(45 + 90 * k)
        x, y = P["vida_r"] * math.cos(a), P["vida_r"] * math.sin(a)
        z0 = P["kapak_ic_z"]
        kasa = kasa.cut(cq.Workplane("XY").workplane(offset=z0 - 0.01).center(x, y)
                        .circle(P["vida_delik"] / 2).extrude(3.2))

    # ince pahlar: gövde alt kenarı
    try:
        kasa = kasa.faces("<Z").edges().chamfer(0.25)
    except Exception:
        pass
    return kasa


def arka_kapak(P):
    z_alt = P["kasa_alt_z"]
    z_ust = P["kapak_ic_z"]
    z_dis = z_ust - P["kapak_kal"]
    kapak = (cq.Workplane("XY").workplane(offset=z_dis)
             .circle(P["kapak_cap"] / 2).extrude(P["kapak_kal"]))
    # dış yüzde hafif kubbe hissi için pah
    kapak = kapak.faces("<Z").edges().chamfer(0.6)
    # safir pencere yuvası (dıştan) + görüş deliği
    kapak = kapak.cut(cq.Workplane("XY").workplane(offset=z_dis - 0.01)
                      .circle(P["pencere_cap"] / 2 + 0.05).extrude(P["pencere_kal"] + 0.01))
    kapak = kapak.cut(cq.Workplane("XY").workplane(offset=z_dis)
                      .circle(P["pencere_cap"] / 2 - 0.8).extrude(5))
    # vidalar için havşalı geçiş delikleri
    for k in range(4):
        a = math.radians(45 + 90 * k)
        x, y = P["vida_r"] * math.cos(a), P["vida_r"] * math.sin(a)
        kapak = kapak.cut(cq.Workplane("XY").workplane(offset=z_dis - 0.01).center(x, y)
                          .circle(P["vida_gecis"] / 2).extrude(5))
        kapak = kapak.cut(cq.Workplane("XY").workplane(offset=z_dis - 0.01).center(x, y)
                          .circle(1.55).extrude(0.6))
    # iç yüzde 12 köşeli yıldız gravürü için sığ halka (dekor)
    return kapak


def mekanizma_halkasi(P):
    z_ust = -P["kadran_kal"] - 0.05
    z_alt = P["kapak_ic_z"]
    h = z_ust - z_alt
    halka = (cq.Workplane("XY").workplane(offset=z_alt)
             .circle(P["halka_dis"] / 2).circle(P["halka_ic"] / 2).extrude(h))
    # kurma mili için kanal
    halka = halka.cut(cq.Workplane("XY").box(8, 3.0, h + 1).translate((P["halka_dis"] / 2, 0, z_alt + h / 2)))
    # arkadan görünen yüzde 11 küçük süs deliği (kurma kolu tarafı boş)
    for k in range(12):
        if k == 0:
            continue
        a = math.radians(30 * k)
        r = (P["halka_dis"] + P["halka_ic"]) / 4
        halka = halka.cut(cq.Workplane("XY").workplane(offset=z_alt - 0.01)
                          .center(r * math.cos(a), r * math.sin(a)).circle(0.45).extrude(0.6))
    return halka


def main():
    CIKTI.mkdir(exist_ok=True)
    P = PARAM
    parcalar = {
        "orta_kasa": orta_kasa(P),
        "arka_kapak": arka_kapak(P),
        "mekanizma_halkasi": mekanizma_halkasi(P),
    }
    for ad, p in parcalar.items():
        cq.exporters.export(p, str(CIKTI / f"{ad}.step"))
        cq.exporters.export(p, str(CIKTI / f"{ad}.stl"), tolerance=0.01, angularTolerance=0.1)
        bb = p.val().BoundingBox()
        print(f"{ad:20s} {bb.xlen:6.2f} x {bb.ylen:6.2f} x {bb.zlen:6.2f} mm  "
              f"hacim {p.val().Volume() / 1000:.2f} cm3")
    glb_paketle(list(parcalar), CIKTI / "montaj.glb")


def glb_paketle(adlar, hedef):
    """STL'leri parça başına tek ağ olacak şekilde yumuşak gölgeli GLB'ye çevirir (önizleme için)."""
    import trimesh
    from trimesh.graph import smooth_shade

    sahne = trimesh.Scene()
    for ad in adlar:
        m = trimesh.load(str(CIKTI / f"{ad}.stl"))
        m.merge_vertices()
        m = smooth_shade(m, angle=math.radians(28))
        sahne.add_geometry(m, node_name=ad, geom_name=ad)
    sahne.export(str(hedef), include_normals=True)


if __name__ == "__main__":
    main()
