#!/usr/bin/env python3
"""Validate verifiable invariants of the Master build Architecture repository."""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path

REQUIRED_GOVERNANCE: tuple[str, ...] = (
    "governance/README.md",
    "governance/WORKFLOW-FIRST.md",
    "governance/MEMORY-PROTOCOL.md",
    "governance/REFERENCE-LIBRARY.md",
    "agents/OPERATING-REGISTRY.md",
    "workflows/README.md",
)
CREDENTIAL_PATTERN: re.Pattern[str] = re.compile(r"(?:github_pat_|ghp_)[A-Za-z0-9_]+")


@dataclass(frozen=True)
class Finding:
    """One deterministic validation result."""

    level: str
    code: str
    message: str
    path: str


def iter_agent_directories(root: Path) -> list[Path]:
    """Return only concrete agent directories, excluding category directories."""
    agents_root = root / "agents"
    return sorted(
        path
        for path in agents_root.glob("*/*")
        if path.is_dir() and path.name != "__pycache__"
    )


def scan_credentials(root: Path) -> list[Finding]:
    """Find PAT-like values in tracked text files while skipping Git metadata."""
    findings: list[Finding] = []
    for path in root.rglob("*"):
        if not path.is_file() or ".git" in path.parts or path.suffix not in {".md", ".py", ".json", ".txt"}:
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if CREDENTIAL_PATTERN.search(content):
            findings.append(Finding("error", "SECRET-001", "PAT-like value found", str(path.relative_to(root))))
    return findings


def validate(root: Path) -> tuple[list[Finding], dict[str, int]]:
    """Run repository checks and return findings plus measurable summary data."""
    findings: list[Finding] = []
    for relative_path in REQUIRED_GOVERNANCE:
        path = root / relative_path
        if not path.is_file():
            findings.append(Finding("error", "GOV-001", "Required governance file missing", relative_path))

    workflow_rule = root / "governance/WORKFLOW-FIRST.md"
    if workflow_rule.is_file() and "Ogni app parte da un workflow" not in workflow_rule.read_text(encoding="utf-8"):
        findings.append(Finding("error", "WF-001", "Workflow-first rule is incomplete", str(workflow_rule.relative_to(root))))

    evals_path = root / "evals/evals.json"
    if not evals_path.is_file():
        findings.append(Finding("error", "EVAL-001", "Evaluation catalogue missing", "evals/evals.json"))
    else:
        try:
            parsed: object = json.loads(evals_path.read_text(encoding="utf-8"))
            if not isinstance(parsed, dict) or not isinstance(parsed.get("evals"), list):
                findings.append(Finding("error", "EVAL-002", "Evaluation catalogue has an invalid shape", "evals/evals.json"))
        except json.JSONDecodeError as exc:
            findings.append(Finding("error", "EVAL-003", f"Invalid JSON: {exc.msg}", "evals/evals.json"))

    agent_dirs = iter_agent_directories(root)
    complete = 0
    partial = 0
    for directory in agent_dirs:
        count = len(list(directory.glob("*.md")))
        relative = str(directory.relative_to(root))
        if count >= 7:
            complete += 1
        else:
            partial += 1
            findings.append(Finding("warning", "AGENT-001", f"Agent has {count}/7 canonical Markdown files", relative))

    findings.extend(scan_credentials(root))
    memory_index = root / "memory/MEMORY-INDEX.md"
    if not memory_index.is_file():
        findings.append(Finding("error", "MEM-001", "Memory index missing", "memory/MEMORY-INDEX.md"))

    if complete < 25:
        findings.append(Finding("error", "AGENT-002", f"Only {complete}/25 complete agent directories", "agents/"))

    required_reference_dirs = ("04-processes", "05-decision-trees", "07-templates", "09-faq", "10-references")
    for directory_name in required_reference_dirs:
        directory = root / "references/knowledge-pack" / directory_name
        if not directory.is_dir() or not any(directory.iterdir()):
            findings.append(Finding("error", "REF-001", "Required knowledge-pack section is missing or empty", str(directory.relative_to(root))))

    summary = {"agent_directories": len(agent_dirs), "complete_agents": complete, "partial_agents": partial}
    return findings, summary


def main() -> int:
    """Parse arguments, run validation, and write a machine-readable report."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--report", type=Path, default=Path("memory/self-improvement/validation-report.json"))
    args = parser.parse_args()
    root = args.root.resolve()
    findings, summary = validate(root)
    report_path = args.report if args.report.is_absolute() else root / args.report
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report: dict[str, object] = {"summary": summary, "findings": [asdict(item) for item in findings]}
    report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    errors = sum(item.level == "error" for item in findings)
    warnings = sum(item.level == "warning" for item in findings)
    print(f"Validation: {errors} error(s), {warnings} warning(s); report: {report_path}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
