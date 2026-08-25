from __future__ import annotations

import argparse
import json
from pathlib import Path

from .contracts import ContractError, ContractRegistry


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate an OCP JSON contract")
    parser.add_argument("schema")
    parser.add_argument("payload", type=Path)
    args = parser.parse_args()
    registry = ContractRegistry(Path.cwd())
    try:
        payload = json.loads(args.payload.read_text(encoding="utf-8"))
        registry.validate(args.schema, payload)
    except (OSError, json.JSONDecodeError, ContractError) as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}))
        return 2
    print(json.dumps({"status": "PASS", "schema": args.schema, "payload": str(args.payload)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
