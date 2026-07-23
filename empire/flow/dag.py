"""
EMPIRE FLOW — ordine topologico, rilevamento cicli, "cosa è sbloccato adesso".

Owner: Gael · Origine: FORGE (lotto G-C, CP-20260722)

Generico: opera su qualunque mappa {id: [depends...]}. Usato sia per il DAG
decisioni->workflow di workflows.yaml reale, sia per il DAG di step di un
singolo workflow (dove i depends_on tra step esistono davvero).
"""
from __future__ import annotations

__all__ = ["CycleError", "topological_order", "unlocked", "from_flow_spec"]


class CycleError(ValueError):
    def __init__(self, cycle: list[str]):
        self.cycle = cycle
        super().__init__(f"ciclo rilevato nel DAG: {' -> '.join(cycle)}")


def topological_order(edges: dict[str, list[str]]) -> list[str]:
    """Ordine topologico di Kahn. `edges[node] = [dipendenze di node]`.
    Solleva CycleError se il grafo ha un ciclo.
    """
    nodes = set(edges)
    for deps in edges.values():
        nodes.update(deps)

    indegree = {n: 0 for n in nodes}
    adj: dict[str, list[str]] = {n: [] for n in nodes}
    for n, deps in edges.items():
        for d in deps:
            adj[d].append(n)
            indegree[n] += 1

    queue = sorted(n for n, d in indegree.items() if d == 0)
    order: list[str] = []
    while queue:
        queue.sort()
        n = queue.pop(0)
        order.append(n)
        for m in adj[n]:
            indegree[m] -= 1
            if indegree[m] == 0:
                queue.append(m)

    if len(order) != len(nodes):
        remaining = sorted(n for n in nodes if n not in order)
        raise CycleError(remaining)
    return order


def unlocked(edges: dict[str, list[str]], done: set[str]) -> list[str]:
    """Nodi le cui dipendenze sono TUTTE in `done` e non sono già in `done` loro stessi."""
    out = []
    for n, deps in edges.items():
        if n in done:
            continue
        if all(d in done for d in deps):
            out.append(n)
    return sorted(out)


def from_flow_spec(spec) -> dict[str, list[str]]:
    """DAG decisioni -> workflow, costruito dai campi reali di workflows.yaml:
    ogni decisione `blocks` una lista di stream (nomi corti, es. 'S2'), ogni
    workflow `depends` da una lista di id (es. DEC-EST-001). Uniamo le due
    direzioni in un'unica mappa node->deps senza duplicare l'informazione.
    """
    edges: dict[str, list[str]] = {}

    for d in spec.decisions:
        edges.setdefault(d["id"], [])

    for wf_id, wf in spec.workflows.items():
        edges[wf_id] = list(wf.depends)

    short_to_full = {}
    for wf_id in spec.workflows:
        short = wf_id.split("-", 2)
        if len(short) >= 2:
            short_to_full[short[1]] = wf_id

    for d in spec.decisions:
        for short in d.get("blocks", []) or []:
            full = short_to_full.get(short)
            if full and full in edges and d["id"] not in edges[full]:
                edges[full].append(d["id"])

    return edges
