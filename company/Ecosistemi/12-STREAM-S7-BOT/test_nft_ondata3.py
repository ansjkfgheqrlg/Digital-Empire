"""
TEST — Layer NFT Stream S7, ONDATA 3 (4 perfezionamenti).

Esecuzione:  python test_nft_ondata3.py
"""
import json
import os
import sys

from nft_analysis_engine import FairValueModel, calibrate_entry_threshold, estimate_liquidity_days
from nft_monte_carlo import monte_carlo_expectancy
from nft_ondata3 import (
    backtest_across_collections, stress_test_marketplace_unreachable, stress_test_market_crash,
    rug_pull_breakeven_probability, bootstrap_r_squared_ci, validate_sourced_report,
)

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


def test_perfezionamento_1_backtest():
    section("1. NFT (Perfezionamento 1) — Backtest su piu' collection reali")

    bt = backtest_across_collections(RAW)
    check("3 collection testate (nessuna scartata dal report)", bt["n_collections_tested"] == 3)
    check("2/3 collection producono un fit valido (y00ts no_fit per rarity assente)",
          bt["n_collections_fitted"] == 2, str({k: v["status"] for k, v in bt["per_collection"].items()}))
    check("SOLO 1/3 collection produce un segnale tradeable oggi (onesto, non nascosto)",
          bt["n_collections_with_tradeable_signal"] == 1,
          f"{bt['n_collections_with_tradeable_signal']}/3 — risultato reale, non un fallimento del test")
    return bt


def test_perfezionamento_2_stress():
    section("2. NFT (Perfezionamento 2) — Stress test scenari avversi")

    unreachable = stress_test_marketplace_unreachable()
    check("Marketplace irraggiungibile: eccezione reale gestita in modo pulito",
          unreachable["handled_cleanly"] is True, str(unreachable))

    m = FairValueModel()
    m.fit(RAW["degods"]["listings"])
    residuals = m.residuals(RAW["degods"]["listings"])
    calib = calibrate_entry_threshold(residuals)
    fair_values, prices = m.fair_values_and_prices(RAW["degods"]["listings"])
    liq = estimate_liquidity_days(MAD_LADS_ACTIVITIES_DEEP, listed_count=242)
    mc = monte_carlo_expectancy(residuals, calib["entry_threshold_sol"], fair_values, prices,
                                 liq["k_sales_observed"], liq["span_days_observed"], 242,
                                 holding_horizon_days=30.0, n_sims=20000, return_raw=True)

    crash = stress_test_market_crash(mc["raw_net_pnl_pct"], crash_prob=0.10, crash_severity_pct=50.0)
    check("Crash di mercato: mean_after < mean_before (peggiora, come atteso)",
          crash["mean_after_pct"] < crash["mean_before_pct"],
          f"{crash['mean_before_pct']:.2f}%% -> {crash['mean_after_pct']:.2f}%%")
    check("Crash di mercato: IC95%% inferiore crolla molto di piu' della media",
          crash["ci95_after_pct"][0] < -40.0, f"IC95%% low={crash['ci95_after_pct'][0]:.2f}%%")

    rug = rug_pull_breakeven_probability(mc["raw_net_pnl_pct"])
    check("Rug-pull breakeven calcolato (0-1)", 0.0 <= rug["breakeven_p_rug"] <= 1.0,
          f"p_rug breakeven = {rug['breakeven_p_rug']:.1%}")
    print(f"\n  >>> Se P(rug-pull/abbandono) reale > {rug['breakeven_p_rug']:.1%}, l'expectancy media "
          f"diventa negativa (mean_base={rug['mean_base_pct']:.2f}%%) — soglia esplicita per il "
          f"Controllo Chirurgico #2 (Ondata 4)")
    return mc, crash, rug


def test_perfezionamento_3_ic_fit():
    section("3. NFT (Perfezionamento 3) — Intervallo di confidenza (anche sulla qualita' del fit)")

    boot_mad = bootstrap_r_squared_ci(RAW["mad_lads"]["listings"])
    boot_deg = bootstrap_r_squared_ci(RAW["degods"]["listings"])

    check("mad_lads: bootstrap R^2 con IC95%% (non solo il punto 0.04)",
          boot_mad["ci95_r_squared"] is not None and boot_mad["ci95_r_squared"][0] < boot_mad["point_r_squared"] < boot_mad["ci95_r_squared"][1],
          f"punto={boot_mad['point_r_squared']:.4f} IC95%%={tuple(round(x,4) for x in boot_mad['ci95_r_squared'])}")
    check("degods: bootstrap R^2 con IC95%%", boot_deg["ci95_r_squared"] is not None,
          f"punto={boot_deg['point_r_squared']:.4f} IC95%%={tuple(round(x,4) for x in boot_deg['ci95_r_squared'])}")

    print(f"\n  [NOTA] il fit e' non solo debole ma INSTABILE: IC95%% di mad_lads arriva fino a "
          f"{boot_mad['ci95_r_squared'][1]:.3f}, quello di degods fino a {boot_deg['ci95_r_squared'][1]:.3f} — "
          f"il campione reale odierno non basta per distinguere 'nessun edge' da 'edge modesto ma reale'")


def test_perfezionamento_4_fonti():
    section("4. NFT (Perfezionamento 4) — Ogni percentuale cita la fonte")

    good_report = [
        {"label": "expectancy media (degods, MC)", "value": 20.31, "source": "nft_monte_carlo.monte_carlo_expectancy, n=20000, CP-20260730-002/004"},
        {"label": "rug breakeven p", "value": 16.9, "source": "nft_ondata3.rug_pull_breakeven_probability"},
    ]
    missing_good = validate_sourced_report(good_report)
    check("Report ben formato: 0 percentuali senza fonte", missing_good == [], str(missing_good))

    bad_report = good_report + [{"label": "numero senza fonte (test negativo)", "value": 99}]
    missing_bad = validate_sourced_report(bad_report)
    check("Validator BLOCCA un report con un numero senza fonte (test negativo)",
          missing_bad == ["numero senza fonte (test negativo)"], str(missing_bad))


if __name__ == "__main__":
    test_perfezionamento_1_backtest()
    test_perfezionamento_2_stress()
    test_perfezionamento_3_ic_fit()
    test_perfezionamento_4_fonti()

    section("RIEPILOGO")
    if failures:
        print(f"\n  [FALLITI] {len(failures)} controlli:")
        for f in failures:
            print(f"     - {f}")
        sys.exit(1)

    print(f"\n  [OK] Tutti i controlli superati — ONDATA 3 (4 perfezionamenti) verificata.")
    sys.exit(0)
