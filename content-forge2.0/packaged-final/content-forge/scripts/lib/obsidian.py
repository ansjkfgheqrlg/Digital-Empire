"""Helper Obsidian-specifici: slug, wikilink integrity, MOC scaffold.

Usato da: scripts/obsidian_packager.py + B7 wiki-builder-agent.

Part of: content-forge / scripts/lib
"""
from __future__ import annotations

import re
import unicodedata
from pathlib import Path

from . import markdown_tools

__all__ = [
    "slugify",
    "build_alias_index",
    "check_wikilink_integrity",
    "weave_wikilinks",
]


def slugify(title: str, style: str = "kebab", max_len: int = 60) -> str:
    """Slug per filename Obsidian.

    style: "kebab" (default), "snake", "title"
    """
    s = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode()
    s = re.sub(r"[^\w\s-]", "", s).strip().lower()
    if style == "kebab":
        result = re.sub(r"[\s_]+", "-", s)
    elif style == "snake":
        result = re.sub(r"[\s-]+", "_", s)
    elif style == "title":
        result = title.strip()
    else:
        raise ValueError(f"unknown style: {style}")
    return result[:max_len].rstrip("-_")


def build_alias_index(vault_dir: str | Path) -> dict[str, str]:
    """Cammina il vault e costruisce mappa alias→slug (per weaving wikilink).

    Restituisce: {alias_lower: slug, ...}
    Considera sia il filename che il campo `aliases` nel frontmatter.
    """
    from .frontmatter import parse as parse_fm
    vault_dir = Path(vault_dir)
    index: dict[str, str] = {}
    for note in vault_dir.rglob("*.md"):
        slug = note.stem
        # Lo slug stesso è un alias
        index[slug.lower()] = slug
        # Aggiungi aliases dal frontmatter
        try:
            fm, _ = parse_fm(note)
        except Exception:
            fm = None
        if fm and isinstance(fm, dict):
            for alias in fm.get("aliases", []) or []:
                if isinstance(alias, str):
                    index[alias.lower()] = slug
            # Anche il title
            title = fm.get("title")
            if isinstance(title, str):
                index[title.lower()] = slug
    return index


def check_wikilink_integrity(vault_dir: str | Path) -> list[dict]:
    """Verifica che ogni [[wikilink]] punti a un file esistente.

    Ritorna lista di issue: [{file, target, offset, raw}, ...].
    Lista vuota = tutto OK.
    """
    vault_dir = Path(vault_dir)
    existing = {p.stem.lower() for p in vault_dir.rglob("*.md")}
    # Aggiungi gli aliases come "esistenti"
    aliases = build_alias_index(vault_dir)
    existing |= set(aliases.keys())

    issues = []
    for note in vault_dir.rglob("*.md"):
        text = note.read_text(encoding="utf-8")
        wls = markdown_tools.extract_wikilinks(text)
        for wl in wls:
            target = wl["target"]
            target_lower = target.lower()
            # 1. Match diretto (stem o alias)
            if target_lower in existing:
                continue
            # 2. Match path-based: [[folder/note]] → cerca folder/note.md
            if "/" in target:
                # Risolvi rispetto al vault dir
                candidate = (vault_dir / f"{target}.md")
                if candidate.exists():
                    continue
                # Anche relativo (folder/note → cerca qualunque match)
                stem = target.split("/")[-1].lower()
                if stem in existing:
                    continue
            issues.append({
                "file": str(note.relative_to(vault_dir)),
                "target": target,
                "offset": wl["offset"],
                "raw": wl["raw"],
            })
    return issues


def weave_wikilinks(text: str, alias_index: dict[str, str],
                    once_per_section: bool = True) -> str:
    """Sostituisce menzioni di alias con [[wikilink]].

    Strategia: word-boundary, case-insensitive, match dell'alias più lungo per primo.
    Se `once_per_section`: solo prima occorrenza per ogni heading section.
    """
    sorted_aliases = sorted(alias_index.keys(), key=len, reverse=True)

    if not once_per_section:
        for alias in sorted_aliases:
            slug = alias_index[alias]
            if alias.lower() == slug.lower():
                replacement = f"[[{slug}]]"
            else:
                # Preserva la forma originale come alias visualizzato
                replacement = f"[[{slug}|{alias}]]"
            pattern = re.compile(rf"\b{re.escape(alias)}\b", re.I)
            text = pattern.sub(replacement, text, count=1)
        return text

    # once_per_section: spezza per heading, applica per sezione
    sections = re.split(r"^(#+\s.*)$", text, flags=re.MULTILINE)
    out_parts = []
    for part in sections:
        if part.lstrip().startswith("#"):
            out_parts.append(part)
            continue
        for alias in sorted_aliases:
            slug = alias_index[alias]
            replacement = f"[[{slug}]]" if alias.lower() == slug.lower() else f"[[{slug}|{alias}]]"
            pattern = re.compile(rf"\b{re.escape(alias)}\b", re.I)
            part = pattern.sub(replacement, part, count=1)
        out_parts.append(part)
    return "".join(out_parts)
