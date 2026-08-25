from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum

from .errors import InvariantViolation


class SideEffectMode(StrEnum):
    NONE = "NONE"
    IDEMPOTENT = "IDEMPOTENT"
    COMPENSATABLE = "COMPENSATABLE"
    IRREVERSIBLE = "IRREVERSIBLE"


@dataclass(frozen=True)
class SideEffectContract:
    mode: SideEffectMode
    idempotency_key_template: str | None = None
    result_lookup: bool = False
    reconciliation_operation: str | None = None
    compensation_operation: str | None = None
    irreversible_approval: str | None = None

    def __post_init__(self) -> None:
        if self.mode is SideEffectMode.NONE:
            if any(
                (
                    self.idempotency_key_template,
                    self.reconciliation_operation,
                    self.compensation_operation,
                    self.irreversible_approval,
                )
            ):
                raise InvariantViolation("NONE side effect cannot declare action controls")
        elif self.mode is SideEffectMode.IDEMPOTENT:
            if not self.idempotency_key_template or not self.result_lookup:
                raise InvariantViolation("IDEMPOTENT requires a key template and result lookup")
        elif self.mode is SideEffectMode.COMPENSATABLE:
            if not self.reconciliation_operation or not self.compensation_operation:
                raise InvariantViolation(
                    "COMPENSATABLE requires reconciliation and compensation operations"
                )
        elif self.mode is SideEffectMode.IRREVERSIBLE:
            if not self.irreversible_approval:
                raise InvariantViolation("IRREVERSIBLE requires explicit approval policy")
            if self.compensation_operation:
                raise InvariantViolation("IRREVERSIBLE cannot claim compensation")

    @property
    def retryable(self) -> bool:
        return self.mode in {SideEffectMode.NONE, SideEffectMode.IDEMPOTENT}
