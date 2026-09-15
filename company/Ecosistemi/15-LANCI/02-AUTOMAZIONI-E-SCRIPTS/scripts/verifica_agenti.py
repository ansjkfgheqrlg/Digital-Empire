# -*- coding: utf-8 -*-
"""Verifica che i 15 file `.claude/agents/lan-*.md` rispettino il registro.

PERCHE' ESISTE. Il registro (`PIANO-MAESTRO/29-ECOSISTEMA-LANCI/dati/registro.yaml`) e' la fonte
di verita' su chi sono gli agenti, che modello usano, quali strumenti hanno e cosa producono. I
file `.claude/agents/*.md` sono una copia leggibile da Claude Code di quella verita': se
divergono in silenzio, un agente lavora con un modello sbagliato, uno strumento che non doveva
avere, o un campo di frontmatter inventato che lo fa scartare senza errore
(`.claude/agents/emperator.md` SS6.6). Questo script ricalcola la divergenza, non la presume.

Uso:
    PYTHONIOENCODING=utf-8 python scripts/verifica_agenti.py

Esce 0 solo se tutti gli agenti del registro sono ok, 1 altrimenti.
"""
from __future__ import annotations

import os
import sys

import yaml

SCRIPTS = os.path.dirname(os.path.abspath(__file__))
ECOSISTEMA = os.path.dirname(os.path.dirname(SCRIPTS))
RADICE = os.path.dirname(os.path.dirname(os.path.dirname(ECOSISTEMA)))
DATI = os.path.join(RADICE, "PIANO-MAESTRO", "29-ECOSISTEMA-LANCI", "dati")
REGISTRO = os.path.join(DATI, "registro.yaml")
AG = os.path.join(RADICE, ".claude", "agents")

# I soli campi ammessi nel frontmatter di un agente ufficiale. Un campo in piu' -> l'agente
# viene scartato in silenzio da Claude Code (emperator.md SS6.6): qui lo diciamo ad alta voce.
CAMPI_AMMESSI = {"name", "description", "model", "color", "tools"}


class ErroreFrontmatter(Exception):
    pass


def carica_registro() -> dict:
    with open(REGISTRO, encoding="utf-8") as f:
        return yaml.safe_load(f)


def leggi_frontmatter(percorso: str) -> tuple[dict, str]:
    """Ritorna (frontmatter come mappa, corpo del file dopo il frontmatter).
    Parser semplice e deliberato: cerca le prime due righe '---' e passa cio' che sta in
    mezzo a yaml.safe_load, esattamente come richiesto dal compito."""
    with open(percorso, encoding="utf-8") as f:
        righe = f.readlines()
    if not righe or righe[0].strip() != "---":
        raise ErroreFrontmatter("il file non inizia con '---'")
    fine = None
    for i in range(1, len(righe)):
        if righe[i].strip() == "---":
            fine = i
            break
    if fine is None:
        raise ErroreFrontmatter("frontmatter senza '---' di chiusura")
    blocco = "".join(righe[1:fine])
    try:
        dati = yaml.safe_load(blocco)
    except yaml.YAMLError as e:
        raise ErroreFrontmatter("YAML del frontmatter non valido: %s" % e)
    if not isinstance(dati, dict):
        raise ErroreFrontmatter("il frontmatter non e' una mappa")
    corpo = "".join(righe[fine + 1:])
    return dati, corpo


def verifica_agente(agente: dict, mappa_artefatti: dict) -> tuple[bool, list[str]]:
    """agente: una voce di registro['agenti']. mappa_artefatti: {ART-id: file} da
    registro['artefatti'], per risolvere INV-22. Ritorna (ok, problemi)."""
    problemi: list[str] = []
    id_ = agente["id"]
    percorso = os.path.join(AG, id_ + ".md")

    if not os.path.exists(percorso):
        return False, ["file assente: %s" % percorso]

    try:
        front, corpo = leggi_frontmatter(percorso)
    except ErroreFrontmatter as e:
        return False, ["frontmatter illeggibile: %s" % e]

    # nessun campo oltre i cinque ammessi
    extra = sorted(set(front.keys()) - CAMPI_AMMESSI)
    if extra:
        problemi.append("campi non ammessi nel frontmatter: %s" % extra)

    # name == id
    if front.get("name") != id_:
        problemi.append("name=%r != id registro %r" % (front.get("name"), id_))

    # model == registro, esatto (mai un alias)
    if front.get("model") != agente["modello"]:
        problemi.append("model=%r != registro %r" % (front.get("model"), agente["modello"]))

    # tools == registro, stessa lista, stesso ordine
    tools = front.get("tools")
    if tools != agente["tools"]:
        problemi.append("tools=%r != registro %r" % (tools, agente["tools"]))

    # description: presente, non vuota, una riga sola
    descr = front.get("description")
    if not isinstance(descr, str) or not descr.strip():
        problemi.append("description assente o vuota")
    elif "\n" in descr:
        problemi.append("description su piu' di una riga")

    # INV-09: lan-gate non ha Write ne' Edit
    if id_ == "lan-gate":
        t = tools if isinstance(tools, list) else []
        vietati = [x for x in ("Write", "Edit") if x in t]
        if vietati:
            problemi.append("INV-09: lan-gate ha %s fra i tools" % vietati)

    # INV-22: il campo 'produce' del registro coincide con l'artefatto citato nel corpo
    for p in agente.get("produce", []):
        atteso = mappa_artefatti.get(p, p)  # se p non e' un ART-id (es. 'verbali'), usa se stesso
        if atteso not in corpo:
            problemi.append("INV-22: '%s' (produce=%s) non citato nel corpo del file" % (atteso, p))

    return (len(problemi) == 0), problemi


def main() -> int:
    reg = carica_registro()
    agenti = reg["agenti"]
    mappa_artefatti = {a["id"]: a["file"] for a in reg["artefatti"]}

    righe = []
    for agente in agenti:
        ok, problemi = verifica_agente(agente, mappa_artefatti)
        righe.append((agente["id"], ok, problemi))

    larghezza = max(len(id_) for id_, _, _ in righe) + 2
    for id_, ok, problemi in righe:
        stato = "ok" if ok else "NO"
        print("%-*s %s" % (larghezza, id_, stato))
        for p in problemi:
            print("    - %s" % p)

    n_ok = sum(1 for _, ok, _ in righe if ok)
    tutti_ok = n_ok == len(righe)
    print()
    print("%d/%d agenti ok" % (n_ok, len(righe)))
    return 0 if tutti_ok else 1


if __name__ == "__main__":
    sys.exit(main())
