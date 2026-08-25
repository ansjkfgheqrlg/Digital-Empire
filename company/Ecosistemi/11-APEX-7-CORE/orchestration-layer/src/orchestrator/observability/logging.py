from __future__ import annotations

import json
import re
from datetime import UTC, datetime
from typing import Any
from uuid import uuid4


PATTERNS = (
    (re.compile(r"\b[\w.+-]+@[\w-]+\.[A-Za-z]{2,}\b"), "EMAIL_REDACTED"),
    (re.compile(r"(?i)\bBearer\s+[A-Za-z0-9._-]+"), "Bearer TOKEN_REDACTED"),
    (re.compile(r'(?i)(["\']?(?:password|api[_-]?key|secret)["\']?\s*[:=]\s*)["\']?[^\s,"\']+["\']?'), r"\1REDACTED"),
    (re.compile(r"\b(?:\d[ -]*?){13,19}\b"), "CARD_REDACTED"),
)


def redact(value: str) -> str:
    result = value
    for pattern, replacement in PATTERNS:
        result = pattern.sub(replacement, result)
    return result


def redact_attributes(value: Any, key: str = "") -> Any:
    if key.casefold() in {"password", "secret", "api_key", "apikey", "token"}:
        return "REDACTED"
    if isinstance(value, dict):
        return {name: redact_attributes(item, str(name)) for name, item in value.items()}
    if isinstance(value, list):
        return [redact_attributes(item) for item in value]
    if isinstance(value, str):
        return redact(value)
    return value


class StructuredLogger:
    """Produces redacted JSON records; transport is supplied by the caller."""

    def record(
        self,
        *,
        level: str,
        event: str,
        workflow_id: str,
        trace_id: str,
        tenant_id: str,
        detail: str = "",
        attributes: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        if level not in {"DEBUG", "INFO", "WARN", "ERROR", "CRITICAL"}:
            raise ValueError("Invalid log level")
        safe_attributes = redact_attributes(attributes or {})
        return {
            "log_id": str(uuid4()),
            "timestamp": datetime.now(UTC).isoformat(),
            "level": level,
            "event": event,
            "workflow_id": workflow_id,
            "trace_id": trace_id,
            "tenant_id_hash": __import__("hashlib").sha256(tenant_id.encode()).hexdigest(),
            "detail": redact(detail),
            "attributes": safe_attributes,
        }
