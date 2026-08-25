from __future__ import annotations

from prometheus_client import CollectorRegistry, Counter, Gauge, Histogram, generate_latest


class OcpMetrics:
    def __init__(self):
        self.registry = CollectorRegistry()
        self.workflow_total = Counter(
            "ocp_workflow_total", "Terminal workflows", ["type", "risk", "status"], registry=self.registry
        )
        self.workflow_duration = Histogram(
            "ocp_workflow_duration_seconds", "Workflow duration", ["type", "status"], registry=self.registry
        )
        self.task_attempt_total = Counter(
            "ocp_task_attempt_total", "Task attempts", ["runtime", "result"], registry=self.registry
        )
        self.policy_decision_total = Counter(
            "ocp_policy_decision_total", "Policy decisions", ["effect", "reason"], registry=self.registry
        )
        self.reconciliation_total = Counter(
            "ocp_reconciliation_total", "Reconciliation outcomes", ["result"], registry=self.registry
        )
        self.compensation_total = Counter(
            "ocp_compensation_total", "Compensation outcomes", ["result"], registry=self.registry
        )
        self.runtime_breaker = Gauge(
            "ocp_runtime_breaker_state", "0 closed, 1 open, 2 half-open", ["runtime"], registry=self.registry
        )
        self.budget_committed = Counter(
            "ocp_budget_committed_usd_total", "Committed model cost", ["tenant_class"], registry=self.registry
        )
        self.audit_gap_total = Counter(
            "ocp_audit_sequence_gap_total", "Detected audit sequence gaps", registry=self.registry
        )

    def render(self) -> bytes:
        return generate_latest(self.registry)
