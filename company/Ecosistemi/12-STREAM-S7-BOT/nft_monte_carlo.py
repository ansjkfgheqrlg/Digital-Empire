"""
ONDATA 1 — Blocco 8: simulazione Monte Carlo dell'expectancy netta.

Bootstrap sui residui REALI (Blocco 3, fit su listing veri di piu' collection)
+ tasso di liquidita' REALE (Blocco 6, Poisson su attivita' vere) — nessuna
distribuzione assunta a tavolino: si ricampiona da numeri fetchati oggi.

Incertezza sul tasso di vendita propagata con un bootstrap Bayesiano
Gamma-Poisson (prior di Jeffreys, shape=k+0.5, scale=1/T) via numpy — niente
scipy nell'ambiente, ma numpy.random.Generator.gamma e' sufficiente ed e'
lo stesso principio (posteriore coniugato), non un'approssimazione a mano.
"""
from typing import Any, Dict, List, Optional

import numpy as np

from nft_analysis_engine import net_edge_sol, MARKETPLACE_FEE_PCT, DEFAULT_CREATOR_ROYALTY_PCT, SOLANA_BASE_FEE_LAMPORTS


def monte_carlo_expectancy(
    residuals_sol: List[float],
    entry_threshold_sol: float,
    fair_values_sol: List[float],
    listing_prices_sol: List[float],
    liquidity_k_sales: int,
    liquidity_span_days: float,
    listed_count: int,
    holding_horizon_days: float = 30.0,
    n_sims: int = 20000,
    marketplace_fee_pct: float = MARKETPLACE_FEE_PCT,
    creator_royalty_pct: float = DEFAULT_CREATOR_ROYALTY_PCT,
    seed: int = 7,
) -> Dict[str, Any]:
    """
    Per ogni simulazione:
      1. Ricampiona (bootstrap) una coppia (listing_price, fair_value) reale
         tra quelle che superano gia' la soglia di ingresso (Blocco 4) —
         solo i trade che la strategia avrebbe davvero eseguito.
      2. Ricampiona un tasso di vendita/giorno dal posteriore Gamma-Poisson
         (incertezza reale sulla liquidita', Blocco 6).
      3. Se il tempo-atteso-di-vendita simulato eccede l'orizzonte dichiarato
         -> scenario "illiquidita'" (capitale bloccato, PnL netto = -costi,
         nessun profitto realizzato nell'orizzonte).
      4. Altrimenti -> PnL netto = net_edge_sol (Blocco 5) sul trade
         ricampionato.

    Ritorna media, deviazione standard, IC 95% (percentile bootstrap) e
    probabilita' di trade netto negativo — mai un singolo numero puntuale
    (Fase 0, criterio 5).
    """
    rng = np.random.default_rng(seed)

    eligible_idx = [i for i, r in enumerate(residuals_sol) if r <= entry_threshold_sol]
    if len(eligible_idx) < 2:
        raise ValueError(
            f"Solo {len(eligible_idx)} listing superano la soglia di ingresso "
            f"({entry_threshold_sol:.4f} SOL): campione troppo piccolo per Monte Carlo"
        )

    eligible_prices = np.array([listing_prices_sol[i] for i in eligible_idx])
    eligible_fair_values = np.array([fair_values_sol[i] for i in eligible_idx])

    # Posteriore Gamma-Poisson (Jeffreys: shape=k+0.5) per il tasso di vendita/giorno.
    shape = liquidity_k_sales + 0.5
    scale = 1.0 / liquidity_span_days
    sampled_rates_market = rng.gamma(shape=shape, scale=scale, size=n_sims)  # vendite/giorno, tutta la collection
    sampled_rates_listing = sampled_rates_market / listed_count  # per singolo listing (assunzione: uniforme tra i listing)

    idx_draw = rng.integers(0, len(eligible_idx), size=n_sims)
    draw_prices = eligible_prices[idx_draw]
    draw_fair_values = eligible_fair_values[idx_draw]

    prob_sell_within_horizon = 1 - np.exp(-sampled_rates_listing * holding_horizon_days)
    sells_within_horizon = rng.random(n_sims) < prob_sell_within_horizon

    net_pnls = np.zeros(n_sims)
    net_pnls_pct = np.zeros(n_sims)
    for i in range(n_sims):
        edge = net_edge_sol(
            listing_price_sol=float(draw_prices[i]),
            fair_value_sol=float(draw_fair_values[i]),
            marketplace_fee_pct=marketplace_fee_pct,
            creator_royalty_pct=creator_royalty_pct,
        )
        if sells_within_horizon[i]:
            net_pnls[i] = edge["net_edge_sol"]
        else:
            # Illiquidita': capitale bloccato, si realizza solo il costo (fee+gas gia' pagati
            # per entrare), nessun profitto entro l'orizzonte dichiarato.
            net_pnls[i] = -edge["total_cost_sol"]
        net_pnls_pct[i] = (net_pnls[i] / draw_prices[i] * 100.0) if draw_prices[i] else 0.0

    mean_pnl_pct = float(np.mean(net_pnls_pct))
    std_pnl_pct = float(np.std(net_pnls_pct, ddof=1))
    ci_lower, ci_upper = np.percentile(net_pnls_pct, [2.5, 97.5])
    prob_negative = float(np.mean(net_pnls_pct < 0))
    prob_illiquid_scenario = float(np.mean(~sells_within_horizon))

    return {
        "n_sims": n_sims,
        "n_eligible_real_listings_used": len(eligible_idx),
        "mean_net_pnl_pct": mean_pnl_pct,
        "std_net_pnl_pct": std_pnl_pct,
        "ci95_net_pnl_pct": (float(ci_lower), float(ci_upper)),
        "prob_negative_trade": prob_negative,
        "prob_illiquid_scenario": prob_illiquid_scenario,
        "holding_horizon_days": holding_horizon_days,
    }
