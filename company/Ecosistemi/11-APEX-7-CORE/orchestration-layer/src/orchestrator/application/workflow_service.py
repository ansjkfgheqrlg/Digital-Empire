from __future__ import annotations

import json
from decimal import Decimal
from typing import Any, Callable
from uuid import uuid4

from sqlalchemy import text

from orchestrator.adapters.postgres.uow import PostgresUnitOfWork
from orchestrator.domain import ActorType, BudgetAmount, RiskClass, Workflow, WorkflowStatus
from orchestrator.domain.transitions import TransitionContext
from orchestrator.identity.operator import AuthContext


INSERT_DRIVER_TASK = text("""
INSERT INTO tasks (
  task_id, tenant_id, workflow_id, ordinal, role, objective, status,
  completion_criteria, capabilities, side_effect, budget_limit,
  max_attempts, input_ref
) VALUES (
  CAST(:task_id AS uuid), :tenant_id, CAST(:workflow_id AS uuid), 0,
  'planner', 'Execute repository ADR workflow', 'READY',
  CAST(:completion AS jsonb), CAST(:capabilities AS jsonb),
  CAST(:side_effect AS jsonb), CAST(:budget AS jsonb), 2, :input_ref
)
""")


class WorkflowService:
    def __init__(self, uow_factory: Callable[[str], PostgresUnitOfWork], tenant_id: str):
        self.uow_factory = uow_factory
        self.tenant_id = tenant_id

    async def create(
        self,
        payload: dict[str, Any],
        auth: AuthContext,
        idempotency_key: str,
        trace_id: str,
    ) -> dict[str, Any]:
        if "TOKEN_ISSUER" not in auth.roles and "LOCAL_OWNER" not in auth.roles:
            raise PermissionError("Operator cannot create workflows")
        workflow_id = str(uuid4())
        risk = RiskClass(payload.get("risk_hint", "R1"))
        if risk not in {RiskClass.R0, RiskClass.R1}:
            raise PermissionError("Local pilot permits only R0/R1")
        skill_input = payload["skill_input"]
        workflow = Workflow.create(
            workflow_id=workflow_id,
            tenant_id=self.tenant_id,
            workflow_type=payload["workflow_type"],
            goal=payload["goal"],
            risk=risk,
            requested_by=auth.operator_id,
            idempotency_key=idempotency_key,
            budget_limit=BudgetAmount(
                int(payload["constraints"]["max_tokens"]),
                Decimal(str(payload["constraints"]["max_cost_usd"])),
                int(payload["constraints"]["deadline_seconds"]) * 1000,
            ),
            constraints={"skill_input": skill_input},
        )
        task_id = str(uuid4())
        async with self.uow_factory(self.tenant_id) as uow:
            canonical_id = await uow.workflows.add(workflow, trace_id)
            if canonical_id != workflow_id:
                existing = await uow.workflows.get(canonical_id)
                await uow.commit()
                return {"workflow_id": canonical_id, "task_id": None, "status": existing["status"], "idempotent_replay": True}
            await uow.session.execute(
                INSERT_DRIVER_TASK,
                {
                    "task_id": task_id,
                    "tenant_id": self.tenant_id,
                    "workflow_id": workflow_id,
                    "completion": json.dumps(["Workflow reaches a terminal audited state"]),
                    "capabilities": json.dumps(["repo.read", "artifact.write:adr/**"]),
                    "side_effect": json.dumps({"mode": "NONE"}),
                    "budget": json.dumps(payload["constraints"]),
                    "input_ref": "workflow.constraints.skill_input",
                },
            )
            await uow.commit()
        return {"workflow_id": workflow_id, "task_id": task_id, "status": "RECEIVED"}

    async def get(self, workflow_id: str) -> dict[str, Any] | None:
        async with self.uow_factory(self.tenant_id) as uow:
            row = await uow.workflows.get(workflow_id)
            await uow.commit()
            return row

    async def cancel(
        self,
        workflow_id: str,
        auth: AuthContext,
        trace_id: str,
    ) -> dict[str, Any]:
        async with self.uow_factory(self.tenant_id) as uow:
            workflow = await uow.workflows.load_aggregate(workflow_id)
            if workflow is None:
                raise KeyError(workflow_id)
            previous = workflow.version
            event = workflow.transition(
                WorkflowStatus.CANCEL_REQUESTED,
                ActorType.HUMAN,
                TransitionContext(
                    evidence_refs=(f"operator://{auth.operator_id}",),
                    flags=frozenset({"cancel_request_persisted"}),
                ),
                expected_version=previous,
            )
            await uow.workflows.persist_transition(workflow, previous, event, trace_id)
            await uow.session.execute(
                text("""
                    UPDATE tasks
                    SET status='CANCELLED', updated_at=now(), version=version+1
                    WHERE tenant_id=:tenant_id
                      AND workflow_id=CAST(:workflow_id AS uuid)
                      AND status IN ('PENDING','BLOCKED','READY','RETRY_WAIT')
                """),
                {"tenant_id": self.tenant_id, "workflow_id": workflow_id},
            )
            await uow.commit()
            return {"workflow_id": workflow_id, "status": workflow.status.value}

    async def events(self, workflow_id: str) -> list[dict[str, Any]]:
        async with self.uow_factory(self.tenant_id) as uow:
            result = await uow.session.execute(
                text("""
                    SELECT sequence, event_type, actor_type, actor_id, payload,
                           payload_hash, trace_id, occurred_at
                    FROM audit_events
                    WHERE tenant_id=:tenant_id AND workflow_id=CAST(:workflow_id AS uuid)
                    ORDER BY sequence
                """),
                {"tenant_id": self.tenant_id, "workflow_id": workflow_id},
            )
            rows = [dict(row) for row in result.mappings().all()]
            await uow.commit()
            return rows
