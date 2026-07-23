"""
Owner: Max · Controllore: Claude · Origine: FORGE
Governo: MANDATO Art.8 + ADR-008
"""
from __future__ import annotations

import json
from empire import paths
from empire.memory import write as memory_write
from .record import PerfRecord, perf_to_atom

def capture_run(perf: PerfRecord) -> PerfRecord:
    # Converte il PerfRecord in un Atomo di memoria
    atom = perf_to_atom(perf)
    
    # Scrive l'atomo in memoria centrale con dedup attivo per l'idempotenza
    saved_atom = memory_write(atom, dedup=True)
    perf.id = saved_atom.id
    
    # Percorso del file JSON grezzo per la run
    runs_dir = paths.resolve("isp_telemetry") / "runs"
    runs_dir.mkdir(parents=True, exist_ok=True)
    
    record_file = runs_dir / f"RUN-{perf.id}.json"
    
    data = {
        "id": perf.id,
        "agent": perf.agent,
        "task": perf.task,
        "workflow": perf.workflow,
        "family": perf.family,
        "result": perf.result,
        "started": perf.started.isoformat(),
        "ended": perf.ended.isoformat(),
        "ttd_h": perf.ttd_h,
        "debug": perf.debug,
        "output_ref": [str(p) for p in perf.output_ref],
        "verification": perf.verification,
        "scorecard": perf.scorecard,
        "feedback_ids": perf.feedback_ids
    }
    
    with open(record_file, "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2, ensure_ascii=False)
        
    return perf
