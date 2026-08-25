from __future__ import annotations

from typing import Any

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession


CLAIM_OUTBOX = text("""
SELECT event_id, tenant_id, aggregate_id, event_type, schema_version, payload, occurred_at
FROM outbox_events
WHERE published_at IS NULL
  AND attempts < :max_attempts
ORDER BY occurred_at
FOR UPDATE SKIP LOCKED
LIMIT :batch_size
""")

MARK_PUBLISHED = text("""
UPDATE outbox_events
SET published_at = now(), attempts = attempts + 1, last_error = NULL
WHERE event_id = ANY(CAST(:event_ids AS uuid[]))
""")

MARK_FAILED = text("""
UPDATE outbox_events
SET attempts = attempts + 1, last_error = left(:error, 2000)
WHERE event_id = :event_id AND published_at IS NULL
""")


class PostgresOutbox:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def claim_batch(self, batch_size: int = 100, max_attempts: int = 10) -> list[dict[str, Any]]:
        if not 1 <= batch_size <= 500:
            raise ValueError("batch_size must be 1..500")
        result = await self.session.execute(
            CLAIM_OUTBOX, {"batch_size": batch_size, "max_attempts": max_attempts}
        )
        return [dict(row) for row in result.mappings().all()]

    async def mark_published(self, event_ids: list[str]) -> None:
        if not event_ids:
            return
        await self.session.execute(MARK_PUBLISHED, {"event_ids": event_ids})

    async def mark_failed(self, event_id: str, error: str) -> None:
        await self.session.execute(MARK_FAILED, {"event_id": event_id, "error": error})
