from __future__ import annotations

import time
from collections.abc import Awaitable, Callable

from .models import AgentResult, TaskAssignment, Usage


AgentHandler = Callable[[TaskAssignment], Awaitable[AgentResult]]


class LocalAgentRuntime:
    """Deterministic baseline runtime. It cannot spawn agents or call tools itself."""

    def __init__(self):
        self._handlers: dict[str, AgentHandler] = {}

    def register(self, role: str, handler: AgentHandler) -> None:
        if role in self._handlers:
            raise ValueError(f"Handler already registered for role: {role}")
        self._handlers[role] = handler

    async def execute(self, assignment: TaskAssignment) -> AgentResult:
        handler = self._handlers.get(assignment.role)
        if handler is None:
            return AgentResult(
                task_id=assignment.task_id,
                status="FAILED",
                output={},
                failure={"code": "RUN_ROLE_UNAVAILABLE", "role": assignment.role},
            )
        if not 1 <= assignment.timeout_seconds <= 300:
            return AgentResult(
                task_id=assignment.task_id,
                status="FAILED",
                output={},
                failure={"code": "BUD_TIMEOUT_INVALID"},
            )
        started = time.perf_counter()
        result = await handler(assignment)
        duration = int((time.perf_counter() - started) * 1000)
        return AgentResult(
            task_id=result.task_id,
            status=result.status,
            output=result.output,
            claims=result.claims,
            usage=Usage(
                tokens_in=result.usage.tokens_in,
                tokens_out=result.usage.tokens_out,
                cost_usd=result.usage.cost_usd,
                duration_ms=duration,
            ),
            failure=result.failure,
        )
