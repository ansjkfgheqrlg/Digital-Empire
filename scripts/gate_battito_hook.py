#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
gate_battito_hook.py — il gate che scatta DA SOLO (hook Stop).

PERCHE' ESISTE (2026-09-05, sera). Nel pomeriggio dello stesso giorno il battito era
uscito fuori forma quattro volte, e la contromisura era stata `verifica_recap.py`: uno
strumento che dice SI o NO sulla forma. Max ha fatto la domanda giusta -- "hai risolto in
modo definitivo?" -- e la risposta onesta era NO: lo strumento c'era, ma l'ordine di USARLO
restava una riga scritta in dottrina, cioe' esattamente il tipo di regola che aveva gia'
ceduto cinque volte. Uno strumento che dipende dal fatto che io mi ricordi di lanciarlo non
e' un gate: e' un altro promemoria.

Questo hook chiude il cerchio. Gira all'evento Stop (fine turno), legge l'ultimo messaggio
che sto per consegnare a Max, e se contiene un battito fuori forma BLOCCA la consegna
ordinandomi di riscriverlo. Non dipende piu' dalla mia memoria del momento.

TRE PROTEZIONI, tutte necessarie:
  1. FALSI POSITIVI. Le righe dentro blocchi ``` , le citazioni `>` e le righe indentate
     sono ESEMPI (documentazione, dottrina, spiegazioni a Max) e non vengono mai validate.
     Senza questo, ogni volta che scrivo del formato del battito mi bloccherei da solo.
  2. ANTI-LOOP. Se `stop_hook_active` e' vero il blocco e' gia' scattato una volta in questo
     turno: si esce senza bloccare. Un gate che intrappola la sessione e' peggio del difetto
     che sorveglia.
  3. MAI ROTTURA. Qualunque errore imprevisto -> exit 0 silenzioso. Un hook che fa fallire
     il turno di Max sarebbe un danno piu' grande di un battito storto.

Lo schema NON e' duplicato qui: si importa da `verifica_recap.py`, che resta l'unica fonte
di verita' della forma (lezione §6.13 -- non esistono due corpi da tenere allineati).
"""

import io
import json
import os
import re
import sys

QUI = os.path.dirname(os.path.abspath(__file__))
if QUI not in sys.path:
    sys.path.insert(0, QUI)

# Segnali che il testo CONTIENE un tentativo di battito. Se non ce n'e' nessuno,
# l'hook non ha niente da dire: non si impone un battito dove non serve.
SEGNALE_TITOLO = re.compile(r"^\s*\*\*.{0,3}\s*RECAP\s*[—-]", re.IGNORECASE)
SEGNALE_VOCE = re.compile(r"^🟠")


def righe_reali(testo):
    """Le righe di prosa vera: fuori dai blocchi di codice, non citate, non indentate.

    Serve a distinguere UN BATTITO da un ESEMPIO di battito. Documentazione, dottrina e
    spiegazioni mostrano il formato dentro ``` o dopo `>`: quelle righe non sono un battito
    consegnato a Max, sono un discorso sul battito, e non vanno mai giudicate.
    """
    dentro_codice = False
    fuori = []
    for i, riga in enumerate(testo.replace("\r\n", "\n").split("\n")):
        spoglia = riga.strip()
        if spoglia.startswith("```") or spoglia.startswith("~~~"):
            dentro_codice = not dentro_codice
            fuori.append((i, None))
            continue
        if dentro_codice or spoglia.startswith(">") or riga.startswith("    "):
            fuori.append((i, None))
            continue
        fuori.append((i, riga))
    return fuori


def trova_battito(testo):
    """Ritorna (indice_prima_riga, blocco_di_8_righe) del battito, o (None, None).

    Il battito e' titolo + riga vuota + sei voci: si prende quella finestra e la si passa
    al validatore vero. Se c'e' solo un troncone (voci senza titolo), si passa quello: il
    validatore dira' esattamente cosa manca.
    """
    righe = testo.replace("\r\n", "\n").split("\n")
    utili = {i: r for i, r in righe_reali(testo) if r is not None}

    inizio = None
    for i in sorted(utili):
        if SEGNALE_TITOLO.match(utili[i]):
            inizio = i
            break
    if inizio is None:
        for i in sorted(utili):
            if SEGNALE_VOCE.match(utili[i]):
                inizio = i
                break
    if inizio is None:
        return None, None

    return inizio, "\n".join(righe[inizio:inizio + 8])


def blocchi_testo_del_turno(percorso):
    """I blocchi `text` dell'ultimo turno, SEPARATI — non concatenati.

    Separati e' la parte che conta, ed e' una correzione pagata in produzione il 2026-09-05:
    la prima versione li univa in un testo solo, e in un turno lungo (piu' messaggi intervallati
    da strumenti) il battito finiva a meta' della concatenazione. Il gate lo leggeva come
    "battito non in cima" e bloccava un messaggio giusto — al primo turno vero, su di me.
    Ogni blocco e' un messaggio a se' che Max legge da solo: la posizione del battito si giudica
    DENTRO il suo blocco, non dentro la somma del turno.
    """
    try:
        righe = io.open(percorso, encoding="utf-8", errors="replace").read().splitlines()
    except Exception:
        return ""

    pezzi = []
    for riga in reversed(righe):
        try:
            d = json.loads(riga)
        except Exception:
            continue
        tipo = d.get("type")
        msg = d.get("message") or {}
        contenuto = msg.get("content")

        if tipo == "user":
            # un tool_result e' la macchina che risponde a me, non Max che parla
            solo_tool = False
            if isinstance(contenuto, list):
                tipi = [b.get("type") for b in contenuto if isinstance(b, dict)]
                solo_tool = bool(tipi) and all(t == "tool_result" for t in tipi)
            if not solo_tool:
                break
            continue

        if tipo == "assistant" and isinstance(contenuto, list):
            for b in contenuto:
                if isinstance(b, dict) and b.get("type") == "text":
                    t = b.get("text") or ""
                    if t.strip():
                        pezzi.append(t)

    return list(reversed(pezzi))


def main():
    try:
        grezzo = sys.stdin.buffer.read().decode("utf-8", "replace")
    except Exception:
        return 0
    if not grezzo.strip():
        return 0

    try:
        dati = json.loads(grezzo)
    except Exception:
        return 0

    # PROTEZIONE 2 — il blocco e' gia' scattato in questo turno: non si insiste.
    if dati.get("stop_hook_active"):
        return 0

    percorso = dati.get("transcript_path") or ""
    if not percorso or not os.path.exists(percorso):
        return 0

    messaggi = blocchi_testo_del_turno(percorso)
    if not messaggi:
        return 0

    from verifica_recap import valida  # unica fonte di verita' della forma

    problemi = []
    for testo in messaggi:
        inizio, blocco = trova_battito(testo)
        if blocco is None:
            continue  # questo messaggio non porta un battito: niente da sorvegliare

        guai = valida(blocco)

        # La posizione e' parte della regola (§6.11: il battito va IN CIMA) e si giudica
        # DENTRO il messaggio che lo contiene — mai sulla somma del turno (vedi la nota in
        # blocchi_testo_del_turno: quella confusione bloccava messaggi corretti).
        prima = "\n".join(testo.split("\n")[:inizio]).strip()
        if prima:
            guai = ["il battito non e' in cima al messaggio: prima di esso ci sono gia' "
                    "%d caratteri di testo (§6.11 -- mai in fondo, mai dopo l'analisi)"
                    % len(prima)] + guai

        problemi.extend(guai)

    if not problemi:
        return 0

    motivo = (
        "GATE BATTITO — la forma non torna, il messaggio non parte cosi'.\n\n"
        + "\n".join("  - " + p for p in problemi)
        + "\n\nRiscrivi il battito nella forma fissa (emperator.md 6.11), poi consegna:\n\n"
        "**⏱️ RECAP — <n>%**\n\n"
        "\U0001f7e0 **Fatto:** <una riga>\n"
        "\U0001f7e0 **Sto facendo:** <una riga>\n"
        "\U0001f7e0 **Farò:** <una riga>\n"
        "\U0001f7e0 **Forze:** <n> attive — <GRADO> <nome> <cosa fa>  |  nessuna, sto lavorando da solo\n"
        "\U0001f7e0 **Assetto:** **GOD EMPEROR DOOM**  |  normale\n"
        "\U0001f7e0 **Potere:** <n>%\n"
    )

    risposta = {"decision": "block", "reason": motivo}
    sys.stdout.buffer.write(json.dumps(risposta, ensure_ascii=False).encode("utf-8"))
    sys.stdout.buffer.flush()
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:  # PROTEZIONE 3 — non si rompe mai il turno di Max
        try:
            p = os.path.join(QUI, ".gate_battito_hook.log")
            import datetime
            import traceback
            with io.open(p, "a", encoding="utf-8") as f:
                f.write("[%s] %r\n%s\n" % (
                    datetime.datetime.now().isoformat(timespec="seconds"),
                    exc, traceback.format_exc()))
        except Exception:
            pass
        sys.exit(0)
