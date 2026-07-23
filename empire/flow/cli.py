"""
EMPIRE FLOW — plugin CLI: `python -m empire flow <comando>`.
Owner: Gael · Origine: FORGE (lotto G-C). Caricato dal loop di plugin di cli.py.
"""
from __future__ import annotations

import json

from . import dag as _dag
from . import runner as _runner
from . import spec as _spec


def cmd_flow_validate(a) -> int:
    findings, _s = _runner.validate(a.workflow)
    blocks = [f for f in findings if f.severity == "block"]
    if a.json:
        print(json.dumps([f.to_dict() for f in findings], indent=2, ensure_ascii=False))
    else:
        for f in findings:
            print(f)
        print(f"\nblock: {len(blocks)}   totale: {len(findings)}")
    return 1 if blocks else 0


def cmd_flow_gates(a) -> int:
    results = _runner.gates_table(a.workflow)
    icon = {"GREEN": "🟢", "RED": "🔴", "PENDING": "⏳"}
    if a.json:
        print(json.dumps([{
            "id": r.id, "status": r.status, "deadline": r.deadline.isoformat(),
            "reason": r.reason, "on_red": r.on_red,
        } for r in results], indent=2, ensure_ascii=False))
        return 0
    for r in results:
        print(f"{icon.get(r.status, '?')} {r.id:14} scad. {r.deadline.isoformat()}  {r.reason}")
        if r.status == "RED" and r.on_red:
            print(f"      -> on_red: {r.on_red}")
    return 0


def cmd_flow_gate(a) -> int:
    if a.confirm:
        r = _runner.confirm_gate(a.gate_id, actor=a.actor, evidence=a.evidence or "")
    else:
        r = _runner.evaluate_gate(a.gate_id, a.workflow)
    if r is None:
        print(f"gate sconosciuto: {a.gate_id}")
        return 2
    print(f"{r.id}: {r.status} — {r.reason}")
    return 0


def cmd_flow_status(a) -> int:
    s = _spec.load_spec(a.workflow)
    print(f"EMPIRE FLOW — {s.project}  (finestra {s.window.get('start')}..{s.window.get('end')})")
    print(f"  workflow: {len(s.workflows)}   decisioni: {len(s.decisions)}   gate: {len(s.gates)}")
    for wf_id in sorted(s.workflows):
        wf = s.workflows[wf_id]
        dict_steps = [st for st in wf.steps if isinstance(st, dict)]
        n_done = sum(1 for st in dict_steps if _runner.step_status(st.get("id", f"{wf_id}-?")) == "DONE")
        print(f"  {wf_id:20} owner={wf.owner or '?':10} step chiusi {n_done}/{len(wf.steps)}")
    return 0


def cmd_flow_next(a) -> int:
    s = _spec.load_spec(a.workflow)
    edges = _dag.from_flow_spec(s)
    unlocked = _runner.next_unlocked(edges)
    if a.json:
        print(json.dumps(unlocked, indent=2, ensure_ascii=False))
    else:
        print("Sbloccato adesso:", ", ".join(unlocked) if unlocked else "(nulla)")
    return 0


def cmd_flow_start(a) -> int:
    s = _spec.load_spec(a.workflow)
    edges = _dag.from_flow_spec(s)
    ok, msg = _runner.start_step(a.step, edges=edges, actor=a.actor)
    print(("✅ " if ok else "🚫 ") + msg)
    return 0 if ok else 1


def cmd_flow_done(a) -> int:
    ok, msg = _runner.done_step(a.step, actor=a.actor, evidence=a.evidence or "", note=a.note or "")
    print(("✅ " if ok else "ℹ️ ") + msg)
    return 0


def register(sub) -> None:
    p_flow = sub.add_parser("flow", help="motore workflow (GEM-06): stato, gate, coda")
    flow_sub = p_flow.add_subparsers(dest="flow_cmd", required=True)

    p = flow_sub.add_parser("validate", help="valida workflows.yaml (schema + DAG)")
    p.add_argument("--workflow", default=None)
    p.add_argument("--json", action="store_true")
    p.set_defaults(fn=cmd_flow_validate)

    p = flow_sub.add_parser("gates", help="valuta tutti i gate")
    p.add_argument("--workflow", default=None)
    p.add_argument("--json", action="store_true")
    p.set_defaults(fn=cmd_flow_gates)

    p = flow_sub.add_parser("gate", help="valuta o conferma un gate specifico")
    p.add_argument("gate_id")
    p.add_argument("--workflow", default=None)
    p.add_argument("--confirm", action="store_true", help="conferma umana (solo gate type=human)")
    p.add_argument("--actor", default="?")
    p.add_argument("--evidence", default="")
    p.set_defaults(fn=cmd_flow_gate)

    p = flow_sub.add_parser("status", help="stato dei workflow")
    p.add_argument("--workflow", default=None)
    p.set_defaults(fn=cmd_flow_status)

    p = flow_sub.add_parser("next", help="cosa è sbloccato adesso")
    p.add_argument("--workflow", default=None)
    p.add_argument("--json", action="store_true")
    p.set_defaults(fn=cmd_flow_next)

    p = flow_sub.add_parser("start", help="avvia uno step (fallisce se dipendenze aperte)")
    p.add_argument("--step", required=True)
    p.add_argument("--workflow", default=None)
    p.add_argument("--actor", default="?")
    p.set_defaults(fn=cmd_flow_start)

    p = flow_sub.add_parser("done", help="chiude uno step (idempotente)")
    p.add_argument("--step", required=True)
    p.add_argument("--actor", default="?")
    p.add_argument("--evidence", default="")
    p.add_argument("--note", default="")
    p.set_defaults(fn=cmd_flow_done)

    def _dispatch(a):
        return a.fn(a)
    p_flow.set_defaults(fn=_dispatch)
