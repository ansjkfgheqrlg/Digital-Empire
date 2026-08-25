"""NERVE-SAVE :: classifier.py
FASE 0 + FASE 1: Intent Compression Engine + Economy Classifier.
Analizza query -> assegna intent, livello, formato, budget.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from enum import Enum

from orchestrator.quality.patterns import (
    ESCALATION_TRIGGERS,
    INTENT_PATTERNS,
    LEVEL_BUDGETS,
)


class TokenLevel(Enum):
    MICRO = 1
    MEDIO = 2
    ALTO = 3
    MASSIMO = 4


class IntentType(Enum):
    CONFERMA = "conferma"
    INFO_PUNTUALE = "info_puntuale"
    HOW_TO = "how_to"
    DEBUG = "debug"
    ARCHITETTURA = "architettura"
    CODICE = "codice"
    COMPARAZIONE = "comparazione"
    SPIEGAZIONE = "spiegazione"
    DOCUMENTO = "documento"


class OutputFormat(Enum):
    PROSA_DIRETTA = "prosa_diretta"
    BULLET_LIST = "bullet_list"
    LISTA_ORDINATA = "lista_ordinata"
    TABELLA = "tabella"
    CODICE = "codice"
    STRUTTURA = "struttura_gerarchica"
    DOCUMENTO = "documento_completo"


INTENT_TO_LEVEL: dict[IntentType, TokenLevel] = {
    IntentType.CONFERMA: TokenLevel.MICRO,
    IntentType.INFO_PUNTUALE: TokenLevel.MICRO,
    IntentType.HOW_TO: TokenLevel.MEDIO,
    IntentType.DEBUG: TokenLevel.MEDIO,
    IntentType.SPIEGAZIONE: TokenLevel.MEDIO,
    IntentType.COMPARAZIONE: TokenLevel.MEDIO,
    IntentType.ARCHITETTURA: TokenLevel.ALTO,
    IntentType.CODICE: TokenLevel.ALTO,
    IntentType.DOCUMENTO: TokenLevel.MASSIMO,
}

INTENT_TO_FORMAT: dict[IntentType, OutputFormat] = {
    IntentType.CONFERMA: OutputFormat.PROSA_DIRETTA,
    IntentType.INFO_PUNTUALE: OutputFormat.PROSA_DIRETTA,
    IntentType.HOW_TO: OutputFormat.LISTA_ORDINATA,
    IntentType.DEBUG: OutputFormat.BULLET_LIST,
    IntentType.SPIEGAZIONE: OutputFormat.PROSA_DIRETTA,
    IntentType.COMPARAZIONE: OutputFormat.TABELLA,
    IntentType.ARCHITETTURA: OutputFormat.STRUTTURA,
    IntentType.CODICE: OutputFormat.CODICE,
    IntentType.DOCUMENTO: OutputFormat.DOCUMENTO,
}

INTENT_TOKEN_RANGES: dict[IntentType, tuple[int, int]] = {
    IntentType.CONFERMA: (1, 30),
    IntentType.INFO_PUNTUALE: (10, 50),
    IntentType.HOW_TO: (50, 150),
    IntentType.DEBUG: (40, 180),
    IntentType.SPIEGAZIONE: (60, 200),
    IntentType.COMPARAZIONE: (80, 200),
    IntentType.ARCHITETTURA: (200, 450),
    IntentType.CODICE: (150, 500),
    IntentType.DOCUMENTO: (500, 9999),
}


@dataclass(frozen=True)
class EscalationRecord:
    triggered: bool
    reason: str
    original_level: TokenLevel
    escalated_level: TokenLevel


@dataclass(frozen=True)
class IntentScore:
    intent: IntentType
    score: int
    patterns_matched: tuple[str, ...] = field(default_factory=tuple)


@dataclass(frozen=True)
class ClassificationResult:
    query: str
    intent: IntentType
    intent_scores: tuple[IntentScore, ...]
    level: TokenLevel
    format: OutputFormat
    token_budget: tuple[int, int]
    intent_token_range: tuple[int, int]
    confidence: float
    escalation: EscalationRecord

    def budget_str(self) -> str:
        lo, hi = self.token_budget
        return f"{lo}–{hi}" if hi < 9999 else f"{lo}+"

    def intent_range_str(self) -> str:
        lo, hi = self.intent_token_range
        return f"{lo}–{hi}" if hi < 9999 else f"{lo}+"


def classify_query(query: str) -> ClassificationResult:
    """Classifica query -> intent + livello + formato + budget."""
    query_lower = query.lower()

    # Step 1: scoring
    scores: list[IntentScore] = []
    for intent_str, patterns in INTENT_PATTERNS.items():
        intent = IntentType(intent_str)
        matched: list[str] = []
        for p in patterns:
            if re.search(p, query_lower):
                matched.append(p)
        scores.append(
            IntentScore(
                intent=intent,
                score=len(matched),
                patterns_matched=tuple(matched),
            )
        )

    # Step 2: intent primario
    best = max(scores, key=lambda s: s.score)
    if best.score == 0:
        primary_intent = IntentType.SPIEGAZIONE
        confidence = 0.35
    else:
        primary_intent = best.intent
        total_matches = sum(s.score for s in scores)
        confidence = min(round(best.score / max(total_matches, 1), 2), 0.95)

    # Step 3: livello e formato base
    base_level = INTENT_TO_LEVEL[primary_intent]
    base_format = INTENT_TO_FORMAT[primary_intent]

    # Step 4: escalation
    escalation = EscalationRecord(
        triggered=False,
        reason="",
        original_level=base_level,
        escalated_level=base_level,
    )
    for pattern, reason in ESCALATION_TRIGGERS:
        if re.search(pattern, query_lower):
            new_level_val = min(base_level.value + 1, 4)
            escalation = EscalationRecord(
                triggered=True,
                reason=reason,
                original_level=base_level,
                escalated_level=TokenLevel(new_level_val),
            )
            base_level = TokenLevel(new_level_val)
            break

    # Step 5: budget
    level_name = base_level.name
    token_budget = LEVEL_BUDGETS[level_name]
    intent_range = INTENT_TOKEN_RANGES[primary_intent]

    return ClassificationResult(
        query=query,
        intent=primary_intent,
        intent_scores=tuple(scores),
        level=base_level,
        format=base_format,
        token_budget=token_budget,
        intent_token_range=intent_range,
        confidence=confidence,
        escalation=escalation,
    )
