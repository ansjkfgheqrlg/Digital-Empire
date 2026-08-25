#!/usr/bin/env python3
"""Standalone health check script for local orchestration layer environment."""
from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from builder_team.registry import BuilderTeamRegistry
from orchestrator.application.skill_registry import SkillRegistry
from plan_memory.manifest import PlanManifest


def check_all() -> int:
    checks_passed = 0
    total_checks = 4

    print("=== OCP LOCAL HEALTH CHECK ===")

    # 1. Plans manifest
    try:
        manifest = PlanManifest.load(REPO_ROOT)
        highest = max((r.level for r in manifest.records if r.is_approved), default=0)
        print(f"[OK] Plans manifest: {len(manifest.records)} levels, highest approved: L{highest}")
        checks_passed += 1
    except Exception as exc:
        print(f"[FAIL] Plans manifest error: {exc}")

    # 2. Builder team
    try:
        team = BuilderTeamRegistry(REPO_ROOT).load_team()
        print(f"[OK] Builder team: {team.team_id} (version {team.version}, {len(team.agents)} roles)")
        checks_passed += 1
    except Exception as exc:
        print(f"[FAIL] Builder team error: {exc}")

    # 3. Skills registry
    try:
        skills = SkillRegistry(REPO_ROOT / "skills")
        names = skills.list_skills()
        print(f"[OK] Skills registered ({len(names)}): {', '.join(names)}")
        checks_passed += 1
    except Exception as exc:
        print(f"[FAIL] Skills error: {exc}")

    # 4. Contracts source of truth
    try:
        contracts_dir = REPO_ROOT / "contracts" / "schemas"
        schemas = list(contracts_dir.rglob("*.json"))
        print(f"[OK] Schemas found: {len(schemas)}")
        checks_passed += 1
    except Exception as exc:
        print(f"[FAIL] Contracts error: {exc}")

    print("==============================")
    print(f"Result: {checks_passed}/{total_checks} checks passed.")
    return 0 if checks_passed == total_checks else 1


if __name__ == "__main__":
    sys.exit(check_all())
