#!/usr/bin/env python3
"""Deterministic gate for MB-OS planning claims."""
from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def validate_dag(tasks: dict[str, dict]) -> None:
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(task_id: str) -> None:
        if task_id in visited:
            return
        if task_id in visiting:
            raise AssertionError(f"Dependency cycle at {task_id}")
        visiting.add(task_id)
        for dependency in tasks[task_id]["dependencies"]:
            assert dependency in tasks, f"Unknown dependency {dependency} from {task_id}"
            visit(dependency)
        visiting.remove(task_id)
        visited.add(task_id)

    for task_id in tasks:
        visit(task_id)


def main() -> None:
    plan = json.loads((ROOT / "PLAN.json").read_text(encoding="utf-8"))
    phases = plan["phases"]
    task_list = [task for phase in phases for task in phase["tasks"]]
    tasks = {task["id"]: task for task in task_list}
    assert len(phases) == plan["counts"]["phases"] == 10
    assert len(task_list) == len(tasks) == plan["counts"]["tasks"] == 32
    assert all(task_id in tasks for task_id in plan["critical_path"])
    validate_dag(tasks)

    brainstorming = (ROOT / "02-BRAINSTORMING-MASTER.md").read_text(encoding="utf-8")
    ideas = re.findall(r"^\d+\. \*\*([BCRVGODM]\d{2})\s+—", brainstorming, re.MULTILINE)
    assert len(ideas) == len(set(ideas)) == 64, f"Brainstorm ideas: {len(ideas)}/{len(set(ideas))}"

    matrix = (ROOT / "03-DECISION-MATRIX.md").read_text(encoding="utf-8")
    matrix_ids = re.findall(r"^\| (S\d{2}) \|", matrix, re.MULTILINE)
    assert len(matrix_ids) == len(set(matrix_ids)) == 16, f"Matrix initiatives: {len(matrix_ids)}"

    calendar = (ROOT / "05-CALENDAR-28D-SEED.md").read_text(encoding="utf-8")
    rows = re.findall(
        r"^\|\s*(\d+)\s*\|\s*(Reel|Carousel)\s*\|\s*(P[1-5])\s*\|\s*([AB])\s*\|\s*([LE])\s*\|",
        calendar,
        re.MULTILINE,
    )
    days = [int(row[0]) for row in rows]
    assert days == list(range(1, 29)), f"Calendar days: {days}"
    formats = Counter(row[1] for row in rows)
    pillars = Counter(row[2] for row in rows)
    hooks = Counter(row[3] for row in rows)
    slots = Counter(row[4] for row in rows)
    assert formats == {"Reel": 16, "Carousel": 12}, formats
    assert pillars == {"P1": 8, "P2": 7, "P3": 6, "P4": 4, "P5": 3}, pillars
    assert hooks == {"A": 14, "B": 14}, hooks
    assert slots == {"L": 14, "E": 14}, slots

    print("PLAN GATE PASS")
    print(f"- phases: {len(phases)}")
    print(f"- tasks: {len(tasks)} (DAG valid)")
    print(f"- brainstorming ideas: {len(ideas)}")
    print(f"- matrix initiatives: {len(matrix_ids)}")
    print(f"- calendar: {dict(formats)}, {dict(pillars)}, hooks={dict(hooks)}, slots={dict(slots)}")


if __name__ == "__main__":
    main()
