from __future__ import annotations

import hashlib
import json
from typing import Any

from orchestrator.runtime.models import AgentResult, TaskAssignment, Usage


class PlannerAgent:
    async def __call__(self, assignment: TaskAssignment) -> AgentResult:
        files = assignment.context.get("repository_files", [])
        if not files:
            return AgentResult(
                assignment.task_id,
                "NEEDS_INPUT",
                {},
                failure={"code": "VAL_REPOSITORY_FILES_REQUIRED"},
            )
        plan = {
            "tasks": [
                {"id": "analyze-and-write", "role": "implementer", "depends_on": []},
                {"id": "critic", "role": "critic", "depends_on": ["analyze-and-write"]},
                {"id": "gate", "role": "gate", "depends_on": ["critic"]},
            ],
            "repository_files": files,
            "artifact_path": assignment.context.get("artifact_path", "adr/0001-repository.md"),
        }
        return AgentResult(
            assignment.task_id,
            "SUCCEEDED",
            plan,
            usage=Usage(tokens_in=len(files), tokens_out=80),
        )


class ImplementerAgent:
    REQUIRED_SECTIONS = ("Status", "Context", "Decision", "Consequences", "Evidence")

    async def __call__(self, assignment: TaskAssignment) -> AgentResult:
        sources = assignment.context.get("sources")
        if not isinstance(sources, dict) or not sources:
            return AgentResult(
                assignment.task_id,
                "NEEDS_INPUT",
                {},
                failure={"code": "VAL_SOURCE_EVIDENCE_REQUIRED"},
            )
        evidence = []
        languages: set[str] = set()
        for path, source in sorted(sources.items()):
            content = source["content"]
            digest = source["sha256"]
            evidence.append({"path": path, "sha256": digest})
            suffix = path.rsplit(".", 1)[-1] if "." in path else ""
            languages.add({"py": "Python", "ts": "TypeScript", "js": "JavaScript"}.get(suffix, suffix or "text"))

        language_text = ", ".join(sorted(languages))
        file_list = ", ".join(item["path"] for item in evidence)
        evidence_lines = "\n".join(
            f"- `{item['path']}` — `sha256:{item['sha256']}`" for item in evidence
        )
        adr = f"""# ADR: Repository analysis baseline

## Status
Accepted for local pilot evaluation.

## Context
The repository fixture contains {len(evidence)} inspected file(s): {file_list}. Detected formats: {language_text}.

## Decision
Use a deterministic, evidence-linked repository analysis before enabling any probabilistic runtime. Keep the repository read-only and write the ADR only to the scoped artifact store.

## Consequences
- Analysis is reproducible from the cited file hashes.
- No claim is made about files outside the supplied scope.
- RuFlo and external side effects remain disabled.

## Evidence
{evidence_lines}
"""
        claims = (
            {
                "text": f"The scoped repository contains {len(evidence)} inspected files.",
                "evidence_refs": [f"repo://{item['path']}#sha256:{item['sha256']}" for item in evidence],
            },
        )
        return AgentResult(
            assignment.task_id,
            "SUCCEEDED",
            {"adr": adr, "evidence": evidence},
            claims=claims,
            usage=Usage(tokens_in=sum(len(v["content"].split()) for v in sources.values()), tokens_out=len(adr.split())),
        )


class CriticAgent:
    async def __call__(self, assignment: TaskAssignment) -> AgentResult:
        adr = str(assignment.context.get("adr", ""))
        evidence = assignment.context.get("evidence", [])
        issues: list[dict[str, Any]] = []
        for section in ImplementerAgent.REQUIRED_SECTIONS:
            if f"## {section}" not in adr:
                issues.append(
                    {"severity": "CRITICAL", "issue": f"Missing section: {section}", "blocking": True}
                )
        for item in evidence:
            marker = f"sha256:{item['sha256']}"
            if marker not in adr or item["path"] not in adr:
                issues.append(
                    {"severity": "HIGH", "issue": f"Evidence not cited: {item['path']}", "blocking": True}
                )
        return AgentResult(
            assignment.task_id,
            "SUCCEEDED",
            {"issues": issues, "blocking_count": sum(1 for issue in issues if issue["blocking"])},
            usage=Usage(tokens_in=len(adr.split()), tokens_out=max(10, len(issues) * 20)),
        )


class GateAgent:
    async def __call__(self, assignment: TaskAssignment) -> AgentResult:
        issues = assignment.context.get("issues", [])
        deterministic_gates = assignment.context.get("deterministic_gates", {})
        failures = [issue for issue in issues if issue.get("blocking")]
        failures.extend(
            {"issue": name, "blocking": True}
            for name, passed in deterministic_gates.items()
            if not passed
        )
        verdict = "PASS" if not failures else "REMEDIATE"
        return AgentResult(
            assignment.task_id,
            "SUCCEEDED",
            {
                "verdict": verdict,
                "blocking_failures": failures,
                "artifact_hash": assignment.context.get("artifact_hash"),
            },
            usage=Usage(tokens_in=len(json.dumps(assignment.context)), tokens_out=40),
        )
