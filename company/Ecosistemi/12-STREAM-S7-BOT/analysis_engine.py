import json
import logging
import os
import urllib.error
import urllib.request
import pandas as pd
import numpy as np
from datetime import datetime
from typing import Callable, Optional

logger = logging.getLogger(__name__)

from event_bus import global_bus
from memory_interface import global_memory

DEFAULT_SPIKE_THRESHOLD_SOL = 100.0
STRATEGY_NAME = "volume_spike_v1"
PROBLEM_TYPE = "volume_spike_detection"
# Ogni quanti trade chiusi si ricalibra la soglia. Sotto questo campione non si tocca nulla.
ADJUST_EVERY_N_TRADES = 2
ROLLING_WINDOW = 10

# Wrapped SOL: e' sempre il lato "prezzo" dello swap, mai il token comprato/venduto.
WSOL_MINT = "So11111111111111111111111111111111111111112"
DEFAULT_RPC_URL = "https://api.mainnet-beta.solana.com"
RPC_TIMEOUT_S = 8
LAMPORTS_PER_SOL = 1_000_000_000


class AnalysisEngine:
    """
    Layer B: Il Cervello Decisionale (Worker Agent - Analyst).
    Analizza il flusso di transazioni per identificare spike di volumi o anomalie di prezzo.

    La soglia non e' piu' un numero scelto a mano: all'avvio la recupera dalla
    memoria se una calibrazione precedente esiste, e ascolta l'esito reale dei
    trade (trade.executed / trade.failed) per correggerla. Output -> valutazione
    -> correzione: e' il feedback loop richiesto dal gate L2_TO_L3.

    Il parser legge transazioni Solana vere: una notifica logsSubscribe porta
    solo firma + log testuali, mai gli account coinvolti. Per il volume reale
    in SOL e per il token address veri serve la transazione intera
    (getTransaction), letta dalle variazioni di saldo (preBalances/postBalances,
    preTokenBalances/postTokenBalances) — non da un regex sul testo dei log,
    che su Solana vero e' binario/base64, non "Amount: 120 SOL" leggibile.
    """

    def __init__(self, agent_id="ANALYST-ENGINE-1", rpc_url: Optional[str] = None,
                 tx_fetcher: Optional[Callable[[str], Optional[dict]]] = None):
        self.agent_id = agent_id
        self.recent_events = []
        self.recent_outcomes: list[bool] = []
        self.spike_threshold_sol = self._seed_threshold()
        self.rpc_url = rpc_url or os.getenv("SOLANA_RPC_URL", DEFAULT_RPC_URL)
        # Iniettabile: in produzione chiama davvero l'RPC Solana; nei test si
        # passa un fetcher deterministico per non dipendere dalla rete reale.
        self._tx_fetcher = tx_fetcher or self._fetch_transaction_sync

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
        Riceve l'evento crudo dal Data Manager, estrae i dati veri della
        transazione e decide se inviare un segnale di "BUY" all'Execution Engine.
        """
        try:
            val = event.get("params", {}).get("result", {}).get("value", {})
            signature = val.get("signature", "unknown")

            trade = await self._resolve_trade_data(signature)
            if trade is None:
                return None  # niente volume reale da leggere: non e' una trade valida

            self.recent_events.append({
                "timestamp": datetime.now(),
                "signature": signature,
                "volume": trade["volume_sol"],
                "token_address": trade["token_address"],
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

    # ------------------------------------------------------------------ #
    # Parser dati reale — getTransaction, non regex sul testo dei log
    # ------------------------------------------------------------------ #

    async def _resolve_trade_data(self, signature: str) -> Optional[dict]:
        """
        Wrapper asincrono: la chiamata RPC e' bloccante (urllib), quindi gira
        in un executor per non fermare il loop mentre aspetta la rete.
        """
        import asyncio
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._extract_trade_data, signature)

    def _extract_trade_data(self, signature: str) -> Optional[dict]:
        """
        Legge la transazione vera (getTransaction) e ne ricava volume e token
        dalle variazioni di saldo reali, non da testo nei log:
          - volume in SOL: la maggior variazione di lamports tra gli account
            coinvolti (preBalances -> postBalances). E' il lato "prezzo" dello
            swap, affidabile a prescindere dal programma (Raydium/Pump.fun/altro).
          - token address: il mint (diverso da Wrapped SOL) con la maggior
            variazione di saldo token (preTokenBalances -> postTokenBalances).
            E' negli account della transazione, mai nei log.
        Verificato su transazioni Raydium/Pump.fun reali di mainnet (vedi
        checkpoint): su transazioni non-trade (fee-only, bundle che rientra a
        saldo netto zero) ritorna None correttamente, non un dato inventato.
        """
        tx = self._tx_fetcher(signature)
        if not tx:
            return None

        meta = tx.get("meta") or {}
        if meta.get("err") is not None:
            return None  # transazione fallita on-chain: nessun volume reale da leggere

        pre_bal = meta.get("preBalances") or []
        post_bal = meta.get("postBalances") or []
        lamport_deltas = [abs(a - b) for a, b in zip(pre_bal, post_bal)]
        volume_sol = (max(lamport_deltas) / LAMPORTS_PER_SOL) if lamport_deltas else 0.0

        pre_tok = {b["accountIndex"]: b for b in meta.get("preTokenBalances") or []}
        post_tok = {b["accountIndex"]: b for b in meta.get("postTokenBalances") or []}

        token_address, biggest_delta = None, 0.0
        for idx in set(pre_tok) | set(post_tok):
            p, o = pre_tok.get(idx, {}), post_tok.get(idx, {})
            mint = (o or p).get("mint")
            if not mint or mint == WSOL_MINT:
                continue
            pre_amt = (p.get("uiTokenAmount") or {}).get("uiAmount") or 0.0
            post_amt = (o.get("uiTokenAmount") or {}).get("uiAmount") or 0.0
            delta = abs(post_amt - pre_amt)
            if delta > biggest_delta:
                biggest_delta, token_address = delta, mint

        if token_address is None or volume_sol <= 0:
            return None

        return {"volume_sol": round(volume_sol, 6), "token_address": token_address}

    def _fetch_transaction_sync(self, signature: str) -> Optional[dict]:
        """
        Unico punto che tocca davvero la rete: getTransaction sul nodo RPC
        configurato (SOLANA_RPC_URL, default endpoint pubblico mainnet).
        Bloccante di proposito: e' iniettabile via tx_fetcher per i test.
        """
        payload = json.dumps({
            "jsonrpc": "2.0", "id": 1, "method": "getTransaction",
            "params": [signature, {"encoding": "jsonParsed", "maxSupportedTransactionVersion": 0}],
        }).encode()
        req = urllib.request.Request(self.rpc_url, data=payload, headers={"Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=RPC_TIMEOUT_S) as resp:
                body = json.loads(resp.read())
        except (urllib.error.URLError, OSError, ValueError) as e:
            logger.warning(f"[{self.agent_id}] getTransaction fallita per {signature}: {e}")
            return None
        return body.get("result")

    def _cleanup_old_events(self):
        """Mantiene solo la finestra temporale recente (es. 1 minuto)."""
        now = datetime.now()
        self.recent_events = [e for e in self.recent_events if (now - e["timestamp"]).total_seconds() < 60]

    def _detect_spike(self) -> dict | None:
        """
        Logica Quant (PANDAS/NUMPY): Se il volume negli ultimi 60s supera N deviazioni standard,
        è un'anomalia MEV/Whale. C'è un edge potenziale.

        Fix G-C: prima, una volta superata la soglia, la finestra restava piena
        finche' i 60s non scadevano da soli -> ogni evento successivo dentro la
        stessa finestra ripubblicava lo stesso segnale (spam). Ora, appena un
        segnale parte, la finestra si svuota: il prossimo spike deve accumularsi
        da capo su eventi davvero nuovi.
        """
        if len(self.recent_events) < 2:
            return None

        df = pd.DataFrame(self.recent_events)
        total_vol = df['volume'].sum()

        if total_vol > self.spike_threshold_sol:
            token_address = self.recent_events[-1]["token_address"]
            signal = {
                "action": "BUY",
                "token_address": token_address,
                "strategy": STRATEGY_NAME,
                "confidence": 0.95,
                "expected_slippage_bps": 50, # 0.5%
                "recommended_gas_bribe": 0.001 # SOL per prioritizzare la tx
            }
            self.recent_events = []  # finestra "gia' segnalata": si riparte da zero
            return signal
        return None
