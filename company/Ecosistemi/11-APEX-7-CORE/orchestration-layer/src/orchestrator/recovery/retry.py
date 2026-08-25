from __future__ import annotations

import hashlib
import secrets
from dataclasses import dataclass
from datetime import datetime, timedelta
from enum import StrEnum

from orchestrator.domain.side_effect import SideEffectContract


class RetryDecision(StrEnum):
    RETRY = "RETRY"
    RECONCILE = "RECONCILE"
    FAIL = "FAIL"
    PAUSE = "PAUSE"


@dataclass(frozen=True)
class Failure:
    code: str
    outcome_known: bool
    retry_after_seconds: float | None = None


@dataclass(frozen=True)
class RetryPlan:
    decision: RetryDecision
    delay_seconds: float
    reason: str


class RetryPolicy:
    TRANSIENT = {"RUN_TIMEOUT", "RUN_UNAVAILABLE", "RUN_RATE_LIMIT", "TOOL_5XX", "STATE_CONFLICT"}
    NON_RETRYABLE = {"RUN_PROVIDER_AUTH", "TOOL_4XX", "SECURITY", "POLICY_DENY", "BUDGET_EXCEEDED"}

    def decide(
        self,
        failure: Failure,
        *,
        attempt: int,
        max_attempts: int,
        now: datetime,
        deadline: datetime,
        budget_available: bool,
        side_effect: SideEffectContract,
        base_delay_seconds: float = 0.1,
        cap_seconds: float = 30.0,
        jitter_seed: int | None = None,
    ) -> RetryPlan:
        if not failure.outcome_known:
            return RetryPlan(RetryDecision.RECONCILE, 0, "external outcome is unknown")
        if failure.code in self.NON_RETRYABLE:
            return RetryPlan(RetryDecision.FAIL, 0, "failure class is non-retryable")
        if failure.code not in self.TRANSIENT:
            return RetryPlan(RetryDecision.FAIL, 0, "failure class is not allowlisted")
        if not side_effect.retryable:
            return RetryPlan(RetryDecision.RECONCILE, 0, "side effect is not safely retryable")
        if not budget_available:
            return RetryPlan(RetryDecision.PAUSE, 0, "budget is unavailable")
        if attempt >= max_attempts:
            return RetryPlan(RetryDecision.FAIL, 0, "maximum attempts reached")
        raw = failure.retry_after_seconds
        if raw is None:
            raw = min(cap_seconds, base_delay_seconds * (2 ** max(attempt - 1, 0)))
            if jitter_seed is None:
                fraction = secrets.randbelow(1_000_001) / 1_000_000
            else:
                digest = hashlib.sha256(f"{jitter_seed}:{attempt}".encode()).digest()
                fraction = int.from_bytes(digest[:8], "big") / ((1 << 64) - 1)
            raw *= fraction
        if now + timedelta(seconds=raw) >= deadline:
            return RetryPlan(RetryDecision.FAIL, 0, "deadline would be exceeded")
        return RetryPlan(RetryDecision.RETRY, raw, "transient and bounded")
