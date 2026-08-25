from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum
from typing import Any, Protocol


class ReconciliationStatus(StrEnum):
    ABSENT = "ABSENT"
    PRESENT = "PRESENT"
    UNKNOWN = "UNKNOWN"


@dataclass(frozen=True)
class ReconciliationResult:
    status: ReconciliationStatus
    evidence: dict[str, Any]


@dataclass(frozen=True)
class CompensationResult:
    success: bool
    evidence: dict[str, Any]
    error: str | None = None


class CompensatingOperation(Protocol):
    async def reconcile(self, context: dict[str, Any]) -> ReconciliationResult: ...
    async def compensate(self, context: dict[str, Any]) -> CompensationResult: ...


class CompensationCatalog:
    def __init__(self):
        self._operations: dict[str, CompensatingOperation] = {}

    def register(self, operation_id: str, operation: CompensatingOperation) -> None:
        if operation_id in self._operations:
            raise ValueError(f"Compensation operation already registered: {operation_id}")
        self._operations[operation_id] = operation

    def require(self, operation_id: str) -> CompensatingOperation:
        try:
            return self._operations[operation_id]
        except KeyError as exc:
            raise KeyError(f"Unregistered compensation operation: {operation_id}") from exc
