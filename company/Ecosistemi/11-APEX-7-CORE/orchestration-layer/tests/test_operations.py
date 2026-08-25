from __future__ import annotations

import sys
import unittest
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT / "src"))

from orchestrator.observability import ComponentHealth, HealthService, OcpMetrics, StructuredLogger
from orchestrator.operations import ErrorBudget, ProductionReadinessReview


class LoggingTests(unittest.TestCase):
    def test_structured_log_redacts_sensitive_values_and_hashes_tenant(self) -> None:
        record = StructuredLogger().record(
            level="ERROR",
            event="test",
            workflow_id="w1",
            trace_id="trace-1234567890",
            tenant_id="tenant-secret-name",
            detail="email person@example.test Bearer abcdefghijklmnopqrstuvwxyz",
            attributes={"password": "supersecretvalue", "card": "4111 1111 1111 1111"},
        )
        encoded = str(record)
        self.assertNotIn("person@example.test", encoded)
        self.assertNotIn("abcdefghijklmnopqrstuvwxyz", encoded)
        self.assertNotIn("supersecretvalue", encoded)
        self.assertNotIn("4111 1111 1111 1111", encoded)
        self.assertNotEqual("tenant-secret-name", record["tenant_id_hash"])


class MetricsTests(unittest.TestCase):
    def test_metrics_render_without_tenant_identity_label(self) -> None:
        metrics = OcpMetrics()
        metrics.workflow_total.labels("repository_adr", "R1", "COMPLETED").inc()
        metrics.policy_decision_total.labels("DENY", "POL_DEFAULT_DENY").inc()
        rendered = metrics.render().decode()
        self.assertIn("ocp_workflow_total", rendered)
        self.assertIn("ocp_policy_decision_total", rendered)
        self.assertNotIn("tenant_id", rendered)


class HealthTests(unittest.IsolatedAsyncioTestCase):
    async def test_required_down_component_blocks_readiness(self) -> None:
        async def db(): return ComponentHealth("postgres", "UP", required=True)
        async def opa(): return ComponentHealth("opa", "DOWN", required=True)
        async def ruflo(): return ComponentHealth("ruflo", "DOWN", required=False)
        result = await HealthService([db, opa, ruflo]).readiness()
        self.assertEqual("NOT_READY", result["status"])

    async def test_optional_ruflo_down_does_not_block_local_mode(self) -> None:
        async def db(): return ComponentHealth("postgres", "UP", required=True)
        async def opa(): return ComponentHealth("opa", "UP", required=True)
        async def ruflo(): return ComponentHealth("ruflo", "DOWN", required=False)
        result = await HealthService([db, opa, ruflo]).readiness()
        self.assertEqual("READY", result["status"])


class ErrorBudgetTests(unittest.TestCase):
    def test_burn_actions(self) -> None:
        self.assertEqual("CONTINUE", ErrorBudget(0.95, 100, 1).action)
        self.assertEqual("RELIABILITY_SPRINT", ErrorBudget(0.95, 100, 3).action)
        self.assertEqual("FREEZE", ErrorBudget(0.95, 100, 5).action)
        self.assertEqual("FREEZE", ErrorBudget(1.0, 100, 1).action)


class PrrTests(unittest.TestCase):
    def test_current_readiness_is_no_go_with_explicit_blockers(self) -> None:
        result = ProductionReadinessReview(PROJECT).evaluate()
        self.assertEqual("NO_GO", result.verdict)
        blocked = {item["id"] for item in result.blocked}
        self.assertIn("OWNERS_ASSIGNED", blocked)
        self.assertIn("EXTERNAL_PENTEST", blocked)
        self.assertIn("MANAGED_FAILOVER_PITR", blocked)
        self.assertIn("CLOUD_IDP_RESIDENCY", blocked)
        self.assertIn("ARCH_BLUEPRINT", result.passed)
        self.assertTrue(any("RuFlo" in warning for warning in result.warnings))

    def test_local_secure_pilot_is_go_but_not_production(self) -> None:
        result = ProductionReadinessReview(PROJECT).evaluate_local_pilot()
        self.assertEqual("GO_LOCAL_PILOT", result.verdict)
        self.assertEqual(0, len(result.blocked))
        self.assertTrue(any("not production" in warning for warning in result.warnings))

    def test_runbooks_exist(self) -> None:
        runbooks = list((PROJECT / "operations/runbooks").glob("RB-*.md"))
        self.assertGreaterEqual(len(runbooks), 5)


if __name__ == "__main__":
    unittest.main()
