"""
Parser - File ibridi Markdown/YAML per identità agente
"""
from __future__ import annotations

import logging
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

logger = logging.getLogger("empire.parser")

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n(.*)", re.DOTALL)

class AgentFileParseError(Exception):
    pass

@dataclass(frozen=True, slots=True)
class ParsedAgentFile:
    metadata: dict[str, Any]
    system_prompt: str
    source_path: Path

    @property
    def name(self) -> str:
        return str(self.metadata.get("name", self.source_path.stem))

    @property
    def role(self) -> str:
        return str(self.metadata.get("role", "Generic Agent"))

    @property
    def model(self) -> str:
        return str(self.metadata.get("model", "claude-3-5-sonnet-20241022"))

    @property
    def max_history(self) -> int:
        return int(self.metadata.get("max_history", 10))

    @property
    def allowed_tools(self) -> list[str] | None:
        tools = self.metadata.get("tools")
        if tools is None:
            return None
        return [str(t) for t in tools]

    @property
    def description(self) -> str:
        return str(self.metadata.get("description", ""))


def parse_hybrid_agent_file(file_path: Path | str) -> ParsedAgentFile:
    path = Path(file_path)
    if not path.exists():
        raise AgentFileParseError(f"File non trovato: {path}")

    raw = path.read_text(encoding="utf-8")
    if not raw.strip():
        raise AgentFileParseError(f"File vuoto: {path}")

    match = FRONTMATTER_RE.match(raw.strip())
    if not match:
        logger.warning(f"No frontmatter in {path.name}, treating all as prompt")
        return ParsedAgentFile(metadata={}, system_prompt=raw.strip(), source_path=path)

    yaml_raw, md_body = match.groups()
    try:
        meta = yaml.safe_load(yaml_raw) or {}
        if not isinstance(meta, dict):
            raise AgentFileParseError("Frontmatter deve essere dict")
    except yaml.YAMLError as e:
        raise AgentFileParseError(f"YAML invalido in {path.name}: {e}") from e

    body = md_body.strip()
    if not body:
        raise AgentFileParseError(f"System prompt vuoto in {path.name}")

    return ParsedAgentFile(metadata=meta, system_prompt=body, source_path=path)
