from __future__ import annotations

import json
from datetime import datetime
from typing import Any

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from orchestrator.governance.grants import GrantBinding, GrantRecord


INSERT_GRANT = text("""
INSERT INTO capability_grants (
  grant_id, tenant_id, workflow_id, task_id, subject, capabilities, constraints,
  token_hash, nonce_hash, expires_at
) VALUES (
  CAST(:grant_id AS uuid), :tenant_id, CAST(:workflow_id AS uuid), CAST(:task_id AS uuid),
  :subject, CAST(:capabilities AS jsonb), CAST(:constraints AS jsonb),
  :token_hash, :nonce_hash, :expires_at
)
""")

CONSUME_GRANT = text("""
UPDATE capability_grants
SET consumed_at = :now
WHERE token_hash = :token_hash
  AND tenant_id = :tenant_id
  AND workflow_id = CAST(:workflow_id AS uuid)
  AND task_id = CAST(:task_id AS uuid)
  AND constraints->>'audience' = :audience
  AND constraints->>'execution_token_hash' = :execution_token_hash
  AND CAST(constraints->>'not_before' AS timestamptz) <= :now
  AND consumed_at IS NULL
  AND revoked_at IS NULL
  AND expires_at > :now
RETURNING grant_id, token_hash, nonce_hash, subject, capabilities, constraints,
          expires_at, consumed_at, revoked_at
""")

REVOKE_TASK = text("""
UPDATE capability_grants
SET revoked_at = :now
WHERE tenant_id = :tenant_id
  AND task_id = CAST(:task_id AS uuid)
  AND consumed_at IS NULL
  AND revoked_at IS NULL
RETURNING grant_id
""")


class PostgresCapabilityStore:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def insert(self, record: GrantRecord) -> None:
        constraints = {
            **record.constraints,
            "audience": record.binding.audience,
            "execution_token_hash": record.binding.execution_token_hash,
            "not_before": record.not_before.isoformat(),
        }
        await self.session.execute(
            INSERT_GRANT,
            {
                "grant_id": record.grant_id,
                "tenant_id": record.binding.tenant_id,
                "workflow_id": record.binding.workflow_id,
                "task_id": record.binding.task_id,
                "subject": record.subject,
                "capabilities": json.dumps([record.capability_scope]),
                "constraints": json.dumps(constraints),
                "token_hash": record.token_hash,
                "nonce_hash": record.nonce_hash,
                "expires_at": record.expires_at,
            },
        )

    async def consume(
        self, token_hash: str, binding: GrantBinding, now: datetime
    ) -> GrantRecord | None:
        result = await self.session.execute(
            CONSUME_GRANT,
            {
                "token_hash": token_hash,
                "tenant_id": binding.tenant_id,
                "workflow_id": binding.workflow_id,
                "task_id": binding.task_id,
                "audience": binding.audience,
                "execution_token_hash": binding.execution_token_hash,
                "now": now,
            },
        )
        row = result.mappings().one_or_none()
        if row is None:
            return None
        constraints = dict(row["constraints"])
        not_before = datetime.fromisoformat(constraints.pop("not_before"))
        capability_scope = list(row["capabilities"])[0]
        return GrantRecord(
            grant_id=str(row["grant_id"]),
            token_hash=row["token_hash"],
            nonce_hash=row["nonce_hash"],
            subject=row["subject"],
            binding=binding,
            capability_scope=capability_scope,
            constraints=constraints,
            not_before=not_before,
            expires_at=row["expires_at"],
            consumed_at=row["consumed_at"],
            revoked_at=row["revoked_at"],
        )

    async def revoke_for_task(self, tenant_id: str, task_id: str, now: datetime) -> int:
        result = await self.session.execute(
            REVOKE_TASK, {"tenant_id": tenant_id, "task_id": task_id, "now": now}
        )
        return len(result.mappings().all())
