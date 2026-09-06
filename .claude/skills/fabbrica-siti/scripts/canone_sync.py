# -*- coding: utf-8 -*-
"""
canone_sync.py — verifica che canone.css e canone.json non siano divergenti.

Il dossier 32 promette che i due file "non possono divergere". Questo script e'
cio' che rende vera quella frase invece di lasciarla un'intenzione.

Controlla tre cose:
  1. ogni colore esadecimale scritto in canone.css e' fra gli "ammessi" del JSON
  2. nessun colore "vietato" del JSON compare in canone.css
  3. le curve dichiarate nel JSON esistono identiche nel CSS

Uso:
  python .claude/skills/fabbrica-siti/scripts/canone_sync.py

Esce con 0 se il canone e' coerente, 1 altrimenti. Nessuna emoji: la console
Windows di questo repo e' cp1252.
"""
import json
import os
import re
import sys

QUI = os.path.dirname(os.path.abspath(__file__))
CANONE = os.path.join(os.path.dirname(QUI), "canone")
CSS = os.path.join(CANONE, "canone.css")
JSON_ = os.path.join(CANONE, "canone.json")

HEX = re.compile(r"#[0-9a-fA-F]{3,8}\b")


def normalizza(h):
    """#fff -> #ffffff, cosi' la forma corta non sfugge al controllo."""
    h = h.lower()
    if len(h) == 4:
        return "#" + h[1] * 2 + h[2] * 2 + h[3] * 2
    return h


def leggi(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def main():
    css = leggi(CSS)
    dati = json.loads(leggi(JSON_))

    # Fuori dal controllo: i data: URI della grana (contengono %23n, un id SVG,
    # non un colore) e i commenti, dove i colori VIETATI sono citati apposta per
    # dire di non usarli.
    css_pulito = re.sub(r'url\("data:[^"]*"\)', "", css)
    css_pulito = re.sub(r"/\*.*?\*/", "", css_pulito, flags=re.S)

    ammessi = {c.lower() for c in dati["colori"]["ammessi"]}
    vietati = {c.lower(): m for c, m in dati["colori"]["vietati"].items()}

    errori = []

    # --- 1. colori del CSS non dichiarati nel JSON -------------------------
    trovati = {normalizza(h) for h in HEX.findall(css_pulito)}
    non_dichiarati = sorted(trovati - ammessi - set(vietati))
    for c in non_dichiarati:
        errori.append("colore %s usato in canone.css ma non fra gli ammessi in canone.json" % c)

    # --- 2. colori vietati usati davvero ----------------------------------
    for c in sorted(trovati & set(vietati)):
        errori.append("colore VIETATO %s presente in canone.css - %s" % (c, vietati[c]))

    # --- 3. curve -----------------------------------------------------------
    for nome, valore in dati["curve"].items():
        if not nome.startswith("--"):
            continue
        atteso = "%s: %s;" % (nome, valore)
        if atteso not in re.sub(r"[ 	]+", " ", css):
            errori.append("curva %s dichiarata nel JSON come '%s' ma non trovata identica nel CSS"
                          % (nome, valore))

    # --- esito --------------------------------------------------------------
    print("CANONE SYNC - Fabbrica Siti")
    print("  canone.css  : %d righe, %d colori distinti" % (css.count("\n") + 1, len(trovati)))
    print("  canone.json : %d ammessi, %d vietati, %d curve"
          % (len(ammessi), len(vietati), len([k for k in dati["curve"] if k.startswith("--")])))

    if errori:
        print("\n  FAIL - %d divergenze:" % len(errori))
        for e in errori:
            print("    - " + e)
        return 1

    print("\n  PASS - canone.css e canone.json sono allineati.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
