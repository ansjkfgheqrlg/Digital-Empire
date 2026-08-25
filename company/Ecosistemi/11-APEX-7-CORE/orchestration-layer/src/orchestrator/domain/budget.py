from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal

from .errors import BudgetExceeded, InvariantViolation


@dataclass(frozen=True)
class BudgetAmount:
    tokens: int
    cost_usd: Decimal
    duration_ms: int

    def __post_init__(self) -> None:
        if self.tokens < 0 or self.cost_usd < 0 or self.duration_ms < 0:
            raise InvariantViolation("Budget values cannot be negative")

    @classmethod
    def zero(cls) -> "BudgetAmount":
        return cls(tokens=0, cost_usd=Decimal("0"), duration_ms=0)

    def __add__(self, other: "BudgetAmount") -> "BudgetAmount":
        return BudgetAmount(
            self.tokens + other.tokens,
            self.cost_usd + other.cost_usd,
            self.duration_ms + other.duration_ms,
        )

    def __sub__(self, other: "BudgetAmount") -> "BudgetAmount":
        return BudgetAmount(
            self.tokens - other.tokens,
            self.cost_usd - other.cost_usd,
            self.duration_ms - other.duration_ms,
        )

    def fits_within(self, limit: "BudgetAmount") -> bool:
        return (
            self.tokens <= limit.tokens
            and self.cost_usd <= limit.cost_usd
            and self.duration_ms <= limit.duration_ms
        )


class BudgetLedger:
    """Reservation/commit ledger with monotonic committed usage."""

    def __init__(self, limit: BudgetAmount):
        self.limit = limit
        self.committed = BudgetAmount.zero()
        self._reservations: dict[str, BudgetAmount] = {}

    @classmethod
    def from_state(cls, limit: BudgetAmount, committed: BudgetAmount) -> "BudgetLedger":
        if not committed.fits_within(limit):
            raise InvariantViolation("Committed budget exceeds limit")
        ledger = cls(limit)
        ledger.committed = committed
        return ledger

    @property
    def reserved(self) -> BudgetAmount:
        total = BudgetAmount.zero()
        for amount in self._reservations.values():
            total = total + amount
        return total

    @property
    def available(self) -> BudgetAmount:
        return self.limit - (self.committed + self.reserved)

    def reserve(self, reservation_id: str, amount: BudgetAmount) -> None:
        if reservation_id in self._reservations:
            if self._reservations[reservation_id] == amount:
                return
            raise InvariantViolation("Reservation id already exists with a different amount")
        projected = self.committed + self.reserved + amount
        if not projected.fits_within(self.limit):
            raise BudgetExceeded("Reservation exceeds workflow budget")
        self._reservations[reservation_id] = amount

    def commit(self, reservation_id: str, actual: BudgetAmount) -> None:
        reserved = self._reservations.get(reservation_id)
        if reserved is None:
            raise InvariantViolation("Unknown reservation")
        if not actual.fits_within(reserved):
            raise BudgetExceeded("Actual usage exceeds reserved amount")
        previous = self.committed
        self.committed = self.committed + actual
        if not previous.fits_within(self.committed):
            raise InvariantViolation("Committed usage must be monotonic")
        del self._reservations[reservation_id]

    def release(self, reservation_id: str) -> None:
        if reservation_id not in self._reservations:
            raise InvariantViolation("Unknown reservation")
        del self._reservations[reservation_id]
