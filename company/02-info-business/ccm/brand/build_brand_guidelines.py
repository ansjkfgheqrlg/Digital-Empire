"""
build_brand_guidelines.py — Brand Guidelines di Claude Code Mastery (lancio 2026).

Motore condiviso: `PIANO-MAESTRO/scripts/pdf_engine_empire.py`, lo stesso standard-oro di
`28-DOSSIER-HIGGSFIELD-ELEVENLABS.pdf` (direttiva Max, 2026-09-05: quel PDF e' lo standard,
questo file ne eredita CSS e copertina invece di tenerne uno leggermente diverso). Qui restano
solo i componenti che il dossier 28 non usa (campioni colore, checklist, confronto, ecc.).

Regole di stile (ereditate, non ridiscusse):
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
import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))  # radice del repo
ENGINE_DIR = os.path.join(ROOT, "PIANO-MAESTRO", "scripts")
sys.path.insert(0, ENGINE_DIR)

from pdf_engine_empire import CSS_TEMPLATE, grain_data_uri  # noqa: E402

OUT_HTML = os.path.join(HERE, "CCM-Brand-Guidelines.html")
OUT_PDF = os.path.join(HERE, "CCM-Brand-Guidelines.pdf")

GRAIN = grain_data_uri()

# --------------------------------------------------------------------------- CSS
# Il motore (CSS_TEMPLATE) porta gia': variabili colore, .page/.grain/.masthead/.foot,
# .eyebrow/.title/.lead, .body/.unit/.stack, .kicker/.note, .grid2/.grid3, ul.clean,
# e la copertina standard (.cover-mid, h1.big, .cover-lead, .cover-meta). Qui restano
# SOLO i componenti specifici delle Brand Guidelines che il dossier 28 non usa.
BRAND_CSS = """
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
.spec { border-radius: 3px; padding: 6mm; }
.spec .label {
  font-size: 8px; letter-spacing: 0.16em; text-transform: uppercase;
  color: rgba(244,242,246,0.45); margin-bottom: 4mm;
}
.silver-word {
  font-size: 31px; font-weight: 700; letter-spacing: -0.03em;
  background: linear-gradient(180deg, #ffffff 0%, #e8e3ef 35%, #b5afbd 72%, #8a8594 100%);
  -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent;
}
.silverorange-word {
  font-size: 31px; font-weight: 700; font-style: italic; letter-spacing: -0.03em;
  background: linear-gradient(135deg, #ffffff 0%, #d9d4e1 20%, #fb4604 55%, #ff8a4a 78%, #ffffff 100%);
  -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent;
}
.silverblack-word {
  font-size: 31px; font-weight: 700; letter-spacing: -0.03em;
  background: linear-gradient(180deg, #3a3a3a 0%, #1c1c1c 50%, #0a0a0a 100%);
  -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent;
}

/* campioni di grana: stessa superficie, tre intensita' */
.grainrow { display: grid; grid-template-columns: repeat(3, 1fr); gap: 6mm; }
.gspec { position: relative; height: 22mm; border-radius: 3px; overflow: hidden; background: #1c1c1c; }
.gspec::after {
  content: ""; position: absolute; inset: 0;
  background-image: url("__GRAIN__");
  background-repeat: repeat; background-size: 3mm 3mm;
}
.gspec.g0::after { opacity: 0; }
.gspec.g1::after { opacity: 0.13; }
.gspec.g2::after { opacity: 0.30; }
.gspec .tag {
  position: absolute; left: 4mm; bottom: 3.5mm; z-index: 2;
  font-size: 8px; letter-spacing: 0.16em; text-transform: uppercase;
  color: rgba(244,242,246,0.72);
}
.gcap { font-size: 9px; color: rgba(244,242,246,0.55); margin-top: 3mm; line-height: 1.5; }

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
.check { display: flex; gap: 4mm; align-items: flex-start; margin-bottom: 7.6mm; break-inside: avoid; }
.check .box {
  width: 3.6mm; height: 3.6mm; border-radius: 1px; flex: none; margin-top: 1.4mm;
  border: 1.4px solid var(--ink);
}
.check .t { font-size: 10.5px; line-height: 1.55; }
.check .t span { color: var(--text-2); }

/* La copertina (.cover-mid, h1.big, .cover-lead, .cover-meta) e' quella del motore
   condiviso — niente piu' glow radiale ne' testo centrato: stessa impostazione bassa
   e ferma del dossier 28 (direttiva Max, 2026-09-05, sulla copertina). */

/* ---------------------------------------------------------------- indice */
.toc-row { display: flex; align-items: baseline; gap: 5mm; padding: 3.5mm 0; break-inside: avoid; }
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
    css = (CSS_TEMPLATE + BRAND_CSS).replace("__GRAIN__", GRAIN)
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
