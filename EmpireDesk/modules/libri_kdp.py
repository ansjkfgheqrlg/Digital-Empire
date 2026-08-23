# -*- coding: utf-8 -*-
"""
modules/libri_kdp.py — il pannello dei LIBRI KDP dentro Aureus (piano V2, checkpoint V7).

Cosa aggiunge: una tile "Libri KDP" che mostra a che punto sono i libri in lavorazione,
quali sono pronti da caricare, e permette di lanciare l'analisi delle nicchie su Amazon.

PERCHE' IL PULSANTE NON "SCRIVE UN LIBRO" — la parte onesta:
la scrittura dei capitoli passa da Claude in sessione (SOP-SCRIVERE-UN-LIBRO.md), non da uno
script: non esiste un eseguibile che produca un manoscritto da solo, e fingere un bottone
"Genera libro" significherebbe mettere in Aureus un pulsante che non fa quello che promette.
Quello che il pannello fa davvero:
  - dice a che punto e' ogni libro (capitoli scritti, parole, cosa manca);
  - elenca i pacchetti pronti in LIBRI/libri_pronti/ con il verdetto di pubblicabilita';
  - lancia l'ANALISI NICCHIE, che e' automatica per intero.

Regole rispettate:
- ADR-003 (wrap, mai riscrittura): il lancio passa dalla tile standard kind="py" e usa
  `engine/kdp.py`, il comando unico del workflow. Qui non vive nessuna logica di produzione.
- Route in SOLA LETTURA (come modules/libri.py e modules/youtube.py): leggono file di stato
  gia' su disco, non lanciano processi e non ricalcolano nulla a runtime.
- Nessun numero inventato: se un file manca si dichiara, col percorso atteso.
"""
import json
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
WORKFLOW_DIR = (REPO_ROOT / "company" / "Ecosistemi" / "02-INFO-BUSINESS" / "Workflow"
                / "libri-performanti-multiagente")
LIBRI_DIR = WORKFLOW_DIR / "LIBRI"
IN_LAVORAZIONE = LIBRI_DIR / "in_lavorazione"
PRONTI = LIBRI_DIR / "libri_pronti"
PUBBLICATI = LIBRI_DIR / "libri_pubblicati"
CLI = WORKFLOW_DIR / "engine" / "kdp.py"


def _leggi_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None


def in_lavorazione(payload=None):
    """POST /api/librikdp/lavorazione — a che punto e' ogni libro non ancora finito."""
    if not IN_LAVORAZIONE.exists():
        return {"ok": True, "libri": [], "nota": f"Nessun libro in lavorazione ({IN_LAVORAZIONE})"}

    libri = []
    for cartella in sorted(IN_LAVORAZIONE.iterdir()):
        cfg = _leggi_json(cartella / "progetto.json")
        if not cfg:
            continue
        dir_capitoli = cartella / "capitoli"
        scritti, parole = [], 0
        if dir_capitoli.exists():
            for f in sorted(dir_capitoli.glob("cap_*.md")):
                testo = f.read_text(encoding="utf-8")
                # un file quasi vuoto non conta come capitolo scritto
                if len(testo.split()) >= 50:
                    scritti.append(f.stem)
                    parole += len(testo.split())
        totali = cfg.get("capitoli_totali", 0)
        libri.append({
            "slug": cartella.name,
            "titolo": cfg.get("titolo", cartella.name),
            "nicchia": cfg.get("nicchia", ""),
            "capitoli_scritti": len(scritti),
            "capitoli_totali": totali,
            "parole": parole,
            "pagine_stimate": round(parole / 300, 1),
            "mancanti": max(0, totali - len(scritti)),
        })
    return {"ok": True, "libri": libri}


def pronti(payload=None):
    """POST /api/librikdp/pronti — i pacchetti finiti, col verdetto di pubblicabilita'."""
    if not PRONTI.exists():
        return {"ok": True, "libri": [], "nota": f"Nessun pacchetto pronto ({PRONTI})"}

    libri = []
    for cartella in sorted(PRONTI.iterdir()):
        if not cartella.is_dir():
            continue
        validazione = _leggi_json(cartella / "validazione.json")
        libri.append({
            "cartella": cartella.name,
            "pdf": next((f.name for f in cartella.glob("*.pdf")), None),
            "copertina": next((f.name for f in cartella.glob("Cover_*.png")), None),
            "report": "REPORT.md" if (cartella / "REPORT.md").exists() else None,
            "pubblicabile": validazione.get("pubblicabile") if validazione else "non verificato",
            "bloccanti": validazione.get("bloccanti", []) if validazione else [],
        })
    return {"ok": True, "libri": libri,
            "pubblicati": len(list(PUBBLICATI.iterdir())) if PUBBLICATI.exists() else 0}


def nicchie(payload=None):
    """POST /api/librikdp/nicchie — analizza su Amazon le keyword indicate e le classifica.

    E' l'unica route che LANCIA un processo, ed e' voluto: l'analisi nicchie e' l'unico
    pezzo del flusso completamente automatico. Fa richieste reali ad Amazon, quindi ha un
    timeout esplicito e ritorna l'output cosi' com'e', senza reinterpretarlo."""
    payload = payload or {}
    keywords = [k.strip() for k in (payload.get("keywords") or "").split(",") if k.strip()]
    if not keywords:
        return {"ok": False, "errore": "Serve almeno una keyword, separate da virgola."}
    if not CLI.exists():
        return {"ok": False, "errore": f"Comando non trovato: {CLI}"}

    try:
        esito = subprocess.run(
            [sys.executable, "-m", "engine.kdp", "nicchie", "--keywords", *keywords],
            cwd=str(WORKFLOW_DIR), capture_output=True, text=True, timeout=900,
        )
    except subprocess.TimeoutExpired:
        return {"ok": False, "errore": "Amazon non ha risposto entro 15 minuti."}
    return {"ok": esito.returncode == 0, "exit_code": esito.returncode,
            "output": (esito.stdout or "")[-4000:], "errori": (esito.stderr or "")[-1500:]}


PANEL_HTML = """
<div class="panel">
  <h3>Libri KDP</h3>
  <p class="muted">
    I capitoli li scrive Claude seguendo <code>SOP-SCRIVERE-UN-LIBRO.md</code>: qui vedi a che
    punto sono i libri e lanci l'analisi delle nicchie, che e' automatica.
  </p>

  <button class="btn" onclick="edApi('librikdp/lavorazione',{}).then(r=>{
    document.getElementById('librikdp-out').textContent = JSON.stringify(r, null, 2);
  })">Libri in lavorazione</button>

  <button class="btn" onclick="edApi('librikdp/pronti',{}).then(r=>{
    document.getElementById('librikdp-out').textContent = JSON.stringify(r, null, 2);
  })">Pronti da caricare su KDP</button>

  <div style="margin-top:10px">
    <input id="librikdp-kw" class="inp" style="width:60%"
           placeholder="cozy mystery cats, small town romance" />
    <button class="btn" onclick="
      document.getElementById('librikdp-out').textContent = 'Analizzo su Amazon, puo\\' richiedere qualche minuto...';
      edApi('librikdp/nicchie',{keywords: document.getElementById('librikdp-kw').value}).then(r=>{
        document.getElementById('librikdp-out').textContent = r.output || JSON.stringify(r, null, 2);
      })">Analizza nicchie</button>
  </div>

  <pre id="librikdp-out" class="log-pane">Premi un bottone.</pre>
</div>
"""

# kind="readonly": la tile apre la cartella dei libri pronti invece di lanciare un processo.
# E' la scelta corretta qui — non esiste uno script che "produce un libro" da solo (la
# scrittura passa da Claude in sessione), quindi un kind="py" prometterebbe qualcosa che non
# succede. Le azioni vere stanno nel pannello: stato dei libri e analisi nicchie.
# (I kind validi sono readonly/bat/py/node: al primo tentativo avevo inventato "panel" e il
# selftest di EmpireDesk lo ha giustamente scartato.)
TILE = {
    "id": "librikdp",
    "icon": "\U0001F4D5",
    "name": "Libri KDP",
    "desc": "Stato dei libri, pacchetti pronti da caricare, analisi nicchie su Amazon",
    "kind": "readonly",
    "path": "company/Ecosistemi/02-INFO-BUSINESS/Workflow/libri-performanti-multiagente/LIBRI/libri_pronti",
    "input": None,
}

MODULE = {
    "id": "libri_kdp",
    "tile": TILE,
    "routes": {
        "librikdp/lavorazione": in_lavorazione,
        "librikdp/pronti": pronti,
        "librikdp/nicchie": nicchie,
    },
    "panel_html": PANEL_HTML,
}


def selftest():
    """Verifica che il pannello possa funzionare, SENZA lanciare analisi reali
    (una richiesta ad Amazon durante un selftest non ci sta)."""
    if not WORKFLOW_DIR.exists():
        return False, f"libri_kdp: workflow non trovato ({WORKFLOW_DIR})"
    if not CLI.exists():
        return False, f"libri_kdp: comando kdp.py non trovato ({CLI})"
    lav = in_lavorazione()
    pro = pronti()
    if not lav.get("ok") or not pro.get("ok"):
        return False, "libri_kdp: le route di lettura non rispondono"
    return True, (f"libri_kdp: {len(lav['libri'])} in lavorazione, "
                  f"{len(pro['libri'])} pronti da caricare")
