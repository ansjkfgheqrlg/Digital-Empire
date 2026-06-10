#!/usr/bin/env python3
"""
Orchestrator — Digital Empire / Claude Code Mastery
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Direttore d'orchestra per il Workflow Multi-Agente di Lancio CCM.
Usa l'intelligenza artificiale (mock o API vere) per creare 10 script
dalla fase di strategia, scrittura, validazione (loop fino a perfezione),
fino alla stesura delle caption social.

Uso:
    python orchestrator.py genera --quantita 2 --mode mock
"""

import sys
import os
import json
import argparse
from pathlib import Path
from datetime import datetime

# Importo il Validatore Spietato (Agente 3)
from hook_validator import HookValidator, ValidationResult

sys.stdout.reconfigure(encoding='utf-8')

# ═══════════════════════════════════════════════════════════════
# CLASSI AGENTI IA
# ═══════════════════════════════════════════════════════════════

class AIAgentBase:
    """Classe base per chiamate LLM. Supporta modalità MOCK per testing."""
    def __init__(self, mode="mock", api_key=None, provider="openai"):
        self.mode = mode
        self.api_key = api_key or os.getenv("LLM_API_KEY")
        self.provider = provider

    def ask(self, system_prompt: str, user_prompt: str) -> str:
        """Esegue la chiamata all'AI vera o restituisce stringa mock."""
        if self.mode == "mock":
            return self._mock_response(user_prompt)
        else:
            return self._real_api_call(system_prompt, user_prompt)

    def _real_api_call(self, system_prompt: str, user_prompt: str) -> str:
        # Qui potrai implementare le chiamate Anthropic o OpenAI vere
        # richiedendo il client corrispondente
        if not self.api_key:
            return "[Errore: API_KEY non impostata. Ritorno al Mock]\n" + self._mock_response(user_prompt)
        
        # Semplice skeleton per far capire all'utente dove inserire la logica
        return "[LLM OUTPUT REALE NON ANCORA IMPLEMENTATO - MOCK FALLBACK]\n"

    def _mock_response(self, user_prompt: str) -> str:
        pass


class Agente1_Strategist(AIAgentBase):
    """Genera lo scheletro dell'argomento e angolazione."""
    def _mock_response(self, user_prompt: str) -> str:
        return json.dumps({
            "argomento": "Il CLAUDE.md file per non ripetere prompt",
            "angolo": "L'errore comune che ti fa perdere 2 ore a settimana",
            "hook_suggerito": "Affermazione Shock",
            "durata_stimata": "45 secondi"
        })

class Agente2_Copywriter(AIAgentBase):
    """Scrive lo script materiale basato su Skill.md."""
    def _mock_response(self, user_prompt: str) -> str:
        if "Riscrivi lo script" in user_prompt:
            return "C'è un file che Claude legge in automatico. Serve per non ripeterti. Si chiama CLAUDE.md ed è la fine del copia-incolla."
        else:
            # Ritorna volontariamente uno script CON ERRORI per far intervenire il validatore
            return "Ciao ragazzi, oggi vi parlo del potenziale di Claude e di come cambia le regole del gioco. Create il file skill.md."

class Agente4_SocialManager(AIAgentBase):
    """Crea la formattazione social e caption."""
    def _mock_response(self, user_prompt: str) -> str:
        return "🔥 Il file misterioso di Claude\n\nTi faccio vedere come smettere di sprecare token.\n#ClaudeCode #AI #DigitalEmpire"


# ═══════════════════════════════════════════════════════════════
# MOTORE CENTRALE: ORCHESTRATOR
# ═══════════════════════════════════════════════════════════════

class Orchestrator:
    def __init__(self, mode="mock", max_retries=3):
        self.mode = mode
        self.max_retries = max_retries
        
        print(f"🔧 Inizializzazione Orchestratore Multi-Agente [{str.upper(self.mode)} MODE]")
        self.agente_strategist = Agente1_Strategist(mode=self.mode)
        self.agente_copywriter = Agente2_Copywriter(mode=self.mode)
        self.validator = HookValidator()
        self.agente_social = Agente4_SocialManager(mode=self.mode)

        self._load_knowledge()

    def _load_knowledge(self):
        """Carica il Mega Prompt e le conoscenze (Skill.md, ecc.)"""
        self.skill_md_content = ""
        try:
            with open("Skill.md", "r", encoding="utf-8") as f:
                self.skill_md_content = f.read()
        except FileNotFoundError:
            print("⚠️ Errore: 'Skill.md' non trovato. Assicurati di essere nella cartella corretta.")

    def run_pipeline(self, num_scripts: int):
        print(f"\n🚀 Avvio pipeline per la creazione di {num_scripts} script performanti.")
        
        output_dir = Path("output_scripts")
        output_dir.mkdir(exist_ok=True)
        file_out_path = output_dir / f"batch_scripts_{datetime.now().strftime('%Y-%m-%d_%H%M')}.md"
        
        final_scripts_compilati = []

        for i in range(1, num_scripts + 1):
            print(f"\n" + "="*50)
            print(f"🎬 SCRIPT {i}/{num_scripts} IN LAVORAZIONE")
            print("="*50)

            # --- AGENTE 1: STRATEGIA ---
            print("[Agente 1] 🧠 Content Strategist: Elaborazione scheletro...")
            prompt_strat = "Genera un nuovo argomento tecnico AI che non abbiamo ancora coperto."
            skeleton_json = self.agente_strategist.ask(system_prompt="Sei lo strategist.", user_prompt=prompt_strat)
            
            try:
                scheletro = json.loads(skeleton_json)
                print(f"   > Argomento scelto: {scheletro['argomento']}")
            except:
                print("   > Errore decodifica strategia, proseguimento in safe-mode.")

            # --- AGENTE 2 + AGENTE 3: SCRITTURA E VALIDAZIONE (LOOP) ---
            print("[Agente 2] ✍️ Copywriter Elite: Stesura bozza...")
            prompt_copy = f"Crea lo script per questo: {skeleton_json}"
            bozza_corrente = self.agente_copywriter.ask(system_prompt=self.skill_md_content, user_prompt=prompt_copy)
            
            tentativo = 1
            script_approvato = False

            while tentativo <= self.max_retries and not script_approvato:
                print(f"[Agente 3] 🕵️ Validatore: Analisi tentativo {tentativo}...")
                validazione = self.validator.validate_script(bozza_corrente)
                
                if validazione.is_valid:
                    print("   > ✅ Script PERFETTO. Nessuna violazione trovata.")
                    script_approvato = True
                else:
                    print("   > ❌ Violazioni trovate. Rigetto lo script all'Agente 2.")
                    for err in validazione.errors:
                        print(f"     - {err}")
                    
                    # Feedback Loop: Ritorno all'Agente 2
                    if tentativo < self.max_retries:
                        print("   > ✍️ Copywriter: Riscrivo basandomi sul feedback dell'inquisitore...")
                        full_feedback_prompt = prompt_copy + "\n\n" + validazione.feedback_prompt
                        bozza_corrente = self.agente_copywriter.ask(system_prompt=self.skill_md_content, user_prompt=full_feedback_prompt)
                    else:
                        print("   > ⚠️ Limite massimo di tentativi raggiunto. Trovato compromesso accettabile.")
                tentativo += 1

            # --- AGENTE 4: SOCIAL ---
            print("[Agente 4] 📱 Social Manager: Confezionamento e Caption...")
            testo_finale = bozza_corrente
            caption = self.agente_social.ask(system_prompt="", user_prompt=f"Crea la caption per questo script:\n{testo_finale}")

            # Salvataggio nel documento cumulativo
            script_assemblato = f"""## Script #{i}
**Strategia:** {json.loads(skeleton_json).get('argomento', 'N/A')}

### Lo Script Base (da recitare):
{testo_finale}

### Caption (da incollare):
{caption}

---
"""
            final_scripts_compilati.append(script_assemblato)

        # Scrittura su file
        with open(file_out_path, "w", encoding="utf-8") as out_file:
            out_file.write("# BATCH SCRIPT ELITE OUTPUT\n\n")
            out_file.writelines(final_scripts_compilati)

        print("\n" + "🌟"*25)
        print(f"🎉 PIPELINE COMPLETATA! Cerca i file in: {file_out_path}")
        print("🌟"*25)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Orchestrator Workflow CCM")
    parser.add_argument("comando", choices=["genera"], help="Comando eseguire")
    parser.add_argument("--quantita", type=int, default=1, help="Numero di script da generare")
    parser.add_argument("--mode", choices=["mock", "api"], default="mock", help="Modalità di connessione all'LLM (mock = simulato locale senza wifi/api)")
    
    args = parser.parse_args()

    if args.comando == "genera":
        orchestrator = Orchestrator(mode=args.mode)
        orchestrator.run_pipeline(args.quantita)
