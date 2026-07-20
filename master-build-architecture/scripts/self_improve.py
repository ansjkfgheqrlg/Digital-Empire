#!/usr/bin/env python3
"""Turn deterministic validation findings into a bounded self-improvement plan."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


def classify_action(code: str, path: str, message: str) -> str:
    """Map a finding to a safe, human-reviewable remediation action."""
    if code == "SECRET-001":
        return f"Block release; revoke exposed credential if real, redact `{path}`, then re-run validation."
    if code == "AGENT-001":
        return f"Complete the six missing canonical artefacts for `{path}`; do not claim the agent is complete beforehand."
    if code.startswith("WF-"):
        return "Restore the WF-0 workflow-first rule before approving requirements or implementation."
    if code.startswith("GOV-"):
        return f"Restore required control file `{path}` from the approved governance baseline."
    return f"Investigate `{path}`: {message}"


def main() -> int:
    """Run validation, persist a plan, and return nonzero only for blocking errors."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    root = args.root.resolve()
    report = root / "memory/self-improvement/validation-report.json"
    command = [sys.executable, str(root / "scripts/validate_skill.py"), "--root", str(root), "--report", str(report)]
    completed = subprocess.run(command, check=False, capture_output=True, text=True)
    payload: object = json.loads(report.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise RuntimeError("Validation report has invalid shape.")
    raw_findings = payload.get("findings")
    if not isinstance(raw_findings, list):
        raise RuntimeError("Validation report lacks findings.")

    actions: list[str] = []
    for raw in raw_findings:
        if not isinstance(raw, dict):
            continue
        code = str(raw.get("code", "UNKNOWN"))
        path = str(raw.get("path", "unknown"))
        message = str(raw.get("message", "No message"))
        actions.append(f"- [{code}] {classify_action(code, path, message)}")
    if not actions:
        actions.append("- No remediation is required. Keep the scheduled validation gate active.")

    now = datetime.now(timezone.utc).isoformat()
    plan = root / "memory/self-improvement/PLAN-v1.md"
    plan.write_text(
        "# Self-Improvement Plan\n\n"
        f"- Generated: {now}\n"
        "- Input: deterministic `scripts/validate_skill.py` report\n"
        "- Safety boundary: this process creates plans and evidence; it does not change architecture, dependencies, or credentials without review.\n\n"
        "## Proposed actions\n" + "\n".join(actions) + "\n\n"
        "## Verification gate\n"
        "1. Apply an approved action.\n"
        "2. Re-run `python scripts/validate_skill.py --root .`.\n"
        "3. Record the actual result in `memory/MEMORY-INDEX.md`.\n",
        encoding="utf-8",
    )
    print(completed.stdout.strip())
    print(f"Self-improvement plan: {plan}")
    return completed.returncode


if __name__ == "__main__":
    raise SystemExit(main())
