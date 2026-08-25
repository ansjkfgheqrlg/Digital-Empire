from __future__ import annotations

import argparse
import asyncio
import json
from pathlib import Path

from .executor import BuilderSwarmExecutor, LocalBuilderHandlers
from .workflow import WorkItemPlanner


async def run(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    item = WorkItemPlanner(root).create(args.id, args.title, args.risk)
    executor = BuilderSwarmExecutor(root, LocalBuilderHandlers(root))
    result = await executor.execute(item, touches_ruflo=args.touches_ruflo)
    checkpoint = executor.save_run(result)
    print(
        json.dumps(
            {
                "run_id": result.run_id,
                "status": result.status,
                "attempt": result.attempt,
                "checkpoint": str(checkpoint),
            },
            indent=2,
        )
    )
    return 0 if result.status == "READY_TO_MERGE" else 2


def main() -> int:
    parser = argparse.ArgumentParser(description="Activate the Builder Swarm in a sandbox")
    parser.add_argument("--root", default=".")
    parser.add_argument("--id", required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--risk", choices=["R0", "R1", "R2", "R3"], default="R1")
    parser.add_argument("--touches-ruflo", action="store_true")
    return asyncio.run(run(parser.parse_args()))


if __name__ == "__main__":
    raise SystemExit(main())
