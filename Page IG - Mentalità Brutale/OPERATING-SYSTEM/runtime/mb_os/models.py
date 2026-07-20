from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

SUPPORTED_FORMATS = {"IMAGE", "CAROUSEL", "REEL"}


@dataclass(frozen=True)
class MediaAsset:
    path: str | None = None
    public_url: str | None = None
    alt_text: str | None = None
    media_type: str | None = None

    @classmethod
    def from_dict(cls, value: dict[str, Any]) -> "MediaAsset":
        return cls(
            path=str(value["path"]) if value.get("path") else None,
            public_url=str(value["public_url"]) if value.get("public_url") else None,
            alt_text=str(value["alt_text"]) if value.get("alt_text") else None,
            media_type=str(value["media_type"]).upper() if value.get("media_type") else None,
        )

    def identity(self) -> dict[str, Any]:
        return {
            "path": self.path,
            "public_url": self.public_url,
            "alt_text": self.alt_text,
            "media_type": self.media_type,
        }


@dataclass(frozen=True)
class ContentManifest:
    content_id: str
    brand: str
    format: str
    caption: str
    scheduled_at: str
    media: tuple[MediaAsset, ...]
    experiment: dict[str, Any] = field(default_factory=dict)
    quality_evidence: dict[str, str] = field(default_factory=dict)
    rights: dict[str, Any] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)
    source_path: Path | None = None

    @classmethod
    def from_dict(cls, value: dict[str, Any], source_path: Path | None = None) -> "ContentManifest":
        return cls(
            content_id=str(value.get("content_id", "")).strip(),
            brand=str(value.get("brand", "")).strip(),
            format=str(value.get("format", "")).strip().upper(),
            caption=str(value.get("caption", "")),
            scheduled_at=str(value.get("scheduled_at", "")).strip(),
            media=tuple(MediaAsset.from_dict(item) for item in value.get("media", [])),
            experiment=dict(value.get("experiment", {})),
            quality_evidence={str(k): str(v).upper() for k, v in value.get("quality_evidence", {}).items()},
            rights=dict(value.get("rights", {})),
            metadata=dict(value.get("metadata", {})),
            source_path=source_path,
        )

    @classmethod
    def load(cls, path: str | Path) -> "ContentManifest":
        source = Path(path).expanduser().resolve()
        value = json.loads(source.read_text(encoding="utf-8"))
        if not isinstance(value, dict):
            raise ValueError("Il manifest deve essere un oggetto JSON")
        return cls.from_dict(value, source)

    def scheduled_datetime(self) -> datetime:
        if not self.scheduled_at:
            return datetime.now(timezone.utc)
        value = self.scheduled_at.replace("Z", "+00:00")
        parsed = datetime.fromisoformat(value)
        if parsed.tzinfo is None:
            raise ValueError("scheduled_at deve includere il timezone")
        return parsed.astimezone(timezone.utc)

    def canonical_dict(self) -> dict[str, Any]:
        return {
            "content_id": self.content_id,
            "brand": self.brand,
            "format": self.format,
            "caption": self.caption,
            "scheduled_at": self.scheduled_at,
            "media": [item.identity() for item in self.media],
            "experiment": self.experiment,
            "quality_evidence": self.quality_evidence,
            "rights": self.rights,
            "metadata": self.metadata,
        }

    def canonical_json(self) -> str:
        return json.dumps(self.canonical_dict(), sort_keys=True, ensure_ascii=False, separators=(",", ":"))

    def publication_identity(self) -> dict[str, Any]:
        """Stable identity for side effects; scheduling/experiments must not permit a duplicate publish."""
        return {
            "content_id": self.content_id,
            "brand": self.brand,
            "format": self.format,
            "caption": self.caption,
            "media": [item.identity() for item in self.media],
        }

    @property
    def content_hash(self) -> str:
        payload = json.dumps(self.publication_identity(), sort_keys=True, ensure_ascii=False, separators=(",", ":"))
        return hashlib.sha256(payload.encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class GateResult:
    gate: str
    status: str
    message: str

    def as_dict(self) -> dict[str, str]:
        return {"gate": self.gate, "status": self.status, "message": self.message}
