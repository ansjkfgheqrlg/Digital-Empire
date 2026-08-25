from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum


class ReleaseRing(StrEnum):
    DEV = "DEV"
    TEST = "TEST"
    SHADOW = "SHADOW"
    CANARY_5 = "CANARY_5"
    CANARY_25 = "CANARY_25"
    PILOT = "PILOT"
    PROD = "PROD"
    ROLLED_BACK = "ROLLED_BACK"


ORDER = [
    ReleaseRing.DEV,
    ReleaseRing.TEST,
    ReleaseRing.SHADOW,
    ReleaseRing.CANARY_5,
    ReleaseRing.CANARY_25,
    ReleaseRing.PILOT,
    ReleaseRing.PROD,
]


class RolloutError(RuntimeError):
    pass


@dataclass
class ReleaseController:
    release_id: str
    prr_verdict: str
    ring: ReleaseRing = ReleaseRing.DEV
    history: list[dict] = field(default_factory=list)

    def promote(self, target: ReleaseRing, *, hard_gates_pass: bool) -> None:
        if self.ring is ReleaseRing.ROLLED_BACK:
            raise RolloutError("Rolled-back release cannot be promoted")
        current_index = ORDER.index(self.ring)
        if target not in ORDER or ORDER.index(target) != current_index + 1:
            raise RolloutError(f"Promotion must be one ring at a time: {self.ring}->{target}")
        if not hard_gates_pass:
            raise RolloutError("Hard gate failure blocks promotion")
        if target is ReleaseRing.PROD and self.prr_verdict != "GO":
            raise RolloutError("Production promotion requires PRR GO")
        previous = self.ring
        self.ring = target
        self.history.append({"action": "PROMOTE", "from": previous.value, "to": target.value})

    def rollback(self, reason: str) -> None:
        if not reason:
            raise RolloutError("Rollback requires a reason")
        previous = self.ring
        self.ring = ReleaseRing.ROLLED_BACK
        self.history.append({"action": "ROLLBACK", "from": previous.value, "reason": reason})
