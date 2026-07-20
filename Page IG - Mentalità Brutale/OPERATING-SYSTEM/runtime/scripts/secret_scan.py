#!/usr/bin/env python3
"""Fail if current tracked source contains common hard-coded credential assignments."""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
PATTERNS = [
    re.compile(r'(?i)(password|access[_-]?token|app[_-]?secret|api[_-]?key)\s*=\s*["\'][^"\'\n]{6,}["\']'),
    re.compile(r'(?i)["\'](password|access_token|client_secret)["\']\s*:\s*["\'][^"\'\n]{6,}["\']'),
]
ALLOW_MARKERS = ("<REDACTED>", "YOUR_", "example", "os.environ", "getenv", "[REDACTED]", "CHANGEME", "not-real")
TARGET_PREFIXES = (
    "Page IG - Mentalità Brutale/OPERATING-SYSTEM/",
    "SKILL & Agenti/Workflow pubblicazione automatica/",
)


def tracked_files() -> list[Path]:
    output = subprocess.check_output(
        ["git", "-c", "core.quotepath=false", "ls-files", "-z", "--cached", "--others", "--exclude-standard"],
        cwd=REPO,
    ).decode("utf-8")
    return [REPO / line for line in output.split("\0") if line and line.startswith(TARGET_PREFIXES)]


def main() -> int:
    findings: list[str] = []
    for path in tracked_files():
        if not path.is_file() or path.suffix.lower() not in {".py", ".json", ".md", ".txt", ".yaml", ".yml", ".example"}:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for line_no, line in enumerate(text.splitlines(), start=1):
            if any(marker.casefold() in line.casefold() for marker in ALLOW_MARKERS):
                continue
            if any(pattern.search(line) for pattern in PATTERNS):
                findings.append(f"{path.relative_to(REPO)}:{line_no}")
    if findings:
        print("SECRET SCAN FAIL")
        for finding in findings:
            print(f"- {finding}")
        return 1
    print("SECRET SCAN PASS — no hard-coded credential assignments in current target files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
