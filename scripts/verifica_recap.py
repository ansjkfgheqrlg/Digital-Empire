#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
verifica_recap.py — il gate meccanico del battito (emperator.md §6.11).

PERCHE' ESISTE (2026-09-05): la forma del battito era scritta carattere per carattere
in emperator.md §6.11 e ripetuta nel promemoria di ogni messaggio (emperator_hook.py).
Nonostante questo e' uscita fuori forma almeno quattro volte nello stesso giorno.
Questo script e' il controllo che non dipende dalla memoria del momento: legge un battito
e dice SI o NO, con la riga esatta che non torna.

FORMA A BULLET SEMPLICI, NIENTE CENTRAGGIO (2026-09-09, 8º giro). Sette giri avevano provato
a centrare il battito (riquadri, spazi, punti, blocchi di codice, tabelle markdown — vedi la
cronologia completa nella storia di git di questo file, troppo lunga per stare qui). L'8º giro
e' la resa dei conti: Max ha chiuso il filone chiedendo di tornare al formato SEMPLICE di
prima di tutta la saga del centraggio — un bullet `🟢 **<Etichetta>:** <contenuto libero>`
per voce, testo che va a capo da solo (nessun conteggio di 44 caratteri, nessun rientro,
nessuna tabella) — con UNA sola eccezione: la voce Forze, quando ha piu' unita' nominate,
resta ad ALBERO con le frecce `├─🟢→`/`└─🟢→` (5º giro, mai contestata). **Lezione della
saga intera:** sette giri di soluzioni via via piu' sofisticate (spazi, punti, fence, tabelle)
stavano tutti risolvendo un problema — il centraggio — che alla fine Max non voleva piu'.
La tecnica giusta per un requisito sbagliato resta una soluzione sbagliata: prima di
ingegnerizzare la centesima variante tecnica, verificare che il requisito di fondo sia ancora
quello vero.

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

TITOLO_RE = re.compile(r"^\*\*⏱️ RECAP — (\d{1,3})%\*\*$")
ASSETTO_RE = re.compile(r"^(\*\*GOD EMPEROR DOOM\*\*|normale)$")
POTERE_RE = re.compile(r"^(\d{1,3})%$")

# Etichetta ad albero (nome di un GRUPPO Forze): `🟢 <NOME>`, MA non un'altra voce bold tipo
# `🟢 **Assetto:**` — l'esclusione (?!\*\*) e' quello che li distingue.
GRUPPO_RE = re.compile(r"^🟢 (?!\*\*)(.+)$")
RAMO_RE = re.compile(r"^(├─🟢→|└─🟢→) (.+)$")

VOCI_SEMPLICI = ["Fatto", "Sto facendo", "Farò"]


def _leggi_stdin():
    grezzo = sys.stdin.buffer.read()
    return grezzo.decode("utf-8", "replace")


def _e_gruppi_forze(v):
    """True se `v` e' una lista di gruppi [(nome, [voce, ...]), ...] invece di una stringa
    piatta — il formato ad albero per Forze quando ci sono più unità nominate (5º giro)."""
    return isinstance(v, list) and len(v) > 0 and all(
        isinstance(x, tuple) and len(x) == 2 and isinstance(x[0], str) and isinstance(x[1], list)
        for x in v
    )


def _albero_forze(gruppi):
    """Genera le righe (piatte) dell'albero Forze da una lista di gruppi
    [(nome, [voce, ...]), ...]. `None` = riga vuota VERA fra un gruppo e l'altro."""
    righe = []
    for i, (nome, voci) in enumerate(gruppi):
        if not voci:
            raise ValueError("gruppo Forze '%s': nessuna voce" % nome)
        righe.append("🟢 %s" % nome.upper())
        righe.append("│")
        for j, v in enumerate(voci):
            ramo = "└─🟢→" if j == len(voci) - 1 else "├─🟢→"
            righe.append("%s %s" % (ramo, v))
        if i < len(gruppi) - 1:
            righe.append(None)
    return righe


def _leggi_albero_forze(righe, idx, problemi):
    """Legge un albero Forze a partire da `idx` — deve puntare alla prima etichetta di
    gruppo `🟢 <NOME>`. Ritorna l'indice subito dopo l'ultimo ramo `└─...` (o dopo l'ultima
    riga vuota fra gruppi, se il testo continua con un altro gruppo)."""
    while idx < len(righe):
        if not GRUPPO_RE.match(righe[idx]):
            break
        idx += 1  # etichetta di gruppo

        if idx >= len(righe) or righe[idx] != "│":
            problemi.append(
                "riga %d: dopo l'etichetta di un gruppo Forze serve la riga `│` da sola"
                % (idx + 1)
            )
        else:
            idx += 1

        rami = []
        while idx < len(righe):
            m = RAMO_RE.match(righe[idx])
            if not m:
                break
            rami.append((idx, m.group(1), m.group(2)))
            idx += 1

        if not rami:
            problemi.append("gruppo Forze: nessuna voce sotto `│` (serve almeno un ramo)")
        else:
            for riga_num, simbolo, _ in rami[:-1]:
                if simbolo != "├─🟢→":
                    problemi.append(
                        "riga %d: ramo non finale dev'essere `├─🟢→`, trovato `%s`"
                        % (riga_num + 1, simbolo)
                    )
            ultimo_num, ultimo_simbolo, _ = rami[-1]
            if ultimo_simbolo != "└─🟢→":
                problemi.append(
                    "riga %d: l'ultimo ramo del gruppo dev'essere `└─🟢→`, trovato `%s`"
                    % (ultimo_num + 1, ultimo_simbolo)
                )

        # riga vuota VERA fra un gruppo e il successivo — si consuma solo se dopo c'e'
        # DAVVERO un altro gruppo, altrimenti e' la riga vuota che separa Forze dalla
        # voce successiva (Assetto) e resta li' per chi legge dopo di noi.
        if (idx < len(righe) and righe[idx] == ""
                and idx + 1 < len(righe) and GRUPPO_RE.match(righe[idx + 1])):
            idx += 1
            continue
        break

    return idx


def valida(testo):
    """Ritorna una lista di problemi. Lista vuota = battito conforme."""
    problemi = []
    righe = testo.replace("\r\n", "\n").split("\n")

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

    for etichetta in VOCI_SEMPLICI:
        prefisso = "🟢 **%s:** " % etichetta
        if idx >= len(righe) or not righe[idx].startswith(prefisso) or righe[idx] == prefisso.rstrip():
            problemi.append(
                "riga %d: attesa `%s<contenuto>`, trovato: %r"
                % (idx + 1, prefisso, righe[idx] if idx < len(righe) else "<fine testo>")
            )
        else:
            if not righe[idx][len(prefisso):].strip():
                problemi.append("riga %d: voce '%s' senza contenuto" % (idx + 1, etichetta))
        idx += 1
        if idx >= len(righe) or righe[idx].strip() != "":
            problemi.append(
                "riga %d: manca la riga vuota dopo la voce '%s'" % (idx + 1, etichetta)
            )
        else:
            idx += 1

    # Forze — flat (`🟢 **Forze:** <contenuto>`) oppure ad albero (`🟢 **Forze:**` da sola
    # seguita dai gruppi).
    prefisso_forze = "🟢 **Forze:** "
    if idx < len(righe) and righe[idx] == "🟢 **Forze:**":
        idx += 1
        if idx >= len(righe) or not GRUPPO_RE.match(righe[idx]):
            problemi.append(
                "riga %d: dopo `🟢 **Forze:**` da sola serve almeno un gruppo `🟢 <NOME>`"
                % (idx + 1)
            )
        else:
            idx = _leggi_albero_forze(righe, idx, problemi)
    elif idx < len(righe) and righe[idx].startswith(prefisso_forze):
        if not righe[idx][len(prefisso_forze):].strip():
            problemi.append("riga %d: voce 'Forze' senza contenuto" % (idx + 1))
        idx += 1
    else:
        problemi.append(
            "riga %d: attesa la voce `🟢 **Forze:** <contenuto>` (o `🟢 **Forze:**` da sola "
            "per l'albero), trovato: %r" % (idx + 1, righe[idx] if idx < len(righe) else "<fine testo>")
        )
        idx += 1

    if idx >= len(righe) or righe[idx].strip() != "":
        problemi.append("riga %d: manca la riga vuota dopo la voce 'Forze'" % (idx + 1))
    else:
        idx += 1

    # Assetto
    prefisso_assetto = "🟢 **Assetto:** "
    if idx < len(righe) and righe[idx].startswith(prefisso_assetto):
        valore = righe[idx][len(prefisso_assetto):]
        if not ASSETTO_RE.match(valore):
            problemi.append(
                "riga %d: valore di Assetto non valido (%r) — atteso `normale` oppure "
                "`**GOD EMPEROR DOOM**`" % (idx + 1, valore)
            )
        idx += 1
    else:
        problemi.append(
            "riga %d: attesa `%s<normale|**GOD EMPEROR DOOM**>`, trovato: %r"
            % (idx + 1, prefisso_assetto, righe[idx] if idx < len(righe) else "<fine testo>")
        )
        idx += 1

    if idx >= len(righe) or righe[idx].strip() != "":
        problemi.append("riga %d: manca la riga vuota dopo la voce 'Assetto'" % (idx + 1))
    else:
        idx += 1

    # Potere
    prefisso_potere = "🟢 **Potere:** "
    if idx < len(righe) and righe[idx].startswith(prefisso_potere):
        valore = righe[idx][len(prefisso_potere):]
        mm = POTERE_RE.match(valore)
        if not mm:
            problemi.append(
                "riga %d: attesa `%s<n>%%`, trovato: %r" % (idx + 1, prefisso_potere, valore)
            )
        else:
            n = int(mm.group(1))
            if n > 100:
                problemi.append("riga %d: potere %d%% impossibile (>100)" % (idx + 1, n))
        idx += 1
    else:
        problemi.append(
            "riga %d: attesa `%s<n>%%`, trovato: %r"
            % (idx + 1, prefisso_potere, righe[idx] if idx < len(righe) else "<fine testo>")
        )
        idx += 1

    if idx < len(righe) and righe[idx].strip() != "":
        problemi.append(
            "riga %d: contenuto extra dopo la voce Potere (%r) — il battito finisce li'"
            % (idx + 1, righe[idx])
        )

    return problemi


def costruisci(fatto, sto_facendo, farò, forze, assetto, potere, percentuale):
    """Genera il testo del battito a partire dai valori — cosi' non si disegna a mano
    (stesso principio di frantuma.py). `fatto`/`sto_facendo`/`farò` sono STRINGHE (una
    frase libera, va a capo da sola — 8º giro, niente piu' righe multiple a mano). `forze`
    e' una stringa (forma piatta) oppure una lista di GRUPPI
    `[(nome_gruppo, [voce, voce, ...]), ...]` per il formato ad albero (5º giro, unica
    eccezione al bullet semplice). `assetto` e' "normale" oppure "GOD EMPEROR DOOM"."""
    out = ["**⏱️ RECAP — %d%%**" % percentuale, ""]

    for etichetta, contenuto in (("Fatto", fatto), ("Sto facendo", sto_facendo), ("Farò", farò)):
        out.append("🟢 **%s:** %s" % (etichetta, contenuto))
        out.append("")

    if _e_gruppi_forze(forze):
        out.append("🟢 **Forze:**")
        for r in _albero_forze(forze):
            out.append("" if r is None else r)
        out.append("")
    else:
        out.append("🟢 **Forze:** %s" % forze)
        out.append("")

    out.append("🟢 **Assetto:** %s" % ("**GOD EMPEROR DOOM**" if assetto == "GOD EMPEROR DOOM" else "normale"))
    out.append("")
    out.append("🟢 **Potere:** %d%%" % potere)

    return "\n".join(out)


# --- Missione (§6.11, ordine di Max 2026-09-09): controllo di rotta, non di progresso.
# Stesso principio del battito — schema fisso, verificabile da codice, non a braccio — ma
# marcato 🔴 rosso apposta per non confondersi col battito 🟢 a colpo d'occhio. Le "Fasi"
# sono la STESSA grammatica ad albero di Forze (│ / ├─→ / └─→), qui in rosso, un solo
# livello (nessun nome di gruppo): sono un'opinione di Emperator, non un impegno.
RAMO_ROSSO_RE = re.compile(r"^(├─🔴→|└─🔴→) (.+)$")


def costruisci_missione(sto_facendo, obiettivo, fasi):
    """`sto_facendo`/`obiettivo` sono stringhe (una frase libera). `fasi` e' una lista di
    1+ stringhe, una per fase, nell'ordine in cui Emperator pensa di percorrerle — una
    previsione, non un piano vincolante."""
    if not fasi:
        raise ValueError("Missione: serve almeno una fase")
    out = [
        "🔴 **Sto facendo:** %s" % sto_facendo,
        "🔴 **Obiettivo:** %s" % obiettivo,
        "🔴 Fasi:",
        "│",
    ]
    for i, f in enumerate(fasi):
        ramo = "└─🔴→" if i == len(fasi) - 1 else "├─🔴→"
        out.append("%s %s" % (ramo, f))
    return "\n".join(out)


def valida_missione(testo):
    """Ritorna una lista di problemi. Lista vuota = Missione conforme."""
    problemi = []
    righe = testo.replace("\r\n", "\n").split("\n")

    idx = 0
    while idx < len(righe) and righe[idx].strip() == "":
        idx += 1
    if idx >= len(righe):
        return ["blocco vuoto: nessuna Missione trovata nel testo passato"]

    for prefisso, nome in (("🔴 **Sto facendo:** ", "Sto facendo"), ("🔴 **Obiettivo:** ", "Obiettivo")):
        if idx >= len(righe) or not righe[idx].startswith(prefisso):
            problemi.append(
                "riga %d: attesa `%s<contenuto>`, trovato: %r"
                % (idx + 1, prefisso, righe[idx] if idx < len(righe) else "<fine testo>")
            )
        elif not righe[idx][len(prefisso):].strip():
            problemi.append("riga %d: '%s' senza contenuto" % (idx + 1, nome))
        idx += 1

    if idx >= len(righe) or righe[idx] != "🔴 Fasi:":
        problemi.append(
            "riga %d: attesa `🔴 Fasi:`, trovato: %r"
            % (idx + 1, righe[idx] if idx < len(righe) else "<fine testo>")
        )
        return problemi
    idx += 1

    if idx >= len(righe) or righe[idx] != "│":
        problemi.append("riga %d: dopo `🔴 Fasi:` serve la riga `│` da sola" % (idx + 1))
    else:
        idx += 1

    rami = []
    while idx < len(righe):
        m = RAMO_ROSSO_RE.match(righe[idx])
        if not m:
            break
        rami.append((idx, m.group(1), m.group(2)))
        idx += 1

    if not rami:
        problemi.append("Fasi: nessuna fase sotto `│` (serve almeno una)")
    else:
        for riga_num, simbolo, _ in rami[:-1]:
            if simbolo != "├─🔴→":
                problemi.append(
                    "riga %d: fase non finale dev'essere `├─🔴→`, trovato `%s`"
                    % (riga_num + 1, simbolo)
                )
        ultimo_num, ultimo_simbolo, _ = rami[-1]
        if ultimo_simbolo != "└─🔴→":
            problemi.append(
                "riga %d: l'ultima fase dev'essere `└─🔴→`, trovato `%s`"
                % (ultimo_num + 1, ultimo_simbolo)
            )

    if idx < len(righe) and righe[idx].strip() != "":
        problemi.append(
            "riga %d: contenuto extra dopo l'ultima fase (%r)" % (idx + 1, righe[idx])
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
