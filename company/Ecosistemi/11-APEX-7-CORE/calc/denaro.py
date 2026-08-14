"""
APEX-7 Calc Layer — denaro: rendimenti, costi invisibili, royalty, guadagni.

Due errori dello zip `apex7_orchestrator` sono corretti qui, ed erano entrambi
capaci di ribaltare una conclusione:

1. **Le tasse si pagano sulla plusvalenza NOMINALE**, non sul rendimento reale.
   In Italia non esiste indicizzazione all'inflazione: si tassa il guadagno in
   euro correnti. Lo zip tassava il rendimento reale, sbagliando del +2,4% a 10
   anni e del -11,4% a 30 (cambiava pure segno).
2. **Il confronto col risk-free deve essere OMOGENEO.** Lo zip metteva un
   valore atteso netto di tasse e inflazione contro un BTP lordo nominale: sul
   suo stesso dossier concludeva che un ETF All-World perdeva contro il BTP di
   10.812 EUR, mentre a parita' di trattamento ne guadagnava 25.373.

In piu': il capitale finale non puo' essere negativo per un investimento
long-only, e qui e' un vincolo esplicito, non una speranza.
"""
from __future__ import annotations

import math
from typing import Any, Dict, List, Mapping

from .core import Assunzione, ErroreCalcolo, Parametro, SafeMath, num, registra

P = Parametro

# Valori di riferimento. Sono DEFAULT DICHIARATI, non misure: ogni risultato che
# li usa se li porta dietro nella lista `assunzioni`.
RIFERIMENTI: Dict[str, Dict[str, Any]] = {
    "inflazione_annua": {"valore": 0.025, "fonte": "ancora storica EU CPI ~2.5%"},
    "risk_free_annuo": {"valore": 0.038, "fonte": "rendimento BTP 10y di riferimento"},
    "tassa_capital_gain": {"valore": 0.26, "fonte": "aliquota IT su rendite finanziarie 26%"},
    "tassa_titoli_stato": {"valore": 0.125, "fonte": "aliquota IT agevolata titoli di Stato 12.5%"},
}


def _netto_reale(capitale: float, tasso: float, anni: float, commissioni: float,
                 tassa: float, inflazione: float) -> Dict[str, float]:
    """Il calcolo corretto, usato da tutti i moduli di questo file."""
    tasso_netto_comm = tasso - commissioni
    nominale = capitale * SafeMath.pow(1.0 + tasso_netto_comm, anni, capitale)
    plusvalenza = max(0.0, nominale - capitale)          # si tassa solo il guadagno
    imposta = plusvalenza * tassa                        # ...e sul NOMINALE
    netto_nominale = nominale - imposta
    deflatore = SafeMath.pow(1.0 + inflazione, anni, 1.0)
    netto_reale = SafeMath.div(netto_nominale, deflatore, netto_nominale)
    return {
        "nominale_lordo": nominale,
        "plusvalenza_nominale": plusvalenza,
        "imposta": imposta,
        "netto_nominale": netto_nominale,
        "netto_reale": netto_reale,
    }


@registra("rendimento", "denaro",
          "Valore finale di un capitale, netto di commissioni, tasse e inflazione", [
              P("capitale", "capitale investito", unita="EUR"),
              P("anni", "orizzonte in anni"),
              P("rendimento_annuo", "rendimento lordo atteso in decimale (0.07 = 7%)"),
              P("commissioni_annue", "costo annuo in decimale", obbligatorio=False, default=0.0),
              P("tassa", "aliquota sulla plusvalenza in decimale", obbligatorio=False, default=0.26),
              P("inflazione_annua", "inflazione in decimale", obbligatorio=False, default=0.025)])
def rendimento(v: Mapping[str, Any]) -> Dict[str, Any]:
    c = num(v, "capitale", minimo=0.0)
    anni = num(v, "anni", minimo=1e-9)
    r = num(v, "rendimento_annuo")
    comm = num(v, "commissioni_annue", default=0.0, minimo=0.0, massimo=1.0)
    tassa = num(v, "tassa", default=RIFERIMENTI["tassa_capital_gain"]["valore"],
                minimo=0.0, massimo=1.0)
    infl = num(v, "inflazione_annua", default=RIFERIMENTI["inflazione_annua"]["valore"])

    d = _netto_reale(c, r, anni, comm, tassa, infl)
    cagr_reale = (SafeMath.pow(SafeMath.div(d["netto_reale"], c, 1.0), 1.0 / anni, 1.0) - 1.0) * 100.0
    return {
        **d,
        "guadagno_reale": d["netto_reale"] - c,
        "guadagno_reale_pct": SafeMath.variazione_pct(c, d["netto_reale"]) if c else 0.0,
        "cagr_reale_pct": cagr_reale,
        "potere_acquisto_eroso": d["netto_nominale"] - d["netto_reale"],
    }


@registra("costi_invisibili", "denaro",
          "Quanto si perde per inflazione, commissioni e tasse, voce per voce", [
              P("capitale", "capitale investito", unita="EUR"),
              P("anni", "orizzonte in anni"),
              P("rendimento_annuo", "rendimento lordo atteso in decimale"),
              P("commissioni_annue", "costo annuo in decimale", obbligatorio=False, default=0.0),
              P("tassa", "aliquota sulla plusvalenza", obbligatorio=False, default=0.26),
              P("inflazione_annua", "inflazione in decimale", obbligatorio=False, default=0.025)])
def costi_invisibili(v: Mapping[str, Any]) -> Dict[str, Any]:
    c = num(v, "capitale", minimo=0.0)
    anni = num(v, "anni", minimo=1e-9)
    r = num(v, "rendimento_annuo")
    comm = num(v, "commissioni_annue", default=0.0, minimo=0.0, massimo=1.0)
    tassa = num(v, "tassa", default=0.26, minimo=0.0, massimo=1.0)
    infl = num(v, "inflazione_annua", default=0.025)

    con_comm = _netto_reale(c, r, anni, comm, tassa, infl)
    senza_comm = _netto_reale(c, r, anni, 0.0, tassa, infl)
    senza_nulla = c * SafeMath.pow(1.0 + r, anni, c)

    costo_commissioni = max(0.0, senza_comm["nominale_lordo"] - con_comm["nominale_lordo"])
    costo_tasse = con_comm["imposta"]
    costo_inflazione = con_comm["netto_nominale"] - con_comm["netto_reale"]
    totale = costo_commissioni + costo_tasse + costo_inflazione

    return {
        "costo_commissioni": costo_commissioni,
        "costo_tasse": costo_tasse,
        "costo_inflazione": costo_inflazione,
        "costo_totale": totale,
        "lordo_teorico": senza_nulla,
        "netto_reale": con_comm["netto_reale"],
        "quota_erosa_pct": SafeMath.pct(totale, senza_nulla) if senza_nulla else 0.0,
    }


@registra("confronto_risk_free", "denaro",
          "Confronto OMOGENEO fra un investimento e l'alternativa senza rischio", [
              P("capitale", "capitale investito", unita="EUR"),
              P("anni", "orizzonte in anni"),
              P("rendimento_annuo", "rendimento lordo atteso dell'investimento"),
              P("commissioni_annue", "costo annuo", obbligatorio=False, default=0.0),
              P("tassa", "aliquota sull'investimento", obbligatorio=False, default=0.26),
              P("risk_free_annuo", "rendimento senza rischio", obbligatorio=False, default=0.038),
              P("tassa_risk_free", "aliquota sul risk-free", obbligatorio=False, default=0.125),
              P("inflazione_annua", "inflazione", obbligatorio=False, default=0.025)])
def confronto_risk_free(v: Mapping[str, Any]) -> Dict[str, Any]:
    c = num(v, "capitale", minimo=0.0)
    anni = num(v, "anni", minimo=1e-9)
    r = num(v, "rendimento_annuo")
    comm = num(v, "commissioni_annue", default=0.0, minimo=0.0, massimo=1.0)
    tassa = num(v, "tassa", default=0.26, minimo=0.0, massimo=1.0)
    rf = num(v, "risk_free_annuo", default=RIFERIMENTI["risk_free_annuo"]["valore"])
    tassa_rf = num(v, "tassa_risk_free", default=RIFERIMENTI["tassa_titoli_stato"]["valore"],
                   minimo=0.0, massimo=1.0)
    infl = num(v, "inflazione_annua", default=0.025)

    # Entrambi netti di tasse e inflazione: e' l'unico confronto che significhi qualcosa.
    inv = _netto_reale(c, r, anni, comm, tassa, infl)["netto_reale"]
    sicuro = _netto_reale(c, rf, anni, 0.0, tassa_rf, infl)["netto_reale"]
    premio = inv - sicuro

    return {
        "investimento_netto_reale": inv,
        "risk_free_netto_reale": sicuro,
        "premio_al_rischio": premio,
        "premio_al_rischio_pct": SafeMath.pct(premio, sicuro) if sicuro else 0.0,
        "conviene_rischiare": premio > 0,
        "soglia_indifferenza_annua_pct": (
            SafeMath.pow(SafeMath.div(sicuro, c, 1.0), 1.0 / anni, 1.0) - 1.0) * 100.0,
    }


@registra("rischio", "denaro", "Perdita massima, rapporto rischio/rendimento e VaR", [
    P("capitale", "capitale esposto", unita="EUR"),
    P("anni", "orizzonte in anni"),
    P("rendimento_annuo", "rendimento atteso in decimale"),
    P("perdita_massima_pct", "drawdown massimo tollerato in decimale (0.20 = 20%)"),
    P("risk_free_annuo", "rendimento senza rischio", obbligatorio=False, default=0.038)])
def rischio(v: Mapping[str, Any]) -> Dict[str, Any]:
    c = num(v, "capitale", minimo=0.0)
    anni = num(v, "anni", minimo=1e-9)
    r = num(v, "rendimento_annuo")
    # vincolo esplicito: non si puo' perdere piu' del capitale investito
    dd = num(v, "perdita_massima_pct", minimo=0.0, massimo=1.0)
    rf = num(v, "risk_free_annuo", default=0.038)

    perdita = c * dd
    guadagno = c * r * anni
    sigma_annua = dd / 1.645 if dd > 0 else 0.0    # dd letto come quantile 95%
    var95 = min(c, c * 1.645 * sigma_annua * math.sqrt(anni))

    return {
        "perdita_massima": perdita,
        "capitale_minimo_residuo": max(0.0, c - perdita),
        "guadagno_potenziale": guadagno,
        "rapporto_rendimento_rischio": SafeMath.div(guadagno, perdita, 0.0),
        "sharpe_approssimato": SafeMath.div(r - rf, sigma_annua, 0.0) if sigma_annua else 0.0,
        "var_95": var95,
        "var_95_pct": SafeMath.pct(var95, c) if c else 0.0,
        "rischio_asimmetrico": SafeMath.div(guadagno, perdita, 0.0) < 1.0,
    }


# ─────────────────────────────────────────────────────────────────────────────
# Royalty e guadagni
# ─────────────────────────────────────────────────────────────────────────────

@registra("royalty", "guadagni",
          "Guadagno da royalty su N unita' vendute, al netto di costi fissi e per unita'", [
              P("prezzo", "prezzo di vendita al pubblico", unita="EUR"),
              P("aliquota_royalty", "quota che resta all'autore in decimale (0.70 = 70%)"),
              P("unita_vendute", "quante unita'"),
              P("costo_per_unita", "costo di consegna/stampa per unita'",
                obbligatorio=False, default=0.0),
              P("costi_fissi", "costi una tantum (copertina, editing, ads)",
                obbligatorio=False, default=0.0)])
def royalty(v: Mapping[str, Any]) -> Dict[str, Any]:
    prezzo = num(v, "prezzo", minimo=0.0)
    aliq = num(v, "aliquota_royalty", minimo=0.0, massimo=1.0)
    unita = num(v, "unita_vendute", minimo=0.0)
    costo_u = num(v, "costo_per_unita", default=0.0, minimo=0.0)
    fissi = num(v, "costi_fissi", default=0.0, minimo=0.0)

    per_unita = prezzo * aliq - costo_u
    lordo = per_unita * unita
    netto = lordo - fissi
    pareggio = SafeMath.div(fissi, per_unita, 0.0) if per_unita > 0 else float("inf")

    out = {
        "royalty_per_unita": per_unita,
        "guadagno_lordo": lordo,
        "guadagno_netto": netto,
        "costi_fissi": fissi,
        "margine_pct": SafeMath.pct(per_unita, prezzo) if prezzo else 0.0,
        "in_utile": netto > 0,
    }
    if per_unita > 0:
        out["unita_per_pareggio"] = math.ceil(pareggio)
        out["unita_mancanti_al_pareggio"] = max(0.0, math.ceil(pareggio) - unita)
    else:
        out["unita_per_pareggio"] = -1.0   # -1 = irraggiungibile: ogni copia perde denaro
    return out


@registra("royalty_kdp", "guadagni",
          "Royalty Amazon KDP: ebook 70%/35% con costo di consegna, oppure paperback", [
              P("prezzo", "prezzo di listino", unita="EUR"),
              P("formato", "1 = ebook, 0 = cartaceo", obbligatorio=False, default=1.0),
              P("peso_file_mb", "dimensione del file, per il costo di consegna (solo ebook)",
                obbligatorio=False, default=1.0),
              P("costo_consegna_per_mb", "costo di consegna per MB",
                obbligatorio=False, default=0.15),
              P("costo_stampa", "costo di stampa per copia (solo cartaceo)",
                obbligatorio=False, default=0.0),
              P("unita_vendute", "copie vendute", obbligatorio=False, default=1.0),
              P("costi_fissi", "costi una tantum", obbligatorio=False, default=0.0)])
def royalty_kdp(v: Mapping[str, Any]) -> Dict[str, Any]:
    prezzo = num(v, "prezzo", minimo=0.0)
    ebook = num(v, "formato", default=1.0) >= 0.5
    unita = num(v, "unita_vendute", default=1.0, minimo=0.0)
    fissi = num(v, "costi_fissi", default=0.0, minimo=0.0)

    if ebook:
        mb = num(v, "peso_file_mb", default=1.0, minimo=0.0)
        costo_mb = num(v, "costo_consegna_per_mb", default=0.15, minimo=0.0)
        # La fascia 70% e' quella dichiarata da KDP: fuori da 2.99-9.99 si scende al 35%,
        # e nel 35% il costo di consegna non viene addebitato.
        in_fascia = 2.99 <= prezzo <= 9.99
        aliquota = 0.70 if in_fascia else 0.35
        consegna = mb * costo_mb if in_fascia else 0.0
        per_unita = prezzo * aliquota - consegna
        dettaglio = {"aliquota_applicata": aliquota, "costo_consegna": consegna,
                     "in_fascia_70": in_fascia}
    else:
        stampa = num(v, "costo_stampa", default=0.0, minimo=0.0)
        aliquota = 0.60
        per_unita = prezzo * aliquota - stampa
        dettaglio = {"aliquota_applicata": aliquota, "costo_stampa": stampa,
                     "in_fascia_70": False}

    lordo = per_unita * unita
    netto = lordo - fissi
    out = {
        **dettaglio,
        "royalty_per_copia": per_unita,
        "guadagno_lordo": lordo,
        "guadagno_netto": netto,
        "margine_pct": SafeMath.pct(per_unita, prezzo) if prezzo else 0.0,
        "in_utile": netto > 0,
    }
    if per_unita > 0:
        out["copie_per_pareggio"] = math.ceil(SafeMath.div(fissi, per_unita, 0.0))
    else:
        out["copie_per_pareggio"] = -1.0
    return out


@registra("prezzo_ottimale", "guadagni",
          "Prezzo che massimizza il guadagno, data l'elasticita' della domanda", [
              P("prezzo_attuale", "prezzo di partenza", unita="EUR"),
              P("unita_attuali", "unita' vendute al prezzo attuale"),
              P("elasticita", "variazione % della domanda per 1% di prezzo (di norma negativa)"),
              P("aliquota_royalty", "quota che resta all'autore", obbligatorio=False, default=0.70),
              P("costo_per_unita", "costo per unita'", obbligatorio=False, default=0.0),
              P("prezzo_min", "prezzo minimo esplorabile", obbligatorio=False, default=0.99),
              P("prezzo_max", "prezzo massimo esplorabile", obbligatorio=False, default=99.0)])
def prezzo_ottimale(v: Mapping[str, Any]) -> Dict[str, Any]:
    p0 = num(v, "prezzo_attuale", minimo=1e-6)
    q0 = num(v, "unita_attuali", minimo=0.0)
    el = num(v, "elasticita")
    aliq = num(v, "aliquota_royalty", default=0.70, minimo=0.0, massimo=1.0)
    costo = num(v, "costo_per_unita", default=0.0, minimo=0.0)
    pmin = num(v, "prezzo_min", default=0.99, minimo=0.01)
    pmax = num(v, "prezzo_max", default=99.0, minimo=0.02)
    if pmax <= pmin:
        raise ErroreCalcolo("prezzo_max deve essere maggiore di prezzo_min")
    if el >= 0:
        raise ErroreCalcolo(
            "elasticita' >= 0: significa che alzando il prezzo vendi di piu', "
            "e il massimo profitto sarebbe sempre il prezzo massimo. Serve un valore negativo.")

    migliore_p, migliore_g, curva = p0, -math.inf, []
    passi = 200
    for i in range(passi + 1):
        p = pmin + (pmax - pmin) * i / passi
        q = q0 * SafeMath.pow(p / p0, el, 0.0)          # domanda a elasticita' costante
        g = (p * aliq - costo) * q
        curva.append((p, g))
        if g > migliore_g:
            migliore_p, migliore_g = p, g

    attuale = (p0 * aliq - costo) * q0
    return {
        "prezzo_ottimale": migliore_p,
        "guadagno_ottimale": migliore_g,
        "prezzo_attuale": p0,
        "guadagno_attuale": attuale,
        "guadagno_aggiuntivo": migliore_g - attuale,
        "miglioramento_pct": SafeMath.variazione_pct(attuale, migliore_g) if attuale else 0.0,
        "unita_stimate_al_prezzo_ottimale": q0 * SafeMath.pow(migliore_p / p0, el, 0.0),
        "alzare_il_prezzo": migliore_p > p0,
    }
