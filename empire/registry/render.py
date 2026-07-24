"""
empire.registry.render — rigenerazione chirurgica di REGISTRO-IMPRESA.md e skills-map.yaml preservando le sezioni manuali.

Owner: Max · Controllore: Claude · Origine: FORGE (GEM-04)
Governo: MANDATO Art.8 + ADR-008
"""
from __future__ import annotations

import re
from pathlib import Path
from typing import Sequence

from empire.paths import repo_root
from empire.schema import Artifact

__all__ = ["render_all", "render_registro", "render_skills_map"]

MD_BEGIN_MARKER = "<!-- EMPIRE-CENSUS:BEGIN (rigenerato, non modificare a mano) -->"
MD_END_MARKER = "<!-- EMPIRE-CENSUS:END -->"

YAML_BEGIN_MARKER = "# <!-- EMPIRE-CENSUS:BEGIN (rigenerato, non modificare a mano) -->"
YAML_END_MARKER = "# <!-- EMPIRE-CENSUS:END -->"


def _replace_block(text: str, begin_marker: str, end_marker: str, new_content: str, default_insert_before: str | None = None) -> str:
    """Sostituisce il blocco tra begin e end marker preservando millimetricamente tutto il testo esterno."""
    if begin_marker in text and end_marker in text:
        pattern = re.compile(re.escape(begin_marker) + r".*?" + re.escape(end_marker), re.DOTALL)
        replacement = f"{begin_marker}\n{new_content}\n{end_marker}"
        return pattern.sub(replacement, text)
    
    # Se i marker non esistono ancora, li inseriamo prima di un marcatore noto (es. Regola di chiusura) o alla fine
    block = f"\n{begin_marker}\n{new_content}\n{end_marker}\n"
    if default_insert_before and default_insert_before in text:
        parts = text.split(default_insert_before, 1)
        return parts[0].rstrip() + "\n" + block + "\n" + default_insert_before + parts[1]
    
    return text.rstrip() + "\n" + block


def render_registro(artifacts: Sequence[Artifact], root: Path | None = None) -> Path:
    """Rigenera la tabella di censimento automatico dentro REGISTRO-IMPRESA.md."""
    if root is None:
        root = repo_root()

    target_path = root / "company" / "REGISTRO-IMPRESA.md"
    if not target_path.exists():
        return target_path

    original_text = target_path.read_text(encoding="utf-8", errors="replace")

    # Filtra e ordina artefatti maggiori censiti
    majors = [a for a in artifacts if a.kind in ("agent", "department", "ecosystem", "workflow", "skill", "dashboard") and a.kind != "vendored"]
    majors.sort(key=lambda a: (a.kind, str(a.path)))

    lines = [
        "## 6. CENSIMENTO AUTOMATICO DEGLI ARTEFATTI MAGGIORI (FORGE / census.py)",
        "",
        "| Tipo | Path | Proprietario (Owner) | Controllore | Origine | Governo | CF-Grade |",
        "|---|---|---|---|---|---|---|"
    ]
    for a in majors[:600]:  # Cap a 600 per leggibilità e DoD-2 (>= 500 censiti)
        p_str = a.path.as_posix() if isinstance(a.path, Path) else str(a.path)
        ow = a.prov.owner or "—"
        co = a.prov.controller or "—"
        ori = a.prov.origin or "—"
        gov = a.prov.governance or "—"
        cfg = "✅ 7/7" if getattr(a, "cf_grade", False) else "—"
        lines.append(f"| `{a.kind}` | `{p_str}` | {ow} | {co} | {ori} | {gov} | {cfg} |")

    new_block = "\n".join(lines)
    updated_text = _replace_block(original_text, MD_BEGIN_MARKER, MD_END_MARKER, new_block, default_insert_before="## Regola di chiusura")
    target_path.write_text(updated_text, encoding="utf-8")
    return target_path


def render_skills_map(artifacts: Sequence[Artifact], root: Path | None = None) -> Path:
    """Rigenera il blocco di censimento in skills-map.yaml preservando le sezioni manuali."""
    if root is None:
        root = repo_root()

    target_path = root / "company" / "skills-map.yaml"
    if not target_path.exists():
        return target_path

    original_text = target_path.read_text(encoding="utf-8", errors="replace")

    skills_wfs = [a for a in artifacts if a.kind in ("skill", "workflow", "script") and a.kind != "vendored"]
    skills_wfs.sort(key=lambda a: (a.kind, str(a.path)))

    # Le voci vanno sotto una loro chiave (`artefatti:`). Prima venivano emesse allo
    # stesso livello di `note:`, cioe' una chiave di mappa seguita da elementi di lista:
    # YAML non valido. Risultato: `company/skills-map.yaml` — l'anagrafe che per ADR-008
    # deve garantire che nessun artefatto sia orfano — non era leggibile da nessun
    # parser. Il difetto e' sopravvissuto perche' il file veniva solo scritto e letto a
    # occhio, mai caricato da una macchina.
    lines = [
        "censimento_automatico_forge:",
        "  note: 'Sezione generata automaticamente da empire.registry.render (ADR-008). Non modificare a mano.'",
        "  artefatti:",
    ]
    for a in skills_wfs[:400]:
        p_str = a.path.as_posix() if isinstance(a.path, Path) else str(a.path)
        slug = p_str.replace("/", "_").replace(".", "_").lower()[:60]
        lines.append(f"    - id: auto_{slug}")
        lines.append(f"      percorso: {p_str}")
        lines.append(f"      tipo: {a.kind}")
        ow = a.prov.owner or "non-dichiarato"
        lines.append(f"      proprietario: \"{ow}\"")

    new_block = "\n".join(lines)
    updated_text = _replace_block(original_text, YAML_BEGIN_MARKER, YAML_END_MARKER, new_block, default_insert_before="stats:")
    target_path.write_text(updated_text, encoding="utf-8")
    return target_path


def render_all(artifacts: Sequence[Artifact], root: Path | None = None) -> tuple[Path, Path]:
    if root is None:
        root = repo_root()
    p1 = render_registro(artifacts, root=root)
    p2 = render_skills_map(artifacts, root=root)
    return p1, p2
