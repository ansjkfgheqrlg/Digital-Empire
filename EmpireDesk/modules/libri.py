# -*- coding: utf-8 -*-
"""
modules/libri.py — Blueprint "Libri Performanti" (workflow multi-agente KDP) dentro Aureus.
Importato da zip workspace-019fc6f4 (2026-08-03), salvato in company/Ecosistemi/
02-INFO-BUSINESS/Workflow/libri-performanti-multiagente/.

Lo zip conteneva 4 varianti dell'architettura. Solo UNA è auto-consistente ed è stata
VERIFICATA con un'esecuzione reale (`python assembly_finale.py`, exit code 0, manifest
rigenerato identico al precedente — deterministico):
- `architettura_completa_7_livelli/` — 95 agenti reali, 26 team, 18 skill, 38 memory
  component, 5 flow, 9 ecosistemi. Entrypoint: `Orchestrator/assembly_finale.py` (fix
  applicato: path hardcoded `/home/user/...` reso relativo a `__file__`, nessuna modifica
  di logica). Playwright confermato simulato (nessuna chiamata di rete).
- `workflow_architecture/` (variante originariamente importata) — dichiara 104 agenti ma
  `main.py`/`orchestrator_assembly.py` referenziano file inesistenti (`agents/all_agents.py`),
  e i file `L1/`/`L2/` dipendono da un `Agent` incompatibile importato da un'ALTRA cartella
  dello zip (`architettura_sincrona/core.py`, campi diversi). NON eseguibile, lasciata
  intatta come riferimento storico.
I due numeri (95 vs 104) NON sono lo stesso conteggio validato — sono due varianti diverse
consegnate nello stesso zip. Qui si espone solo quello verificato.

Regole vincolanti:
- Le route restano sola lettura + calcolo puro (come modules/youtube.py): leggono il
  manifest già scritto su disco, non lo ricalcolano MAI a runtime (Mandato Art.2).
- Il lancio reale (rigenerazione manifest) passa dalla tile standard kind="py" di
  EmpireDesk (subprocess wrapper, ADR-003) — nessuna logica di lancio duplicata qui.
"""
import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
BLUEPRINT_DIR = (REPO_ROOT / "company" / "Ecosistemi" / "02-INFO-BUSINESS" / "Workflow"
                  / "libri-performanti-multiagente")
# PIANO-KDP-67 CP11 (2026-08-05): le varianti narrative (compresa questa) sono state
# archiviate in _archivio_blueprint_narrativo/ — sostituite dal motore reale in engine/
# (vedi modulo Aureus dedicato modules/libri_kdp.py, CP10). Path aggiornato di conseguenza,
# questa tile resta solo per rileggere/rilanciare la validazione strutturale storica.
VERIFIED_DIR = BLUEPRINT_DIR / "_archivio_blueprint_narrativo" / "architettura_completa_7_livelli"
MANIFEST_PATH = VERIFIED_DIR / "Orchestrator" / "manifest_finale_completo.json"
ENTRYPOINT = VERIFIED_DIR / "Orchestrator" / "assembly_finale.py"


def manifest(payload=None):
    """POST /api/libri/manifest — manifest della variante VERIFICATA (letto, non ricalcolato).
    Premi la tile per rigenerarlo davvero (lancia assembly_finale.py, sempre deterministico)."""
    if not MANIFEST_PATH.exists():
        return {"stato": "nessun dato", "nota": "manifest_finale_completo.json non trovato — lancia la tile per generarlo",
                "fonte": str(MANIFEST_PATH)}
    try:
        data = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        return {"stato": f"errore lettura: {e}", "fonte": str(MANIFEST_PATH)}
    data["stato"] = "ok"
    data["nota"] = ("variante verificata (architettura_completa_7_livelli) — eseguita realmente, "
                     "exit code 0, output deterministico. workflow_architecture/ (104 agenti dichiarati) "
                     "resta non eseguibile, non è questo il numero validato.")
    return data


PANEL_HTML = """
<div id="panel-libri" class="panel">
  <h2>\U0001F4DA Libri Performanti — blueprint multi-agente (verificato)</h2>
  <p class="hint">Architettura KDP importata il 2026-08-03. Variante eseguibile verificata:
  95 agenti reali, 26 team, 9 ecosistemi. Premi la tile per rilanciarla davvero.</p>
  <button class="btn" onclick="edApi('libri/manifest',{}).then(r=>{
    document.getElementById('libri-out').textContent = JSON.stringify(r, null, 2);
  })">Leggi ultimo manifest generato</button>
  <pre id="libri-out" class="log-pane">Premi Leggi ultimo manifest generato.</pre>
</div>
"""

TILE = {
    "id": "libri", "icon": "\U0001F4DA", "name": "Libri Performanti (assembly)",
    "desc": "Rigenera l'architettura multi-agente KDP verificata (95 agenti, 26 team, 9 ecosistemi)",
    "kind": "py",
    "script": str((ENTRYPOINT.relative_to(REPO_ROOT))).replace("\\", "/"),
    "cwd": str((ENTRYPOINT.parent.relative_to(REPO_ROOT))).replace("\\", "/"),
    "input": None,
}

MODULE = {
    "id": "libri",
    "tile": TILE,
    "routes": {"libri/manifest": manifest},
    "panel_html": PANEL_HTML,
}


def selftest():
    """Probe: verifica che la variante VERIFICATA sia lanciabile (file presenti, mai eseguita qui)."""
    if not ENTRYPOINT.exists():
        return False, f"libri: entrypoint verificato non trovato ({ENTRYPOINT})"
    core = VERIFIED_DIR / "core.py"
    if not core.exists():
        return False, f"libri: core.py mancante in architettura_completa_7_livelli ({core})"
    nota_manifest = "manifest presente" if MANIFEST_PATH.exists() else "manifest assente (mai lanciato)"
    return True, f"libri: assembly_finale.py presente e lanciabile, {nota_manifest}"
