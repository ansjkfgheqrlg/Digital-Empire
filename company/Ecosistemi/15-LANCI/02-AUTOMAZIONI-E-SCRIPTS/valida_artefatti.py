# -*- coding: utf-8 -*-
"""SUPERATO da `python -m scripts.lancio valida <slug>`.

Questo file e' nato qualche ora prima del comando `lancio`, per chiudere lo
scaglione S1 con una prova invece che con una dichiarazione. Ha fatto il suo
lavoro: ha trovato quattro nomi di campo che avevo indovinato invece di leggere.

Adesso la stessa cosa la fa `scripts/stato_lancio.py`, che in piu' conosce lo
stato del lancio, i verbali e il lock. Due validatori sono due fonti di verita',
ed e' esattamente la malattia che la decisione 3 di ADR-025 vieta.

Non e' stato cancellato (Direttiva Max 2026-08-31: niente si scarta, si rende
operativo): chi lo chiama viene mandato dove si lavora adesso.
"""
import os
import sys

QUI = os.path.dirname(os.path.abspath(__file__))


def main() -> int:
    slug = sys.argv[1] if len(sys.argv) > 1 else "<slug>"
    print()
    print("  Questo script e' superato. Usa il comando del lancio:")
    print()
    print("     cd \"%s\"" % QUI)
    print("     python -m scripts.lancio valida %s" % slug)
    print()
    print("  Fa la stessa validazione, piu' lo stato, i verbali e il lock.")
    print()
    return 2


if __name__ == "__main__":
    sys.exit(main())
