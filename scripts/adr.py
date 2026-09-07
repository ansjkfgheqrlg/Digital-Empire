# -*- coding: utf-8 -*-
"""
ADR - il numero di una decisione si CONIA, non si sceglie.

Il problema che risolve
-----------------------
Il numero di un ADR e' progressivo per forza: ADR-025 viene dopo ADR-024, e non
si puo' sorteggiare come un checkpoint, perche' l'ordine e' l'informazione.
Ma "progressivo" e "scelto a mano" insieme sono una collisione garantita: due
sessioni che non si vedono guardano la cartella, leggono lo stesso ultimo
numero, e scrivono tutt'e due il successivo.

E' successo davvero, tre volte di fila, sullo stesso documento:

  2026-09-05  il piano LANCI prenota ADR-022  -> occupato da un'altra sessione
  2026-09-06  il piano LANCI ripiega su ADR-023 -> occupato da "fabbrica siti"
  2026-09-07  ADR-024 occupato da "canone v2"; il piano punta ancora al 023

Un numero prenotato dentro la prosa di un documento non e' prenotato: e' un
desiderio. La cartella `company/Memory/decisions/` porta gia' la cicatrice di
due numeri usati due volte (ADR-012 e ADR-016, due file ciascuno).

Cosa fa
-------
La prenotazione avviene creando il FILE, subito, in modo atomico (O_EXCL): il
numero e' occupato nell'istante in cui nasce, e una seconda sessione che tenta
lo stesso numero nello stesso momento fallisce invece di sovrascrivere.

Il numero successivo si calcola su DUE fonti, non una:
  - i file presenti adesso in company/Memory/decisions/
  - ogni nome di file mai aggiunto in tutta la storia git, su ogni ramo
La seconda serve perche' un numero puo' essere stato usato in una sessione
parallela e poi rinominato o cancellato: la cartella di adesso non basta.
E' la stessa legge anti-collisione di scripts/checkpoint.py (B-009).

Uso:
    python scripts/adr.py prossimo
    python scripts/adr.py verifica
    python scripts/adr.py conia --slug ecosistema-lanci --titolo "Nasce LANCI" \
                                --stato PROPOSTA --ordinato-da "Gael"

`conia` stampa il numero e crea il file. Il corpo si scrive dopo, nello stesso
turno: un ADR coniato e non scritto e' un debito silenzioso, esattamente come
un checkpoint vuoto (lezione CP-20260907-96DY).
"""
from __future__ import annotations

import argparse
import io
import os
import re
import subprocess
import sys
from datetime import datetime

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARTELLA = os.path.join(RADICE, "company", "Memory", "decisions")
SOTTOCARTELLA_GIT = "company/Memory/decisions"

_RE_ADR = re.compile(r"^ADR-(\d{3,4})(?:-(.*))?$")


def _numeri_su_disco() -> dict[int, list[str]]:
    """Numero -> nomi di file che lo usano. Piu' di uno significa duplicato."""
    trovati: dict[int, list[str]] = {}
    if not os.path.isdir(CARTELLA):
        return trovati
    for nome in sorted(os.listdir(CARTELLA)):
        if not nome.endswith(".md"):
            continue
        m = _RE_ADR.match(nome[:-3])
        if m:
            trovati.setdefault(int(m.group(1)), []).append(nome)
    return trovati


def _numeri_nella_storia() -> set[int]:
    """Ogni numero ADR mai aggiunto al repo, su qualunque ramo.

    Un numero puo' essere nato in una sessione parallela e poi essere stato
    rinominato: sparisce dalla cartella e resta occupato nella storia. Senza
    questo controllo lo si riassegnerebbe, che e' il modo piu' silenzioso di
    perdere una decisione.
    """
    numeri: set[int] = set()
    try:
        out = subprocess.run(
            ["git", "log", "--all", "--diff-filter=A", "--name-only",
             "--pretty=format:", "--", SOTTOCARTELLA_GIT],
            cwd=RADICE, capture_output=True, text=True, timeout=60)
        for riga in out.stdout.splitlines():
            riga = riga.strip()
            if not riga.endswith(".md"):
                continue
            m = _RE_ADR.match(os.path.basename(riga)[:-3])
            if m:
                numeri.add(int(m.group(1)))
    except Exception:
        pass  # senza git si lavora lo stesso, con meno memoria
    return numeri


def occupati() -> set[int]:
    return set(_numeri_su_disco()) | _numeri_nella_storia()


def prossimo_numero() -> int:
    usati = occupati()
    return (max(usati) + 1) if usati else 1


def verifica() -> int:
    """Stampa lo stato del registro. Esce 1 se ci sono duplicati."""
    disco = _numeri_su_disco()
    storia = _numeri_nella_storia()
    duplicati = {n: f for n, f in disco.items() if len(f) > 1}
    solo_storia = sorted(storia - set(disco))

    print("ADR sul disco : %d file, numeri da %d a %d"
          % (sum(len(v) for v in disco.values()),
             min(disco) if disco else 0, max(disco) if disco else 0))
    if solo_storia:
        print("Numeri occupati SOLO nella storia git (rinominati o cancellati): %s"
              % ", ".join("ADR-%03d" % n for n in solo_storia))
    buchi = [n for n in range(1, (max(disco) if disco else 0)) if n not in disco]
    if buchi:
        print("Buchi (numeri mai usati): %s"
              % ", ".join("ADR-%03d" % n for n in buchi))
    print("Prossimo numero libero: ADR-%03d" % prossimo_numero())

    if duplicati:
        print("")
        print("DUPLICATI - due decisioni diverse con lo stesso numero:")
        for n in sorted(duplicati):
            print("  ADR-%03d:" % n)
            for f in duplicati[n]:
                print("      %s" % f)
        print("")
        print("Non si rinumera in silenzio: rinumerare un ADR gia' citato altrove")
        print("rompe ogni puntatore che lo nomina. Va deciso da chi lo ha firmato.")
        return 1
    return 0


def conia(slug: str, titolo: str, stato: str = "PROPOSTA",
          ordinato_da: str = "") -> str:
    """Occupa il prossimo numero creando il file in modo atomico.

    O_EXCL e' il punto di tutta la funzione: se due sessioni arrivano insieme,
    una vince e l'altra prende FileExistsError e riprova col numero dopo,
    invece di sovrascrivere una decisione che non ha mai letto.
    """
    if not re.match(r"^[a-z0-9]+(-[a-z0-9]+)*$", slug):
        raise SystemExit("slug non valido: minuscole, cifre e trattini "
                         "(esempio: ecosistema-lanci)")
    os.makedirs(CARTELLA, exist_ok=True)
    oggi = datetime.now().strftime("%Y-%m-%d")

    numero = prossimo_numero()
    for _ in range(50):
        nome = "ADR-%03d-%s.md" % (numero, slug)
        percorso = os.path.join(CARTELLA, nome)
        corpo = (
            "# ADR-%03d - %s\n\n"
            "- **Stato:** %s\n"
            "- **Data:** %s\n"
            "%s"
            "\n## Contesto\n\n_da scrivere nello stesso turno in cui il numero e' stato coniato_\n"
            "\n## Decisione\n\n\n## Conseguenze\n\n"
        ) % (numero, titolo, stato, oggi,
             ("- **Ordinato da:** %s\n" % ordinato_da) if ordinato_da else "")
        try:
            fd = os.open(percorso, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        except FileExistsError:
            numero += 1
            continue
        with io.open(fd, "w", encoding="utf-8", newline="\n") as f:
            f.write(corpo)
        codice = "ADR-%03d" % numero
        print("")
        print("  ADR CONIATO (numero occupato sul disco, non solo in un documento)")
        print("")
        print("     NUMERO:  %s" % codice)
        print("     Titolo:  %s" % titolo)
        print("     Stato:   %s" % stato)
        print("     File:    company/Memory/decisions/%s" % nome)
        print("")
        print("  Il file esiste gia': nessuna altra sessione puo' prendere questo numero.")
        print("  Scrivine il corpo ADESSO: un ADR coniato e vuoto e' un debito silenzioso.")
        print("")
        return codice
    raise RuntimeError("Nessun numero ADR libero nei 50 successivi: cartella rotta.")


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Conia numeri ADR senza collisioni (vedi B-009).")
    sub = ap.add_subparsers(dest="azione", required=True)

    sub.add_parser("prossimo", help="stampa il prossimo numero libero, senza prenderlo")
    sub.add_parser("verifica", help="duplicati, buchi e numeri occupati solo in git")

    c = sub.add_parser("conia", help="occupa il prossimo numero e crea il file")
    c.add_argument("--slug", required=True, help="es. ecosistema-lanci")
    c.add_argument("--titolo", required=True)
    c.add_argument("--stato", default="PROPOSTA",
                   help="PROPOSTA (default) | ATTIVA | SUPERATA")
    c.add_argument("--ordinato-da", default="", dest="ordinato_da")

    a = ap.parse_args()
    if a.azione == "prossimo":
        print("ADR-%03d" % prossimo_numero())
        return 0
    if a.azione == "verifica":
        return verifica()
    conia(a.slug, a.titolo, a.stato, a.ordinato_da)
    return 0


if __name__ == "__main__":
    sys.exit(main())
