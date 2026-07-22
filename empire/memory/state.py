"""
EMPIRE MEMORY — blocco di stato per STATO-EMPIRE.md.

Owner: Max · Controllore: Claude · Origine: FORGE (M-A) · Governo: ADR-002 + ADR-003

STATO-EMPIRE.md e' il file che Max legge a occhio: resta Markdown, resta scritto a mano,
non viene mai sostituito da un generatore. Qui si produce SOLO un blocco riassuntivo da
anteporre, e per default lo si stampa soltanto: scrivere richiede --write esplicito.
"""
from __future__ import annotations

from datetime import datetime

from ..paths import resolve
from .model import TZ
from .store import all_atoms, stats

__all__ = ["build_block", "prepend"]

_MARK_BEGIN = "<!-- EMPIRE-MEM:BEGIN (generato da `empire mem state`) -->"
_MARK_END = "<!-- EMPIRE-MEM:END -->"


def build_block() -> str:
    s = stats()
    atoms = sorted(all_atoms(), key=lambda a: a.ts, reverse=True)
    recent = atoms[:5]
    open_plans = [a for a in atoms if a.kind == "plan" and a.status == "open"]
    errors = [a for a in atoms if a.kind == "error"]
    decisions = [a for a in atoms if a.kind == "decision" and a.status.upper() in ("ATTIVO", "ATTIVA")]

    lines = [
        _MARK_BEGIN,
        f"## 🧠 MEMORIA — istantanea automatica {datetime.now(TZ).strftime('%Y-%m-%d %H:%M')}",
        "",
        f"- **atomi totali:** {s['total']}  ·  " +
        "  ·  ".join(f"{k}: {v}" for k, v in list(s["by_kind"].items())[:8]),
        f"- **decisioni attive:** {len(decisions)}  ·  **backlog aperto:** {len(open_plans)}"
        f"  ·  **errori registrati:** {len(errors)}",
        "",
        "**Ultimi 5 atomi:**",
    ]
    for a in recent:
        lines.append(f"- `{a.id}` {a.ts[:10]} — {a.title[:110]}")
    if open_plans:
        lines += ["", "**Backlog aperto (primi 5):**"]
        for a in open_plans[:5]:
            lines.append(f"- {a.title[:120]}")
    lines += ["",
              "> Rigenerabile con `python -m empire mem state --write`. "
              "Tutto cio' che sta FUORI dai marcatori e' scritto a mano e non viene toccato.",
              _MARK_END, ""]
    return "\n".join(lines)


def prepend(*, write: bool = False) -> str:
    """Inserisce/sostituisce il blocco in testa a STATO-EMPIRE.md, sotto il titolo H1."""
    block = build_block()
    if not write:
        return block

    p = resolve("memory_stato")
    text = p.read_text(encoding="utf-8")

    if _MARK_BEGIN in text and _MARK_END in text:
        pre, _, rest = text.partition(_MARK_BEGIN)
        _, _, post = rest.partition(_MARK_END)
        new = pre + block + post.lstrip("\n")
    else:
        lines = text.splitlines(keepends=True)
        i = 1 if lines and lines[0].startswith("# ") else 0
        new = "".join(lines[:i]) + "\n" + block + "\n" + "".join(lines[i:])

    p.write_text(new, encoding="utf-8")
    return block
