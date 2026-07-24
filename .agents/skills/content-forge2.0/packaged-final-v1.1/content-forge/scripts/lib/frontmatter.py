"""Parse/serialize YAML frontmatter da/verso markdown.

Usato da: schema_validator.py, obsidian_packager.py, e ovunque serva manipolare
frontmatter di file markdown.

Part of: content-forge / scripts/lib
"""
from __future__ import annotations

import re
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:
    yaml = None  # type: ignore

__all__ = ["parse", "split", "serialize", "merge_into_file"]


_FM_RE = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.DOTALL)


def split(text: str) -> tuple[dict | None, str]:
    """Spezza markdown in (frontmatter_dict, body).
    Se non c'è frontmatter, ritorna (None, text).
    Se yaml non installato e c'è frontmatter, ritorna (raw_dict_unparsed, body).
    """
    m = _FM_RE.match(text)
    if not m:
        return None, text
    fm_raw = m.group(1)
    body = m.group(2)
    if yaml is None:
        # Best-effort: split key:value lines (non gestisce nested o liste complesse)
        fm = {}
        for line in fm_raw.split("\n"):
            line = line.rstrip()
            if not line or line.startswith("#"):
                continue
            if ":" in line and not line.startswith(" ") and not line.startswith("-"):
                k, _, v = line.partition(":")
                fm[k.strip()] = v.strip().strip('"').strip("'")
        return fm, body
    try:
        fm = yaml.safe_load(fm_raw) or {}
        return fm, body
    except yaml.YAMLError:
        return None, text


def parse(path: str | Path) -> tuple[dict | None, str]:
    """Legge file markdown e ritorna (frontmatter, body)."""
    path = Path(path)
    text = path.read_text(encoding="utf-8")
    return split(text)


def serialize(frontmatter: dict, body: str) -> str:
    """Serializza dict + body in markdown con frontmatter."""
    if yaml is None:
        # Fallback molto basic
        lines = ["---"]
        for k, v in frontmatter.items():
            if isinstance(v, list):
                lines.append(f"{k}:")
                for item in v:
                    lines.append(f"  - {item}")
            elif isinstance(v, dict):
                lines.append(f"{k}:")
                for subk, subv in v.items():
                    lines.append(f"  {subk}: {subv}")
            else:
                # Quote se contiene caratteri speciali
                if isinstance(v, str) and (":" in v or "#" in v or v.startswith("<")):
                    v = f'"{v}"'
                lines.append(f"{k}: {v}")
        lines.append("---")
        lines.append("")
        lines.append(body.lstrip("\n"))
        return "\n".join(lines)
    fm_text = yaml.safe_dump(frontmatter, default_flow_style=False, allow_unicode=True, sort_keys=False)
    return f"---\n{fm_text}---\n{body}"


def merge_into_file(path: str | Path, updates: dict) -> None:
    """Aggiorna chiavi del frontmatter di un file, preservando il body."""
    path = Path(path)
    fm, body = parse(path)
    fm = fm or {}
    fm.update(updates)
    path.write_text(serialize(fm, body), encoding="utf-8")
