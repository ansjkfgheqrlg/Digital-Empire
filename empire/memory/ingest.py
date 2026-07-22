"""
EMPIRE MEMORY — import storico dei sistemi di memoria esistenti.

Owner: Max · Controllore: Claude · Origine: FORGE (M-A) · Governo: ADR-002 + ADR-003

Tre memorie oggi si ignorano a vicenda: company/Memory/, DIGITAL-EMPIRE/00-MEMORY/ e la
memoria del workflow estate. Qui vengono lette e portate negli atomi, UNA VOLTA.

ADR-003: nessun file esistente viene spostato, riformattato o cancellato. Si legge soltanto.
Idempotente: rieseguire non duplica (dedup su hash del contenuto).
"""
from __future__ import annotations

import re


from ..paths import iter_files, rel, resolve
from .model import Atom
from .render import parse
from .store import write_many, all_atoms

__all__ = ["ingest_all", "IngestReport"]

_BACKLOG_ROW = re.compile(r"^\|\s*(B-\d+)\s*\|\s*(.+?)\s*\|(.*)\|\s*(⬜|✅|🟡)?\s*\|?\s*$")
_STATO_BLOCK = re.compile(r"^##\s+(.*)$")
_DATE_IN_TEXT = re.compile(r"(20\d{2})[-/](\d{2})[-/](\d{2})")


class IngestReport(dict):
    def __str__(self) -> str:
        lines = ["IMPORT MEMORIA — riepilogo", ""]
        for src, counts in self.items():
            if src.startswith("_"):
                continue
            tot = sum(counts.values())
            det = ", ".join(f"{k}:{v}" for k, v in sorted(counts.items()))
            lines.append(f"  {src:34} {tot:4}   ({det})")
        if "_written" in self:
            lines += ["", f"  scritti: {self['_written']}   gia' presenti (dedup): {self.get('_dup', 0)}"]
        return "\n".join(lines)


def _iso_from(text: str, fallback: str = "2026-01-01") -> str:
    m = _DATE_IN_TEXT.search(text)
    if m:
        return f"{m.group(1)}-{m.group(2)}-{m.group(3)}T00:00:00+02:00"
    return f"{fallback}T00:00:00+02:00"


def _collect_md(alias_or_path, kind: str, actor: str = "") -> list[Atom]:
    try:
        base = resolve(alias_or_path) if isinstance(alias_or_path, str) else alias_or_path
    except Exception:
        return []
    if not base.exists():
        return []
    out: list[Atom] = []
    for f in iter_files(base, suffixes=(".md",)):
        try:
            text = f.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        if not text.strip():
            continue
        a = parse(text, kind=kind)
        if not a.title:
            a.title = f.stem
        if not a.actor:
            a.actor = actor
        a.source = rel(f)
        if a.ts.startswith("1970"):
            a.ts = _iso_from(text)
        out.append(a)
    return out


def _collect_backlog() -> list[Atom]:
    try:
        p = resolve("memory_backlog")
    except Exception:
        return []
    if not p.exists():
        return []
    out: list[Atom] = []
    for line in p.read_text(encoding="utf-8", errors="replace").splitlines():
        m = _BACKLOG_ROW.match(line.strip())
        if not m:
            continue
        bid, what, rest = m.group(1), m.group(2), m.group(3)
        out.append(Atom(
            kind="plan", title=f"{bid} — {what[:140]}",
            body=line.strip(), status="open", source=rel(p),
            extra={"backlog_id": bid, "note": rest.strip(" |")},
        ))
    return out


def _collect_stato() -> list[Atom]:
    """STATO-EMPIRE.md e' il file piu' informativo del repo: ogni blocco '##' e' un atomo."""
    try:
        p = resolve("memory_stato")
    except Exception:
        return []
    if not p.exists():
        return []
    text = p.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    out: list[Atom] = []
    starts = [i for i, l in enumerate(lines) if _STATO_BLOCK.match(l)]
    for n, i in enumerate(starts):
        end = starts[n + 1] if n + 1 < len(starts) else len(lines)
        block = "\n".join(lines[i:end]).strip()
        if len(block) < 40:
            continue
        title = _STATO_BLOCK.match(lines[i]).group(1).strip()
        out.append(Atom(
            kind="session", title=title[:160], body=block,
            ts=_iso_from(title) if _DATE_IN_TEXT.search(title) else _iso_from(block),
            source=rel(p), status="storico",
        ))
    return out


# Sottocartelle di DIGITAL-EMPIRE/00-MEMORY/ -> kind. Il workflow estate ha kind misti:
# importarli tutti come "checkpoint" perderebbe l'informazione.
_ESTATE_DIRS = {
    "checkpoints": "checkpoint", "decisions": "decision", "plans": "plan",
    "brainstorms": "brainstorm", "feedback": "feedback", "performances": "perf",
    "reasoning-bank": "pattern", "errors": "error", "metrics": "metric", "retro": "retro",
}


def _collect_estate() -> dict[str, list[Atom]]:
    """Memoria del workflow estate, un gruppo per sottocartella (kind corretto)."""
    out: dict[str, list[Atom]] = {}
    try:
        base = resolve("estate_memory")
    except Exception:
        return out
    if not base.is_dir():
        return out
    for sub, kind in _ESTATE_DIRS.items():
        d = base / sub
        if d.is_dir():
            atoms = _collect_md(d, kind)
            if atoms:
                out[f"estate 00-MEMORY/{sub}"] = atoms
    # file sciolti alla radice (MEMORY-INDEX, RETRO-PROTOCOLLO)
    loose = [f for f in base.iterdir() if f.is_file() and f.suffix == ".md"]
    if loose:
        atoms = []
        for f in loose:
            text = f.read_text(encoding="utf-8", errors="replace")
            a = parse(text, kind="plan")
            a.title = a.title or f.stem
            a.source = rel(f)
            if a.ts.startswith("1970"):
                a.ts = _iso_from(text)
            atoms.append(a)
        out["estate 00-MEMORY/(radice)"] = atoms
    return out


def ingest_all(*, dry_run: bool = True) -> IngestReport:
    """Importa i tre sistemi. dry_run=True conta soltanto, non scrive."""
    sources: dict[str, list[Atom]] = {
        "company/Memory/checkpoints": _collect_md("memory_cp", "checkpoint"),
        "company/Memory/decisions":   _collect_md("memory_adr", "decision"),
        "company/Memory/sessions":    _collect_md(resolve("memory") / "sessions", "session"),
        "company/Memory/plans":       _collect_md(resolve("memory") / "plans", "plan"),
        "company/Memory/tasks":       _collect_md("memory_tasks", "plan"),
        "company/Memory/BACKLOG.md":  _collect_backlog(),
        "company/Memory/STATO-EMPIRE": _collect_stato(),
        **_collect_estate(),
    }

    report = IngestReport()
    written = dup = 0
    seen: set[str] = set()
    if not dry_run:
        seen = {a.hash for a in all_atoms() if a.hash}

    batch: list[Atom] = []
    for name, atoms in sources.items():
        counts: dict[str, int] = {}
        for a in atoms:
            counts[a.kind] = counts.get(a.kind, 0) + 1
            if dry_run:
                continue
            h = a.hash or a.compute_hash()
            if h in seen:
                dup += 1
                continue
            a.hash = h
            batch.append(a)
            seen.add(h)
            written += 1
        report[name] = counts

    if batch:
        write_many(batch)

    report["_written"] = written
    report["_dup"] = dup
    return report
