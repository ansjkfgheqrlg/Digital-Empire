"""Modelli di dominio (Pydantic v2).

Regole trasversali applicate qui, non solo documentate:

* i timestamp sono sempre timezone-aware (UTC);
* un asset creativo nasce con ``originality_checked=False`` e non puo' essere approvato
  finche' resta tale;
* il campo ``reference_only`` sui candidati ricorda che i contenuti dei competitor sono
  materiale di **analisi**, mai da replicare.
"""

from __future__ import annotations

import uuid
from datetime import UTC, datetime
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, HttpUrl, field_validator, model_validator

from .enums import (
    AgentLevel,
    ApprovalDecision,
    AssetKind,
    CopyReviewStatus,
    ProductionJobStatus,
    ReviewOutcome,
    WorkflowState,
)


def utc_now() -> datetime:
    """Istante corrente, timezone-aware."""
    return datetime.now(UTC)


def new_id() -> str:
    return uuid.uuid4().hex[:12]


NonEmptyStr = Annotated[str, Field(min_length=1)]


class _Base(BaseModel):
    model_config = ConfigDict(extra="forbid", validate_assignment=True)


# ---------------------------------------------------------------------------------------
# Ricerca e riferimenti
# ---------------------------------------------------------------------------------------
class TranscriptAsset(_Base):
    """Transcript di un video di riferimento, quando disponibile.

    Se non e' disponibile, ``text`` resta ``None`` e ``note`` spiega il perche'. Non si
    inventa mai contenuto per riempire il campo.
    """

    video_id: NonEmptyStr
    text: str | None = None
    language: str | None = None
    available: bool = False
    note: str = "Transcript non recuperato."
    retrieved_at: datetime = Field(default_factory=utc_now)

    @model_validator(mode="after")
    def _coerenza(self) -> TranscriptAsset:
        if self.available and not self.text:
            raise ValueError("available=True richiede un testo non vuoto.")
        if not self.available and self.text:
            raise ValueError("Un transcript con testo deve avere available=True.")
        return self


class VideoCandidate(_Base):
    """Video individuato su YouTube, usato **solo come riferimento analitico**."""

    id: str = Field(default_factory=new_id)
    title: NonEmptyStr
    url: HttpUrl
    channel: NonEmptyStr
    topic: NonEmptyStr
    views: int = Field(ge=0)
    niche: NonEmptyStr
    transcript: TranscriptAsset | None = None
    discovered_at: datetime = Field(default_factory=utc_now)
    reference_only: bool = True
    notes: list[str] = Field(default_factory=list)

    @field_validator("reference_only")
    @classmethod
    def _sempre_riferimento(cls, value: bool) -> bool:
        if not value:
            raise ValueError(
                "I contenuti di terzi sono ammessi solo come riferimento analitico: "
                "reference_only non puo' essere False."
            )
        return value

    def has_minimum_data(self) -> tuple[bool, list[str]]:
        """Verifica i dati minimi per poter essere valutato dal livello senior."""
        mancanti: list[str] = []
        if self.views <= 0:
            mancanti.append("views")
        if not self.topic.strip():
            mancanti.append("topic")
        if not self.channel.strip():
            mancanti.append("channel")
        return (not mancanti, mancanti)


# ---------------------------------------------------------------------------------------
# Revisioni e approvazioni
# ---------------------------------------------------------------------------------------
class ReviewRequest(_Base):
    """Esito di una revisione di primo livello."""

    id: str = Field(default_factory=new_id)
    subject_id: NonEmptyStr
    reviewer: NonEmptyStr
    outcome: ReviewOutcome
    reason: NonEmptyStr
    missing_fields: list[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=utc_now)


class Approval(_Base):
    """Approvazione o rifiuto formale, con l'autore e il suo livello."""

    id: str = Field(default_factory=new_id)
    subject_id: NonEmptyStr
    decision: ApprovalDecision
    approver: NonEmptyStr
    approver_level: AgentLevel
    reason: NonEmptyStr
    created_at: datetime = Field(default_factory=utc_now)

    @property
    def is_approved(self) -> bool:
        return self.decision is ApprovalDecision.APPROVED


# ---------------------------------------------------------------------------------------
# Asset creativi
# ---------------------------------------------------------------------------------------
class _CreativeAsset(_Base):
    """Base comune agli asset originali prodotti dalla fabbrica."""

    id: str = Field(default_factory=new_id)
    workflow_id: NonEmptyStr
    author: NonEmptyStr
    brief: NonEmptyStr
    originality_checked: bool = False
    originality_reasons: list[str] = Field(default_factory=list)
    approved: bool = False
    created_at: datetime = Field(default_factory=utc_now)

    @model_validator(mode="after")
    def _no_approvazione_senza_controllo(self) -> _CreativeAsset:
        if self.approved and not self.originality_checked:
            raise ValueError("Un asset non puo' risultare approvato con originality_checked=False.")
        return self


class ScriptAsset(_CreativeAsset):
    """Script originale. Non deriva dal transcript del riferimento."""

    kind: AssetKind = AssetKind.SCRIPT
    title: NonEmptyStr
    body: NonEmptyStr
    reference_candidate_id: str | None = None
    derived_from_transcript: bool = False

    @field_validator("derived_from_transcript")
    @classmethod
    def _mai_derivato(cls, value: bool) -> bool:
        if value:
            raise ValueError(
                "Lo script non puo' essere derivato dal transcript del riferimento: "
                "il transcript si analizza per tema e bisogni dell'audience, non si riusa."
            )
        return value

    @property
    def word_count(self) -> int:
        return len(self.body.split())


class CopyAsset(_CreativeAsset):
    """Copy originale, soggetto a revisione esterna del settore copy di Digital Empire."""

    kind: AssetKind = AssetKind.COPY
    headline: NonEmptyStr
    body: NonEmptyStr
    digital_empire_status: CopyReviewStatus = CopyReviewStatus.NOT_SUBMITTED
    digital_empire_reviewer: str | None = None
    digital_empire_reason: str | None = None
    pattern_insights: list[str] = Field(default_factory=list)

    @model_validator(mode="after")
    def _approvazione_richiede_revisione_esterna(self) -> CopyAsset:
        if self.approved and self.digital_empire_status is not CopyReviewStatus.APPROVED:
            raise ValueError(
                "Il copy non puo' essere finale senza l'approvazione del settore copy di "
                "Digital Empire."
            )
        return self


class ThumbnailAsset(_CreativeAsset):
    """Copertina originale. Il brief e' obbligatorio anche quando non viene generata."""

    kind: AssetKind = AssetKind.THUMBNAIL
    concept: NonEmptyStr
    generated: bool = False
    generation_backend: str | None = None
    image_path: str | None = None
    replicates_competitor_layout: bool = False

    @field_validator("replicates_competitor_layout")
    @classmethod
    def _mai_replica(cls, value: bool) -> bool:
        if value:
            raise ValueError(
                "La copertina non puo' replicare layout o elementi distintivi di terzi."
            )
        return value

    @model_validator(mode="after")
    def _generazione_coerente(self) -> ThumbnailAsset:
        if self.generated and not self.generation_backend:
            raise ValueError("Una copertina generata deve dichiarare il backend usato.")
        if not self.generated and self.image_path:
            raise ValueError(
                "image_path presente ma generated=False: non dichiarare copertine inesistenti."
            )
        return self


# ---------------------------------------------------------------------------------------
# Produzione
# ---------------------------------------------------------------------------------------
class ProductionJob(_Base):
    """Job di produzione video. Esiste solo a fronte di uno script approvato."""

    id: str = Field(default_factory=new_id)
    workflow_id: NonEmptyStr
    script_id: NonEmptyStr
    adapter: NonEmptyStr
    status: ProductionJobStatus = ProductionJobStatus.CREATED
    voice_agents: list[str] = Field(default_factory=list)
    subtitles_enabled: bool = True
    subtitle_preset: str | None = None
    output_path: str | None = None
    is_real_render: bool = False
    messages: list[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=utc_now)
    updated_at: datetime = Field(default_factory=utc_now)


# ---------------------------------------------------------------------------------------
# Intelligence
# ---------------------------------------------------------------------------------------
class CompetitorReport(_Base):
    """Osservazioni su competitor e performance di canale."""

    id: str = Field(default_factory=new_id)
    niche: NonEmptyStr
    channels_analysed: list[str] = Field(default_factory=list)
    observations: list[str] = Field(default_factory=list)
    channel_metrics: dict[str, float] = Field(default_factory=dict)
    data_gaps: list[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=utc_now)


class ChannelDiscovery(_Base):
    """Canale della stessa nicchia, individuato per ampliare il bacino di analisi."""

    id: str = Field(default_factory=new_id)
    name: NonEmptyStr
    url: HttpUrl
    niche: NonEmptyStr
    rationale: NonEmptyStr
    discovered_at: datetime = Field(default_factory=utc_now)


class NicheProposal(_Base):
    """Proposta di nicchia. **Non** modifica la nicchia primaria."""

    id: str = Field(default_factory=new_id)
    name: NonEmptyStr
    rationale: NonEmptyStr
    evidence: list[str] = Field(default_factory=list)
    requires_senior_decision: bool = True
    senior_decision: ApprovalDecision | None = None
    created_at: datetime = Field(default_factory=utc_now)

    @field_validator("requires_senior_decision")
    @classmethod
    def _sempre_da_decidere(cls, value: bool) -> bool:
        if not value:
            raise ValueError(
                "Ogni proposta di nicchia resta soggetta a decisione senior: "
                "requires_senior_decision non puo' essere False."
            )
        return value


# ---------------------------------------------------------------------------------------
# Workflow
# ---------------------------------------------------------------------------------------
class WorkflowEvent(_Base):
    """Riga del registro eventi. Immutabile per costruzione."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    id: str = Field(default_factory=new_id)
    workflow_id: NonEmptyStr
    actor: NonEmptyStr
    actor_level: AgentLevel | None = None
    action: NonEmptyStr
    from_state: WorkflowState | None = None
    to_state: WorkflowState | None = None
    reason: str = ""
    at: datetime = Field(default_factory=utc_now)


class WorkflowRun(_Base):
    """Stato completo di un'esecuzione della fabbrica."""

    id: str = Field(default_factory=new_id)
    niche: NonEmptyStr
    state: WorkflowState = WorkflowState.DISCOVERED
    candidate: VideoCandidate | None = None
    review: ReviewRequest | None = None
    approvals: list[Approval] = Field(default_factory=list)
    script: ScriptAsset | None = None
    copy_asset: CopyAsset | None = None
    thumbnail: ThumbnailAsset | None = None
    production_job: ProductionJob | None = None
    events: list[WorkflowEvent] = Field(default_factory=list)
    blocked_reasons: list[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=utc_now)

    def approvals_for(self, subject_id: str) -> list[Approval]:
        return [a for a in self.approvals if a.subject_id == subject_id]

    def has_senior_approval(self, subject_id: str) -> bool:
        return any(
            a.is_approved and a.approver_level is AgentLevel.SENIOR
            for a in self.approvals_for(subject_id)
        )
