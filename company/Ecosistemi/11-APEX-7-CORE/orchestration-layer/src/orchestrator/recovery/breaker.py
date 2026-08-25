from __future__ import annotations

from collections import deque
from datetime import datetime, timedelta
from enum import StrEnum


class CircuitState(StrEnum):
    CLOSED = "CLOSED"
    OPEN = "OPEN"
    HALF_OPEN = "HALF_OPEN"


class CircuitBreaker:
    def __init__(
        self,
        failure_threshold: int = 5,
        window_seconds: int = 60,
        open_seconds: int = 30,
    ):
        if failure_threshold < 1:
            raise ValueError("failure_threshold must be positive")
        self.failure_threshold = failure_threshold
        self.window = timedelta(seconds=window_seconds)
        self.open_duration = timedelta(seconds=open_seconds)
        self.state = CircuitState.CLOSED
        self._failures: deque[datetime] = deque()
        self._opened_at: datetime | None = None
        self._probe_in_flight = False

    def allow(self, now: datetime) -> bool:
        if self.state is CircuitState.OPEN:
            if self._opened_at and now - self._opened_at >= self.open_duration:
                self.state = CircuitState.HALF_OPEN
                self._probe_in_flight = False
            else:
                return False
        if self.state is CircuitState.HALF_OPEN:
            if self._probe_in_flight:
                return False
            self._probe_in_flight = True
        return True

    def record_success(self) -> None:
        self.state = CircuitState.CLOSED
        self._failures.clear()
        self._opened_at = None
        self._probe_in_flight = False

    def record_failure(self, now: datetime) -> None:
        if self.state is CircuitState.HALF_OPEN:
            self._open(now)
            return
        cutoff = now - self.window
        while self._failures and self._failures[0] < cutoff:
            self._failures.popleft()
        self._failures.append(now)
        if len(self._failures) >= self.failure_threshold:
            self._open(now)

    def _open(self, now: datetime) -> None:
        self.state = CircuitState.OPEN
        self._opened_at = now
        self._probe_in_flight = False
