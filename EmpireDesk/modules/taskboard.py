# -*- coding: utf-8 -*-
"""
B4 — modules/taskboard.py (Half B, owner: Gael — contratto dossier 17 §5.3).

Task board Max/Gael live. Fonte: EmpireDesk/state/taskboard.json. Seed iniziale = i task REALI
della settimana da PIANO-MAESTRO/16-PIANO-ESTATE-REVENUE.md (Mandato Art.2: mai inventare task
o stati — il seed è testuale dal dossier, lo stato parte neutro "da_fare" perché il dossier
descrive un piano, non uno stato di avanzamento verificato riga per riga).
"""
import json
import time
from pathlib import Path

STATE = Path(__file__).resolve().parents[1] / "state" / "taskboard.json"
STATI_VALIDI = ["da_fare", "in_corso", "fatto", "bloccato"]

_id_counter = 0  # per id univoci anche entro lo stesso secondo


def _new_id() -> str:
    """Id univoco anche a più aggiunte nello stesso secondo (stesso bug di scheduler)."""
    global _id_counter
    _id_counter += 1
    return f"tb-{int(time.time())}-{_id_counter}"

# Seed dal dossier 16 (PIANO ESTATE REVENUE) — testo copiato dal dossier, non inventato.
_SEED_TASKS = [
    # --- MAX ---
    {"owner": "Max", "giorno": "G1 (sab 19-20)", "titolo": "Decidere PREZZO Manuale con team-prezzi (chiude B-003, bloccante S2/S3/S4)"},
    {"owner": "Max", "giorno": "G1-G2", "titolo": "Lista 7 concessionari: nome, stato relazione, canale contatto preferito"},
    {"owner": "Max", "giorno": "G2 (lun 21)", "titolo": 'Rivedere+approvare offerta "Partenza Anticipata" preparata da Claude/A5'},
    {"owner": "Max", "giorno": "G2-G4", "titolo": "Contattare i 7 concessionari (call/whatsapp, script A8 in mano)"},
    {"owner": "Max", "giorno": "G3", "titolo": "Approvare landing+prezzo funnel Manuale (review 10 minuti, non costruire)"},
    {"owner": "Max", "giorno": "G4-G5", "titolo": "Decidere nicchia canale YouTube #1 (proposta analisi competitor di Gael)"},
    {"owner": "Max", "giorno": "G6-G7", "titolo": "Push vendita Manuale sui canali personali caldi (post, storie, contatti diretti)"},
    {"owner": "Max", "giorno": "G2", "titolo": "Scegliere il NOME nuovo di PreventivoForge dalla shortlist S6"},
    {"owner": "Max", "giorno": "G5", "titolo": "Approvare promo-kit (landing+demo+case study) preparato da Gael/Claude"},
    # --- GAEL ---
    {"owner": "Gael", "giorno": "G1", "titolo": "(30min) Chiudere CF-R8 -> 03-CONTENT-FACTORY 9/9"},
    {"owner": "Gael", "giorno": "G1", "titolo": "AUDIT ASSET P0.2: censire tutte le pagine (mentalita.brutale, crea.illtuo_impero, altre pagine lancio, sito)"},
    {"owner": "Gael", "giorno": "G2", "titolo": "Funnel Manuale: landing empire-premium-style + checkout + 3 email"},
    {"owner": "Gael", "giorno": "G2-G3", "titolo": "Batch riattivazione S3: 7 caroselli crea.illtuo_impero (carousel-factory) + bio->funnel"},
    {"owner": "Gael", "giorno": "G3-G4", "titolo": "Pipeline mentalita.brutale 100% auto: carousel-factory wrap -> gate QA auto -> scheduler -> report"},
    {"owner": "Gael", "giorno": "G4-G5", "titolo": "WF-YT v1: architettura workflow YouTube-Fliki + test 1 video end-to-end con API"},
    {"owner": "Gael", "giorno": "G6", "titolo": "Analisi competitor nicchie YT (3 candidate, dati citati) -> proposta a Max"},
    {"owner": "Gael", "giorno": "G5-G6", "titolo": "Promo-kit S6: landing rebrand + case study Novacar + lista concessionari import-DE"},
    {"owner": "Gael", "giorno": "G7", "titolo": "Consolidamento settimana: CP + metriche reali -> RETRO"},
]


def _seed() -> dict:
    now = time.strftime("%Y-%m-%d %H:%M")
    tasks = []
    for i, t in enumerate(_SEED_TASKS, 1):
        tasks.append({
            "id": f"tb-seed-{i:02d}", "owner": t["owner"], "giorno": t["giorno"],
            "titolo": t["titolo"], "stato": "da_fare", "note": "",
        })
    return {"tasks": tasks, "fonte": "PIANO-MAESTRO/16-PIANO-ESTATE-REVENUE.md", "creato": now, "aggiornato": now}


def _load() -> dict:
    if not STATE.exists():
        data = _seed()
        _save(data)
        return data
    try:
        return json.loads(STATE.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {"tasks": [], "errore": f"{STATE} illeggibile"}


def _save(data: dict) -> None:
    STATE.parent.mkdir(parents=True, exist_ok=True)
    STATE.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def elenco(payload=None):
    """POST /api/taskboard/elenco — tutti i task, raggruppabili per owner lato UI."""
    return _load()


def aggiorna(payload=None):
    """POST /api/taskboard/aggiorna — {id, campo, valore}: aggiorna UN task (stato o note)."""
    p = payload or {}
    tid, campo, valore = p.get("id"), p.get("campo"), p.get("valore")
    if not (tid and campo in ("stato", "note")):
        return {"errore": "servono 'id' e 'campo' ('stato' o 'note') + 'valore'"}
    if campo == "stato" and valore not in STATI_VALIDI:
        return {"errore": f"stato non valido: {valore}. Validi: {STATI_VALIDI}"}
    data = _load()
    for t in data.get("tasks", []):
        if t.get("id") == tid:
            t[campo] = valore
            data["aggiornato"] = time.strftime("%Y-%m-%d %H:%M")
            _save(data)
            return {"ok": True, "id": tid, campo: valore}
    return {"errore": f"id '{tid}' non trovato"}


def aggiungi(payload=None):
    """POST /api/taskboard/aggiungi — {owner, titolo, giorno}: nuovo task oltre al seed."""
    p = payload or {}
    owner, titolo = (p.get("owner") or "").strip(), (p.get("titolo") or "").strip()
    if owner not in ("Max", "Gael") or not titolo:
        return {"errore": "servono 'owner' ('Max' o 'Gael') e 'titolo' non vuoto"}
    data = _load()
    tasks = data.setdefault("tasks", [])
    new_id = _new_id()
    tasks.append({
        "id": new_id, "owner": owner, "giorno": (p.get("giorno") or "").strip(),
        "titolo": titolo, "stato": "da_fare", "note": "",
    })
    data["aggiornato"] = time.strftime("%Y-%m-%d %H:%M")
    _save(data)
    return {"ok": True, "id": new_id}


PANEL_HTML = """
<div id="panel-taskboard" class="panel">
  <h2>&#128203; Task Board — Max / Gael</h2>
  <p class="hint">Seed dal dossier 16 (PIANO ESTATE REVENUE). Stati: da_fare -> in_corso -> fatto (o bloccato).</p>
  <div class="row">
    <select id="tb-owner" class="inp"><option value="Max">Max</option><option value="Gael">Gael</option></select>
    <input id="tb-giorno" class="inp" placeholder="giorno (es. G3)" style="max-width:110px">
    <input id="tb-titolo" class="inp" placeholder="nuovo task...">
    <button class="btn" onclick="edTbAggiungi()">Aggiungi</button>
  </div>
  <div id="tb-list" style="margin-top:12px"></div>
</div>
<script>
  function edTbAggiungi(){
    var owner = document.getElementById('tb-owner').value;
    var giorno = document.getElementById('tb-giorno').value;
    var titolo = document.getElementById('tb-titolo').value;
    if (!titolo.trim()) return;
    edApi('taskboard/aggiungi', {owner: owner, giorno: giorno, titolo: titolo}).then(function(r){
      if (r.errore) { alert(r.errore); } else { document.getElementById('tb-titolo').value=''; edTbRender(); }
    });
  }
  function edTbSetStato(id, stato){ edApi('taskboard/aggiorna', {id: id, campo: 'stato', valore: stato}).then(edTbRender); }
  function edTbRender(){
    edApi('taskboard/elenco', {}).then(function(r){
      var el = document.getElementById('tb-list');
      var tasks = r.tasks || [];
      var owners = ['Max', 'Gael'];
      var html = '';
      owners.forEach(function(owner){
        var mine = tasks.filter(function(t){ return t.owner === owner; });
        html += '<div style="margin-bottom:14px"><b>' + owner + '</b> (' + mine.length + ')</div>';
        mine.forEach(function(t){
          var color = t.stato === 'fatto' ? 'var(--ok)' : (t.stato === 'bloccato' ? 'var(--err)' : 'var(--muted)');
          html += '<div class="row" style="margin-bottom:5px">' +
            '<span style="color:' + color + ';min-width:70px;font-size:11px;text-transform:uppercase">' + t.stato + '</span>' +
            '<span style="flex:1">[' + (t.giorno || '?') + '] ' + t.titolo + '</span>' +
            '<select onchange="edTbSetStato(\\'' + t.id + '\\', this.value)" class="inp" style="max-width:110px">' +
            ['da_fare','in_corso','fatto','bloccato'].map(function(s){
              return '<option value="' + s + '"' + (s === t.stato ? ' selected' : '') + '>' + s + '</option>';
            }).join('') + '</select>' +
            '</div>';
        });
      });
      el.innerHTML = html;
    });
  }
  edTbRender();
</script>
"""

MODULE = {
    "id": "taskboard",
    "tile": None,
    "routes": {
        "taskboard/elenco": elenco,
        "taskboard/aggiorna": aggiorna,
        "taskboard/aggiungi": aggiungi,
    },
    "panel_html": PANEL_HTML,
}


def selftest():
    """Probe: state scrivibile, seed presente (o creabile). NESSUN lancio reale."""
    try:
        data = _load()
        n = len(data.get("tasks", []))
        return True, f"taskboard: {n} task ({STATE})"
    except OSError as exc:
        return False, f"taskboard: state non scrivibile — {exc}"
