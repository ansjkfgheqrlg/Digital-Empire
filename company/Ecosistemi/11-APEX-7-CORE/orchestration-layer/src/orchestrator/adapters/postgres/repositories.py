from __future__ import annotations

import hashlib
import json
from decimal import Decimal
from typing import Any
from uuid import uuid4

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from orchestrator.domain.budget import BudgetAmount, BudgetLedger
from orchestrator.domain.errors import StaleVersion
from orchestrator.domain.events import DomainEvent
from orchestrator.domain.states import RiskClass, WorkflowStatus
from orchestrator.domain.workflow import Workflow


INSERT_WORKFLOW = text("""
INSERT INTO workflows (
  workflow_id, tenant_id, workflow_type, risk, status, goal, constraints,
  budget_limit, budget_used, idempotency_key, requested_by, version, sequence
) VALUES (
  :workflow_id, :tenant_id, :workflow_type, :risk, :status, :goal, CAST(:constraints AS jsonb),
  CAST(:budget_limit AS jsonb), CAST(:budget_used AS jsonb), :idempotency_key,
  :requested_by, :version, :sequence
)
ON CONFLICT (tenant_id, idempotency_key) DO NOTHING
RETURNING workflow_id
""")

SELECT_WORKFLOW = text("""
SELECT workflow_id, tenant_id, workflow_type, risk, status, goal, constraints,
       budget_limit, budget_used, idempotency_key, requested_by, version, sequence,
       created_at, updated_at
FROM workflows
WHERE workflow_id = :workflow_id AND tenant_id = :tenant_id
""")

UPDATE_WORKFLOW = text("""
UPDATE workflows
SET status = :status,
    version = :new_version,
    sequence = :sequence,
    budget_used = CAST(:budget_used AS jsonb),
    updated_at = now()
WHERE workflow_id = :workflow_id
  AND tenant_id = :tenant_id
  AND version = :previous_version
RETURNING version
""")

INSERT_AUDIT = text("""
INSERT INTO audit_events (
  event_id, tenant_id, workflow_id, sequence, actor_type, actor_id,
  event_type, payload, payload_hash, trace_id, occurred_at
) VALUES (
  :event_id, :tenant_id, :workflow_id, :sequence, :actor_type, :actor_id,
  :event_type, CAST(:payload AS jsonb), :payload_hash, :trace_id, CAST(:occurred_at AS timestamptz)
)
""")

INSERT_OUTBOX = text("""
INSERT INTO outbox_events (
  event_id, tenant_id, aggregate_id, event_type, schema_version, payload, occurred_at
) VALUES (
  :event_id, :tenant_id, :aggregate_id, :event_type, '1.0',
  CAST(:payload AS jsonb), CAST(:occurred_at AS timestamptz)
)
""")


class PostgresWorkflowRepository:
    def __init__(self, session: AsyncSession, tenant_id: str):
        self.session = session
        self.tenant_id = tenant_id

    async def add(self, workflow: Workflow, trace_id: str) -> str:
        if workflow.tenant_id != self.tenant_id:
            raise ValueError("Workflow tenant does not match Unit of Work tenant")
        values = self._workflow_values(workflow)
        result = await self.session.execute(INSERT_WORKFLOW, values)
        inserted = result.scalar_one_or_none()
        if inserted is None:
            existing = await self.session.execute(
                text("""
                    SELECT workflow_id FROM workflows
                    WHERE tenant_id=:tenant_id AND idempotency_key=:idempotency_key
                """),
                {"tenant_id": self.tenant_id, "idempotency_key": workflow.idempotency_key},
            )
            existing_id = existing.scalar_one()
            return str(existing_id)
        await self._append_event(workflow.events[0], trace_id, actor_type="API", actor_id=workflow.requested_by)
        return workflow.workflow_id

    async def get(self, workflow_id: str) -> dict[str, Any] | None:
        result = await self.session.execute(
            SELECT_WORKFLOW, {"workflow_id": workflow_id, "tenant_id": self.tenant_id}
        )
        row = result.mappings().one_or_none()
        return dict(row) if row else None

    async def load_aggregate(self, workflow_id: str) -> Workflow | None:
        row = await self.get(workflow_id)
        if row is None:
            return None
        limit = row["budget_limit"]
        used = row["budget_used"]
        return Workflow(
            workflow_id=str(row["workflow_id"]),
            tenant_id=row["tenant_id"],
            workflow_type=row["workflow_type"],
            goal=row["goal"],
            risk=RiskClass(row["risk"]),
            requested_by=row["requested_by"],
            idempotency_key=row["idempotency_key"],
            budget=BudgetLedger.from_state(
                BudgetAmount(int(limit["tokens"]), Decimal(str(limit["cost_usd"])), int(limit["duration_ms"])),
                BudgetAmount(int(used["tokens"]), Decimal(str(used["cost_usd"])), int(used["duration_ms"])),
            ),
            status=WorkflowStatus(row["status"]),
            version=int(row["version"]),
            sequence=int(row["sequence"]),
            constraints=dict(row["constraints"]),
        )

    async def persist_event_stream(
        self,
        workflow: Workflow,
        previous_version: int,
        events: list[DomainEvent],
        trace_id: str,
    ) -> None:
        expected = previous_version
        for event in events:
            target = event.payload.get("to")
            if not isinstance(target, str) or event.aggregate_version != expected + 1:
                raise ValueError("Invalid transition event stream")
            result = await self.session.execute(
                UPDATE_WORKFLOW,
                {
                    "workflow_id": workflow.workflow_id,
                    "tenant_id": self.tenant_id,
                    "status": target,
                    "new_version": event.aggregate_version,
                    "previous_version": expected,
                    "sequence": event.sequence,
                    "budget_used": json.dumps(self._budget_json(workflow)),
                },
            )
            if result.scalar_one_or_none() is None:
                raise StaleVersion(f"Database rejected event stream at version {expected}")
            await self._append_event(
                event,
                trace_id,
                actor_type=str(event.payload.get("actor", "SYSTEM")),
                actor_id=str(event.payload.get("actor", "SYSTEM")),
            )
            expected = event.aggregate_version

    async def persist_transition(
        self,
        workflow: Workflow,
        previous_version: int,
        event: DomainEvent,
        trace_id: str,
    ) -> None:
        if workflow.version != previous_version + 1:
            raise ValueError("Workflow domain version is not the next version")
        result = await self.session.execute(
            UPDATE_WORKFLOW,
            {
                "workflow_id": workflow.workflow_id,
                "tenant_id": self.tenant_id,
                "status": workflow.status.value,
                "new_version": workflow.version,
                "previous_version": previous_version,
                "sequence": workflow.sequence,
                "budget_used": json.dumps(self._budget_json(workflow)),
            },
        )
        if result.scalar_one_or_none() is None:
            raise StaleVersion(
                f"Database rejected stale workflow version {previous_version}"
            )
        await self._append_event(
            event,
            trace_id,
            actor_type=event.payload.get("actor", "SYSTEM"),
            actor_id=event.payload.get("actor", "SYSTEM"),
        )

    async def _append_event(
        self,
        event: DomainEvent,
        trace_id: str,
        actor_type: str,
        actor_id: str,
    ) -> None:
        payload = json.dumps(event.payload, sort_keys=True, separators=(",", ":"))
        payload_hash = "sha256:" + hashlib.sha256(payload.encode()).hexdigest()
        await self.session.execute(
            INSERT_AUDIT,
            {
                "event_id": event.event_id,
                "tenant_id": self.tenant_id,
                "workflow_id": event.workflow_id,
                "sequence": event.sequence,
                "actor_type": actor_type,
                "actor_id": actor_id,
                "event_type": event.event_type,
                "payload": payload,
                "payload_hash": payload_hash,
                "trace_id": trace_id,
                "occurred_at": event.occurred_at,
            },
        )
        await self.session.execute(
            INSERT_OUTBOX,
            {
                "event_id": str(uuid4()),
                "tenant_id": self.tenant_id,
                "aggregate_id": event.workflow_id,
                "event_type": event.event_type,
                "payload": payload,
                "occurred_at": event.occurred_at,
            },
        )

    def _workflow_values(self, workflow: Workflow) -> dict[str, Any]:
        return {
            "workflow_id": workflow.workflow_id,
            "tenant_id": workflow.tenant_id,
            "workflow_type": workflow.workflow_type,
            "risk": workflow.risk.value,
            "status": workflow.status.value,
            "goal": workflow.goal,
            "constraints": json.dumps(workflow.constraints),
            "budget_limit": json.dumps(
                {
                    "tokens": workflow.budget.limit.tokens,
                    "cost_usd": str(workflow.budget.limit.cost_usd),
                    "duration_ms": workflow.budget.limit.duration_ms,
                }
            ),
            "budget_used": json.dumps(self._budget_json(workflow)),
            "idempotency_key": workflow.idempotency_key,
            "requested_by": workflow.requested_by,
            "version": workflow.version,
            "sequence": workflow.sequence,
        }

    @staticmethod
    def _budget_json(workflow: Workflow) -> dict[str, Any]:
        return {
            "tokens": workflow.budget.committed.tokens,
            "cost_usd": str(workflow.budget.committed.cost_usd),
            "duration_ms": workflow.budget.committed.duration_ms,
        }
