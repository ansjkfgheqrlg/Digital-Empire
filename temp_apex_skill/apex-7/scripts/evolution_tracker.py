#!/usr/bin/env python3
"""
APEX-7 Evolution Tracker
Traccia le metriche di performance e propone evoluzioni.
"""

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional


METRICS_FILE = Path("/home/user/apex-7/self-evolution/metrics.json")


def iso_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_metrics() -> Dict:
    """Carica le metriche storiche."""
    if METRICS_FILE.exists():
        return json.loads(METRICS_FILE.read_text())
    return {
        "sessions": [],
        "evolutions": [],
        "baseline": {
            "avg_quality_score": 7.5,
            "avg_cycles_to_pass": 2.3,
            "gate_pass_rate": 0.78,
            "avg_session_time_min": 25,
        },
    }


def save_metrics(metrics: Dict):
    METRICS_FILE.parent.mkdir(parents=True, exist_ok=True)
    METRICS_FILE.write_text(json.dumps(metrics, indent=2))


def record_session(
    session_id: str,
    quality_score: float,
    cycles: int,
    gate_passed: bool,
    duration_min: float,
    agents_activated: List[str],
):
    """Registra una sessione completata."""
    metrics = load_metrics()

    metrics["sessions"].append({
        "session_id": session_id,
        "timestamp": iso_now(),
        "quality_score": quality_score,
        "cycles": cycles,
        "gate_passed": gate_passed,
        "duration_min": duration_min,
        "agents_activated": agents_activated,
    })

    # Mantieni solo ultime 100 sessioni
    if len(metrics["sessions"]) > 100:
        metrics["sessions"] = metrics["sessions"][-100:]

    save_metrics(metrics)


def get_recent_stats(n_sessions: int = 10) -> Dict:
    """Calcola statistiche sulle sessioni recenti."""
    metrics = load_metrics()
    recent = metrics["sessions"][-n_sessions:]

    if not recent:
        return metrics["baseline"]

    scores = [s["quality_score"] for s in recent]
    gate_passes = sum(1 for s in recent if s["gate_passed"])
    durations = [s["duration_min"] for s in recent]
    cycles = [s["cycles"] for s in recent]

    return {
        "avg_quality_score": round(sum(scores) / len(scores), 2),
        "avg_cycles_to_pass": round(sum(cycles) / len(cycles), 2),
        "gate_pass_rate": round(gate_passes / len(recent), 2),
        "avg_session_time_min": round(sum(durations) / len(durations), 1),
        "sessions_analyzed": len(recent),
    }


def check_evolution_rollback() -> Optional[str]:
    """Verifica se necessario rollback."""
    metrics = load_metrics()
    recent = metrics["sessions"][-5:]

    if len(recent) < 5:
        return None

    baseline = metrics["baseline"]
    current = get_recent_stats(5)

    # Quality drop > 10%
    if current["avg_quality_score"] < baseline["avg_quality_score"] * 0.9:
        return f"QUALITY_DROP: {current['avg_quality_score']} vs baseline {baseline['avg_quality_score']}"

    # Gate failure spike
    if current["gate_pass_rate"] < baseline["gate_pass_rate"] * 0.8:
        return f"GATE_FAILURE_SPIKE: {current['gate_pass_rate']} vs baseline {baseline['gate_pass_rate']}"

    return None


def propose_evolution() -> Optional[Dict]:
    """Propone un'evoluzione basata sulle metriche."""
    stats = get_recent_stats(20)
    baseline = load_metrics()["baseline"]

    # Se quality stagnante, proponi modifica threshold
    if (
        abs(stats["avg_quality_score"] - baseline["avg_quality_score"]) < 0.3
        and stats["avg_cycles_to_pass"] > 2.5
    ):
        return {
            "variable": "critique_max_iterations",
            "current": 3,
            "proposed": 4,
            "rationale": f"Avg cycles to pass = {stats['avg_cycles_to_pass']}, quality stagnante",
            "expected_improvement": "+0.3 quality score",
            "risk": "LOW",
        }

    # Se gate troppo severo
    if stats["gate_pass_rate"] < 0.60:
        return {
            "variable": "gate_threshold_L1_L2",
            "current": 0.80,
            "proposed": 0.75,
            "rationale": f"Gate pass rate = {stats['gate_pass_rate']}, possibile over-gating",
            "expected_improvement": "+10% pass rate",
            "risk": "MEDIUM",
        }

    return None


def record_evolution(
    variable: str,
    old_value: float,
    new_value: float,
    rationale: str,
    adopted: bool,
):
    """Registra un'evoluzione applicata."""
    metrics = load_metrics()

    metrics["evolutions"].append({
        "timestamp": iso_now(),
        "variable": variable,
        "old_value": old_value,
        "new_value": new_value,
        "rationale": rationale,
        "adopted": adopted,
        "pre_stats": get_recent_stats(5),
    })

    save_metrics(metrics)


if __name__ == "__main__":
    stats = get_recent_stats()
    print(f"Recent stats (10 sessions): {json.dumps(stats, indent=2)}")

    evolution = propose_evolution()
    if evolution:
        print(f"\nEvolution proposed: {json.dumps(evolution, indent=2)}")

    rollback = check_evolution_rollback()
    if rollback:
        print(f"\n⚠️ ROLLBACK NEEDED: {rollback}")
