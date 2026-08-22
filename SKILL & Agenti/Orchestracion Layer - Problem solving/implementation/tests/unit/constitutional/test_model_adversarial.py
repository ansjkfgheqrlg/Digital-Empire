from __future__ import annotations

from datetime import datetime
from uuid import uuid4

import pytest
from pydantic import ValidationError

from conftest import FixedClock
from orchestration_layer.constitutional.canonical import canonical_bytes, sha256_hex
from orchestration_layer.constitutional.models import (
    ActivationCommand,
    ActivationReceipt,
    BoundaryDisposition,
    BoundaryRule,
    ConstitutionAuditEvent,
    ConstitutionBinding,
    ConstitutionPayload,
    SignedConstitutionBundle,
)
from orchestration_layer.constitutional.signing import Ed25519TrustStoreVerifier

HEX_A = "a" * 64
HEX_B = "b" * 64
HEX_C = "c" * 64


def test_boundary_rules_reject_inconsistent_handoffs() -> None:
    with pytest.raises(ValidationError, match="requires target_layer"):
        BoundaryRule(
            capability="finance.model",
            disposition=BoundaryDisposition.OUT_OF_LAYER,
            target_layer=None,
            reason="Specialist boundary",
        )

    with pytest.raises(ValidationError, match="cannot nominate target_layer"):
        BoundaryRule(
            capability="nerve.triage",
            disposition=BoundaryDisposition.IN_LAYER,
            target_layer="LAYER_2",
            reason="Core boundary",
        )


@pytest.mark.parametrize("defect", ["rank", "domain", "capability"])
def test_constitution_rejects_ambiguous_policy_tables(
    payload: ConstitutionPayload,
    defect: str,
) -> None:
    raw = payload.model_dump(mode="python")
    if defect == "rank":
        precedence = list(raw["precedence"])
        precedence[1] = {**precedence[1], "rank": 1}
        raw["precedence"] = tuple(precedence)
        expected = "ordered and contiguous"
    elif defect == "domain":
        precedence = list(raw["precedence"])
        precedence[4] = {**precedence[4], "domain": precedence[0]["domain"]}
        raw["precedence"] = tuple(precedence)
        expected = "domains must be unique"
    else:
        boundaries = list(raw["boundaries"])
        boundaries[-1] = {**boundaries[-1], "capability": boundaries[0]["capability"]}
        raw["boundaries"] = tuple(boundaries)
        expected = "capabilities must be unique"

    with pytest.raises(ValidationError, match=expected):
        ConstitutionPayload.model_validate(raw, strict=True)


def test_bundle_rejects_malformed_base64(payload: ConstitutionPayload) -> None:
    with pytest.raises(ValidationError, match="not valid base64"):
        SignedConstitutionBundle(
            payload=payload,
            payload_hash=sha256_hex(canonical_bytes(payload)),
            key_id="root",
            signature_b64="not-base64!",
        )


def test_bundle_rejects_missing_signature(signing_material) -> None:
    bundle, _verifier = signing_material
    raw = bundle.model_dump(mode="python")
    del raw["signature_b64"]
    with pytest.raises(ValidationError):
        SignedConstitutionBundle.model_validate(raw, strict=True)


def test_trust_store_rejects_blank_key_identifier() -> None:
    with pytest.raises(ValueError, match="key_id cannot be empty"):
        Ed25519TrustStoreVerifier({" ": b"0" * 32})


def test_constitution_rejects_naive_issued_at(payload: ConstitutionPayload) -> None:
    raw = payload.model_dump(mode="python")
    raw["issued_at"] = datetime(2026, 8, 13, 8, 0)
    with pytest.raises(ValidationError, match="issued_at must be timezone-aware"):
        ConstitutionPayload.model_validate(raw, strict=True)


def test_binding_rejects_naive_bound_at() -> None:
    with pytest.raises(ValidationError, match="bound_at must be timezone-aware"):
        ConstitutionBinding(
            binding_id=uuid4(),
            case_id=uuid4(),
            constitution_version="2.1.0",
            constitution_hash=HEX_A,
            phase_policy_hash=HEX_B,
            scope_hash=HEX_C,
            bound_at=datetime(2026, 8, 13, 8, 0),
            binding_hash=HEX_A,
        )


def test_activation_command_rejects_naive_requested_at() -> None:
    with pytest.raises(ValidationError, match="requested_at must be timezone-aware"):
        ActivationCommand(
            command_id=uuid4(),
            principal_id="governance-owner",
            authority_decision_ref="authority://decision/1",
            expected_current_version=None,
            target_version="2.1.0",
            migration_plan_ref="artifact://migration/1",
            requested_at=datetime(2026, 8, 13, 8, 0),
        )


def test_activation_receipt_rejects_naive_activated_at() -> None:
    with pytest.raises(ValidationError, match="activated_at must be timezone-aware"):
        ActivationReceipt(
            command_id=uuid4(),
            previous_version=None,
            active_version="2.1.0",
            constitution_hash=HEX_A,
            activated_at=datetime(2026, 8, 13, 8, 0),
            repository_version=1,
        )


def test_audit_event_rejects_naive_occurred_at() -> None:
    with pytest.raises(ValidationError, match="occurred_at must be timezone-aware"):
        ConstitutionAuditEvent(
            event_id=uuid4(),
            event_type="CONSTITUTION_ACTIVATED",
            occurred_at=datetime(2026, 8, 13, 8, 0),
            principal_id="governance-owner",
            target_version="2.1.0",
            constitution_hash=HEX_A,
            command_id=uuid4(),
            authority_decision_ref="authority://decision/1",
        )


def test_timestamp_models_accept_aware_values() -> None:
    now = FixedClock().now()
    receipt = ActivationReceipt(
        command_id=uuid4(),
        previous_version=None,
        active_version="2.1.0",
        constitution_hash=HEX_A,
        activated_at=now,
        repository_version=1,
    )
    event = ConstitutionAuditEvent(
        event_id=uuid4(),
        event_type="CONSTITUTION_ACTIVATED",
        occurred_at=now,
        principal_id="governance-owner",
        target_version="2.1.0",
        constitution_hash=HEX_A,
        command_id=receipt.command_id,
        authority_decision_ref="authority://decision/1",
    )

    assert receipt.activated_at == now
    assert event.occurred_at == now
