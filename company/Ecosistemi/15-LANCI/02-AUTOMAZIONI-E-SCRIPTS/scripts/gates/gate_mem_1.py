# -*- coding: utf-8 -*-
"""GATE-MEM-1 — presidia debrief.json (ART-DBR): CHIUSO diventa APPRESO solo da qui.

Criterio eseguibile (registro, testuale):
    ogni scarto oltre il 10% fra ART-PRV e ART-CNS ha causa scritta
    AND schemi.count >= 3
    AND ogni schema ha si_applica_quando non vuoto
    AND ogni record di memoria della fase cita un artefatto esistente su disco

Gli scarti sono RICALCOLATI dal gate confrontando previsione.json (scenario `atteso`) e
consuntivo.json (dato_da_terzi), non letti dal campo `confronto`, che e' solo riportato:
  - ricavo_lordo: scenari.atteso.ricavo_lordo  vs  consuntivo.ricavo_lordo
  - ordini:       scenari.atteso.copie          vs  consuntivo.ordini.numero (se `copie` c'e')
scarto% = (reale - previsto) / previsto * 100; oltre il 10% in valore assoluto serve una
riga in `cause[]` con la stessa `voce`. "Record di memoria che cita un artefatto" = ogni
schema con `artefatto_di_origine` deve citare un file che esiste nella cartella del
lancio. La controfirma della Regia (`controfirma.chi`) deve esserci: nessuno scrive da
solo la storia di com'e' andata.
"""
from __future__ import annotations

import os

from ._comune import Verdetto, leggi_artefatto, registro, valida_contro_schema

ID = "GATE-MEM-1"
ARTEFATTO = "debrief.json"
SCARTO_MASSIMO = 10.0
SCHEMI_MINIMI = 3


def _ramo():
    for a in registro()["artefatti"]:
        if a.get("gate") == ID:
            return a.get("se_fallisce")
    return None


def _scarto(previsto, reale):
    if not isinstance(previsto, (int, float)) or not isinstance(reale, (int, float)):
        return None
    if previsto == 0:
        return None if reale == 0 else float("inf")
    return round((reale - previsto) / previsto * 100.0, 2)


def esegui(dir_lancio: str, rete) -> Verdetto:
    ramo = _ramo()
    errori = valida_contro_schema(dir_lancio, ARTEFATTO)
    if errori:
        pref = "" if errori == ["assente"] else "schema: "
        return Verdetto(ID, False, [pref + e for e in errori], {}, ramo)
    db = leggi_artefatto(dir_lancio, ARTEFATTO)
    problemi: list[str] = []

    previsione = leggi_artefatto(dir_lancio, "previsione.json")
    consuntivo = leggi_artefatto(dir_lancio, "consuntivo.json")
    scarti = {}
    if previsione is None:
        problemi.append("previsione.json assente: senza previsione non esiste scarto, e senza scarto non c'e' debrief")
    if consuntivo is None:
        problemi.append("consuntivo.json assente: senza consuntivo non esiste scarto")
    if previsione is not None and consuntivo is not None:
        atteso = (previsione.get("scenari") or {}).get("atteso") or {}
        coppie = {"ricavo_lordo": (atteso.get("ricavo_lordo"), consuntivo.get("ricavo_lordo"))}
        if "copie" in atteso:
            coppie["ordini"] = (atteso.get("copie"), (consuntivo.get("ordini") or {}).get("numero"))
        voci_con_causa = {c.get("voce") for c in db.get("cause", [])
                          if c.get("causa") and c.get("cosa_faremmo_di_diverso")}
        for voce, (prev, reale) in coppie.items():
            s = _scarto(prev, reale)
            scarti[voce] = {"previsto": prev, "reale": reale, "scarto_percentuale": s}
            if s is not None and abs(s) > SCARTO_MASSIMO and voce not in voci_con_causa:
                problemi.append("scarto %s%% su %s (previsto %s, reale %s) oltre il %d%% senza una causa scritta in "
                                "cause[] con voce %r" % (s, voce, prev, reale, SCARTO_MASSIMO, voce))

    schemi = db.get("schemi", [])
    if len(schemi) < SCHEMI_MINIMI:
        problemi.append("schemi: %d, servono almeno %d" % (len(schemi), SCHEMI_MINIMI))
    origini_mancanti = 0
    for i, s in enumerate(schemi):
        if not str(s.get("si_applica_quando") or "").strip():
            problemi.append("schema #%d %r: si_applica_quando vuoto — una regola senza confini si applica dove "
                            "non vale" % (i, (s.get("testo") or "")[:40]))
        if "artefatto_di_origine" in s:
            a = s.get("artefatto_di_origine") or ""
            if not a or not os.path.isfile(os.path.join(dir_lancio, *a.split("/"))):
                origini_mancanti += 1
                problemi.append("schema #%d: artefatto_di_origine %r non esiste nella cartella del lancio" % (i, a))

    cf = db.get("controfirma") or {}
    if not str(cf.get("chi") or "").strip():
        problemi.append("controfirma.chi assente: la Regia deve controfirmare il giudizio della Memoria")

    dati = {"scarti": scarti, "schemi": len(schemi), "cause": len(db.get("cause", [])),
            "origini_mancanti": origini_mancanti, "controfirma_chi": cf.get("chi"),
            "confronto_dichiarato": db.get("confronto", [])}
    return Verdetto(ID, not problemi, problemi, dati, ramo if problemi else None)
