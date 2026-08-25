from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from datetime import UTC, datetime
from pathlib import Path

from .models import ManifestError
from .registry import BuilderTeamRegistry
from .workflow import WorkItemPlanner


def project_root() -> Path:
    override = os.environ.get("ORCHESTRATION_ROOT")
    return Path(override).resolve() if override else Path.cwd().resolve()


def hash_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate(root: Path) -> int:
    evidence = BuilderTeamRegistry(root).validate()
    print(json.dumps({"status": "PASS", "evidence": evidence}, indent=2))
    return 0


def show_team(root: Path) -> int:
    team = BuilderTeamRegistry(root).load_team()
    payload = {
        "team": team.team_id,
        "version": team.version,
        "limits": {"max_wip": team.max_wip, "max_concurrency": team.max_concurrency},
        "agents": [
            {
                "id": agent.agent_id,
                "role": agent.role,
                "responsibility": agent.responsibility,
                "writes": list(agent.writes),
                "denied": list(agent.denied),
            }
            for agent in team.agents
        ],
    }
    print(json.dumps(payload, indent=2))
    return 0


def bootstrap(root: Path) -> int:
    evidence = BuilderTeamRegistry(root).validate()
    plans = sorted((root / "plans").glob("level-*.md"))
    checkpoint = {
        "checkpoint_id": "W0-BUILDER-SWARM",
        "checkpoint_version": "1.0",
        "created_at": datetime.now(UTC).isoformat(),
        "status": "BOOTSTRAPPED",
        "team_validation": evidence,
        "plans": [
            {"path": str(path.relative_to(root)), "sha256": hash_file(path)} for path in plans
        ],
        "constraints": {
            "ruflo_enabled": False,
            "production_credentials": False,
            "external_side_effects": False,
            "human_approval_required_for_activation": True,
        },
    }
    target = root / "memory_store" / "checkpoints" / "w0-builder-swarm.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(checkpoint, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PASS", "checkpoint": str(target)}, indent=2))
    return 0


def create_work_item(root: Path, args: argparse.Namespace) -> int:
    registry = BuilderTeamRegistry(root)
    registry.validate()
    planner = WorkItemPlanner(root)
    item = planner.create(args.id, args.title, args.risk)
    checkpoint = planner.checkpoint(item)
    target = root / "memory_store" / "checkpoints" / f"{args.id.lower()}.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists() and not args.force:
        raise ManifestError(f"Checkpoint exists: {target}; use --force to replace")
    target.write_text(json.dumps(checkpoint, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "CREATED", "checkpoint": str(target)}, indent=2))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Governed Builder Team control CLI")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("validate")
    commands.add_parser("show-team")
    commands.add_parser("bootstrap")
    create = commands.add_parser("create-work-item")
    create.add_argument("--id", required=True)
    create.add_argument("--title", required=True)
    create.add_argument("--risk", choices=["R0", "R1", "R2", "R3"], required=True)
    create.add_argument("--force", action="store_true")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    root = project_root()
    try:
        if args.command == "validate":
            return validate(root)
        if args.command == "show-team":
            return show_team(root)
        if args.command == "bootstrap":
            return bootstrap(root)
        if args.command == "create-work-item":
            return create_work_item(root, args)
    except (ManifestError, ValueError) as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}), file=sys.stderr)
        return 2
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
