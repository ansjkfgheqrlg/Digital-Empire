from __future__ import annotations

from datetime import timedelta
from typing import Any

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession


CLAIM_TASK = text("""
WITH candidate AS (
  SELECT task.task_id
  FROM tasks AS task
  JOIN workflows AS workflow
    ON workflow.tenant_id = task.tenant_id
   AND workflow.workflow_id = task.workflow_id
  WHERE task.tenant_id = :tenant_id
    AND workflow.status NOT IN (
      'CANCEL_REQUESTED','CANCELLING','CANCELLED','COMPENSATING','COMPENSATED',
      'COMPLETED','FAILED','REJECTED','MANUAL_INTERVENTION'
    )
    AND task.attempt < task.max_attempts
    AND (
      (task.status IN ('READY', 'RETRY_WAIT') AND task.ready_at <= now())
      OR
      (task.status IN ('LEASED', 'RUNNING') AND task.leased_until < now())
    )
  ORDER BY task.ready_at, task.created_at
  FOR UPDATE OF task SKIP LOCKED
  LIMIT 1
)
UPDATE tasks AS task
SET status = 'LEASED',
    leased_by = :worker_id,
    leased_until = now() + (:lease_seconds * interval '1 second'),
    execution_token_hash = :execution_token_hash,
    attempt = attempt + 1,
    version = version + 1,
    updated_at = now()
FROM candidate
WHERE task.task_id = candidate.task_id
RETURNING task.*
""")

HEARTBEAT = text("""
UPDATE tasks
SET leased_until = now() + (:lease_seconds * interval '1 second'), updated_at = now()
WHERE task_id = :task_id
  AND tenant_id = :tenant_id
  AND status IN ('LEASED', 'RUNNING')
  AND leased_by = :worker_id
  AND execution_token_hash = :execution_token_hash
  AND leased_until > now()
RETURNING leased_until
""")

ACCEPT_RESULT = text("""
UPDATE tasks
SET status = :target_status,
    output_ref = :output_ref,
    failure_code = :failure_code,
    leased_by = NULL,
    leased_until = NULL,
    execution_token_hash = NULL,
    version = version + 1,
    updated_at = now()
WHERE task_id = :task_id
  AND tenant_id = :tenant_id
  AND status IN ('LEASED', 'RUNNING')
  AND leased_by = :worker_id
  AND execution_token_hash = :execution_token_hash
  AND leased_until > now()
RETURNING version
""")


class LeaseLost(RuntimeError):
    pass


class PostgresTaskQueue:
    def __init__(self, session: AsyncSession, tenant_id: str):
        self.session = session
        self.tenant_id = tenant_id

    async def claim(
        self,
        worker_id: str,
        execution_token_hash: str,
        lease_seconds: int = 30,
    ) -> dict[str, Any] | None:
        if not 5 <= lease_seconds <= 300:
            raise ValueError("lease_seconds must be 5..300")
        result = await self.session.execute(
            CLAIM_TASK,
            {
                "tenant_id": self.tenant_id,
                "worker_id": worker_id,
                "execution_token_hash": execution_token_hash,
                "lease_seconds": lease_seconds,
            },
        )
        row = result.mappings().one_or_none()
        return dict(row) if row else None

    async def heartbeat(
        self,
        task_id: str,
        worker_id: str,
        execution_token_hash: str,
        lease_seconds: int = 30,
    ) -> None:
        result = await self.session.execute(
            HEARTBEAT,
            {
                "task_id": task_id,
                "tenant_id": self.tenant_id,
                "worker_id": worker_id,
                "execution_token_hash": execution_token_hash,
                "lease_seconds": lease_seconds,
            },
        )
        if result.scalar_one_or_none() is None:
            raise LeaseLost("Heartbeat rejected because the lease is stale or lost")

    async def accept_result(
        self,
        task_id: str,
        worker_id: str,
        execution_token_hash: str,
        *,
        succeeded: bool,
        output_ref: str | None = None,
        failure_code: str | None = None,
    ) -> None:
        result = await self.session.execute(
            ACCEPT_RESULT,
            {
                "task_id": task_id,
                "tenant_id": self.tenant_id,
                "worker_id": worker_id,
                "execution_token_hash": execution_token_hash,
                "target_status": "SUCCEEDED" if succeeded else "FAILED",
                "output_ref": output_ref,
                "failure_code": failure_code,
            },
        )
        if result.scalar_one_or_none() is None:
            raise LeaseLost("Result rejected because the lease/token is stale")
