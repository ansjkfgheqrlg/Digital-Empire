from __future__ import annotations

from typing import Protocol

from orchestrator.runtime.models import AgentResult, TaskAssignment


class AgentRuntimePort(Protocol):
    async def execute(self, assignment: TaskAssignment) -> AgentResult: ...
