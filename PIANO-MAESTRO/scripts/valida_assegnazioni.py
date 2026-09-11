"""
valida_assegnazioni.py — FASE 0, passo 2b del piano 35: il giudice della classificazione.

Legge le assegnazioni prodotte dagli agenti classificatori
(36-LIBRO-AGENCY-INTEGRALE/assegnazioni/lotto-NN.json), le confronta con i lotti
e con la tassonomia fissa, e RIFIUTA quello che non torna. Poi, se tutto torna,
riscrive `atomi-index.json` con libro/capitolo/peso dentro e propaga la scelta ai
doppioni (che ereditano dal proprio principale).

Nessuna correzione silenziosa: cio' che non torna viene elencato per nome.
Console Windows cp1252: nessuna emoji nei print.
"""

import json
import os
import sys
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, "36-LIBRO-AGENCY-INTEGRALE")
LOTTI_DIR = os.path.join(OUT_DIR, "lotti")
ASSEGN_DIR = os.path.join(OUT_DIR, "assegnazioni")

PESI = {"portante", "supporto", "contesto"}


def leggi(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def main():
    tass = leggi(os.path.join(OUT_DIR, "TASSONOMIA.json"))
    capitoli_validi = set(tass["capitoli"])
    indice = leggi(os.path.join(OUT_DIR, "atomi-index.json"))
    per_uid = {a["uid"]: a for a in indice["atomi"]}

    lotti = sorted(f for f in os.listdir(LOTTI_DIR) if f.startswith("lotto-"))
    if not os.path.isdir(ASSEGN_DIR):
        print("NIENTE DA VALIDARE: manca %s" % ASSEGN_DIR)
        return 1

    attesi, ricevuti = {}, {}
    for nome in lotti:
        lotto = leggi(os.path.join(LOTTI_DIR, nome))
        attesi[nome] = {a["uid"] for a in lotto["atomi"]}

    errori, mancanti_lotti, assegnazioni = [], [], {}
    for nome in lotti:
        path = os.path.join(ASSEGN_DIR, nome)
        if not os.path.exists(path):
            mancanti_lotti.append(nome)
            continue
        try:
            dati = leggi(path)
        except Exception as exc:
            errori.append("%s: file illeggibile (%s)" % (nome, exc))
            continue
        righe = dati.get("assegnazioni") or dati.get("atomi") or (
            dati if isinstance(dati, list) else [])
        visti = set()
        for r in righe:
            uid = r.get("uid")
            if uid not in attesi[nome]:
                errori.append("%s: uid non appartiene al lotto -> %s" % (nome, uid))
                continue
            cap = (r.get("capitolo") or "").strip()
            peso = (r.get("peso") or "").strip().lower()
            if cap not in capitoli_validi:
                errori.append("%s: capitolo inventato '%s' su %s" % (nome, cap, uid))
                continue
            if peso not in PESI:
                errori.append("%s: peso non valido '%s' su %s" % (nome, peso, uid))
                continue
            if cap == "FUORI" and not (r.get("nota") or "").strip():
                errori.append("%s: FUORI senza nota su %s" % (nome, uid))
                continue
            visti.add(uid)
            assegnazioni[uid] = {
                "libro": cap.split(".")[0] if cap != "FUORI" else "FUORI",
                "capitolo": cap,
                "peso": peso,
                "nota": (r.get("nota") or "").strip() or None,
            }
        buchi = attesi[nome] - visti
        if buchi:
            errori.append("%s: %d atomi non classificati (es. %s)"
                          % (nome, len(buchi), sorted(buchi)[0]))
        ricevuti[nome] = len(visti)

    print("lotti previsti: %d   consegnati: %d   mancanti: %d"
          % (len(lotti), len(ricevuti), len(mancanti_lotti)))
    for nome in mancanti_lotti:
        print("  MANCA: %s" % nome)
    if errori:
        print("")
        print("ERRORI (%d) — nessuna scrittura fatta:" % len(errori))
        for e in errori[:60]:
            print("  - %s" % e)
        if len(errori) > 60:
            print("  ... e altri %d" % (len(errori) - 60))
        return 1
    if mancanti_lotti:
        print("")
        print("INCOMPLETO: mancano %d lotti. Indice non riscritto." % len(mancanti_lotti))
        return 1

    # --- propagazione ai doppioni ------------------------------------------------
    per_impronta = defaultdict(list)
    for a in indice["atomi"]:
        per_impronta[a["impronta"]].append(a)

    scritti, ereditati, orfani = 0, 0, []
    for a in indice["atomi"]:
        scelta = assegnazioni.get(a["uid"])
        if scelta is None and a["principale_di"]:
            scelta = assegnazioni.get(a["principale_di"])
            if scelta:
                ereditati += 1
        if scelta is None:
            orfani.append(a["uid"])
            continue
        a["libro"] = scelta["libro"]
        a["capitolo"] = scelta["capitolo"]
        a["peso"] = scelta["peso"]
        if scelta["nota"]:
            a["nota"] = scelta["nota"]
        scritti += 1

    if orfani:
        print("")
        print("ORFANI: %d atomi senza capitolo. Indice non riscritto." % len(orfani))
        for u in orfani[:20]:
            print("  - %s" % u)
        return 1

    indice["classificazione"] = {
        "atomi_classificati": scritti,
        "ereditati_da_doppione": ereditati,
        "per_libro": dict(Counter(a["libro"] for a in indice["atomi"])),
        "per_peso": dict(Counter(a["peso"] for a in indice["atomi"])),
    }
    with open(os.path.join(OUT_DIR, "atomi-index.json"), "w", encoding="utf-8") as fh:
        json.dump(indice, fh, ensure_ascii=False, indent=1)

    print("")
    print("OK. classificati=%d (di cui ereditati da doppione=%d), orfani=0"
          % (scritti, ereditati))
    print("per libro : %s" % indice["classificazione"]["per_libro"])
    print("per peso  : %s" % indice["classificazione"]["per_peso"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
