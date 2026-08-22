from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


def script_path() -> Path:
    return Path(__file__).parents[3] / "scripts/verify_m3_response.py"


def run_verifier(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(  # noqa: S603 - executable and script path are controlled
        [sys.executable, str(script_path()), *args],
        check=False,
        capture_output=True,
        text=True,
    )


def test_m3_verifier_public_rfc8032_self_test_passes_without_private_key() -> None:
    result = run_verifier("--self-test")

    assert result.returncode == 0
    assert "PASS: RFC 8032 public vector verified" in result.stdout
    assert "PASS: tampered message rejected" in result.stdout
    assert "PRIVATE_KEY_MATERIAL=NOT_USED" in result.stdout


def test_m3_verifier_missing_external_response_blocks_cleanly(tmp_path: Path) -> None:
    result = run_verifier("--response", str(tmp_path / "absent.json"))

    assert result.returncode == 2
    assert "BLOCKED: external M3 response not supplied" in result.stdout
    assert "M3=OPEN" in result.stdout


def test_m3_verifier_rejects_any_private_key_shaped_field(tmp_path: Path) -> None:
    response = tmp_path / "unsafe.json"
    response.write_text(
        json.dumps({"schema_version": "1.0", "private_key": "forbidden-placeholder"}),
        encoding="utf-8",
    )

    result = run_verifier("--response", str(response))

    assert result.returncode == 1
    assert "FAIL: forbidden secret/private-key shaped field" in result.stdout
