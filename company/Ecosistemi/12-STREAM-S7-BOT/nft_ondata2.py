"""
ONDATA 2 — 8 miglioramenti sopra i 10 blocchi di Ondata 1.

Ogni funzione/classe qui parte da un numero gia' misurato in Ondata 1 e lo
migliora, con un prima/dopo esplicito (task, sezione 3, Ondata 2). Nessun file
frozen toccato; riusa RiskManager/PositionMonitor esistenti dove serve
(Miglioramento 8), non li duplica.
"""
import logging
import math
import time
from collections import Counter
from typing import Any, Dict, List, Optional, Tuple

from event_bus import global_bus
from nft_analysis_engine import FairValueModel, STRATEGY_NAME
from nft_magiceden_client import MagicEdenClient, best_rarity_rank

logger = logging.getLogger(__name__)


# --------------------------------------------------------------------------- #
# MIGLIORAMENTO 1 — Auto-calibrazione della soglia sui risultati reali
# --------------------------------------------------------------------------- #
class AdaptiveZCalibrator:
    """
    PRIMA (Ondata 1, Blocco 4): z fisso a 1.5, mai corretto dagli esiti.
    DOPO: stesso pattern di analysis_engine._on_trade_closed applicato a z —
    ascolta trade.executed/trade.failed per la strategia NFT, ogni 2 esiti
    ricalcola il success_rate sugli ultimi 10 e alza/abbassa z.
    """

    ADJUST_EVERY_N = 2
    ROLLING_WINDOW = 10

    def __init__(self, initial_z: float = 1.5, agent_id: str = "NFT-Z-CALIBRATOR-1", bus=None):
        self.z = initial_z
        self.agent_id = agent_id
        self.bus = bus or global_bus
        self.recent_outcomes: List[bool] = []
        self.history: List[Tuple[float, float]] = [(0.0, self.z)]  # (t, z) per il prima/dopo
        self.bus.subscribe("trade.executed", self._on_outcome, subscriber_id=f"{agent_id}.exec")
        self.bus.subscribe("trade.failed", self._on_outcome, subscriber_id=f"{agent_id}.fail")

    def _on_outcome(self, event_msg: dict):
        payload = event_msg.get("payload", {})
        signal = payload.get("signal", {})
        if signal.get("strategy") != STRATEGY_NAME:
            return
        success = event_msg.get("event_type") == "trade.executed"
        self.recent_outcomes.append(success)
        self.recent_outcomes = self.recent_outcomes[-self.ROLLING_WINDOW:]

        if len(self.recent_outcomes) < self.ADJUST_EVERY_N or len(self.recent_outcomes) % self.ADJUST_EVERY_N:
            return

        success_rate = sum(self.recent_outcomes) / len(self.recent_outcomes)
        old_z = self.z
        if success_rate < 0.5:
            self.z = round(old_z * 1.10, 4)   # troppi falsi segnali: alzo l'asticella (piu' conservativo)
        elif success_rate > 0.85:
            self.z = round(max(old_z * 0.90, 0.5), 4)  # segnali affidabili: colgo di piu'

        if self.z != old_z:
            self.history.append((time.time(), self.z))
            logger.info(f"[{self.agent_id}] z ricalibrato: {old_z} -> {self.z} (success_rate {success_rate:.0%})")

    def teardown(self):
        self.bus.unsubscribe("trade.executed", f"{self.agent_id}.exec")
        self.bus.unsubscribe("trade.failed", f"{self.agent_id}.fail")


# --------------------------------------------------------------------------- #
# MIGLIORAMENTO 2 — Filtro anti-wash-trading (concentrazione venditore reale)
# --------------------------------------------------------------------------- #
def seller_concentration(activities: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    PRIMA (Ondata 1): scan_listings ignora del tutto chi vende — un listing
    del venditore che genera il 29%% dell'attivita' recente (misurato oggi su
    y00ts, vedi CP-20260730-002) sarebbe trattato come chiunque altro.
    DOPO: calcola la quota reale del venditore piu' attivo sull'attivita'
    recente della collection — segnale di wash-trading/market-making
    aggressivo, non prova definitiva ma soglia dichiarata e misurabile.
    """
    sellers = Counter(a.get("seller") for a in activities if a.get("seller"))
    total = sum(sellers.values())
    if total == 0:
        return {"top_seller": None, "top_share": 0.0, "n": 0}
    top_seller, top_n = sellers.most_common(1)[0]
    return {"top_seller": top_seller, "top_share": top_n / total, "n": total}


def is_wash_trading_suspect(listing: Dict[str, Any], concentration: Dict[str, Any],
                             share_threshold: float = 0.15) -> bool:
    """DOPO: un listing e' sospetto se il suo venditore E' il top-seller sopra soglia."""
    return listing.get("seller") == concentration.get("top_seller") and concentration.get("top_share", 0.0) > share_threshold


# --------------------------------------------------------------------------- #
# MIGLIORAMENTO 3 — Filtro anti-scam-collection
# --------------------------------------------------------------------------- #
MIN_FLOOR_SOL = 0.5
MIN_LISTED_COUNT = 20
MIN_VOLUME_7D_SOL = 10.0


def scam_collection_filter(stats: Dict[str, Any]) -> Dict[str, Any]:
    """
    PRIMA (Ondata 1): qualunque collection con >=3 listing validi entra nel
    modello, senza controllo di eta'/dimensione/volume.
    DOPO: 3 soglie reali su dati gia' verificati (STUDIO-NFT-FASE0.md §2) —
    floor, numero di listing, volume settimanale. Non elimina il rischio
    rug/scam (serve storia on-chain del creator, fuori scope qui), ma scarta
    i casi piu' ovvi (collection appena create con floor quasi nullo).
    """
    floor_sol = stats.get("floorPrice", 0) / 1_000_000_000
    listed = stats.get("listedCount", 0)
    volume7d_sol = stats.get("volume7d", 0) / 1_000_000_000

    checks = {
        "floor_ok": floor_sol >= MIN_FLOOR_SOL,
        "listed_count_ok": listed >= MIN_LISTED_COUNT,
        "volume_ok": volume7d_sol >= MIN_VOLUME_7D_SOL,
    }
    passed = all(checks.values())
    return {"passed": passed, "checks": checks, "floor_sol": floor_sol, "listed": listed, "volume7d_sol": volume7d_sol}


# --------------------------------------------------------------------------- #
# MIGLIORAMENTO 4 — Segmentazione del success-rate per fascia di prezzo
# --------------------------------------------------------------------------- #
def segment_by_price_band(listings: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    PRIMA (Ondata 1, Blocco 3): un solo fit globale (mad_lads R^2=0.0400,
    degods R^2=0.0264) — un unico numero medio su tutta la collection.
    DOPO: split a meta' (sopra/sotto la mediana di prezzo) e fit separato per
    banda — se il fit migliora in una banda, il segnale reale e' li', non
    spalmato uniformemente.
    """
    prices = sorted(lst.get("price", 0) for lst in listings if isinstance(lst.get("price"), (int, float)))
    if len(prices) < 6:
        raise ValueError("Servono almeno 6 listing per segmentare in 2 bande")
    median_price = prices[len(prices) // 2]

    low_band = [lst for lst in listings if isinstance(lst.get("price"), (int, float)) and lst["price"] <= median_price]
    high_band = [lst for lst in listings if isinstance(lst.get("price"), (int, float)) and lst["price"] > median_price]

    result = {"median_price_sol": median_price, "n_low": len(low_band), "n_high": len(high_band)}
    for name, band in (("low", low_band), ("high", high_band)):
        try:
            m = FairValueModel()
            fit = m.fit(band)
            result[f"{name}_band_r_squared"] = fit["r_squared"]
            result[f"{name}_band_n_points"] = fit["n_points"]
        except ValueError as e:
            result[f"{name}_band_error"] = str(e)
    return result


# --------------------------------------------------------------------------- #
# MIGLIORAMENTO 5 — Latenza reale detection -> acquisto (misurata, non assunta)
# --------------------------------------------------------------------------- #
def measure_real_latency(client: MagicEdenClient, symbol: str, n_calls: int = 3) -> Dict[str, Any]:
    """
    PRIMA (Fase 0 §2): latenza nota solo per il path RPC Solana (300-800ms,
    report-studio.md), il path REST Magic Eden non era ancora stato misurato.
    DOPO: n chiamate reali cronometrate qui, stessa API usata in produzione
    dal motore NFT (get_listings) — confronto diretto in ms, non stimato.
    """
    timings_ms = []
    for _ in range(n_calls):
        t0 = time.time()
        client.get_listings(symbol, offset=0, limit=5)
        timings_ms.append((time.time() - t0) * 1000.0)

    avg_ms = sum(timings_ms) / len(timings_ms)
    return {
        "n_calls": n_calls,
        "timings_ms": [round(t, 1) for t in timings_ms],
        "avg_ms": round(avg_ms, 1),
        "mev_benchmark_ms": (300, 800),  # report-studio.md, path RPC mempool
        "slower_than_mev_benchmark": avg_ms > 800,
    }


# --------------------------------------------------------------------------- #
# MIGLIORAMENTO 6 — Correlazione tra collection in portafoglio
# --------------------------------------------------------------------------- #
def pearson_r(xs: List[float], ys: List[float]) -> float:
    n = len(xs)
    if n < 3 or n != len(ys):
        raise ValueError("Servono >=3 coppie di punti della stessa lunghezza")
    mx, my = sum(xs) / n, sum(ys) / n
    cov = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    vx = sum((x - mx) ** 2 for x in xs)
    vy = sum((y - my) ** 2 for y in ys)
    denom = math.sqrt(vx * vy)
    return cov / denom if denom else 0.0


def bid_price_time_series(activities: List[Dict[str, Any]], bin_seconds: int = 600) -> Dict[int, float]:
    """Prezzo medio dei bid reali per bin temporale — serie osservabile da dati gia' fetchati."""
    bins: Dict[int, List[float]] = {}
    for a in activities:
        if a.get("type") != "bid" or not isinstance(a.get("price"), (int, float)) or not a.get("blockTime"):
            continue
        b = a["blockTime"] // bin_seconds
        bins.setdefault(b, []).append(a["price"])
    return {b: sum(v) / len(v) for b, v in bins.items()}


def collection_correlation(activities_a: List[Dict[str, Any]], activities_b: List[Dict[str, Any]],
                            bin_seconds: int = 600) -> Dict[str, Any]:
    """
    PRIMA (Ondata 1): ogni collection valutata in isolamento, nessuna verifica
    di concentrazione di rischio tra posizioni correlate.
    DOPO: correlazione reale (Pearson) tra le serie di prezzo-bid nei bin
    temporali in cui ENTRAMBE le collection hanno almeno un bid reale.
    Dichiarato con cautela: n piccolo (singola finestra di fetch), non un
    time-series storico lungo — vedi campo 'n_overlapping_bins'.
    """
    series_a = bid_price_time_series(activities_a, bin_seconds)
    series_b = bid_price_time_series(activities_b, bin_seconds)
    common_bins = sorted(set(series_a) & set(series_b))
    if len(common_bins) < 3:
        return {"n_overlapping_bins": len(common_bins), "correlation": None,
                "note": "Campione troppo piccolo per una correlazione affidabile con i dati fetchati oggi"}
    xs = [series_a[b] for b in common_bins]
    ys = [series_b[b] for b in common_bins]
    return {"n_overlapping_bins": len(common_bins), "correlation": pearson_r(xs, ys)}


# --------------------------------------------------------------------------- #
# MIGLIORAMENTO 7 — Tracciamento PnL reale per collection
# --------------------------------------------------------------------------- #
class NFTPnLTracker:
    """
    PRIMA (Ondata 1, Blocco 10): il CSV di paper_trade_log_nft.csv logga
    token_address/costo/status ma NON la collection (execution_engine.py e'
    frozen, non aggiungo colonne li'). Il PnL aggregato per collection era
    quindi irrecuperabile dal solo log.
    DOPO: mapping token_address -> collection popolato al momento del segnale
    (l'unico punto in cui l'informazione esiste davvero), poi accumulo del
    PnL reale letto da position.closed (evento gia' catalogato).
    """

    def __init__(self, agent_id: str = "NFT-PNL-TRACKER-1", bus=None):
        self.agent_id = agent_id
        self.bus = bus or global_bus
        self.token_to_collection: Dict[str, str] = {}
        self.pnl_by_collection: Dict[str, float] = {}
        self.closes_by_collection: Dict[str, int] = {}
        self.bus.subscribe("position.closed", self._on_closed, subscriber_id=f"{agent_id}.closed")

    def register_signal(self, signal: Dict[str, Any]):
        token = signal.get("token_address")
        collection = signal.get("collection")
        if token and collection:
            self.token_to_collection[token] = collection

    def _on_closed(self, event_msg: dict):
        payload = event_msg.get("payload", {})
        token = payload.get("token_address")
        collection = self.token_to_collection.get(token)
        if not collection:
            return  # posizione non aperta da questo tracker (es. lane memecoin)
        pnl = payload.get("pnl_sol", 0.0)
        self.pnl_by_collection[collection] = self.pnl_by_collection.get(collection, 0.0) + pnl
        self.closes_by_collection[collection] = self.closes_by_collection.get(collection, 0) + 1

    def teardown(self):
        self.bus.unsubscribe("position.closed", f"{self.agent_id}.closed")


# --------------------------------------------------------------------------- #
# MIGLIORAMENTO 8 — Kill-switch specifico NFT (riusa RiskManager, non ne crea uno nuovo)
# --------------------------------------------------------------------------- #
def check_floor_crash_killswitch(risk_manager, symbol: str, floor_prev_sol: float, floor_now_sol: float,
                                  drop_pct_threshold: float = 15.0) -> Optional[Dict[str, Any]]:
    """
    PRIMA (Ondata 1): nessun controllo sul crollo del floor — solo il
    drawdown sul bankroll (RiskManager.check_portfolio_health) blocca, e solo
    a posteriori (dopo che i trade sono gia' stati eseguiti).
    DOPO: stesso principio del kill-switch gia' esistente
    (RiskManager.activate_kill_switch), attivato PRIMA che il drawdown
    reale si materializzi, sulla base del crollo del floor osservato.
    Misurato oggi (STUDIO-NFT-FASE0.md, 2 letture reali a ~15 minuti di
    distanza): mad_lads floor invariato 7.389 -> 7.389 SOL (0.0%%, sotto
    soglia, nessun trigger) — vedi test per il caso sintetico che PROVA che
    il meccanismo scatta quando il crollo e' reale.
    """
    if floor_prev_sol <= 0:
        return None
    drop_pct = (floor_prev_sol - floor_now_sol) / floor_prev_sol * 100.0
    if drop_pct >= drop_pct_threshold:
        risk_manager.activate_kill_switch(reason=f"floor {symbol} crollato {drop_pct:.1f}%% in finestra osservata")
        return {"triggered": True, "drop_pct": drop_pct}
    return {"triggered": False, "drop_pct": drop_pct}
