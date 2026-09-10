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
  1. FALSI POSITIVI. Un blocco di codice che non e' IN CIMA al messaggio, o che non
     contiene un titolo di battito come sua prima riga, e' un ESEMPIO (documentazione,
     spiegazione a Max) e non viene mai validato — altrimenti mi bloccherei da solo ogni
     volta che discuto il formato con un esempio incorporato nella prosa.
  2. ANTI-LOOP. Se `stop_hook_active` e' vero il blocco e' gia' scattato una volta in questo
     turno: si esce senza bloccare. Un gate che intrappola la sessione e' peggio del difetto
     che sorveglia.
  3. MAI ROTTURA. Qualunque errore imprevisto -> exit 0 silenzioso. Un hook che fa fallire
     il turno di Max sarebbe un danno piu' grande di un battito storto.

Lo schema NON e' duplicato qui: si importa da `verifica_recap.py`, che resta l'unica fonte
di verita' della forma (lezione §6.13 -- non esistono due corpi da tenere allineati).

IL BATTITO VERO NON STA MAI DENTRO UN BLOCCO DI CODICE (2026-09-09, fermo dal 7º giro). Il
6º giro aveva messo il battito dentro ``` perche' li' lo spazio di centraggio non collassa.
Funzionava per gli spazi, ma Max ha bocciato l'effetto collaterale mai controllato: nel suo
renderer (VSCode) un blocco di codice e' un widget a se' — sfondo/testo blu, pulsante
"copia" — non testo semplice. Ordine di Max, testuale: *"non deve mai essere con quel
formato da copiare e tutto di colori azzurri"*. Questo divieto e' rimasto fermo anche
all'8º giro (2026-09-09, piu' tardi): Max ha chiesto di tornare al formato SEMPLICE
pre-centraggio — bullet `🟩 **<Etichetta>:** <contenuto libero>`, senza tabella e senza
rientro a mano (vedi `verifica_recap.py` per la storia completa). Questo hook cerca il
battito PRIMA dentro un fence in cima: se lo trova, e' VIETATO e blocca con quel motivo
specifico. Se il messaggio porta un tentativo di battito fuori da un fence (il formato
giusto), lo valida come bullet. Un fence che non e' in cima, o che non apre con un titolo
di battito come prima riga, o che ha prosa vera anche DOPO la sua chiusura, resta un
ESEMPIO di documentazione e non viene toccato.
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
SEGNALE_VOCE = re.compile(r"^🟩 \*\*[^:]+:\*\*")  # fallback: una voce bullet, es. `🟩 **Fatto:** ...`
SEGNALE_POTERE = re.compile(r"^🟩 \*\*Potere:\*\* \d{1,3}%$")  # ultima riga di ogni battito valido
TETTO_RIGHE_BLOCCO = 60  # protezione anti-input-rotto: nessun battito reale supera questo

# Segnale di un tentativo di Missione (§6.11, 🔴): stessa filosofia del battito ma piu'
# semplice — niente centraggio, niente rendering ambiguo, quindi niente saga di giri.
SEGNALE_MISSIONE = re.compile(r"^🔴 \*\*Sto facendo:\*\*")
TETTO_RIGHE_MISSIONE = 30  # una Missione e' sempre corta: 2 righe + poche fasi


def righe_reali(testo):
    """Le righe di prosa vera: fuori dai blocchi di codice, non citate, non indentate.

    Usata SOLO per il ramo di fallback (un tentativo di battito scritto fuori da un fence,
    da bloccare col motivo "manca il blocco di codice"): serve a non confondere un esempio
    di documentazione dentro un ``` con un tentativo di consegna vero fuori da un fence.
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
    """Ritorna (indice_prima_riga, blocco, dentro_fence) del battito, o (None, None, None).

    Prima cerca un blocco ``` IN CIMA al messaggio (dopo eventuali righe vuote) la cui
    prima riga di contenuto e' un titolo di battito: se lo trova, il battito e' quello,
    `dentro_fence=True`, e `blocco` e' il testo fra le due righe di fence (titolo incluso).
    Un fence in cima che NON apre con un titolo e' un blocco di codice qualunque: ignorato.
    Un fence che contiene un titolo ma non e' in cima (c'e' prosa vera prima) e' un esempio
    di documentazione: ignorato anche lui, non e' un tentativo di consegna.

    Se non c'e' nessun fence in cima, cerca un tentativo di battito scritto in chiaro — dal
    7º giro e' il formato GIUSTO (tabella markdown, niente fence): se lo trova lo valida
    come tabella; se il testo e' comunque malformato, `valida()` dira' dove.
    """
    righe = testo.replace("\r\n", "\n").split("\n")

    idx = 0
    while idx < len(righe) and righe[idx].strip() == "":
        idx += 1
    if idx < len(righe):
        prima_riga = righe[idx].strip()
        if prima_riga.startswith("```") or prima_riga.startswith("~~~"):
            marcatore = prima_riga[:3]
            k = idx + 1
            while k < len(righe) and righe[k].strip() == "":
                k += 1
            if k < len(righe) and SEGNALE_TITOLO.match(righe[k]):
                limite = min(len(righe), k + TETTO_RIGHE_BLOCCO)
                fine = limite
                for m in range(k, limite):
                    if righe[m].strip().startswith(marcatore):
                        fine = m
                        break
                return idx, "\n".join(righe[k:fine]), True
            # un fence in cima che non apre con un battito: non e' un suo tentativo,
            # non c'e' altro da controllare in questo messaggio.
            return None, None, None

    # Nessun fence in cima. Prima di arrendersi, si cerca un fence PIU' AVANTI nel
    # messaggio che apra con un titolo di battito: se dopo la sua chiusura non c'e' PIU'
    # nessun testo vero, e' un tentativo di consegna con della prosa incollata prima per
    # errore (§6.11: mai in fondo, mai dopo l'analisi) — si blocca per posizione. Se invece
    # dopo la chiusura c'e' ancora prosa vera, e' un "panino" di documentazione ("ecco lo
    # schema: ``` ... ``` chiaro?") e si lascia stare, come sempre.
    i = 0
    while i < len(righe):
        spoglia = righe[i].strip()
        if spoglia.startswith("```") or spoglia.startswith("~~~"):
            marcatore = spoglia[:3]
            k = i + 1
            while k < len(righe) and righe[k].strip() == "":
                k += 1
            if k < len(righe) and SEGNALE_TITOLO.match(righe[k]):
                limite = min(len(righe), k + TETTO_RIGHE_BLOCCO)
                fine = limite
                chiusa_a = None
                for m in range(k, limite):
                    if righe[m].strip().startswith(marcatore):
                        fine = m
                        chiusa_a = m
                        break
                dopo = "\n".join(righe[(chiusa_a + 1):]).strip() if chiusa_a is not None else ""
                if not dopo:
                    return i, "\n".join(righe[k:fine]), True  # posizione sbagliata, valida() giudica il resto
                return None, None, None  # panino di documentazione: ignorato
            i = k
            continue
        i += 1

    # nessun fence, in cima o altrove: si cerca un tentativo scritto in chiaro — il
    # formato giusto dal 7º giro (tabella markdown, niente fence).
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
        return None, None, None

    fine = min(len(righe), inizio + TETTO_RIGHE_BLOCCO)
    for i in range(inizio, fine):
        if SEGNALE_POTERE.match(righe[i]):
            fine = i + 1
            break

    return inizio, "\n".join(righe[inizio:fine]), False


def trova_missione(testo):
    """Ritorna (indice_prima_riga, blocco, dentro_fence) di un tentativo di Missione, o
    (None, None, None). Stessa filosofia di `trova_battito()` ma piu' semplice: niente
    centraggio da preservare, quindi niente bisogno della doppia ricerca fence/plain — un
    fence in cima che apre con `🔴 **Sto facendo:**` e' vietato allo stesso modo del
    battito (stesso motivo: mai il widget blu copiabile); altrimenti si cerca in chiaro.
    """
    righe = testo.replace("\r\n", "\n").split("\n")

    idx = 0
    while idx < len(righe) and righe[idx].strip() == "":
        idx += 1
    if idx >= len(righe):
        return None, None, None

    prima_riga = righe[idx].strip()
    if prima_riga.startswith("```") or prima_riga.startswith("~~~"):
        marcatore = prima_riga[:3]
        k = idx + 1
        while k < len(righe) and righe[k].strip() == "":
            k += 1
        if k < len(righe) and SEGNALE_MISSIONE.match(righe[k]):
            limite = min(len(righe), k + TETTO_RIGHE_MISSIONE)
            fine = limite
            for m in range(k, limite):
                if righe[m].strip().startswith(marcatore):
                    fine = m
                    break
            return idx, "\n".join(righe[k:fine]), True
        return None, None, None  # fence che non apre con Missione: non e' un suo tentativo

    # Niente fence: si cerca un tentativo scritto in chiaro OVUNQUE nel messaggio (non solo
    # in cima) — se non e' in cima, `main()` lo segnala come problema di posizione, ma va
    # comunque TROVATO per poterlo segnalare (stessa logica del fallback di `trova_battito`).
    utili = {i: r for i, r in righe_reali(testo) if r is not None}
    inizio = None
    for i in sorted(utili):
        if SEGNALE_MISSIONE.match(utili[i]):
            inizio = i
            break
    if inizio is None:
        return None, None, None

    fine = min(len(righe), inizio + TETTO_RIGHE_MISSIONE)
    for i in range(inizio, fine):
        if righe[i].strip() == "":
            fine = i
            break
    return inizio, "\n".join(righe[inizio:fine]), False


# ---------------------------------------------------------------------------
# INNESCO DI MISSIONE — aggiunto il 2026-09-10 dopo un fallimento in produzione.
#
# Il gate sapeva gia' validare una Missione MALFATTA. Non sapeva accorgersi di una
# Missione MANCANTE: `trova_missione` restituiva None e il gate passava in silenzio
# (riga "questo messaggio non porta ne' un battito ne' una Missione"). Max ha scritto
# `Missione`, io ho risposto a braccio, e nessun controllo ha fiatato.
#
# Il battito non aveva questo buco perche' e' periodico: e' sempre dovuto, quindi la sua
# assenza si vede. Missione e' su richiesta — e nessuno guardava la richiesta.
# Un controllo a valle senza innesco a monte non e' un controllo: e' una speranza.
# ---------------------------------------------------------------------------

def missione_richiesta(percorso):
    """True se l'ultimo messaggio di Max e' il comando `Missione` (§6.11 del libro).

    Lettura stretta, per scelta: il libro dice «`Missione` (o `missione`) — DA SOLA».
    Si accetta la parola sola, con eventuale punteggiatura o emoji attorno; non si accetta
    dentro una frase, dove «la missione e' al 10%» non e' un comando ma un discorso.
    In dubbio si lascia passare: un gate che blocca a sproposito viene disattivato, e un
    gate disattivato non protegge piu' niente.
    """
    try:
        righe = io.open(percorso, encoding="utf-8", errors="replace").read().splitlines()
    except Exception:
        return False

    for riga in reversed(righe):
        try:
            d = json.loads(riga)
        except Exception:
            continue
        if d.get("type") != "user":
            continue
        contenuto = (d.get("message") or {}).get("content")
        if isinstance(contenuto, list):
            tipi = [b.get("type") for b in contenuto if isinstance(b, dict)]
            if tipi and all(t == "tool_result" for t in tipi):
                continue  # la macchina che risponde a me, non Max che parla
            testo = " ".join(b.get("text", "") for b in contenuto
                             if isinstance(b, dict) and b.get("type") == "text")
        else:
            testo = contenuto or ""
        # i promemoria di sistema non sono parole di Max
        testo = re.sub(r"<system-reminder>.*?</system-reminder>", " ", testo, flags=re.S)
        pulito = re.sub(r"[^\w\s]", " ", testo, flags=re.U).strip().lower()
        return pulito in ("missione",)
    return False


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

    from verifica_recap import valida, valida_missione  # unica fonte di verita' della forma

    problemi = []
    problemi_battito = []
    problemi_missione = []

    # INNESCO — Max ha chiesto `Missione`? Allora una Missione e' DOVUTA, e la sua assenza
    # e' un guasto come lo e' una forma sbagliata. (2026-09-10, vedi missione_richiesta)
    if missione_richiesta(percorso):
        if not any(trova_missione(t)[1] is not None for t in messaggi):
            problemi_missione.append(
                "Max ha scritto `Missione` e questo messaggio non ne porta nessuna. "
                "Missione non e' una domanda sullo stato: e' un comando con uno schema "
                "fisso (§6.11 del libro), marcato 🔴 e mai 🟩, in cima al messaggio. "
                "Costruiscila con verifica_recap.costruisci_missione(sto_facendo, "
                "obiettivo, fasi) — mai a mano — e rispondi con quella."
            )

    for testo in messaggi:
        inizio, blocco, dentro_fence = trova_battito(testo)
        if blocco is not None:
            guai = []
            if dentro_fence:
                guai.append(
                    "il battito e' dentro un blocco di codice ``` — VIETATO dal 7º giro "
                    "(§6.11): nel renderer di Max un blocco di codice e' un widget blu con "
                    "pulsante copia, non testo semplice, e Max l'ha bocciato. Il battito ora "
                    "sono bullet semplici (`🟩 **<Etichetta>:** <contenuto>`) scritti in "
                    "chiaro, MAI dentro ```. Togli il fence."
                )
            guai.extend(valida(blocco))

            # La posizione e' parte della regola (§6.11: il battito va IN CIMA) e si giudica
            # DENTRO il messaggio che lo contiene — mai sulla somma del turno (vedi la nota in
            # blocchi_testo_del_turno: quella confusione bloccava messaggi corretti).
            prima = "\n".join(testo.split("\n")[:inizio]).strip()
            if prima:
                guai = ["il battito non e' in cima al messaggio: prima di esso ci sono gia' "
                        "%d caratteri di testo (§6.11 -- mai in fondo, mai dopo l'analisi)"
                        % len(prima)] + guai

            problemi.extend(guai)
            problemi_battito.extend(guai)
            continue  # un messaggio porta un battito O una Missione, mai tutti e due

        inizio_m, blocco_m, dentro_fence_m = trova_missione(testo)
        if blocco_m is None:
            continue  # questo messaggio non porta ne' un battito ne' una Missione

        guai_m = []
        if dentro_fence_m:
            guai_m.append(
                "la Missione e' dentro un blocco di codice ``` — vietato per lo stesso "
                "motivo del battito (§6.11): niente widget blu copiabile. Scrivila in "
                "chiaro, MAI dentro ```."
            )
        guai_m.extend(valida_missione(blocco_m))

        prima_m = "\n".join(testo.split("\n")[:inizio_m]).strip()
        if prima_m:
            guai_m = ["la Missione non e' in cima al messaggio: prima di essa ci sono gia' "
                      "%d caratteri di testo" % len(prima_m)] + guai_m

        problemi.extend(guai_m)
        problemi_missione.extend(guai_m)

    if not problemi:
        return 0

    # L'esempio e' un extra per rendere il messaggio di blocco piu' chiaro: se la sua
    # generazione fallisce, il BLOCCO VERO (deciso sopra, basato su `problemi`) non deve
    # sparire con lui — lezione pagata il 2026-09-09 (un placeholder troppo lungo aveva
    # spento il gate intero attraverso la PROTEZIONE 3). Isolato in un try proprio.
    istruzioni = []
    if problemi_battito:
        esempio = ""
        try:
            from verifica_recap import costruisci  # stesso principio: una sola fonte di verita'
            esempio = "\n\nEsempio di forma (valori segnaposto):\n\n" + costruisci(
                "<una frase libera>", "<una frase libera>", "<una frase libera>",
                "nessuna, sto lavorando da solo",
                "normale", 100, 0,
            )
        except Exception:
            pass
        istruzioni.append(
            "BATTITO — riscrivilo nella forma fissa (emperator.md 6.11, 8º giro) — bullet "
            "semplici, NIENTE centraggio: titolo in chiaro, riga vuota, poi `🟩 **<Etichetta>:** "
            "<contenuto libero>` con una riga vuota dopo ognuno (Fatto, Sto facendo, Farò, "
            "Forze, Assetto, Potere). MAI dentro un blocco di codice ```, MAI in tabella. Unica "
            "eccezione: Forze con più unità nominate resta ad ALBERO (`🟩 **Forze:**` da sola, "
            "poi `🟩 <NOME>` / `│` / `├─🟩→`/`└─🟩→`). Non disegnarlo a mano: chiama "
            "`verifica_recap.costruisci(...)` con i sei valori." + esempio
        )
    if problemi_missione:
        esempio_m = ""
        try:
            from verifica_recap import costruisci_missione
            esempio_m = "\n\nEsempio di forma (valori segnaposto):\n\n" + costruisci_missione(
                "<l'azione concreta di questo momento>",
                "<perché lo sto facendo, cosa vuol dire finito>",
                ["<fase 1>", "<fase 2>"],
            )
        except Exception:
            pass
        istruzioni.append(
            "MISSIONE — riscrivila nella forma fissa (emperator.md 6.11): `🔴 **Sto "
            "facendo:** <contenuto>`, poi `🔴 **Obiettivo:** <contenuto>`, poi `🔴 Fasi:` "
            "da sola, poi `│`, poi una fase per riga `├─🔴→ <fase>` (l'ultima `└─🔴→`). "
            "Nessuna riga vuota in mezzo, MAI dentro un blocco di codice ```. Non "
            "disegnarla a mano: chiama `verifica_recap.costruisci_missione(...)`."
            + esempio_m
        )

    motivo = (
        "GATE BATTITO — la forma non torna, il messaggio non parte cosi'.\n\n"
        + "\n".join("  - " + p for p in problemi)
        + "\n\n" + "\n\n".join(istruzioni)
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
