class DomainError(ValueError):
    """Base error for deterministic domain invariant violations."""


class InvariantViolation(DomainError):
    pass


class IllegalTransition(DomainError):
    pass


class StaleVersion(DomainError):
    pass


class BudgetExceeded(DomainError):
    pass


class InvalidPlan(DomainError):
    pass
