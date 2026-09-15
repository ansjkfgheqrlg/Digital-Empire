# -*- coding: utf-8 -*-
"""GATE-PRD-1 — presidia certificato.json (ART-CRT).

Criterio eseguibile (registro, testuale):
    bandiere_rosse[].presente tutte false
    AND file_prodotto esiste e dimensione>0
    AND ogni link del prodotto testato con esito registrato
    AND (modalita=='integrale' OR (modalita=='retroattiva' AND debito_collaudo dichiarato))

Dato da terzi: "i link sono testati dal gate, non dichiarati dal produttore" — ogni
`link_testati[].url` viene RIAPERTO tramite `rete.codice_http`; un codice registrato nel
file non basta. Vivo = codice presente e < 400.

`file_prodotto.percorso` puo' essere assoluto o relativo alla radice del repository
(RADICE di _comune). Il `byte` dichiarato non e' confrontato con quello reale (il file del
prodotto puo' cambiare legittimamente): finisce nei dati, come misura.
"""
from __future__ import annotations

import os

from ._comune import RADICE, Verdetto, leggi_artefatto, registro, valida_contro_schema

ID = "GATE-PRD-1"
ARTEFATTO = "certificato.json"
MODALITA = ("integrale", "retroattiva")


def _ramo():
    for a in registro()["artefatti"]:
        if a.get("gate") == ID:
            return a.get("se_fallisce")
    return None


def _percorso_prodotto(rel):
    if not isinstance(rel, str) or not rel.strip():
        return None
    if os.path.isabs(rel):
        return rel
    return os.path.join(RADICE, *rel.replace("\\", "/").split("/"))


def _vivo(codice):
    return isinstance(codice, int) and codice < 400


def esegui(dir_lancio: str, rete) -> Verdetto:
    ramo = _ramo()
    errori = valida_contro_schema(dir_lancio, ARTEFATTO)
    if errori:
        pref = "" if errori == ["assente"] else "schema: "
        return Verdetto(ID, False, [pref + e for e in errori], {}, ramo)
    crt = leggi_artefatto(dir_lancio, ARTEFATTO)
    problemi: list[str] = []

    # 1. bandiere rosse
    presenti = [b.get("id", "?") for b in crt.get("bandiere_rosse", []) if b.get("presente") is not False]
    if presenti:
        problemi.append("bandiere rosse presenti (%d): %s" % (len(presenti), ", ".join(presenti)))

    # 2. il file del prodotto
    fp = crt.get("file_prodotto") or {}
    p = _percorso_prodotto(fp.get("percorso"))
    byte_reali = None
    if p is None or not os.path.isfile(p):
        problemi.append("file_prodotto.percorso %r non esiste (ne' assoluto ne' relativo a %s)"
                        % (fp.get("percorso"), RADICE))
    else:
        byte_reali = os.path.getsize(p)
        if byte_reali <= 0:
            problemi.append("file_prodotto %r ha dimensione 0 byte" % fp.get("percorso"))

    # 3. ogni link testato con esito registrato E riaperto dal gate
    riaperti = {}
    for l in crt.get("link_testati", []):
        url = l.get("url")
        if not isinstance(url, str) or not url.strip():
            problemi.append("link_testati: url vuoto o non stringa: %r" % url)
            continue
        if l.get("codice") is None:
            problemi.append("link %s: esito non registrato (codice null): va testato" % url)
        codice = rete.codice_http(url)
        riaperti[url] = codice
        if not _vivo(codice):
            problemi.append("link morto: %s risponde %s alla riapertura del gate"
                            % (url, "irraggiungibile" if codice is None else codice))
        elif l.get("codice") is not None and l.get("codice") != codice:
            problemi.append("link %s: registrato %s ma riaperto %s: il certificato e' stantio"
                            % (url, l.get("codice"), codice))

    # 4. modalita'
    m = crt.get("modalita")
    if m not in MODALITA:
        problemi.append("modalita %r non ammessa (integrale | retroattiva)" % m)
    elif m == "retroattiva":
        deb = crt.get("debito_collaudo")
        if not isinstance(deb, str) or not deb.strip():
            problemi.append("modalita retroattiva senza debito_collaudo dichiarato: un'eccezione "
                            "senza debito scritto diventa la regola")

    if crt.get("esito") == "non-consegnabile":
        problemi.append("esito dichiarato 'non-consegnabile' dal produttore")

    dati = {"bandiere_presenti": presenti, "byte_dichiarati": fp.get("byte"),
            "byte_reali": byte_reali, "link_riaperti": riaperti,
            "link_vivi": sum(1 for c in riaperti.values() if _vivo(c)),
            "modalita": m}
    return Verdetto(ID, not problemi, problemi, dati, ramo if problemi else None)
