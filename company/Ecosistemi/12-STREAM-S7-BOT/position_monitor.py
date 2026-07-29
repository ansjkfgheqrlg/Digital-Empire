import logging
import os
import random
import time
from typing import Any, Dict, Optional

from event_bus import global_bus
from memory_interface import global_memory

logger = logging.getLogger(__name__)

DEFAULT_TAKE_PROFIT_PCT = float(os.getenv("TAKE_PROFIT_PCT", 50.0))
DEFAULT_STOP_LOSS_PCT = float(os.getenv("STOP_LOSS_PCT", 20.0))
# Deviazione standard del passo casuale per tick — e' una STIMA (vedi docstring).
PRICE_STEP_STD = 0.03


class PositionMonitor:
    """
    Layer E: uscita dalle posizioni (Worker Agent - Position Monitor).
    Il bot comprava e basta: questo layer chiude quello che RiskManager apre.

    STIMA DICHIARATA: non c'e' un feed prezzo live collegato in questa fase.
    Il valore della posizione e' una simulazione a random-walk applicata a ogni
    "tick" di mercato (un nuovo dato grezzo ricevuto), non il prezzo reale del
    token. Il PnL calcolato su take-profit/stop-loss e' quindi stimato, non
    misurato — va dichiarato cosi' in ogni report, non spacciato per prezzo vero.

    Si iscrive al bus come tutti gli altri layer, nessuna chiamata diretta a
    RiskManager: apre la propria posizione leggendo trade.executed (lo stesso
    evento che ascolta anche RiskManager, indipendentemente) e pubblica
    position.closed quando take-profit o stop-loss scattano — RiskManager lo
    ascolta per liberare lo slot in open_positions.
    """

    def __init__(self, agent_id: str = "POSITION-MONITOR-1",
                 take_profit_pct: float = DEFAULT_TAKE_PROFIT_PCT,
                 stop_loss_pct: float = DEFAULT_STOP_LOSS_PCT,
                 rng: Optional[random.Random] = None):
        self.agent_id = agent_id
        self.take_profit_pct = take_profit_pct
        self.stop_loss_pct = stop_loss_pct
        self.positions: Dict[str, Dict[str, Any]] = {}
        self._rng = rng or random.Random()

        global_bus.subscribe("trade.executed", self._on_trade_executed,
                             subscriber_id=f"{agent_id}.opened")
        global_bus.subscribe("data.raw_event_received", self._on_tick,
                             subscriber_id=f"{agent_id}.tick")

    # ------------------------------------------------------------------ #
    # Apertura — stesso evento di RiskManager, tracciamento indipendente
    # ------------------------------------------------------------------ #

    def _on_trade_executed(self, event_msg: dict):
        payload = event_msg.get("payload", {})
        signal = payload.get("signal", {})
        token = signal.get("token_address")
        if not token or token in self.positions:
            return
        cost = payload.get("cost", 0.0)
        self.positions[token] = {
            "token": token,
            "entry_cost_sol": cost,
            "estimated_value_sol": cost,
            "opened_at": time.time(),
        }
        logger.info(f"[{self.agent_id}] Posizione aperta {token}: {cost} SOL (costo base, valore stimato = costo)")

    # ------------------------------------------------------------------ #
    # Ogni tick di mercato rivaluta le posizioni aperte e applica TP/SL
    # ------------------------------------------------------------------ #

    def _on_tick(self, event_msg: dict):
        if not self.positions:
            return
        for token in list(self.positions):
            self._revalue_and_check(token)

    def _revalue_and_check(self, token: str):
        pos = self.positions.get(token)
        if pos is None:
            return

        step = self._rng.gauss(0, PRICE_STEP_STD)
        pos["estimated_value_sol"] = max(0.0, pos["estimated_value_sol"] * (1 + step))
        entry = pos["entry_cost_sol"]
        pnl_pct = ((pos["estimated_value_sol"] - entry) / entry * 100.0) if entry else 0.0

        if pnl_pct >= self.take_profit_pct:
            self._close_position(token, pos, reason="take_profit", pnl_pct=pnl_pct)
        elif pnl_pct <= -self.stop_loss_pct:
            self._close_position(token, pos, reason="stop_loss", pnl_pct=pnl_pct)

    def _close_position(self, token: str, pos: dict, reason: str, pnl_pct: float):
        pnl_sol = pos["estimated_value_sol"] - pos["entry_cost_sol"]
        del self.positions[token]

        global_memory.write("metrics", {
            "kind": "position_closed",
            "token": token,
            "reason": reason,
            "entry_cost_sol": round(pos["entry_cost_sol"], 6),
            "exit_value_sol": round(pos["estimated_value_sol"], 6),
            "pnl_sol": round(pnl_sol, 6),
            "pnl_pct": round(pnl_pct, 2),
            "estimated": True,  # nessun feed prezzo live: valore stimato, non misurato
        }, self.agent_id, importance=0.7)

        logger.info(f"[{self.agent_id}] Posizione chiusa {token} ({reason}): "
                    f"PnL stimato {pnl_sol:.4f} SOL ({pnl_pct:.1f}%)")

        global_bus.publish("position.closed", {
            "token_address": token,
            "reason": reason,
            "pnl_sol": round(pnl_sol, 6),
            "pnl_pct": round(pnl_pct, 2),
        })
