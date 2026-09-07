# -*- coding: utf-8 -*-
"""
analizza_css.py — estrae da un CSS grosso solo cio' che insegna qualcosa.

Perche' esiste: il CSS di `claude-speedrun.com` pesa 96 KB e quello di
`apsales.eu` 127 KB. Leggerli riga per riga costa quanto tre studi e insegna
quanto mezzo. Quasi tutto il peso e' utility generate (Tailwind); il valore sta
in sei posti soli:

  1. le variabili (:root, @theme, @layer) ..... la sua palette e le sue misure
  2. i @keyframes con il corpo ................ i suoi movimenti, per intero
  3. filtri, blend, clip-path, mask, backdrop .. gli effetti che non sono banali
  4. i gradienti non banali ................... come costruisce le superfici
  5. @font-face ............................... i caratteri e come li serve
  6. le classi scritte a mano ................. cio' che NON e' utility generata

Uso:
  python analizza_css.py <cartella-capture>          # es. capture/12-claude-speedrun-v2
  python analizza_css.py <cartella-capture> --file src/31-index.css

Scrive `<cartella>/estratto-css.md`. Nessuna emoji: console cp1252.
"""
import argparse
import io
import json
import os
import re
import sys

RE_VAR_BLOCK = re.compile(r"(:root|@theme[^{]*|html|\[data-theme[^\]]*\])\s*\{([^}]*)\}", re.S)
RE_VAR = re.compile(r"(--[A-Za-z0-9_-]+)\s*:\s*([^;]+);")
RE_KEYFRAMES = re.compile(r"@(?:-webkit-)?keyframes\s+([A-Za-z0-9_-]+)\s*\{", re.S)
RE_FONTFACE = re.compile(r"@font-face\s*\{([^}]*)\}", re.S)
RE_REGOLA = re.compile(r"([^{}@/]{1,400}?)\s*\{([^{}]*)\}", re.S)

INTERESSANTI = [
    ("filtri", re.compile(r"(?:^|[;{\s])(-webkit-)?(backdrop-)?filter\s*:\s*([^;}]+)")),
    ("blend", re.compile(r"(?:^|[;{\s])(mix-blend-mode|background-blend-mode)\s*:\s*([^;}]+)")),
    ("clip/mask", re.compile(r"(?:^|[;{\s])(clip-path|-webkit-mask[a-z-]*|mask[a-z-]*)\s*:\s*([^;}]+)")),
    ("ombre-testo", re.compile(r"(?:^|[;{\s])text-shadow\s*:\s*([^;}]+)")),
    ("contorno-testo", re.compile(r"(?:^|[;{\s])(-webkit-text-stroke[a-z-]*)\s*:\s*([^;}]+)")),
    ("prospettiva", re.compile(r"(?:^|[;{\s])(perspective|transform-style|backface-visibility)\s*:\s*([^;}]+)")),
    ("scroll", re.compile(r"(?:^|[;{\s])(scroll-behavior|scroll-snap-[a-z]+|overscroll-[a-z]+)\s*:\s*([^;}]+)")),
    ("container", re.compile(r"(?:^|[;{\s])(container-type|container-name)\s*:\s*([^;}]+)")),
]

RE_GRADIENTE = re.compile(r"((?:repeating-)?(?:linear|radial|conic)-gradient\([^;]{40,400}?\))")
RE_CUBIC = re.compile(r"cubic-bezier\([^)]+\)")
RE_COMMENTO = re.compile(r"/\*(.{20,600}?)\*/", re.S)


def corpo_keyframes(css, start):
    """Prende il corpo di un @keyframes contando le graffe."""
    i = css.index("{", start)
    liv = 0
    for j in range(i, len(css)):
        if css[j] == "{":
            liv += 1
        elif css[j] == "}":
            liv -= 1
            if liv == 0:
                return css[i:j + 1]
    return ""


def analizza(css, nome):
    fuori = []
    ap = fuori.append

    # 1 --- variabili
    variabili = {}
    for _, blocco in RE_VAR_BLOCK.findall(css):
        for k, v in RE_VAR.findall(blocco):
            v = " ".join(v.split())
            if len(v) < 200:
                variabili.setdefault(k, v)
    if variabili:
        ap("### Variabili — %d" % len(variabili))
        ap("")
        colori = {k: v for k, v in variabili.items()
                  if re.search(r"#[0-9a-fA-F]{3,8}|rgb|hsl|oklch|color-mix", v)}
        altre = {k: v for k, v in variabili.items() if k not in colori}
        if colori:
            ap("**Colore (%d):**" % len(colori))
            ap("```css")
            for k, v in list(colori.items())[:80]:
                ap("%s: %s;" % (k, v))
            ap("```")
            ap("")
        if altre:
            ap("**Misura, curva, tempo, carattere (%d):**" % len(altre))
            ap("```css")
            for k, v in list(altre.items())[:80]:
                ap("%s: %s;" % (k, v))
            ap("```")
            ap("")

    # 2 --- keyframes col corpo
    kf = []
    for m in RE_KEYFRAMES.finditer(css):
        kf.append((m.group(1), corpo_keyframes(css, m.start())))
    if kf:
        ap("### Movimenti — %d @keyframes" % len(kf))
        ap("")
        ap("```css")
        for nome_kf, corpo in kf[:26]:
            corpo = re.sub(r"\s+", " ", corpo).strip()
            ap("@keyframes %s %s" % (nome_kf, corpo[:420]))
        ap("```")
        ap("")

    # 3 --- proprieta' interessanti
    for etichetta, rx in INTERESSANTI:
        trovati = []
        for m in rx.finditer(css):
            val = " ".join(m.groups()[-1].split())
            if val and val not in ("none", "initial", "unset") and len(val) < 200:
                trovati.append(val)
        trovati = sorted(set(trovati))
        if trovati:
            ap("### %s — %d valori distinti" % (etichetta, len(trovati)))
            ap("```")
            for v in trovati[:22]:
                ap(v)
            ap("```")
            ap("")

    # 4 --- gradienti non banali
    grad = sorted(set(" ".join(g.split()) for g in RE_GRADIENTE.findall(css)))
    if grad:
        ap("### Gradienti non banali — %d" % len(grad))
        ap("```css")
        for g in grad[:18]:
            ap(g[:300])
        ap("```")
        ap("")

    # 5 --- curve
    curve = sorted(set(" ".join(c.split()) for c in RE_CUBIC.findall(css)))
    if curve:
        ap("### Curve — %d" % len(curve))
        ap("```")
        for c in curve[:20]:
            ap(c)
        ap("```")
        ap("")

    # 6 --- font-face
    ff = RE_FONTFACE.findall(css)
    if ff:
        ap("### @font-face — %d" % len(ff))
        ap("```css")
        for f in ff[:10]:
            ap("@font-face { %s }" % " ".join(f.split())[:260])
        ap("```")
        ap("")

    # 7 --- commenti dell'autore (lo strato 4: come l'ha costruito)
    commenti = [" ".join(c.split()) for c in RE_COMMENTO.findall(css)]
    commenti = [c for c in commenti if not c.lower().startswith(("!", "* ! ", "copyright", "licensed"))]
    if commenti:
        ap("### Commenti dell'autore — %d (**lo strato 4**)" % len(commenti))
        ap("")
        for c in commenti[:30]:
            ap("- %s" % c[:400])
        ap("")

    return fuori


def main():
    ap_ = argparse.ArgumentParser()
    ap_.add_argument("cartella")
    ap_.add_argument("--file", default=None)
    a = ap_.parse_args()

    d = a.cartella
    if not os.path.isdir(d):
        print("FAIL - cartella non trovata: %s" % d)
        return 1

    if a.file:
        css_files = [a.file]
    else:
        indice_p = os.path.join(d, "src", "_INDICE.json")
        if not os.path.isfile(indice_p):
            print("FAIL - manca src/_INDICE.json (cattura fatta con --no-src?)")
            return 1
        indice = json.load(io.open(indice_p, encoding="utf-8"))
        css_files = [r["file"] for r in sorted(indice, key=lambda x: -x["bytes"])
                     if r["file"].endswith(".css")]

    if not css_files:
        print("FAIL - nessun CSS nella cattura")
        return 1

    fuori = ["# Estratto CSS — %s" % os.path.basename(d.rstrip("/\\")),
             "",
             "Solo cio' che insegna qualcosa: variabili, movimenti, effetti, gradienti, curve,",
             "caratteri e **i commenti dell'autore**. Il resto e' utility generata e non si legge.",
             "",
             "Generato da `scripts/analizza_css.py`.",
             ""]
    for f in css_files[:6]:
        p = os.path.join(d, f)
        if not os.path.isfile(p):
            continue
        css = io.open(p, encoding="utf-8", errors="replace").read()
        fuori += ["---", "", "## `%s` — %d KB" % (f, len(css) // 1024), ""]
        pezzi = analizza(css, f)
        if pezzi:
            fuori += pezzi
        else:
            fuori += ["*(niente di notevole: utility generata)*", ""]

    out = os.path.join(d, "estratto-css.md")
    io.open(out, "w", encoding="utf-8", newline="").write("\n".join(fuori))
    print("[OK] %s -> estratto-css.md (%d CSS analizzati, %d KB di uscita)"
          % (os.path.basename(d.rstrip("/\\")), len(css_files[:6]),
             os.path.getsize(out) // 1024))
    return 0


if __name__ == "__main__":
    sys.exit(main())
