# -*- coding: utf-8 -*-
"""Il comando `lancio`. Scaglione S2a: crea, stato, elenco, valida.

    python -m scripts.lancio crea prova-vuota --prodotto "Prova"
    python -m scripts.lancio stato prova-vuota
    python -m scripts.lancio elenco
    python -m scripts.lancio valida prova-vuota

CODICI D'USCITA, gli stessi di tutto l'Impero:
    0  fatto
    1  c'e' qualcosa da sistemare (non e' un errore del programma)
    2  parametri sbagliati
    3  errore di sistema

`avanza`, `firma`, `blocchi`, `costi` NON stanno qui: sono S2b e S5, e il
comando lo dice invece di fingere di non conoscerli.
"""
from __future__ import annotations

import argparse
import io
import os
import sys

if __package__ in (None, ""):
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from scripts.stato_lancio import ErroreLancio, Lancio, elenca  # noqa: E402
else:
    from .stato_lancio import ErroreLancio, Lancio, elenca

DA_FARE = {
    "avanza": "scaglione S2b, micro-task MT-3XWC",
    "firma": "scaglione S3",
    "blocchi": "scaglione S5, micro-task MT-RGZ6",
    "costi": "scaglione S5, micro-task MT-RGZ6",
    "sospendi": "scaglione S2b",
    "riprendi": "scaglione S2b",
    "via-libera": "scaglione S3",
    "abbandona": "scaglione S2b",
}


def _cmd_crea(a) -> int:
    lancio = Lancio(a.slug)
    dati = lancio.crea(a.prodotto)
    print()
    print("  LANCIO CREATO")
    print()
    print("     id:       %s" % dati["lancio_id"])
    print("     prodotto: %s" % dati["prodotto"])
    print("     stato:    %s" % dati["stato"])
    print("     cartella: %s" % lancio.dir)
    print()
    print("  Prossimo passo: compilare gli artefatti e controllarli con")
    print("     python -m scripts.lancio valida %s" % a.slug)
    print()
    return 0


def _cmd_stato(a) -> int:
    lancio = Lancio(a.slug)
    s = lancio.stato()
    presenti = lancio.artefatti_presenti()
    print()
    print("  %s  [%s]" % (s["lancio_id"], s["stato"]))
    print("  prodotto: %s" % s.get("prodotto", "?"))
    print("  fermo da: %d giorni" % lancio.fermo_da_giorni())
    print()
    print("  artefatti presenti: %d" % len(presenti))
    for nome in sorted(presenti):
        problemi = lancio.valida_artefatto(nome)
        print("     %-20s %s" % (nome, "valido" if not problemi
                                 else "%d problemi" % len(problemi)))
    proposte = [n for n in os.listdir(lancio.dir) if n.endswith(".PROPOSTA.json")]
    if proposte:
        print()
        print("  proposte in attesa di firma umana: %s" % ", ".join(sorted(proposte)))
    print()
    print("  storia:")
    for p in s.get("storia", [])[-6:]:
        print("     %s  %s -> %s  (%s)" % (p["il"], p["da"] or "-", p["a"], p["perche"]))
    print()
    return 0


def _cmd_elenco(_a) -> int:
    lanci = elenca()
    if not lanci:
        print("  Nessun lancio. Creane uno con:  lancio crea <id> --prodotto \"...\"")
        return 0
    print()
    print("  %-24s %-16s %8s  %s" % ("LANCIO", "STATO", "FERMO DA", "ARTEFATTI"))
    for lancio in lanci:
        s = lancio.stato()
        problemi = lancio.valida_tutti()
        non_validi = sum(1 for v in problemi.values() if v)
        nota = "%d" % len(problemi)
        if non_validi:
            nota += " (%d non validi)" % non_validi
        print("  %-24s %-16s %5d gg  %s"
              % (s["lancio_id"], s["stato"], lancio.fermo_da_giorni(), nota))
    print()
    return 0


def _cmd_valida(a) -> int:
    lancio = Lancio(a.slug)
    lancio.stato()  # esiste?
    problemi = lancio.valida_tutti()
    if not problemi:
        print("  Nessun artefatto presente in %s" % lancio.dir)
        return 1
    print()
    guasti = 0
    for nome in sorted(problemi):
        elenco_problemi = problemi[nome]
        if not elenco_problemi:
            print("  ok   %-22s valido" % nome)
            continue
        guasti += 1
        print("  NO   %-22s %d problemi:" % (nome, len(elenco_problemi)))
        for riga in elenco_problemi[:8]:
            print("         %s" % riga[:120])
        if len(elenco_problemi) > 8:
            print("         ... e altri %d" % (len(elenco_problemi) - 8))
    print()
    print("  artefatti: %d   non validi: %d" % (len(problemi), guasti))
    if guasti:
        lancio.verbale("validazione-fallita",
                       {"non_validi": {k: v for k, v in problemi.items() if v}})
    return 1 if guasti else 0


def _stdout_utf8():
    """Su Windows stdout e' cp1252 e i caratteri accentati lo fanno morire.

    Si chiama SOLO da riga di comando, mai da dentro `main()`: avvolgere lo
    stdout di chi ci chiama gli chiude il buffer sotto i piedi, e con pytest
    significa far fallire la raccolta dell'output di tutta la sessione invece
    del proprio test. Trovato al primo giro di prove, il 2026-09-10."""
    if hasattr(sys.stdout, "buffer"):
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8",
                                      errors="replace", line_buffering=True)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="lancio", description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="azione", required=True)

    c = sub.add_parser("crea", help="crea un lancio nuovo in stato IDEA")
    c.add_argument("slug")
    c.add_argument("--prodotto", required=True)

    s = sub.add_parser("stato", help="stato, artefatti e storia di un lancio")
    s.add_argument("slug")

    sub.add_parser("elenco", help="una riga per lancio, con da quanti giorni e' fermo")

    v = sub.add_parser("valida", help="ricalcola la validita' di ogni artefatto")
    v.add_argument("slug")

    for nome, dove in DA_FARE.items():
        # `nargs=argparse.REMAINDER` di proposito: chi digita
        # `lancio avanza manuale-claude-code` deve leggere che il pezzo non
        # c'e' ancora, non un errore di argomenti che non gli dice niente.
        p_futuro = sub.add_parser(nome, help="non ancora costruito (%s)" % dove)
        p_futuro.add_argument("resto", nargs=argparse.REMAINDER)

    a = ap.parse_args(argv)

    if a.azione in DA_FARE:
        print()
        print("  `lancio %s` non e' ancora costruito: %s." % (a.azione, DA_FARE[a.azione]))
        print("  Non e' un errore: e' un pezzo che non esiste, e preferisco dirlo")
        print("  piuttosto che far finta di eseguirlo.")
        print()
        return 2

    azioni = {"crea": _cmd_crea, "stato": _cmd_stato,
              "elenco": _cmd_elenco, "valida": _cmd_valida}
    try:
        return azioni[a.azione](a)
    except ErroreLancio as e:
        print()
        print("  %s" % e)
        print()
        return 2
    except Exception as e:  # noqa: BLE001
        print()
        print("  Errore di sistema: %s: %s" % (type(e).__name__, e))
        print()
        return 3


if __name__ == "__main__":
    _stdout_utf8()
    sys.exit(main())
