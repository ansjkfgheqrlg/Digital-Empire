"""
Filesystem tools - sandboxed su workspace_dir
"""
from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

from empire.config import get_settings

if TYPE_CHECKING:
    from empire.tools.registry import ToolRegistry

def _safe_resolve(base: Path, user_path: str) -> Path:
    """Risolve path evitando traversal attack."""
    settings = get_settings()
    base_resolved = base.resolve()
    target = (base / user_path).resolve()
    # Se sandbox disabilitata, allow
    if not settings.sandbox_enabled:
        return target
    # Check che sia dentro project_root
    project_root = settings.project_root.resolve()
    try:
        target.relative_to(project_root)
    except ValueError:
        raise PermissionError(f"Accesso negato fuori da project_root: {user_path}")
    return target

def read_file(path: str) -> str:
    settings = get_settings()
    target = _safe_resolve(settings.project_root, path)
    if not target.exists():
        raise FileNotFoundError(f"File non trovato: {path}")
    if target.stat().st_size > 500_000:
        raise ValueError(f"File troppo grande (>500KB): {path}")
    return target.read_text(encoding="utf-8", errors="ignore")

def write_file(path: str, content: str) -> str:
    settings = get_settings()
    target = _safe_resolve(settings.project_root, path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")
    return f"Written {len(content)} chars to {path}"

def list_directory(path: str = ".") -> str:
    settings = get_settings()
    target = _safe_resolve(settings.project_root, path)
    if not target.exists():
        raise FileNotFoundError(f"Dir non trovata: {path}")
    if not target.is_dir():
        raise NotADirectoryError(f"Non è una directory: {path}")
    items = []
    for child in sorted(target.iterdir())[:100]:
        t = "DIR" if child.is_dir() else "FILE"
        items.append(f"{t:4} {child.name}")
    return "\n".join(items) or "(vuota)"

def delete_file(path: str) -> str:
    settings = get_settings()
    target = _safe_resolve(settings.project_root, path)
    if not target.exists():
        return f"File già assente: {path}"
    # Safety: non permettere delete fuori workspace/data/agents
    allowed_prefixes = [settings.workspace_dir, settings.data_dir, settings.agents_dir]
    if settings.sandbox_enabled:
        if not any(str(target.resolve()).startswith(str(p.resolve())) for p in allowed_prefixes):
            raise PermissionError(f"Delete consentito solo in workspace/data/agents, non in {path}")
    target.unlink()
    return f"Deleted {path}"

def register_filesystem_tools(registry: ToolRegistry) -> None:
    registry.register(
        registry._tools.get("read_file")  # dummy to avoid duplicate check
        if False else __import__("empire.tools.registry", fromlist=["ToolDefinition"]).ToolDefinition(
            name="read_file",
            description="Legge un file di testo dal workspace (sandboxed). Max 500KB.",
            input_schema={
                "type": "object",
                "properties": {"path": {"type": "string", "description": "Path relativo, es. 'agents/ceo_agent.md'"}},
                "required": ["path"],
            },
            handler=read_file,
        )
    )
    # The above trick avoids circular. Let's properly register below:

    from empire.tools.registry import ToolDefinition

    # Se già registrato, skip
    if not registry.has("read_file"):
        registry.register(ToolDefinition(
            name="read_file",
            description="Legge un file di testo dal workspace (sandboxed). Max 500KB.",
            input_schema={
                "type": "object",
                "properties": {"path": {"type": "string", "description": "Path relativo da project root"}},
                "required": ["path"],
            },
            handler=read_file,
        ))
    if not registry.has("write_file"):
        registry.register(ToolDefinition(
            name="write_file",
            description="Scrive un file nel workspace. Crea directory se necessario.",
            input_schema={
                "type": "object",
                "properties": {
                    "path": {"type": "string"},
                    "content": {"type": "string", "description": "Contenuto file"},
                },
                "required": ["path", "content"],
            },
            handler=write_file,
        ))
    if not registry.has("list_directory"):
        registry.register(ToolDefinition(
            name="list_directory",
            description="Lista file e cartelle in una directory del workspace.",
            input_schema={
                "type": "object",
                "properties": {"path": {"type": "string", "default": "."}},
                "required": [],
            },
            handler=list_directory,
        ))
    if not registry.has("delete_file"):
        registry.register(ToolDefinition(
            name="delete_file",
            description="Elimina un file (solo in workspace/data/agents).",
            input_schema={
                "type": "object",
                "properties": {"path": {"type": "string"}},
                "required": ["path"],
            },
            handler=delete_file,
            requires_approval=True,
        ))
