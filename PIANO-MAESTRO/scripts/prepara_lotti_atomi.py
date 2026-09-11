"""
prepara_lotti_atomi.py — FASE 0, passo 2 del piano 35.

Divide i 2.877 atomi principali (i doppioni ereditano dal principale) in lotti
maneggiabili, uno per agente classificatore. Ogni lotto e' un file JSON snello:
solo cio' che serve per decidere Libro + capitolo + peso, senza l'ancora e senza
le relazioni, che gonfierebbero il contesto dell'agente senza aiutarlo a scegliere.

Uscita:  36-LIBRO-AGENCY-INTEGRALE/lotti/lotto-NN.json
"""

import json
import os
import sys
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, "36-LIBRO-AGENCY-INTEGRALE")
LOTTI_DIR = os.path.join(OUT_DIR, "lotti")

MAX_ATOMI = 200          # per lotto: sopra, l'agente comincia a sbrigarsi
MAX_CARATTERI = 900      # per atomo: oltre non serve per classificare


def main():
    with open(os.path.join(OUT_DIR, "atomi-index.json"), encoding="utf-8") as fh:
        indice = json.load(fh)

    principali = [a for a in indice["atomi"] if not a["principale_di"]]
    print("atomi principali da classificare: %d" % len(principali))

    per_run = defaultdict(list)
    for a in principali:
        per_run[a["run"]].append(a)

    # Le run grandi si spezzano; le piccole si accorpano. Cosi' ogni agente vede
    # materiale coerente invece di un'insalata di fonti scollegate.
    lotti, corrente, capienza = [], [], 0
    for run in sorted(per_run, key=lambda r: -len(per_run[r])):
        atomi = per_run[run]
        if len(atomi) >= MAX_ATOMI:
            for i in range(0, len(atomi), MAX_ATOMI):
                lotti.append(atomi[i:i + MAX_ATOMI])
            continue
        if capienza + len(atomi) > MAX_ATOMI and corrente:
            lotti.append(corrente)
            corrente, capienza = [], 0
        corrente.extend(atomi)
        capienza += len(atomi)
    if corrente:
        lotti.append(corrente)

    os.makedirs(LOTTI_DIR, exist_ok=True)
    for vecchio in os.listdir(LOTTI_DIR):
        if vecchio.startswith("lotto-") and vecchio.endswith(".json"):
            os.remove(os.path.join(LOTTI_DIR, vecchio))

    for n, lotto in enumerate(lotti, 1):
        snello = [{
            "uid": a["uid"],
            "run": a["run"],
            "tipo": a["tipo"],
            "testo": a["contenuto"][:MAX_CARATTERI],
        } for a in lotto]
        nome = "lotto-%02d.json" % n
        with open(os.path.join(LOTTI_DIR, nome), "w", encoding="utf-8") as fh:
            json.dump({"lotto": n, "totale": len(snello), "atomi": snello},
                      fh, ensure_ascii=False, indent=1)
        run_dentro = sorted({a["run"] for a in lotto})
        etichetta = run_dentro[0] if len(run_dentro) == 1 else "%d run" % len(run_dentro)
        print("  %s  %3d atomi  (%s)" % (nome, len(snello), etichetta))

    print("")
    print("lotti creati: %d  -> %s" % (len(lotti), LOTTI_DIR))
    return 0


if __name__ == "__main__":
    sys.exit(main())
