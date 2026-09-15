# -*- coding: utf-8 -*-
"""GATE-EDT-1 — presidia editoriale.json (ART-EDT).

Criterio eseguibile (registro, testuale):
    nessuna riga con campi obbligatori vuoti
    AND ogni contenuto ha destinazione risolvibile in ART-FNL
    AND ogni giorno del carrello ha almeno un contenuto

"Risolvibile in ART-FNL": la destinazione e' l'url o il `ruolo` di una pagina di
funnel.json del lancio (dato_da_terzi: verificata contro il funnel reale, non contro una
descrizione). Il carrello va da offerta.data_apertura a offerta.data_chiusura inclusi;
se data_chiusura manca (e' facoltativa nello schema) si usa
data_apertura + durata_carrello_gg - 1. I giorni scoperti sono ricalcolati e riportati
in `dati`, il campo `giorni_scoperti` del file non viene creduto.
"""
from __future__ import annotations

from datetime import date, timedelta

from ._comune import Verdetto, leggi_artefatto, registro, valida_contro_schema

ID = "GATE-EDT-1"
ARTEFATTO = "editoriale.json"
CAMPI_OBBLIGATORI = ("id", "data_uscita", "canale", "formato", "destinazione", "stato")


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


def giorni_carrello(offerta: dict) -> list[date]:
    """Tutti i giorni fra apertura e chiusura inclusi; [] se le date non si leggono."""
    apertura = _data(offerta.get("data_apertura"))
    if apertura is None:
        return []
    chiusura = _data(offerta.get("data_chiusura"))
    if chiusura is None:
        durata = offerta.get("durata_carrello_gg")
        if not isinstance(durata, int) or durata <= 0:
            return []
        chiusura = apertura + timedelta(days=durata - 1)
    if chiusura < apertura:
        return []
    return [apertura + timedelta(days=i) for i in range((chiusura - apertura).days + 1)]


def esegui(dir_lancio: str, rete) -> Verdetto:
    ramo = _ramo()
    errori = valida_contro_schema(dir_lancio, ARTEFATTO)
    if errori:
        pref = "" if errori == ["assente"] else "schema: "
        return Verdetto(ID, False, [pref + e for e in errori], {}, ramo)
    ed = leggi_artefatto(dir_lancio, ARTEFATTO)
    problemi: list[str] = []

    funnel = leggi_artefatto(dir_lancio, "funnel.json")
    destinazioni = set()
    if funnel is None:
        problemi.append("funnel.json assente: nessuna destinazione e' risolvibile")
    else:
        for p in funnel.get("pagine", []):
            for k in ("url", "ruolo"):
                if p.get(k):
                    destinazioni.add(p[k])

    offerta = leggi_artefatto(dir_lancio, "offerta.json")
    giorni = giorni_carrello(offerta) if offerta else []
    if not giorni:
        problemi.append("offerta.json assente o senza date leggibili: il carrello non ha giorni")

    righe_incomplete = 0
    non_risolte = 0
    giorni_coperti = set()
    for i, c in enumerate(ed.get("contenuti", [])):
        cid = c.get("id") or "#%d" % i
        vuoti = [k for k in CAMPI_OBBLIGATORI if c.get(k) in (None, "")]
        if vuoti:
            righe_incomplete += 1
            problemi.append("contenuto %s: campi obbligatori vuoti: %s" % (cid, ", ".join(vuoti)))
        dest = c.get("destinazione")
        if dest and funnel is not None and dest not in destinazioni:
            non_risolte += 1
            problemi.append("contenuto %s: destinazione %r non e' ne' url ne' ruolo di una pagina di funnel.json"
                            % (cid, dest))
        g = _data(c.get("data_uscita"))
        if g is not None:
            giorni_coperti.add(g)

    scoperti = [g for g in giorni if g not in giorni_coperti]
    for g in scoperti:
        problemi.append("giorno %s del carrello senza nessun contenuto" % g.isoformat())

    dati = {"contenuti": len(ed.get("contenuti", [])), "righe_incomplete": righe_incomplete,
            "destinazioni_non_risolte": non_risolte, "giorni_carrello": len(giorni),
            "giorni_scoperti": [g.isoformat() for g in scoperti]}
    return Verdetto(ID, not problemi, problemi, dati, ramo if problemi else None)
