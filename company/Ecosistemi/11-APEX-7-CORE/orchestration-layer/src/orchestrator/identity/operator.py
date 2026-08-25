from __future__ import annotations

import hashlib
import secrets
from dataclasses import dataclass
from datetime import UTC, datetime, timedelta

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey


class IdentityError(PermissionError):
    pass


@dataclass(frozen=True)
class Operator:
    operator_id: str
    public_key: Ed25519PublicKey
    roles: frozenset[str]
    enabled: bool = True


@dataclass(frozen=True)
class Challenge:
    challenge_id: str
    operator_id: str
    nonce: bytes
    expires_at: datetime
    consumed: bool = False


@dataclass(frozen=True)
class AuthContext:
    operator_id: str
    roles: frozenset[str]
    authenticated_at: datetime
    method: str = "ED25519_CHALLENGE"


class OperatorRegistry:
    def __init__(self):
        self._operators: dict[str, Operator] = {}

    def register_raw_public_key(
        self, operator_id: str, public_key_raw: bytes, roles: set[str]
    ) -> None:
        if not operator_id or len(public_key_raw) != 32 or not roles:
            raise ValueError("Operator id, 32-byte public key and roles are required")
        if operator_id in self._operators:
            raise ValueError("Operator already registered")
        self._operators[operator_id] = Operator(
            operator_id,
            Ed25519PublicKey.from_public_bytes(public_key_raw),
            frozenset(roles),
        )

    def require(self, operator_id: str) -> Operator:
        operator = self._operators.get(operator_id)
        if operator is None or not operator.enabled:
            raise IdentityError("Unknown or disabled operator")
        return operator


class OperatorIdentityService:
    MAX_TTL_SECONDS = 120

    def __init__(self, registry: OperatorRegistry):
        self.registry = registry
        self._challenges: dict[str, Challenge] = {}

    def create_challenge(
        self, operator_id: str, *, ttl_seconds: int = 60, now: datetime | None = None
    ) -> tuple[str, bytes]:
        self.registry.require(operator_id)
        if not 1 <= ttl_seconds <= self.MAX_TTL_SECONDS:
            raise IdentityError("Challenge TTL must be 1..120 seconds")
        current = now or datetime.now(UTC)
        nonce = secrets.token_bytes(32)
        challenge_id = secrets.token_urlsafe(18)
        self._challenges[challenge_id] = Challenge(
            challenge_id,
            operator_id,
            nonce,
            current + timedelta(seconds=ttl_seconds),
        )
        message = self._message(challenge_id, operator_id, nonce)
        return challenge_id, message

    def verify(
        self,
        challenge_id: str,
        operator_id: str,
        signature: bytes,
        *,
        now: datetime | None = None,
    ) -> AuthContext:
        current = now or datetime.now(UTC)
        challenge = self._challenges.get(challenge_id)
        if (
            challenge is None
            or challenge.operator_id != operator_id
            or challenge.consumed
            or current >= challenge.expires_at
        ):
            raise IdentityError("Challenge invalid, expired or consumed")
        operator = self.registry.require(operator_id)
        message = self._message(challenge_id, operator_id, challenge.nonce)
        try:
            operator.public_key.verify(signature, message)
        except InvalidSignature as exc:
            raise IdentityError("Invalid operator signature") from exc
        self._challenges[challenge_id] = Challenge(
            challenge.challenge_id,
            challenge.operator_id,
            challenge.nonce,
            challenge.expires_at,
            True,
        )
        return AuthContext(operator_id, operator.roles, current)

    @staticmethod
    def _message(challenge_id: str, operator_id: str, nonce: bytes) -> bytes:
        return b"OCP-OPERATOR-V1\x00" + challenge_id.encode() + b"\x00" + operator_id.encode() + b"\x00" + nonce
