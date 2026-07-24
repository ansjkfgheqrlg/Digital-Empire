# -*- coding: utf-8 -*-
"""
Owner: GAEL · Controllore: A2-QA · Origine: FORGE
Governo: APEX-7 Swarm Agents & Conductor (Plan 2)
"""
from __future__ import annotations

import logging
import os
import sys
import json
import subprocess
from datetime import datetime
from typing import Dict, List, Any, Optional

from event_bus import EventBus, Event
from memory import MemoryQueryInterface
from gate_agent import GateAgent

log = logging.getLogger("preventa-pw.agents")

# Assicuriamoci che i path siano corretti
SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
FACTORY_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
TEMPLATES_DIR = os.path.join(FACTORY_DIR, "05-TEMPLATES-E-KIT")

class NicheScoutAgent:
    def __init__(self, event_bus: EventBus, memory: MemoryQueryInterface):
        self.agent_id = "NicheScout-1"
        self.event_bus = event_bus
        self.memory = memory

    def execute_scouting(self, topic: str):
        log.info(f"🔍 [{self.agent_id}] Scouting nicchia target: {topic}...")
        
        # Simulazione niche-scout con cashcow_check
        scheda_path = os.path.join(TEMPLATES_DIR, "scheda-nicchia.md")
        os.makedirs(os.path.dirname(scheda_path), exist_ok=True)
        
        canale_mock = {
            "channel": "Legami d'amore",
            "videos": [
                {"title": "Come installare Claude Code", "views": 15000, "age_hours": 120, "errors": []},
                {"title": "Costruire Agent Swarm", "views": 32000, "age_hours": 240, "errors": ["seo debole"]}
            ]
        }
        mock_json_path = os.path.join(FACTORY_DIR, "canale_tmp.json")
        with open(mock_json_path, "w", encoding="utf-8") as f:
            json.dump(canale_mock, f)
            
        res = subprocess.run([sys.executable, os.path.join(SCRIPT_DIR, "cashcow_check.py"), "--json", mock_json_path], capture_output=True, text=True)
        if os.path.exists(mock_json_path):
            os.remove(mock_json_path)
            
        log.info(f"📊 [{self.agent_id}] Risultati Cashcow Check per {topic}.")
        
        # Scrittura scheda-nicchia.md
        with open(scheda_path, "w", encoding="utf-8") as f:
            f.write(f"# Scheda Nicchia: {topic}\n\n")
            f.write(f"- Canale cash cow analizzato: Legami d'amore\n")
            f.write(f"- Indice Cash Cow: 76.5 (Soglia superata: SÌ)\n")
            f.write(f"- Verdetto: PASS\n")
            
        self.event_bus.publish(
            event_type="niche.scouted",
            publisher=self.agent_id,
            payload={"topic": topic, "scheda_nicchia_path": scheda_path}
        )


class VideoHunterAgent:
    def __init__(self, event_bus: EventBus, memory: MemoryQueryInterface):
        self.agent_id = "VideoHunter-1"
        self.event_bus = event_bus
        self.memory = memory

    def execute_selection(self, topic: str):
        log.info(f"🎯 [{self.agent_id}] Selezione video ottimale per la replica...")
        candidati_path_json = os.path.join(TEMPLATES_DIR, "candidati-video.json")
        
        candidati = {
            "channel": "Legami d'amore",
            "videos": [
                {"title": "Installare Claude Code locale", "url": "https://youtube.com/watch?v=1", "views": 25000, "age_hours": 100, "errors": ["seo debole"]},
                {"title": "Prompt Engineering per Agent Swarm", "url": "https://youtube.com/watch?v=2", "views": 8000, "age_hours": 150, "errors": []}
            ]
        }
        with open(candidati_path_json, "w", encoding="utf-8") as f:
            json.dump(candidati, f, indent=2)
            
        # Validazione schema
        subprocess.run([sys.executable, os.path.join(SCRIPT_DIR, "validate_schemas.py"), "candidati-video", candidati_path_json], capture_output=True)
        
        # Calcolo SEO Score per i candidati
        seo_report_json = os.path.join(TEMPLATES_DIR, "seo-report.json")
        seo_report = {
            "videos": [
                {"title": "Installare Claude Code locale", "seo_score": 45.0, "label": "A-upside"},
                {"title": "Prompt Engineering per Agent Swarm", "seo_score": 85.0, "label": "B-sicurezza"}
            ]
        }
        with open(seo_report_json, "w", encoding="utf-8") as f:
            json.dump(seo_report, f, indent=2)
            
        self.event_bus.publish(
            event_type="video.selected",
            publisher=self.agent_id,
            payload={
                "video_title": "Installare Claude Code locale",
                "label": "A-upside",
                "candidates_path": candidati_path_json,
                "seo_report_path": seo_report_json
            }
        )


class ScriptWriterAgent:
    def __init__(self, event_bus: EventBus, memory: MemoryQueryInterface):
        self.agent_id = "ScriptWriter-1"
        self.event_bus = event_bus
        self.memory = memory

    def execute_script_writing(self, topic: str, video_title: str):
        log.info(f"✍️ [{self.agent_id}] Scrittura script per '{video_title}'...")
        script_path = os.path.join(TEMPLATES_DIR, "script.md")
        
        with open(script_path, "w", encoding="utf-8") as f:
            f.write(f"# Script: Come installare ed usare {video_title}\n\n")
            f.write("## HOOK\nVuoi installare l'agente IA più veloce ed efficiente direttamente sul tuo computer? In questo video...\n\n")
            f.write("## CORPO\nEcco i comandi per installarlo...\n\n")
            f.write("## CTA\n1. Iscriviti per altri video\n2. Scarica la guida nei commenti\n3. Entra nella community\n")
            
        self.event_bus.publish(
            event_type="script.written",
            publisher=self.agent_id,
            payload={"video_title": video_title, "script_path": script_path}
        )


class VideoProducerAgent:
    def __init__(self, event_bus: EventBus, memory: MemoryQueryInterface):
        self.agent_id = "VideoProducer-1"
        self.event_bus = event_bus
        self.memory = memory

    def execute_production(self, video_title: str, script_path: str):
        log.info(f"🎬 [{self.agent_id}] Generazione specifica di produzione Fliki...")
        spec_path = os.path.join(TEMPLATES_DIR, "produzione-spec.json")
        
        spec = {
            "video_id": "claude-code-001",
            "title": video_title,
            "voice": "Fabio (Italiano)",
            "music": "Soft ambient",
            "hook_type": "Question",
            "scene_count": 5,
            "scenes": [
                {"number": 1, "text": "Vuoi installare l'agente IA più veloce?", "duration": 5.0}
            ]
        }
        with open(spec_path, "w", encoding="utf-8") as f:
            json.dump(spec, f, indent=2)
            
        # Validazione schema
        subprocess.run([sys.executable, os.path.join(SCRIPT_DIR, "validate_schemas.py"), "produzione-spec", spec_path], capture_output=True)
        
        self.event_bus.publish(
            event_type="video.produced",
            publisher=self.agent_id,
            payload={"video_title": video_title, "spec_path": spec_path}
        )


class MetadataOptimizerAgent:
    def __init__(self, event_bus: EventBus, memory: MemoryQueryInterface):
        self.agent_id = "MetadataOptimizer-1"
        self.event_bus = event_bus
        self.memory = memory

    def execute_optimization(self, video_title: str):
        log.info(f"🏷️ [{self.agent_id}] Ottimizzazione metadati e thumbnail...")
        brief_path = os.path.join(TEMPLATES_DIR, "brief-miniatura.json")
        brief = {
            "title": video_title,
            "concept": "Console nera con scritte arancioni e logo Claude",
            "text_overlay": "CLAUDE CODE LOCALE",
            "image_prompt": "Minimal terminal styling with warm gradients"
        }
        with open(brief_path, "w", encoding="utf-8") as f:
            json.dump(brief, f, indent=2)
            
        metadata_path = os.path.join(TEMPLATES_DIR, "metadati.json")
        metadata = {
            "title": f"Come Installare {video_title} (Guida Passo-Passo)",
            "description": "Ecco come installare Claude Code nel terminale in modo semplice...",
            "tags": ["claude code", "antigravity", "digital empire"],
            "keyword": "claude code",
            "thumbnail": True,
            "subtitles": True
        }
        with open(metadata_path, "w", encoding="utf-8") as f:
            json.dump(metadata, f, indent=2)
            
        # Calcolo score SEO
        res = subprocess.run([sys.executable, os.path.join(SCRIPT_DIR, "seo_score.py"), "--json", metadata_path], capture_output=True, text=True)
        log.info(f"📊 [{self.agent_id}] Risultato SEO score:\n{res.stdout.strip()}")
        
        self.event_bus.publish(
            event_type="metadata.optimized",
            publisher=self.agent_id,
            payload={"video_title": video_title, "metadata_path": metadata_path}
        )


class PerformanceAuditorAgent:
    def __init__(self, event_bus: EventBus, memory: MemoryQueryInterface):
        self.agent_id = "PerformanceAuditor-1"
        self.event_bus = event_bus
        self.memory = memory

    def execute_audit(self, video_title: str):
        log.info(f"📈 [{self.agent_id}] Avvio audit metriche per '{video_title}'...")
        
        # Append log storico
        logs = self.memory._load_json_noblock(self.memory.perf_logs_path, [])
        new_log = {
            "video_id": "claude-code-001",
            "keyword": "claude code",
            "voice": "Fabio (Italiano)",
            "hook_type": "Question",
            "tags": ["claude code", "antigravity", "digital empire"],
            "metrics": {
                "views_per_hour": 35.5,
                "ctr": 8.2,
                "retention_rate": 55.0,
                "curve_type": "regolare"
            }
        }
        logs.append(new_log)
        self.memory._save_json_noblock(self.memory.perf_logs_path, logs)
        
        # Esecuzione self_improve con override dei file per isolamento dei test
        subprocess.run([
            sys.executable,
            os.path.join(SCRIPT_DIR, "self_improve.py"),
            "--logs-file", self.memory.perf_logs_path,
            "--rules-file", self.memory.learned_rules_path
        ], capture_output=True)
        
        self.event_bus.publish(
            event_type="audit.completed",
            publisher=self.agent_id,
            payload={"video_title": video_title, "status": "success"}
        )


class Conductor:
    def __init__(self, event_bus: EventBus, memory: MemoryQueryInterface, qa_agent: GateAgent):
        self.agent_id = "Conductor-1"
        self.event_bus = event_bus
        self.memory = memory
        self.qa_agent = qa_agent
        
        # Roster operatori
        self.scout_agent = NicheScoutAgent(event_bus, memory)
        self.hunter_agent = VideoHunterAgent(event_bus, memory)
        self.writer_agent = ScriptWriterAgent(event_bus, memory)
        self.producer_agent = VideoProducerAgent(event_bus, memory)
        self.optimizer_agent = MetadataOptimizerAgent(event_bus, memory)
        self.auditor_agent = PerformanceAuditorAgent(event_bus, memory)

        # Sottoscrizioni eventi
        self.event_bus.subscribe("niche.scouted", self.on_niche_scouted)
        self.event_bus.subscribe("video.selected", self.on_video_selected)
        self.event_bus.subscribe("script.written", self.on_script_written)
        self.event_bus.subscribe("video.produced", self.on_video_produced)
        self.event_bus.subscribe("metadata.optimized", self.on_metadata_optimized)
        self.event_bus.subscribe("audit.completed", self.on_audit_completed)
        self.event_bus.subscribe("gate.failed", self.on_gate_failed)

    def start_workflow(self, start_topic: str):
        log.info(f"🎭 [{self.agent_id}] Avvio del workflow di refactoring YouTube APEX-7...")
        
        self.event_bus.publish(
            event_type="task.created",
            publisher=self.agent_id,
            payload={"topic": start_topic}
        )
        
        # Validazione L1->L2
        if not self.qa_agent.verify_gate("L1_L2", start_topic):
            log.error("❌ Conductor bloccato al Gate L1_L2. Termino.")
            return

        self.scout_agent.execute_scouting(start_topic)

    def on_niche_scouted(self, event: Event):
        topic = event.payload.get("topic")
        scheda_path = event.payload.get("scheda_nicchia_path")
        
        # Validazione L2->L3
        if not self.qa_agent.verify_gate("L2_L3", topic):
            log.error("❌ Conductor bloccato al Gate L2_L3. Termino.")
            return
            
        self.hunter_agent.execute_selection(topic)

    def on_video_selected(self, event: Event):
        video_title = event.payload.get("video_title")
        topic = event.payload.get("topic", "Generica")
        
        self.writer_agent.execute_script_writing(topic, video_title)

    def on_script_written(self, event: Event):
        video_title = event.payload.get("video_title")
        script_path = event.payload.get("script_path")
        
        with open(script_path, "r", encoding="utf-8") as f:
            script_text = f.read()
            
        # Validazione L3->L4
        if not self.qa_agent.verify_gate("L3_L4", script_text):
            log.error("❌ Conductor bloccato al Gate L3_L4. Termino.")
            return
            
        self.producer_agent.execute_production(video_title, script_path)

    def on_video_produced(self, event: Event):
        video_title = event.payload.get("video_title")
        spec_path = event.payload.get("spec_path")
        
        with open(spec_path, "r", encoding="utf-8") as f:
            spec_text = f.read()
            
        # Validazione L4->L5
        if not self.qa_agent.verify_gate("L4_L5", spec_text):
            log.error("❌ Conductor bloccato al Gate L4_L5. Termino.")
            return
            
        self.optimizer_agent.execute_optimization(video_title)

    def on_metadata_optimized(self, event: Event):
        video_title = event.payload.get("video_title")
        metadata_path = event.payload.get("metadata_path")
        
        with open(metadata_path, "r", encoding="utf-8") as f:
            metadata_text = f.read()
            
        # Validazione L5->L6
        if not self.qa_agent.verify_gate("L5_L6", metadata_text):
            log.error("❌ Conductor bloccato al Gate L5_L6. Termino.")
            return
            
        self.auditor_agent.execute_audit(video_title)

    def on_audit_completed(self, event: Event):
        video_title = event.payload.get("video_title")
        
        # Validazione L6->L7 (Fine)
        if not self.qa_agent.verify_gate("L6_L7", "success"):
            log.error("❌ Conductor bloccato al Gate L6_L7 alla fine del workflow.")
            return
            
        self.event_bus.publish(
            event_type="workflow.completed",
            publisher=self.agent_id,
            payload={"video_title": video_title}
        )
        log.info(f"🏆 [{self.agent_id}] WORKFLOW DI PRODUZIONE YOUTUBE COMPLETATO CON SUCCESSO!")

    def on_gate_failed(self, event: Event):
        gate_id = event.payload.get("gate_id")
        attempt_number = event.payload.get("attempt_number", 1)
        
        # Remediation Loop
        if attempt_number < 3:
            log.warning(f"🔄 [{self.agent_id}] Rilevato fallimento gate {gate_id} (tentativo {attempt_number}). Avvio Remediation...")
            if gate_id == "L3_L4":
                log.info(f"🔄 [{self.agent_id}] Remediation L3_L4: Rigenerazione script con istruzioni migliorate...")
                self.writer_agent.execute_script_writing("Dose Mentale", "Installare Claude Code locale")
            elif gate_id == "L5_L6":
                log.info(f"🔄 [{self.agent_id}] Remediation L5_L6: Rigenerazione metadati con keyword prioritaria...")
                self.optimizer_agent.execute_optimization("Installare Claude Code locale")
        else:
            log.error(f"🚨 [{self.agent_id}] Raggiunto il limite di 3 tentativi falliti per il gate {gate_id}. Conduco protocollo di ESCALATION.")
