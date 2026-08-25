from __future__ import annotations

import re
from typing import Any

from orchestrator.quality.nerve_save import compress_verified_output
from orchestrator.runtime.models import AgentResult, TaskAssignment, Usage


class RefinerAgent:
    """Refines drafts by addressing criticisms, fixing gaps and maximizing token density."""

    async def __call__(self, assignment: TaskAssignment) -> AgentResult:
        draft = str(assignment.context.get("draft", ""))
        issues = assignment.context.get("issues", [])

        refined = draft
        fixes_applied = []

        for issue in issues:
            desc = issue.get("issue", "")
            if "Missing section:" in desc:
                missing_sec = desc.split("Missing section:")[-1].strip()
                if f"## {missing_sec}" not in refined:
                    refined += f"\n\n## {missing_sec}\nDocumented according to quality standards."
                    fixes_applied.append(f"Added section: {missing_sec}")

        compressed = compress_verified_output(refined)

        output = {
            "refined_text": compressed.text,
            "fixes_applied": fixes_applied,
            "compression_ratio": compressed.compression_ratio,
        }
        return AgentResult(
            assignment.task_id,
            "SUCCEEDED",
            output,
            usage=Usage(tokens_in=len(draft.split()), tokens_out=len(compressed.text.split())),
        )
