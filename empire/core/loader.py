"""
AgentLoader - carica tutti gli agenti da directory
"""
from __future__ import annotations

import logging
from pathlib import Path
from typing import TYPE_CHECKING

from empire.config import get_settings
from empire.parser import ParsedAgentFile, parse_hybrid_agent_file, AgentFileParseError

if TYPE_CHECKING:
    pass

logger = logging.getLogger("empire.loader")

class AgentLoader:
    def __init__(self, agents_dir: Path | str | None = None):
        settings = get_settings()
        self.agents_dir = Path(agents_dir) if agents_dir else settings.agents_dir
        self.agents_dir.mkdir(parents=True, exist_ok=True)

    def discover(self) -> list[Path]:
        """Ritorna lista file .md agenti."""
        return sorted(self.agents_dir.glob("*.md"))

    def load_all(self) -> dict[str, ParsedAgentFile]:
        """Carica tutti gli agenti, skip su errore."""
        result: dict[str, ParsedAgentFile] = {}
        for path in self.discover():
            try:
                parsed = parse_hybrid_agent_file(path)
                result[parsed.name] = parsed
                logger.info(f"Loaded agent {parsed.name} from {path.name}")
            except AgentFileParseError as e:
                logger.warning(f"Skip {path.name}: {e}")
        return result

    def load_one(self, name_or_path: str) -> ParsedAgentFile:
        """Carica singolo agente per nome o path."""
        p = Path(name_or_path)
        if p.exists():
            return parse_hybrid_agent_file(p)
        # cerca per nome
        candidate = self.agents_dir / f"{name_or_path}.md"
        if candidate.exists():
            return parse_hybrid_agent_file(candidate)
        candidate = self.agents_dir / name_or_path
        if candidate.exists():
            return parse_hybrid_agent_file(candidate)
        # cerca case-insensitive
        for path in self.discover():
            parsed = parse_hybrid_agent_file(path)
            if parsed.name.lower() == name_or_path.lower():
                return parsed
        raise FileNotFoundError(f"Agente non trovato: {name_or_path}")
