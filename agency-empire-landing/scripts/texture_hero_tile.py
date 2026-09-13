#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
texture_hero_tile.py — lo sfondo dell'hero dall'immagine VERA di Max (ordine del 13/09 sera).

Legge public/texture/hero-onde-ORIGINALE.jpg (899x1748, intatta, mai rigenerata) e produce
hero-onde.jpg + hero-onde.webp (3840x2000 = 2x di un hero 1920x1000):
  - la tessera occupa TUTTA l'altezza (si vede intera) e NON viene ingrandita: sul desktop 1x e'
    rimpicciolita a ~0,57, quindi piu' nitida dell'originale, mai piu' sfocata;
  - ripetuta in orizzontale finche' copre tutto (4-5 doppioni), alternate specchiate cosi' le onde
    si toccano sullo stesso bordo;
  - i giunti sono cuciti con una sfumatura a nero (bordi della tessera + velo scuro centrato sul
    giunto), cosi' i tagli fra i doppioni non si leggono.
Uso: py -3 scripts/texture_hero_tile.py   (dalla cartella agency-empire-landing)
"""
import os
from PIL import Image, ImageDraw

QUI = os.path.dirname(os.path.abspath(__file__))
TEX = os.path.join(QUI, "..", "public", "texture")
W, H = 3840, 2000
FEATHER, OVERLAP, GIUNTO = 150, 90, 120


def main():
    src = Image.open(os.path.join(TEX, "hero-onde-ORIGINALE.jpg")).convert("RGB")
    sw, sh = src.size
    scale = H / sh
    tw, th = round(sw * scale), H
    tile = src.resize((tw, th), Image.LANCZOS)

    mask = Image.new("L", (tw, th), 255)
    px = mask.load()
    for x in range(FEATHER):
        a = int(255 * (x / FEATHER) ** 1.6)
        for y in range(th):
            px[x, y] = a
            px[tw - 1 - x, y] = a

    canvas = Image.new("RGB", (W, H), (0, 0, 0))
    step = tw - OVERLAP
    n = (W - OVERLAP) // step + 2
    for i in range(n):
        x = i * step
        if x >= W:
            break
        t = tile.transpose(Image.FLIP_LEFT_RIGHT) if i % 2 else tile
        canvas.paste(t, (x, 0), mask)

    velo = Image.new("L", (W, H), 0)
    d = ImageDraw.Draw(velo)
    for i in range(1, n):
        cx = i * step + (tw - step) // 2
        for k in range(GIUNTO):
            a = int(110 * (1 - k / GIUNTO) ** 2)
            d.line([(cx - k, 0), (cx - k, H)], fill=a)
            d.line([(cx + k, 0), (cx + k, H)], fill=a)
    canvas = Image.composite(Image.new("RGB", (W, H), (0, 0, 0)), canvas, velo)

    canvas.save(os.path.join(TEX, "hero-onde.jpg"), quality=90, subsampling=0, optimize=True)
    canvas.save(os.path.join(TEX, "hero-onde.webp"), quality=86, method=6)
    print("tessera %dx%d, %d doppioni, tela %dx%d" % (tw, th, min(n, W // step + 1), W, H))


if __name__ == "__main__":
    main()
