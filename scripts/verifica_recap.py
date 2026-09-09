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

FORMA A QUADRATI (2026-09-09, ordine di Max — solo estetica, il contenuto delle sei voci
non cambia). Il vecchio elenco piatto a sei righe con pallino era corretto ma illeggibile
di corsa. Max ha chiesto esplicitamente un formato diverso da quello di `frantuma.py`
(niente albero con rami `├──`): titolo, poi cinque riquadri in markdown puro (mai dentro
```: un blocco di codice sparisce dal controllo, vedi `righe_reali` in
gate_battito_hook.py), uno per Fatto / Sto facendo / Farò / Forze / Assetto+Potere,
uniti da una freccia `↓` su riga propria. Ogni riquadro e' aperto sul lato destro (solo
`┌─...`, `│ testo`, `└─...`) apposta: un bordo destro allineato richiederebbe imbottire
il testo con spazi multipli, e gli spazi multipli fuori da un blocco di codice possono
essere compressi dal renderer che mostra il messaggio a Max — un bordo destro storto
sarebbe peggio di nessun bordo destro. Nessuna larghezza va quindi confrontata fra
riquadri: si controlla solo che i caratteri giusti (┌ │ └ ─ ↓) siano nei punti giusti.

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

# I cinque riquadri, in ordine fisso (emperator.md §6.11). Il secondo elemento e' il
# numero di righe di contenuto ammesse dopo l'etichetta (min, max) — "MAX quattro frasi"
# per le prime quattro (ordine di Max, 2026-09-09); il quinto e' Assetto+Potere insieme,
# sempre esattamente due righe (l'assetto, poi il potere).
RIQUADRI = [
    ("Fatto", 1, 4),
    ("Sto facendo", 1, 4),
    ("Farò", 1, 4),
    ("Forze", 1, 4),
    ("Assetto", 2, 2),
]

TITOLO_RE = re.compile(r"^\*\*⏱️ RECAP — (\d{1,3})%\*\*$")
TOP_RE = re.compile(r"^┌─+$")
BOTTOM_RE = re.compile(r"^└─+$")
RIGA_RE = re.compile(r"^│ (.+)$")
FRECCIA = "↓"
ASSETTO_RE = re.compile(r"^(\*\*GOD EMPEROR DOOM\*\*|normale)$")
POTERE_RE = re.compile(r"^🟠 Potere: (\d{1,3})%$")


def _leggi_stdin():
    grezzo = sys.stdin.buffer.read()
    return grezzo.decode("utf-8", "replace")


def _riquadro(righe, idx, etichetta, min_righe, max_righe, problemi):
    """Legge un riquadro a partire da `idx` (che deve puntare a `┌─...`).

    Ritorna l'indice subito dopo `└─...`. Non solleva mai — accumula i problemi
    e prova comunque a ripartire dalla riga successiva, cosi' un solo riquadro
    rotto non nasconde gli errori di quelli dopo.
    """
    if idx >= len(righe) or not TOP_RE.match(righe[idx]):
        problemi.append(
            "riga %d: atteso il bordo superiore del riquadro '%s' (`┌─...`), trovato: %r"
            % (idx + 1, etichetta, righe[idx] if idx < len(righe) else "<fine testo>")
        )
        return idx + 1
    idx += 1

    if idx >= len(righe) or righe[idx] != "│ 🟠 %s" % etichetta:
        problemi.append(
            "riga %d: attesa l'etichetta `│ 🟠 %s`, trovato: %r"
            % (idx + 1, etichetta, righe[idx] if idx < len(righe) else "<fine testo>")
        )
    else:
        idx += 1

    contenuto = []
    while idx < len(righe) and RIGA_RE.match(righe[idx]) and not BOTTOM_RE.match(righe[idx]):
        contenuto.append((idx, RIGA_RE.match(righe[idx]).group(1)))
        idx += 1

    if len(contenuto) < min_righe:
        problemi.append(
            "riquadro '%s': servono almeno %d riga/e di contenuto, trovate %d"
            % (etichetta, min_righe, len(contenuto))
        )
    if len(contenuto) > max_righe:
        problemi.append(
            "riquadro '%s': massimo %d riga/e di contenuto (ordine di Max, 2026-09-09), "
            "trovate %d — accorcia" % (etichetta, max_righe, len(contenuto))
        )
    for riga_num, valore in contenuto:
        if not valore.strip():
            problemi.append("riga %d: riga del riquadro '%s' vuota" % (riga_num + 1, etichetta))
        elif "**" in valore and valore.strip() != "**GOD EMPEROR DOOM**":
            problemi.append(
                "riga %d: il contenuto del riquadro '%s' non va in grassetto (eccezione unica: "
                "`**GOD EMPEROR DOOM**` nel riquadro Assetto)" % (riga_num + 1, etichetta)
            )

    if etichetta == "Assetto" and len(contenuto) >= 1:
        valore_assetto = contenuto[0][1]
        if not ASSETTO_RE.match(valore_assetto):
            problemi.append(
                "riga %d: valore di Assetto non valido (%r) — atteso `normale` oppure "
                "`**GOD EMPEROR DOOM**`" % (contenuto[0][0] + 1, valore_assetto)
            )
        if len(contenuto) >= 2:
            valore_potere = contenuto[1][1]
            if not POTERE_RE.match(valore_potere):
                problemi.append(
                    "riga %d: attesa `🟠 Potere: <n>%%`, trovato: %r"
                    % (contenuto[1][0] + 1, valore_potere)
                )
            else:
                n = int(POTERE_RE.match(valore_potere).group(1))
                if n > 100:
                    problemi.append("riga %d: potere %d%% impossibile (>100)" % (contenuto[1][0] + 1, n))

    if idx >= len(righe) or not BOTTOM_RE.match(righe[idx]):
        problemi.append(
            "riga %d: atteso il bordo inferiore del riquadro '%s' (`└─...`), trovato: %r"
            % (idx + 1, etichetta, righe[idx] if idx < len(righe) else "<fine testo>")
        )
        return idx + 1
    return idx + 1


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
            "riga %d: titolo non conforme — atteso `**⏱️ RECAP — <n>%%**` "
            "in grassetto da solo, trovato: %r" % (riga_num, righe[idx])
        )
    else:
        n = int(m.group(1))
        if n > 100:
            problemi.append("riga %d: percentuale %d%% impossibile (>100)" % (riga_num, n))
    idx += 1

    # riga vuota fra il titolo e il primo riquadro (stessa regola di sempre)
    if idx >= len(righe) or righe[idx].strip() != "":
        problemi.append("riga %d: manca la riga vuota fra il titolo e il primo riquadro" % (idx + 1))
    else:
        idx += 1

    # i cinque riquadri, in ordine, separati da una riga con solo la freccia ↓
    for i, (etichetta, mn, mx) in enumerate(RIQUADRI):
        idx = _riquadro(righe, idx, etichetta, mn, mx, problemi)
        e_ultimo = i == len(RIQUADRI) - 1
        if not e_ultimo:
            if idx >= len(righe) or righe[idx].strip() != FRECCIA:
                problemi.append(
                    "riga %d: manca la freccia `%s` su riga propria fra i riquadri '%s' e '%s'"
                    % (idx + 1, FRECCIA, etichetta, RIQUADRI[i + 1][0])
                )
            else:
                idx += 1

    # righe residue non vuote dopo l'ultimo riquadro = testo attaccato al battito
    if idx < len(righe) and righe[idx].strip() != "":
        problemi.append(
            "riga %d: contenuto extra subito dopo l'ultimo riquadro (%r) — il battito finisce "
            "col bordo di Assetto/Potere" % (idx + 1, righe[idx])
        )

    return problemi


def costruisci(fatto, sto_facendo, farò, forze, assetto, potere, percentuale):
    """Genera il testo del battito a partire dai valori — cosi' non si disegnano i
    riquadri a mano (stesso principio di frantuma.py: generato dal codice, mai scritto
    a mano). Ogni argomento voce e' una stringa o una lista di 1-4 righe; `assetto` e'
    "normale" oppure "GOD EMPEROR DOOM" (senza asterischi, li aggiunge la funzione)."""
    def _righe(v):
        return v if isinstance(v, list) else [v]

    blocchi = [
        ("Fatto", _righe(fatto)),
        ("Sto facendo", _righe(sto_facendo)),
        ("Farò", _righe(farò)),
        ("Forze", _righe(forze)),
        ("Assetto", [
            "**GOD EMPEROR DOOM**" if assetto == "GOD EMPEROR DOOM" else "normale",
            "🟠 Potere: %d%%" % potere,
        ]),
    ]

    out = ["**⏱️ RECAP — %d%%**" % percentuale, ""]
    for i, (etichetta, righe) in enumerate(blocchi):
        larghezza = max([len(etichetta) + 3] + [len(r) for r in righe]) + 2
        out.append("┌" + "─" * larghezza)
        out.append("│ 🟠 %s" % etichetta)
        for r in righe:
            out.append("│ %s" % r)
        out.append("└" + "─" * larghezza)
        if i < len(blocchi) - 1:
            out.append(FRECCIA)
    return "\n".join(out)


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
