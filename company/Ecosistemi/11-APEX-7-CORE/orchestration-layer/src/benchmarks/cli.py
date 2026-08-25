from __future__ import annotations

import argparse
import asyncio
import json
from pathlib import Path

from .w9 import run_w9_benchmark


def main() -> int:
    parser = argparse.ArgumentParser(description="Run W9 deterministic baseline benchmarks")
    parser.add_argument("--root", default=".")
    parser.add_argument("--output", default="quality/benchmarks/w9-baseline.json")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    report = asyncio.run(run_w9_benchmark(root))
    output = root / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(output), "hard_gates": report["hard_gates"]}, indent=2))
    return 0 if all(report["hard_gates"].values()) else 2


if __name__ == "__main__":
    raise SystemExit(main())
