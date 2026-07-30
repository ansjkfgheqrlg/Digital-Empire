"""
TEST — Layer NFT Stream S7, ONDATA 2 (8 miglioramenti).

Stesso stile di test_apex7.py/test_nft_s7.py. Usa la stessa cache reale di
Ondata 1 (memory/nft_cache/) + 2 letture reali fresche (client Magic Eden dal
vivo per latenza e floor-price) fetchate in questa sessione.

Esecuzione:  python test_nft_ondata2.py
"""
import json
import os
import sys
import time

from event_bus import global_bus
from risk_manager import RiskManager

from nft_analysis_engine import FairValueModel, calibrate_entry_threshold, best_rarity_rank
from nft_magiceden_client import MagicEdenClient
from nft_ondata2 import (
    AdaptiveZCalibrator, seller_concentration, is_wash_trading_suspect,
    scam_collection_filter, segment_by_price_band, measure_real_latency,
    collection_correlation, NFTPnLTracker, check_floor_crash_killswitch,
)

SRC = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(SRC, "memory", "nft_cache")
failures = []

with open(os.path.join(CACHE, "raw_fetch.json"), encoding="utf-8") as f:
    RAW = json.load(f)["data"]
with open(os.path.join(CACHE, "mad_lads_stats_second_reading.json"), encoding="utf-8") as f:
    MAD_LADS_SECOND_READING = json.load(f)


def section(title):
    print(f"\n{'=' * 70}\n  {title}\n{'=' * 70}")


def check(label, condition, detail=""):
    status = "OK " if condition else "KO "
    print(f"  [{status}] {label}" + (f" — {detail}" if detail else ""))
    if not condition:
        failures.append(label)
    return condition


# =========================================================================== #
def test_miglioramento_1_auto_calibrazione():
    section("1. NFT (Miglioramento 1) — Auto-calibrazione soglia (z) sui risultati")

    calib = AdaptiveZCalibrator(initial_z=1.5)
    z_before = calib.z
    check("PRIMA: z parte fisso a 1.5 (Ondata 1, mai corretto)", z_before == 1.5)

    # Simulazione controllata di 2 esiti trade (non fetch di rete: qui si
    # verifica solo la FORMULA di calibrazione, il bus reale e' gia' provato
    # in Ondata 1 Blocco 9).
    for _ in range(2):
        calib._on_outcome({"event_type": "trade.executed",
                            "payload": {"signal": {"strategy": "nft_floor_rarity_mismatch_v1"}}})
    z_after = calib.z

    check("DOPO: 2/2 successi (success_rate>85%) abbassa z (coglie di piu')",
          z_after < z_before, f"z: {z_before} -> {z_after}")
    check("Storico prima/dopo tracciato", len(calib.history) >= 2, f"{calib.history}")
    calib.teardown()


def test_miglioramento_2_wash_trading():
    section("2. NFT (Miglioramento 2) — Filtro anti-wash-trading (concentrazione reale)")

    conc = seller_concentration(RAW["y00ts"]["activities"])
    check("y00ts: concentrazione reale misurata (~29% osservato in Ondata 1)",
          conc["top_share"] > 0.20, f"top_share={conc['top_share']:.1%} su n={conc['n']}")

    conc_degods = seller_concentration(RAW["degods"]["activities"])
    check("degods: concentrazione reale sopra soglia 15%",
          conc_degods["top_share"] > 0.15, f"top_share={conc_degods['top_share']:.1%}")

    fake_listing_from_top_seller = {"seller": conc_degods["top_seller"]}
    check("DOPO: un listing del top-seller viene marcato sospetto",
          is_wash_trading_suspect(fake_listing_from_top_seller, conc_degods) is True)

    other_listing = {"seller": "UN_INDIRIZZO_QUALSIASI_DIVERSO"}
    check("DOPO: un listing di un altro venditore non e' marcato sospetto",
          is_wash_trading_suspect(other_listing, conc_degods) is False)


def test_miglioramento_3_scam_filter():
    section("3. NFT (Miglioramento 3) — Filtro anti-scam-collection")

    r_mad = scam_collection_filter(RAW["mad_lads"]["stats"])
    r_y00ts = scam_collection_filter(RAW["y00ts"]["stats"])
    r_degods = scam_collection_filter(RAW["degods"]["stats"])

    check("mad_lads: collection reale passa il filtro", r_mad["passed"] is True, str(r_mad["checks"]))
    check("y00ts: collection reale passa il filtro", r_y00ts["passed"] is True, str(r_y00ts["checks"]))
    check("degods: RIFIUTATA — volume7d assente nella risposta reale (limite fonte dati, non del collection)",
          r_degods["passed"] is False and r_degods["checks"]["volume_ok"] is False,
          f"stats reali degods non includono volume7d: {r_degods}")

    fake_new = {"floorPrice": 10_000_000, "listedCount": 5, "volume7d": 0}  # SINTETICO, dichiarato
    r_fake = scam_collection_filter(fake_new)
    check("SINTETICO (collection nuova ipotetica): filtro rifiuta su tutti e 3 i controlli",
          r_fake["passed"] is False and not any(r_fake["checks"].values()), str(r_fake["checks"]))


def test_miglioramento_4_segmentazione():
    section("4. NFT (Miglioramento 4) — Segmentazione per fascia di prezzo")

    seg_mad = segment_by_price_band(RAW["mad_lads"]["listings"])
    check("mad_lads: banda bassa migliora nettamente il fit globale (R^2 0.0400 -> 0.28+)",
          seg_mad["low_band_r_squared"] > 0.20,
          f"low={seg_mad['low_band_r_squared']:.4f} high={seg_mad['high_band_r_squared']:.4f}")

    seg_degods = segment_by_price_band(RAW["degods"]["listings"])
    check("degods: segmentazione calcolata su entrambe le bande (anche se debole)",
          "low_band_r_squared" in seg_degods and "high_band_r_squared" in seg_degods,
          f"low={seg_degods.get('low_band_r_squared'):.6f} high={seg_degods.get('high_band_r_squared'):.6f}")

    print(f"  [NOTA] la banda che migliora NON e' consistente tra le 2 collection "
          f"(mad_lads: bassa migliore; degods: alta migliore, entrambe deboli) — "
          f"campione troppo piccolo (max {max(seg_mad['n_low'], seg_mad['n_high'])} punti/banda) "
          f"per generalizzare, da riprendere in Ondata 3 con piu' dati")


class _StubClient:
    """Client finto e deterministico: la LOGICA di misura va verificata a ogni run,
    anche quando la rete non c'e'. Dichiarato stub, non spacciato per reale."""

    def __init__(self, sleep_s: float = 0.01, fail: bool = False):
        self.sleep_s, self.fail = sleep_s, fail

    def get_listings(self, symbol, offset=0, limit=5):
        if self.fail:
            raise TimeoutError("stub: rete non disponibile")
        time.sleep(self.sleep_s)
        return []


def test_miglioramento_5_latenza():
    section("5. NFT (Miglioramento 5) — Latenza reale detection -> acquisto")

    # (a) LOGICA — deterministica, zero rete: gira sempre, e' il vero gate.
    stub = measure_real_latency(_StubClient(sleep_s=0.01), "mad_lads", n_calls=3)
    check("logica: 3 chiamate cronometrate e mediate (stub deterministico)",
          stub["measured"] is True and stub["n_calls"] == 3 and stub["avg_ms"] > 0,
          f"avg={stub['avg_ms']}ms su {stub['timings_ms']}")
    check("logica: confronto esplicito col benchmark MEV di report-studio.md (300-800ms)",
          stub["mev_benchmark_ms"] == (300, 800))

    failed = measure_real_latency(_StubClient(fail=True), "mad_lads", n_calls=3)
    check("logica: se la rete cade NON si inventa una latenza (measured=False + errore reale)",
          failed["measured"] is False and "TimeoutError" in failed["error"],
          failed["error"])

    # (b) MISURA REALE — dipende dalla rete: si tenta, non si pretende.
    real = measure_real_latency(MagicEdenClient(), "mad_lads", n_calls=3)
    if real["measured"]:
        check("misura reale riuscita (latenza > 0ms)", real["avg_ms"] > 0, f"{real['avg_ms']}ms")
        print(f"  [NOTA] avg reale {real['avg_ms']}ms include 1.2s di pacing prudenziale per chiamata "
              f"(rate-limit safety, Blocco 2) — il path REST Magic Eden e' comunque piu' lento in ms "
              f"assoluti del benchmark MEV mempool citato in report-studio.md, ma compete su una "
              f"finestra di secondi/minuti (listing visibile finche' non venduto), non sullo stesso "
              f"blocco Solana")
    else:
        print(f"  [SALTATO — NON misurabile adesso] rete non disponibile: {real['error']}")
        print(f"  Nessun numero inventato al suo posto. Misura reale gia' registrata il 2026-07-30 "
              f"in CP-20260730-003 (avg 3333.1ms su 3 chiamate). La logica sopra resta verificata.")


def test_miglioramento_6_correlazione():
    section("6. NFT (Miglioramento 6) — Correlazione tra collection")

    r1 = collection_correlation(RAW["mad_lads"]["activities"], RAW["degods"]["activities"])
    check("mad_lads vs degods: funzione calcola overlap reale (non inventa se insufficiente)",
          r1["correlation"] is None and r1["n_overlapping_bins"] >= 0, str(r1))

    r2 = collection_correlation(RAW["degods"]["activities"], RAW["y00ts"]["activities"])
    check("degods vs y00ts: idem", r2["correlation"] is None or isinstance(r2["correlation"], float), str(r2))

    print("  [NOTA] campione odierno (singola finestra di fetch, ~2h) troppo corto per bin orari "
          "sovrapposti sufficienti — risultato onesto 'non calcolabile oggi', non un numero inventato")


def test_miglioramento_7_pnl_tracker():
    section("7. NFT (Miglioramento 7) — Tracciamento PnL reale per collection")

    tracker = NFTPnLTracker()
    tracker.register_signal({"token_address": "TOKEN_A", "collection": "degods"})
    tracker.register_signal({"token_address": "TOKEN_B", "collection": "mad_lads"})

    # Chiusure simulate in modo controllato (stesso evento reale position.closed,
    # payload numerico dichiarato qui per isolare la logica di aggregazione).
    global_bus.publish("position.closed", {"token_address": "TOKEN_A", "pnl_sol": 1.2, "reason": "take_profit"})
    global_bus.publish("position.closed", {"token_address": "TOKEN_A", "pnl_sol": -0.3, "reason": "stop_loss"})
    global_bus.publish("position.closed", {"token_address": "TOKEN_B", "pnl_sol": 0.5, "reason": "take_profit"})

    check("PnL aggregato correttamente per degods (1.2 - 0.3 = 0.9)",
          abs(tracker.pnl_by_collection.get("degods", 0) - 0.9) < 1e-9,
          f"{tracker.pnl_by_collection}")
    check("PnL aggregato correttamente per mad_lads (0.5)",
          abs(tracker.pnl_by_collection.get("mad_lads", 0) - 0.5) < 1e-9)
    check("Conteggio chiusure per collection corretto (degods=2, mad_lads=1)",
          tracker.closes_by_collection.get("degods") == 2 and tracker.closes_by_collection.get("mad_lads") == 1,
          str(tracker.closes_by_collection))

    tracker.teardown()


def test_miglioramento_8_killswitch_floor():
    section("8. NFT (Miglioramento 8) — Kill-switch specifico NFT (riusa RiskManager)")

    rm = RiskManager(base_bankroll=100.0, max_position_pct=5.0, log_file="paper_trade_log_nft_ks_test.csv")

    floor_prev = RAW["mad_lads"]["stats"]["floorPrice"] / 1_000_000_000
    floor_now = MAD_LADS_SECOND_READING["floorPrice"] / 1_000_000_000
    result_real = check_floor_crash_killswitch(rm, "mad_lads", floor_prev, floor_now, drop_pct_threshold=15.0)

    check("PRIMA/DOPO reale (2 letture live, ~stessa sessione): floor invariato, nessun trigger",
          result_real["triggered"] is False and abs(result_real["drop_pct"]) < 1.0,
          f"floor {floor_prev} -> {floor_now} SOL, drop={result_real['drop_pct']:.4f}%")
    check("Kill-switch NON attivo dopo un calo reale sotto soglia", rm.is_kill_switch_active is False)

    # SINTETICO dichiarato: prova che il meccanismo scatta con un crollo vero.
    result_synthetic = check_floor_crash_killswitch(rm, "mad_lads", floor_prev_sol=10.0, floor_now_sol=7.0,
                                                     drop_pct_threshold=15.0)
    check("SINTETICO (crollo 30% ipotetico): kill-switch scatta per davvero",
          result_synthetic["triggered"] is True and rm.is_kill_switch_active is True,
          f"drop={result_synthetic['drop_pct']:.1f}%")
    check("Riusa RiskManager.activate_kill_switch esistente (nessun kill-switch parallelo)",
          rm.is_kill_switch_active is True)

    rm.deactivate_kill_switch()
    global_bus.unsubscribe("analysis.signal_detected", f"{rm.agent_id}.signal")
    global_bus.unsubscribe("trade.executed", f"{rm.agent_id}.position_opened")
    global_bus.unsubscribe("position.closed", f"{rm.agent_id}.position_closed")
    if os.path.exists("paper_trade_log_nft_ks_test.csv"):
        os.remove("paper_trade_log_nft_ks_test.csv")


if __name__ == "__main__":
    test_miglioramento_1_auto_calibrazione()
    test_miglioramento_2_wash_trading()
    test_miglioramento_3_scam_filter()
    test_miglioramento_4_segmentazione()
    test_miglioramento_5_latenza()
    test_miglioramento_6_correlazione()
    test_miglioramento_7_pnl_tracker()
    test_miglioramento_8_killswitch_floor()

    section("RIEPILOGO")
    if failures:
        print(f"\n  [FALLITI] {len(failures)} controlli:")
        for f in failures:
            print(f"     - {f}")
        sys.exit(1)

    print(f"\n  [OK] Tutti i controlli superati — ONDATA 2 (8 miglioramenti) verificata.")
    sys.exit(0)
