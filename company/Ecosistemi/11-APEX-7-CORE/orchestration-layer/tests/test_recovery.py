from __future__ import annotations

import sys
import tempfile
import unittest
from datetime import UTC, datetime, timedelta
from decimal import Decimal
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT / "src"))

from orchestrator.chaos import ChaosExperiment
from orchestrator.domain import (
    ActorType,
    BudgetAmount,
    RiskClass,
    SideEffectContract,
    SideEffectMode,
    Workflow,
    WorkflowStatus,
)
from orchestrator.domain.transitions import TransitionContext
from orchestrator.governance.grants import (
    CapabilityGrantService,
    GrantBinding,
    GrantDenied,
    InMemoryCapabilityStore,
)
from orchestrator.recovery.artifact import ArtifactCompensation
from orchestrator.recovery.breaker import CircuitBreaker, CircuitState
from orchestrator.recovery.catalog import (
    CompensationCatalog,
    CompensationResult,
    ReconciliationResult,
    ReconciliationStatus,
)
from orchestrator.recovery.coordinator import RecoveryCoordinator, RecoveryOutcome
from orchestrator.recovery.retry import Failure, RetryDecision, RetryPolicy


def make_workflow() -> Workflow:
    workflow = Workflow.create(
        "workflow-a",
        "tenant-a",
        "repository_adr",
        "Create ADR",
        RiskClass.R1,
        "user-a",
        "idem-a",
        BudgetAmount(10000, Decimal("2"), 100000),
    )
    transitions = [
        (WorkflowStatus.VALIDATING, ActorType.API, {"request_persisted"}),
        (WorkflowStatus.PLANNING, ActorType.WORKER, {"validation_passed"}),
        (
            WorkflowStatus.PLAN_REVIEW,
            ActorType.WORKER,
            {"plan_schema_valid", "dag_valid", "budget_valid"},
        ),
        (WorkflowStatus.AUTHORIZED, ActorType.POLICY, {"policy_allowed"}),
        (
            WorkflowStatus.RUNNING,
            ActorType.WORKER,
            {"lease_valid", "budget_available", "grant_valid"},
        ),
    ]
    for target, actor, flags in transitions:
        workflow.transition(
            target,
            actor,
            TransitionContext(flags=frozenset(flags)),
            workflow.version,
        )
    return workflow


class FakeOperation:
    def __init__(self, status: ReconciliationStatus, compensation_success: bool = True):
        self.status = status
        self.compensation_success = compensation_success

    async def reconcile(self, context):
        return ReconciliationResult(self.status, {"probe": self.status.value})

    async def compensate(self, context):
        return CompensationResult(self.compensation_success, {"compensated": self.compensation_success}, None if self.compensation_success else "failed")


class RetryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.policy = RetryPolicy()
        self.now = datetime(2026, 8, 23, tzinfo=UTC)
        self.deadline = self.now + timedelta(minutes=1)
        self.none = SideEffectContract(SideEffectMode.NONE)

    def test_unknown_outcome_always_reconciles(self) -> None:
        plan = self.policy.decide(
            Failure("RUN_TIMEOUT", outcome_known=False),
            attempt=1,
            max_attempts=3,
            now=self.now,
            deadline=self.deadline,
            budget_available=True,
            side_effect=self.none,
        )
        self.assertEqual(RetryDecision.RECONCILE, plan.decision)

    def test_transient_bounded_retry(self) -> None:
        plan = self.policy.decide(
            Failure("TOOL_5XX", outcome_known=True),
            attempt=1,
            max_attempts=3,
            now=self.now,
            deadline=self.deadline,
            budget_available=True,
            side_effect=self.none,
            jitter_seed=7,
        )
        self.assertEqual(RetryDecision.RETRY, plan.decision)
        self.assertGreaterEqual(plan.delay_seconds, 0)

    def test_irreversible_does_not_retry(self) -> None:
        irreversible = SideEffectContract(
            SideEffectMode.IRREVERSIBLE, irreversible_approval="human-r3"
        )
        plan = self.policy.decide(
            Failure("TOOL_5XX", outcome_known=True),
            attempt=1,
            max_attempts=3,
            now=self.now,
            deadline=self.deadline,
            budget_available=True,
            side_effect=irreversible,
        )
        self.assertEqual(RetryDecision.RECONCILE, plan.decision)

    def test_budget_exhaustion_pauses(self) -> None:
        plan = self.policy.decide(
            Failure("RUN_TIMEOUT", outcome_known=True),
            attempt=1,
            max_attempts=3,
            now=self.now,
            deadline=self.deadline,
            budget_available=False,
            side_effect=self.none,
        )
        self.assertEqual(RetryDecision.PAUSE, plan.decision)


class BreakerTests(unittest.TestCase):
    def test_open_half_open_and_close(self) -> None:
        now = datetime(2026, 8, 23, tzinfo=UTC)
        breaker = CircuitBreaker(failure_threshold=2, window_seconds=60, open_seconds=30)
        breaker.record_failure(now)
        breaker.record_failure(now + timedelta(seconds=1))
        self.assertEqual(CircuitState.OPEN, breaker.state)
        self.assertFalse(breaker.allow(now + timedelta(seconds=10)))
        self.assertTrue(breaker.allow(now + timedelta(seconds=31)))
        self.assertEqual(CircuitState.HALF_OPEN, breaker.state)
        self.assertFalse(breaker.allow(now + timedelta(seconds=32)))
        breaker.record_success()
        self.assertEqual(CircuitState.CLOSED, breaker.state)


class RecoveryCoordinatorTests(unittest.IsolatedAsyncioTestCase):
    async def coordinator(self, operation) -> tuple[RecoveryCoordinator, CapabilityGrantService]:
        catalog = CompensationCatalog()
        catalog.register("artifact", operation)
        grants = CapabilityGrantService(InMemoryCapabilityStore())
        return RecoveryCoordinator(catalog, grants), grants

    async def test_present_effect_is_compensated(self) -> None:
        coordinator, _ = await self.coordinator(FakeOperation(ReconciliationStatus.PRESENT))
        workflow = make_workflow()
        result = await coordinator.reconcile_and_recover(workflow, "artifact", {})
        self.assertEqual(RecoveryOutcome.COMPENSATED, result.outcome)
        self.assertEqual(WorkflowStatus.COMPENSATED, workflow.status)

    async def test_unknown_effect_requires_manual_intervention(self) -> None:
        coordinator, _ = await self.coordinator(FakeOperation(ReconciliationStatus.UNKNOWN))
        workflow = make_workflow()
        result = await coordinator.reconcile_and_recover(workflow, "artifact", {})
        self.assertEqual(RecoveryOutcome.MANUAL_INTERVENTION, result.outcome)
        self.assertEqual(WorkflowStatus.MANUAL_INTERVENTION, workflow.status)

    async def test_absent_effect_can_retry(self) -> None:
        coordinator, _ = await self.coordinator(FakeOperation(ReconciliationStatus.ABSENT))
        workflow = make_workflow()
        result = await coordinator.reconcile_and_recover(workflow, "artifact", {})
        self.assertEqual(RecoveryOutcome.RETRYABLE, result.outcome)
        self.assertEqual(WorkflowStatus.RUNNING, workflow.status)

    async def test_cancel_revokes_task_grant(self) -> None:
        coordinator, grants = await self.coordinator(FakeOperation(ReconciliationStatus.ABSENT))
        workflow = make_workflow()
        binding = GrantBinding("tenant-a", "workflow-a", "task-a", "sha256:exec")
        token, _ = await grants.issue(
            subject="agent",
            binding=binding,
            capability_scope="repo.read",
            constraints={},
            ttl_seconds=60,
        )
        result = await coordinator.request_cancel(
            workflow, running_task_id="task-a", residual_effect=False
        )
        self.assertEqual(WorkflowStatus.CANCELLING, workflow.status)
        self.assertEqual(RecoveryOutcome.RETRYABLE, result.outcome)
        with self.assertRaises(GrantDenied):
            await grants.consume(token, binding, "repo.read")

    async def test_cancel_unknown_then_absent_finishes_cancelled(self) -> None:
        coordinator, _ = await self.coordinator(FakeOperation(ReconciliationStatus.ABSENT))
        workflow = make_workflow()
        await coordinator.request_cancel(workflow, running_task_id="task-a", residual_effect=False)
        result = await coordinator.reconcile_and_recover(
            workflow, "artifact", {}, from_cancellation=True
        )
        self.assertEqual(RecoveryOutcome.CANCELLED, result.outcome)
        self.assertEqual(WorkflowStatus.CANCELLED, workflow.status)


class ArtifactRecoveryTests(unittest.IsolatedAsyncioTestCase):
    async def test_hash_match_deletes_unreferenced_artifact(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / "adr/a.md"
            path.parent.mkdir()
            path.write_text("artifact", encoding="utf-8")
            import hashlib
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            operation = ArtifactCompensation(root)
            result = await operation.compensate(
                {"path": "adr/a.md", "expected_sha256": digest, "referenced": False}
            )
            self.assertTrue(result.success)
            self.assertFalse(path.exists())

    async def test_hash_mismatch_never_deletes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / "adr/a.md"
            path.parent.mkdir()
            path.write_text("artifact", encoding="utf-8")
            result = await ArtifactCompensation(root).compensate(
                {"path": "adr/a.md", "expected_sha256": "0" * 64, "referenced": False}
            )
            self.assertFalse(result.success)
            self.assertTrue(path.exists())


class ChaosHarnessTests(unittest.IsolatedAsyncioTestCase):
    async def test_failed_steady_state_aborts_and_cleans_up(self) -> None:
        state = {"healthy": True, "clean": False, "aborted": False}

        async def probe(): return state["healthy"]
        async def inject(): state["healthy"] = False
        async def cleanup(): state["healthy"] = True; state["clean"] = True
        async def cleanup_probe(): return state["clean"] and state["healthy"]
        async def abort(): state["aborted"] = True

        result = await ChaosExperiment(
            "CH-TEST", probe, inject, probe, cleanup, cleanup_probe, abort
        ).run()
        self.assertTrue(result.aborted)
        self.assertTrue(result.cleanup_pass)
        self.assertTrue(state["aborted"])


if __name__ == "__main__":
    unittest.main()
