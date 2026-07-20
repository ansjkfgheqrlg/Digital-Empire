# -*- coding: utf-8 -*-
"""
B4 — modules/taskboard.py (Half B, owner: Gael — contratto dossier 17 §5.3).

Task board Max/Gael live. Fonte autoritativa = dossier 16 §3 (PIANO-ESTATE-REVENUE.md).
Il file di stato `EmpireDesk/state/taskboard.json` viene inizializzato automaticamente
dalla lista task del dossier (stream/source = "dossier16") se non esiste ancora.

Pattern: ogni completamento tile (via coda push_tile_completion) aggiorna automaticamente
lo stato del task corrispondente quando la tile associata termina.

Il modulo NON lancia automazioni (Mandato Art.4.3).
"""
import json
import threading
import time as _time
from datetime import datetime
from pathlib import Path

STATE_DIR = Path(__file__).resolve().parents[1] / "state"
STATE_FILE = STATE_DIR / "taskboard.json"

_loop_started = False

# Mapping tile_id → task_id (per auto-update a fine run)
_TILE_TO_TASK: dict[str, str] = {}

# Task iniziali da dossier 16 §3 (fonte autoritativa — Gael tasks)
_INITIAL_TASKS = [
    # G1
    {
        "id": "g1-cf-r8",
        "label": "Chiudere CF-R8 → 03-CONTENT-FACTORY 9/9",
        "assignee": "Gael",
        "stream": "infra",
        "priority": "high",
        "status": "in_progress",
        "output": "CP",
        "tile_id": None,
        "notes": "",
    },
    {
        "id": "g1-audit-asset",
        "label": "AUDIT ASSET P0.2 — censire tutte le pagine",
        "assignee": "Gael",
        "stream": "S3/S4",
        "priority": "high",
        "status": "todo",
        "output": "AUDIT-PAGINE-20260719.md",
        "tile_id": None,
        "notes": "",
    },
    # G2
    {
        "id": "g2-funnel-manuale",
        "label": "Funnel Manuale — landing + checkout + 3 email",
        "assignee": "Gael",
        "stream": "S2",
        "priority": "high",
        "status": "todo",
        "output": "funnel live",
        "tile_id": None,
        "notes": "",
    },
    {
        "id": "g2-batch-caroselli",
        "label": "Batch riattivazione S3: 7 caroselli crea.illtuo_impero + bio→funnel",
        "assignee": "Gael",
        "stream": "S3",
        "priority": "medium",
        "status": "todo",
        "output": "pagina riparte",
        "tile_id": "caroselli",
        "notes": "",
    },
    # G3-G4
    {
        "id": "g3-pipeline-mb",
        "label": "Pipeline mentalita.brutale 100% auto",
        "assignee": "Gael",
        "stream": "S4",
        "priority": "medium",
        "status": "todo",
        "output": "pipeline testata end-to-end",
        "tile_id": None,
        "notes": "",
    },
    # G4-G5
    {
        "id": "g4-wf-yt",
        "label": "WF-YT v1: workflow YouTube-Fliki + test 1 video end-to-end",
        "assignee": "Gael",
        "stream": "S5",
        "priority": "medium",
        "status": "todo",
        "output": "1 video + WF docs",
        "tile_id": "studio",
        "notes": "",
    },
    # G6
    {
        "id": "g6-yt-nicchie",
        "label": "Analisi competitor nicchie YT (3 candidate) → proposta a Max",
        "assignee": "Gael",
        "stream": "S5",
        "priority": "low",
        "status": "todo",
        "output": "doc proposta",
        "tile_id": None,
        "notes": "",
    },
    # G5-G6
    {
        "id": "g5-promokit-s6",
        "label": "Promo-kit S6: landing rebrand + case study Novacar + lista lead",
        "assignee": "Gael",
        "stream": "S6",
        "priority": "medium",
        "status": "todo",
        "output": "kit pronto",
        "tile_id": None,
        "notes": "",
    },
    # G7
    {
        "id": "g7-retro",
        "label": "Consolidamento: CP + metriche reali + RETRO settimanale",
        "assignee": "Gael",
        "stream": "tutti",
        "priority": "high",
        "status": "todo",
        "output": "CP settimanale",
        "tile_id": None,
        "notes": "",
    },
]

# Costruisci mapping tile→task
for t in _INITIAL_TASKS:
    if t.get("tile_id"):
        _TILE_TO_TASK[t["tile_id"]] = t["id"]


# --------------------------------------------------------------------------- #
# Persistenza
# --------------------------------------------------------------------------- #
def _load() -> list[dict]:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            pass
    # First run: inizializza da dossier 16 con timestamp
    tasks = []
    for t in _INITIAL_TASKS:
        tasks.append({**t, "created_at": datetime.now().isoformat(timespec="seconds"), "updated_at": datetime.now().isoformat(timespec="seconds")})
    _save(tasks)
    return tasks


def _save(tasks: list[dict]) -> None:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(tasks, ensure_ascii=False, indent=2), encoding="utf-8")


# --------------------------------------------------------------------------- #
# Auto-update da coda completamento
# --------------------------------------------------------------------------- #
def run_background(host) -> None:
    """Chiamato da app.py::start_module_background_tasks(). Polla la coda completamenti
    e aggiorna automaticamente il task associato quando la tile termina."""
    global _loop_started
    if _loop_started:
        return
    _loop_started = True

    from app import poll_completions

    def _loop():
        while True:
            try:
                for ev in poll_completions():
                    tile_id = ev.get("id")
                    exit_code = ev.get("exit_code")
                    error = ev.get("error")

                    # Trova task associato a questa tile
                    task_id = _TILE_TO_TASK.get(tile_id)
                    if not task_id:
                        continue

                    tasks = _load()
                    for t in tasks:
                        if t["id"] == task_id:
                            old = t.get("status")
                            if error or (exit_code and exit_code != 0):
                                t["status"] = "blocked"
                                t["notes"] = f"[auto] Tile '{tile_id}' fallita: {error or f'exit {exit_code}'}"
                            else:
                                t["status"] = "done"
                                t["notes"] = f"[auto] Tile '{tile_id}' completata con successo (exit {exit_code})"
                            t["updated_at"] = datetime.now().isoformat(timespec="seconds")
                            if t["status"] != old:
                                _save(tasks)
                            break
            except Exception:  # noqa: BLE001 — il loop non deve mai fermarsi
                pass
            _time.sleep(3)

    threading.Thread(target=_loop, daemon=True).start()


# --------------------------------------------------------------------------- #
# Routes
# --------------------------------------------------------------------------- #
def elenco(payload=None) -> dict:
    """Ritorna tutti i task, opzionalmente filtrati per assignee o status."""
    p = payload or {}
    tasks = _load()
    assignee = p.get("assignee")
    status = p.get("status")
    if assignee:
        tasks = [t for t in tasks if t.get("assignee") == assignee]
    if status:
        tasks = [t for t in tasks if t.get("status") == status]
    return {"tasks": tasks, "total": len(tasks)}


def aggiorna(payload=None) -> dict:
    """Aggiorna uno o più campi di un task (status, notes, priority)."""
    p = payload or {}
    task_id = p.get("id")
    if not task_id:
        return {"errore": "manca 'id'"}
    tasks = _load()
    for t in tasks:
        if t["id"] == task_id:
            for field in ("status", "notes", "priority", "label"):
                if field in p:
                    t[field] = p[field]
            t["updated_at"] = datetime.now().isoformat(timespec="seconds")
            _save(tasks)
            return {"ok": True, "task": t}
    return {"errore": f"task '{task_id}' non trovato"}


def aggiungi(payload=None) -> dict:
    """Aggiunge un nuovo task manualmente."""
    p = payload or {}
    label = p.get("label")
    assignee = p.get("assignee", "Gael")
    if not label:
        return {"errore": "manca 'label'"}
    tasks = _load()
    new_id = f"manual-{int(_time.time())}"
    new_task = {
        "id": new_id,
        "label": label,
        "assignee": assignee,
        "stream": p.get("stream", ""),
        "priority": p.get("priority", "medium"),
        "status": "todo",
        "output": p.get("output", ""),
        "tile_id": p.get("tile_id"),
        "notes": p.get("notes", ""),
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "updated_at": datetime.now().isoformat(timespec="seconds"),
    }
    tasks.append(new_task)
    _save(tasks)
    return {"ok": True, "task": new_task}


# --------------------------------------------------------------------------- #
# Panel HTML (inline — usa edApi per le route modulo)
# --------------------------------------------------------------------------- #
PANEL_HTML = """
<div id="panel-taskboard" class="panel">
  <h2>&#9745; Task Board</h2>
  <p class="hint">Task da <b>dossier 16 §3</b> — aggiornamento automatico quando una tile termina.</p>
  <div class="filter-row" style="margin-bottom:10px">
    <button class="btn btn-active" id="tb-filter-all" onclick="tbFilter('all')">Tutti</button>
    <button class="btn" id="tb-filter-todo" onclick="tbFilter('todo')">Da fare</button>
    <button class="btn" id="tb-filter-in_progress" onclick="tbFilter('in_progress')">In corso</button>
    <button class="btn" id="tb-filter-done" onclick="tbFilter('done')">Fatti</button>
    <button class="btn" id="tb-filter-blocked" onclick="tbFilter('blocked')">Bloccati</button>
  </div>
  <div id="tb-list" style="margin-bottom:12px"></div>
  <div class="row" style="margin-top:8px">
    <input id="tb-new-label" class="inp" placeholder="Nuovo task..." style="flex:1">
    <button class="btn" onclick="tbAggiungi()">+ Task</button>
    <button class="btn" onclick="tbRender()">&#8635;</button>
  </div>
</div>
<script>
  var _tbFilter = 'all';
  function tbFilter(f) {
    _tbFilter = f;
    document.querySelectorAll('.filter-row .btn').forEach(function(b){ b.classList.remove('btn-active'); });
    var el = document.getElementById('tb-filter-' + f);
    if (el) el.classList.add('btn-active');
    tbRender();
  }
  function _tbStatusColor(s) {
    if (s === 'done') return '#22c55e';
    if (s === 'in_progress') return '#3b82f6';
    if (s === 'blocked') return '#ef4444';
    return '#9fb0bb';
  }
  function _tbPriorityLabel(p) {
    if (p === 'high') return '<span style="color:#fb4604;font-size:11px">HIGH</span>';
    if (p === 'medium') return '<span style="color:#f59e0b;font-size:11px">MED</span>';
    return '<span style="color:#6b7280;font-size:11px">LOW</span>';
  }
  function tbRender() {
    edApi('taskboard/elenco', {}).then(function(r) {
      var tasks = (r.tasks || []);
      var html = '<table style="width:100%;border-collapse:collapse;font-size:13px">';
      html += '<tr style="color:#9fb0bb;text-align:left">'
        + '<th style="padding:4px 6px">Stato</th><th style="padding:4px 6px">Task</th>'
        + '<th style="padding:4px 6px">Stream</th><th style="padding:4px 6px">Note</th><th style="padding:4px 6px"></th>'
        + '</tr>';
      var shown = 0;
      tasks.forEach(function(t) {
        if (_tbFilter !== 'all' && t.status !== _tbFilter) return;
        shown++;
        var color = _tbStatusColor(t.status);
        var prio = _tbPriorityLabel(t.priority);
        var statusLabel = t.status === 'todo' ? '&#9744;' : t.status === 'in_progress' ? '&#9728;' : t.status === 'done' ? '&#9745;' : '&#9888;';
        html += '<tr style="border-bottom:1px solid #2a3540">'
          + '<td style="padding:6px 6px;color:' + color + '">' + statusLabel + '</td>'
          + '<td style="padding:6px 6px"><b>' + t.label + '</b> ' + prio + '</td>'
          + '<td style="padding:6px 6px;color:#9fb0bb;font-size:12px">' + (t.stream || '-') + '</td>'
          + '<td style="padding:6px 6px;color:#6b7280;font-size:11px;max-width:160px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap" title="' + (t.notes || '') + '">' + (t.notes || '-') + '</td>'
          + '<td style="padding:6px 4px;text-align:right">'
          + '<button class="btn" style="padding:2px 8px;font-size:11px" onclick="tbToggle(\'' + t.id + '\',\'' + t.status + '\')">&#8635;</button>'
          + '</td></tr>';
      });
      if (shown === 0) html += '<tr><td colspan="5" style="padding:16px;text-align:center;color:#6b7280">Nessun task in questo stato.</td></tr>';
      html += '</table>';
      html += '<p style="color:#6b7280;font-size:12px;margin-top:8px">' + r.total + ' task totali</p>';
      document.getElementById('tb-list').innerHTML = html;
    });
  }
  function tbToggle(id, currentStatus) {
    var nextStatus = currentStatus === 'todo' ? 'in_progress' : currentStatus === 'in_progress' ? 'done' : 'todo';
    edApi('taskboard/aggiorna', {id: id, status: nextStatus}).then(tbRender);
  }
  function tbAggiungi() {
    var label = document.getElementById('tb-new-label').value.trim();
    if (!label) return;
    edApi('taskboard/aggiungi', {label: label}).then(function() {
      document.getElementById('tb-new-label').value = '';
      tbRender();
    });
  }
  tbRender();
</script>
"""


# --------------------------------------------------------------------------- #
# Contratto modulo (dossier 17 §5.3)
# --------------------------------------------------------------------------- #
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


def selftest() -> tuple[bool, str]:
    """Probe: state scrivibile, JSON leggibile, task iniziali presenti."""
    try:
        STATE_DIR.mkdir(parents=True, exist_ok=True)
        tasks = _load()
        return True, f"taskboard: {len(tasks)} task ({sum(1 for t in tasks if t.get('status')=='todo')} da fare)"
    except OSError as exc:
        return False, f"taskboard: state non scrivibile — {exc}"
