"""
EMPIRE — data model dell'azienda.

Owner: Max · Controllore: Claude · Origine: FORGE (seed CP-20260722-003)
Governo: ADR-008 (ogni artefatto ha proprietario/controllore/origine/governo)

FILE CONGELATO nella forma dei campi: aggiungere campi è consentito,
rinominarli o rimuoverli richiede nota di coordinamento in STATO-EMPIRE.md
(Gael costruisce loader/index/conform su queste firme).
"""
from __future__ import annotations

from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Any, Literal

__all__ = [
    "Provenance", "Agent", "Department", "Ecosystem", "Workflow", "Skill",
    "Artifact", "Finding", "Severity",
]

Severity = Literal["block", "warn", "info"]


def _ser(v: Any) -> Any:
    if isinstance(v, Path):
        return v.as_posix()
    if isinstance(v, (list, tuple)):
        return [_ser(x) for x in v]
    if isinstance(v, dict):
        return {k: _ser(x) for k, x in v.items()}
    return v


class _Base:
    def to_dict(self) -> dict:
        return {k: _ser(v) for k, v in asdict(self).items()}


@dataclass(slots=True)
class Provenance(_Base):
    """I 4 campi imposti da ADR-008. None = artefatto orfano (finding)."""
    owner: str | None = None
    controller: str | None = None
    origin: str | None = None
    governance: str | None = None
    source_file: Path | None = None
    line: int | None = None

    @property
    def complete(self) -> bool:
        return all((self.owner, self.controller, self.origin, self.governance))

    @property
    def missing(self) -> list[str]:
        pairs = (("owner", self.owner), ("controller", self.controller),
                 ("origin", self.origin), ("governance", self.governance))
        return [k for k, v in pairs if not v]


@dataclass(slots=True)
class Agent(_Base):
    id: str
    name: str
    path: Path
    ecosystem: str | None = None
    department: str | None = None
    role: str | None = None          # director | conductor | operativo | qa | ...
    tier: str | None = None          # opus | sonnet | haiku, se dichiarato
    skills: list[str] = field(default_factory=list)
    workflows: list[str] = field(default_factory=list)
    cf_grade: bool = False           # rispetta lo standard content-forge a 7 file
    prov: Provenance = field(default_factory=Provenance)


@dataclass(slots=True)
class Department(_Base):
    id: str
    path: Path
    ecosystem: str | None = None
    agents: list[str] = field(default_factory=list)
    workflows: list[str] = field(default_factory=list)
    prov: Provenance = field(default_factory=Provenance)


@dataclass(slots=True)
class Ecosystem(_Base):
    id: str
    name: str
    path: Path
    departments: list[str] = field(default_factory=list)
    agents_count: int = 0
    has_backbone: bool = False
    has_ecosistema_md: bool = False
    prov: Provenance = field(default_factory=Provenance)


@dataclass(slots=True)
class Workflow(_Base):
    id: str
    path: Path
    owner: str | None = None
    steps: list[str] = field(default_factory=list)
    gates: list[str] = field(default_factory=list)
    referenced_paths: list[str] = field(default_factory=list)  # input di conform.check_links
    prov: Provenance = field(default_factory=Provenance)


@dataclass(slots=True)
class Skill(_Base):
    name: str
    path: Path
    scope: str = "project"           # global | project | vendored | estate
    has_skill_md: bool = False
    prov: Provenance = field(default_factory=Provenance)


@dataclass(slots=True)
class Artifact(_Base):
    path: Path
    kind: str = "doc"                # agent|department|ecosystem|workflow|skill|script|doc|template|asset
    size: int = 0
    hash: str = ""
    mtime: float = 0.0
    git_author: str | None = None
    git_date: str | None = None
    references: list[str] = field(default_factory=list)
    referenced_by: list[str] = field(default_factory=list)
    prov: Provenance = field(default_factory=Provenance)


@dataclass(slots=True)
class Finding(_Base):
    """Esito di un controllo di conformità. Ordinabile per severità."""
    severity: Severity
    rule: str                        # "MANDATO-Art8" | "ADR-008" | "LINK-DEAD" | ...
    path: Path
    message: str
    fix: str = ""
    line: int | None = None
    target: str | None = None        # il riferimento incriminato, se pertinente

    _ORDER = {"block": 0, "warn": 1, "info": 2}

    @property
    def rank(self) -> int:
        return self._ORDER.get(self.severity, 9)

    def __str__(self) -> str:
        loc = f"{self.path.as_posix() if isinstance(self.path, Path) else self.path}"
        if self.line:
            loc += f":{self.line}"
        return f"[{self.severity.upper():5}] {self.rule:14} {loc}\n        {self.message}"
