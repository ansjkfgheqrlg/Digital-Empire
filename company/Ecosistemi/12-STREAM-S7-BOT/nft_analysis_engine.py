"""
ONDATA 1 — Blocchi 1, 3-9: motore di analisi NFT (Stream S7, layer NFT).

Si affianca al motore memecoin gia' chiuso (G-A/G-B/G-C: analysis_engine.py,
risk_manager.py, execution_engine.py, position_monitor.py) — non li riscrive,
li riusa dove serve (Blocco 7/9). File frozen del task (event_bus.py,
memory_interface.py, quality_gates.py, gate_verifiers.py, gate_agent.py,
meta_agent.py, orchestrator.py, ruflo_adapter.py, analysis_engine.py,
risk_manager.py, execution_engine.py, position_monitor.py) NON toccati.

Ogni funzione qui sotto e' un blocco della Ondata 1, numerato come nel task
(company/Memory/tasks/TASK-GAEL-20260730-STREAM-S7-NFT-METODO.md, sezione 3).
"""
import logging
import math
from typing import Any, Dict, List, Optional, Tuple

from event_bus import global_bus
from nft_magiceden_client import best_rarity_rank

logger = logging.getLogger(__name__)

# --------------------------------------------------------------------------- #
# BLOCCO 1 — Edge dichiarato
# --------------------------------------------------------------------------- #
EDGE_STATEMENT = (
    "Mismatch floor-price/rarity su Magic Eden: un listing prezzato sotto il "
    "fair-value implicito dal suo rank di rarita' nella stessa collection "
    "(non il mempool-spike edge del memecoin, gia' coperto da analysis_engine.py)."
)
STRATEGY_NAME = "nft_floor_rarity_mismatch_v1"
PROBLEM_TYPE = "nft_listing_mismatch_detection"


# --------------------------------------------------------------------------- #
# BLOCCO 3 — Modello di fair value (regressione reale su dati fetchati)
# --------------------------------------------------------------------------- #
class FairValueModel:
    """
    Fair value stimato per NFT come funzione lineare della rarity rank media
    (Blocco 3). Fit ai minimi quadrati su listing reali (niente libreria
    esterna: 2 parametri, formula chiusa, verificabile a mano).

    price_hat(rank) = intercept + slope * rank
    """

    def __init__(self):
        self.intercept: Optional[float] = None
        self.slope: Optional[float] = None
        self.r_squared: Optional[float] = None
        self.n_points: int = 0

    @staticmethod
    def _extract_points(listings: List[Dict[str, Any]]) -> Tuple[List[float], List[float]]:
        ranks, prices = [], []
        for lst in listings:
            rank = best_rarity_rank(lst)
            price = lst.get("price")
            if rank is None or not isinstance(price, (int, float)) or price <= 0:
                continue
            ranks.append(float(rank))
            prices.append(float(price))
        return ranks, prices

    def fit(self, listings: List[Dict[str, Any]]) -> Dict[str, Any]:
        ranks, prices = self._extract_points(listings)
        n = len(ranks)
        if n < 3:
            raise ValueError(f"Servono almeno 3 listing con rarity+price validi, trovati {n}")

        mean_x = sum(ranks) / n
        mean_y = sum(prices) / n
        ss_xy = sum((x - mean_x) * (y - mean_y) for x, y in zip(ranks, prices))
        ss_xx = sum((x - mean_x) ** 2 for x in ranks)

        self.slope = ss_xy / ss_xx if ss_xx else 0.0
        self.intercept = mean_y - self.slope * mean_x
        self.n_points = n

        # R^2
        ss_tot = sum((y - mean_y) ** 2 for y in prices)
        ss_res = sum((y - (self.intercept + self.slope * x)) ** 2 for x, y in zip(ranks, prices))
        self.r_squared = 1 - (ss_res / ss_tot) if ss_tot else 0.0

        return {
            "n_points": self.n_points,
            "slope": self.slope,
            "intercept": self.intercept,
            "r_squared": self.r_squared,
        }

    def predict(self, rank: float) -> float:
        if self.slope is None:
            raise RuntimeError("FairValueModel non addestrato: chiama fit() prima")
        return self.intercept + self.slope * rank

    def residuals(self, listings: List[Dict[str, Any]]) -> List[float]:
        """residuo = prezzo_reale - prezzo_atteso_dal_modello (negativo = sottoprezzato)."""
        ranks, prices = self._extract_points(listings)
        return [p - self.predict(r) for r, p in zip(ranks, prices)]

    def fair_values_and_prices(self, listings: List[Dict[str, Any]]) -> Tuple[List[float], List[float]]:
        """Stesso filtro/ordine di residuals(): (fair_value_stimato, prezzo_reale) per listing valido."""
        ranks, prices = self._extract_points(listings)
        fair_values = [self.predict(r) for r in ranks]
        return fair_values, prices


# --------------------------------------------------------------------------- #
# BLOCCO 4 — Soglia di ingresso statistica (calibrata sui residui reali)
# --------------------------------------------------------------------------- #
DEFAULT_ENTRY_Z = 1.5  # numero di deviazioni standard sotto la media dei residui


def calibrate_entry_threshold(residuals: List[float], z: float = DEFAULT_ENTRY_Z) -> Dict[str, float]:
    """
    Soglia = media(residui) - z * std(residui). Un listing e' un segnale BUY
    quando il suo residuo (prezzo reale - fair value stimato) e' sotto questa
    soglia, cioe' e' sottoprezzato di piu' di z deviazioni standard rispetto
    al mismatch "tipico" gia' osservato nel dataset — stesso stile statistico
    di analysis_engine.spike_threshold_sol, applicato al mismatch invece che
    al volume.
    """
    n = len(residuals)
    if n < 3:
        raise ValueError(f"Servono almeno 3 residui per calibrare, trovati {n}")
    mean_r = sum(residuals) / n
    var_r = sum((r - mean_r) ** 2 for r in residuals) / (n - 1)
    std_r = math.sqrt(var_r)
    threshold = mean_r - z * std_r
    return {"mean_residual_sol": mean_r, "std_residual_sol": std_r, "entry_threshold_sol": threshold, "z": z, "n": n}


# --------------------------------------------------------------------------- #
# BLOCCO 5 — Modello di costo reale
# --------------------------------------------------------------------------- #
# Fonte: STUDIO-NFT-FASE0.md §2 — verificato oggi via chiamate reali dove possibile.
MARKETPLACE_FEE_PCT = 0.02          # NON riverificato oggi con fonte primaria propria (429 sull'endpoint) — DA CONFERMARE
SOLANA_BASE_FEE_LAMPORTS = 5000      # costante di protocollo Solana documentata (non stimata)
LAMPORTS_PER_SOL = 1_000_000_000
DEFAULT_CREATOR_ROYALTY_PCT = 0.0    # non presente nel payload /listings fetchato oggi — DA CONFERMARE per collection


def net_edge_sol(
    listing_price_sol: float,
    fair_value_sol: float,
    marketplace_fee_pct: float = MARKETPLACE_FEE_PCT,
    creator_royalty_pct: float = DEFAULT_CREATOR_ROYALTY_PCT,
    priority_fee_lamports: float = 0.0,
    base_fee_lamports: float = SOLANA_BASE_FEE_LAMPORTS,
) -> Dict[str, float]:
    """
    Edge lordo = fair_value - listing_price (quanto e' sottoprezzato).
    Edge netto = edge lordo - fee marketplace (sul prezzo pagato) - royalty
    creator (sul prezzo pagato, pagata alla rivendita) - gas (base+priority).
    Tutto in SOL, mai lamports non convertiti (Blocco/criterio unita' di misura).
    """
    gross_edge = fair_value_sol - listing_price_sol
    fee_cost = listing_price_sol * marketplace_fee_pct
    royalty_cost = listing_price_sol * creator_royalty_pct
    gas_cost = (base_fee_lamports + priority_fee_lamports) / LAMPORTS_PER_SOL
    total_cost = fee_cost + royalty_cost + gas_cost
    net_edge = gross_edge - total_cost
    net_edge_pct_of_price = (net_edge / listing_price_sol * 100.0) if listing_price_sol else 0.0
    return {
        "gross_edge_sol": gross_edge,
        "fee_cost_sol": fee_cost,
        "royalty_cost_sol": royalty_cost,
        "gas_cost_sol": gas_cost,
        "total_cost_sol": total_cost,
        "net_edge_sol": net_edge,
        "net_edge_pct_of_price": net_edge_pct_of_price,
    }


# --------------------------------------------------------------------------- #
# BLOCCO 6 — Modello di liquidita' (da attivita' reali, Poisson esatto)
# --------------------------------------------------------------------------- #
def estimate_liquidity_days(
    activities: List[Dict[str, Any]],
    listed_count: int,
    sale_types: Tuple[str, ...] = ("buyNow", "sale"),
) -> Dict[str, float]:
    """
    Stima quanti giorni ci si aspetta di attendere perche' UN listing
    specifico trovi un acquirente, dal tasso di vendite reali osservato
    nella finestra di attivita' fetchata.

    IC al 95% con formula esatta di Poisson (k eventi in T giorni di
    esposizione reale): niente scipy nell'ambiente, chi-quadro con df pari
    ha forma chiusa (vedi commento inline) — non approssimato a mano libera.
    """
    times = sorted(a["blockTime"] for a in activities if a.get("blockTime"))
    if len(times) < 2:
        raise ValueError("Servono almeno 2 timestamp reali per stimare una finestra di esposizione")

    span_days = (times[-1] - times[0]) / 86400.0
    if span_days <= 0:
        raise ValueError("Finestra di esposizione nulla: dati insufficienti")

    k = sum(1 for a in activities if a.get("type") in sale_types)
    point_rate = k / span_days if span_days else 0.0

    # chi2^-1(0.025, df=2) = -2*ln(1-0.025)  (df=2 e' Exp(scale=2), forma chiusa esatta)
    chi2_025_df2 = -2 * math.log(1 - 0.025)
    # chi2^-1(0.975, df=4): forma chiusa df pari (m=2), F(x)=1-e^{-x/2}(1+x/2)=0.975, bisezione
    chi2_975_df4 = _chi2_quantile_df4(0.975)

    if k == 0:
        # Nessuna vendita osservata: solo limite superiore stimabile (tasso >= 0).
        lower_rate, upper_rate = 0.0, chi2_975_df4 / (2 * span_days)
    else:
        lower_rate = chi2_025_df2 / (2 * span_days)
        upper_rate = chi2_975_df4 / (2 * span_days)

    def days_for(rate: float) -> float:
        return (listed_count / rate) if rate > 0 else float("inf")

    return {
        "k_sales_observed": k,
        "span_days_observed": span_days,
        "point_sales_per_day": point_rate,
        "ci95_sales_per_day": (lower_rate, upper_rate),
        "expected_days_to_sell_point": days_for(point_rate),
        "expected_days_to_sell_ci95": (days_for(upper_rate), days_for(lower_rate)),
    }


def _chi2_quantile_df4(p: float) -> float:
    """CDF chiusa per chi-quadro df=4: F(x) = 1 - e^(-x/2)(1+x/2). Bisezione numerica."""
    def cdf(x: float) -> float:
        return 1 - math.exp(-x / 2) * (1 + x / 2)

    lo, hi = 0.0, 100.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if cdf(mid) < p:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


# --------------------------------------------------------------------------- #
# BLOCCO 7 — Position sizing (riusa RiskManager esistente, non lo duplica)
# --------------------------------------------------------------------------- #
def position_size_sol(risk_manager) -> float:
    """
    Stesso calcolo di RiskManager.assess_trade (bankroll * max_position_pct%),
    letto dall'istanza esistente passata dal chiamante — zero logica di rischio
    reimplementata qui. Se si vuole il gate anti-3-posizioni/kill-switch reale,
    si pubblica il segnale su un Event Bus dove un RiskManager e' iscritto
    (Blocco 9), non si richiama questa funzione da sola in produzione.
    """
    return risk_manager.bankroll * (risk_manager.max_position_pct / 100.0)


# --------------------------------------------------------------------------- #
# BLOCCO 9 — Integrazione architetturale: pubblica sull'Event Bus esistente
# --------------------------------------------------------------------------- #
class NFTAnalysisEngine:
    """
    Layer NFT — pubblica "analysis.signal_detected" (evento GIA' catalogato,
    stesso event_bus.py, zero modifiche) quando un listing e' sotto soglia.
    Un RiskManager iscritto allo stesso bus lo approva/rifiuta esattamente
    come un segnale memecoin — nessuna logica di rischio duplicata.

    Non condivide il bus globale del bot memecoin gia' in produzione (main.py):
    RiskManager/ExecutionEngine non hanno un campo di routing per asset class
    e non li tocco per aggiungerlo (file frozen). Il layer NFT gira su un
    EventBus dedicato (stessa classe, istanza separata) per evitare la doppia
    esecuzione dello stesso segnale approvato su due Execution Engine distinti.
    """

    def __init__(self, bus=None, agent_id: str = "NFT-ANALYSIS-ENGINE-1", fair_value_model: Optional[FairValueModel] = None):
        self.agent_id = agent_id
        self.bus = bus or global_bus
        self.fair_value_model = fair_value_model or FairValueModel()
        self.entry_threshold_sol: Optional[float] = None
        self.last_signals: List[Dict[str, Any]] = []

    def calibrate(self, listings: List[Dict[str, Any]]) -> Dict[str, Any]:
        fit_stats = self.fair_value_model.fit(listings)
        residuals = self.fair_value_model.residuals(listings)
        calib = calibrate_entry_threshold(residuals)
        self.entry_threshold_sol = calib["entry_threshold_sol"]
        return {"fit": fit_stats, "calibration": calib}

    def scan_listings(self, symbol: str, listings: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Blocco 1+4+9: per ogni listing reale, calcola il residuo e pubblica un
        segnale BUY se sotto soglia. Ritorna i segnali pubblicati (per i test).
        """
        if self.entry_threshold_sol is None:
            raise RuntimeError("Chiama calibrate() prima di scan_listings()")

        published = []
        for lst in listings:
            rank = best_rarity_rank(lst)
            price = lst.get("price")
            if rank is None or not isinstance(price, (int, float)):
                continue
            predicted = self.fair_value_model.predict(rank)
            residual = price - predicted
            if residual <= self.entry_threshold_sol:
                signal = {
                    "action": "BUY",
                    "asset_class": "nft",
                    "collection": symbol,
                    "token_address": lst.get("tokenMint"),
                    "strategy": STRATEGY_NAME,
                    "listing_price_sol": price,
                    "fair_value_sol": predicted,
                    "residual_sol": residual,
                    "rarity_rank_avg": rank,
                    "confidence": 0.6,  # dichiarata, non calibrata su esiti reali finche' Ondata 2 blocco 1 non gira
                }
                self.bus.publish("analysis.signal_detected", signal)
                published.append(signal)
        self.last_signals = published
        return published
