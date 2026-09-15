# -*- coding: utf-8 -*-
"""GATE-STR-1 — presidia decisione.json (ART-DEC).

Criterio eseguibile (registro, testuale):
    tutte e cinque le domande hanno risposta in [si, no] e nessuna e' 'no'

Dato da terzi: "le risposte citano artefatti esistenti su disco, verificati dal gate" —
ogni `sostenuta_da` deve essere un file che ESISTE nella cartella del lancio. Una risposta
'si' senza file dietro vale 'no' (schema, descrizione del campo).
"""
from __future__ import annotations

import os

from ._comune import Verdetto, leggi_artefatto, registro, valida_contro_schema

ID = "GATE-STR-1"
ARTEFATTO = "decisione.json"
DOMANDE = ("D1-prodotto-esiste", "D2-pubblico-esiste", "D3-si-puo-incassare",
           "D4-capacita-nel-periodo", "D5-nessun-lancio-in-conflitto")
RISPOSTE = ("si", "no")


def _ramo():
    for a in registro()["artefatti"]:
        if a.get("gate") == ID:
            return a.get("se_fallisce")
    return None


def _file_nel_lancio(dir_lancio: str, rel) -> bool:
    if not isinstance(rel, str) or not rel.strip() or os.path.isabs(rel):
        return False
    radice = os.path.realpath(dir_lancio)
    p = os.path.realpath(os.path.join(dir_lancio, *rel.replace("\\", "/").split("/")))
    return p.startswith(radice + os.sep) and os.path.isfile(p)


def esegui(dir_lancio: str, rete) -> Verdetto:
    ramo = _ramo()
    errori = valida_contro_schema(dir_lancio, ARTEFATTO)
    if errori:
        pref = "" if errori == ["assente"] else "schema: "
        return Verdetto(ID, False, [pref + e for e in errori], {}, ramo)
    dec = leggi_artefatto(dir_lancio, ARTEFATTO)
    problemi: list[str] = []

    domande = dec.get("domande", [])
    ids = [d.get("id") for d in domande]
    mancanti = [i for i in DOMANDE if i not in ids]
    if len(domande) != 5 or mancanti:
        problemi.append("servono esattamente le cinque domande %s: trovate %d, mancano %s"
                        % (", ".join(DOMANDE), len(domande), mancanti or "nessuna"))

    n_si = n_no = 0
    file_mancanti = []
    for d in domande:
        did = d.get("id", "?")
        r = d.get("risposta")
        if r not in RISPOSTE:
            problemi.append("domanda %s: risposta %r non e' in [si, no]" % (did, r))
            continue
        if r == "no":
            n_no += 1
            problemi.append("domanda %s: risposta 'no' (%s)" % (did, d.get("testo", "")))
        else:
            n_si += 1
        s = d.get("sostenuta_da")
        if not _file_nel_lancio(dir_lancio, s):
            file_mancanti.append(s)
            problemi.append("domanda %s: sostenuta_da %r non e' un file esistente nella "
                            "cartella del lancio: una risposta senza file dietro vale 'no'"
                            % (did, s))

    if dec.get("esito") == "archiviato":
        problemi.append("esito dichiarato 'archiviato': il lancio non prosegue (ragione: %s)"
                        % dec.get("ragione_archiviazione"))

    dati = {"domande": len(domande), "si": n_si, "no": n_no,
            "file_mancanti": file_mancanti, "esito_dichiarato": dec.get("esito")}
    return Verdetto(ID, not problemi, problemi, dati, ramo if problemi else None)
