"""Adapter di produzione: solo mock, nessun servizio esterno."""

from __future__ import annotations

import pytest

from youtube_automation_factory.core.enums import ProductionJobStatus
from youtube_automation_factory.core.exceptions import (
    ApprovalRequiredError,
    FlikAdapterError,
)
from youtube_automation_factory.integrations.flik_adapter import (
    FlikAdapter,
    MockFlikAdapter,
    get_adapter,
)


def test_interfaccia_astratta_non_istanziabile() -> None:
    with pytest.raises(TypeError):
        FlikAdapter()  # type: ignore[abstract]


def test_get_adapter_restituisce_il_mock() -> None:
    assert isinstance(get_adapter("mock"), MockFlikAdapter)
    assert isinstance(get_adapter(""), MockFlikAdapter)


def test_get_adapter_rifiuta_adapter_inesistenti() -> None:
    with pytest.raises(FlikAdapterError, match="non disponibile"):
        get_adapter("servizio-reale")


def test_mock_rifiuta_script_non_approvato(adapter: MockFlikAdapter, script, run) -> None:
    with pytest.raises(FlikAdapterError, match="non e' approvato"):
        adapter.submit_script(
            script, workflow_id=run.id, voice_agents=["v"], subtitles_enabled=True
        )


def _approva(script, originality) -> None:
    originality.apply(script)
    script.approved = True


def test_mock_crea_job_da_script_approvato(
    adapter: MockFlikAdapter, script, run, originality
) -> None:
    _approva(script, originality)
    job = adapter.submit_script(
        script,
        workflow_id=run.id,
        voice_agents=["narratore"],
        subtitles_enabled=True,
        subtitle_preset="standard",
    )
    assert job.status is ProductionJobStatus.CREATED
    assert job.is_real_render is False
    assert job.subtitles_enabled is True
    assert any("nessun video reale" in m.lower() for m in job.messages)


def test_mock_avanza_negli_stati(adapter: MockFlikAdapter, script, run, originality) -> None:
    _approva(script, originality)
    job = adapter.submit_script(
        script, workflow_id=run.id, voice_agents=["v"], subtitles_enabled=True
    )
    assert adapter.get_job_status(job.id) is ProductionJobStatus.SUBMITTED
    assert adapter.get_job_status(job.id) is ProductionJobStatus.PROCESSING
    assert adapter.get_job_status(job.id) is ProductionJobStatus.READY


def test_mock_fetch_result_non_dichiara_video_reali(
    adapter: MockFlikAdapter, script, run, originality
) -> None:
    _approva(script, originality)
    job = adapter.submit_script(
        script, workflow_id=run.id, voice_agents=["v"], subtitles_enabled=True
    )
    result = adapter.fetch_result(job.id)
    assert result.status is ProductionJobStatus.READY
    assert result.is_real_render is False
    assert result.output_path.startswith("mock://")


def test_mock_job_sconosciuto(adapter: MockFlikAdapter) -> None:
    with pytest.raises(FlikAdapterError, match="sconosciuto"):
        adapter.get_job_status("inesistente")


def test_production_agent_richiede_approvazione(producer, script, run) -> None:
    with pytest.raises(ApprovalRequiredError):
        producer.create_job(workflow_id=run.id, script=script)


def test_production_agent_allinea_il_job(producer, script, run, originality) -> None:
    _approva(script, originality)
    job = producer.create_job(workflow_id=run.id, script=script)
    result = producer.wait_for_result(job)
    assert job.status is ProductionJobStatus.READY
    assert job.output_path == result.output_path
    assert job.is_real_render is False
