# -*- coding: utf-8 -*-
"""Il comando `lancio`. S2a: crea, stato, elenco, valida. S2b: avanza e i comandi umani.

    python -m scripts.lancio crea prova-vuota --prodotto "Prova" [--con-esempio]
    python -m scripts.lancio stato prova-vuota
    python -m scripts.lancio elenco
    python -m scripts.lancio valida prova-vuota
    python -m scripts.lancio avanza prova-vuota [--solo-gate GATE-PUB-1] [--a-vuoto]
    python -m scripts.lancio firma prova-vuota --prezzo 47 --data 01/12/2026 [--chi NOME] [--ruolo vendita]
    python -m scripts.lancio via-libera prova-vuota [--chi NOME]
    python -m scripts.lancio sospendi prova-vuota --motivo "..." --revisione 01/12/2026
    python -m scripts.lancio riprendi prova-vuota
    python -m scripts.lancio abbandona prova-vuota --motivo "..."

CODICI D'USCITA, gli stessi di tutto l'Impero:
    0  fatto
    1  c'e' qualcosa da sistemare (non e' un errore del programma)
    2  parametri sbagliati
    3  errore di sistema

`blocchi` e `costi` NON stanno qui: sono S5 (MT-RGZ6), e il comando lo dice
invece di fingere di non conoscerli.
"""
from __future__ import annotations

import argparse
import io
import os
import sys

if __package__ in (None, ""):
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from scripts.stato_lancio import (ECOSISTEMA, ErroreLancio, Lancio,  # noqa: E402
                                      avanza, data_italiana, elenca)
else:
    from .stato_lancio import ECOSISTEMA, ErroreLancio, Lancio, avanza, data_italiana, elenca

DA_FARE = {
    "blocchi": "scaglione S5, micro-task MT-RGZ6",
    "costi": "scaglione S5, micro-task MT-RGZ6",
}

ESEMPIO = os.path.join(ECOSISTEMA, "05-TEMPLATES-E-KIT", "esempio")


def _cmd_crea(a) -> int:
    lancio = Lancio(a.slug)
    dati = lancio.crea(a.prodotto)
    copiati = []
    if getattr(a, "con_esempio", False):
        if os.path.isdir(ESEMPIO):
            copiati = lancio.copia_esempio(ESEMPIO)
        else:
            print()
            print("  La cartella d'esempio non c'e' (%s): creo il lancio vuoto." % ESEMPIO)
    print()
    print("  LANCIO CREATO")
    print()
    print("     id:       %s" % dati["lancio_id"])
    print("     prodotto: %s" % dati["prodotto"])
    print("     stato:    %s" % dati["stato"])
    print("     cartella: %s" % lancio.dir)
    if copiati:
        print("     esempio:  %d file copiati (%s)" % (len(copiati), ", ".join(copiati)))
    print()
    print("  Prossimo passo: compilare gli artefatti e controllarli con")
    print("     python -m scripts.lancio valida %s" % a.slug)
    print("  poi farlo avanzare con")
    print("     python -m scripts.lancio avanza %s" % a.slug)
    print()
    return 0


def _cmd_stato(a) -> int:
    lancio = Lancio(a.slug)
    s = lancio._stato_completo()
    presenti = lancio.artefatti_presenti()
    print()
    print("  %s  [%s]" % (s["lancio_id"], s["stato"]))
    print("  prodotto: %s" % s.get("prodotto", "?"))
    print("  fermo da: %d giorni" % lancio.fermo_da_giorni())
    if s.get("bloccato_da"):
        b = s["bloccato_da"]
        print("  bloccato da: %s (dal %s)" % (b.get("gate"), str(b.get("dal", "?"))[:10]))
        for p in b.get("problemi", [])[:5]:
            print("     - %s" % str(p)[:120])
    if s.get("sospensione"):
        sp = s["sospensione"]
        print("  SOSPESO dal %s, partenza %s, revisione il %s" % (
            str(sp.get("dal", "?"))[:10], sp.get("stato_di_partenza"),
            str(sp.get("revisione_il", "?"))[:10]))
        print("     motivo:      %s" % sp.get("motivo"))
        print("     per uscirne: %s" % sp.get("come_si_esce"))
    if s.get("punti_umani_aperti"):
        print()
        print("  punti umani aperti:")
        for p in s["punti_umani_aperti"]:
            print("     %-12s da %2d gg  %s" % (p["id"], _giorni_da(p.get("aperto_il")),
                                                 p.get("domanda", "")))
            print("     %-12s        -> %s" % ("", p.get("come_si_esce", "")))
    if s.get("da_rivedere"):
        print("  da rivedere (ingressi cambiati): %s" % ", ".join(s["da_rivedere"]))
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


def _giorni_da(iso) -> int:
    from datetime import datetime, timezone
    if not iso:
        return 0
    try:
        dt = datetime.fromisoformat(iso)
    except ValueError:
        return 0
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return max(0, (datetime.now(timezone.utc) - dt).days)


def _cmd_avanza(a) -> int:
    print()
    codice = avanza(a.slug, solo_gate=a.solo_gate, a_vuoto=a.a_vuoto)
    print()
    print("  codice: %d  (%s)" % (codice, {0: "avanzato fin dove poteva", 1: "bloccato",
                                          2: "ingresso non valido", 3: "ambiente"}.get(codice, "?")))
    print()
    return codice


def _cmd_sospendi(a) -> int:
    dati = Lancio(a.slug).sospendi(a.motivo, data_italiana(a.revisione))
    print("  %s -> SOSPESO (partenza: %s)" % (a.slug, dati["sospensione"]["stato_di_partenza"]))
    return 0


def _cmd_riprendi(a) -> int:
    dati = Lancio(a.slug).riprendi()
    print("  %s -> %s (ripreso, orologi ripartiti dal valore congelato)" % (a.slug, dati["stato"]))
    return 0


def _cmd_abbandona(a) -> int:
    Lancio(a.slug).abbandona(a.motivo)
    return 0


def _cmd_firma(a) -> int:
    offerta = Lancio(a.slug).firma(a.prezzo, data_italiana(a.data), chi=a.chi,
                                   ruolo=a.ruolo, durata_gg=a.durata)
    f = offerta["firma"]
    print()
    print("  FIRMATO  %s  prezzo %s EUR  apertura %s  chiusura %s" % (
        a.slug, offerta["prezzo"], offerta["data_apertura"], offerta["data_chiusura"]))
    print("     chi: %s   canale: %s   impronta proposta: %s..." % (
        f["chi"], f["canale"], f["proposta_impronta"][:12]))
    print("  Prossimo passo:  python -m scripts.lancio avanza %s" % a.slug)
    print()
    return 0


def _cmd_via_libera(a) -> int:
    ape = Lancio(a.slug).via_libera(chi=a.chi)
    print()
    print("  VIA LIBERA dato da %s (canale comando-utente) il %s" % (
        ape["via_libera"]["chi"], ape["via_libera"]["il"]))
    print("  Prossimo passo:  python -m scripts.lancio avanza %s" % a.slug)
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
    c.add_argument("--con-esempio", action="store_true", dest="con_esempio",
                   help="copia dentro il lancio i file di 05-TEMPLATES-E-KIT/esempio")

    s = sub.add_parser("stato", help="stato, artefatti e storia di un lancio")
    s.add_argument("slug")

    sub.add_parser("elenco", help="una riga per lancio, con da quanti giorni e' fermo")

    v = sub.add_parser("valida", help="ricalcola la validita' di ogni artefatto")
    v.add_argument("slug")

    av = sub.add_parser("avanza", help="fa avanzare il lancio finche' un controllo non lo ferma")
    av.add_argument("slug")
    av.add_argument("--solo-gate", dest="solo_gate", default=None,
                    help="riesegue un solo controllo (es. GATE-PUB-1) dopo una correzione")
    av.add_argument("--a-vuoto", dest="a_vuoto", action="store_true",
                    help="calcola e stampa, non scrive niente")

    so = sub.add_parser("sospendi", help="porta il lancio in SOSPESO e congela gli orologi")
    so.add_argument("slug")
    so.add_argument("--motivo", required=True)
    so.add_argument("--revisione", required=True, help="gg/mm/aaaa")

    ri = sub.add_parser("riprendi", help="riporta il lancio allo stato di partenza")
    ri.add_argument("slug")

    ab = sub.add_parser("abbandona", help="porta il lancio in ABORTITO, conservando cio' che si salva")
    ab.add_argument("slug")
    ab.add_argument("--motivo", required=True)

    fi = sub.add_parser("firma", help="firma umana su prezzo e data (canale comando-utente)")
    fi.add_argument("slug")
    fi.add_argument("--prezzo", type=float, required=True)
    fi.add_argument("--data", required=True, help="data di apertura, gg/mm/aaaa")
    fi.add_argument("--chi", default=None, help="default: git config user.name")
    fi.add_argument("--ruolo", choices=["vendita", "acquisizione-contatti"], default=None)
    fi.add_argument("--durata", type=int, default=None,
                    help="giorni di carrello (default: dalla proposta)")

    vl = sub.add_parser("via-libera", help="autorizza l'apertura della vendita")
    vl.add_argument("slug")
    vl.add_argument("--chi", default=None)

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
              "elenco": _cmd_elenco, "valida": _cmd_valida,
              "avanza": _cmd_avanza, "sospendi": _cmd_sospendi, "riprendi": _cmd_riprendi,
              "abbandona": _cmd_abbandona, "firma": _cmd_firma, "via-libera": _cmd_via_libera}
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
