import asyncio
import json
import logging
import websockets
from typing import Callable, Any

logger = logging.getLogger(__name__)

class SolanaDataManager:
    """
    Layer A: Ingestione Dati Real-Time via WebSocket.
    Si connette a un nodo RPC Solana (es. Alchemy/Helius) per ascoltare gli eventi del mempool.
    In modalità simulazione senza chiave API premium, può utilizzare una connessione mock o WSS pubblica.
    """
    
    def __init__(self, wss_url: str):
        self.wss_url = wss_url
        self.callbacks = []
        self._running = False
        
    def register_callback(self, callback: Callable[[dict[str, Any]], None]):
        """Registra un listener per i nuovi eventi mempool."""
        self.callbacks.append(callback)
        
    async def listen_logs(self):
        """Ascolta i log in tempo reale per specifici indirizzi di smart contract (es. Raydium/Pump.fun)."""
        subscribe_msg = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "logsSubscribe",
            "params": [
                {"mentions": ["6EF8rrecthR5Dkzon8Nwu78hRvfTj1zP5R3Q1Ld7MvVj"]}, # Pump.fun Program ID
                {"commitment": "processed"}
            ]
        }

        self._running = True
        logger.info(f"Connessione al nodo WebSocket: {self.wss_url}")
        
        while self._running:
            try:
                # Se wss_url è vuoto o fittizio, simula i dati per il paper trading test
                if not self.wss_url or "your_wss_url" in self.wss_url:
                    await self._mock_stream()
                    break

                async with websockets.connect(self.wss_url) as ws:
                    await ws.send(json.dumps(subscribe_msg))
                    response = await ws.recv()
                    logger.info(f"Iscrizione confermata: {response}")
                    
                    async for msg in ws:
                        if not self._running:
                            break
                        data = json.loads(msg)
                        for cb in self.callbacks:
                            # Avvia le callback di analisi in modo concorrente
                            asyncio.create_task(self._safe_call(cb, data))
                            
            except Exception as e:
                logger.error(f"Errore connessione WebSocket: {e}. Riconnessione in 3 secondi...")
                await asyncio.sleep(3)

    async def _safe_call(self, cb, data):
        try:
            if asyncio.iscoroutinefunction(cb):
                await cb(data)
            else:
                cb(data)
        except Exception as e:
            logger.error(f"Errore nella callback {cb.__name__}: {e}")

    async def _mock_stream(self):
        """Generatore di eventi fittizi basato su dati storici per il testing offline e la simulazione S7."""
        logger.warning("Esecuzione in MOCK STREAM (Nessun WSS URL fornito). Generazione dati simulati...")
        mock_data_series = [
            {"params": {"result": {"value": {"signature": "sig1", "logs": ["Program log: Instruction: InitializeMint", "Volume spike: 50 SOL"]}}}},
            {"params": {"result": {"value": {"signature": "sig2", "logs": ["Program log: Instruction: Buy", "Amount: 120 SOL"]}}}},
            {"params": {"result": {"value": {"signature": "sig3", "logs": ["Program log: Instruction: Sell", "Amount: 10 SOL"]}}}},
        ]
        
        for mock_event in mock_data_series:
            if not self._running:
                break
            await asyncio.sleep(1.5) # Simula ritardo di rete
            for cb in self.callbacks:
                await self._safe_call(cb, mock_event)
        
        self._running = False
        
    def stop(self):
        """Disarma il data manager (Kill Switch)."""
        self._running = False
        logger.info("Data Manager fermato.")
