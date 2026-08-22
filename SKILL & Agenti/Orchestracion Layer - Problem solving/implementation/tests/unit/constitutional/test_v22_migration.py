from __future__ import annotations

import base64
import json
from pathlib import Path
from uuid import uuid4

import pytest
from pydantic import ValidationError

from conftest import FakeAuthority, FixedClock, InMemoryConstitutionRepository
from orchestration_layer.constitutional.canonical import canonical_bytes, sha256_hex
from orchestration_layer.constitutional.errors import (
    ActivationDenied,
    ConstitutionIntegrityError,
    ConstitutionSignatureError,
)
from orchestration_layer.constitutional.models import (
    ActivationCommand,
    ConstitutionPayload,
    SignedConstitutionBundle,
)
from orchestration_layer.constitutional.signing import Ed25519TrustStoreVerifier

HEX_A = "a" * 64
HEX_B = "b" * 64
TEST_KEY_ID = "test-only-static-proposal-verifier"
TEST_SIGNATURE = b"NS-A-v2.2-verifier-port-test-double".ljust(64, b"-")
TEST_SIGNATURE_B64 = base64.b64encode(TEST_SIGNATURE).decode("ascii")


def payload_path(version: str) -> Path:
    root = Path(__file__).parents[3]
    if version == "2.1.0":
        return root / "config/constitutions/nerve-solve-2.1.0.payload.json"
    if version == "2.2.0":
        return root / "proposals/constitution/nerve-solve-2.2.0.payload.proposed.json"
    raise ValueError(f"unsupported test payload version {version}")


def load_payload(version: str) -> ConstitutionPayload:
    return ConstitutionPayload.model_validate_json(
        payload_path(version).read_text(encoding="utf-8"),
        strict=True,
    )


def make_test_bundle(payload: ConstitutionPayload) -> SignedConstitutionBundle:
    """Build an in-memory port-test object; this is not a signed release artifact."""

    return SignedConstitutionBundle(
        payload=payload,
        payload_hash=sha256_hex(canonical_bytes(payload)),
        key_id=TEST_KEY_ID,
        signature_b64=TEST_SIGNATURE_B64,
    )


class StaticProposalVerifier:
    """No-key verifier test double scoped to exact canonical messages and bytes."""

    def __init__(
        self,
        *payloads: ConstitutionPayload,
        revoked_key_ids: frozenset[str] = frozenset(),
    ) -> None:
        self._messages = {canonical_bytes(payload) for payload in payloads}
        self._revoked_key_ids = revoked_key_ids

    def verify(self, *, key_id: str, message: bytes, signature: bytes) -> bool:
        return (
            key_id == TEST_KEY_ID
            and key_id not in self._revoked_key_ids
            and message in self._messages
            and signature == TEST_SIGNATURE
        )


def migration_command(*, expected: str, target: str) -> ActivationCommand:
    """Return an in-memory negative-path command; never a release/activation artifact."""

    return ActivationCommand(
        command_id=uuid4(),
        principal_id="negative-path-test-principal",
        authority_decision_ref="test-only://not-an-authority-decision",
        expected_current_version=expected,
        target_version=target,
        migration_plan_ref="test-only://migration-negative-path",
        requested_at=FixedClock().now(),
    )


def test_v22_proposed_payload_passes_strict_schema_and_rejects_extra_fields() -> None:
    raw_text = payload_path("2.2.0").read_text(encoding="utf-8")

    proposed = ConstitutionPayload.model_validate_json(raw_text, strict=True)

    assert proposed.schema_version == "1.0"
    assert proposed.constitution_version == "2.2.0"
    assert [item.principle_id for item in proposed.principles] == list(range(10))
    assert [item.rank for item in proposed.precedence] == list(range(1, 12))
    assert {item.capability for item in proposed.boundaries} >= {
        "nerve.problem_structure",
        "nerve.execution_commitment",
    }

    with_extra = json.loads(raw_text)
    with_extra["unreviewed_extension"] = True
    with pytest.raises(ValidationError, match="Extra inputs are not permitted"):
        ConstitutionPayload.model_validate(with_extra, strict=True)


@pytest.mark.asyncio
async def test_v21_to_v22_diff_is_semantic_controlled_and_side_effect_free(
    make_kernel,
) -> None:
    before_payload = load_payload("2.1.0")
    after_payload = load_payload("2.2.0")
    before = make_test_bundle(before_payload)
    after = make_test_bundle(after_payload)
    repository = InMemoryConstitutionRepository([before, after])
    verifier = StaticProposalVerifier(before_payload, after_payload)
    kernel, repository, authority, _ = make_kernel(
        before,
        verifier,
        repository=repository,
    )

    diff = await kernel.diff_constitution_versions("2.1.0", "2.2.0")

    assert diff.from_hash == "66a9a215c5af4f0ed3011b6f51489170c01fb4ba09e4af8a8fc0318b850642c4"
    assert diff.to_hash == "a7d3d32d41eb22ae2dd02ae5297be1660e8edb9a701cd5e6f641148b345ade4d"
    assert diff.identity_changed is False
    assert diff.changed_principle_ids == (0, 2, 4, 6, 7)
    assert diff.added_capabilities == (
        "nerve.execution_commitment",
        "nerve.problem_structure",
    )
    assert diff.removed_capabilities == ()
    assert diff.changed_capabilities == ()
    assert diff.precedence_changed is False
    assert repository.active_version is None
    assert repository.repository_version == 0
    assert repository.audit_events == []
    assert authority.calls == []


@pytest.mark.asyncio
async def test_dual_candidates_keep_case_bindings_isolated_and_immutable(
    make_kernel,
) -> None:
    before_payload = load_payload("2.1.0")
    after_payload = load_payload("2.2.0")
    before = make_test_bundle(before_payload)
    after = make_test_bundle(after_payload)
    repository = InMemoryConstitutionRepository([before, after])
    verifier = StaticProposalVerifier(before_payload, after_payload)
    kernel, _, _, _ = make_kernel(before, verifier, repository=repository)

    before_binding = kernel.bind_constitution_to_case(
        case_id=uuid4(),
        bundle=before,
        phase_policy_hash=HEX_A,
        scope_hash=HEX_B,
    )
    after_binding = kernel.bind_constitution_to_case(
        case_id=uuid4(),
        bundle=after,
        phase_policy_hash=HEX_B,
        scope_hash=HEX_A,
    )

    assert await kernel.verify_constitution_binding(before_binding) is True
    assert await kernel.verify_constitution_binding(after_binding) is True
    assert before_binding.constitution_version == "2.1.0"
    assert after_binding.constitution_version == "2.2.0"
    assert before_binding.constitution_hash != after_binding.constitution_hash
    with pytest.raises(ValidationError, match="Instance is frozen"):
        before_binding.constitution_version = "2.2.0"  # type: ignore[misc]
    assert before_binding.constitution_version == "2.1.0"
    assert repository.active_version is None


def test_ed25519_verifier_explicit_revocation_overrides_valid_signature() -> None:
    """RFC 8032 §7.1 public test vector; no private key is generated or stored."""

    key_id = "rfc8032-public-test-vector-1"
    public_key = bytes.fromhex(
        "d75a980182b10ab7d54bfed3c964073a"
        "0ee172f3daa62325af021a68f707511a"
    )
    signature = bytes.fromhex(
        "e5564300c360ac729086e2cc806e828a"
        "84877f1eb8e5d974d873e06522490155"
        "5fb8821590a33bacc61e39701cf9b46b"
        "d25bf5f0595bbe24655141438e7a100b"
    )

    trusted = Ed25519TrustStoreVerifier({key_id: public_key})
    revoked = Ed25519TrustStoreVerifier(
        {key_id: public_key},
        revoked_key_ids=frozenset({key_id}),
    )

    assert trusted.verify(key_id=key_id, message=b"", signature=signature) is True
    assert revoked.verify(key_id=key_id, message=b"", signature=signature) is False


@pytest.mark.asyncio
async def test_v22_candidate_rejects_revoked_key_signature_tamper_and_payload_tamper(
    make_kernel,
) -> None:
    proposed = load_payload("2.2.0")
    bundle = make_test_bundle(proposed)

    revoked = StaticProposalVerifier(
        proposed,
        revoked_key_ids=frozenset({TEST_KEY_ID}),
    )
    revoked_kernel, _, _, _ = make_kernel(bundle, revoked)
    with pytest.raises(ConstitutionSignatureError):
        await revoked_kernel.load_constitution("2.2.0")

    bad_signature = bundle.model_copy(
        update={
            "signature_b64": base64.b64encode(b"x" * 64).decode("ascii"),
        }
    )
    verifier = StaticProposalVerifier(proposed)
    signature_kernel, _, _, _ = make_kernel(bad_signature, verifier)
    with pytest.raises(ConstitutionSignatureError):
        await signature_kernel.load_constitution("2.2.0")

    tampered_principle = proposed.principles[0].model_copy(
        update={"falsifier": "Tampered after review."}
    )
    tampered_payload = proposed.model_copy(
        update={"principles": (tampered_principle, *proposed.principles[1:])}
    )
    payload_tamper = bundle.model_copy(update={"payload": tampered_payload})
    payload_kernel, _, _, _ = make_kernel(payload_tamper, verifier)
    with pytest.raises(ConstitutionIntegrityError, match="hash mismatch"):
        await payload_kernel.load_constitution("2.2.0")


@pytest.mark.asyncio
async def test_activation_rejects_downgrade_before_authority_or_repository_side_effect(
    make_kernel,
) -> None:
    before_payload = load_payload("2.1.0")
    after_payload = load_payload("2.2.0")
    before = make_test_bundle(before_payload)
    after = make_test_bundle(after_payload)
    repository = InMemoryConstitutionRepository([before, after])
    repository.active_version = "2.2.0"
    authority = FakeAuthority(allowed=True)
    verifier = StaticProposalVerifier(before_payload, after_payload)
    kernel, _, _, _ = make_kernel(
        before,
        verifier,
        repository=repository,
        authority=authority,
    )

    with pytest.raises(ActivationDenied, match="newer"):
        await kernel.activate_constitution_version(
            migration_command(expected="2.2.0", target="2.1.0")
        )

    assert authority.calls == []
    assert repository.active_version == "2.2.0"
    assert repository.repository_version == 0
    assert repository.audit_events == []


@pytest.mark.asyncio
async def test_forward_version_reaches_authority_but_denial_leaves_state_unchanged(
    make_kernel,
) -> None:
    before_payload = load_payload("2.1.0")
    after_payload = load_payload("2.2.0")
    before = make_test_bundle(before_payload)
    after = make_test_bundle(after_payload)
    repository = InMemoryConstitutionRepository([before, after])
    repository.active_version = "2.1.0"
    authority = FakeAuthority(allowed=False)
    verifier = StaticProposalVerifier(before_payload, after_payload)
    kernel, _, _, _ = make_kernel(
        before,
        verifier,
        repository=repository,
        authority=authority,
    )

    with pytest.raises(ActivationDenied, match="authority denied"):
        await kernel.activate_constitution_version(
            migration_command(expected="2.1.0", target="2.2.0")
        )

    assert len(authority.calls) == 1
    assert repository.active_version == "2.1.0"
    assert repository.repository_version == 0
    assert repository.audit_events == []


@pytest.mark.asyncio
async def test_activation_rejects_same_version_collision_before_authority(
    make_kernel,
) -> None:
    payload = load_payload("2.1.0")
    bundle = make_test_bundle(payload)
    repository = InMemoryConstitutionRepository([bundle])
    repository.active_version = "2.1.0"
    authority = FakeAuthority(allowed=True)
    verifier = StaticProposalVerifier(payload)
    kernel, _, _, _ = make_kernel(
        bundle,
        verifier,
        repository=repository,
        authority=authority,
    )

    with pytest.raises(ActivationDenied, match="newer"):
        await kernel.activate_constitution_version(
            migration_command(expected="2.1.0", target="2.1.0")
        )

    assert authority.calls == []
    assert repository.repository_version == 0
    assert repository.audit_events == []
