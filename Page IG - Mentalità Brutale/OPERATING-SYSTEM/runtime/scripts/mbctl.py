#!/usr/bin/env python3
"""Repository-local entry point for MB-OS."""
from __future__ import annotations

import sys
from pathlib import Path

RUNTIME = Path(__file__).resolve().parents[1]
if str(RUNTIME) not in sys.path:
    sys.path.insert(0, str(RUNTIME))

from mb_os.cli import main


if __name__ == "__main__":
    raise SystemExit(main())
