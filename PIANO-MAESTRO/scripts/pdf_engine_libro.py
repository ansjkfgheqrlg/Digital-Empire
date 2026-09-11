"""
pdf_engine_libro.py — FASE 1 del piano 35: il motore del LIBRO, a flusso continuo.

Differenza con `pdf_engine_empire.py` (il motore dei dossier, standard-oro):
quello impagina pagine ad altezza fissa `297mm` con `overflow:hidden` — perfetto per
un dossier da dieci pagine, **letale per un libro**: qualunque riga in eccesso viene
tagliata in silenzio, senza errore. Qui il testo scorre e Chromium impagina da solo.

Cosa resta identico (estetica approvata da Max, non si tocca):
  - la tavolozza, la tipografia Onest + IBM Plex Mono, la grana PNG, l'arancio come
    accento sotto il 10%, nessuna linea o bordo, la copertina scura.
Cosa cambia:
  - `.flow`: niente altezza fissa, niente overflow nascosto;
  - la grana sta su `body::before { position:fixed }` — Chromium la ridisegna su ogni
    pagina, e l'immagine viene incorporata UNA volta sola;
  - intestazione e piede li stampa Playwright (`display_header_footer`), quindi la
    numerazione e' automatica e continua su settecento pagine;
  - le copertine e le aperture di Libro restano pagine intere forzate: li' il taglio
    non puo' avvenire perche' il contenuto e' corto e deciso.

Uso:
    from pdf_engine_libro import LibroDoc
    doc = LibroDoc(titolo="Il Libro dell'Agency", out_html=..., out_pdf=...)
    doc.copertina(...); doc.apertura_libro(...); doc.capitolo("II.3", "Titolo", markdown)
    doc.build()

Prova di tenuta:
    python pdf_engine_libro.py --test        # 200 pagine finte: peso, tempo, integrita'

Console Windows cp1252: nessuna emoji nei print.
"""

from __future__ import annotations

import io
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdf_engine_empire import CSS_TEMPLATE, grain_data_uri   # noqa: E402  (stile riusato verbatim)

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


# ------------------------------------------------------------------ CSS aggiuntivo (flusso)

CSS_FLUSSO = """
/* La pagina la decide Playwright (margini passati a page.pdf), non il CSS:
   con prefer_css_page_size l'intestazione e il piede non troverebbero spazio. */
@page { size:A4; }

html, body { background:var(--paper); }

/* La grana: una sola immagine, fissa, ridisegnata da Chromium su ogni pagina. */
body::before {
  content:""; position:fixed; inset:0; pointer-events:none; z-index:0;
  opacity:0.13; background-image:url("__GRAIN__");
  background-repeat:repeat; background-size:3mm 3mm;
}
.flow { position:relative; z-index:1; }

/* --- il corpo che scorre ------------------------------------------------- */
.flow p { font-size:11px; line-height:1.72; color:var(--text-2); margin:0 0 4.6mm 0; }
.flow p strong { color:var(--ink); font-weight:600; }
.flow h2.cap-t {
  font-size:26px; max-width:24ch; margin:0 0 6mm 0;
  break-after:avoid; page-break-after:avoid;
}
.flow h3 {
  font-size:14px; margin:9mm 0 3.5mm 0; color:var(--ink);
  break-after:avoid; page-break-after:avoid;
}
.flow h4 {
  font-size:9px; font-weight:700; letter-spacing:0.16em; text-transform:uppercase;
  color:var(--orange); margin:7mm 0 3mm 0;
  break-after:avoid; page-break-after:avoid;
}
.flow ul, .flow ol { margin:0 0 5mm 0; padding-left:6mm; }
.flow li {
  font-size:11px; line-height:1.64; color:var(--text-2); margin-bottom:3.2mm;
  break-inside:avoid;
}
.flow li strong { color:var(--ink); font-weight:600; }
.flow blockquote {
  margin:6mm 0; padding-left:6mm; position:relative;
  font-size:12px; line-height:1.66; color:var(--ink); font-weight:500; max-width:62ch;
  break-inside:avoid;
}
.flow blockquote::before {
  content:""; position:absolute; left:0; top:1mm; bottom:1mm; width:1.6mm;
  background:var(--orange); border-radius:1px;
}
.flow blockquote p { color:inherit; font-size:inherit; }
.flow code {
  font-family:'IBM Plex Mono',ui-monospace,monospace; font-size:9.5px;
  background:var(--tint); padding:0.4mm 1.2mm; border-radius:2px; color:var(--ink);
}
.flow pre {
  background:var(--tint); padding:4mm; border-radius:3px; overflow:hidden;
  break-inside:avoid; margin:0 0 5mm 0;
}
.flow pre code { background:none; padding:0; font-size:9px; line-height:1.55; }
.flow table {
  width:100%; border-collapse:collapse; margin:0 0 6mm 0; break-inside:avoid;
}
.flow th {
  font-size:7.5px; font-weight:600; letter-spacing:0.18em; text-transform:uppercase;
  color:var(--text-3); text-align:left; padding:0 4mm 3.5mm 0; vertical-align:bottom;
}
.flow td {
  font-size:10px; color:var(--text-2); padding:3mm 4mm 3mm 0;
  vertical-align:top; line-height:1.5;
}
.flow tbody tr:nth-child(odd) td { background:var(--tint); }
.flow tbody tr td:first-child { padding-left:3mm; }
.flow hr { border:0; height:0; margin:8mm 0; }

/* --- l'atomo citato: la prova che il contenuto viene davvero dalla fonte --- */
.ka {
  font-size:9.5px; color:var(--text-3); margin:0 0 5mm 0; line-height:1.6;
  break-inside:avoid;
}
.ka .id {
  font-family:'IBM Plex Mono',ui-monospace,monospace; font-weight:600;
  color:var(--orange); margin-right:6px; font-size:9px;
}

/* --- il blocco di confine: cosa fa Digital Empire su questo punto --------- */
.de {
  margin:9mm 0 6mm 0; padding:6mm 6mm 6mm 7mm; position:relative;
  background:var(--tint); border-radius:3px; break-inside:avoid;
}
.de::before {
  content:""; position:absolute; left:0; top:0; bottom:0; width:2mm;
  background:var(--ink); border-radius:3px 0 0 3px;
}
.de .tag {
  font-size:7.5px; font-weight:700; letter-spacing:0.2em; text-transform:uppercase;
  color:var(--ink); margin-bottom:3mm;
}
.de p { color:var(--text-2); font-size:10.5px; }

/* --- pagine intere e forzate: copertina, aperture, apertura di capitolo --- */
.piena {
  position:relative; width:100%; min-height:247mm;
  display:flex; flex-direction:column; justify-content:flex-end;
  page-break-after:always; break-after:page;
}
.piena.scura {
  background:var(--ink); color:#f4f2f6;
  margin:-24mm -20mm 0 -20mm; padding:24mm 20mm 20mm 20mm; min-height:297mm;
}
.piena.scura h1.big .soft { color:rgba(244,242,246,0.38); }
.piena.scura .occhiello { color:var(--orange); }
.piena.scura .sotto { color:rgba(244,242,246,0.66); }
.piena .occhiello {
  font-size:8.5px; font-weight:700; letter-spacing:0.22em; text-transform:uppercase;
  color:var(--orange); margin-bottom:5mm;
}
.piena .sotto { font-size:12px; color:var(--text-2); max-width:60ch; margin-top:10mm; line-height:1.74; }
h1.big { font-size:60px; line-height:0.94; letter-spacing:-0.04em; }
h1.libro { font-size:44px; line-height:0.98; letter-spacing:-0.035em; max-width:20ch; }
.romano {
  font-family:'IBM Plex Mono',ui-monospace,monospace; font-size:64px; font-weight:600;
  color:var(--orange); line-height:1; margin-bottom:8mm;
}
.indice-libro { margin-top:12mm; }
.indice-libro .voce {
  display:flex; gap:5mm; font-size:10.5px; color:var(--text-2);
  margin-bottom:3.4mm; break-inside:avoid;
}
.indice-libro .voce .c {
  font-family:'IBM Plex Mono',ui-monospace,monospace; font-size:9.5px;
  color:var(--text-3); min-width:13mm;
}
.cap-apre { break-before:page; page-break-before:always; padding-top:4mm; }
.cap-apre .occhiello {
  font-size:8.5px; font-weight:700; letter-spacing:0.22em; text-transform:uppercase;
  color:var(--orange); margin-bottom:5mm;
}
.cap-apre .lead {
  font-size:12px; color:var(--text-2); max-width:64ch; margin:0 0 10mm 0; line-height:1.72;
}
"""


# ------------------------------------------------------------------ conversione markdown

def md_html(testo: str) -> str:
    """Markdown -> HTML. Tabelle incluse. Nessun rischio: `markdown` e' gia' installato."""
    import markdown as _md
    return _md.markdown(
        testo,
        extensions=["tables", "fenced_code", "sane_lists", "attr_list"],
        output_format="html5",
    )


def esc(t: str) -> str:
    return (t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


# ------------------------------------------------------------------ il documento

class LibroDoc:
    """Un libro a flusso continuo. Si riempie in ordine, poi .build()."""

    def __init__(self, titolo: str, out_html: str, out_pdf: str,
                 marchio: str = "DIGITAL EMPIRE",
                 etichetta: str = "Il Libro dell'Agency — Edizione Integrale") -> None:
        self.titolo = titolo
        self.marchio = marchio
        self.etichetta = etichetta
        self.out_html = out_html
        self.out_pdf = out_pdf
        self._pezzi: list[str] = []

    # --- pagine intere -------------------------------------------------------

    def copertina(self, occhiello: str, titolo_html: str, sotto: str,
                  meta: list[tuple[str, str]] | None = None) -> None:
        voci = "".join(
            "<div><div class='k' style=\"font-size:7.5px;letter-spacing:0.2em;"
            "text-transform:uppercase;color:rgba(244,242,246,0.36);margin-bottom:2.5mm\">%s</div>"
            "<div class='v' style=\"font-size:11px;font-weight:600;color:#fff\">%s</div></div>"
            % (k, v) for k, v in (meta or [])
        )
        blocco_meta = ("<div style='display:flex;gap:9mm;margin-top:16mm;width:100%%'>%s</div>"
                       % voci) if voci else ""
        self._pezzi.append(
            "<section class='piena scura'>"
            "<div class='occhiello'>%s</div><h1 class='big'>%s</h1>"
            "<p class='sotto'>%s</p>%s</section>"
            % (occhiello, titolo_html, sotto, blocco_meta)
        )

    def apertura_libro(self, romano: str, titolo: str, sommario: str,
                       capitoli: list[tuple[str, str]] | None = None) -> None:
        voci = "".join(
            "<div class='voce'><span class='c'>%s</span><span>%s</span></div>" % (c, t)
            for c, t in (capitoli or [])
        )
        indice = "<div class='indice-libro'>%s</div>" % voci if voci else ""
        self._pezzi.append(
            "<section class='piena'>"
            "<div class='romano'>%s</div><h1 class='libro'>%s</h1>"
            "<p class='sotto'>%s</p>%s</section>"
            % (romano, titolo, sommario, indice)
        )

    # --- corpo ---------------------------------------------------------------

    def capitolo(self, codice: str, titolo: str, corpo_md: str,
                 apertura: str = "", blocco_de: str = "") -> None:
        lead = "<p class='lead'>%s</p>" % apertura if apertura else ""
        de = ""
        if blocco_de:
            de = ("<div class='de'><div class='tag'>Cosa fa Digital Empire su questo punto</div>%s</div>"
                  % md_html(blocco_de))
        self._pezzi.append(
            "<section class='cap-apre'>"
            "<div class='occhiello'>Capitolo %s</div>"
            "<h2 class='cap-t'>%s</h2>%s%s%s</section>"
            % (codice, titolo, lead, md_html(corpo_md), de)
        )

    def grezzo(self, html: str) -> None:
        self._pezzi.append(html)

    # --- costruzione ---------------------------------------------------------

    def render_html(self) -> str:
        css = (CSS_TEMPLATE + CSS_FLUSSO).replace("__GRAIN__", grain_data_uri(size=90))
        return (
            "<!doctype html><html lang='it'><head><meta charset='utf-8'>"
            "<title>%s</title><style>%s</style></head>"
            "<body><div class='flow'>%s</div></body></html>"
            % (esc(self.titolo), css, "".join(self._pezzi))
        )

    def _templates(self) -> tuple[str, str]:
        base = ("font-family:'Segoe UI',sans-serif;font-size:7pt;"
                "letter-spacing:0.14em;text-transform:uppercase;color:#8b8890;"
                "width:100%;padding:0 20mm;-webkit-print-color-adjust:exact;")
        testa = ("<div style=\"%s display:flex;justify-content:space-between;\">"
                 "<span style='font-weight:700;color:#1c1c1c'>%s</span>"
                 "<span>%s</span></div>" % (base, self.marchio, self.etichetta))
        piede = ("<div style=\"%s display:flex;justify-content:space-between;\">"
                 "<span>%s</span>"
                 "<span style='font-weight:600;color:#1c1c1c' class='pageNumber'></span></div>"
                 % (base, self.etichetta))
        return testa, piede

    def build(self, solo_html: bool = False) -> int:
        t0 = time.time()
        html = self.render_html()
        with io.open(self.out_html, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(html)
        print("[ok] HTML   %s  (%.0f KB)" % (self.out_html, len(html) / 1024))
        if solo_html:
            return 0

        from playwright.sync_api import sync_playwright

        testa, piede = self._templates()
        with sync_playwright() as p:
            browser = p.chromium.launch()
            pg = browser.new_page()
            pg.goto("file:///" + self.out_html.replace("\\", "/"), wait_until="load")
            pg.wait_for_timeout(2500)      # i font arrivano da Google: senza attesa stampa in fallback
            pg.pdf(
                path=self.out_pdf,
                format="A4",
                print_background=True,
                display_header_footer=True,
                header_template=testa,
                footer_template=piede,
                margin={"top": "24mm", "right": "20mm", "bottom": "20mm", "left": "20mm"},
            )
            browser.close()

        peso = os.path.getsize(self.out_pdf) / (1024 * 1024)
        pagine = conta_pagine(self.out_pdf)
        print("[ok] PDF    %s  (%.2f MB, %s pagine, %.1fs)"
              % (self.out_pdf, peso, pagine if pagine else "?", time.time() - t0))
        if peso > 12:
            print("[!]  oltre 12 MB: il piano 35 prevede la consegna in due tomi")
        elif peso > 8:
            print("[!]  oltre 8 MB: soglia di attenzione, grana gia' a size=90")
        return pagine or 0


def conta_pagine(path_pdf: str) -> int | None:
    """Conta le pagine leggendo il PDF grezzo: nessuna dipendenza in piu'."""
    try:
        with open(path_pdf, "rb") as fh:
            dati = fh.read()
    except Exception:
        return None
    n = dati.count(b"/Type /Page") - dati.count(b"/Type /Pages")
    if n <= 0:
        n = dati.count(b"/Type/Page") - dati.count(b"/Type/Pages")
    return n if n > 0 else None


# ------------------------------------------------------------------ prova di tenuta

def testo_del_pdf(path_pdf: str) -> str:
    """Rilegge il PDF e ne estrae il testo: e' l'unico modo onesto di provare
    che nulla e' stato tagliato in silenzio."""
    from pypdf import PdfReader
    lettore = PdfReader(path_pdf)
    return "\n".join((p.extract_text() or "") for p in lettore.pages)


def prova_di_tenuta() -> int:
    """~200 pagine finte. Non basta contarle: si rilegge il PDF e si verifica che
    ogni capitolo scritto sia davvero finito dentro, parola per parola."""
    qui = os.path.dirname(os.path.abspath(__file__))
    fuori = os.path.join(os.path.dirname(qui), "36-LIBRO-AGENCY-INTEGRALE", "prova")
    os.makedirs(fuori, exist_ok=True)

    doc = LibroDoc(
        titolo="Prova di tenuta del motore",
        out_html=os.path.join(fuori, "prova-tenuta.html"),
        out_pdf=os.path.join(fuori, "prova-tenuta.pdf"),
        etichetta="Prova di tenuta — 200 pagine",
    )
    doc.copertina(
        "Prova tecnica",
        "Duecento pagine <span class='soft'>per vedere se regge.</span>",
        "Nessun contenuto vero: solo carico. Si misura peso, tempo e integrita' del flusso.",
        [("Pagine attese", "~200"), ("Grana", "PNG size=90"), ("Motore", "flusso continuo")],
    )
    paragrafo = (
        "Questo paragrafo esiste solo per occupare spazio e mettere alla prova l'impaginazione "
        "a flusso continuo. Contiene **grassetto**, del `codice inline`, e abbastanza parole da "
        "riempire diverse righe di seguito senza che il motore possa barare. Se il testo venisse "
        "tagliato in silenzio, come faceva il vecchio contenitore ad altezza fissa, il conteggio "
        "finale delle pagine risulterebbe piu' basso del previsto e la prova fallirebbe. "
    )
    parole_sorgente = 0
    sentinelle = []          # una frase unica per capitolo: deve ricomparire nel PDF
    for n in range(1, 91):
        corpo = []
        sentinella = "SENTINELLA numero %d di questo capitolo di prova" % n
        sentinelle.append(sentinella)
        corpo.append(sentinella + ". ")
        corpo.append(paragrafo * 3)
        corpo.append("\n\n### Un sottotitolo che non deve restare orfano a fine pagina\n\n")
        corpo.append(paragrafo * 2)
        corpo.append("\n\n| Voce | Misura | Nota |\n|---|---|---|\n")
        for r in range(6):
            corpo.append("| Riga %d | %d | testo di contorno |\n" % (r + 1, r * 137))
        corpo.append("\n> Una citazione che deve restare intera e non spezzarsi fra due pagine.\n\n")
        corpo.append(paragrafo * 3)
        corpo.append("\n\n- primo punto di un elenco\n- secondo punto\n- terzo punto\n\n")
        corpo.append(paragrafo * 2)
        testo = "".join(corpo)
        parole_sorgente += len(testo.split())
        if n % 15 == 1:
            doc.apertura_libro("%d" % (n // 15 + 1), "Libro di prova numero %d" % (n // 15 + 1),
                               "Apertura forzata: deve occupare una pagina intera da sola.",
                               [("X.%d" % i, "Capitolo finto numero %d" % i) for i in range(1, 6)])
        doc.capitolo("P.%02d" % n, "Capitolo di prova numero %d" % n, testo,
                     apertura="Riga di apertura del capitolo, per vedere come si comporta il lead.",
                     blocco_de="Qui finirebbe il blocco di confine col metodo dell'Impero.")

    pagine = doc.build()
    peso = os.path.getsize(doc.out_pdf) / (1024 * 1024)

    testo_pdf = testo_del_pdf(doc.out_pdf)
    parole_pdf = len(testo_pdf.split())
    perse = [s for s in sentinelle if s.split(" di questo")[0] not in testo_pdf]

    print("")
    print("--- ESITO DELLA PROVA ---")
    print("capitoli scritti  : %d" % len(sentinelle))
    print("pagine prodotte   : %d" % pagine)
    print("parole in ingresso: %d" % parole_sorgente)
    print("parole rilette    : %d  (%.0f%% — il resto sono intestazioni e piedi)"
          % (parole_pdf, 100.0 * parole_pdf / max(1, parole_sorgente)))
    print("parole per pagina : %.0f" % (parole_sorgente / max(1, pagine)))
    print("peso              : %.2f MB  (%.1f KB/pagina)" % (peso, peso * 1024 / max(1, pagine)))
    print("proiezione 700 pag: %.1f MB" % (peso / max(1, pagine) * 700))
    print("capitoli persi    : %d" % len(perse))
    for s in perse[:10]:
        print("   MANCA: %s" % s)

    esito = (not perse) and parole_pdf >= 0.95 * parole_sorgente and pagine >= 150
    print("esito             : %s" % (
        "PASSA — nessun capitolo tagliato, il flusso regge"
        if esito else "FALLITO — qualcosa e' stato tagliato in silenzio"))
    return 0 if esito else 1


if __name__ == "__main__":
    if "--test" in sys.argv:
        sys.exit(prova_di_tenuta())
    print("Motore del libro. Prova di tenuta:  python pdf_engine_libro.py --test")
