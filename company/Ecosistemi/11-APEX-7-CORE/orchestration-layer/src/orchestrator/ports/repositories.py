from __future__ import annotations

from typing import Protocol

from orchestrator.domain.events import DomainEvent
from orchestrator.domain.workflow import Workflow


class WorkflowRepositoryPort(Protocol):
    async def add(self, workflow: Workflow, trace_id: str) -> str: ...
    async def get(self, workflow_id: str) -> dict | None: ...
    async def persist_transition(
        self,
        workflow: Workflow,
        previous_version: int,
        event: DomainEvent,
        trace_id: str,
    ) -> None: ...
