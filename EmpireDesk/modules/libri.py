# -*- coding: utf-8 -*-
"""
modules/libri.py — Blueprint "Libri Performanti" (workflow multi-agente KDP) dentro Aureus.
Importato da zip workspace-019fc6f4 (2026-08-03), salvato in company/Ecosistemi/
02-INFO-BUSINESS/Workflow/libri-performanti-multiagente/.

Regole vincolanti:
- Solo lettura + calcolo puro (come modules/youtube.py): questo modulo non lancia processi
  né tocca la rete.
- `workflow_architecture/main.py` e `orchestrator_assembly.py` (consegnati nello zip)
  referenziano `agents/all_agents.py` e `agents/senior_and_operational.py`, file che NON
  esistono nella consegna (la struttura reale usa L1/, L2/*.py, L3/all_L3_leaders_aggregated.py,
  L4/all_L4_senior_aggregated.py + agenti singoli sotto teams/*/*.py) — NON sono eseguibili
  as-is. Finché nessuno li corregge, questo modulo espone SOLO il manifest dichiarato dal
  blueprint stesso (architecture_manifest.json), mai un ricalcolo (Mandato Art.2: mai numeri
  inventati, "nessun dato" se manca).
"""
import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
BLUEPRINT_DIR = (REPO_ROOT / "company" / "Ecosistemi" / "02-INFO-BUSINESS" / "Workflow"
                  / "libri-performanti-multiagente")
MANIFEST_PATH = BLUEPRINT_DIR / "workflow_architecture" / "architecture_manifest.json"
MAIN_PY = BLUEPRINT_DIR / "workflow_architecture" / "main.py"
MISSING_REFS = [
    BLUEPRINT_DIR / "workflow_architecture" / "agents" / "all_agents.py",
    BLUEPRINT_DIR / "workflow_architecture" / "agents" / "senior_and_operational.py",
]


def manifest(payload=None):
    """POST /api/libri/manifest — manifest dichiarato dal blueprint (letto, non ricalcolato)."""
    if not MANIFEST_PATH.exists():
        return {"stato": "nessun dato", "nota": "architecture_manifest.json non trovato",
                "fonte": str(MANIFEST_PATH)}
    try:
        data = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        return {"stato": f"errore lettura: {e}", "fonte": str(MANIFEST_PATH)}
    ancora_mancanti = [str(p.relative_to(BLUEPRINT_DIR)) for p in MISSING_REFS if not p.exists()]
    data["stato"] = "ok"
    data["nota"] = ("manifest dichiarato dal blueprint originale, non validato a runtime — "
                     "main.py/orchestrator_assembly.py NON eseguibili as-is")
    data["file_referenziati_mancanti"] = ancora_mancanti
    return data


PANEL_HTML = """
<div id="panel-libri" class="panel">
  <h2>\U0001F4DA Libri Performanti — blueprint multi-agente</h2>
  <p class="hint">Architettura KDP importata il 2026-08-03 (104 agenti dichiarati, 7 livelli).
  Non ancora eseguibile: gli entrypoint originali referenziano file mancanti nella consegna.</p>
  <button class="btn" onclick="edApi('libri/manifest',{}).then(r=>{
    document.getElementById('libri-out').textContent = JSON.stringify(r, null, 2);
  })">Leggi manifest dichiarato</button>
  <pre id="libri-out" class="log-pane">Premi Leggi manifest dichiarato.</pre>
</div>
"""

TILE = {
    "id": "libri", "icon": "\U0001F4DA", "name": "Libri Performanti (blueprint)",
    "desc": "Architettura multi-agente KDP — blueprint, main.py non ancora eseguibile",
    "kind": "readonly",
    "path": "company/Ecosistemi/02-INFO-BUSINESS/Workflow/libri-performanti-multiagente/ARCHITETTURA_COMPLETA_FINALE.md",
}

MODULE = {
    "id": "libri",
    "tile": TILE,
    "routes": {"libri/manifest": manifest},
    "panel_html": PANEL_HTML,
}


def selftest():
    """Probe: file chiave presenti + segnala esplicitamente i riferimenti rotti di main.py."""
    if not BLUEPRINT_DIR.is_dir():
        return False, f"libri: cartella blueprint non trovata ({BLUEPRINT_DIR})"
    missing = []
    if not MANIFEST_PATH.exists():
        missing.append("architecture_manifest.json")
    if not MAIN_PY.exists():
        missing.append("main.py")
    if missing:
        return False, f"libri: file mancanti ({', '.join(missing)})"
    ancora_mancanti = [str(p.relative_to(BLUEPRINT_DIR)) for p in MISSING_REFS if not p.exists()]
    if ancora_mancanti:
        return True, (f"libri: blueprint presente ma main.py non eseguibile — "
                       f"riferimenti mancanti: {', '.join(ancora_mancanti)}")
    return True, "libri: blueprint presente, main.py referenzia file tutti esistenti"
