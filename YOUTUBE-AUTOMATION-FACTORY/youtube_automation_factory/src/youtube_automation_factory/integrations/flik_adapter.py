"""Integrazione con il servizio di produzione video ("Flik").

## Perche' qui non c'e' un client HTTP

In questo repository **non esiste una specifica API verificata** per Flik. Inventare endpoint,
nomi di campo o formati di risposta produrrebbe codice che sembra funzionante e fallisce al
primo contatto con il servizio reale. Perciò:

* ``FlikAdapter`` e' un'interfaccia astratta che descrive il *contratto* di cui la fabbrica ha
  bisogno;
* ``MockFlikAdapter`` e' un'implementazione locale per sviluppo, demo e test, che **non**
  produce alcun video reale e lo dichiara esplicitamente in ogni output;
* un adapter reale andra' aggiunto quando la documentazione dell'API sara' disponibile,
  implementando la stessa interfaccia senza toccare il resto del sistema.
"""

from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass, field

from ..core.enums import ProductionJobStatus
from ..core.exceptions import FlikAdapterError
from ..core.models import ProductionJob, ScriptAsset, utc_now

logger = logging.getLogger(__name__)


@dataclass
class ProductionResult:
    """Risultato restituito da un adapter al termine della lavorazione."""

    job_id: str
    status: ProductionJobStatus
    is_real_render: bool
    output_path: str | None = None
    messages: list[str] = field(default_factory=list)


class FlikAdapter(ABC):
    """Contratto minimo per un fornitore di produzione video."""

    name: str = "abstract"

    @abstractmethod
    def submit_script(
        self,
        script: ScriptAsset,
        *,
        workflow_id: str,
        voice_agents: list[str],
        subtitles_enabled: bool,
        subtitle_preset: str | None = None,
    ) -> ProductionJob:
        """Crea un job a partire da uno script **gia' approvato**."""

    @abstractmethod
    def get_job_status(self, job_id: str) -> ProductionJobStatus:
        """Stato corrente del job."""

    @abstractmethod
    def fetch_result(self, job_id: str) -> ProductionResult:
        """Risultato finale del job."""


class MockFlikAdapter(FlikAdapter):
    """Adapter locale deterministico. Non contatta nessun servizio esterno.

    Il ciclo di stati e' ``CREATED → SUBMITTED → PROCESSING → READY`` e avanza a ogni
    interrogazione, cosi' i test possono osservare la progressione senza attese reali.
    """

    name = "mock"

    #: Progressione degli stati simulati.
    _SEQUENCE: tuple[ProductionJobStatus, ...] = (
        ProductionJobStatus.SUBMITTED,
        ProductionJobStatus.PROCESSING,
        ProductionJobStatus.READY,
    )

    def __init__(self) -> None:
        self._jobs: dict[str, ProductionJob] = {}
        self._steps: dict[str, int] = {}

    def submit_script(
        self,
        script: ScriptAsset,
        *,
        workflow_id: str,
        voice_agents: list[str],
        subtitles_enabled: bool,
        subtitle_preset: str | None = None,
    ) -> ProductionJob:
        if not script.approved:
            raise FlikAdapterError(
                "Lo script non e' approvato: la produzione non puo' essere avviata."
            )
        if not script.originality_checked:
            raise FlikAdapterError(
                "Lo script non ha superato il controllo di originalita'."
            )

        job = ProductionJob(
            workflow_id=workflow_id,
            script_id=script.id,
            adapter=self.name,
            status=ProductionJobStatus.CREATED,
            voice_agents=list(voice_agents),
            subtitles_enabled=subtitles_enabled,
            subtitle_preset=subtitle_preset,
            is_real_render=False,
            messages=[
                "Job simulato: nessun video reale e' stato prodotto.",
                f"Voci richieste: {', '.join(voice_agents) or 'nessuna'}.",
                f"Sottotitoli: {'attivi' if subtitles_enabled else 'disattivi'}.",
            ],
        )
        self._jobs[job.id] = job
        self._steps[job.id] = 0
        logger.info("[mock] job %s creato per lo script %s", job.id, script.id)
        return job

    def get_job_status(self, job_id: str) -> ProductionJobStatus:
        job = self._jobs.get(job_id)
        if job is None:
            raise FlikAdapterError(f"Job sconosciuto: {job_id}")
        indice = self._steps[job_id]
        if indice < len(self._SEQUENCE):
            job.status = self._SEQUENCE[indice]
            self._steps[job_id] = indice + 1
            job.updated_at = utc_now()
        return job.status

    def fetch_result(self, job_id: str) -> ProductionResult:
        job = self._jobs.get(job_id)
        if job is None:
            raise FlikAdapterError(f"Job sconosciuto: {job_id}")
        while job.status is not ProductionJobStatus.READY:
            self.get_job_status(job_id)

        job.output_path = f"mock://production/{job.id}"
        return ProductionResult(
            job_id=job.id,
            status=job.status,
            is_real_render=False,
            output_path=job.output_path,
            messages=[
                "Output simulato prodotto localmente.",
                "Nessun file video reale esiste su disco.",
            ],
        )


def get_adapter(name: str) -> FlikAdapter:
    """Restituisce l'adapter richiesto.

    Solo ``mock`` e' disponibile: un adapter reale richiede una specifica API verificata,
    che questo repository non possiede.
    """
    chiave = (name or "mock").strip().lower()
    if chiave == "mock":
        return MockFlikAdapter()
    raise FlikAdapterError(
        f"Adapter '{name}' non disponibile. In questo repository esiste solo l'adapter "
        f"'mock': un'integrazione reale va implementata sulla base della documentazione "
        f"ufficiale del fornitore, che qui non e' presente."
    )
