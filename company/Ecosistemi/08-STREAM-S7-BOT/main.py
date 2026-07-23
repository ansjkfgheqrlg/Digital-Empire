import asyncio
import logging
import os
from dotenv import load_dotenv

from data_manager import SolanaDataManager
from analysis_engine import AnalysisEngine
from execution_engine import ExecutionEngine
from risk_manager import RiskManager

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
    
    # Inizializzazione dei 4 Layer
    data_manager = SolanaDataManager(wss_url=wss_url)
    analysis_engine = AnalysisEngine()
    execution_engine = ExecutionEngine(mode=trade_mode)
    risk_manager = RiskManager(base_bankroll=base_bankroll, max_position_pct=max_position)
    
    # Callback che lega i layer
    async def on_new_event(event_data):
        # Layer B
        signal = await analysis_engine.process_event(event_data)
        
        if signal:
            # Layer D
            capital_to_allocate = risk_manager.assess_trade(signal)
            
            if capital_to_allocate:
                # Layer C
                success = await execution_engine.execute_trade(signal, capital_to_allocate)
                if not success:
                    logger.warning("Trade simulato fallito o droppato dal network/slippage.")
    
    # Registrazione callback sul Data Manager
    data_manager.register_callback(on_new_event)
    
    # Avvio ascolto infinito
    try:
        await data_manager.listen_logs()
    except KeyboardInterrupt:
        logger.info("Spegnimento manuale del bot...")
        data_manager.stop()

if __name__ == "__main__":
    asyncio.run(main())
