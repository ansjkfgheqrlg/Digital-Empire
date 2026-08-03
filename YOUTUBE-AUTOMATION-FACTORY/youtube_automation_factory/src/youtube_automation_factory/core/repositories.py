"""Persistenza dei workflow.

Due implementazioni: una in memoria (test) e una su file JSON (CLI demo). L'interfaccia e'
un ``Protocol``, cosi' sostituire lo storage non richiede toccare gli agenti.
"""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Protocol

from .models import WorkflowRun

logger = logging.getLogger(__name__)


class WorkflowRepository(Protocol):
    """Contratto minimo di persistenza."""

    def save(self, run: WorkflowRun) -> None: ...

    def get(self, run_id: str) -> WorkflowRun | None: ...

    def list_ids(self) -> list[str]: ...


class InMemoryWorkflowRepository:
    """Storage volatile, usato dai test."""

    def __init__(self) -> None:
        self._items: dict[str, WorkflowRun] = {}

    def save(self, run: WorkflowRun) -> None:
        self._items[run.id] = run

    def get(self, run_id: str) -> WorkflowRun | None:
        return self._items.get(run_id)

    def list_ids(self) -> list[str]:
        return sorted(self._items)


class JsonFileWorkflowRepository:
    """Storage su file JSON, un file per workflow."""

    def __init__(self, directory: Path) -> None:
        self.directory = directory
        self.directory.mkdir(parents=True, exist_ok=True)

    def _path(self, run_id: str) -> Path:
        return self.directory / f"workflow-{run_id}.json"

    def save(self, run: WorkflowRun) -> None:
        path = self._path(run.id)
        path.write_text(run.model_dump_json(indent=2), encoding="utf-8")
        logger.debug("Workflow %s salvato in %s", run.id, path)

    def get(self, run_id: str) -> WorkflowRun | None:
        path = self._path(run_id)
        if not path.exists():
            return None
        try:
            return WorkflowRun.model_validate_json(path.read_text(encoding="utf-8"))
        except (ValueError, json.JSONDecodeError) as exc:
            logger.error("Workflow %s non leggibile: %s", run_id, exc)
            return None

    def list_ids(self) -> list[str]:
        file = self.directory.glob("workflow-*.json")
        return sorted(p.stem.removeprefix("workflow-") for p in file)
