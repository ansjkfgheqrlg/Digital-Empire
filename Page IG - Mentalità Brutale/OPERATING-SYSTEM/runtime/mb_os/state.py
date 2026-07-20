from __future__ import annotations

import json
import sqlite3
from contextlib import contextmanager
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Iterator

from .models import ContentManifest


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


class StateStore:
    def __init__(self, path: Path):
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.migrate()

    @contextmanager
    def connection(self) -> Iterator[sqlite3.Connection]:
        conn = sqlite3.connect(self.path)
        conn.row_factory = sqlite3.Row
        try:
            yield conn
            conn.commit()
        finally:
            conn.close()

    def migrate(self) -> None:
        with self.connection() as conn:
            conn.executescript(
                """
                PRAGMA journal_mode=WAL;
                CREATE TABLE IF NOT EXISTS control (
                    key TEXT PRIMARY KEY,
                    value TEXT NOT NULL,
                    updated_at TEXT NOT NULL
                );
                CREATE TABLE IF NOT EXISTS jobs (
                    content_hash TEXT PRIMARY KEY,
                    content_id TEXT NOT NULL,
                    scheduled_at TEXT NOT NULL,
                    status TEXT NOT NULL,
                    manifest_json TEXT NOT NULL,
                    attempts INTEGER NOT NULL DEFAULT 0,
                    last_error TEXT,
                    created_at TEXT NOT NULL,
                    updated_at TEXT NOT NULL
                );
                CREATE TABLE IF NOT EXISTS publications (
                    content_hash TEXT PRIMARY KEY,
                    content_id TEXT NOT NULL,
                    media_id TEXT NOT NULL,
                    container_id TEXT,
                    permalink TEXT,
                    published_at TEXT NOT NULL,
                    response_json TEXT NOT NULL
                );
                CREATE TABLE IF NOT EXISTS metric_snapshots (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    content_id TEXT NOT NULL,
                    media_id TEXT NOT NULL,
                    media_type TEXT NOT NULL,
                    captured_at TEXT NOT NULL,
                    metrics_json TEXT NOT NULL,
                    quality_action_rate REAL,
                    UNIQUE(media_id, captured_at)
                );
                CREATE TABLE IF NOT EXISTS events (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    ts TEXT NOT NULL,
                    content_id TEXT,
                    event TEXT NOT NULL,
                    payload_json TEXT NOT NULL
                );
                """
            )
            self._set_default(conn, "autonomy_mode", "SHADOW")
            self._set_default(conn, "kill_switch", "ACTIVE")

    @staticmethod
    def _set_default(conn: sqlite3.Connection, key: str, value: str) -> None:
        conn.execute(
            "INSERT OR IGNORE INTO control(key,value,updated_at) VALUES(?,?,?)",
            (key, value, utc_now()),
        )

    def get_control(self, key: str, default: str = "") -> str:
        with self.connection() as conn:
            row = conn.execute("SELECT value FROM control WHERE key=?", (key,)).fetchone()
        return str(row["value"]) if row else default

    def set_control(self, key: str, value: str) -> None:
        with self.connection() as conn:
            conn.execute(
                "INSERT INTO control(key,value,updated_at) VALUES(?,?,?) "
                "ON CONFLICT(key) DO UPDATE SET value=excluded.value,updated_at=excluded.updated_at",
                (key, value, utc_now()),
            )
        self.event("CONTROL_CHANGED", {"key": key, "value": value})

    def enqueue(self, manifest: ContentManifest) -> bool:
        now = utc_now()
        with self.connection() as conn:
            cursor = conn.execute(
                "INSERT OR IGNORE INTO jobs(content_hash,content_id,scheduled_at,status,manifest_json,created_at,updated_at) "
                "VALUES(?,?,?,?,?,?,?)",
                (
                    manifest.content_hash,
                    manifest.content_id,
                    manifest.scheduled_datetime().isoformat().replace("+00:00", "Z"),
                    "QUEUED",
                    manifest.canonical_json(),
                    now,
                    now,
                ),
            )
            created = cursor.rowcount == 1
        self.event("JOB_ENQUEUED" if created else "JOB_DUPLICATE_SKIPPED", {"content_hash": manifest.content_hash}, manifest.content_id)
        return created

    def due_jobs(self, now: datetime | None = None, limit: int = 20) -> list[sqlite3.Row]:
        instant = (now or datetime.now(timezone.utc)).astimezone(timezone.utc).isoformat().replace("+00:00", "Z")
        with self.connection() as conn:
            return list(
                conn.execute(
                    "SELECT * FROM jobs WHERE status IN ('QUEUED','RETRY') AND attempts<3 AND scheduled_at<=? "
                    "ORDER BY scheduled_at ASC LIMIT ?",
                    (instant, limit),
                ).fetchall()
            )

    def get_job(self, content_hash: str) -> dict | None:
        with self.connection() as conn:
            row = conn.execute("SELECT * FROM jobs WHERE content_hash=?", (content_hash,)).fetchone()
        return dict(row) if row else None

    def publications_last_24h(self) -> int:
        cutoff = (datetime.now(timezone.utc) - timedelta(hours=24)).isoformat().replace("+00:00", "Z")
        with self.connection() as conn:
            row = conn.execute("SELECT COUNT(*) AS n FROM publications WHERE published_at>=?", (cutoff,)).fetchone()
        return int(row["n"]) if row else 0

    def update_job(self, content_hash: str, status: str, error: str | None = None, increment_attempt: bool = False) -> None:
        with self.connection() as conn:
            conn.execute(
                "UPDATE jobs SET status=?, last_error=?, attempts=attempts+?, updated_at=? WHERE content_hash=?",
                (status, error, 1 if increment_attempt else 0, utc_now(), content_hash),
            )

    def find_publication(self, content_hash: str) -> dict | None:
        with self.connection() as conn:
            row = conn.execute("SELECT * FROM publications WHERE content_hash=?", (content_hash,)).fetchone()
        return dict(row) if row else None

    def record_publication(self, manifest: ContentManifest, result: dict) -> None:
        media_id = str(result.get("media_id") or result.get("id") or "")
        if not media_id:
            raise ValueError("Risposta publish senza media_id")
        with self.connection() as conn:
            conn.execute(
                "INSERT OR IGNORE INTO publications(content_hash,content_id,media_id,container_id,permalink,published_at,response_json) "
                "VALUES(?,?,?,?,?,?,?)",
                (
                    manifest.content_hash,
                    manifest.content_id,
                    media_id,
                    result.get("container_id"),
                    result.get("permalink"),
                    result.get("published_at", utc_now()),
                    json.dumps(result, ensure_ascii=False, sort_keys=True),
                ),
            )
        self.event("PUBLISHED", result, manifest.content_id)

    def record_metrics(self, content_id: str, media_id: str, media_type: str, metrics: dict, score: float | None) -> None:
        captured_at = utc_now()
        with self.connection() as conn:
            conn.execute(
                "INSERT OR IGNORE INTO metric_snapshots(content_id,media_id,media_type,captured_at,metrics_json,quality_action_rate) "
                "VALUES(?,?,?,?,?,?)",
                (content_id, media_id, media_type, captured_at, json.dumps(metrics, sort_keys=True), score),
            )
        self.event("METRICS_CAPTURED", {"media_id": media_id, "media_type": media_type, "score": score}, content_id)

    def metric_rows_since(self, since_iso: str) -> list[dict]:
        with self.connection() as conn:
            rows = conn.execute(
                "SELECT * FROM metric_snapshots WHERE captured_at>=? ORDER BY captured_at DESC", (since_iso,)
            ).fetchall()
        return [dict(row) for row in rows]

    def event(self, event: str, payload: dict, content_id: str | None = None) -> None:
        with self.connection() as conn:
            conn.execute(
                "INSERT INTO events(ts,content_id,event,payload_json) VALUES(?,?,?,?)",
                (utc_now(), content_id, event, json.dumps(payload, ensure_ascii=False, sort_keys=True)),
            )
