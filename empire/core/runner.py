"""
AgentRunner v2 - Core runtime con memoria persistente + tools
Evoluzione del file singolo agent_runner.py, ora modulare e production-grade
"""
from __future__ import annotations

import asyncio
import logging
import uuid
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, AsyncGenerator

from anthropic import APIError, AsyncAnthropic
from anthropic.types import Message, ToolUseBlock

from empire.config import Settings, get_settings
from empire.memory.sqlite_store import SQLiteStore
from empire.memory.window import MemoryWindow
from empire.parser import ParsedAgentFile, parse_hybrid_agent_file
from empire.tools.builtins import register_all_builtin_tools
from empire.tools.registry import ToolRegistry

logger = logging.getLogger("empire.runner")

@dataclass
class AgentRunner:
    """
    Runner per singolo agente con:
    - system_prompt fisso
    - MemoryWindow short-term
    - SQLiteStore long-term persistence
    - ToolRegistry MCP
    - Async streaming + tool loop
    """
    system_prompt: str
    agent_name: str = "Agent"
    agent_role: str = "Generic"
    metadata: dict[str, Any] = field(default_factory=dict)
    model: str = "claude-3-5-sonnet-20241022"
    max_history: int = 10
    max_tool_iterations: int = 5
    session_id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])
    tool_registry: ToolRegistry | None = None
    memory_window: MemoryWindow | None = None
    store: SQLiteStore | None = None
    client: AsyncAnthropic | None = None
    settings: Settings = field(default_factory=get_settings)

    _client_owned: bool = field(default=False, init=False, repr=False)

    def __post_init__(self) -> None:
        if not self.system_prompt:
            raise ValueError("system_prompt vuoto")

        self.settings.ensure_dirs()

        if self.client is None:
            self.client = AsyncAnthropic()
            self._client_owned = True

        if self.tool_registry is None:
            reg = ToolRegistry()
            register_all_builtin_tools(reg)
            self.tool_registry = reg

        if self.memory_window is None:
            self.memory_window = MemoryWindow(max_messages=self.max_history)

        if self.store is None and self.settings.enable_persistence:
            self.store = SQLiteStore(self.settings.db_path)

        logger.info(f"[{self.agent_name}] Runner init | model={self.model} | session={self.session_id} | tools={self.tool_registry.list_names() if self.tool_registry else []}")

    @classmethod
    def from_file(
        cls,
        file_path: Path | str,
        session_id: str | None = None,
        tool_registry: ToolRegistry | None = None,
        store: SQLiteStore | None = None,
        client: AsyncAnthropic | None = None,
        model_override: str | None = None,
        settings: Settings | None = None,
    ) -> AgentRunner:
        parsed = parse_hybrid_agent_file(file_path)
        st = settings or get_settings()

        # Filtra tool se metadata contiene allowed list
        base_registry = tool_registry
        if base_registry is None:
            base_registry = ToolRegistry()
            register_all_builtin_tools(base_registry)

        if parsed.allowed_tools:
            filtered = ToolRegistry()
            for name in parsed.allowed_tools:
                if base_registry.has(name):
                    filtered._tools[name] = base_registry._tools[name]  # type: ignore
                else:
                    logger.warning(f"Tool {name} richiesto da {parsed.name} non esiste")
            base_registry = filtered

        return cls(
            system_prompt=parsed.system_prompt,
            agent_name=parsed.name,
            agent_role=parsed.role,
            metadata=parsed.metadata,
            model=model_override or parsed.model or st.default_model,
            max_history=parsed.max_history,
            max_tool_iterations=st.max_tool_iterations,
            session_id=session_id or str(uuid.uuid4())[:8],
            tool_registry=base_registry,
            store=store,
            client=client,
            settings=st,
        )

    async def load_persisted_history(self) -> None:
        """Carica history da SQLite in MemoryWindow."""
        if not self.store or not self.memory_window:
            return
        history = await self.store.load_history(self.agent_name, self.session_id, limit=self.max_history)
        self.memory_window.clear()
        self.memory_window.extend(history)
        logger.info(f"[{self.agent_name}] Loaded {len(history)} persisted messages")

    async def _save_message(self, role: str, content: Any) -> None:
        if self.store:
            try:
                await self.store.save_message(self.agent_name, self.session_id, role, content)
            except Exception as e:
                logger.warning(f"Persist failed: {e}")

    async def _dispatch_tools(self, tool_blocks: list[ToolUseBlock]) -> list[dict[str, Any]]:
        assert self.tool_registry
        results = []
        for block in tool_blocks:
            res = await self.tool_registry.execute(block.name, block.id, block.input)  # type: ignore
            results.append({
                "type": "tool_result",
                "tool_use_id": res["tool_use_id"],
                "content": res["content"],
                "is_error": res["is_error"],
            })
        return results

    async def chat(
        self,
        user_message: str,
        stream_console: bool = True,
        persist: bool = True,
    ) -> str:
        """
        Chat async con streaming + tool agentic loop.
        Ritorna risposta finale.
        """
        if not user_message.strip():
            raise ValueError("user_message vuoto")

        assert self.memory_window and self.tool_registry and self.client

        # Save user msg
        if persist:
            await self._save_message("user", user_message)

        self.memory_window.append({"role": "user", "content": user_message})

        final_answer = ""

        for iteration in range(self.max_tool_iterations):
            try:
                anthropic_tools = self.tool_registry.get_anthropic_schemas()

                async with self.client.messages.stream(
                    model=self.model,
                    max_tokens=4096,
                    system=self.system_prompt,
                    messages=self.memory_window.get_messages(),
                    tools=anthropic_tools if anthropic_tools else None,  # type: ignore
                ) as stream:
                    current_text = ""
                    async for text in stream.text_stream:
                        current_text += text
                        if stream_console:
                            print(text, end="", flush=True)
                    if stream_console and current_text:
                        print()

                    final_message: Message = await stream.get_final_message()

            except APIError as e:
                logger.error(f"Anthropic API error: {e}")
                raise
            except Exception as e:
                logger.exception("Unexpected chat error")
                raise RuntimeError(f"Chat failed: {e}") from e

            # Parse blocks
            tool_blocks: list[ToolUseBlock] = [
                b for b in final_message.content if getattr(b, "type", None) == "tool_use"  # type: ignore
            ]
            text_blocks = [getattr(b, "text", "") for b in final_message.content if getattr(b, "type", None) == "text"]  # type: ignore
            iteration_text = "".join(text_blocks)

            # Build assistant content for history (deve contenere raw tool_use)
            assistant_payload: list[dict[str, Any]] = []
            for b in final_message.content:
                if b.type == "text":  # type: ignore
                    assistant_payload.append({"type": "text", "text": b.text})  # type: ignore
                elif b.type == "tool_use":  # type: ignore
                    assistant_payload.append({
                        "type": "tool_use",
                        "id": b.id,  # type: ignore
                        "name": b.name,  # type: ignore
                        "input": b.input,  # type: ignore
                    })

            self.memory_window.append({"role": "assistant", "content": assistant_payload})
            if persist:
                await self._save_message("assistant", assistant_payload)

            if not tool_blocks:
                final_answer = iteration_text
                break

            if stream_console:
                print(f"\n[🔧 {self.agent_name}] {len(tool_blocks)} tool → eseguo: {[b.name for b in tool_blocks]}\n")  # type: ignore

            tool_results = await self._dispatch_tools(tool_blocks)  # type: ignore
            # Save & append tool results come user
            self.memory_window.append({"role": "user", "content": tool_results})
            if persist:
                await self._save_message("user", tool_results)
        else:
            logger.warning(f"Max tool iterations reached {self.max_tool_iterations}")

        return final_answer or iteration_text  # type: ignore

    async def chat_stream(self, user_message: str) -> AsyncGenerator[str, None]:
        """
        Versione generator che yields chunks per UI/API
        """
        # Simplified: riusa chat ma yields - per brevità qui facciamo wrapper non-stream
        # In prod, duplica logicissima ma con yield dentro text_stream
        response = await self.chat(user_message, stream_console=False)
        # Yield a pezzi per simulare stream
        chunk_size = 30
        for i in range(0, len(response), chunk_size):
            yield response[i:i+chunk_size]
            await asyncio.sleep(0.02)

    def clear_memory(self, clear_persisted: bool = False) -> None:
        assert self.memory_window
        self.memory_window.clear()
        if clear_persisted and self.store:
            asyncio.create_task(self.store.clear_session(self.agent_name, self.session_id))

    @property
    def history(self) -> list[dict[str, Any]]:
        return self.memory_window.get_messages() if self.memory_window else []
