"""Typed, fail-closed Constitutional Kernel errors."""


class ConstitutionError(Exception):
    """Base class for errors safe to map to typed application failures."""


class ConstitutionNotFound(ConstitutionError):
    """The requested constitution version does not exist."""


class ConstitutionIntegrityError(ConstitutionError):
    """Canonical content and the declared digest do not match."""


class ConstitutionSignatureError(ConstitutionError):
    """The signature or signing identity cannot be verified."""


class InvalidBinding(ConstitutionError):
    """A case binding is absent, stale or inconsistent with its constitution."""


class ActivationDenied(ConstitutionError):
    """Independent authority or a migration prerequisite denied activation."""


class ActivationConflict(ConstitutionError):
    """Atomic activation lost a compare-and-swap race."""
