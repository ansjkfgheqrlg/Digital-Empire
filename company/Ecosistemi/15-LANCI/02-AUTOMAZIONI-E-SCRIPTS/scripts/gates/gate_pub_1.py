# -*- coding: utf-8 -*-
"""GATE-PUB-1 — presidia pubblico.json (ART-PUB).

Criterio eseguibile (registro, testuale):
    somma(canali[].raggiungibili_verificati) > 0
    AND ogni canale ha prova.tipo in [esporto-lista, schermata-conteggio-piattaforma,
        misura-analytics] con data non anteriore a 30 giorni

Non apre nulla in rete: controlla le prove. "Data non anteriore a 30 giorni" e' letta
rispetto a `misurato_il` (la misura), non rispetto a oggi: cosi' il verdetto dipende dal
file e non dal giorno in cui si rilancia il gate (idempotenza). La somma e' ricalcolata dai
canali; il campo `totale_raggiungibile_verificato` e' confrontato, mai creduto.
"""
from __future__ import annotations

from datetime import date, datetime, timedelta

from ._comune import Verdetto, leggi_artefatto, registro, valida_contro_schema

ID = "GATE-PUB-1"
ARTEFATTO = "pubblico.json"
TIPI_PROVA_AMMESSI = ("esporto-lista", "schermata-conteggio-piattaforma", "misura-analytics")
GIORNI_MAX_PROVA = 30


def _ramo():
    for a in registro()["artefatti"]:
        if a.get("gate") == ID:
            return a.get("se_fallisce")
    return None


def _data(s):
    """date da 'YYYY-MM-DD' o da un date-time ISO; None se non si legge."""
    if not isinstance(s, str):
        return None
    try:
        return datetime.fromisoformat(s.replace("Z", "+00:00")).date()
    except ValueError:
        try:
            return date.fromisoformat(s[:10])
        except ValueError:
            return None


def esegui(dir_lancio: str, rete) -> Verdetto:
    ramo = _ramo()
    errori = valida_contro_schema(dir_lancio, ARTEFATTO)
    if errori:
        pref = "" if errori == ["assente"] else "schema: "
        return Verdetto(ID, False, [pref + e for e in errori], {}, ramo)
    pub = leggi_artefatto(dir_lancio, ARTEFATTO)
    problemi: list[str] = []

    misurato_il = _data(pub.get("misurato_il"))
    if misurato_il is None:
        problemi.append("misurato_il non e' una data leggibile: %r" % pub.get("misurato_il"))

    somma_verificata = 0          # solo i canali con prova ammessa e fresca
    somma_grezza = 0              # tutti i canali, per confronto
    canali_con_prova = 0
    for c in pub.get("canali", []):
        cid = c.get("id", "?")
        n = c.get("raggiungibili_verificati", 0)
        somma_grezza += n
        prova = c.get("prova") or {}
        tipo = prova.get("tipo")
        valida = True
        if tipo not in TIPI_PROVA_AMMESSI:
            valida = False
            problemi.append("canale %s: prova.tipo %r non ammessa (serve una fra %s): il "
                            "conteggio vale zero" % (cid, tipo, ", ".join(TIPI_PROVA_AMMESSI)))
        d_prova = _data(prova.get("data"))
        if d_prova is None:
            valida = False
            problemi.append("canale %s: prova.data %r non e' una data leggibile"
                            % (cid, prova.get("data")))
        elif misurato_il is not None:
            if d_prova > misurato_il:
                valida = False
                problemi.append("canale %s: prova.data %s e' posteriore a misurato_il %s"
                                % (cid, d_prova, misurato_il))
            elif misurato_il - d_prova > timedelta(days=GIORNI_MAX_PROVA):
                valida = False
                problemi.append("canale %s: prova del %s anteriore a %d giorni rispetto a "
                                "misurato_il %s: il conteggio vale zero"
                                % (cid, d_prova, GIORNI_MAX_PROVA, misurato_il))
        if valida:
            canali_con_prova += 1
            somma_verificata += n

    if somma_verificata <= 0:
        problemi.append("nessun pubblico verificato: somma(raggiungibili_verificati con prova "
                        "valida) = %d, serve > 0" % somma_verificata)

    dichiarato = pub.get("totale_raggiungibile_verificato")
    if dichiarato != somma_verificata:
        problemi.append("totale_raggiungibile_verificato dichiarato %r ma ricalcolato %d dai "
                        "canali con prova valida" % (dichiarato, somma_verificata))

    dati = {"somma_verificata": somma_verificata, "somma_grezza": somma_grezza,
            "totale_dichiarato": dichiarato, "canali": len(pub.get("canali", [])),
            "canali_con_prova_valida": canali_con_prova}
    return Verdetto(ID, not problemi, problemi, dati, ramo if problemi else None)
