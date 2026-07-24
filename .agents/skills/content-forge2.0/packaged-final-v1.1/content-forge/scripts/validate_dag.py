"""DAG validation utilities (cycle detection, orphan detection) per i workflow.

Used by:
- B5 workflow-builder-agent (validation durante BUILD)
- C3 target-schema-validator-agent (custom check per workflow)

Part of: content-forge

Library API:
    from validate_dag import has_cycle, find_orphans

CLI:
    python scripts/validate_dag.py <workflow-dir> [--json]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict, deque
from pathlib import Path


def has_cycle(edges: list[tuple[str, str]], nodes: list[str]) -> bool:
    """Kahn's topological sort. Ritorna True se contiene un ciclo."""
    indeg: dict[str, int] = defaultdict(int)
    adj: dict[str, list[str]] = defaultdict(list)
    for n in nodes:
        indeg[n] = 0  # init
    for a, b in edges:
        adj[a].append(b)
        indeg[b] += 1
    q = deque([n for n in nodes if indeg[n] == 0])
    seen = 0
    while q:
        n = q.popleft()
        seen += 1
        for m in adj[n]:
            indeg[m] -= 1
            if indeg[m] == 0:
                q.append(m)
    return seen != len(nodes)


def find_orphans(edges: list[tuple[str, str]], nodes: list[str],
                  start_nodes: list[str]) -> list[str]:
    """Nodi non raggiungibili dai trigger."""
    adj: dict[str, list[str]] = defaultdict(list)
    for a, b in edges:
        adj[a].append(b)
    visited: set[str] = set()
    q = deque(start_nodes)
    while q:
        n = q.popleft()
        if n in visited:
            continue
        visited.add(n)
        q.extend(adj[n])
    return [n for n in nodes if n not in visited]


def parse_flow_md(flow_md: Path) -> tuple[list[str], list[tuple[str, str]], list[str]]:
    """Parser semplice di flow.md per estrarre nodes, edges, start_nodes.

    Cerca pattern come:
    - "### Step 01 — Foo" → nodo "step-01"
    - "On success: → Step 02" → edge step-01 → step-02
    - "Trigger" section → start nodes
    """
    text = flow_md.read_text(encoding="utf-8")

    # Estrai nodi (step header)
    nodes = []
    node_re = re.compile(r"^###?\s+Step\s+(\d+)", re.MULTILINE | re.IGNORECASE)
    for m in node_re.finditer(text):
        nodes.append(f"step-{int(m.group(1)):02d}")

    # Estrai edge (On success/failure → Step X)
    edges: list[tuple[str, str]] = []
    current_step: str | None = None
    for line in text.split("\n"):
        m_step = node_re.match(line)
        if m_step:
            current_step = f"step-{int(m_step.group(1)):02d}"
            continue
        if current_step:
            m_next = re.search(r"(?:on\s+success|on\s+failure|→|->)\s*[:\s→]*\s*Step\s+(\d+)",
                                line, re.IGNORECASE)
            if m_next:
                edges.append((current_step, f"step-{int(m_next.group(1)):02d}"))

    # Heuristica: il primo step è start node
    start_nodes = [nodes[0]] if nodes else []

    return nodes, edges, start_nodes


def validate_workflow_dir(workflow_dir: Path) -> dict:
    """Valida un workflow-dir parsando flow.md."""
    flow_md = workflow_dir / "flow.md"
    if not flow_md.exists():
        return {
            "verdict": "FAIL",
            "issues": [f"flow.md non trovato in {workflow_dir}"],
            "nodes": [], "edges": [], "orphans": [],
        }
    nodes, edges, starts = parse_flow_md(flow_md)
    issues = []
    if not nodes:
        issues.append("Nessun step trovato in flow.md")
    if has_cycle(edges, nodes):
        issues.append("DAG contiene un ciclo")
    orphans = find_orphans(edges, nodes, starts)
    if orphans:
        issues.append(f"Step orfani (non raggiungibili dal trigger): {orphans}")
    return {
        "verdict": "PASS" if not issues else "FAIL",
        "issues": issues,
        "nodes_count": len(nodes),
        "edges_count": len(edges),
        "orphans": orphans,
        "nodes": nodes,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("workflow_dir", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)

    if not args.workflow_dir.exists():
        print(f"ERROR: dir non esiste: {args.workflow_dir}", file=sys.stderr)
        return 2

    result = validate_workflow_dir(args.workflow_dir)

    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        icon = "✅" if result["verdict"] == "PASS" else "❌"
        print(f"{icon} Workflow DAG validation: {result['verdict']}")
        print(f"   Nodes: {result['nodes_count']}, Edges: {result['edges_count']}")
        if result["orphans"]:
            print(f"   Orphans: {result['orphans']}")
        for issue in result["issues"]:
            print(f"   ⚠️  {issue}")

    return 0 if result["verdict"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
