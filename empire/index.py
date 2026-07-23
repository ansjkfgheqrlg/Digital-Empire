"""
EMPIRE — indice materializzato: costruisce, cachea e interroga il catalogo azienda.

Owner: Gael · Controllore: Claude · Origine: FORGE (lotto G-A, CP-20260722)
Governo: MANDATO Art.8 + ADR-008
"""
from __future__ import annotations

import json
import time
from pathlib import Path

from .paths import repo_root, rel
from . import loader

__all__ = ["build_index", "load_index", "search", "stats", "INDEX_PATH", "META_PATH"]

_CACHE_DIR = repo_root() / "empire" / ".cache"
INDEX_PATH = _CACHE_DIR / "index.json"
META_PATH = _CACHE_DIR / "index.meta.json"

_KIND_LOADERS = {
    "agents": loader.load_agents,
    "departments": loader.load_departments,
    "ecosystems": loader.load_ecosystems,
    "workflows": loader.load_workflows,
    "skills": loader.load_skills,
}


def build_index() -> dict:
    """Esegue tutti i loader, produce un dict serializzabile e lo scrive su disco.

    Idempotente: due run consecutivi producono lo stesso contenuto (a parità di stato
    disco), zero duplicati — ogni run ricostruisce da zero, non fa append.
    """
    t0 = time.time()
    data: dict = {}
    for kind, fn in _KIND_LOADERS.items():
        items = fn()
        data[kind] = [it.to_dict() for it in items]
    dt = time.time() - t0

    _CACHE_DIR.mkdir(parents=True, exist_ok=True)
    INDEX_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")

    meta = {
        "built_at": time.time(),
        "build_seconds": round(dt, 3),
        "counts": {k: len(v) for k, v in data.items()},
    }
    META_PATH.write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8")
    return data


def load_index(max_age_s: int = 3600) -> dict:
    """Usa la cache se fresca, altrimenti ricostruisce."""
    if INDEX_PATH.exists() and META_PATH.exists():
        try:
            meta = json.loads(META_PATH.read_text(encoding="utf-8"))
            if time.time() - meta.get("built_at", 0) < max_age_s:
                return json.loads(INDEX_PATH.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            pass
    return build_index()


def search(query: str, kind: str | None = None) -> list[dict]:
    """Ricerca substring case-insensitive su id/name/path/skill."""
    data = load_index()
    q = query.lower().strip()
    if not q:
        return []
    kinds = [kind] if kind else list(data.keys())
    out: list[dict] = []
    for k in kinds:
        for item in data.get(k, []):
            hay = " ".join(str(v) for key, v in item.items()
                            if key in ("id", "name", "path") and v is not None)
            skills = item.get("skills") or []
            hay += " " + " ".join(skills)
            if q in hay.lower():
                out.append({"kind": k, **item})
    return out


def stats() -> dict:
    data = load_index()
    agents = data.get("agents", [])
    out = {
        "counts": {k: len(v) for k, v in data.items()},
        "agents_by_ecosystem": {},
        "agents_cf_grade": sum(1 for a in agents if a.get("cf_grade")),
        "agents_no_provenance": sum(
            1 for a in agents if not (a.get("prov") or {}).get("owner")
        ),
    }
    by_eco: dict = {}
    for a in agents:
        eco = a.get("ecosystem") or "(sconosciuto)"
        by_eco[eco] = by_eco.get(eco, 0) + 1
    out["agents_by_ecosystem"] = dict(sorted(by_eco.items(), key=lambda kv: -kv[1]))
    return out