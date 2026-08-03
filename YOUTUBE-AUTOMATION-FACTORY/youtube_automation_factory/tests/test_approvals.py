"""Gerarchia applicata dal codice: chi puo' fare cosa."""

from __future__ import annotations

import pytest

from youtube_automation_factory.agents import (
    CopywritingAgent,
    DigitalEmpireCopyReviewer,
    ProfitableNicheAgent,
    ResearchAgent,
    ReviewAgent,
    SeniorDecisionAgent,
)
from youtube_automation_factory.core.approvals import require_level
from youtube_automation_factory.core.enums import (
    AgentLevel,
    ApprovalDecision,
    CopyReviewStatus,
    ReviewOutcome,
)
from youtube_automation_factory.core.exceptions import (
    AuthorizationError,
    NicheLockError,
)
from youtube_automation_factory.core.models import VideoCandidate


def test_operativo_non_puo_approvare_riferimento() -> None:
    with pytest.raises(AuthorizationError):
        require_level("research-1", AgentLevel.OPERATIONAL, "approve_reference")


def test_revisore_non_puo_approvare_script() -> None:
    with pytest.raises(AuthorizationError):
        require_level("review-1", AgentLevel.REVIEWER, "approve_script")


def test_regolatore_non_approva_contenuti() -> None:
    with pytest.raises(AuthorizationError):
        require_level("regulator-1", AgentLevel.REGULATORY, "approve_script")


def test_solo_il_regolatore_blocca() -> None:
    require_level("regulator-1", AgentLevel.REGULATORY, "block_workflow")
    with pytest.raises(AuthorizationError):
        require_level("senior-1", AgentLevel.SENIOR, "block_workflow")


def test_senior_approva_riferimento_valido(run, candidate, senior) -> None:
    approvazione = senior.approve_reference(run, candidate)
    assert approvazione.decision is ApprovalDecision.APPROVED
    assert run.has_senior_approval(candidate.id)


def test_senior_respinge_candidato_con_poche_visualizzazioni(
    run, senior: SeniorDecisionAgent, niche: str
) -> None:
    debole = VideoCandidate(
        title="t",
        url="https://www.youtube.com/watch?v=y",
        channel="c",
        topic="a",
        views=10,
        niche=niche,
    )
    approvazione = senior.approve_reference(run, debole)
    assert approvazione.decision is ApprovalDecision.REJECTED
    assert "visualizzazioni_significative" in approvazione.reason


def test_revisore_chiede_integrazioni_se_mancano_dati(
    reviewer: ReviewAgent, niche: str
) -> None:
    incompleto = VideoCandidate(
        title="t",
        url="https://www.youtube.com/watch?v=z",
        channel="c",
        topic="a",
        views=0,
        niche=niche,
    )
    esito = reviewer.review(incompleto)
    assert esito.outcome is ReviewOutcome.NEEDS_MORE_DATA
    assert "views" in esito.missing_fields


def test_revisore_respinge_fuori_nicchia(reviewer: ReviewAgent) -> None:
    fuori = VideoCandidate(
        title="t",
        url="https://www.youtube.com/watch?v=w",
        channel="c",
        topic="a",
        views=5_000,
        niche="Altra Nicchia",
    )
    esito = reviewer.review(fuori)
    assert esito.outcome is ReviewOutcome.REJECTED


def test_revisore_approva_candidato_completo(reviewer: ReviewAgent, candidate) -> None:
    assert reviewer.review(candidate).outcome is ReviewOutcome.APPROVED


def test_research_agent_usa_sempre_la_nicchia_primaria(
    researcher: ResearchAgent, niche: str
) -> None:
    c = researcher.build_candidate(
        title="t",
        url="https://www.youtube.com/watch?v=q",
        channel="c",
        topic="a",
        views=1_000,
    )
    assert c.niche == niche


def test_agente_non_puo_lavorare_fuori_nicchia(researcher: ResearchAgent) -> None:
    with pytest.raises(NicheLockError):
        researcher.assert_primary_niche("Altra Nicchia")


def test_proposta_nicchia_non_cambia_la_primaria(niche: str) -> None:
    agente = ProfitableNicheAgent("niche-1", niche)
    proposta = agente.propose(name="Nuova Nicchia", rationale="motivo")
    assert proposta.requires_senior_decision is True
    assert proposta.senior_decision is None
    assert agente.primary_niche == niche

    from config.settings import PRIMARY_NICHE

    assert niche == PRIMARY_NICHE


def test_senior_decide_proposta_senza_attivarla(niche: str) -> None:
    agente = ProfitableNicheAgent("niche-1", niche)
    senior = SeniorDecisionAgent("senior-1", niche)
    proposta = agente.propose(name="Nuova Nicchia", rationale="motivo")
    senior.decide_niche_proposal(proposta, approve=True, reason="da valutare in futuro")
    assert proposta.senior_decision is ApprovalDecision.APPROVED

    from config.settings import PRIMARY_NICHE

    assert niche == PRIMARY_NICHE


def test_copy_deve_essere_inviato_prima_di_essere_revisionato(run, niche: str) -> None:
    copywriter = CopywritingAgent("copy-1", niche)
    revisore = DigitalEmpireCopyReviewer()
    copy = copywriter.draft_copy(
        workflow_id=run.id, headline="h", body="b", brief="brief"
    )
    with pytest.raises(ValueError, match="non e' stato inviato"):
        revisore.review(copy, approve=True, reason="ok")

    copywriter.submit_to_digital_empire(copy)
    assert copy.digital_empire_status is CopyReviewStatus.PENDING
    revisore.review(copy, approve=True, reason="conforme")
    assert copy.digital_empire_status is CopyReviewStatus.APPROVED
    assert copy.digital_empire_reviewer == "settore-copy-digital-empire"
