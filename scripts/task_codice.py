# -*- coding: utf-8 -*-
"""
TASK A CODICE — il sistema con cui Gael e Neri scelgono e riprendono le loro task.

Il problema che risolve
------------------------
Gael e Neri lavorano a task (settimanali o piu' lunghe), su un'altra macchina,
in chat separate da quella di Max. Quando Emperator gli propone 3-4 task da
cominciare, ognuna deve poter essere ripresa in una CHAT NUOVA senza dover
rispiegare da capo di cosa si tratta.

Cosa fa
-------
Ogni task scelta diventa un CODICE breve, legato alla persona (GAEL o NERI).
Loro copiano il codice, aprono una chat nuova, scrivono "Emperator <codice>",
ed Emperator legge la scheda e parte subito su quella task precisa — senza
richiedere altro contesto.

Diverso dai checkpoint EMP-XXXX (scripts/checkpoint.py): quelli sono la
ripresa del LAVORO DI EMPERATOR (qualsiasi cosa, a meta'). Questi sono
l'ELENCO DELLE TASK che Gael e Neri possono scegliere ed eseguire.

Il codice
---------
Forma: GAEL-XXXX o NERI-XXXX (quattro caratteri). Stesso alfabeto senza
lettere ambigue del sistema EMP-XXXX: niente O/0, I/1/L, S/5, B/8 — un
codice si detta a voce.

Uso:
    python scripts/task_codice.py crea --persona GAEL --titolo "..." \
        --madre "TASK-GAEL-20260831-SETTIMANA-02.md" --sezione "FIX-1" \
        --gate "4 ASIN registrati, libri_pubblicati/ non vuoto"
    python scripts/task_codice.py lista --persona GAEL
    python scripts/task_codice.py leggi GAEL-K7Q2
    python scripts/task_codice.py chiudi GAEL-K7Q2

Console Windows: solo ASCII in output.
"""

import os
import io
import re
import sys
import random
import argparse
from datetime import datetime

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARTELLA = os.path.join(RADICE, "company", "Memory", "tasks", "codici")

ALFABETO = "ACDEFGHJKMNPQRTUVWXYZ2346789"
PERSONE = ("GAEL", "NERI")


def assicura_cartella():
    os.makedirs(CARTELLA, exist_ok=True)


def valida_persona(persona):
    p = persona.strip().upper()
    if p not in PERSONE:
        raise ValueError("Persona '%s' non valida. Deve essere GAEL o NERI." % persona)
    return p


def codici_esistenti(persona=None):
    if not os.path.isdir(CARTELLA):
        return set()
    nomi = set(n[:-3] for n in os.listdir(CARTELLA) if n.endswith(".md"))
    if persona:
        nomi = set(n for n in nomi if n.startswith(persona + "-"))
    return nomi


def nuovo_codice(persona):
    usati = codici_esistenti()
    for _ in range(500):
        c = persona + "-" + "".join(random.choice(ALFABETO) for _ in range(4))
        if c not in usati:
            return c
    raise RuntimeError("Non trovo un codice libero: sono finiti o la cartella e' rotta.")


def percorso(codice):
    return os.path.join(CARTELLA, codice + ".md")


def normalizza_codice(c):
    """Si detta a voce: accetta 'gael k7q2', 'GAEL-K7Q2', 'neri-m3xz'."""
    c = c.strip().upper()
    for p in PERSONE:
        if c.replace("-", " ").replace("_", " ").startswith(p):
            resto = re.sub(r"[^A-Z0-9]", "", c[len(p):])
            return p + "-" + resto
    raise ValueError("Codice '%s' non riconosciuto: deve iniziare con GAEL o NERI." % c)


MODELLO = """# {codice} — {titolo}

- **Codice:** `{codice}`
- **Persona:** {persona}
- **Aperto:** {data}
- **Stato:** APERTO
- **Task madre:** {madre}
- **Sezione:** {sezione}

---

## COSA FARE

{titolo}

## GATE — quando e' chiusa

{gate}

---

## NOTE DI RIPRESA

<!-- Emperator aggiorna qui man mano che il lavoro procede su questo codice:
     cosa e' fatto, cosa resta, trappole trovate. Vale la stessa regola dei
     checkpoint EMP-XXXX: solo cose verificate, mai "quasi fatto". -->

-

---

*Si legge con: `python scripts/task_codice.py leggi {codice}`*
*Si chiude con: `python scripts/task_codice.py chiudi {codice}`*
"""


def crea(persona, titolo, madre, sezione, gate):
    persona = valida_persona(persona)
    assicura_cartella()
    codice = nuovo_codice(persona)
    testo = MODELLO.format(
        codice=codice, titolo=titolo, persona=persona, madre=madre,
        sezione=sezione or "-", gate=gate or "-",
        data=datetime.now().strftime("%Y-%m-%d %H:%M"))
    with io.open(percorso(codice), "w", encoding="utf-8", newline="\n") as f:
        f.write(testo)
    print("")
    print("  CODICE TASK CREATO")
    print("")
    print("     CODICE:  %s" % codice)
    print("     Titolo:  %s" % titolo)
    print("     File:    company/Memory/tasks/codici/%s.md" % codice)
    print("")
    print("  %s apre una chat nuova e scrive: Emperator %s" % (persona, codice))
    print("")
    return codice


def leggi_intestazione(codice):
    p = percorso(codice)
    if not os.path.exists(p):
        return None
    titolo, stato, data, persona = "(senza titolo)", "?", "?", "?"
    with io.open(p, encoding="utf-8") as f:
        for riga in f:
            r = riga.rstrip("\n")
            if r.startswith("# ") and titolo == "(senza titolo)":
                pezzi = r[2:].split("—", 1)
                titolo = pezzi[1].strip() if len(pezzi) > 1 else r[2:].strip()
            elif "**Stato:**" in r:
                stato = r.split("**Stato:**", 1)[1].strip()
            elif "**Aperto:**" in r:
                data = r.split("**Aperto:**", 1)[1].strip()
            elif "**Persona:**" in r:
                persona = r.split("**Persona:**", 1)[1].strip()
    return {"codice": codice, "titolo": titolo, "stato": stato,
            "data": data, "persona": persona}


def lista(persona=None, tutti=False):
    assicura_cartella()
    if persona:
        persona = valida_persona(persona)
    codici = sorted(codici_esistenti(persona))
    schede = [leggi_intestazione(c) for c in codici]
    schede = [s for s in schede if s]
    if not tutti:
        schede = [s for s in schede if "CHIUS" not in s["stato"].upper()]
    schede.sort(key=lambda s: s["data"], reverse=True)

    titolo_sezione = "TASK A CODICE" + (" — " + persona if persona else "") + \
        ("" if tutti else " - aperte")
    print("")
    print("=" * 78)
    print("  " + titolo_sezione)
    print("=" * 78)
    if not schede:
        print("")
        print("  Nessuna task a codice%s." % ("" if tutti else " aperta"))
        print("")
        return
    print("")
    for s in schede:
        marchio = "" if "CHIUS" not in s["stato"].upper() else "  [chiusa]"
        print("  - %s%s" % (s["codice"], marchio))
        print("      %s" % s["titolo"])
        print("      aperta il %s" % s["data"])
        print("")
    print("=" * 78)
    print("")


def leggi(codice):
    p = percorso(codice)
    if not os.path.exists(p):
        print("")
        print("  Nessuna task con codice %s." % codice)
        print("  Quelle che esistono:")
        print("")
        for c in sorted(codici_esistenti()):
            print("    %s" % c)
        print("")
        return 1
    with io.open(p, encoding="utf-8") as f:
        sys.stdout.write(f.read())
    return 0


def chiudi(codice):
    p = percorso(codice)
    if not os.path.exists(p):
        print("Nessuna task con codice %s." % codice)
        return 1
    s = io.open(p, encoding="utf-8", newline="").read()
    if "**Stato:** APERTO" not in s:
        print("%s non risulta aperta." % codice)
        return 0
    s = s.replace("**Stato:** APERTO",
                  "**Stato:** CHIUSO il %s" % datetime.now().strftime("%Y-%m-%d %H:%M"))
    io.open(p, "w", encoding="utf-8", newline="\n").write(s)
    print("%s chiusa. Resta leggibile, esce dalla lista delle aperte." % codice)
    return 0


def main():
    ap = argparse.ArgumentParser(
        description="Task a codice - come Gael e Neri scelgono e riprendono le loro task")
    sub = ap.add_subparsers(dest="comando")

    n = sub.add_parser("crea", help="apre un codice task e lo stampa")
    n.add_argument("--persona", required=True, help="GAEL o NERI")
    n.add_argument("--titolo", required=True, help="cosa fare, in una frase")
    n.add_argument("--madre", required=True, help="file TASK-*.md di origine")
    n.add_argument("--sezione", default="", help="la sotto-task dentro il file madre")
    n.add_argument("--gate", default="", help="quando si considera chiusa")

    l = sub.add_parser("lista", help="le task a codice aperte")
    l.add_argument("--persona", default=None, help="filtra per GAEL o NERI")
    l.add_argument("--tutti", action="store_true", help="anche quelle chiuse")

    g = sub.add_parser("leggi", help="stampa una task a codice")
    g.add_argument("codice")

    c = sub.add_parser("chiudi", help="marca una task a codice come chiusa")
    c.add_argument("codice")

    a = ap.parse_args()

    if a.comando == "crea":
        crea(a.persona, a.titolo, a.madre, a.sezione, a.gate)
    elif a.comando == "leggi":
        return leggi(normalizza_codice(a.codice))
    elif a.comando == "chiudi":
        return chiudi(normalizza_codice(a.codice))
    else:
        lista(getattr(a, "persona", None), getattr(a, "tutti", False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
