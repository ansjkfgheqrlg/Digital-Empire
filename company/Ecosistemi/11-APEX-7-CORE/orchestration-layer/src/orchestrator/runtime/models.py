from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class TaskAssignment:
    workflow_id: str
    task_id: str
    role: str
    objective: str
    allowed_capabilities: tuple[str, ...]
    context: dict[str, Any]
    max_tokens: int
    timeout_seconds: int
    max_cost_usd: float
    output_schema: str


@dataclass(frozen=True)
class Usage:
    tokens_in: int = 0
    tokens_out: int = 0
    cost_usd: float = 0.0
    duration_ms: int = 0


@dataclass(frozen=True)
class AgentResult:
    task_id: str
    status: str
    output: dict[str, Any]
    claims: tuple[dict[str, Any], ...] = ()
    usage: Usage = field(default_factory=Usage)
    failure: dict[str, Any] | None = None
