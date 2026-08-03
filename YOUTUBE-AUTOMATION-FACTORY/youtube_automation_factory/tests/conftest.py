"""Fixture condivise. Nessun test tocca rete, browser o credenziali."""

from __future__ import annotations

from pathlib import Path

import pytest

from youtube_automation_factory.agents import (
    ProductionAgent,
    RegulatoryAgent,
    ResearchAgent,
    ReviewAgent,
    ScriptAgent,
    SeniorDecisionAgent,
)
from youtube_automation_factory.core.models import (
    CopyAsset,
    ScriptAsset,
    ThumbnailAsset,
    VideoCandidate,
    WorkflowRun,
)
from youtube_automation_factory.core.workflow import YouTubeFactoryWorkflow
from youtube_automation_factory.integrations.flik_adapter import MockFlikAdapter
from youtube_automation_factory.services.originality_service import OriginalityService

NICHE = "Dose Mentale"

SCRIPT_BODY = " ".join(
    [
        "Testo originale scritto per la suite di test, sufficientemente lungo da superare la",
        "soglia minima di parole richiesta dai validatori. Serve a verificare che i controlli",
        "sulla lunghezza e sulla presenza del corpo funzionino davvero, senza dipendere da",
        "contenuti esterni o da materiale di terzi. Ogni frase e' scritta qui e non proviene",
        "da nessun transcript. La ripetizione serve solo a raggiungere il conteggio minimo",
        "di cinquanta parole previsto dalla regola di validazione dello script.",
    ]
)


@pytest.fixture
def niche() -> str:
    return NICHE


@pytest.fixture
def reports_dir(tmp_path: Path) -> Path:
    d = tmp_path / "reports"
    d.mkdir()
    return d


@pytest.fixture
def run() -> WorkflowRun:
    return WorkflowRun(niche=NICHE)


@pytest.fixture
def workflow(run: WorkflowRun) -> YouTubeFactoryWorkflow:
    return YouTubeFactoryWorkflow(run, NICHE)


@pytest.fixture
def candidate() -> VideoCandidate:
    return VideoCandidate(
        title="Titolo di riferimento",
        url="https://www.youtube.com/watch?v=test00000001",
        channel="Canale di test",
        topic="Argomento di test",
        views=50_000,
        niche=NICHE,
    )


@pytest.fixture
def script(run: WorkflowRun, candidate: VideoCandidate) -> ScriptAsset:
    return ScriptAsset(
        workflow_id=run.id,
        author="script-test",
        brief="Brief editoriale proprio.",
        title="Titolo originale",
        body=SCRIPT_BODY,
        reference_candidate_id=candidate.id,
    )


@pytest.fixture
def copy_asset(run: WorkflowRun) -> CopyAsset:
    return CopyAsset(
        workflow_id=run.id,
        author="copy-test",
        brief="Brief copy proprio.",
        headline="Headline originale",
        body="Testo del copy scritto per il test.",
    )


@pytest.fixture
def thumbnail(run: WorkflowRun) -> ThumbnailAsset:
    return ThumbnailAsset(
        workflow_id=run.id,
        author="thumb-test",
        brief="Brief copertina proprio.",
        concept="Concept originale",
    )


@pytest.fixture
def originality() -> OriginalityService:
    return OriginalityService()


@pytest.fixture
def researcher() -> ResearchAgent:
    return ResearchAgent("research-test", NICHE)


@pytest.fixture
def reviewer() -> ReviewAgent:
    return ReviewAgent("review-test", NICHE)


@pytest.fixture
def senior() -> SeniorDecisionAgent:
    return SeniorDecisionAgent("senior-test", NICHE)


@pytest.fixture
def scripter() -> ScriptAgent:
    return ScriptAgent("script-test", NICHE)


@pytest.fixture
def adapter() -> MockFlikAdapter:
    return MockFlikAdapter()


@pytest.fixture
def producer(adapter: MockFlikAdapter) -> ProductionAgent:
    return ProductionAgent("production-test", NICHE, adapter)


@pytest.fixture
def regulator(originality: OriginalityService) -> RegulatoryAgent:
    return RegulatoryAgent("regulator-test", NICHE, originality)
