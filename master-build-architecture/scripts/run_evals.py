#!/usr/bin/env python3
"""Run structural acceptance evaluations and score each one from 1 to 5."""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path


def score(condition_count: int, total: int) -> int:
    """Convert satisfied deterministic conditions to a transparent 1–5 score."""
    if total == 0:
        return 1
    ratio = condition_count / total
    if ratio == 1:
        return 5
    if ratio >= 0.75:
        return 4
    if ratio >= 0.5:
        return 3
    if ratio >= 0.25:
        return 2
    return 1


def main() -> int:
    """Evaluate repository capabilities without pretending to test external services."""
    root = Path(__file__).resolve().parents[1]
    evals = json.loads((root / "evals/evals.json").read_text(encoding="utf-8"))
    complete_agents = sum(
        len(list(directory.glob("*.md"))) >= 7
        for directory in (root / "agents").glob("*/*")
        if directory.is_dir()
    )
    checks: list[tuple[str, list[bool], str]] = [
        (
            "basic-swarm-with-memory",
            [complete_agents >= 10, (root / "memory/MEMORY-INDEX.md").is_file(), (root / "scripts/memory_manager.py").is_file(), (root / "governance/MEMORY-PROTOCOL.md").is_file()],
            "Structural readiness for a memory-backed swarm; no external Ruflo runtime was invoked.",
        ),
        (
            "meta-transform-knowledge-pack",
            [complete_agents >= 25, (root / "references/knowledge-pack/00-master/master.md").is_file(), (root / "scripts/validate_skill.py").is_file(), (root / "workflows/README.md").is_file()],
            "Structural readiness for meta transformation; this is not a generative-model benchmark.",
        ),
        (
            "full-ecosystem-with-ruflo-integration",
            [(root / "governance/REFERENCE-LIBRARY.md").is_file(), (root / "scripts/self_improve.py").is_file(), (root / "memory/self-improvement/PLAN-v1.md").is_file(), (root / "agents/OPERATING-REGISTRY.md").is_file()],
            "Architecture controls, self-improvement plan and agent registry are present; external integrations were not run.",
        ),
    ]
    results: list[dict[str, object]] = []
    for identifier, assertions, scope in checks:
        results.append({"id": identifier, "score_1_to_5": score(sum(assertions), len(assertions)), "passed": sum(assertions), "total": len(assertions), "scope": scope})
    output = {"generated_at": datetime.now(timezone.utc).isoformat(), "catalogue_count": len(evals.get("evals", [])), "results": results}
    destination = root / "memory/self-improvement/eval-scores.json"
    destination.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    for result in results:
        print(f"{result['id']}: {result['score_1_to_5']}/5 ({result['passed']}/{result['total']})")
    return 0 if all(item["score_1_to_5"] == 5 for item in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
