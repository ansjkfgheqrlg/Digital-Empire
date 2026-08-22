#!/usr/bin/env python3
"""Verify a quarantined M3 signer/trust response without handling private keys.

Normal mode is pinned to the exact NERVE-SOLVE v2.2 proposal and M1/M2 evidence.
Self-test mode uses the RFC 8032 public test vector and never generates, loads, or
persists private-key material.
"""

from __future__ import annotations

import argparse
import base64
import binascii
import hashlib
import json
from datetime import datetime
from pathlib import Path
from typing import Any

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_RESPONSE = ROOT / "incoming/NS-A-v22-M3-signer-trust-response.json"
EXPECTED_FILES = {
    "payload_file_sha256": (
        ROOT / "proposals/constitution/nerve-solve-2.2.0.payload.proposed.json",
        "9dd23985e37961cefcb08fa11ac84cd4d84775f9358856692a869bc2323415d1",
    ),
    "architecture_sha256": (
        ROOT.parent / "ARCHITETTURA_DEFINITIVA_NERVE-SOLVE_Orchestration_Layer_v2.2.md",
        "d7862b9407ee38e469cfb0d1d1776dd1ee60223bc84eae405ae6546db28cad5b",
    ),
    "system_prompt_sha256": (
        ROOT.parent / "SYSTEM_PROMPT_Orchestration_Layer_Architect_v2.2.md",
        "214e4145dfa0cd2595a414ca58faca10ce5ef54eef5a9ebad88c86a77f9a05f2",
    ),
    "m1_decision_sha256": (
        ROOT / "decisions/NS-A-v22-M1-AUTHORITY-DECISION-2026-08-20.json",
        "3c1bbc095ffc8bf120a9dc3bc289da309c5d72e8c98f06d1b185b6f493cc3fc9",
    ),
    "m2_gate_sha256": (
        ROOT / "evidence/NS-A-v22-M2-GATE-CLOSURE-2026-08-20.log",
        "b6d58ff4d9cd5f70fff0b424bbc28ab9aa73406051f89578b9a7813246d3739a",
    ),
}
EXPECTED_CANONICAL_PAYLOAD = "a7d3d32d41eb22ae2dd02ae5297be1660e8edb9a701cd5e6f641148b345ade4d"
EXPECTED_M1_REFERENCE = "NS-A-v22-M1-DECISION-2026-08-20-001"
FORBIDDEN_KEY_FRAGMENTS = {
    "private_key",
    "privatekey",
    "secret_key",
    "secretkey",
    "signing_seed",
    "seed_phrase",
    "mnemonic",
    "password",
}
FORBIDDEN_VALUE_MARKERS = {
    "-----BEGIN PRIVATE KEY-----",
    "-----BEGIN OPENSSH PRIVATE KEY-----",
    "-----BEGIN ENCRYPTED PRIVATE KEY-----",
}
NON_AUTHORIZATIONS = {
    "activation",
    "deployment",
    "active_lock_change",
    "case_migration",
    "component_b_start",
    "layer_2_start",
    "layer_3_start",
}


class VerificationFailure(ValueError):
    """Fail-closed M3 response error."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise VerificationFailure(message)


def require_dict(value: object, label: str) -> dict[str, Any]:
    require(isinstance(value, dict), f"{label} must be an object")
    return value


def exact_keys(value: dict[str, Any], expected: set[str], label: str) -> None:
    actual = set(value)
    require(
        actual == expected,
        f"{label} keys mismatch: missing={sorted(expected - actual)}, "
        f"extra={sorted(actual - expected)}",
    )


def nonempty_text(value: object, label: str) -> str:
    require(isinstance(value, str) and bool(value.strip()), f"{label} must be non-empty text")
    return value


def aware_timestamp(value: object, label: str) -> None:
    text = nonempty_text(value, label)
    try:
        parsed = datetime.fromisoformat(text)
    except ValueError as exc:
        raise VerificationFailure(f"{label} is not ISO-8601: {exc}") from exc
    require(parsed.tzinfo is not None, f"{label} must include timezone")


def file_digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_payload_bytes() -> bytes:
    path = EXPECTED_FILES["payload_file_sha256"][0]
    payload = json.loads(path.read_text(encoding="utf-8"))
    return json.dumps(
        payload,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    ).encode("utf-8")


def decode_b64(value: object, label: str) -> bytes:
    text = nonempty_text(value, label)
    try:
        return base64.b64decode(text, validate=True)
    except (binascii.Error, ValueError) as exc:
        raise VerificationFailure(f"{label} is not strict base64") from exc


def reject_private_material(value: object, path: str = "response") -> None:
    if isinstance(value, dict):
        for key, item in value.items():
            normalized = key.lower().replace("-", "_").replace(" ", "_")
            if any(fragment in normalized for fragment in FORBIDDEN_KEY_FRAGMENTS):
                raise VerificationFailure(
                    f"forbidden secret/private-key shaped field at {path}.{key}"
                )
            reject_private_material(item, f"{path}.{key}")
    elif isinstance(value, list):
        for index, item in enumerate(value):
            reject_private_material(item, f"{path}[{index}]")
    elif isinstance(value, str):
        upper = value.upper()
        if any(marker in upper for marker in FORBIDDEN_VALUE_MARKERS):
            raise VerificationFailure(f"forbidden private-key material at {path}")


def verify_file_bindings(provenance: dict[str, Any]) -> None:
    for field, (path, expected) in EXPECTED_FILES.items():
        require(file_digest(path) == expected, f"local artifact drift: {path}")
        require(provenance[field] == expected, f"provenance digest mismatch: {field}")


def verify_response(response: object) -> None:
    reject_private_material(response)
    record = require_dict(response, "response")
    exact_keys(
        record,
        {
            "schema_version",
            "response_reference",
            "response_status",
            "signer",
            "trust_approval",
            "signature",
            "provenance",
            "independent_verification",
            "explicit_non_authorizations",
        },
        "response",
    )
    require(record["schema_version"] == "1.0", "unsupported response schema")
    nonempty_text(record["response_reference"], "response_reference")
    require(record["response_status"] == "M3_SIGNED_CANDIDATE", "wrong response status")

    signer = require_dict(record["signer"], "signer")
    exact_keys(
        signer,
        {
            "identity",
            "governed_role",
            "authorization_reference",
            "separation_attestation",
        },
        "signer",
    )
    signer_identity = nonempty_text(signer["identity"], "signer.identity")
    require(
        signer["governed_role"] == "SEPARATE_CONSTITUTION_SIGNER",
        "wrong signer role",
    )
    nonempty_text(signer["authorization_reference"], "signer.authorization_reference")
    require(signer["separation_attestation"] is True, "signer separation not attested")
    require(
        signer_identity not in {"NERVE-SOLVE user", "NERVE-SOLVE implementation agent"},
        "signer identity is not separated from classification/implementation",
    )

    trust = require_dict(record["trust_approval"], "trust_approval")
    exact_keys(
        trust,
        {
            "approver_identity",
            "governed_role",
            "approval_reference",
            "key_id",
            "algorithm",
            "public_key_b64",
            "public_key_sha256",
            "status",
            "revoked",
            "revocation_authority",
            "revocation_status_reference",
        },
        "trust_approval",
    )
    trust_identity = nonempty_text(trust["approver_identity"], "trust_approval.approver_identity")
    require(
        trust["governed_role"] == "CONSTITUTION_TRUST_AUTHORITY",
        "wrong trust approver role",
    )
    nonempty_text(trust["approval_reference"], "trust_approval.approval_reference")
    key_id = nonempty_text(trust["key_id"], "trust_approval.key_id")
    require(trust["algorithm"] == "Ed25519", "unapproved trust algorithm")
    require(trust["status"] == "APPROVED", "trust root is not approved")
    require(trust["revoked"] is False, "signing key is revoked")
    nonempty_text(trust["revocation_authority"], "trust_approval.revocation_authority")
    nonempty_text(
        trust["revocation_status_reference"],
        "trust_approval.revocation_status_reference",
    )

    signature = require_dict(record["signature"], "signature")
    exact_keys(
        signature,
        {
            "key_id",
            "algorithm",
            "signed_content",
            "canonical_payload_sha256",
            "value_b64",
        },
        "signature",
    )
    require(signature["key_id"] == key_id, "signature/trust key_id mismatch")
    require(signature["algorithm"] == "Ed25519", "unapproved signature algorithm")
    require(
        signature["signed_content"] == "CANONICAL_CONSTITUTION_PAYLOAD_JSON",
        "wrong signed-content contract",
    )
    require(
        signature["canonical_payload_sha256"] == EXPECTED_CANONICAL_PAYLOAD,
        "signature canonical digest mismatch",
    )

    provenance = require_dict(record["provenance"], "provenance")
    exact_keys(
        provenance,
        {
            "payload_file_sha256",
            "architecture_sha256",
            "system_prompt_sha256",
            "m1_decision_reference",
            "m1_decision_sha256",
            "m2_gate_sha256",
            "ceremony_reference",
            "signed_at",
        },
        "provenance",
    )
    verify_file_bindings(provenance)
    require(
        provenance["m1_decision_reference"] == EXPECTED_M1_REFERENCE,
        "M1 decision reference mismatch",
    )
    nonempty_text(provenance["ceremony_reference"], "provenance.ceremony_reference")
    aware_timestamp(provenance["signed_at"], "provenance.signed_at")

    independent = require_dict(record["independent_verification"], "independent_verification")
    exact_keys(
        independent,
        {
            "verifier_identity",
            "governed_role",
            "verification_reference",
            "verified_at",
        },
        "independent_verification",
    )
    verifier_identity = nonempty_text(
        independent["verifier_identity"],
        "independent_verification.verifier_identity",
    )
    require(
        independent["governed_role"] == "INDEPENDENT_SIGNATURE_VERIFIER",
        "wrong independent-verifier role",
    )
    nonempty_text(
        independent["verification_reference"],
        "independent_verification.verification_reference",
    )
    aware_timestamp(independent["verified_at"], "independent_verification.verified_at")
    require(
        len({signer_identity, trust_identity, verifier_identity}) == 3,
        "signer, trust approver and independent verifier identities must be distinct",
    )

    exclusions = require_dict(
        record["explicit_non_authorizations"],
        "explicit_non_authorizations",
    )
    exact_keys(exclusions, NON_AUTHORIZATIONS, "explicit_non_authorizations")
    require(
        all(value is False for value in exclusions.values()),
        "M3 response contains a forbidden authorization",
    )

    message = canonical_payload_bytes()
    require(
        hashlib.sha256(message).hexdigest() == EXPECTED_CANONICAL_PAYLOAD,
        "local canonical payload digest drift",
    )
    public_key = decode_b64(trust["public_key_b64"], "trust_approval.public_key_b64")
    require(len(public_key) == 32, "Ed25519 public key must be 32 bytes")
    require(
        hashlib.sha256(public_key).hexdigest() == trust["public_key_sha256"],
        "public-key digest mismatch",
    )
    signature_bytes = decode_b64(signature["value_b64"], "signature.value_b64")
    require(len(signature_bytes) == 64, "Ed25519 signature must be 64 bytes")
    try:
        Ed25519PublicKey.from_public_bytes(public_key).verify(signature_bytes, message)
    except (InvalidSignature, ValueError) as exc:
        raise VerificationFailure("Ed25519 signature verification failed") from exc


def self_test() -> None:
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
    verifier = Ed25519PublicKey.from_public_bytes(public_key)
    verifier.verify(signature, b"")
    print("PASS: RFC 8032 public vector verified")
    try:
        verifier.verify(signature, b"tampered")
    except InvalidSignature:
        print("PASS: tampered message rejected")
    else:
        raise VerificationFailure("tampered RFC 8032 message was accepted")
    print("PRIVATE_KEY_MATERIAL=NOT_USED")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--response", type=Path, default=DEFAULT_RESPONSE)
    parser.add_argument("--self-test", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        if args.self_test:
            self_test()
            return 0
        if not args.response.is_file():
            print(f"BLOCKED: external M3 response not supplied: {args.response}")
            print("M3=OPEN")
            print("V22=UNSIGNED_UNTRUSTED_INACTIVE")
            return 2
        response = json.loads(args.response.read_text(encoding="utf-8"))
        verify_response(response)
    except (VerificationFailure, json.JSONDecodeError, OSError) as exc:
        print(f"FAIL: {exc}")
        print("M3=REJECTED")
        print("V22=UNSIGNED_UNTRUSTED_INACTIVE")
        return 1
    print("PASS: M3 signer/trust response and Ed25519 signature verified")
    print("M3=PASS_CANDIDATE_EVIDENCE")
    print("V22=SIGNED_CANDIDATE_NOT_ACTIVE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
