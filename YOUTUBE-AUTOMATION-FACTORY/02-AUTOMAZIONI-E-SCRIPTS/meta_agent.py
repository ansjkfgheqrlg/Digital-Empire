# -*- coding: utf-8 -*-
"""
Owner: GAEL · Controllore: A2-QA · Origine: FORGE
Governo: APEX-7 Meta-Agent Supervisor (Plan 5)
"""
from __future__ import annotations

import logging
import json
import os
from typing import Dict, List, Any

from memory import MemoryQueryInterface

log = logging.getLogger("preventa-pw.meta_agent_sup")

class MetaAgent:
    def __init__(self, memory: MemoryQueryInterface):
        self.agent_id = "META-AGENT-1"
        self.memory = memory

    def analyze_and_optimize(self) -> Dict[str, Any]:
        """Esegue un ciclo di analisi sui log decisionali e di performance per ottimizzare le regole e i gate."""
        log.info(f"🧠 [{self.agent_id}] Avvio supervisione e calibrazione dinamica delle strategie...")
        
        # Legge il log storico di performance e decisioni
        decisions = self.memory._load_json_noblock(self.memory.decision_log_path, [])
        perf_logs = self.memory._load_json_noblock(self.memory.perf_logs_path, [])
        strategies = self.memory._load_json_noblock(self.memory.strategy_store_path, [])
        
        # 1. Analisi dei colli di bottiglia nei gate qualitativi
        gate_failures: Dict[str, int] = {}
        for dec in decisions:
            decision_text = dec.get("decision", "")
            if "FAIL" in decision_text:
                # Estrae il gate ID dal nome o testo
                gate_id = dec.get("id", "").split("-")[1] if "-" in dec.get("id", "") else "sconosciuto"
                gate_failures[gate_id] = gate_failures.get(gate_id, 0) + 1

        log.info(f"📊 [{self.agent_id}] Colli di bottiglia rilevati (fallimenti gate): {gate_failures}")

        # 2. Ottimizzazione pesi e success rate delle strategie
        # Calcoliamo la performance reale dei video prodotti con determinate strategie
        updated_strategies_count = 0
        for strat in strategies:
            strat_name = strat.get("name")
            # Associazione strategia ↔ performance log: si considerano TUTTI i log con una
            # keyword reale e un CTR misurato. Prima il filtro era fisso su `keyword ==
            # "claude code"` (funnel morto): sui video di @dosementale non trovava mai nulla e
            # il success rate delle strategie non veniva mai aggiornato (2026-07-31).
            matching_perf = [log_rec for log_rec in perf_logs
                             if log_rec.get("keyword")
                             and (log_rec.get("metrics") or {}).get("ctr") is not None]
            
            if matching_perf:
                # Calcola il CTR medio e la retention
                ctrs = [p["metrics"]["ctr"] for p in matching_perf]
                avg_ctr = sum(ctrs) / len(ctrs) if ctrs else 0.0
                
                # Se il CTR medio è > 7.5%, aumentiamo il success rate della strategia
                old_rate = strat.get("success_rate", 0.5)
                if avg_ctr > 7.5:
                    new_rate = min(1.0, round(old_rate + 0.02, 2))
                else:
                    new_rate = max(0.0, round(old_rate - 0.05, 2))
                    
                strat["success_rate"] = new_rate
                strat["times_used"] = strat.get("times_used", 0) + len(matching_perf)
                updated_strategies_count += 1
                log.info(f"📈 [{self.agent_id}] Strategia '{strat_name}' ricalibrata: {old_rate} -> {new_rate} (CTR Medio: {avg_ctr}%)")

        if updated_strategies_count > 0:
            self.memory._acquire_lock()
            try:
                self.memory._save_json_noblock(self.memory.strategy_store_path, strategies)
            finally:
                self.memory._release_lock()

        # 3. Raccomandazione regolazione soglia gate
        recommendations = {}
        for gate_id, fails in gate_failures.items():
            if fails >= 3:
                recommendations[gate_id] = "Diminuire la tolleranza e richiedere rigenerazione automatica preventiva"
                
        return {
            "status": "success",
            "gate_bottlenecks": gate_failures,
            "strategies_updated": updated_strategies_count,
            "recommendations": recommendations
        }
