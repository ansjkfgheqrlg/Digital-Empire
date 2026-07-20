# -*- coding: utf-8 -*-
"""
A1 — modules/metrics.py (Half A, owner: Max — contratto dossier 17 §5.3)
Dashboard metriche settimana (dossier 16 §4) da DATI REALI.
Regola vincolante: dato assente -> "nessun dato". MAI numeri inventati (Mandato Art.2).
Solo lettura: questo modulo non lancia MAI processi.
"""
import json
import time
from pathlib import Path

# EmpireDesk/modules/metrics.py -> repo root = parents[2]
REPO_ROOT = Path(__file__).resolve().parents[2]

# Fonti REALI (probe a runtime; ognuna può mancare — si dichiara, non si inventa)
SOURCES = {
    "linkedin_run_log": REPO_ROOT / "Outreach" / "LinkedIn Automation" / "run_today_log.txt",
    "linkedin_comments": REPO_ROOT / "Outreach" / "LinkedIn Automation" / "comments_log.txt",
    "email_workflow_dir": REPO_ROOT / "Outreach" / "Outreach Workflow",
    "caroselli_factory": REPO_ROOT / "Workfolw crea caroselli à" / "carousel-factory",
    "clienti_dir": REPO_ROOT / "Clienti",
    "revenue_state": Path(__file__).resolve().parents[1] / "state" / "revenue.json",
}


def _count_lines_today(path: Path) -> dict:
    if not path.exists():
        return {"stato": "nessun dato", "fonte": str(path)}
    today = time.strftime("%Y-%m-%d")
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
        righe = text.splitlines()
        oggi = [r for r in righe if today in r]
        return {"stato": "ok", "righe_totali": len(righe), "righe_oggi": len(oggi), "fonte": str(path)}
    except OSError as e:
        return {"stato": f"errore lettura: {e}", "fonte": str(path)}


def _count_ready_emails(dirpath: Path) -> dict:
    if not dirpath.exists():
        return {"stato": "nessun dato", "fonte": str(dirpath)}
    ready = sorted(set(dirpath.glob("emails_*_ready.json")) | set(dirpath.glob("emails_ready.json")))
    tot = 0
    for f in ready:
        try:
            data = json.loads(f.read_text(encoding="utf-8", errors="replace"))
            tot += len(data) if isinstance(data, list) else 1
        except (OSError, ValueError):
            pass  # file corrotto: non conto nulla, non invento
    return {"stato": "ok" if ready else "nessun file ready",
            "file_ready": len(ready), "email_in_coda": tot, "fonte": str(dirpath)}


def _count_pdf_preventivi(dirpath: Path) -> dict:
    if not dirpath.exists():
        return {"stato": "nessun dato", "fonte": str(dirpath)}
    try:
        pdfs = list(dirpath.rglob("*.pdf"))
        week_ago = time.time() - 7 * 86400
        recenti = [p for p in pdfs if p.stat().st_mtime >= week_ago]
        return {"stato": "ok", "pdf_totali": len(pdfs), "pdf_ultimi_7gg": len(recenti), "fonte": str(dirpath)}
    except OSError as e:
        return {"stato": f"errore lettura: {e}", "fonte": str(dirpath)}


def _caroselli(dirpath: Path) -> dict:
    if not dirpath.exists():
        return {"stato": "nessun dato", "fonte": str(dirpath)}
    out = dirpath / "output"
    if not out.exists():
        return {"stato": "cartella output assente", "fonte": str(out)}
    try:
        png = list(out.rglob("*.png"))
        week_ago = time.time() - 7 * 86400
        recenti = [p for p in png if p.stat().st_mtime >= week_ago]
        return {"stato": "ok", "png_totali": len(png), "png_ultimi_7gg": len(recenti), "fonte": str(out)}
    except OSError as e:
        return {"stato": f"errore lettura: {e}", "fonte": str(dirpath)}


def summary(payload=None):
    """POST /api/metrics/summary — metriche dossier 16 §4, solo da fonti reali."""
    rev = {"stato": "nessun dato", "fonte": str(SOURCES["revenue_state"])}
    if SOURCES["revenue_state"].exists():
        try:
            data = json.loads(SOURCES["revenue_state"].read_text(encoding="utf-8"))
            chiusi = [c for c in data.get("concessionari", []) if c.get("stato") == "incassato"]
            rev = {"stato": "ok", "anticipi_incassati": len(chiusi),
                   "pipeline_totale": len(data.get("concessionari", [])),
                   "fonte": str(SOURCES["revenue_state"])}
        except (OSError, ValueError) as e:
            rev = {"stato": f"errore lettura: {e}", "fonte": str(SOURCES["revenue_state"])}
    return {
        "generato": time.strftime("%Y-%m-%d %H:%M"),
        "nota": "Solo dati reali (Mandato Art.2). 'nessun dato' = fonte assente, non zero.",
        "outreach_linkedin": _count_lines_today(SOURCES["linkedin_run_log"]),
        "outreach_commenti": _count_lines_today(SOURCES["linkedin_comments"]),
        "outreach_email": _count_ready_emails(SOURCES["email_workflow_dir"]),
        "caroselli": _caroselli(SOURCES["caroselli_factory"]),
        "preventivi": _count_pdf_preventivi(SOURCES["clienti_dir"]),
        "revenue": rev,
    }


PANEL_HTML = """
<div id="panel-metrics" class="panel">
  <h2>📈 Metriche Settimana</h2>
  <p class="hint">Dossier 16 §4 — solo dati reali. «nessun dato» = fonte assente, mai zero inventato.</p>
  <button class="btn" onclick="edApi('metrics/summary',{}).then(r=>{
    document.getElementById('metrics-out').textContent = JSON.stringify(r, null, 2);
  })">Aggiorna</button>
  <pre id="metrics-out" class="log-pane">Premi Aggiorna.</pre>
</div>
"""

MODULE = {
    "id": "metrics",
    "tile": None,  # niente tile nel grid: è un pannello (zero bottoni finti)
    "routes": {"metrics/summary": summary},
    "panel_html": PANEL_HTML,
}


def selftest():
    """Verifica fonti SENZA lanciare nulla. Verde se il probe funziona (assenze dichiarate, non errori)."""
    presenti = [k for k, p in SOURCES.items() if p.exists()]
    return True, f"metrics: {len(presenti)}/{len(SOURCES)} fonti presenti ({', '.join(presenti) or 'nessuna'})"
