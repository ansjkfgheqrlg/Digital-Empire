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

FORMA A TABELLA MARKDOWN CENTRATA, FUORI DA QUALSIASI BLOCCO DI CODICE (2026-09-09, 7º giro
— solo estetica, il contenuto delle sei voci non cambia). Storia dei tentativi, in ordine —
tenuta per intero perche' ogni giro ha smentito un'ipotesi tecnica plausibile che sembrava
corretta:

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
  6º giro — il TESTO CHE SCRIVO IO passa da un motore che collassa gli spazi ripetuti in
     prosa normale, mentre un blocco di codice li preserva ESATTI. Soluzione di allora:
     spazio vero, ma dentro un blocco ```. FUNZIONAVA per il centraggio, ma introduceva un
     difetto nuovo che nessuno aveva ancora visto — vedi 7º giro.
  7º giro — Max ha mandato lo screenshot del battito dentro ```: nel suo renderer (VSCode)
     un blocco di codice non è testo semplice, è un WIDGET — sfondo/testo colorati diversi
     dal resto della chat (blu/ciano), pulsante "copia" in alto a destra, e il contenuto
     resta comunque allineato a SINISTRA dentro quel widget (il centraggio a spazi funziona
     sull'ASSE ma il widget stesso non è "la pagina", è un rettangolo a sé). Max l'ha
     bocciato in una riga: *"non deve mai essere con quel formato da copiare e tutto di
     colori azzurri... dev'essere tutto centrato"*. Il blocco di codice risolveva il
     problema degli spazi che si mangiava il rendering, ma ne creava uno peggiore (l'aspetto
     del messaggio) — un'AGGIUNTA che sembrava solo tecnica aveva in realtà un costo
     estetico che nessuno aveva verificato guardando lo schermo vero. **Soluzione nuova, non
     un'altra variante della stessa idea**: una TABELLA markdown (GFM) a una colonna, con
     l'allineamento dichiarato nel separatore (`|:---:|` = centrato). Il centraggio lo fa il
     RENDERER via CSS `text-align:center`, non più un conteggio di spazi mio — quindi è
     immune al difetto dei giri 2-6 (il motore che collassa gli spazi ripetuti non tocca
     l'allineamento delle celle, che è una proprietà della tabella, non dello spazio bianco)
     — e una tabella non è un blocco di codice: nessun widget blu, nessun pulsante copia.
     Il titolo (`**⏱️ RECAP — <n>%**`) resta FUORI dalla tabella, testo semplice: è l'unica
     riga che deve restare a sinistra (regola 1 sotto), e fuori dalla tabella lo è
     naturalmente, senza bisogno di alcun trucco. **Lezione:** una tecnica che risolve il
     sintomo che sto guardando (gli spazi) può introdurre un difetto in una dimensione che
     non stavo controllando (l'aspetto del contenitore) — verificare vuol dire guardare TUTTO
     lo schermo, non solo la riga che stavo correggendo.

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

TITOLO_RE = re.compile(r"^\*\*⏱️ RECAP — (\d{1,3})%\*\*$")
FRECCIA = "↓"
ASSETTO_RE = re.compile(r"^(\*\*GOD EMPEROR DOOM\*\*|normale)$")
POTERE_RE = re.compile(r"^🟠 Potere: (\d{1,3})%$")
RAMO_RE = re.compile(r"^(├─🟠→|└─🟠→) (.+)$")
GRUPPO_RE = re.compile(r"^🟠 (.+)$")

# La tabella: intestazione vuota, separatore centrato, poi una riga `| ... |` per cella
# (7º giro — vedi il docstring sopra per il perché).
RIGA_TABELLA_RE = re.compile(r"^\|(.*)\|$")
SEPARATORE_RE = re.compile(r"^\|\s*:?-{2,}:?\s*\|$")


def _leggi_stdin():
    grezzo = sys.stdin.buffer.read()
    return grezzo.decode("utf-8", "replace")


def _e_gruppi_forze(v):
    """True se `v` e' una lista di gruppi [(nome, [voce, ...]), ...] invece di righe piatte
    — il formato ad albero per Forze quando ci sono più unità nominate (5º giro)."""
    return isinstance(v, list) and len(v) > 0 and all(
        isinstance(x, tuple) and len(x) == 2 and isinstance(x[0], str) and isinstance(x[1], list)
        for x in v
    )


def _albero_forze(gruppi):
    """Genera le righe (piatte, senza rientro) dell'albero Forze da una lista di gruppi
    [(nome, [voce, ...]), ...]. `None` = separatore fra un gruppo e l'altro — diventa una
    cella vuota `| |` nella tabella (`costruisci()`), letta come cella vuota vera da
    `_leggi_albero_forze()`."""
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


def _leggi_albero_forze(celle, idx, problemi):
    """Legge un albero Forze a partire da `idx` (indice dentro `celle`, la lista di celle
    `(numero_riga, testo)` della tabella) — deve puntare alla prima etichetta di gruppo
    `🟠 <NOME>`. Ritorna l'indice subito dopo l'ultimo ramo `└─...` (o dopo l'ultima cella
    vuota fra gruppi, se la tabella continua con un altro gruppo).

    Non prova a indovinare quanti gruppi ci sono: continua finche' vede altre etichette di
    gruppo dopo una cella vuota, si ferma alla prima cella che non e' ne' vuota ne' un'altra
    etichetta di gruppo (tipicamente la freccia verso la voce successiva). Niente controllo
    di rientro: la tabella allinea da sola, non c'e' piu' niente da confrontare riga per riga
    (7º giro — l'intera classe di errori "rientro diverso" sparisce con lo spazio a mano).
    """
    while idx < len(celle):
        testo = celle[idx][1]
        if not GRUPPO_RE.match(testo) or testo == FRECCIA:
            break
        idx += 1  # etichetta di gruppo

        if idx >= len(celle) or celle[idx][1] != "│":
            problemi.append(
                "riga %d: dopo l'etichetta di un gruppo Forze serve una cella `| │ |` da sola"
                % ((celle[idx][0] + 1) if idx < len(celle) else (celle[-1][0] + 2))
            )
        else:
            idx += 1

        rami = []
        while idx < len(celle):
            testo2 = celle[idx][1]
            m = RAMO_RE.match(testo2)
            if not m:
                break
            rami.append((celle[idx][0], m.group(1), m.group(2)))
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

        # cella vuota VERA fra un gruppo e il successivo (riga `| |`, contenuto "")
        if idx < len(celle) and celle[idx][1] == "":
            idx += 1
            continue
        break

    return idx


def _leggi_voce_piatta(celle, idx, etichetta, min_righe, max_righe, problemi):
    """Legge una voce in forma piatta: cella-etichetta + 1..N celle di contenuto. Ritorna
    l'indice subito dopo l'ultima cella di contenuto."""
    attesa = "🟠 %s:" % etichetta
    if idx >= len(celle) or celle[idx][1] != attesa:
        problemi.append(
            "riga %s: attesa la cella `%s`, trovato: %r"
            % ((celle[idx][0] + 1) if idx < len(celle) else "<fine tabella>", attesa,
               celle[idx][1] if idx < len(celle) else "<fine tabella>")
        )
        return idx + 1
    idx += 1

    contenuto = []
    while idx < len(celle):
        testo = celle[idx][1]
        if testo == FRECCIA or testo == "":
            break
        contenuto.append(celle[idx])
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
        if not valore.strip():
            problemi.append("riga %d: cella della voce '%s' vuota" % (riga_num + 1, etichetta))
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
            "in grassetto da solo, allineato a sinistra, FUORI da qualunque tabella o "
            "blocco di codice, trovato: %r" % (riga_num, righe[idx])
        )
    else:
        n = int(m.group(1))
        if n > 100:
            problemi.append("riga %d: percentuale %d%% impossibile (>100)" % (riga_num, n))
    idx += 1

    if idx >= len(righe) or righe[idx].strip() != "":
        problemi.append("riga %d: manca la riga vuota fra il titolo e la tabella" % (idx + 1))
    else:
        idx += 1

    # Intestazione della tabella (vuota) e separatore centrato — 7º giro: il battito e'
    # una tabella markdown, non piu' testo rientrato a mano.
    if idx >= len(righe) or not RIGA_TABELLA_RE.match(righe[idx].strip()):
        problemi.append(
            "riga %d: manca l'intestazione della tabella `| |` — il battito ora e' una "
            "TABELLA markdown centrata (7º giro), non piu' testo rientrato a spazi"
            % (idx + 1)
        )
        return problemi
    idx += 1
    if idx >= len(righe) or not SEPARATORE_RE.match(righe[idx].strip()):
        problemi.append(
            "riga %d: manca il separatore centrato `|:---:|` sotto l'intestazione della "
            "tabella" % (idx + 1)
        )
        return problemi
    idx += 1

    celle = []
    while idx < len(righe):
        r = righe[idx].strip()
        mm = RIGA_TABELLA_RE.match(r)
        if not mm:
            break
        celle.append((idx, mm.group(1).strip()))
        idx += 1

    if not celle:
        problemi.append("la tabella non ha righe di contenuto dopo il separatore")
        return problemi

    j = 0
    for i, (etichetta, mn, mx) in enumerate(VOCI):
        if etichetta == "Forze":
            attesa = "🟠 Forze:"
            if j >= len(celle) or celle[j][1] != attesa:
                problemi.append(
                    "riga %s: attesa la cella `%s`, trovato: %r"
                    % ((celle[j][0] + 1) if j < len(celle) else "<fine tabella>", attesa,
                       celle[j][1] if j < len(celle) else "<fine tabella>")
                )
                j += 1
            else:
                j += 1
                # dopo l'etichetta: o e' un albero (la cella dopo e' un'altra etichetta
                # `🟠 <NOME>`, non la freccia) o e' testo piatto — si decide guardando la
                # cella successiva, senza consumarla.
                if j < len(celle) and GRUPPO_RE.match(celle[j][1]) and celle[j][1] != FRECCIA:
                    j = _leggi_albero_forze(celle, j, problemi)
                else:
                    contenuto = []
                    while j < len(celle):
                        testo = celle[j][1]
                        if testo == FRECCIA or testo == "":
                            break
                        contenuto.append(celle[j])
                        j += 1
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
            j = _leggi_voce_piatta(celle, j, etichetta, mn, mx, problemi)

        e_ultima = i == len(VOCI) - 1
        if not e_ultima:
            if j >= len(celle) or celle[j][1] != FRECCIA:
                problemi.append(
                    "riga %s: manca la cella freccia `| %s |` fra le voci '%s' e '%s'"
                    % ((celle[j][0] + 1) if j < len(celle) else "<fine tabella>", FRECCIA,
                       etichetta, VOCI[i + 1][0])
                )
            else:
                j += 1

    if j < len(celle):
        problemi.append(
            "riga %d: contenuto extra nella tabella dopo l'ultima voce (%r) — il battito "
            "finisce con la cella del Potere" % (celle[j][0] + 1, celle[j][1])
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

    Il titolo resta testo semplice, fuori dalla tabella (allineato a sinistra di suo). Ogni
    voce e le frecce `↓` fra un blocco e il successivo diventano righe `| ... |` di una
    TABELLA markdown a una colonna, con separatore `|:---:|` (centrato) — il renderer
    centra da solo via CSS, non serve più calcolare rientri a mano (7º giro, vedi il
    docstring del modulo per il perché)."""
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

    corpo = []
    for i, (etichetta, righe) in enumerate(blocchi):
        corpo.append("🟠 %s:" % etichetta)
        corpo.extend(righe)
        if i < len(blocchi) - 1:
            corpo.append(FRECCIA)

    righe_tabella = ["| |", "|:---:|"]
    for cella in corpo:
        righe_tabella.append("| |" if cella is None else "| %s |" % cella)

    out = ["**⏱️ RECAP — %d%%**" % percentuale, ""] + righe_tabella
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
