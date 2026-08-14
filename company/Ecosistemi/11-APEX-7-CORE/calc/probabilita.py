"""
APEX-7 Calc Layer — probabilita', distribuzioni e percentuali.

Regole rispettate ovunque qui dentro:
  - le probabilita' vivono in [0, 100] e, quando formano una distribuzione,
    sommano a 100 (verificato, non assunto);
  - nessun risultato "puntuale" spacciato per distribuzione;
  - le probabilita' di soglia dichiarano il modello che le ha prodotte.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Mapping

from .core import Assunzione, ErroreCalcolo, Parametro, SafeMath, num, registra

P = Parametro


# ─────────────────────────────────────────────────────────────────────────────
# Percentuali e rapporti — il pane quotidiano
# ─────────────────────────────────────────────────────────────────────────────

@registra("percentuale", "base", "Che percentuale e' una parte di un totale", [
    P("parte", "valore parziale"), P("totale", "valore totale")])
def percentuale(v: Mapping[str, Any]) -> Dict[str, Any]:
    parte, totale = num(v, "parte"), num(v, "totale")
    if totale == 0:
        raise ErroreCalcolo("il totale non puo' essere zero")
    return {"percentuale": SafeMath.pct(parte, totale), "resto": totale - parte,
            "percentuale_resto": SafeMath.pct(totale - parte, totale)}


@registra("variazione_percentuale", "base", "Variazione percentuale fra due valori", [
    P("da", "valore iniziale"), P("a", "valore finale")])
def variazione_percentuale(v: Mapping[str, Any]) -> Dict[str, Any]:
    da, a = num(v, "da"), num(v, "a")
    if da == 0:
        raise ErroreCalcolo("variazione da zero non definita in percentuale")
    var = SafeMath.variazione_pct(da, a)
    return {"variazione_pct": var, "delta_assoluto": a - da,
            "moltiplicatore": SafeMath.div(a, da, 0.0), "in_aumento": a > da}


@registra("applica_percentuale", "base", "Applica una percentuale a un valore (sconto o aumento)", [
    P("valore", "valore di partenza"), P("percentuale", "percentuale da applicare", unita="%"),
    P("in_aumento", "1 aumenta, 0 sconta", obbligatorio=False, default=1.0)])
def applica_percentuale(v: Mapping[str, Any]) -> Dict[str, Any]:
    val, pct = num(v, "valore"), num(v, "percentuale")
    su = num(v, "in_aumento", default=1.0) >= 0.5
    delta = val * pct / 100.0
    return {"risultato": val + delta if su else val - delta,
            "delta": delta if su else -delta, "valore_originale": val}


@registra("crescita_composta", "base", "Crescita composta di un valore su N periodi", [
    P("valore_iniziale", "valore di partenza"),
    P("tasso_periodo", "tasso per periodo in decimale (0.07 = 7%)"),
    P("periodi", "numero di periodi")])
def crescita_composta(v: Mapping[str, Any]) -> Dict[str, Any]:
    c = num(v, "valore_iniziale")
    r = num(v, "tasso_periodo")
    n = num(v, "periodi", minimo=0.0)
    finale = c * SafeMath.pow(1.0 + r, n)
    return {"valore_finale": finale, "crescita_assoluta": finale - c,
            "crescita_pct": SafeMath.variazione_pct(c, finale) if c else 0.0,
            "tasso_medio_pct": r * 100.0}


# ─────────────────────────────────────────────────────────────────────────────
# Probabilita' elementare
# ─────────────────────────────────────────────────────────────────────────────

@registra("probabilita_composta", "probabilita",
          "Probabilita' che eventi indipendenti accadano tutti (AND) o almeno uno (OR)", [
              P("probabilita_pct", "lista di probabilita' in % (passata come lista)", unita="%")])
def probabilita_composta(v: Mapping[str, Any]) -> Dict[str, Any]:
    lista = v.get("probabilita_pct")
    if not isinstance(lista, (list, tuple)) or not lista:
        raise ErroreCalcolo("'probabilita_pct' deve essere una lista non vuota di percentuali")
    p: List[float] = []
    for i, x in enumerate(lista):
        if isinstance(x, bool) or not isinstance(x, (int, float)) or not math.isfinite(float(x)):
            raise ErroreCalcolo(f"probabilita_pct[{i}] non e' un numero finito")
        if not 0.0 <= float(x) <= 100.0:
            raise ErroreCalcolo(f"probabilita_pct[{i}] = {x} fuori dall'intervallo 0-100")
        p.append(float(x) / 100.0)

    tutti = 1.0
    nessuno = 1.0
    for x in p:
        tutti *= x
        nessuno *= (1.0 - x)
    return {"tutti_pct": tutti * 100.0, "almeno_uno_pct": (1.0 - nessuno) * 100.0,
            "nessuno_pct": nessuno * 100.0, "eventi": len(p)}


@registra("bayes", "probabilita", "Probabilita' a posteriori con il teorema di Bayes", [
    P("prior_pct", "probabilita' a priori dell'ipotesi", unita="%"),
    P("sensibilita_pct", "P(prova | ipotesi vera)", unita="%"),
    P("falsi_positivi_pct", "P(prova | ipotesi falsa)", unita="%")])
def bayes(v: Mapping[str, Any]) -> Dict[str, Any]:
    prior = num(v, "prior_pct", minimo=0.0, massimo=100.0) / 100.0
    sens = num(v, "sensibilita_pct", minimo=0.0, massimo=100.0) / 100.0
    fp = num(v, "falsi_positivi_pct", minimo=0.0, massimo=100.0) / 100.0
    evidenza = sens * prior + fp * (1.0 - prior)
    if evidenza <= 0:
        raise ErroreCalcolo("la prova ha probabilita' nulla: posteriore non definita")
    post = (sens * prior) / evidenza
    return {"posteriore_pct": post * 100.0, "prior_pct": prior * 100.0,
            "evidenza_pct": evidenza * 100.0,
            "guadagno_informativo_pct": (post - prior) * 100.0}


@registra("probabilita_soglia", "probabilita",
          "Probabilita' che un valore che cresce a tasso incerto superi una soglia", [
              P("valore_iniziale", "valore di partenza"),
              P("soglia", "valore da superare"),
              P("tasso_atteso", "tasso medio per periodo in decimale"),
              P("volatilita", "deviazione standard del tasso per periodo in decimale"),
              P("periodi", "numero di periodi")])
def probabilita_soglia(v: Mapping[str, Any]) -> Dict[str, Any]:
    c = num(v, "valore_iniziale", minimo=1e-9)
    soglia = num(v, "soglia", minimo=0.0)
    r = num(v, "tasso_atteso")
    sigma = num(v, "volatilita", minimo=0.0)
    n = num(v, "periodi", minimo=1e-9)

    if sigma == 0:
        finale = c * SafeMath.pow(1.0 + r, n)
        return {"probabilita_pct": 100.0 if finale >= soglia else 0.0,
                "valore_atteso": finale, "modello": 0.0, "deterministico": True}

    # lognormale: log-rendimento ~ N(n*mu, sigma*sqrt(n)), mu con correzione di Ito
    mu = SafeMath.ln(1.0 + r, 0.0) - 0.5 * sigma * sigma
    sd = sigma * math.sqrt(n)
    z = SafeMath.div(SafeMath.ln(soglia / c, 0.0) - mu * n, sd, 0.0)
    prob = (1.0 - SafeMath.phi(z)) * 100.0
    atteso = c * SafeMath.pow(1.0 + r, n)
    return {"probabilita_pct": SafeMath.clamp(prob, 0.0, 100.0),
            "valore_atteso": atteso,
            "mediana": c * math.exp(mu * n),
            "z_score": z, "deterministico": False}


@registra("monte_carlo", "probabilita",
          "Simulazione Monte Carlo: distribuzione degli esiti e percentili", [
              P("valore_iniziale", "valore di partenza"),
              P("tasso_atteso", "tasso medio per periodo in decimale"),
              P("volatilita", "deviazione standard per periodo in decimale"),
              P("periodi", "numero di periodi"),
              P("simulazioni", "quante traiettorie simulare", obbligatorio=False, default=10000),
              P("soglia", "soglia di cui stimare la probabilita' di superamento",
                obbligatorio=False, default=None),
              P("seme", "seme del generatore, per risultati riproducibili",
                obbligatorio=False, default=42)])
def monte_carlo(v: Mapping[str, Any]) -> Dict[str, Any]:
    c = num(v, "valore_iniziale", minimo=1e-9)
    r = num(v, "tasso_atteso")
    sigma = num(v, "volatilita", minimo=0.0)
    n = int(num(v, "periodi", minimo=1))
    sim = int(num(v, "simulazioni", default=10000, minimo=100, massimo=200_000))
    seme = int(num(v, "seme", default=42))

    rng = random.Random(seme)   # seme fisso: due run sugli stessi dati danno lo stesso numero
    mu = SafeMath.ln(1.0 + r, 0.0) - 0.5 * sigma * sigma
    esiti: List[float] = []
    for _ in range(sim):
        log_tot = 0.0
        for _ in range(n):
            log_tot += mu + sigma * rng.gauss(0.0, 1.0)
        esiti.append(c * math.exp(log_tot))
    esiti.sort()

    def perc(q: float) -> float:
        idx = SafeMath.clamp(q * (len(esiti) - 1), 0, len(esiti) - 1)
        basso, alto = int(math.floor(idx)), int(math.ceil(idx))
        if basso == alto:
            return esiti[basso]
        return esiti[basso] + (esiti[alto] - esiti[basso]) * (idx - basso)

    out: Dict[str, Any] = {
        "media": sum(esiti) / len(esiti),
        "mediana": perc(0.50),
        "p05": perc(0.05), "p25": perc(0.25), "p75": perc(0.75), "p95": perc(0.95),
        "minimo": esiti[0], "massimo": esiti[-1],
        "simulazioni": float(sim),
        "prob_perdita_pct": SafeMath.pct(sum(1 for e in esiti if e < c), len(esiti)),
    }
    soglia = v.get("soglia")
    if soglia is not None:
        s = num(v, "soglia")
        out["prob_sopra_soglia_pct"] = SafeMath.pct(sum(1 for e in esiti if e >= s), len(esiti))
        out["soglia"] = s
    return out


# ─────────────────────────────────────────────────────────────────────────────
# Scenari calibrati — il pezzo che nello zip era sbagliato
# ─────────────────────────────────────────────────────────────────────────────

@registra("scenari_calibrati", "probabilita",
          "Tre scenari (migliore/base/peggiore) con probabilita' che sommano a 100 e valore atteso", [
              P("valore_migliore", "esito nello scenario migliore"),
              P("valore_base", "esito nello scenario base"),
              P("valore_peggiore", "esito nello scenario peggiore"),
              P("prob_migliore_pct", "probabilita' del migliore", obbligatorio=False, default=25.0),
              P("prob_base_pct", "probabilita' del base", obbligatorio=False, default=50.0),
              P("prob_peggiore_pct", "probabilita' del peggiore", obbligatorio=False, default=25.0)])
def scenari_calibrati(v: Mapping[str, Any]) -> Dict[str, Any]:
    vm = num(v, "valore_migliore")
    vb = num(v, "valore_base")
    vp = num(v, "valore_peggiore")
    pm = num(v, "prob_migliore_pct", default=25.0, minimo=0.0, massimo=100.0)
    pb = num(v, "prob_base_pct", default=50.0, minimo=0.0, massimo=100.0)
    pp = num(v, "prob_peggiore_pct", default=25.0, minimo=0.0, massimo=100.0)

    somma = pm + pb + pp
    if abs(somma - 100.0) > 1e-6:
        raise ErroreCalcolo(
            f"le probabilita' sommano a {somma}%, non a 100%: la distribuzione non e' calibrata")
    if vp > vb or vb > vm:
        raise ErroreCalcolo(
            f"ordine incoerente: peggiore ({vp}) <= base ({vb}) <= migliore ({vm}) non rispettato")

    ev = (pm / 100.0) * vm + (pb / 100.0) * vb + (pp / 100.0) * vp
    varianza = ((pm / 100.0) * (vm - ev) ** 2 + (pb / 100.0) * (vb - ev) ** 2
                + (pp / 100.0) * (vp - ev) ** 2)
    dev = math.sqrt(varianza) if varianza > 0 else 0.0
    return {"valore_atteso": ev, "deviazione_standard": dev,
            "coefficiente_variazione": SafeMath.div(dev, abs(ev), 0.0),
            "escursione": vm - vp, "somma_probabilita_pct": somma,
            "distribuzione_degenere": vm == vb == vp}
