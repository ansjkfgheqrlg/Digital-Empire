# -*- coding: utf-8 -*-
"""GATE-CNS-1 — presidia consuntivo.json (ART-CNS): il lancio non chiude senza un'origine.

Criterio eseguibile (registro, testuale):
    ricavo_lordo ha origine in [fornitore-pagamento, esporto-piattaforma]
    AND periodo copre tutte le date del carrello
    AND ordini.count coerente con ricavo/prezzo

Il carrello e' offerta.data_apertura .. data_chiusura (o apertura + durata - 1 se la
chiusura manca): periodo.dal <= apertura e periodo.al >= chiusura. La coerenza degli
ordini e' ricalcolata: |ordini.numero - round(ricavo_lordo / ordini.prezzo_medio)| <= 1
(tolleranza di un ordine, per arrotondamenti e sconti). Con prezzo_medio 0 e' coerente
solo un ricavo 0 (un lancio che incassa zero e' un lancio misurato, e va scritto).
"""
from __future__ import annotations

from datetime import date, timedelta

from ._comune import Verdetto, leggi_artefatto, registro, valida_contro_schema

ID = "GATE-CNS-1"
ARTEFATTO = "consuntivo.json"
ORIGINI_AMMESSE = ("fornitore-pagamento", "esporto-piattaforma")
TOLLERANZA_ORDINI = 1


def _ramo():
    for a in registro()["artefatti"]:
        if a.get("gate") == ID:
            return a.get("se_fallisce")
    return None


def _data(s):
    try:
        return date.fromisoformat(str(s)[:10])
    except (ValueError, TypeError):
        return None


def carrello(offerta: dict):
    """(apertura, chiusura) del carrello, o (None, None) se non si leggono."""
    apertura = _data(offerta.get("data_apertura"))
    if apertura is None:
        return None, None
    chiusura = _data(offerta.get("data_chiusura"))
    if chiusura is None:
        durata = offerta.get("durata_carrello_gg")
        if not isinstance(durata, int) or durata <= 0:
            return apertura, None
        chiusura = apertura + timedelta(days=durata - 1)
    return apertura, chiusura


def esegui(dir_lancio: str, rete) -> Verdetto:
    ramo = _ramo()
    errori = valida_contro_schema(dir_lancio, ARTEFATTO)
    if errori:
        pref = "" if errori == ["assente"] else "schema: "
        return Verdetto(ID, False, [pref + e for e in errori], {}, ramo)
    c = leggi_artefatto(dir_lancio, ARTEFATTO)
    problemi: list[str] = []

    origine = c.get("origine") or {}
    if origine.get("tipo") not in ORIGINI_AMMESSE or not origine.get("riferimento"):
        problemi.append("origine %r non verificabile: il ricavo si legge dal fornitore di pagamento o da un "
                        "esporto della piattaforma (%s), mai dichiarato" % (origine, ", ".join(ORIGINI_AMMESSE)))

    apertura = chiusura = None
    periodo = c.get("periodo") or {}
    dal, al = _data(periodo.get("dal")), _data(periodo.get("al"))
    offerta = leggi_artefatto(dir_lancio, "offerta.json")
    if offerta is None:
        problemi.append("offerta.json assente: non si sa quali giorni il periodo deve coprire")
    else:
        apertura, chiusura = carrello(offerta)
        if apertura is None or chiusura is None:
            problemi.append("offerta.json senza date di carrello leggibili")
        elif dal is None or al is None:
            problemi.append("periodo %r non ha date leggibili" % periodo)
        else:
            if dal > apertura:
                problemi.append("periodo.dal %s posteriore all'apertura del carrello %s: giorni non coperti"
                                % (dal, apertura))
            if al < chiusura:
                problemi.append("periodo.al %s anteriore alla chiusura del carrello %s: giorni non coperti"
                                % (al, chiusura))

    ordini = c.get("ordini") or {}
    numero = ordini.get("numero")
    prezzo_medio = ordini.get("prezzo_medio")
    ricavo = c.get("ricavo_lordo")
    ordini_ricalcolati = None
    if isinstance(prezzo_medio, (int, float)) and isinstance(ricavo, (int, float)) and isinstance(numero, int):
        if prezzo_medio > 0:
            ordini_ricalcolati = int(round(ricavo / prezzo_medio))
        else:
            ordini_ricalcolati = 0 if ricavo == 0 else None
        if ordini_ricalcolati is None or abs(numero - ordini_ricalcolati) > TOLLERANZA_ORDINI:
            problemi.append("ordini.numero %r non coerente con ricavo_lordo %s / prezzo_medio %s = %s (tolleranza "
                            "%d ordine)" % (numero, ricavo, prezzo_medio, ordini_ricalcolati, TOLLERANZA_ORDINI))
    else:
        problemi.append("ordini o ricavo_lordo non numerici: %r / %r" % (ordini, ricavo))

    dati = {"ricavo_lordo": ricavo, "origine_tipo": origine.get("tipo"), "periodo": [str(dal), str(al)],
            "carrello": [str(apertura), str(chiusura)], "ordini_dichiarati": numero,
            "ordini_ricalcolati": ordini_ricalcolati}
    return Verdetto(ID, not problemi, problemi, dati, ramo if problemi else None)
