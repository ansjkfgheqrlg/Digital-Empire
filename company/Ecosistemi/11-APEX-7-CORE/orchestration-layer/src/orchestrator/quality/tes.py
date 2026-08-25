"""NERVE-SAVE :: tes.py
FASE 3 (Pre-Output Audit) + FASE 5 (Token Efficiency Score).
Calcola TES, esegue audit 6-check, certifica output.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

from orchestrator.quality.patterns import FILLER_WORD_SET


class TESGrade(Enum):
    ECCELLENTE = "🟢 ECCELLENTE"
    ACCETTABILE = "🟡 ACCETTABILE"
    SOTTO_STANDARD = "🟠 SOTTO STANDARD"
    FALLIMENTO = "🔴 FALLIMENTO"


class AuditVerdict(Enum):
    PASSED = "PASSED"
    FAILED = "FAILED"


def count_tokens(text: str) -> int:
    """Conta token (parole + punteggiatura significativa)."""
    return len(re.findall(r"\b\w+\b|[^\w\s]", text))


def count_words(text: str) -> int:
    return len(text.split())


def count_unique_concepts(text: str) -> int:
    """Stima concetti unici come frasi con >= 3 parole che non siano formule di cortesia."""
    courtesy = re.compile(
        r"^\s*(sì|no|ok|grazie|certo|esatto|bene|perfetto|ottimo)\s*$",
        re.IGNORECASE,
    )
    sentences = re.split(r"[.!?;\n]", text)
    return sum(
        1 for s in sentences if len(s.split()) >= 3 and not courtesy.match(s.strip())
    )


def calculate_filler_density(text: str) -> float:
    """Rapporto parole filler / parole totali."""
    words = text.lower().split()
    if not words:
        return 0.0
    filler_count = sum(
        1 for w in words if w.rstrip(",.!?:;") in FILLER_WORD_SET
    )
    return round(filler_count / len(words), 4)


def count_semantic_repetitions(text: str) -> int:
    """Rileva ripetizioni semantiche tramite overlap Jaccard > 0.70 tra coppie di frasi."""
    sentences = [
        s.strip() for s in re.split(r"[.!?\n]", text) if len(s.strip()) > 10
    ]
    repetitions = 0
    seen: list[set[str]] = []
    for sentence in sentences:
        words = set(sentence.lower().split())
        for prev in seen:
            union = words | prev
            if not union:
                continue
            jaccard = len(words & prev) / len(union)
            if jaccard > 0.70:
                repetitions += 1
                break
        seen.append(words)
    return repetitions


def detect_format_efficiency(text: str) -> float:
    """Valuta se il formato usato è quello ottimale disponibile. Score 0.0–1.0."""
    has_table = bool(re.search(r"\|.+\|", text))
    has_ordered = bool(re.search(r"^\s*\d+\.\s+", text, re.MULTILINE))
    has_unorder = bool(re.search(r"^[\s]*[-•*]\s+", text, re.MULTILINE))
    has_code = bool(re.search(r"```", text))
    parallel_ct = len(re.findall(r"\n[^\n]+:\s+[^\n]+", text))
    total_tokens = count_tokens(text)
    score = 0.50  # baseline prosa
    if has_table:
        score += 0.30
    if has_ordered:
        score += 0.12
    if has_unorder:
        score += 0.08
    if has_code:
        score += 0.10
    # Penalità: contenuto tabulare in prosa
    if parallel_ct >= 3 and not (has_table or has_unorder or has_ordered):
        score -= 0.25
    # Penalità: testo molto lungo senza struttura
    if total_tokens > 150 and not (has_table or has_ordered or has_unorder or has_code):
        score -= 0.20
    return round(min(max(score, 0.0), 1.0), 4)


@dataclass(frozen=True)
class AuditItem:
    check_id: int
    name: str
    verdict: AuditVerdict
    detail: str
    token_impact: int

    @property
    def passed(self) -> bool:
        return self.verdict == AuditVerdict.PASSED


@dataclass(frozen=True)
class TESReport:
    text: str
    token_count: int
    word_count: int
    concept_count: int
    filler_density: float
    repetition_count: int
    format_efficiency: float
    concept_density: float
    tes_score: float
    grade: TESGrade
    audit_items: tuple[AuditItem, ...] = field(default_factory=tuple)
    estimated_saveable_tokens: int = 0
    all_audits_passed: bool = False


def calculate_tes(
    text: str,
    expected_concepts: Optional[int] = None,
) -> TESReport:
    """Calcola TES + esegue Pre-Output Audit completo (6 check)."""
    token_count = count_tokens(text)
    word_count = count_words(text)
    concept_count = count_unique_concepts(text)
    filler_density = calculate_filler_density(text)
    repetition_count = count_semantic_repetitions(text)
    format_eff = detect_format_efficiency(text)

    if token_count == 0:
        tes = 0.0
        concept_density = 0.0
    else:
        concept_density = concept_count / max(token_count / 50, 1)
        rep_ratio = min(repetition_count / max(concept_count, 1), 1.0)
        tes = round(
            min(
                concept_density * 0.40
                + format_eff * 0.25
                + (1 - filler_density) * 0.20
                + (1 - rep_ratio) * 0.15,
                1.0,
            ),
            4,
        )

    grade = (
        TESGrade.ECCELLENTE
        if tes >= 0.80
        else TESGrade.ACCETTABILE
        if tes >= 0.60
        else TESGrade.SOTTO_STANDARD
        if tes >= 0.40
        else TESGrade.FALLIMENTO
    )

    # Pre-output audit 6 check
    audit: list[AuditItem] = []
    avg_sentence_len = token_count / max(concept_count, 1)

    # CHECK 1 — Taglio frase
    c1_pass = avg_sentence_len < 30
    audit.append(
        AuditItem(
            check_id=1,
            name="Taglio frase",
            verdict=AuditVerdict.PASSED if c1_pass else AuditVerdict.FAILED,
            detail=f"Lunghezza media frase: {avg_sentence_len:.1f} token (soglia: 30)",
            token_impact=int(token_count * 0.15) if not c1_pass else 0,
        )
    )

    # CHECK 2 — Ripetizioni
    c2_pass = repetition_count == 0
    audit.append(
        AuditItem(
            check_id=2,
            name="Zero ripetizioni semantiche",
            verdict=AuditVerdict.PASSED if c2_pass else AuditVerdict.FAILED,
            detail=f"{repetition_count} ripetizioni semantiche (Jaccard > 0.70)",
            token_impact=repetition_count * 18 if not c2_pass else 0,
        )
    )

    # CHECK 3 — Filler
    c3_pass = filler_density < 0.03
    audit.append(
        AuditItem(
            check_id=3,
            name="Filler zero-tolerance",
            verdict=AuditVerdict.PASSED if c3_pass else AuditVerdict.FAILED,
            detail=f"Densità filler: {filler_density * 100:.2f}% (soglia: 3%)",
            token_impact=int(token_count * filler_density) if not c3_pass else 0,
        )
    )

    # CHECK 4 — Formato
    c4_pass = format_eff >= 0.50
    audit.append(
        AuditItem(
            check_id=4,
            name="Format ottimale",
            verdict=AuditVerdict.PASSED if c4_pass else AuditVerdict.FAILED,
            detail=f"Format efficiency: {format_eff * 100:.1f}% (soglia: 50%)",
            token_impact=int(token_count * 0.20) if not c4_pass else 0,
        )
    )

    # CHECK 5 — Proporzionalità
    if expected_concepts is not None:
        ratio = concept_count / max(expected_concepts, 1)
        c5_pass = ratio <= 1.50
        audit.append(
            AuditItem(
                check_id=5,
                name="Proporzionalità",
                verdict=AuditVerdict.PASSED if c5_pass else AuditVerdict.FAILED,
                detail=(
                    f"Concetti: {concept_count} / attesi: {expected_concepts} "
                    f"(ratio: {ratio:.2f}, soglia: 1.50)"
                ),
                token_impact=int(token_count * 0.25) if not c5_pass else 0,
            )
        )
    else:
        c5_pass = concept_density >= 0.4
        audit.append(
            AuditItem(
                check_id=5,
                name="Proporzionalità (auto)",
                verdict=AuditVerdict.PASSED if c5_pass else AuditVerdict.FAILED,
                detail=f"Densità concettuale: {concept_density:.3f} (soglia: 0.40)",
                token_impact=int(token_count * 0.10) if not c5_pass else 0,
            )
        )

    # CHECK 6 — 30% Reduction Test
    c6_pass = filler_density < 0.05 and repetition_count == 0
    audit.append(
        AuditItem(
            check_id=6,
            name="30% Reduction Test",
            verdict=AuditVerdict.PASSED if c6_pass else AuditVerdict.FAILED,
            detail=(
                "Filler o ripetizioni presenti: riscrittura con -30% token possibile"
                if not c6_pass
                else "Nessuna riscrittura necessaria"
            ),
            token_impact=int(token_count * 0.30) if not c6_pass else 0,
        )
    )

    all_passed = all(item.passed for item in audit)
    saveable = sum(item.token_impact for item in audit if not item.passed)

    return TESReport(
        text=text,
        token_count=token_count,
        word_count=word_count,
        concept_count=concept_count,
        filler_density=filler_density,
        repetition_count=repetition_count,
        format_efficiency=format_eff,
        concept_density=concept_density,
        tes_score=tes,
        grade=grade,
        audit_items=tuple(audit),
        estimated_saveable_tokens=saveable,
        all_audits_passed=all_passed,
    )
