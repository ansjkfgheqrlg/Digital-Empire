from __future__ import annotations

import re
from typing import Any

from orchestrator.runtime.models import AgentResult, TaskAssignment, Usage

SECURITY_PATTERNS = {
    "SECRET_KEY": re.compile(r"(?:api_key|secret|password|private_key|token)\s*=\s*['\"][A-Za-z0-9_\-+/]{12,}['\"]", re.I),
    "HARDCODED_IP": re.compile(r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b"),
    "SQL_INJECTION_RISK": re.compile(r"(?:SELECT|INSERT|UPDATE|DELETE)\s+.*\+\s*\w+", re.I),
    "EVAL_EXEC": re.compile(r"\b(?:eval|exec)\s*\(", re.I),
}


class SecurityAuditAgent:
    async def __call__(self, assignment: TaskAssignment) -> AgentResult:
        sources = assignment.context.get("sources")
        if not isinstance(sources, dict):
            return AgentResult(
                assignment.task_id,
                "NEEDS_INPUT",
                {},
                failure={"code": "VAL_SOURCES_REQUIRED"},
            )

        vulnerabilities: list[dict[str, Any]] = []
        for path, data in sources.items():
            content = data.get("content", "")
            for pattern_name, regex in SECURITY_PATTERNS.items():
                matches = list(regex.finditer(content))
                for match in matches:
                    vulnerabilities.append({
                        "file": path,
                        "vulnerability_type": pattern_name,
                        "severity": "CRITICAL" if pattern_name in ("SECRET_KEY", "EVAL_EXEC") else "HIGH",
                        "matched_snippet": match.group(0)[:60],
                    })

        status = "FAIL" if any(v["severity"] == "CRITICAL" for v in vulnerabilities) else "PASS"
        output = {
            "status": status,
            "vulnerabilities": vulnerabilities,
            "critical_count": sum(1 for v in vulnerabilities if v["severity"] == "CRITICAL"),
            "high_count": sum(1 for v in vulnerabilities if v["severity"] == "HIGH"),
        }
        return AgentResult(
            assignment.task_id,
            "SUCCEEDED",
            output,
            usage=Usage(tokens_in=sum(len(v["content"].split()) for v in sources.values()), tokens_out=len(vulnerabilities) * 20 + 30),
        )
