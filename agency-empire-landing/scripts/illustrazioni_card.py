#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
illustrazioni_card.py — le 5 illustrazioni delle card fluttuanti dell'hero (F5, scagnozzo beta).

Stile: monocromo bianco-su-nero, granuloso come una stampa a inchiostro/fotocopia (risograph),
come l'allegato 02 del brief. Soggetti disegnati a forme geometriche grandi (linee 3-6px equiv.,
riempimenti), poi "sporcati": blur leggero, rumore gaussiano forte, mezzo passaggio a dither
1-bit (Floyd-Steinberg) mescolato col tono continuo, vignettatura, qualche graffio. Un solo
dettaglio arancione (#fb4604) per immagine, aggiunto DOPO la grana cosi' resta leggibile.

Formato 800x640 (2x della resa ~200x160 nella card). Sfondo nero puro #050505.
Salva in public/card/c1.png .. c5.png, palette 64 colori + optimize, target <=120KB.

Uso: py -3 scripts/illustrazioni_card.py
"""
import os
import random

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageOps

QUI = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(QUI, "..", "public", "card")
W, H = 800, 640          # tela di disegno (definizione alta per un vettoriale pulito)
RESA_W, RESA_H = 400, 320  # 2x della resa reale in card (~200x160): riduzione finale prima del salvataggio
BG = 5          # nero puro di fondo
FG = 235        # bianco/argento delle forme
ARANCIO = (251, 70, 4)  # #fb4604
ACCENTO = "__ARANCIO__"  # sentinella: le funzioni soggetto la usano per marcare il tocco di colore


def nuova_tela():
    return Image.new("L", (W, H), BG)


class _DrawProxy:
    """Fa passare ad ImageDraw.Draw le chiamate delle funzioni soggetto, traducendo la sentinella
    ACCENTO in base alla modalita': 'base' -> diventa FG (cosi' il tocco arancione e' comunque
    presente come forma piena e riceve la grana come tutto il resto); 'marker' -> diventa ARANCIO
    e tutte le altre chiamate (quelle con FG) vengono ignorate, per isolare solo l'accento."""

    def __init__(self, real, modo, colore_accento):
        self.real = real
        self.modo = modo
        self.colore_accento = colore_accento

    def __getattr__(self, name):
        real_fn = getattr(self.real, name)

        def wrapped(*args, **kwargs):
            fill = kwargs.get("fill")
            outline = kwargs.get("outline")
            e_accento = fill == ACCENTO or outline == ACCENTO
            if self.modo == "marker" and not e_accento:
                return None
            if e_accento:
                if fill == ACCENTO:
                    kwargs["fill"] = self.colore_accento
                if outline == ACCENTO:
                    kwargs["outline"] = self.colore_accento
            return real_fn(*args, **kwargs)
        return wrapped


# ---------------------------------------------------------------- soggetti --

def disegna_terminale(d):
    """1 — terminale/monitor retro, cursore e riga '> 300 msg . ok'."""
    # corpo monitor
    d.rounded_rectangle([120, 90, 680, 430], radius=14, outline=FG, width=10)
    # piedistallo
    d.rectangle([370, 430, 430, 480], fill=FG)
    d.rectangle([300, 480, 500, 500], fill=FG)
    # schermo interno
    d.rectangle([160, 130, 640, 390], outline=FG, width=6)
    # riga di testo "> 300 msg . ok" disegnata a blocchi (font non affidabile in Pillow default,
    # quindi la componiamo come glifi geometrici semplici, leggibile come segnaposto terminale)
    bx, by = 195, 240
    d.line([bx, by, bx + 26, by + 20], fill=FG, width=8)      # >
    d.line([bx, by + 40, bx + 26, by + 20], fill=FG, width=8)
    for i in range(9):
        cx = bx + 55 + i * 34
        h = 26 if i % 3 else 40
        d.rectangle([cx, by + 20 - h // 2, cx + 18, by + 20 + h // 2], fill=FG)
    # cursore lampeggiante — il tocco arancione
    d.rectangle([bx + 55 + 9 * 34 + 30, by - 4, bx + 55 + 9 * 34 + 30 + 20, by + 44], fill="__ARANCIO__")
    # piedini di scansione (righe orizzontali sottili sullo schermo, effetto CRT)
    for y in range(140, 385, 14):
        d.line([165, y, 635, y], fill=FG, width=1)


def disegna_calendario(d):
    """2 — calendario a strappo con '7'."""
    d.rounded_rectangle([150, 130, 650, 520], radius=16, outline=FG, width=10)
    d.line([150, 230, 650, 230], fill=FG, width=8)
    # anelli in alto
    d.rounded_rectangle([230, 90, 270, 170], radius=14, outline=FG, width=8)
    d.rounded_rectangle([530, 90, 570, 170], radius=14, outline=FG, width=8)
    # numero "7" grande, disegnato come forma (non testo di sistema)
    seven = [(340, 280), (500, 280), (500, 310), (420, 500), (370, 500), (445, 320), (340, 320)]
    d.polygon(seven, fill=FG)
    # linea strappata in basso (dentellatura)
    y0 = 500
    pts = [(150, y0)]
    for x in range(150, 651, 22):
        pts.append((x, y0 + (14 if (x // 22) % 2 == 0 else -6)))
    pts.append((650, y0))
    d.line(pts, fill=BG, width=4)
    # graffetta arancione angolo — tocco colore
    d.ellipse([580, 150, 616, 186], outline="__ARANCIO__", width=6)


def disegna_lucchetto(d):
    """3 — lucchetto aperto con chiave."""
    # arco (shackle) aperto — ruotato verso l'alto a sinistra
    d.arc([210, 90, 430, 300], start=160, end=360, fill=FG, width=18)
    # corpo lucchetto
    d.rounded_rectangle([260, 260, 560, 470], radius=20, outline=FG, width=10)
    # buco chiave
    d.ellipse([385, 320, 435, 370], outline=FG, width=8)
    d.polygon([(400, 365), (420, 365), (415, 410), (405, 410)], fill=FG)
    # chiave separata a destra — il dente arancione
    d.line([490, 500, 640, 500], fill=FG, width=12)
    d.ellipse([610, 470, 670, 530], outline=FG, width=10)
    d.rectangle([480, 490, 505, 512], fill="__ARANCIO__")
    d.rectangle([505, 500, 525, 520], fill=FG)


def disegna_server(d):
    """4 — rack server con led, un solo led arancione."""
    top = 110
    for i in range(4):
        y0 = top + i * 100
        d.rounded_rectangle([140, y0, 660, y0 + 80], radius=10, outline=FG, width=8)
        # prese di sfiato
        for gx in range(430, 620, 26):
            d.line([gx, y0 + 20, gx, y0 + 60], fill=FG, width=4)
        # vite ai lati
        d.ellipse([180, y0 + 32, 200, y0 + 52], outline=FG, width=4)
    # led: solo il primo arancione, gli altri chiari/spenti
    for i in range(4):
        y0 = top + i * 100
        cx, cy = 250, y0 + 40
        if i == 0:
            d.ellipse([cx - 14, cy - 14, cx + 14, cy + 14], fill="__ARANCIO__")
        else:
            d.ellipse([cx - 10, cy - 10, cx + 10, cy + 10], outline=FG, width=4)


def disegna_busta(d):
    """5 — busta/lettera con un timbro."""
    d.rounded_rectangle([110, 160, 690, 460], radius=14, outline=FG, width=10)
    d.line([115, 168, 400, 340], fill=FG, width=8)
    d.line([685, 168, 400, 340], fill=FG, width=8)
    # timbro in alto a destra — cerchio con dentellatura semplice + croce arancione
    scx, scy, sr = 600, 240, 60
    d.ellipse([scx - sr, scy - sr, scx + sr, scy + sr], outline=FG, width=6)
    d.ellipse([scx - sr + 16, scy - sr + 16, scx + sr - 16, scy + sr - 16], outline=FG, width=3)
    d.line([scx - 22, scy, scx + 22, scy], fill="__ARANCIO__", width=10)
    d.line([scx, scy - 22, scx, scy + 22], fill="__ARANCIO__", width=10)
    # francobollo dentellato in basso a sinistra
    d.rectangle([150, 360, 260, 430], outline=FG, width=6)


SOGGETTI = [disegna_terminale, disegna_calendario, disegna_lucchetto, disegna_server, disegna_busta]


# ------------------------------------------------------------------- grana --

def applica_grana(img_l: Image.Image, seed: int) -> Image.Image:
    """Grana concentrata vicino alle forme (come una stampa vera: il fondo nero resta quasi
    pulito, la texture si addensa sui soggetti), non "statico TV" uniforme su tutta la tela."""
    rnd = random.Random(seed)

    # maschera di prossimita': dilata il disegno pulito, cosi' la grana forte segue i soggetti
    forma = img_l.point(lambda p: 255 if p > 40 else 0)
    alone = forma.filter(ImageFilter.MaxFilter(31)).filter(ImageFilter.GaussianBlur(18))
    alone_arr = np.array(alone, dtype=np.float32) / 255.0  # 0 = fondo lontano, 1 = sopra/vicino alla forma

    # 1) blur leggero per ammorbidire i bordi netti del vettoriale
    soft = np.array(img_l.filter(ImageFilter.GaussianBlur(1.3)), dtype=np.float32)

    # 2) rumore gaussiano: forte sulla forma, debole sul fondo
    rng = np.random.default_rng(seed)
    sigma = 12 + alone_arr * 46
    noise = rng.normal(0, 1, soft.shape) * sigma
    noisy = np.clip(soft + noise, 0, 255).astype(np.uint8)
    noisy_img = Image.fromarray(noisy, mode="L")

    # 3) mezzo passaggio a dither 1-bit (Floyd-Steinberg) — effetto stampa/fotocopia, pesato di piu' sulla forma
    dithered = noisy_img.convert("1", dither=Image.FLOYDSTEINBERG).convert("L")
    dith_arr = np.array(dithered, dtype=np.float32)
    peso_dither = 0.22 + alone_arr * 0.18
    mixed = noisy.astype(np.float32) * (1 - peso_dither) + dith_arr * peso_dither

    # 4) schiaccia il fondo lontano dalla forma verso il nero puro (stampa pulita, non statico)
    fondo_lontano = 1 - alone_arr
    mixed = mixed - fondo_lontano * 9
    out = Image.fromarray(np.clip(mixed, 0, 255).astype(np.uint8), mode="L")

    # 5) leggero autocontrast per far respirare bianchi/neri
    out = ImageOps.autocontrast(out, cutoff=1)

    # 6) vignettatura marcata sugli angoli
    vx, vy = np.meshgrid(np.linspace(-1, 1, W), np.linspace(-1, 1, H))
    dist = np.sqrt(vx ** 2 + vy ** 2)
    vig = np.clip(1 - 0.45 * (dist ** 2), 0.35, 1.0)
    out_arr = np.array(out, dtype=np.float32) * vig
    out = Image.fromarray(np.clip(out_arr, 0, 255).astype(np.uint8), mode="L")

    # 7) qualche graffio (linee sottili quasi verticali, opacita' bassa)
    d = ImageDraw.Draw(out)
    for _ in range(rnd.randint(3, 6)):
        x = rnd.randint(20, W - 20)
        y0 = rnd.randint(0, H // 3)
        y1 = y0 + rnd.randint(H // 3, H)
        jitter = rnd.randint(-8, 8)
        tono = rnd.choice([BG, FG])
        d.line([(x, y0), (x + jitter, min(y1, H))], fill=tono, width=1)

    return out


def _palette_fissa(n_grigi: int = 48) -> Image.Image:
    """Palette indicizzata fissa: N grigi in rampa + l'arancio esatto (251,70,4), cosi' la
    quantizzazione a 256 colori non 'sporca' l'accento (l'adattiva lo confondeva col grigio)."""
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


def componi(nome_out: str, disegna_fn) -> str:
    base = nuova_tela()
    d_base = _DrawProxy(ImageDraw.Draw(base), "base", FG)
    disegna_fn(d_base)
    grezza = applica_grana(base, seed=hash(nome_out) % 10000)

    rgb = Image.merge("RGB", (grezza, grezza, grezza))

    # isola il/i dettaglio/i arancione richiamando la stessa funzione soggetto in modalita' 'marker':
    # solo le chiamate marcate ACCENTO disegnano (in arancione vero), il resto e' ignorato
    marker = nuova_tela().convert("RGB")
    d_marker = _DrawProxy(ImageDraw.Draw(marker), "marker", ARANCIO)
    disegna_fn(d_marker)
    marker_l = ImageOps.grayscale(marker)
    mask = marker_l.point(lambda p: 255 if p > 10 else 0)
    mask = mask.filter(ImageFilter.GaussianBlur(0.6))
    arancio_layer = Image.new("RGB", (W, H), ARANCIO)
    rgb = Image.composite(arancio_layer, rgb, mask)

    # resa finale 2x del formato mostrato in card (~200x160): 400x320, ridotta con LANCZOS da 800x640
    # cosi' la grana resta fine ma il peso file scende sotto la soglia dei 120 KB
    rgb = rgb.resize((RESA_W, RESA_H), Image.LANCZOS)

    path = os.path.join(OUT, nome_out)
    pal_img = _palette_fissa(40)
    quant = rgb.quantize(palette=pal_img, dither=Image.NONE)
    quant.save(path, optimize=True)
    kb = os.path.getsize(path) / 1024
    print(f"{nome_out}: {kb:.1f} KB")
    return path


def main():
    os.makedirs(OUT, exist_ok=True)
    for i, fn in enumerate(SOGGETTI, start=1):
        componi(f"c{i}.png", fn)


if __name__ == "__main__":
    main()
