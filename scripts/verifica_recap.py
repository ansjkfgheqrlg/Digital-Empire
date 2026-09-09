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
uniti da una freccia `↓` su riga propria.

**Chiusi e centrati** (correzione di Max, 2026-09-09, sul primo giro — il primo tentativo
aveva i riquadri aperti a destra: sbagliato, Max li vuole un rettangolo vero). `costruisci()`
misura ogni riquadro (larghezza = riga di contenuto piu' lunga, incluso `🟠 <Etichetta>`),
poi li chiude tutti e quattro i lati (`┌─...─┐` / `│ testo │` / `└─...─┘`), e li rientra
tutti sullo stesso "canvas" — largo quanto il riquadro piu' largo — cosi' ogni riquadro piu'
stretto risulta centrato rispetto agli altri invece che accostato a sinistra. Le frecce `↓`
fra un riquadro e il successivo stanno sullo stesso asse centrale del canvas, non a colonna 0.
Un riquadro rimane comunque piu' stretto del canvas quando il suo contenuto e' piu' corto:
e' voluto, e' quello che lo fa apparire centrato invece che a tutta larghezza.

**MAI DENTRO UN BLOCCO ``` (2026-09-09, secondo giro di correzione).** Uno screenshot
mandato da Max — battito con riquadri gia' chiusi/centrati, ma renderizzato a pezzi, testo
che esce dal bordo, freccia storta — ha mostrato il guasto vero: il battito era dentro un
blocco di codice. Un blocco ``` (a) e' "il formato apposta per copiare" (parole di Max): non
e' come si consegna un rapporto, e (b) SPARISCE dal controllo del gate — `righe_reali` in
gate_battito_hook.py lo esclude apposta, cosi' un ESEMPIO di battito dentro la dottrina non
blocca la consegna quando ne parlo con Max. Se il battito VERO finisce per errore dentro un
blocco di codice, il gate non lo vede: non lo blocca, ma non lo valida nemmeno — passa senza
controllo, ed e' esattamente il buco che ha lasciato passare quel battito storto. Il battito
vero e' SEMPRE testo semplice, mai fra ```. `gate_battito_hook.py` ora rileva anche il caso
"tutto il messaggio e' un unico blocco di codice che contiene un battito" e lo blocca con un
motivo dedicato, invece di lasciarlo passare come se fosse solo un esempio di dottrina.

**RIGHE CORTE, SEMPRE (stesso giro).** Una riga di contenuto troppo lunga si spezza da sola
quando lo spazio dove Max legge e' piu' stretto della riga — e un rettangolo con una riga
spezzata non e' piu' un rettangolo, indipendentemente da quanto sia giusta la matematica del
centraggio. `LARGHEZZA_MASSIMA_RIGA` (44 caratteri) e' il tetto duro per ogni riga di
contenuto: `costruisci()` rifiuta di generare un riquadro che lo sfora (eccezione, non un
riquadro storto silenzioso) e `valida()` lo controlla comunque, per i battiti scritti a mano.

**SPAZI VERI, NON SPAZI ASCII (2026-09-09, terzo giro — quello decisivo).** Max ha guardato
il battito VERO che avevo appena mandato (non un altro screenshot: il mio) e ha detto la cosa
che serviva: *"tu li fai tutti verso il lato di sinistra"* — il centraggio che il codice
calcolava (rientro a spazi ASCII prima di `┌`) non arrivava sullo schermo. Causa tecnica: i
renderer markdown collassano le sequenze di spazi ASCII normali in prosa non-fenced (regola
CommonMark/HTML standard) — il rientro veniva scritto correttamente nella stringa, ma
spariva o si accorciava in modo incoerente da un riquadro all'altro nel momento in cui Max
lo leggeva, e quello e' anche il motivo delle "linee sfalsate, messe a caso": ogni riga
collassava un numero diverso di spazi. Lo spazio non-interrompibile (` `, NBSP) NON
collassa — e' cosi' che l'HTML preserva spaziature multiple (`&nbsp;` e' lo stesso trucco).
Da questo giro, OGNI spazio strutturale del battito — il rientro di centraggio, il margine
dentro i riquadri fra `│` e il testo, l'indentazione della freccia — e' NBSP, mai spazio
ASCII. Solo gli spazi FRA LE PAROLE dentro le frasi restano ASCII normali (li' va bene che
si comportino da spazi qualunque). `valida()` accetta entrambi in lettura (compatibilita'
con un battito scritto a mano con spazi normali), ma `costruisci()` da ora genera solo NBSP
per la struttura.

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

LARGHEZZA_MASSIMA_RIGA = 44  # caratteri per riga di contenuto (non il bordo) — vedi nota sopra

NBSP = " "  # spazio non-interrompibile: non collassa nel rendering, a differenza di " "
_SP = "  "  # entrambi accettati in lettura (vedi nota "SPAZI VERI" sopra)

TITOLO_RE = re.compile(r"^\*\*⏱️ RECAP — (\d{1,3})%\*\*$")
TOP_RE = re.compile(r"^┌─+┐$")
BOTTOM_RE = re.compile(r"^└─+┘$")
RIGA_RE = re.compile(r"^│[  ](.*?)[  ]*│$")
FRECCIA = "↓"
ASSETTO_RE = re.compile(r"^(\*\*GOD EMPEROR DOOM\*\*|normale)$")
POTERE_RE = re.compile(r"^🟠 Potere: (\d{1,3})%$")


def _leggi_stdin():
    grezzo = sys.stdin.buffer.read()
    return grezzo.decode("utf-8", "replace")


def _riquadro(righe, idx, etichetta, min_righe, max_righe, problemi):
    """Legge un riquadro a partire da `idx` (che deve puntare al bordo superiore).

    Tollera un rientro qualunque (il centraggio in `costruisci`) purche' sia LO STESSO
    su ogni riga del riquadro — un rettangolo chiuso non puo' avere lati storti. Ritorna
    l'indice subito dopo il bordo inferiore. Non solleva mai — accumula i problemi e
    prova comunque a ripartire dalla riga successiva, cosi' un solo riquadro rotto non
    nasconde gli errori di quelli dopo.
    """
    def _rientro(riga):
        # senza argomenti: strippa QUALUNQUE whitespace, spazio ASCII o NBSP (entrambi
        # accettati in lettura, vedi nota "SPAZI VERI" — `costruisci()` scrive solo NBSP).
        return len(riga) - len(riga.lstrip())

    if idx >= len(righe) or not TOP_RE.match(righe[idx].lstrip()):
        problemi.append(
            "riga %d: atteso il bordo superiore del riquadro '%s' (`┌─...─┐`), trovato: %r"
            % (idx + 1, etichetta, righe[idx] if idx < len(righe) else "<fine testo>")
        )
        return idx + 1
    rientro_box = _rientro(righe[idx])
    larghezza_box = len(righe[idx].lstrip())
    idx += 1

    if idx >= len(righe):
        problemi.append("riquadro '%s': troncato subito dopo il bordo superiore" % etichetta)
        return idx

    m = RIGA_RE.match(righe[idx].lstrip())
    if not m or m.group(1) != "🟠 %s" % etichetta:
        problemi.append(
            "riga %d: attesa l'etichetta `🟠 %s` dentro il riquadro, trovato: %r"
            % (idx + 1, etichetta, righe[idx])
        )
    else:
        idx += 1

    contenuto = []
    while idx < len(righe):
        spoglia = righe[idx].lstrip()
        if BOTTOM_RE.match(spoglia):
            break
        m = RIGA_RE.match(spoglia)
        if not m:
            break
        contenuto.append((idx, m.group(1)))
        idx += 1

    for riga_num, _ in contenuto:
        if _rientro(righe[riga_num]) != rientro_box:
            problemi.append(
                "riga %d: rientro diverso dal resto del riquadro '%s' — il rettangolo "
                "e' storto, dev'essere lo stesso rientro su ogni riga" % (riga_num + 1, etichetta)
            )
        if len(righe[riga_num].rstrip("\n")) != larghezza_box + rientro_box:
            problemi.append(
                "riga %d: il riquadro '%s' non e' chiuso — questa riga non arriva al bordo "
                "destro `│` alla stessa colonna del bordo superiore" % (riga_num + 1, etichetta)
            )

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
        if len(valore) > LARGHEZZA_MASSIMA_RIGA:
            problemi.append(
                "riga %d: riga del riquadro '%s' lunga %d caratteri, il tetto e' %d — "
                "una riga troppo lunga si spezza da sola nello spazio dove Max legge e rompe "
                "il rettangolo, accorciala" % (riga_num + 1, etichetta, len(valore), LARGHEZZA_MASSIMA_RIGA)
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

    if idx >= len(righe) or not BOTTOM_RE.match(righe[idx].lstrip()):
        problemi.append(
            "riga %d: atteso il bordo inferiore del riquadro '%s' (`└─...─┘`), trovato: %r"
            % (idx + 1, etichetta, righe[idx] if idx < len(righe) else "<fine testo>")
        )
        return idx + 1
    if _rientro(righe[idx]) != rientro_box or len(righe[idx].lstrip()) != larghezza_box:
        problemi.append(
            "riga %d: il bordo inferiore del riquadro '%s' non e' allineato al bordo "
            "superiore — stesso rientro, stessa larghezza" % (idx + 1, etichetta)
        )
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
    "normale" oppure "GOD EMPEROR DOOM" (senza asterischi, li aggiunge la funzione).

    I riquadri escono CHIUSI su tutti e quattro i lati e CENTRATI su un asse comune —
    largo quanto il riquadro piu' largo (`canvas`) — cosi' quelli piu' stretti non
    restano accostati a sinistra. Le frecce fra un riquadro e il successivo stanno
    sullo stesso asse centrale, non a colonna 0 (ordine di Max, 2026-09-09, corretto
    dopo un primo giro con riquadri aperti a destra e frecce a sinistra: sbagliato)."""
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

    # 1a passata: ogni riquadro chiuso alla sua larghezza naturale, senza rientro.
    riquadri = []
    for etichetta, righe in blocchi:
        for r in righe:
            if len(r) > LARGHEZZA_MASSIMA_RIGA:
                raise ValueError(
                    "riquadro '%s': riga di %d caratteri sfora il tetto di %d — accorciala "
                    "(una riga troppo lunga si spezza da sola e rompe il rettangolo): %r"
                    % (etichetta, len(r), LARGHEZZA_MASSIMA_RIGA, r)
                )
        contenuto = ["🟠 %s" % etichetta] + righe
        interno = max(len(r) for r in contenuto) + 2  # 1 NBSP di margine per lato
        righe_box = ["┌" + "─" * interno + "┐"]
        for r in contenuto:
            # NBSP, non spazio ASCII: il margine e il riempimento sono struttura, non
            # prosa — devono arrivare intatti sullo schermo (vedi nota "SPAZI VERI" sopra).
            righe_box.append("│" + NBSP + r.ljust(interno - 2, NBSP) + NBSP + "│")
        righe_box.append("└" + "─" * interno + "┘")
        riquadri.append((righe_box, interno + 2))  # +2 = i due caratteri │/┌└┐┘

    canvas = max(larghezza for _, larghezza in riquadri)

    out = ["**⏱️ RECAP — %d%%**" % percentuale, ""]
    for i, (righe_box, larghezza) in enumerate(riquadri):
        rientro = (canvas - larghezza) // 2
        for r in righe_box:
            out.append(NBSP * rientro + r)
        if i < len(riquadri) - 1:
            out.append(NBSP * (canvas // 2) + FRECCIA)
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
