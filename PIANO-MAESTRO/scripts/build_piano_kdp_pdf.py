"""
build_piano_kdp_pdf.py — Piano editoriale settimanale KDP in PDF impaginato.

Edizione da leggere del piano che `engine/piano.py` (workflow libri-performanti-multiagente)
scrive in `LIBRI/_piani/piano_<data>.json`. Il JSON e il Markdown restano l'originale vivo;
questo file ne fa il PDF sopra il motore standard-oro `pdf_engine_empire.py` (emperator.md §6.19).

Ordine di Max (2026-09-11): in `documentazione Empire/` entra SOLO il PDF. La documentazione
ufficiale di un piano si compone di tre pezzi: il Markdown (casa naturale), lo script Python
(questo) e il PDF (casa naturale + doppione in `documentazione Empire/Piani/KDP/`, §6.17).

Uso:
    python build_piano_kdp_pdf.py                       # ultimo piano in LIBRI/_piani/
    python build_piano_kdp_pdf.py --piano piano_2026-08-31.json
    python build_piano_kdp_pdf.py --html-only
    python build_piano_kdp_pdf.py --no-doppione         # niente copia in documentazione Empire
"""

from __future__ import annotations

import argparse
import glob
import html
import io
import json
import os
import re
import shutil
import sys
from datetime import date

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))  # Digital Empire/
sys.path.insert(0, HERE)

from pdf_engine_empire import PDFDoc  # noqa: E402

WORKFLOW = os.path.join(
    ROOT, "company", "Ecosistemi", "02-INFO-BUSINESS", "Workflow", "libri-performanti-multiagente"
)
LIBRI = os.path.join(WORKFLOW, "LIBRI")
PIANI = os.path.join(LIBRI, "_piani")
DOC_EMPIRE = os.path.join(ROOT, "documentazione Empire", "Piani", "KDP")

MESI = [
    "", "gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno",
    "luglio", "agosto", "settembre", "ottobre", "novembre", "dicembre",
]


def data_it(iso: str, con_anno: bool = False) -> str:
    y, m, d = (int(x) for x in iso[:10].split("-"))
    s = f"{d} {MESI[m]}"
    return f"{s} {y}" if con_anno else s


def slug(titolo: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", titolo.lower()).strip("-")
    return s


def stato_libro(titolo: str) -> str:
    """Dove sta il libro adesso, letto dal disco: pubblicato / pronto / in lavorazione / da aprire."""
    cartella = titolo.replace(" ", "_").replace("'", "")
    if os.path.isdir(os.path.join(LIBRI, "libri_pubblicati", cartella)):
        return "pubblicato"
    if os.path.isdir(os.path.join(LIBRI, "libri_pronti", cartella)):
        return "pronto"
    if os.path.isdir(os.path.join(LIBRI, "in_lavorazione", slug(titolo))):
        return "in lavorazione"
    return "da aprire"


def esc(s: str) -> str:
    return html.escape(s, quote=False)


def num(x: float | int) -> str:
    if isinstance(x, float) and not x.is_integer():
        return f"{x:.1f}".replace(".", ",")
    return f"{int(x)}"


def prezzo(x: float | int) -> str:
    return f"${x:.2f}".replace(".", ",")


def carica_piano(percorso: str | None) -> tuple[dict, str]:
    if percorso is None:
        candidati = sorted(glob.glob(os.path.join(PIANI, "piano_*.json")))
        if not candidati:
            sys.exit(f"[x] nessun piano in {PIANI}")
        percorso = candidati[-1]
    elif not os.path.isabs(percorso):
        percorso = os.path.join(PIANI, percorso)
    with io.open(percorso, encoding="utf-8") as fh:
        return json.load(fh), percorso


def costruisci(piano: dict, out_html: str, out_pdf: str, html_only: bool) -> None:
    righe = piano["righe"]
    dal = piano["settimana_dal"]
    al = righe[-1]["data_produzione"]
    generato = piano["generato_il"][:10]
    nicchia_cat = piano["nicchia_catalogo"]
    autore = piano["autore_catalogo"]
    n = len(righe)
    stati = {r["titolo_lavoro"]: stato_libro(r["titolo_lavoro"]) for r in righe}
    fatti = sum(1 for s in stati.values() if s in ("pronto", "pubblicato"))

    doc = PDFDoc(
        title=f"Piano editoriale KDP — settimana dal {data_it(dal, True)}",
        doc_label=f"Piano editoriale KDP · settimana {data_it(dal)} – {data_it(al, True)}",
        footer_left="Piano editoriale KDP",
        out_html=out_html,
        out_pdf=out_pdf,
    )
    head, tab, figure = doc.head, doc.tab, doc.figure

    # ---------------------------------------------------------------- copertina
    doc.page(
        f"""
<div class='cover-mid'>
  <h1 class='big'>Piano editoriale<br><span class='acc'>KDP</span><span class='soft'>.</span></h1>
  <p class='cover-lead'>{n} libri in {n} giorni, dal {data_it(dal)} al {data_it(al, True)}.
  Ogni giorno una nicchia misurata su Amazon, una premessa, un angolo che la distingue dai
  concorrenti e il comando che apre il libro. Chi apre una riga non deve decidere niente.</p>
  <div class='cover-meta'>
    <div><div class='k'>Libri</div><div class='v'>{n} · uno al giorno</div></div>
    <div><div class='k'>Nicchia di catalogo</div><div class='v'>{esc(nicchia_cat)}</div></div>
    <div><div class='k'>Autore</div><div class='v'>{esc(autore)}</div></div>
    <div><div class='k'>Per</div><div class='v'>Max</div></div>
  </div>
</div>
""",
        cls="cover dark",
        foot_l=f"Gael · generato il {data_it(generato, True)}",
        foot_r="Piano settimanale",
    )

    # ---------------------------------------------------------------- il quadro
    rows = []
    for r in righe:
        a = r["dati_amazon"]
        rows.append([
            f"~{r['giorno']}",
            f"*{esc(r['titolo_lavoro'])}",
            esc(r["nicchia"]),
            f"~{num(a['punteggio'])}",
            f"~{prezzo(a['prezzo_medio'])}",
            f"~{a['concorrenti_deboli']}/{a['concorrenti_analizzati']}",
            stati[r["titolo_lavoro"]],
        ])
    doc.page(
        head(
            "A",
            "Il quadro della settimana",
            f"{n} libri, <span class='soft'>una nicchia al giorno.</span>",
            "Le nicchie sono ordinate per punteggio: si parte dalla più forte. Il punteggio nasce "
            "dai numeri Amazon del giorno in cui il piano è stato generato, non da una stima.",
        )
        + "<div class='body stack'><div class='unit'>"
        + tab(
            ["~G", "Titolo di lavoro", "Nicchia", "~Punteggio", "~Prezzo medio", "~Deboli", "Stato"],
            rows,
            cap=f"Stato letto dal disco al {data_it(date.today().isoformat(), True)}: "
            f"<strong>{fatti} su {n}</strong> già pronti o pubblicati. «Deboli» = concorrenti "
            "con presenza debole sul totale analizzato; più sono, più la nicchia è aperta.",
        )
        + """</div>
  <div class='unit'>
    <div class='kicker'><span class='n'>—</span>Come si legge una riga</div>
    <ul class='clean'>
      <li><strong>Punteggio:</strong> 0–100, misurato dal KDP-SCOUT su recensioni, prezzo e debolezza dei concorrenti. Sopra 70 si produce.</li>
      <li><strong>Prezzo medio:</strong> quello dei concorrenti sulla stessa nicchia; è il riferimento per il prezzo di listino del nostro libro.</li>
      <li><strong>Stato:</strong> «da aprire» = comando mai lanciato; «in lavorazione» = capitoli in corso; «pronto» = pacchetto passato dal KDP-GATE; «pubblicato» = su Amazon.</li>
    </ul>
  </div>
</div>""",
    )

    # ---------------------------------------------------------------- un libro per pagina
    for r in righe:
        a = r["dati_amazon"]
        st = r["struttura_prevista"]
        titolo = esc(r["titolo_lavoro"])
        idx = f"{r['giorno']:02d}"
        comando = esc(r.get("comando") or (
            f"python -m engine.kdp nuovo \"{r['titolo_lavoro']}\" "
            f"--nicchia \"{r['nicchia']}\" --autore \"{r['autore']}\""
        ))
        doc.page(
            head(
                idx,
                f"Giorno {r['giorno']} · {data_it(r['data_produzione'])} · {stati[r['titolo_lavoro']]}",
                f"{titolo}<span class='soft'>.</span>",
                f"Nicchia <strong>{esc(r['nicchia'])}</strong> · autore {esc(r['autore'])} · "
                f"{st['capitoli']} capitoli da circa {st['parole_per_capitolo']} parole, "
                f"minimo {st['pagine_minime_reali']} pagine reali.",
            )
            + "<div class='body stack'><div class='unit grid3'>"
            + figure("Punteggio nicchia", num(a["punteggio"]), f"su 100 · misurato il {data_it(a['misurato_il'])}", acc=True)
            + figure("Recensioni mediana", num(a["recensioni_mediana"]), "dei concorrenti analizzati")
            + figure("Prezzo medio", prezzo(a["prezzo_medio"]), f"{a['concorrenti_deboli']} deboli su {a['concorrenti_analizzati']}")
            + f"""</div>
  <div class='unit'>
    <div class='kicker'><span class='n'>—</span>Premessa</div>
    <p class='note'>{esc(r['premessa'])}</p>
  </div>
  <div class='unit'>
    <div class='kicker'><span class='n'>—</span>L’angolo che lo distingue</div>
    <p class='note'>{esc(r['angolo_differenziante'])}</p>
  </div>
  <div class='unit push'>
    <div class='kicker'><span class='n'>—</span>Il comando che apre il libro</div>
    <p class='note mono'>{comando}</p>
  </div>
</div>""",
        )

    # ---------------------------------------------------------------- il metodo
    doc.page(
        head(
            "B",
            "Come nasce il piano",
            "Il metodo, <span class='soft'>una volta per tutte.</span>",
            "Il piano non si scrive a mano: lo produce il motore del workflow libri, e ogni pezzo "
            "ha un agente responsabile. Qui c’è chi fa cosa, così il piano della settimana dopo "
            "nasce uguale.",
        )
        + """<div class='body stack'>
  <div class='unit'>
    <div class='step'><div class='idx'>01</div><div><h3>KDP-SCOUT misura le nicchie</h3>
    <p class='note'>Legge Amazon sulla nicchia di catalogo, conta recensioni, prezzi e concorrenti deboli, assegna il punteggio 0–100 e rifornisce il magazzino degli argomenti (<span class='mono'>magazzino_argomenti.json</span>). Da solo, senza che nessuno glielo chieda.</p></div></div>
  </div>
  <div class='unit'>
    <div class='step'><div class='idx'>02</div><div><h3>Il motore compone la settimana</h3>
    <p class='note'><span class='mono'>engine/piano.py</span> prende le nicchie migliori, ne assegna una al giorno, scrive premessa e angolo differenziante contro i concorrenti reali, e produce <span class='mono'>piano_<data>.json</span> più il Markdown. Skill: <span class='mono'>/piano-libri</span>.</p></div></div>
  </div>
  <div class='unit'>
    <div class='step'><div class='idx'>03</div><div><h3>Ogni mattina, il libro del giorno</h3>
    <p class='note'>La skill <span class='mono'>/libro-del-giorno</span> apre la riga di oggi e lancia il comando. KDP-EDITOR scrive i 24 capitoli; il libro passa da <span class='mono'>in_lavorazione/</span> a <span class='mono'>libri_pronti/</span> solo se il KDP-GATE conta le pagine reali (minimo 115), la numerazione e i metadati.</p></div></div>
  </div>
  <div class='unit'>
    <div class='step'><div class='idx'>04</div><div><h3>Caricamento su KDP</h3>
    <p class='note'>Da <span class='mono'>libri_pronti/</span> si carica seguendo <span class='mono'>LIBRI/CARICA-SU-KDP.md</span>; <span class='mono'>KDP_METADATA.txt</span> contiene titolo, descrizione, parole chiave e categorie già pronte. Dopo la pubblicazione il libro va in <span class='mono'>libri_pubblicati/</span>.</p></div></div>
  </div>
  <div class='unit push'>
    <p class='quote'>«Ogni riga è eseguibile così com’è: chi la apre non deve decidere niente.»
    <span class='src'>Intestazione del piano · Gael · 2 settembre 2026</span></p>
  </div>
</div>""",
    )

    doc.build(html_only=html_only)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--piano", help="file JSON del piano (nome in LIBRI/_piani/ o percorso)")
    ap.add_argument("--html-only", action="store_true")
    ap.add_argument("--no-doppione", action="store_true", help="non copiare in documentazione Empire")
    args = ap.parse_args()

    piano, percorso = carica_piano(args.piano)
    base = os.path.splitext(os.path.basename(percorso))[0]  # piano_2026-08-31
    out_html = os.path.join(PIANI, base + ".html")
    out_pdf = os.path.join(PIANI, base + ".pdf")
    costruisci(piano, out_html, out_pdf, args.html_only)

    if args.html_only:
        return
    # l'HTML e' un intermedio: non resta accanto al piano
    try:
        os.remove(out_html)
    except OSError:
        pass

    if not args.no_doppione:
        os.makedirs(DOC_EMPIRE, exist_ok=True)
        dal = piano["settimana_dal"]
        dest = os.path.join(DOC_EMPIRE, f"piano-editoriale-kdp-settimana-{dal}.pdf")
        shutil.copyfile(out_pdf, dest)
        print(f"[ok] DOPPIONE {dest}")


if __name__ == "__main__":
    main()
