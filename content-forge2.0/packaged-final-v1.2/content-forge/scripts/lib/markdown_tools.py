"""Parsing/manipolazione markdown (heading tree, TOC, link extraction).

Usato da: doc-builder (verifica TOC), MKD-builder (cross-ref weaving), wiki-builder.

Part of: content-forge / scripts/lib
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any

__all__ = [
    "Heading",
    "extract_headings",
    "extract_links",
    "extract_wikilinks",
    "build_toc",
    "word_count",
    "strip_code_blocks",
    "strip_html_comments",
]


@dataclass
class Heading:
    level: int          # 1..6
    text: str
    anchor: str         # slug per anchor link
    offset: int         # byte offset nel testo
    children: list["Heading"] = field(default_factory=list)


_HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)(?:\s+\{#([\w-]+)\})?\s*$", re.MULTILINE)
_CODE_BLOCK_RE = re.compile(r"```.*?```", re.DOTALL)
_INLINE_CODE_RE = re.compile(r"`[^`]+`")
_LINK_RE = re.compile(r"(?<!!)\[([^\]]+)\]\(([^)]+)\)")
_WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:\#([^\]|]+))?(?:\|([^\]]+))?\]\]")
_HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)


def _slugify(text: str) -> str:
    """Slug semplice per anchor (sostituibile da naming.md regex)."""
    import unicodedata
    s = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    s = re.sub(r"[^\w\s-]", "", s).strip().lower()
    return re.sub(r"[\s_]+", "-", s)


def extract_headings(text: str) -> list[Heading]:
    """Estrae heading da markdown. Ignora heading dentro blocchi code."""
    # Maschera i code blocks
    masked = _CODE_BLOCK_RE.sub(lambda m: " " * len(m.group(0)), text)
    headings = []
    for m in _HEADING_RE.finditer(masked):
        level = len(m.group(1))
        title = m.group(2).strip()
        explicit_anchor = m.group(3)
        anchor = explicit_anchor or _slugify(title)
        headings.append(Heading(level=level, text=title, anchor=anchor, offset=m.start()))
    return headings


def build_toc(text: str, max_level: int = 3) -> str:
    """Genera TOC markdown dai heading (livelli H2 e H3 di default)."""
    headings = extract_headings(text)
    lines = []
    for h in headings:
        if h.level == 1 or h.level > max_level:
            continue
        indent = "  " * (h.level - 2)
        lines.append(f"{indent}- [{h.text}](#{h.anchor})")
    return "\n".join(lines)


def extract_links(text: str) -> list[tuple[str, str, int]]:
    """Estrae link markdown standard [text](url). Ritorna (text, url, offset)."""
    masked = _CODE_BLOCK_RE.sub(lambda m: " " * len(m.group(0)), text)
    return [(m.group(1), m.group(2), m.start()) for m in _LINK_RE.finditer(masked)]


def extract_wikilinks(text: str) -> list[dict]:
    """Estrae wikilink Obsidian [[target]] / [[target#anchor]] / [[target|alias]]."""
    masked = _CODE_BLOCK_RE.sub(lambda m: " " * len(m.group(0)), text)
    results = []
    for m in _WIKILINK_RE.finditer(masked):
        results.append({
            "target": m.group(1).strip(),
            "anchor": (m.group(2) or "").strip() or None,
            "alias": (m.group(3) or "").strip() or None,
            "offset": m.start(),
            "raw": m.group(0),
        })
    return results


def word_count(text: str, exclude_code: bool = True) -> int:
    """Conta parole, opzionalmente escludendo code blocks."""
    if exclude_code:
        text = _CODE_BLOCK_RE.sub(" ", text)
        text = _INLINE_CODE_RE.sub(" ", text)
    # Conta sequenze di word chars
    return len(re.findall(r"\b\w+\b", text))


def strip_code_blocks(text: str) -> str:
    """Rimuove tutti i code blocks dal testo (utile per analisi semantica)."""
    return _CODE_BLOCK_RE.sub("", text)


def strip_html_comments(text: str) -> str:
    """Rimuove commenti HTML (utile per pulire FORGE_SOURCE_BOUNDARY se serve testo display)."""
    return _HTML_COMMENT_RE.sub("", text)
