from __future__ import annotations

import argparse
import asyncio
import hashlib
import json
from pathlib import Path

from orchestrator.application.local_vertical_slice import RepositoryAdrVerticalSlice
from orchestrator.governance.grants import CapabilityGrantService, InMemoryCapabilityStore
from orchestrator.governance.policy import OpaPolicyClient


async def run(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    policy_hash = "sha256:" + hashlib.sha256(
        (root / "policies/authorization.rego").read_bytes()
    ).hexdigest()
    policy = OpaPolicyClient(args.opa_url, policy_hash)
    try:
        runner = RepositoryAdrVerticalSlice(
            root=root,
            repository_root=Path(args.repository).resolve(),
            artifact_root=Path(args.artifacts).resolve(),
            policy=policy,
            grants=CapabilityGrantService(InMemoryCapabilityStore()),
        )
        result = await runner.run(
            tenant_id=args.tenant,
            requested_by=args.requested_by,
            repository_files=args.file,
            artifact_path=args.artifact_path,
        )
        payload = dict(result.__dict__)
        payload.pop("event_stream", None)
        print(json.dumps(payload, indent=2, ensure_ascii=False))
        return 0
    finally:
        await policy.close()


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the local R1 repository ADR slice")
    parser.add_argument("--root", default=".")
    parser.add_argument("--repository", required=True)
    parser.add_argument("--artifacts", required=True)
    parser.add_argument("--file", action="append", required=True)
    parser.add_argument("--artifact-path", default="adr/0001-repository.md")
    parser.add_argument("--tenant", default="local-test")
    parser.add_argument("--requested-by", default="local-operator")
    parser.add_argument("--opa-url", default="http://127.0.0.1:8181")
    args = parser.parse_args()
    return asyncio.run(run(args))


if __name__ == "__main__":
    raise SystemExit(main())
