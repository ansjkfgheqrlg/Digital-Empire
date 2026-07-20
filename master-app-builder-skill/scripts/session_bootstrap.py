#!/usr/bin/env python3
"""Verify the Python environment for the Master App Builder skill project."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

REQUIRED_PYTHON: tuple[int, int] = (3, 11)
PROJECT_ROOT: Path = Path(__file__).resolve().parents[1]
REQUIREMENTS: Path = PROJECT_ROOT / "requirements.txt"


def check_python_version() -> None:
    """Raise an error when the interpreter is below the supported version."""
    current: tuple[int, int] = sys.version_info[:2]
    if current < REQUIRED_PYTHON:
        required: str = ".".join(map(str, REQUIRED_PYTHON))
        actual: str = ".".join(map(str, current))
        raise RuntimeError(f"Python {required}+ required; current version: {actual}")
    print(f"Python {sys.version.split()[0]} — OK")


def check_dependencies() -> None:
    """Run pip's consistency check when a requirements file exists."""
    if not REQUIREMENTS.exists():
        print("requirements.txt not present — dependency check skipped.")
        return
    result: subprocess.CompletedProcess[str] = subprocess.run(
        [sys.executable, "-m", "pip", "check"],
        capture_output=True,
        check=False,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(f"Inconsistent dependencies:\n{result.stdout}{result.stderr}")
    print("Dependencies — OK")


def main() -> None:
    """Run all environment validations."""
    print("Master App Builder — Environment Bootstrap")
    check_python_version()
    check_dependencies()
    print("Environment ready.")


if __name__ == "__main__":
    main()
