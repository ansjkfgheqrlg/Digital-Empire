"""Workflow dimostrativo completo, senza servizi esterni.

Serve a due cose: dare alla CLI qualcosa di eseguibile e ai test un percorso end-to-end
verificabile. Usa dati locali, l'adapter mock e nessuna rete.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from pathlib import Path

from .agents import (
    CompetitorAnalysisAgent,
    CopywritingAgent,
    DigitalEmpireCopyReviewer,
    NicheChannelScoutAgent,
    ProductionAgent,
    ProfitableNicheAgent,
    RegulatoryAgent,
    ResearchAgent,
    ReviewAgent,
    ScriptAgent,
    SeniorDecisionAgent,
    ThumbnailAgent,
)
from .core.enums import ReviewOutcome, WorkflowState
from .core.models import WorkflowRun
from .core.reporting import ReportingService
from .core.workflow import YouTubeFactoryWorkflow
from .integrations.flik_adapter import MockFlikAdapter
from .services.originality_service import OriginalityService

logger = logging.getLogger(__name__)

DEMO_SCRIPT_BODY = (
    "Apertura: una domanda diretta a chi ascolta, per mettere a fuoco il problema prima di "
    "proporre qualunque risposta. Sviluppo: si distingue fra cio' che si puo' osservare e "
    "cio' che si puo' solo supporre, e si spiega perche' la differenza conta nella vita di "
    "tutti i giorni. Si porta un esempio concreto, si mostra come cambia la lettura della "
    "situazione e si anticipa l'obiezione piu' probabile invece di ignorarla. Chiusura: un "
    "passo pratico, piccolo e verificabile, che chi ascolta puo' compiere subito, senza "
    "promesse di risultati che nessuno puo' garantire. Il registro resta piano e rispettoso, "
    "senza urgenza artificiale e senza scorciatoie retoriche."
)


@dataclass
class DemoResult:
    """Esito della demo, con i percorsi dei report generati."""

    run: WorkflowRun
    reports: list[Path] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)


def run_demo_workflow(
    *, primary_niche: str, reports_dir: Path, complete: bool = True
) -> DemoResult:
    """Esegue il percorso completo dalla ricerca alla chiusura.

    Con ``complete=False`` si ferma prima dell'approvazione esterna del copy: serve a
    dimostrare (e testare) che il workflow **non** puo' chiudersi in quello stato.
    """
    reporting = ReportingService(reports_dir)
    originality = OriginalityService()
    result = DemoResult(run=WorkflowRun(niche=primary_niche))
    run = result.run
    wf = YouTubeFactoryWorkflow(run, primary_niche)

    research = ResearchAgent("research-1", primary_niche)
    reviewer = ReviewAgent("review-1", primary_niche)
    senior = SeniorDecisionAgent("senior-1", primary_niche)
    scripter = ScriptAgent("script-1", primary_niche)
    producer = ProductionAgent("production-1", primary_niche, MockFlikAdapter())
    copywriter = CopywritingAgent("copy-1", primary_niche)
    de_reviewer = DigitalEmpireCopyReviewer()
    thumbnailer = ThumbnailAgent("thumbnail-1", primary_niche)
    regulator = RegulatoryAgent("regulator-1", primary_niche, originality)

    # 1. Ricerca ---------------------------------------------------------------------
    candidate = research.build_candidate(
        title="Esempio di contenuto della nicchia",
        url="https://www.youtube.com/watch?v=demo00000001",
        channel="Canale di riferimento",
        topic="Gestione dell'attenzione nella vita quotidiana",
        views=125_000,
        transcript=research.transcript_unavailable(
            "demo00000001",
            "Nessun transcript recuperato: automazione browser non configurata in demo.",
        ),
        notes=["Dati locali di dimostrazione: nessuna chiamata di rete."],
    )
    run.candidate = candidate
    result.reports.append(reporting.candidate_report(run, candidate))

    # 2. Revisione -------------------------------------------------------------------
    wf.transition(
        WorkflowState.UNDER_REVIEW, actor=reviewer.name, actor_level=reviewer.level
    )
    review = reviewer.review(candidate)
    run.review = review
    result.reports.append(reporting.review_report(run, review))
    if review.outcome is not ReviewOutcome.APPROVED:
        result.notes.append(f"Revisione non superata: {review.reason}")
        result.reports.append(reporting.final_report(run))
        return result

    # 3. Decisione senior ------------------------------------------------------------
    senior.approve_reference(run, candidate)
    wf.transition(
        WorkflowState.APPROVED_AS_REFERENCE,
        actor=senior.name,
        actor_level=senior.level,
        reason="Approvato come riferimento analitico.",
    )
    result.reports.append(reporting.senior_decision_report(run))

    # 4. Script ----------------------------------------------------------------------
    wf.transition(WorkflowState.SCRIPT_DRAFT, actor=scripter.name, actor_level=scripter.level)
    script = scripter.draft_script(
        workflow_id=run.id,
        candidate=candidate,
        title="Un modo diverso di guardare la stessa domanda",
        body=DEMO_SCRIPT_BODY,
    )
    run.script = script
    esito_orig = originality.apply(script)
    result.reports.append(reporting.script_brief_report(run, script))
    result.reports.append(reporting.originality_report(run, esito_orig))

    wf.transition(
        WorkflowState.SCRIPT_PENDING_APPROVAL, actor=scripter.name, actor_level=scripter.level
    )
    approvazione = senior.approve_script(run, script)
    script.approved = approvazione.is_approved
    wf.transition(
        WorkflowState.SCRIPT_APPROVED,
        actor=senior.name,
        actor_level=senior.level,
        reason=approvazione.reason,
    )

    # 5. Produzione ------------------------------------------------------------------
    wf.transition(
        WorkflowState.PRODUCTION_PENDING, actor=producer.name, actor_level=producer.level
    )
    job = producer.create_job(
        workflow_id=run.id,
        script=script,
        voice_agents=["narratore-principale"],
        subtitles_enabled=True,
        subtitle_preset="standard",
    )
    run.production_job = job
    wf.transition(
        WorkflowState.IN_PRODUCTION, actor=producer.name, actor_level=producer.level
    )
    produzione = producer.wait_for_result(job)
    result.notes.append(
        f"Produzione simulata: {produzione.status}. Nessun video reale prodotto."
    )
    wf.transition(
        WorkflowState.VIDEO_READY_FOR_QA, actor=producer.name, actor_level=producer.level
    )

    # 6. Copy ------------------------------------------------------------------------
    wf.transition(
        WorkflowState.COPY_DRAFT, actor=copywriter.name, actor_level=copywriter.level
    )
    copy = copywriter.draft_copy(
        workflow_id=run.id,
        headline="Una domanda che cambia la risposta",
        body=(
            "Testo originale scritto per questo video. Nessuna frase proviene da materiale "
            "di terzi: gli schemi comunicativi studiati influenzano la struttura, non le parole."
        ),
        brief="Copy coerente con lo script approvato, registro piano, nessuna promessa.",
        pattern_insights=[
            "Studio di pattern: domanda diretta in apertura.",
            "Studio di pattern: promessa concreta e verificabile.",
        ],
    )
    run.copy_asset = copy
    originality.apply(copy)
    copywriter.submit_to_digital_empire(copy)
    wf.transition(
        WorkflowState.COPY_PENDING_DIGITAL_EMPIRE_REVIEW,
        actor=copywriter.name,
        actor_level=copywriter.level,
    )
    result.reports.append(reporting.copy_report(run, copy))

    if not complete:
        result.notes.append(
            "Demo interrotta prima della revisione esterna: il workflow non puo' chiudersi "
            "senza l'approvazione del settore copy di Digital Empire."
        )
        result.reports.append(reporting.final_report(run))
        return result

    de_reviewer.review(copy, approve=True, reason="Conforme agli standard di casa.")
    copy.approved = True
    wf.transition(
        WorkflowState.COPY_APPROVED, actor=de_reviewer.reviewer_name, reason="Revisione esterna."
    )
    result.reports.append(reporting.copy_report(run, copy))

    # 7. Copertina -------------------------------------------------------------------
    wf.transition(
        WorkflowState.THUMBNAIL_DRAFT, actor=thumbnailer.name, actor_level=thumbnailer.level
    )
    thumbnail = thumbnailer.draft_thumbnail(workflow_id=run.id, script=script, copy=copy)
    run.thumbnail = thumbnail
    originality.apply(thumbnail)
    wf.transition(
        WorkflowState.THUMBNAIL_PENDING_REVIEW,
        actor=thumbnailer.name,
        actor_level=thumbnailer.level,
    )
    thumbnail.approved = True
    wf.transition(
        WorkflowState.THUMBNAIL_APPROVED,
        actor=senior.name,
        actor_level=senior.level,
        reason="Brief originale e coerente con script e copy.",
    )
    result.notes.append(
        "Copertina non generata: automazione Arena non configurata in demo. Il brief e' "
        "comunque prodotto e approvato."
    )
    result.reports.append(reporting.thumbnail_report(run, thumbnail))

    # 8. Quality control -------------------------------------------------------------
    wf.transition(
        WorkflowState.QUALITY_CONTROL, actor=regulator.name, actor_level=regulator.level
    )
    blocchi = regulator.final_quality_control(wf)
    if blocchi:
        result.notes.append("Blocco regolatorio: " + "; ".join(blocchi))
    else:
        wf.transition(
            WorkflowState.COMPLETED,
            actor=regulator.name,
            actor_level=regulator.level,
            reason="Tutti i requisiti soddisfatti.",
        )

    result.reports.append(reporting.final_report(run))
    return result


def run_side_analyses(*, primary_niche: str, reports_dir: Path) -> list[Path]:
    """Esegue i team trasversali (competitor, canali, proposte di nicchia)."""
    reporting = ReportingService(reports_dir)
    percorsi: list[Path] = []

    competitor = CompetitorAnalysisAgent("competitor-1", primary_niche)
    report = competitor.analyse(
        channels=["Canale di riferimento", "Canale affine"],
        video_views={"video-a": 125_000, "video-b": 18_000, "video-c": 4_200},
        channel_metrics={"video_analizzati": 3.0},
    )
    percorsi.append(reporting.competitor_report(report))

    scout = NicheChannelScoutAgent("scout-1", primary_niche)
    canali = scout.register_many(
        [
            {
                "name": "Canale affine",
                "url": "https://www.youtube.com/@canale-affine",
                "rationale": "Stessa nicchia, formato ripetibile, pubblico sovrapponibile.",
            }
        ]
    )
    percorsi.append(reporting.channel_discovery_report(canali))

    niche_agent = ProfitableNicheAgent("niche-1", primary_niche)
    proposta = niche_agent.propose(
        name="Nicchia adiacente da valutare",
        rationale="Domanda osservata e concorrenza limitata sul formato.",
        evidence=["Osservazione preliminare su dati pubblici."],
    )
    percorsi.append(reporting.niche_proposal_report(proposta))
    return percorsi
