"""
ONDATA 3 — 4 perfezionamenti (task, sezione 3, Ondata 3). Nessun file frozen
toccato. Si appoggia a Ondata 1 (nft_analysis_engine.py, nft_monte_carlo.py).
"""
import logging
from typing import Any, Dict, List, Optional

import numpy as np

from nft_analysis_engine import FairValueModel, calibrate_entry_threshold
from nft_magiceden_client import MagicEdenClient, MagicEdenRateLimited

logger = logging.getLogger(__name__)


# --------------------------------------------------------------------------- #
# PERFEZIONAMENTO 1 — Backtest su piu' collection reali (non simulazioni astratte)
# --------------------------------------------------------------------------- #
def backtest_across_collections(raw_data: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
    """
    Applica l'intera pipeline di Ondata 1 (fit -> calibra -> conta segnali
    eleggibili) a OGNI collection nel dataset reale, senza scartare quelle
    che non producono segnali (un backtest che riporta solo i casi positivi
    non e' un backtest, e' marketing).
    """
    results = {}
    for symbol, data in raw_data.items():
        listings = data.get("listings", [])
        try:
            m = FairValueModel()
            fit = m.fit(listings)
            residuals = m.residuals(listings)
            calib = calibrate_entry_threshold(residuals)
            n_eligible = sum(1 for r in residuals if r <= calib["entry_threshold_sol"])
            results[symbol] = {
                "status": "fitted",
                "n_points": fit["n_points"],
                "r_squared": fit["r_squared"],
                "n_eligible_signals": n_eligible,
                "entry_threshold_sol": calib["entry_threshold_sol"],
            }
        except ValueError as e:
            results[symbol] = {"status": "no_fit", "reason": str(e)}

    n_fitted = sum(1 for r in results.values() if r["status"] == "fitted")
    n_with_signals = sum(1 for r in results.values() if r.get("n_eligible_signals", 0) > 0)
    return {
        "per_collection": results,
        "n_collections_tested": len(results),
        "n_collections_fitted": n_fitted,
        "n_collections_with_tradeable_signal": n_with_signals,
    }


# --------------------------------------------------------------------------- #
# PERFEZIONAMENTO 2 — Stress test su scenari avversi
# --------------------------------------------------------------------------- #
def stress_test_marketplace_unreachable() -> Dict[str, Any]:
    """
    Scenario avverso reale (non simulato): un host inesistente, stesso client
    di produzione. Verifica che l'errore sia gestito in modo pulito (eccezione
    catturabile, non un hang o un crash del processo).
    """
    broken_client = MagicEdenClient(base_url="https://this-host-does-not-exist.invalid-magiceden.example/v2")
    try:
        broken_client.get_stats("mad_lads")
        return {"handled_cleanly": False, "detail": "Nessuna eccezione sollevata: inatteso"}
    except MagicEdenRateLimited as e:
        return {"handled_cleanly": False, "detail": f"Eccezione sbagliata (rate-limit invece di rete): {e}"}
    except Exception as e:
        return {"handled_cleanly": True, "exception_type": type(e).__name__, "detail": str(e)[:200]}


def stress_test_market_crash(raw_net_pnl_pct: np.ndarray, crash_prob: float, crash_severity_pct: float,
                              seed: int = 11) -> Dict[str, Any]:
    """
    Aggiunge sopra i risultati GIA' calcolati da monte_carlo_expectancy (Blocco 8)
    uno shock di crollo di mercato: con probabilita' crash_prob, il trade perde
    crash_severity_pct punti percentuali aggiuntivi (es. il floor crolla mentre
    la posizione e' aperta). Confronta media/IC prima vs dopo.
    """
    rng = np.random.default_rng(seed)
    n = len(raw_net_pnl_pct)
    crash_hits = rng.random(n) < crash_prob
    stressed = raw_net_pnl_pct.copy()
    stressed[crash_hits] = stressed[crash_hits] - crash_severity_pct

    return {
        "crash_prob": crash_prob,
        "crash_severity_pct": crash_severity_pct,
        "mean_before_pct": float(np.mean(raw_net_pnl_pct)),
        "mean_after_pct": float(np.mean(stressed)),
        "ci95_after_pct": tuple(float(x) for x in np.percentile(stressed, [2.5, 97.5])),
        "prob_negative_after": float(np.mean(stressed < 0)),
    }


def rug_pull_breakeven_probability(raw_net_pnl_pct: np.ndarray, search_steps: int = 200) -> Dict[str, Any]:
    """
    Trova la probabilita' di rug-pull (perdita totale della posizione, -100%)
    oltre la quale l'expectancy media diventa negativa — non un numero a
    caso, e' l'intersezione di una funzione monotona crescente in p_rug,
    calcolata per bisezione sui dati reali gia' simulati.
    """
    mean_base = float(np.mean(raw_net_pnl_pct))

    def mean_at(p_rug: float) -> float:
        return (1 - p_rug) * mean_base + p_rug * (-100.0)

    if mean_at(0.0) <= 0:
        return {"breakeven_p_rug": 0.0, "note": "Expectancy gia' <=0 senza alcun rischio di rug aggiuntivo"}
    if mean_at(1.0) > 0:
        return {"breakeven_p_rug": None, "note": "Expectancy resta positiva anche con rug certo al 100% (improbabile, verificare input)"}

    lo, hi = 0.0, 1.0
    for _ in range(search_steps):
        mid = (lo + hi) / 2
        if mean_at(mid) > 0:
            lo = mid
        else:
            hi = mid
    return {"breakeven_p_rug": (lo + hi) / 2, "mean_base_pct": mean_base}


# --------------------------------------------------------------------------- #
# PERFEZIONAMENTO 3 — Intervallo di confidenza esplicito (anche sulla qualita' del fit)
# --------------------------------------------------------------------------- #
def bootstrap_r_squared_ci(listings: List[Dict[str, Any]], n_boot: int = 500, seed: int = 3) -> Dict[str, Any]:
    """
    Il R^2 di Ondata 1 (Blocco 3) e' un singolo numero puntuale su un singolo
    campione. Qui si ricampiona (bootstrap, con reinserimento) lo stesso
    dataset reale n_boot volte, si rifitta ogni volta, e si riporta la
    distribuzione — mostra quanto e' INSTABILE quel R^2 debole, non solo il
    suo valore medio.
    """
    rng = np.random.default_rng(seed)
    base = FairValueModel()
    base_fit = base.fit(listings)
    n = len(listings)

    r2_samples = []
    for _ in range(n_boot):
        idx = rng.integers(0, n, size=n)
        sample = [listings[i] for i in idx]
        try:
            m = FairValueModel()
            fit = m.fit(sample)
            r2_samples.append(fit["r_squared"])
        except ValueError:
            continue

    r2_arr = np.array(r2_samples)
    return {
        "point_r_squared": base_fit["r_squared"],
        "n_boot_valid": len(r2_arr),
        "bootstrap_mean_r_squared": float(np.mean(r2_arr)) if len(r2_arr) else None,
        "ci95_r_squared": tuple(float(x) for x in np.percentile(r2_arr, [2.5, 97.5])) if len(r2_arr) else None,
    }


# --------------------------------------------------------------------------- #
# PERFEZIONAMENTO 4 — Ogni percentuale del report finale cita la fonte
# --------------------------------------------------------------------------- #
def validate_sourced_report(entries: List[Dict[str, Any]]) -> List[str]:
    """
    Un report finale (Ondata 4) e' una lista di {label, value, source}.
    Ritorna la lista delle label SENZA fonte dichiarata — vuota se tutto e'
    tracciabile. Usato come gate, non come consiglio: un report con questa
    lista non vuota non e' pronto per Max.
    """
    missing = []
    for entry in entries:
        source = entry.get("source")
        if not source or not str(source).strip():
            missing.append(entry.get("label", "<senza label>"))
    return missing
