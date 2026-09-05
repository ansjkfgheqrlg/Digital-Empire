#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
verifica_recap.py — il gate meccanico del battito (emperator.md §6.11).

PERCHE' ESISTE (2026-09-05): la forma del battito era scritta carattere per carattere
in emperator.md §6.11 e ripetuta nel promemoria di ogni messaggio (emperator_hook.py).
Nonostante questo e' uscita fuori forma almeno quattro volte nello stesso giorno.
Quattro incidenti precedenti sulla stessa regola (posizione, gergo, forze, assetto) erano
gia' documentati in §6.11 — la prosa, per quanto ripetuta, non e' un gate: dipende dalla
disciplina del turno in corso, che un contesto lungo o una riga scritta di fretta erodono.
Questo script e' il controllo che non dipende dalla memoria del momento: legge un battito
e dice SI o NO, con la riga esatta che non torna.

USO (prima di inviare OGNI battito):
    printf '%s' "<testo del battito>" | py -3 scripts/verifica_recap.py
    py -3 scripts/verifica_recap.py --file percorso\\al\\battito.txt

Esce 0 se il battito e' conforme, 1 se non lo e' (con l'elenco dei problemi su stdout).
Non fallisce mai in modo silenzioso: un'eccezione imprevista stampa il traceback ed esce 1,
mai 0 — un gate che dice "va bene" per errore e' peggio di nessun gate.
"""

import io
import re
import sys

# Le sei voci, sempre in quest'ordine (emperator.md §6.11, regola 4).
# Il secondo elemento, se presente, e' il vincolo sul VALORE dopo l'etichetta.
VOCI = [
    ("Fatto", None),
    ("Sto facendo", None),
    ("Farò", None),
    ("Forze", None),
    ("Assetto", r"(\*\*GOD EMPEROR DOOM\*\*|normale)"),
    ("Potere", r"\d{1,3}%"),
]

TITOLO_RE = re.compile(r"^\*\*⏱️ RECAP — (\d{1,3})%\*\*$")


def _leggi_stdin():
    grezzo = sys.stdin.buffer.read()
    return grezzo.decode("utf-8", "replace")


def valida(testo):
    """Ritorna una lista di problemi. Lista vuota = battito conforme."""
    problemi = []
    righe = testo.replace("\r\n", "\n").split("\n")

    # Il battito deve stare in CIMA: si cerca dalla prima riga non vuota, non altrove
    # nel messaggio (emperator.md §6.11: "un battito in fondo non è un battito").
    idx = 0
    while idx < len(righe) and righe[idx].strip() == "":
        idx += 1
    if idx >= len(righe):
        return ["blocco vuoto: nessun battito trovato nel testo passato"]

    riga_num = idx + 1
    titolo = righe[idx].strip()
    m = TITOLO_RE.match(titolo)
    if not m:
        problemi.append(
            "riga %d: titolo non conforme — atteso `**\u23f1\ufe0f RECAP \u2014 <n>%%**` "
            "in grassetto da solo, trovato: %r" % (riga_num, righe[idx])
        )
    else:
        n = int(m.group(1))
        if n > 100:
            problemi.append("riga %d: percentuale %d%% impossibile (>100)" % (riga_num, n))
    idx += 1

    # riga vuota fra titolo e le sei voci (regola 2)
    if idx >= len(righe) or righe[idx].strip() != "":
        riga_num = idx + 1
        problemi.append("riga %d: manca la riga vuota fra il titolo e le sei voci" % riga_num)
    else:
        idx += 1

    # le sei voci, in ordine, nessuna esclusa (regola 4)
    for label, vincolo_valore in VOCI:
        riga_num = idx + 1
        if idx >= len(righe):
            problemi.append("manca la voce '%s:' — il battito è troncato" % label)
            continue
        riga = righe[idx]
        pattern = r"^🟠 \*\*%s:\*\* (.+)$" % re.escape(label)
        m = re.match(pattern, riga)
        if not m:
            problemi.append(
                "riga %d: attesa `🟠 **%s:** ...`, trovato: %r" % (riga_num, label, riga)
            )
        else:
            valore = m.group(1).strip()
            if not valore:
                problemi.append("riga %d: voce '%s' senza contenuto dopo i due punti" % (riga_num, label))
            elif vincolo_valore and not re.fullmatch(vincolo_valore, valore):
                problemi.append(
                    "riga %d: valore di '%s' non valido (%r) — atteso uno fra %s"
                    % (riga_num, label, valore, vincolo_valore)
                )
            # regola 6: niente grassetto sparso nel valore, tranne GOD EMPEROR DOOM in Assetto
            if label != "Assetto" and "**" in valore:
                problemi.append(
                    "riga %d: il testo dopo l'etichetta '%s' non va in grassetto" % (riga_num, label)
                )
        idx += 1

    # righe residue non vuote subito dopo le sei voci = settima voce o testo attaccato
    if idx < len(righe) and righe[idx].strip() != "":
        problemi.append(
            "riga %d: contenuto extra subito dopo le sei voci (%r) — il battito è tre blocchi, "
            "non uno più lungo" % (idx + 1, righe[idx])
        )

    return problemi


def main():
    args = sys.argv[1:]
    if args and args[0] == "--file":
        if len(args) < 2:
            sys.stderr.write("uso: verifica_recap.py --file <percorso>\n")
            return 1
        with io.open(args[1], encoding="utf-8", errors="replace") as f:
            testo = f.read()
    else:
        testo = _leggi_stdin()

    problemi = valida(testo)

    out = []
    if not problemi:
        out.append("OK — battito conforme allo schema fisso (emperator.md §6.11)")
    else:
        out.append("BATTITO NON CONFORME — %d problema/i, non si invia così:" % len(problemi))
        for p in problemi:
            out.append("  - " + p)

    sys.stdout.buffer.write(("\n".join(out) + "\n").encode("utf-8"))
    sys.stdout.buffer.flush()
    return 0 if not problemi else 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        import traceback
        sys.stderr.buffer.write(traceback.format_exc().encode("utf-8", "replace"))
        sys.exit(1)
