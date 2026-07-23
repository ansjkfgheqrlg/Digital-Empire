"""
Owner: Max · Controllore: Claude · Origine: FORGE
Governo: MANDATO Art.8 + ADR-008
"""
from __future__ import annotations

# Benchmark dei tempi di consegna (Time to Deliver - TTD) in ore per famiglia-task.
# Valori aggiornabili e tarabili nel tempo.
BENCHMARKS: dict[str, float] = {
    "build-python": 2.0,
    "copy-landing": 3.0,
    "test-suite": 1.0,
    "default": 4.0
}

def get_benchmark(family: str) -> float:
    """Restituisce il TTD benchmark per una determinata famiglia di task."""
    return BENCHMARKS.get(family, BENCHMARKS["default"])
