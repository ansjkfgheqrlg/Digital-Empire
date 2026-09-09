# -*- coding: utf-8 -*-
"""
frantuma.py -- spacca una task grande in micro-task ufficiali, ognuna col suo
codice -- esattamente come un checkpoint di ripresa (scripts/checkpoint.py).

Cosa fa questa funzione, e SOLO questa (corretta due volte da Max lo stesso
giorno: prima tolte onde/parallelismo/scope non richiesti, poi corretto l'ID
stesso -- non un percorso di file, un CODICE BREVE, la stessa cosa di un
checkpoint. "Con ID intendo il checkpoint, capisci? sono la stessa cosa. Lo
copio, lo metto in un'altra chat, e quella parte subito facendo la micro
task.").

Il codice
---------
Forma: MT-XXXX (quattro caratteri). Stesso alfabeto senza caratteri ambigui di
scripts/checkpoint.py (niente O/0, I/1/L, S/5, B/8) -- un codice si detta a
voce. NON e' progressivo: e' sorteggiato e verificato contro ogni micro-task
mai esistita (disco + storia git, ogni ramo), stessa legge anti-collisione di
checkpoint.py e adr.py (B-009). Un numero progressivo per-padre (MT-01, MT-02)
sarebbe stato ambiguo: incollato in una chat nuova senza dire anche il padre,
non porta da nessuna parte. Un codice sorteggiato e' gia' univoco da solo.

Uso:
    python scripts/frantuma.py conia --padre TASK-LANCI-BUILD-W3 \
        --slug chiave-brevo --titolo "Sostituire la chiave Brevo esposta"
    python scripts/frantuma.py trova MT-6R2M
    python scripts/frantuma.py report --padre TASK-LANCI-BUILD-W3
"""
from __future__ import annotations

import argparse
import io
import os
import random
import re
import subprocess
import sys
from datetime import datetime

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARTELLA_BASE = os.path.join(RADICE, "company", "Memory", "tasks", "micro")
SOTTOCARTELLA_GIT = "company/Memory/tasks/micro"

# stesso alfabeto di scripts/checkpoint.py: si detta a voce senza ambiguita'
ALFABETO = "ACDEFGHJKMNPQRTUVWXYZ2346789"

_RE_MT = re.compile(r"^(MT-[A-Z0-9]{4})-(.*)$")
_RE_TITOLO = re.compile(r"^#\s*MT-[A-Z0-9]{4}\s*[—-]\s*(.+)$", re.MULTILINE)


def _cartella(padre: str) -> str:
    return os.path.join(CARTELLA_BASE, padre)


def _sorteggia(n: int = 4) -> str:
    return "".join(random.choice(ALFABETO) for _ in range(n))


def _codici_su_disco() -> set[str]:
    trovati: set[str] = set()
    if not os.path.isdir(CARTELLA_BASE):
        return trovati
    for radice, _dirs, nomi in os.walk(CARTELLA_BASE):
        for nome in nomi:
            if not nome.endswith(".md"):
                continue
            m = _RE_MT.match(nome[:-3])
            if m:
                trovati.add(m.group(1))
    return trovati


def _codici_nella_storia() -> set[str]:
    """Ogni codice MT mai aggiunto al repo, su qualunque ramo -- stessa
    ragione di adr.py/checkpoint.py: un codice nato in una sessione parallela
    e poi rinominato sparisce dal disco e resta occupato."""
    codici: set[str] = set()
    try:
        out = subprocess.run(
            ["git", "log", "--all", "--diff-filter=A", "--name-only",
             "--pretty=format:", "--", SOTTOCARTELLA_GIT],
            cwd=RADICE, capture_output=True, text=True, timeout=60)
        for riga in out.stdout.splitlines():
            riga = riga.strip()
            if not riga.endswith(".md"):
                continue
            m = _RE_MT.match(os.path.basename(riga)[:-3])
            if m:
                codici.add(m.group(1))
    except Exception:
        pass  # senza git si lavora lo stesso, con meno memoria
    return codici


def nuovo_codice() -> str:
    occupati = _codici_su_disco() | _codici_nella_storia()
    for _ in range(2000):
        c = "MT-" + _sorteggia(4)
        if c not in occupati:
            return c
    raise RuntimeError("Nessun codice MT libero: alfabeto esaurito o cartella rotta.")


def conia(padre: str, slug: str, titolo: str) -> str:
    """Sorteggia il codice e crea il file in modo atomico (O_CREAT|O_EXCL):
    se due sessioni coniano nello stesso istante, una vince e l'altra
    risorteggia, invece di scriversi sopra."""
    if not re.match(r"^[a-z0-9]+(-[a-z0-9]+)*$", slug):
        raise SystemExit("slug non valido: minuscole, cifre e trattini")
    if not re.match(r"^[A-Za-z0-9_-]+$", padre):
        raise SystemExit("padre non valido: usa il codice della task grande "
                          "(es. TASK-LANCI-BUILD-W3), senza spazi")
    cart = _cartella(padre)
    os.makedirs(cart, exist_ok=True)
    oggi = datetime.now().strftime("%Y-%m-%d")
    # L'ORDINE DI CONIO, e perche' serve (2026-09-09). Il codice e' sorteggiato,
    # quindi ordinare per nome di file significa ordinare a caso: il primo report
    # reale metteva S0.1 in cima e S0.0 in nona posizione, cioe' perdeva proprio
    # l'informazione che ADR-025 chiama non negoziabile (il gesto zero viene prima).
    # Chi conia le micro-task le conia nell'ordine in cui vanno fatte: si registra quello.
    ordine = len(leggi_tutte(padre)) + 1

    for _ in range(2000):
        codice = nuovo_codice()
        nome = "%s-%s.md" % (codice, slug)
        percorso = os.path.join(cart, nome)
        corpo = (
            "# %s — %s\n\n"
            "- **Padre:** %s\n"
            "- **Data:** %s\n"
            "- **Ordine:** %d\n\n"
            "## Cosa fa\n\n_da scrivere nello stesso turno in cui la micro-task e' coniata_\n\n"
            "## Gate di chiusura\n\n\n"
            "## Output\n\n"
        ) % (codice, titolo, padre, oggi, ordine)
        try:
            fd = os.open(percorso, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        except FileExistsError:
            continue
        with io.open(fd, "w", encoding="utf-8", newline="\n") as f:
            f.write(corpo)
        print("")
        print("  MICRO-TASK CONIATA (codice irripetibile, mai progressivo)")
        print("")
        print("     CODICE:  %s" % codice)
        print("     Padre:   %s" % padre)
        print("     Titolo:  %s" % titolo)
        print("     File:    company/Memory/tasks/micro/%s/%s" % (padre, nome))
        print("")
        print("  Basta dire %s in un'altra chat: la trova con `frantuma.py trova`." % codice)
        print("")
        return codice
    raise RuntimeError("Non riesco a coniare: nessun codice libero dopo 2000 tentativi.")


def _tutti_i_file() -> list[tuple[str, str, str]]:
    """(codice, padre, nome_file) per ogni micro-task su disco."""
    risultato = []
    if not os.path.isdir(CARTELLA_BASE):
        return risultato
    for padre in sorted(os.listdir(CARTELLA_BASE)):
        cart = _cartella(padre)
        if not os.path.isdir(cart):
            continue
        for nome in sorted(os.listdir(cart)):
            if not nome.endswith(".md"):
                continue
            m = _RE_MT.match(nome[:-3])
            if m:
                risultato.append((m.group(1), padre, nome))
    return risultato


def trova_percorso(codice: str) -> str | None:
    """Il percorso del file di una micro-task, cercando in TUTTE le task
    padre -- e' il senso stesso del codice: non serve sapere altro."""
    codice = codice.upper()
    if not codice.startswith("MT-"):
        codice = "MT-" + codice
    for c, padre, nome in _tutti_i_file():
        if c == codice:
            return os.path.join(CARTELLA_BASE, padre, nome)
    return None


_RE_ORDINE = re.compile(r"^- \*\*Ordine:\*\* *(\d+)", re.M)


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
        ordine_m = _RE_ORDINE.search(testo)
        righe.append({
            "codice": m.group(1),
            "titolo": titolo_m.group(1).strip() if titolo_m else m.group(2),
            "ordine": int(ordine_m.group(1)) if ordine_m else None,
            "_nome": nome,
        })
    # Ordine di conio, non alfabetico: il codice e' sorteggiato e ordinare per
    # nome e' ordinare a caso. Una micro-task senza il campo (coniata prima del
    # 2026-09-09) va in fondo, stabile per nome, invece di far saltare tutto.
    righe.sort(key=lambda r: (r["ordine"] is None, r["ordine"] or 0, r["_nome"]))
    return righe


def report(padre: str) -> str:
    """Schema fisso viola-con-frecce, scelto da Max il 2026-09-08/09. Calcolato
    dai file reali (titolo incluso), mai scritto a mano.

    Legge SOLO file gia' coniati -- non esiste un "report" su micro-task che
    non sono ancora state create. Per questo il suo output e' sempre la
    FASE 2 (conferma): ogni riga porta il CODICE -- lo stesso di un
    checkpoint -- non un percorso: e' quello che si copia e si incolla in
    un'altra chat. La FASE 1 (proposta, prima che Max/Gael/Neri accettino)
    non passa da qui: si compone a mano, sugli stessi titoli, SENZA coniare
    nulla -- vedi emperator.md 6.24.
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
        righe.append("   %s🟣→ **%s** · %s" % (ramo, m["codice"], m["titolo"]))
    return "\n".join(righe)


def main() -> int:
    # Su Windows stdout e' cp1252 e il carattere viola non ci sta: `report`
    # moriva con UnicodeEncodeError prima di stampare una riga, cioe' il comando
    # non funzionava sulla macchina su cui gira (trovato il 2026-09-09, al primo
    # uso reale). Lo schema viola e' tutto il punto della funzione: senza questo
    # la FASE 2 di /frantuma non e' eseguibile.
    if hasattr(sys.stdout, "buffer"):
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8",
                                      errors="replace", line_buffering=True)
    ap = argparse.ArgumentParser(
        description="Spacca una task grande in micro-task con codice (/frantuma).")
    sub = ap.add_subparsers(dest="azione", required=True)

    c = sub.add_parser("conia", help="crea una micro-task nuova, codice sorteggiato")
    c.add_argument("--padre", required=True)
    c.add_argument("--slug", required=True)
    c.add_argument("--titolo", required=True)

    t = sub.add_parser("trova", help="trova e stampa una micro-task dal suo codice")
    t.add_argument("codice")

    r = sub.add_parser("report", help="stampa lo schema fisso viola-con-frecce")
    r.add_argument("--padre", required=True)

    a = ap.parse_args()
    if a.azione == "conia":
        conia(a.padre, a.slug, a.titolo)
        return 0
    if a.azione == "trova":
        p = trova_percorso(a.codice)
        if not p:
            print("Nessuna micro-task con codice %s." % a.codice)
            return 1
        sys.stdout.write(io.open(p, encoding="utf-8").read())
        return 0
    if a.azione == "report":
        print(report(a.padre))
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
