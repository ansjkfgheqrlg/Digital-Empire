"""Controlli regolatori, originalita' e blocchi."""

from __future__ import annotations

import pytest

from youtube_automation_factory.core.enums import CopyReviewStatus, WorkflowState
from youtube_automation_factory.services.originality_service import OriginalityService


def test_originalita_fallisce_in_copy_mode(originality: OriginalityService, script) -> None:
    esito = originality.check(script, copy_mode=True)
    assert not esito.passed
    assert any("copy_mode" in r for r in esito.reasons)


def test_originalita_passa_su_asset_conforme(originality: OriginalityService, script) -> None:
    esito = originality.apply(script)
    assert esito.passed
    assert script.originality_checked is True
    assert esito.disclaimer


def test_originalita_fallisce_senza_brief(originality: OriginalityService, run) -> None:
    from youtube_automation_factory.core.models import ThumbnailAsset

    t = ThumbnailAsset(workflow_id=run.id, author="a", brief=" ", concept="c")
    esito = originality.apply(t)
    assert not esito.passed
    assert t.originality_checked is False


def test_originalita_fallisce_su_script_troppo_corto(originality: OriginalityService, run) -> None:
    from youtube_automation_factory.core.models import ScriptAsset

    s = ScriptAsset(workflow_id=run.id, author="a", brief="b", title="t", body="troppo corto")
    esito = originality.apply(s)
    assert not esito.passed


def test_audit_segnala_originalita_mancante(regulator, run, script) -> None:
    run.script = script
    problemi = regulator.audit(run)
    assert any("originalita" in p for p in problemi)


def test_audit_segnala_copy_senza_digital_empire(regulator, run, copy_asset) -> None:
    copy_asset.originality_checked = True
    run.copy_asset = copy_asset
    problemi = regulator.audit(run)
    assert any("Digital Empire" in p for p in problemi)


def test_audit_pulito_su_asset_conformi(
    regulator, run, script, copy_asset, thumbnail, originality
) -> None:
    originality.apply(script)
    originality.apply(copy_asset)
    originality.apply(thumbnail)
    copy_asset.digital_empire_status = CopyReviewStatus.APPROVED
    run.script, run.copy_asset, run.thumbnail = script, copy_asset, thumbnail
    assert regulator.audit(run) == []


def test_blocco_porta_lo_stato_a_blocked(regulator, workflow, script) -> None:
    workflow.run.script = script  # senza controllo di originalita'
    motivi = regulator.block_if_needed(workflow)
    assert motivi
    assert workflow.run.state is WorkflowState.BLOCKED
    assert workflow.run.blocked_reasons == motivi


def test_sblocco_rifiutato_se_restano_non_conformita(regulator, workflow, script) -> None:
    workflow.run.script = script
    regulator.block_if_needed(workflow)
    with pytest.raises(ValueError, match="restano non conformita"):
        regulator.clear_block(workflow, WorkflowState.SCRIPT_DRAFT)


def test_sblocco_riuscito_dopo_la_correzione(regulator, workflow, script, originality) -> None:
    workflow.run.script = script
    regulator.block_if_needed(workflow)
    originality.apply(script)
    regulator.clear_block(workflow, WorkflowState.SCRIPT_DRAFT)
    assert workflow.run.state is WorkflowState.SCRIPT_DRAFT
    assert workflow.run.blocked_reasons == []


def test_quality_control_finale_blocca_se_manca_qualcosa(regulator, workflow) -> None:
    workflow.run.state = WorkflowState.QUALITY_CONTROL
    motivi = regulator.final_quality_control(workflow)
    assert motivi
    assert workflow.run.state is WorkflowState.BLOCKED
    assert len(motivi) == len(set(motivi)), "i motivi non devono essere duplicati"


def test_verify_transition_non_applica_nulla(regulator, run) -> None:
    assert regulator.verify_transition(run, WorkflowState.UNDER_REVIEW) is True
    assert regulator.verify_transition(run, WorkflowState.COMPLETED) is False
    assert run.state is WorkflowState.DISCOVERED
