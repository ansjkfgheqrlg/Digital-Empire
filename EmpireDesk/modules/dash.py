# -*- coding: utf-8 -*-
"""
A2 — modules/dash.py (Half A, owner: Max — contratto dossier 17 §5.3)
Modulo di integrazione per la Dashboard Aziendale (GEM-05).
"""
import json
import time
import sys
from pathlib import Path
REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from empire.dash.collect import collect_all


def summary(payload=None):
    """POST /api/dash/summary — ritorna lo stato dei KPI e dei gate dal collettore."""
    try:
        data = collect_all()
        return {
            "stato": "ok",
            "generato": time.strftime("%Y-%m-%d %H:%M:%S"),
            "data": data
        }
    except Exception as e:
        return {
            "stato": "errore",
            "errore": str(e)
        }


PANEL_HTML = """
<div id="panel-dash" class="panel">
  <h2>📊 Cruscotto di Conformità (GEM-05)</h2>
  <p class="hint">Visualizza le metriche live calcolate sul monorepo e lo stato dei 6 gate.</p>
  <button class="btn" onclick="edApi('dash/summary',{}).then(r=>{
    document.getElementById('dash-out').textContent = JSON.stringify(r, null, 2);
  })">Aggiorna KPI Live</button>
  <pre id="dash-out" class="log-pane">Premi Aggiorna KPI Live.</pre>
</div>
"""

TILE = {
    "id": "dash_tile",
    "icon": "📊",
    "name": "Dashboard KPI",
    "desc": "Visualizza la dashboard di conformità aziendale (GEM-05)",
    "kind": "readonly",
    "path": "WORKFLOW-ESTATE/06-DASHBOARD-E-METRICHE/DASHBOARD.md"
}

MODULE = {
    "id": "dash",
    "tile": TILE,
    "routes": {"dash/summary": summary},
    "panel_html": PANEL_HTML,
}


def selftest():
    """Verifica la presenza fisica dei file chiave del modulo."""
    lead_file = REPO_ROOT / "WORKFLOW-ESTATE" / "06-DASHBOARD-E-METRICHE" / "lead.csv"
    dash_md = REPO_ROOT / "WORKFLOW-ESTATE" / "06-DASHBOARD-E-METRICHE" / "DASHBOARD.md"
    
    missing = []
    if not lead_file.exists():
        missing.append("lead.csv")
    if not dash_md.exists():
        missing.append("DASHBOARD.md")
        
    if missing:
        return False, f"dash: file mancanti ({', '.join(missing)})"
    return True, "dash: lead.csv e DASHBOARD.md presenti"
