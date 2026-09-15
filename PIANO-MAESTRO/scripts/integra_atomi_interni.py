"""
integra_atomi_interni.py — porta gli atomi del materiale INTERNO (Libro I) dentro
`atomi-index.json`, con lo stesso schema degli altri, gia' classificati (capitolo + peso
li decide l'atomizzatore, perche' il Libro I ha 7 capitoli e il materiale e' nostro).

Legge:  36-LIBRO-AGENCY-INTEGRALE/atomi-interni/<gruppo>.json
Scrive: atomi-index.json (aggiunge/sostituisce le run "DE-<gruppo>", non tocca il resto)

Rilanciabile: le run DE-* vengono rimosse e riscritte ogni volta.
Console Windows cp1252: nessuna emoji nei print.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import sys
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, "36-LIBRO-AGENCY-INTEGRALE")
INT_DIR = os.path.join(OUT_DIR, "atomi-interni")

CAPITOLI_I = {"I.1", "I.2", "I.3", "I.4", "I.5", "I.6", "I.7"}
PESI = {"portante", "supporto", "contesto"}


def impronta(testo: str) -> str:
    pulito = re.sub(r"\s+", " ", (testo or "").lower()).strip()[:400]
    return hashlib.md5(pulito.encode("utf-8")).hexdigest()


def main() -> int:
    if not os.path.isdir(INT_DIR):
        print("manca %s" % INT_DIR)
        return 1
    with open(os.path.join(OUT_DIR, "atomi-index.json"), encoding="utf-8") as fh:
        indice = json.load(fh)

    prima = len(indice["atomi"])
    indice["atomi"] = [a for a in indice["atomi"] if not a["run"].startswith("DE-")]
    tolti = prima - len(indice["atomi"])

    errori, nuovi = [], []
    for nome in sorted(os.listdir(INT_DIR)):
        if not nome.endswith(".json"):
            continue
        path = os.path.join(INT_DIR, nome)
        try:
            with open(path, encoding="utf-8") as fh:
                dati = json.load(fh)
        except Exception as exc:
            errori.append("%s: illeggibile (%s)" % (nome, exc))
            continue
        gruppo = dati.get("gruppo") or nome[:-5]
        run = "DE-" + re.sub(r"[^A-Za-z0-9_-]", "_", gruppo)
        rel = os.path.relpath(path, os.path.dirname(ROOT)).replace(os.sep, "/")
        for i, a in enumerate(dati.get("atoms") or []):
            ka = a.get("id") or "KA-%03d" % (i + 1)
            cap = (a.get("capitolo") or "").strip()
            peso = (a.get("peso") or "").strip().lower()
            if cap not in CAPITOLI_I:
                errori.append("%s %s: capitolo non del Libro I -> '%s'" % (run, ka, cap))
                continue
            if peso not in PESI:
                errori.append("%s %s: peso non valido '%s'" % (run, ka, peso))
                continue
            if not (a.get("ancora") or "").strip():
                errori.append("%s %s: ancora vuota" % (run, ka))
                continue
            contenuto = (a.get("contenuto") or "").strip()
            if not contenuto:
                continue
            nuovi.append({
                "uid": "%s::%s" % (run, ka),
                "ka_id": ka,
                "run": run,
                "tipo": a.get("tipo") or "",
                "contenuto": contenuto,
                "ancora": a["ancora"].strip(),
                "fonte": a.get("fonte") or "",
                "frame": "",
                "confidenza": a.get("confidenza") or "osservato",
                "tags": [],
                "relazioni": a.get("relazioni") or [],
                "file_sorgente": rel,
                "parole": len(contenuto.split()),
                "libro": "I",
                "capitolo": cap,
                "peso": peso,
                "principale_di": None,
                "impronta": impronta(contenuto),
            })

    if errori:
        print("ERRORI (%d) — indice non toccato:" % len(errori))
        for e in errori[:40]:
            print("  - %s" % e)
        return 1

    indice["atomi"].extend(nuovi)
    indice["totale_atomi"] = len(indice["atomi"])
    indice["run"] = len({a["run"] for a in indice["atomi"]})
    if "classificazione" in indice:
        indice["classificazione"]["per_libro"] = dict(Counter(a["libro"] for a in indice["atomi"]))
        indice["classificazione"]["per_peso"] = dict(Counter(a["peso"] for a in indice["atomi"]))
    with open(os.path.join(OUT_DIR, "atomi-index.json"), "w", encoding="utf-8") as fh:
        json.dump(indice, fh, ensure_ascii=False, indent=1)

    print("atomi interni integrati: %d (rimossi i precedenti: %d)" % (len(nuovi), tolti))
    print("per capitolo: %s" % dict(sorted(Counter(a["capitolo"] for a in nuovi).items())))
    print("per peso    : %s" % dict(Counter(a["peso"] for a in nuovi)))
    print("indice totale: %d atomi" % len(indice["atomi"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
