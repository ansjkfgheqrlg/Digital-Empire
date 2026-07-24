# -*- coding: utf-8 -*-
"""
Test runner for APEX-7 Deep Refinement components (Event Bus, Memory, Quality Gate, Gate Agent).
"""
import os
import sys
import unittest
import shutil

# Assicura che la directory degli script sia sul path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from event_bus import EventBus, Event
from memory import MemoryQueryInterface
from quality_gate import QualityGateEngine, GATE_DEFINITIONS
from gate_agent import GateAgent

class TestApex7Components(unittest.TestCase):
    
    def setUp(self):
        # Reset dei singleton e dei file temporanei
        self.bus = EventBus()
        self.bus.clear()
        
        self.test_db_path = "data/test_memory_db.json"
        if os.path.exists(self.test_db_path):
            os.remove(self.test_db_path)
            
        self.memory = MemoryQueryInterface(memory_filepath=self.test_db_path)
        self.gate_engine = QualityGateEngine(self.memory, self.bus)
        self.agent = GateAgent(self.memory, self.bus)
        from agents import QAAgent
        self.qa_agent = QAAgent(self.agent, self.bus)

    def tearDown(self):
        if os.path.exists(self.test_db_path):
            os.remove(self.test_db_path)

    def test_event_bus_pub_sub(self):
        """Test che la pubblicazione e sottoscrizione degli eventi funzioni correctly."""
        received_payloads = []
        
        def test_handler(event: Event):
            received_payloads.append(event.payload)
            
        self.bus.subscribe("task.created", test_handler)
        
        payload = {"task_id": "T-1", "description": "Test Scraper run"}
        self.bus.publish("task.created", publisher="Orchestrator", payload=payload)
        
        self.assertEqual(len(received_payloads), 1)
        self.assertEqual(received_payloads[0]["task_id"], "T-1")

    def test_event_bus_exactly_once(self):
        """Test che la consegna EXACTLY_ONCE prevenga doppie elaborazioni dello stesso evento."""
        run_count = 0
        
        def duplicate_handler(event: Event):
            nonlocal run_count
            run_count += 1
            
        self.bus.subscribe("task.decomposed", duplicate_handler)
        
        # Pubblica lo stesso evento due volte (tramite lo stesso bus instance ed ID)
        event_obj = self.bus.publish("task.decomposed", publisher="Planner", payload={"task_id": "T-2"}, delivery_mode="EXACTLY_ONCE")
        
        # Simuliamo reinvio dello stesso identico ID di evento
        # Nel nostro bus, pubblicare con gli stessi parametri genera un nuovo ID, quindi forziamo la stessa elaborazione
        # tramite simulazione o ripetizione dello stesso ID.
        self.bus._event_history.append(event_obj)
        # Eseguiamo il dispatch manuale come farebbe il bus se ricevesse l'evento duplicato
        subscribers = self.bus._subscribers.get("task.decomposed", [])
        for sub in subscribers:
            sub_name = getattr(sub, "__name__", str(sub))
            if event_obj.id in self.bus._processed_exactly_once.get(sub_name, []):
                continue  # Dovrebbe skippare
            sub(event_obj)
            
        self.assertEqual(run_count, 1)

    def test_memory_write_and_contextual_recall(self):
        """Test di scrittura e recupero contestuale (relevance * recency * confidence)."""
        author = "test_agent"
        # Scrive un record rilevante
        self.memory.write(
            layer="general_knowledge",
            content={"topic": "Playwright anti-blocking settings", "settings": "--disable-blink-features"},
            author=author,
            importance=0.9
        )
        
        # Esegue contextual recall
        recall = self.memory.contextual_recall(current_task="anti-blocking settings Playwright", current_agent="test_agent")
        
        self.assertEqual(recall["returned"], 1)
        self.assertEqual(recall["results"][0]["content"]["topic"], "Playwright anti-blocking settings")

    def test_memory_forget(self):
        """Test di strategic forgetting (archiviazione logica)."""
        author = "test_agent"
        mem_id = self.memory.write(
            layer="strategy_store",
            content={"name": "Old Strategy", "success_rate": 0.2},
            author=author
        )
        self.assertIsNotNone(mem_id)
        
        # Archivia
        success = self.memory.forget(record_id=mem_id, reason="low success rate")
        self.assertTrue(success)
        
        # Verifica che non sia più attivo nel contextual recall
        recall = self.memory.contextual_recall(current_task="Old Strategy", current_agent="test_agent")
        self.assertEqual(recall["returned"], 0)

    def test_memory_lead_store(self):
        """Test che le funzioni write_lead e get_lead gestiscano correttamente lo stato dei lead."""
        author = "test_agent"
        lead_id = "+3902555555"
        lead_data = {"nome_attivita": "Memory Auto SRL", "stato": "da_contattare", "citta": "Brescia"}
        
        # Scrittura
        success = self.memory.write_lead(lead_id, lead_data, author)
        self.assertTrue(success)
        
        # Lettura
        retrieved = self.memory.get_lead(lead_id)
        self.assertIsNotNone(retrieved)
        self.assertEqual(retrieved["nome_attivita"], "Memory Auto SRL")
        self.assertEqual(retrieved["stato"], "da_contattare")
        
        # Aggiornamento stato
        success_update = self.memory.write_lead(lead_id, {"stato": "contattato"}, author)
        self.assertTrue(success_update)
        
        # Verifica aggiornato
        updated = self.memory.get_lead(lead_id)
        self.assertEqual(updated["stato"], "contattato")
        self.assertEqual(updated["citta"], "Brescia") # Conserva altri campi

    def test_quality_gate_engine_pass(self):
        """Test che il motore del Quality Gate approvi un livello se lo score supera la soglia."""
        criteria_evals = {
            "C1": "PASS",
            "C2": "PASS",
            "C3": "PASS",
            "C4": "PASS",
            "C5": "PASS"
        }
        
        report = self.gate_engine.run_check(gate_id="L1_L2", criteria_evaluations=criteria_evals, evaluator_agent="GATE-1")
        
        self.assertTrue(report["passed"])
        self.assertEqual(report["score"], 1.0)

    def test_quality_gate_engine_fail_and_escalate(self):
        """Test che l'escalation protocol scatti al 3° fallimento consecutivo."""
        criteria_evals = {
            "C1": "FAIL",
            "C2": "FAIL",
            "C3": "FAIL",
            "C4": "FAIL",
            "C5": "FAIL"
        }
        
        # Subscriber per intercettare l'evento di escalation
        escalation_received = False
        def escalation_handler(event: Event):
            nonlocal escalation_received
            escalation_received = True
            
        self.bus.subscribe("gate.escalated", escalation_handler)
        
        # 1° tentativo fallito
        self.gate_engine.run_check(gate_id="L1_L2", criteria_evaluations=criteria_evals, evaluator_agent="GATE-1")
        self.assertFalse(escalation_received)
        
        # 2° tentativo fallito
        self.gate_engine.run_check(gate_id="L1_L2", criteria_evaluations=criteria_evals, evaluator_agent="GATE-1")
        self.assertFalse(escalation_received)
        
        # 3° tentativo fallito -> deve scattare l'escalation
        self.gate_engine.run_check(gate_id="L1_L2", criteria_evaluations=criteria_evals, evaluator_agent="GATE-1")
        self.assertTrue(escalation_received)

    def test_gate_agent_integration(self):
        """Test di integrazione del GateAgent e transizione degli stati."""
        output = "città: Como, categoria: concessionario auto, limit: 10"
        report = self.agent.evaluate_output(gate_id="L1_L2", output_to_evaluate=output)
        
        self.assertTrue(report["passed"])
        self.assertEqual(report["score"], 1.0)
        self.assertEqual(self.agent.state, "IDLE")

    def test_writer_agent_generation(self):
        """Test che il WriterAgent generi i messaggi personalizzati correttamente."""
        from agents import WriterAgent
        writer = WriterAgent(self.bus)
        leads = [
            {
                "nome_attivita": "Test Auto Srl",
                "telefono": "+390212345",
                "priorita_lead": "ALTA",
                "ha_sito": False,
                "note_qualifica": "Senza sito web"
            }
        ]
        messages = writer.generate_messages(leads, "Milano")
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0]["nome_attivita"], "Test Auto Srl")
        self.assertIn("whatsapp_msg1", messages[0])

    def test_sender_agent_transmission(self):
        """Test che il SenderAgent invii i messaggi e pubblichi l'evento corretto."""
        from agents import SenderAgent
        sender = SenderAgent(self.bus)
        messages = [
            {
                "nome_attivita": "Test Auto Srl",
                "canale_primario": "whatsapp",
                "whatsapp_msg1": "Ciao, ho visto la tua scheda..."
            }
        ]
        sent = sender.send_outreach(messages, "Milano")
        self.assertEqual(sent[0]["stato"], "contattato")

    def test_responder_agent_classification(self):
        """Test della classificazione delle risposte ricevute tramite ResponderAgent."""
        from agents import ResponderAgent
        responder = ResponderAgent(self.bus)
        
        r1 = responder.process_reply("Test Auto Srl", "Sì, mi interessa saperne di più")
        self.assertEqual(r1["esito"], "interessato")
        self.assertIn("Ti propongo", r1["suggested_response"])
        
        r2 = responder.process_reply("Test Auto Srl", "No, non ci interessa, non scriveteci")
        self.assertEqual(r2["esito"], "no_grazie")

    def test_conductor_workflow_e2e(self):
        """Test del workflow Conductor end-to-end con i nuovi agenti."""
        from agents import Conductor, ScraperAgent, QualifierAgent, WriterAgent, SenderAgent, QAAgent
        
        # Mock Scraper che restituisce lead immediato
        class MockScraper(ScraperAgent):
            def execute_scraping(self, city, categoria, limit):
                self.event_bus.publish("leads.extracted", self.agent_id, {
                    "city": city,
                    "leads": [{"nome_attivita": "Mock Auto Srl", "telefono": "+390212345", "sito_web": ""}],
                    "count": 1
                })
        
        scraper = MockScraper(None, self.bus)
        qualifier = QualifierAgent(self.bus)
        writer = WriterAgent(self.bus)
        sender = SenderAgent(self.bus)
        
        conductor = Conductor(
            event_bus=self.bus,
            scraper_agent=scraper,
            qualifier_agent=qualifier,
            writer_agent=writer,
            sender_agent=sender,
            sheets_agent=None,
            qa_agent=self.qa_agent,
            output_csv_path="data/test_output.csv",
            only_alta=False
        )
        
        workflow_completed = False
        def on_completed(event):
            nonlocal workflow_completed
            workflow_completed = True
            
        self.bus.subscribe("run.completed", on_completed)
        
        # Lancia il workflow per Como
        conductor.run_city_workflow("Como", "concessionario auto", 2)
        
        self.assertTrue(workflow_completed)
        
        # Pulisci file temporaneo generato dal test
        if os.path.exists("data/test_output.csv"):
            os.remove("data/test_output.csv")

    def test_meta_optimizer_loop(self):
        """Test che il MetaOptimizer calcoli correttamente le conversioni e archivi strategie scarse."""
        from meta_optimization import MetaOptimizer
        optimizer = MetaOptimizer(self.memory)
        
        # Inseriamo dei lead finti nel DB di memoria per simulare performance
        # Gancio 2 (B) ha ottime conversioni, Gancio 3 (C) fallisce sempre
        for i in range(10):
            # 10 invii con gancio 2 di cui 8 interessati
            self.memory.write_lead(f"L-A-{i}", {
                "nome_attivita": f"Lead A{i}",
                "stato": "interessato" if i < 8 else "contattato",
                "gancio_scelto": {"numero": 2, "nome": "Gancio B"}
            }, "test_agent")
            
        for i in range(6):
            # 6 invii con gancio 3 di cui 0 interessati
            self.memory.write_lead(f"L-B-{i}", {
                "nome_attivita": f"Lead B{i}",
                "stato": "no_grazie",
                "gancio_scelto": {"numero": 3, "nome": "Gancio C"}
            }, "test_agent")
            
        res = optimizer.run_optimization_loop()
        self.assertEqual(res["status"], "COMPLETED")
        
        # Verifichiamo che la strategia del gancio 3 (C) sia stata archiviata
        db = self.memory._read_db()
        strategies = db.get("strategy_store", [])
        
        for s in strategies:
            c = s["content"]
            g_num = c.get("parameters", {}).get("gancio_numero")
            if g_num == 3:
                self.assertEqual(s["status"], "ARCHIVED")
            elif g_num == 2:
                self.assertEqual(c["success_rate"], 0.8)

if __name__ == "__main__":
    unittest.main()

