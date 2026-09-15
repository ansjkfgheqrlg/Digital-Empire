# -*- coding: utf-8 -*-
"""GATE-OFF-1 — presidia offerta.json (ART-OFF), l'artefatto firmato da una persona.

Criterio eseguibile (registro, testuale):
    prezzo e' numero > 0
    AND prezzo non in lista_valori_evasivi
    AND data_apertura e' data futura valida
    AND durata_carrello_gg > 0
    AND ruolo_prodotto in [vendita, acquisizione-contatti]
    AND firma.canale in canali_firma_ammessi
    AND firma.proposta_hash == sha256(file proposta corrente)
    AND somma(bonus[].valore dove fonte_valore != null) usata per rapporto_valore_prezzo

Caso normale, non errore: `offerta.json` assente ma `offerta.PROPOSTA.json` presente ->
boccia con "offerta non firmata: esiste solo la proposta". Il lancio aspetta una persona.

`lista_valori_evasivi` e' quella di 03-FLUSSO-OFFERTA.md §8: "NON LO SO", "da definire",
"TBD" (confronto senza maiuscole/spazi) e 0 quando ruolo_prodotto e' 'vendita'.

L'impronta: `firma.proposta_impronta` deve essere il sha256 del file
`offerta.PROPOSTA.json` accanto a `offerta.json` (la "proposta corrente"). Se la
proposta manca, la firma non e' verificabile e il gate boccia; se e' stata rigenerata
dopo la firma, l'impronta non torna e la firma decade (§6 del documento 03).

Il rapporto valore/prezzo e' RICALCOLATO: (prezzo + somma dei bonus con fonte_valore non
nulla) / prezzo, e deve essere >= `struttura.soglia_rapporto_minima` (3 se assente). I
campi `valore_dichiarato` e `rapporto_valore_prezzo` sono confrontati col ricalcolo, mai
creduti. Il "valore del prodotto" e' il prezzo stesso (come nella proposta reale di
manuale-claude-code, dove valore_dichiarato = prezzo con bonus a zero).
"""
from __future__ import annotations

import os
from datetime import date, datetime

from ._comune import (Verdetto, leggi_artefatto, percorso_artefatto, registro, sha256_file,
                      valida_contro_schema)

ID = "GATE-OFF-1"
ARTEFATTO = "offerta.json"
PROPOSTA = "offerta.PROPOSTA.json"
RUOLI = ("vendita", "acquisizione-contatti")
SOGLIA_RAPPORTO_DEFAULT = 3
VALORI_EVASIVI_TESTO = ("non lo so", "da definire", "tbd")


def _ramo():
    for a in registro()["artefatti"]:
        if a.get("gate") == ID:
            return a.get("se_fallisce")
    return None


def _numero(x) -> bool:
    return isinstance(x, (int, float)) and not isinstance(x, bool)


def _data(s):
    """date da ISO 'YYYY-MM-DD' o da 'gg/mm/aaaa'; None se non si legge."""
    if not isinstance(s, str):
        return None
    s = s.strip()
    if len(s) >= 10 and s[4] == "-":
        try:
            return date.fromisoformat(s[:10])
        except ValueError:
            return None
    try:
        return datetime.strptime(s, "%d/%m/%Y").date()
    except ValueError:
        return None


def _evasivo(prezzo, ruolo) -> bool:
    if isinstance(prezzo, str):
        return " ".join(prezzo.split()).lower() in VALORI_EVASIVI_TESTO
    if _numero(prezzo):
        return prezzo == 0 and ruolo == "vendita"
    return False


def esegui(dir_lancio: str, rete) -> Verdetto:
    ramo = _ramo()
    p_proposta = percorso_artefatto(dir_lancio, PROPOSTA)
    if not os.path.exists(percorso_artefatto(dir_lancio, ARTEFATTO)):
        if os.path.exists(p_proposta):
            return Verdetto(ID, False, ["offerta non firmata: esiste solo la proposta (%s); serve "
                                        "la firma di una persona, nessun agente puo' scriverla" % PROPOSTA],
                            {"proposta_sha256": sha256_file(p_proposta)}, ramo)
        return Verdetto(ID, False, ["assente"], {}, ramo)
    errori = valida_contro_schema(dir_lancio, ARTEFATTO)
    if errori:
        return Verdetto(ID, False, ["schema: " + e for e in errori], {}, ramo)
    off = leggi_artefatto(dir_lancio, ARTEFATTO)
    problemi: list[str] = []
    oggi = date.today()

    # 1. prezzo numero > 0
    prezzo = off.get("prezzo")
    ruolo = off.get("ruolo_prodotto")
    if not _numero(prezzo) or prezzo <= 0:
        problemi.append("prezzo %r non e' un numero > 0" % (prezzo,))
    # 2. non in lista_valori_evasivi
    if _evasivo(prezzo, ruolo):
        problemi.append("prezzo %r e' un valore evasivo (03-FLUSSO-OFFERTA §8): sembra una "
                        "risposta e non lo e'" % (prezzo,))
    # 3. data_apertura futura valida
    d_ap = _data(off.get("data_apertura"))
    if d_ap is None:
        problemi.append("data_apertura %r non e' una data valida (ISO o gg/mm/aaaa)"
                        % (off.get("data_apertura"),))
    elif d_ap <= oggi:
        problemi.append("data_apertura %s non e' futura (oggi %s)" % (d_ap, oggi))
    # 4. durata_carrello_gg > 0
    durata = off.get("durata_carrello_gg")
    if not isinstance(durata, int) or isinstance(durata, bool) or durata <= 0:
        problemi.append("durata_carrello_gg %r non e' un intero > 0" % (durata,))
    # 5. ruolo_prodotto ammesso
    if ruolo not in RUOLI:
        problemi.append("ruolo_prodotto %r non e' in %s" % (ruolo, list(RUOLI)))
    # 6. firma.canale in canali_firma_ammessi (dal registro)
    firma = off.get("firma") or {}
    canali = list(registro().get("canali_firma_ammessi") or [])
    if firma.get("canale") not in canali:
        problemi.append("firma.canale %r non e' fra i canali ammessi %s: la firma non vale"
                        % (firma.get("canale"), canali))
    # 7. impronta della proposta corrente
    impronta_proposta = None
    if not os.path.exists(p_proposta):
        problemi.append("proposta assente: manca %s accanto a offerta.json, l'impronta della firma "
                        "non e' verificabile" % PROPOSTA)
    else:
        impronta_proposta = sha256_file(p_proposta)
        if firma.get("proposta_impronta") != impronta_proposta:
            problemi.append("firma.proposta_impronta non corrisponde alla proposta corrente "
                            "(firmata %s..., corrente %s...): la proposta e' stata rigenerata dopo la "
                            "firma, la firma decade" % (str(firma.get("proposta_impronta"))[:12],
                                                        impronta_proposta[:12]))
    # 8. rapporto valore/prezzo ricalcolato dai bonus con fonte
    st = off.get("struttura") or {}
    bonus = st.get("bonus") or []
    somma_bonus = sum(b.get("valore", 0) for b in bonus
                      if b.get("fonte_valore") is not None and _numero(b.get("valore")))
    bonus_senza_fonte = [b.get("nome") for b in bonus if b.get("fonte_valore") is None]
    soglia = st.get("soglia_rapporto_minima", SOGLIA_RAPPORTO_DEFAULT)
    if not _numero(soglia):
        soglia = SOGLIA_RAPPORTO_DEFAULT
    valore = rapporto = None
    if _numero(prezzo) and prezzo > 0:
        valore = prezzo + somma_bonus
        rapporto = valore / prezzo
        if _numero(st.get("valore_dichiarato")) and abs(st["valore_dichiarato"] - valore) > 0.01:
            problemi.append("struttura.valore_dichiarato %r ma ricalcolato %.2f (prezzo + bonus con "
                            "fonte)" % (st.get("valore_dichiarato"), valore))
        if _numero(st.get("rapporto_valore_prezzo")) and abs(st["rapporto_valore_prezzo"] - rapporto) > 0.01:
            problemi.append("struttura.rapporto_valore_prezzo %r ma ricalcolato %.2f"
                            % (st.get("rapporto_valore_prezzo"), rapporto))
        if rapporto < soglia:
            problemi.append("rapporto valore/prezzo ricalcolato %.2f < soglia %s (bonus con fonte: "
                            "%.2f; senza fonte, che valgono zero: %s)"
                            % (rapporto, soglia, somma_bonus, bonus_senza_fonte or "nessuno"))

    dati = {"prezzo": prezzo, "data_apertura": str(d_ap) if d_ap else None,
            "durata_carrello_gg": durata, "canale_firma": firma.get("canale"),
            "proposta_sha256": impronta_proposta, "somma_bonus_con_fonte": somma_bonus,
            "bonus_senza_fonte": bonus_senza_fonte, "valore_ricalcolato": valore,
            "rapporto_ricalcolato": round(rapporto, 4) if rapporto is not None else None,
            "soglia": soglia}
    return Verdetto(ID, not problemi, problemi, dati, ramo if problemi else None)
