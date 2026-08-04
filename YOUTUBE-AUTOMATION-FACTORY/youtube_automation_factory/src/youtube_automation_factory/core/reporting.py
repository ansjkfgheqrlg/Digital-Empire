"""Generazione dei report Markdown.

Ogni report contiene sempre: identificativo, stato corrente, responsabile, data e ora
(timezone-aware), motivazioni e prossimo passo previsto.
"""

from __future__ import annotations

import logging
import re
from pathlib import Path

from .enums import WorkflowState
from .models import (
    ChannelDiscovery,
    CompetitorReport,
    CopyAsset,
    NicheProposal,
    ReviewRequest,
    ScriptAsset,
    ThumbnailAsset,
    VideoCandidate,
    WorkflowRun,
    utc_now,
)

logger = logging.getLogger(__name__)

_UNSAFE = re.compile(r"[^A-Za-z0-9._-]+")


def safe_filename(*parts: str) -> str:
    """Nome file sicuro: solo caratteri innocui, niente percorsi relativi."""
    pulite = [_UNSAFE.sub("-", p.strip()).strip("-") for p in parts if p and p.strip()]
    base = "_".join(x for x in pulite if x) or "report"
    return base[:120]


#: Prossimo passo atteso per ciascuno stato: rende ogni report azionabile.
NEXT_STEP: dict[WorkflowState, str] = {
    WorkflowState.DISCOVERED: "Revisione dati da parte del ReviewAgent.",
    WorkflowState.UNDER_REVIEW: "Decisione del livello senior sul candidato.",
    WorkflowState.NEEDS_MORE_DATA: "Integrazione dati da parte degli agenti operativi.",
    WorkflowState.REJECTED: "Nessuno: candidato scartato.",
    WorkflowState.APPROVED_AS_REFERENCE: "Stesura del brief e dello script originale.",
    WorkflowState.SCRIPT_DRAFT: "Controllo di originalita' e invio in approvazione.",
    WorkflowState.SCRIPT_PENDING_APPROVAL: "Approvazione senior dello script.",
    WorkflowState.SCRIPT_APPROVED: "Preparazione del job di produzione.",
    WorkflowState.PRODUCTION_PENDING: "Invio del job all'adapter di produzione.",
    WorkflowState.IN_PRODUCTION: "Attesa del completamento della produzione.",
    WorkflowState.VIDEO_READY_FOR_QA: "Stesura del copy originale.",
    WorkflowState.COPY_DRAFT: "Invio del copy al settore copy di Digital Empire.",
    WorkflowState.COPY_PENDING_DIGITAL_EMPIRE_REVIEW: "Esito della revisione esterna.",
    WorkflowState.COPY_APPROVED: "Brief della copertina.",
    WorkflowState.THUMBNAIL_DRAFT: "Controllo di originalita' della copertina.",
    WorkflowState.THUMBNAIL_PENDING_REVIEW: "Approvazione della copertina.",
    WorkflowState.THUMBNAIL_APPROVED: "Controllo qualita' finale.",
    WorkflowState.QUALITY_CONTROL: "Chiusura del workflow.",
    WorkflowState.COMPLETED: "Nessuno: workflow concluso.",
    WorkflowState.BLOCKED: "Rimozione delle cause di blocco e sblocco regolatorio.",
}


class ReportingService:
    """Scrive report Markdown nella cartella configurata."""

    def __init__(self, reports_dir: Path) -> None:
        self.reports_dir = reports_dir
        self.reports_dir.mkdir(parents=True, exist_ok=True)

    # -- helper ---------------------------------------------------------------------
    def _write(self, filename: str, content: str) -> Path:
        path = self.reports_dir / filename
        path.write_text(content, encoding="utf-8")
        logger.info("Report scritto: %s", path)
        return path

    @staticmethod
    def _intestazione(titolo: str, *, ident: str, stato: str, responsabile: str) -> str:
        return (
            f"# {titolo}\n\n"
            f"| Campo | Valore |\n|---|---|\n"
            f"| ID | `{ident}` |\n"
            f"| Stato corrente | **{stato}** |\n"
            f"| Responsabile | {responsabile} |\n"
            f"| Data e ora (UTC) | {utc_now().isoformat(timespec='seconds')} |\n\n"
        )

    @staticmethod
    def _prossimo_passo(stato: WorkflowState) -> str:
        return f"\n## Prossimo passo\n{NEXT_STEP.get(stato, 'Da definire.')}\n"

    @staticmethod
    def _elenco(titolo: str, voci: list[str], vuoto: str = "_Nessuna._") -> str:
        if not voci:
            return f"\n## {titolo}\n{vuoto}\n"
        righe = "\n".join(f"- {v}" for v in voci)
        return f"\n## {titolo}\n{righe}\n"

    # -- report ---------------------------------------------------------------------
    def candidate_report(self, run: WorkflowRun, candidate: VideoCandidate) -> Path:
        transcript = candidate.transcript
        if transcript is None:
            stato_tr = "non richiesto"
            nota_tr = "—"
        elif transcript.available:
            stato_tr = "disponibile"
            nota_tr = f"{len((transcript.text or '').split())} parole, lingua {transcript.language}"
        else:
            stato_tr = "non disponibile"
            nota_tr = transcript.note

        corpo = (
            self._intestazione(
                "Scheda video candidato",
                ident=candidate.id,
                stato=run.state,
                responsabile="ResearchAgent (operativo)",
            )
            + "## Dati raccolti\n\n"
            + f"| Campo | Valore |\n|---|---|\n"
            + f"| Titolo | {candidate.title} |\n"
            + f"| URL | {candidate.url} |\n"
            + f"| Canale | {candidate.channel} |\n"
            + f"| Argomento | {candidate.topic} |\n"
            + f"| Visualizzazioni | {candidate.views:,} |\n".replace(",", ".")
            + f"| Nicchia | {candidate.niche} |\n"
            + f"| Transcript | {stato_tr} — {nota_tr} |\n"
            + "\n> **Uso ammesso:** riferimento analitico. Il contenuto di questo video non va "
            "replicato: se ne analizzano tema, concetti e bisogni dell'audience.\n"
            + self._elenco("Note", candidate.notes)
            + self._prossimo_passo(run.state)
        )
        return self._write(safe_filename("candidate", candidate.id) + ".md", corpo)

    def review_report(self, run: WorkflowRun, review: ReviewRequest) -> Path:
        corpo = (
            self._intestazione(
                "Esito revisione",
                ident=review.id,
                stato=run.state,
                responsabile=f"{review.reviewer} (revisore)",
            )
            + f"## Esito\n**{review.outcome}**\n\n## Motivazione\n{review.reason}\n"
            + self._elenco("Campi mancanti", review.missing_fields)
            + self._prossimo_passo(run.state)
        )
        return self._write(safe_filename("review", review.id) + ".md", corpo)

    def senior_decision_report(self, run: WorkflowRun) -> Path:
        righe = [
            f"**{a.decision}** su `{a.subject_id}` — {a.approver} ({a.approver_level}): {a.reason}"
            for a in run.approvals
        ]
        corpo = (
            self._intestazione(
                "Decisione senior",
                ident=run.id,
                stato=run.state,
                responsabile="SeniorDecisionAgent (senior)",
            )
            + self._elenco("Decisioni registrate", righe)
            + "\n> Un candidato approvato lo e' **esclusivamente come riferimento analitico**.\n"
            + self._prossimo_passo(run.state)
        )
        return self._write(safe_filename("senior-decision", run.id) + ".md", corpo)

    def script_brief_report(self, run: WorkflowRun, script: ScriptAsset) -> Path:
        corpo = (
            self._intestazione(
                "Brief script",
                ident=script.id,
                stato=run.state,
                responsabile=f"{script.author} (operativo)",
            )
            + f"## Titolo\n{script.title}\n\n## Brief\n{script.brief}\n\n"
            + f"## Corpo\n\n{script.body}\n\n"
            + f"- Parole: **{script.word_count}**\n"
            + f"- Derivato da transcript: **{script.derived_from_transcript}** "
            "(deve essere sempre `False`)\n"
            + f"- Controllo originalita': **{script.originality_checked}**\n"
            + f"- Approvato: **{script.approved}**\n"
            + self._prossimo_passo(run.state)
        )
        return self._write(safe_filename("script", script.id) + ".md", corpo)

    def originality_report(self, run: WorkflowRun, result: object) -> Path:
        checks = getattr(result, "checks", [])
        righe = [
            f"{'PASSA' if c.passed else 'BLOCCA'} — `{c.name}`: {c.detail}" for c in checks
        ]
        asset_id = getattr(result, "asset_id", "?")
        passed = getattr(result, "passed", False)
        corpo = (
            self._intestazione(
                "Esito controllo originalita'",
                ident=str(asset_id),
                stato=run.state,
                responsabile="OriginalityService (regolatorio)",
            )
            + f"## Esito\n**{'SUPERATO' if passed else 'NON SUPERATO'}**\n"
            + self._elenco("Controlli eseguiti", righe)
            + self._elenco("Motivazioni di blocco", list(getattr(result, "reasons", [])))
            + f"\n> {getattr(result, 'disclaimer', '')}\n"
            + self._prossimo_passo(run.state)
        )
        return self._write(safe_filename("originality", str(asset_id)) + ".md", corpo)

    def copy_report(self, run: WorkflowRun, copy: CopyAsset) -> Path:
        corpo = (
            self._intestazione(
                "Copy e revisione Digital Empire",
                ident=copy.id,
                stato=run.state,
                responsabile=f"{copy.author} (operativo)",
            )
            + f"## Headline\n{copy.headline}\n\n## Testo\n{copy.body}\n\n"
            + f"## Revisione Digital Empire\n\n"
            + f"| Campo | Valore |\n|---|---|\n"
            + f"| Stato | **{copy.digital_empire_status}** |\n"
            + f"| Revisore | {copy.digital_empire_reviewer or '—'} |\n"
            + f"| Motivazione | {copy.digital_empire_reason or '—'} |\n"
            + self._elenco("Pattern studiati (solo analisi)", copy.pattern_insights)
            + self._prossimo_passo(run.state)
        )
        return self._write(safe_filename("copy", copy.id) + ".md", corpo)

    def thumbnail_report(self, run: WorkflowRun, thumbnail: ThumbnailAsset) -> Path:
        corpo = (
            self._intestazione(
                "Brief copertina",
                ident=thumbnail.id,
                stato=run.state,
                responsabile=f"{thumbnail.author} (operativo)",
            )
            + f"## Concept\n{thumbnail.concept}\n\n## Brief\n{thumbnail.brief}\n\n"
            + f"| Campo | Valore |\n|---|---|\n"
            + f"| Generata | **{thumbnail.generated}** |\n"
            + f"| Backend | {thumbnail.generation_backend or '—'} |\n"
            + f"| File | {thumbnail.image_path or '—'} |\n"
            + f"| Controllo originalita' | {thumbnail.originality_checked} |\n"
            + f"| Approvata | {thumbnail.approved} |\n"
            + "\n> Se il backend di generazione non e' configurato, il brief resta valido e la "
            "copertina **non** viene dichiarata generata.\n"
            + self._prossimo_passo(run.state)
        )
        return self._write(safe_filename("thumbnail", thumbnail.id) + ".md", corpo)

    def competitor_report(self, report: CompetitorReport) -> Path:
        metriche = [f"{k}: {v}" for k, v in sorted(report.channel_metrics.items())]
        corpo = (
            self._intestazione(
                "Analisi competitor",
                ident=report.id,
                stato="—",
                responsabile="CompetitorAnalysisAgent (operativo)",
            )
            + self._elenco("Canali analizzati", report.channels_analysed)
            + self._elenco("Osservazioni", report.observations)
            + self._elenco("Metriche di canale", metriche)
            + self._elenco("Dati non disponibili", report.data_gaps)
            + "\n> Le osservazioni servono a capire **perche'** qualcosa funziona. "
            "Non sono indicazioni per replicare contenuti altrui.\n"
        )
        return self._write(safe_filename("competitor", report.id) + ".md", corpo)

    def channel_discovery_report(self, discoveries: list[ChannelDiscovery]) -> Path:
        righe = [f"**{d.name}** — {d.url}\n  - {d.rationale}" for d in discoveries]
        ident = discoveries[0].id if discoveries else "vuoto"
        corpo = (
            self._intestazione(
                "Analisi canali di nicchia",
                ident=ident,
                stato="—",
                responsabile="NicheChannelScoutAgent (operativo)",
            )
            + self._elenco("Canali individuati", righe)
            + "\n> Ampliare il bacino di analisi **non** cambia la nicchia primaria.\n"
        )
        return self._write(safe_filename("channels", ident) + ".md", corpo)

    def niche_proposal_report(self, proposal: NicheProposal) -> Path:
        corpo = (
            self._intestazione(
                "Proposta di nicchia",
                ident=proposal.id,
                stato=str(proposal.senior_decision or "IN ATTESA DI DECISIONE SENIOR"),
                responsabile="ProfitableNicheAgent (operativo)",
            )
            + f"## Nicchia proposta\n{proposal.name}\n\n## Motivazione\n{proposal.rationale}\n"
            + self._elenco("Evidenze", proposal.evidence)
            + f"\n## Vincolo\nRichiede decisione senior: "
            f"**{proposal.requires_senior_decision}**. Questa proposta **non** modifica la "
            "nicchia primaria in configurazione.\n"
        )
        return self._write(safe_filename("niche-proposal", proposal.id) + ".md", corpo)

    def final_report(self, run: WorkflowRun) -> Path:
        eventi = [
            f"`{e.at.isoformat(timespec='seconds')}` **{e.action}** — {e.actor}"
            + (f" ({e.from_state} → {e.to_state})" if e.to_state else "")
            + (f": {e.reason}" if e.reason else "")
            for e in run.events
        ]
        asset_righe = [
            f"Script: {'approvato' if run.script and run.script.approved else 'non approvato'}",
            f"Copy: {'approvato' if run.copy and run.copy.approved else 'non approvato'}",
            f"Copertina: {'approvata' if run.thumbnail and run.thumbnail.approved else 'non approvata'}",
            f"Produzione: {run.production_job.status if run.production_job else 'assente'}",
        ]
        corpo = (
            self._intestazione(
                "Report finale del workflow",
                ident=run.id,
                stato=run.state,
                responsabile="RegulatoryAgent (regolatorio)",
            )
            + f"- Nicchia: **{run.niche}**\n"
            + self._elenco("Stato degli asset", asset_righe)
            + self._elenco("Motivi di blocco", run.blocked_reasons)
            + self._elenco("Registro eventi", eventi)
            + self._prossimo_passo(run.state)
        )
        return self._write(safe_filename("workflow", run.id, "final") + ".md", corpo)
