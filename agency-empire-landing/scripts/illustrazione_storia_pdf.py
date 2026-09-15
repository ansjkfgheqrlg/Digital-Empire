#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
illustrazione_storia_pdf.py — still per «La storia dei preventivi» (F6, scagnozzo gamma).

Stesso stile delle 5 illustrazioni dell'hero (scripts/illustrazioni_card.py, scagnozzo beta):
monocromo bianco-su-nero, granuloso come una stampa a inchiostro/fotocopia (rumore gaussiano +
mezzo dither Floyd-Steinberg + vignettatura + graffi), un solo dettaglio arancione (#fb4604)
aggiunto DOPO la grana. Non importa il file del beta (evita collisioni fra scagnozzi che lavorano
in parallelo sullo stesso file): la logica di grana è duplicata qui, volutamente identica.

Soggetto: un monitor/schermo con un foglio PDF che ne esce (ruotato, "sollevato" dal bordo alto,
angolo piegato), un logo-placeholder in alto a sinistra del foglio, righe che imitano le voci di
un preventivo, e il totale finale evidenziato in arancione (il dettaglio di colore).

Formato 900x700 (resa finale). Sfondo nero puro #050505.
Salva in public/card/storia-pdf.png, target <=150KB.

Uso: py -3 scripts/illustrazione_storia_pdf.py
"""
import os
import random

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageOps

QUI = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(QUI, "..", "public", "card")
W, H = 1800, 1400          # tela di disegno (2x della resa finale, per una grana fine)
RESA_W, RESA_H = 900, 700  # resa finale richiesta dal brief F6 (blocco F1)
BG = 5
FG = 235
ARANCIO = (251, 70, 4)

FOGLIO_BOX = (480, 130, 1330, 1080)   # (x0, y0, x1, y1) prima della rotazione
FOGLIO_CENTRO = (905, 605)
FOGLIO_ANGOLO = -4                    # gradi


def disegna_monitor(base: Image.Image):
    """Monitor dietro (solo contorno + righe dati), disegnato direttamente sulla tela base."""
    d = ImageDraw.Draw(base)
    mon_l, mon_t, mon_r, mon_b = 260, 420, 1540, 1180
    d.rounded_rectangle([mon_l, mon_t, mon_r, mon_b], radius=22, outline=FG, width=12)
    d.rectangle([mon_l + 40, mon_t + 40, mon_r - 40, mon_b - 180], outline=FG, width=6)
    d.rectangle([820, mon_b, 980, mon_b + 90], fill=FG)          # collo piedistallo
    d.rectangle([700, mon_b + 90, 1100, mon_b + 118], fill=FG)   # base
    for i, y in enumerate(range(mon_t + 90, mon_b - 220, 34)):
        larg = 260 if i % 3 else 420
        d.rectangle([mon_l + 70, y, mon_l + 70 + larg, y + 14], fill=FG)


def _layer_foglio(totale_arancio: bool) -> Image.Image:
    """Un layer L 0/255 col foglio del preventivo, ruotato — usato sia per il foglio bianco (FG)
    sia (in una seconda chiamata, con totale_arancio=True e solo il rigo del totale disegnato) per
    isolare il dettaglio arancione con la stessa rotazione."""
    layer = Image.new("L", (W, H), 0)
    d = ImageDraw.Draw(layer)
    fx0, fy0, fx1, fy1 = FOGLIO_BOX

    if not totale_arancio:
        d.rounded_rectangle([fx0, fy0, fx1, fy1], radius=10, fill=FG)
        # angolo piegato in alto a destra ("buca" la pagina + piega visibile)
        d.polygon([(fx1 - 120, fy0), (fx1, fy0), (fx1, fy0 + 120)], fill=0)
        d.line([(fx1 - 120, fy0), (fx1 - 60, fy0 + 60), (fx1, fy0 + 120)], fill=FG, width=6)
        # logo-placeholder in alto a sinistra
        lx, ly = fx0 + 60, fy0 + 70
        d.rectangle([lx, ly, lx + 90, ly + 90], outline=0, width=10)
        d.rectangle([lx + 130, ly + 10, lx + 420, ly + 34], fill=0)
        d.rectangle([lx + 130, ly + 50, lx + 300, ly + 68], fill=0)
        # separatore sotto l'intestazione
        d.line([(fx0 + 60, fy0 + 200), (fx1 - 60, fy0 + 200)], fill=0, width=6)
        # righe del preventivo (etichetta + valore)
        ty = fy0 + 260
        for i in range(6):
            w_lab = 260 if i % 2 == 0 else 200
            d.rectangle([fx0 + 60, ty, fx0 + 60 + w_lab, ty + 22], fill=0)
            d.rectangle([fx1 - 220, ty, fx1 - 60, ty + 22], fill=0)
            ty += 70
        ty += 10
        d.line([(fx0 + 60, ty), (fx1 - 60, ty)], fill=0, width=6)
    else:
        ty = fy0 + 260 + 70 * 6 + 40
        d.rectangle([fx0 + 60, ty, fx0 + 320, ty + 30], fill=FG)
        d.rectangle([fx1 - 240, ty, fx1 - 60, ty + 30], fill=FG)

    return layer.rotate(FOGLIO_ANGOLO, resample=Image.BICUBIC, center=FOGLIO_CENTRO, fillcolor=0)


def applica_grana(img_l: Image.Image, seed: int) -> Image.Image:
    rnd = random.Random(seed)
    forma = img_l.point(lambda p: 255 if p > 40 else 0)
    alone = forma.filter(ImageFilter.MaxFilter(31)).filter(ImageFilter.GaussianBlur(18))
    alone_arr = np.array(alone, dtype=np.float32) / 255.0

    soft = np.array(img_l.filter(ImageFilter.GaussianBlur(1.3)), dtype=np.float32)

    rng = np.random.default_rng(seed)
    sigma = 7 + alone_arr * 26
    noise = rng.normal(0, 1, soft.shape) * sigma
    noisy = np.clip(soft + noise, 0, 255).astype(np.uint8)
    noisy_img = Image.fromarray(noisy, mode="L")

    dithered = noisy_img.convert("1", dither=Image.FLOYDSTEINBERG).convert("L")
    dith_arr = np.array(dithered, dtype=np.float32)
    peso_dither = 0.22 + alone_arr * 0.18
    mixed = noisy.astype(np.float32) * (1 - peso_dither) + dith_arr * peso_dither

    fondo_lontano = 1 - alone_arr
    mixed = mixed - fondo_lontano * 9
    out = Image.fromarray(np.clip(mixed, 0, 255).astype(np.uint8), mode="L")
    out = ImageOps.autocontrast(out, cutoff=1)

    vx, vy = np.meshgrid(np.linspace(-1, 1, W), np.linspace(-1, 1, H))
    dist = np.sqrt(vx ** 2 + vy ** 2)
    vig = np.clip(1 - 0.45 * (dist ** 2), 0.35, 1.0)
    out_arr = np.array(out, dtype=np.float32) * vig
    out = Image.fromarray(np.clip(out_arr, 0, 255).astype(np.uint8), mode="L")

    d = ImageDraw.Draw(out)
    for _ in range(rnd.randint(3, 6)):
        x = rnd.randint(20, W - 20)
        y0 = rnd.randint(0, H // 3)
        y1 = y0 + rnd.randint(H // 3, H)
        jitter = rnd.randint(-8, 8)
        tono = rnd.choice([BG, FG])
        d.line([(x, y0), (x + jitter, min(y1, H))], fill=tono, width=1)

    return out


def _palette_fissa(n_grigi: int = 40) -> Image.Image:
    n_grigi = max(2, min(n_grigi, 255))
    entries = []
    for i in range(n_grigi):
        v = round(i * 255 / (n_grigi - 1))
        entries.extend([v, v, v])
    entries.extend(list(ARANCIO))
    while len(entries) < 256 * 3:
        entries.extend(list(ARANCIO))
    pal_img = Image.new("P", (16, 16))
    pal_img.putpalette(entries[:768])
    return pal_img


def main():
    os.makedirs(OUT, exist_ok=True)

    base = Image.new("L", (W, H), BG)
    disegna_monitor(base)
    foglio = _layer_foglio(totale_arancio=False)
    base = Image.fromarray(np.maximum(np.array(base), np.array(foglio)), mode="L")

    grezza = applica_grana(base, seed=hash("storia-pdf") % 10000)
    rgb = Image.merge("RGB", (grezza, grezza, grezza))

    # dettaglio arancione: solo il rigo del totale, stessa rotazione del foglio
    totale = _layer_foglio(totale_arancio=True)
    mask = totale.point(lambda p: 255 if p > 10 else 0).filter(ImageFilter.GaussianBlur(0.6))
    arancio_layer = Image.new("RGB", (W, H), ARANCIO)
    rgb = Image.composite(arancio_layer, rgb, mask)

    rgb = rgb.resize((RESA_W, RESA_H), Image.LANCZOS)

    path = os.path.join(OUT, "storia-pdf.png")
    pal_img = _palette_fissa(22)
    quant = rgb.quantize(palette=pal_img, dither=Image.NONE)
    quant.save(path, optimize=True, compress_level=9)
    kb = os.path.getsize(path) / 1024
    print(f"storia-pdf.png: {kb:.1f} KB ({RESA_W}x{RESA_H})")


if __name__ == "__main__":
    main()
