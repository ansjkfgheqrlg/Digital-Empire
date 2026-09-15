# -*- coding: utf-8 -*-
"""GATE-FNL-1 — presidia funnel.json (ART-FNL).

Criterio eseguibile (registro, testuale):
    ogni pagina risponde 200
    AND ogni pagina ha evento_conversione con prova.origine=='piattaforma'
    AND prova_cassa.stato=='incassato_e_rimborsato'
    AND prova_cassa.riferimento_transazione != null

"Risponde 200" e' RIAPERTO dal gate attraverso `rete.codice_http(url)`: il campo
`codice_http` salvato nel file non basta e non viene creduto (regola 1 e 2 di _comune.py).
Con ReteFinta un url non dichiarato risponde None = irraggiungibile = boccia.

NOTA SU 'piattaforma'. Il registro scrive `prova.origine=='piattaforma'`; lo schema
funnel.schema.json ammette solo [piattaforma-misura, registro-server, fornitore-pagamento].
Il valore letterale 'piattaforma' non passerebbe mai lo schema: qui si accetta
'piattaforma-misura', l'unico valore dello schema che corrisponde alla clausola
("l'evento si legge dalla piattaforma di misura", dato_da_terzi). La divergenza fra
registro e schema e' segnalata nel rapporto di costruzione, non risolta qui.
"""
from __future__ import annotations

from ._comune import Verdetto, leggi_artefatto, registro, valida_contro_schema

ID = "GATE-FNL-1"
ARTEFATTO = "funnel.json"
ORIGINI_AMMESSE = ("piattaforma-misura",)
STATO_CASSA_RICHIESTO = "incassato_e_rimborsato"


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
    fn = leggi_artefatto(dir_lancio, ARTEFATTO)
    problemi: list[str] = []

    codici = {}
    pagine_200 = 0
    pagine_con_evento = 0
    for p in fn.get("pagine", []):
        url = p.get("url")
        ruolo = p.get("ruolo", "?")
        codice = rete.codice_http(url)
        codici[url] = codice
        if codice == 200:
            pagine_200 += 1
        else:
            problemi.append("pagina %s (%s): riaperta dal gate risponde %s, serve 200 (il campo salvato "
                            "codice_http=%r non conta)" % (ruolo, url, codice if codice is not None else
                                                           "irraggiungibile", p.get("codice_http")))
        ev = p.get("evento_conversione") or {}
        origine = (ev.get("prova") or {}).get("origine")
        if not ev.get("nome"):
            problemi.append("pagina %s (%s): manca evento_conversione" % (ruolo, url))
        elif origine not in ORIGINI_AMMESSE:
            problemi.append("pagina %s (%s): evento %r con prova.origine %r, serve %s"
                            % (ruolo, url, ev.get("nome"), origine, " o ".join(ORIGINI_AMMESSE)))
        else:
            pagine_con_evento += 1

    cassa = fn.get("prova_cassa") or {}
    if cassa.get("stato") != STATO_CASSA_RICHIESTO:
        problemi.append("prova_cassa.stato %r: serve %r (incassare non basta, bisogna anche aver restituito)"
                        % (cassa.get("stato"), STATO_CASSA_RICHIESTO))
    if cassa.get("riferimento_transazione") in (None, ""):
        problemi.append("prova_cassa.riferimento_transazione assente: senza il riferimento del fornitore "
                        "la transazione di prova e' una dichiarazione, non una prova")

    dati = {"pagine": len(fn.get("pagine", [])), "pagine_200": pagine_200, "codici_riaperti": codici,
            "pagine_con_evento_da_piattaforma": pagine_con_evento, "stato_cassa": cassa.get("stato"),
            "riferimento_transazione": cassa.get("riferimento_transazione")}
    return Verdetto(ID, not problemi, problemi, dati, ramo if problemi else None)
