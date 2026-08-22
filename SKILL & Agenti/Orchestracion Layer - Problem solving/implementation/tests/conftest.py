from __future__ import annotations

import base64
from collections.abc import Iterator
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import pytest
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

from orchestration_layer.constitutional.canonical import canonical_bytes, sha256_hex
from orchestration_layer.constitutional.errors import ActivationConflict
from orchestration_layer.constitutional.models import (
    ActivationCommand,
    ActivationReceipt,
    ConstitutionAuditEvent,
    ConstitutionPayload,
    SignedConstitutionBundle,
)
from orchestration_layer.constitutional.signing import Ed25519TrustStoreVerifier


class FixedClock:
    def __init__(self, value: datetime | None = None) -> None:
        self.value = value or datetime(2026, 8, 13, 8, 0, tzinfo=UTC)

    def now(self) -> datetime:
        return self.value


class FakeAuthority:
    def __init__(self, allowed: bool = True) -> None:
        self.allowed = allowed
        self.calls: list[tuple[ActivationCommand, str]] = []

    async def is_authorized(
        self,
        *,
        command: ActivationCommand,
        constitution_hash: str,
    ) -> bool:
        self.calls.append((command, constitution_hash))
        return self.allowed


class InMemoryConstitutionRepository:
    """Test double only; production persistence remains PostgreSQL."""

    def __init__(self, bundles: list[SignedConstitutionBundle] | None = None) -> None:
        self.bundles = {
            item.payload.constitution_version: item for item in (bundles or [])
        }
        self.active_version: str | None = None
        self.repository_version = 0
        self.audit_events: list[ConstitutionAuditEvent] = []

    async def load(self, version: str) -> SignedConstitutionBundle | None:
        return self.bundles.get(version)

    async def activate(
        self,
        *,
        command: ActivationCommand,
        constitution_hash: str,
        activated_at: datetime,
        audit_event: ConstitutionAuditEvent,
    ) -> ActivationReceipt:
        if self.active_version != command.expected_current_version:
            raise ActivationConflict("expected active version is stale")
        previous = self.active_version
        self.active_version = command.target_version
        self.repository_version += 1
        self.audit_events.append(audit_event)
        return ActivationReceipt(
            command_id=command.command_id,
            previous_version=previous,
            active_version=command.target_version,
            constitution_hash=constitution_hash,
            activated_at=activated_at,
            repository_version=self.repository_version,
        )


def sign_payload(
    payload: ConstitutionPayload,
    private_key: Ed25519PrivateKey,
    *,
    key_id: str = "test-root-1",
    payload_hash: str | None = None,
    message_override: bytes | None = None,
) -> SignedConstitutionBundle:
    message = canonical_bytes(payload)
    signature = private_key.sign(message if message_override is None else message_override)
    return SignedConstitutionBundle(
        payload=payload,
        payload_hash=payload_hash or sha256_hex(message),
        key_id=key_id,
        signature_b64=base64.b64encode(signature).decode("ascii"),
    )


@pytest.fixture
def payload() -> ConstitutionPayload:
    path = (
        Path(__file__).parents[1]
        / "config"
        / "constitutions"
        / "nerve-solve-2.1.0.payload.json"
    )
    return ConstitutionPayload.model_validate_json(path.read_text(encoding="utf-8"), strict=True)


@pytest.fixture
def signing_material(
    payload: ConstitutionPayload,
) -> Iterator[tuple[SignedConstitutionBundle, Ed25519TrustStoreVerifier]]:
    private_key = Ed25519PrivateKey.generate()
    public_key = private_key.public_key().public_bytes(
        encoding=serialization.Encoding.Raw,
        format=serialization.PublicFormat.Raw,
    )
    yield sign_payload(payload, private_key), Ed25519TrustStoreVerifier(
        {"test-root-1": public_key}
    )


@pytest.fixture
def make_kernel() -> Any:
    from orchestration_layer.constitutional.kernel import ConstitutionalKernel

    def factory(
        bundle: SignedConstitutionBundle,
        verifier: Ed25519TrustStoreVerifier,
        *,
        authority: FakeAuthority | None = None,
        clock: FixedClock | None = None,
        repository: InMemoryConstitutionRepository | None = None,
    ) -> tuple[
        ConstitutionalKernel,
        InMemoryConstitutionRepository,
        FakeAuthority,
        FixedClock,
    ]:
        repo = repository or InMemoryConstitutionRepository([bundle])
        auth = authority or FakeAuthority()
        fixed_clock = clock or FixedClock()
        return (
            ConstitutionalKernel(
                repository=repo,
                signature_verifier=verifier,
                authority_verifier=auth,
                clock=fixed_clock,
            ),
            repo,
            auth,
            fixed_clock,
        )

    return factory
