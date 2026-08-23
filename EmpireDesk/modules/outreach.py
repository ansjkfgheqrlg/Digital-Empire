# -*- coding: utf-8 -*-
"""
modules/outreach.py — il pulsante di avvio dell'OUTREACH dentro Aureus (piano V2, checkpoint V8).

Richiesta esplicita di Gael: nella sezione automazioni, accanto agli altri tool, deve esserci
anche il tasto di avvio di outreach.

Cosa fa la tile: lancia `Outreach/preventa-maps-scraper/02-AUTOMAZIONI-E-SCRIPTS/run.py`,
il runner reale gia' in produzione (scraping Google Maps -> qualifica -> push su Areus).

Regole rispettate:
- ADR-003 (wrap, mai riscrittura): nessuna logica di outreach vive qui. Il runner e' l'unica
  implementazione; questo modulo lo lancia e ne legge i risultati.
- Route in SOLA LETTURA: leggono i CSV gia' scritti su disco, non lanciano processi e non
  ricalcolano niente a runtime.
- Nessun numero inventato: se un file manca si dichiara, col percorso atteso.

NOTA sul lancio: il runner apre un browser REALE su Google Maps e fa richieste vere. Non e'
un'operazione gratuita ne' istantanea (minuti, non secondi), e per questo la tile parte senza
parametri con i default del runner: chi vuole citta'/categorie specifiche le passa da riga di
comando, dove ha il controllo completo.
"""
import csv
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
OUTREACH_DIR = REPO_ROOT / "Outreach" / "preventa-maps-scraper"
SCRIPTS_DIR = OUTREACH_DIR / "02-AUTOMAZIONI-E-SCRIPTS"
RUNNER = SCRIPTS_DIR / "run.py"
DATA_DIR = SCRIPTS_DIR / "data"


def _csv_piu_recente() -> Path | None:
    if not DATA_DIR.exists():
        return None
    csvs = sorted(DATA_DIR.glob("*.csv"), key=lambda p: p.stat().st_mtime, reverse=True)
    return csvs[0] if csvs else None


def ultimi_lead(payload=None):
    """POST /api/outreach/lead — i lead dell'ultimo giro, letti dal CSV gia' su disco."""
    percorso = _csv_piu_recente()
    if percorso is None:
        return {"ok": True, "lead": [], "nota": f"Nessun CSV di lead ancora prodotto ({DATA_DIR})"}

    try:
        with percorso.open(encoding="utf-8", newline="") as f:
            righe = list(csv.DictReader(f))
    except OSError as e:
        return {"ok": False, "errore": f"CSV illeggibile ({percorso.name}): {e}"}

    def priorita(r):
        for chiave in ("priorita", "priorità", "priority"):
            if r.get(chiave):
                return str(r[chiave]).strip().upper()
        return ""

    alta = [r for r in righe if priorita(r) == "ALTA"]
    return {
        "ok": True,
        "file": percorso.name,
        "aggiornato": datetime.fromtimestamp(percorso.stat().st_mtime).strftime("%d/%m/%Y %H:%M"),
        "totale": len(righe),
        "priorita_alta": len(alta),
        "anteprima": [
            {k: v for k, v in r.items() if k in ("nome_attivita", "nome", "citta", "telefono",
                                                  "sito", "priorita", "priorità")}
            for r in righe[:10]
        ],
    }


def storico(payload=None):
    """POST /api/outreach/storico — i giri fatti finora, dal piu' recente."""
    if not DATA_DIR.exists():
        return {"ok": True, "giri": [], "nota": f"Cartella dati assente ({DATA_DIR})"}
    giri = []
    for p in sorted(DATA_DIR.glob("*.csv"), key=lambda x: x.stat().st_mtime, reverse=True)[:15]:
        try:
            with p.open(encoding="utf-8", newline="") as f:
                n = sum(1 for _ in csv.DictReader(f))
        except OSError:
            n = None
        giri.append({
            "file": p.name,
            "lead": n,
            "quando": datetime.fromtimestamp(p.stat().st_mtime).strftime("%d/%m/%Y %H:%M"),
            "kb": round(p.stat().st_size / 1024, 1),
        })
    return {"ok": True, "giri": giri}


PANEL_HTML = """
<div class="panel">
  <h3>Outreach</h3>
  <p class="muted">
    Il pulsante <b>Avvia</b> della tile lancia il giro reale: apre un browser su Google Maps,
    raccoglie i lead, li qualifica e li spinge su Areus. Richiede minuti, non secondi.
  </p>

  <button class="btn" onclick="edApi('outreach/lead',{}).then(r=>{
    document.getElementById('outreach-out').textContent = JSON.stringify(r, null, 2);
  })">Lead dell'ultimo giro</button>

  <button class="btn" onclick="edApi('outreach/storico',{}).then(r=>{
    document.getElementById('outreach-out').textContent = JSON.stringify(r, null, 2);
  })">Storico dei giri</button>

  <pre id="outreach-out" class="log-pane">Premi un bottone.</pre>
</div>
"""

TILE = {
    "id": "outreach",
    "icon": "\U0001F4DE",
    "name": "Outreach",
    "desc": "Giro reale su Google Maps: raccolta lead, qualifica e push su Areus (minuti, browser reale)",
    "kind": "py",
    "script": "Outreach/preventa-maps-scraper/02-AUTOMAZIONI-E-SCRIPTS/run.py",
    "cwd": "Outreach/preventa-maps-scraper/02-AUTOMAZIONI-E-SCRIPTS",
    "input": None,
}

MODULE = {
    "id": "outreach",
    "tile": TILE,
    "routes": {
        "outreach/lead": ultimi_lead,
        "outreach/storico": storico,
    },
    "panel_html": PANEL_HTML,
}


def selftest():
    """Verifica che il pulsante sia LANCIABILE, senza lanciarlo (un selftest non deve
    aprire un browser su Google Maps ne' scrivere su Areus)."""
    if not RUNNER.exists():
        return False, f"outreach: runner non trovato ({RUNNER})"
    mancanti = [p.name for p in (SCRIPTS_DIR / "agents.py", SCRIPTS_DIR / "browser.py",
                                  SCRIPTS_DIR / "checker.py") if not p.exists()]
    if mancanti:
        return False, f"outreach: pezzi della catena mancanti: {', '.join(mancanti)}"
    esito = ultimi_lead()
    if not esito.get("ok"):
        return False, f"outreach: route di lettura in errore ({esito.get('errore')})"
    n = esito.get("totale")
    return True, ("outreach: runner presente, "
                  + (f"ultimo giro {esito.get('file')} con {n} lead"
                     if n is not None else "nessun giro ancora eseguito"))
