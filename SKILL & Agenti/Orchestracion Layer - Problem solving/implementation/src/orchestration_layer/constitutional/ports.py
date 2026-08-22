"""Ports required by the Constitutional Kernel.

Implementations may use PostgreSQL, KMS or another approved service. The kernel itself
never receives private signing keys and never treats RuFLO as authoritative storage.
"""

from __future__ import annotations

from datetime import datetime
from typing import Protocol

from .models import (
    ActivationCommand,
    ActivationReceipt,
    ConstitutionAuditEvent,
    SignedConstitutionBundle,
)


class ConstitutionRepository(Protocol):
    async def load(self, version: str) -> SignedConstitutionBundle | None:
        """Load an immutable signed bundle by exact version."""

    async def activate(
        self,
        *,
        command: ActivationCommand,
        constitution_hash: str,
        activated_at: datetime,
        audit_event: ConstitutionAuditEvent,
    ) -> ActivationReceipt:
        """Atomically activate and append audit if expected version matches."""


class SignatureVerifier(Protocol):
    def verify(self, *, key_id: str, message: bytes, signature: bytes) -> bool:
        """Verify with an approved public key; unknown keys return False."""


class ActivationAuthorityVerifier(Protocol):
    async def is_authorized(
        self,
        *,
        command: ActivationCommand,
        constitution_hash: str,
    ) -> bool:
        """Validate an external, scoped authority decision."""


class Clock(Protocol):
    def now(self) -> datetime:
        """Return a timezone-aware timestamp."""
