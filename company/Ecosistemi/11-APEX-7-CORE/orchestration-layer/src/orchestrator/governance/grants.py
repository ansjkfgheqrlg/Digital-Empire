from __future__ import annotations

import asyncio
import hashlib
import secrets
from dataclasses import dataclass
from datetime import UTC, datetime, timedelta
from typing import Any, Protocol
from uuid import uuid4


class GrantDenied(PermissionError):
    pass


@dataclass(frozen=True)
class GrantBinding:
    tenant_id: str
    workflow_id: str
    task_id: str
    execution_token_hash: str
    audience: str = "tool-gateway"


@dataclass(frozen=True)
class GrantRecord:
    grant_id: str
    token_hash: str
    nonce_hash: str
    subject: str
    binding: GrantBinding
    capability_scope: str
    constraints: dict[str, Any]
    not_before: datetime
    expires_at: datetime
    consumed_at: datetime | None = None
    revoked_at: datetime | None = None


class CapabilityStore(Protocol):
    async def insert(self, record: GrantRecord) -> None: ...
    async def consume(
        self, token_hash: str, binding: GrantBinding, now: datetime
    ) -> GrantRecord | None: ...
    async def revoke_for_task(self, tenant_id: str, task_id: str, now: datetime) -> int: ...


class InMemoryCapabilityStore:
    """Concurrency-safe test/pilot store. Production uses PostgreSQL."""

    def __init__(self):
        self._records: dict[str, GrantRecord] = {}
        self._lock = asyncio.Lock()

    async def insert(self, record: GrantRecord) -> None:
        async with self._lock:
            if record.token_hash in self._records:
                raise ValueError("Duplicate capability token hash")
            self._records[record.token_hash] = record

    async def consume(
        self, token_hash: str, binding: GrantBinding, now: datetime
    ) -> GrantRecord | None:
        async with self._lock:
            record = self._records.get(token_hash)
            if record is None:
                return None
            if (
                record.binding != binding
                or record.consumed_at is not None
                or record.revoked_at is not None
                or now < record.not_before
                or now >= record.expires_at
            ):
                return None
            consumed = GrantRecord(**{**record.__dict__, "consumed_at": now})
            self._records[token_hash] = consumed
            return consumed

    async def revoke_for_task(self, tenant_id: str, task_id: str, now: datetime) -> int:
        count = 0
        async with self._lock:
            for token_hash, record in tuple(self._records.items()):
                if (
                    record.binding.tenant_id == tenant_id
                    and record.binding.task_id == task_id
                    and record.revoked_at is None
                    and record.consumed_at is None
                ):
                    self._records[token_hash] = GrantRecord(
                        **{**record.__dict__, "revoked_at": now}
                    )
                    count += 1
        return count


class CapabilityGrantService:
    MAX_TTL_SECONDS = 300

    def __init__(self, store: CapabilityStore):
        self.store = store

    async def issue(
        self,
        *,
        subject: str,
        binding: GrantBinding,
        capability_scope: str,
        constraints: dict[str, Any],
        ttl_seconds: int,
        now: datetime | None = None,
    ) -> tuple[str, GrantRecord]:
        if not 1 <= ttl_seconds <= self.MAX_TTL_SECONDS:
            raise GrantDenied("Grant TTL must be 1..300 seconds")
        if not subject or not capability_scope:
            raise GrantDenied("Grant subject and capability are required")
        if binding.audience != "tool-gateway":
            raise GrantDenied("Unsupported grant audience")
        current = now or datetime.now(UTC)
        token = secrets.token_urlsafe(32)
        nonce = secrets.token_urlsafe(18)
        record = GrantRecord(
            grant_id=str(uuid4()),
            token_hash=self.hash_secret(token),
            nonce_hash=self.hash_secret(nonce),
            subject=subject,
            binding=binding,
            capability_scope=capability_scope,
            constraints={**constraints, "audience": binding.audience},
            not_before=current,
            expires_at=current + timedelta(seconds=ttl_seconds),
        )
        await self.store.insert(record)
        return token, record

    async def consume(
        self,
        token: str,
        binding: GrantBinding,
        requested_capability: str,
        now: datetime | None = None,
    ) -> GrantRecord:
        if not token:
            raise GrantDenied("Missing capability token")
        record = await self.store.consume(
            self.hash_secret(token), binding, now or datetime.now(UTC)
        )
        if record is None:
            raise GrantDenied("Capability token invalid, expired, revoked or already consumed")
        if not scope_allows(record.capability_scope, requested_capability):
            raise GrantDenied("Capability scope does not allow the requested operation")
        return record

    async def revoke_task(self, tenant_id: str, task_id: str) -> int:
        return await self.store.revoke_for_task(tenant_id, task_id, datetime.now(UTC))

    @staticmethod
    def hash_secret(value: str) -> str:
        return "sha256:" + hashlib.sha256(value.encode("utf-8")).hexdigest()


def scope_allows(scope: str, requested: str) -> bool:
    if scope == requested:
        return True
    if scope.endswith("/**"):
        return requested.startswith(scope[:-2])
    return False
