"""
╔══════════════════════════════════════════════════════════════╗
║         📊 TEAM QUANT — Analisi Quantitativa                ║
║                                                              ║
║  Calcola edge statistico, EV, Win Rate, Expectancy.         ║
║  Produce segnali solo quando i numeri lo giustificano.       ║
║  Bias: NON tradare se non c'è edge misurabile.               ║
╚══════════════════════════════════════════════════════════════╝
"""
from __future__ import annotations

import math
import statistics
import time
import uuid
from typing import Dict, Any, List, Optional, Tuple

from event_bus import global_bus
from memory_interface import global_memory


class QuantTeam:
    """
    📊 Team Quant — Analisi Quantitativa dei segnali di trading.

    Agenti nel team:
    - ExpectancyCalculator: calcola EV atteso per ogni setup
    - PatternScorer: valuta la robustezza statistica di un pattern
    - RiskAdjuster: corregge la dimensione della posizione per volatilità

    Principio: Un numero senza contesto è un'opinione.
               Un numero con N >= 30 campioni è un fatto.
    """

    MIN_SAMPLES_VALID = 10   # sotto questo: segnale non statisticamente robusto
    MIN_EDGE_THRESHOLD = 0.02  # edge minimo richiesto (2%) per generare segnale

    def __init__(self, team_id: str = "QUANT-TEAM-1"):
        self.team_id = team_id
        self.analyses_run: int = 0
        self.signals_generated: int = 0
        self.signals_rejected: int = 0
        self._history: List[Dict[str, Any]] = []

        global_bus.subscribe(
            "task.created",
            self._on_task_assigned,
            subscriber_id=f"{team_id}.task_in",
        )

        print(f"[{self.team_id}] Team Quant pronto. "
              f"Edge minimo: {self.MIN_EDGE_THRESHOLD:.0%}, "
              f"campioni minimi: {self.MIN_SAMPLES_VALID}")

    # ------------------------------------------------------------------ #
    # Calcolo Expectancy (EV)
    # ------------------------------------------------------------------ #

    def calculate_expectancy(
        self,
        win_rate: float,
        avg_win: float,
        avg_loss: float,
    ) -> Dict[str, Any]:
        """
        EV = (Win Rate × Avg Win) - (Loss Rate × Avg Loss)

        Un sistema è profittevole se EV > 0.
        Un sistema è DEGNO DI FIDUCIA se EV > MIN_EDGE_THRESHOLD.
        """
        if avg_loss <= 0:
            raise ValueError("avg_loss deve essere positivo (è una perdita assoluta)")

        loss_rate = 1.0 - win_rate
        ev = (win_rate * avg_win) - (loss_rate * avg_loss)
        edge = ev / avg_loss  # edge normalizzato per la perdita media

        result = {
            "win_rate": round(win_rate, 4),
            "loss_rate": round(loss_rate, 4),
            "avg_win": avg_win,
            "avg_loss": avg_loss,
            "expected_value": round(ev, 6),
            "edge": round(edge, 4),
            "has_edge": edge >= self.MIN_EDGE_THRESHOLD,
            "quality": self._rate_edge_quality(edge),
            "verdict": "TRADE" if edge >= self.MIN_EDGE_THRESHOLD else "SKIP",
        }

        self.analyses_run += 1
        self._history.append({"type": "expectancy", "result": result, "at": time.time()})

        if result["has_edge"]:
            self.signals_generated += 1
        else:
            self.signals_rejected += 1
            print(f"[{self.team_id}] ⛔ Segnale RIFIUTATO: edge {edge:.2%} < "
                  f"soglia {self.MIN_EDGE_THRESHOLD:.2%}")

        return result

    def _rate_edge_quality(self, edge: float) -> str:
        if edge < 0:
            return "NEGATIVE"
        if edge < self.MIN_EDGE_THRESHOLD:
            return "INSUFFICIENT"
        if edge < 0.10:
            return "ACCEPTABLE"
        if edge < 0.25:
            return "GOOD"
        return "EXCELLENT"

    # ------------------------------------------------------------------ #
    # Valutazione robustezza statistica
    # ------------------------------------------------------------------ #

    def score_pattern_robustness(
        self,
        sample_results: List[float],
        benchmark: float = 0.0,
    ) -> Dict[str, Any]:
        """
        Valuta se un pattern è statisticamente robusto.

        Controlla:
        - N campioni sufficiente
        - Sharpe-like ratio (rendimento / deviazione)
        - Consistenza (% di periodi positivi)
        - Max drawdown
        """
        n = len(sample_results)

        if n < self.MIN_SAMPLES_VALID:
            return {
                "valid": False,
                "reason": f"Campioni insufficienti: {n} < {self.MIN_SAMPLES_VALID}",
                "n": n,
            }

        mean_ret = statistics.mean(sample_results)
        std_ret = statistics.stdev(sample_results) if n > 1 else 0.0
        sharpe = (mean_ret - benchmark) / std_ret if std_ret > 0 else 0.0
        consistency = sum(1 for r in sample_results if r > 0) / n
        max_dd = self._max_drawdown(sample_results)

        robust = sharpe >= 0.5 and consistency >= 0.55

        return {
            "valid": True,
            "n": n,
            "mean_return": round(mean_ret, 6),
            "std_return": round(std_ret, 6),
            "sharpe_ratio": round(sharpe, 3),
            "consistency": round(consistency, 4),
            "max_drawdown": round(max_dd, 4),
            "robust": robust,
            "verdict": "USE" if robust else "DISCARD",
        }

    def _max_drawdown(self, returns: List[float]) -> float:
        """Calcola il max drawdown dalla serie di rendimenti."""
        equity = [1.0]
        for r in returns:
            equity.append(equity[-1] * (1 + r))
        peak = equity[0]
        max_dd = 0.0
        for v in equity:
            if v > peak:
                peak = v
            dd = (peak - v) / peak if peak > 0 else 0.0
            max_dd = max(max_dd, dd)
        return max_dd

    # ------------------------------------------------------------------ #
    # Position sizing (Kelly corretto)
    # ------------------------------------------------------------------ #

    def kelly_position_size(
        self,
        win_rate: float,
        win_loss_ratio: float,
        fraction: float = 0.25,
    ) -> Dict[str, Any]:
        """
        Kelly Criterion: f = (bp - q) / b
        dove b = win/loss ratio, p = win rate, q = loss rate.

        Usa fraction=0.25 (Quarter Kelly) per ridurre il rischio di rovina.
        """
        q = 1.0 - win_rate
        b = win_loss_ratio

        if b <= 0:
            return {"kelly_full": 0.0, "kelly_fractional": 0.0, "verdict": "NO_TRADE"}

        kelly_full = (b * win_rate - q) / b
        kelly_frac = max(0.0, kelly_full * fraction)

        return {
            "kelly_full": round(kelly_full, 4),
            "kelly_fractional": round(kelly_frac, 4),
            "fraction_used": fraction,
            "verdict": "TRADE" if kelly_frac > 0 else "NO_TRADE",
            "max_pct_bankroll": round(kelly_frac * 100, 2),
        }

    # ------------------------------------------------------------------ #
    # Reazione agli eventi del bus
    # ------------------------------------------------------------------ #

    def _on_task_assigned(self, event: Dict[str, Any]):
        payload = event.get("payload", {})
        if payload.get("assigned_team") != "quant":
            return

        task_id = payload.get("task_id")
        description = payload.get("description", "")
        print(f"[{self.team_id}] 📊 Ricevuto task {task_id}: {description[:60]}...")

        # Pubblica che il task è stato preso in carico
        global_bus.publish("task.completed", {
            "task_id": task_id,
            "agent_id": self.team_id,
            "output": f"Analisi quantitativa avviata per: {description}",
            "assigned_team": "quant",
        })

    # ------------------------------------------------------------------ #
    # Stato
    # ------------------------------------------------------------------ #

    def status(self) -> Dict[str, Any]:
        return {
            "team": self.team_id,
            "analyses_run": self.analyses_run,
            "signals_generated": self.signals_generated,
            "signals_rejected": self.signals_rejected,
            "rejection_rate": (
                round(self.signals_rejected / self.analyses_run, 3)
                if self.analyses_run else 0.0
            ),
        }


# Istanza globale
quant_team = QuantTeam()
