"""
ONDATA 4 — 3 controlli chirurgici (audit finale, indipendente da chi ha
costruito). Task, sezione 3, Ondata 4. Nessun file frozen toccato: il
Controllo Chirurgico #3 RIUSA il gate_agent.gate_1 esistente (stesso ruolo di
controllore gia' avuto da Claude su G-A/G-B/G-C), non ne scrive uno nuovo.
"""
from typing import Any, Dict, List

from nft_magiceden_client import best_rarity_rank


# --------------------------------------------------------------------------- #
# CONTROLLO CHIRURGICO #1 — Ricalcolo matematico indipendente
# --------------------------------------------------------------------------- #
def independent_expectancy_recheck(listings: List[Dict[str, Any]], z: float = 1.5,
                                    fee_pct: float = 0.02, gas_sol: float = 5000 / 1_000_000_000) -> Dict[str, Any]:
    """
    Ricalcola la regressione, la soglia e l'expectancy grezza (senza Monte
    Carlo/liquidita') PARTENDO DA ZERO, con formule scritte qui — non chiama
    FairValueModel/calibrate_entry_threshold/net_edge_sol di nft_analysis_engine.py.
    Se questo numero non torna vicino a quello della pipeline originale, la
    pipeline originale ha un bug, punto (non ci si fida del codice che ha
    prodotto il risultato).
    """
    pts = []
    for lst in listings:
        r = best_rarity_rank(lst)
        p = lst.get("price")
        if r is None or not isinstance(p, (int, float)) or p <= 0:
            continue
        pts.append((r, p))

    n = len(pts)
    if n < 3:
        raise ValueError(f"Servono almeno 3 punti validi, trovati {n}")

    mean_x = sum(r for r, p in pts) / n
    mean_y = sum(p for r, p in pts) / n
    sxy = sum((r - mean_x) * (p - mean_y) for r, p in pts)
    sxx = sum((r - mean_x) ** 2 for r, p in pts)
    slope = sxy / sxx if sxx else 0.0
    intercept = mean_y - slope * mean_x

    residuals = [p - (intercept + slope * r) for r, p in pts]
    mean_res = sum(residuals) / n
    var_res = sum((x - mean_res) ** 2 for x in residuals) / (n - 1)
    std_res = var_res ** 0.5
    threshold = mean_res - z * std_res

    eligible = [(r, p, res) for (r, p), res in zip(pts, residuals) if res <= threshold]

    net_pcts = []
    for r, p, res in eligible:
        fair = intercept + slope * r
        gross = fair - p
        fee = p * fee_pct
        net = gross - fee - gas_sol
        net_pcts.append(net / p * 100.0)

    return {
        "n_points": n,
        "slope": slope,
        "intercept": intercept,
        "entry_threshold_sol": threshold,
        "n_eligible": len(eligible),
        "net_pct_per_trade": net_pcts,
        "mean_net_pct_raw_no_liquidity": (sum(net_pcts) / len(net_pcts)) if net_pcts else None,
    }


def cross_check_against_pipeline(independent: Dict[str, Any], pipeline_fit: Dict[str, Any],
                                  pipeline_n_eligible: int, tolerance: float = 1e-6) -> Dict[str, Any]:
    """Confronta il ricalcolo indipendente con l'output della pipeline originale (Ondata 1)."""
    slope_match = abs(independent["slope"] - pipeline_fit["slope"]) < tolerance
    n_match = independent["n_points"] == pipeline_fit["n_points"]
    eligible_match = independent["n_eligible"] == pipeline_n_eligible
    return {
        "slope_match": slope_match,
        "n_points_match": n_match,
        "n_eligible_match": eligible_match,
        "all_match": slope_match and n_match and eligible_match,
    }


# --------------------------------------------------------------------------- #
# CONTROLLO CHIRURGICO #2 — Coerenza con report-studio.md (il punto che conta di piu')
# --------------------------------------------------------------------------- #
def confronto_report_studio(evidence: Dict[str, Any]) -> Dict[str, Any]:
    """
    Per ognuno dei 3 problemi strutturali di report-studio.md, verdetto
    esplicito RISOLTO / PARZIALE / NON RISOLTO + il numero che lo giustifica.
    'evidence' porta i numeri gia' misurati nelle ondate precedenti (nessun
    numero nuovo inventato qui, solo assemblato).
    """
    problemi = [
        {
            "problema": "1. Latenza contro MEV bot istituzionali (300-800ms mempool)",
            "verdetto": "NON RISOLTO",
            "spiegazione": (
                f"Latenza REALE misurata sul path Magic Eden REST: media {evidence['latency_avg_ms']}ms "
                f"(range {evidence['latency_range_ms']}) — PIU' ALTA in ms assoluti del benchmark MEV, "
                f"non piu' bassa. Il timescale competitivo e' diverso (un listing sottoprezzato resta "
                f"visibile finche' non viene comprato, non un singolo blocco), ma questo e' un "
                f"RIFRAMING del problema, non una soluzione: qualunque altro bot/umano puo' interrogare "
                f"la stessa API pubblica anche piu' velocemente di {evidence['latency_avg_ms']}ms."
            ),
        },
        {
            "problema": "2. RPC pubblico rate-limita dopo 2 chiamate getTransaction",
            "verdetto": "PARZIALMENTE RISOLTO",
            "spiegazione": (
                f"Il path di SCANSIONE del layer NFT non usa getTransaction su RPC Solana: usa "
                f"l'API REST Magic Eden, misurata a {evidence['me_burst_concurrent_ok']} richieste "
                f"concorrenti senza 429 (vs 2 per l'RPC Solana pubblico, CP-20260728-006) — "
                f"miglioramento REALE e specifico del collo di bottiglia di SCANSIONE. NON risolve "
                f"pero' il lato ESECUZIONE (inviare davvero una transazione di acquisto richiede "
                f"comunque l'RPC Solana, non misurato qui perche' si resta in paper trading)."
            ),
        },
        {
            "problema": "3. Rug pull (99% dei nuovi progetti Pump.fun/Raydium)",
            "verdetto": "NON RISOLTO (rischio ridimensionato, non eliminato)",
            "spiegazione": (
                f"Il layer NFT punta a collection consolidate (filtro anti-scam, Ondata 2) invece di "
                f"token appena nati — categoria di rischio diversa dal 99%% di Pump.fun, ma NON "
                f"misurata con dati reali qui (nessun tasso storico di abbandono/rug per collection "
                f"blue-chip verificato in questa sessione). Soglia di rottura calcolata: "
                f"P(rug/abbandono) > {evidence['rug_breakeven_pct']:.1f}%% rende l'expectancy media "
                f"negativa (Ondata 3) — un NUMERO ESPLICITO, ma la probabilita' reale resta ignota."
            ),
        },
    ]

    n_risolti = sum(1 for p in problemi if p["verdetto"] == "RISOLTO")
    n_parziali = sum(1 for p in problemi if "PARZIALMENTE" in p["verdetto"])

    altre_criticita = [
        f"Solo {evidence['n_collections_with_signal']}/{evidence['n_collections_tested']} collection reali "
        f"testate producono un segnale tradeable oggi (backtest Ondata 3).",
        f"Il fit fair-value e' debole E instabile: R^2 puntuale {evidence['r_squared_point']:.4f}, "
        f"IC95%% bootstrap fino a {evidence['r_squared_ci_upper']:.3f} (Ondata 3) — potrebbe essere "
        f"rumore, non edge.",
        f"L'IC95%% dell'expectancy Monte Carlo ({evidence['mc_ci_lower']:.2f}%%, {evidence['mc_ci_upper']:.2f}%%) "
        f"include valori negativi al limite inferiore: l'edge non e' statisticamente distinguibile da "
        f"zero al 95%% di confidenza sull'unica collection con segnale reale.",
        f"L'evento che il metodo assume come meccanismo di uscita (buyNow diretto) e' il piu' raro "
        f"nell'attivita' reale osservata ({evidence['buynow_rate']}) — la maggioranza del mercato reale "
        f"scorre su bid/pool, un meccanismo diverso da quello modellato (CP-20260730-002).",
    ]

    verdetto_finale = (
        "VERDETTO INVARIATO: bocciato per live, coerente con report-studio.md. "
        f"Solo {n_risolti + n_parziali}/3 problemi strutturali migliorano (1 parzialmente — la "
        "scansione, non l'esecuzione), gli altri 2 restano aperti o ridimensionati senza prova. "
        "L'edge sull'unica collection con segnale reale non e' statisticamente distinguibile da "
        "zero al 95%% di confidenza, il campione e' minuscolo (3 trade reali su 1 collection su 3 "
        "testate), e il meccanismo di edge assunto (buyNow) e' empiricamente il piu' raro nel "
        "mercato reale osservato. Nessun problema strutturale e' spiegato-con-numeri al punto da "
        "giustificare un cambio di verdetto — la clausola del task si applica: resta valido il "
        "verdetto attuale."
    )

    return {"problemi": problemi, "altre_criticita": altre_criticita, "verdetto_finale": verdetto_finale}
