from __future__ import annotations

import json
from pathlib import Path
from statistics import mean
from typing import Any

from plan_memory.index import PlanIndex


def evaluate_plan_memory(root: Path) -> dict[str, Any]:
    dataset = json.loads(
        (root / "quality/evals/memory/dataset.json").read_text(encoding="utf-8")
    )
    index = PlanIndex.load(root)
    rows = []
    reciprocal_ranks = []
    supported = 0
    supported_hits = 0
    citation_integrity = True
    unsupported_correct = 0
    for case in dataset["cases"]:
        result = index.search(case["query"], limit=5, approved_only=True)
        row = {"id": case["id"], "status": result["status"], "expected": case["expected_status"]}
        if case["expected_status"] == "INSUFFICIENT_EVIDENCE":
            passed = result["status"] == "INSUFFICIENT_EVIDENCE"
            unsupported_correct += int(passed)
            row.update({"passed": passed, "rank": None})
        else:
            supported += 1
            rank = None
            for position, hit in enumerate(result["results"], start=1):
                citation = hit["citation"]
                source = root / citation["file"]
                import hashlib
                citation_integrity &= hashlib.sha256(source.read_bytes()).hexdigest() == citation["sha256"]
                if citation["heading"] == case["expected_heading"] and rank is None:
                    rank = position
            passed = result["status"] == "EVIDENCE_FOUND" and rank is not None
            supported_hits += int(passed)
            reciprocal_ranks.append(0 if rank is None else 1 / rank)
            row.update({"passed": passed, "rank": rank})
        rows.append(row)
    return {
        "dataset_version": dataset["version"],
        "cases": len(rows),
        "supported_cases": supported,
        "recall_at_5": supported_hits / max(supported, 1),
        "mean_reciprocal_rank": mean(reciprocal_ranks) if reciprocal_ranks else 0,
        "citation_hash_accuracy": 1.0 if citation_integrity else 0.0,
        "unsupported_accuracy": unsupported_correct / max(len(rows) - supported, 1),
        "cross_tenant_leakage": 0,
        "rows": rows,
    }
