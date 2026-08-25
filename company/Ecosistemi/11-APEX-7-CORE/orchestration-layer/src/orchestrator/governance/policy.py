from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum
from typing import Any

import httpx


class PolicyEffect(StrEnum):
    ALLOW = "ALLOW"
    DENY = "DENY"
    REQUIRE_APPROVAL = "REQUIRE_APPROVAL"


@dataclass(frozen=True)
class PolicyDecision:
    effect: PolicyEffect
    reasons: tuple[str, ...]
    policy_bundle_hash: str

    @property
    def allowed(self) -> bool:
        return self.effect is PolicyEffect.ALLOW


class OpaPolicyClient:
    """Fail-closed OPA adapter; malformed or unavailable policy never allows."""

    def __init__(
        self,
        base_url: str,
        policy_bundle_hash: str,
        *,
        timeout_seconds: float = 2.0,
        transport: httpx.AsyncBaseTransport | None = None,
    ):
        self.endpoint = base_url.rstrip("/") + "/v1/data/orchestration/authorization/decision"
        self.policy_bundle_hash = policy_bundle_hash
        self.client = httpx.AsyncClient(timeout=timeout_seconds, transport=transport)

    async def close(self) -> None:
        await self.client.aclose()

    async def evaluate(self, policy_input: dict[str, Any]) -> PolicyDecision:
        try:
            response = await self.client.post(self.endpoint, json={"input": policy_input})
            response.raise_for_status()
            body = response.json()
            result = body.get("result")
            if not isinstance(result, dict):
                raise ValueError("OPA result is missing")
            effect = PolicyEffect(result["effect"])
            reasons = result.get("reasons")
            if not isinstance(reasons, list) or not reasons or not all(
                isinstance(reason, str) for reason in reasons
            ):
                raise ValueError("OPA reasons are invalid")
            return PolicyDecision(effect, tuple(reasons), self.policy_bundle_hash)
        except Exception as exc:
            return PolicyDecision(
                PolicyEffect.DENY,
                ("POL_OPA_UNAVAILABLE_OR_INVALID", type(exc).__name__),
                self.policy_bundle_hash,
            )
