"""
Story Validator (PIANO-KDP-67, CP3) — GO/NO-GO deterministico: libro di nicchia CON
STORIA (fiction narrativa: cozy mystery, romance, thriller, memoir, true crime...) SI,
diario/questionario/journal/tracker NO.

Deliberatamente SENZA chiamate LLM: è un controllo a keyword su titolo+descrizione,
trasparente e verificabile, non un "agente" che decide in modo opaco. Regola critica
trovata nello zip originale (CRITICAL_RULE_001_NICHE_STORY_ONLY): un libro diario deve
essere scartato PRIMA di spendere qualunque sforzo di scrittura, non dopo.
"""
from __future__ import annotations

from dataclasses import dataclass, field

from . import config


@dataclass
class ValidationResult:
    is_go: bool
    matched_forbidden: list[str] = field(default_factory=list)
    matched_required: list[str] = field(default_factory=list)
    motivation: str = ""


def validate(title: str, description: str = "") -> ValidationResult:
    """Ritorna GO se il testo (titolo+descrizione) indica un libro di nicchia con storia,
    NO-GO se indica un diario/questionario/journal/tracker — deterministico, ripetibile,
    nessun costo, nessuna chiamata esterna."""
    text = f"{title} {description}".lower()

    matched_forbidden = [kw for kw in config.FORBIDDEN_NICHE_KEYWORDS if kw.lower() in text]
    matched_required = [kw for kw in config.REQUIRED_NICHE_KEYWORDS if kw.lower() in text]

    if matched_forbidden:
        return ValidationResult(
            is_go=False,
            matched_forbidden=matched_forbidden,
            matched_required=matched_required,
            motivation=(
                f"NO-GO: rilevate keyword vietate {matched_forbidden} — indica diario/"
                f"questionario/tracker, non libro di nicchia con storia. Auto-reject "
                f"indipendentemente da altri segnali (regola critica)."
            ),
        )

    if matched_required:
        return ValidationResult(
            is_go=True,
            matched_forbidden=[],
            matched_required=matched_required,
            motivation=f"GO: rilevate keyword di nicchia con storia {matched_required}, nessuna keyword vietata.",
        )

    return ValidationResult(
        is_go=False,
        matched_forbidden=[],
        matched_required=[],
        motivation=(
            "NO-GO: nessuna keyword di nicchia con storia riconosciuta e nessuna keyword "
            "vietata riconosciuta — testo ambiguo, non classificabile con sicurezza. "
            "Non si genera un libro su un segnale ambiguo (mai inventare, mai forzare un GO)."
        ),
    )


if __name__ == "__main__":
    # Auto-test CP3: 5 titoli reali (3 devono passare, 2 devono essere respinti) — vedi
    # "Fatto" nel piano. Titoli presi dal REPORT_Libro_Copiato_Info.md consegnato (libri
    # Amazon reali citati nello zip analizzato) per un confronto onesto sugli stessi dati.
    test_cases = [
        ("The Cozy Cat Mystery of Maple Street: A Small Town Cozy Mystery with Cats", True),
        ("Whispers in the Lighthouse: A Small Town Romance Suspense Novel", True),
        ("Midnight Bakery: A Cozy Mystery Novella", True),
        ("BestSelf 13-Week Self Journal & Goal Planner - Undated Daily ADHD-Friendly Journal", False),
        ("Worry for Nothing: Guided Anxiety Journal, Cognitive Behavioral Therapy Mental Health Journal", False),
    ]
    print("=== CP3 self-test: 5 titoli reali, 3 attesi GO, 2 attesi NO-GO ===\n")
    n_ok = 0
    for title, expected_go in test_cases:
        result = validate(title)
        ok = result.is_go == expected_go
        n_ok += int(ok)
        status = "OK" if ok else "MISMATCH"
        print(f"[{status}] atteso={'GO' if expected_go else 'NO-GO'} ottenuto={'GO' if result.is_go else 'NO-GO'}")
        print(f"        titolo: {title}")
        print(f"        motivo: {result.motivation}\n")
    print(f"Risultato: {n_ok}/{len(test_cases)} corretti")
    if n_ok != len(test_cases):
        raise SystemExit(1)
