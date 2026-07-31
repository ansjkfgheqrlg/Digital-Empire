# -*- coding: utf-8 -*-
"""
Owner: GAEL · Controllore: A2-QA · Origine: FORGE
Governo: APEX-7 YouTube E2E Swarm Runner (Plan 7)

⚠️ DEPRECATO (TASK-YT-005, 2026-07-29). Questo runner usa il Conductor MOCK (agents.py) e
scriveva la dashboard canonica con 6 fasi SEMPRE 🟢 PASS sul canale fisso "Dose Mentale",
scollegato dalle fasi reali F1-F6. La dashboard canonica è ora scritta da
`Apex7Orchestrator.write_dashboard()` (apex7_orchestrator.py) dai dati REALI della run.
Per non clobberare più la dashboard vera, qui scriviamo su un file *-LEGACY.md e stampiamo
un avviso. Non è stato cancellato (vincolo additivo): resta come simulazione swarm storica.
Run reale: `python apex7_orchestrator.py run --phase 6`.
"""
from __future__ import annotations

import logging
import os
import sys
from datetime import datetime

# Forza stdout e stderr in utf-8 su Windows per prevenire errori cp1252. reconfigure() e non un
# nuovo io.TextIOWrapper: quest'ultimo blocca l'output su file (buffering a blocchi) e, se un
# altro modulo dello stesso processo fa lo stesso, chiude il buffer condiviso al garbage
# collection ("I/O operation on closed file"). Bug reali trovati il 2026-07-30.
if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)
    sys.stderr.reconfigure(encoding="utf-8", line_buffering=True)

# Aggiungi cartella script a sys.path
SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, SCRIPT_DIR)

from event_bus import EventBus
from memory import MemoryQueryInterface
from gate_agent import GateAgent
from agents import Conductor
from meta_agent import MetaAgent

# Configurazione logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)
log = logging.getLogger("preventa-pw.runner")

def run_e2e_swarm():
    log.warning("⚠️ [DEPRECATO] Simulazione MOCK (Conductor). La dashboard canonica reale è scritta "
                "da Apex7Orchestrator.write_dashboard(). Qui scrivo solo un file *-LEGACY.md.")
    log.info("🎬 [APEX-7 Swarm Runner] Avvio della simulazione E2E per il canale Dose Mentale...")
    
    # Inizializzazione componenti
    run_id = f"yt-run-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
    memory = MemoryQueryInterface(run_id=run_id)
    event_bus = EventBus()
    qa_agent = GateAgent(event_bus, memory)
    
    # Inizializzazione Conductor
    conductor = Conductor(event_bus, memory, qa_agent)
    
    # Avvio workflow sulla nicchia Dose Mentale
    conductor.start_workflow("Dose Mentale")
    
    # Ottimizzazione tramite Meta-Agent
    meta = MetaAgent(memory)
    meta_res = meta.analyze_and_optimize()
    log.info(f"🧠 [Meta-Agent] Ottimizzazione completata: {meta_res}")
    
    # DEPRECATO: scriviamo su un file *-LEGACY.md per NON sovrascrivere la dashboard canonica reale.
    dashboard_path = os.path.join(os.path.dirname(SCRIPT_DIR), "06-DASHBOARD-E-METRICHE", "YOUTUBE-PERFORMANCE-DASHBOARD-LEGACY.md")
    os.makedirs(os.path.dirname(dashboard_path), exist_ok=True)
    
    with open(dashboard_path, "w", encoding="utf-8") as f:
        f.write("# YouTube Automation Factory - Performance Dashboard\n\n")
        f.write(f"- **Ultimo Run ID**: {run_id}\n")
        f.write(f"- **Data Aggiornamento**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("- **Canale Target**: Dose Mentale ([@dosementale](https://www.youtube.com/@dosementale))\n")
        f.write("- **Stato Fabbrica**: 🟢 OPERATIVA / APEX-7 COMPLIANT\n\n")
        
        f.write("## 📊 Metriche di Esecuzione\n")
        f.write("| Fase | Componente | Stato | Esito Gate | Criterio |\n")
        f.write("|---|---|---|---|---|\n")
        f.write("| F1 | Scouting | Completato | 🟢 PASS | Potenziale Nicchia |\n")
        f.write("| F2 | Selezione | Completato | 🟢 PASS | views/ora > 25 |\n")
        f.write("| F3 | Script | Completato | 🟢 PASS | HOOK/CORPO/CTA |\n")
        f.write("| F4 | Produzione | Completato | 🟢 PASS | Fliki Spec Valid |\n")
        f.write("| F5 | Pubblicazione | Completato | 🟢 PASS | SEO score >= 70 |\n")
        f.write("| F6 | Audit | Completato | 🟢 PASS | Auto-Miglioramento |\n\n")
        
        f.write("## 🧠 Regole Apprese & Ottimizzazioni (Meta-Agent)\n")
        f.write(f"- **Colli di Bottiglia Rilevati**: {meta_res.get('gate_bottlenecks', {})}\n")
        f.write(f"- **Strategie Ottimizzate**: {meta_res.get('strategies_updated', 0)} aggiornate in `strategy_store.json`\n")
        f.write("- **Stato Regole**: 🛡️ Blacklist e soglie caricate dinamicamente in `learned_rules.json`.\n")

    log.info(f"🏆 [Runner] Dashboard creata con successo in {dashboard_path}")
    print("\n✅ RUN E2E COMPLETATO CON SUCCESSO! Dashboard generata.")

if __name__ == "__main__":
    run_e2e_swarm()
