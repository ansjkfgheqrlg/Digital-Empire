from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

from .index import PlanIndex
from .manifest import PlanManifest, PlanMemoryError


def root_path() -> Path:
    return Path(os.environ.get("ORCHESTRATION_ROOT", Path.cwd())).resolve()


def main() -> int:
    parser = argparse.ArgumentParser(description="Read-only Plan Memory Agent")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("verify")
    sub.add_parser("build")
    query = sub.add_parser("query")
    query.add_argument("text")
    query.add_argument("--limit", type=int, default=5)
    query.add_argument("--approved-only", action="store_true")
    args = parser.parse_args()
    root = root_path()

    try:
        if args.command == "verify":
            manifest = PlanManifest.load(root)
            print(json.dumps({"status": "PASS", "plans": len(manifest.records)}, indent=2))
            return 0
        if args.command == "build":
            index = PlanIndex.build(root)
            target = index.save()
            print(
                json.dumps(
                    {"status": "PASS", "chunks": len(index.chunks), "index": str(target)},
                    indent=2,
                )
            )
            return 0
        if args.command == "query":
            index = PlanIndex.load(root)
            print(
                json.dumps(
                    index.search(args.text, args.limit, args.approved_only),
                    indent=2,
                    ensure_ascii=False,
                )
            )
            return 0
    except PlanMemoryError as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}), file=sys.stderr)
        return 2
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
