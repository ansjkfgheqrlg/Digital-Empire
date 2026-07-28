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
            "evidence": r.evidence, "on_red_applied": r.on_red_applied,
        } for r in results], indent=2, ensure_ascii=False))
        return 0
    for r in results:
        print(f"{icon.get(r.status, '?')} {r.id:14} scad. {r.deadline.isoformat()}  {r.reason}")
        if r.evidence:
            print(f"      evidenza: {r.evidence}")
        if r.status == "RED" and r.on_red:
            marca = "APPLICATO" if r.on_red_applied else "DA APPLICARE"
            print(f"      -> on_red [{marca}]: {r.on_red}")
    return 0


def cmd_flow_gate(a) -> int:
    if a.applied_on_red:
        ok, msg = _runner.mark_on_red_applied(a.gate_id, actor=a.actor, evidence=a.evidence or "")
        print(msg)
        return 0 if ok else 1
    if a.confirm:
        r = _runner.confirm_gate(a.gate_id, actor=a.actor, evidence=a.evidence or "")
    else:
        r = _runner.evaluate_gate(a.gate_id, a.workflow)
    if r is None:
        print(f"gate sconosciuto: {a.gate_id}")
        return 2
    print(f"{r.id}: {r.status} — {r.reason}")
    if r.evidence:
        print(f"  evidenza: {r.evidence}")
    return 0


def cmd_flow_decisions(a) -> int:
    statuses = _runner.apply_decisions(a.workflow, write=not a.dry_run)
    icon = {"ATTIVA": "🟢", "VETO": "🛑", "IN_ATTESA": "⏳"}
    if a.json:
        print(json.dumps([{
            "id": s.id, "topic": s.topic, "default": s.default, "state": s.state,
            "fact": s.fact, "reason": s.reason,
            "veto_deadline": s.veto_deadline.isoformat() if s.veto_deadline else None,
        } for s in statuses], indent=2, ensure_ascii=False))
        return 0
    for s in statuses:
        print(f"{icon.get(s.state, '?')} {s.id:14} {s.state:10} {s.topic}")
        print(f"      default: {s.default}")
        print(f"      {s.reason}   [fatto: {s.fact}]")
    if a.dry_run:
        print("\n(dry-run: nessun fatto scritto)")
    return 0


def cmd_flow_veto(a) -> int:
    ok, msg = _runner.register_veto(a.decision_id, actor=a.actor, reason=a.reason)
    print(msg)
    return 0 if ok else 1


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
    p.add_argument("--applied-on-red", dest="applied_on_red", action="store_true",
                   help="registra che la contromossa on_red e' stata eseguita (NON rende verde il gate)")
    p.add_argument("--actor", default="?")
    p.add_argument("--evidence", default="")
    p.set_defaults(fn=cmd_flow_gate)

    p = flow_sub.add_parser("decisions", help="decisioni default-piu-veto (ADR-EST-006)")
    p.add_argument("--workflow", default=None)
    p.add_argument("--json", action="store_true")
    p.add_argument("--dry-run", dest="dry_run", action="store_true",
                   help="mostra senza scrivere i fatti")
    p.set_defaults(fn=cmd_flow_decisions)

    p = flow_sub.add_parser("veto", help="registra un veto umano su una decisione")
    p.add_argument("decision_id")
    p.add_argument("--actor", required=True)
    p.add_argument("--reason", required=True)
    p.set_defaults(fn=cmd_flow_veto)

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

    # `empire estate` — verdetto unico sul Workflow Estate. Vive in empire/estate.py ma
    # si registra da qui: empire/cli.py e' congelato e la sua tupla _PLUGIN_MODULES non
    # elenca empire.estate. Il loop passa a ogni plugin i subparser di primo livello,
    # quindi un modulo gia' elencato puo' aggiungere il comando senza toccare il file
    # congelato — che e' esattamente cio' che il congelamento vuole evitare (merge
    # conflittuali fra sessioni parallele di Max, Gael e Gemini).
    try:
        from .. import estate as _estate
    except ImportError:
        pass
    else:
        _estate.register(sub)

    # `empire trace` — le 5 tracce del Piano 2. Registrato da qui per lo stesso motivo
    # di `estate`: cli.py e' congelato e non elenca empire.trace fra i plugin.
    try:
        from .. import trace as _trace
    except ImportError:
        pass
    else:
        _trace.register(sub)

    # `empire forge` — misura quanto gli agenti sono operativi. Stesso motivo di
    # registrazione da qui: cli.py e' congelato.
    try:
        from .. import forge as _forge
    except ImportError:
        pass
    else:
        _forge.register(sub)

    # `empire avvia-estate` — accende il sistema nervoso con un comando. Registrato da qui
    # perche' cli.py e' congelato.
    try:
        from .. import avvia as _avvia
    except ImportError:
        pass
    else:
        _avvia.register(sub)

    # `empire controllo` — centro di comando su tutti i workflow. Registrato da qui
    # (cli.py congelato).
    try:
        from .. import controllo as _controllo
    except ImportError:
        pass
    else:
        _controllo.register(sub)
