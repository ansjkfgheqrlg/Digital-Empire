from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator


SECRET_PATTERNS = (
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"\bBearer\s+[A-Za-z0-9._-]{16,}", re.IGNORECASE),
    re.compile(r"\b(?:password|api[_-]?key|secret)\s*[:=]\s*[^\s]{8,}", re.IGNORECASE),
)


@dataclass(frozen=True)
class QualityReport:
    schema_pass: bool
    security_pass: bool
    correctness_pass: bool
    evidence_pass: bool
    failures: tuple[str, ...]

    @property
    def passed(self) -> bool:
        return all(
            (self.schema_pass, self.security_pass, self.correctness_pass, self.evidence_pass)
        )

    def as_gate_map(self) -> dict[str, bool]:
        return {
            "schema": self.schema_pass,
            "security": self.security_pass,
            "correctness": self.correctness_pass,
            "evidence": self.evidence_pass,
        }


class QualityPipeline:
    REQUIRED_SECTIONS = ("Status", "Context", "Decision", "Consequences", "Evidence")

    def __init__(self, output_schema: dict[str, Any]):
        Draft202012Validator.check_schema(output_schema)
        self.validator = Draft202012Validator(output_schema)

    def evaluate(self, output: dict[str, Any], known_sources: dict[str, dict]) -> QualityReport:
        failures: list[str] = []
        schema_errors = sorted(self.validator.iter_errors(output), key=lambda error: list(error.path))
        schema_pass = not schema_errors
        failures.extend(f"schema:{error.message}" for error in schema_errors)

        adr = output.get("adr", "") if isinstance(output, dict) else ""
        security_pass = isinstance(adr, str) and not any(pattern.search(adr) for pattern in SECRET_PATTERNS)
        if not security_pass:
            failures.append("security:secret_or_token_pattern")

        correctness_pass = isinstance(adr, str) and all(
            f"## {section}" in adr for section in self.REQUIRED_SECTIONS
        )
        if not correctness_pass:
            failures.append("correctness:required_sections_missing")

        evidence_pass = True
        evidence = output.get("evidence", []) if isinstance(output, dict) else []
        if len(evidence) != len(known_sources):
            evidence_pass = False
        else:
            for item in evidence:
                source = known_sources.get(item.get("path"))
                if source is None or source.get("sha256") != item.get("sha256"):
                    evidence_pass = False
                    break
                if item["path"] not in adr or f"sha256:{item['sha256']}" not in adr:
                    evidence_pass = False
                    break
        if not evidence_pass:
            failures.append("evidence:path_or_hash_mismatch")

        return QualityReport(
            schema_pass=schema_pass,
            security_pass=security_pass,
            correctness_pass=correctness_pass,
            evidence_pass=evidence_pass,
            failures=tuple(failures),
        )
