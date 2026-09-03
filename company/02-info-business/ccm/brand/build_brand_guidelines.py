"""
build_brand_guidelines.py — Brand Guidelines di Claude Code Mastery (lancio 2026).

Metodo: HTML + Chromium `page.pdf()` via Playwright. Stesso motore del piano editoriale
YouTube, ma con le regole di stile che Max ha fissato dopo quello:
  - fondo chiaro + grana leggera, mai massimalista (rif. AP Sales, 2026-08-30)
  - UN heading per pagina
  - il colore e' accento, non superficie: niente card a gradiente pieno dietro al testo
  - NIENTE linee: la separazione e' spazio (regola 2026-08-29)
  - unita' atomiche: un blocco o entra intero nella pagina, o va alla successiva

I valori del sistema NON sono inventati: sono letti da
`Lancio corso skill beast/Leanding Page CCM/ccm-premium/src/app/globals.css`.
I dati del concorrente vengono dalla cattura forense in
`competitor/Andrei Pascu/site-study/capture/07-claude-speedrun/design-tokens.json`.

Uso:
    python build_brand_guidelines.py
    python build_brand_guidelines.py --html-only     # niente PDF, solo l'HTML per ispezione
"""

from __future__ import annotations

import argparse
import base64
import io
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_HTML = os.path.join(HERE, "CCM-Brand-Guidelines.html")
OUT_PDF = os.path.join(HERE, "CCM-Brand-Guidelines.pdf")


# --------------------------------------------------------------------------- grana
def _grain_data_uri(size: int = 140, lo: int = 25, hi: int = 235, seed: int = 11) -> str:
    """Grana come PNG pre-renderizzato.

    Non feTurbulence SVG: in stampa Chromium lo rasterizza e il file passa i 16 MB
    (lezione del piano editoriale YouTube). Range piu' stretto di quello: qui la grana
    deve accompagnare, non dominare.
    """
    from PIL import Image

    random.seed(seed)
    img = Image.new("L", (size, size))
    px = img.load()
    for y in range(size):
        for x in range(size):
            px[x, y] = random.randint(lo, hi)
    buf = io.BytesIO()
    img.save(buf, format="PNG", optimize=True)
    return "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode("ascii")


GRAIN = _grain_data_uri()


# --------------------------------------------------------------------------- CSS
CSS = """
@import url('https://fonts.googleapis.com/css2?family=Onest:wght@300;400;500;600;700;800&family=IBM+Plex+Mono:wght@400;500;600&display=swap');

:root {
  --ink:        #1c1c1c;
  --ink-2:      #0a0a0a;
  --ink-soft:   #2a2a2a;
  --paper:      #fafafa;
  --grey-bg:    #e8e8e6;
  --orange:     #fb4604;
  --orange-br:  #ff6a2e;
  --orange-dp:  #c9370a;
  --silver:     #d9d4e1;
  --silver-dim: #8a8594;
  --text-2:     #55535a;
  --text-3:     #8b8890;
}

* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; }
body {
  font-family: 'Onest', -apple-system, 'Segoe UI', sans-serif;
  color: var(--ink);
  background: var(--paper);
  font-size: 11.5px;
  -webkit-font-smoothing: antialiased;
}
h1, h2, h3 { margin: 0; font-weight: 700; letter-spacing: -0.028em; line-height: 1.06; }
p { margin: 0; line-height: 1.68; }
strong { font-weight: 600; }
em { font-style: italic; }
.mono {
  font-family: 'IBM Plex Mono', ui-monospace, Menlo, monospace;
  font-variant-numeric: tabular-nums;
}

/* ---------------------------------------------------------------- impaginato */
.page {
  position: relative;
  width: 210mm;
  height: 297mm;
  padding: 22mm 20mm 18mm 20mm;
  overflow: hidden;
  page-break-after: always;
  background: var(--paper);
}
.page:last-child { page-break-after: avoid; }
.page.dark { background: var(--ink); color: #f4f2f6; }
.page.grey { background: var(--grey-bg); }

.grain::before {
  content: ""; position: absolute; inset: 0; pointer-events: none; z-index: 0;
  opacity: 0.13;
  background-image: url("__GRAIN__");
  background-repeat: repeat; background-size: 3mm 3mm;
}
.page.dark .grain::before { opacity: 0.22; mix-blend-mode: overlay; }
.layer { position: relative; z-index: 1; height: 100%; display: flex; flex-direction: column; }

/* masthead e piede: solo spazio, nessuna linea */
.page.cover .masthead { position: absolute; left: 20mm; right: 20mm; top: 22mm; }
.masthead {
  display: flex; justify-content: space-between; align-items: baseline;
  font-size: 8px; letter-spacing: 0.2em; text-transform: uppercase;
  color: var(--text-3); margin-bottom: 15mm;
}
.page.dark .masthead { color: rgba(244,242,246,0.42); }
.masthead .mk { font-weight: 700; color: var(--ink); letter-spacing: 0.2em; }
.page.dark .masthead .mk { color: rgba(244,242,246,0.8); }

.foot {
  position: absolute; left: 20mm; right: 20mm; bottom: 11mm; z-index: 1;
  display: flex; justify-content: space-between;
  font-size: 7.5px; letter-spacing: 0.14em; text-transform: uppercase; color: var(--text-3);
}
.page.dark .foot { color: rgba(244,242,246,0.32); }
.foot .num { font-weight: 600; color: var(--ink); }
.page.dark .foot .num { color: rgba(244,242,246,0.7); }

/* ---------------------------------------------------------------- titolo di pagina */
.eyebrow {
  font-size: 8.5px; font-weight: 700; letter-spacing: 0.22em; text-transform: uppercase;
  color: var(--orange); margin-bottom: 5mm;
}
.eyebrow .idx { color: var(--text-3); margin-right: 8px; }
.page.dark .eyebrow .idx { color: rgba(244,242,246,0.35); }
h2.title { font-size: 30px; max-width: 20ch; }
h2.title .soft { color: var(--text-3); font-weight: 300; }
.page.dark h2.title .soft { color: rgba(244,242,246,0.42); }
.lead {
  font-size: 12px; color: var(--text-2); max-width: 62ch; margin-top: 7mm; line-height: 1.72;
}
.page.dark .lead { color: rgba(244,242,246,0.66); }

.body { flex: 1; margin-top: 14mm; display: flex; flex-direction: column; }
.unit { break-inside: avoid; page-break-inside: avoid; }
.stack > * + * { margin-top: 11mm; }
.stack-tight > * + * { margin-top: 7.5mm; }

/* ---------------------------------------------------------------- blocchi */
.kicker {
  font-size: 9px; font-weight: 700; letter-spacing: 0.16em; text-transform: uppercase;
  color: var(--ink); margin-bottom: 3mm;
}
.page.dark .kicker { color: rgba(244,242,246,0.9); }
.kicker .n { color: var(--orange); margin-right: 7px; }

.note { font-size: 10.5px; color: var(--text-2); line-height: 1.7; }
.page.dark .note { color: rgba(244,242,246,0.62); }

.grid2 { display: grid; grid-template-columns: 1fr 1fr; gap: 9mm; }
.grid3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 7mm; }

/* liste senza pallini grafici: il trattino e' tipografia, non decorazione */
ul.clean { list-style: none; margin: 0; padding: 0; }
ul.clean li {
  position: relative; padding-left: 6mm; margin-bottom: 4.4mm;
  font-size: 10.5px; line-height: 1.62; color: var(--text-2); break-inside: avoid;
}
ul.clean li::before { content: "—"; position: absolute; left: 0; color: var(--text-3); }
ul.clean li strong { color: var(--ink); font-weight: 600; }
.page.dark ul.clean li { color: rgba(244,242,246,0.66); }
.page.dark ul.clean li strong { color: #ffffff; }
.page.dark ul.clean li::before { color: rgba(244,242,246,0.3); }

/* dato misurato: il monospaziato dice "qui si misura" senza scriverlo */
.datum { display: flex; align-items: baseline; gap: 5mm; margin-bottom: 4.2mm; }
.datum .k {
  font-size: 8.5px; letter-spacing: 0.14em; text-transform: uppercase;
  color: var(--text-3); width: 42mm; flex: none;
}
.datum .v { font-size: 10.5px; color: var(--ink); flex: 1; min-width: 0; }
.page.dark .datum .v { color: #ffffff; }
.page.dark .datum .k { color: rgba(244,242,246,0.38); }
.spec.light .label { color: #8b8890 !important; }
.page.dark .spec.light .datum .k { color: #8b8890; }
.page.dark .spec.light .datum .v { color: #1c1c1c; }

/* ---------------------------------------------------------------- campioni colore */
.swatches { display: grid; grid-template-columns: repeat(4, 1fr); gap: 7mm 6mm; }
.sw .chip { height: 26mm; border-radius: 3px; }
.sw .nm { font-size: 9.5px; font-weight: 600; margin-top: 3mm; }
.sw .hex { font-size: 9px; color: var(--text-3); margin-top: 1mm; }
.sw .use { font-size: 8.5px; color: var(--text-2); margin-top: 2mm; line-height: 1.5; }
.page.dark .sw .use { color: rgba(244,242,246,0.55); }
.page.dark .sw .hex { color: rgba(244,242,246,0.4); }

.ramp { display: grid; grid-template-columns: repeat(6, 1fr); gap: 0; }
.ramp div { height: 12mm; }
.ramp-label { display: flex; justify-content: space-between; font-size: 8px; color: var(--text-3); margin-top: 2mm; }

/* specimen: il gradiente si mostra come campione etichettato, mai come fondo di testo */
.spec { border-radius: 3px; padding: 7mm; }
.spec .label {
  font-size: 8px; letter-spacing: 0.16em; text-transform: uppercase;
  color: rgba(244,242,246,0.45); margin-bottom: 4mm;
}
.silver-word {
  font-size: 34px; font-weight: 700; letter-spacing: -0.03em;
  background: linear-gradient(180deg, #ffffff 0%, #e8e3ef 35%, #b5afbd 72%, #8a8594 100%);
  -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent;
}
.silverorange-word {
  font-size: 34px; font-weight: 700; font-style: italic; letter-spacing: -0.03em;
  background: linear-gradient(135deg, #ffffff 0%, #d9d4e1 20%, #fb4604 55%, #ff8a4a 78%, #ffffff 100%);
  -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent;
}
.silverblack-word {
  font-size: 34px; font-weight: 700; letter-spacing: -0.03em;
  background: linear-gradient(180deg, #3a3a3a 0%, #1c1c1c 50%, #0a0a0a 100%);
  -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent;
}

/* ---------------------------------------------------------------- componenti dal vivo */
.btn-orange {
  display: inline-flex; align-items: center; gap: 7px;
  padding: 3.4mm 7mm; border-radius: 12px;
  font-weight: 600; font-size: 11px; letter-spacing: -0.01em;
  color: #ffffff; background: var(--orange);
  border: 1px solid rgba(255,255,255,0.12);
  box-shadow: 0 0 40px 0 rgba(251,70,4,0.35), inset 0 1px 0 rgba(255,255,255,0.18);
}
.btn-ghost {
  display: inline-flex; align-items: center; gap: 7px;
  padding: 3.4mm 7mm; border-radius: 12px;
  font-weight: 500; font-size: 11px; color: #f9f9f9;
  background: transparent; border: 2px solid rgba(249,249,249,0.18);
}
.bubble-orange {
  display: inline-flex; align-items: center; gap: 5px;
  background: linear-gradient(135deg, #fb4604 0%, #ff6a2e 100%);
  color: #fff; border-radius: 9999px; padding: 1.6mm 4mm;
  font-weight: 600; font-size: 9.5px;
}
.bubble-silver {
  display: inline-flex; align-items: center; gap: 5px;
  background: linear-gradient(135deg, #ffffff 0%, #d9d4e1 50%, #8a8594 100%);
  color: #1c1c1c; border-radius: 9999px; padding: 1.6mm 4mm;
  font-weight: 600; font-size: 9.5px;
}
.step-num {
  display: inline-flex; align-items: center; justify-content: center;
  width: 12mm; height: 12mm; border-radius: 12px;
  background: linear-gradient(135deg, #fb4604 0%, #ff8a4a 60%, #ffffff 100%);
  color: #1c1c1c; font-weight: 800; font-size: 14px;
}
.hl-block {
  display: inline; padding: 0.15em 0.3em; color: #fff; border-radius: 2px;
  background: linear-gradient(180deg, #ff6a2e 0%, #fb4604 55%, #c9370a 100%);
  box-shadow: inset 0 1px 0 rgba(255,255,255,0.18);
}
.pre-headline {
  font-size: 9px; font-weight: 600; letter-spacing: 0.3em; text-transform: uppercase;
  color: var(--silver-dim);
}
.chipbox { position: relative; height: 34mm; }
.silver-chip {
  position: absolute; display: inline-flex; align-items: center; gap: 5px;
  background: linear-gradient(135deg, rgba(255,255,255,0.95) 0%, #d9d4e1 60%, #b5afbd 100%);
  color: #1c1c1c; border-radius: 9999px; padding: 1.4mm 3.6mm;
  font-size: 9px; font-weight: 600;
  box-shadow: 0 8px 22px -12px rgba(0,0,0,0.6);
}
.silver-chip .dot { width: 5px; height: 5px; border-radius: 50%; background: var(--orange); }
.corner-demo { position: relative; height: 30mm; }
.corner-demo .cb { position: absolute; width: 7mm; height: 7mm; }
.corner-demo .tl { top: 0; left: 0; border-left: 2px solid var(--orange); border-top: 2px solid var(--orange); }
.corner-demo .tr { top: 0; right: 0; border-right: 2px solid var(--orange); border-top: 2px solid var(--orange); }
.corner-demo .bl { bottom: 0; left: 0; border-left: 2px solid var(--orange); border-bottom: 2px solid var(--orange); }
.corner-demo .br { bottom: 0; right: 0; border-right: 2px solid var(--orange); border-bottom: 2px solid var(--orange); }

.comp { break-inside: avoid; }
.comp .demo > * { white-space: nowrap; }
.comp .demo {
  min-height: 20mm; display: flex; align-items: center; justify-content: center;
  background: rgba(255,255,255,0.04); border-radius: 3px; padding: 5mm;
}
.comp .nm { font-size: 9.5px; font-weight: 600; margin-top: 4mm; }
.comp .rule { font-size: 8.5px; color: rgba(244,242,246,0.5); margin-top: 1.5mm; line-height: 1.5; }

/* ---------------------------------------------------------------- si / no */
.yn { display: grid; grid-template-columns: 1fr 1fr; gap: 8mm; }
.yn .h {
  font-size: 8.5px; font-weight: 700; letter-spacing: 0.18em; text-transform: uppercase;
  margin-bottom: 3.5mm;
}
.yn .si .h { color: var(--orange); }
.yn .no .h { color: var(--text-3); }
.yn .q { font-size: 11.5px; line-height: 1.6; color: var(--ink); }
.yn .no .q { color: var(--text-3); }
.yn .why { font-size: 9px; color: var(--text-2); margin-top: 2.5mm; line-height: 1.55; }
.page.dark .yn .q { color: #fff; }
.page.dark .yn .why { color: rgba(244,242,246,0.55); }

/* ---------------------------------------------------------------- confronto */
.vs { display: grid; grid-template-columns: 40mm 1fr 1fr; gap: 0 6mm; }
.vs .hd {
  font-size: 8.5px; font-weight: 700; letter-spacing: 0.16em; text-transform: uppercase;
  padding-bottom: 3mm;
}
.vs .hd.us { color: var(--orange); }
.vs .hd.them { color: var(--text-3); }
.vs .k { font-size: 9px; color: var(--text-3); padding: 3.6mm 0; }
.vs .c { font-size: 10px; padding: 3.6mm 0; color: var(--ink); }
.vs .c.dim { color: var(--text-3); }
.vs .band { background: rgba(251,70,4,0.05); }

/* ---------------------------------------------------------------- checklist */
.check { display: flex; gap: 4mm; align-items: flex-start; margin-bottom: 5.6mm; break-inside: avoid; }
.check .box {
  width: 3.6mm; height: 3.6mm; border-radius: 1px; flex: none; margin-top: 1.4mm;
  border: 1.4px solid var(--ink);
}
.check .t { font-size: 10.5px; line-height: 1.55; }
.check .t span { color: var(--text-2); }

/* ---------------------------------------------------------------- copertina */
.page.cover { padding: 24mm 20mm 22mm 20mm; }
.page.cover .layer { justify-content: flex-end; }
.page.cover .glow {
  position: absolute; left: -15%; right: -15%; bottom: -25%; height: 65%;
  background: radial-gradient(58% 100% at 26% 100%, rgba(251,70,4,0.42) 0%, transparent 68%),
              radial-gradient(48% 92% at 78% 100%, rgba(217,212,225,0.20) 0%, transparent 70%);
  z-index: 0;
}
.page.cover h1 {
  font-size: 62px; line-height: 0.95;
  letter-spacing: -0.038em;
}
.page.cover .sub {
  font-size: 10px; letter-spacing: 0.24em; text-transform: uppercase;
  color: rgba(244,242,246,0.45); margin-top: 9mm;
}
.page.cover .meta { display: flex; gap: 16mm; margin-top: 14mm; }
.page.cover .meta .lb {
  font-size: 7.5px; letter-spacing: 0.2em; text-transform: uppercase;
  color: rgba(244,242,246,0.35);
}
.page.cover .meta .vl { font-size: 10px; color: rgba(244,242,246,0.85); margin-top: 1.5mm; }

/* ---------------------------------------------------------------- indice */
.toc-row { display: flex; align-items: baseline; gap: 5mm; padding: 2.5mm 0; break-inside: avoid; }
.toc-row .n { font-size: 9px; color: var(--orange); width: 8mm; flex: none; font-weight: 600; }
.toc-row .t { font-size: 11px; font-weight: 500; }
.toc-row .d { flex: 1; }
.toc-row .p { font-size: 9px; color: var(--text-3); }
"""


# --------------------------------------------------------------------------- helper
def masthead(right: str) -> str:
    return (
        '<div class="masthead"><span class="mk">CCM</span>'
        f"<span>{right}</span></div>"
    )


def foot(num: int) -> str:
    return (
        '<div class="foot"><span>Claude Code Mastery · Brand Guidelines · v1.0</span>'
        f'<span class="num">{num:02d}</span></div>'
    )


_pages: list[str] = []


def page(inner: str, *, kind: str = "", head: str = "", num: int | None = None) -> None:
    cls = "page grain" + (f" {kind}" if kind else "")
    f = foot(num) if num is not None else ""
    _pages.append(f'<section class="{cls}"><div class="layer">{masthead(head) if head else ""}{inner}</div>{f}</section>')


def title_block(idx: str, eyebrow: str, title_html: str, lead: str = "") -> str:
    lead_html = f'<p class="lead">{lead}</p>' if lead else ""
    idx_html = f'<span class="idx mono">{idx}</span>' if idx else ""
    return (
        f'<div class="unit"><div class="eyebrow">{idx_html}{eyebrow}</div>'
        f'<h2 class="title">{title_html}</h2>{lead_html}</div>'
    )


# --------------------------------------------------------------------------- stampa
def render_html() -> str:
    import content

    content.build(page, title_block)
    css = CSS.replace("__GRAIN__", GRAIN)
    return (
        "<!doctype html><html lang='it'><head><meta charset='utf-8'>"
        "<title>Claude Code Mastery — Brand Guidelines</title>"
        f"<style>{css}</style></head><body>{''.join(_pages)}</body></html>"
    )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--html-only", action="store_true", help="scrive solo l'HTML, niente PDF")
    args = ap.parse_args()

    html = render_html()
    with io.open(OUT_HTML, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(html)
    print(f"[ok] HTML   {OUT_HTML}  ({len(html)/1024:.0f} KB, {len(_pages)} pagine)")

    if args.html_only:
        return 0

    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.chromium.launch()
        pg = browser.new_page()
        pg.goto("file:///" + OUT_HTML.replace("\\", "/"), wait_until="networkidle")
        # i font arrivano da Google: senza questa attesa la prima pagina stampa in fallback
        pg.wait_for_timeout(2500)
        pg.pdf(
            path=OUT_PDF,
            format="A4",
            print_background=True,
            margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
            prefer_css_page_size=True,
        )
        browser.close()

    size_mb = os.path.getsize(OUT_PDF) / (1024 * 1024)
    print(f"[ok] PDF    {OUT_PDF}  ({size_mb:.2f} MB)")
    if size_mb > 8:
        print("[!]  oltre 8 MB: controllare che la grana non sia finita in SVG invece che PNG")
    return 0


if __name__ == "__main__":
    sys.exit(main())
