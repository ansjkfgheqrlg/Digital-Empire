"""Enumerazioni del dominio: stati del workflow, livelli gerarchici, esiti."""

from __future__ import annotations

from enum import StrEnum


class WorkflowState(StrEnum):
    """Stati attraversabili da un workflow di produzione."""

    DISCOVERED = "DISCOVERED"
    UNDER_REVIEW = "UNDER_REVIEW"
    NEEDS_MORE_DATA = "NEEDS_MORE_DATA"
    REJECTED = "REJECTED"
    APPROVED_AS_REFERENCE = "APPROVED_AS_REFERENCE"
    SCRIPT_DRAFT = "SCRIPT_DRAFT"
    SCRIPT_PENDING_APPROVAL = "SCRIPT_PENDING_APPROVAL"
    SCRIPT_APPROVED = "SCRIPT_APPROVED"
    PRODUCTION_PENDING = "PRODUCTION_PENDING"
    IN_PRODUCTION = "IN_PRODUCTION"
    VIDEO_READY_FOR_QA = "VIDEO_READY_FOR_QA"
    COPY_DRAFT = "COPY_DRAFT"
    COPY_PENDING_DIGITAL_EMPIRE_REVIEW = "COPY_PENDING_DIGITAL_EMPIRE_REVIEW"
    COPY_APPROVED = "COPY_APPROVED"
    THUMBNAIL_DRAFT = "THUMBNAIL_DRAFT"
    THUMBNAIL_PENDING_REVIEW = "THUMBNAIL_PENDING_REVIEW"
    THUMBNAIL_APPROVED = "THUMBNAIL_APPROVED"
    QUALITY_CONTROL = "QUALITY_CONTROL"
    COMPLETED = "COMPLETED"
    BLOCKED = "BLOCKED"


#: Stati terminali: da qui non si prosegue senza un intervento esterno.
TERMINAL_STATES: frozenset[WorkflowState] = frozenset(
    {WorkflowState.COMPLETED, WorkflowState.REJECTED}
)


class AgentLevel(StrEnum):
    """Livelli della gerarchia. L'ordine e' significativo: vedi ``rank``."""

    OPERATIONAL = "OPERATIONAL"
    REVIEWER = "REVIEWER"
    SENIOR = "SENIOR"
    REGULATORY = "REGULATORY"

    @property
    def rank(self) -> int:
        """Peso decisionale. I regolatori sono trasversali: bloccano, non decidono."""
        return {
            AgentLevel.OPERATIONAL: 0,
            AgentLevel.REVIEWER: 1,
            AgentLevel.SENIOR: 2,
            AgentLevel.REGULATORY: 2,
        }[self]


class ReviewOutcome(StrEnum):
    """Esito di una revisione di primo livello."""

    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    NEEDS_MORE_DATA = "NEEDS_MORE_DATA"


class ApprovalDecision(StrEnum):
    """Decisione formale registrata da un'approvazione."""

    APPROVED = "APPROVED"
    REJECTED = "REJECTED"


class AssetKind(StrEnum):
    """Tipo di asset sottoposto a controllo."""

    SCRIPT = "SCRIPT"
    COPY = "COPY"
    THUMBNAIL = "THUMBNAIL"


class ProductionJobStatus(StrEnum):
    """Stato di un job di produzione presso il fornitore video."""

    CREATED = "CREATED"
    SUBMITTED = "SUBMITTED"
    PROCESSING = "PROCESSING"
    READY = "READY"
    FAILED = "FAILED"


class CopyReviewStatus(StrEnum):
    """Stato della revisione esterna affidata al settore copy di Digital Empire."""

    NOT_SUBMITTED = "NOT_SUBMITTED"
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
