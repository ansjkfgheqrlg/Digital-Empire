import logging
from typing import Optional

logger = logging.getLogger(__name__)

class RiskManager:
    """
    Layer D: Risk & Treasury.
    Gestisce l'esposizione del portafoglio e i kill-switch di emergenza.
    """
    def __init__(self, base_bankroll: float, max_position_pct: float):
        self.bankroll = base_bankroll
        self.max_position_pct = max_position_pct
        self.is_kill_switch_active = False
        
        # Simulazione posizioni aperte per logica Take-Profit/Stop-Loss
        self.open_positions = {}

    def assess_trade(self, signal: dict) -> Optional[float]:
        """
        Valuta se autorizzare il trade.
        Ritorna l'ammontare in SOL da allocare, oppure None se il trade è bloccato.
        """
        if self.is_kill_switch_active:
            logger.warning("[RISK] Kill-Switch attivo. Trade bloccato.")
            return None
            
        # Calcola il massimo allocabile (es. 5% di 10 SOL = 0.5 SOL)
        max_alloc = self.bankroll * (self.max_position_pct / 100.0)
        
        # Aggiungi ulteriore logica: se abbiamo già troppe posizioni aperte, blocca.
        if len(self.open_positions) >= 3:
            logger.warning("[RISK] Troppe posizioni aperte. Trade bloccato.")
            return None
            
        logger.info(f"[RISK] Trade approvato. Capitale allocato: {max_alloc} SOL")
        return max_alloc

    def activate_kill_switch(self):
        """Disarma l'intero sistema in caso di crollo del mercato o bug."""
        self.is_kill_switch_active = True
        logger.critical("🚨 KILL SWITCH ATTIVATO. Nessuna nuova transazione sarà autorizzata.")

    def deactivate_kill_switch(self):
        self.is_kill_switch_active = False
        logger.info("✅ Kill Switch disattivato. Ripresa operazioni.")
        
    def check_portfolio_health(self) -> bool:
        """Controlla se il bankroll è sceso sotto una soglia critica (es. -20%)."""
        # Se in futuro il paper trading loggherà perdite fittizie, questa funzione
        # ridurrà il bankroll e allerterà il sistema.
        pass
