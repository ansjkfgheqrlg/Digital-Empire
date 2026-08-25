from __future__ import annotations

import json
import re
from pathlib import Path

ROOTS = [Path("src"), Path("policies"), Path("ruflo_bridge/src"), Path("builder_swarm")]
PATTERNS = {
    "private_key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "aws_access_key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "github_token": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}\b"),
    "bearer_token": re.compile(r"\bBearer\s+[A-Za-z0-9._-]{24,}"),
    "assigned_secret": re.compile(
        r"(?i)\b(?:password|api[_-]?key|secret)\s*=\s*['\"][^'\"]{12,}['\"]"
    ),
}


def main() -> int:
    findings = []
    for root in ROOTS:
        if not root.exists():
            continue
        for path in root.rglob("*"):
            if not path.is_file() or path.suffix not in {".py", ".ts", ".js", ".mjs", ".json", ".rego", ".md", ".yaml"}:
                continue
            text = path.read_text(encoding="utf-8", errors="replace")
            for name, pattern in PATTERNS.items():
                for match in pattern.finditer(text):
                    findings.append({"type": name, "path": str(path), "line": text.count("\n", 0, match.start()) + 1})
    report = {"scanner_version": "1.0", "files_roots": [str(root) for root in ROOTS], "findings": findings, "status": "PASS" if not findings else "FAIL"}
    target = Path("quality/evidence/w10-secret-scan.json")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    return 0 if not findings else 2


if __name__ == "__main__":
    raise SystemExit(main())
