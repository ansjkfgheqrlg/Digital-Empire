"""KG loader & accessors.

Carica e valida `kg.json`. Espone API uniforme per accesso a atomi, cluster, edge.
Usato da: tutti gli agenti che leggono il KG (A4, A5, B1-B8, C1, C3).

Part of: content-forge / scripts/lib
"""
from __future__ import annotations

import json
from collections import defaultdict, deque
from pathlib import Path
from typing import Any

__all__ = [
    "KG",
    "load_kg",
    "topological_atoms",
    "find_clusters_containing",
]


class KG:
    """Wrapper sopra kg.json con accessor convenienti."""

    def __init__(self, data: dict):
        self.data = data
        self.atoms: list[dict] = data.get("atoms", [])
        self.clusters: list[dict] = data.get("clusters", [])
        self.edges: list[dict] = data.get("edges", [])
        self.gaps: list[dict] = data.get("gaps", [])
        self.stats: dict = data.get("stats", {})
        self.source_meta: dict = data.get("source_meta", {})

        # Indici interni
        self._atoms_by_id: dict[str, dict] = {a["id"]: a for a in self.atoms}
        self._clusters_by_id: dict[str, dict] = {c["id"]: c for c in self.clusters}
        self._edges_from: dict[str, list[dict]] = defaultdict(list)
        self._edges_to: dict[str, list[dict]] = defaultdict(list)
        for e in self.edges:
            self._edges_from[e["from"]].append(e)
            self._edges_to[e["to"]].append(e)

    # --- Lookup base ---

    def atom(self, atom_id: str) -> dict | None:
        return self._atoms_by_id.get(atom_id)

    def cluster(self, cluster_id: str) -> dict | None:
        return self._clusters_by_id.get(cluster_id)

    def atoms_in_cluster(self, cluster_id: str) -> list[dict]:
        cluster = self.cluster(cluster_id)
        if not cluster:
            return []
        return [self.atom(aid) for aid in cluster.get("atom_ids", []) if self.atom(aid)]

    # --- Edges ---

    def outgoing(self, atom_id: str, edge_type: str | None = None) -> list[dict]:
        edges = self._edges_from.get(atom_id, [])
        if edge_type:
            edges = [e for e in edges if e.get("type") == edge_type]
        return edges

    def incoming(self, atom_id: str, edge_type: str | None = None) -> list[dict]:
        edges = self._edges_to.get(atom_id, [])
        if edge_type:
            edges = [e for e in edges if e.get("type") == edge_type]
        return edges

    def prerequisites(self, atom_id: str) -> list[dict]:
        """Atomi che sono prerequisiti di atom_id."""
        return [self.atom(e["from"]) for e in self.incoming(atom_id, "prerequisite") if self.atom(e["from"])]

    def related(self, atom_id: str) -> list[dict]:
        """Atomi correlati (see_also, sibling_of, applies_in)."""
        out_ids = {e["to"] for e in self.outgoing(atom_id) if e.get("type") in ("see_also", "sibling_of", "applies_in")}
        in_ids = {e["from"] for e in self.incoming(atom_id) if e.get("type") in ("see_also", "sibling_of")}
        ids = out_ids | in_ids
        return [self.atom(i) for i in ids if self.atom(i)]

    # --- Iterazione ---

    def __iter__(self):
        return iter(self.atoms)

    def __len__(self) -> int:
        return len(self.atoms)


def load_kg(path: str | Path) -> KG:
    """Carica kg.json e ritorna oggetto KG. Solleva ValueError se schema fondamentale è violato."""
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"KG file non trovato: {path}")
    with path.open(encoding="utf-8") as f:
        data = json.load(f)
    # Validazione minima
    for required in ["atoms", "clusters", "edges"]:
        if required not in data:
            raise ValueError(f"kg.json non valido: manca campo '{required}'")
    # Validazione ID univoci
    atom_ids = [a.get("id") for a in data["atoms"]]
    if len(atom_ids) != len(set(atom_ids)):
        raise ValueError("kg.json non valido: atom IDs non univoci")
    return KG(data)


def topological_atoms(kg: KG, restrict_to: list[str] | None = None) -> list[str]:
    """Topological sort degli atomi via Kahn (basato su edge `prerequisite`).
    Ritorna lista di atom_id in ordine: prima i prerequisiti, poi i dipendenti.
    Se ci sono cicli (non dovrebbero esserci) rompe l'ordine ma include tutti.
    """
    if restrict_to is None:
        nodes = [a["id"] for a in kg.atoms]
    else:
        nodes = list(restrict_to)
    nodes_set = set(nodes)

    # Filtra solo edge tra i nodi del set
    indeg: dict[str, int] = defaultdict(int)
    adj: dict[str, list[str]] = defaultdict(list)
    for n in nodes:
        indeg[n] = 0
    for e in kg.edges:
        if e.get("type") == "prerequisite" and e["from"] in nodes_set and e["to"] in nodes_set:
            adj[e["from"]].append(e["to"])
            indeg[e["to"]] += 1

    q = deque([n for n in nodes if indeg[n] == 0])
    order: list[str] = []
    while q:
        n = q.popleft()
        order.append(n)
        for m in adj[n]:
            indeg[m] -= 1
            if indeg[m] == 0:
                q.append(m)

    # Se restano nodi (ciclo o orfani da indeg starter sbagliato), append in coda
    remaining = [n for n in nodes if n not in order]
    order.extend(remaining)
    return order


def find_clusters_containing(kg: KG, atom_id: str) -> list[dict]:
    """Cluster (di solito 1) che contengono questo atomo."""
    return [c for c in kg.clusters if atom_id in c.get("atom_ids", [])]
