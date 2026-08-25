from __future__ import annotations

from dataclasses import dataclass

from .budget import BudgetAmount
from .errors import InvariantViolation
from .side_effect import SideEffectContract


ALLOWED_ROLES = {"planner", "implementer", "critic", "gate", "compensator"}


@dataclass(frozen=True)
class TaskSpec:
    task_id: str
    role: str
    objective: str
    depends_on: tuple[str, ...]
    completion_criteria: tuple[str, ...]
    capabilities: tuple[str, ...]
    budget: BudgetAmount
    side_effect: SideEffectContract

    def __post_init__(self) -> None:
        if not self.task_id.strip():
            raise InvariantViolation("Task id is required")
        if self.role not in ALLOWED_ROLES:
            raise InvariantViolation(f"Unsupported task role: {self.role}")
        if not self.objective.strip() or len(self.objective) > 8000:
            raise InvariantViolation("Task objective must contain 1..8000 characters")
        if not self.completion_criteria:
            raise InvariantViolation("Task requires completion criteria")
        if len(set(self.capabilities)) != len(self.capabilities):
            raise InvariantViolation("Task capabilities must be unique")
        if self.task_id in self.depends_on:
            raise InvariantViolation("Task cannot depend on itself")
