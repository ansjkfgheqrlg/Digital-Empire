"""Agente operativo di produzione: prepara il job solo per script approvati."""

from __future__ import annotations

import logging

from ..core.enums import AgentLevel
from ..core.exceptions import ApprovalRequiredError
from ..core.models import ProductionJob, ScriptAsset
from ..integrations.flik_adapter import FlikAdapter, ProductionResult
from .base import BaseAgent

logger = logging.getLogger(__name__)

#: Voci di default del job. Sovrascrivibili per singolo workflow.
DEFAULT_VOICE_AGENTS: tuple[str, ...] = ("narratore-principale",)


class ProductionAgent(BaseAgent):
    """Ponte fra lo script approvato e l'adapter di produzione."""

    level = AgentLevel.OPERATIONAL

    def __init__(self, name: str, primary_niche: str, adapter: FlikAdapter) -> None:
        super().__init__(name, primary_niche)
        self.adapter = adapter

    def create_job(
        self,
        *,
        workflow_id: str,
        script: ScriptAsset,
        voice_agents: list[str] | None = None,
        subtitles_enabled: bool = True,
        subtitle_preset: str | None = None,
    ) -> ProductionJob:
        """Crea il job. Fallisce se lo script non e' approvato."""
        if not script.approved:
            raise ApprovalRequiredError("Produzione video", "SENIOR")
        job = self.adapter.submit_script(
            script,
            workflow_id=workflow_id,
            voice_agents=list(voice_agents or DEFAULT_VOICE_AGENTS),
            subtitles_enabled=subtitles_enabled,
            subtitle_preset=subtitle_preset,
        )
        logger.info("[%s] job %s creato (adapter=%s)", self.name, job.id, self.adapter.name)
        return job

    def wait_for_result(self, job: ProductionJob) -> ProductionResult:
        """Recupera il risultato e allinea il job locale."""
        result = self.adapter.fetch_result(job.id)
        job.status = result.status
        job.output_path = result.output_path
        job.is_real_render = result.is_real_render
        job.messages.extend(result.messages)
        return result
