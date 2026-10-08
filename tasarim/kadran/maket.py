#!/usr/bin/env python3
"""Kadran önizlemesinin üstüne ibre, bezel ve kurma kolu çizerek düz bir saat maketi üretir.

Kullanım:  python3 maket.py <kadran.webp> <cap_mm> <cikti.png> [stil] [ibre_rengi]
stil "coklu" ise alt kadran ibreleri de çizilir (konumlar kadran.py içindeki COKLU'dan).
"""

import math
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from kadran import COKLU  # noqa: E402

IBRE = {"mavi": (20, 32, 79, 255), "altin": (214, 176, 98, 255), "siyah": (18, 19, 22, 255)}


def maket(kadran_yol, cap, cikti, stil="roma", ibre="mavi", saat=(10, 9, 36)):
    olc = 40.0                                   # piksel / mm
    R = cap / 2
    kasa_r = R + 3.4
    W = int((kasa_r + 4) * 2 * olc)
    c = W / 2
    img = Image.new("RGBA", (W, W), (226, 228, 228, 255))
    d = ImageDraw.Draw(img)

    # kurma kolu (saat 3)
    d.rounded_rectangle([c + kasa_r * olc - 6, c - 2.8 * olc, c + (kasa_r + 2.6) * olc, c + 2.8 * olc], 8, fill=(170, 173, 178, 255))
    for i in range(14):
        y = c - 2.6 * olc + i * 0.4 * olc
        d.line([c + kasa_r * olc + 4, y, c + (kasa_r + 2.5) * olc, y], fill=(130, 133, 138, 255), width=2)
    # cilalı kasa: ışınsal gri gradyan
    yy, xx = np.mgrid[0:W, 0:W].astype(np.float32)
    aci = np.arctan2(yy - c, xx - c)
    r = np.hypot(xx - c, yy - c) / olc
    ton = 175 + 60 * np.cos(2 * aci + 0.7) * np.clip((r - R) / (kasa_r - R), 0, 1)
    halka = (r <= kasa_r) & (r > R - 0.2)
    arr = np.array(img)
    for k in range(3):
        arr[..., k] = np.where(halka, np.clip(ton + (4 if k == 2 else 0), 0, 255), arr[..., k])
    img = Image.fromarray(arr)
    d = ImageDraw.Draw(img)

    # kadran
    kd = Image.open(kadran_yol).convert("RGBA").resize((int(2 * R * olc), int(2 * R * olc)), Image.LANCZOS)
    img.alpha_composite(kd, (int(c - R * olc), int(c - R * olc)))
    d = ImageDraw.Draw(img)

    def nokta(x, y):
        return (c + x * olc, c - y * olc)

    def yaprak(L, w, a, merkez=(0, 0), kuyruk=1.5, renk=IBRE[ibre]):
        pts = []
        for t in np.linspace(0, 1, 30):
            pts.append((w / 2 * math.sin(math.pi * t) ** 0.8, -kuyruk * 0.15 + (L + kuyruk * 0.15) * t))
        sag = [(x, y) for x, y in pts]
        sol = [(-x, y) for x, y in reversed(pts)]
        poly = sag + sol
        ca, sa = math.cos(math.radians(-a)), math.sin(math.radians(-a))
        d.polygon([nokta(merkez[0] + x * ca - y * sa, merkez[1] + x * sa + y * ca) for x, y in poly], fill=renk)
        bx, by = kuyruk * math.sin(math.radians(a + 180)), kuyruk * math.cos(math.radians(a + 180))
        d.line([nokta(*merkez), nokta(merkez[0] + bx, merkez[1] + by)], fill=renk, width=int(0.25 * olc))

    def cubuk(L, a, merkez=(0, 0), w=0.16, renk=IBRE[ibre]):
        x, y = L * math.sin(math.radians(a)), L * math.cos(math.radians(a))
        d.line([nokta(*merkez), nokta(merkez[0] + x, merkez[1] + y)], fill=renk, width=max(2, int(w * olc)))
        rr = 0.35 * olc
        cx, cy = nokta(*merkez)
        d.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], fill=renk)

    sa, dk, sn = saat
    if stil == "coklu":
        rs = COKLU["alt_r"] * R
        for m, deg in ((COKLU["sol_merkez"], 360 / 7 * 3), (COKLU["sag_merkez"], 30 * 9)):
            cubuk(rs * 0.82, deg, (m[0] * R, m[1] * R), w=0.14)
    yaprak(0.56 * R, 0.085 * R, (sa % 12 + dk / 60) * 30)
    yaprak(0.86 * R, 0.065 * R, dk * 6)
    cubuk(0.90 * R, sn * 6, w=0.10)
    rr = 0.07 * R * olc
    d.ellipse([c - rr, c - rr, c + rr, c + rr], fill=IBRE[ibre])
    img = img.filter(ImageFilter.SMOOTH)
    img.convert("RGB").save(cikti, quality=92)


if __name__ == "__main__":
    a = sys.argv[1:]
    maket(a[0], float(a[1]), a[2], a[3] if len(a) > 3 else "roma", a[4] if len(a) > 4 else "mavi")
