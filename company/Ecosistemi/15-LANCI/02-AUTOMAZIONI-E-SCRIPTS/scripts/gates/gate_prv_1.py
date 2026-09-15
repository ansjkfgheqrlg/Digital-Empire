# -*- coding: utf-8 -*-
"""GATE-PRV-1 — presidia previsione.json (ART-PRV).

Criterio eseguibile (registro, testuale):
    scenari ha esattamente [pessimista, atteso, ottimista]
    AND ogni scenario ha ricavo_lordo calcolato dalla formula dichiarata
    AND ogni assunzione ha stato in [misurato, assunto]
    AND nessuna assunzione con stato=='misurato' priva di fonte

La formula e' scritta nel file (02-PREVISIONE-E-DENARO.md §2.1) e il gate la RIFA':
`ricavo_lordo = pubblico_raggiungibile * tasso_visita * tasso_acquisto * prezzo`. Il
valutatore accetta solo formule a prodotto (`nome = fattore * fattore * ...`, con `*` o
`×`), dove ogni fattore e' un nome fra gli ingressi/il scenario oppure un numero: niente
eval, niente altri operatori. Confronto con tolleranza assoluta 0.01 (centesimi).

Dato da terzi: "pubblico e prezzo arrivano da ART-PUB e ART-OFF" — se accanto ci sono
pubblico.json e/o offerta.json (o offerta.PROPOSTA.json), il gate confronta gli ingressi
con quei file: una previsione che si sceglie il pubblico non e' una previsione.
"""
from __future__ import annotations

import re

from ._comune import ErroreArtefatto, Verdetto, leggi_artefatto, registro, valida_contro_schema

ID = "GATE-PRV-1"
ARTEFATTO = "previsione.json"
SCENARI = ("pessimista", "atteso", "ottimista")
STATI = ("misurato", "assunto")
TOLLERANZA = 0.01
_NOME = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")
_NUMERO = re.compile(r"^[0-9]+(\.[0-9]+)?$")


def _ramo():
    for a in registro()["artefatti"]:
        if a.get("gate") == ID:
            return a.get("se_fallisce")
    return None


def analizza_formula(formula) -> tuple[str | None, list[str], str | None]:
    """'ricavo_lordo = a * b * c' -> ('ricavo_lordo', ['a','b','c'], None) oppure
    (None, [], 'messaggio di errore'). Solo prodotti: nessun altro operatore."""
    if not isinstance(formula, str) or "=" not in formula:
        return None, [], "formula %r non ha la forma 'nome = fattore * fattore'" % (formula,)
    sinistra, destra = formula.split("=", 1)
    sinistra = sinistra.strip()
    if not _NOME.match(sinistra):
        return None, [], "formula: il membro sinistro %r non e' un nome" % sinistra
    if re.search(r"[+\-/()^]", destra):
        return None, [], "formula: ammesso solo il prodotto, trovato altro operatore in %r" % destra.strip()
    fattori = [f.strip() for f in re.split(r"[*×]", destra)]
    if not fattori or any(not f for f in fattori):
        return None, [], "formula: fattore vuoto in %r" % destra.strip()
    for f in fattori:
        if not (_NOME.match(f) or _NUMERO.match(f)):
            return None, [], "formula: fattore %r non e' un nome ne' un numero" % f
    return sinistra, fattori, None


def valuta_prodotto(fattori: list[str], variabili: dict) -> tuple[float | None, str | None]:
    """Il prodotto dei fattori, ogni nome risolto in `variabili`. Mai eval."""
    risultato = 1.0
    for f in fattori:
        if _NUMERO.match(f):
            v = float(f)
        elif f in variabili and isinstance(variabili[f], (int, float)) \
                and not isinstance(variabili[f], bool):
            v = float(variabili[f])
        else:
            return None, "fattore %r non risolvibile (non e' negli ingressi ne' nello scenario)" % f
        risultato *= v
    return risultato, None


def _leggi_accanto(dir_lancio, nome):
    """Un artefatto vicino, letto senza schema: None se assente o illeggibile."""
    try:
        return leggi_artefatto(dir_lancio, nome)
    except ErroreArtefatto:
        return None


def esegui(dir_lancio: str, rete) -> Verdetto:
    ramo = _ramo()
    errori = valida_contro_schema(dir_lancio, ARTEFATTO)
    if errori:
        pref = "" if errori == ["assente"] else "schema: "
        return Verdetto(ID, False, [pref + e for e in errori], {}, ramo)
    prv = leggi_artefatto(dir_lancio, ARTEFATTO)
    problemi: list[str] = []
    ingressi = prv.get("ingressi") or {}

    # 1. scenari esattamente {pessimista, atteso, ottimista}
    scenari = prv.get("scenari") or {}
    if set(scenari.keys()) != set(SCENARI):
        problemi.append("scenari: trovati %s, servono esattamente %s"
                        % (sorted(scenari.keys()), list(SCENARI)))

    # 2. ricavo_lordo ricalcolato dalla formula dichiarata
    obiettivo, fattori, err = analizza_formula(prv.get("formula"))
    ricalcolati = {}
    if err:
        problemi.append(err)
    else:
        if obiettivo != "ricavo_lordo":
            problemi.append("formula: calcola %r, deve calcolare 'ricavo_lordo'" % obiettivo)
        for nome in SCENARI:
            s = scenari.get(nome)
            if not isinstance(s, dict):
                continue
            variabili = dict(ingressi)
            variabili.update({k: v for k, v in s.items() if k != "ricavo_lordo"})
            atteso, e2 = valuta_prodotto(fattori, variabili)
            if e2:
                problemi.append("scenario %s: %s" % (nome, e2))
                continue
            ricalcolati[nome] = round(atteso, 4)
            dichiarato = s.get("ricavo_lordo")
            if not isinstance(dichiarato, (int, float)) or isinstance(dichiarato, bool) \
                    or abs(float(dichiarato) - atteso) > TOLLERANZA:
                problemi.append("scenario %s: ricavo_lordo dichiarato %r ma la formula da' %.2f"
                                % (nome, dichiarato, atteso))

    # 3-4. assunzioni: stato ammesso, 'misurato' sempre con fonte
    n_mis = n_ass = 0
    for a in prv.get("assunzioni", []):
        nome = a.get("nome", "?")
        st = a.get("stato")
        if st not in STATI:
            problemi.append("assunzione %s: stato %r non e' in [misurato, assunto]" % (nome, st))
            continue
        if st == "misurato":
            n_mis += 1
            fonte = a.get("fonte")
            if not isinstance(fonte, str) or not fonte.strip():
                problemi.append("assunzione %s: dichiarata 'misurato' ma senza fonte: un'assunzione "
                                "travestita da misura" % nome)
        else:
            n_ass += 1

    # dato da terzi: pubblico e prezzo confrontati con ART-PUB e ART-OFF se presenti accanto
    pub = _leggi_accanto(dir_lancio, "pubblico.json")
    if isinstance(pub, dict) and isinstance(pub.get("canali"), list):
        somma = sum(c.get("raggiungibili_verificati", 0) for c in pub["canali"]
                    if isinstance(c, dict) and (c.get("prova") or {}).get("tipo") != "nessuna")
        if ingressi.get("pubblico_raggiungibile") != somma:
            problemi.append("ingressi.pubblico_raggiungibile %r non coincide con pubblico.json "
                            "(somma dei canali con prova: %d)" % (ingressi.get("pubblico_raggiungibile"), somma))
    off = _leggi_accanto(dir_lancio, "offerta.json") or _leggi_accanto(dir_lancio, "offerta.PROPOSTA.json")
    if isinstance(off, dict) and isinstance(off.get("prezzo"), (int, float)):
        if ingressi.get("prezzo") != off["prezzo"]:
            problemi.append("ingressi.prezzo %r non coincide con il prezzo dell'offerta (%r)"
                            % (ingressi.get("prezzo"), off["prezzo"]))

    dati = {"scenari": sorted(scenari.keys()), "ricavo_ricalcolato": ricalcolati,
            "ricavo_dichiarato": {n: (scenari.get(n) or {}).get("ricavo_lordo") for n in SCENARI},
            "assunzioni_misurate": n_mis, "assunzioni_assunte": n_ass,
            "pubblico_raggiungibile": ingressi.get("pubblico_raggiungibile"),
            "prezzo": ingressi.get("prezzo")}
    return Verdetto(ID, not problemi, problemi, dati, ramo if problemi else None)
