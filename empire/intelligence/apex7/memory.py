"""Memory Ecosystem — 5 livelli di memoria persistente (SQLite).

LAYER 1: working_memory      (contesto sessione corrente)
LAYER 2: decision_log        (ogni scelta + motivo + alternative)
LAYER 3: strategy_store      (pattern vincenti, success_rate)
LAYER 4: architecture_snapshots (versioni di architettura)
LAYER 5: compressed_knowledge (lessons / best / anti-patterns / policies)
"""
from __future__ import annotations

import json
import sqlite3
import uuid
from datetime import datetime, timezone
from pathlib import Path


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


SCHEMA = """
CREATE TABLE IF NOT EXISTS working_memory (
    id INTEGER PRIMARY KEY,
    session_id TEXT,
    current_task TEXT,
    current_phase TEXT,
    active_agents TEXT,
    context_variables TEXT,
    updated_at TEXT
);
CREATE TABLE IF NOT EXISTS decision_log (
    id TEXT PRIMARY KEY,
    decision TEXT,
    reason TEXT,
    alternatives_rejected TEXT,
    confidence REAL,
    outcome TEXT,
    timestamp TEXT
);
CREATE TABLE IF NOT EXISTS strategy_store (
    name TEXT PRIMARY KEY,
    description TEXT,
    success_rate REAL,
    status TEXT,
    applicable_to TEXT,
    times_used INTEGER DEFAULT 0,
    last_used TEXT
);
CREATE TABLE IF NOT EXISTS architecture_snapshots (
    version TEXT PRIMARY KEY,
    description TEXT,
    score REAL,
    status TEXT,
    config TEXT,
    diff_from_previous TEXT
);
CREATE TABLE IF NOT EXISTS compressed_knowledge (
    key TEXT PRIMARY KEY,
    value TEXT
);
"""


class MemoryEcosystem:
    def __init__(self, db_path: str = "apex7_memory.db") -> None:
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        self._init_schema()
        self.session_id = "apex7-" + uuid.uuid4().hex[:8]
        self._init_working_memory()

    # ---------- schema / working memory ----------
    def _init_schema(self) -> None:
        self.conn.executescript(SCHEMA)
        self.conn.commit()

    def _init_working_memory(self) -> None:
        self.conn.execute(
            "INSERT OR REPLACE INTO working_memory "
            "(id, session_id, current_task, current_phase, active_agents, context_variables, updated_at) "
            "VALUES (1, ?, '', '', '[]', '{}', ?)",
            (self.session_id, _now()),
        )
        self.conn.commit()

    def set_working(self, task="", phase="", agents=None, context=None) -> None:
        self.conn.execute(
            "UPDATE working_memory SET current_task=?, current_phase=?, "
            "active_agents=?, context_variables=?, updated_at=? WHERE id=1",
            (task, phase, json.dumps(agents or []),
             json.dumps(context or {}), _now()),
        )
        self.conn.commit()

    # ---------- LAYER 2: decision_log ----------
    def record_decision(self, decision, reason, alternatives=None,
                        confidence=0.8, outcome="") -> str:
        did = "DEC-" + uuid.uuid4().hex[:8].upper()
        self.conn.execute(
            "INSERT INTO decision_log "
            "(id, decision, reason, alternatives_rejected, confidence, outcome, timestamp) "
            "VALUES (?,?,?,?,?,?,?)",
            (did, decision, reason, json.dumps(alternatives or []),
             confidence, outcome, _now()),
        )
        self.conn.commit()
        return did

    def close_decision(self, decision_id: str, outcome: str) -> None:
        self.conn.execute(
            "UPDATE decision_log SET outcome=? WHERE id=?",
            (outcome, decision_id),
        )
        self.conn.commit()

    # ---------- LAYER 3: strategy_store ----------
    def add_strategy(self, name, description, applicable_to=None,
                     status="active") -> None:
        self.conn.execute(
            "INSERT OR REPLACE INTO strategy_store "
            "(name, description, success_rate, status, applicable_to, times_used, last_used) "
            "VALUES (?,?,?,?,?,?,?)",
            (name, description, None, status,
             json.dumps(applicable_to or []), 0, None),
        )
        self.conn.commit()

    def update_strategy_usage(self, name, success_rate=None) -> None:
        row = self.conn.execute(
            "SELECT times_used FROM strategy_store WHERE name=?", (name,)
        ).fetchone()
        used = (row["times_used"] if row else 0) + 1
        self.conn.execute(
            "UPDATE strategy_store SET times_used=?, last_used=?, success_rate=? WHERE name=?",
            (used, _now(), success_rate, name),
        )
        self.conn.commit()

    # ---------- LAYER 4: architecture_snapshots ----------
    def add_snapshot(self, version, description, score,
                     status="current", config=None, diff=None) -> None:
        self.conn.execute(
            "INSERT OR REPLACE INTO architecture_snapshots "
            "(version, description, score, status, config, diff_from_previous) "
            "VALUES (?,?,?,?,?,?)",
            (version, description, score, status,
             json.dumps(config or {}), diff or ""),
        )
        self.conn.commit()

    # ---------- LAYER 5: compressed_knowledge ----------
    def add_compressed(self, key, value) -> None:
        self.conn.execute(
            "INSERT OR REPLACE INTO compressed_knowledge (key, value) VALUES (?,?)",
            (key, json.dumps(value, ensure_ascii=False)),
        )
        self.conn.commit()

    def get_compressed(self, key):
        row = self.conn.execute(
            "SELECT value FROM compressed_knowledge WHERE key=?", (key,)
        ).fetchone()
        return json.loads(row["value"]) if row else None

    # ---------- export (schema spec-compliant) ----------
    def export_json(self, path: str | None = None) -> dict:
        wm = self.conn.execute(
            "SELECT * FROM working_memory WHERE id=1").fetchone()
        decisions = [dict(r) for r in self.conn.execute(
            "SELECT * FROM decision_log").fetchall()]
        strategies = [dict(r) for r in self.conn.execute(
            "SELECT * FROM strategy_store").fetchall()]
        snaps = [dict(r) for r in self.conn.execute(
            "SELECT * FROM architecture_snapshots").fetchall()]
        compressed = {
            r["key"]: json.loads(r["value"])
            for r in self.conn.execute("SELECT * FROM compressed_knowledge").fetchall()
        }
        out = {
            "apex7_memory": {
                "system_id": "apex7-001",
                "session_id": self.session_id,
                "working_memory": dict(wm) if wm else {},
                "decision_log": decisions,
                "strategy_store": strategies,
                "architecture_snapshots": snaps,
                "compressed_knowledge": compressed,
            }
        }
        if path:
            Path(path).write_text(
                json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
        return out

    def close(self) -> None:
        self.conn.close()
