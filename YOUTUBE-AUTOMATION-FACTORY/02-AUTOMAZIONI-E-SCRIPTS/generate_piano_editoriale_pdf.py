#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_piano_editoriale_pdf.py — Genera il PDF del piano editoriale @Legamidiamore
(70 video/30gg/3 strategie) da memory/piano_editoriale_70.json.

Design v2 (2026-08-29, correzione dopo feedback Max: il v1 era "una tabella dentro un PDF",
troppo denso/colorato — riferimento dato da Max: deck "AP Sales", minimal, un concetto per
pagina, tanto bianco, grana leggerissima, rosso solo come accento, nessuna card a sfondo pieno).
Stack: HTML/CSS statico -> Playwright (Chromium) -> PDF.

Uso:
    python generate_piano_editoriale_pdf.py
    python generate_piano_editoriale_pdf.py --screenshot-only   # solo controllo visivo copertina
"""
import argparse
import base64
import html
import io
import json
import os
import random
from datetime import date

from playwright.sync_api import sync_playwright

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
FACTORY_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
IN_JSON = os.path.join(FACTORY_DIR, "memory", "piano_editoriale_70.json")
OUT_DIR = os.path.join(FACTORY_DIR, "06-DASHBOARD-E-METRICHE")
OUT_HTML = os.path.join(OUT_DIR, "piano-editoriale-70-legamidiamore-30gg.html")
OUT_PDF = os.path.join(OUT_DIR, "piano-editoriale-70-legamidiamore-30gg.pdf")
OUT_SHOT = os.path.join(OUT_DIR, "_cover-screenshot.png")

def _grain_data_uri() -> str:
    """Texture di grana come bitmap PNG pre-renderizzato (non feTurbulence SVG: un filtro SVG
    rasterizzato da Chromium in stampa PDF gonfiava il file a 16+MB). Contrasto alto (0-255
    pieno) perche' la v2 con range stretto (90-165) risultava invisibile — grana vera, non un
    accenno."""
    from PIL import Image
    random.seed(7)
    w = h = 140
    img = Image.new("L", (w, h))
    px = img.load()
    for y in range(h):
        for x in range(w):
            px[x, y] = random.randint(15, 240)
    buf = io.BytesIO()
    img.save(buf, format="PNG", optimize=True)
    b64 = base64.b64encode(buf.getvalue()).decode("ascii")
    return f"data:image/png;base64,{b64}"


GRAIN_PNG = _grain_data_uri()

CSS = f"""
@import url('https://fonts.googleapis.com/css2?family=Onest:wght@400;500;600;700;800;900&display=swap');

:root {{
  --red: #8B0000;
  --red-bright: #B22222;
  --ink: #111111;
  --grey: #666666;
  --grey-light: #999999;
  --paper: #FAFAF8;
  --hairline: rgba(17,17,17,0.12);
  --white: #FFFFFF;
}}
* {{ box-sizing: border-box; }}
html, body {{ margin: 0; padding: 0; }}
body {{
  font-family: 'Onest', -apple-system, 'Segoe UI', sans-serif;
  color: var(--ink);
  background: var(--paper);
  font-size: 12.5px;
}}
h1, h2, h3, h4 {{ font-family: 'Onest', sans-serif; font-weight: 800; letter-spacing: -0.02em; margin: 0; }}
p {{ line-height: 1.65; }}
a {{ color: var(--red); text-decoration: none; }}

.page {{
  position: relative;
  width: 100%;
  min-height: 297mm;
  padding: 20mm 18mm 16mm 18mm;
  page-break-after: always;
}}
.page:last-child {{ page-break-after: avoid; }}

.grain::before {{
  content: ""; position: absolute; inset: 0; pointer-events: none; z-index: 0;
  opacity: 0.16;
  background-image: url("{GRAIN_PNG}");
  background-repeat: repeat; background-size: 3.2mm 3.2mm;
}}
.grain-dark::before {{
  content: ""; position: absolute; inset: 0; pointer-events: none; z-index: 0;
  opacity: 0.24;
  background-image: url("{GRAIN_PNG}");
  background-repeat: repeat; background-size: 3.2mm 3.2mm;
}}

/* ---------- masthead / footer, ripetuti identici su ogni pagina interna. NIENTE LINEE: la
   separazione e' solo spazio, mai un border/hr (regola Max, 2026-08-29). ---------- */
.masthead {{
  position: relative; z-index: 1; display: flex; justify-content: space-between;
  align-items: center; font-size: 9px; letter-spacing: 0.14em; text-transform: uppercase;
  color: var(--grey); margin-bottom: 16mm;
}}
.masthead .mark {{ display: flex; align-items: center; gap: 6px; color: var(--ink); font-weight: 700; }}
.masthead .mark .tri {{
  width: 0; height: 0; border-left: 5px solid transparent; border-right: 5px solid transparent;
  border-bottom: 8px solid var(--red);
}}
.foot {{
  position: absolute; left: 18mm; right: 18mm; bottom: 10mm; z-index: 1;
  display: flex; justify-content: space-between; font-size: 8px; letter-spacing: 0.08em;
  text-transform: uppercase; color: var(--grey-light);
}}

/* ---------- COVER ---------- */
.cover {{
  background: var(--ink);
  color: var(--white);
  display: flex; flex-direction: column; justify-content: space-between;
  padding: 20mm 18mm;
  overflow: hidden;
}}
.cover .glow {{
  position: absolute; left: -10%; right: -10%; bottom: -20%; height: 60%;
  background: radial-gradient(60% 100% at 30% 100%, rgba(178,34,34,0.55) 0%, transparent 70%),
              radial-gradient(50% 90% at 75% 100%, rgba(139,0,0,0.5) 0%, transparent 70%);
  filter: blur(2px); z-index: 0;
}}
.cover .top-row {{ position: relative; z-index: 1; display: flex; justify-content: space-between; }}
.cover .pill {{
  display: inline-flex; align-items: center; border: 1px solid rgba(255,255,255,0.35);
  border-radius: 999px; padding: 8px 18px; font-size: 10.5px; font-weight: 600;
  letter-spacing: 0.02em; color: var(--white);
}}
.cover .mark {{ display: flex; align-items: center; gap: 6px; opacity: 0.85; }}
.cover .mark .tri {{
  width: 0; height: 0; border-left: 6px solid transparent; border-right: 6px solid transparent;
  border-bottom: 10px solid var(--red-bright);
}}
.cover h1 {{
  position: relative; z-index: 1; font-size: 60px; line-height: 0.98; margin-top: 30mm;
  text-transform: uppercase;
}}
.cover h1 .line-red {{ color: var(--red-bright); }}
.cover .sub {{
  position: relative; z-index: 1; font-size: 11px; color: rgba(255,255,255,0.6);
  margin-top: 8mm; text-transform: uppercase; letter-spacing: 0.06em;
}}
.cover .bottom-row {{
  position: relative; z-index: 1; display: flex; justify-content: space-between;
  align-items: flex-end; font-size: 9.5px; color: rgba(255,255,255,0.55);
  padding-top: 6mm;
}}
.cover .bottom-row .label {{ text-transform: uppercase; letter-spacing: 0.1em; font-size: 8px; color: rgba(255,255,255,0.4); margin-bottom: 2px; }}
.cover .bottom-row .val {{ color: rgba(255,255,255,0.85); font-weight: 500; }}

/* ---------- CONTENT PAGES ---------- */
.eyebrow {{
  position: relative; z-index: 1; font-size: 11px; font-weight: 800; color: var(--red);
  text-transform: uppercase; letter-spacing: 0.02em;
}}
.page h2.title {{ position: relative; z-index: 1; font-size: 32px; margin-top: 4px; color: var(--ink); }}
.lead {{ position: relative; z-index: 1; font-size: 12.5px; color: #333; max-width: 145mm; margin: 10mm 0 6mm 0; }}

/* Unita' atomiche: mai spezzate tra due pagine — o entrano intere, o vanno alla pagina dopo
   (regola Max, 2026-08-29). Le tabelle lunghe (Appendice) sono l'unica eccezione voluta. */
.unit {{ position: relative; z-index: 1; break-inside: avoid; page-break-inside: avoid; margin-top: 10mm; }}
.unit:first-of-type {{ margin-top: 0; }}

.section-label {{
  font-size: 13px; font-weight: 800; margin-bottom: 3mm;
}}
.section-label .num {{ color: var(--red); }}

ol.clean, ul.clean {{ margin: 4mm 0 0 0; padding-left: 5mm; }}
ol.clean li, ul.clean li {{ margin-bottom: 3.2mm; font-size: 12px; line-height: 1.6; color: #222; break-inside: avoid; }}
ol.clean li b, ul.clean li b {{ font-weight: 700; color: var(--ink); }}
ul.clean.dash {{ list-style: none; padding-left: 0; }}
ul.clean.dash li {{ padding-left: 4mm; position: relative; }}
ul.clean.dash li::before {{ content: "—"; position: absolute; left: 0; color: var(--grey-light); }}

.callout {{
  padding: 5mm 6mm; background: rgba(139,0,0,0.045); border-radius: 3px;
  font-size: 11.5px; line-height: 1.6; color: #222;
}}
.callout b {{ color: var(--red); }}

/* ---------- strategy blocks (niente linee: separati da spazio + tinta di sfondo alternata) ---------- */
.strat-block {{ padding: 6mm 6mm; border-radius: 4px; }}
.strat-block:nth-of-type(odd) {{ background: rgba(17,17,17,0.028); }}
.strat-block .row {{ display: flex; align-items: baseline; gap: 8px; }}
.strat-block .letter {{
  font-size: 13px; font-weight: 800; color: var(--white); background: var(--red);
  width: 20px; height: 20px; border-radius: 4px; display: inline-flex; align-items: center;
  justify-content: center; flex-shrink: 0;
}}
.strat-block h3 {{ font-size: 17px; }}
.strat-block .kv {{ margin-top: 3mm; font-size: 11px; color: #333; line-height: 1.7; }}
.strat-block .kv .k {{ color: var(--grey); text-transform: uppercase; font-size: 8.5px; letter-spacing: 0.08em; display: block; margin-top: 3mm; }}

/* ---------- calendar (niente linee: celle definite da spazio/tinta, non da bordi) ---------- */
.cal-grid {{ position: relative; z-index: 1; display: grid; grid-template-columns: repeat(7, 1fr); gap: 2.5mm; margin-top: 8mm; }}
.cal-cell {{ background: rgba(17,17,17,0.03); border-radius: 3px; padding: 3mm 2.5mm; min-height: 15mm; font-size: 8px; }}
.cal-cell .d {{ font-weight: 700; font-size: 9.5px; color: var(--ink); }}
.cal-cell .strats {{ margin-top: 2mm; display: flex; gap: 2px; flex-wrap: wrap; }}
.cal-cell .s {{ font-size: 7px; font-weight: 700; color: var(--red); }}
.cal-legend {{ display: flex; gap: 14mm; margin-top: 6mm; font-size: 9.5px; color: #333; }}

/* ---------- table (70 righe) — niente linee: righe separate da tinta alternata + padding ---------- */
table.plan {{ position: relative; z-index: 1; width: 100%; border-collapse: collapse; margin-top: 6mm; font-size: 9.2px; }}
table.plan thead {{ display: table-header-group; }}
table.plan tr {{ page-break-inside: avoid; break-inside: avoid; }}
table.plan th {{
  text-align: left; padding: 3mm 2.5mm 4mm 2.5mm; font-size: 8px; text-transform: uppercase;
  letter-spacing: 0.05em; font-weight: 700; color: var(--grey);
}}
table.plan tbody tr:nth-child(odd) td {{ background: rgba(17,17,17,0.028); }}
table.plan td {{ padding: 3.6mm 2.5mm; vertical-align: top; }}
table.plan td:first-child {{ border-radius: 3px 0 0 3px; }}
table.plan td:last-child {{ border-radius: 0 3px 3px 0; }}
table.plan .num {{ color: var(--grey-light); font-weight: 600; }}
table.plan .strat {{ font-weight: 800; color: var(--red); }}
table.plan .tit {{ font-weight: 700; color: var(--ink); }}
table.plan .hook {{ color: var(--grey); font-size: 8.6px; margin-top: 1mm; }}
table.plan .src {{ color: var(--grey); font-size: 8.4px; }}
table.plan .cmd {{ font-family: 'Consolas', monospace; font-size: 7px; color: var(--grey); word-break: break-all; }}
"""


def esc(s):
    return html.escape(str(s), quote=True)


def build_cover(piano):
    return f"""
<div class="page cover grain-dark">
  <div class="glow"></div>
  <div class="top-row">
    <div class="pill">Piano Operativo &middot; Ottobre 2026</div>
    <div class="mark"><span class="tri"></span> Digital Empire</div>
  </div>
  <div>
    <h1>Piano<br/>Editoriale<br/><span class="line-red">Mensile</span></h1>
    <div class="sub">70 video &middot; 30 giorni &middot; 3 strategie &middot; @Legamidiamore</div>
  </div>
  <div class="bottom-row">
    <div><div class="label">Periodo</div><div class="val">{esc(piano['periodo']['inizio'])} &rarr; {esc(piano['periodo']['fine'])}</div></div>
    <div><div class="label">Fonti</div><div class="val">223 video reali analizzati</div></div>
    <div><div class="label">Generato</div><div class="val">{esc(piano['generato_il'])}</div></div>
  </div>
</div>
"""


def masthead():
    return ('<div class="masthead"><span>Digital Empire</span>'
            '<span class="mark"><span class="tri"></span> Legami d\'Amore</span></div>')


def foot(page_label):
    return f'<div class="foot"><span>Piano Editoriale &middot; @Legamidiamore</span><span>{esc(page_label)}</span></div>'


def build_premessa(piano):
    return f"""
<div class="page grain">
  {masthead()}
  <div class="eyebrow">Premessa</div>
  <h2 class="title">Come leggere questo documento</h2>
  <p class="lead">Questo piano copre {piano['totale_video']} video su {piano['periodo']['giorni']} giorni,
  divisi su 3 strategie testate in parallelo sullo stesso canale. Ogni video ha una fonte reale
  verificata oggi — nessun link è inventato.</p>

  <div class="unit">
    <div class="section-label">Come è strutturato</div>
    <ol class="clean">
      <li><b>Fase 1 — Ricerca</b>: come sono stati trovati i 70 video sorgente, e cosa è cambiato
      rispetto al piano precedente.</li>
      <li><b>Fase 2 — Strategia</b>: le 3 strategie in test, una per canale reale.</li>
      <li><b>Fase 3 — Calendario</b>: quando esce ogni video.</li>
      <li><b>Fase 4 — Esecuzione</b>: il comando unico per produrre ogni video.</li>
      <li><b>Fase 5 — Performance</b>: quando e come si decide quale strategia vince.</li>
      <li><b>Appendice</b>: le 70 righe, ognuna pronta da eseguire.</li>
    </ol>
  </div>

  <div class="unit">
    <div class="section-label">Regola non negoziabile</div>
    <p style="font-size:12px; line-height:1.6; color:#222;">Zero video inventati. Ogni riga in
    questo documento è tracciabile in una cache reale scaricata il {esc(piano['generato_il'])}.
    Dove i dati reali non bastavano, il piano lo dice apertamente invece di riempire il vuoto.</p>
  </div>
  {foot('01')}
</div>
"""


def build_fase1(piano):
    return f"""
<div class="page grain">
  {masthead()}
  <div class="eyebrow">Fase 1</div>
  <h2 class="title">Ricerca — cosa è reale oggi</h2>
  <p class="lead">Scraping reale rilanciato il {esc(piano['generato_il'])} su 6 canali competitor
  storicamente monitorati. Risultato: 223 candidati validi, ma 2 correzioni rispetto a 3
  settimane fa.</p>

  <div class="unit">
    <div class="section-label">Cosa è cambiato</div>
    <ul class="clean dash">
      <li><b>@ciraolone</b> — nel calendario precedente era fonte per attrazione. Oggi è un canale
      AI/tech (tutorial Claude Code, CapCut). Escluso come fonte.</li>
      <li><b>@linguaggiosegretodelcorpo-6589</b> — nome suggerisce linguaggio del corpo, il
      contenuto reale è una scuola di ballo (Arthur Murray, tango, valzer). Mai stato in nicchia.
      Escluso.</li>
      <li><b>Soglia MIN_VPH=20</b> (standard del progetto per giudicare un video "performante") —
      nessun video reale in questa nicchia oggi la raggiunge (il migliore tocca 10,6 views/ora).
      Non applicata come filtro assoluto: selezione per ranking relativo dentro ogni canale.</li>
    </ul>
  </div>

  <div class="unit">
    <div class="section-label">Cosa resta (fonte reale, verificata)</div>
    <ul class="clean dash">
      <li><b>@PsicologiaFemminile-f8c</b> — 100 video validi, mediana 5,1 views/ora.</li>
      <li><b>@PsicologiadellAttrazionee</b> — 23 video validi, mediana 0,46 views/ora.</li>
      <li><b>@DinamicheSocialiAcademy</b> — 100 video validi, mediana 0,16 views/ora.</li>
    </ul>
  </div>

  <div class="unit callout"><b>Scelta editoriale</b> — 3 titoli originali con framing esplicito
  "dark psychology"/manipolazione (es. tattiche di Machiavelli, tecniche di controllo) sono
  stati scartati durante la selezione, anche se ad alto vph. Sostituiti con i successivi
  candidati reali dello stesso canale.</div>
  {foot('02')}
</div>
"""


def build_fase2(piano):
    s = piano["strategie"]
    kpi_breve = {
        "A": "vph medio riga ≥ 5,1 (mediana pool A alla generazione)",
        "B": "vph medio riga ≥ 0,46 (mediana pool B — pool più piccolo, atteso)",
        "C": "vph medio riga ≥ 0,16 (mediana pool C alla generazione)",
    }
    blocks = ""
    for k in ("A", "B", "C"):
        d = s[k]
        blocks += f"""
        <div class="strat-block unit">
          <div class="row"><span class="letter">{k}</span><h3>{esc(d['nome'])}</h3></div>
          <div class="kv">
            <span class="k">Fonte reale</span>@{esc(d['canale_sorgente'])}
            <span class="k">Target</span>{esc(d['target'])}
            <span class="k">Formato</span>{esc(d['formato'])}
            <span class="k">Volume</span>{esc(d['volume'])} video su 70 &middot; {esc(d['frequenza'])}
            <span class="k">KPI</span>{kpi_breve[k]}
          </div>
        </div>
        """
    return f"""
<div class="page grain">
  {masthead()}
  <div class="eyebrow">Fase 2</div>
  <h2 class="title">Le 3 strategie in test</h2>
  <p class="lead">Ogni strategia è mappata su un canale reale distinto. Il vincente ai
  checkpoint (Fase 5) si scala nel mese successivo, i perdenti si riducono.</p>
  {blocks}
  <div class="unit callout" style="margin-top:6mm;"><b>Nota sul KPI</b> — la soglia standard
  MIN_VPH=20 (<code>cashcow_check.py</code>) non è raggiunta da nessun video reale in questa
  nicchia oggi (il migliore tocca 10,6 vph). Ogni strategia usa quindi la propria mediana come
  riferimento, non la soglia standard del progetto.</div>
  {foot('03')}
</div>
"""


def build_fase3(piano):
    righe = piano["righe"]
    per_giorno = {}
    for r in righe:
        per_giorno.setdefault(r["data_pubblicazione"], []).append(r["strategia"])

    inizio = date.fromisoformat(piano["periodo"]["inizio"])
    fine = date.fromisoformat(piano["periodo"]["fine"])
    n_giorni = (fine - inizio).days + 1

    cells = ""
    for i in range(n_giorni):
        d = date.fromordinal(inizio.toordinal() + i)
        strat_del_giorno = per_giorno.get(d.isoformat(), [])
        marks = " ".join(f'<span class="s">{s}</span>' for s in strat_del_giorno)
        cells += f'<div class="cal-cell"><div class="d">{d.day}/{d.month}</div><div class="strats">{marks}</div></div>'

    return f"""
<div class="page grain">
  {masthead()}
  <div class="eyebrow">Fase 3</div>
  <h2 class="title">Calendario — 30 giorni</h2>
  <p class="lead">Ogni lettera in una cella è un video pubblicato quel giorno. Weekend e i due
  giorni bonus (lancio, metà mese) portano tutte e 3 le strategie insieme.</p>
  <div class="unit">
    <div class="cal-grid">{cells}</div>
    <div class="cal-legend">
      <span><b style="color:var(--red);">A</b> — Segnali &amp; Decodifica</span>
      <span><b style="color:var(--red);">B</b> — Tecnica &amp; Comando</span>
      <span><b style="color:var(--red);">C</b> — Allarme &amp; Verità Sociale</span>
    </div>
  </div>
  {foot('04')}
</div>
"""


def build_fase4():
    return f"""
<div class="page grain">
  {masthead()}
  <div class="eyebrow">Fase 4</div>
  <h2 class="title">Esecuzione — un comando</h2>
  <p class="lead">Ogni riga dell'appendice ha un comando già pronto. Non servono altre
  decisioni: si prende l'URL della riga e si lancia.</p>

  <div class="unit">
    <div class="section-label">Comando</div>
    <p style="font-family:'Consolas',monospace; font-size:11px; background:#111; color:#eee; padding:6mm 7mm; border-radius:3px;">
    python apex7_orchestrator.py run --canale legamidiamore --video-sorgente &lt;url_riga&gt; --phase 1
    </p>
  </div>

  <div class="unit">
    <div class="section-label">Regole permanenti del canale (automatiche, non si ripetono riga per riga)</div>
    <ul class="clean dash">
      <li>Voce sempre femminile, Fliki tier Ultra.</li>
      <li>Sottotitoli piccoli.</li>
      <li>Solo donne o coppia in scena — mai un uomo da solo.</li>
      <li>Pubblicazione sempre <b>privata</b> di default.</li>
      <li><code>--upload</code> richiede copertina reale già presente nella cartella video
      (regola permanente dal 2026-08-18, nessuna eccezione).</li>
    </ul>
  </div>
  {foot('05')}
</div>
"""


def build_fase5():
    return f"""
<div class="page grain">
  {masthead()}
  <div class="eyebrow">Fase 5</div>
  <h2 class="title">Performance &amp; pivot</h2>
  <p class="lead">Baseline di riferimento: MIN_VPH=20 di <code>cashcow_check.py</code> — soglia
  standard del progetto, qui usata per il lungo periodo, non per la selezione iniziale (Fase 1).</p>

  <div class="unit">
    <div class="section-label">4 checkpoint</div>
    <ol class="clean">
      <li><b>Giorno 7</b> — prima raccolta dati, nessun pivot, solo osservazione.</li>
      <li><b>Giorno 14</b> — primi confronti tra strategie, si individuano i trend.</li>
      <li><b>Giorno 21</b> — pivot possibile se una strategia è chiaramente indietro.</li>
      <li><b>Giorno 30</b> — verdetto: strategia vincente per il mese successivo.</li>
    </ol>
  </div>

  <div class="unit">
    <div class="section-label">Regole di pivot</div>
    <ul class="clean dash">
      <li>Strategia -30/-40% sotto la media delle altre due per almeno 14 giorni: volume ridotto
      del 50% nei giorni successivi, riallocato alla strategia migliore.</li>
      <li>Se dopo 21 giorni resta -40%: sostituzione completa della fonte per quella strategia.</li>
      <li>Strategia +30% sopra le altre: +25% di volume dalla settimana 3, si documenta il pattern
      vincente.</li>
      <li>Nessun cambio a metà settimana: gli aggiustamenti partono dal giorno dopo il checkpoint.</li>
    </ul>
  </div>
  {foot('06')}
</div>
"""


def build_appendice_intro():
    return f"""
<div class="page grain">
  {masthead()}
  <div class="eyebrow">Appendice</div>
  <h2 class="title">Le 70 righe</h2>
  <p class="lead">Ogni riga: data/ora, strategia, fonte reale con link, titolo adattato, hook,
  comando pronto. Zero campi da definire.</p>
  {foot('07')}
</div>
"""


def build_tabella_pages(piano):
    """Spezza le 70 righe su piu' pagine da ~14 righe, con lo stesso masthead/foot."""
    righe = piano["righe"]
    chunk = 14
    pages = []
    for i in range(0, len(righe), chunk):
        gruppo = righe[i:i + chunk]
        rows_html = ""
        for r in gruppo:
            rows_html += f"""
            <tr>
              <td class="num">{r['giorno']:02d}</td>
              <td>{esc(r['data_pubblicazione'])}<br/>{esc(r['orario_pubblicazione'])}</td>
              <td class="strat">{r['strategia']}</td>
              <td class="src">@{esc(r['canale_sorgente'])}<br/><a href="{esc(r['url_sorgente_reale'])}">link reale &rarr;</a></td>
              <td><span class="tit">{esc(r['titolo_adattato'])}</span><div class="hook">{esc(r['hook_3_secondi'])}</div></td>
              <td class="cmd">{esc(r['comando_cli'])}</td>
            </tr>
            """
        page_n = 8 + (i // chunk)
        pages.append(f"""
<div class="page grain">
  {masthead()}
  <table class="plan">
    <thead><tr>
      <th style="width:4%">#</th><th style="width:11%">Data/Ora</th><th style="width:5%">Str.</th>
      <th style="width:20%">Fonte reale</th><th style="width:38%">Titolo adattato + hook</th>
      <th style="width:22%">Comando</th>
    </tr></thead>
    <tbody>{rows_html}</tbody>
  </table>
  {foot(f'{page_n:02d}')}
</div>
""")
    return "".join(pages)


def build_html(piano):
    body = (build_cover(piano) + build_premessa(piano) + build_fase1(piano) + build_fase2(piano)
            + build_fase3(piano) + build_fase4() + build_fase5() + build_appendice_intro()
            + build_tabella_pages(piano))
    return f"""<!doctype html>
<html lang="it"><head><meta charset="utf-8"/>
<title>Piano Editoriale — Legami d'Amore</title>
<style>{CSS}</style></head>
<body>{body}</body></html>"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--screenshot-only", action="store_true",
                     help="Genera solo l'HTML e uno screenshot della copertina, niente PDF completo.")
    args = ap.parse_args()

    with open(IN_JSON, "r", encoding="utf-8") as f:
        piano = json.load(f)

    os.makedirs(OUT_DIR, exist_ok=True)
    html_doc = build_html(piano)
    with open(OUT_HTML, "w", encoding="utf-8") as f:
        f.write(html_doc)
    print(f"[+] HTML scritto: {OUT_HTML}")

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 900, "height": 1200})
        page.goto(f"file:///{OUT_HTML.replace(os.sep, '/')}", wait_until="networkidle", timeout=60000)

        page.screenshot(path=OUT_SHOT, clip={"x": 0, "y": 0, "width": 900, "height": 1200})
        print(f"[+] Screenshot copertina: {OUT_SHOT}")

        if not args.screenshot_only:
            page.pdf(
                path=OUT_PDF,
                format="A4",
                print_background=True,
                display_header_footer=False,
                margin={"top": "0mm", "bottom": "0mm", "left": "0mm", "right": "0mm"},
            )
            print(f"[+] PDF scritto: {OUT_PDF}")
        browser.close()


if __name__ == "__main__":
    main()
