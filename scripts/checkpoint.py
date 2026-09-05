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
    python scripts/checkpoint.py cp --titolo "..."   (CP-YYYYMMDD-XXXX)

LEGGE ANTI-COLLISIONE (ordine di Max, 2026-09-05)
-------------------------------------------------
Nessun identificativo di checkpoint e' progressivo. Ne' EMP-XXXX ne'
CP-YYYYMMDD-XXXX. Il progressivo e' rotto per costruzione: due chat che
lavorano in parallelo non si vedono, calcolano lo stesso "prossimo numero" e
si sovrascrivono. I codici si SORTEGGIANO, si verificano contro il disco E
contro tutta la storia git (ogni ramo), e il file nasce subito per occupare
il codice.

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
    usati = set()
    if os.path.isdir(CARTELLA):
        usati |= set(n[:-3] for n in os.listdir(CARTELLA) if n.endswith(".md"))
    usati |= _nomi_mai_esistiti("company/Memory/riprese")
    return usati


def nuovo_codice():
    """Quattro caratteri, mai uno gia' usato."""
    usati = codici_esistenti()
    for _ in range(500):
        c = "EMP-" + "".join(random.choice(ALFABETO) for _ in range(4))
        if c not in usati:
            return c
    raise RuntimeError("Non trovo un codice libero: sono finiti o la cartella e' rotta.")


CARTELLA_CP = os.path.join(RADICE, "company", "Memory", "checkpoints")

_CACHE_GIT = {}


def _nomi_mai_esistiti(sottocartella):
    """Ogni nome di file MAI aggiunto in tutta la storia del repo, su ogni ramo.

    Serve perche' un codice puo' essere stato usato in una sessione parallela e
    poi spostato, rinominato o cancellato: la cartella di adesso non basta.
    """
    if sottocartella in _CACHE_GIT:
        return _CACHE_GIT[sottocartella]
    nomi = set()
    try:
        import subprocess
        out = subprocess.run(
            ["git", "log", "--all", "--diff-filter=A", "--name-only",
             "--pretty=format:", "--", sottocartella],
            cwd=RADICE, capture_output=True, text=True, timeout=60)
        for riga in out.stdout.splitlines():
            riga = riga.strip()
            if riga.endswith(".md"):
                nomi.add(os.path.basename(riga)[:-3])
    except Exception:
        pass  # senza git si lavora lo stesso, con meno memoria
    _CACHE_GIT[sottocartella] = nomi
    return nomi


def sorteggia(n=4):
    return "".join(random.choice(ALFABETO) for _ in range(n))


def cp_esistenti():
    """Tutti i CP: quelli sul disco adesso + quelli mai nati nella storia git."""
    usati = set()
    if os.path.isdir(CARTELLA_CP):
        usati |= set(n[:-3] for n in os.listdir(CARTELLA_CP) if n.endswith(".md"))
    usati |= _nomi_mai_esistiti("company/Memory/checkpoints")
    return usati


def nuovo_cp(titolo, quando=None):
    """Conia un identificativo di checkpoint IRRIPETIBILE: CP-YYYYMMDD-XXXX.

    Il numero progressivo e' vietato per costruzione: due chat che non si
    vedono sceglierebbero lo stesso 'prossimo numero'. Qui i quattro caratteri
    sono sorteggiati (614.656 combinazioni al giorno) e il file viene creato
    subito, cosi' il codice e' occupato nell'istante in cui nasce.
    """
    os.makedirs(CARTELLA_CP, exist_ok=True)
    giorno = (quando or datetime.now()).strftime("%Y%m%d")
    usati = cp_esistenti()
    codice = None
    for _ in range(2000):
        c = "CP-%s-%s" % (giorno, sorteggia(4))
        if c not in usati and not os.path.exists(os.path.join(CARTELLA_CP, c + ".md")):
            codice = c
            break
    if not codice:
        raise RuntimeError("Nessun codice CP libero: cartella rotta o alfabeto esaurito.")
    modello = os.path.join(RADICE, "company", "Memory", "templates", "CP-template.md")
    testo = ""
    if os.path.exists(modello):
        testo = io.open(modello, encoding="utf-8").read()
        testo = testo.replace("CP-YYYYMMDD-NNN", codice, 1)
        testo = testo.replace("<titolo task>", titolo, 1)
        testo = testo.replace("YYYY-MM-DD", datetime.now().strftime("%Y-%m-%d"), 1)
    else:
        righe = ["# " + codice + " - " + titolo, "",
                 "- **Data:** " + datetime.now().strftime("%Y-%m-%d"), ""]
        testo = chr(10).join(righe)
    with io.open(os.path.join(CARTELLA_CP, codice + ".md"), "w",
                 encoding="utf-8", newline=chr(10)) as f:
        f.write(testo)
    print("")
    print("  CHECKPOINT DI LAVORO CONIATO (codice irripetibile, mai progressivo)")
    print("")
    print("     CODICE:  %s" % codice)
    print("     Titolo:  %s" % titolo)
    print("     File:    company/Memory/checkpoints/%s.md" % codice)
    print("")
    print("  Il file esiste gia': il codice e' occupato, nessuna altra chat puo' prenderlo.")
    print("")
    return codice


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

    k = sub.add_parser("cp", help="conia un CP di lavoro con codice irripetibile")
    k.add_argument("--titolo", required=True)

    a = ap.parse_args()

    if a.comando == "nuovo":
        crea(a.titolo, a.task)
    elif a.comando == "leggi":
        return leggi(normalizza_codice(a.codice))
    elif a.comando == "chiudi":
        return chiudi(normalizza_codice(a.codice))
    elif a.comando == "cp":
        nuovo_cp(a.titolo)
    else:
        lista(getattr(a, "tutti", False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
