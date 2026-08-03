"""Report Markdown, nomi file sicuri e demo end-to-end."""

from __future__ import annotations

from pathlib import Path

from youtube_automation_factory.core.enums import WorkflowState
from youtube_automation_factory.core.reporting import ReportingService, safe_filename
from youtube_automation_factory.core.repositories import (
    InMemoryWorkflowRepository,
    JsonFileWorkflowRepository,
)
from youtube_automation_factory.demo import run_demo_workflow, run_side_analyses


def test_safe_filename_rimuove_caratteri_pericolosi() -> None:
    nome = safe_filename("../../etc", "pass wd:1")
    assert "/" not in nome and "\\" not in nome and ".." not in nome
    assert nome.startswith("etc")


def test_report_candidato_contiene_i_campi_obbligatori(
    reports_dir: Path, run, candidate
) -> None:
    run.candidate = candidate
    percorso = ReportingService(reports_dir).candidate_report(run, candidate)
    testo = percorso.read_text(encoding="utf-8")
    assert candidate.id in testo
    assert "Stato corrente" in testo
    assert "Responsabile" in testo
    assert "Data e ora (UTC)" in testo
    assert "Prossimo passo" in testo
    assert "riferimento analitico" in testo


def test_report_originalita_riporta_il_disclaimer(
    reports_dir: Path, run, script, originality
) -> None:
    esito = originality.apply(script)
    percorso = ReportingService(reports_dir).originality_report(run, esito)
    testo = percorso.read_text(encoding="utf-8")
    assert "non e' una certificazione legale" in testo.replace("'", "'").lower() or (
        "non una certificazione legale" in testo.lower()
    )
    assert "SUPERATO" in testo


def test_report_finale_elenca_eventi_e_stato(reports_dir: Path, run, workflow) -> None:
    workflow.transition(WorkflowState.UNDER_REVIEW, actor="tester")
    percorso = ReportingService(reports_dir).final_report(run)
    testo = percorso.read_text(encoding="utf-8")
    assert run.id in testo
    assert "UNDER_REVIEW" in testo
    assert "Registro eventi" in testo


def test_demo_end_to_end_completa(reports_dir: Path, niche: str) -> None:
    risultato = run_demo_workflow(primary_niche=niche, reports_dir=reports_dir)
    assert risultato.run.state is WorkflowState.COMPLETED
    assert risultato.run.blocked_reasons == []
    assert len(risultato.reports) >= 8
    for percorso in risultato.reports:
        assert percorso.exists()
        assert percorso.read_text(encoding="utf-8").strip()


def test_demo_non_completa_senza_revisione_esterna(reports_dir: Path, niche: str) -> None:
    risultato = run_demo_workflow(
        primary_niche=niche, reports_dir=reports_dir, complete=False
    )
    assert risultato.run.state is WorkflowState.COPY_PENDING_DIGITAL_EMPIRE_REVIEW
    assert risultato.run.state is not WorkflowState.COMPLETED


def test_demo_non_dichiara_video_reali(reports_dir: Path, niche: str) -> None:
    risultato = run_demo_workflow(primary_niche=niche, reports_dir=reports_dir)
    assert risultato.run.production_job is not None
    assert risultato.run.production_job.is_real_render is False


def test_demo_non_dichiara_copertine_generate(reports_dir: Path, niche: str) -> None:
    risultato = run_demo_workflow(primary_niche=niche, reports_dir=reports_dir)
    assert risultato.run.thumbnail is not None
    assert risultato.run.thumbnail.generated is False
    assert risultato.run.thumbnail.brief


def test_analisi_trasversali_generano_report(reports_dir: Path, niche: str) -> None:
    percorsi = run_side_analyses(primary_niche=niche, reports_dir=reports_dir)
    assert len(percorsi) == 3
    for p in percorsi:
        assert p.exists()
    testo_nicchia = next(p for p in percorsi if "niche-proposal" in p.name).read_text(
        encoding="utf-8"
    )
    assert "non** modifica la nicchia primaria" in testo_nicchia


def test_repository_in_memoria(run) -> None:
    repo = InMemoryWorkflowRepository()
    repo.save(run)
    assert repo.get(run.id) is run
    assert run.id in repo.list_ids()
    assert repo.get("inesistente") is None


def test_repository_su_file(tmp_path: Path, run, candidate) -> None:
    run.candidate = candidate
    repo = JsonFileWorkflowRepository(tmp_path / "wf")
    repo.save(run)
    ricaricato = repo.get(run.id)
    assert ricaricato is not None
    assert ricaricato.id == run.id
    assert ricaricato.candidate is not None
    assert ricaricato.candidate.title == candidate.title
    assert run.id in repo.list_ids()
