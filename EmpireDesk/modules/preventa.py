# -*- coding: utf-8 -*-
"""
Preventa — Outreach Freddo (Half B, owner: Gael — contratto dossier 17 §5.3).

Serve alla UI Areus i lead che `Outreach/preventa-maps-scraper` scrive in
`state/preventa_leads.json` (via `02-AUTOMAZIONI-E-SCRIPTS/areus.py`). Sostituisce Google
Sheets: nessuna credenziale esterna, stesso file letto/scritto da entrambe le parti.
Stage usa lo stesso enum LeadStage di `platform/types.ts` (NEW/CONTACTED/...).
"""
import json
import time
from pathlib import Path

STATE = Path(__file__).resolve().parents[1] / "state" / "preventa_leads.json"
STAGES_VALIDI = ["NEW", "CONTACTED", "PROPOSAL", "NEGOTIATION", "CLOSED_WON", "CLOSED_LOST"]


def _load() -> dict:
    if not STATE.exists():
        return {"leads": [], "aggiornato": None}
    try:
        return json.loads(STATE.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {"leads": [], "errore": f"{STATE} illeggibile"}


def _save(data: dict) -> None:
    STATE.parent.mkdir(parents=True, exist_ok=True)
    data["aggiornato"] = time.strftime("%Y-%m-%d %H:%M")
    STATE.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def elenco(payload=None):
    """POST /api/preventa/elenco — tutti i lead scraper, con conteggi per stage."""
    data = _load()
    leads = data.get("leads", [])
    conteggi = {}
    for l in leads:
        s = l.get("stage", "NEW")
        conteggi[s] = conteggi.get(s, 0) + 1
    return {"leads": leads, "conteggi": conteggi, "aggiornato": data.get("aggiornato")}


def aggiorna_stage(payload=None):
    """POST /api/preventa/aggiorna_stage — {telefono, stage, note?}: sposta un lead di stage."""
    p = payload or {}
    telefono, stage = (p.get("telefono") or "").strip(), p.get("stage")
    if not telefono or stage not in STAGES_VALIDI:
        return {"errore": f"servono 'telefono' e 'stage' valido ({STAGES_VALIDI})"}
    data = _load()
    trovato = False
    for l in data.get("leads", []):
        if (l.get("telefono") or "").strip() == telefono:
            l["stage"] = stage
            if "note" in p:
                l["note"] = p["note"]
            trovato = True
    if not trovato:
        return {"errore": f"lead con telefono '{telefono}' non trovato"}
    _save(data)
    return {"ok": True, "telefono": telefono, "stage": stage}


PANEL_HTML = """
<div id="panel-preventa" class="panel">
  <h2>&#128663; Preventa — Outreach Freddo</h2>
  <p class="hint">Lead reali dallo scraper Google Maps concessionari. Stage: NEW (freddo) -> CONTACTED -> PROPOSAL -> NEGOTIATION -> CLOSED_WON/CLOSED_LOST.</p>
  <div id="pv-stats" style="margin-bottom:10px"></div>
  <div id="pv-list"></div>
</div>
<script>
  function pvSetStage(tel, stage){ edApi('preventa/aggiorna_stage', {telefono: tel, stage: stage}).then(pvRender); }
  function pvRender(){
    edApi('preventa/elenco', {}).then(function(r){
      var statsEl = document.getElementById('pv-stats');
      var c = r.conteggi || {};
      statsEl.innerHTML = Object.keys(c).map(function(k){ return '<b>' + k + '</b>: ' + c[k]; }).join(' &middot; ') || 'Nessun lead ancora.';
      var el = document.getElementById('pv-list');
      var leads = r.leads || [];
      var html = '';
      leads.forEach(function(l){
        html += '<div class="row" style="margin-bottom:5px">' +
          '<span style="min-width:70px;font-size:11px;text-transform:uppercase">' + (l.priorita_lead||'') + '</span>' +
          '<span style="flex:1">' + l.nome_attivita + ' — ' + (l.telefono||'') + ' (' + (l.citta_ricerca||'') + ')</span>' +
          '<select onchange="pvSetStage(\\'' + l.telefono + '\\', this.value)" class="inp" style="max-width:140px">' +
          ['NEW','CONTACTED','PROPOSAL','NEGOTIATION','CLOSED_WON','CLOSED_LOST'].map(function(s){
            return '<option value="' + s + '"' + (s === l.stage ? ' selected' : '') + '>' + s + '</option>';
          }).join('') + '</select>' +
          '</div>';
      });
      el.innerHTML = html || '<p class="hint">Lancia lo scraper in preventa-maps-scraper per popolare questa lista.</p>';
    });
  }
  pvRender();
</script>
"""

MODULE = {
    "id": "preventa",
    "tile": None,
    "routes": {
        "preventa/elenco": elenco,
        "preventa/aggiorna_stage": aggiorna_stage,
    },
    "panel_html": PANEL_HTML,
}


def selftest():
    """Probe: state leggibile/scrivibile. NESSUN lancio reale."""
    try:
        data = _load()
        n = len(data.get("leads", []))
        return True, f"preventa: {n} lead ({STATE})"
    except OSError as exc:
        return False, f"preventa: state non scrivibile — {exc}"
