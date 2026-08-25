from __future__ import annotations

import asyncio
import unittest
from pathlib import Path

from orchestrator.agents import (
    CodeReviewImplementerAgent,
    CodeReviewPlannerAgent,
    RefinerAgent,
    SecurityAuditAgent,
    SummarizerAgent,
)
from orchestrator.application.skill_registry import SkillRegistry
from orchestrator.runtime.models import TaskAssignment


class ExtendedAgentsTests(unittest.TestCase):
    def test_skill_registry_loads_all_skills(self):
        root = Path(__file__).resolve().parent.parent
        registry = SkillRegistry(root / "skills")
        skills = registry.list_skills()
        self.assertIn("repository-adr", skills)
        self.assertIn("code-review", skills)
        self.assertIn("security-audit", skills)
        self.assertIn("summarize", skills)

        cr = registry.get("code-review")
        self.assertIsNotNone(cr)
        self.assertEqual(cr.risk, "R1")
        self.assertIn("repo.read", cr.capabilities)

    def test_code_review_agents(self):
        planner = CodeReviewPlannerAgent()
        p_res = asyncio.run(
            planner(
                TaskAssignment(
                    "wf-1",
                    "task-1",
                    "code_review_planner",
                    "Plan review",
                    (),
                    {"code_files": ["src/main.py", "src/auth.py"]},
                    1000,
                    30,
                    0.5,
                    "spec-1",
                )
            )
        )
        self.assertEqual(p_res.status, "SUCCEEDED")
        self.assertEqual(len(p_res.output["tasks"]), 4)

        implementer = CodeReviewImplementerAgent()
        sources = {
            "src/main.py": {"content": "print('hello world')\n# TODO: add auth", "sha256": "abc"},
            "src/auth.py": {"content": "\n".join(f"line {i}" for i in range(350)), "sha256": "def"},
        }
        i_res = asyncio.run(
            implementer(
                TaskAssignment(
                    "wf-1",
                    "task-2",
                    "code_review_implementer",
                    "Review code",
                    (),
                    {"sources": sources},
                    2000,
                    60,
                    0.5,
                    "spec-2",
                )
            )
        )
        self.assertEqual(i_res.status, "SUCCEEDED")
        self.assertEqual(len(i_res.output["files"]), 2)
        self.assertGreaterEqual(i_res.output["total_findings"], 2)

    def test_security_audit_agent(self):
        audit_agent = SecurityAuditAgent()
        sources = {
            "src/config.py": {
                "content": "API_KEY = 'AKIA1234567890SECRETKEY'\nserver = '192.168.1.100'",
                "sha256": "123",
            }
        }
        res = asyncio.run(
            audit_agent(
                TaskAssignment(
                    "wf-1",
                    "task-3",
                    "security_audit",
                    "Scan code",
                    (),
                    {"sources": sources},
                    1000,
                    30,
                    0.5,
                    "spec-3",
                )
            )
        )
        self.assertEqual(res.status, "SUCCEEDED")
        self.assertEqual(res.output["status"], "FAIL")
        self.assertEqual(res.output["critical_count"], 1)

    def test_summarizer_and_refiner_agents(self):
        summarizer = SummarizerAgent()
        text = "È fondamentale notare che questo è un testo lungo con informazioni importanti su un cluster Kubernetes."
        s_res = asyncio.run(
            summarizer(
                TaskAssignment(
                    "wf-1",
                    "task-4",
                    "summarizer",
                    "Summarize",
                    (),
                    {"text": text, "max_words": 10},
                    500,
                    20,
                    0.5,
                    "spec-4",
                )
            )
        )
        self.assertEqual(s_res.status, "SUCCEEDED")
        self.assertNotIn("È fondamentale notare che", s_res.output["summary"])

        refiner = RefinerAgent()
        r_res = asyncio.run(
            refiner(
                TaskAssignment(
                    "wf-1",
                    "task-5",
                    "refiner",
                    "Refine draft",
                    (),
                    {
                        "draft": "# Title\n\n## Context\nSome context",
                        "issues": [{"issue": "Missing section: Decision"}],
                    },
                    1000,
                    30,
                    0.5,
                    "spec-5",
                )
            )
        )
        self.assertEqual(r_res.status, "SUCCEEDED")
        self.assertIn("## Decision", r_res.output["refined_text"])


if __name__ == "__main__":
    unittest.main()
