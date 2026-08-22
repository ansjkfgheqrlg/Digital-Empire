"""Canonical serialization and digest helpers."""

from __future__ import annotations

import hashlib
import json
from typing import Any

from pydantic import BaseModel


def canonical_bytes(value: BaseModel | dict[str, Any]) -> bytes:
    """Serialize JSON deterministically for hashing and signature verification."""

    data = value.model_dump(mode="json") if isinstance(value, BaseModel) else value
    return json.dumps(
        data,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    ).encode("utf-8")


def sha256_hex(value: bytes) -> str:
    """Return a lowercase SHA-256 digest."""

    return hashlib.sha256(value).hexdigest()
