"""
Shell tools - esecuzione script e comandi con sandbox
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path
from typing import TYPE_CHECKING

from empire.config import get_settings

if TYPE_CHECKING:
    from empire.tools.registry import ToolRegistry

def _ensure_inside_project(target: Path) -> None:
    settings = get_settings()
    if not settings.sandbox_enabled:
        return
    proj = settings.project_root.resolve()
    try:
        target.resolve().relative_to(proj)
    except ValueError:
        raise PermissionError(f"Esecuzione negata fuori da project_root: {target}")

def run_local_script(script_path: str, args: str = "") -> str:
    """
    Esegue script Python locale in workspace_scripts
    """
    settings = get_settings()
    base = settings.workspace_dir
    target = (base / script_path).resolve()
    # fallback se utente passa path da root
    if not target.exists():
        # prova anche da project_root
        alt = (settings.project_root / script_path).resolve()
        if alt.exists():
            target = alt
    if not target.exists():
        raise FileNotFoundError(f"Script non trovato: {script_path} (cercato in {base})")
    _ensure_inside_project(target)

    if target.suffix not in settings.allowed_script_extensions:
        raise ValueError(f"Estensione non permessa: {target.suffix}. Permesse: {settings.allowed_script_extensions}")

    cmd = [sys.executable, str(target)] + (args.split() if args else [])
    try:
        proc = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=settings.shell_timeout,
            cwd=str(settings.project_root),
        )
        out = f"EXIT:{proc.returncode}\nSTDOUT:\n{proc.stdout}\nSTDERR:\n{proc.stderr}"
        return out[: settings.max_tool_output_chars]
    except subprocess.TimeoutExpired:
        raise TimeoutError(f"Timeout {settings.shell_timeout}s per {script_path}")

def run_shell_command(command: str) -> str:
    """Esegue comando shell limitato (whitelist base)."""
    settings = get_settings()
    # blacklist super pericolosa
    forbidden = ["rm -rf /", ":(){:|:&};:", "mkfs", "dd if=", "> /dev/sda"]
    for f in forbidden:
        if f in command:
            raise PermissionError(f"Comando proibito: {f}")

    if settings.sandbox_enabled and ("sudo" in command or "chmod 777" in command):
        raise PermissionError("Comandi sudo/chmod 777 non permessi in sandbox")

    try:
        proc = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=settings.shell_timeout,
            cwd=str(settings.project_root),
        )
        out = f"EXIT:{proc.returncode}\n{proc.stdout}\n{proc.stderr}"
        return out[: settings.max_tool_output_chars]
    except subprocess.TimeoutExpired:
        raise TimeoutError("Timeout comando shell")

def register_shell_tools(registry: ToolRegistry) -> None:
    from empire.tools.registry import ToolDefinition

    if not registry.has("run_local_script"):
        registry.register(ToolDefinition(
            name="run_local_script",
            description="Esegue script Python locale in workspace_scripts. Es: 'report/sales.py'",
            input_schema={
                "type": "object",
                "properties": {
                    "script_path": {"type": "string", "description": "Path relativo in workspace_scripts"},
                    "args": {"type": "string", "description": "Argomenti opzionali"},
                },
                "required": ["script_path"],
            },
            handler=run_local_script,
        ))
    if not registry.has("run_shell_command"):
        registry.register(ToolDefinition(
            name="run_shell_command",
            description="Esegue comando shell sandboxato (ls, cat, python -c, etc). No sudo.",
            input_schema={
                "type": "object",
                "properties": {"command": {"type": "string"}},
                "required": ["command"],
            },
            handler=run_shell_command,
            requires_approval=True,
        ))
