"""
EMPIRE FLOW — orchestrazione ad alto livello (GEM-06 §4.6): valida, valuta gate,
avvia/chiude passi, dice cosa è sbloccato, cosa è in ritardo.

Owner: Gael · Origine: FORGE (lotto G-C, CP-20260722)
"""
from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

from . import dag as _dag
from . import gate as _gate
from . import spec as _spec
from . import state as _state
from ..paths import repo_root, rel

__all__ = [
    "validate", "gates_table", "evaluate_gate", "confirm_gate",
    "start_step", "done_step", "step_status", "next_unlocked", "late_steps",
]


def validate(workflow_root=None) -> tuple[list, object]:
    """Ritorna (findings, spec). findings vuoto + DAG senza cicli = valido."""
    s = _spec.load_spec(workflow_root)
    findings = list(_spec.validate(s))
    try:
        _dag.topological_order(_dag.from_flow_spec(s))
    except _dag.CycleError as e:
        from ..schema import Finding
        findings.append(Finding(severity="block", rule="FLOW-CYCLE",
                                 path=Path("workflows.yaml"), message=str(e)))
    findings.sort(key=lambda f: (f.rank, f.rule))
    return findings, s


def _confirmed_gate_ids() -> frozenset[str]:
    confirmed = set()
    state_dir = _state.STATE_DIR
    if state_dir.exists():
        for f in state_dir.glob("gate_*.json"):
            gate_id = f.stem[len("gate_"):]
            if _state.is_done(f"gate_{gate_id}"):
                confirmed.add(gate_id)
    return frozenset(confirmed)


def gates_table(workflow_root=None, *, now: datetime | None = None) -> list[_gate.GateResult]:
    s = _spec.load_spec(workflow_root)
    facts = _gate.load_facts()
    confirmed = _confirmed_gate_ids()
    return _gate.evaluate_all(s.gates, now=now, facts=facts, confirmed_ids=confirmed)


def evaluate_gate(gate_id: str, workflow_root=None, *, now: datetime | None = None) -> _gate.GateResult | None:
    for r in gates_table(workflow_root, now=now):
        if r.id == gate_id:
            return r
    return None


def confirm_gate(gate_id: str, *, actor: str, evidence: str) -> _gate.GateResult:
    """Conferma umana esplicita di un gate `human` (GEM-06 §3: l'engine non finge
    mai che un passo umano sia stato fatto — questa è l'UNICA via per farlo diventare verde)."""
    key = f"gate_{gate_id}"
    if _state.is_done(key):
        h = _state.history(key)
        return _gate.GateResult(gate_id, "GREEN", h[-1].ts, "già confermato in precedenza (idempotente)", "")
    _state.record(key, to_status="DONE", actor=actor, evidence=evidence, note="conferma gate human")
    r = evaluate_gate(gate_id)
    return r


def start_step(step_id: str, *, edges: dict[str, list[str]], actor: str) -> tuple[bool, str]:
    """Un passo con dipendenza aperta non può partire (DoD-4)."""
    deps = edges.get(step_id, [])
    open_deps = [d for d in deps if not _state.is_done(d)]
    if open_deps:
        return False, f"bloccato: dipendenze aperte {open_deps}"
    if _state.current_status(step_id) not in ("OPEN",):
        return False, f"stato attuale non permette start: {_state.current_status(step_id)}"
    _state.record(step_id, to_status="IN_PROGRESS", actor=actor, note="avviato")
    return True, "avviato"


def done_step(step_id: str, *, actor: str, evidence: str, note: str = "") -> tuple[bool, str]:
    """Idempotente: chiudere due volte non duplica, segnala 'già chiuso' (DoD-9)."""
    if _state.is_done(step_id):
        h = _state.history(step_id)
        return False, f"già chiuso il {h[-1].ts}"
    _state.record(step_id, to_status="DONE", actor=actor, evidence=evidence, note=note)
    return True, "chiuso"


def step_status(step_id: str) -> str:
    return _state.current_status(step_id)


def next_unlocked(edges: dict[str, list[str]]) -> list[str]:
    done = {n for n in edges if _state.is_done(n)}
    return _dag.unlocked(edges, done)


def late_steps(edges: dict[str, list[str]], deadlines: dict[str, datetime],
                *, now: datetime | None = None) -> list[tuple[str, datetime]]:
    now = now or datetime.now(timezone.utc).astimezone()
    out = []
    for step_id, dl in deadlines.items():
        if _state.is_done(step_id):
            continue
        if now >= dl:
            out.append((step_id, dl))
    return sorted(out, key=lambda x: x[1])
