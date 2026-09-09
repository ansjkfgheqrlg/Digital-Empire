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

FORMA A BLOCCHI CENTRATI, DENTRO UN BLOCCO DI CODICE (2026-09-09, ordine di Max — solo
estetica, il contenuto delle sei voci non cambia). Storia dei tentativi, in ordine — tenuta
per intero perche' ogni giro ha smentito un'ipotesi tecnica plausibile che sembrava corretta:

  1º giro — riquadri con bordo (┌─┐/│/└─┘) aperti a destra. Bocciato: Max li voleva chiusi
     e centrati ("i quadratini devono essere al centro... completamente chiusi").
  2º giro — riquadri chiusi, centrati con rientro a spazi ASCII, fuori da un blocco di
     codice (si credeva, allora, che dentro un blocco di codice il battito sparisse dal
     controllo del gate — vedi 6º giro, era vero ma la soluzione era un'altra). Bocciato di
     nuovo sulla stessa base (visto su un'altra sessione, EMP-LAN1): la regola non bastava.
  3º giro — ipotesi: gli spazi ASCII ripetuti collassano nel rendering fuori da un blocco
     di codice, l'NBSP no (stesso trucco di `&nbsp;` in HTML). Sbagliata: la NBSP e'
     whitespace quanto lo spazio ASCII, questo renderer non fa distinzioni.
  4º giro — diagnosi tecnica corretta ma soluzione poi abbandonata: non conta il TIPO di
     carattere di spaziatura, conta la RIPETIZIONE — un carattere isolato sopravvive, un
     TRATTO di 2+ dello stesso carattere collassa sempre, fuori da un blocco di codice.
     Soluzione di allora: PUNTO (`·`) per ogni tratto di 2+ caratteri strutturali.
  5º giro — il 4º giro RENDEVA bene (centrato per davvero) ma Max ha bocciato l'ESTETICA:
     i puntini si vedono, "che schifo". Tolto anche il bordo (non serviva). Aggiunto pero'
     il formato AD ALBERO per la voce Forze quando ci sono più unità nominate (sentinelle,
     doom bot, ecc.) — mostrato da Max con un esempio scritto a mano: `🟠 <NOME>`, poi `│`,
     poi `├─🟠→ <voce>` per ognuna tranne l'ultima che è `└─🟠→ <voce>`. Questo pezzo resta.
  6º giro — la svolta. Il vero motivo per cui gli spazi ripetuti sparivano non era "dentro
     o fuori da un blocco di codice" in astratto: era che il TESTO CHE SCRIVO IO passa da
     un motore che collassa gli spazi ripetuti in prosa normale, mentre un blocco di codice
     li preserva ESATTI — la stessa ragione per cui l'esempio scritto a mano da MAX (fuori
     da qualunque controllo mio) si leggeva perfetto: lui non passa dallo stesso motore.
     Max ha scelto esplicitamente: dentro un blocco di codice, spazi veri. Il divieto dei
     giri 2-5 ("mai dentro un blocco ```") è ABROGATO: ora e' l'opposto, il battito vero
     DEVE stare dentro un blocco di codice, altrimenti gli spazi non reggono. Il bordo non
     torna (il 5º giro l'aveva tolto per altre ragioni, restano valide); il riempimento
     torna a essere SPAZIO VERO, non piu' `·` (dentro un blocco di codice lo spazio non
     collassa, il punto non serve più).

**RIGHE CORTE, SEMPRE.** Una riga di contenuto troppo lunga puo' comunque risultare scomoda
da leggere o forzare uno scroll orizzontale. `LARGHEZZA_MASSIMA_RIGA` (44 caratteri) resta il
tetto duro: `costruisci()` rifiuta di generare una voce che lo sfora (eccezione, non una riga
silenziosamente troppo lunga) e `valida()` lo controlla comunque, per un battito scritto a
mano.

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

# Le cinque voci, in ordine fisso (emperator.md §6.11). Il secondo/terzo elemento e' il
# numero di righe di contenuto ammesse (min, max) in forma PIATTA — "MAX quattro frasi" per
# le prime quattro (ordine di Max, 2026-09-09); Assetto+Potere ne ha sempre esattamente due.
# Forze puo' anche essere in forma AD ALBERO (vedi _albero_forze / _leggi_albero_forze):
# in quel caso min/max non si applicano alle righe piatte, si applica la grammatica ad albero.
VOCI = [
    ("Fatto", 1, 4),
    ("Sto facendo", 1, 4),
    ("Farò", 1, 4),
    ("Forze", 1, 4),
    ("Assetto", 2, 2),
]

LARGHEZZA_MASSIMA_RIGA = 44  # caratteri per riga di contenuto — vedi nota "RIGHE CORTE"

# Riempimento strutturale: spazio vero (6º giro, dentro un blocco di codice non collassa).
# Restano tollerati in lettura NBSP e punto medio: un battito scritto a mano prima di
# questa regola (o da un’altra sessione non ancora sincronizzata) puo’ ancora averli.
_RIENTRO_CHARS = "  ·"

TITOLO_RE = re.compile(r"^\*\*⏱️ RECAP — (\d{1,3})%\*\*$")
FRECCIA = "↓"
ASSETTO_RE = re.compile(r"^(\*\*GOD EMPEROR DOOM\*\*|normale)$")
POTERE_RE = re.compile(r"^🟠 Potere: (\d{1,3})%$")
RAMO_RE = re.compile(r"^(├─🟠→|└─🟠→) (.+)$")
GRUPPO_RE = re.compile(r"^🟠 (.+)$")


def _leggi_stdin():
    grezzo = sys.stdin.buffer.read()
    return grezzo.decode("utf-8", "replace")


def _rientro(riga):
    return len(riga) - len(riga.lstrip(_RIENTRO_CHARS))


def _spoglia(riga):
    return riga.lstrip(_RIENTRO_CHARS)


def _e_gruppi_forze(v):
    """True se `v` e' una lista di gruppi [(nome, [voce, ...]), ...] invece di righe piatte
    — il formato ad albero per Forze quando ci sono più unità nominate (5º giro)."""
    return isinstance(v, list) and len(v) > 0 and all(
        isinstance(x, tuple) and len(x) == 2 and isinstance(x[0], str) and isinstance(x[1], list)
        for x in v
    )


def _albero_forze(gruppi):
    """Genera le righe (piatte, senza rientro) dell'albero Forze da una lista di gruppi
    [(nome, [voce, ...]), ...]. `None` = riga vuota VERA fra un gruppo e l'altro (mai
    rientrata a punti: una riga vuota vera non collassa, non e' un tratto di spaziatura
    dentro una riga)."""
    righe = []
    for i, (nome, voci) in enumerate(gruppi):
        if not voci:
            raise ValueError("gruppo Forze '%s': nessuna voce" % nome)
        righe.append("🟠 %s" % nome.upper())
        righe.append("│")
        for j, v in enumerate(voci):
            ramo = "└─🟠→" if j == len(voci) - 1 else "├─🟠→"
            righe.append("%s %s" % (ramo, v))
        if i < len(gruppi) - 1:
            righe.append(None)
    return righe


def _leggi_albero_forze(righe, idx, problemi):
    """Legge un albero Forze a partire da `idx` (che deve puntare alla prima etichetta di
    gruppo `🟠 <NOME>`). Ritorna l'indice subito dopo l'ultimo ramo `└─...` (o dopo l'ultima
    riga vuota fra gruppi, se il testo continua con un altro gruppo).

    Non prova a indovinare quanti gruppi ci sono: continua finche' vede altre etichette di
    gruppo dopo una riga vuota, si ferma alla prima riga che non e' ne' vuota ne' un'altra
    etichetta di gruppo (tipicamente la freccia verso la voce successiva).
    """
    rientro_atteso = None
    while idx < len(righe):
        spoglia = _spoglia(righe[idx])
        if not GRUPPO_RE.match(spoglia) or spoglia == FRECCIA:
            break
        if rientro_atteso is None:
            rientro_atteso = _rientro(righe[idx])
        elif _rientro(righe[idx]) != rientro_atteso:
            problemi.append(
                "riga %d: rientro diverso dal resto dell'albero Forze — dev'essere lo "
                "stesso su ogni riga del blocco" % (idx + 1)
            )
        idx += 1  # etichetta di gruppo

        if idx >= len(righe) or _spoglia(righe[idx]) != "│":
            problemi.append(
                "riga %d: dopo l'etichetta di un gruppo Forze serve la riga `│` da sola"
                % (idx + 1)
            )
        else:
            idx += 1

        rami = []
        while idx < len(righe):
            spoglia = _spoglia(righe[idx])
            m = RAMO_RE.match(spoglia)
            if not m:
                break
            rami.append((idx, m.group(1), m.group(2)))
            idx += 1

        if not rami:
            problemi.append("gruppo Forze: nessuna voce sotto `│` (serve almeno un ramo)")
        else:
            for riga_num, simbolo, voce in rami[:-1]:
                if simbolo != "├─🟠→":
                    problemi.append(
                        "riga %d: ramo non finale dev'essere `├─🟠→`, trovato `%s`"
                        % (riga_num + 1, simbolo)
                    )
            ultimo_num, ultimo_simbolo, _ = rami[-1]
            if ultimo_simbolo != "└─🟠→":
                problemi.append(
                    "riga %d: l'ultimo ramo del gruppo dev'essere `└─🟠→`, trovato `%s`"
                    % (ultimo_num + 1, ultimo_simbolo)
                )
            for riga_num, _, voce in rami:
                if len(voce) > LARGHEZZA_MASSIMA_RIGA:
                    problemi.append(
                        "riga %d: voce lunga %d caratteri, il tetto e' %d — accorciala"
                        % (riga_num + 1, len(voce), LARGHEZZA_MASSIMA_RIGA)
                    )

        # riga vuota VERA fra un gruppo e il successivo (mai rientrata)
        if idx < len(righe) and righe[idx] == "":
            idx += 1
            continue
        break

    return idx


def _leggi_voce_piatta(righe, idx, etichetta, min_righe, max_righe, problemi):
    """Legge una voce in forma piatta: etichetta + 1..N righe di contenuto, tutte con lo
    stesso rientro. Ritorna l'indice subito dopo l'ultima riga di contenuto."""
    attesa = "🟠 %s:" % etichetta
    if idx >= len(righe) or _spoglia(righe[idx]) != attesa:
        problemi.append(
            "riga %d: attesa l'etichetta `%s`, trovato: %r"
            % (idx + 1, attesa, righe[idx] if idx < len(righe) else "<fine testo>")
        )
        return idx + 1
    rientro_voce = _rientro(righe[idx])
    idx += 1

    contenuto = []
    while idx < len(righe):
        spoglia = _spoglia(righe[idx])
        if spoglia == FRECCIA or spoglia == "":
            break
        contenuto.append((idx, spoglia))
        idx += 1

    if len(contenuto) < min_righe:
        problemi.append(
            "voce '%s': servono almeno %d riga/e di contenuto, trovate %d"
            % (etichetta, min_righe, len(contenuto))
        )
    if len(contenuto) > max_righe:
        problemi.append(
            "voce '%s': massimo %d riga/e di contenuto, trovate %d — accorcia"
            % (etichetta, max_righe, len(contenuto))
        )
    for riga_num, valore in contenuto:
        if _rientro(righe[riga_num]) != rientro_voce:
            problemi.append(
                "riga %d: rientro diverso dall'etichetta della voce '%s' — dev'essere lo "
                "stesso rientro su ogni riga della voce" % (riga_num + 1, etichetta)
            )
        if not valore.strip():
            problemi.append("riga %d: riga della voce '%s' vuota" % (riga_num + 1, etichetta))
        elif "**" in valore and valore.strip() != "**GOD EMPEROR DOOM**":
            problemi.append(
                "riga %d: il contenuto della voce '%s' non va in grassetto (eccezione unica: "
                "`**GOD EMPEROR DOOM**` nella voce Assetto)" % (riga_num + 1, etichetta)
            )
        if len(valore) > LARGHEZZA_MASSIMA_RIGA:
            problemi.append(
                "riga %d: riga della voce '%s' lunga %d caratteri, il tetto e' %d — accorciala"
                % (riga_num + 1, etichetta, len(valore), LARGHEZZA_MASSIMA_RIGA)
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

    return idx


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
            "in grassetto da solo, allineato a sinistra, trovato: %r" % (riga_num, righe[idx])
        )
    else:
        n = int(m.group(1))
        if n > 100:
            problemi.append("riga %d: percentuale %d%% impossibile (>100)" % (riga_num, n))
    idx += 1

    if idx >= len(righe) or righe[idx].strip() != "":
        problemi.append("riga %d: manca la riga vuota fra il titolo e la prima voce" % (idx + 1))
    else:
        idx += 1

    for i, (etichetta, mn, mx) in enumerate(VOCI):
        if etichetta == "Forze":
            attesa = "🟠 Forze:"
            if idx >= len(righe) or _spoglia(righe[idx]) != attesa:
                problemi.append(
                    "riga %d: attesa l'etichetta `%s`, trovato: %r"
                    % (idx + 1, attesa, righe[idx] if idx < len(righe) else "<fine testo>")
                )
                idx += 1
            else:
                idx += 1
                # dopo l'etichetta: o e' un albero (la riga dopo e' un'altra etichetta
                # `🟠 <NOME>`, non la freccia) o e' testo piatto — si decide guardando la
                # riga successiva, senza consumarla.
                if idx < len(righe) and GRUPPO_RE.match(_spoglia(righe[idx])) and _spoglia(righe[idx]) != FRECCIA:
                    idx = _leggi_albero_forze(righe, idx, problemi)
                else:
                    # forma piatta: stesso schema delle altre voci, ma l'etichetta e'
                    # gia' stata consumata sopra — si legge solo il contenuto qui.
                    rientro_voce = None
                    contenuto = []
                    while idx < len(righe):
                        spoglia = _spoglia(righe[idx])
                        if spoglia == FRECCIA or spoglia == "":
                            break
                        if rientro_voce is None:
                            rientro_voce = _rientro(righe[idx])
                        contenuto.append((idx, spoglia))
                        idx += 1
                    if len(contenuto) < mn:
                        problemi.append(
                            "voce 'Forze': servono almeno %d riga/e di contenuto, trovate %d"
                            % (mn, len(contenuto))
                        )
                    if len(contenuto) > mx:
                        problemi.append(
                            "voce 'Forze': massimo %d riga/e di contenuto, trovate %d — accorcia"
                            % (mx, len(contenuto))
                        )
                    for riga_num, valore in contenuto:
                        if len(valore) > LARGHEZZA_MASSIMA_RIGA:
                            problemi.append(
                                "riga %d: riga della voce 'Forze' lunga %d caratteri, il "
                                "tetto e' %d — accorciala" % (riga_num + 1, len(valore), LARGHEZZA_MASSIMA_RIGA)
                            )
        else:
            idx = _leggi_voce_piatta(righe, idx, etichetta, mn, mx, problemi)

        e_ultima = i == len(VOCI) - 1
        if not e_ultima:
            if idx >= len(righe) or righe[idx].strip(_RIENTRO_CHARS) != FRECCIA:
                problemi.append(
                    "riga %d: manca la freccia `%s` su riga propria fra le voci '%s' e '%s'"
                    % (idx + 1, FRECCIA, etichetta, VOCI[i + 1][0])
                )
            else:
                idx += 1

    if idx < len(righe) and righe[idx].strip() != "":
        problemi.append(
            "riga %d: contenuto extra dopo l'ultima voce (%r) — il battito finisce con "
            "la riga del Potere" % (idx + 1, righe[idx])
        )

    return problemi


def costruisci(fatto, sto_facendo, farò, forze, assetto, potere, percentuale):
    """Genera il testo del battito a partire dai valori — cosi' non si disegna a mano
    (stesso principio di frantuma.py). Ogni argomento voce e' una stringa o una lista di
    1-4 righe; `assetto` e' "normale" oppure "GOD EMPEROR DOOM" (senza asterischi, li
    aggiunge la funzione).

    `forze` accetta anche una lista di GRUPPI — [(nome_gruppo, [voce, voce, ...]), ...] —
    per il formato ad albero quando Forze ha più unità nominate (5º giro, esempio di Max:
    sentinelle/doom bot). Con una lista di stringhe semplici resta la forma piatta.

    Ogni voce e' un blocco: etichetta `🟠 <Nome>:` + le sue righe, tutte con LO STESSO
    rientro — calcolato dalla larghezza del blocco stesso, centrato su un "canvas" comune
    (largo quanto il blocco piu' largo di tutto il battito), cosi' i blocchi piu' stretti
    appaiono centrati invece che accostati a sinistra. Frecce `↓` fra un blocco e il
    successivo, centrate sullo stesso asse. NESSUN bordo (niente `┌│└─┐┘`): non serve e non
    regge nel rendering di Max (5º giro) — il rientro a `·` da solo centra tutto."""
    def _righe(v):
        return v if isinstance(v, list) else [v]

    blocchi = [
        ("Fatto", _righe(fatto)),
        ("Sto facendo", _righe(sto_facendo)),
        ("Farò", _righe(farò)),
    ]

    if _e_gruppi_forze(forze):
        blocchi.append(("Forze", _albero_forze(forze)))
    else:
        blocchi.append(("Forze", _righe(forze)))

    blocchi.append(("Assetto", [
        "**GOD EMPEROR DOOM**" if assetto == "GOD EMPEROR DOOM" else "normale",
        "🟠 Potere: %d%%" % potere,
    ]))

    for etichetta, righe in blocchi:
        for r in righe:
            if r is not None and len(r) > LARGHEZZA_MASSIMA_RIGA:
                raise ValueError(
                    "voce '%s': riga di %d caratteri sfora il tetto di %d — accorciala: %r"
                    % (etichetta, len(r), LARGHEZZA_MASSIMA_RIGA, r)
                )

    render = []
    for etichetta, righe in blocchi:
        linee = ["🟠 %s:" % etichetta] + righe
        larghezza = max(len(l) for l in linee if l is not None)
        render.append((linee, larghezza))

    canvas = max(larghezza for _, larghezza in render)

    out = ["**⏱️ RECAP — %d%%**" % percentuale, ""]
    for i, (linee, larghezza) in enumerate(render):
        rientro = (canvas - larghezza) // 2
        for l in linee:
            out.append("" if l is None else " " * rientro + l)
        if i < len(render) - 1:
            out.append(" " * (canvas // 2) + FRECCIA)
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
