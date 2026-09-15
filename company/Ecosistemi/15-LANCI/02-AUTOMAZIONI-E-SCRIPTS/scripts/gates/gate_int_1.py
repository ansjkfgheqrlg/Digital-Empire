# -*- coding: utf-8 -*-
"""GATE-INT-1 — presidia ricerca.json (ART-RIC).

Criterio eseguibile (registro, testuale):
    frasi.count >= 15
    AND ogni frase ha fonte.url
    AND campione_verificato.count >= 3
    AND ogni elemento del campione ha esito.raggiungibile == true

Dato da terzi: "il campione viene riaperto dal gate, non dall'analista" — ogni
`campione_verificato[].url` viene riaperto con `rete.codice_http` (vivo = codice < 400);
il `raggiungibile: true` scritto nel file e' confrontato, non creduto. Se per un elemento
`testo_ritrovato` e' true, il gate scarica `rete.testo(url)` e pretende che contenga il
testo di almeno una delle frasi che citano quell'url. Ogni url del campione deve essere
la fonte di almeno una frase: un campione che non campiona le frasi non prova niente.
"""
from __future__ import annotations

from ._comune import Verdetto, leggi_artefatto, registro, valida_contro_schema

ID = "GATE-INT-1"
ARTEFATTO = "ricerca.json"
MIN_FRASI = 15
MIN_CAMPIONE = 3


def _ramo():
    for a in registro()["artefatti"]:
        if a.get("gate") == ID:
            return a.get("se_fallisce")
    return None


def _vivo(codice):
    return isinstance(codice, int) and codice < 400


def _norm(s: str) -> str:
    return " ".join(s.split()).lower()


def esegui(dir_lancio: str, rete) -> Verdetto:
    ramo = _ramo()
    errori = valida_contro_schema(dir_lancio, ARTEFATTO)
    if errori:
        pref = "" if errori == ["assente"] else "schema: "
        return Verdetto(ID, False, [pref + e for e in errori], {}, ramo)
    ric = leggi_artefatto(dir_lancio, ARTEFATTO)
    problemi: list[str] = []

    # 1. frasi.count >= 15
    frasi = ric.get("frasi", [])
    if len(frasi) < MIN_FRASI:
        problemi.append("frasi: %d, servono almeno %d" % (len(frasi), MIN_FRASI))

    # 2. ogni frase ha fonte.url
    frasi_per_url: dict[str, list[str]] = {}
    senza_fonte = 0
    for i, f in enumerate(frasi):
        url = (f.get("fonte") or {}).get("url")
        if not isinstance(url, str) or not url.strip():
            senza_fonte += 1
            problemi.append("frase %d senza fonte.url: %r" % (i + 1, (f.get("testo") or "")[:60]))
            continue
        frasi_per_url.setdefault(url, []).append(f.get("testo") or "")

    # 3. campione_verificato.count >= 3
    campione = ric.get("campione_verificato", [])
    if len(campione) < MIN_CAMPIONE:
        problemi.append("campione_verificato: %d elementi, servono almeno %d"
                        % (len(campione), MIN_CAMPIONE))

    # 4. ogni elemento del campione raggiungibile: dichiarato E riaperto dal gate
    riaperti = {}
    testi_controllati = 0
    for c in campione:
        url = c.get("url")
        if not isinstance(url, str) or not url.strip():
            problemi.append("campione: url vuoto o non stringa: %r" % url)
            continue
        if c.get("raggiungibile") is not True:
            problemi.append("campione %s: raggiungibile dichiarato %r, serve true"
                            % (url, c.get("raggiungibile")))
        codice = rete.codice_http(url)
        riaperti[url] = codice
        if not _vivo(codice):
            problemi.append("campione %s: irraggiungibile alla riapertura del gate (%s)"
                            % (url, "nessuna risposta" if codice is None else "codice %s" % codice))
            continue
        if url not in frasi_per_url:
            problemi.append("campione %s: non e' la fonte di nessuna frase" % url)
        if c.get("testo_ritrovato") is True:
            testi_controllati += 1
            corpo = rete.testo(url)
            attese = [t for t in frasi_per_url.get(url, []) if t]
            if not attese:
                problemi.append("campione %s: testo_ritrovato=true ma nessuna frase cita questo url"
                                % url)
            elif corpo is None or not any(_norm(t) in _norm(corpo) for t in attese):
                problemi.append("campione %s: testo_ritrovato=true ma la pagina riaperta non "
                                "contiene nessuna delle %d frasi che la citano" % (url, len(attese)))

    dati = {"frasi": len(frasi), "frasi_senza_fonte": senza_fonte,
            "fonti_distinte": len(frasi_per_url), "campione": len(campione),
            "campione_riaperto": riaperti,
            "campione_vivo": sum(1 for c in riaperti.values() if _vivo(c)),
            "testi_controllati": testi_controllati}
    return Verdetto(ID, not problemi, problemi, dati, ramo if problemi else None)
