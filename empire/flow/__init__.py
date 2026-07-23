"""
EMPIRE FLOW — motore che esegue workflows.yaml: stato, gate, coda, registrazione.

Owner: Gael · Controllore: Claude · Origine: FORGE (lotto G-C, CP-20260722, brief GEM-06)
Governo: MANDATO Art.8 + ADR-006 (ciclo 9 passi) + ADR-003 (wrap)

Principio non negoziabile (GEM-06 §3): l'engine non esegue il lavoro (non scrive copy,
non chiama concessionari, non genera video). Tiene stato, applica gate, assegna, registra.
Un passo `executor: human` non si chiude mai da solo.
"""
from __future__ import annotations

__all__ = ["spec", "dag", "gate", "queue", "state", "runner"]
