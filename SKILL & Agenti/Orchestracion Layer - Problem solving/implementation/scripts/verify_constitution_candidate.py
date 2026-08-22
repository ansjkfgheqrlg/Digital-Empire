#!/usr/bin/env python3
"""Verify the locked local Component A constitution candidate without signing capability."""

from __future__ import annotations

import base64
import hashlib
import json
from pathlib import Path
from typing import Any

from orchestration_layer.constitutional import (
    ConstitutionPayload,
    Ed25519TrustStoreVerifier,
    SignedConstitutionBundle,
)
from orchestration_layer.constitutional.canonical import canonical_bytes, sha256_hex

EXPECTED_ARTIFACT_STATUS = "LOCAL_TEST_CANDIDATE_NOT_ACTIVE"
EXPECTED_TRUST_STATUS = "LOCAL_TEST_ONLY_NOT_PRODUCTION_TRUST"
EXPECTED_ARCHITECTURE_SHA256 = "b04ac7d7ae6ae05dc1770062f15dde2334fb927aa9cd1ec0d41c288d819ff781"
EXPECTED_PAYLOAD_SHA256 = "66a9a215c5af4f0ed3011b6f51489170c01fb4ba09e4af8a8fc0318b850642c4"
EXPECTED_PUBLIC_KEY_SHA256 = "c713d06c64ae5dc759feb8c99a5c5ce74228d0b0fce93eeea5ec470fbc66a6bc"
EXPECTED_KEY_ID = "local-test-component-a-2026-08-13"
EXPECTED_CONSTITUTION_VERSION = "2.1.0"
LOCK_RELATIVE_PATH = Path("config/constitutions/nerve-solve-2.1.0.lock.json")
EXPECTED_PATHS = {
    "architecture": "../ARCHITETTURA_DEFINITIVA_NERVE-SOLVE_Orchestration_Layer_v2.1.md",
    "payload": "config/constitutions/nerve-solve-2.1.0.payload.json",
    "bundle": "config/constitutions/nerve-solve-2.1.0.bundle.json",
    "trust_store": "config/trust/constitutional-test-roots.json",
}


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_object(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise TypeError(f"{path} must contain a JSON object")
    return value


def require_equal(actual: object, expected: object, label: str) -> None:
    if actual != expected:
        raise ValueError(f"{label} mismatch: expected {expected!r}, got {actual!r}")


def nested_object(parent: dict[str, Any], key: str) -> dict[str, Any]:
    value = parent.get(key)
    if not isinstance(value, dict):
        raise TypeError(f"lock field {key!r} must be an object")
    return value


def resolve_locked_path(root: Path, record: dict[str, Any], label: str) -> Path:
    relative = record.get("path")
    if not isinstance(relative, str) or not relative:
        raise TypeError(f"{label}.path must be a non-empty string")
    require_equal(relative, EXPECTED_PATHS[label], f"{label}.path")
    candidate = (root / relative).resolve()
    if not candidate.is_relative_to(root.parent.resolve()):
        raise ValueError(f"{label}.path escapes the project boundary")
    return candidate


def main() -> None:
    implementation_root = Path(__file__).resolve().parents[1]
    lock = load_object(implementation_root / LOCK_RELATIVE_PATH)
    require_equal(lock.get("schema_version"), "1.0", "lock schema version")
    require_equal(lock.get("artifact_status"), EXPECTED_ARTIFACT_STATUS, "artifact status")
    require_equal(lock.get("production_activation_authorized"), False, "activation flag")
    require_equal(lock.get("private_key_persisted"), False, "private-key persistence flag")

    architecture_record = nested_object(lock, "architecture")
    payload_record = nested_object(lock, "payload")
    bundle_record = nested_object(lock, "bundle")
    trust_record = nested_object(lock, "trust_store")
    require_equal(
        architecture_record.get("sha256"),
        EXPECTED_ARCHITECTURE_SHA256,
        "pinned architecture hash",
    )
    require_equal(
        payload_record.get("canonical_sha256"),
        EXPECTED_PAYLOAD_SHA256,
        "pinned canonical payload hash",
    )
    require_equal(bundle_record.get("key_id"), EXPECTED_KEY_ID, "pinned bundle key ID")
    require_equal(
        trust_record.get("public_key_sha256"),
        EXPECTED_PUBLIC_KEY_SHA256,
        "pinned public key hash",
    )
    architecture_path = resolve_locked_path(
        implementation_root, architecture_record, "architecture"
    )
    payload_path = resolve_locked_path(implementation_root, payload_record, "payload")
    bundle_path = resolve_locked_path(implementation_root, bundle_record, "bundle")
    trust_path = resolve_locked_path(implementation_root, trust_record, "trust_store")

    for label, path, record in (
        ("architecture", architecture_path, architecture_record),
        ("payload", payload_path, payload_record),
        ("bundle", bundle_path, bundle_record),
        ("trust_store", trust_path, trust_record),
    ):
        require_equal(file_sha256(path), record.get("file_sha256", record.get("sha256")), label)

    payload = ConstitutionPayload.model_validate_json(payload_path.read_text(), strict=True)
    bundle = SignedConstitutionBundle.model_validate_json(bundle_path.read_text(), strict=True)
    require_equal(
        payload.constitution_version,
        EXPECTED_CONSTITUTION_VERSION,
        "constitution version",
    )
    require_equal(bundle.payload, payload, "detached payload")
    require_equal(
        sha256_hex(canonical_bytes(payload)), payload_record.get("canonical_sha256"), "payload"
    )
    require_equal(
        bundle.payload_hash, payload_record.get("canonical_sha256"), "bundle payload hash"
    )
    require_equal(bundle.key_id, bundle_record.get("key_id"), "bundle key ID")
    require_equal(bundle_record.get("signature_algorithm"), "Ed25519", "signature algorithm")

    trust = load_object(trust_path)
    require_equal(trust.get("status"), EXPECTED_TRUST_STATUS, "trust status")
    require_equal(trust_record.get("status"), EXPECTED_TRUST_STATUS, "locked trust status")
    keys = trust.get("keys")
    if not isinstance(keys, list) or len(keys) != 1 or not isinstance(keys[0], dict):
        raise ValueError("local trust store must contain exactly one key record")
    key_record = keys[0]
    require_equal(key_record.get("key_id"), bundle.key_id, "trusted key ID")
    require_equal(key_record.get("algorithm"), "Ed25519", "trusted key algorithm")
    encoded_key = key_record.get("public_key_b64")
    if not isinstance(encoded_key, str):
        raise TypeError("public_key_b64 must be a string")
    public_key = base64.b64decode(encoded_key, validate=True)
    require_equal(
        hashlib.sha256(public_key).hexdigest(), key_record.get("public_key_sha256"), "public key"
    )
    require_equal(
        key_record.get("public_key_sha256"),
        trust_record.get("public_key_sha256"),
        "locked public key",
    )

    verifier = Ed25519TrustStoreVerifier({bundle.key_id: public_key})
    signature = base64.b64decode(bundle.signature_b64, validate=True)
    if not verifier.verify(
        key_id=bundle.key_id,
        message=canonical_bytes(bundle.payload),
        signature=signature,
    ):
        raise ValueError("Ed25519 constitution signature verification failed")

    print(
        "PASS: locked local constitution candidate verified; "
        "production activation remains explicitly unauthorized"
    )


if __name__ == "__main__":
    main()
