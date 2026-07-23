"""
EMPIRE FLOW — orchestrazione ad alto livello (GEM-06 §4.6): valida, valuta gate,
avvia/chiude passi, dice cosa è sbloccato, cosa è in ritardo.

Owner: Gael · Origine: FORGE (lotto G-C, CP-20260722)
"""
from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

from . import dag as _dag
from . import decisions as _decisions
from . import gate as _gate
from . import spec as _spec
from . import state as _state
from ..paths import repo_root, rel

__all__ = [
    "validate", "gates_table", "evaluate_gate", "confirm_gate",
    "start_step", "done_step", "step_status", "next_unlocked", "late_steps",
    "apply_decisions", "register_veto", "mark_on_red_applied",
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


def _on_red_applied_ids() -> frozenset[str]:
    applied = set()
    if _state.STATE_DIR.exists():
        for f in _state.STATE_DIR.glob("onred_*.json"):
            gate_id = f.stem[len("onred_"):]
            if _state.is_done(f"onred_{gate_id}"):
                applied.add(gate_id)
    return frozenset(applied)


def gates_table(workflow_root=None, *, now: datetime | None = None,
                apply_decisions_first: bool = True) -> list[_gate.GateResult]:
    """Valuta i 6 gate.

    Prima di valutare applica le decisioni a default-più-veto (ADR-EST-006): senza questo
    passaggio Gate-DEC resterebbe rosso non perché la decisione manchi, ma perché nessuno
    ha scritto il fatto che la registra. È esattamente il caso trovato il 23/07.
    """
    s = _spec.load_spec(workflow_root)
    if apply_decisions_first:
        _decisions.apply_all(s.decisions, now=now)
    facts = _gate.load_facts()
    return _gate.evaluate_all(s.gates, now=now, facts=facts,
                              confirmed_ids=_confirmed_gate_ids(),
                              on_red_applied_ids=_on_red_applied_ids())


def apply_decisions(workflow_root=None, *, now: datetime | None = None,
                    write: bool = True) -> list:
    s = _spec.load_spec(workflow_root)
    return _decisions.apply_all(s.decisions, now=now, write=write)


def register_veto(decision_id: str, *, actor: str, reason: str) -> tuple[bool, str]:
    return _decisions.register_veto(decision_id, actor=actor, reason=reason)


def mark_on_red_applied(gate_id: str, *, actor: str, evidence: str) -> tuple[bool, str]:
    """Registra che la contromossa `on_red` di un gate rosso è stata davvero eseguita.

    NON rende verde il gate: il colore continua a dire la verità sul mondo. Serve a
    distinguere un rosso previsto-e-gestito da un rosso ignorato, che è la differenza
    fra un piano che regge e un piano abbandonato.
    """
    if not evidence.strip():
        return False, "serve --evidence: senza prova, 'applicato' e' solo una parola"
    key = f"onred_{gate_id}"
    if _state.is_done(key):
        h = _state.history(key)
        return False, f"gia' registrato il {h[-1].ts}"
    _state.record(key, to_status="DONE", actor=actor, evidence=evidence,
                  note=f"on_red applicato per {gate_id}")
    return True, f"on_red di {gate_id} registrato come applicato"


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
