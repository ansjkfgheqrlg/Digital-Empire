from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Protocol

from orchestrator.governance.grants import CapabilityGrantService, GrantBinding, GrantDenied


class ToolGatewayError(RuntimeError):
    pass


@dataclass(frozen=True)
class ToolRequest:
    operation: str
    capability: str
    token: str
    binding: GrantBinding
    arguments: dict[str, Any]


class ToolHandler(Protocol):
    async def execute(self, arguments: dict[str, Any], constraints: dict[str, Any]) -> dict: ...


class ToolGateway:
    """The only component allowed to turn a capability grant into a tool call."""

    def __init__(self, grant_service: CapabilityGrantService):
        self.grant_service = grant_service
        self._handlers: dict[str, ToolHandler] = {}

    def register(self, operation: str, handler: ToolHandler) -> None:
        if operation in self._handlers:
            raise ValueError(f"Tool operation already registered: {operation}")
        self._handlers[operation] = handler

    async def execute(self, request: ToolRequest) -> dict:
        handler = self._handlers.get(request.operation)
        if handler is None:
            raise ToolGatewayError("Unknown tool operation")
        try:
            grant = await self.grant_service.consume(
                request.token,
                request.binding,
                request.capability,
            )
        except GrantDenied as exc:
            raise ToolGatewayError(str(exc)) from exc
        try:
            return await handler.execute(request.arguments, grant.constraints)
        except Exception as exc:
            # The token is intentionally already consumed. Retry requires a fresh grant.
            raise ToolGatewayError(f"Tool execution failed: {type(exc).__name__}: {exc}") from exc
