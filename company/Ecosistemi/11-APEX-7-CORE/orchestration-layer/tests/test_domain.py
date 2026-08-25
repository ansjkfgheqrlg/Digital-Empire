from __future__ import annotations

import sys
import unittest
from decimal import Decimal
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT / "src"))

from orchestrator.domain import (
    ActorType,
    BudgetAmount,
    BudgetExceeded,
    BudgetLedger,
    IllegalTransition,
    InvalidPlan,
    Plan,
    RiskClass,
    SideEffectContract,
    SideEffectMode,
    TaskSpec,
    Workflow,
    WorkflowStatus,
)
from orchestrator.domain.errors import InvariantViolation, StaleVersion
from orchestrator.domain.transitions import TransitionContext


def amount(tokens: int, cost: str, duration_ms: int) -> BudgetAmount:
    return BudgetAmount(tokens, Decimal(cost), duration_ms)


def task(
    task_id: str,
    role: str,
    depends_on: tuple[str, ...] = (),
    budget: BudgetAmount | None = None,
) -> TaskSpec:
    return TaskSpec(
        task_id=task_id,
        role=role,
        objective=f"Execute {task_id}",
        depends_on=depends_on,
        completion_criteria=("Result has evidence",),
        capabilities=("artifact.read",),
        budget=budget or amount(1000, "0.10", 10000),
        side_effect=SideEffectContract(SideEffectMode.NONE),
    )


class BudgetTests(unittest.TestCase):
    def test_reservation_commit_and_release(self) -> None:
        ledger = BudgetLedger(amount(10000, "2.00", 100000))
        ledger.reserve("a", amount(3000, "0.50", 20000))
        ledger.commit("a", amount(2500, "0.40", 18000))
        self.assertEqual(2500, ledger.committed.tokens)
        self.assertEqual(7500, ledger.available.tokens)
        ledger.reserve("b", amount(1000, "0.10", 10000))
        ledger.release("b")
        self.assertEqual(7500, ledger.available.tokens)

    def test_budget_cannot_be_over_reserved(self) -> None:
        ledger = BudgetLedger(amount(100, "1.00", 1000))
        with self.assertRaises(BudgetExceeded):
            ledger.reserve("x", amount(101, "0.10", 100))

    def test_actual_cannot_exceed_reservation(self) -> None:
        ledger = BudgetLedger(amount(1000, "1.00", 10000))
        ledger.reserve("x", amount(100, "0.10", 1000))
        with self.assertRaises(BudgetExceeded):
            ledger.commit("x", amount(101, "0.10", 1000))


class SideEffectTests(unittest.TestCase):
    def test_idempotent_requires_key_and_lookup(self) -> None:
        with self.assertRaises(InvariantViolation):
            SideEffectContract(SideEffectMode.IDEMPOTENT)

    def test_compensatable_requires_reconcile_and_compensate(self) -> None:
        with self.assertRaises(InvariantViolation):
            SideEffectContract(
                SideEffectMode.COMPENSATABLE,
                reconciliation_operation="artifact.lookup",
            )

    def test_irreversible_is_not_retryable(self) -> None:
        contract = SideEffectContract(
            SideEffectMode.IRREVERSIBLE,
            irreversible_approval="human-r3",
        )
        self.assertFalse(contract.retryable)


class PlanTests(unittest.TestCase):
    def test_topological_order_and_parallel_groups(self) -> None:
        plan = Plan(
            "p1",
            "w1",
            (
                task("a", "planner"),
                task("b", "implementer", ("a",)),
                task("c", "critic", ("a",)),
                task("d", "gate", ("b", "c")),
            ),
            amount(10000, "2.00", 100000),
        )
        self.assertEqual(("a", "b", "c", "d"), plan.topological_order())
        self.assertEqual((("a",), ("b", "c"), ("d",)), plan.parallel_groups())

    def test_cycle_is_rejected(self) -> None:
        with self.assertRaises(InvalidPlan):
            Plan(
                "p",
                "w",
                (task("a", "planner", ("b",)), task("b", "gate", ("a",))),
                amount(10000, "2.00", 100000),
            )

    def test_unknown_dependency_is_rejected(self) -> None:
        with self.assertRaises(InvalidPlan):
            Plan(
                "p",
                "w",
                (task("a", "gate", ("missing",)),),
                amount(10000, "2.00", 100000),
            )

    def test_plan_requires_gate(self) -> None:
        with self.assertRaises(InvalidPlan):
            Plan(
                "p",
                "w",
                (task("a", "implementer"),),
                amount(10000, "2.00", 100000),
            )

    def test_plan_budget_must_fit(self) -> None:
        with self.assertRaises(InvalidPlan):
            Plan(
                "p",
                "w",
                (task("a", "gate", budget=amount(2000, "1.00", 1000)),),
                amount(1000, "1.00", 1000),
            )


class WorkflowTests(unittest.TestCase):
    def make_workflow(self) -> Workflow:
        return Workflow.create(
            workflow_id="w1",
            tenant_id="tenant-a",
            workflow_type="repository_adr",
            goal="Create ADR",
            risk=RiskClass.R1,
            requested_by="user-a",
            idempotency_key="idem-0001",
            budget_limit=amount(30000, "2.00", 300000),
        )

    def test_legal_transition_emits_ordered_event(self) -> None:
        workflow = self.make_workflow()
        event = workflow.transition(
            WorkflowStatus.VALIDATING,
            ActorType.API,
            TransitionContext(evidence_refs=("request://1",), flags=frozenset({"request_persisted"})),
            expected_version=0,
        )
        self.assertEqual(WorkflowStatus.VALIDATING, workflow.status)
        self.assertEqual(1, workflow.version)
        self.assertEqual(2, event.sequence)
        self.assertEqual("RECEIVED", event.payload["from"])

    def test_wrong_actor_is_rejected(self) -> None:
        workflow = self.make_workflow()
        with self.assertRaises(IllegalTransition):
            workflow.transition(
                WorkflowStatus.VALIDATING,
                ActorType.WORKER,
                TransitionContext(flags=frozenset({"request_persisted"})),
                expected_version=0,
            )

    def test_missing_guard_is_rejected(self) -> None:
        workflow = self.make_workflow()
        with self.assertRaises(IllegalTransition):
            workflow.transition(
                WorkflowStatus.VALIDATING,
                ActorType.API,
                TransitionContext(),
                expected_version=0,
            )

    def test_stale_version_is_rejected(self) -> None:
        workflow = self.make_workflow()
        with self.assertRaises(StaleVersion):
            workflow.transition(
                WorkflowStatus.VALIDATING,
                ActorType.API,
                TransitionContext(flags=frozenset({"request_persisted"})),
                expected_version=4,
            )

    def test_cancel_is_a_transition_not_immediate_terminal(self) -> None:
        workflow = self.make_workflow()
        workflow.transition(
            WorkflowStatus.CANCEL_REQUESTED,
            ActorType.API,
            TransitionContext(flags=frozenset({"cancel_request_persisted"})),
            expected_version=0,
        )
        self.assertEqual(WorkflowStatus.CANCEL_REQUESTED, workflow.status)
        self.assertFalse(workflow.status.terminal)


if __name__ == "__main__":
    unittest.main()
