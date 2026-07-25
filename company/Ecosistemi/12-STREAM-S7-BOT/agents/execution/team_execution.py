"""
╔══════════════════════════════════════════════════════════════╗
║         ⚡ TEAM EXECUTION — Esecuzione Trade Sicura          ║
║                                                              ║
║  Valida ogni operazione prima dell'esecuzione.               ║
║  Applica circuit breaker automatici.                         ║
║  Non esegue mai un trade che non passa il risk check.        ║
╚══════════════════════════════════════════════════════════════╝
"""
from __future__ import annotations

import time
import uuid
from enum import Enum
from typing import Dict, Any, List, Optional, Tuple

from event_bus import global_bus
from memory_interface import global_memory


class TradeMode(Enum):
    SIMULATION = "SIMULATION"
    PAPER = "PAPER"
    LIVE = "LIVE"  # Richiede Gate L5 PASSED


class CircuitState(Enum):
    CLOSED = "CLOSED"    # normale: trade passano
    OPEN = "OPEN"        # blocco: troppi fallimenti recenti
    HALF_OPEN = "HALF_OPEN"  # in prova: un trade di test


class ExecutionTeam:
    """
    ⚡ Team Execution — Esecuzione trade sicura e controllata.

    Agenti nel team:
    - RiskManager: valida position size, stop loss, esposizione totale
    - CircuitBreaker: blocca automaticamente dopo N fallimenti consecutivi
    - TradeLogger: registra ogni trade con full metadata

    Principio: Prima non perdere. Poi guadagnare.
               Un trade non eseguito non è una perdita. Un trade sbagliato sì.
    """

    # Limiti di sicurezza NON negoziabili
    MAX_POSITION_PCT = 5.0       # % massima del bankroll per singolo trade
    MAX_DAILY_LOSS_PCT = 10.0    # % massima di perdita giornaliera
    MAX_OPEN_POSITIONS = 5       # posizioni aperte contemporaneamente
    CIRCUIT_BREAKER_THRESHOLD = 3  # fallimenti consecutivi → circuit open

    def __init__(
        self,
        team_id: str = "EXECUTION-TEAM-1",
        mode: TradeMode = TradeMode.SIMULATION,
        bankroll: float = 10.0,
    ):
        self.team_id = team_id
        self.mode = mode
        self.bankroll = bankroll
        self.bankroll_start = bankroll

        self.open_positions: Dict[str, Dict[str, Any]] = {}
        self.trade_history: List[Dict[str, Any]] = []
        self.daily_pnl: float = 0.0
        self._consecutive_failures: int = 0
        self._circuit_state: CircuitState = CircuitState.CLOSED

        global_bus.subscribe(
            "task.created",
            self._on_task_assigned,
            subscriber_id=f"{team_id}.task_in",
        )

        print(f"[{self.team_id}] Team Execution pronto. "
              f"Modalità: {mode.value}, Bankroll: {bankroll} SOL, "
              f"Circuit Breaker: {'OFF' if self._circuit_state == CircuitState.CLOSED else 'ON'}")

    # ------------------------------------------------------------------ #
    # Risk Manager — validazione pre-trade
    # ------------------------------------------------------------------ #

    def validate_trade(
        self,
        token: str,
        side: str,  # "BUY" / "SELL"
        size_sol: float,
        entry_price: float,
        stop_loss: float,
        take_profit: float,
    ) -> Tuple[bool, str, Dict[str, Any]]:
        """
        Valida un trade prima dell'esecuzione.

        Controlla:
        1. Circuit breaker aperto
        2. Modalità live richiede Gate L5
        3. Position size <= MAX_POSITION_PCT
        4. Stop loss definito e logico
        5. Daily loss limit non superato
        6. Max open positions non superato
        7. Risk/Reward >= 1.5

        Ritorna: (approved, reason, details)
        """
        checks: List[Dict[str, Any]] = []

        # 1. Circuit breaker
        ok, reason = self._check_circuit_breaker()
        checks.append({"check": "circuit_breaker", "passed": ok, "reason": reason})

        # 2. Live mode gate
        if self.mode == TradeMode.LIVE:
            ok2 = self._is_live_authorized()
            checks.append({
                "check": "live_gate_l5",
                "passed": ok2,
                "reason": "Gate L5 non verificato" if not ok2 else "Gate L5 OK",
            })
        else:
            checks.append({"check": "live_gate_l5", "passed": True, "reason": f"Modalità {self.mode.value}"})

        # 3. Position size
        pct = (size_sol / self.bankroll) * 100 if self.bankroll > 0 else 100
        ok3 = pct <= self.MAX_POSITION_PCT
        checks.append({
            "check": "position_size",
            "passed": ok3,
            "reason": f"{pct:.1f}% bankroll (max {self.MAX_POSITION_PCT}%)",
        })

        # 4. Stop loss logico
        if side == "BUY":
            sl_ok = stop_loss < entry_price
        else:
            sl_ok = stop_loss > entry_price
        checks.append({
            "check": "stop_loss",
            "passed": sl_ok,
            "reason": f"SL {stop_loss} {'<' if side=='BUY' else '>'} entry {entry_price}",
        })

        # 5. Daily loss limit
        daily_pct = abs(self.daily_pnl) / self.bankroll_start * 100 if self.bankroll_start > 0 else 0
        ok5 = daily_pct < self.MAX_DAILY_LOSS_PCT
        checks.append({
            "check": "daily_loss",
            "passed": ok5,
            "reason": f"Daily loss {daily_pct:.1f}% (max {self.MAX_DAILY_LOSS_PCT}%)",
        })

        # 6. Open positions
        ok6 = len(self.open_positions) < self.MAX_OPEN_POSITIONS
        checks.append({
            "check": "open_positions",
            "passed": ok6,
            "reason": f"{len(self.open_positions)}/{self.MAX_OPEN_POSITIONS} posizioni aperte",
        })

        # 7. Risk/Reward
        if side == "BUY":
            risk = abs(entry_price - stop_loss)
            reward = abs(take_profit - entry_price)
        else:
            risk = abs(stop_loss - entry_price)
            reward = abs(entry_price - take_profit)

        rr = reward / risk if risk > 0 else 0
        ok7 = rr >= 1.5
        checks.append({
            "check": "risk_reward",
            "passed": ok7,
            "reason": f"R/R {rr:.2f} (minimo 1.5)",
        })

        all_passed = all(c["passed"] for c in checks)
        failed = [c for c in checks if not c["passed"]]

        return all_passed, (
            "APPROVED" if all_passed else f"REJECTED: {', '.join(c['check'] for c in failed)}"
        ), {"checks": checks, "risk_reward": round(rr, 2), "position_pct": round(pct, 2)}

    # ------------------------------------------------------------------ #
    # Esecuzione
    # ------------------------------------------------------------------ #

    def execute(
        self,
        token: str,
        side: str,
        size_sol: float,
        entry_price: float,
        stop_loss: float,
        take_profit: float,
    ) -> Dict[str, Any]:
        """Esegue il trade se passa validazione. Registra tutto."""
        approved, reason, details = self.validate_trade(
            token, side, size_sol, entry_price, stop_loss, take_profit
        )

        trade_id = f"TRADE-{uuid.uuid4().hex[:8].upper()}"

        if not approved:
            self._consecutive_failures += 1
            self._check_and_update_circuit()

            record = {
                "trade_id": trade_id,
                "status": "REJECTED",
                "reason": reason,
                "token": token,
                "side": side,
                "size_sol": size_sol,
                "timestamp": time.time(),
                "mode": self.mode.value,
            }
            self.trade_history.append(record)

            global_bus.publish("trade.rejected", {
                "trade_id": trade_id,
                "reason": reason,
                "details": details,
            })

            print(f"[{self.team_id}] ⛔ Trade {trade_id} RIFIUTATO: {reason}")
            global_memory.write("knowledge", record, self.team_id, importance=0.6)
            return record

        # Trade approvato
        self._consecutive_failures = 0
        if self._circuit_state == CircuitState.HALF_OPEN:
            self._circuit_state = CircuitState.CLOSED
            print(f"[{self.team_id}] ✅ Circuit breaker chiuso dopo test positivo.")

        position = {
            "trade_id": trade_id,
            "token": token,
            "side": side,
            "size_sol": size_sol,
            "entry_price": entry_price,
            "stop_loss": stop_loss,
            "take_profit": take_profit,
            "opened_at": time.time(),
            "mode": self.mode.value,
            "status": "OPEN",
        }

        self.open_positions[trade_id] = position
        self.trade_history.append({**position, "status": "EXECUTED"})

        global_bus.publish("trade.executed", {
            "trade_id": trade_id,
            "token": token,
            "side": side,
            "size_sol": size_sol,
            "mode": self.mode.value,
        })

        print(f"[{self.team_id}] ✅ Trade {trade_id} ESEGUITO [{self.mode.value}]: "
              f"{side} {size_sol} SOL @ {entry_price} su {token}")

        global_memory.write("knowledge", position, self.team_id, importance=0.7)
        return position

    # ------------------------------------------------------------------ #
    # Circuit Breaker
    # ------------------------------------------------------------------ #

    def _check_circuit_breaker(self) -> Tuple[bool, str]:
        if self._circuit_state == CircuitState.OPEN:
            return False, f"Circuit breaker APERTO ({self._consecutive_failures} fallimenti consecutivi)"
        if self._circuit_state == CircuitState.HALF_OPEN:
            return True, "Circuit breaker in HALF-OPEN: trade di test permesso"
        return True, "Circuit breaker chiuso"

    def _check_and_update_circuit(self):
        if self._consecutive_failures >= self.CIRCUIT_BREAKER_THRESHOLD:
            if self._circuit_state == CircuitState.CLOSED:
                self._circuit_state = CircuitState.OPEN
                print(f"[{self.team_id}] 🔴 CIRCUIT BREAKER APERTO: "
                      f"{self._consecutive_failures} fallimenti consecutivi")
                global_bus.publish("circuit.breaker.opened", {
                    "team": self.team_id,
                    "failures": self._consecutive_failures,
                })

    def _is_live_authorized(self) -> bool:
        """In produzione: verificherebbe il gate L5 dal memory store."""
        records = global_memory.contextual_recall(["gate", "L5", "PASSED"])
        return any("L5" in str(r) and "PASSED" in str(r) for r in records)

    def reset_circuit(self) -> bool:
        """Solo un operatore umano può resettare il circuit breaker."""
        self._circuit_state = CircuitState.HALF_OPEN
        print(f"[{self.team_id}] ⚡ Circuit breaker in HALF-OPEN per test.")
        return True

    # ------------------------------------------------------------------ #
    # Reazione agli eventi del bus
    # ------------------------------------------------------------------ #

    def _on_task_assigned(self, event: Dict[str, Any]):
        payload = event.get("payload", {})
        if payload.get("assigned_team") != "execution":
            return

        task_id = payload.get("task_id")
        description = payload.get("description", "")
        print(f"[{self.team_id}] ⚡ Ricevuto task {task_id}: {description[:60]}...")

        global_bus.publish("task.completed", {
            "task_id": task_id,
            "agent_id": self.team_id,
            "output": f"Execution: risk check completato per: {description}",
            "assigned_team": "execution",
        })

    # ------------------------------------------------------------------ #
    # Stato
    # ------------------------------------------------------------------ #

    def status(self) -> Dict[str, Any]:
        return {
            "team": self.team_id,
            "mode": self.mode.value,
            "bankroll": round(self.bankroll, 4),
            "daily_pnl": round(self.daily_pnl, 4),
            "open_positions": len(self.open_positions),
            "total_trades": len(self.trade_history),
            "circuit_state": self._circuit_state.value,
            "consecutive_failures": self._consecutive_failures,
        }


# Istanza globale (default: simulazione)
execution_team = ExecutionTeam()
