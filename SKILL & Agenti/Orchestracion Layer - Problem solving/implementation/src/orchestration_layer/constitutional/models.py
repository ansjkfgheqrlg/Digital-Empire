"""Strict immutable contracts for Component A — Constitutional Kernel."""

from __future__ import annotations

import base64
from datetime import datetime
from enum import StrEnum
from typing import Annotated, Self
from uuid import UUID

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    StringConstraints,
    field_validator,
    model_validator,
)

Hash256 = Annotated[str, StringConstraints(pattern=r"^[0-9a-f]{64}$")]
NonEmpty = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]
Version = Annotated[str, StringConstraints(pattern=r"^[0-9]+\.[0-9]+\.[0-9]+$")]
CapabilityName = Annotated[
    str,
    StringConstraints(pattern=r"^[a-z][a-z0-9_.:-]{2,127}$"),
]


class StrictFrozenModel(BaseModel):
    """No coercion, no unknown fields and no mutation after validation."""

    model_config = ConfigDict(strict=True, frozen=True, extra="forbid")


class PrecedenceDomain(StrEnum):
    SAFETY = "SAFETY"
    LEGALITY = "LEGALITY"
    AUTHORITY = "AUTHORITY"
    INTEGRITY = "INTEGRITY"
    EPISTEMIC_TRUTH = "EPISTEMIC_TRUTH"
    SCOPE = "SCOPE"
    REVERSIBILITY = "REVERSIBILITY"
    UTILITY = "UTILITY"
    IMPLEMENTABILITY = "IMPLEMENTABILITY"
    COST_LATENCY = "COST_LATENCY"
    STYLE = "STYLE"


class BoundaryDisposition(StrEnum):
    IN_LAYER = "IN_LAYER"
    OUT_OF_LAYER = "OUT_OF_LAYER"


class IdentityAnchor(StrictFrozenModel):
    name: NonEmpty
    first_person_statement: NonEmpty
    not_a: tuple[NonEmpty, ...] = Field(min_length=1)


class Principle(StrictFrozenModel):
    principle_id: int = Field(ge=0, le=9)
    statement: Annotated[
        str,
        StringConstraints(pattern="^IO [A-ZÀ-ÖØ-Þ0-9 '\\u2019.-]+\\.$"),
    ]
    falsifier: NonEmpty


class PrecedenceRule(StrictFrozenModel):
    rank: int = Field(ge=1)
    domain: PrecedenceDomain
    rationale: NonEmpty


class BoundaryRule(StrictFrozenModel):
    capability: CapabilityName
    disposition: BoundaryDisposition
    target_layer: NonEmpty | None = None
    reason: NonEmpty

    @model_validator(mode="after")
    def out_of_layer_requires_target(self) -> Self:
        if self.disposition is BoundaryDisposition.OUT_OF_LAYER and self.target_layer is None:
            raise ValueError("OUT_OF_LAYER boundary requires target_layer")
        if self.disposition is BoundaryDisposition.IN_LAYER and self.target_layer is not None:
            raise ValueError("IN_LAYER boundary cannot nominate target_layer")
        return self


class ConstitutionPayload(StrictFrozenModel):
    schema_version: Annotated[str, StringConstraints(pattern=r"^1\.[0-9]+$")]
    constitution_version: Version
    issued_at: datetime
    identity: IdentityAnchor
    principles: tuple[Principle, ...] = Field(min_length=10, max_length=10)
    precedence: tuple[PrecedenceRule, ...] = Field(min_length=1)
    boundaries: tuple[BoundaryRule, ...] = Field(min_length=1)

    @field_validator("issued_at")
    @classmethod
    def timestamp_must_be_aware(cls, value: datetime) -> datetime:
        if value.tzinfo is None or value.utcoffset() is None:
            raise ValueError("issued_at must be timezone-aware")
        return value

    @model_validator(mode="after")
    def validate_constitution_invariants(self) -> Self:
        principle_ids = [item.principle_id for item in self.principles]
        if principle_ids != list(range(10)):
            raise ValueError("principles must be ordered exactly 0..9")

        ranks = [item.rank for item in self.precedence]
        if sorted(ranks) != list(range(1, len(ranks) + 1)) or ranks != sorted(ranks):
            raise ValueError("precedence ranks must be ordered and contiguous from 1")
        domains = [item.domain for item in self.precedence]
        if len(domains) != len(set(domains)):
            raise ValueError("precedence domains must be unique")

        capabilities = [item.capability for item in self.boundaries]
        if len(capabilities) != len(set(capabilities)):
            raise ValueError("boundary capabilities must be unique")

        required_top = {
            PrecedenceDomain.SAFETY,
            PrecedenceDomain.LEGALITY,
            PrecedenceDomain.AUTHORITY,
            PrecedenceDomain.INTEGRITY,
        }
        top_four = {item.domain for item in self.precedence[:4]}
        if top_four != required_top:
            raise ValueError("top four precedence domains must preserve constitutional safety")
        return self


class SignedConstitutionBundle(StrictFrozenModel):
    payload: ConstitutionPayload
    payload_hash: Hash256
    key_id: NonEmpty
    signature_b64: NonEmpty

    @field_validator("signature_b64")
    @classmethod
    def signature_must_be_canonical_base64(cls, value: str) -> str:
        try:
            decoded = base64.b64decode(value, validate=True)
        except ValueError as exc:
            raise ValueError("signature_b64 is not valid base64") from exc
        if len(decoded) != 64 or base64.b64encode(decoded).decode("ascii") != value:
            raise ValueError("signature_b64 must be canonical Ed25519 signature bytes")
        return value


class ConstitutionBinding(StrictFrozenModel):
    binding_id: UUID
    case_id: UUID
    constitution_version: Version
    constitution_hash: Hash256
    phase_policy_hash: Hash256
    scope_hash: Hash256
    bound_at: datetime
    binding_hash: Hash256

    @field_validator("bound_at")
    @classmethod
    def bound_timestamp_must_be_aware(cls, value: datetime) -> datetime:
        if value.tzinfo is None or value.utcoffset() is None:
            raise ValueError("bound_at must be timezone-aware")
        return value


class RuleCandidate(StrictFrozenModel):
    candidate_id: NonEmpty
    domain: PrecedenceDomain
    statement: NonEmpty


class PrecedenceDecision(StrictFrozenModel):
    winner: RuleCandidate
    rejected_candidate_ids: tuple[NonEmpty, ...]
    winning_rank: int = Field(ge=1)
    constitution_hash: Hash256
    reason: NonEmpty


class BoundaryDecision(StrictFrozenModel):
    capability: CapabilityName
    disposition: BoundaryDisposition
    target_layer: NonEmpty | None
    requires_handoff: bool
    constitution_hash: Hash256
    reason_code: NonEmpty
    reason: NonEmpty


class ConstitutionDiff(StrictFrozenModel):
    from_version: Version
    to_version: Version
    from_hash: Hash256
    to_hash: Hash256
    identity_changed: bool
    changed_principle_ids: tuple[int, ...]
    added_capabilities: tuple[CapabilityName, ...]
    removed_capabilities: tuple[CapabilityName, ...]
    changed_capabilities: tuple[CapabilityName, ...]
    precedence_changed: bool


class ActivationCommand(StrictFrozenModel):
    command_id: UUID
    principal_id: NonEmpty
    authority_decision_ref: NonEmpty
    expected_current_version: Version | None
    target_version: Version
    migration_plan_ref: NonEmpty
    requested_at: datetime

    @field_validator("requested_at")
    @classmethod
    def requested_timestamp_must_be_aware(cls, value: datetime) -> datetime:
        if value.tzinfo is None or value.utcoffset() is None:
            raise ValueError("requested_at must be timezone-aware")
        return value


class ActivationReceipt(StrictFrozenModel):
    command_id: UUID
    previous_version: Version | None
    active_version: Version
    constitution_hash: Hash256
    activated_at: datetime
    repository_version: int = Field(ge=1)

    @field_validator("activated_at")
    @classmethod
    def activated_timestamp_must_be_aware(cls, value: datetime) -> datetime:
        if value.tzinfo is None or value.utcoffset() is None:
            raise ValueError("activated_at must be timezone-aware")
        return value


class ConstitutionAuditEvent(StrictFrozenModel):
    event_id: UUID
    event_type: NonEmpty
    occurred_at: datetime
    principal_id: NonEmpty
    target_version: Version
    constitution_hash: Hash256
    command_id: UUID
    authority_decision_ref: NonEmpty

    @field_validator("occurred_at")
    @classmethod
    def event_timestamp_must_be_aware(cls, value: datetime) -> datetime:
        if value.tzinfo is None or value.utcoffset() is None:
            raise ValueError("occurred_at must be timezone-aware")
        return value
