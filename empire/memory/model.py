"""
EMPIRE MEMORY — l'atomo di memoria.

Owner: Max · Controllore: Claude · Origine: FORGE (M-A) · Governo: ADR-002 (memory-first)

Un solo tipo di record, discriminato da `kind`. Il livello operativo (JSONL) e' la VERITA';
il Markdown in company/Memory/ e' la VISTA. Se divergono si rigenera la vista, mai il contrario.

Regola dalla skill memory-empire: archiviazione INTEGRALE. Il `body` non si riassume mai.
"""
from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone, timedelta
from typing import Any

__all__ = ["KINDS", "PREFIX", "Atom", "now_iso", "today_compact", "AtomError"]

# Fuso orario di lavoro (Italia). Le date sono sempre assolute (regola del Mandato).
TZ = timezone(timedelta(hours=2))


class AtomError(ValueError):
    """Atomo non valido."""


# I kind sono dedotti dai sistemi esistenti (company/Memory/ + DIGITAL-EMPIRE/00-MEMORY/).
# Non inventarne altri senza un ADR.
KINDS: dict[str, str] = {
    "checkpoint": "task chiuso, con prove (ADR-002: nessun task e' fatto senza checkpoint)",
    "decision":   "ADR — decisione architetturale o di governo",
    "plan":       "piano di lavoro o voce di backlog",
    "brainstorm": "idee, shortlist, esplorazioni",
    "error":      "errore reale osservato, con comando ed errore esatti",
    "metric":     "misura numerica datata",
    "pattern":    "ReasoningBank — pattern vincente o fallimentare",
    "retro":      "retrospettiva di fase o settimana",
    "perf":       "performance record (GEM-03 / WF-PERF-LOOP T1)",
    "feedback":   "TIP | RULE-NOTE | MUTATION-PROP (WF-PERF-LOOP T4)",
    "session":    "sessione di lavoro",
    "ingestion":  "contenuto ingerito (Empire Studio / memory-empire)",
    "audit":      "audit o ispezione",
}

# Prefisso dell'ID per kind. Segue la convenzione gia' in uso su disco.
PREFIX: dict[str, str] = {
    "checkpoint": "CP", "decision": "ADR", "plan": "PLAN", "brainstorm": "BRN",
    "error": "ERR", "metric": "MET", "pattern": "PAT", "retro": "RETRO",
    "perf": "PERF", "feedback": "FB", "session": "SESS", "ingestion": "ING",
    "audit": "AUD",
}

# Campi obbligatori in piu' rispetto al minimo, per kind.
REQUIRED_EXTRA: dict[str, tuple[str, ...]] = {
    "perf": ("agent", "task"),
    "feedback": ("ftype", "to"),
    "metric": ("name", "value"),
}

ID_RE = re.compile(r"^[A-Z]+-\d{8}-\d{3}$")


def now_iso() -> str:
    return datetime.now(TZ).isoformat(timespec="seconds")


def today_compact(ts: str | None = None) -> str:
    if ts:
        return datetime.fromisoformat(ts).strftime("%Y%m%d")
    return datetime.now(TZ).strftime("%Y%m%d")


@dataclass(slots=True)
class Atom:
    kind: str
    title: str
    body: str = ""
    id: str = ""
    ts: str = field(default_factory=now_iso)
    actor: str = ""                       # Max | Gael | Claude | Gemini | <agente>
    task: str = ""
    workflow: str = ""
    ecosystem: str = ""
    status: str = ""                      # done|open|ATTIVO|proposto|confirmed|recurred|...
    refs: list[str] = field(default_factory=list)      # id di altri atomi / ADR
    artifacts: list[str] = field(default_factory=list) # path prodotti
    source: str = ""                      # file .md di provenienza (import legacy)
    extra: dict[str, Any] = field(default_factory=dict)
    hash: str = ""

    # -------------------------------------------------------------- validazione
    def validate(self) -> None:
        if self.kind not in KINDS:
            raise AtomError(f"kind sconosciuto: {self.kind!r}. Ammessi: {', '.join(sorted(KINDS))}")
        if not self.title.strip():
            raise AtomError("title obbligatorio")
        if self.id and not ID_RE.match(self.id):
            raise AtomError(f"id malformato: {self.id!r} (atteso PREFIX-YYYYMMDD-NNN)")
        # I campi extra obbligatori valgono per gli atomi CREATI dal runtime.
        # Gli atomi IMPORTATI da file legacy (source valorizzato) si prendono come sono:
        # inventare un campo mancante sarebbe falsificare la storia (Mandato Art.2).
        if not self.source:
            for f in REQUIRED_EXTRA.get(self.kind, ()):
                if f not in self.extra and not getattr(self, f, ""):
                    raise AtomError(f"kind {self.kind!r}: campo obbligatorio mancante: {f}")

    # -------------------------------------------------------------- identita'
    def compute_hash(self) -> str:
        """Impronta del CONTENUTO (non dell'id ne' del timestamp): serve al dedup dell'import."""
        payload = "\x1f".join([
            self.kind, self.title.strip(), self.body.strip(),
            self.actor.strip(), self.task.strip(),
        ])
        return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:16]

    @property
    def prefix(self) -> str:
        return PREFIX.get(self.kind, "ATOM")

    # -------------------------------------------------------------- (de)serializzazione
    def to_dict(self) -> dict:
        d = asdict(self)
        if not d["hash"]:
            d["hash"] = self.compute_hash()
        return d

    @classmethod
    def from_dict(cls, d: dict) -> "Atom":
        known = {f for f in cls.__slots__}
        return cls(**{k: v for k, v in d.items() if k in known})

    def searchable(self) -> str:
        return " ".join([
            self.id, self.kind, self.title, self.body, self.actor, self.task,
            self.workflow, self.ecosystem, self.status,
            " ".join(self.refs), " ".join(self.artifacts),
        ]).lower()
