"""
System tools - status, time, memory
"""
from __future__ import annotations

import json
import platform
from datetime import datetime, timezone
from typing import TYPE_CHECKING

from empire.config import get_settings

if TYPE_CHECKING:
    from empire.tools.registry import ToolRegistry

def get_system_status() -> str:
    settings = get_settings()
    data = {
        "system": platform.system(),
        "release": platform.release(),
        "python": platform.python_version(),
        "project_root": str(settings.project_root),
        "agents_dir": str(settings.agents_dir),
        "workspace_dir": str(settings.workspace_dir),
        "db_exists": settings.db_path.exists(),
        "digital_empire": "ONLINE",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
    return json.dumps(data, indent=2)

def get_current_time() -> str:
    return datetime.now(timezone.utc).isoformat() + " | Local: " + datetime.now().astimezone().isoformat()

def get_agent_list() -> str:
    settings = get_settings()
    agents = list(settings.agents_dir.glob("*.md"))
    return json.dumps([{"name": p.stem, "file": str(p)} for p in agents], indent=2)

def register_system_tools(registry: ToolRegistry) -> None:
    from empire.tools.registry import ToolDefinition

    if not registry.has("get_system_status"):
        registry.register(ToolDefinition(
            name="get_system_status",
            description="Ritorna stato sistema Digital Empire",
            input_schema={"type": "object", "properties": {}, "required": []},
            handler=get_system_status,
        ))
    if not registry.has("get_current_time"):
        registry.register(ToolDefinition(
            name="get_current_time",
            description="Ritorna data/ora UTC e locale",
            input_schema={"type": "object", "properties": {}, "required": []},
            handler=get_current_time,
        ))
    if not registry.has("get_agent_list"):
        registry.register(ToolDefinition(
            name="get_agent_list",
            description="Lista agenti disponibili nel sistema",
            input_schema={"type": "object", "properties": {}, "required": []},
            handler=get_agent_list,
        ))
