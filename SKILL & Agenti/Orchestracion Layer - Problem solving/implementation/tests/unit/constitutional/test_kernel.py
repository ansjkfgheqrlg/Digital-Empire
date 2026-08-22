from __future__ import annotations

import asyncio
import base64
from datetime import datetime, timedelta
from uuid import uuid4

import pytest
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from pydantic import ValidationError

from conftest import FakeAuthority, FixedClock, InMemoryConstitutionRepository, sign_payload
from orchestration_layer.constitutional.canonical import canonical_bytes, sha256_hex
from orchestration_layer.constitutional.errors import (
    ActivationConflict,
    ActivationDenied,
    ConstitutionIntegrityError,
    ConstitutionNotFound,
    ConstitutionSignatureError,
    InvalidBinding,
)
from orchestration_layer.constitutional.models import (
    ActivationCommand,
    ActivationReceipt,
    BoundaryDisposition,
    ConstitutionPayload,
    PrecedenceDomain,
    Principle,
    RuleCandidate,
    SignedConstitutionBundle,
)
from orchestration_layer.constitutional.signing import Ed25519TrustStoreVerifier

HEX_A = "a" * 64
HEX_B = "b" * 64


@pytest.mark.asyncio
async def test_loads_valid_signed_constitution(signing_material, make_kernel) -> None:
    bundle, verifier = signing_material
    kernel, _, _, _ = make_kernel(bundle, verifier)

    loaded = await kernel.load_constitution("2.1.0")

    assert loaded == bundle


@pytest.mark.asyncio
async def test_missing_version_fails_closed(signing_material, make_kernel) -> None:
    bundle, verifier = signing_material
    kernel, _, _, _ = make_kernel(bundle, verifier)

    with pytest.raises(ConstitutionNotFound):
        await kernel.load_constitution("9.9.9")


@pytest.mark.asyncio
async def test_hash_mismatch_precedes_signature_acceptance(
    payload: ConstitutionPayload,
    signing_material,
    make_kernel,
) -> None:
    _, verifier = signing_material
    private_key = Ed25519PrivateKey.generate()
    bundle = sign_payload(payload, private_key, payload_hash="0" * 64)
    kernel, _, _, _ = make_kernel(bundle, verifier)

    with pytest.raises(ConstitutionIntegrityError, match="hash mismatch"):
        await kernel.load_constitution("2.1.0")


@pytest.mark.asyncio
async def test_unknown_key_and_bad_signature_are_rejected(
    payload: ConstitutionPayload,
    signing_material,
    make_kernel,
) -> None:
    valid_bundle, verifier = signing_material
    unknown_key_bundle = valid_bundle.model_copy(update={"key_id": "unknown-root"})
    unknown_kernel, _, _, _ = make_kernel(unknown_key_bundle, verifier)
    with pytest.raises(ConstitutionSignatureError):
        await unknown_kernel.load_constitution("2.1.0")

    wrong_private_key = Ed25519PrivateKey.generate()
    wrong_signature = wrong_private_key.sign(canonical_bytes(payload))
    bad_bundle = valid_bundle.model_copy(
        update={"signature_b64": base64.b64encode(wrong_signature).decode("ascii")}
    )
    bad_kernel, _, _, _ = make_kernel(bad_bundle, verifier)
    with pytest.raises(ConstitutionSignatureError):
        await bad_kernel.load_constitution("2.1.0")


@pytest.mark.asyncio
async def test_repository_cannot_alias_a_different_version(
    signing_material,
    make_kernel,
) -> None:
    bundle, verifier = signing_material
    repository = InMemoryConstitutionRepository()
    repository.bundles["2.2.0"] = bundle
    kernel, _, _, _ = make_kernel(bundle, verifier, repository=repository)

    with pytest.raises(ConstitutionIntegrityError, match="version and payload version"):
        await kernel.load_constitution("2.2.0")


def test_constitution_requires_exactly_ten_ordered_principles(
    payload: ConstitutionPayload,
) -> None:
    raw = payload.model_dump(mode="python")
    raw["principles"] = raw["principles"][:-1]
    with pytest.raises(ValidationError):
        ConstitutionPayload.model_validate(raw, strict=True)

    reordered = payload.model_dump(mode="python")
    principles = list(reordered["principles"])
    principles[0], principles[1] = principles[1], principles[0]
    reordered["principles"] = tuple(principles)
    with pytest.raises(ValidationError, match=r"ordered exactly 0\.\.9"):
        ConstitutionPayload.model_validate(reordered, strict=True)


def test_constitution_rejects_demoted_safety_domain(payload: ConstitutionPayload) -> None:
    raw = payload.model_dump(mode="python")
    precedence = list(raw["precedence"])
    precedence[0], precedence[4] = precedence[4], precedence[0]
    precedence = [{**item, "rank": index} for index, item in enumerate(precedence, 1)]
    raw["precedence"] = tuple(precedence)

    with pytest.raises(ValidationError, match="top four precedence"):
        ConstitutionPayload.model_validate(raw, strict=True)


@pytest.mark.asyncio
async def test_binding_is_immutable_and_detects_material_tampering(
    signing_material,
    make_kernel,
) -> None:
    bundle, verifier = signing_material
    kernel, _, _, _ = make_kernel(bundle, verifier)
    binding = kernel.bind_constitution_to_case(
        case_id=uuid4(),
        bundle=bundle,
        phase_policy_hash=HEX_A,
        scope_hash=HEX_B,
    )

    assert await kernel.verify_constitution_binding(binding) is True
    with pytest.raises(ValidationError):
        binding.scope_hash = HEX_A  # type: ignore[misc]

    tampered = binding.model_copy(update={"scope_hash": HEX_A})
    with pytest.raises(InvalidBinding, match="binding hash mismatch"):
        await kernel.verify_constitution_binding(tampered)


@pytest.mark.asyncio
async def test_binding_rejects_each_tampered_material_field(
    signing_material,
    make_kernel,
) -> None:
    bundle, verifier = signing_material
    kernel, _, _, _ = make_kernel(bundle, verifier)
    binding = kernel.bind_constitution_to_case(
        case_id=uuid4(), bundle=bundle, phase_policy_hash=HEX_A, scope_hash=HEX_B
    )
    mutations = (
        {"binding_id": uuid4()},
        {"case_id": uuid4()},
        {"constitution_hash": "c" * 64},
        {"phase_policy_hash": "d" * 64},
        {"scope_hash": "e" * 64},
        {"bound_at": binding.bound_at + timedelta(seconds=1)},
        {"binding_hash": "f" * 64},
    )

    for update in mutations:
        with pytest.raises(InvalidBinding):
            await kernel.verify_constitution_binding(binding.model_copy(update=update))

    wrong_version = binding.model_copy(update={"constitution_version": "9.9.9"})
    with pytest.raises(ConstitutionNotFound):
        await kernel.verify_constitution_binding(wrong_version)


@pytest.mark.asyncio
async def test_binding_detects_same_version_content_replacement(
    payload: ConstitutionPayload,
    signing_material,
    make_kernel,
) -> None:
    bundle, verifier = signing_material
    kernel, repository, _, _ = make_kernel(bundle, verifier)
    binding = kernel.bind_constitution_to_case(
        case_id=uuid4(), bundle=bundle, phase_policy_hash=HEX_A, scope_hash=HEX_B
    )

    changed_identity = payload.identity.model_copy(
        update={"first_person_statement": "IO SONO UNA VERSIONE DIVERSA."}
    )
    changed_payload = payload.model_copy(update={"identity": changed_identity})
    private_key = Ed25519PrivateKey.generate()
    replacement = sign_payload(changed_payload, private_key)
    repository.bundles["2.1.0"] = replacement

    class ReplacementVerifier:
        def verify(self, *, key_id: str, message: bytes, signature: bytes) -> bool:
            return message in {
                canonical_bytes(bundle.payload),
                canonical_bytes(replacement.payload),
            }

    replacement_kernel, _, _, _ = make_kernel(
        bundle,
        ReplacementVerifier(),  # type: ignore[arg-type]
        repository=repository,
    )
    with pytest.raises(InvalidBinding, match="no longer matches"):
        await replacement_kernel.verify_constitution_binding(binding)


def test_precedence_selects_higher_constitutional_domain(
    signing_material,
    make_kernel,
) -> None:
    bundle, verifier = signing_material
    kernel, _, _, _ = make_kernel(bundle, verifier)
    candidates = (
        RuleCandidate(
            candidate_id="fast",
            domain=PrecedenceDomain.COST_LATENCY,
            statement="Deliver immediately",
        ),
        RuleCandidate(
            candidate_id="safe",
            domain=PrecedenceDomain.SAFETY,
            statement="Contain harm before delivery",
        ),
    )

    decision = kernel.resolve_rule_precedence(bundle=bundle, candidates=candidates)

    assert decision.winner.candidate_id == "safe"
    assert decision.winning_rank == 1
    assert decision.rejected_candidate_ids == ("fast",)


def test_same_rank_conflict_does_not_use_hidden_tiebreak(signing_material, make_kernel) -> None:
    bundle, verifier = signing_material
    kernel, _, _, _ = make_kernel(bundle, verifier)
    candidates = (
        RuleCandidate(
            candidate_id="safety-a",
            domain=PrecedenceDomain.SAFETY,
            statement="Contain A",
        ),
        RuleCandidate(
            candidate_id="safety-b",
            domain=PrecedenceDomain.SAFETY,
            statement="Contain B",
        ),
    )

    with pytest.raises(ConstitutionIntegrityError, match="same-rank"):
        kernel.resolve_rule_precedence(bundle=bundle, candidates=candidates)


@pytest.mark.parametrize(
    ("capability", "disposition", "handoff", "target"),
    [
        ("nerve.triage", BoundaryDisposition.IN_LAYER, False, None),
        ("finance.quantitative_model", BoundaryDisposition.OUT_OF_LAYER, True, "LAYER_2"),
        ("unknown.specialty", BoundaryDisposition.OUT_OF_LAYER, True, "UNRESOLVED_CAPABILITY"),
    ],
)
def test_boundary_decisions_are_typed_and_unknown_fails_closed(
    signing_material,
    make_kernel,
    capability: str,
    disposition: BoundaryDisposition,
    handoff: bool,
    target: str | None,
) -> None:
    bundle, verifier = signing_material
    kernel, _, _, _ = make_kernel(bundle, verifier)

    decision = kernel.assert_layer_boundary(bundle=bundle, capability=capability)

    assert decision.disposition is disposition
    assert decision.requires_handoff is handoff
    assert decision.target_layer == target


@pytest.mark.asyncio
async def test_identity_anchor_requires_verified_case_binding(
    signing_material,
    make_kernel,
) -> None:
    bundle, verifier = signing_material
    kernel, _, _, _ = make_kernel(bundle, verifier)
    binding = kernel.bind_constitution_to_case(
        case_id=uuid4(), bundle=bundle, phase_policy_hash=HEX_A, scope_hash=HEX_B
    )

    anchor = await kernel.render_identity_anchor(binding)

    assert anchor.name == "NERVE-SOLVE"
    assert "IO SONO" in anchor.first_person_statement
    assert "checklist" in anchor.not_a

    tampered = binding.model_copy(update={"case_id": uuid4()})
    with pytest.raises(InvalidBinding, match="binding hash mismatch"):
        await kernel.render_identity_anchor(tampered)


@pytest.mark.asyncio
async def test_diff_has_no_activation_side_effect(
    payload: ConstitutionPayload,
    signing_material,
    make_kernel,
) -> None:
    before, _verifier = signing_material
    private_key = Ed25519PrivateKey.generate()
    changed_principle = payload.principles[9].model_copy(
        update={"falsifier": "Una closure avviene con un blocco ancora aperto."}
    )
    next_payload = payload.model_copy(
        update={
            "constitution_version": "2.2.0",
            "principles": (*payload.principles[:9], changed_principle),
        }
    )
    after = sign_payload(next_payload, private_key)
    repository = InMemoryConstitutionRepository([before, after])
    # The verifier trusts both public keys only in this test.
    # Replace the second bundle with one signed by the original test key is impossible here,
    # so use a deterministic verifier scoped to the exact bundle hashes.
    class BundleVerifier:
        def verify(self, *, key_id: str, message: bytes, signature: bytes) -> bool:
            return message in {canonical_bytes(before.payload), canonical_bytes(after.payload)}

    kernel, repository, _, _ = make_kernel(
        before,
        BundleVerifier(),  # type: ignore[arg-type]
        repository=repository,
    )

    diff = await kernel.diff_constitution_versions("2.1.0", "2.2.0")

    assert diff.changed_principle_ids == (9,)
    assert diff.identity_changed is False
    assert repository.active_version is None
    assert repository.audit_events == []


def activation_command(*, expected: str | None = None) -> ActivationCommand:
    return ActivationCommand(
        command_id=uuid4(),
        principal_id="governance-owner",
        authority_decision_ref="authority://decision/approved-1",
        expected_current_version=expected,
        target_version="2.1.0",
        migration_plan_ref="artifact://migration/plan-1",
        requested_at=FixedClock().now(),
    )


def test_activation_command_requires_migration_plan() -> None:
    raw = activation_command().model_dump(mode="python")
    raw["migration_plan_ref"] = ""
    with pytest.raises(ValidationError):
        ActivationCommand.model_validate(raw, strict=True)


@pytest.mark.asyncio
async def test_activation_requires_independent_authority(signing_material, make_kernel) -> None:
    bundle, verifier = signing_material
    authority = FakeAuthority(allowed=False)
    kernel, repository, _, _ = make_kernel(bundle, verifier, authority=authority)

    with pytest.raises(ActivationDenied):
        await kernel.activate_constitution_version(activation_command())
    assert repository.active_version is None
    assert repository.audit_events == []


@pytest.mark.asyncio
async def test_concurrent_activation_has_one_cas_winner(signing_material, make_kernel) -> None:
    bundle, verifier = signing_material
    kernel, repository, _, _ = make_kernel(bundle, verifier)

    results = await asyncio.gather(
        kernel.activate_constitution_version(activation_command()),
        kernel.activate_constitution_version(activation_command()),
        return_exceptions=True,
    )

    assert sum(isinstance(item, ActivationReceipt) for item in results) == 1
    assert sum(isinstance(item, ActivationConflict) for item in results) == 1
    assert repository.repository_version == 1
    assert len(repository.audit_events) == 1


@pytest.mark.asyncio
async def test_activation_is_compare_and_swap_and_audit_is_atomic(
    signing_material,
    make_kernel,
) -> None:
    bundle, verifier = signing_material
    kernel, repository, _, clock = make_kernel(bundle, verifier)

    receipt = await kernel.activate_constitution_version(activation_command())

    assert receipt.active_version == "2.1.0"
    assert receipt.constitution_hash == bundle.payload_hash
    assert receipt.repository_version == 1
    assert repository.active_version == "2.1.0"
    assert len(repository.audit_events) == 1
    assert repository.audit_events[0].occurred_at == clock.now()

    with pytest.raises(ActivationConflict):
        await kernel.activate_constitution_version(activation_command(expected=None))
    assert repository.repository_version == 1
    assert len(repository.audit_events) == 1


def test_naive_clock_is_rejected(signing_material, make_kernel) -> None:
    bundle, verifier = signing_material
    naive_clock = FixedClock(datetime(2026, 8, 13, 8, 0))
    kernel, _, _, _ = make_kernel(bundle, verifier, clock=naive_clock)

    with pytest.raises(ConstitutionIntegrityError, match="naive timestamp"):
        kernel.bind_constitution_to_case(
            case_id=uuid4(), bundle=bundle, phase_policy_hash=HEX_A, scope_hash=HEX_B
        )


def test_ed25519_trust_store_rejects_invalid_key_length() -> None:
    with pytest.raises(ValueError):
        Ed25519TrustStoreVerifier({"root": b"too-short"})


def test_bundle_rejects_noncanonical_signature(payload: ConstitutionPayload) -> None:
    with pytest.raises(ValidationError, match="canonical Ed25519"):
        SignedConstitutionBundle(
            payload=payload,
            payload_hash=sha256_hex(canonical_bytes(payload)),
            key_id="root",
            signature_b64=base64.b64encode(b"short").decode("ascii"),
        )


def test_principle_requires_visceral_first_person_statement() -> None:
    with pytest.raises(ValidationError):
        Principle(principle_id=0, statement="Validate the request.", falsifier="No validation")
