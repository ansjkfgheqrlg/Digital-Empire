"""
MemoryWindow - Gestione sliding window + stima token
"""
from __future__ import annotations

import logging
from collections import deque
from typing import Any

logger = logging.getLogger("empire.memory")

def estimate_tokens(text: str) -> int:
    """Stima rough: 1 token ~ 4 chars (Claude-like)"""
    return max(1, len(text) // 4)

class MemoryWindow:
    """
    Gestisce la short-term memory con finestra scorrevole.
    System prompt è sempre fuori dalla window.
    """
    def __init__(self, max_messages: int = 10, max_tokens: int = 12000):
        if max_messages < 1:
            raise ValueError("max_messages >= 1")
        self.max_messages = max_messages
        self.max_tokens = max_tokens
        self._history: deque[dict[str, Any]] = deque()

    def append(self, message: dict[str, Any]) -> None:
        self._history.append(message)
        self._trim()

    def extend(self, messages: list[dict[str, Any]]) -> None:
        for m in messages:
            self._history.append(m)
        self._trim()

    def _trim(self) -> None:
        # Trim per numero messaggi
        while len(self._history) > self.max_messages:
            removed = self._history.popleft()
            logger.debug(f"MemoryWindow trim: removed {removed.get('role')}")

        # Trim per token budget (euristico)
        total = 0
        for msg in reversed(self._history):
            content = msg.get("content", "")
            if isinstance(content, list):
                text = "".join(
                    block.get("text", "") if isinstance(block, dict) else str(block)
                    for block in content
                )
            else:
                text = str(content)
            total += estimate_tokens(text)

        while total > self.max_tokens and len(self._history) > 2:
            removed = self._history.popleft()
            # ricalcola
            total = sum(
                estimate_tokens(str(m.get("content",""))) for m in self._history
            )

    def get_messages(self) -> list[dict[str, Any]]:
        return list(self._history)

    def clear(self) -> None:
        self._history.clear()
        logger.info("MemoryWindow cleared")

    def __len__(self) -> int:
        return len(self._history)

    def __bool__(self) -> bool:
        # Oggetto sempre truthy anche se vuoto, per evitare assert mute su __len__==0
        return True

    def __repr__(self) -> str:
        return f"MemoryWindow(len={len(self._history)}/{self.max_messages}, tokens_budget={self.max_tokens})"
