"""
build_dossier28_pdf.py — Dossier 28 (Higgsfield + ElevenLabs) in PDF impaginato.

Metodo: HTML + Chromium `page.pdf()` via Playwright — lo stesso motore di
`company/02-info-business/ccm/brand/build_brand_guidelines.py`, e le stesse regole di
stile che Max ha fissato dopo AP Sales (2026-08-30):
  - fondo chiaro + grana leggera, mai massimalista
  - UN heading per pagina
  - il colore è accento, non superficie: niente card a gradiente pieno dietro al testo
  - NIENTE linee: la separazione è spazio (le tabelle usano un velo di tinta, non tratti)
  - unità atomiche: un blocco o entra intero nella pagina, o va alla successiva

La grana è un PNG pre-renderizzato, MAI feTurbulence SVG: in stampa Chromium lo
rasterizza e il file supera i 16 MB (lezione del piano editoriale YouTube).

Sorgente dei contenuti: `PIANO-MAESTRO/28-DOSSIER-HIGGSFIELD-ELEVENLABS.md`.
Il markdown resta l’originale; questo file ne fa l’edizione da leggere.

Uso:
    python build_dossier28_pdf.py
    python build_dossier28_pdf.py --html-only
"""

from __future__ import annotations

import argparse
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

HERE = os.path.dirname(os.path.abspath(__file__))
DEST = os.path.dirname(HERE)  # PIANO-MAESTRO/
OUT_HTML = os.path.join(DEST, "28-DOSSIER-HIGGSFIELD-ELEVENLABS.html")
OUT_PDF = os.path.join(DEST, "28-DOSSIER-HIGGSFIELD-ELEVENLABS.pdf")


# --------------------------------------------------------------------------- grana
def _grain_data_uri(size: int = 140, lo: int = 25, hi: int = 235, seed: int = 11) -> str:
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
/* Zero NON barrato: in un documento di cifre lo zero slashed di Plex sembra un refuso.
   `zero 0` spegne quella feature, `tnum` tiene le colonne allineate. */
.mono, .tab td.n, .tab th.n, .figure .n {
  font-feature-settings:"zero" 0, "tnum" 1;
  font-variant-numeric:tabular-nums;
}
.mono { font-family:'IBM Plex Mono',ui-monospace,Menlo,monospace; }

/* ------------------------------------------------------------------ impaginato */
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

/* ------------------------------------------------------------------ copertina */
.page.cover .masthead { position:absolute; left:20mm; right:20mm; top:22mm; margin:0; }
/* Il titolo siede sul terzo basso, non al centro: sopra resta l’aria, sotto la firma. */
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
.cover-meta { display:grid; grid-template-columns:repeat(4,1fr); gap:6mm; margin-top:18mm; }
.cover-meta .k {
  font-size:7.5px; letter-spacing:0.2em; text-transform:uppercase;
  color:rgba(244,242,246,0.36); margin-bottom:2.5mm;
}
.cover-meta .v { font-size:11px; font-weight:600; color:#fff; }

/* ------------------------------------------------------------------ pagina */
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

/* La colonna distribuisce i blocchi su tutta l’altezza: i margini sono il minimo,
   lo spazio che avanza si divide fra i blocchi invece di cadere tutto in fondo.
   È la differenza fra una pagina impaginata e una pagina che finisce prima. */
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

/* ------------------------------------------------------------------ numero grosso */
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

/* ------------------------------------------------------------------ tabella
   Nessuna linea: le righe si separano con un velo di tinta, che è superficie. */
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

/* ------------------------------------------------------------------ correzione */
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

/* ------------------------------------------------------------------ passo */
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


# --------------------------------------------------------------------------- pagine
_pages: list[str] = []


def page(html: str, cls: str = "", foot_l: str = "", foot_r: str = "") -> None:
    n = len(_pages) + 1
    left = foot_l or "Dossier 28 · Higgsfield ed ElevenLabs"
    right = foot_r or f"<span class='num'>{n:02d}</span>"
    mast = (
        "<div class='masthead'><span class='mk'>DIGITAL EMPIRE</span>"
        "<span>Dossier 28 · revisione 5 · 5 settembre 2026</span></div>"
    )
    _pages.append(
        f"<section class='page grain {cls}'><div class='layer'>{mast}{html}</div>"
        f"<div class='foot'><span>{left}</span><span>{right}</span></div></section>"
    )


def head(idx: str, eyebrow: str, title: str, lead: str = "") -> str:
    lead_html = f"<p class='lead'>{lead}</p>" if lead else ""
    return (
        f"<div class='eyebrow'><span class='idx'>{idx}</span>{eyebrow}</div>"
        f"<h2 class='title'>{title}</h2>{lead_html}"
    )


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


def figure(k: str, n: str, u: str, acc: bool = False) -> str:
    return (
        f"<div class='figure'><div class='k'>{k}</div>"
        f"<div class='n{' acc' if acc else ''}'>{n}</div><div class='u'>{u}</div></div>"
    )


# ============================================================ 01 · copertina
page(
    """
<div class='cover-mid'>
  <h1 class='big'>Higgsfield<br><span class='soft'>ed</span> <span class='acc'>ElevenLabs</span>.</h1>
  <p class='cover-lead'>Sessantotto pagine dei due siti lette sul DOM renderizzato, i Termini
  d’uso e la normativa italiana. Il conto è fatto sul volume di produzione dichiarato, non su
  un video singolo. Tre conclusioni delle stesure precedenti erano sbagliate e qui sono
  corrette, ognuna segnata dov’è.</p>
  <div class='cover-metà>
    <div><div class='k'>Volume</div><div class='v'>172 video · 904 min</div></div>
    <div><div class='k'>Mese di prova</div><div class='v'>circa €139</div></div>
    <div><div class='k'>A regime</div><div class='v'>€2.113 al mese</div></div>
    <div><div class='k'>Per</div><div class='v'>Max</div></div>
  </div>
</div>
""",
    cls="cover dark",
    foot_l="Emperator · 5 settembre 2026",
    foot_r="Piano d’acquisto",
)

# ============================================================ 02 · la prima mossa
page(
    head(
        "A",
        "La prima mossa",
        "Un mese di prova, <span class='soft'>mensile.</span>",
        "Nessun impegno annuale finche' le prove non hanno risposto. L’annuale sconta il 30% "
        "ma blocca dodici mesi: su un mese di prova annullerebbe la prova stessa.",
    )
    + """
<div class='body stack'>
  <div class='unit grid3'>
    """
    + figure("Higgsfield · Ultra 3.000", "€129", "Mensile. Tutti i modelli, otto job in parallelo, Canvas, Vibe Motion, Supercomputer, e i sette giorni di Kling 3.0 unlimited.")
    + figure("ElevenLabs · Creator", "$11", "Primo mese al 50%, poi $22. Voice cloning professionale, 121.000 crediti di voce, 275 minuti di chiamate.")
    + figure("Totale del mese di prova", "€139", "Il prezzo dell’opzione di dire di no. Promozioni come il 30% vengono rimesse ogni due mesi.", acc=True)
    + """
  </div>
  <div class='unit'>
    <div class='kicker'><span class='n'>—</span>Perché Ultra e non Plus</div>
    <p class='note'>Plus costa €59 e da' 1.200 crediti; le prove ne chiedono 2.640, quindi
    servirebbero €66 di pacchetti. Totale €125, praticamente identico — ma con sei job
    paralleli invece di otto e <strong>zero margine per gli scarti</strong>. A parità di spesa
    si prende quello che non finisce a metà prova.</p>
  </div>
  <div class='unit push'>
    <p class='quote'>«Faremo un acquisto di prova solamente per un mese, il minimo indispensabile
    per fare tutte le prove possibili. Pero' considera che le prime prove saranno scarti, perché
    sbaglieremo qualcosa.»<span class='src'>Max — 5 settembre 2026</span></p>
  </div>
</div>
"""
)

# ============================================================ 03 · le nove prove
page(
    head(
        "A",
        "Il mese di prova",
        "Nove prove, <span class='soft'>con lo scarto dentro al conto.</span>",
        "Tasso di scarto 3× invece di 2×: la prima volta si sbaglia il prompt, la reference o "
        "il formato. È messo nel conto, non sperato via.",
    )
    + "<div class='body stack'><div class='unit'>"
    + tab(
        ["Prova", "Composizione", "~Crediti"],
        [
            ["*1 · Video YouTube", "Un segmento da 2 min provato 3 volte, poi un video intero da 10 min", "~664"],
            ["*2 · Corti Vibe Motion", "3 corti, 3 iterazioni ciascuno, sfondi condivisi", "~552"],
            ["*3 · Misura del TTS", "5 campioni di lunghezza nota — incognita, budget", "~150"],
            ["*4 · Canvas", "Costruzione gratis, 3 esecuzioni del template", "~330"],
            ["*5 · Layers su slide Arena", "10 rigenerazioni del solo testo — incognita, budget", "~80"],
            ["*6 · Avatar UGC", "300 volti Soul 2.0, training del personaggio, 1 video da 30s", "~372"],
            ["*7 · Promo prodotto 30s", "Manuale Claude Code", "~144"],
            ["*8 · Confronto premium", "Seedance 2.0, Veo 3.1 e Sora 2 Pro sulla stessa scena", "~248"],
            ["*9 · MCP da Claude Code", "10 generazioni miste guidate da qui", "~100"],
            ["*Somma più 25% di margine", "2.640 + 660", "~3.300"],
        ],
        hi=2,
        cap="Ultra da' 3.000 crediti, quindi si è 300 sotto — <strong>ma solo sulla carta</strong>: "
        "i sette giorni di Kling 3.0 unlimited coprono a mano circa 900 crediti delle prove 1, 2, 7 "
        "e in parte 4. La finestra unlimited va usata per prima, non per ultima.",
    )
    + """</div>
  <div class='unit'>
    <div class='kicker'><span class='n'>—</span>Le regole di condotta</div>
    <ul class='clean'>
      <li><strong>Tetto di spesa nel codice:</strong> nessuna generazione sopra 50 crediti senza via libera esplicito. L’MCP non ne ha uno nativo.</li>
      <li><strong>Registro delle prove:</strong> ogni generazione annotata con modello, crediti ed esito. Senza registro il mese produce impressioni, non numeri.</li>
      <li><strong>Data del rinnovo sul calendario</strong> il giorno stesso dell’acquisto. Disdetta se due prove su tre falliscono.</li>
      <li><strong>I crediti non si riportano al mese dopo:</strong> quello che non si spende è perso, quindi le prove si fanno tutte.</li>
    </ul>
  </div>
</div>"""
)

# ============================================================ 04 · il volume
page(
    head(
        "B",
        "Il conto a regime",
        "Il volume vero <span class='soft'>di Digital Empire.</span>",
        "Le stesure precedenti costavano un video singolo e si fermavano lì. Questo è il "
        "conto che decide.",
    )
    + "<div class='body stack'><div class='unit'>"
    + tab(
        ["Formato", "Cadenza", "~Al mese", "~Minuti"],
        [
            ["*Video YouTube 10 min", "3-2-3-2 alternata, due giorni di stop", "~70", "~700"],
            ["*Corti 1-3 min", "Tre al giorno, sei una volta a settimana", "~102", "~204"],
            ["*Chiamate agente vocale", "Cento al giorno", "~3.000", "~6.000"],
        ],
        cap="Totale: <strong>172 video e 904 minuti di video finito al mese</strong>.",
    )
    + "</div><div class='unit'>"
    + tab(
        ["Scenario", "~Cr / video YT", "~Cr / corto", "~Crediti al mese", "~Higgsfield / mese"],
        [
            ["*Magro — poche clip, molte immagini; corti di sola grafica", "~176", "~45", "~16.890", "~€635"],
            ["*Medio — b-roll vero; corti con quattro sfondi in movimento", "~349", "~109", "~35.514", "~€1.496"],
            ["*Ricco — aperture Seedance 2.0; corti con otto clip", "~645", "~175", "~63.006", "~€2.768"],
        ],
        hi=1,
        cap="Base Ultra 9.000 (€270 annuale) più pacchetti a €0,046 il credito. Tasso di riprova 2×. "
        "Calcolo riproducibile: <strong>PIANO-MAESTRO/scripts/costo_produzione_higgsfield.py</strong>",
    )
    + "</div><div class='unit grid3'>"
    + figure("Higgsfield, scenario medio", "€1.496", "35.514 crediti al mese: quattro volte il tetto acquistabile da soli.")
    + figure("ElevenLabs, tutto compreso", "€617", "Pro più eccedenza chiamate, telefonia italiana e modello.")
    + figure("Totale mensile", "€2.113", "Circa €25.400 all’anno. Con il tasso di riprova a 1,3: €1.604 al mese.", acc=True)
    + "</div></div>"
)

# ============================================================ 05 · il listino
page(
    head(
        "B",
        "Il listino",
        "Dove stanno <span class='soft'>i crediti economici.</span>",
        "Sorpresa del listino: i piani per squadre sono i crediti più cari di tutti, perché il "
        "prezzo è per posto con un minimo di cinque.",
    )
    + "<div class='body stack'><div class='unit'>"
    + tab(
        ["Piano Higgsfield", "~Crediti/mese", "~Costo/mese", "~Per credito"],
        [
            ["*Team — cinque posti", "~5.000", "~€325", "~€0,0650"],
            ["*Scale — cinque posti", "~12.500", "~€750", "~€0,0600"],
            ["*Pacchetti extra", "~a consumo", "~—", "~€0,0463"],
            ["*Plus", "~1.200", "~€47", "~€0,0392"],
            ["*Ultra 3.000", "~3.000", "~€99", "~€0,0330"],
            ["*Ultra 6.000", "~6.000", "~€194", "~€0,0323"],
            ["*Ultra 9.000", "~9.000", "~€270", "~€0,0300"],
        ],
        hi=6,
        cap="Tariffe annuali, IVA esclusa. <strong>Starter non accede a Seedance</strong>: il piano "
        "minimo utile è Plus. Ultra 9.000 è il massimo acquistabile senza passare da un commerciale.",
    )
    + "</div><div class='unit'>"
    + tab(
        ["Piano ElevenLabs", "~Canone", "~Eccedenza chiamate", "~Totale/mese", "Crediti voce bastano?"],
        [
            ["*Creator", "~$22", "~$458", "~$480", "No — 121k contro 204k"],
            ["*Pro", "~$99", "~$381", "~$480", "Si' — 600k, concorrenza 20"],
            ["*Scale", "~$299", "~$181", "~$480", "Si', ma margine inutile"],
            ["*Business", "~$990", "~$0", "~$990", "Si', e costa il doppio per nulla"],
        ],
        hi=1,
        cap="<strong>Scoperta che vale $510 al mese:</strong> i piani per gli agenti vocali sono "
        "perfettamente lineari a $0,08 al minuto, quindi salire di livello non fa risparmiare un "
        "centesimo sulle chiamate — cambia solo i crediti voce e la concorrenza. Si prende il più "
        "basso che copra i crediti, ed è Pro.",
    )
    + "</div></div>"
)

# ============================================================ 06 · le correzioni
page(
    head(
        "C",
        "Onestà",
        "Dove mi ero <span class='soft'>sbagliato.</span>",
        "Tre conclusioni mie, corrette per iscritto invece che riscritte di nascosto. Nascono "
        "tutte dallo stesso difetto: rispondere sul caso singolo invece che sul sistema.",
    )
    + """
<div class='body stack'>
  <div class='unit fix'>
    <div class='tag'>Correzione 1 · Fliki</div>
    <h3>Higgsfield sostituisce Fliki, e fa un altro mestiere.</h3>
    <p class='note'>Avevo scritto che il tetto di quindici secondi per clip rendeva impraticabile
    un video da dieci minuti. Il conto era giusto <strong>solo se il video è tutto video</strong>.
    Esiste un modulo dedicato, <strong>AI Long Video Generator</strong>, che dichiara alla lettera
    il nostro caso d’uso: «Build YouTube and long-form content — faceless channels — full episodes
    with consistent voice and look».</p>
  </div>
  <div class='unit fix'>
    <div class='tag'>Correzione 2 · Caroselli</div>
    <h3>I caroselli restano su Arena. Il prezzo era l’asse sbagliato.</h3>
    <p class='note'>Le slide che Max produce in Arena sono un sistema di design coerente — tag
    pre-headline in pillola, grana, arancione sotto il dieci per cento come accento, grotesque
    bold col corsivo serif, card argento, numerazione, firma. Nano Banana Pro a due crediti
    genera <strong>la fotografia di una slide</strong>, non un layout. Su Arena il problema non è
    la qualità: è l’affidabilità dell’automazione, e quella va riparata, non sostituita.</p>
  </div>
  <div class='unit fix'>
    <div class='tag'>Correzione 3 · Il conto</div>
    <h3>Il costo di un video non è una risposta.</h3>
    <p class='note'>«€2,78 a video» era vero e inutile: su una decisione di spesa ricorrente il
    costo unitario va moltiplicato per il volume che l’azienda produce davvero — e il volume si
    chiede, se non lo si sa. Nello stesso errore stavano i corti, costati come dodici clip
    generative quando sono <strong>progetti Vibe Motion</strong>: da 239 a 109 crediti l’uno, e
    lì se ne andava metà del conto.</p>
  </div>
</div>
"""
)

# ============================================================ 07 · le leve
page(
    head(
        "D",
        "Architettura",
        "Le quattro leve, <span class='soft'>in ordine di peso.</span>",
        "Il conto non si vince comprando un piano più grande. Si vince qui.",
    )
    + """
<div class='body stack'>
  <div class='unit'>
    <div class='kicker'><span class='n'>01</span>Il tasso di riprova — vale metà del conto</div>
    <p class='note'>Se una clip su due va buttata, si paga il doppio. Passare da 2× a 1,3× porta
    Higgsfield da €1.496 a <strong>€987</strong> al mese: <strong>seimila euro all’anno</strong>.
    Non è una trattativa col fornitore — è la nostra libreria di prompt e le reference. È il
    lavoro che rende di più in assoluto.</p>
  </div>
  <div class='unit'>
    <div class='kicker'><span class='n'>02</span>Immagini al posto delle clip — rapporto 66 a 1</div>
    <p class='note'>Un’immagine Soul 2.0 costa <strong>0,12 crediti</strong>; un secondo di clip
    Kling 3.0 in 1080p ne costa 1,6. <strong>Sessantasei volte tanto.</strong> Il video lungo
    faceless va costruito su immagini mosse in montaggio, con le clip riservate a hook, stacchi e
    momenti che devono muoversi davvero.</p>
  </div>
  <div class='unit'>
    <div class='kicker'><span class='n'>03</span>Lo stampo — Canvas e Vibe Motion</div>
    <p class='note'>Vibe Motion produce un <strong>asset strutturato e modificabile</strong>, non
    un video piatto: si costruisce il modello una volta e si rigenera solo il testo, cento volte.
    Canvas salva l’intero flusso come template riutilizzabile. È qui che 102 corti al mese
    smettono di essere 102 produzioni e diventano cinque stampi.</p>
  </div>
  <div class='unit'>
    <div class='kicker'><span class='n'>04</span>Lo sprint dei sette giorni unlimited</div>
    <p class='note'>Kling 3.0 unlimited a inizio mese produce il girato senza toccare un credito.
    Ma la coda è rilassata — <strong>una generazione alla volta</strong> — e i Termini vietano
    l’automazione. A mano, sei ore al giorno per sette giorni, copre forse un quarto del
    fabbisogno. È una leva reale, non è la soluzione.</p>
  </div>
</div>
"""
)

# ============================================================ 08 · le due macchine
page(
    head(
        "E",
        "La fabbrica",
        "Le due macchine <span class='soft'>da sapere a memoria.</span>",
        "A 172 video al mese non conta saper generare: conta saper costruire lo stampo.",
    )
    + """
<div class='body stack'>
  <div class='unit'>
    <div class='kicker'><span class='n'>—</span>Canvas · l’officina a nodi</div>
    <ul class='clean'>
      <li><strong>Come si costruisce:</strong> nuova lavagna, nodo Text Prompt, lo colleghi a un nodo di generazione, scegli il modello, colleghi l’uscita al passo dopo. Ogni modello Higgsfield è un nodo, audio compreso.</li>
      <li><strong>Il dettaglio che fa sbagliare tutti:</strong> i nodi <strong>Seedance</strong> leggono le reference collegate solo se il prompt ne dichiara il ruolo; i nodi <strong>Kling</strong> trattano l’immagine collegata come primo fotogramma, e per il personaggio vogliono il tag @nome-elemento.</li>
      <li><strong>Crediti:</strong> costruire e collegare è gratis. Si paga solo quando un nodo genera. Quindi si progetta l’intera pipeline a costo zero.</li>
      <li><strong>Parallelo:</strong> otto job insieme su Ultra, output confrontabili a fianco. È così che si abbatte il tasso di riprova — si sceglie fra quattro varianti invece di rigenerare quattro volte la stessa.</li>
    </ul>
  </div>
  <div class='unit'>
    <div class='kicker'><span class='n'>—</span>Vibe Motion · il motore da testo ad animazione</div>
    <ul class='clean'>
      <li><strong>Non genera pixel:</strong> costruisce la logica dell’animazione, e l’uscita è un asset modificabile. Un template si riusa cento volte cambiando solo il testo.</li>
      <li><strong>Colore:</strong> si inseriscono i codici HEX o RGB esatti. Il nostro <strong>#fb4604</strong> entra alla lettera, non «più o meno arancione».</li>
      <li><strong>Safe zone social:</strong> gli elementi si trascinano dove servono e i sottotitoli non finiscono sotto i bottoni dell’interfaccia.</li>
      <li><strong>Movimento e tipografia:</strong> durata, ritardo e curve di easing su cursori; font nostri, crenatura e interlinea, ridimensionamento senza perdita. Categorie native: Infografiche, Presentazioni, Kinematic Captions.</li>
      <li><strong>Il costo è l’incognita:</strong> le iterazioni bruciano in fretta. Stima di terzi 15-50 crediti a progetto — nel calcolatore vale 40, ed è da tarare sul campo.</li>
    </ul>
  </div>
</div>
"""
)

# ============================================================ 09 · il muro legale
page(
    head(
        "F",
        "Vincolo",
        "Il muro sulle <span class='soft'>chiamate a freddo.</span>",
        "Non è prudenza: è aritmetica. Un agente vocale che chiama a freddo numeri italiani "
        "senza consenso e senza dichiararsi mette a rischio l’azienda per un ritorno che non "
        "vale la cifra.",
    )
    + """
<div class='body stack'>
  <div class='unit'>
    <div class='kicker'><span class='n'>—</span>Cosa è cambiato quest’anno</div>
    <ul class='clean'>
      <li><strong>Legge 49/2026, dal 19 giugno.</strong> Modifica l’articolo 51 del Codice del Consumo: opt-in obbligatorio, consenso preventivo esplicito e tracciabile. Nasce sul settore energia, le fonti divergono sulla trasversalità — va verificato con un legale prima di costruire, non dopo.</li>
      <li><strong>Registro Pubblico delle Opposizioni:</strong> copre anche le utenze aziendali, e vale sia per l’operatore umano sia per le chiamate automatiche.</li>
      <li><strong>Il 68% dei numeri «aziendali»</strong> nelle liste è intestato a persone fisiche: GDPR pieno, consenso esplicito.</li>
      <li><strong>AI Act articolo 50, dal 2 agosto.</strong> Obbligo di dichiarare dentro la conversazione, al primo contatto, che si parla con un’AI e per conto di chi. La privacy policy non basta.</li>
      <li><strong>Fino a €20 milioni o il 4% del fatturato</strong>, con responsabilità in solido fra mandante e contact center: non ci si copre appaltando.</li>
    </ul>
  </div>
  <div class='unit fix'>
    <div class='tag'>La strada che resta, ed è migliore</div>
    <p class='note'>In Preventa la catena di consenso <strong>esiste già</strong>: mandiamo
    WhatsApp, il concessionario risponde. Quello è un contatto che ha manifestato interesse, ed
    è lì che entra l’agente vocale — richiamo del lead caldo entro cinque minuti, qualifica in
    entrata, conferma appuntamenti, riattivazione dormienti, post-vendita. Con la dichiarazione AI
    nei primi tre secondi e l’opt-out immediato è in regola, e converte più del freddo.</p>
  </div>
  <div class='unit fix mute'>
    <div class='tag'>Il vincolo vero, che non è il prezzo</div>
    <p class='note'>Tremila chiamate al mese richiedono <strong>tremila contatti con consenso
    tracciabile</strong>. La domanda da rispondere prima di attivare l’agente non è quanto costa:
    è se generiamo cento risposte al giorno da richiamare.</p>
  </div>
</div>
"""
)

# ============================================================ 10 · il piano
page(
    head(
        "G",
        "Esecuzione",
        "Il piano, <span class='soft'>nell’ordine che conta.</span>",
        "Le prime tre mosse non costano niente e cambiano di quanto la quarta va dimensionata.",
    )
    + """
<div class='body stack-tight'>
  <div class='unit step'>
    <div class='idx'>F01</div>
    <div>
      <h3>Le tre mosse a costo zero, oggi</h3>
      <ul class='clean'>
        <li><strong>Startup Grant ElevenLabs.</strong> 33 milioni di caratteri contro un consumo di 204.000 al mese: vale oltre dieci anni di voce dei corti. Mezz’ora di lavoro.</li>
        <li><strong>Trattativa Enterprise con Higgsfield.</strong> Unico livello con sconti a volume per modello e crediti che si riportano al mese dopo — e con una cadenza 3-2-3-2 la produzione non è piatta. Richiede settimane: va aperta ora.</li>
        <li><strong>Riparare quality_gate.py:93.</strong> Ventuno fallimenti identici in memoria; a tre video al giorno quel gate ferma settanta produzioni al mese.</li>
      </ul>
    </div>
  </div>
  <div class='unit step'>
    <div class='idx'>F02</div>
    <div>
      <h3>Il mese di prova</h3>
      <p class='note'>Ultra 3.000 mensile più ElevenLabs Creator. Nove prove col budget crediti
      dichiarato, la finestra unlimited usata per prima, il registro delle prove aperto dal primo
      giorno. <strong>La misura del costo del TTS viene prima di ogni altra prova:</strong> senza
      quel numero nessun conto di questo dossier è chiuso.</p>
    </div>
  </div>
  <div class='unit step'>
    <div class='idx'>F03</div>
    <div>
      <h3>La fabbrica — settimane due-sei</h3>
      <ul class='clean'>
        <li><strong>Cinque template Canvas</strong>, uno per formato: YouTube lungo, corto prodotto, corto Preventa, promo, UGC.</li>
        <li><strong>Cinque template Vibe Motion</strong> con le Brand Guidelines dentro: safe zone, font, HEX esatti.</li>
        <li>Skill <strong>video-youtube-higgsfield</strong> al posto del ramo Fliki, sottotitoli nostri.</li>
        <li>Soul ID del personaggio di brand e libreria di reference — è la leva che abbassa il tasso di riprova, cioè metà del conto.</li>
        <li><strong>Riparazione del ramo Arena</strong> per i caroselli, che restano lì.</li>
      </ul>
    </div>
  </div>
  <div class='unit step'>
    <div class='idx'>F04</div>
    <div>
      <h3>L’agente vocale — settimane quattro-otto</h3>
      <p class='note'>Parere legale prima di tutto. Poi l’agente «richiamo lead caldo» su Preventa,
      dichiarazione AI nei primi tre secondi, opt-out immediato, registro dei consensi a prova di
      ispezione. Test su venti lead, poi si decide se salire.</p>
    </div>
  </div>
</div>
"""
)

# ============================================================ 11 · chiusura
page(
    head(
        "H",
        "Metodo e limiti",
        "Cosa è misurato <span class='soft'>e cosa no.</span>",
    )
    + """
<div class='body stack'>
  <div class='unit'>
    <div class='kicker'><span class='n'>—</span>Come è stato fatto</div>
    <p class='note'>Sessantotto pagine di higgsfield.ai lette con Playwright sul DOM renderizzato.
    Le pagine prezzi sono applicazioni a pagina singola: il fetch semplice le vede vuote e
    restituisce listini di terze parti, che nei fatti erano <strong>tutti sbagliati</strong> —
    davano Plus a $39 e Ultra a $99 in dollari, quando il listino reale in euro è €47 e €99 con
    una scala fino a €270. Più la documentazione API, l’help center, i Termini d’uso, i listini
    ElevenLabs e la documentazione del Voice Changer.</p>
  </div>
  <div class='unit'>
    <div class='kicker'><span class='n'>—</span>Le due incognite, dichiarate</div>
    <ul class='clean'>
      <li><strong>Il costo in crediti del Text-to-Speech Higgsfield.</strong> Non pubblicato da nessuna parte. Decide se i 700 minuti di voce dei video lunghi restano lì o vanno su ElevenLabs — cioè se a regime basta Pro o serve Scale.</li>
      <li><strong>Il costo reale di un progetto Vibe Motion.</strong> Nel calcolatore vale 40 crediti ed è una stima di terzi. Con 102 corti al mese, sbagliarla di venti crediti sposta €1.100 all’anno.</li>
    </ul>
    <p class='note'>Entrambe si misurano nella prima settimana del mese di prova. Sono scritte qui
    perché <strong>un numero non misurato resta non misurato</strong> anche quando fa comodo.</p>
  </div>
  <div class='unit push'>
    <div class='kicker'><span class='n'>—</span>Dove vive questo dossier</div>
    <ul class='clean'>
      <li><strong>Originale:</strong> PIANO-MAESTRO/28-DOSSIER-HIGGSFIELD-ELEVENLABS.md</li>
      <li><strong>Calcolatore:</strong> PIANO-MAESTRO/scripts/costo_produzione_higgsfield.py</li>
      <li><strong>Checkpoint:</strong> company/Memory/checkpoints/CP-20260905-001.md — codice di ripresa EMP-HGFD</li>
      <li><strong>Wiki:</strong> second-brain-vault/wiki/tools/Tool_Higgsfield_ElevenLabs.md</li>
    </ul>
  </div>
</div>
"""
)


# --------------------------------------------------------------------------- render
def render_html() -> str:
    css = CSS.replace("__GRAIN__", GRAIN)
    return (
        "<!doctype html><html lang='it'><head><meta charset='utf-8'>"
        "<title>Dossier 28 — Higgsfield ed ElevenLabs</title>"
        "<style>@page{size:A4;margin:0;}</style>"
        f"<style>{css}</style></head><body>{''.join(_pages)}</body></html>"
    )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--html-only", action="store_true")
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
        pg.wait_for_timeout(2500)  # i font arrivano da Google: senza attesa stampa in fallback
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
