from __future__ import annotations

import asyncio
import hashlib
import secrets
from pathlib import Path
from typing import Callable

from orchestrator.adapters.postgres.outbox import PostgresOutbox
from orchestrator.adapters.postgres.queue import LeaseLost, PostgresTaskQueue
from orchestrator.adapters.postgres.uow import PostgresUnitOfWork
from orchestrator.application.local_vertical_slice import RepositoryAdrVerticalSlice
from orchestrator.governance.grants import CapabilityGrantService, InMemoryCapabilityStore
from orchestrator.governance.policy import OpaPolicyClient


class WorkerService:
    def __init__(
        self,
        *,
        root: Path,
        tenant_id: str,
        worker_id: str,
        repository_root: Path,
        artifact_root: Path,
        uow_factory: Callable[[str], PostgresUnitOfWork],
        policy: OpaPolicyClient,
    ):
        self.root = root
        self.tenant_id = tenant_id
        self.worker_id = worker_id
        self.repository_root = repository_root
        self.artifact_root = artifact_root
        self.uow_factory = uow_factory
        self.policy = policy
        self.stop_event = asyncio.Event()

    async def run_once(self) -> bool:
        raw_token = secrets.token_urlsafe(32)
        token_hash = "sha256:" + hashlib.sha256(raw_token.encode()).hexdigest()
        async with self.uow_factory(self.tenant_id) as uow:
            queue = PostgresTaskQueue(uow.session, self.tenant_id)
            task = await queue.claim(self.worker_id, token_hash, 30)
            if task is None:
                await uow.commit()
                return False
            workflow = await uow.workflows.get(str(task["workflow_id"]))
            await uow.commit()
        if workflow is None:
            raise RuntimeError("Claimed task references missing workflow")

        skill_input = workflow["constraints"].get("skill_input", {})
        runner = RepositoryAdrVerticalSlice(
            root=self.root,
            repository_root=self.repository_root,
            artifact_root=self.artifact_root,
            policy=self.policy,
            grants=CapabilityGrantService(InMemoryCapabilityStore()),
        )
        try:
            result = await runner.run(
                tenant_id=self.tenant_id,
                requested_by=workflow["requested_by"],
                repository_files=list(skill_input["repository_files"]),
                artifact_path=skill_input["artifact_path"],
                workflow_id=str(workflow["workflow_id"]),
                idempotency_key=workflow["idempotency_key"],
            )
            async with self.uow_factory(self.tenant_id) as uow:
                current = await uow.workflows.load_aggregate(str(workflow["workflow_id"]))
                if current is None:
                    raise RuntimeError("Workflow disappeared before result commit")
                await uow.workflows.persist_event_stream(
                    current,
                    previous_version=current.version,
                    events=list(result.event_stream[1:]),
                    trace_id=f"worker-{self.worker_id}",
                )
                await PostgresTaskQueue(uow.session, self.tenant_id).accept_result(
                    str(task["task_id"]),
                    self.worker_id,
                    token_hash,
                    succeeded=True,
                    output_ref=f"artifact://{result.artifact_path}#sha256:{result.artifact_sha256}",
                )
                await uow.commit()
            return True
        except Exception as exc:
            async with self.uow_factory(self.tenant_id) as uow:
                try:
                    await PostgresTaskQueue(uow.session, self.tenant_id).accept_result(
                        str(task["task_id"]),
                        self.worker_id,
                        token_hash,
                        succeeded=False,
                        failure_code=type(exc).__name__,
                    )
                    await uow.commit()
                except LeaseLost:
                    await uow.rollback()
            raise

    async def run(self, poll_seconds: float = 0.5) -> None:
        while not self.stop_event.is_set():
            processed = await self.run_once()
            if not processed:
                try:
                    await asyncio.wait_for(self.stop_event.wait(), timeout=poll_seconds)
                except TimeoutError:
                    pass

    def stop(self) -> None:
        self.stop_event.set()


class OutboxPublisherService:
    def __init__(self, uow_factory: Callable[[str], PostgresUnitOfWork], tenant_id: str, sink):
        self.uow_factory = uow_factory
        self.tenant_id = tenant_id
        self.sink = sink

    async def publish_once(self, batch_size: int = 100) -> int:
        async with self.uow_factory(self.tenant_id) as uow:
            outbox = PostgresOutbox(uow.session)
            events = await outbox.claim_batch(batch_size)
            published = []
            for event in events:
                try:
                    await self.sink(event)
                    published.append(str(event["event_id"]))
                except Exception as exc:
                    await outbox.mark_failed(str(event["event_id"]), str(exc))
            await outbox.mark_published(published)
            await uow.commit()
            return len(published)
