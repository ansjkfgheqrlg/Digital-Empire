"""
APEX-7 Orchestration Layer — DAG di calcolo con circuit breaker.

Risolve le dipendenze fra nodi in ordine topologico ed esegue ogni nodo
isolato: se salta, il suo fallback lo degrada invece di far cadere il grafo.

Tre differenze volute rispetto a un ciclo "while pending" ingenuo:
  1. I cicli si scoprono PRIMA di eseguire qualsiasi cosa (DAGCycleError),
     non dopo N iterazioni a vuoto.
  2. Un nodo la cui dipendenza e' fallita esce come BLOCKED esplicito: non
     sparisce in silenzio dai risultati facendo credere al gate che il grafo
     sia completo.
  3. Lo stato di ogni nodo e' sempre presente nel risultato, anche quando e'
     un fallimento. Un grafo che si "assottiglia" e' un grafo che mente.
"""
from __future__ import annotations

import time
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional, Tuple

from .contracts import is_finite_number

ComputeFn = Callable[[Dict[str, Any], Dict[str, Any]], Dict[str, Any]]
FallbackFn = Callable[[Dict[str, Any]], Dict[str, Any]]


class DAGCycleError(ValueError):
    """Il grafo contiene un ciclo: non e' un DAG."""


class DAGMissingDependencyError(ValueError):
    """Un nodo dichiara una dipendenza che non esiste nel grafo."""


@dataclass
class ComputationNode:
    name: str
    dependencies: List[str] = field(default_factory=list)
    compute_fn: Optional[ComputeFn] = None
    fallback_fn: Optional[FallbackFn] = None
    critical: bool = True


@dataclass(frozen=True)
class NodeResult:
    node_name: str
    status: str            # SUCCESS | DEGRADED | FAILED | BLOCKED
    duration_ms: float
    output: Dict[str, Any]
    error: Optional[str] = None
    fallback_applied: bool = False

    @property
    def usable(self) -> bool:
        return self.status in ("SUCCESS", "DEGRADED")

    def to_dict(self) -> Dict[str, Any]:
        return {
            "node": self.node_name,
            "status": self.status,
            "duration_ms": round(self.duration_ms, 3),
            "output_keys": sorted(self.output.keys()),
            "error": self.error,
            "fallback_applied": self.fallback_applied,
        }


def topological_order(nodes: Dict[str, ComputationNode]) -> List[str]:
    """Kahn. Solleva su dipendenze inesistenti o cicli, prima di eseguire."""
    for node in nodes.values():
        for dep in node.dependencies:
            if dep not in nodes:
                raise DAGMissingDependencyError(
                    f"Nodo '{node.name}' dipende da '{dep}', che non esiste nel grafo"
                )

    indegree = {name: len(set(n.dependencies)) for name, n in nodes.items()}
    dependents: Dict[str, List[str]] = {name: [] for name in nodes}
    for name, node in nodes.items():
        for dep in set(node.dependencies):
            dependents[dep].append(name)

    # ordinamento stabile: a parita' di grado, ordine alfabetico
    ready = sorted([n for n, d in indegree.items() if d == 0])
    order: List[str] = []
    while ready:
        current = ready.pop(0)
        order.append(current)
        for child in sorted(dependents[current]):
            indegree[child] -= 1
            if indegree[child] == 0:
                ready.append(child)
        ready.sort()

    if len(order) != len(nodes):
        residui = sorted(set(nodes) - set(order))
        raise DAGCycleError(f"Ciclo di dipendenze fra i nodi: {residui}")
    return order


class DAGEngine:
    """Esegue un grafo di nodi in ordine topologico, un nodo alla volta."""

    def __init__(self, nodes: List[ComputationNode]):
        if not nodes:
            raise ValueError("Un DAG senza nodi non e' eseguibile")
        duplicati = [n.name for n in nodes if [x.name for x in nodes].count(n.name) > 1]
        if duplicati:
            raise ValueError(f"Nomi di nodo duplicati nel grafo: {sorted(set(duplicati))}")
        self.nodes: Dict[str, ComputationNode] = {n.name: n for n in nodes}
        self.order: List[str] = topological_order(self.nodes)

    def execute(self, inputs: Dict[str, Any]) -> Tuple[Dict[str, NodeResult], List[str]]:
        results: Dict[str, NodeResult] = {}
        log: List[str] = []

        for name in self.order:
            node = self.nodes[name]

            bloccanti = [d for d in node.dependencies if not results[d].usable]
            if bloccanti:
                results[name] = NodeResult(
                    node_name=name,
                    status="BLOCKED",
                    duration_ms=0.0,
                    output={},
                    error=f"dipendenze non utilizzabili: {bloccanti}",
                )
                log.append(f"[DAG_BLOCKED] {name} — dipendenze non utilizzabili: {bloccanti}")
                continue

            upstream = {d: results[d].output for d in node.dependencies}
            t0 = time.perf_counter()
            try:
                if node.compute_fn is None:
                    raise ValueError(f"Nodo '{name}' senza compute_fn")
                output = node.compute_fn(inputs, upstream)
                if not isinstance(output, dict):
                    raise TypeError(f"Nodo '{name}' ha restituito {type(output).__name__}, atteso dict")
                dur = (time.perf_counter() - t0) * 1000.0
                results[name] = NodeResult(name, "SUCCESS", dur, output)
                log.append(f"[DAG_OK] {name} in {dur:.2f}ms")
            except Exception as exc:  # circuit breaker per nodo
                dur = (time.perf_counter() - t0) * 1000.0
                if node.fallback_fn is not None:
                    try:
                        fb = node.fallback_fn(inputs)
                        results[name] = NodeResult(name, "DEGRADED", dur, fb, str(exc), True)
                        log.append(f"[DAG_CIRCUIT_BREAKER] {name} fallito ({exc}) — fallback applicato")
                        continue
                    except Exception as fb_exc:
                        exc = RuntimeError(f"{exc} | fallback fallito: {fb_exc}")
                results[name] = NodeResult(name, "FAILED", dur, {}, str(exc))
                log.append(f"[DAG_FAILED] {name} — {exc}")

        return results, log

    def non_finite_outputs(self, results: Dict[str, NodeResult]) -> List[str]:
        """Elenca i campi numerici NaN/Inf prodotti dai nodi (il gate L2 li usa)."""
        sporchi: List[str] = []
        for name, res in results.items():
            for k, v in res.output.items():
                if isinstance(v, (int, float)) and not is_finite_number(v):
                    sporchi.append(f"{name}.{k}={v!r}")
        return sporchi
