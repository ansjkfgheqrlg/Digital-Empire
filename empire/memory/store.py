"""
EMPIRE MEMORY — archivio append-only e assegnazione ID senza collisioni.

Owner: Max · Controllore: Claude · Origine: FORGE (M-A) · Governo: ADR-002

Chiude B-009: il 2026-07-22 la collisione di ID checkpoint si e' verificata TRE volte in
quindici minuti (Claude e Gael in parallelo su CP-20260722-002 e -003), perche' l'ID si
assegnava contando i file a occhio. Qui l'ID si assegna sotto lock esclusivo su file,
leggendo il massimo NNN sia dagli atomi sia dai nomi dei file gia' su disco.
"""
from __future__ import annotations

import json
import os
import re
import time
from pathlib import Path
from typing import Iterator

from ..config import data_dir
from ..paths import repo_root, resolve
from .model import Atom, PREFIX, today_compact

__all__ = ["atoms_path", "next_id", "write", "write_many", "read", "all_atoms", "stats", "IdLockTimeout"]

_LOCK_TIMEOUT_S = 5.0
_LOCK_POLL_S = 0.05
_MAX_BYTES = 50 * 1024 * 1024      # rotazione a 50 MB

# Dove cercare ID gia' usati oltre a atoms.jsonl (nomi file su disco).
_DISK_SOURCES: dict[str, tuple[str, ...]] = {
    "CP":  ("memory_cp",),
    "ADR": ("memory_adr",),
}
_FILE_ID_RE = re.compile(r"^([A-Z]+)-(\d{8})-(\d{3})")


class IdLockTimeout(RuntimeError):
    """Lock dell'ID non ottenuto entro il timeout."""


def atoms_path() -> Path:
    return data_dir("memory") / "atoms.jsonl"


def _lock_path() -> Path:
    return data_dir("memory") / ".idlock"


# --------------------------------------------------------------------------- lock
class _IdLock:
    """Lock esclusivo su file, portabile (O_CREAT|O_EXCL). Regge processi diversi."""

    def __init__(self, timeout: float = _LOCK_TIMEOUT_S):
        self.timeout = timeout
        self.fd: int | None = None

    def __enter__(self) -> "_IdLock":
        p = _lock_path()
        deadline = time.monotonic() + self.timeout
        while True:
            try:
                self.fd = os.open(p, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
                os.write(self.fd, f"{os.getpid()} {time.time():.3f}".encode())
                return self
            except FileExistsError:
                # lock abbandonato da un processo morto: recupero dopo 30 s
                try:
                    if time.time() - p.stat().st_mtime > 30:
                        p.unlink(missing_ok=True)
                        continue
                except OSError:
                    pass
                if time.monotonic() > deadline:
                    raise IdLockTimeout(
                        f"lock ID non ottenuto in {self.timeout}s ({p}). "
                        "Se nessun altro processo sta scrivendo, cancella il file."
                    )
                time.sleep(_LOCK_POLL_S)

    def __exit__(self, *exc) -> None:
        if self.fd is not None:
            os.close(self.fd)
        _lock_path().unlink(missing_ok=True)


# --------------------------------------------------------------------------- id
def _max_seq_in_atoms(prefix: str, day: str) -> int:
    hi = 0
    p = atoms_path()
    if not p.exists():
        return 0
    head = f'"{prefix}-{day}-'
    with open(p, encoding="utf-8", errors="replace") as fh:
        for line in fh:
            if head not in line:
                continue
            try:
                aid = json.loads(line).get("id", "")
            except json.JSONDecodeError:
                continue
            m = _FILE_ID_RE.match(aid or "")
            if m and m.group(1) == prefix and m.group(2) == day:
                hi = max(hi, int(m.group(3)))
    return hi


def _max_seq_on_disk(prefix: str, day: str) -> int:
    """Legge anche i file .md gia' presenti: e' cosi' che si evita la collisione con Gael."""
    hi = 0
    for alias in _DISK_SOURCES.get(prefix, ()):
        try:
            d = resolve(alias)
        except Exception:
            continue
        if not d.is_dir():
            continue
        for f in d.iterdir():
            m = _FILE_ID_RE.match(f.name)
            if m and m.group(1) == prefix and m.group(2) == day:
                hi = max(hi, int(m.group(3)))
    return hi


def next_id(kind: str, *, day: str | None = None, _locked: bool = False) -> str:
    """Prossimo ID libero per (kind, giorno). Da chiamare SEMPRE sotto lock."""
    prefix = PREFIX.get(kind, "ATOM")
    day = day or today_compact()

    def _compute() -> str:
        seq = max(_max_seq_in_atoms(prefix, day), _max_seq_on_disk(prefix, day)) + 1
        if seq > 999:
            raise RuntimeError(f"esauriti gli ID per {prefix}-{day} (999). Serve un ADR.")
        return f"{prefix}-{day}-{seq:03d}"

    if _locked:
        return _compute()
    with _IdLock():
        return _compute()


# --------------------------------------------------------------------------- write
def _rotate_if_needed() -> None:
    p = atoms_path()
    if p.exists() and p.stat().st_size > _MAX_BYTES:
        n = 1
        while (alt := p.with_suffix(f".{n}.jsonl")).exists():
            n += 1
        p.rename(alt)


def write(atom: Atom, *, dedup: bool = False) -> Atom:
    """Assegna l'ID (se manca) e appende. Ritorna l'atomo completo.

    dedup=True: se un atomo con lo stesso hash di contenuto esiste gia', non riscrive
    e restituisce quello esistente. Serve all'import, che deve essere idempotente.
    """
    atom.validate()
    if not atom.hash:
        atom.hash = atom.compute_hash()

    if dedup:
        for existing in all_atoms():
            if existing.hash == atom.hash:
                return existing

    with _IdLock():
        if not atom.id:
            atom.id = next_id(atom.kind, day=today_compact(atom.ts), _locked=True)
        _rotate_if_needed()
        line = json.dumps(atom.to_dict(), ensure_ascii=False)
        with open(atoms_path(), "a", encoding="utf-8") as fh:
            fh.write(line + "\n")
            fh.flush()
            os.fsync(fh.fileno())
    return atom


def write_many(atoms: list[Atom]) -> list[Atom]:
    """Scrittura in blocco: un solo lock e un solo fsync per l'intero lotto.

    Serve all'import storico: 255 atomi con lock+fsync individuali costano ~20 s,
    in blocco meno di un secondo. Gli ID restano comunque univoci perche' il lock
    copre l'intera sequenza di assegnazione.
    """
    if not atoms:
        return []
    for a in atoms:
        a.validate()
        if not a.hash:
            a.hash = a.compute_hash()

    with _IdLock():
        _rotate_if_needed()
        used: dict[tuple[str, str], int] = {}
        lines = []
        for a in atoms:
            if not a.id:
                day = today_compact(a.ts)
                key = (a.prefix, day)
                if key not in used:
                    used[key] = max(_max_seq_in_atoms(a.prefix, day),
                                    _max_seq_on_disk(a.prefix, day))
                used[key] += 1
                a.id = f"{a.prefix}-{day}-{used[key]:03d}"
            lines.append(json.dumps(a.to_dict(), ensure_ascii=False))
        with open(atoms_path(), "a", encoding="utf-8") as fh:
            fh.write("\n".join(lines) + "\n")
            fh.flush()
            os.fsync(fh.fileno())
    return atoms


# --------------------------------------------------------------------------- read
def all_atoms(*, kind: str | None = None) -> Iterator[Atom]:
    p = atoms_path()
    if not p.exists():
        return
    with open(p, encoding="utf-8", errors="replace") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                d = json.loads(line)
            except json.JSONDecodeError:
                continue
            if kind and d.get("kind") != kind:
                continue
            yield Atom.from_dict(d)


def read(atom_id: str) -> Atom | None:
    """Ultima versione dell'atomo (append-only: l'ultima riga vince)."""
    found = None
    for a in all_atoms():
        if a.id == atom_id:
            found = a
    return found


def stats() -> dict:
    counts: dict[str, int] = {}
    last = None
    total = 0
    for a in all_atoms():
        counts[a.kind] = counts.get(a.kind, 0) + 1
        total += 1
        last = a
    p = atoms_path()
    return {
        "total": total,
        "by_kind": dict(sorted(counts.items(), key=lambda x: -x[1])),
        "last": {"id": last.id, "title": last.title, "ts": last.ts} if last else None,
        "path": str(p.relative_to(repo_root())) if p.exists() else "(vuoto)",
    }
