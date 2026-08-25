from __future__ import annotations

import hashlib
import json
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class CheckpointRecord:
    checkpoint_id: str
    workflow_id: str
    tenant_id: str
    workflow_type: str
    status: str
    timestamp: str
    event_count: int
    data_hash: str
    summary: str


class CheckpointWriter:
    def __init__(self, checkpoints_dir: Path):
        self.checkpoints_dir = checkpoints_dir
        self.checkpoints_dir.mkdir(parents=True, exist_ok=True)

    def write_checkpoint(
        self,
        *,
        checkpoint_id: str,
        workflow_id: str,
        tenant_id: str,
        workflow_type: str,
        status: str,
        event_count: int,
        context: dict[str, Any],
        summary: str = "",
    ) -> CheckpointRecord:
        now = datetime.now(timezone.utc).isoformat()
        context_bytes = json.dumps(context, sort_keys=True).encode("utf-8")
        data_hash = "sha256:" + hashlib.sha256(context_bytes).hexdigest()

        record = CheckpointRecord(
            checkpoint_id=checkpoint_id,
            workflow_id=workflow_id,
            tenant_id=tenant_id,
            workflow_type=workflow_type,
            status=status,
            timestamp=now,
            event_count=event_count,
            data_hash=data_hash,
            summary=summary,
        )

        target_file = self.checkpoints_dir / f"{checkpoint_id}.json"
        target_file.write_text(json.dumps(asdict(record), indent=2), encoding="utf-8")
        return record

    def get_checkpoint(self, checkpoint_id: str) -> CheckpointRecord | None:
        target_file = self.checkpoints_dir / f"{checkpoint_id}.json"
        if not target_file.exists():
            return None
        data = json.loads(target_file.read_text(encoding="utf-8"))
        return CheckpointRecord(**data)

    def list_checkpoints(self) -> list[str]:
        return [p.stem for p in self.checkpoints_dir.glob("*.json")]
