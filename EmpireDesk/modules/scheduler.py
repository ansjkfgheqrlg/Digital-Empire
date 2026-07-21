# -*- coding: utf-8 -*-
"""
B2 — modules/scheduler.py (Half B, owner: Gael — contratto dossier 17 §5.3).

Run programmate per tile: giorni+ora ricorrenti, persistenza in EmpireDesk/state/scheduler.json.
Riusa il lock "un processo per tile" già presente in TileManager (via host.launch): se la tile è
già in corso al momento previsto, quel giro si SALTA (si registra nel log), non si accoda mai.

Il modulo non importa app.py né conosce TileManager: riceve un `host` (con .launch/.poll/
.tile_ids) tramite `run_background(host)`, chiamato da app.py SOLO quando un motore GUI reale
sta per partire — mai durante `--selftest` (Mandato Art.4.3: zero lanci/automazioni in selftest).
"""
import json
import threading
import time as _time
from datetime import datetime
from pathlib import Path

STATE = Path(__file__).resolve().parents[1] / "state" / "scheduler.json"
GIORNI = ["lun", "mar", "mer", "gio", "ven", "sab", "dom"]  # datetime.weekday(): 0=lun

_HOST = None            # iniettato da run_background(host)
_LAST_RUN: dict = {}    # {entry_id: "YYYY-MM-DD HH:MM"} — evita doppio trigger nello stesso minuto
_LOG: list = []         # ultime righe (in memoria, per il pannello)
_loop_started = False
_id_counter = 0         # per id univoci anche entro lo stesso secondo


def _new_id() -> str:
    """Id univoco anche se si creano più entry nello stesso secondo (bug trovato in test:
    `sch-<int(time)>` collideva)."""
    global _id_counter
    _id_counter += 1
    return f"sch-{int(_time.time())}-{_id_counter}"


def _valid_hhmm(s: str) -> bool:
    try:
        hh, mm = str(s).split(":")
        return 0 <= int(hh) <= 23 and 0 <= int(mm) <= 59 and len(mm) == 2
    except (ValueError, AttributeError):
        return False


def run_background(host) -> None:
    """Chiamato da app.py::start_module_background_tasks() a motore GUI già avviato."""
    global _HOST, _loop_started
    _HOST = host
    if _loop_started:
        return
    _loop_started = True
    threading.Thread(target=_loop, daemon=True).start()
    _log_line("scheduler avviato")


def _load() -> dict:
    if not STATE.exists():
        return {"entries": []}
    try:
        return json.loads(STATE.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {"entries": []}


def _save(data: dict) -> None:
    STATE.parent.mkdir(parents=True, exist_ok=True)
    STATE.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def _log_line(s: str) -> None:
    _LOG.append(f"{datetime.now():%Y-%m-%d %H:%M:%S} {s}")
    del _LOG[:-200]


def _loop() -> None:
    while True:
        try:
            _tick()
        except Exception as exc:  # noqa: BLE001 — il loop non deve mai fermarsi da solo
            _log_line(f"ERRORE loop: {exc}")
        _time.sleep(30)


def _tick() -> None:
    if _HOST is None:
        return
    now = datetime.now()
    giorno = GIORNI[now.weekday()]
    hhmm = now.strftime("%H:%M")
    stamp_minuto = now.strftime("%Y-%m-%d %H:%M")
    data = _load()
    valid_ids = set(_HOST.tile_ids())
    for e in data.get("entries", []):
        if not e.get("enabled", True):
            continue
        if e.get("tile_id") not in valid_ids:
            continue
        if giorno not in (e.get("giorni") or []):
            continue
        if e.get("ora") != hhmm:
            continue
        key = e.get("id") or e.get("tile_id")
        if _LAST_RUN.get(key) == stamp_minuto:
            continue  # già innescato in questo minuto
        _LAST_RUN[key] = stamp_minuto
        r = _HOST.launch(e["tile_id"], e.get("input"))
        if r.get("ok"):
            _log_line(f"avviata '{e['tile_id']}' (schedulata {hhmm})")
        else:
            _log_line(f"'{e['tile_id']}' NON avviata ({hhmm}): {r.get('error')}")


# --------------------------------------------------------------------------- #
# Routes esposte al pannello (montate su POST /api/scheduler/<...>)
# --------------------------------------------------------------------------- #
def elenco(payload=None):
    return {"entries": _load().get("entries", []), "log": _LOG[-50:]}


def aggiungi(payload=None):
    p = payload or {}
    tile_id, ora, giorni = p.get("tile_id"), p.get("ora"), p.get("giorni")
    if not (tile_id and ora and giorni):
        return {"errore": "servono 'tile_id', 'ora' (HH:MM) e 'giorni' (lista)"}
    # La validazione della tile richiede l'host (le tile lanciabili le conosce solo lui, escluse
    # le readonly): senza host non si può programmare nulla di sensato, quindi si rifiuta con un
    # messaggio chiaro invece di accettare tile inesistenti/readonly (bug trovato in test: con
    # _HOST=None il controllo veniva saltato e QUALSIASI tile_id passava).
    if _HOST is None:
        return {"errore": "scheduler non ancora inizializzato (host non disponibile)"}
    if tile_id not in _HOST.tile_ids():
        return {"errore": f"tile non programmabile (inesistente o sola lettura): {tile_id}"}
    if not _valid_hhmm(ora):
        return {"errore": f"ora non valida (serve HH:MM 00:00-23:59): {ora}"}
    if not (isinstance(giorni, list) and giorni and all(g in GIORNI for g in giorni)):
        return {"errore": f"giorni non validi (lista non vuota da {GIORNI})"}
    data = _load()
    entries = data.setdefault("entries", [])
    new_id = _new_id()
    entries.append({
        "id": new_id, "tile_id": tile_id, "ora": ora, "giorni": giorni,
        "input": p.get("input"), "enabled": True,
    })
    _save(data)
    return {"ok": True, "id": new_id}


def rimuovi(payload=None):
    p = payload or {}
    eid = p.get("id")
    data = _load()
    before = len(data.get("entries", []))
    data["entries"] = [e for e in data.get("entries", []) if e.get("id") != eid]
    _save(data)
    return {"ok": True, "rimossa": before != len(data["entries"])}


def toggle(payload=None):
    p = payload or {}
    eid = p.get("id")
    data = _load()
    found = False
    for e in data.get("entries", []):
        if e.get("id") == eid:
            e["enabled"] = not e.get("enabled", True)
            found = True
    _save(data)
    return {"ok": found}


PANEL_HTML = """
<div id="panel-scheduler" class="panel">
  <h2>&#9200; Scheduler</h2>
  <p class="hint">Run programmate per tile. Se una tile e' gia' in corso al momento previsto, quel giro si salta (resta nel log, non si accoda).</p>
  <div class="row">
    <select id="sch-tile" class="inp"></select>
    <input id="sch-ora" class="inp" placeholder="HH:MM" style="max-width:90px">
    <input id="sch-giorni" class="inp" placeholder="lun,mar,mer,gio,ven,sab,dom">
    <input id="sch-input" class="inp" placeholder="input (opzionale)">
    <button class="btn" onclick="edSchedAggiungi()">Aggiungi</button>
  </div>
  <div id="sch-list" style="margin-top:10px"></div>
  <pre id="sch-log" class="log-pane">Premi Aggiorna per caricare.</pre>
  <button class="btn" style="margin-top:8px" onclick="edSchedRender()">Aggiorna</button>
</div>
<script>
  function edSchedAggiungi(){
    var tile = document.getElementById('sch-tile').value;
    var ora = document.getElementById('sch-ora').value;
    var giorni = document.getElementById('sch-giorni').value.split(',').map(function(s){return s.trim();}).filter(Boolean);
    var input = document.getElementById('sch-input').value || null;
    edApi('scheduler/aggiungi', {tile_id: tile, ora: ora, giorni: giorni, input: input}).then(function(r){
      if (r.errore) { alert(r.errore); } else { edSchedRender(); }
    });
  }
  function edSchedRender(){
    edApi('scheduler/elenco', {}).then(function(r){
      var list = document.getElementById('sch-list');
      var rows = (r.entries || []).map(function(e){
        var stato = e.enabled ? '<span style="color:var(--ok)">attiva</span>' : '<span style="color:var(--muted)">pausa</span>';
        return '<div class="row" style="margin-bottom:4px">' +
          '<b>' + e.tile_id + '</b> &mdash; ' + e.ora + ' (' + (e.giorni || []).join(',') + ') ' + stato +
          ' <button class="btn" onclick="edSchedToggle(\\'' + e.id + '\\')">Pausa/Riprendi</button>' +
          ' <button class="btn" onclick="edSchedRimuovi(\\'' + e.id + '\\')">Rimuovi</button>' +
          '</div>';
      }).join('') || '<div class="hint">Nessuna run programmata.</div>';
      list.innerHTML = rows;
      document.getElementById('sch-log').textContent = (r.log || []).join('\\n') || 'Nessun evento ancora.';
    });
  }
  function edSchedToggle(id){ edApi('scheduler/toggle', {id: id}).then(edSchedRender); }
  function edSchedRimuovi(id){ edApi('scheduler/rimuovi', {id: id}).then(edSchedRender); }
  edApi('tiles', {}).then(function(r){
    var sel = document.getElementById('sch-tile');
    ((r && r.tiles) || []).forEach(function(t){
      if (t.kind === 'readonly') return;
      var o = document.createElement('option'); o.value = t.id; o.textContent = t.name;
      sel.appendChild(o);
    });
  });
  edSchedRender();
</script>
"""

MODULE = {
    "id": "scheduler",
    "tile": None,
    "routes": {
        "scheduler/elenco": elenco,
        "scheduler/aggiungi": aggiungi,
        "scheduler/rimuovi": rimuovi,
        "scheduler/toggle": toggle,
    },
    "panel_html": PANEL_HTML,
}


def selftest():
    """Probe: cartella state scrivibile, JSON leggibile. NON avvia il loop né lancia nulla."""
    try:
        STATE.parent.mkdir(parents=True, exist_ok=True)
        data = _load()
        n = len(data.get("entries", []))
        return True, f"scheduler: {n} run programmate, state scrivibile ({STATE})"
    except OSError as exc:
        return False, f"scheduler: state non scrivibile — {exc}"
