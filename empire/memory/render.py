"""
EMPIRE MEMORY — la VISTA: atomo -> Markdown nel formato gia' in uso, e ritorno.

Owner: Max · Controllore: Claude · Origine: FORGE (M-A) · Governo: ADR-002 + ADR-003

Il formato NON e' inventato: e' quello osservato in company/Memory/templates/CP-template.md,
ADR-template.md e nei ~30 checkpoint reali su disco. I file esistenti restano dove sono e
come sono; qui si produce lo stesso formato per i nuovi.

Invariante testata: parse(render(atom)) == atom sui campi significativi.
"""
from __future__ import annotations

import re
from pathlib import Path

from ..paths import resolve
from .model import Atom, PREFIX

__all__ = ["render", "parse", "target_path", "write_view"]

# Etichette osservate nei checkpoint reali, in quest'ordine.
_CP_FIELDS = [
    ("Data", "_date"),
    ("Autore", "actor"),
    ("Ecosistema/Reparto", "ecosystem"),
    ("Task", "task"),
    ("Esito", "_esito"),
    ("Output", "_artifacts"),
    ("Decisioni prese", "_refs"),
    ("Lezioni/errori", "_lezioni"),
    ("Costi", "_costi"),
    ("Prossimo passo", "_next"),
]

_ESITO = {"done": "✅ completato", "partial": "⚠️ parziale", "failed": "❌ fallito",
          "open": "⏳ in corso"}
_ESITO_INV = {v.split()[-1]: k for k, v in _ESITO.items()}

_BULLET_RE = re.compile(r"^-\s+\*\*([^:*]+):\*\*\s*(.*)$")
_TITLE_RE = re.compile(r"^#\s+([A-Z]+-\d{8}-\d{3})\s+—\s+(.*)$")


def _fmt_list(v: list[str]) -> str:
    return ", ".join(f"`{x}`" for x in v) if v else "nessuna"


def render(atom: Atom) -> str:
    """Atomo -> Markdown. `decision` usa il formato ADR, tutto il resto il formato CP."""
    if atom.kind == "decision":
        return _render_adr(atom)
    return _render_cp(atom)


def _render_cp(atom: Atom) -> str:
    date = atom.ts[:10]
    rows = {
        "_date": date,
        "actor": atom.actor or "—",
        "ecosystem": atom.ecosystem or "—",
        "task": atom.task or atom.title,
        "_esito": _ESITO.get(atom.status, atom.status or "✅ completato"),
        "_artifacts": _fmt_list(atom.artifacts) if atom.artifacts else "—",
        "_refs": _fmt_list(atom.refs),
        "_lezioni": atom.extra.get("lezioni", "nessuna"),
        "_costi": atom.extra.get("costi", "—"),
        "_next": atom.extra.get("next", "—"),
    }
    out = [f"# {atom.id} — {atom.title}", ""]
    for label, key in _CP_FIELDS:
        val = rows.get(key, getattr(atom, key, "") if not key.startswith("_") else "")
        out.append(f"- **{label}:** {val}")
    if atom.body.strip():
        out += ["", "---", "", atom.body.rstrip()]
    out.append("")
    return "\n".join(out)


def _render_adr(atom: Atom) -> str:
    e = atom.extra
    return "\n".join([
        f"# {atom.id} — {atom.title}",
        "",
        f"- **Data:** {atom.ts[:10]}",
        f"- **Stato:** {atom.status or 'proposto'}",
        f"- **Decisori:** {atom.actor or 'Max'}",
        "",
        "## Contesto",
        e.get("contesto", atom.body or "—"),
        "",
        "## Decisione",
        e.get("decisione", "—"),
        "",
        "## Alternative scartate",
        e.get("alternative", "- nessuna registrata"),
        "",
        "## Conseguenze",
        e.get("conseguenze", "—"),
        "",
        "## Contradiction-check",
        e.get("contradiction_check", "verificato contro ADR attivi: nessun conflitto"),
        "",
    ])


def parse(text: str, *, kind: str | None = None) -> Atom:
    """Markdown -> Atomo. Tollerante: i file reali non seguono il template alla lettera."""
    lines = text.splitlines()
    atom_id, title = "", ""
    for line in lines[:5]:
        m = _TITLE_RE.match(line.strip())
        if m:
            atom_id, title = m.group(1), m.group(2).strip()
            break
    if not title:
        for line in lines[:5]:
            if line.startswith("# "):
                title = line[2:].strip()
                break

    fields: dict[str, str] = {}
    body_start = len(lines)
    for i, line in enumerate(lines):
        m = _BULLET_RE.match(line.strip())
        if m:
            fields[m.group(1).strip()] = m.group(2).strip()
        elif line.strip() == "---" and fields:
            body_start = i + 1
            break

    prefix = atom_id.split("-")[0] if atom_id else ""
    if kind is None:
        kind = next((k for k, p in PREFIX.items() if p == prefix), "checkpoint")

    esito = fields.get("Esito", "")
    status = next((v for k, v in _ESITO_INV.items() if k in esito), "") or ("ATTIVO" if kind == "decision" else "done")

    body = "\n".join(lines[body_start:]).strip()
    if not body:
        body = "\n".join(lines[1:]).strip()

    return Atom(
        kind=kind,
        id=atom_id,
        title=title,
        body=body,
        ts=(fields.get("Data", "")[:10] or "1970-01-01") + "T00:00:00+02:00",
        actor=fields.get("Autore", "") or fields.get("Decisori", ""),
        ecosystem=fields.get("Ecosistema/Reparto", ""),
        task=fields.get("Task", ""),
        status=fields.get("Stato", "") or status,
        extra={k: v for k, v in fields.items()
               if k in ("Lezioni/errori", "Costi", "Prossimo passo")},
    )


def target_path(atom: Atom) -> Path:
    """Dove vive la vista Markdown di questo atomo."""
    if atom.kind == "decision":
        return resolve("memory_adr") / f"{atom.id}.md"
    if atom.kind == "checkpoint":
        return resolve("memory_cp") / f"{atom.id}.md"
    return resolve("memory") / atom.kind / f"{atom.id}.md"


def write_view(atom: Atom, *, overwrite: bool = False) -> Path:
    """Scrive la vista Markdown. Non sovrascrive un file esistente senza overwrite=True."""
    p = target_path(atom)
    p.parent.mkdir(parents=True, exist_ok=True)
    if p.exists() and not overwrite:
        return p
    # newline="\n" NON e' un dettaglio: senza, su Windows write_text traduce ogni \n in
    # \r\n e la vista esce in CRLF mentre tutto il repo e' LF. Git allora vede il file
    # RISCRITTO DA CAPO invece che modificato, e al merge non sa piu' cosa tenere.
    # E' B-028, misurato: un checkpoint di 12 righe cambiate risultava 100 insertions /
    # 90 deletions. Ed e' la stessa forma del guaio che il 2026-08-23 stava per duplicare
    # ~6500 righe di STATO-EMPIRE. Chiuso il 2026-09-03.
    p.write_text(render(atom), encoding="utf-8", newline="\n")
    return p
