from __future__ import annotations

from dataclasses import dataclass

from .budget import BudgetAmount
from .errors import InvalidPlan
from .task import TaskSpec


@dataclass(frozen=True)
class Plan:
    plan_id: str
    workflow_id: str
    tasks: tuple[TaskSpec, ...]
    workflow_budget: BudgetAmount

    def __post_init__(self) -> None:
        if not self.plan_id or not self.workflow_id:
            raise InvalidPlan("Plan and workflow ids are required")
        if not 1 <= len(self.tasks) <= 6:
            raise InvalidPlan("Plan must contain 1..6 tasks including remediation")
        task_ids = [task.task_id for task in self.tasks]
        if len(task_ids) != len(set(task_ids)):
            raise InvalidPlan("Task ids must be unique")
        known = set(task_ids)
        for task in self.tasks:
            unknown = set(task.depends_on) - known
            if unknown:
                raise InvalidPlan(
                    f"Task {task.task_id} has unknown dependencies: {sorted(unknown)}"
                )
        self.topological_order()
        total = BudgetAmount.zero()
        for task in self.tasks:
            total = total + task.budget
        if not total.fits_within(self.workflow_budget):
            raise InvalidPlan("Task budgets exceed workflow budget")
        if not any(task.role == "gate" for task in self.tasks):
            raise InvalidPlan("Plan requires at least one gate task")

    def topological_order(self) -> tuple[str, ...]:
        incoming = {task.task_id: set(task.depends_on) for task in self.tasks}
        outgoing: dict[str, set[str]] = {task.task_id: set() for task in self.tasks}
        for task in self.tasks:
            for dependency in task.depends_on:
                outgoing.setdefault(dependency, set()).add(task.task_id)
        ready = sorted(task_id for task_id, dependencies in incoming.items() if not dependencies)
        result: list[str] = []
        while ready:
            current = ready.pop(0)
            result.append(current)
            for dependent in sorted(outgoing[current]):
                incoming[dependent].discard(current)
                if not incoming[dependent] and dependent not in result and dependent not in ready:
                    ready.append(dependent)
                    ready.sort()
        if len(result) != len(self.tasks):
            raise InvalidPlan("Task dependency graph contains a cycle")
        return tuple(result)

    def parallel_groups(self) -> tuple[tuple[str, ...], ...]:
        remaining = {task.task_id: set(task.depends_on) for task in self.tasks}
        completed: set[str] = set()
        groups: list[tuple[str, ...]] = []
        while remaining:
            group = tuple(sorted(task for task, deps in remaining.items() if deps <= completed))
            if not group:
                raise InvalidPlan("Task dependency graph contains a cycle")
            groups.append(group)
            completed.update(group)
            for task_id in group:
                del remaining[task_id]
        return tuple(groups)
