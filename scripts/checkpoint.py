# -*- coding: utf-8 -*-
"""
CHECKPOINT DI RIPRESA - il codice che riporta Emperator dove era rimasto.

Il problema che risolve
-----------------------
Una conversazione lunga si riempie di contesto e diventa cara. Ma aprirne una
nuova costa tutto il contesto: Emperator non sa piu' cosa stava facendo, quali
decisioni erano gia' prese, quali errori erano gia' stati commessi e superati.
Risultato: si ricomincia, si rifanno le stesse domande, si ripetono gli stessi
sbagli.

Cosa fa
-------
Ogni lavoro puo' essere chiuso in un CHECKPOINT DI RIPRESA con un CODICE breve.
Max apre una chat nuova, dice il codice, ed Emperator riprende esattamente da li':
sa cosa era fatto, cosa era a meta', qual e' il prossimo passo esatto, quali
decisioni non vanno ridiscusse e in quali trappole non ricadere.

Il codice
---------
Forma: EMP-XXXX (quattro caratteri). Alfabeto senza lettere ambigue: niente
O/0, I/1/L, S/5 - un codice si detta a voce, e "EMP-S0IL" e' illeggibile.

Uso:
    python scripts/checkpoint.py lista
    python scripts/checkpoint.py leggi EMP-K7Q2
    python scripts/checkpoint.py nuovo --titolo "..." --task "..."
    python scripts/checkpoint.py chiudi EMP-K7Q2

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
CARTELLA = os.path.join(RADICE, "company", "Memory", "riprese")

# alfabeto senza caratteri che si confondono a voce o a schermo:
# via O e 0, via I 1 L, via S e 5, via B e 8
ALFABETO = "ACDEFGHJKMNPQRTUVWXYZ2346789"


def assicura_cartella():
    os.makedirs(CARTELLA, exist_ok=True)


def codici_esistenti():
    if not os.path.isdir(CARTELLA):
        return set()
    return set(n[:-3] for n in os.listdir(CARTELLA) if n.endswith(".md"))


def nuovo_codice():
    """Quattro caratteri, mai uno gia' usato."""
    usati = codici_esistenti()
    for _ in range(500):
        c = "EMP-" + "".join(random.choice(ALFABETO) for _ in range(4))
        if c not in usati:
            return c
    raise RuntimeError("Non trovo un codice libero: sono finiti o la cartella e' rotta.")


def percorso(codice):
    return os.path.join(CARTELLA, codice + ".md")


def normalizza_codice(c):
    """Max lo detta a voce: accetta 'emp k7q2', 'EMP-K7Q2', 'k7q2'."""
    c = re.sub(r"[^A-Za-z0-9]", "", c).upper()
    if c.startswith("EMP"):
        c = c[3:]
    return "EMP-" + c


MODELLO = """# {codice} — {titolo}

- **Codice di ripresa:** `{codice}`
- **Aperto:** {data}
- **Stato:** APERTO
- **Chi riprende:** basta dire `{codice}` in una chat nuova dentro Digital Empire.

---

## 1. IL LAVORO IN UNA FRASE

{task}

---

## 2. DOVE SIAMO — cosa e' FATTO davvero

<!-- Solo cose verificate sul disco. Niente "quasi fatto": o e' fatto o non lo e'. -->

-

## 3. COSA E' RIMASTO A META'

<!-- Il pezzo piu' prezioso: qui muoiono i lavori quando cambia la chat. -->

-

## 4. IL PROSSIMO PASSO ESATTO

<!-- Non "continuare il lavoro": il comando o il file preciso da cui ripartire. -->

-

---

## 5. DECISIONI GIA' PRESE — non ridiscuterle

<!-- Perche' la chat nuova non le sa, e senza questo le rimette in discussione. -->

-

## 6. TRAPPOLE — errori gia' fatti, non rifarli

<!-- Ogni riga qui vale un'ora risparmiata. -->

-

---

## 7. COMANDI PER RIPARTIRE

```bash
```

## 8. FILE TOCCATI

-

---

*Chiudi con: `python scripts/checkpoint.py chiudi {codice}`*
"""


def crea(titolo, task):
    assicura_cartella()
    codice = nuovo_codice()
    testo = MODELLO.format(
        codice=codice, titolo=titolo, task=task,
        data=datetime.now().strftime("%Y-%m-%d %H:%M"))
    with io.open(percorso(codice), "w", encoding="utf-8", newline="\n") as f:
        f.write(testo)
    print("")
    print("  CHECKPOINT DI RIPRESA CREATO")
    print("")
    print("     CODICE:  %s" % codice)
    print("     Titolo:  %s" % titolo)
    print("     File:    company/Memory/riprese/%s.md" % codice)
    print("")
    print("  Adesso riempilo: stato, cosa e' a meta', prossimo passo, trappole.")
    print("  In una chat nuova bastera' dire %s." % codice)
    print("")
    return codice


def leggi_intestazione(codice):
    """Titolo, stato, data e la frase del lavoro, senza caricare tutto il file."""
    p = percorso(codice)
    if not os.path.exists(p):
        return None
    titolo, stato, data, frase = "(senza titolo)", "?", "?", ""
    dentro_frase = False
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
            elif "IL LAVORO IN UNA FRASE" in r:
                dentro_frase = True
            elif dentro_frase:
                if r.startswith("---") or r.startswith("##"):
                    dentro_frase = False
                elif r.strip() and not r.startswith("<!--"):
                    frase = (frase + " " + r.strip()).strip()
    return {"codice": codice, "titolo": titolo, "stato": stato,
            "data": data, "frase": frase[:200]}


def lista(tutti=False):
    assicura_cartella()
    codici = sorted(codici_esistenti())
    schede = [leggi_intestazione(c) for c in codici]
    schede = [s for s in schede if s]
    if not tutti:
        schede = [s for s in schede if "CHIUS" not in s["stato"].upper()]
    schede.sort(key=lambda s: s["data"], reverse=True)

    print("")
    print("=" * 78)
    print("  CHECKPOINT DI RIPRESA" + ("" if tutti else " - aperti"))
    print("=" * 78)
    if not schede:
        print("")
        print("  Nessun checkpoint%s." % ("" if tutti else " aperto"))
        print("  Se ne apre uno con:")
        print('    python scripts/checkpoint.py nuovo --titolo "..." --task "..."')
        print("")
        return
    print("")
    for s in schede:
        marchio = "" if "CHIUS" not in s["stato"].upper() else "  [chiuso]"
        print("  - %s%s" % (s["codice"], marchio))
        print("      %s" % s["titolo"])
        if s["frase"]:
            print("      %s" % s["frase"])
        print("      aperto il %s" % s["data"])
        print("")
    print("=" * 78)
    print("  Per riprenderne uno: dillo e basta, in qualunque chat di Digital")
    print("  Empire. Esempio: \"Emperator, riprendi %s\"" % schede[0]["codice"])
    print("=" * 78)
    print("")


def leggi(codice):
    p = percorso(codice)
    if not os.path.exists(p):
        print("")
        print("  Nessun checkpoint con codice %s." % codice)
        print("  Quelli che esistono:")
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
        print("Nessun checkpoint con codice %s." % codice)
        return 1
    s = io.open(p, encoding="utf-8", newline="").read()
    if "**Stato:** APERTO" not in s:
        print("%s non risulta aperto." % codice)
        return 0
    s = s.replace("**Stato:** APERTO",
                  "**Stato:** CHIUSO il %s" % datetime.now().strftime("%Y-%m-%d %H:%M"))
    io.open(p, "w", encoding="utf-8", newline="\n").write(s)
    print("%s chiuso. Resta leggibile, esce dalla lista degli aperti." % codice)
    return 0


def main():
    ap = argparse.ArgumentParser(
        description="Checkpoint di ripresa - il codice che riporta Emperator dove era")
    sub = ap.add_subparsers(dest="comando")

    n = sub.add_parser("nuovo", help="apre un checkpoint e stampa il codice")
    n.add_argument("--titolo", required=True)
    n.add_argument("--task", required=True, help="il lavoro in una frase")

    l = sub.add_parser("lista", help="i checkpoint aperti")
    l.add_argument("--tutti", action="store_true", help="anche quelli chiusi")

    g = sub.add_parser("leggi", help="stampa un checkpoint")
    g.add_argument("codice")

    c = sub.add_parser("chiudi", help="marca un checkpoint come chiuso")
    c.add_argument("codice")

    a = ap.parse_args()

    if a.comando == "nuovo":
        crea(a.titolo, a.task)
    elif a.comando == "leggi":
        return leggi(normalizza_codice(a.codice))
    elif a.comando == "chiudi":
        return chiudi(normalizza_codice(a.codice))
    else:
        lista(getattr(a, "tutti", False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
