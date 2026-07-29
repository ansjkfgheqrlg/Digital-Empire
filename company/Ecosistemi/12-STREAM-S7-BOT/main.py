import asyncio
import logging
import os
from dotenv import load_dotenv

from data_manager import SolanaDataManager
from analysis_engine import AnalysisEngine
from execution_engine import ExecutionEngine
from risk_manager import RiskManager
from position_monitor import PositionMonitor
from event_bus import global_bus

# Configurazione Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("S7-Bot-Main")

async def main():
    logger.info("Avvio Stream S7 - Macchina Automatica Trading (MODALITÀ SIMULATA)")
    
    # Caricamento configurazioni da .env fittizio/reale
    load_dotenv()
    
    wss_url = os.getenv("SOLANA_WSS_URL", "")
    trade_mode = os.getenv("TRADE_MODE", "SIMULATION")
    base_bankroll = float(os.getenv("BASE_BANKROLL_SOL", 10.0))
    max_position = float(os.getenv("MAX_POSITION_PCT", 5.0))
    
    # Inizializzazione dei 5 Layer. Da qui in poi si parlano solo via Event Bus:
    # data.raw_event_received -> AnalysisEngine -> analysis.signal_detected
    # -> RiskManager -> risk.trade_approved -> ExecutionEngine -> trade.executed
    # -> RiskManager (apre open_positions) + PositionMonitor (apre e sorveglia
    # TP/SL, pubblica position.closed) -> RiskManager libera lo slot.
    # Un solo percorso, nessuna chiamata diretta che possa bypassare il rischio.
    data_manager = SolanaDataManager(wss_url=wss_url)
    analysis_engine = AnalysisEngine()
    risk_manager = RiskManager(base_bankroll=base_bankroll, max_position_pct=max_position)
    execution_engine = ExecutionEngine(mode=trade_mode)
    position_monitor = PositionMonitor()

    async def on_new_event(event_data):
        global_bus.publish("data.raw_event_received", event_data)

    data_manager.register_callback(on_new_event)
    
    # Avvio ascolto infinito
    try:
        await data_manager.listen_logs()
    except KeyboardInterrupt:
        logger.info("Spegnimento manuale del bot...")
        data_manager.stop()

if __name__ == "__main__":
    asyncio.run(main())
