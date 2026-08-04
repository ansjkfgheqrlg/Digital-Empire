"""Validazione dei modelli e regole codificate nei tipi."""

from __future__ import annotations

import pytest
from pydantic import ValidationError

from youtube_automation_factory.core.enums import CopyReviewStatus
from youtube_automation_factory.core.models import (
    CopyAsset,
    NicheProposal,
    ScriptAsset,
    ThumbnailAsset,
    TranscriptAsset,
    VideoCandidate,
)


def test_timestamp_sono_timezone_aware(candidate: VideoCandidate) -> None:
    assert candidate.discovered_at.tzinfo is not None


def test_views_negative_rifiutate(niche: str) -> None:
    with pytest.raises(ValidationError):
        VideoCandidate(
            title="t",
            url="https://www.youtube.com/watch?v=x",
            channel="c",
            topic="a",
            views=-1,
            niche=niche,
        )


def test_candidato_e_sempre_solo_riferimento(niche: str) -> None:
    with pytest.raises(ValidationError, match="riferimento analitico"):
        VideoCandidate(
            title="t",
            url="https://www.youtube.com/watch?v=x",
            channel="c",
            topic="a",
            views=10,
            niche=niche,
            reference_only=False,
        )


def test_dati_minimi_segnalano_i_campi_mancanti(niche: str) -> None:
    c = VideoCandidate(
        title="t",
        url="https://www.youtube.com/watch?v=x",
        channel="c",
        topic="a",
        views=0,
        niche=niche,
    )
    ok, mancanti = c.has_minimum_data()
    assert not ok
    assert "views" in mancanti


def test_transcript_non_disponibile_non_ha_testo() -> None:
    t = TranscriptAsset(video_id="v1", available=False, note="non offerto")
    assert t.text is None
    with pytest.raises(ValidationError):
        TranscriptAsset(video_id="v1", available=True)


def test_script_non_puo_derivare_dal_transcript(run, script: ScriptAsset) -> None:
    with pytest.raises(ValidationError, match="non puo' essere derivato"):
        ScriptAsset(
            workflow_id=run.id,
            author="a",
            brief="b",
            title="t",
            body=script.body,
            derived_from_transcript=True,
        )


def test_asset_non_approvabile_senza_controllo_originalita(script: ScriptAsset) -> None:
    assert script.originality_checked is False
    with pytest.raises(ValidationError, match="originality_checked"):
        script.approved = True


def test_copy_non_finale_senza_revisione_esterna(copy_asset: CopyAsset) -> None:
    copy_asset.originality_checked = True
    with pytest.raises(ValidationError, match="Digital Empire"):
        copy_asset.approved = True

    copy_asset.digital_empire_status = CopyReviewStatus.APPROVED
    copy_asset.approved = True
    assert copy_asset.approved


def test_copertina_non_puo_replicare_layout_altrui(run) -> None:
    with pytest.raises(ValidationError, match="replicare layout"):
        ThumbnailAsset(
            workflow_id=run.id,
            author="a",
            brief="b",
            concept="c",
            replicates_competitor_layout=True,
        )


def test_copertina_generata_deve_dichiarare_il_backend(run) -> None:
    with pytest.raises(ValidationError, match="backend"):
        ThumbnailAsset(workflow_id=run.id, author="a", brief="b", concept="c", generated=True)


def test_copertina_non_generata_non_puo_avere_file(run) -> None:
    with pytest.raises(ValidationError, match="image_path"):
        ThumbnailAsset(
            workflow_id=run.id,
            author="a",
            brief="b",
            concept="c",
            generated=False,
            image_path="/tmp/x.png",
        )


def test_proposta_nicchia_richiede_sempre_decisione_senior() -> None:
    with pytest.raises(ValidationError, match="requires_senior_decision"):
        NicheProposal(name="n", rationale="r", requires_senior_decision=False)


def test_campi_sconosciuti_rifiutati(run) -> None:
    with pytest.raises(ValidationError):
        ThumbnailAsset(workflow_id=run.id, author="a", brief="b", concept="c", campo_inesistente=1)
