from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime
from typing import Any
from uuid import uuid4


@dataclass(frozen=True)
class DomainEvent:
    event_id: str
    event_type: str
    workflow_id: str
    sequence: int
    aggregate_version: int
    occurred_at: datetime
    payload: dict[str, Any]

    @classmethod
    def create(
        cls,
        event_type: str,
        workflow_id: str,
        sequence: int,
        aggregate_version: int,
        payload: dict[str, Any],
    ) -> "DomainEvent":
        return cls(
            event_id=str(uuid4()),
            event_type=event_type,
            workflow_id=workflow_id,
            sequence=sequence,
            aggregate_version=aggregate_version,
            occurred_at=datetime.now(UTC),
            payload=payload,
        )
