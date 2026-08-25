from __future__ import annotations

from orchestrator.quality.nerve_save import compress_verified_output
from orchestrator.runtime.models import AgentResult, TaskAssignment, Usage


class SummarizerAgent:
    """Produces token-efficient summaries using NERVE-SAVE principles."""

    async def __call__(self, assignment: TaskAssignment) -> AgentResult:
        text = str(assignment.context.get("text", ""))
        max_words = int(assignment.context.get("max_words", 100))

        if not text:
            return AgentResult(
                assignment.task_id,
                "NEEDS_INPUT",
                {},
                failure={"code": "VAL_TEXT_REQUIRED"},
            )

        # Extract core sentences
        compressed = compress_verified_output(text)
        words = compressed.text.split()
        if len(words) > max_words:
            summary = " ".join(words[:max_words]) + "..."
        else:
            summary = compressed.text

        output = {
            "summary": summary,
            "original_length": len(text),
            "summary_length": len(summary),
            "compression_ratio": len(summary) / max(len(text), 1),
        }
        return AgentResult(
            assignment.task_id,
            "SUCCEEDED",
            output,
            usage=Usage(tokens_in=len(text.split()), tokens_out=len(summary.split())),
        )
