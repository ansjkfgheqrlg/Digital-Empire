"""
EMPIRE — risoluzione dei path del monorepo.

Owner: Max · Controllore: Claude · Origine: FORGE (seed CP-20260722-006)
Governo: MANDATO Art.8 + ADR-003 (wrap) + ADR-008 (intestazione)

FILE CONGELATO — è la fondazione condivisa Max/Gael/Gemini.
Modifiche solo con nota di coordinamento in company/Memory/STATO-EMPIRE.md.

Regole non negoziabili:
  - zero path assoluti hardcoded: la radice si TROVA, non si dichiara
  - ogni open() usa encoding="utf-8"
  - i path del monorepo contengono spazi ("qui tutto", "Digital Empire"):
    sempre pathlib.Path e liste di argomenti, mai interpolazione in stringa shell
"""
from __future__ import annotations

import os
import sys
import tomllib
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Iterator

__all__ = [
    "EmpireRootNotFound", "UnknownAlias",
    "repo_root", "config_data", "resolve", "resolve_legacy",
    "iter_files", "rel", "safe_stdout",
]


class EmpireRootNotFound(RuntimeError):
    """La radice del monorepo non è stata trovata risalendo dall'albero."""


class UnknownAlias(KeyError):
    """Alias logico non presente in empire.toml."""


def safe_stdout() -> None:
    """Windows cp1252 manda in crash qualunque print con emoji.

    Bug reale osservato il 2026-07-22 su
    WORKFLOW-ESTATE/02-AUTOMAZIONI-E-SCRIPTS/memory_manager.py:
        UnicodeEncodeError: 'charmap' codec can't encode character '\\U0001f9e0'
    Chiamare questa funzione come PRIMA istruzione di ogni entry-point.
    """
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            try:
                stream.reconfigure(encoding="utf-8", errors="replace")
            except (ValueError, OSError):
                pass


@lru_cache(maxsize=1)
def _toml_path() -> Path:
    return Path(__file__).resolve().parent / "empire.toml"


@lru_cache(maxsize=1)
def config_data() -> dict:
    """Contenuto di empire.toml. Letto una sola volta per processo."""
    p = _toml_path()
    if not p.exists():
        raise EmpireRootNotFound(f"empire.toml mancante: atteso in {p}")
    with open(p, "rb") as fh:
        return tomllib.load(fh)


@lru_cache(maxsize=1)
def repo_root() -> Path:
    """Radice del monorepo, trovata risalendo finché non compare il root_marker.

    Ordine di ricerca: EMPIRE_ROOT (env) → dalla posizione di questo file → dal CWD.
    """
    marker = config_data()["meta"]["root_marker"]

    env = os.environ.get("EMPIRE_ROOT")
    if env:
        cand = Path(env).expanduser().resolve()
        if (cand / marker).exists():
            return cand

    tried: list[str] = []
    for start in (Path(__file__).resolve().parent, Path.cwd().resolve()):
        tried.append(str(start))
        for cand in (start, *start.parents):
            if (cand / marker).exists():
                return cand

    raise EmpireRootNotFound(
        "Radice del monorepo non trovata.\n"
        f"  cercavo il marker: {marker}\n"
        f"  ho risalito da:    {' e da '.join(tried)}\n"
        "  soluzione: esegui da dentro il monorepo, oppure imposta EMPIRE_ROOT."
    )


def resolve(alias: str, *parts: str) -> Path:
    """Alias logico (o path relativo alla radice) → Path assoluto.

    >>> resolve("memory_cp")                      # company/Memory/checkpoints
    >>> resolve("memory_cp", "CP-20260722-005.md")
    """
    aliases = config_data()["alias"]
    if alias in aliases:
        base = repo_root() / aliases[alias]
    elif (repo_root() / alias).exists():
        base = repo_root() / alias
    else:
        known = ", ".join(sorted(aliases))
        raise UnknownAlias(f"alias sconosciuto: {alias!r}. Noti: {known}")
    return base.joinpath(*parts) if parts else base


def resolve_legacy(ref: str, cited_from: Path | None = None) -> Path | None:
    """Ripara un riferimento scritto dentro un .md senza modificare il .md (ADR-003).

    Ordine di tentativi:
      1. relativo al file che lo cita
      2. relativo alla radice del monorepo
      3. eccezione esplicita in [legacy_files]
      4. prefisso logico da [legacy]  (es. "00-MEMORY/..." -> DIGITAL-EMPIRE/00-MEMORY/...)
    Restituisce None se davvero non esiste da nessuna parte (= dead-end, finding bloccante).
    """
    ref = ref.strip().strip("`").strip()
    if not ref:
        return None
    ref = ref.replace("\\", "/").lstrip("./").rstrip("/")
    root = repo_root()

    if cited_from is not None:
        base = cited_from.parent if cited_from.is_file() else cited_from
        cand = (base / ref)
        if cand.exists():
            return cand.resolve()

    cand = root / ref
    if cand.exists():
        return cand.resolve()

    cfg = config_data()
    exact = cfg.get("legacy_files", {}).get(ref)
    if exact and (root / exact).exists():
        return (root / exact).resolve()

    head, _, tail = ref.partition("/")
    mapped = cfg.get("legacy", {}).get(head)
    if mapped:
        cand = root / mapped / tail if tail else root / mapped
        if cand.exists():
            return cand.resolve()

    return None


def rel(p: Path | str) -> str:
    """Path → stringa relativa alla radice, con slash. Per output leggibile e stabile."""
    p = Path(p).resolve()
    try:
        return p.relative_to(repo_root()).as_posix()
    except ValueError:
        return p.as_posix()


def iter_files(base: Path | str | None = None, *, suffixes: tuple[str, ...] | None = None) -> Iterator[Path]:
    """Scansione veloce con le esclusioni di [scan]. os.scandir, non rglob."""
    cfg = config_data()["scan"]
    excl_dirs = set(cfg["exclude_dirs"])
    excl_suf = tuple(cfg["exclude_suffix"])

    start = Path(base) if base is not None else repo_root()
    if start.is_file():
        yield start
        return

    stack = [start]
    while stack:
        cur = stack.pop()
        try:
            entries = list(os.scandir(cur))
        except (PermissionError, FileNotFoundError, OSError):
            continue
        for e in entries:
            name = e.name
            try:
                if e.is_dir(follow_symlinks=False):
                    if name in excl_dirs or name.startswith(".git"):
                        continue
                    stack.append(Path(e.path))
                elif e.is_file(follow_symlinks=False):
                    if name.endswith(excl_suf):
                        continue
                    if suffixes and not name.endswith(suffixes):
                        continue
                    yield Path(e.path)
            except OSError:
                continue


@dataclass(slots=True, frozen=True)
class RootInfo:
    root: Path
    marker: str
    aliases: int
    version: str


def info() -> RootInfo:
    cfg = config_data()
    return RootInfo(
        root=repo_root(),
        marker=cfg["meta"]["root_marker"],
        aliases=len(cfg["alias"]),
        version=cfg["meta"]["version"],
    )
