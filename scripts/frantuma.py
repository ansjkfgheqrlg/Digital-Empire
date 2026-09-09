# -*- coding: utf-8 -*-
"""
frantuma.py -- spacca una task grande in micro-task ufficiali, ognuna col suo ID.

Cosa fa questa funzione, e SOLO questa (corretto da Max il 2026-09-08, dopo una
prima versione che ci aveva messo dentro onde/parallelismo/verifica di scope
che nessuno aveva chiesto): prende una task grande e la spacca in micro-task,
ognuna con un ID coniato -- MT-01, MT-02, ... -- esattamente come un ADR o un
checkpoint. Non pianifica chi la esegue, non calcola parallelismo, non decide
un ordine. Divide, e basta.

Il problema che risolve
------------------------
Due sessioni non devono mai coniare la stessa micro-task nello stesso istante.
Stessa legge anti-collisione di scripts/adr.py e scripts/checkpoint.py (B-009):
il numero si occupa creando il FILE, in modo atomico (O_CREAT|O_EXCL), non
leggendo la cartella e scrivendo il successivo.

La numerazione e' per-padre: ogni task grande ha la sua sequenza MT-01, MT-02...
che riparte da 1 per una task diversa, perche' il numero deve dire "il pezzo
N-esimo DI QUESTA task", non un ID globale senza significato.

Lo schema di risposta
----------------------
Fisso, scelto da Max il 2026-09-08 dopo tre giri (bocciati: un albero ASCII
boxato/evidenziato con "onde" — cringe; un Artifact — vietato, vuole la chat).
Colore dominante VIOLA (🟣), come l'arancione (🟠) e' di /recap. Generato da
`report()`, mai scritto a mano: stessa filosofia del battito
(verifica_recap.py) -- la forma la garantisce il codice, non la mia memoria.

Uso:
    python scripts/frantuma.py conia --padre TASK-LANCI-BUILD-W3 \
        --slug chiave-brevo --titolo "Sostituire la chiave Brevo esposta"
    python scripts/frantuma.py report --padre TASK-LANCI-BUILD-W3
"""
from __future__ import annotations

import argparse
import io
import os
import re
import sys
from datetime import datetime

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARTELLA_BASE = os.path.join(RADICE, "company", "Memory", "tasks", "micro")

_RE_MT = re.compile(r"^MT-(\d{2,4})-(.*)$")
_RE_TITOLO = re.compile(r"^#\s*MT-\d+\s*[—-]\s*(.+)$", re.MULTILINE)


def _cartella(padre: str) -> str:
    return os.path.join(CARTELLA_BASE, padre)


def _numeri_su_disco(padre: str) -> dict[int, list[str]]:
    trovati: dict[int, list[str]] = {}
    cart = _cartella(padre)
    if not os.path.isdir(cart):
        return trovati
    for nome in sorted(os.listdir(cart)):
        if not nome.endswith(".md"):
            continue
        m = _RE_MT.match(nome[:-3])
        if m:
            trovati.setdefault(int(m.group(1)), []).append(nome)
    return trovati


def prossimo_numero(padre: str) -> int:
    disco = _numeri_su_disco(padre)
    return (max(disco) + 1) if disco else 1


def conia(padre: str, slug: str, titolo: str) -> str:
    """Occupa il prossimo numero MT-NN dentro la cartella del padre, atomico."""
    if not re.match(r"^[a-z0-9]+(-[a-z0-9]+)*$", slug):
        raise SystemExit("slug non valido: minuscole, cifre e trattini")
    if not re.match(r"^[A-Za-z0-9_-]+$", padre):
        raise SystemExit("padre non valido: usa il codice della task grande "
                          "(es. TASK-LANCI-BUILD-W3), senza spazi")
    cart = _cartella(padre)
    os.makedirs(cart, exist_ok=True)
    oggi = datetime.now().strftime("%Y-%m-%d")

    numero = prossimo_numero(padre)
    for _ in range(200):
        nome = "MT-%02d-%s.md" % (numero, slug)
        percorso = os.path.join(cart, nome)
        corpo = (
            "# MT-%02d — %s\n\n"
            "- **Padre:** %s\n"
            "- **Data:** %s\n\n"
            "## Cosa fa\n\n_da scrivere nello stesso turno in cui la micro-task e' coniata_\n\n"
            "## Gate di chiusura\n\n\n"
            "## Output\n\n"
        ) % (numero, titolo, padre, oggi)
        try:
            fd = os.open(percorso, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        except FileExistsError:
            numero += 1
            continue
        with io.open(fd, "w", encoding="utf-8", newline="\n") as f:
            f.write(corpo)
        codice = "MT-%02d" % numero
        print("")
        print("  MICRO-TASK CONIATA (numero occupato sul disco)")
        print("")
        print("     CODICE:  %s" % codice)
        print("     Padre:   %s" % padre)
        print("     Titolo:  %s" % titolo)
        print("     File:    company/Memory/tasks/micro/%s/%s" % (padre, nome))
        print("")
        return codice
    raise RuntimeError("Nessun numero MT libero nei 200 successivi: cartella rotta.")


def leggi_tutte(padre: str) -> list[dict]:
    cart = _cartella(padre)
    if not os.path.isdir(cart):
        return []
    righe = []
    for nome in sorted(os.listdir(cart)):
        if not nome.endswith(".md"):
            continue
        m = _RE_MT.match(nome[:-3])
        if not m:
            continue
        testo = io.open(os.path.join(cart, nome), encoding="utf-8").read()
        titolo_m = _RE_TITOLO.search(testo)
        righe.append({
            "codice": "MT-%02d" % int(m.group(1)),
            "numero": int(m.group(1)),
            "titolo": titolo_m.group(1).strip() if titolo_m else m.group(2),
        })
    return sorted(righe, key=lambda r: r["numero"])


def report(padre: str) -> str:
    """Schema fisso viola-con-frecce, scelto da Max il 2026-09-08/09. Calcolato
    dai file reali (titolo incluso), mai scritto a mano.

    Questa funzione legge SOLO file gia' coniati -- non esiste un "report" su
    micro-task che non sono ancora state create. Per questo il suo output e'
    sempre la FASE 2 (conferma): ogni riga porta il richiamo che l'ID e'
    ufficiale e usabile in un'altra chat/sessione. La FASE 1 (proposta, prima
    che Max/Gael/Neri accettino) non passa da qui: si compone a mano, sugli
    stessi titoli, SENZA coniare nulla -- vedi emperator.md 6.24.
    """
    tutte = leggi_tutte(padre)
    if not tutte:
        return "Nessuna micro-task coniata per %s. Usa `frantuma.py conia`." % padre

    righe = []
    righe.append("🟣 **%s**" % padre)
    righe.append("🟣 divisa in %d micro-task ufficiali" % len(tutte))
    righe.append("   │")
    for i, m in enumerate(tutte):
        ramo = "└──" if i == len(tutte) - 1 else "├──"
        righe.append("   %s🟣→ **%s** · %s — ID ufficiale, usabile in altre chat/sessioni"
                      % (ramo, m["codice"], m["titolo"]))
    return "\n".join(righe)


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Spacca una task grande in micro-task con ID (/frantuma).")
    sub = ap.add_subparsers(dest="azione", required=True)

    c = sub.add_parser("conia", help="crea una micro-task nuova, numero atomico")
    c.add_argument("--padre", required=True)
    c.add_argument("--slug", required=True)
    c.add_argument("--titolo", required=True)

    r = sub.add_parser("report", help="stampa lo schema fisso viola-con-frecce")
    r.add_argument("--padre", required=True)

    a = ap.parse_args()
    if a.azione == "conia":
        conia(a.padre, a.slug, a.titolo)
        return 0
    if a.azione == "report":
        print(report(a.padre))
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
