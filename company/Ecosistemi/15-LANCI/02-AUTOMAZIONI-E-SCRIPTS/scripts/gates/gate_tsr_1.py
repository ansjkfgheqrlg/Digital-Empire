# -*- coding: utf-8 -*-
"""GATE-TSR-1 — presidia budget.json (ART-BDG), all'ingresso in produzione.

Criterio eseguibile (registro, testuale):
    costo_totale_previsto <= tetto
    AND pareggio.copie calcolato da ART-PRV
    AND costo_macchina_previsto presente e > 0

"Calcolato da ART-PRV" = il gate RIFA' il conto: copie = ceil(costo_totale_previsto /
prezzo), col prezzo di offerta.json (che previsione.json dichiara di aver ricevuto da
ART-OFF: i due prezzi devono coincidere, altrimenti la previsione e' di un'altra offerta).
Il campo `pareggio.copie` del file viene confrontato con il ricalcolo, mai creduto
(dato_da_terzi: il pareggio usa il ricavo previsto, non un numero del contabile).
Il costo totale e' anche ricalcolato dalle voci, per confronto.
"""
from __future__ import annotations

import math

from ._comune import Verdetto, leggi_artefatto, registro, valida_contro_schema

ID = "GATE-TSR-1"
ARTEFATTO = "budget.json"


def _ramo():
    for a in registro()["artefatti"]:
        if a.get("gate") == ID:
            return a.get("se_fallisce")
    return None


def esegui(dir_lancio: str, rete) -> Verdetto:
    ramo = _ramo()
    errori = valida_contro_schema(dir_lancio, ARTEFATTO)
    if errori:
        pref = "" if errori == ["assente"] else "schema: "
        return Verdetto(ID, False, [pref + e for e in errori], {}, ramo)
    b = leggi_artefatto(dir_lancio, ARTEFATTO)
    problemi: list[str] = []

    tetto = b.get("tetto")
    costo = b.get("costo_totale_previsto")
    if not isinstance(costo, (int, float)) or not isinstance(tetto, (int, float)) or costo > tetto:
        problemi.append("costo_totale_previsto %r oltre il tetto %r (scostamento %s)"
                        % (costo, tetto, round(costo - tetto, 2) if isinstance(costo, (int, float))
                           and isinstance(tetto, (int, float)) else "?"))
    somma_voci = round(sum(v.get("importo", 0) for v in b.get("voci", [])), 2)
    if isinstance(costo, (int, float)) and b.get("voci") and abs(somma_voci - costo) > 0.005:
        problemi.append("costo_totale_previsto %r ma la somma delle voci e' %r" % (costo, somma_voci))

    macchina = b.get("costo_macchina_previsto")
    if not isinstance(macchina, (int, float)) or macchina <= 0:
        problemi.append("costo_macchina_previsto %r: deve essere presente e > 0 (le chiamate ai modelli "
                        "costano, un lancio che non lo sa non calcola nessun pareggio)" % (macchina,))

    copie_ricalcolate = None
    prezzo = None
    previsione = leggi_artefatto(dir_lancio, "previsione.json")
    offerta = leggi_artefatto(dir_lancio, "offerta.json")
    if previsione is None:
        problemi.append("previsione.json assente: il pareggio non si puo' calcolare da ART-PRV")
    if offerta is None:
        problemi.append("offerta.json assente: manca il prezzo per il pareggio")
    if previsione is not None and offerta is not None:
        prezzo = offerta.get("prezzo")
        prezzo_prv = (previsione.get("ingressi") or {}).get("prezzo")
        if not isinstance(prezzo, (int, float)) or prezzo <= 0:
            problemi.append("offerta.prezzo %r non e' un numero > 0" % (prezzo,))
        elif prezzo_prv != prezzo:
            problemi.append("previsione.ingressi.prezzo %r diverso da offerta.prezzo %r: la previsione e' di "
                            "un'altra offerta" % (prezzo_prv, prezzo))
        elif isinstance(costo, (int, float)):
            copie_ricalcolate = math.ceil(costo / prezzo)
            dichiarate = (b.get("pareggio") or {}).get("copie")
            if dichiarate != copie_ricalcolate:
                problemi.append("pareggio.copie dichiarato %r ma ricalcolato %d = ceil(%s / %s) da previsione.json "
                                "e offerta.json" % (dichiarate, copie_ricalcolate, costo, prezzo))

    dati = {"costo_totale_previsto": costo, "tetto": tetto, "somma_voci": somma_voci,
            "costo_macchina_previsto": macchina, "prezzo": prezzo,
            "pareggio_copie_dichiarato": (b.get("pareggio") or {}).get("copie"),
            "pareggio_copie_ricalcolato": copie_ricalcolate}
    return Verdetto(ID, not problemi, problemi, dati, ramo if problemi else None)
