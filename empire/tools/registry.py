"""
ToolRegistry - MCP-like dispatcher locale
"""
from __future__ import annotations

import asyncio
import logging
from collections.abc import Awaitable, Callable
from dataclasses import dataclass, field
from typing import Any, TypedDict

logger = logging.getLogger("empire.tools")

class ToolResult(TypedDict):
    tool_use_id: str
    content: str
    is_error: bool

ToolHandler = Callable[..., Any]

@dataclass
class ToolDefinition:
    name: str
    description: str
    input_schema: dict[str, Any]
    handler: ToolHandler
    is_async: bool = False
    requires_approval: bool = False

class ToolRegistry:
    def __init__(self) -> None:
        self._tools: dict[str, ToolDefinition] = {}

    def register(self, tool: ToolDefinition) -> None:
        self._tools[tool.name] = tool
        logger.info(f"Tool registered: {tool.name}")

    def tool(self, name: str, description: str, input_schema: dict[str, Any], is_async: bool = False, requires_approval: bool = False):
        """Decorator per registrare tool rapidamente."""
        def decorator(fn: ToolHandler) -> ToolHandler:
            self.register(ToolDefinition(
                name=name,
                description=description,
                input_schema=input_schema,
                handler=fn,
                is_async=is_async,
                requires_approval=requires_approval
            ))
            return fn
        return decorator

    def get_anthropic_schemas(self, allowed: list[str] | None = None) -> list[dict[str, Any]]:
        tools = self._tools.values()
        if allowed:
            tools = [t for t in tools if t.name in allowed]
        return [
            {"name": t.name, "description": t.description, "input_schema": t.input_schema}
            for t in tools
        ]

    def list_names(self) -> list[str]:
        return list(self._tools.keys())

    def has(self, name: str) -> bool:
        return name in self._tools

    async def execute(self, name: str, tool_use_id: str, input_data: dict[str, Any]) -> ToolResult:
        if name not in self._tools:
            return ToolResult(
                tool_use_id=tool_use_id,
                content=f"Tool '{name}' non trovato. Disponibili: {self.list_names()}",
                is_error=True,
            )
        tool = self._tools[name]
        try:
            logger.info(f"▶️ EXEC {name} {input_data}")
            if tool.is_async:
                result = await tool.handler(**input_data)  # type: ignore
            else:
                result = await asyncio.to_thread(tool.handler, **input_data)

            content = str(result) if result is not None else "OK"
            # truncamento di sicurezza
            if len(content) > 8000:
                content = content[:8000] + "\n...[TRUNCATED]"

            return ToolResult(tool_use_id=tool_use_id, content=content, is_error=False)
        except Exception as e:
            logger.exception(f"Tool {name} failed")
            return ToolResult(tool_use_id=tool_use_id, content=f"TOOL ERROR {name}: {e}", is_error=True)
