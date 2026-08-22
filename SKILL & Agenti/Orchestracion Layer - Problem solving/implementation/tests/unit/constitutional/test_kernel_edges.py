from __future__ import annotations

import pytest

from orchestration_layer.constitutional.canonical import canonical_bytes, sha256_hex
from orchestration_layer.constitutional.errors import ConstitutionIntegrityError
from orchestration_layer.constitutional.models import PrecedenceDomain, RuleCandidate


def test_precedence_requires_at_least_one_candidate(signing_material, make_kernel) -> None:
    bundle, verifier = signing_material
    kernel, _, _, _ = make_kernel(bundle, verifier)

    with pytest.raises(ValueError, match="at least one rule candidate"):
        kernel.resolve_rule_precedence(bundle=bundle, candidates=())


def test_precedence_rejects_domain_absent_from_signed_table(signing_material, make_kernel) -> None:
    bundle, _verifier = signing_material
    reduced_payload = bundle.payload.model_copy(
        update={"precedence": bundle.payload.precedence[:-1]}
    )
    reduced_bundle = bundle.model_copy(
        update={
            "payload": reduced_payload,
            "payload_hash": sha256_hex(canonical_bytes(reduced_payload)),
        }
    )

    class ExactPayloadVerifier:
        def verify(self, *, key_id: str, message: bytes, signature: bytes) -> bool:
            return message == canonical_bytes(reduced_payload)

    kernel, _, _, _ = make_kernel(
        reduced_bundle,
        ExactPayloadVerifier(),  # type: ignore[arg-type]
    )
    candidate = RuleCandidate(
        candidate_id="style-only",
        domain=PrecedenceDomain.STYLE,
        statement="Prefer a stylistic convention",
    )

    with pytest.raises(ConstitutionIntegrityError, match="unranked precedence"):
        kernel.resolve_rule_precedence(bundle=reduced_bundle, candidates=(candidate,))
