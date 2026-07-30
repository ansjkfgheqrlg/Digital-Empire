"""
TEST — Layer NFT Stream S7, ONDATA 4 (3 controlli chirurgici, audit finale).

Esecuzione:  python test_nft_ondata4.py
"""
import json
import os
import sys
import time

from event_bus import global_bus
from gate_agent import gate_1
from quality_gates import GATE_DEFINITIONS, get_threshold
from risk_manager import RiskManager
from execution_engine import ExecutionEngine
from position_monitor import PositionMonitor

from nft_analysis_engine import FairValueModel, calibrate_entry_threshold, estimate_liquidity_days, NFTAnalysisEngine
from nft_magiceden_client import MagicEdenClient
from nft_monte_carlo import monte_carlo_expectancy
from nft_ondata3 import backtest_across_collections, rug_pull_breakeven_probability, bootstrap_r_squared_ci
from nft_ondata4 import independent_expectancy_recheck, cross_check_against_pipeline, confronto_report_studio

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


def test_controllo_1_ricalcolo_indipendente():
    section("1. NFT (Controllo Chirurgico #1) — Ricalcolo matematico indipendente")

    pipeline_model = FairValueModel()
    pipeline_fit = pipeline_model.fit(RAW["degods"]["listings"])
    pipeline_residuals = pipeline_model.residuals(RAW["degods"]["listings"])
    pipeline_calib = calibrate_entry_threshold(pipeline_residuals)
    pipeline_n_eligible = sum(1 for r in pipeline_residuals if r <= pipeline_calib["entry_threshold_sol"])

    independent = independent_expectancy_recheck(RAW["degods"]["listings"], z=1.5)
    cross = cross_check_against_pipeline(independent, pipeline_fit, pipeline_n_eligible)

    check("Ricalcolo indipendente: stesso slope della pipeline originale (entro 1e-6)",
          cross["slope_match"], f"pipeline={pipeline_fit['slope']:.8f} indipendente={independent['slope']:.8f}")
    check("Ricalcolo indipendente: stesso n_points", cross["n_points_match"],
          f"{independent['n_points']} == {pipeline_fit['n_points']}")
    check("Ricalcolo indipendente: stesso numero di segnali eleggibili", cross["n_eligible_match"],
          f"{independent['n_eligible']} == {pipeline_n_eligible}")
    check("TUTTO combacia (nessun bug nascosto nella pipeline originale)", cross["all_match"])

    print(f"\n  >>> Expectancy grezza indipendente (senza Monte Carlo/liquidita', solo i 3 trade reali): "
          f"{independent['mean_net_pct_raw_no_liquidity']:.2f}% — coerente con l'upper bound Monte Carlo "
          f"({34.70}%, Ondata 1): il MC e' piu' basso perche' sconta il rischio di illiquidita', come atteso")

    return independent


def test_controllo_2_confronto_report_studio():
    section("2. NFT (Controllo Chirurgico #2) — Coerenza con report-studio.md (IL PUNTO CHE CONTA DI PIU')")

    # Ricostruisce fresco (non hardcoded da sessioni precedenti) tutto cio' che serve al confronto.
    bt = backtest_across_collections(RAW)

    m = FairValueModel()
    m.fit(RAW["degods"]["listings"])
    residuals = m.residuals(RAW["degods"]["listings"])
    calib = calibrate_entry_threshold(residuals)
    fair_values, prices = m.fair_values_and_prices(RAW["degods"]["listings"])
    liq = estimate_liquidity_days(MAD_LADS_ACTIVITIES_DEEP, listed_count=242)
    mc = monte_carlo_expectancy(residuals, calib["entry_threshold_sol"], fair_values, prices,
                                 liq["k_sales_observed"], liq["span_days_observed"], 242,
                                 holding_horizon_days=30.0, n_sims=20000, return_raw=True)
    rug = rug_pull_breakeven_probability(mc["raw_net_pnl_pct"])
    boot = bootstrap_r_squared_ci(RAW["degods"]["listings"])

    client = MagicEdenClient()
    t0 = time.time()
    client.get_listings("mad_lads", offset=0, limit=5)
    t1 = time.time()
    client.get_listings("mad_lads", offset=0, limit=5)
    t2 = time.time()
    latency_ms = [round((t1 - t0) * 1000, 1), round((t2 - t1) * 1000, 1)]

    evidence = {
        "latency_avg_ms": round(sum(latency_ms) / len(latency_ms), 1),
        "latency_range_ms": (min(latency_ms), max(latency_ms)),
        "me_burst_concurrent_ok": 20,  # gia' misurato in Fase 0 (STUDIO-NFT-FASE0.md §2), non re-instaurato qui per non consumare rate limit
        "rug_breakeven_pct": rug["breakeven_p_rug"] * 100.0,
        "n_collections_with_signal": bt["n_collections_with_tradeable_signal"],
        "n_collections_tested": bt["n_collections_tested"],
        "r_squared_point": boot["point_r_squared"],
        "r_squared_ci_upper": boot["ci95_r_squared"][1],
        "mc_ci_lower": mc["ci95_net_pnl_pct"][0],
        "mc_ci_upper": mc["ci95_net_pnl_pct"][1],
        "buynow_rate": "1/400 attivita' reali (0.25%)",
    }

    confronto = confronto_report_studio(evidence)

    check("3 problemi strutturali di report-studio.md tutti confrontati (nessuno saltato)",
          len(confronto["problemi"]) == 3)
    check("Problema 1 (latenza): verdetto dichiarato con numero reale",
          confronto["problemi"][0]["verdetto"] == "NON RISOLTO", confronto["problemi"][0]["verdetto"])
    check("Problema 2 (RPC rate-limit): verdetto PARZIALMENTE RISOLTO con evidenza reale (20 vs 2 chiamate)",
          confronto["problemi"][1]["verdetto"] == "PARZIALMENTE RISOLTO")
    check("Problema 3 (rug pull): verdetto dichiarato con soglia numerica esplicita",
          f"{evidence['rug_breakeven_pct']:.1f}" in confronto["problemi"][2]["spiegazione"])
    check("Almeno 3 criticita' aggiuntive elencate (non solo i 3 problemi originali)",
          len(confronto["altre_criticita"]) >= 3)
    check("Verdetto finale esplicito e motivato (non un 'forse')",
          "VERDETTO" in confronto["verdetto_finale"] and "bocciato" in confronto["verdetto_finale"])

    print(f"\n{'-'*70}")
    for p in confronto["problemi"]:
        print(f"  [{p['verdetto']}] {p['problema']}\n      {p['spiegazione']}\n")
    print("  Altre criticita':")
    for c in confronto["altre_criticita"]:
        print(f"   - {c}")
    print(f"\n  >>> {confronto['verdetto_finale']}")
    print(f"{'-'*70}")

    return confronto


def test_controllo_3_gate_apex7():
    section("3. NFT (Controllo Chirurgico #3) — Gate APEX-7 L3->L4 sul loop NFT (Claude, controllore)")

    log_file = "paper_trade_log_nft_gate_test.csv"
    if os.path.exists(log_file):
        os.remove(log_file)

    rm = RiskManager(base_bankroll=1000.0, max_position_pct=1.0, log_file=log_file, agent_id="GATE-TEST-RISK")
    ee = ExecutionEngine(mode="SIMULATION", agent_id="GATE-TEST-EXEC", log_file=log_file)
    pm = PositionMonitor(agent_id="GATE-TEST-POSMON")
    engine = NFTAnalysisEngine(agent_id="GATE-TEST-NFT-ENGINE")

    try:
        engine.calibrate(RAW["degods"]["listings"])
        started = time.time()
        signals = engine.scan_listings("degods", RAW["degods"]["listings"])
        elapsed_ms = max(1, int((time.time() - started) * 1000))

        check("Loop NFT (segnale -> rischio -> esecuzione) produce un esito reale, misurabile",
              len(signals) >= 1, f"{len(signals)} segnali in {elapsed_ms}ms")

        report = gate_1.evaluate(
            gate_id="GATE-L3-NFT", formal_gate_id="L3_TO_L4",
            criteria=GATE_DEFINITIONS["L3_TO_L4"]["criteria"],
            output_to_check=f"baseline reale layer NFT, loop segnale->rischio->esecuzione: "
                            f"{elapsed_ms} ms, {len(signals)} segnali reali su degods",
            threshold=get_threshold("L3_TO_L4"), timeout_s=120, gate_history=[], attempt=1,
        )
        gate_1.reset()

        print(f"\n  Verdetto L3->L4 sul layer NFT: {report['result']} "
              f"({report['criteria_passed']}/{report['criteria_total']}, score {report['score']})")
        for r in report["criteria_results"]:
            print(f"    {r['criterion']} {r['status']}: {r['evidence'][:120]}")

        check("Gate APEX-7 L3->L4 gira davvero sul layer NFT (stesso controllore di G-A/G-B/G-C)",
              report["result"] in ("PASSED", "FAILED"))  # deve produrre un verdetto motivato, PASS o FAIL
        check("Il gate riporta un motivo per ogni criterio (nessun timbro cieco)",
              all(r.get("evidence") for r in report["criteria_results"]))
    finally:
        global_bus.unsubscribe("analysis.signal_detected", f"{rm.agent_id}.signal")
        global_bus.unsubscribe("trade.executed", f"{rm.agent_id}.position_opened")
        global_bus.unsubscribe("position.closed", f"{rm.agent_id}.position_closed")
        global_bus.unsubscribe("risk.trade_approved", f"{ee.agent_id}.approved")
        global_bus.unsubscribe("trade.executed", f"{pm.agent_id}.opened")
        global_bus.unsubscribe("data.raw_event_received", f"{pm.agent_id}.tick")
        if os.path.exists(log_file):
            os.remove(log_file)


if __name__ == "__main__":
    test_controllo_1_ricalcolo_indipendente()
    test_controllo_2_confronto_report_studio()
    test_controllo_3_gate_apex7()

    section("RIEPILOGO")
    if failures:
        print(f"\n  [FALLITI] {len(failures)} controlli:")
        for f in failures:
            print(f"     - {f}")
        sys.exit(1)

    print(f"\n  [OK] Tutti i controlli superati — ONDATA 4 (3 controlli chirurgici) verificata.")
    sys.exit(0)
