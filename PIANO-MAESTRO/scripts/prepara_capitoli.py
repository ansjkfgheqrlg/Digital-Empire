"""
prepara_capitoli.py — FASE 2, passo 7 del piano 35: il fascicolo di ogni capitolo.

Per ogni capitolo della tassonomia produce UN file che l'agente scrittore riceve:
    36-LIBRO-AGENCY-INTEGRALE/capitoli-input/<cap>[-<parte>].json
con dentro:
  - gli atomi principali del capitolo, INTERI (contenuto, ancora verbatim, fonte, frame,
    relazioni), col peso deciso in Fase 0;
  - per ogni atomo, gli eventuali doppioni (lo stesso concetto detto da un'altra fonte),
    cosi' il capitolo puo' dire "lo dicono in due";
  - i file di testo integrale (L2) da cui gli atomi provengono, come puntatori: lo
    scrittore li apre per espandere, non si accontenta dell'atomo;
  - la lista esatta dei marcatori [[uid]] che il gate pretendera'.

Nessun target di lunghezza (piano 35, errore 4): solo la lista di atomi e la soglia
per atomo. I capitoli grandi si spezzano in parti da massimo MAX_PORTANTI portanti,
tenendo insieme gli atomi della stessa run.

Console Windows cp1252: nessuna emoji nei print.
"""

from __future__ import annotations

import json
import os
import re
import sys
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(ROOT)
OUT_DIR = os.path.join(ROOT, "36-LIBRO-AGENCY-INTEGRALE")
IN_DIR = os.path.join(OUT_DIR, "capitoli-input")
KNOWLEDGE = os.path.join(REPO, "SKILL & Agenti", "Empire Studio Suite", "empire-studio",
                         "memory-empire", "knowledge")

MAX_PORTANTI = 45          # per parte: oltre, un solo agente non regge la densita'
MAX_ATOMI = 110

TESTI_BUONI = ("contenuto-integrale.md", "transcript.md", "video-analysis.md")
TESTI_ESCLUSI = ("coverage.md", "scenes.md", "enrichment-report.md", "README.md")


def chiave_cap(c: str):
    if c == "FUORI":
        return ("Z", 0)
    l, n = c.split(".")
    return (l, int(n))


def video_id(run: str):
    m = re.search(r"([A-Za-z0-9_-]{11})$", run)
    return m.group(1) if m else None


def fonti_di(run: str, file_sorgente: str) -> list[str]:
    """I file di testo integrale (L2) di una run, come percorsi assoluti."""
    cartella = os.path.dirname(os.path.join(REPO, file_sorgente))
    trovati = []
    try:
        nomi = sorted(os.listdir(cartella))
    except OSError:
        nomi = []
    for n in nomi:
        if n in TESTI_BUONI:
            trovati.append(os.path.join(cartella, n))
    for n in nomi:
        if n.startswith("_parte-") and n.endswith(".md"):
            trovati.append(os.path.join(cartella, n))
    if not trovati:
        for n in nomi:
            if n.endswith(".md") and n not in TESTI_ESCLUSI and not n.startswith("atoms"):
                trovati.append(os.path.join(cartella, n))
    vid = video_id(run)
    if vid:
        extra = os.path.join(KNOWLEDGE, vid, "contenuto-integrale.md")
        if os.path.exists(extra) and extra not in trovati:
            trovati.append(extra)
    return trovati


def spezza(atomi: list[dict]) -> list[list[dict]]:
    """Parti da <= MAX_PORTANTI portanti e <= MAX_ATOMI atomi, run per run."""
    portanti = sum(1 for a in atomi if a["peso"] == "portante")
    if portanti <= MAX_PORTANTI and len(atomi) <= MAX_ATOMI:
        return [atomi]
    per_run = defaultdict(list)
    for a in atomi:
        per_run[a["run"]].append(a)
    parti, corrente, np_, na = [], [], 0, 0
    for run in sorted(per_run, key=lambda r: -len(per_run[r])):
        gruppo = per_run[run]
        gp = sum(1 for a in gruppo if a["peso"] == "portante")
        if gp > MAX_PORTANTI or len(gruppo) > MAX_ATOMI:
            # una run sola piu' grande di una parte: si taglia a fette
            if corrente:
                parti.append(corrente); corrente, np_, na = [], 0, 0
            fetta, fp = [], 0
            for a in gruppo:
                fetta.append(a); fp += a["peso"] == "portante"
                if fp >= MAX_PORTANTI or len(fetta) >= MAX_ATOMI:
                    parti.append(fetta); fetta, fp = [], 0
            if fetta:
                parti.append(fetta)
            continue
        if corrente and (np_ + gp > MAX_PORTANTI or na + len(gruppo) > MAX_ATOMI):
            parti.append(corrente); corrente, np_, na = [], 0, 0
        corrente.extend(gruppo); np_ += gp; na += len(gruppo)
    if corrente:
        parti.append(corrente)
    return parti


def main() -> int:
    with open(os.path.join(OUT_DIR, "atomi-index.json"), encoding="utf-8") as fh:
        indice = json.load(fh)
    with open(os.path.join(OUT_DIR, "TASSONOMIA.json"), encoding="utf-8") as fh:
        tass = json.load(fh)

    doppioni = defaultdict(list)
    for a in indice["atomi"]:
        if a["principale_di"]:
            doppioni[a["principale_di"]].append(
                {"uid": a["uid"], "run": a["run"], "fonte": a["fonte"]})

    per_cap = defaultdict(list)
    for a in indice["atomi"]:
        if a["principale_di"] or not a["capitolo"] or a["capitolo"] == "FUORI":
            continue
        per_cap[a["capitolo"]].append(a)

    os.makedirs(IN_DIR, exist_ok=True)
    for vecchio in os.listdir(IN_DIR):
        if vecchio.endswith(".json"):
            os.remove(os.path.join(IN_DIR, vecchio))

    manifesto = []
    for cap in sorted(per_cap, key=chiave_cap):
        atomi = sorted(per_cap[cap], key=lambda a: (a["run"], a["ka_id"]))
        parti = spezza(atomi)
        lettere = "abcdefghijklmnop"
        for i, parte in enumerate(parti):
            nome = cap if len(parti) == 1 else "%s-%s" % (cap, lettere[i])
            fonti = {}
            for a in parte:
                if a["run"].startswith("DE-"):
                    # materiale interno: la fonte e' il file citato nell'atomo stesso
                    percorso = re.split(r"\s*[§#]\s*|\s+\(", a["fonte"] or "", 1)[0].strip()
                    if percorso:
                        assoluto = percorso if os.path.isabs(percorso) else os.path.join(REPO, percorso)
                        if os.path.exists(assoluto):
                            fonti.setdefault(a["run"], [])
                            if assoluto not in fonti[a["run"]]:
                                fonti[a["run"]].append(assoluto)
                    continue
                if a["run"] not in fonti:
                    fonti[a["run"]] = fonti_di(a["run"], a["file_sorgente"])
            fascicolo = {
                "capitolo": cap,
                "parte": nome,
                "parte_n": i + 1,
                "parti_totali": len(parti),
                "titolo": tass["capitoli"][cap],
                "libro": cap.split(".")[0],
                "libro_titolo": tass["libri"][cap.split(".")[0]],
                "regole": {
                    "portante": "entra espanso, MINIMO 150 parole attorno al marcatore [[uid]], "
                                "con la citazione letterale della fonte (campo `ancora`) riportata",
                    "supporto": "entra come citazione dentro un paragrafo, col marcatore [[uid]]",
                    "contesto": "NON entra nel corpo: sta in appendice (generata da codice)",
                },
                "marcatori_richiesti": [a["uid"] for a in parte
                                        if a["peso"] in ("portante", "supporto")],
                "fonti_integrali": fonti,
                "atomi": [{
                    "uid": a["uid"], "peso": a["peso"], "tipo": a["tipo"],
                    "contenuto": a["contenuto"], "ancora": a["ancora"],
                    "fonte": a["fonte"], "frame": a["frame"], "run": a["run"],
                    "relazioni": a["relazioni"],
                    "detto_anche_da": doppioni.get(a["uid"], []),
                } for a in parte],
            }
            with open(os.path.join(IN_DIR, nome + ".json"), "w", encoding="utf-8") as fh:
                json.dump(fascicolo, fh, ensure_ascii=False, indent=1)
            np_ = sum(1 for a in parte if a["peso"] == "portante")
            ns = sum(1 for a in parte if a["peso"] == "supporto")
            manifesto.append((nome, cap.split(".")[0], len(parte), np_, ns, len(fonti)))

    with open(os.path.join(IN_DIR, "MANIFESTO.md"), "w", encoding="utf-8") as fh:
        fh.write("# Fascicoli di scrittura — generati da prepara_capitoli.py\n\n")
        fh.write("| Fascicolo | Libro | Atomi | Portanti | Supporto | Run |\n|---|---|---|---|---|---|\n")
        for r in manifesto:
            fh.write("| `%s` | %s | %d | %d | %d | %d |\n" % r)
        fh.write("\nTotale fascicoli: %d — parole minime dai portanti: %d\n"
                 % (len(manifesto), sum(r[3] for r in manifesto) * 150))

    print("fascicoli: %d  -> %s" % (len(manifesto), IN_DIR))
    for libro in ("I", "II", "III", "IV", "V", "VI", "VII"):
        f = [r for r in manifesto if r[1] == libro]
        print("  Libro %-4s %2d fascicoli  %4d atomi  %4d portanti"
              % (libro, len(f), sum(r[2] for r in f), sum(r[3] for r in f)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
