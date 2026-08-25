from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Optional

from orchestrator.quality.patterns import FILLER_PATTERNS
from orchestrator.quality.tes import TESReport, calculate_tes

NUMBER_RE = re.compile(r"(?<!\w)\d+(?:[.,]\d+)?%?(?!\w)")
NEGATION_RE = re.compile(r"\b(?:non|nessun[oa]?|mai|vietat[oa]|senza)\b", re.I)
CODE_RE = re.compile(r"`[^`]+`|```.*?```", re.S)
WARNING_RE = re.compile(
    r"[^.!?\n]*\b(?:warning|attenzione|limite|vietato|errore)\b[^.!?\n]*[.!?]?",
    re.I,
)


@dataclass(frozen=True)
class NerveSaveResult:
    text: str
    original_length: int
    final_length: int
    protected_spans: tuple[str, ...]
    preservation_pass: bool
    tes_report: Optional[TESReport] = None

    @property
    def compression_ratio(self) -> float:
        return self.final_length / max(self.original_length, 1)


def _protected(text: str) -> tuple[str, ...]:
    values = []
    for pattern in (CODE_RE, WARNING_RE, NUMBER_RE, NEGATION_RE):
        values.extend(match.group(0) for match in pattern.finditer(text))
    return tuple(dict.fromkeys(values))


def compress_verified_output(
    text: str,
    expected_concepts: Optional[int] = None,
) -> NerveSaveResult:
    """Conservative post-verification compression with exact protected-span checks and full v2.0 filler elimination."""
    protected = _protected(text)
    compressed = text

    # Eliminate all filler patterns by category
    for cat, patterns in FILLER_PATTERNS.items():
        for pat in patterns:
            compressed = re.sub(pat, "", compressed, flags=re.IGNORECASE)

    compressed = re.sub(r"[ \t]{2,}", " ", compressed)
    compressed = re.sub(r"\n{3,}", "\n\n", compressed).strip()

    preservation = all(span in compressed for span in protected)
    if not preservation:
        compressed = text.strip()

    tes_report = calculate_tes(compressed, expected_concepts=expected_concepts)

    return NerveSaveResult(
        text=compressed,
        original_length=len(text),
        final_length=len(compressed),
        protected_spans=protected,
        preservation_pass=preservation,
        tes_report=tes_report,
    )
