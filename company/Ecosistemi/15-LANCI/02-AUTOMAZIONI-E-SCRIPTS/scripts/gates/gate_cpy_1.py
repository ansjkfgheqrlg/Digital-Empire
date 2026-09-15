# -*- coding: utf-8 -*-
"""GATE-CPY-1 — presidia copy/manifest.json (ART-CPY).

Criterio eseguibile (registro, testuale):
    punteggio_totale >= 80
    AND nessun blocco sotto il 50% dei propri punti
    AND ogni affermazione con categoria=='prova' ha riferimento risolvibile

Una verifica per clausola, piu' due che il criterio da' per scontate: ogni `pezzi[].file`
esiste nella cartella del lancio (un manifesto che cita un testo assente non descrive
niente) e il pezzo intero non sta sotto il 50% (un pezzo non ha `punti_massimi`: si
considera 100).

SINTASSI DEI RIFERIMENTI. Le prove si risolvono contro certificato.json e ricerca.json
del lancio, mai contro il testo stesso (dato_da_terzi). Un riferimento e':

    <file>#<percorso>        es. "certificato.json#bandiere_rosse[0].come_verificata"
                                 "ricerca.json#frasi[3]"
                                 "ricerca.json#concorrenti[1].prezzo"

<file> in {certificato.json, ricerca.json}; <percorso> e' una catena di chiavi separate
da punto, con indici numerici fra parentesi quadre. Il riferimento e' risolvibile se il
file esiste e la navigazione arriva a un valore (anche 0 o "" — ma non a un nodo assente).
"""
from __future__ import annotations

import os
import re

from ._comune import ErroreArtefatto, Verdetto, leggi_artefatto, registro, valida_contro_schema

ID = "GATE-CPY-1"
ARTEFATTO = "copy/manifest.json"
SOGLIA_TOTALE = 80
QUOTA_MINIMA_BLOCCO = 0.5
FILE_PROVA = ("certificato.json", "ricerca.json")
_TOKEN = re.compile(r"([^.\[\]]+)|\[(\d+)\]")


def _ramo():
    for a in registro()["artefatti"]:
        if a.get("gate") == ID:
            return a.get("se_fallisce")
    return None


def risolvi_riferimento(dir_lancio: str, riferimento) -> tuple[bool, str]:
    """(risolvibile, motivo). Vedi la sintassi nel docstring del modulo."""
    if not isinstance(riferimento, str) or "#" not in riferimento:
        return False, "riferimento %r non nella forma <file>#<percorso>" % (riferimento,)
    nome, percorso = riferimento.split("#", 1)
    if nome not in FILE_PROVA:
        return False, "riferimento %r: il file deve essere uno fra %s" % (riferimento, ", ".join(FILE_PROVA))
    try:
        nodo = leggi_artefatto(dir_lancio, nome)
    except ErroreArtefatto as e:
        return False, str(e)
    if nodo is None:
        return False, "riferimento %r: %s assente nel lancio" % (riferimento, nome)
    if not percorso:
        return False, "riferimento %r: percorso vuoto dopo '#'" % riferimento
    for m in _TOKEN.finditer(percorso):
        chiave, indice = m.group(1), m.group(2)
        if indice is not None:
            i = int(indice)
            if not isinstance(nodo, list) or i >= len(nodo):
                return False, "riferimento %r: indice [%d] fuori misura" % (riferimento, i)
            nodo = nodo[i]
        else:
            if not isinstance(nodo, dict) or chiave not in nodo:
                return False, "riferimento %r: chiave %r non trovata" % (riferimento, chiave)
            nodo = nodo[chiave]
    return True, ""


def esegui(dir_lancio: str, rete) -> Verdetto:
    ramo = _ramo()
    errori = valida_contro_schema(dir_lancio, ARTEFATTO)
    if errori:
        pref = "" if errori == ["assente"] else "schema: "
        return Verdetto(ID, False, [pref + e for e in errori], {}, ramo)
    m = leggi_artefatto(dir_lancio, ARTEFATTO)
    problemi: list[str] = []

    totale = m.get("punteggio_totale")
    if not isinstance(totale, (int, float)) or totale < SOGLIA_TOTALE:
        problemi.append("punteggio_totale %r sotto la soglia %d" % (totale, SOGLIA_TOTALE))

    blocchi_sotto = 0
    prove_non_risolte = 0
    file_mancanti = 0
    n_prove = 0
    for pezzo in m.get("pezzi", []):
        pid = pezzo.get("id", "?")
        punt = pezzo.get("punteggio") or {}
        tot_pezzo = punt.get("totale", 0)
        if tot_pezzo < 100 * QUOTA_MINIMA_BLOCCO:
            blocchi_sotto += 1
            problemi.append("pezzo %s: punteggio %s sotto il 50%% dei propri punti (100)" % (pid, tot_pezzo))
        for b in punt.get("blocchi", []):
            massimo = b.get("punti_massimi") or 100
            punti = b.get("punti", 0)
            if punti < massimo * QUOTA_MINIMA_BLOCCO:
                blocchi_sotto += 1
                problemi.append("pezzo %s, blocco %r: %s su %s punti = %d%%, sotto il 50%%"
                                % (pid, b.get("nome"), punti, massimo, round(100.0 * punti / massimo)))
        for a in pezzo.get("affermazioni", []):
            if a.get("categoria") != "prova":
                continue
            n_prove += 1
            ok, motivo = risolvi_riferimento(dir_lancio, a.get("riferimento"))
            if not ok:
                prove_non_risolte += 1
                problemi.append("pezzo %s, affermazione %r: prova senza riferimento risolvibile — %s"
                                % (pid, a.get("testo"), motivo))
        file_pezzo = pezzo.get("file") or ""
        if not file_pezzo or not os.path.isfile(os.path.join(dir_lancio, *file_pezzo.split("/"))):
            file_mancanti += 1
            problemi.append("pezzo %s: il file %r non esiste nella cartella del lancio" % (pid, file_pezzo))

    dati = {"punteggio_totale": totale, "pezzi": len(m.get("pezzi", [])), "blocchi_sotto_50": blocchi_sotto,
            "prove": n_prove, "prove_non_risolte": prove_non_risolte, "file_mancanti": file_mancanti}
    return Verdetto(ID, not problemi, problemi, dati, ramo if problemi else None)
