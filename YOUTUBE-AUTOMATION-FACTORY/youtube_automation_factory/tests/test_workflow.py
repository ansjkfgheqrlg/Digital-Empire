"""Transizioni di stato, blocco della nicchia e vincoli di completamento."""

from __future__ import annotations

import pytest

from youtube_automation_factory.core.enums import (
    AgentLevel,
    ApprovalDecision,
    WorkflowState,
)
from youtube_automation_factory.core.exceptions import (
    ApprovalRequiredError,
    InvalidTransitionError,
    NicheLockError,
    RegulatoryBlockError,
)
from youtube_automation_factory.core.models import Approval
from youtube_automation_factory.core.workflow import (
    ALLOWED_TRANSITIONS,
    YouTubeFactoryWorkflow,
)


def test_transizione_valida(workflow: YouTubeFactoryWorkflow) -> None:
    workflow.transition(WorkflowState.UNDER_REVIEW, actor="review-test")
    assert workflow.run.state is WorkflowState.UNDER_REVIEW


def test_transizione_invalida_solleva_e_lascia_traccia(
    workflow: YouTubeFactoryWorkflow,
) -> None:
    with pytest.raises(InvalidTransitionError):
        workflow.transition(WorkflowState.COMPLETED, actor="tester")
    assert workflow.run.state is WorkflowState.DISCOVERED
    azioni = [e.action for e in workflow.run.events]
    assert "transition_rejected" in azioni


def test_approvazione_riferimento_richiede_il_senior(
    workflow: YouTubeFactoryWorkflow, candidate
) -> None:
    workflow.run.candidate = candidate
    workflow.transition(WorkflowState.UNDER_REVIEW, actor="review-test")
    with pytest.raises(ApprovalRequiredError):
        workflow.transition(WorkflowState.APPROVED_AS_REFERENCE, actor="review-test")


def test_approvazione_di_un_revisore_non_basta(workflow: YouTubeFactoryWorkflow, candidate) -> None:
    workflow.run.candidate = candidate
    workflow.run.approvals.append(
        Approval(
            subject_id=candidate.id,
            decision=ApprovalDecision.APPROVED,
            approver="review-test",
            approver_level=AgentLevel.REVIEWER,
            reason="tentativo di scavalcare il senior",
        )
    )
    workflow.transition(WorkflowState.UNDER_REVIEW, actor="review-test")
    with pytest.raises(ApprovalRequiredError):
        workflow.transition(WorkflowState.APPROVED_AS_REFERENCE, actor="review-test")


def test_script_non_approvabile_senza_controllo_originalita(
    workflow: YouTubeFactoryWorkflow, candidate, script, senior
) -> None:
    workflow.run.candidate = candidate
    workflow.run.script = script
    workflow.run.state = WorkflowState.SCRIPT_PENDING_APPROVAL
    senior.approve_script(workflow.run, script)
    with pytest.raises(RegulatoryBlockError, match="originalita"):
        workflow.transition(WorkflowState.SCRIPT_APPROVED, actor="senior-test")


def test_produzione_richiede_script_approvato(workflow: YouTubeFactoryWorkflow, script) -> None:
    workflow.run.script = script
    workflow.run.state = WorkflowState.SCRIPT_APPROVED
    with pytest.raises(InvalidTransitionError, match="script approvato"):
        workflow.transition(WorkflowState.PRODUCTION_PENDING, actor="production-test")


def test_copy_non_approvabile_senza_digital_empire(
    workflow: YouTubeFactoryWorkflow, copy_asset
) -> None:
    workflow.run.copy_asset = copy_asset
    workflow.run.state = WorkflowState.COPY_PENDING_DIGITAL_EMPIRE_REVIEW
    with pytest.raises(RegulatoryBlockError, match="Digital Empire"):
        workflow.transition(WorkflowState.COPY_APPROVED, actor="copy-test")


def test_copertina_non_approvabile_senza_originalita(
    workflow: YouTubeFactoryWorkflow, thumbnail
) -> None:
    workflow.run.thumbnail = thumbnail
    workflow.run.state = WorkflowState.THUMBNAIL_PENDING_REVIEW
    with pytest.raises(RegulatoryBlockError, match="originalita"):
        workflow.transition(WorkflowState.THUMBNAIL_APPROVED, actor="thumb-test")


def test_completamento_bloccato_senza_asset(workflow: YouTubeFactoryWorkflow) -> None:
    workflow.run.state = WorkflowState.QUALITY_CONTROL
    with pytest.raises(RegulatoryBlockError) as exc:
        workflow.transition(WorkflowState.COMPLETED, actor="regulator-test")
    motivi = " ".join(exc.value.reasons)
    assert "Copy assente" in motivi
    assert "Copertina assente" in motivi


def test_nicchia_primaria_non_modificabile(workflow: YouTubeFactoryWorkflow) -> None:
    with pytest.raises(NicheLockError):
        workflow.assert_niche_unchanged("agente-operativo", "Altra Nicchia")
    azioni = [e.action for e in workflow.run.events]
    assert "niche_change_blocked" in azioni


def test_nicchia_uguale_passa(workflow: YouTubeFactoryWorkflow, niche: str) -> None:
    workflow.assert_niche_unchanged("agente", niche.lower())


def test_stati_terminali_non_hanno_successori() -> None:
    assert ALLOWED_TRANSITIONS[WorkflowState.COMPLETED] == frozenset()
    assert ALLOWED_TRANSITIONS[WorkflowState.REJECTED] == frozenset()


def test_ogni_stato_e_mappato() -> None:
    assert set(ALLOWED_TRANSITIONS) == set(WorkflowState)


def test_blocco_registra_motivi(workflow: YouTubeFactoryWorkflow) -> None:
    workflow.block(actor="regulator-test", reasons=["motivo di prova"])
    assert workflow.run.state is WorkflowState.BLOCKED
    assert workflow.run.blocked_reasons == ["motivo di prova"]
