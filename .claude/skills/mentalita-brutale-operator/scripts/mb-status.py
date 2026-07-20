#!/usr/bin/env python3
"""Convenience wrapper: print MB-OS control status without duplicating runtime logic."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
CLI = REPO / "Page IG - Mentalità Brutale" / "OPERATING-SYSTEM" / "runtime" / "scripts" / "mbctl.py"
raise SystemExit(subprocess.call([sys.executable, str(CLI), "status"]))
