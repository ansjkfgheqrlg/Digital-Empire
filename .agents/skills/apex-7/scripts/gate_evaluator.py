#!/usr/bin/env python3
"""
APEX-7 Gate Evaluator
Valuta i criteri di gate per ogni livello e calcola il gate_score.
"""

from typing import List, Dict, Tuple


# Gate universali (G0-G4) + specifici per livello
GATE_CRITERIA = {
    1: {  # L1→L2: Base
        "universal": ["G0", "G1", "G2", "G3", "G4"],
        "specific": ["GL1", "GL2", "GL3"],
        "threshold": 0.80,
    },
    2: {  # L2→L3: Struttura
        "universal": ["G0", "G1", "G2", "G3", "G4"],
        "specific": ["GL4", "GL5", "GL6"],
        "threshold": 0.80,
    },
    3: {  # L3→L4: Parallelismo
        "universal": ["G0", "G1", "G2", "G3", "G4"],
        "specific": ["GL7", "GL8", "GL9"],
        "threshold": 0.83,
    },
    4: {  # L4→L5: Meta
        "universal": ["G0", "G1", "G2", "G3", "G4"],
        "specific": ["GL10", "GL11", "GL12"],
        "threshold": 0.80,
    },
    5: {  # L5→L6: Safety — ZERO TOLLERANZA
        "universal": ["G0", "G1", "G2", "G3", "G4"],
        "specific": ["GL13", "GL14", "GL15"],
        "threshold": 1.00,  # ZERO TOLLERANZA
        "zero_tolerance": True,
    },
    6: {  # L6→L7: APEX — ZERO TOLLERANZA
        "universal": ["G0", "G1", "G2", "G3", "G4"],
        "specific": ["GL16", "GL17", "GL18", "GL19", "GL20"],
        "threshold": 1.00,  # ZERO TOLLERANZA
        "zero_tolerance": True,
    },
}

CRITERION_DESCRIPTIONS = {
    "G0": "Risponde all'obiettivo dell'utente?",
    "G1": "L'output è completo? (nessun placeholder o omissioni)",
    "G2": "L'output è coerente internamente?",
    "G3": "L'output è immediatamente usabile?",
    "G4": "Il CRITIC ha dato PASS (score ≥ 8.0)?",
    "GL1": "Tutti i componenti base sono definiti?",
    "GL2": "Ogni componente ha responsabilità unica?",
    "GL3": "Le interfacce sono definite?",
    "GL4": "Il feedback loop è documentato e completo?",
    "GL5": "Max_iterations è definito (no loop infiniti)?",
    "GL6": "Le condizioni di routing sono specifiche?",
    "GL7": "La parallelizzazione è sicura (no race cond.)?",
    "GL8": "I checkpoint sono definiti?",
    "GL9": "Il rollback è possibile?",
    "GL10": "Il Meta Agent ha visibilità su tutto?",
    "GL11": "Il quality scoring è calibrato?",
    "GL12": "Il pattern detection ha soglie definite?",
    "GL13": "Self-evolution non causa instabilità?",
    "GL14": "Human override sempre possibile?",
    "GL15": "Limiti di sicurezza definiti?",
    "GL16": "Tutti i gate precedenti superati?",
    "GL17": "End-to-end test completato?",
    "GL18": "Performance ≥ 150% vs baseline?",
    "GL19": "Memory consistency verificata?",
    "GL20": "Self-healing dimostrato?",
}


def evaluate_gate(
    level: int,
    results: Dict[str, str],
) -> Tuple[float, bool, List[str]]:
    """
    Valuta un gate check.

    Args:
        level: livello corrente (1-6, dove 1 = L1→L2)
        results: dict criterion_id → "PASS"|"PARTIAL"|"FAIL"

    Returns:
        (gate_score, passed, remediation_list)
    """
    config = GATE_CRITERIA[level]
    all_criteria = config["universal"] + config["specific"]
    threshold = config["threshold"]
    zero_tolerance = config.get("zero_tolerance", False)

    status_to_score = {"PASS": 1.0, "PARTIAL": 0.5, "FAIL": 0.0}

    total = len(all_criteria)
    score_sum = 0.0
    remediation = []

    for criterion in all_criteria:
        status = results.get(criterion, "FAIL")
        score_sum += status_to_score[status]

        if status == "FAIL":
            remediation.append(
                f"Fix {criterion}: {CRITERION_DESCRIPTIONS[criterion]} — FAIL"
            )
        elif status == "PARTIAL":
            remediation.append(
                f"Complete {criterion}: {CRITERION_DESCRIPTIONS[criterion]} — PARTIAL"
            )

    gate_score = score_sum / total if total > 0 else 0.0

    # Zero tolerance: ogni FAIL = gate FAILED
    if zero_tolerance:
        has_any_fail = any(
            results.get(c, "FAIL") == "FAIL" for c in all_criteria
        )
        passed = not has_any_fail
    else:
        passed = gate_score >= threshold

    return round(gate_score, 2), passed, remediation


def format_gate_report(
    level: int,
    results: Dict[str, str],
    attempt: int,
) -> str:
    """Genera il Gate Report formattato."""
    config = GATE_CRITERIA[level]
    all_criteria = config["universal"] + config["specific"]
    gate_score, passed, remediation = evaluate_gate(level, results)

    status_icons = {"PASS": "✓", "PARTIAL": "◐", "FAIL": "✗"}

    lines = [
        "[GATE AGENT] Gate Check Report",
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
        f"GATE: L{level}→L{level+1}",
        f"TENTATIVO: {attempt} di 3",
        "",
        "CRITERI:",
        "┌──────┬─────────────────────────────┬─────────┬──────────┐",
        "│ ID   │ Criterio                    │ Status  │ Evidenza │",
        "├──────┼─────────────────────────────┼─────────┼──────────┤",
    ]

    for criterion in all_criteria:
        status = results.get(criterion, "FAIL")
        icon = status_icons.get(status, "?")
        desc = CRITERION_DESCRIPTIONS.get(criterion, criterion)[:27]
        evidence = results.get(f"{criterion}_evidence", "-")[:8]
        lines.append(
            f"│ {criterion:<4} │ {desc:<27} │ {status} {icon} │ {evidence:<8} │"
        )

    lines.extend([
        "└──────┴─────────────────────────────┴─────────┴──────────┘",
        "",
        f"GATE SCORE: {gate_score}/{config['threshold']} → {'PASSED' if passed else 'FAILED'}",
    ])

    if not passed:
        lines.append("")
        lines.append("REMEDIATION REQUIRED:")
        for i, fix in enumerate(remediation, 1):
            lines.append(f"→ Fix {i}: {fix}")

        if attempt >= 3:
            lines.append("NEXT ACTION: ESCALATE → META AGENT")
        else:
            lines.append("NEXT ACTION: torna a REFINER")
    else:
        lines.append("")
        lines.append("GATE SUPERATO ✓")
        lines.append(f"NEXT ACTION: avanza al livello {level+1} / output finale")

    lines.append("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    return "\n".join(lines)


if __name__ == "__main__":
    # Example
    example_results = {
        "G0": "PASS",
        "G1": "PASS",
        "G2": "PASS",
        "G3": "PARTIAL",
        "G4": "PASS",
        "GL1": "PASS",
        "GL2": "PASS",
        "GL3": "FAIL",
    }
    print(format_gate_report(level=1, results=example_results, attempt=1))
