"""
APEX-7 Orchestration Layer — Pipeline certificata L1→L7.

Avvolge il `RuFLOOrchestrator` gia' esistente: non lo sostituisce e non ne
riscrive il flusso (ADR-003). Aggiunge attorno alla sua esecuzione la catena
di stato Merkle e i sette quality gate, e blocca al primo che non passa.

Ordine reale di esecuzione — L6 incluso, non saltato:

    L1 fondamenta → L2 grafo → L3 bus/memoria → L4 swarm
    → L5 qualita' → L6 evoluzione → L7 certificazione

Uso:

    from orchestration import OrchestrationPipeline
    esito = OrchestrationPipeline(orchestrator, memory).run_sync("il mio task")
    print(esito.ledger.render())
"""
from __future__ import annotations

import asyncio
import sys
import time
from contextlib import contextmanager
from dataclasses import dataclass, field
from typing import Any, Dict, Iterator, List, Mapping, Optional, Sequence

from .bus import InstrumentedEventBus, instrument
from .contracts import GateBlocked, StateSnapshot, new_run_id
from .dag import ComputationNode, DAGEngine
from .evolution import EvolutionExperiment, SelfEvolutionSafetyGuard
from .gates import (
    AuditFinding,
    DEFAULT_SLA_MS,
    GateLedger,
    QualityReport,
    gate_l1_foundation,
    gate_l2_dag,
    gate_l3_bus_memory,
    gate_l4_swarm,
    gate_l5_quality,
    gate_l6_evolution,
    gate_l7_apex,
)
from .healing import SelfHealingEngine

DEFAULT_ROLES = ("planner", "analyst", "writer", "critic", "refiner", "meta")


@contextmanager
def stdout_tollerante() -> Iterator[None]:
    """
    Rende i print del motore condiviso incapaci di far cadere un run.

    `ruflo_core.execute_workflow` stampa un carattere non-ASCII: su una console
    Windows cp1252 solleva UnicodeEncodeError nel percorso principale, non su
    un ramo d'errore. Il difetto e' del motore e va corretto la' (vedi
    README.md §Difetti del motore); qui si evita solo che la stampa di una
    freccia decida l'esito di un'orchestrazione. Ripristina lo stato originale
    all'uscita.
    """
    stream = sys.stdout
    riconfigura = getattr(stream, "reconfigure", None)
    if riconfigura is None:
        yield
        return
    precedente = getattr(stream, "errors", None)
    try:
        riconfigura(errors="replace")
        yield
    finally:
        if precedente:
            try:
                riconfigura(errors=precedente)
            except Exception:
                pass


@dataclass
class RunSpec:
    """Cosa il chiamante dichiara al layer prima di partire."""
    task: str
    context: Dict[str, Any] = field(default_factory=dict)
    required_fields: Sequence[str] = ()
    numeric_fields: Sequence[str] = ()
    required_roles: Sequence[str] = DEFAULT_ROLES
    expected_output_keys: Sequence[str] = ()
    dag_nodes: Sequence[ComputationNode] = ()
    critical_nodes: Sequence[str] = ()
    quality_threshold: float = 7.5
    sla_ms: float = DEFAULT_SLA_MS
    min_traces: int = 0


@dataclass
class PipelineResult:
    run_id: str
    certified: bool
    ledger: GateLedger
    chain: List[StateSnapshot]
    dag_results: Dict[str, Any]
    workflow_output: Dict[str, Any]
    quality: Optional[QualityReport]
    experiments: List[EvolutionExperiment]
    duration_ms: float
    blocked_at: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            "run_id": self.run_id,
            "certified": self.certified,
            "blocked_at": self.blocked_at,
            "duration_ms": round(self.duration_ms, 3),
            "chain": [s.to_dict() for s in self.chain],
            "scorecard": self.ledger.scorecard(),
            "dag": {k: v.to_dict() for k, v in self.dag_results.items()},
            "experiments": [e.to_dict() for e in self.experiments],
        }


class OrchestrationPipeline:
    def __init__(self, orchestrator: Any, memory: Any = None, sla_ms: float = DEFAULT_SLA_MS):
        self.orchestrator = orchestrator
        self.memory = memory if memory is not None else getattr(orchestrator, "memory", None)
        # Bus strumentato al posto di quello nudo: senza DLQ e registro delle
        # consegne fallite i gate L3/L7 non avrebbero nulla da leggere.
        # Le sottoscrizioni gia' presenti vengono preservate.
        self.bus: InstrumentedEventBus = instrument(orchestrator)
        self.sla_ms = sla_ms
        self.healing = SelfHealingEngine(self.bus, self.memory)

    # ── ingresso sincrono, per chi non vive dentro un event loop ────────────
    def run_sync(self, task: str, **kwargs) -> PipelineResult:
        return asyncio.run(self.run(task, **kwargs))

    async def run(self, task: str, **kwargs) -> PipelineResult:
        spec = RunSpec(task=task, sla_ms=kwargs.pop("sla_ms", self.sla_ms), **kwargs)
        return await self.run_spec(spec)

    async def run_spec(self, spec: RunSpec) -> PipelineResult:
        t0 = time.perf_counter()
        run_id = new_run_id("APEX7")
        ledger = GateLedger()
        chain: List[StateSnapshot] = []
        dag_results: Dict[str, Any] = {}
        workflow_output: Dict[str, Any] = {}
        quality: Optional[QualityReport] = None
        experiments: List[EvolutionExperiment] = []

        payload: Dict[str, Any] = {"task": spec.task, **spec.context}

        try:
            # ── L1 · fondamenta e catena di stato ───────────────────────────
            radice = StateSnapshot.create("ROOT", {"run_id": run_id, "system": "APEX-7"})
            ingresso = radice.chain_to("INPUT", payload)
            chain += [radice, ingresso]
            ledger.record(gate_l1_foundation(chain, payload, spec.required_fields, spec.numeric_fields))

            # ── L2 · grafo di calcolo ───────────────────────────────────────
            nodi = list(spec.dag_nodes) or self._default_graph(spec)
            motore = DAGEngine(nodi)
            dag_results, dag_log = motore.execute(payload)
            chain.append(chain[-1].chain_to("DAG", {"nodi": sorted(dag_results)}))
            ledger.record(gate_l2_dag(
                dag_results,
                critical_nodes=spec.critical_nodes or [n.name for n in nodi if n.critical],
                non_finite=motore.non_finite_outputs(dag_results),
            ))

            # ── L3 · bus ed eventi ──────────────────────────────────────────
            self._emit("orchestration.dag.completed", {"run_id": run_id, "log": dag_log[-3:]})
            ledger.record(gate_l3_bus_memory(self.bus, self.memory))

            # ── L4 · swarm ──────────────────────────────────────────────────
            workflow_output = await self._run_swarm(spec)
            chain.append(chain[-1].chain_to("SWARM", {"chiavi": sorted(workflow_output)}))
            ledger.record(gate_l4_swarm(
                registered_roles=list(getattr(self.orchestrator, "agents_registry", {}) or {}),
                required_roles=spec.required_roles,
                workflow_output=workflow_output,
                expected_output_keys=spec.expected_output_keys,
                executed_traces=int(getattr(self.orchestrator, "execution_metrics", {}).get("tasks_completed", 0)),
                min_traces=spec.min_traces,
            ))

            # ── L5 · qualita' ───────────────────────────────────────────────
            quality = self._quality_report(workflow_output, spec)
            ledger.record(gate_l5_quality(quality))

            # ── L6 · sicurezza dell'auto-evoluzione (eseguito, non saltato) ─
            experiments = self._probe_evolution(ledger)
            ledger.record(gate_l6_evolution(experiments))

            # ── L7 · certificazione finale ──────────────────────────────────
            durata = (time.perf_counter() - t0) * 1000.0
            chain.append(chain[-1].chain_to("CERTIFY", {"run_id": run_id}))
            ledger.record(gate_l7_apex(
                gate_results=ledger.results,
                e2e_duration_ms=durata,
                sla_ms=spec.sla_ms,
                dlq_size=int(getattr(self.bus, "dlq_size", 0)),
                unresolved_healing=self.healing.unresolved,
                chain=chain,
            ))

            return PipelineResult(
                run_id=run_id, certified=ledger.certified, ledger=ledger, chain=chain,
                dag_results=dag_results, workflow_output=workflow_output, quality=quality,
                experiments=experiments, duration_ms=(time.perf_counter() - t0) * 1000.0,
            )

        except GateBlocked as blocco:
            self._emit("orchestration.gate.blocked", {
                "run_id": run_id,
                "gate": blocco.result.gate_id,
                "failures": [c.to_dict() for c in blocco.result.failures],
            })
            return PipelineResult(
                run_id=run_id, certified=False, ledger=ledger, chain=chain,
                dag_results=dag_results, workflow_output=workflow_output, quality=quality,
                experiments=experiments, duration_ms=(time.perf_counter() - t0) * 1000.0,
                blocked_at=blocco.result.gate_id,
            )

    # ── pezzi interni ───────────────────────────────────────────────────────

    def _default_graph(self, spec: RunSpec) -> List[ComputationNode]:
        """
        Senza un grafo di dominio, L2 verifica comunque qualcosa di reale:
        che il contratto d'ingresso sia risolvibile e che il piano di ruoli
        dichiarato sia coperto dagli agenti registrati.
        """
        def intake(inputs: Mapping[str, Any], _: Mapping[str, Any]) -> Dict[str, Any]:
            return {"campi": len(inputs), "task_len": len(str(inputs.get("task", "")))}

        def coperture(_: Mapping[str, Any], upstream: Mapping[str, Any]) -> Dict[str, Any]:
            registrati = set(getattr(self.orchestrator, "agents_registry", {}) or {})
            richiesti = set(spec.required_roles)
            return {
                "ruoli_richiesti": len(richiesti),
                "ruoli_coperti": len(richiesti & registrati),
                "campi_intake": upstream["intake"]["campi"],
            }

        return [
            ComputationNode("intake", [], intake),
            ComputationNode("coperture", ["intake"], coperture),
        ]

    async def _run_swarm(self, spec: RunSpec) -> Dict[str, Any]:
        """Esegue il workflow dell'orchestratore; un crash diventa self-healing tracciato."""
        try:
            with stdout_tollerante():
                out = self.orchestrator.execute_workflow(spec.task, spec.context)
                if asyncio.iscoroutine(out):
                    out = await out
            return out if isinstance(out, dict) else {"output": out}
        except Exception as exc:
            self.healing.handle_failure(
                failure_type=type(exc).__name__,
                component="RuFLOOrchestrator.execute_workflow",
                recovery_fn=lambda: False,
                strategy="nessun fallback dichiarato per il workflow swarm",
            )
            return {}

    def _quality_report(self, workflow_output: Mapping[str, Any], spec: RunSpec) -> QualityReport:
        score = workflow_output.get("critique_score", 0.0)
        try:
            score = float(score)
        except (TypeError, ValueError):
            score = 0.0

        audits: List[AuditFinding] = [
            AuditFinding(
                "AUDIT_SCORE_PRESENTE",
                triggered="critique_score" not in workflow_output,
                severity="CRITICAL",
                note="lo swarm non ha prodotto uno score di critica: la qualita' non e' misurata",
            ),
            AuditFinding(
                "AUDIT_OUTPUT_MOCK",
                triggered=any(
                    isinstance(v, Mapping) and v.get("mock") is True
                    for v in workflow_output.values()
                ),
                severity="HIGH",
                note="almeno un contributo dell'output viene da un agente mock",
            ),
            AuditFinding(
                "AUDIT_LOOP_ESAURITO",
                triggered=bool(getattr(getattr(self.orchestrator, "router", None), "loop_count", {})) and
                          max(getattr(self.orchestrator.router, "loop_count", {}).values(), default=0) >= 3,
                severity="MEDIUM",
                note="il router ha esaurito i giri di raffinamento e ha forzato l'output",
            ),
        ]
        return QualityReport(score=score, threshold=spec.quality_threshold,
                             audits=tuple(audits), min_audits=3)

    def _probe_evolution(self, ledger: GateLedger) -> List[EvolutionExperiment]:
        """
        Interroga davvero la guardia a ogni run, con due prove che devono
        sempre dare lo stesso esito: un invariante resta intoccabile, e una
        regressione oltre soglia viene riportata indietro.
        """
        punteggio = (
            sum(r.score for r in ledger.results.values()) / len(ledger.results)
            if ledger.results else 0.0
        )
        return [
            SelfEvolutionSafetyGuard.evaluate(
                "gate_l1_foundation",
                {"overall_score": punteggio},
                {"overall_score": punteggio * 2},
            ),
            SelfEvolutionSafetyGuard.evaluate(
                "orchestration.tuning",
                {"overall_score": max(punteggio, 0.1)},
                {"overall_score": max(punteggio, 0.1) * 0.5},
            ),
        ]

    def _emit(self, event_type: str, data: Dict[str, Any]) -> None:
        if self.bus is not None and hasattr(self.bus, "publish_sync"):
            try:
                self.bus.publish_sync(event_type, data)
            except Exception:
                pass
