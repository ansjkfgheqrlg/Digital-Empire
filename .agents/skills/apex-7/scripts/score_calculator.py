#!/usr/bin/env python3
"""
APEX-7 Score Calculator
Calcola il weighted total score dalle 5 dimensioni di CRITIC.
"""

import json
from typing import Dict, List, Tuple


WEIGHTS = {
    "completezza": 0.25,
    "precisione": 0.25,
    "actionability": 0.20,
    "coerenza_interna": 0.20,
    "efficacia_obiettivo": 0.10,
}


def calculate_weighted_score(scores: Dict[str, float]) -> Tuple[float, str]:
    """
    Calcola weighted total e determina il verdict.

    Args:
        scores: dict con punteggi per le 5 dimensioni
                {"completezza": 8.5, "precisione": 7.0, ...}

    Returns:
        (weighted_total, verdict)
    """
    weighted_total = sum(scores[k] * WEIGHTS[k] for k in WEIGHTS)

    has_blockers = scores.get("has_blockers", False)

    if has_blockers:
        verdict = "REFINE"
    elif weighted_total >= 8.0:
        verdict = "PASS"
    elif weighted_total >= 6.0:
        verdict = "REFINE"
    else:
        verdict = "RESTART"

    return round(weighted_total, 2), verdict


def calculate_gate_score(criteria_results: List[Dict]) -> Tuple[float, bool]:
    """
    Calcola il gate score dai risultati dei criteri.

    Args:
        criteria_results: lista di {"status": "PASS"|"PARTIAL"|"FAIL"}

    Returns:
        (gate_score, passed)
    """
    status_to_score = {"PASS": 1.0, "PARTIAL": 0.5, "FAIL": 0.0}
    total = len(criteria_results)
    score = sum(status_to_score[c["status"]] for c in criteria_results) / total

    return round(score, 2), score >= get_threshold(total)


def get_threshold(num_criteria: int, level: int = 1) -> float:
    """Restituisce la soglia in base al livello."""
    thresholds = {
        1: 0.80,  # L1→L2
        2: 0.80,  # L2→L3
        3: 0.83,  # L3→L4
        4: 0.80,  # L4→L5
        5: 1.00,  # L5→L6 — ZERO TOLLERANZA
        6: 1.00,  # L6→L7 — ZERO TOLLERANZA
    }
    return thresholds.get(level, 0.80)


def format_score_table(scores: Dict[str, float]) -> str:
    """Formatta la tabella degli score per output."""
    weighted_total, verdict = calculate_weighted_score(scores)

    lines = [
        "SCORING:",
        "┌─────────────────────┬───────┬────────┬───────────┐",
        "│ Dimensione          │ Peso  │ Score  │ Weighted  │",
        "├─────────────────────┼───────┼────────┼───────────┤",
    ]

    dimension_names = {
        "completezza": "Completezza",
        "precisione": "Precisione",
        "actionability": "Actionability",
        "coerenza_interna": "Coerenza Interna",
        "efficacia_obiettivo": "Efficacia Obiettivo",
    }

    for key, name in dimension_names.items():
        score = scores.get(key, 0)
        weight = WEIGHTS[key]
        weighted = round(score * weight, 2)
        lines.append(
            f"│ {name:<19} │ {weight:<5} │ {score}/10 │ {weighted:<9} │"
        )

    lines.extend([
        "├─────────────────────┴───────┴────────┼───────────┤",
        f"│ WEIGHTED TOTAL                       │ {weighted_total:<9} │",
        "└──────────────────────────────────────┴───────────┘",
        f"VERDICT: {verdict}",
    ])

    return "\n".join(lines)


if __name__ == "__main__":
    # Example usage
    example_scores = {
        "completezza": 8.5,
        "precisione": 7.0,
        "actionability": 9.0,
        "coerenza_interna": 8.0,
        "efficacia_obiettivo": 7.5,
    }
    print(format_score_table(example_scores))
