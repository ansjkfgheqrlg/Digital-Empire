"""
EmpireKernel - Orchestratore multi-agente per Digital Empire OS
Gestisce routing, handoff, broadcast, e memoria condivisa
"""
from __future__ import annotations

import asyncio
import logging
import uuid
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from anthropic import AsyncAnthropic

from empire.config import Settings, get_settings
from empire.core.loader import AgentLoader
from empire.core.runner import AgentRunner
from empire.memory.sqlite_store import SQLiteStore
from empire.tools.registry import ToolRegistry
from empire.tools.builtins import register_all_builtin_tools

logger = logging.getLogger("empire.kernel")

@dataclass
class AgentTask:
    task_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    prompt: str = ""
    agent_name: str | None = None  # None = auto-routing
    session_id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])
    metadata: dict[str, Any] = field(default_factory=dict)

@dataclass
class TaskResult:
    task_id: str
    agent_name: str
    output: str
    success: bool = True
    error: str | None = None

class EmpireKernel:
    """
    Kernel centrale del OS:
    - Carica tutti gli agenti
    - Mantiene pool di runners
    - Routing intelligente (per nome o per ruolo)
    - Tool di delega inter-agente
    """

    def __init__(
        self,
        settings: Settings | None = None,
        client: AsyncAnthropic | None = None,
        store: SQLiteStore | None = None,
    ):
        self.settings = settings or get_settings()
        self.settings.ensure_dirs()
        self.client = client or AsyncAnthropic()
        self.store = store or SQLiteStore(self.settings.db_path)
        self.loader = AgentLoader(self.settings.agents_dir)

        self._runners: dict[str, AgentRunner] = {}
        self._global_registry = ToolRegistry()
        register_all_builtin_tools(self._global_registry)

        # Tool speciale: delegate_to_agent
        self._register_delegation_tool()

        logger.info("EmpireKernel initialized")

    def _register_delegation_tool(self) -> None:
        from empire.tools.registry import ToolDefinition

        async def delegate_to_agent(target_agent: str, task: str) -> str:
            """Delega task ad altro agente specializzato."""
            logger.info(f"Delegation request: {target_agent} -> {task[:100]}")
            try:
                result = await self.execute(AgentTask(prompt=task, agent_name=target_agent))
                return f"[Delega a {target_agent} completata]\n{result.output}"
            except Exception as e:
                return f"Delega fallita a {target_agent}: {e}"

        self._global_registry.register(ToolDefinition(
            name="delegate_to_agent",
            description="Delega un sotto-task ad un altro agente specializzato. Usalo per CTO, Marketing, Sales.",
            input_schema={
                "type": "object",
                "properties": {
                    "target_agent": {"type": "string", "description": "Nome agente target: es. 'CTO', 'Marketing', 'Vittorio'"},
                    "task": {"type": "string", "description": "Task da delegare, ben descritto"},
                },
                "required": ["target_agent", "task"],
            },
            handler=delegate_to_agent,
            is_async=True,
        ))

    def discover_agents(self) -> list[str]:
        return [p.stem for p in self.loader.discover()]

    def _get_or_create_runner(self, agent_name: str, session_id: str | None = None) -> AgentRunner:
        cache_key = f"{agent_name}:{session_id or 'default'}"
        if cache_key in self._runners:
            return self._runners[cache_key]

        parsed = self.loader.load_one(agent_name)
        runner = AgentRunner.from_file(
            parsed.source_path,
            session_id=session_id,
            tool_registry=self._global_registry,
            store=self.store,
            client=self.client,
            settings=self.settings,
        )
        self._runners[cache_key] = runner
        return runner

    def _auto_route(self, prompt: str) -> str:
        """Routing euristico semplice basato su keywords. In prod usa LLM classifier."""
        low = prompt.lower()
        agents = self.discover_agents()
        if not agents:
            raise RuntimeError("Nessun agente disponibile")

        # Mappatura keyword -> agente
        mapping = {
            "code": "cto",
            "tech": "cto",
            "bug": "cto",
            "marketing": "marketing",
            "vendite": "sales",
            "sales": "sales",
            "ceo": "ceo",
            "strateg": "ceo",
            "vittorio": "ceo",
        }
        for kw, target in mapping.items():
            if kw in low:
                # trova agente che match target
                for a in agents:
                    if target.lower() in a.lower():
                        return a
        # default: CEO o primo
        for a in agents:
            if "ceo" in a.lower() or "vittorio" in a.lower():
                return a
        return agents[0]

    async def execute(self, task: AgentTask) -> TaskResult:
        target_name = task.agent_name or self._auto_route(task.prompt)
        logger.info(f"Executing task {task.task_id} on {target_name}")

        try:
            runner = self._get_or_create_runner(target_name, task.session_id)
            # carica history persistita
            await runner.load_persisted_history()

            output = await runner.chat(task.prompt, stream_console=False)

            return TaskResult(
                task_id=task.task_id,
                agent_name=target_name,
                output=output,
                success=True,
            )
        except Exception as e:
            logger.exception(f"Task {task.task_id} failed")
            return TaskResult(
                task_id=task.task_id,
                agent_name=target_name,
                output="",
                success=False,
                error=str(e),
            )

    async def chat(
        self,
        message: str,
        agent_name: str | None = None,
        session_id: str | None = None,
        stream: bool = True,
    ) -> str:
        target = agent_name or self._auto_route(message)
        runner = self._get_or_create_runner(target, session_id)
        await runner.load_persisted_history()
        return await runner.chat(message, stream_console=stream)

    async def broadcast(self, message: str, session_id: str | None = None) -> dict[str, TaskResult]:
        """Invia stesso prompt a tutti gli agenti in parallelo."""
        agents = self.discover_agents()
        tasks = [
            AgentTask(prompt=message, agent_name=agent, session_id=session_id or str(uuid.uuid4())[:8])
            for agent in agents
        ]
        results = await asyncio.gather(*(self.execute(t) for t in tasks))
        return {r.agent_name: r for r in results}

    def list_runners(self) -> list[str]:
        return list(self._runners.keys())

    async def clear_all_sessions(self) -> None:
        # placeholder per cleanup
        for runner in self._runners.values():
            runner.clear_memory(clear_persisted=True)
