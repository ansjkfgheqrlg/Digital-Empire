"""
SQLiteStore - Persistenza async per conversazioni e long-term memory
Usa aiosqlite se disponibile, altrimenti sqlite3 in thread.
"""
from __future__ import annotations

import asyncio
import json
import logging
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

logger = logging.getLogger("empire.store")

CREATE_SQL = """
CREATE TABLE IF NOT EXISTS conversations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    agent_name TEXT NOT NULL,
    session_id TEXT NOT NULL,
    role TEXT NOT NULL,
    content_json TEXT NOT NULL,
    created_at TEXT NOT NULL,
    token_estimate INTEGER DEFAULT 0
);
CREATE INDEX IF NOT EXISTS idx_agent_session ON conversations(agent_name, session_id, created_at);

CREATE TABLE IF NOT EXISTS long_term_memory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    agent_name TEXT NOT NULL,
    key TEXT NOT NULL,
    value_json TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    UNIQUE(agent_name, key)
);

CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_id TEXT UNIQUE NOT NULL,
    agent_name TEXT NOT NULL,
    status TEXT NOT NULL,
    payload_json TEXT NOT NULL,
    created_at TEXT NOT NULL
);
"""

class SQLiteStore:
    def __init__(self, db_path: Path | str):
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._aiosqlite = None
        try:
            import aiosqlite  # type: ignore
            self._aiosqlite = aiosqlite
            logger.info("SQLiteStore using aiosqlite")
        except ImportError:
            logger.warning("aiosqlite non trovato, uso sqlite3+thread (installa aiosqlite per performance)")
        self._init_lock = asyncio.Lock()
        self._initialized = False

    async def _ensure_init(self) -> None:
        if self._initialized:
            return
        async with self._init_lock:
            if self._initialized:
                return
            if self._aiosqlite:
                async with self._aiosqlite.connect(self.db_path) as db:
                    await db.executescript(CREATE_SQL)
                    await db.commit()
            else:
                def _sync():
                    import sqlite3
                    conn = sqlite3.connect(self.db_path)
                    conn.executescript(CREATE_SQL)
                    conn.commit()
                    conn.close()
                await asyncio.to_thread(_sync)
            self._initialized = True
            logger.info(f"SQLiteStore ready at {self.db_path}")

    async def save_message(self, agent_name: str, session_id: str, role: str, content: Any) -> int:
        await self._ensure_init()
        content_json = json.dumps(content, ensure_ascii=False, default=str)
        token_est = len(content_json)//4
        created_at = datetime.now(timezone.utc).isoformat()

        if self._aiosqlite:
            async with self._aiosqlite.connect(self.db_path) as db:
                cur = await db.execute(
                    "INSERT INTO conversations (agent_name, session_id, role, content_json, created_at, token_estimate) VALUES (?,?,?,?,?,?)",
                    (agent_name, session_id, role, content_json, created_at, token_est),
                )
                await db.commit()
                return cur.lastrowid or 0
        else:
            def _sync() -> int:
                import sqlite3
                conn = sqlite3.connect(self.db_path)
                cur = conn.execute(
                    "INSERT INTO conversations (agent_name, session_id, role, content_json, created_at, token_estimate) VALUES (?,?,?,?,?,?)",
                    (agent_name, session_id, role, content_json, created_at, token_est),
                )
                conn.commit()
                rowid = cur.lastrowid or 0
                conn.close()
                return rowid
            return await asyncio.to_thread(_sync)

    async def load_history(self, agent_name: str, session_id: str, limit: int = 50) -> list[dict[str, Any]]:
        await self._ensure_init()
        if self._aiosqlite:
            async with self._aiosqlite.connect(self.db_path) as db:
                db.row_factory = self._aiosqlite.Row
                async with db.execute(
                    "SELECT role, content_json, created_at FROM conversations WHERE agent_name=? AND session_id=? ORDER BY created_at DESC LIMIT ?",
                    (agent_name, session_id, limit),
                ) as cur:
                    rows = await cur.fetchall()
                    rows = list(reversed(rows))
        else:
            def _sync():
                import sqlite3
                conn = sqlite3.connect(self.db_path)
                cur = conn.execute(
                    "SELECT role, content_json, created_at FROM conversations WHERE agent_name=? AND session_id=? ORDER BY created_at DESC LIMIT ?",
                    (agent_name, session_id, limit),
                )
                rows = cur.fetchall()
                conn.close()
                return list(reversed(rows))
            raw_rows = await asyncio.to_thread(_sync)
            # normalize to dict-like
            rows = [{"role": r[0], "content_json": r[1], "created_at": r[2]} for r in raw_rows]
            # below handle both cases

        history: list[dict[str, Any]] = []
        for r in rows:
            if isinstance(r, dict):
                role = r["role"]
                content_json = r["content_json"]
            else:
                role = r["role"]
                content_json = r["content_json"]
            try:
                content = json.loads(content_json)
            except Exception:
                content = content_json
            history.append({"role": role, "content": content})
        return history

    async def set_long_term(self, agent_name: str, key: str, value: Any) -> None:
        await self._ensure_init()
        value_json = json.dumps(value, ensure_ascii=False, default=str)
        updated_at = datetime.now(timezone.utc).isoformat()
        if self._aiosqlite:
            async with self._aiosqlite.connect(self.db_path) as db:
                await db.execute(
                    "INSERT INTO long_term_memory (agent_name, key, value_json, updated_at) VALUES (?,?,?,?) ON CONFLICT(agent_name,key) DO UPDATE SET value_json=excluded.value_json, updated_at=excluded.updated_at",
                    (agent_name, key, value_json, updated_at),
                )
                await db.commit()
        else:
            def _sync():
                import sqlite3
                conn = sqlite3.connect(self.db_path)
                conn.execute(
                    "INSERT INTO long_term_memory (agent_name, key, value_json, updated_at) VALUES (?,?,?,?) ON CONFLICT(agent_name,key) DO UPDATE SET value_json=excluded.value_json, updated_at=excluded.updated_at",
                    (agent_name, key, value_json, updated_at),
                )
                conn.commit()
                conn.close()
            await asyncio.to_thread(_sync)

    async def get_long_term(self, agent_name: str, key: str) -> Any | None:
        await self._ensure_init()
        if self._aiosqlite:
            async with self._aiosqlite.connect(self.db_path) as db:
                async with db.execute(
                    "SELECT value_json FROM long_term_memory WHERE agent_name=? AND key=?",
                    (agent_name, key),
                ) as cur:
                    row = await cur.fetchone()
                    if not row:
                        return None
                    return json.loads(row[0])
        else:
            def _sync():
                import sqlite3
                conn = sqlite3.connect(self.db_path)
                cur = conn.execute(
                    "SELECT value_json FROM long_term_memory WHERE agent_name=? AND key=?",
                    (agent_name, key),
                )
                row = cur.fetchone()
                conn.close()
                if not row:
                    return None
                return json.loads(row[0])
            return await asyncio.to_thread(_sync)

    async def clear_session(self, agent_name: str, session_id: str) -> None:
        await self._ensure_init()
        if self._aiosqlite:
            async with self._aiosqlite.connect(self.db_path) as db:
                await db.execute(
                    "DELETE FROM conversations WHERE agent_name=? AND session_id=?",
                    (agent_name, session_id),
                )
                await db.commit()
        else:
            def _sync():
                import sqlite3
                conn = sqlite3.connect(self.db_path)
                conn.execute(
                    "DELETE FROM conversations WHERE agent_name=? AND session_id=?",
                    (agent_name, session_id),
                )
                conn.commit()
                conn.close()
            await asyncio.to_thread(_sync)
        logger.info(f"Cleared session {session_id} for {agent_name}")
