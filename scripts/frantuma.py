# -*- coding: utf-8 -*-
"""
frantuma.py -- spacca una task grande in micro-task ufficiali, senza collisioni.

Il problema che risolve
------------------------
Max ha chiesto una funzione per me stesso (Emperator): prendere una task grande
(es. TASK-LANCI-BUILD-W3, 139-187 ore-uomo) e spaccarla in micro-task che piu'
chat/sessioni possano eseguire IN PARALLELO, ognuna nella sua chat, senza
pestarsi i piedi.

Due rischi distinti, due protezioni distinte:
  1. Due sessioni coniano la stessa micro-task nello stesso momento
     -> stesso schema anti-collisione di scripts/adr.py e scripts/checkpoint.py
        (numero per-padre, O_CREAT|O_EXCL: chi arriva secondo prende il numero
        dopo, non sovrascrive).
  2. Due micro-task DIVERSE, eseguite in due chat diverse, toccano lo stesso
     file -> collisione di merge silenziosa, il vero motivo per cui questa
     funzione deve esistere. Ogni micro-task dichiara il suo `scope` (i
     percorsi che tocca) e `verifica` segnala qualunque sovrapposizione PRIMA
     che qualcuno esegua, non dopo.

La forma dell'output (schema "Onde ad albero", scelta da Max il 2026-09-08) e'
calcolata da `report()`, mai scritta a mano: stessa filosofia del battito
(verifica_recap.py) -- il contenuto e' mio, la forma la garantisce il codice.

Uso:
    python scripts/frantuma.py conia --padre TASK-LANCI-BUILD-W3 \
        --slug s0-incasso --titolo "Giorno zero: catena dell'incasso" \
        --onda 1 --deps "" --scope "path/a,path/b"
    python scripts/frantuma.py verifica --padre TASK-LANCI-BUILD-W3
    python scripts/frantuma.py report   --padre TASK-LANCI-BUILD-W3
    python scripts/frantuma.py chiudi   --padre TASK-LANCI-BUILD-W3 --codice MT-01
"""
from __future__ import annotations

import argparse
import io
import os
import re
import sys
from datetime import datetime

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARTELLA_BASE = os.path.join(RADICE, "company", "Memory", "tasks", "micro")

_RE_MT = re.compile(r"^MT-(\d{2,4})-(.*)$")
_RE_ONDA = re.compile(r"^\s*-\s*\*\*Onda:\*\*\s*(\d+)", re.MULTILINE)
_RE_STATO = re.compile(r"^\s*-\s*\*\*Stato:\*\*\s*(\S+)", re.MULTILINE)
_RE_TITOLO = re.compile(r"^#\s*MT-\d+\s*[—-]\s*(.+)$", re.MULTILINE)
_RE_DEPS = re.compile(r"^\s*-\s*\*\*Dipende da:\*\*\s*(.*)$", re.MULTILINE)
_RE_SCOPE_BLOCK = re.compile(
    r"\*\*Scope.*?:\*\*\s*\n((?:\s*-\s*.+\n?)*)", re.MULTILINE)


def _cartella(padre: str) -> str:
    return os.path.join(CARTELLA_BASE, padre)


def _numeri_su_disco(padre: str) -> dict[int, list[str]]:
    trovati: dict[int, list[str]] = {}
    cart = _cartella(padre)
    if not os.path.isdir(cart):
        return trovati
    for nome in sorted(os.listdir(cart)):
        if not nome.endswith(".md"):
            continue
        m = _RE_MT.match(nome[:-3])
        if m:
            trovati.setdefault(int(m.group(1)), []).append(nome)
    return trovati


def prossimo_numero(padre: str) -> int:
    disco = _numeri_su_disco(padre)
    return (max(disco) + 1) if disco else 1


def _parse_deps(raw: str) -> list[str]:
    raw = (raw or "").strip()
    if not raw or raw in ("-", "—"):
        return []
    return [d.strip() for d in raw.split(",") if d.strip()]


def _parse_scope(raw: str) -> list[str]:
    return [p.strip() for p in (raw or "").split(",") if p.strip()]


def conia(padre: str, slug: str, titolo: str, onda: int,
          deps: str = "", scope: str = "", stato: str = "APERTA") -> str:
    """Occupa il prossimo numero MT-NN dentro la cartella del padre, atomico."""
    if not re.match(r"^[a-z0-9]+(-[a-z0-9]+)*$", slug):
        raise SystemExit("slug non valido: minuscole, cifre e trattini")
    if not re.match(r"^[A-Za-z0-9_-]+$", padre):
        raise SystemExit("padre non valido: usa il codice della task grande "
                          "(es. TASK-LANCI-BUILD-W3), senza spazi")
    cart = _cartella(padre)
    os.makedirs(cart, exist_ok=True)
    oggi = datetime.now().strftime("%Y-%m-%d")
    deps_lista = _parse_deps(deps)
    scope_lista = _parse_scope(scope)

    numero = prossimo_numero(padre)
    for _ in range(200):
        nome = "MT-%02d-%s.md" % (numero, slug)
        percorso = os.path.join(cart, nome)
        scope_righe = "\n".join("  - %s" % p for p in scope_lista) or "  - _da dichiarare_"
        corpo = (
            "# MT-%02d — %s\n\n"
            "- **Padre:** %s\n"
            "- **Onda:** %d\n"
            "- **Stato:** %s\n"
            "- **Data:** %s\n"
            "- **Dipende da:** %s\n"
            "- **Scope (percorsi che tocca — controllo di sovrapposizione):**\n"
            "%s\n\n"
            "## Cosa fa\n\n_da scrivere nello stesso turno in cui la micro-task e' coniata_\n\n"
            "## Gate di chiusura\n\n\n"
            "## Output\n\n"
        ) % (numero, titolo, padre, onda, stato, oggi,
             (", ".join(deps_lista) if deps_lista else "—"),
             scope_righe)
        try:
            fd = os.open(percorso, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        except FileExistsError:
            numero += 1
            continue
        with io.open(fd, "w", encoding="utf-8", newline="\n") as f:
            f.write(corpo)
        codice = "MT-%02d" % numero
        print("")
        print("  MICRO-TASK CONIATA (numero occupato sul disco)")
        print("")
        print("     CODICE:  %s" % codice)
        print("     Padre:   %s" % padre)
        print("     Onda:    %d" % onda)
        print("     Titolo:  %s" % titolo)
        print("     File:    company/Memory/tasks/micro/%s/%s" % (padre, nome))
        print("")
        return codice
    raise RuntimeError("Nessun numero MT libero nei 200 successivi: cartella rotta.")


def leggi_tutte(padre: str) -> list[dict]:
    cart = _cartella(padre)
    if not os.path.isdir(cart):
        return []
    righe = []
    for nome in sorted(os.listdir(cart)):
        if not nome.endswith(".md"):
            continue
        m = _RE_MT.match(nome[:-3])
        if not m:
            continue
        percorso = os.path.join(cart, nome)
        testo = io.open(percorso, encoding="utf-8").read()
        titolo_m = _RE_TITOLO.search(testo)
        onda_m = _RE_ONDA.search(testo)
        stato_m = _RE_STATO.search(testo)
        deps_m = _RE_DEPS.search(testo)
        scope_m = _RE_SCOPE_BLOCK.search(testo)
        scope_paths = []
        if scope_m:
            for riga in scope_m.group(1).splitlines():
                riga = riga.strip().lstrip("-").strip()
                if riga and riga != "_da dichiarare_":
                    scope_paths.append(riga)
        righe.append({
            "codice": "MT-%02d" % int(m.group(1)),
            "numero": int(m.group(1)),
            "slug": m.group(2),
            "file": nome,
            "titolo": titolo_m.group(1).strip() if titolo_m else m.group(2),
            "onda": int(onda_m.group(1)) if onda_m else 0,
            "stato": stato_m.group(1).strip() if stato_m else "APERTA",
            "deps": _parse_deps(deps_m.group(1)) if deps_m else [],
            "scope": scope_paths,
        })
    return sorted(righe, key=lambda r: r["numero"])


def _dipende_transitivamente(a: dict, b: dict, per_codice: dict[str, dict],
                              visti: set[str] | None = None) -> bool:
    """True se a dipende da b, direttamente o attraverso una catena di deps.

    Due micro-task in sequenza (una aspetta l'altra) toccano legittimamente lo
    stesso percorso: non e' una collisione, e' la costruzione che avanza sullo
    stesso pezzo. La collisione vera esiste solo fra micro-task che NESSUNA
    catena di dipendenze mette in ordine, cioe' quelle che potrebbero davvero
    girare in due chat nello stesso momento.
    """
    if visti is None:
        visti = set()
    if a["codice"] in visti:
        return False
    visti.add(a["codice"])
    for dep in a["deps"]:
        if dep == b["codice"]:
            return True
        altra = per_codice.get(dep)
        if altra and _dipende_transitivamente(altra, b, per_codice, visti):
            return True
    return False


def sovrapposizioni(padre: str) -> list[tuple[str, str, str]]:
    """Coppie di micro-task SENZA relazione di dipendenza fra loro che
    dichiarano lo stesso percorso, o un percorso che e' prefisso dell'altro
    (una cartella dentro l'altra). Solo queste possono davvero girare in
    parallelo in due chat e pestarsi i piedi."""
    tutte = leggi_tutte(padre)
    per_codice = {m["codice"]: m for m in tutte}
    trovate = []
    for i, a in enumerate(tutte):
        for b in tutte[i + 1:]:
            if (_dipende_transitivamente(a, b, per_codice)
                    or _dipende_transitivamente(b, a, per_codice)):
                continue  # in sequenza: stesso percorso e' normale, non un rischio
            for pa in a["scope"]:
                for pb in b["scope"]:
                    if pa == pb or pa.startswith(pb + "/") or pb.startswith(pa + "/"):
                        trovate.append((a["codice"], b["codice"], pa if pa == pb else "%s ~ %s" % (pa, pb)))
    return trovate


def _disponibile(mt: dict, per_codice: dict[str, dict]) -> bool:
    if mt["stato"] == "CHIUSA":
        return False  # gia' fatta, non e' "disponibile da fare"
    for dep in mt["deps"]:
        altra = per_codice.get(dep)
        if altra is None or altra["stato"] != "CHIUSA":
            return False
    return True


def report(padre: str) -> str:
    """Schema 'Onde ad albero' -- scelto da Max il 2026-09-08. Calcolato dai
    file reali, mai scritto a mano: la forma la garantisce il codice."""
    tutte = leggi_tutte(padre)
    if not tutte:
        return "Nessuna micro-task coniata per %s. Usa `frantuma.py conia`." % padre

    per_codice = {m["codice"]: m for m in tutte}
    per_onda: dict[int, list[dict]] = {}
    for m in tutte:
        per_onda.setdefault(m["onda"], []).append(m)

    righe = []
    righe.append("SCOMPOSIZIONE UFFICIALE — %s" % padre)
    righe.append("=" * 50)
    righe.append("%d micro-task, %d onde" % (len(tutte), len(per_onda)))
    righe.append("")

    n_disponibili = 0
    n_chiuse = 0
    for onda in sorted(per_onda):
        gruppo = per_onda[onda]
        tutte_chiuse = all(m["stato"] == "CHIUSA" for m in gruppo)
        intestazione = ("ONDA %d — CHIUSA" % onda) if tutte_chiuse else ("ONDA %d" % onda)
        righe.append(intestazione)
        for m in gruppo:
            if m["stato"] == "CHIUSA":
                simbolo, tag = "[X]", ""
                n_chiuse += 1
            elif _disponibile(m, per_codice):
                simbolo, tag = "[ ]", "  <- via libera ORA"
                n_disponibili += 1
            else:
                mancano = [d for d in m["deps"] if per_codice.get(d, {}).get("stato") != "CHIUSA"]
                simbolo, tag = "[.]", ("  <- aspetta %s" % ", ".join(mancano) if mancano else "")
            righe.append("   %s %s · %s%s" % (simbolo, m["codice"], m["titolo"], tag))
        righe.append("")

    sovr = sovrapposizioni(padre)
    righe.append("-" * 50)
    righe.append("%d disponibili ORA · %d chiuse · %d totali · %d collisioni di scope"
                  % (n_disponibili, n_chiuse, len(tutte), len(sovr)))
    if sovr:
        righe.append("")
        righe.append("ATTENZIONE — scope sovrapposto (non eseguire in parallelo):")
        for a, b, path in sovr:
            righe.append("   %s <-> %s su %s" % (a, b, path))
    return "\n".join(righe)


def chiudi(padre: str, codice: str) -> None:
    m = re.match(r"^MT-(\d{2,4})$", codice)
    if not m:
        raise SystemExit("codice non valido, usa MT-NN")
    numero = int(m.group(1))
    cart = _cartella(padre)
    trovato = None
    for nome in os.listdir(cart) if os.path.isdir(cart) else []:
        if nome.startswith("MT-%02d-" % numero) and nome.endswith(".md"):
            trovato = os.path.join(cart, nome)
            break
    if not trovato:
        raise SystemExit("%s non trovata sotto %s" % (codice, padre))
    testo = io.open(trovato, encoding="utf-8").read()
    nuovo = _RE_STATO.sub("- **Stato:** CHIUSA", testo, count=1)
    io.open(trovato, "w", encoding="utf-8", newline="\n").write(nuovo)
    print("%s chiusa." % codice)


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Spacca una task grande in micro-task senza collisioni (/frantuma).")
    sub = ap.add_subparsers(dest="azione", required=True)

    c = sub.add_parser("conia", help="crea una micro-task nuova, numero atomico")
    c.add_argument("--padre", required=True)
    c.add_argument("--slug", required=True)
    c.add_argument("--titolo", required=True)
    c.add_argument("--onda", type=int, required=True)
    c.add_argument("--deps", default="")
    c.add_argument("--scope", default="")
    c.add_argument("--stato", default="APERTA")

    v = sub.add_parser("verifica", help="segnala sovrapposizioni di scope, esce 1 se ce ne sono")
    v.add_argument("--padre", required=True)

    r = sub.add_parser("report", help="stampa lo schema Onde ad albero")
    r.add_argument("--padre", required=True)

    ch = sub.add_parser("chiudi", help="marca una micro-task CHIUSA")
    ch.add_argument("--padre", required=True)
    ch.add_argument("--codice", required=True)

    a = ap.parse_args()
    if a.azione == "conia":
        conia(a.padre, a.slug, a.titolo, a.onda, a.deps, a.scope, a.stato)
        return 0
    if a.azione == "verifica":
        sovr = sovrapposizioni(a.padre)
        if sovr:
            print("SOVRAPPOSIZIONI TROVATE:")
            for x, y, p in sovr:
                print("  %s <-> %s su %s" % (x, y, p))
            return 1
        print("Nessuna sovrapposizione di scope. %d micro-task verificate."
              % len(leggi_tutte(a.padre)))
        return 0
    if a.azione == "report":
        print(report(a.padre))
        return 0
    if a.azione == "chiudi":
        chiudi(a.padre, a.codice)
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
