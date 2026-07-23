"""
EMPIRE FLOW — parser e validatore di workflows.yaml.

Owner: Gael · Origine: FORGE (lotto G-C, CP-20260722)

Adatta lo schema a quello che esiste già in WORKFLOW-ESTATE/01-FLUSSI-E-PIANI/workflows.yaml
(ADR-003: wrap, non riscrittura) invece di imporne uno nuovo. L'unica estensione fatta al file
è la sezione `gates:` in fondo (6 gate di WF-MASTER.md, prima solo referenziati per nome),
autorizzata dal brief GEM-06 §5 Task 2 ("e' dato di configurazione, modificarlo e' autorizzato").
"""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any

import yaml

from ..paths import resolve
from ..schema import Finding

__all__ = ["Gate", "WorkflowSpec", "FlowSpec", "load_raw", "load_spec", "validate"]

DEFAULT_YAML_PATH = "wf_flussi/workflows.yaml"


@dataclass(slots=True)
class Gate:
    id: str
    deadline: datetime
    type: str                    # metric | file | human | command | conform
    green_if: str | None = None
    on_red: str = ""
    path: str | None = None              # per type=file
    must_not_contain: str | None = None  # per type=file
    must_contain: str | None = None      # per type=file
    command: str | None = None           # per type=command
    evidence: dict | None = None         # evidenza calcolata da mostrare a chi conferma (type=human)


@dataclass(slots=True)
class WorkflowSpec:
    id: str
    raw: dict = field(default_factory=dict)
    owner: str | None = None
    depends: list[str] = field(default_factory=list)   # id di decisioni/workflow da cui dipende
    steps: list[dict] = field(default_factory=list)


@dataclass(slots=True)
class FlowSpec:
    version: int
    project: str
    window: dict
    decisions: list[dict]
    workflows: dict[str, WorkflowSpec]
    gates: list[Gate]
    raw: dict


def _yaml_path(workflow_root: str | Path | None = None) -> Path:
    if workflow_root is None:
        return resolve(DEFAULT_YAML_PATH.split("/")[0]) / "workflows.yaml"
    root = Path(workflow_root)
    if not root.is_absolute():
        root = resolve(str(workflow_root))
    candidate = root / "01-FLUSSI-E-PIANI" / "workflows.yaml"
    if candidate.exists():
        return candidate
    return root / "workflows.yaml"


def load_raw(workflow_root: str | Path | None = None) -> dict:
    path = _yaml_path(workflow_root)
    if not path.exists():
        raise FileNotFoundError(f"workflows.yaml non trovato: {path}")
    with open(path, "r", encoding="utf-8") as fh:
        return yaml.safe_load(fh) or {}


def _parse_deadline(raw_dt) -> datetime:
    if isinstance(raw_dt, datetime):
        dt = raw_dt
    else:
        s = str(raw_dt).strip()
        dt = datetime.fromisoformat(s)
    if dt.tzinfo is None:
        raise ValueError(f"deadline senza timezone (vietato): {raw_dt!r}")
    return dt


def load_spec(workflow_root: str | Path | None = None) -> FlowSpec:
    raw = load_raw(workflow_root)

    workflows: dict[str, WorkflowSpec] = {}
    for wf_id, wf_raw in (raw.get("workflows") or {}).items():
        wf_raw = wf_raw or {}
        depends = list(wf_raw.get("depends") or [])
        workflows[wf_id] = WorkflowSpec(
            id=wf_id, raw=wf_raw, owner=wf_raw.get("owner"),
            depends=depends, steps=list(wf_raw.get("steps") or []),
        )

    gates: list[Gate] = []
    for g in (raw.get("gates") or []):
        gates.append(Gate(
            id=g["id"],
            deadline=_parse_deadline(g["deadline"]),
            type=g.get("type", "human"),
            green_if=g.get("green_if"),
            on_red=g.get("on_red", ""),
            path=g.get("path"),
            must_not_contain=g.get("must_not_contain"),
            must_contain=g.get("must_contain"),
            command=g.get("command"),
            evidence=g.get("evidence"),
        ))

    return FlowSpec(
        version=raw.get("version", 1),
        project=raw.get("project", ""),
        window=raw.get("window") or {},
        decisions=list(raw.get("decisions") or []),
        workflows=workflows,
        gates=gates,
        raw=raw,
    )


def validate(spec: FlowSpec, source_path: Path | None = None) -> list[Finding]:
    """Validazione a load-time (GEM-06 §4.1): depends risolvibili, niente cicli
    (delegato a dag.py da runner/cli, qui solo controlli locali), deadline ISO-8601
    con timezone, gate id referenziati negli step esistono in `gates:`.
    """
    findings: list[Finding] = []
    src = source_path or Path("workflows.yaml")

    decision_ids = {d["id"] for d in spec.decisions if "id" in d}
    workflow_ids = set(spec.workflows)
    gate_ids = {g.id for g in spec.gates}
    known_ids = decision_ids | workflow_ids | gate_ids

    for wf_id, wf in spec.workflows.items():
        for dep in wf.depends:
            if dep not in known_ids:
                findings.append(Finding(
                    severity="block", rule="FLOW-DEPENDS-DEAD", path=src,
                    message=f"{wf_id} dipende da {dep!r}, che non esiste ne' tra le decisioni ne' tra i workflow.",
                    target=dep,
                ))
        for step in wf.steps:
            # alcuni workflow (WF-MEM-EOD, WF-MEM-RETRO) hanno steps come lista
            # di stringhe prosa, non oggetti {id, gate, ...}: tollerante, si salta.
            if not isinstance(step, dict):
                continue
            g = step.get("gate")
            if g and g not in gate_ids:
                findings.append(Finding(
                    severity="warn", rule="FLOW-GATE-UNDECLARED", path=src,
                    message=f"step {step.get('id', '?')} di {wf_id} referenzia il gate {g!r}, "
                            f"non definito nella sezione gates: del file.",
                    target=g,
                ))

    if not spec.gates:
        findings.append(Finding(
            severity="warn", rule="FLOW-NO-GATES", path=src,
            message="nessun gate definito in workflows.yaml (sezione gates: assente o vuota).",
        ))

    for g in spec.gates:
        if g.type == "metric" and not g.green_if:
            findings.append(Finding(
                severity="block", rule="FLOW-GATE-NO-CRITERION", path=src,
                message=f"gate {g.id} è di tipo metric ma non ha green_if.", target=g.id,
            ))
        if g.type == "file" and not g.path:
            findings.append(Finding(
                severity="block", rule="FLOW-GATE-NO-PATH", path=src,
                message=f"gate {g.id} è di tipo file ma non ha path.", target=g.id,
            ))

    findings.sort(key=lambda f: (f.rank, f.rule))
    return findings
