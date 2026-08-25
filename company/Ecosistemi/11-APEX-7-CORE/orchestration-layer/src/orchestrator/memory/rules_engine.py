from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class Rule:
    rule_id: str
    category: str
    severity: str
    statement: str
    enforcement: str


@dataclass(frozen=True)
class RuleEvaluationResult:
    rule_id: str
    passed: bool
    message: str


class RulesEngine:
    def __init__(self, rules_dir: Path):
        self.rules_dir = rules_dir
        self._rules: dict[str, Rule] = {}
        self.load_rules()

    def load_rules(self) -> None:
        if not self.rules_dir.exists():
            return
        for file in self.rules_dir.glob("*.json"):
            data = json.loads(file.read_text(encoding="utf-8"))
            category = data.get("category", file.stem)
            for item in data.get("rules", []):
                rule = Rule(
                    rule_id=item["id"],
                    category=category,
                    severity=item.get("severity", "HIGH"),
                    statement=item["statement"],
                    enforcement=item.get("enforcement", "BLOCK"),
                )
                self._rules[rule.rule_id] = rule

    def evaluate_context(self, context: dict[str, Any]) -> list[RuleEvaluationResult]:
        results: list[RuleEvaluationResult] = []

        # R-001: correlation_id or workflow_id required
        if "R-001" in self._rules:
            has_id = bool(context.get("workflow_id") or context.get("correlation_id"))
            results.append(
                RuleEvaluationResult(
                    "R-001",
                    has_id,
                    "Workflow or correlation ID present" if has_id else "Missing correlation/workflow ID",
                )
            )

        # R-003: idempotency_key on writes
        if "R-003" in self._rules:
            is_write = context.get("is_write", False)
            has_key = bool(context.get("idempotency_key"))
            passed = not is_write or has_key
            results.append(
                RuleEvaluationResult(
                    "R-003",
                    passed,
                    "Idempotency key present for write" if passed else "Write operation requires idempotency_key",
                )
            )

        # R-006: risk class R2/R3 requires human approval
        if "R-006" in self._rules:
            risk = context.get("risk", "R0")
            approved = context.get("human_approved", False)
            passed = risk not in ("R2", "R3") or approved
            results.append(
                RuleEvaluationResult(
                    "R-006",
                    passed,
                    "Risk approved or low" if passed else f"Risk {risk} requires human approval",
                )
            )

        return results

    def get_rule(self, rule_id: str) -> Rule | None:
        return self._rules.get(rule_id)

    def list_rules(self) -> list[Rule]:
        return list(self._rules.values())
