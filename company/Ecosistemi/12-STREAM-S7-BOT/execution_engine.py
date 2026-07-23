import logging
import csv
import os
from datetime import datetime

logger = logging.getLogger(__name__)

class ExecutionEngine:
    """
    Layer C: Execution Engine (PAPER TRADING MODE).
    Costruisce e firma transazioni virtuali per simulare i costi reali di mercato.
    Non tocca mai una chiave privata vera se TRADE_MODE=SIMULATION.
    """
    
    def __init__(self, mode: str = "SIMULATION"):
        self.mode = mode
        self.log_file = "paper_trade_log.csv"
        self._init_log_file()
        
    def _init_log_file(self):
        if not os.path.exists(self.log_file):
            with open(self.log_file, mode='w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([
                    "timestamp", "action", "token_address", "amount_sol", 
                    "base_fee_sol", "bribe_fee_sol", "total_cost_sol", "slippage_bps", "status"
                ])

    async def execute_trade(self, signal: dict, allocated_capital: float) -> bool:
        """
        Esegue la trade in base al segnale. In simulazione, registra solo l'esito
        e deduce teoricamente i costi di transazione per l'analisi dell'expectancy.
        """
        action = signal.get("action")
        token = signal.get("token_address")
        bribe = signal.get("recommended_gas_bribe", 0.00001)
        slippage = signal.get("expected_slippage_bps", 100)
        
        # Simulazione calcolo Fee per Solana
        base_fee = 0.000005 # 5000 Lamports (Standard Solana fee)
        total_fee = base_fee + bribe
        
        # Costo totale stimato per entrare nella posizione (capitale + fee)
        total_cost = allocated_capital + total_fee
        
        if self.mode == "SIMULATION":
            return self._simulate_transaction(action, token, allocated_capital, base_fee, bribe, total_cost, slippage)
        else:
            logger.error("MODALITÀ LIVE NON AUTORIZZATA. Manca l'approvazione del GATE.")
            return False

    def _simulate_transaction(self, action, token, amount, base_fee, bribe, total_cost, slippage) -> bool:
        """Firma virtuale e logging nel paper trade."""
        timestamp = datetime.now().isoformat()
        
        # Simuliamo un tasso di fallimento del 10% tipico contro i MEV bot (slippage eccessivo o TX droppata)
        import random
        is_success = random.random() > 0.10
        status = "SUCCESS" if is_success else "FAILED_SLIPPAGE"
        
        # Anche se fallisce, su Solana paghi la base fee
        actual_cost = total_cost if is_success else base_fee

        try:
            with open(self.log_file, mode='a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([
                    timestamp, action, token, round(amount, 6), 
                    round(base_fee, 6), round(bribe, 6), round(actual_cost, 6), slippage, status
                ])
            logger.info(f"[EXECUTION] Paper Trade Registrato: {action} su {token} | Costo Rete: {round(base_fee + bribe, 6)} SOL | Status: {status}")
            return is_success
        except Exception as e:
            logger.error(f"Errore scrittura log paper trade: {e}")
            return False
