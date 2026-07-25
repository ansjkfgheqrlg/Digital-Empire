# -*- coding: utf-8 -*-
"""
Owner: GAEL · Controllore: A2-QA · Origine: FORGE
Governo: APEX-7 YouTube Refactoring Unit Tests (Plan 1)
"""
from __future__ import annotations

import unittest
import os
import shutil
import json
from datetime import datetime

from event_bus import EventBus, Event
from memory import MemoryQueryInterface
from quality_gate import QualityGateEngine
from gate_agent import GateAgent

class TestYouTubeApex7(unittest.TestCase):
    def setUp(self):
        # Utilizza un run_id temporaneo per isolare i test
        self.run_id = f"test-yt-{int(datetime.now().timestamp())}"
        self.memory = MemoryQueryInterface(run_id=self.run_id)
        
        # Override per isolamento dei test
        self.memory.decision_log_path = os.path.join(self.memory.base_dir, f"decision_log_{self.run_id}.json")
        self.memory.strategy_store_path = os.path.join(self.memory.base_dir, f"strategy_store_{self.run_id}.json")
        self.memory.snapshots_path = os.path.join(self.memory.base_dir, f"snapshots_{self.run_id}.json")
        self.memory.learned_rules_path = os.path.join(self.memory.base_dir, f"learned_rules_{self.run_id}.json")
        self.memory.perf_logs_path = os.path.join(self.memory.base_dir, f"performance_logs_{self.run_id}.json")
        
        # Re-inizializza con i nuovi path isolati
        self.memory.initialize_files()
        
        self.event_bus = EventBus()
        self.gate_agent = GateAgent(self.event_bus, self.memory)

    def tearDown(self):
        # Pulisce tutti i file temporanei con self.run_id nel nome
        for f in os.listdir(self.memory.base_dir):
            if self.run_id in f:
                try:
                    os.remove(os.path.join(self.memory.base_dir, f))
                except Exception:
                    pass
                    
        runs_dir = os.path.join(self.memory.base_dir, "runs")
        if os.path.exists(runs_dir):
            for f in os.listdir(runs_dir):
                if self.run_id in f:
                    try:
                        os.remove(os.path.join(runs_dir, f))
                    except Exception:
                        pass
                        
        decisions_dir = os.path.join(self.memory.base_dir, "decisions")
        if os.path.exists(decisions_dir):
            for f in os.listdir(decisions_dir):
                if self.run_id in f:
                    try:
                        os.remove(os.path.join(decisions_dir, f))
                    except Exception:
                        pass

    def test_event_bus_pub_sub(self):
        events_received = []
        def handler(event: Event):
            events_received.append(event)

        self.event_bus.subscribe("test.event", handler)
        self.event_bus.publish("test.event", "test_sender", {"key": "val"})
        
        self.assertEqual(len(events_received), 1)
        self.assertEqual(events_received[0].publisher, "test_sender")
        self.assertEqual(events_received[0].payload["key"], "val")

    def test_memory_initialization(self):
        self.assertTrue(os.path.exists(self.memory.state_file))
        mem = self.memory.get_working_memory()
        self.assertEqual(mem["run_id"], self.run_id)
        self.assertEqual(mem["current_phase"], 1)

    def test_memory_log_decision(self):
        decision_id = f"DEC-test-decision-{self.run_id}"
        self.memory.log_decision(
            decision_id=decision_id,
            decision="Test Choice",
            reason="Validation of test case",
            rejected=["Option A"],
            confidence=0.9
        )
        md_file = os.path.join(self.memory.base_dir, "decisions", f"{decision_id}_{self.run_id}.md")
        self.assertTrue(os.path.exists(md_file))
        
        # Carica il log delle decisioni e controlla
        decisions = self.memory._load_json_noblock(self.memory.decision_log_path, [])
        found = [d for d in decisions if d["id"] == decision_id]
        self.assertEqual(len(found), 1)
        self.assertEqual(found[0]["decision"], "Test Choice")

    def test_quality_gate_evaluations(self):
        engine = QualityGateEngine()
        
        # Test L1_L2
        passed, score, reasons = engine.evaluate_gate("L1_L2", "Dose Mentale")
        self.assertTrue(passed)
        self.assertEqual(score, 1.0)
        
        passed, score, reasons = engine.evaluate_gate("L1_L2", "")
        self.assertFalse(passed)
        
        # Test L3_L4 (Script structure)
        script_ok = "## HOOK: Ciao a tutti. ## CORPO: Ecco il valore. ## CTA: Iscriviti ora."
        passed, score, reasons = engine.evaluate_gate("L3_L4", script_ok)
        self.assertTrue(passed)
        
        script_fail = "Solo testo senza intestazioni e sezioni richieste."
        passed, score, reasons = engine.evaluate_gate("L3_L4", script_fail)
        self.assertFalse(passed)

    def test_gate_agent_workflow(self):
        # Valida un gate tramite l'agente e controlla lo stato e gli eventi pubblicati
        events = []
        self.event_bus.subscribe("gate.passed", lambda e: events.append(e))
        
        res = self.gate_agent.verify_gate("L1_L2", "Dose Mentale")
        self.assertTrue(res)
        self.assertEqual(len(events), 1)
        self.assertEqual(events[0].payload["gate_id"], "L1_L2")
        self.assertEqual(self.gate_agent.state, "IDLE")

    def test_conductor_workflow_e2e(self):
        from agents import Conductor
        
        events_fired = []
        self.event_bus.subscribe("workflow.completed", lambda e: events_fired.append(e))
        
        conductor = Conductor(self.event_bus, self.memory, self.gate_agent)
        conductor.start_workflow("Dose Mentale")
        
        self.assertEqual(len(events_fired), 1)
        self.assertEqual(events_fired[0].payload["video_title"], "Installare Claude Code locale")

    def test_remediation_and_escalation(self):
        failed_events = []
        escalated_events = []
        self.event_bus.subscribe("gate.failed", lambda e: failed_events.append(e))
        self.event_bus.subscribe("gate.escalated", lambda e: escalated_events.append(e))
        
        # Simuliamo 3 chiamate fallite di fila a verify_gate per L3_L4
        for _ in range(3):
            self.gate_agent.verify_gate("L3_L4", "Testo cortissimo senza intestazioni")
            
        self.assertEqual(len(failed_events), 3)
        self.assertEqual(len(escalated_events), 1)
        self.assertEqual(self.gate_agent.state, "ESCALATING")

    def test_concurrent_writes(self):
        import threading
        
        # Test di scrittura concorrente su working memory
        def worker(thread_id):
            for i in range(10):
                mem = self.memory.get_working_memory()
                mem[f"thread_{thread_id}"] = i
                self.memory.save_working_memory(mem)
                
        threads = []
        for t in range(5):
            thread = threading.Thread(target=worker, args=(t,))
            threads.append(thread)
            thread.start()
            
        for thread in threads:
            thread.join()
            
        # Verifica che tutte le scritture siano registrate correttamente
        final_mem = self.memory.get_working_memory()
        for t in range(5):
            self.assertEqual(final_mem[f"thread_{t}"], 9)

    def test_meta_agent_optimization(self):
        from meta_agent import MetaAgent
        
        # Inseriamo un record di performance finto per simulare un buon CTR
        logs = [
            {
                "video_id": "claude-code-001",
                "keyword": "claude code",
                "metrics": {
                    "views_per_hour": 50.0,
                    "ctr": 9.5,
                    "retention_rate": 60.0
                }
            }
        ]
        self.memory._save_json_noblock(self.memory.perf_logs_path, logs)
        
        # Facciamo eseguire l'agente
        meta_agent = MetaAgent(self.memory)
        res = meta_agent.analyze_and_optimize()
        
        self.assertEqual(res["status"], "success")
        self.assertGreater(res["strategies_updated"], 0)
        
        # Verifica che il success rate sia aumentato
        strategies = self.memory._load_json_noblock(self.memory.strategy_store_path, [])
        self.assertEqual(strategies[0]["success_rate"], 0.97)  # 0.95 + 0.02

    def test_memory_compression(self):
        # Scrive 55 decisioni per triggerare la compressione
        for i in range(55):
            self.memory.log_decision(
                decision_id=f"DEC-comp-{i}-{self.run_id}",
                decision=f"Decision {i}",
                reason="Test logic",
                rejected=[],
                confidence=0.8
            )
            
        # Verifichiamo che il log principale contenga ora 25 record (55 - 30 archiviati)
        log_data = self.memory._load_json_noblock(self.memory.decision_log_path, [])
        self.assertEqual(len(log_data), 25)
        
        # Verifichiamo che l'archivio contenga 30 record
        archive_path = os.path.join(self.memory.base_dir, f"decision_log_archive_{self.run_id}.json")
        archive_data = self.memory._load_json_noblock(archive_path, [])
        self.assertEqual(len(archive_data), 30)

if __name__ == "__main__":
    unittest.main()
