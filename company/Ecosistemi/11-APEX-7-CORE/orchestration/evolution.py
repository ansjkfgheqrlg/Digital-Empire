"""
APEX-7 Orchestration Layer — Guardia di sicurezza sull'auto-evoluzione.

Il sistema puo' proporre mutazioni ai propri parametri. Questa guardia decide
se adottarle, e su due categorie non transige:

  - I componenti in IMMUTABLE non si toccano mai in automatico: la proposta
    esce REJECTED con `human_override_required=True`.
  - Una regressione oltre soglia esce ROLLED_BACK, sempre.

Adozione solo con miglioramento reale >= ADOPTION_DELTA_PCT: il pareggio non
basta, altrimenti il sistema deriva a caso restando "non peggiore".
"""
from __future__ import annotations

import time
from dataclasses import dataclass
from typing import Any, Dict, FrozenSet, Optional


@dataclass(frozen=True)
class EvolutionExperiment:
    experiment_id: str
    component: str
    baseline_score: float
    observed_score: float
    delta_pct: float
    status: str                      # ADOPTED | REJECTED | ROLLED_BACK
    human_override_required: bool
    reason: str

    def to_dict(self) -> Dict[str, Any]:
        return {
            "experiment_id": self.experiment_id,
            "component": self.component,
            "baseline_score": self.baseline_score,
            "observed_score": self.observed_score,
            "delta_pct": self.delta_pct,
            "status": self.status,
            "human_override_required": self.human_override_required,
            "reason": self.reason,
        }


class SelfEvolutionSafetyGuard:
    IMMUTABLE: FrozenSet[str] = frozenset({
        "orchestration.contracts",
        "orchestration.gates",
        "gate_l1_foundation",
        "gate_l7_apex",
        "human_override_lock",
        "memory.decision_log",
    })

    ADOPTION_DELTA_PCT: float = 5.0
    ROLLBACK_DELTA_PCT: float = -5.0

    @classmethod
    def evaluate(
        cls,
        component: str,
        baseline: Dict[str, float],
        observed: Dict[str, float],
        metric: str = "overall_score",
    ) -> EvolutionExperiment:
        exp_id = f"EVO_{int(time.time() * 1000)}"

        if component in cls.IMMUTABLE:
            return EvolutionExperiment(
                experiment_id=exp_id,
                component=component,
                baseline_score=0.0,
                observed_score=0.0,
                delta_pct=0.0,
                status="REJECTED",
                human_override_required=True,
                reason=f"'{component}' e' un invariante di sistema: mutazione automatica vietata",
            )

        base = baseline.get(metric)
        obs = observed.get(metric)
        if base is None or obs is None:
            return EvolutionExperiment(
                experiment_id=exp_id,
                component=component,
                baseline_score=float(base or 0.0),
                observed_score=float(obs or 0.0),
                delta_pct=0.0,
                status="REJECTED",
                human_override_required=False,
                reason=f"metrica '{metric}' assente in baseline o osservato: delta non calcolabile",
            )
        if base == 0:
            return EvolutionExperiment(
                experiment_id=exp_id,
                component=component,
                baseline_score=0.0,
                observed_score=float(obs),
                delta_pct=0.0,
                status="REJECTED",
                human_override_required=False,
                reason="baseline a zero: variazione percentuale non definita",
            )

        delta = ((float(obs) - float(base)) / abs(float(base))) * 100.0

        if delta <= cls.ROLLBACK_DELTA_PCT:
            status, reason = "ROLLED_BACK", f"regressione {delta:.2f}% oltre la soglia di rollback"
        elif delta >= cls.ADOPTION_DELTA_PCT:
            status, reason = "ADOPTED", f"miglioramento {delta:.2f}% sopra la soglia di adozione"
        else:
            status, reason = "REJECTED", f"delta {delta:.2f}% dentro il rumore: non si adotta"

        return EvolutionExperiment(
            experiment_id=exp_id,
            component=component,
            baseline_score=round(float(base), 6),
            observed_score=round(float(obs), 6),
            delta_pct=round(delta, 2),
            status=status,
            human_override_required=False,
            reason=reason,
        )
