# -*- coding: utf-8 -*-
"""
colori_frame.py -- EMP-DIOEDIT, Fase 2.

Misura i colori dominanti di uno o piu' frame PNG, cosi' che nella visione i colori
siano NUMERI (hex) e non impressioni ("un arancione caldo"). La macchina misura,
l'occhio giudica.

Uso:
  python colori_frame.py <frame.png> [<frame2.png> ...]
  python colori_frame.py --cartella <dir> [--n 5]

Stampa per ogni frame: i primi N colori dominanti in hex con la percentuale di
area, piu' luminosita' media (0-255) e se il frame e' "scuro" (< 60) o "chiaro".
Nessuna emoji: console cp1252.
"""
import argparse
import os
import sys

from PIL import Image


def dominanti(path, n=5):
    im = Image.open(path).convert("RGB")
    im.thumbnail((240, 240))
    # quantizza a 16 colori per avere cluster stabili, poi conta
    q = im.quantize(colors=16, method=Image.Quantize.MEDIANCUT)
    pal = q.getpalette()[: 16 * 3]
    conteggio = q.getcolors()
    tot = sum(c for c, _ in conteggio)
    conteggio.sort(reverse=True)
    out = []
    for c, idx in conteggio[:n]:
        r, g, b = pal[idx * 3 : idx * 3 + 3]
        out.append(("#%02x%02x%02x" % (r, g, b), round(100.0 * c / tot, 1)))
    gray = im.convert("L")
    lum = sum(gray.getdata()) / (gray.width * gray.height)
    return out, round(lum, 1)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Colori dominanti dei frame (hex, misurati).")
    ap.add_argument("frames", nargs="*")
    ap.add_argument("--cartella")
    ap.add_argument("--n", type=int, default=5)
    a = ap.parse_args(argv)
    files = list(a.frames)
    if a.cartella:
        files += sorted(
            os.path.join(a.cartella, f) for f in os.listdir(a.cartella) if f.lower().endswith(".png")
        )
    if not files:
        print("nessun frame indicato")
        return 1
    for f in files:
        try:
            cols, lum = dominanti(f, a.n)
        except Exception as e:  # noqa: BLE001
            print(f"{os.path.basename(f)}  ERRORE {e}")
            continue
        tono = "scuro" if lum < 60 else ("medio" if lum < 150 else "chiaro")
        testo = "  ".join(f"{h} {p}%" for h, p in cols)
        print(f"{os.path.basename(f)}  lum={lum} ({tono})  {testo}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
