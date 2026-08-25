from __future__ import annotations

import asyncio
import os
import signal
from pathlib import Path

from orchestrator.adapters.postgres.uow import PostgresUnitOfWork, create_engine_and_factory
from orchestrator.governance.policy import OpaPolicyClient
from orchestrator.worker.service import WorkerService


async def serve() -> None:
    root = Path(os.environ.get("ORCHESTRATION_ROOT", ".")).resolve()
    tenant = os.environ.get("OCP_TENANT_ID", "local-pilot")
    engine, factory = create_engine_and_factory(os.environ["OCP_DATABASE_URL"])
    policy_path = root / "policies/authorization.rego"
    import hashlib
    policy_hash = "sha256:" + hashlib.sha256(policy_path.read_bytes()).hexdigest()
    policy = OpaPolicyClient(os.environ.get("OCP_OPA_URL", "http://127.0.0.1:8181"), policy_hash)
    worker = WorkerService(
        root=root,
        tenant_id=tenant,
        worker_id=os.environ.get("OCP_WORKER_ID", "worker-local-1"),
        repository_root=Path(os.environ["OCP_REPOSITORY_ROOT"]).resolve(),
        artifact_root=Path(os.environ.get("OCP_ARTIFACT_ROOT", "./artifacts")).resolve(),
        uow_factory=lambda tenant_id: PostgresUnitOfWork(factory, tenant_id),
        policy=policy,
    )
    loop = asyncio.get_running_loop()
    for name in (signal.SIGINT, signal.SIGTERM):
        loop.add_signal_handler(name, worker.stop)
    try:
        await worker.run()
    finally:
        await policy.close()
        await engine.dispose()


def main() -> None:
    asyncio.run(serve())


if __name__ == "__main__":
    main()
