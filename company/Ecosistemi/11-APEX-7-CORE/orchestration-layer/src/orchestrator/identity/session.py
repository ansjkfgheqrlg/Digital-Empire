from __future__ import annotations

import hashlib
import secrets
from dataclasses import dataclass
from datetime import UTC, datetime, timedelta

from .operator import AuthContext, IdentityError


@dataclass(frozen=True)
class SessionRecord:
    token_hash: str
    auth: AuthContext
    expires_at: datetime
    revoked: bool = False


class SessionService:
    def __init__(self, ttl_seconds: int = 900):
        if not 60 <= ttl_seconds <= 3600:
            raise ValueError("Session TTL must be 60..3600 seconds")
        self.ttl_seconds = ttl_seconds
        self._sessions: dict[str, SessionRecord] = {}

    def issue(self, auth: AuthContext, now: datetime | None = None) -> str:
        current = now or datetime.now(UTC)
        token = secrets.token_urlsafe(32)
        token_hash = self._hash(token)
        self._sessions[token_hash] = SessionRecord(
            token_hash, auth, current + timedelta(seconds=self.ttl_seconds)
        )
        return token

    def authenticate(self, token: str, now: datetime | None = None) -> AuthContext:
        if not token:
            raise IdentityError("Missing session token")
        record = self._sessions.get(self._hash(token))
        current = now or datetime.now(UTC)
        if record is None or record.revoked or current >= record.expires_at:
            raise IdentityError("Invalid, expired or revoked session")
        return record.auth

    def revoke(self, token: str) -> None:
        token_hash = self._hash(token)
        record = self._sessions.get(token_hash)
        if record:
            self._sessions[token_hash] = SessionRecord(
                record.token_hash, record.auth, record.expires_at, True
            )

    @staticmethod
    def _hash(token: str) -> str:
        return "sha256:" + hashlib.sha256(token.encode()).hexdigest()
