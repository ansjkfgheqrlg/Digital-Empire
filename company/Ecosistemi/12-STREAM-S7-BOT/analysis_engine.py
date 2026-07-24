import logging
import pandas as pd
import numpy as np
from datetime import datetime

logger = logging.getLogger(__name__)

from event_bus import global_bus

class AnalysisEngine:
    """
    Layer B: Il Cervello Decisionale (Worker Agent - Analyst).
    Analizza il flusso di transazioni per identificare spike di volumi o anomalie di prezzo.
    """
    
    def __init__(self, agent_id="ANALYST-ENGINE-1"):
        self.agent_id = agent_id
        # Memoria temporanea per calcolare volumi mobili (rolling window)
        self.recent_events = []
        self.spike_threshold_sol = 100.0 # Valore fittizio di soglia
        
        # Sostituisce la chiamata diretta iscrivendosi all'Event Bus
        global_bus.subscribe("data.raw_event_received", self.handle_raw_event)

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
                logger.info(f"[{self.agent_id}] 🎯 Trovato edge statistico! Spike di volume rilevato. Signal: {signal}")
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
                "confidence": 0.95,
                "expected_slippage_bps": 50, # 0.5%
                "recommended_gas_bribe": 0.001 # SOL per prioritizzare la tx
            }
        return None
