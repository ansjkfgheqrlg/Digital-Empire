#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AGENTE: Orchestratore-1 — Pipeline Orchestration Agent
Owner: GAEL · Controllore: A2-QA · Versione: 2.0
Governo: APEX-7 Framework · preventa-maps-scraper

Documentazione completa: ./AGENTE.md

NON duplicare logica qui: l'orchestrazione event-driven (Scraper → Qualifier → Writer → Sender →
Sheets → Gate E2E) vive nella classe Conductor di ../../02-AUTOMAZIONI-E-SCRIPTS/agents.py, e il
suo entry point CLI è ../../02-AUTOMAZIONI-E-SCRIPTS/orchestrator.py. Questo modulo re-esporta
Conductor sotto il nome canonico OrchestratorAgent per coerenza col pattern cartella-per-agente,
senza ricreare un secondo script CLI ~250 righe quasi identico a orchestrator.py (era il difetto
del vecchio agente_orchestratore.py, wipeato in Phase A).

CLI:
    Usa direttamente ../../02-AUTOMAZIONI-E-SCRIPTS/orchestrator.py (entry point ufficiale).
"""
from __future__ import annotations

import sys
from pathlib import Path

# ── Path resolution ──────────────────────────────────────────────────────────
_AGENT_DIR = Path(__file__).parent
_ROOT_DIR  = _AGENT_DIR.parent.parent
_SCRIPTS   = _ROOT_DIR / "02-AUTOMAZIONI-E-SCRIPTS"

if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from agents import Conductor as OrchestratorAgent  # noqa: E402,F401 — alias canonico per questo agente


def _load_rules() -> str:
    md = _AGENT_DIR / "AGENTE.md"
    return md.read_text(encoding="utf-8") if md.exists() else "Rules not found"


if __name__ == "__main__":
    print(
        "Orchestratore-1 non ha una CLI propria: usa "
        "'python ../../02-AUTOMAZIONI-E-SCRIPTS/orchestrator.py --city <città> ...' "
        "(entry point ufficiale della pipeline completa)."
    )
