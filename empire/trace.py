"""
EMPIRE — le 5 tracce: il lavoro che si registra da solo.

Owner: Claude · Origine: FORGE (esecuzione del PIANO 2, CP-20260724)
Piano: WORKFLOW-ESTATE/01-FLUSSI-E-PIANI/RISTRUTTURAZIONE-02-CICLI.md

## Perche' esiste

`WORKFLOW-ESTATE/02-AUTOMAZIONI-E-SCRIPTS/` ha 11 cartelle e **zero file**. Non e' disordine:
e' il segno che nessun lavoro ha mai lasciato una traccia. La conseguenza misurata e' che
`empire inspect` restituisce 0 su tutte e sei le metriche, con nota "nessun record PERF".

La regola memory-first (ADR-002) esisteva gia', le cartelle pure, e sono rimaste vuote per mesi.
Il motivo non e' indisciplina: **scrivere la traccia era un atto separato**, e gli atti separati
non si fanno. Per questo qui la traccia e' un sottoprodotto, non un compito in piu'.

## Le 5 tracce

    DECISIONE   quando si sceglie fra due strade   -> non ridiscutere fra un mese
    ERRORE      quando qualcosa fallisce           -> non ripetere lo stesso sbaglio
    PRESTAZIONE quando una fase si chiude          -> sapere quanto costa davvero
    LEZIONE     quando si capisce un pattern       -> migliorare il metodo
    SESSIONE    apertura e chiusura di una finestra -> riprendere dove si era rimasti

## Le due regole non negoziabili

1. **Ogni traccia ha un autore.** Non "il sistema": un nome. Serve perche' Max, Gael e Gemini
   lavorano in parallelo e il 19/07 si e' dovuto ricostruire a mano chi avesse fatto cosa.
2. **Ogni traccia ha una prova.** Un campo `prova` vuoto viene rifiutato: senza evidenza, una
   dichiarazione e' solo una parola. E' la stessa regola gia' in vigore nei gate.
"""
from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass, field
from datetime import datetime
from pathlib import Path

from .paths import repo_root

__all__ = ["Traccia", "TIPI", "cartella_per", "scrivi", "leggi", "cerca", "conta"]

# tipo -> cartella (tutte gia' esistenti e vuote: non si crea struttura nuova)
TIPI: dict[str, str] = {
    "decisione": "decisions",
    "errore": "errors",
    "prestazione": "performances",
    "lezione": "reasoning-bank",
    "sessione": "sessions",
}

_BASE = "WORKFLOW-ESTATE/02-AUTOMAZIONI-E-SCRIPTS"
_SLUG_RE = re.compile(r"[^a-z0-9]+")


@dataclass(slots=True)
class Traccia:
    tipo: str
    titolo: str
    autore: str
    prova: str
    quando: str = ""
    contesto: str = ""
    tags: list[str] = field(default_factory=list)
    id: str = ""

    def __post_init__(self) -> None:
        if not self.quando:
            self.quando = datetime.now().astimezone().isoformat(timespec="seconds")
        if not self.id:
            self.id = f"{self.tipo[:3].upper()}-{self.quando[:10].replace('-', '')}-{_slug(self.titolo)[:32]}"


def _slug(testo: str) -> str:
    return _SLUG_RE.sub("-", testo.lower()).strip("-")


def cartella_per(tipo: str) -> Path:
    if tipo not in TIPI:
        raise ValueError(f"tipo di traccia sconosciuto: {tipo!r}. Ammessi: {', '.join(TIPI)}")
    return repo_root() / _BASE / TIPI[tipo]


def scrivi(tipo: str, titolo: str, *, autore: str, prova: str,
           contesto: str = "", tags: list[str] | None = None) -> Path:
    """Scrive una traccia. Idempotente: stesso tipo+titolo+giorno non duplica.

    Rifiuta autore o prova vuoti. Non e' pignoleria: una traccia anonima non serve a
    nessuno quando in tre lavorano in parallelo, e una senza prova e' un'opinione.
    """
    if not autore.strip():
        raise ValueError("serve un autore: una traccia anonima non e' verificabile")
    if not prova.strip():
        raise ValueError("serve una prova: senza evidenza e' solo una parola")

    t = Traccia(tipo=tipo, titolo=titolo.strip(), autore=autore.strip(),
                prova=prova.strip(), contesto=contesto.strip(), tags=tags or [])
    d = cartella_per(tipo)
    d.mkdir(parents=True, exist_ok=True)
    percorso = d / f"{t.id}.json"
    if percorso.exists():          # idempotenza: gia' registrata oggi
        return percorso
    percorso.write_text(json.dumps(asdict(t), indent=2, ensure_ascii=False), encoding="utf-8")
    return percorso


def leggi(tipo: str) -> list[Traccia]:
    d = cartella_per(tipo)
    if not d.exists():
        return []
    out: list[Traccia] = []
    for f in sorted(d.glob("*.json")):
        try:
            out.append(Traccia(**json.loads(f.read_text(encoding="utf-8"))))
        except (json.JSONDecodeError, TypeError, OSError):
            continue          # un file corrotto non deve rendere illeggibili gli altri
    return out


def cerca(testo: str, *, tipo: str | None = None) -> list[Traccia]:
    """Cerca fra le tracce. E' la funzione che risponde alle domande del Piano 5:
    'l'ho gia' deciso?', 'ho gia' sbagliato cosi'?'."""
    ago = testo.lower().strip()
    tipi = [tipo] if tipo else list(TIPI)
    risultati: list[Traccia] = []
    for tp in tipi:
        for t in leggi(tp):
            testo_completo = f"{t.titolo} {t.contesto} {t.prova} {' '.join(t.tags)}".lower()
            if ago in testo_completo:
                risultati.append(t)
    return sorted(risultati, key=lambda x: x.quando, reverse=True)


def conta() -> dict[str, int]:
    return {tp: len(leggi(tp)) for tp in TIPI}


# ------------------------------------------------------------------ CLI

def _cmd_scrivi(a) -> int:
    try:
        p = scrivi(a.tipo, a.titolo, autore=a.autore, prova=a.prova,
                   contesto=a.contesto or "", tags=(a.tags or "").split(",") if a.tags else [])
    except ValueError as e:
        print(f"RIFIUTATA: {e}")
        return 1
    print(f"traccia scritta: {p.relative_to(repo_root())}")
    return 0


def _cmd_elenco(a) -> int:
    tipi = [a.tipo] if a.tipo else list(TIPI)
    totale = 0
    for tp in tipi:
        tracce = leggi(tp)
        totale += len(tracce)
        print(f"\n{tp.upper()} ({TIPI[tp]}) — {len(tracce)}")
        for t in tracce[-a.limite:]:
            print(f"  {t.quando[:16]}  {t.autore:8}  {t.titolo}")
    print(f"\ntotale: {totale}")
    return 0


def _cmd_cerca(a) -> int:
    ris = cerca(a.testo, tipo=a.tipo)
    if not ris:
        print(f"nessuna traccia contiene {a.testo!r}")
        return 0
    for t in ris[:a.limite]:
        print(f"[{t.tipo}] {t.quando[:16]}  {t.autore}")
        print(f"  {t.titolo}")
        print(f"  prova: {t.prova[:120]}")
    return 0


def _cmd_stato(a) -> int:
    c = conta()
    print("TRACCE REGISTRATE")
    for tp, n in c.items():
        stato = "OK " if n else "-- "
        print(f"  {stato} {tp:12} {TIPI[tp]:16} {n}")
    tot = sum(c.values())
    print(f"\ntotale: {tot}")
    if tot == 0:
        print("nessuna traccia: il ciclo non ha ancora girato.")
    return 0


def register(sub) -> None:
    p = sub.add_parser("trace", help="le 5 tracce del lavoro (decisioni, errori, prestazioni, lezioni, sessioni)")
    s = p.add_subparsers(dest="trace_cmd", required=True)

    q = s.add_parser("scrivi", help="registra una traccia")
    q.add_argument("tipo", choices=list(TIPI))
    q.add_argument("titolo")
    q.add_argument("--autore", required=True)
    q.add_argument("--prova", required=True, help="l'evidenza: senza, viene rifiutata")
    q.add_argument("--contesto", default="")
    q.add_argument("--tags", default="")
    q.set_defaults(fn=_cmd_scrivi)

    q = s.add_parser("elenco", help="elenca le tracce")
    q.add_argument("--tipo", choices=list(TIPI), default=None)
    q.add_argument("--limite", type=int, default=10)
    q.set_defaults(fn=_cmd_elenco)

    q = s.add_parser("cerca", help="cerca fra le tracce (l'ho gia' deciso? ho gia' sbagliato cosi'?)")
    q.add_argument("testo")
    q.add_argument("--tipo", choices=list(TIPI), default=None)
    q.add_argument("--limite", type=int, default=5)
    q.set_defaults(fn=_cmd_cerca)

    q = s.add_parser("stato", help="quante tracce ci sono per tipo")
    q.set_defaults(fn=_cmd_stato)

    def _dispatch(a):
        return a.fn(a)
    p.set_defaults(fn=_dispatch)
