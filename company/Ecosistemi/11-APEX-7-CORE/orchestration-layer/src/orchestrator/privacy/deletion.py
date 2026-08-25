from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field
from datetime import UTC, datetime
from enum import StrEnum
from typing import Any


class DeletionState(StrEnum):
    REQUESTED = "REQUESTED"
    IDENTITY_VERIFIED = "IDENTITY_VERIFIED"
    IMPACT_ANALYZED = "IMPACT_ANALYZED"
    ACTIVE_DELETE = "ACTIVE_DELETE"
    INDEX_PURGE = "INDEX_PURGE"
    VERIFIED = "VERIFIED"
    PARTIAL = "PARTIAL"
    CLOSED = "CLOSED"


class DeletionTransitionError(ValueError):
    pass


ALLOWED = {
    DeletionState.REQUESTED: {DeletionState.IDENTITY_VERIFIED},
    DeletionState.IDENTITY_VERIFIED: {DeletionState.IMPACT_ANALYZED},
    DeletionState.IMPACT_ANALYZED: {DeletionState.ACTIVE_DELETE},
    DeletionState.ACTIVE_DELETE: {DeletionState.INDEX_PURGE, DeletionState.PARTIAL},
    DeletionState.INDEX_PURGE: {DeletionState.VERIFIED, DeletionState.PARTIAL},
    DeletionState.PARTIAL: {DeletionState.ACTIVE_DELETE},
    DeletionState.VERIFIED: {DeletionState.CLOSED},
    DeletionState.CLOSED: set(),
}


@dataclass
class DeletionRequest:
    request_id: str
    tenant_id: str
    subject_ref_hashes: tuple[str, ...]
    requested_by: str
    state: DeletionState = DeletionState.REQUESTED
    version: int = 0
    systems: dict[str, str] = field(default_factory=dict)
    evidence: list[dict[str, Any]] = field(default_factory=list)
    backup_expiry_at: str | None = None
    legal_hold: bool = False

    @classmethod
    def create(
        cls,
        request_id: str,
        tenant_id: str,
        subject_refs: list[str],
        requested_by: str,
    ) -> "DeletionRequest":
        if not request_id or not tenant_id or not subject_refs or not requested_by:
            raise DeletionTransitionError("Deletion request requires id, tenant, subjects and requester")
        hashes = tuple(
            "sha256:" + hashlib.sha256(value.encode("utf-8")).hexdigest()
            for value in subject_refs
        )
        return cls(request_id, tenant_id, hashes, requested_by)

    def transition(
        self,
        target: DeletionState,
        *,
        actor: str,
        evidence: dict[str, Any],
        expected_version: int,
    ) -> None:
        if expected_version != self.version:
            raise DeletionTransitionError("Stale deletion request version")
        if target not in ALLOWED[self.state]:
            raise DeletionTransitionError(f"Illegal deletion transition {self.state}->{target}")
        if not actor or not evidence:
            raise DeletionTransitionError("Deletion transition requires actor and evidence")
        if self.legal_hold and target in {DeletionState.ACTIVE_DELETE, DeletionState.INDEX_PURGE}:
            raise DeletionTransitionError("Legal hold blocks active deletion")
        if target is DeletionState.VERIFIED:
            if not self.systems or any(
                status not in {"DELETED", "NOT_FOUND", "PURGED"}
                for status in self.systems.values()
            ):
                raise DeletionTransitionError("All systems must prove deletion/purge before verification")
            if not self.backup_expiry_at:
                raise DeletionTransitionError("Backup expiry must be tracked before verification")
        self.evidence.append(
            {
                "from": self.state.value,
                "to": target.value,
                "actor": actor,
                "evidence": evidence,
                "at": datetime.now(UTC).isoformat(),
            }
        )
        self.state = target
        self.version += 1

    def record_system(self, system: str, status: str, evidence_ref: str) -> None:
        if self.state not in {DeletionState.ACTIVE_DELETE, DeletionState.INDEX_PURGE, DeletionState.PARTIAL}:
            raise DeletionTransitionError("System deletion can only be recorded during deletion/purge")
        if status not in {"DELETED", "NOT_FOUND", "PURGED", "FAILED"}:
            raise DeletionTransitionError("Invalid system deletion status")
        self.systems[system] = status
        self.evidence.append({"system": system, "status": status, "evidence_ref": evidence_ref})

    def receipt(self) -> dict[str, Any]:
        if self.state is not DeletionState.CLOSED:
            raise DeletionTransitionError("Receipt is available only for a closed request")
        payload = {
            "request_id": self.request_id,
            "tenant_id": self.tenant_id,
            "subject_ref_hashes": list(self.subject_ref_hashes),
            "systems": self.systems,
            "backup_expiry_at": self.backup_expiry_at,
            "version": self.version,
        }
        encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
        return {**payload, "receipt_sha256": hashlib.sha256(encoded).hexdigest()}
