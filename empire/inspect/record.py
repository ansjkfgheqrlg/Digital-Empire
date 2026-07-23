"""
Owner: Max · Controllore: Claude · Origine: FORGE
Governo: MANDATO Art.8 + ADR-008
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from empire.memory import Atom

@dataclass(slots=True)
class PerfRecord:
    id: str                    # PERF-YYYYMMDD-NNN
    agent: str                 # ID agente da index
    task: str
    workflow: str
    family: str                # e.g., "build-python"
    result: str                # success | partial | failed
    started: datetime
    ended: datetime
    ttd_h: float
    debug: dict = field(default_factory=dict)         # {errori:int, retry:int, escalation:int, fix_applicati:[str]}
    output_ref: list[Path] = field(default_factory=list)
    verification: dict = field(default_factory=dict)  # {verificatore, first_pass: bool, note}
    scorecard: dict = field(default_factory=dict)     # 5 assi 1-5 + gate traceability bool
    feedback_ids: list[str] = field(default_factory=list)

@dataclass(slots=True)
class FeedbackRecord:
    id: str                    # FB-YYYYMMDD-NNN
    ftype: str                 # TIP | RULE-NOTE | MUTATION-PROP
    to: str                    # agente | regolatore | comandante-di-casta
    micro_input: str           # max 200 caratteri
    on_perf: str               # PERF-id
    status: str                # open → acked → confirmed | recurred
    opened: datetime
    closed: datetime | None = None

def perf_to_atom(perf: PerfRecord) -> Atom:
    extra = {
        "agent": perf.agent,
        "family": perf.family,
        "result": perf.result,
        "started": perf.started.isoformat(),
        "ended": perf.ended.isoformat(),
        "ttd_h": perf.ttd_h,
        "debug": perf.debug,
        "verification": perf.verification,
        "scorecard": perf.scorecard,
    }
    body_data = {
        "started": perf.started.isoformat(),
        "ended": perf.ended.isoformat(),
        "family": perf.family,
        "result": perf.result,
        "ttd_h": perf.ttd_h,
        "debug": perf.debug,
        "verification": perf.verification,
    }
    return Atom(
        kind="perf",
        title=f"Performance: {perf.agent} on {perf.task}",
        body=json.dumps(body_data, ensure_ascii=False),
        id=perf.id,
        ts=perf.ended.isoformat(),
        actor=perf.agent,
        task=perf.task,
        workflow=perf.workflow,
        status=perf.result,
        refs=perf.feedback_ids,
        artifacts=[str(p) for p in perf.output_ref],
        extra=extra
    )

def atom_to_perf(atom: Atom) -> PerfRecord:
    extra = atom.extra or {}
    started_str = extra.get("started")
    ended_str = extra.get("ended") or atom.ts
    started = datetime.fromisoformat(started_str) if started_str else datetime.fromisoformat(atom.ts)
    ended = datetime.fromisoformat(ended_str) if ended_str else datetime.fromisoformat(atom.ts)
    output_ref = [Path(p) for p in atom.artifacts]
    
    return PerfRecord(
        id=atom.id,
        agent=extra.get("agent") or atom.actor,
        task=atom.task,
        workflow=atom.workflow,
        family=extra.get("family", ""),
        result=extra.get("result") or atom.status or "failed",
        started=started,
        ended=ended,
        ttd_h=float(extra.get("ttd_h", 0.0)),
        debug=extra.get("debug") or {},
        output_ref=output_ref,
        verification=extra.get("verification") or {},
        scorecard=extra.get("scorecard") or {},
        feedback_ids=atom.refs
    )

def feedback_to_atom(fb: FeedbackRecord) -> Atom:
    micro_input = fb.micro_input[:200]
    extra = {
        "ftype": fb.ftype,
        "to": fb.to,
        "on_perf": fb.on_perf,
        "opened": fb.opened.isoformat(),
        "closed": fb.closed.isoformat() if fb.closed else None,
    }
    body_data = {
        "micro_input": micro_input,
        "ftype": fb.ftype,
        "to": fb.to,
        "on_perf": fb.on_perf,
        "opened": fb.opened.isoformat(),
    }
    return Atom(
        kind="feedback",
        title=f"Feedback: {fb.ftype} to {fb.to}",
        body=json.dumps(body_data, ensure_ascii=False),
        id=fb.id,
        ts=fb.opened.isoformat(),
        actor=fb.to,
        task="",
        workflow="",
        status=fb.status,
        refs=[fb.on_perf],
        extra=extra
    )

def atom_to_feedback(atom: Atom) -> FeedbackRecord:
    extra = atom.extra or {}
    opened_str = extra.get("opened") or atom.ts
    closed_str = extra.get("closed")
    opened = datetime.fromisoformat(opened_str)
    closed = datetime.fromisoformat(closed_str) if closed_str else None
    
    micro_input = ""
    if atom.body:
        try:
            body_data = json.loads(atom.body)
            micro_input = body_data.get("micro_input", "")
        except json.JSONDecodeError:
            micro_input = atom.body
    if not micro_input:
        micro_input = atom.title
        
    on_perf = extra.get("on_perf")
    if not on_perf and atom.refs:
        on_perf = atom.refs[0]
        
    return FeedbackRecord(
        id=atom.id,
        ftype=extra.get("ftype", "TIP"),
        to=extra.get("to") or atom.actor,
        micro_input=micro_input[:200],
        on_perf=on_perf or "",
        status=atom.status or "open",
        opened=opened,
        closed=closed
    )
