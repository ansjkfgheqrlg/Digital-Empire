"""
pdf_engine_empire.py — il motore PDF di Digital Empire, estratto dallo standard-oro.

Standard-oro dichiarato da Max (2026-09-05): `PIANO-MAESTRO/28-DOSSIER-HIGGSFIELD-ELEVENLABS.pdf`
(revisione 5). Ogni PDF nuovo dell'Impero nasce da QUESTO motore, non da zero — è la
"specializzazione PDF" di Emperator: lo stile, la struttura, la qualità sono già decisi,
non vanno richiesti né discussi ogni volta (doctrine `emperator.md` §6.19).

Uso:
    from pdf_engine_empire import PDFDoc

    doc = PDFDoc(
        title="Titolo per il tag <title>",
        doc_label="Nome dossier · revisione N · data",
        footer_left="Nome dossier",
        out_html=".../nome.html",
        out_pdf=".../nome.pdf",
    )
    doc.page(doc.head("A", "Eyebrow", "Titolo <span class='soft'>attenuato.</span>", "Lead.") + "...")
    doc.build()

Regole di stile già dentro (non ridiscuterle, sono lo standard):
  - fondo chiaro + grana leggera, mai massimalista; copertina scura, pagine interne chiare
  - UN heading forte per pagina
  - il colore (#fb4604) è accento sotto il 10% dell'area, mai sfondo pieno
  - NIENTE linee/bordi da nessuna parte: la separazione è spazio o un velo di tinta
  - unità atomiche: `.unit` — un blocco o entra intero nella pagina o va alla successiva
  - grana come PNG pre-renderizzato (Pillow), MAI feTurbulence SVG: Chromium lo
    rasterizza e il PDF supera i 16 MB
  - tipografia Onest (testo) + IBM Plex Mono (numeri, tabular-nums, zero non barrato)

Motore: HTML + Chromium `page.pdf()` via Playwright — stesso approccio di
`company/02-info-business/ccm/brand/build_brand_guidelines.py` e di
`PIANO-MAESTRO/scripts/build_dossier28_pdf.py` (che ora può essere riscritto sopra
questo modulo, invariato nell'output).
"""

from __future__ import annotations

import base64
import io
import os
import random
import sys

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


# --------------------------------------------------------------------------- grana
def grain_data_uri(size: int = 140, lo: int = 25, hi: int = 235, seed: int = 11) -> str:
    """PNG di rumore pre-renderizzato, mai SVG feTurbulence (gonfia il PDF oltre i 16 MB)."""
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


# --------------------------------------------------------------------------- CSS (standard-oro, verbatim)
CSS_TEMPLATE = """
@import url('https://fonts.googleapis.com/css2?family=Onest:wght@300;400;500;600;700;800&family=IBM+Plex+Mono:wght@400;500;600&display=swap');

:root {
  --ink:#1c1c1c; --ink-2:#0a0a0a; --paper:#fafafa; --grey-bg:#e8e8e6;
  --orange:#fb4604; --orange-dp:#c9370a;
  --silver:#d9d4e1; --text-2:#55535a; --text-3:#8b8890;
  --tint:rgba(28,28,28,0.035);
}
* { box-sizing:border-box; }
html,body { margin:0; padding:0; }
body {
  font-family:'Onest',-apple-system,'Segoe UI',sans-serif;
  color:var(--ink); background:var(--paper); font-size:11.5px;
  -webkit-font-smoothing:antialiased;
}
h1,h2,h3 { margin:0; font-weight:700; letter-spacing:-0.028em; line-height:1.06; }
p { margin:0; line-height:1.68; }
strong { font-weight:600; }
.mono, .tab td.n, .tab th.n, .figure .n {
  font-feature-settings:"zero" 0, "tnum" 1;
  font-variant-numeric:tabular-nums;
}
.mono { font-family:'IBM Plex Mono',ui-monospace,Menlo,monospace; }

.page {
  position:relative; width:210mm; height:297mm; padding:22mm 20mm 18mm 20mm;
  overflow:hidden; page-break-after:always; background:var(--paper);
}
.page:last-child { page-break-after:avoid; }
.page.dark { background:var(--ink); color:#f4f2f6; }
.page.grey { background:var(--grey-bg); }

.grain::before {
  content:""; position:absolute; inset:0; pointer-events:none; z-index:0;
  opacity:0.13; background-image:url("__GRAIN__");
  background-repeat:repeat; background-size:3mm 3mm;
}
.page.dark .grain::before { opacity:0.22; mix-blend-mode:overlay; }
.layer { position:relative; z-index:1; height:100%; display:flex; flex-direction:column; }

.masthead {
  display:flex; justify-content:space-between; align-items:baseline;
  font-size:8px; letter-spacing:0.2em; text-transform:uppercase;
  color:var(--text-3); margin-bottom:15mm;
}
.page.dark .masthead { color:rgba(244,242,246,0.42); }
.masthead .mk { font-weight:700; color:var(--ink); letter-spacing:0.2em; }
.page.dark .masthead .mk { color:rgba(244,242,246,0.8); }

.foot {
  position:absolute; left:20mm; right:20mm; bottom:11mm; z-index:1;
  display:flex; justify-content:space-between;
  font-size:7.5px; letter-spacing:0.14em; text-transform:uppercase; color:var(--text-3);
}
.page.dark .foot { color:rgba(244,242,246,0.32); }
.foot .num { font-weight:600; color:var(--ink); }
.page.dark .foot .num { color:rgba(244,242,246,0.7); }

.page.cover .masthead { position:absolute; left:20mm; right:20mm; top:22mm; margin:0; }
.cover-mid {
  flex:1; display:flex; flex-direction:column; justify-content:flex-end; padding-bottom:14mm;
}
h1.big { font-size:64px; line-height:0.94; letter-spacing:-0.04em; }
h1.big .soft { color:rgba(244,242,246,0.38); font-weight:300; }
h1.big .acc { color:var(--orange); }
.cover-lead {
  font-size:12.5px; color:rgba(244,242,246,0.66); max-width:56ch;
  margin-top:12mm; line-height:1.74;
}
.cover-meta { display:flex; gap:9mm; margin-top:18mm; width:100%; }
.cover-meta > div { flex:1 1 0; min-width:0; }
.cover-meta .k {
  font-size:7.5px; letter-spacing:0.2em; text-transform:uppercase;
  color:rgba(244,242,246,0.36); margin-bottom:2.5mm;
}
.cover-meta .v { font-size:11px; font-weight:600; color:#fff; }

.eyebrow {
  font-size:8.5px; font-weight:700; letter-spacing:0.22em; text-transform:uppercase;
  color:var(--orange); margin-bottom:5mm;
}
.eyebrow .idx { color:var(--text-3); margin-right:8px; }
.page.dark .eyebrow .idx { color:rgba(244,242,246,0.35); }
h2.title { font-size:30px; max-width:22ch; }
h2.title .soft { color:var(--text-3); font-weight:300; }
.page.dark h2.title .soft { color:rgba(244,242,246,0.42); }
.lead { font-size:12px; color:var(--text-2); max-width:64ch; margin-top:7mm; line-height:1.72; }
.page.dark .lead { color:rgba(244,242,246,0.66); }

.body {
  flex:1; margin-top:13mm; padding-bottom:5mm;
  display:flex; flex-direction:column; justify-content:space-between;
}
.unit { break-inside:avoid; page-break-inside:avoid; }
.stack > * + * { margin-top:10mm; }
.stack-tight > * + * { margin-top:7mm; }
.push { margin-top:auto; }

.kicker {
  font-size:9px; font-weight:700; letter-spacing:0.16em; text-transform:uppercase;
  color:var(--ink); margin-bottom:3mm;
}
.page.dark .kicker { color:rgba(244,242,246,0.9); }
.kicker .n { color:var(--orange); margin-right:7px; }
.note { font-size:10.5px; color:var(--text-2); line-height:1.7; }
.page.dark .note { color:rgba(244,242,246,0.62); }
.note strong { color:var(--ink); }
.page.dark .note strong { color:#fff; }

.grid2 { display:grid; grid-template-columns:1fr 1fr; gap:9mm; }
.grid3 { display:grid; grid-template-columns:repeat(3,1fr); gap:7mm; }

ul.clean { list-style:none; margin:0; padding:0; }
ul.clean li {
  position:relative; padding-left:6mm; margin-bottom:4.4mm;
  font-size:10.5px; line-height:1.62; color:var(--text-2); break-inside:avoid;
}
ul.clean li::before { content:"—"; position:absolute; left:0; color:var(--text-3); }
ul.clean li strong { color:var(--ink); font-weight:600; }
.page.dark ul.clean li { color:rgba(244,242,246,0.66); }
.page.dark ul.clean li strong { color:#fff; }
.page.dark ul.clean li::before { color:rgba(244,242,246,0.3); }

.figure { display:flex; flex-direction:column; }
.figure .n {
  font-size:40px; font-weight:800; letter-spacing:-0.04em; line-height:1;
  font-variant-numeric:tabular-nums;
}
.figure .n.acc { color:var(--orange); }
.figure .k {
  font-size:7.5px; letter-spacing:0.2em; text-transform:uppercase;
  color:var(--text-3); margin-bottom:3mm;
}
.page.dark .figure .k { color:rgba(244,242,246,0.36); }
.figure .u { font-size:10px; color:var(--text-2); margin-top:3mm; line-height:1.6; }
.page.dark .figure .u { color:rgba(244,242,246,0.6); }

.tab { width:100%; border-collapse:collapse; }
.tab th {
  font-size:7.5px; font-weight:600; letter-spacing:0.18em; text-transform:uppercase;
  color:var(--text-3); text-align:left; padding:0 4mm 3.5mm 0; vertical-align:bottom;
}
.tab td {
  font-size:10.5px; color:var(--text-2); padding:3.2mm 4mm 3.2mm 0;
  vertical-align:top; line-height:1.5;
}
.tab td:last-child, .tab th:last-child { padding-right:0; }
.tab tbody tr:nth-child(odd) td { background:var(--tint); }
.tab tbody tr td:first-child { padding-left:3mm; }
.tab tbody tr:nth-child(odd) td:first-child { border-radius:2px 0 0 2px; }
.tab tbody tr:nth-child(odd) td:last-child { border-radius:0 2px 2px 0; }
.tab td.k { color:var(--ink); font-weight:500; }
.tab td.n, .tab th.n {
  text-align:right; font-family:'IBM Plex Mono',ui-monospace,monospace;
  font-variant-numeric:tabular-nums; font-size:10px; white-space:nowrap; color:var(--ink);
}
.tab tr.hi td { background:rgba(251,70,4,0.075) !important; }
.tab tr.hi td.k, .tab tr.hi td.n { color:var(--orange-dp); font-weight:600; }
.page.dark .tab td { color:rgba(244,242,246,0.66); }
.page.dark .tab td.k, .page.dark .tab td.n { color:#fff; }
.page.dark .tab tbody tr:nth-child(odd) td { background:rgba(255,255,255,0.045); }
.page.dark .tab th { color:rgba(244,242,246,0.36); }
.cap { font-size:9px; color:var(--text-3); line-height:1.6; margin-top:4mm; max-width:70ch; }
.page.dark .cap { color:rgba(244,242,246,0.42); }
.cap strong { color:var(--text-2); }
.page.dark .cap strong { color:rgba(244,242,246,0.7); }

.fix { padding-left:6mm; position:relative; }
.fix::before {
  content:""; position:absolute; left:0; top:1mm; bottom:1mm; width:1.6mm;
  background:var(--orange); border-radius:1px;
}
.fix .tag {
  font-size:7.5px; font-weight:700; letter-spacing:0.2em; text-transform:uppercase;
  color:var(--orange); margin-bottom:2.5mm;
}
.fix h3 { font-size:14px; margin-bottom:3mm; }
.fix.mute::before { background:var(--silver); }
.fix.mute .tag { color:var(--text-3); }

.step { display:grid; grid-template-columns:14mm 1fr; gap:0; break-inside:avoid; }
.step .idx {
  font-family:'IBM Plex Mono',ui-monospace,monospace; font-size:8.5px; font-weight:600;
  letter-spacing:0.12em; color:var(--orange); padding-top:1.5mm;
}
.step h3 { font-size:13px; margin-bottom:3mm; }

.quote {
  font-size:12.5px; line-height:1.66; color:var(--ink); max-width:60ch;
  font-weight:500;
}
.page.dark .quote { color:#fff; }
.quote .src { display:block; font-size:9px; color:var(--text-3); margin-top:4mm; font-weight:400;
  letter-spacing:0.14em; text-transform:uppercase; }
.page.dark .quote .src { color:rgba(244,242,246,0.4); }
"""


class PDFDoc:
    """Un documento PDF standard-oro. Aggiungi pagine con .page(), poi .build()."""

    def __init__(
        self,
        title: str,
        doc_label: str,
        footer_left: str,
        out_html: str,
        out_pdf: str,
        masthead: str = "DIGITAL EMPIRE",
    ) -> None:
        self.title = title
        self.doc_label = doc_label
        self.footer_left_default = footer_left
        self.masthead = masthead
        self.out_html = out_html
        self.out_pdf = out_pdf
        self._pages: list[str] = []

    def page(self, html: str, cls: str = "", foot_l: str = "", foot_r: str = "") -> None:
        n = len(self._pages) + 1
        left = foot_l or self.footer_left_default
        right = foot_r or f"<span class='num'>{n:02d}</span>"
        mast = (
            f"<div class='masthead'><span class='mk'>{self.masthead}</span>"
            f"<span>{self.doc_label}</span></div>"
        )
        self._pages.append(
            f"<section class='page grain {cls}'><div class='layer'>{mast}{html}</div>"
            f"<div class='foot'><span>{left}</span><span>{right}</span></div></section>"
        )

    @staticmethod
    def head(idx: str, eyebrow: str, title: str, lead: str = "") -> str:
        lead_html = f"<p class='lead'>{lead}</p>" if lead else ""
        return (
            f"<div class='eyebrow'><span class='idx'>{idx}</span>{eyebrow}</div>"
            f"<h2 class='title'>{title}</h2>{lead_html}"
        )

    @staticmethod
    def tab(cols: list[str], rows: list[list[str]], cap: str = "", hi: int | None = None) -> str:
        th = "".join(
            f"<th class='n'>{c[1:]}</th>" if c.startswith("~") else f"<th>{c}</th>" for c in cols
        )
        body = []
        for i, r in enumerate(rows):
            cls = " class='hi'" if hi is not None and i == hi else ""
            tds = "".join(
                f"<td class='n'>{c[1:]}</td>" if c.startswith("~")
                else (f"<td class='k'>{c[1:]}</td>" if c.startswith("*") else f"<td>{c}</td>")
                for c in r
            )
            body.append(f"<tr{cls}>{tds}</tr>")
        cap_html = f"<p class='cap'>{cap}</p>" if cap else ""
        return (
            f"<table class='tab'><thead><tr>{th}</tr></thead>"
            f"<tbody>{''.join(body)}</tbody></table>{cap_html}"
        )

    @staticmethod
    def figure(k: str, n: str, u: str, acc: bool = False) -> str:
        return (
            f"<div class='figure'><div class='k'>{k}</div>"
            f"<div class='n{' acc' if acc else ''}'>{n}</div><div class='u'>{u}</div></div>"
        )

    def render_html(self) -> str:
        css = CSS_TEMPLATE.replace("__GRAIN__", grain_data_uri())
        return (
            "<!doctype html><html lang='it'><head><meta charset='utf-8'>"
            f"<title>{self.title}</title>"
            "<style>@page{size:A4;margin:0;}</style>"
            f"<style>{css}</style></head><body>{''.join(self._pages)}</body></html>"
        )

    def build(self, html_only: bool = False) -> None:
        html = self.render_html()
        with io.open(self.out_html, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(html)
        print(f"[ok] HTML   {self.out_html}  ({len(html)/1024:.0f} KB, {len(self._pages)} pagine)")

        if html_only:
            return

        from playwright.sync_api import sync_playwright

        with sync_playwright() as p:
            browser = p.chromium.launch()
            pg = browser.new_page()
            pg.goto("file:///" + self.out_html.replace("\\", "/"), wait_until="networkidle")
            pg.wait_for_timeout(2500)  # i font arrivano da Google: senza attesa stampa in fallback
            pg.pdf(
                path=self.out_pdf,
                format="A4",
                print_background=True,
                margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
                prefer_css_page_size=True,
            )
            browser.close()

        size_mb = os.path.getsize(self.out_pdf) / (1024 * 1024)
        print(f"[ok] PDF    {self.out_pdf}  ({size_mb:.2f} MB)")
        if size_mb > 8:
            print("[!]  oltre 8 MB: controllare che la grana non sia finita in SVG invece che PNG")
