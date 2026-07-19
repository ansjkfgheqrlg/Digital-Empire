# -*- coding: utf-8 -*-
"""
A2 — modules/revenue.py (Half A, owner: Max — contratto dossier 17 §5.3)
Pannello revenue: pipeline S1 (7 concessionari) da EmpireDesk/state/revenue.json.
Fonte compilata da Max. Dato assente -> dichiarato. Nessun numero inventato (Mandato Art.2).
"""
import json
import time
from pathlib import Path

STATE = Path(__file__).resolve().parents[1] / "state" / "revenue.json"

STATI_VALIDI = ["da_contattare", "contattato", "demo_fatta", "anticipo_promesso", "incassato", "perso"]


def _load() -> dict:
    if not STATE.exists():
        return {"errore": "nessun dato: manca state/revenue.json", "fonte": str(STATE)}
    try:
        return json.loads(STATE.read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        return {"errore": f"revenue.json illeggibile: {e}", "fonte": str(STATE)}


def pipeline(payload=None):
    """POST /api/revenue/pipeline — stato pipeline S1 senza inventare nulla."""
    data = _load()
    if "errore" in data:
        return data
    conc = data.get("concessionari", [])
    per_stato = {s: [c["id"] for c in conc if c.get("stato") == s] for s in STATI_VALIDI}
    da_compilare = [c["id"] for c in conc if c.get("nome") == "da_compilare"]
    incassi = data.get("incassi", [])
    tot = sum(i.get("importo", 0) for i in incassi if isinstance(i.get("importo"), (int, float)))
    return {
        "generato": time.strftime("%Y-%m-%d %H:%M"),
        "aggiornato_da_max": data.get("aggiornato", "mai"),
        "totale_pipeline": len(conc),
        "slot_da_compilare": da_compilare,
        "per_stato": per_stato,
        "incassi_registrati": len(incassi),
        "totale_incassato": tot if incassi else "nessun dato",
        "fonte": str(STATE),
    }


def aggiorna(payload=None):
    """POST /api/revenue/aggiorna — {id, campo, valore}: aggiorna UNO slot (scrittura esplicita di Max)."""
    p = payload or {}
    cid, campo, valore = p.get("id"), p.get("campo"), p.get("valore")
    if not (cid and campo is not None):
        return {"errore": "servono 'id' e 'campo' (+ 'valore')"}
    if campo == "stato" and valore not in STATI_VALIDI:
        return {"errore": f"stato non valido: {valore}. Validi: {STATI_VALIDI}"}
    data = _load()
    if "errore" in data:
        return data
    for c in data.get("concessionari", []):
        if c.get("id") == cid:
            c[campo] = valore
            data["aggiornato"] = time.strftime("%Y-%m-%d")
            STATE.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
            return {"ok": True, "id": cid, campo: valore}
    return {"errore": f"id '{cid}' non trovato"}


PANEL_HTML = """
<div id="panel-revenue" class="panel">
  <h2>💰 Pipeline S1 — 7 Concessionari</h2>
  <p class="hint">Fonte: state/revenue.json (compila Max). Stati: da_contattare → contattato → demo_fatta → anticipo_promesso → incassato.</p>
  <button class="btn" onclick="edApi('revenue/pipeline',{}).then(r=>{
    document.getElementById('revenue-out').textContent = JSON.stringify(r, null, 2);
  })">Aggiorna</button>
  <pre id="revenue-out" class="log-pane">Premi Aggiorna.</pre>
</div>
"""

MODULE = {
    "id": "revenue",
    "tile": None,
    "routes": {"revenue/pipeline": pipeline, "revenue/aggiorna": aggiorna},
    "panel_html": PANEL_HTML,
}


def selftest():
    """Solo probe: file presente e JSON valido. Nessun lancio."""
    if not STATE.exists():
        return False, f"revenue: manca {STATE}"
    try:
        json.loads(STATE.read_text(encoding="utf-8"))
        return True, "revenue: state/revenue.json presente e valido"
    except (OSError, ValueError) as e:
        return False, f"revenue: JSON invalido — {e}"
