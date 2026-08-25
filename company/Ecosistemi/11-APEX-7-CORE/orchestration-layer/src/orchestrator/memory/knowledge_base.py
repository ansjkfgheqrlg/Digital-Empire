from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class KnowledgeEntry:
    entry_id: str
    topic: str
    content: str
    tags: tuple[str, ...]


class KnowledgeBase:
    def __init__(self, memory_dir: Path):
        self.memory_dir = memory_dir
        self._entries: dict[str, KnowledgeEntry] = {}
        self.load()

    def load(self) -> None:
        if not self.memory_dir.exists():
            return
        rules_dir = self.memory_dir / "rules"
        if rules_dir.exists():
            for file in rules_dir.glob("*.json"):
                data = json.loads(file.read_text(encoding="utf-8"))
                for rule in data.get("rules", []):
                    entry = KnowledgeEntry(
                        entry_id=rule["id"],
                        topic=data.get("category", file.stem),
                        content=rule["statement"],
                        tags=tuple(rule.get("tags", [data.get("category", file.stem)])),
                    )
                    self._entries[entry.entry_id] = entry

    def search(self, query: str) -> list[KnowledgeEntry]:
        q_lower = query.lower()
        matches = []
        for entry in self._entries.values():
            if (
                q_lower in entry.topic.lower()
                or q_lower in entry.content.lower()
                or any(q_lower in tag.lower() for tag in entry.tags)
            ):
                matches.append(entry)
        return matches

    def get_entry(self, entry_id: str) -> KnowledgeEntry | None:
        return self._entries.get(entry_id)
