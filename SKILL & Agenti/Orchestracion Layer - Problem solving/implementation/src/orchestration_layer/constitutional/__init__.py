"""Constitutional Kernel public API."""

from .errors import (
    ActivationConflict,
    ActivationDenied,
    ConstitutionError,
    ConstitutionIntegrityError,
    ConstitutionNotFound,
    ConstitutionSignatureError,
    InvalidBinding,
)
from .kernel import ConstitutionalKernel
from .models import (
    ActivationCommand,
    ActivationReceipt,
    BoundaryDecision,
    BoundaryDisposition,
    BoundaryRule,
    ConstitutionAuditEvent,
    ConstitutionBinding,
    ConstitutionDiff,
    ConstitutionPayload,
    IdentityAnchor,
    PrecedenceDecision,
    PrecedenceDomain,
    PrecedenceRule,
    Principle,
    RuleCandidate,
    SignedConstitutionBundle,
)
from .ports import (
    ActivationAuthorityVerifier,
    Clock,
    ConstitutionRepository,
    SignatureVerifier,
)
from .signing import Ed25519TrustStoreVerifier

__all__ = [
    "ActivationAuthorityVerifier",
    "ActivationCommand",
    "ActivationConflict",
    "ActivationDenied",
    "ActivationReceipt",
    "BoundaryDecision",
    "BoundaryDisposition",
    "BoundaryRule",
    "Clock",
    "ConstitutionAuditEvent",
    "ConstitutionBinding",
    "ConstitutionDiff",
    "ConstitutionError",
    "ConstitutionIntegrityError",
    "ConstitutionNotFound",
    "ConstitutionPayload",
    "ConstitutionRepository",
    "ConstitutionSignatureError",
    "ConstitutionalKernel",
    "Ed25519TrustStoreVerifier",
    "IdentityAnchor",
    "InvalidBinding",
    "PrecedenceDecision",
    "PrecedenceDomain",
    "PrecedenceRule",
    "Principle",
    "RuleCandidate",
    "SignatureVerifier",
    "SignedConstitutionBundle",
]
