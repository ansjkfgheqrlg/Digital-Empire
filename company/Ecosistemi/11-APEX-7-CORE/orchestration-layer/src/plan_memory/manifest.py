from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from pathlib import Path


class PlanMemoryError(RuntimeError):
    pass


class IntegrityError(PlanMemoryError):
    pass


@dataclass(frozen=True)
class PlanRecord:
    level: int
    path: str
    status: str
    sha256: str
    supersedes: tuple[int, ...]

    @property
    def is_approved(self) -> bool:
        return self.status == "APPROVED"


class PlanManifest:
    ALLOWED_STATUSES = {"APPROVED", "SUPERSEDED", "PROPOSED", "REJECTED"}

    def __init__(self, root: Path, records: tuple[PlanRecord, ...]):
        self.root = root
        self.records = records

    @classmethod
    def load(cls, root: Path, manifest_path: Path | None = None) -> "PlanManifest":
        path = manifest_path or root / "memory_store" / "plans" / "manifest.json"
        try:
            raw = json.loads(path.read_text(encoding="utf-8"))
        except (FileNotFoundError, json.JSONDecodeError) as exc:
            raise PlanMemoryError(f"Invalid or missing plan manifest: {path}") from exc

        records = tuple(
            PlanRecord(
                level=int(item["level"]),
                path=item["path"],
                status=item["status"],
                sha256=item["sha256"],
                supersedes=tuple(int(value) for value in item.get("supersedes", [])),
            )
            for item in raw.get("plans", [])
        )
        manifest = cls(root, records)
        manifest.validate()
        return manifest

    @staticmethod
    def hash_file(path: Path) -> str:
        digest = hashlib.sha256()
        with path.open("rb") as stream:
            for chunk in iter(lambda: stream.read(65536), b""):
                digest.update(chunk)
        return digest.hexdigest()

    def validate(self) -> None:
        if len(self.records) != 7:
            raise PlanMemoryError("Manifest must contain exactly seven plan levels")
        levels = [record.level for record in self.records]
        if sorted(levels) != list(range(1, 8)) or len(set(levels)) != 7:
            raise PlanMemoryError("Plan levels must be unique and cover 1..7")
        approved = [record for record in self.records if record.is_approved]
        if not approved:
            raise PlanMemoryError("At least one plan must be APPROVED")
        if max(record.level for record in approved) != 7:
            raise PlanMemoryError("Level 7 must be the highest approved authority")

        for record in self.records:
            if record.status not in self.ALLOWED_STATUSES:
                raise PlanMemoryError(f"Invalid status for level {record.level}: {record.status}")
            path = (self.root / record.path).resolve()
            if self.root.resolve() not in path.parents:
                raise PlanMemoryError(f"Plan path escapes project root: {record.path}")
            if not path.is_file():
                raise PlanMemoryError(f"Plan file missing: {record.path}")
            actual = self.hash_file(path)
            if actual != record.sha256:
                raise IntegrityError(
                    f"Hash mismatch for {record.path}: expected {record.sha256}, got {actual}"
                )

    def authority(self, record: PlanRecord) -> tuple[int, int]:
        status_rank = {"APPROVED": 3, "SUPERSEDED": 2, "PROPOSED": 1, "REJECTED": 0}
        return status_rank[record.status], record.level
