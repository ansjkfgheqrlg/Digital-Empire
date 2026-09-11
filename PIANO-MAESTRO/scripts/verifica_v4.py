#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
verifica_v4.py — il gate meccanico di V4 (PIANO-MAESTRO/31-PIANO-IMPERO-VIVO/V4-ESECUTIVO/).

Controlla che ogni documento di scaglione esista e rispetti il template obbligatorio di
00-INDICE.md §3 (sette sezioni 0..6), che non usi `~` davanti a un numero, che ogni «bloccato»
stia in un documento con la sezione 0 (cosa NON e' bloccato), e l'invariante INV-GAEL: solo
15-E5b-INGRESSI.md puo' dipendere da Gael; ogni altro documento che nomina Gael deve dichiararlo
come «non dipende» / «INV-GAEL».

Esce 0 se tutto passa, 1 altrimenti, e stampa per documento la sezione o la regola che manca.
Console Windows cp1252: nessuna emoji nei print.

USO:
    py -3 PIANO-MAESTRO/scripts/verifica_v4.py
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))          # PIANO-MAESTRO/
V4_DIR = os.path.join(ROOT, "31-PIANO-IMPERO-VIVO", "V4-ESECUTIVO")

DOCUMENTI = [
    "01-E0a-MERCE.md",
    "02-E0.5-AGGANCI.md",
    "03-E0b-ROTAZIONE.md",
    "04-E0.9-ATTO-DI-VENDITA.md",
    "05-E0.6-REGOLE.md",
    "06-E0.7-HOOK.md",
    "07-E1-PERIMETRO.md",
    "08-E2-RINOMINA.md",
    "09-F3-EMETTITORE.md",
    "10-E3.0-RIACCENSIONE.md",
    "11-E3-FETTA-VERTICALE.md",
    "12-E4-FUNZIONI.md",
    "13-E5a-GENERATORE.md",
    "14-E5bis-ADOZIONE.md",
    "15-E5b-INGRESSI.md",
    "16-E5c-F1-POPOLATA.md",
    "17-E6-SENZA-MOTORE.md",
    "18-E7-ONDATE.md",
    "19-E8-CONSEGNA.md",
    "20-E9-AUTOMIGLIORAMENTO.md",
]

# Le sette sezioni del template (00-INDICE.md §3). Si accetta `## 0.`, `## 0 `, `## 0 —`, ecc.
SEZIONI = [
    (0, r"^##\s*0[\.\s—–-]"),
    (1, r"^##\s*1[\.\s—–-]"),
    (2, r"^##\s*2[\.\s—–-]"),
    (3, r"^##\s*3[\.\s—–-]"),
    (4, r"^##\s*4[\.\s—–-]"),
    (5, r"^##\s*5[\.\s—–-]"),
    (6, r"^##\s*6[\.\s—–-]"),
]

TILDE_NUMERO = re.compile(r"(?<![`\w])~\s?\d")
GAEL = re.compile(r"\bGael\b")
GAEL_OK = re.compile(r"INV-GAEL|non dipende|non aspetta|nessuna dipendenza", re.IGNORECASE)
BLOCCATO = re.compile(r"\bblocc", re.IGNORECASE)
UNICO_CON_GAEL = "15-E5b-INGRESSI.md"


def leggi(path):
    with io.open(path, encoding="utf-8", errors="replace") as f:
        return f.read()


def verifica_documento(nome):
    path = os.path.join(V4_DIR, nome)
    problemi = []
    if not os.path.exists(path):
        return ["MANCA il file"]
    testo = leggi(path)
    righe = testo.splitlines()

    for numero, pattern in SEZIONI:
        rx = re.compile(pattern, re.MULTILINE)
        if not rx.search(testo):
            problemi.append("manca la sezione %d del template" % numero)

    for i, riga in enumerate(righe, 1):
        if riga.strip().startswith("```"):
            continue
        if TILDE_NUMERO.search(riga):
            problemi.append("riga %d: `~` davanti a un numero (L10)" % i)

    if BLOCCATO.search(testo) and not re.search(SEZIONI[0][1], testo, re.MULTILINE):
        problemi.append("usa 'bloccato' senza la sezione 0 (ADR-028)")

    if nome != UNICO_CON_GAEL and GAEL.search(testo) and not GAEL_OK.search(testo):
        problemi.append("nomina Gael senza dichiarare 'non dipende' / INV-GAEL")

    if len(testo.strip()) < 1500:
        problemi.append("troppo corto (%d caratteri): non e' un documento esecutivo" % len(testo))

    return problemi


def main():
    if not os.path.isdir(V4_DIR):
        sys.stdout.write("cartella V4 non trovata: %s\n" % V4_DIR)
        return 1

    totale_problemi = 0
    ok = 0
    for nome in DOCUMENTI:
        problemi = verifica_documento(nome)
        if problemi:
            totale_problemi += len(problemi)
            sys.stdout.write("[X] %s\n" % nome)
            for p in problemi:
                sys.stdout.write("      - %s\n" % p)
        else:
            ok += 1
            sys.stdout.write("[OK] %s\n" % nome)

    sys.stdout.write("\n%d/%d documenti conformi, %d problemi\n" % (ok, len(DOCUMENTI), totale_problemi))
    return 0 if totale_problemi == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
