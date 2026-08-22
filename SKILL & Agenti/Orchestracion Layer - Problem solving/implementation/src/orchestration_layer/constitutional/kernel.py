"""Fail-closed implementation of architecture functions A01-A08."""

from __future__ import annotations

import base64
import hmac
from collections.abc import Sequence
from datetime import datetime
from uuid import UUID, uuid4

from .canonical import canonical_bytes, sha256_hex
from .errors import (
    ActivationDenied,
    ConstitutionIntegrityError,
    ConstitutionNotFound,
    ConstitutionSignatureError,
    InvalidBinding,
)
from .models import (
    ActivationCommand,
    ActivationReceipt,
    BoundaryDecision,
    BoundaryDisposition,
    ConstitutionAuditEvent,
    ConstitutionBinding,
    ConstitutionDiff,
    IdentityAnchor,
    PrecedenceDecision,
    RuleCandidate,
    SignedConstitutionBundle,
)
from .ports import (
    ActivationAuthorityVerifier,
    Clock,
    ConstitutionRepository,
    SignatureVerifier,
)


class ConstitutionalKernel:
    """Constitutional control surface.

    The class proposes no domain answer and executes no external case action. It only
    validates and binds constitutional state, resolves explicit precedence/boundaries,
    and requests atomic activation through controlled ports.
    """

    def __init__(
        self,
        *,
        repository: ConstitutionRepository,
        signature_verifier: SignatureVerifier,
        authority_verifier: ActivationAuthorityVerifier,
        clock: Clock,
    ) -> None:
        self._repository = repository
        self._signature_verifier = signature_verifier
        self._authority_verifier = authority_verifier
        self._clock = clock

    def _verify_bundle(self, bundle: SignedConstitutionBundle) -> bytes:
        payload_bytes = canonical_bytes(bundle.payload)
        actual_hash = sha256_hex(payload_bytes)
        if not hmac.compare_digest(actual_hash, bundle.payload_hash):
            raise ConstitutionIntegrityError("constitution payload hash mismatch")

        signature = base64.b64decode(bundle.signature_b64, validate=True)
        if not self._signature_verifier.verify(
            key_id=bundle.key_id,
            message=payload_bytes,
            signature=signature,
        ):
            raise ConstitutionSignatureError("constitution signature verification failed")
        return payload_bytes

    async def load_constitution(self, version: str) -> SignedConstitutionBundle:
        """A01 — load an exact version and verify digest/signature before use."""

        bundle = await self._repository.load(version)
        if bundle is None:
            raise ConstitutionNotFound(f"constitution version {version!r} not found")
        if bundle.payload.constitution_version != version:
            raise ConstitutionIntegrityError("repository version and payload version differ")
        self._verify_bundle(bundle)
        return bundle

    def bind_constitution_to_case(
        self,
        *,
        case_id: UUID,
        bundle: SignedConstitutionBundle,
        phase_policy_hash: str,
        scope_hash: str,
    ) -> ConstitutionBinding:
        """A02 — create an immutable case binding to exact content and policies."""

        self._verify_bundle(bundle)
        bound_at = self._aware_now()
        binding_id = uuid4()
        material = {
            "binding_id": str(binding_id),
            "case_id": str(case_id),
            "constitution_version": bundle.payload.constitution_version,
            "constitution_hash": bundle.payload_hash,
            "phase_policy_hash": phase_policy_hash,
            "scope_hash": scope_hash,
            "bound_at": bound_at.isoformat(),
        }
        return ConstitutionBinding(
            binding_id=binding_id,
            case_id=case_id,
            constitution_version=bundle.payload.constitution_version,
            constitution_hash=bundle.payload_hash,
            phase_policy_hash=phase_policy_hash,
            scope_hash=scope_hash,
            bound_at=bound_at,
            binding_hash=sha256_hex(canonical_bytes(material)),
        )

    async def verify_constitution_binding(self, binding: ConstitutionBinding) -> bool:
        """A03 — reload exact content and fail if any binding material changed."""

        bundle = await self.load_constitution(binding.constitution_version)
        self._assert_binding_matches_bundle(binding, bundle)
        return True

    @staticmethod
    def _assert_binding_matches_bundle(
        binding: ConstitutionBinding,
        bundle: SignedConstitutionBundle,
    ) -> None:
        if not hmac.compare_digest(bundle.payload_hash, binding.constitution_hash):
            raise InvalidBinding("bound constitution hash no longer matches exact version")

        material = {
            "binding_id": str(binding.binding_id),
            "case_id": str(binding.case_id),
            "constitution_version": binding.constitution_version,
            "constitution_hash": binding.constitution_hash,
            "phase_policy_hash": binding.phase_policy_hash,
            "scope_hash": binding.scope_hash,
            "bound_at": binding.bound_at.isoformat(),
        }
        expected_hash = sha256_hex(canonical_bytes(material))
        if not hmac.compare_digest(expected_hash, binding.binding_hash):
            raise InvalidBinding("binding hash mismatch")

    def resolve_rule_precedence(
        self,
        *,
        bundle: SignedConstitutionBundle,
        candidates: Sequence[RuleCandidate],
    ) -> PrecedenceDecision:
        """A04 — deterministically select the constitutionally higher rule."""

        self._verify_bundle(bundle)
        if not candidates:
            raise ValueError("at least one rule candidate is required")
        ranks = {item.domain: item.rank for item in bundle.payload.precedence}
        missing = {item.domain for item in candidates if item.domain not in ranks}
        if missing:
            raise ConstitutionIntegrityError(f"unranked precedence domains: {sorted(missing)}")

        winning_rank = min(ranks[item.domain] for item in candidates)
        winners = [item for item in candidates if ranks[item.domain] == winning_rank]
        if len(winners) != 1:
            raise ConstitutionIntegrityError("same-rank rules require an external specific policy")
        winner = winners[0]
        return PrecedenceDecision(
            winner=winner,
            rejected_candidate_ids=tuple(
                item.candidate_id for item in candidates if item.candidate_id != winner.candidate_id
            ),
            winning_rank=winning_rank,
            constitution_hash=bundle.payload_hash,
            reason=f"{winner.domain.value} has constitutional precedence rank {winning_rank}",
        )

    def assert_layer_boundary(
        self,
        *,
        bundle: SignedConstitutionBundle,
        capability: str,
    ) -> BoundaryDecision:
        """A05 — return a conservative typed boundary decision."""

        self._verify_bundle(bundle)
        match = next(
            (item for item in bundle.payload.boundaries if item.capability == capability),
            None,
        )
        if match is None:
            return BoundaryDecision(
                capability=capability,
                disposition=BoundaryDisposition.OUT_OF_LAYER,
                target_layer="UNRESOLVED_CAPABILITY",
                requires_handoff=True,
                constitution_hash=bundle.payload_hash,
                reason_code="UNREGISTERED_CAPABILITY",
                reason="Unknown capability fails closed and requires a governed handoff decision",
            )
        return BoundaryDecision(
            capability=match.capability,
            disposition=match.disposition,
            target_layer=match.target_layer,
            requires_handoff=match.disposition is BoundaryDisposition.OUT_OF_LAYER,
            constitution_hash=bundle.payload_hash,
            reason_code="REGISTERED_BOUNDARY",
            reason=match.reason,
        )

    async def render_identity_anchor(self, binding: ConstitutionBinding) -> IdentityAnchor:
        """A06 — expose identity only through a verified immutable case binding."""

        bundle = await self.load_constitution(binding.constitution_version)
        self._assert_binding_matches_bundle(binding, bundle)
        return bundle.payload.identity

    async def diff_constitution_versions(
        self,
        from_version: str,
        to_version: str,
    ) -> ConstitutionDiff:
        """A07 — compute a structural diff without activation side effects."""

        before = await self.load_constitution(from_version)
        after = await self.load_constitution(to_version)
        before_principles = {item.principle_id: item for item in before.payload.principles}
        after_principles = {item.principle_id: item for item in after.payload.principles}
        changed_principles = tuple(
            item_id
            for item_id in range(10)
            if before_principles[item_id] != after_principles[item_id]
        )

        before_boundaries = {item.capability: item for item in before.payload.boundaries}
        after_boundaries = {item.capability: item for item in after.payload.boundaries}
        before_names = set(before_boundaries)
        after_names = set(after_boundaries)
        return ConstitutionDiff(
            from_version=from_version,
            to_version=to_version,
            from_hash=before.payload_hash,
            to_hash=after.payload_hash,
            identity_changed=before.payload.identity != after.payload.identity,
            changed_principle_ids=changed_principles,
            added_capabilities=tuple(sorted(after_names - before_names)),
            removed_capabilities=tuple(sorted(before_names - after_names)),
            changed_capabilities=tuple(
                sorted(
                    name
                    for name in before_names & after_names
                    if before_boundaries[name] != after_boundaries[name]
                )
            ),
            precedence_changed=before.payload.precedence != after.payload.precedence,
        )

    async def activate_constitution_version(
        self,
        command: ActivationCommand,
    ) -> ActivationReceipt:
        """A08 — request independently authorized, atomic activation and audit."""

        bundle = await self.load_constitution(command.target_version)
        if command.expected_current_version is not None:
            current = tuple(int(part) for part in command.expected_current_version.split("."))
            target = tuple(int(part) for part in command.target_version.split("."))
            if target <= current:
                raise ActivationDenied(
                    "target constitution version must be newer than expected current version"
                )

        allowed = await self._authority_verifier.is_authorized(
            command=command,
            constitution_hash=bundle.payload_hash,
        )
        if not allowed:
            raise ActivationDenied("constitution activation authority denied")

        activated_at = self._aware_now()
        audit_event = ConstitutionAuditEvent(
            event_id=uuid4(),
            event_type="constitution.version.activated",
            occurred_at=activated_at,
            principal_id=command.principal_id,
            target_version=command.target_version,
            constitution_hash=bundle.payload_hash,
            command_id=command.command_id,
            authority_decision_ref=command.authority_decision_ref,
        )
        return await self._repository.activate(
            command=command,
            constitution_hash=bundle.payload_hash,
            activated_at=activated_at,
            audit_event=audit_event,
        )

    def _aware_now(self) -> datetime:
        value = self._clock.now()
        if value.tzinfo is None or value.utcoffset() is None:
            raise ConstitutionIntegrityError("clock returned a naive timestamp")
        return value
