"""Validatori di dominio usati dai regolatori e dal workflow.

Ogni funzione restituisce l'elenco dei motivi di blocco: lista vuota significa "conforme".
Nessuna di queste funzioni modifica lo stato — decidere spetta a chi le chiama.
"""

from __future__ import annotations

from ..core.enums import CopyReviewStatus, WorkflowState
from ..core.models import (
    CopyAsset,
    ScriptAsset,
    ThumbnailAsset,
    VideoCandidate,
    WorkflowRun,
)


def validate_niche(candidate: VideoCandidate, primary_niche: str) -> list[str]:
    """Il candidato deve appartenere alla nicchia primaria."""
    if candidate.niche.strip().casefold() != primary_niche.strip().casefold():
        return [
            f"Nicchia '{candidate.niche}' diversa dalla nicchia primaria '{primary_niche}'."
        ]
    return []


def validate_candidate_data(candidate: VideoCandidate) -> list[str]:
    """Dati minimi per una valutazione senior sensata."""
    ok, mancanti = candidate.has_minimum_data()
    if ok:
        return []
    return [f"Dati minimi mancanti sul candidato: {', '.join(mancanti)}."]


def validate_script(script: ScriptAsset) -> list[str]:
    motivi: list[str] = []
    if not script.originality_checked:
        motivi.append("Lo script non ha superato il controllo di originalita'.")
    if not script.brief.strip():
        motivi.append("Lo script non ha un brief editoriale.")
    if script.word_count < 50:
        motivi.append(f"Script troppo breve ({script.word_count} parole).")
    return motivi


def validate_copy(copy: CopyAsset) -> list[str]:
    motivi: list[str] = []
    if not copy.originality_checked:
        motivi.append("Il copy non ha superato il controllo di originalita'.")
    if copy.digital_empire_status is not CopyReviewStatus.APPROVED:
        motivi.append(
            "Il copy non e' stato approvato dal settore copy di Digital Empire "
            f"(stato: {copy.digital_empire_status})."
        )
    return motivi


def validate_thumbnail(thumbnail: ThumbnailAsset) -> list[str]:
    motivi: list[str] = []
    if not thumbnail.originality_checked:
        motivi.append("La copertina non ha superato il controllo di originalita'.")
    if not thumbnail.brief.strip():
        motivi.append("La copertina non ha un brief associato.")
    if thumbnail.generated and not thumbnail.image_path:
        motivi.append("Copertina dichiarata generata ma senza file associato.")
    return motivi


def validate_ready_for_completion(run: WorkflowRun) -> list[str]:
    """Requisiti per chiudere il workflow: video, sottotitoli, copy e copertina approvati."""
    motivi: list[str] = []

    job = run.production_job
    if job is None:
        motivi.append("Nessun job di produzione: il video non e' stato preparato.")
    else:
        if not job.subtitles_enabled:
            motivi.append("I sottotitoli non risultano abilitati sul job di produzione.")
        if run.state not in (
            WorkflowState.VIDEO_READY_FOR_QA,
            WorkflowState.QUALITY_CONTROL,
            WorkflowState.THUMBNAIL_APPROVED,
            WorkflowState.COPY_APPROVED,
        ):
            # Non e' un errore di per se': lo segnala il controllo di stato del workflow.
            pass

    if run.script is None or not run.script.approved:
        motivi.append("Lo script non risulta approvato.")
    if run.copy is None:
        motivi.append("Copy assente.")
    else:
        motivi.extend(validate_copy(run.copy))
        if not run.copy.approved:
            motivi.append("Il copy non risulta approvato.")
    if run.thumbnail is None:
        motivi.append("Copertina assente.")
    else:
        motivi.extend(validate_thumbnail(run.thumbnail))
        if not run.thumbnail.approved:
            motivi.append("La copertina non risulta approvata.")
    return motivi
