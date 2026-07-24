# -*- coding: utf-8 -*-
"""
Owner: GAEL · Controllore: A2-QA · Origine: FORGE
Governo: APEX-7 Meta-Optimization & Performance Loop (Plan 7)
"""
from __future__ import annotations

import logging
import json
import os
from typing import Dict, List, Any

from memory import MemoryQueryInterface

log = logging.getLogger("preventa-pw.meta_opt")

class MetaOptimizer:
    def __init__(self, memory: MemoryQueryInterface):
        self.memory = memory

    def run_optimization_loop(self) -> Dict[str, Any]:
        """Analizza i lead contattati e le risposte per aggiornare le performance e la rotazione delle strategie."""
        log.info("📈 [MetaOptimizer] Avvio ciclo di ottimizzazione automatica delle strategie...")
        
        db = self.memory._read_db()
        leads = db.get("leads_store", [])
        strategies = db.get("strategy_store", [])
        
        if not leads:
            log.warning("⚠️ Nessun lead presente in memoria per calcolare le performance.")
            return {"status": "NO_LEADS"}

        # Conta esiti per ciascun gancio/strategia
        # Assumiamo che nei lead salviamo lo stato di contatto e il gancio utilizzato
        strategy_stats: Dict[int, Dict[str, int]] = {}
        
        for record in leads:
            content = record.get("content", {})
            stato = content.get("stato", "")
            gancio = content.get("gancio_scelto", {})
            gancio_num = gancio.get("numero")
            
            if gancio_num is None:
                continue
                
            if gancio_num not in strategy_stats:
                strategy_stats[gancio_num] = {"sent": 0, "replied": 0, "interested": 0}
                
            strategy_stats[gancio_num]["sent"] += 1
            if stato in ("risposto", "interessato"):
                strategy_stats[gancio_num]["replied"] += 1
            if stato == "interessato":
                strategy_stats[gancio_num]["interested"] += 1

        log.info(f"📊 Statistiche grezze per gancio: {strategy_stats}")

        # Aggiorna success rate nello strategy_store
        updated_count = 0
        for strat in strategies:
            strat_content = strat.get("content", {})
            gancio_num = strat_content.get("parameters", {}).get("gancio_numero")
            
            if gancio_num in strategy_stats:
                stats = strategy_stats[gancio_num]
                sent = stats["sent"]
                interested = stats["interested"]
                
                # Formula semplice: conversion rate = interessati / inviati (minimo 1 invio)
                new_success_rate = round(interested / sent, 2) if sent > 0 else strat_content.get("success_rate", 0.0)
                
                log.info(f"🔄 Strategia {strat_content['name']}: precedente rate {strat_content.get('success_rate')} -> nuovo {new_success_rate} (inviati {sent})")
                strat_content["success_rate"] = new_success_rate
                strat_content["times_used"] = strat_content.get("times_used", 0) + sent
                
                # Se il tasso di successo scende sotto il 20% dopo almeno 5 invii, marca la strategia come DEPRECATED/ARCHIVED
                if sent >= 5 and new_success_rate < 0.20:
                    strat["status"] = "ARCHIVED"
                    log.warning(f"🧹 Strategia {strat_content['name']} disattivata per scarso rendimento (< 20% conversion).")
                
                updated_count += 1

        if updated_count > 0:
            self.memory._write_db(db, author="meta_optimizer")
            log.info("💾 Strategy store aggiornato con successo in memoria.")
            
        return {
            "status": "COMPLETED",
            "updated_strategies": updated_count,
            "stats": strategy_stats
        }
