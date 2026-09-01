#!/usr/bin/env python3
"""
APEX-7 Memory Manager
Gestisce la creazione, aggiornamento e manutenzione dei 5 layer di memoria.
"""

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional
import uuid


MEMORY_ROOT = Path("/home/user/apex-7/memory")


def generate_id(prefix: str) -> str:
    """Genera un ID univoco con prefisso."""
    return f"{prefix}-{uuid.uuid4().hex[:8]}"


def iso_now() -> str:
    """Restituisce timestamp ISO-8601."""
    return datetime.now(timezone.utc).isoformat()


def write_working_memory(session_id: str, key: str, value: dict) -> Path:
    """Scrive nella Working Memory (Layer 1)."""
    wm_dir = MEMORY_ROOT / "working" / session_id
    wm_dir.mkdir(parents=True, exist_ok=True)

    filepath = wm_dir / f"{key}.json"
    record = {
        "session_id": session_id,
        "key": key,
        "value": value,
        "updated_at": iso_now(),
        "version": 1,
    }

    filepath.write_text(json.dumps(record, indent=2, ensure_ascii=False))
    return filepath


def write_decision(
    session_id: str,
    author_agent: str,
    decision_type: str,
    decision: str,
    reasoning: str,
    alternatives: list,
    confidence: float,
    expected_outcome: str,
    tags: list = None,
) -> str:
    """Scrive una decisione nel Decision Log (Layer 2)."""
    dec_dir = MEMORY_ROOT / "decisions"
    dec_dir.mkdir(parents=True, exist_ok=True)

    dec_id = generate_id("DEC")
    record = {
        "decision_id": dec_id,
        "session_id": session_id,
        "timestamp": iso_now(),
        "author_agent": author_agent,
        "decision_type": decision_type,  # STRATEGIC/TACTICAL/OPERATIONAL
        "decision": decision,
        "reasoning": reasoning,
        "alternatives_considered": alternatives,
        "confidence": confidence,
        "expected_outcome": expected_outcome,
        "actual_outcome": None,
        "outcome_score": None,
        "tags": tags or [],
        "related_decisions": [],
        "status": "ACTIVE",
    }

    filepath = dec_dir / f"{dec_id}.json"
    filepath.write_text(json.dumps(record, indent=2, ensure_ascii=False))

    # Update index
    update_memory_index("decisions", dec_id, decision, iso_now())

    return dec_id


def write_strategy(
    name: str,
    category: str,
    description: str,
    when_to_use: str,
    when_not_to_use: str,
    steps: list,
    parameters: dict = None,
    success_rate: float = 0.0,
) -> str:
    """Scrive una strategia nello Strategy Store (Layer 3)."""
    strat_dir = MEMORY_ROOT / "strategies"
    strat_dir.mkdir(parents=True, exist_ok=True)

    strat_id = generate_id("STR")
    record = {
        "strategy_id": strat_id,
        "name": name,
        "category": category,
        "description": description,
        "when_to_use": when_to_use,
        "when_NOT_to_use": when_not_to_use,
        "parameters": parameters or {},
        "steps": steps,
        "success_rate": success_rate,
        "times_used": 0,
        "last_used": None,
        "avg_quality_improvement": 0.0,
        "source": "META_AGENT",
        "promoted_by": "META_AGENT",
        "status": "ACTIVE",
        "tags": [],
        "anti_pattern_counterpart": None,
    }

    filepath = strat_dir / f"{strat_id}.json"
    filepath.write_text(json.dumps(record, indent=2, ensure_ascii=False))

    return strat_id


def write_snapshot(
    version: str,
    trigger: str,
    system_config: dict,
    performance_metrics: dict,
    changes: list,
    reason: str,
) -> str:
    """Crea un Architecture Snapshot (Layer 4)."""
    snap_dir = MEMORY_ROOT / "snapshots"
    snap_dir.mkdir(parents=True, exist_ok=True)

    snap_id = generate_id("SNAP")
    record = {
        "snapshot_id": snap_id,
        "version": version,
        "timestamp": iso_now(),
        "trigger": trigger,
        "authored_by": "META_AGENT",
        "system_config": system_config,
        "performance_metrics": performance_metrics,
        "changes_from_previous": changes,
        "reason_for_changes": reason,
        "status": "CURRENT",
    }

    filepath = snap_dir / f"{snap_id}.json"
    filepath.write_text(json.dumps(record, indent=2, ensure_ascii=False))

    return snap_id


def update_memory_index(section: str, record_id: str, summary: str, timestamp: str):
    """Aggiorna MEMORY-INDEX.md."""
    index_path = MEMORY_ROOT / "MEMORY-INDEX.md"

    if not index_path.exists():
        index_path.write_text(
            "# MEMORY INDEX\n\n"
            "| Timestamp | Section | Record ID | Summary |\n"
            "|-----------|---------|-----------|----------|\n"
        )

    with open(index_path, "a") as f:
        f.write(f"| {timestamp[:19]} | {section} | {record_id} | {summary[:100]} |\n")


def archive_record(record_id: str, reason: str, superseded_by: str = None):
    """Archivia un record (mai cancellare)."""
    # Cerca in tutti i layer
    for layer in ["decisions", "strategies", "snapshots"]:
        layer_dir = MEMORY_ROOT / layer
        if not layer_dir.exists():
            continue
        for filepath in layer_dir.glob(f"{record_id}*"):
            record = json.loads(filepath.read_text())
            record["status"] = "ARCHIVED"
            record["archived_reason"] = reason
            if superseded_by:
                record["superseded_by"] = superseded_by
            filepath.write_text(json.dumps(record, indent=2, ensure_ascii=False))
            return True
    return False


def initialize_preloaded_strategies():
    """Inizializza le strategie pre-caricate."""
    preloaded = [
        {
            "name": "Piramide Evolutiva",
            "category": "PLANNING",
            "description": "Ogni livello di planning è il migliore del precedente",
            "when_to_use": "Task complessi con più componenti",
            "when_not_to_use": "Task semplici o single-step",
            "steps": ["Scomponi in livelli", "Parti dal generale", "Raffina ogni livello"],
            "success_rate": 0.87,
        },
        {
            "name": "Critique-Before-Output",
            "category": "GENERAL",
            "description": "Nessun output senza autocritica",
            "when_to_use": "Sempre",
            "when_not_to_use": "Mai — applicare sempre",
            "steps": ["Produci draft", "Auto-critica", "Refine", "Output"],
            "success_rate": 0.92,
        },
        {
            "name": "Memory-First Design",
            "category": "GENERAL",
            "description": "Consulta la memoria prima di agire",
            "when_to_use": "All'inizio di ogni task",
            "when_not_to_use": "Mai — applicare sempre",
            "steps": ["Query memoria", "Carica contesto", "Agisci", "Salva risultato"],
            "success_rate": 0.85,
        },
        {
            "name": "Parallel Execution",
            "category": "ORCHESTRATION",
            "description": "ANALYST e WRITER girano in parallelo",
            "when_to_use": "Quando i subtask sono indipendenti",
            "when_not_to_use": "Subtask con dipendenze sequenziali forti",
            "steps": ["Identifica task paralleli", "Spawna in parallelo", "Sincronizza risultati"],
            "success_rate": 0.78,
        },
    ]

    for strat in preloaded:
        write_strategy(**strat)


if __name__ == "__main__":
    initialize_preloaded_strategies()
    print("Memory initialized with preloaded strategies.")
