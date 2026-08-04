"""Autorizzazioni e approvazioni.

La gerarchia non e' una convenzione documentale: le azioni riservate sono elencate qui e
``require_level`` solleva ``AuthorizationError`` quando un agente prova a superare il proprio
livello. Gli agenti chiamano questa funzione nei propri metodi decisionali.
"""

from __future__ import annotations

from .enums import AgentLevel, ApprovalDecision
from .exceptions import ApprovalRequiredError, AuthorizationError
from .models import Approval, WorkflowRun

#: Azione → livello minimo richiesto.
RESTRICTED_ACTIONS: dict[str, AgentLevel] = {
    "approve_reference": AgentLevel.SENIOR,
    "approve_script": AgentLevel.SENIOR,
    "decide_niche_proposal": AgentLevel.SENIOR,
    "set_production_priority": AgentLevel.SENIOR,
    "review_candidate": AgentLevel.REVIEWER,
    "block_workflow": AgentLevel.REGULATORY,
    "clear_regulatory_block": AgentLevel.REGULATORY,
}


def require_level(agent_name: str, agent_level: AgentLevel, action: str) -> None:
    """Verifica che ``agent_level`` basti per ``action``.

    I regolatori sono trasversali: possono bloccare, ma non sostituiscono le approvazioni
    senior — per questo ``block_workflow`` e' riservato a loro e ``approve_*`` al senior.
    """
    richiesto = RESTRICTED_ACTIONS.get(action)
    if richiesto is None:
        return
    if action in ("block_workflow", "clear_regulatory_block"):
        if agent_level is not AgentLevel.REGULATORY:
            raise AuthorizationError(agent_name, agent_level, action)
        return
    if agent_level is AgentLevel.REGULATORY:
        # Un regolatore non approva contenuti: verificherebbe se stesso.
        raise AuthorizationError(agent_name, agent_level, action)
    if agent_level.rank < richiesto.rank:
        raise AuthorizationError(agent_name, agent_level, action)


def record_approval(
    run: WorkflowRun,
    *,
    subject_id: str,
    decision: ApprovalDecision,
    approver: str,
    approver_level: AgentLevel,
    reason: str,
    action: str,
) -> Approval:
    """Registra un'approvazione dopo aver verificato il livello di chi la emette."""
    require_level(approver, approver_level, action)
    approval = Approval(
        subject_id=subject_id,
        decision=decision,
        approver=approver,
        approver_level=approver_level,
        reason=reason,
    )
    run.approvals.append(approval)
    return approval


def assert_senior_approval(run: WorkflowRun, subject_id: str, subject_label: str) -> None:
    """Solleva se manca l'approvazione senior per ``subject_id``."""
    if not run.has_senior_approval(subject_id):
        raise ApprovalRequiredError(subject_label, AgentLevel.SENIOR)
