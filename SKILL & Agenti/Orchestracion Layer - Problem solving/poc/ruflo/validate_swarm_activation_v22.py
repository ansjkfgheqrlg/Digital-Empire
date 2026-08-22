#!/usr/bin/env python3
"""Validate the bounded RuFLO registry for NERVE-SOLVE Component A v2.2 migration.

This validates coordination metadata, pins and permission manifests. It deliberately
does not claim independent worker execution, task dispatch or production authority.
"""

from __future__ import annotations

import csv
import hashlib
import json
import os
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT.parent / "ruflo-source"
EXPECTED_SWARM = "swarm-1786609847075-cjvrv8"
EXPECTED_COMMIT = "5efd5937e588d6e2d20d974f14593a4795562ef8"
EXPECTED_TREE = "6ae9e1a6e5a35ff117e608a96b32617ae860012a"
EXPECTED_PACKAGE_HASH = "26dcf4662f6eb78c9c9ca982e94b1c90e07140cdfcd4fdb0fa264067f426acb6"
EXPECTED_LOCK_HASH = "963a94087412e498f2a7f5cca020337e9d341c28fee172fead6ae562e8f75931"
EXPECTED_ROLES = {
    "coordinator",
    "core-architect",
    "coder",
    "tester",
    "security-auditor",
    "reviewer",
}

assertions = 0


def check(condition: bool, message: str) -> None:
    global assertions
    assertions += 1
    if not condition:
        raise AssertionError(message)


def load_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git(*args: str) -> str:
    return subprocess.check_output(
        ["git", *args], cwd=SOURCE, text=True, stderr=subprocess.STDOUT
    ).strip()


check(sha256(ROOT / "package.json") == EXPECTED_PACKAGE_HASH, "package.json drift")
check(sha256(ROOT / "package-lock.json") == EXPECTED_LOCK_HASH, "package-lock drift")

pin = load_json(ROOT / "RUFLO_SOURCE_PIN.json")
check(isinstance(pin, dict), "source pin is not an object")
check(pin["source_pin"]["tag"] == "v3.38.8", "wrong source tag")
check(pin["source_pin"]["commit"] == EXPECTED_COMMIT, "wrong source pin commit")
check(pin["source_pin"]["tree"] == EXPECTED_TREE, "wrong source tree")
check(pin["requested_clone"]["result"] == "BLOCKED_AUTH_REQUIRED", "gh outcome missing")
check(pin["fallback_clone"]["result"] == "PASS", "public clone fallback missing")
check(not any(pin["authority"].values()), "RuFLO authority must remain false")

check(git("rev-parse", "HEAD") == EXPECTED_COMMIT, "checked-out commit drift")
check(git("rev-parse", "HEAD^{tree}") == EXPECTED_TREE, "checked-out tree drift")
check(git("describe", "--tags", "--exact-match", "HEAD") == "v3.38.8", "tag mismatch")
check(git("status", "--porcelain") == "", "source checkout is dirty")

swarm_store = load_json(ROOT / ".claude-flow/swarm/swarm-state.json")
check(isinstance(swarm_store, dict), "swarm store is not an object")
swarm = swarm_store["swarms"][EXPECTED_SWARM]
check(swarm["status"] == "running", "registry swarm is not running")
check(swarm["topology"] == "hierarchical", "topology drift")
check(swarm["maxAgents"] == 6, "max-agent drift")
check(swarm["config"]["autoScaling"] is False, "auto-scaling must be off")
check(len(swarm["agents"]) == 6, "expected six registered agents")
check(swarm["tasks"] == [], "known swarm index must remain explicitly observed empty")

agent_store = load_json(ROOT / ".claude-flow/agents/store.json")
agents = agent_store["agents"]
check(len(agents) == 6, "agent-store count mismatch")
check({a["agentType"] for a in agents.values()} == EXPECTED_ROLES, "role set mismatch")
for agent in agents.values():
    check(agent["status"] == "active", f"inactive agent {agent['agentId']}")
    check(agent["config"]["autoTools"] is False, f"autoTools enabled for {agent['agentId']}")

with (ROOT / "swarm-a-v22-migration-activation-manifest.tsv").open(
    encoding="utf-8", newline=""
) as handle:
    manifest = list(csv.DictReader(handle, delimiter="\t"))
check(len(manifest) == 6, "migration manifest must contain six assignments")
check({row["role"] for row in manifest} == EXPECTED_ROLES, "manifest role mismatch")

migration_ids = {row["task_id"] for row in manifest}
task_store = load_json(ROOT / ".claude-flow/tasks/store.json")
tasks = task_store["tasks"]
check(migration_ids <= set(tasks), "manifest task missing from task store")
for row in manifest:
    task = tasks[row["task_id"]]
    check(task["status"] == "in_progress", f"task not assigned: {row['task_id']}")
    check(task["assignedTo"] == [row["agent_id"]], f"assignment mismatch: {row['task_id']}")
    check("v2.2" in task["tags"], f"v2.2 tag missing: {row['task_id']}")
    check(
        agents[row["agent_id"]]["currentTask"] == row["task_id"],
        f"agent currentTask mismatch: {row['agent_id']}",
    )

old_tasks = [task for task_id, task in tasks.items() if task_id not in migration_ids]
check(len(old_tasks) == 10, "unexpected historical task count")
for task in old_tasks:
    check(task["status"] == "cancelled", f"historical task remains live: {task['taskId']}")

permissions = [
    json.loads(line)
    for line in (ROOT / ".swarm/permissions.jsonl").read_text(encoding="utf-8").splitlines()
    if line.strip()
]
check(len(permissions) == 6, "permission role count mismatch")
check({row["role"] for row in permissions} == EXPECTED_ROLES, "permission role mismatch")
for row in permissions:
    denied = set(row["deniedTools"])
    check({"Bash", "Edit", "Write", "NotebookEdit"} <= denied, f"write tool allowed: {row['role']}")
    check(row["allowedNetworkHosts"] == [], f"network host allowed: {row['role']}")
    check(any("v2.2" in path for path in row["allowedPaths"]), f"v2.2 path missing: {row['role']}")
    check("../../implementation/config/trust/**" in row["deniedPaths"], f"trust deny missing: {row['role']}")

pid_path = ROOT / ".claude-flow/daemon.pid"
check(pid_path.is_file(), "daemon PID file missing")
pid = int(pid_path.read_text(encoding="utf-8").strip())
try:
    os.kill(pid, 0)
except ProcessLookupError as exc:
    raise AssertionError(f"daemon PID {pid} is not alive") from exc
assertions += 1

migration_tasks = [tasks[task_id] for task_id in migration_ids]
executed = any(
    task.get("progress", 0) > 0 or task.get("completedAt") or task.get("output")
    for task in migration_tasks
)
dependencies_persisted = all("dependencies" in task for task in migration_tasks[2:])
last_activity_observed = any(agent.get("lastActivity") for agent in agents.values())

print(f"PASS: {assertions} bounded coordination assertions")
print(f"daemon_pid={pid}; swarm={EXPECTED_SWARM}; roles=6; migration_tasks=6")
print("source=v3.38.8@" + EXPECTED_COMMIT)
print("WARNING: independent_worker_execution=" + ("OBSERVED" if executed else "NOT_PROVEN"))
print("WARNING: task_index_consistency=FAIL (swarm index is empty while task store has records)")
print("WARNING: dependency_persistence=" + ("OBSERVED" if dependencies_persisted else "NOT_OBSERVED"))
print("WARNING: agent_last_activity=" + ("OBSERVED" if last_activity_observed else "NOT_OBSERVED"))
print("DISPOSITION: ACTIVE_COORDINATION_REGISTRY_LIMITED_NOT_EXECUTION_QUALIFIED")
