from __future__ import annotations

import hashlib
from pathlib import Path
from typing import Any

from .catalog import (
    CompensationResult,
    ReconciliationResult,
    ReconciliationStatus,
)


class ArtifactCompensation:
    """Reconcile/delete a local pilot artifact only when the expected hash matches."""

    def __init__(self, artifact_root: Path):
        self.root = artifact_root.resolve()

    def _path(self, context: dict[str, Any]) -> Path:
        relative = str(context.get("path", ""))
        if not relative or Path(relative).is_absolute():
            raise ValueError("Artifact path must be relative")
        path = (self.root / relative).resolve()
        if not path.is_relative_to(self.root):
            raise ValueError("Artifact path escapes root")
        return path

    async def reconcile(self, context: dict[str, Any]) -> ReconciliationResult:
        path = self._path(context)
        if not path.exists():
            return ReconciliationResult(ReconciliationStatus.ABSENT, {"path": str(path)})
        if not path.is_file() or path.is_symlink():
            return ReconciliationResult(
                ReconciliationStatus.UNKNOWN,
                {"path": str(path), "reason": "not a regular immutable artifact"},
            )
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        expected = context.get("expected_sha256")
        if not expected or digest != expected:
            return ReconciliationResult(
                ReconciliationStatus.UNKNOWN,
                {"path": str(path), "actual_sha256": digest, "expected_sha256": expected},
            )
        return ReconciliationResult(
            ReconciliationStatus.PRESENT,
            {"path": str(path), "sha256": digest},
        )

    async def compensate(self, context: dict[str, Any]) -> CompensationResult:
        reconciliation = await self.reconcile(context)
        if reconciliation.status is not ReconciliationStatus.PRESENT:
            return CompensationResult(
                False,
                reconciliation.evidence,
                f"cannot compensate artifact in state {reconciliation.status.value}",
            )
        if context.get("referenced", False):
            return CompensationResult(
                False,
                reconciliation.evidence,
                "artifact is referenced and cannot be deleted automatically",
            )
        path = self._path(context)
        path.unlink()
        return CompensationResult(True, {**reconciliation.evidence, "deleted": True})
