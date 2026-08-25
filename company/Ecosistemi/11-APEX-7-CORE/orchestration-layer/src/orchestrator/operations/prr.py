from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class PrrResult:
    verdict: str
    passed: tuple[str, ...]
    blocked: tuple[dict[str, str], ...]
    warnings: tuple[str, ...]


class ProductionReadinessReview:
    """Evidence-based PRR. Missing human ownership or external evidence is NO_GO."""

    def __init__(self, root: Path):
        self.root = root

    def evaluate(self) -> PrrResult:
        config = json.loads((self.root / "operations/prr-checklist.json").read_text())
        passed: list[str] = []
        blocked: list[dict[str, str]] = []
        warnings: list[str] = []
        for criterion in config["criteria"]:
            if criterion["kind"] == "file":
                exists = (self.root / criterion["path"]).is_file()
                if exists:
                    passed.append(criterion["id"])
                else:
                    blocked.append({"id": criterion["id"], "reason": f"missing {criterion['path']}"})
            elif criterion["kind"] == "manual":
                if criterion.get("status") == "PASS":
                    passed.append(criterion["id"])
                else:
                    blocked.append({"id": criterion["id"], "reason": criterion["reason"]})
            elif criterion["kind"] == "warning":
                warnings.append(criterion["reason"])
        verdict = "GO" if not blocked else "NO_GO"
        return PrrResult(verdict, tuple(passed), tuple(blocked), tuple(warnings))

    def evaluate_local_pilot(self) -> PrrResult:
        config = json.loads((self.root / "operations/local-pilot-prr.json").read_text())
        passed: list[str] = []
        blocked: list[dict[str, str]] = []
        for criterion in config["criteria"]:
            path = self.root / criterion["path"]
            valid = path.is_file()
            if valid and "json_status" in criterion:
                try:
                    field = criterion.get("json_field", "status")
                    valid = json.loads(path.read_text()).get(field) == criterion["json_status"]
                except (json.JSONDecodeError, OSError):
                    valid = False
            if valid:
                passed.append(criterion["id"])
            else:
                blocked.append({"id": criterion["id"], "reason": f"missing or invalid {criterion['path']}"})
        verdict = config["verdict_on_pass"] if not blocked else "NO_GO_LOCAL_PILOT"
        warnings = (
            "Local pilot only; not production or Internet-facing",
            "Single operator means R2/R3 and separation-of-duties flows remain disabled",
        )
        return PrrResult(verdict, tuple(passed), tuple(blocked), warnings)

    def save(self, result: PrrResult, target: Path) -> None:
        target.write_text(
            json.dumps(
                {
                    "verdict": result.verdict,
                    "passed": list(result.passed),
                    "blocked": list(result.blocked),
                    "warnings": list(result.warnings),
                },
                indent=2,
            )
            + "\n"
        )
