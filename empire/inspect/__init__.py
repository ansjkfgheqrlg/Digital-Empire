"""
Owner: Max · Controllore: Claude · Origine: FORGE
Governo: MANDATO Art.8 + ADR-008

API di sola lettura per il cruscotto (aggiunta dal LOTTO 2/1 del completamento Workflow
Estate, CP-20260723): `status()` e le sei metriche di telemetria. L'organo esisteva gia',
mancava il modo di interrogarlo senza passare dalla CLI.
"""
from __future__ import annotations

from .metrics import (ALL_METRICS, feedback_tips, first_pass, scorecard_5d, status,
                      telemetry_runs, traceability, ttd_vs_bench)

__all__ = ["status", "ALL_METRICS", "telemetry_runs", "scorecard_5d", "first_pass",
           "ttd_vs_bench", "feedback_tips", "traceability"]
