import csv
import logging
import os
import time
from typing import Optional, Dict, Any

from event_bus import global_bus
from memory_interface import global_memory

logger = logging.getLogger(__name__)

# Oltre questo drawdown sul bankroll, il kill-switch scatta da solo.
DEFAULT_MAX_DRAWDOWN_PCT = 20.0


class RiskManager:
    """
    Layer D: Risk & Treasury (Worker Agent - Risk).
    Gestisce l'esposizione del portafoglio e i kill-switch di emergenza.

    E' l'unico punto di passaggio tra un segnale trovato dall'Analyst e
    l'esecuzione: sta sul bus, non viene chiamato a mano. Prima non c'era
    modo di bypassarlo che non fosse gia' un bug (la catena manuale in
    main.py chiamava execute_trade anche quando il Risk Manager non era
    stato interpellato). Ora c'e' un solo percorso: analysis.signal_detected
    -> RiskManager -> risk.trade_approved -> ExecutionEngine.
    """

    def __init__(self, base_bankroll: float, max_position_pct: float,
                 max_drawdown_pct: float = DEFAULT_MAX_DRAWDOWN_PCT,
                 log_file: str = "paper_trade_log.csv", agent_id: str = "RISK-MANAGER-1"):
        self.agent_id = agent_id
        self.bankroll = base_bankroll
        self.max_position_pct = max_position_pct
        self.max_drawdown_pct = max_drawdown_pct
        self.log_file = log_file
        self.is_kill_switch_active = False
        self.open_positions: Dict[str, Any] = {}

        global_bus.subscribe("analysis.signal_detected", self.handle_signal,
                             subscriber_id=f"{agent_id}.signal")
        global_bus.subscribe("trade.executed", self._on_trade_executed,
                             subscriber_id=f"{agent_id}.position_opened")
        global_bus.subscribe("position.closed", self._on_position_closed,
                             subscriber_id=f"{agent_id}.position_closed")

    # ------------------------------------------------------------------ #
    # Tracciamento posizioni — G-B: open_positions era dichiarato ma mai
    # scritto, quindi il limite "max 3 aperte" non scattava mai. Ora si
    # popola sul trade eseguito e si libera sulla chiusura (position.closed,
    # pubblicato dal Position Monitor), sempre via bus, mai per chiamata diretta.
    # ------------------------------------------------------------------ #

    def _on_trade_executed(self, event_msg: dict):
        payload = event_msg.get("payload", {})
        signal = payload.get("signal", {})
        token = signal.get("token_address")
        if not token:
            return
        self.open_positions[token] = {
            "token": token,
            "entry_cost_sol": payload.get("cost", 0.0),
            "opened_at": time.time(),
        }
        logger.info(f"[RISK] Posizione tracciata: {token} "
                    f"(entry {payload.get('cost', 0.0)} SOL) — aperte: {len(self.open_positions)}")

    def _on_position_closed(self, event_msg: dict):
        payload = event_msg.get("payload", {})
        token = payload.get("token_address")
        if token in self.open_positions:
            del self.open_positions[token]
            logger.info(f"[RISK] Posizione chiusa: {token} — aperte: {len(self.open_positions)}")

    # ------------------------------------------------------------------ #
    # Ingresso dal bus
    # ------------------------------------------------------------------ #

    def handle_signal(self, event_msg: dict):
        signal = event_msg.get("payload", {})
        self.check_portfolio_health()  # ogni nuovo segnale ricontrolla lo stato reale prima di decidere
        allocated = self.assess_trade(signal)
        if allocated:
            global_bus.publish("risk.trade_approved", {"signal": signal, "allocated_capital": allocated})
        else:
            global_bus.publish("risk.trade_rejected", {
                "signal": signal,
                "reason": "kill_switch" if self.is_kill_switch_active else "risk_limits",
            })

    # ------------------------------------------------------------------ #
    # Valutazione
    # ------------------------------------------------------------------ #

    def assess_trade(self, signal: dict) -> Optional[float]:
        """
        Valuta se autorizzare il trade.
        Ritorna l'ammontare in SOL da allocare, oppure None se il trade e' bloccato.
        """
        if self.is_kill_switch_active:
            logger.warning("[RISK] Kill-Switch attivo. Trade bloccato.")
            return None

        max_alloc = self.bankroll * (self.max_position_pct / 100.0)

        if len(self.open_positions) >= 3:
            logger.warning("[RISK] Troppe posizioni aperte. Trade bloccato.")
            return None

        logger.info(f"[RISK] Trade approvato. Capitale allocato: {max_alloc} SOL")
        return max_alloc

    # ------------------------------------------------------------------ #
    # Kill switch
    # ------------------------------------------------------------------ #

    def activate_kill_switch(self, reason: str = "manuale"):
        """Disarma l'intero sistema in caso di crollo del mercato o bug."""
        self.is_kill_switch_active = True
        logger.critical(f"[KILL SWITCH] ATTIVATO ({reason}). Nessuna nuova transazione sara' autorizzata.")
        global_memory.record_decision(
            decision=f"Kill-switch attivato: {reason}", author=self.agent_id, outcome="APPLIED",
        )

    def deactivate_kill_switch(self):
        self.is_kill_switch_active = False
        logger.info("[KILL SWITCH] Disattivato. Ripresa operazioni.")

    def check_portfolio_health(self) -> bool:
        """
        Controlla se il bankroll e' sceso sotto la soglia critica leggendo i
        trade realmente eseguiti dal paper trade log. Non e' piu' uno stub:
        se il drawdown supera max_drawdown_pct, il kill-switch scatta da solo.
        Ritorna True se il portafoglio e' in salute.
        """
        if not os.path.exists(self.log_file):
            return True

        realized_cost = 0.0
        trades = 0
        with open(self.log_file, "r", newline="") as f:
            for row in csv.DictReader(f):
                trades += 1
                try:
                    realized_cost += float(row.get("total_cost_sol", 0) or 0)
                except ValueError:
                    continue

        if trades == 0:
            return True

        current_bankroll = self.bankroll - realized_cost
        drawdown_pct = ((self.bankroll - current_bankroll) / self.bankroll) * 100.0 if self.bankroll else 0.0

        global_memory.write("metrics", {
            "kind": "portfolio_health", "trades": trades,
            "current_bankroll": round(current_bankroll, 6), "drawdown_pct": round(drawdown_pct, 2),
        }, self.agent_id, importance=0.6)

        if drawdown_pct >= self.max_drawdown_pct and not self.is_kill_switch_active:
            self.activate_kill_switch(reason=f"drawdown {drawdown_pct:.1f}% >= soglia {self.max_drawdown_pct}%")
            return False

        return not self.is_kill_switch_active
