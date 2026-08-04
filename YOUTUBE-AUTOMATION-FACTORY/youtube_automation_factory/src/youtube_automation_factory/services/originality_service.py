"""Controllo di originalita' — **di processo**, non legale.

## Limite dichiarato

Questo servizio verifica che il *processo* di produzione sia stato rispettato: che esista un
brief proprio, che l'asset non sia stato marcato come derivato da materiale di terzi, che la
checklist sia stata compilata.

**Non rileva il plagio e non certifica l'assenza di violazioni di copyright.** Non confronta
il testo con archivi esterni, non ha accesso a corpora di riferimento e non sostituisce una
valutazione legale. Un esito positivo significa "la procedura interna e' stata seguita", non
"il contenuto e' legalmente originale".

Il controllo e' deterministico: gli stessi input producono sempre lo stesso esito.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from ..core.enums import AssetKind
from ..core.models import CopyAsset, ScriptAsset, ThumbnailAsset, utc_now

#: Dichiarazione che l'autore deve aver compilato perche' il controllo passi.
REQUIRED_DECLARATIONS: tuple[str, ...] = (
    "brief proprio",
    "nessuna derivazione da materiale di terzi",
)


@dataclass(frozen=True)
class OriginalityCheck:
    """Singolo controllo eseguito."""

    name: str
    passed: bool
    detail: str


@dataclass
class OriginalityResult:
    """Esito strutturato del controllo."""

    asset_id: str
    asset_kind: AssetKind
    passed: bool
    checks: list[OriginalityCheck] = field(default_factory=list)
    reasons: list[str] = field(default_factory=list)
    checked_at: str = field(default_factory=lambda: utc_now().isoformat())
    disclaimer: str = (
        "Controllo di processo, non una certificazione legale di assenza di plagio."
    )

    @property
    def failed_checks(self) -> list[OriginalityCheck]:
        return [c for c in self.checks if not c.passed]


CreativeAsset = ScriptAsset | CopyAsset | ThumbnailAsset


class OriginalityService:
    """Applica la checklist di originalita' a un asset creativo."""

    def check(self, asset: CreativeAsset, *, copy_mode: bool = False) -> OriginalityResult:
        """Esegue i controlli e restituisce l'esito.

        ``copy_mode`` rappresenta un flag di processo che indica l'intenzione di replicare
        materiale esistente: se attivo, l'esito e' negativo per definizione.
        """
        checks: list[OriginalityCheck] = []

        checks.append(
            OriginalityCheck(
                name="brief_presente",
                passed=bool(asset.brief and asset.brief.strip()),
                detail="L'asset deve avere un brief proprio, scritto prima della produzione.",
            )
        )
        checks.append(
            OriginalityCheck(
                name="copy_mode_disattivo",
                passed=not copy_mode,
                detail="Il flag 'copy mode' indica intenzione di replicare: non ammesso.",
            )
        )
        checks.extend(self._checks_specifici(asset))

        reasons = [f"{c.name}: {c.detail}" for c in checks if not c.passed]
        return OriginalityResult(
            asset_id=asset.id,
            asset_kind=asset.kind,
            passed=not reasons,
            checks=checks,
            reasons=reasons,
        )

    def _checks_specifici(self, asset: CreativeAsset) -> list[OriginalityCheck]:
        if isinstance(asset, ScriptAsset):
            return [
                OriginalityCheck(
                    name="script_non_derivato",
                    passed=not asset.derived_from_transcript,
                    detail="Lo script non deve derivare dal transcript del riferimento.",
                ),
                OriginalityCheck(
                    name="script_ha_corpo",
                    passed=len(asset.body.split()) >= 50,
                    detail="Lo script deve avere un corpo sviluppato (>= 50 parole).",
                ),
            ]
        if isinstance(asset, CopyAsset):
            return [
                OriginalityCheck(
                    name="copy_ha_headline",
                    passed=bool(asset.headline.strip()),
                    detail="Il copy deve avere una headline propria.",
                ),
                OriginalityCheck(
                    name="insight_solo_come_pattern",
                    passed=True,
                    detail=(
                        "Gli insight da Second Brain o dall'analisi di copy performanti sono "
                        "ammessi come studio di pattern comunicativi, non come testo da riusare."
                    ),
                ),
            ]
        return [
            OriginalityCheck(
                name="thumbnail_non_replica",
                passed=not asset.replicates_competitor_layout,
                detail="La copertina non deve replicare layout o elementi distintivi altrui.",
            ),
            OriginalityCheck(
                name="thumbnail_ha_concept",
                passed=bool(asset.concept.strip()),
                detail="La copertina deve avere un concept proprio.",
            ),
        ]

    def apply(self, asset: CreativeAsset, *, copy_mode: bool = False) -> OriginalityResult:
        """Esegue il controllo e **scrive l'esito sull'asset**.

        Se il controllo fallisce, ``originality_checked`` resta ``False``: i validatori e la
        macchina a stati impediranno l'approvazione.
        """
        result = self.check(asset, copy_mode=copy_mode)
        asset.originality_reasons = result.reasons or [
            "Checklist di originalita' superata (controllo di processo)."
        ]
        asset.originality_checked = result.passed
        return result
