"""
APEX-7 Orchestration Layer — i 7 quality gate del motore canonico (ADR-010).

Sottopacchetto additivo di `11-APEX-7-CORE`: avvolge il RuFLOOrchestrator
esistente senza riscriverlo (ADR-003). Origine: audit dello zip
`apex7_orchestrator` del 2026-08-13 — vedi README.md per cosa e' stato preso,
cosa e' stato scartato e cosa e' stato corretto.
"""
from .bus import InstrumentedEventBus, instrument
from .contracts import (
    GateBlocked,
    GateCheck,
    GateResult,
    StateSnapshot,
    is_finite_number,
    new_run_id,
    verify_chain,
)
from .dag import (
    ComputationNode,
    DAGCycleError,
    DAGEngine,
    DAGMissingDependencyError,
    NodeResult,
    topological_order,
)
from .evolution import EvolutionExperiment, SelfEvolutionSafetyGuard
from .gates import (
    AuditFinding,
    DEFAULT_SLA_MS,
    GateLedger,
    Outcome,
    QualityReport,
    REQUIRED_GATE_IDS,
    THRESHOLDS,
    gate_l1_foundation,
    gate_l2_dag,
    gate_l3_bus_memory,
    gate_l4_swarm,
    gate_l5_quality,
    gate_l6_evolution,
    gate_l7_apex,
)
from .healing import HealingAction, SelfHealingEngine
from .pipeline import DEFAULT_ROLES, OrchestrationPipeline, PipelineResult, RunSpec, stdout_tollerante

__all__ = [
    "AuditFinding", "ComputationNode", "DAGCycleError", "DAGEngine",
    "DAGMissingDependencyError", "DEFAULT_ROLES", "DEFAULT_SLA_MS",
    "EvolutionExperiment", "GateBlocked", "GateCheck", "GateLedger", "GateResult",
    "HealingAction", "InstrumentedEventBus", "instrument", "NodeResult",
    "OrchestrationPipeline", "Outcome", "stdout_tollerante",
    "PipelineResult", "QualityReport", "REQUIRED_GATE_IDS", "RunSpec",
    "SelfEvolutionSafetyGuard", "SelfHealingEngine", "StateSnapshot", "THRESHOLDS",
    "gate_l1_foundation", "gate_l2_dag", "gate_l3_bus_memory", "gate_l4_swarm",
    "gate_l5_quality", "gate_l6_evolution", "gate_l7_apex", "is_finite_number",
    "new_run_id", "topological_order", "verify_chain",
]
