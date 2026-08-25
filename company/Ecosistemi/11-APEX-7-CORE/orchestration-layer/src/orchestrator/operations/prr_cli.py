from __future__ import annotations

import argparse
import json
from pathlib import Path

from .prr import ProductionReadinessReview


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the Production Readiness Review")
    parser.add_argument("--root", default=".")
    parser.add_argument("--output", default="quality/evidence/w11-prr-result.json")
    parser.add_argument("--profile", choices=["production", "local-pilot"], default="production")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    review = ProductionReadinessReview(root)
    result = review.evaluate_local_pilot() if args.profile == "local-pilot" else review.evaluate()
    target = root / args.output
    target.parent.mkdir(parents=True, exist_ok=True)
    review.save(result, target)
    print(json.dumps({"verdict": result.verdict, "blocked": list(result.blocked), "output": str(target)}, indent=2))
    return 0 if result.verdict in {"GO", "GO_LOCAL_PILOT"} else 2


if __name__ == "__main__":
    raise SystemExit(main())
