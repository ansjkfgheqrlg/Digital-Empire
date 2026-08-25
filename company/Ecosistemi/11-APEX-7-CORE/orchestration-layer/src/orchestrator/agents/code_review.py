from __future__ import annotations

import json
from typing import Any

from orchestrator.runtime.models import AgentResult, TaskAssignment, Usage


class CodeReviewPlannerAgent:
    async def __call__(self, assignment: TaskAssignment) -> AgentResult:
        files = assignment.context.get("code_files", [])
        if not files:
            return AgentResult(
                assignment.task_id,
                "NEEDS_INPUT",
                {},
                failure={"code": "VAL_CODE_FILES_REQUIRED"},
            )
        plan = {
            "tasks": [
                {"id": "analyze-code", "role": "code_analyzer", "depends_on": []},
                {"id": "security-check", "role": "security_audit", "depends_on": ["analyze-code"]},
                {"id": "critic", "role": "critic", "depends_on": ["security-check"]},
                {"id": "gate", "role": "gate", "depends_on": ["critic"]},
            ],
            "code_files": files,
        }
        return AgentResult(
            assignment.task_id,
            "SUCCEEDED",
            plan,
            usage=Usage(tokens_in=len(files), tokens_out=75),
        )


class CodeReviewImplementerAgent:
    async def __call__(self, assignment: TaskAssignment) -> AgentResult:
        sources = assignment.context.get("sources")
        if not isinstance(sources, dict) or not sources:
            return AgentResult(
                assignment.task_id,
                "NEEDS_INPUT",
                {},
                failure={"code": "VAL_SOURCE_CODE_REQUIRED"},
            )

        reviews: list[dict[str, Any]] = []
        for path, data in sorted(sources.items()):
            content = data.get("content", "")
            lines = content.splitlines()
            findings = []
            if len(lines) > 300:
                findings.append({"severity": "MEDIUM", "message": f"File exceeds 300 lines ({len(lines)} lines)"})
            if "TODO" in content or "FIXME" in content:
                findings.append({"severity": "LOW", "message": "Contains unresolved TODO/FIXME markers"})
            reviews.append({
                "path": path,
                "sha256": data.get("sha256", ""),
                "lines_count": len(lines),
                "findings": findings,
            })

        output = {
            "review_summary": f"Reviewed {len(reviews)} file(s).",
            "files": reviews,
            "total_findings": sum(len(r["findings"]) for r in reviews),
        }
        return AgentResult(
            assignment.task_id,
            "SUCCEEDED",
            output,
            usage=Usage(tokens_in=sum(len(v["content"].split()) for v in sources.values()), tokens_out=120),
        )
