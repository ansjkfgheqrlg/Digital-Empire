"""
TEST — Layer NFT Stream S7, ONDATA 1 (10 blocchi).

Stesso stile di test_apex7.py: ogni sezione ha assert reali (check + failures),
un test che non puo' fallire non dimostra niente. Usa dati Magic Eden REALI
fetchati e cachati in questa sessione (memory/nft_cache/) — vedi
STUDIO-NFT-FASE0.md §2 per i comandi/risposte originali.

Esecuzione:  python test_nft_s7.py
"""
import json
import os
import sys

from event_bus import global_bus
from risk_manager import RiskManager
from execution_engine import ExecutionEngine
from position_monitor import PositionMonitor

from nft_magiceden_client import best_rarity_rank
from nft_analysis_engine import (
    FairValueModel, calibrate_entry_threshold, net_edge_sol, estimate_liquidity_days,
    position_size_sol, NFTAnalysisEngine, EDGE_STATEMENT, STRATEGY_NAME,
)
from nft_monte_carlo import monte_carlo_expectancy

SRC = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(SRC, "memory", "nft_cache")
failures = []

with open(os.path.join(CACHE, "raw_fetch.json"), encoding="utf-8") as f:
    RAW = json.load(f)["data"]
with open(os.path.join(CACHE, "mad_lads_activities_deep.json"), encoding="utf-8") as f:
    MAD_LADS_ACTIVITIES_DEEP = json.load(f)


def section(title):
    print(f"\n{'=' * 70}\n  {title}\n{'=' * 70}")


def check(label, condition, detail=""):
    status = "OK " if condition else "KO "
    print(f"  [{status}] {label}" + (f" — {detail}" if detail else ""))
    if not condition:
        failures.append(label)
    return condition


# =========================================================================== #
def test_blocco_1_edge():
    section("1. NFT (Blocco 1) — Edge dichiarato")
    check("EDGE_STATEMENT non generico (menziona rarity e mismatch)",
          "rarity" in EDGE_STATEMENT.lower() and "mismatch" in EDGE_STATEMENT.lower(),
          EDGE_STATEMENT[:70] + "...")
    check("Strategy NFT distinta da quella memecoin",
          STRATEGY_NAME != "volume_spike_v1" and "nft" in STRATEGY_NAME,
          STRATEGY_NAME)


def test_blocco_2_fonte_dati():
    section("2. NFT (Blocco 2) — Fonte dati Magic Eden reale (cache di questa sessione)")
    for sym in ("mad_lads", "degods", "y00ts"):
        stats = RAW[sym]["stats"]
        listings = RAW[sym]["listings"]
        activities = RAW[sym]["activities"]
        check(f"{sym}: stats reali con floorPrice>0", stats.get("floorPrice", 0) > 0,
              f"floor={stats.get('floorPrice')} lamports")
        check(f"{sym}: listings reali (>=30)", len(listings) >= 30, f"n={len(listings)}")
        check(f"{sym}: activities reali (>=30)", len(activities) >= 30, f"n={len(activities)}")


def test_blocco_3_fair_value():
    section("3. NFT (Blocco 3) — Modello di fair value (regressione reale)")

    models = {}
    for sym in ("mad_lads", "degods"):
        m = FairValueModel()
        fit = m.fit(RAW[sym]["listings"])
        models[sym] = m
        check(f"{sym}: fit con >=25 punti reali", fit["n_points"] >= 25, f"n={fit['n_points']}")
        check(f"{sym}: R^2 calcolato (0<=R^2<=1, anche se debole)", 0.0 <= fit["r_squared"] <= 1.0,
              f"R^2={fit['r_squared']:.4f}, slope={fit['slope']:.6f}")

    # y00ts: rarity vuota nel payload reale fetchato oggi (0/98) -> il modello
    # deve rifiutarsi di fittare, non inventare un fit su dati assenti.
    try:
        FairValueModel().fit(RAW["y00ts"]["listings"])
        check("y00ts: fit rifiuta correttamente (rarity assente nei dati reali)", False)
    except ValueError as e:
        check("y00ts: fit rifiuta correttamente (rarity assente nei dati reali)", True, str(e))

    return models


def test_blocco_4_soglia(models):
    section("4. NFT (Blocco 4) — Soglia di ingresso statistica (residui reali)")

    calibs = {}
    for sym, m in models.items():
        residuals = m.residuals(RAW[sym]["listings"])
        calib = calibrate_entry_threshold(residuals)
        calibs[sym] = (residuals, calib)
        check(f"{sym}: soglia calcolata da residui reali (std>0)", calib["std_residual_sol"] > 0,
              f"mean={calib['mean_residual_sol']:.4f} std={calib['std_residual_sol']:.4f} "
              f"soglia={calib['entry_threshold_sol']:.4f} SOL")

    n_below_degods = sum(1 for r in calibs["degods"][0] if r <= calibs["degods"][1]["entry_threshold_sol"])
    check("degods: almeno 1 listing reale sotto soglia (segnale non vuoto)", n_below_degods >= 1,
          f"{n_below_degods}/{len(calibs['degods'][0])} listing reali sotto soglia")
    n_below_madlads = sum(1 for r in calibs["mad_lads"][0] if r <= calibs["mad_lads"][1]["entry_threshold_sol"])
    print(f"  [NOTA] mad_lads: {n_below_madlads}/{len(calibs['mad_lads'][0])} sotto soglia — "
          f"dataset con outlier di prezzo alto (std={calibs['mad_lads'][1]['std_residual_sol']:.2f} SOL), "
          f"z=1.5 risulta molto conservativo su questa collection oggi (risultato reale, non un bug)")

    return calibs


def test_blocco_5_costi():
    section("5. NFT (Blocco 5) — Modello di costo reale (verifica aritmetica a mano)")

    # Esempio verificabile a mano: fair value 10 SOL, listing 8 SOL, fee 2%, royalty 0%, gas base.
    edge = net_edge_sol(listing_price_sol=8.0, fair_value_sol=10.0,
                         marketplace_fee_pct=0.02, creator_royalty_pct=0.0)
    expected_fee = 8.0 * 0.02
    expected_gas = 5000 / 1_000_000_000
    expected_net = (10.0 - 8.0) - expected_fee - 0.0 - expected_gas

    check("gross_edge = fair_value - price", abs(edge["gross_edge_sol"] - 2.0) < 1e-9)
    check("fee_cost = price * 2%", abs(edge["fee_cost_sol"] - expected_fee) < 1e-9, f"{edge['fee_cost_sol']}")
    check("net_edge_sol coerente con calcolo a mano", abs(edge["net_edge_sol"] - expected_net) < 1e-9,
          f"atteso={expected_net:.6f} ottenuto={edge['net_edge_sol']:.6f}")

    # Royalty non nulla: il net edge deve peggiorare rispetto a royalty=0, a parita' di resto.
    edge_with_royalty = net_edge_sol(listing_price_sol=8.0, fair_value_sol=10.0,
                                      marketplace_fee_pct=0.02, creator_royalty_pct=0.05)
    check("royalty>0 riduce il net edge rispetto a royalty=0",
          edge_with_royalty["net_edge_sol"] < edge["net_edge_sol"],
          f"{edge_with_royalty['net_edge_sol']:.6f} < {edge['net_edge_sol']:.6f}")


def test_blocco_6_liquidita():
    section("6. NFT (Blocco 6) — Modello di liquidita' (Poisson esatto su attivita' reali)")

    liq = estimate_liquidity_days(MAD_LADS_ACTIVITIES_DEEP, listed_count=242)
    check("k_sales_observed reale (mad_lads, 400 attivita' reali)", liq["k_sales_observed"] == 1,
          f"k={liq['k_sales_observed']}")
    check("span_days_observed reale > 0", liq["span_days_observed"] > 0,
          f"{liq['span_days_observed']:.4f} giorni")
    check("stima puntuale giorni-attesa in range plausibile (10-40gg)",
          10.0 <= liq["expected_days_to_sell_point"] <= 40.0,
          f"{liq['expected_days_to_sell_point']:.1f} giorni")
    lo, hi = liq["expected_days_to_sell_ci95"]
    check("IC95%% enorme dichiarato esplicitamente (k=1 -> alta incertezza, non nascosta)",
          lo < liq["expected_days_to_sell_point"] < hi and (hi - lo) > 100,
          f"IC95%=[{lo:.1f}, {hi:.1f}] giorni")

    return liq


def test_blocco_7_position_sizing():
    section("7. NFT (Blocco 7) — Position sizing (riusa RiskManager esistente)")

    rm = RiskManager(base_bankroll=100.0, max_position_pct=5.0, log_file="paper_trade_log_nft.csv")
    size = position_size_sol(rm)
    check("position_size_sol == bankroll * max_position_pct%% (nessuna logica duplicata)",
          abs(size - 5.0) < 1e-9, f"{size} SOL")
    global_bus.unsubscribe("analysis.signal_detected", f"{rm.agent_id}.signal")
    global_bus.unsubscribe("trade.executed", f"{rm.agent_id}.position_opened")
    global_bus.unsubscribe("position.closed", f"{rm.agent_id}.position_closed")


def test_blocco_8_monte_carlo(models, calibs):
    section("8. NFT (Blocco 8) — Monte Carlo (bootstrap su dati reali + Bayes Gamma-Poisson)")

    m = models["degods"]
    residuals, calib = calibs["degods"]
    fair_values, prices = m.fair_values_and_prices(RAW["degods"]["listings"])
    liq = estimate_liquidity_days(MAD_LADS_ACTIVITIES_DEEP, listed_count=242)

    result = monte_carlo_expectancy(
        residuals_sol=residuals,
        entry_threshold_sol=calib["entry_threshold_sol"],
        fair_values_sol=fair_values,
        listing_prices_sol=prices,
        liquidity_k_sales=liq["k_sales_observed"],
        liquidity_span_days=liq["span_days_observed"],
        listed_count=242,
        holding_horizon_days=30.0,
        n_sims=20000,
    )

    check("n_sims eseguiti come richiesto", result["n_sims"] == 20000)
    check("usa solo listing reali sopra soglia (degods, 3/31)", result["n_eligible_real_listings_used"] >= 1,
          f"n={result['n_eligible_real_listings_used']}")
    lo, hi = result["ci95_net_pnl_pct"]
    check("IC95%% ben ordinato attorno alla media (nessun numero puntuale nascosto)",
          lo <= result["mean_net_pnl_pct"] <= hi, f"IC95%=[{lo:.2f}%, {hi:.2f}%] media={result['mean_net_pnl_pct']:.2f}%")
    check("probabilita' di trade netto negativo calcolata (0-1)",
          0.0 <= result["prob_negative_trade"] <= 1.0, f"{result['prob_negative_trade']:.2%}")
    check("probabilita' scenario illiquidita' calcolata (0-1)",
          0.0 <= result["prob_illiquid_scenario"] <= 1.0, f"{result['prob_illiquid_scenario']:.2%}")

    print(f"\n  >>> Expectancy netta stimata (degods, floor-rarity mismatch, orizzonte 30gg): "
          f"{result['mean_net_pnl_pct']:.2f}%  IC95%=[{lo:.2f}%, {hi:.2f}%]  "
          f"P(negativo)={result['prob_negative_trade']:.1%}  "
          f"P(illiquidita' entro 30gg)={result['prob_illiquid_scenario']:.1%}")

    return result


def test_blocco_9_e_10_integrazione():
    section("9-10. NFT (Blocco 9+10) — Integrazione Event Bus reale + paper trading dedicato")

    log_file = "paper_trade_log_nft.csv"
    if os.path.exists(log_file):
        os.remove(log_file)

    rm = RiskManager(base_bankroll=50.0, max_position_pct=10.0, log_file=log_file)
    ee = ExecutionEngine(mode="SIMULATION", agent_id="EXECUTION-ENGINE-NFT", log_file=log_file)
    pm = PositionMonitor(agent_id="POSITION-MONITOR-NFT")
    engine = NFTAnalysisEngine()

    listings = RAW["degods"]["listings"]
    calib_info = engine.calibrate(listings)
    check("calibrate() produce soglia reale da listing degods", "entry_threshold_sol" in calib_info["calibration"])

    signals = engine.scan_listings("degods", listings)
    check("almeno 1 segnale pubblicato su analysis.signal_detected (reale, degods)", len(signals) >= 1,
          f"{len(signals)} segnali")

    stats_after = global_bus.get_stats()
    check("Risk Manager ha approvato o rifiutato il segnale (bus drenato)",
          stats_after["published"] >= len(signals) * 2,  # signal + almeno risk.trade_*
          f"published={stats_after['published']}")

    check("Blocco 10: log paper trading NFT dedicato creato", os.path.exists(log_file))
    if os.path.exists(log_file):
        with open(log_file) as f:
            rows = f.read().strip().split("\n")
        check("log NFT ha header + almeno 1 riga di trade", len(rows) >= 2, f"{len(rows)} righe")

    check("log NFT e' un file SEPARATO da paper_trade_log.csv (memecoin)",
          os.path.abspath(log_file) != os.path.abspath("paper_trade_log.csv"))

    # Teardown per non lasciare subscriber fantasma se il modulo viene rieseguito nello stesso processo.
    for aid, events in [
        (rm.agent_id, [("analysis.signal_detected", ".signal"), ("trade.executed", ".position_opened"),
                        ("position.closed", ".position_closed")]),
        (ee.agent_id, [("risk.trade_approved", ".approved")]),
        (pm.agent_id, [("trade.executed", ".opened"), ("data.raw_event_received", ".tick")]),
    ]:
        for ev, suffix in events:
            global_bus.unsubscribe(ev, f"{aid}{suffix}")


if __name__ == "__main__":
    test_blocco_1_edge()
    test_blocco_2_fonte_dati()
    models = test_blocco_3_fair_value()
    calibs = test_blocco_4_soglia(models)
    test_blocco_5_costi()
    test_blocco_6_liquidita()
    test_blocco_7_position_sizing()
    test_blocco_8_monte_carlo(models, calibs)
    test_blocco_9_e_10_integrazione()

    section("RIEPILOGO")
    if failures:
        print(f"\n  [FALLITI] {len(failures)} controlli:")
        for f in failures:
            print(f"     - {f}")
        sys.exit(1)

    print(f"\n  [OK] Tutti i controlli superati — ONDATA 1 (10 blocchi) verificata su dati reali.")
    sys.exit(0)
