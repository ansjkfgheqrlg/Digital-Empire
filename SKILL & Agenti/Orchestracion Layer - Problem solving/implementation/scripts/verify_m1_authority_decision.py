#!/usr/bin/env python3
"""Fail-closed verifier for the NS-A v2.2 M1 local authority decision.

This verifies record shape, disposition, scope, exclusions, referenced file digests,
and the canonical proposed-payload digest. It cannot independently prove the human
identity behind the Arena conversation and never upgrades the record into a
production signing identity.
"""

from __future__ import annotations

import hashlib
import json
from datetime import datetime
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
RECORD = ROOT / "decisions/NS-A-v22-M1-AUTHORITY-DECISION-2026-08-20.json"
EXPECTED_DISPOSITION = "APPROVE_AS_CONSTITUTIONAL_CHANGE"
EXPECTED_CANONICAL_PAYLOAD = "a7d3d32d41eb22ae2dd02ae5297be1660e8edb9a701cd5e6f641148b345ade4d"
EXPECTED_BOUND: dict[str, tuple[str, str]] = {
    "architecture_v2_2": (
        "../ARCHITETTURA_DEFINITIVA_NERVE-SOLVE_Orchestration_Layer_v2.2.md",
        "d7862b9407ee38e469cfb0d1d1776dd1ee60223bc84eae405ae6546db28cad5b",
    ),
    "system_prompt_v2_2": (
        "../SYSTEM_PROMPT_Orchestration_Layer_Architect_v2.2.md",
        "214e4145dfa0cd2595a414ca58faca10ce5ef54eef5a9ebad88c86a77f9a05f2",
    ),
    "proposed_payload_file": (
        "proposals/constitution/nerve-solve-2.2.0.payload.proposed.json",
        "9dd23985e37961cefcb08fa11ac84cd4d84775f9358856692a869bc2323415d1",
    ),
    "migration_plan_at_decision": (
        "plans/NS-A_MIGRATION_v2.1_TO_v2.2_PROPOSAL.md",
        "1821abb59faf4ed9a6a566e9d884ec21f5f3d61d2e589b891b940eba1c8f3c42",
    ),
    "m1_technical_recommendation": (
        "evidence/NS-A-v22-M1-TECHNICAL-RECOMMENDATION.md",
        "6c490e2c5c38fb69408a8e4a3ea2c392ea3f5963ef33b0108ca9d3065568077b",
    ),
    "m2_preparatory_report": (
        "evidence/NS-A-v22-M2-PREPARATORY-REPORT.md",
        "a4bf3ae624606617985e442bc54b0922eb42cc309b3c0e2f6049b56be0248e9c",
    ),
    "m2_comprehensive_gate": (
        "evidence/NS-A-v22-M2-PREPARATORY-COMPREHENSIVE-GATE.log",
        "a93df192bc1c9573dfcf9dd2a08c761ef9b94fa07f6d4bbbde6cabcd5998e70b",
    ),
}
EXPECTED_EXCLUSIONS = {
    "production_signature",
    "private_key_generation",
    "trust_root_approval",
    "bundle_release",
    "lock_creation",
    "activation",
    "deployment",
    "component_b_start",
    "layer_2_start",
    "layer_3_start",
}


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def require_dict(value: object, label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        fail(f"{label} must be an object")
    return value


def exact_keys(value: dict[str, Any], expected: set[str], label: str) -> None:
    actual = set(value)
    if actual != expected:
        missing = sorted(expected - actual)
        extra = sorted(actual - expected)
        fail(f"{label} keys mismatch: missing={missing}, extra={extra}")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_digest(path: Path) -> str:
    payload = json.loads(path.read_text(encoding="utf-8"))
    encoded = json.dumps(
        payload,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def main() -> None:
    record = require_dict(json.loads(RECORD.read_text(encoding="utf-8")), "record")
    exact_keys(
        record,
        {
            "schema_version",
            "decision_reference",
            "decision_timestamp",
            "decision_stage",
            "authority",
            "decision",
            "request",
            "bound_evidence",
            "canonical_payload_sha256",
            "explicit_non_authorizations",
            "attestation",
            "effects",
        },
        "record",
    )
    if record["schema_version"] != "1.0" or record["decision_stage"] != "M1":
        fail("wrong schema or stage")
    if record["decision_reference"] != "NS-A-v22-M1-DECISION-2026-08-20-001":
        fail("wrong decision reference")
    try:
        timestamp = datetime.fromisoformat(record["decision_timestamp"])
    except (TypeError, ValueError) as exc:
        fail(f"invalid decision timestamp: {exc}")
    if timestamp.tzinfo is None:
        fail("decision timestamp must include timezone")

    authority = require_dict(record["authority"], "authority")
    exact_keys(
        authority,
        {
            "identity",
            "governed_role",
            "authorization_evidence",
            "identity_assurance",
            "production_identity_verified",
        },
        "authority",
    )
    if authority["governed_role"] != "Project Owner / Constitutional Authority":
        fail("authority role is not the attested role")
    if authority["identity_assurance"] != "SELF_ATTESTED_CONVERSATION_CONTEXT":
        fail("unexpected identity-assurance level")
    if authority["production_identity_verified"] is not False:
        fail("local attestation must not claim production identity verification")

    decision = require_dict(record["decision"], "decision")
    exact_keys(decision, {"disposition", "rationale", "scope"}, "decision")
    if decision["disposition"] != EXPECTED_DISPOSITION:
        fail("decision disposition mismatch")
    if not isinstance(decision["rationale"], str) or not decision["rationale"].strip():
        fail("decision rationale is empty")
    required_scope = {
        "NERVE-SOLVE Layer 1",
        "Component A constitutional kernel",
        "constitution migration 2.1.0 to proposed 2.2.0",
        "the exact hashes bound below",
    }
    if set(decision["scope"]) != required_scope:
        fail("decision scope mismatch")

    request = require_dict(record["request"], "request")
    exact_keys(request, {"path", "sha256"}, "request")
    if request != {
        "path": "proposals/authority/NS-A-v22-M1-AUTHORITY-DECISION-REQUEST.md",
        "sha256": "473e9272313ef609e3fc02165b80c14863f2a8bb0ab3bced4ef12c8ecc423379",
    }:
        fail("request binding mismatch")
    if digest(ROOT / request["path"]) != request["sha256"]:
        fail("request artifact digest mismatch")

    bound = require_dict(record["bound_evidence"], "bound_evidence")
    exact_keys(bound, set(EXPECTED_BOUND), "bound_evidence")
    for name, (expected_path, expected_digest) in EXPECTED_BOUND.items():
        item = require_dict(bound[name], f"bound_evidence.{name}")
        exact_keys(item, {"path", "sha256"}, f"bound_evidence.{name}")
        if item != {"path": expected_path, "sha256": expected_digest}:
            fail(f"declared binding mismatch for {name}")
        if digest(ROOT / expected_path) != expected_digest:
            fail(f"artifact digest mismatch for {name}")

    proposed_payload = ROOT / EXPECTED_BOUND["proposed_payload_file"][0]
    if record["canonical_payload_sha256"] != EXPECTED_CANONICAL_PAYLOAD:
        fail("declared canonical payload digest mismatch")
    if canonical_digest(proposed_payload) != EXPECTED_CANONICAL_PAYLOAD:
        fail("computed canonical payload digest mismatch")

    exclusions = require_dict(record["explicit_non_authorizations"], "explicit_non_authorizations")
    exact_keys(exclusions, EXPECTED_EXCLUSIONS, "explicit_non_authorizations")
    if any(value is not False for value in exclusions.values()):
        fail("M1 record contains a forbidden authorization")

    attestation = require_dict(record["attestation"], "attestation")
    if attestation.get("selection") != "YES_OWNER + APPROVE":
        fail("authority selection mismatch")
    if attestation.get("cryptographic_signature_present") is not False:
        fail("record must not claim a cryptographic signature")
    if attestation.get("valid_for_local_governance_classification") is not True:
        fail("local classification attestation missing")
    if attestation.get("valid_as_production_signing_identity") is not False:
        fail("attestation must not be a production signing identity")

    effects = require_dict(record["effects"], "effects")
    if effects != {
        "m1": "PASS_LOCAL_AUTHORITY_ATTESTATION",
        "m2_may_be_reconciled": True,
        "m3_requires_separate_signer_and_trust_approval": True,
        "v2_2_remains_unsigned_untrusted_inactive": True,
    }:
        fail("decision effects mismatch")

    print("PASS: M1 authority decision record shape and all bound hashes verified")
    print(f"decision={record['decision_reference']}; disposition={EXPECTED_DISPOSITION}")
    print("identity_assurance=SELF_ATTESTED_CONVERSATION_CONTEXT")
    print("production_signing_identity=NOT_VERIFIED")
    print("M1=PASS_LOCAL_AUTHORITY_ATTESTATION")
    print("V22=UNSIGNED_UNTRUSTED_INACTIVE")


if __name__ == "__main__":
    main()
