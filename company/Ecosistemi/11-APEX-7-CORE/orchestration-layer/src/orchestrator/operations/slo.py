from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ErrorBudget:
    slo: float
    total_events: int
    bad_events: int

    def __post_init__(self) -> None:
        if not 0 < self.slo <= 1:
            raise ValueError("SLO must be in (0,1]")
        if self.total_events < 0 or not 0 <= self.bad_events <= self.total_events:
            raise ValueError("Invalid event counts")

    @property
    def allowed_bad_events(self) -> float:
        return self.total_events * (1 - self.slo)

    @property
    def consumed_ratio(self) -> float:
        if self.allowed_bad_events == 0:
            return 0.0 if self.bad_events == 0 else float("inf")
        return self.bad_events / self.allowed_bad_events

    @property
    def action(self) -> str:
        ratio = self.consumed_ratio
        if ratio == float("inf") or ratio >= 0.999999:
            return "FREEZE"
        if ratio >= 0.5:
            return "RELIABILITY_SPRINT"
        if ratio >= 0.25:
            return "REDUCE_RISK"
        return "CONTINUE"
