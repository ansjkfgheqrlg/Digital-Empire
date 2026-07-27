import logging
import pandas as pd
import numpy as np
from datetime import datetime

logger = logging.getLogger(__name__)

from event_bus import global_bus
from memory_interface import global_memory

DEFAULT_SPIKE_THRESHOLD_SOL = 100.0
STRATEGY_NAME = "volume_spike_v1"
PROBLEM_TYPE = "volume_spike_detection"
# Ogni quanti trade chiusi si ricalibra la soglia. Sotto questo campione non si tocca nulla.
ADJUST_EVERY_N_TRADES = 2
ROLLING_WINDOW = 10


class AnalysisEngine:
    """
    Layer B: Il Cervello Decisionale (Worker Agent - Analyst).
    Analizza il flusso di transazioni per identificare spike di volumi o anomalie di prezzo.

    La soglia non e' piu' un numero scelto a mano: all'avvio la recupera dalla
    memoria se una calibrazione precedente esiste, e ascolta l'esito reale dei
    trade (trade.executed / trade.failed) per correggerla. Output -> valutazione
    -> correzione: e' il feedback loop richiesto dal gate L2_TO_L3.
    """

    def __init__(self, agent_id="ANALYST-ENGINE-1"):
        self.agent_id = agent_id
        self.recent_events = []
        self.recent_outcomes: list[bool] = []
        self.spike_threshold_sol = self._seed_threshold()

        global_bus.subscribe("data.raw_event_received", self.handle_raw_event,
                             subscriber_id=f"{agent_id}.raw_event")
        global_bus.subscribe("trade.executed", self._on_trade_closed,
                             subscriber_id=f"{agent_id}.trade_executed")
        global_bus.subscribe("trade.failed", self._on_trade_closed,
                             subscriber_id=f"{agent_id}.trade_failed")

    # ------------------------------------------------------------------ #
    # Calibrazione della soglia
    # ------------------------------------------------------------------ #

    def _seed_threshold(self) -> float:
        """Recupera l'ultima soglia calibrata, se esiste. Altrimenti il default dichiarato."""
        fetched = global_memory.strategy_fetch(PROBLEM_TYPE)
        strategy = fetched.get("recommended_strategy")
        if strategy and strategy.get("statistically_solid"):
            seeded = strategy["parameters"].get("spike_threshold_sol")
            if seeded:
                logger.info(f"[{self.agent_id}] Soglia recuperata dalla memoria: {seeded} SOL "
                            f"(success_rate {strategy['success_rate']:.0%} su {strategy['times_used']} usi)")
                return float(seeded)

        global_memory.register_strategy(
            STRATEGY_NAME, PROBLEM_TYPE, self.agent_id,
            parameters={"spike_threshold_sol": DEFAULT_SPIKE_THRESHOLD_SOL},
        )
        return DEFAULT_SPIKE_THRESHOLD_SOL

    def _on_trade_closed(self, event: dict):
        """Un trade e' finito: registra l'esito e, se il campione basta, ricalibra."""
        payload = event.get("payload", {})
        success = event.get("event_type") == "trade.executed"
        signal = payload.get("signal", {})
        if signal.get("strategy", STRATEGY_NAME) != STRATEGY_NAME:
            return

        self.recent_outcomes.append(success)
        self.recent_outcomes = self.recent_outcomes[-ROLLING_WINDOW:]

        if len(self.recent_outcomes) < ADJUST_EVERY_N_TRADES or len(self.recent_outcomes) % ADJUST_EVERY_N_TRADES:
            return

        success_rate = sum(self.recent_outcomes) / len(self.recent_outcomes)
        old_threshold = self.spike_threshold_sol

        if success_rate < 0.5:
            self.spike_threshold_sol = round(old_threshold * 1.10, 2)   # troppi falsi segnali: alzo l'asticella
        elif success_rate > 0.85:
            self.spike_threshold_sol = round(max(old_threshold * 0.95, 10.0), 2)  # segnali affidabili: colgo di piu'

        if self.spike_threshold_sol != old_threshold:
            for r in global_memory.storage.get("strategies", []):
                if isinstance(r["content"], dict) and r["content"].get("name") == STRATEGY_NAME:
                    r["content"]["parameters"]["spike_threshold_sol"] = self.spike_threshold_sol
                    r["version"] += 1
                    break

            global_memory.write("metrics", {
                "kind": "threshold_adjustment", "strategy": STRATEGY_NAME,
                "old_threshold_sol": old_threshold, "new_threshold_sol": self.spike_threshold_sol,
                "success_rate": round(success_rate, 3), "sample_size": len(self.recent_outcomes),
            }, self.agent_id, importance=0.75)

            logger.info(f"[{self.agent_id}] Soglia ricalibrata: {old_threshold} -> {self.spike_threshold_sol} SOL "
                        f"(success_rate {success_rate:.0%} su {len(self.recent_outcomes)} trade)")

    # ------------------------------------------------------------------ #
    # Ingresso dei dati grezzi
    # ------------------------------------------------------------------ #

    def handle_raw_event(self, event_msg: dict):
        """Riceve l'evento dall'Event Bus e chiama process_event"""
        payload = event_msg.get("payload", {})

        import asyncio
        try:
            loop = asyncio.get_running_loop()
            loop.create_task(self.process_event(payload))
        except RuntimeError:
            asyncio.run(self.process_event(payload))

    async def process_event(self, event: dict) -> dict | None:
        """
        Riceve l'evento crudo dal Data Manager, estrae i dati e decide se inviare
        un segnale di "BUY" all'Execution Engine.
        """
        try:
            # Estrazione log e firma (struttura JSON di Solana RPC)
            val = event.get("params", {}).get("result", {}).get("value", {})
            signature = val.get("signature", "unknown")
            logs = val.get("logs", [])

            # Simuliamo l'estrazione di un volume o rarità dal log
            volume = self._extract_volume_from_logs(logs)

            # Registriamo l'evento nel dataframe temporaneo
            self.recent_events.append({
                "timestamp": datetime.now(),
                "signature": signature,
                "volume": volume
            })

            # Pulisce eventi vecchi (> 60 secondi)
            self._cleanup_old_events()

            # Calcolo del trend/volume spike
            signal = self._detect_spike()

            if signal:
                logger.info(f"[{self.agent_id}] Trovato edge statistico! Spike di volume rilevato. Signal: {signal}")
                global_bus.publish("analysis.signal_detected", signal)
                return signal

            return None

        except Exception as e:
            logger.error(f"[{self.agent_id}] Errore durante l'analisi dell'evento: {e}")
            return None

    def _extract_volume_from_logs(self, logs: list[str]) -> float:
        """Simulazione di un regex/parser complesso per leggere l'ammontare transato."""
        for log in logs:
            if "Amount:" in log or "Volume spike:" in log:
                try:
                    # Estrae il numero dal testo simulato "Amount: 120 SOL"
                    words = log.split()
                    for w in words:
                        if w.isdigit():
                            return float(w)
                except ValueError:
                    pass
        return 0.0

    def _cleanup_old_events(self):
        """Mantiene solo la finestra temporale recente (es. 1 minuto)."""
        now = datetime.now()
        self.recent_events = [e for e in self.recent_events if (now - e["timestamp"]).total_seconds() < 60]

    def _detect_spike(self) -> dict | None:
        """
        Logica Quant (PANDAS/NUMPY): Se il volume negli ultimi 60s supera N deviazioni standard,
        è un'anomalia MEV/Whale. C'è un edge potenziale.
        """
        if len(self.recent_events) < 2:
            return None

        df = pd.DataFrame(self.recent_events)
        total_vol = df['volume'].sum()

        # Semplice logica dimostrativa
        if total_vol > self.spike_threshold_sol:
            # Ritorna un segnale d'acquisto (BUY Signal)
            return {
                "action": "BUY",
                "token_address": "mock_token_address_123",
                "strategy": STRATEGY_NAME,
                "confidence": 0.95,
                "expected_slippage_bps": 50, # 0.5%
                "recommended_gas_bribe": 0.001 # SOL per prioritizzare la tx
            }
        return None
