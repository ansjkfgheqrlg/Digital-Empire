from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class RiskClass(str, Enum):
    R0 = "R0"
    R1 = "R1"
    R2 = "R2"
    R3 = "R3"


class WorkItemStatus(str, Enum):
    CREATED = "CREATED"
    SCOPED = "SCOPED"
    DESIGNED = "DESIGNED"
    IMPLEMENTING = "IMPLEMENTING"
    TESTING = "TESTING"
    SECURITY_REVIEW = "SECURITY_REVIEW"
    GATE_REVIEW = "GATE_REVIEW"
    READY_TO_MERGE = "READY_TO_MERGE"
    REMEDIATING = "REMEDIATING"
    FROZEN = "FROZEN"
    REJECTED = "REJECTED"


@dataclass(frozen=True)
class AgentSpec:
    agent_id: str
    role: str
    responsibility: str
    produces: tuple[str, ...]
    reads: tuple[str, ...]
    writes: tuple[str, ...]
    denied: tuple[str, ...]
    timeout_minutes: int
    max_retries: int
    prompt_file: str
    can_approve: tuple[str, ...] = ()


@dataclass(frozen=True)
class GateCriterion:
    criterion_id: str
    description: str
    blocking: bool
    evidence_required: tuple[str, ...]


@dataclass(frozen=True)
class GateSpec:
    gate_id: str
    owner_agent: str
    maximum_attempts: int
    criteria: tuple[GateCriterion, ...]


@dataclass(frozen=True)
class TeamConfig:
    team_id: str
    version: str
    max_wip: int
    max_concurrency: int
    agents: tuple[AgentSpec, ...]


@dataclass
class WorkItem:
    work_item_id: str
    title: str
    risk: RiskClass
    status: WorkItemStatus = WorkItemStatus.CREATED
    attempt: int = 0
    author_agent: str | None = None
    required_gates: list[str] = field(default_factory=list)
    stages: list[dict[str, Any]] = field(default_factory=list)


class ManifestError(ValueError):
    """Raised when a builder-team manifest violates a governance invariant."""
