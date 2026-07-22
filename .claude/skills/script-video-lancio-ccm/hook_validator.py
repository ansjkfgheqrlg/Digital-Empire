#!/usr/bin/env python3
"""
Hook Validator — Digital Empire / Claude Code Mastery
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Agente 3: L'Inquisitore. Valida gli script generati per assicurarsi
che non contengano termini "guru" e che rispettino le tempistiche 
e il "Self-Check Finale" del Metodo Empire.

Uso:
    python hook_validator.py check_script --file script_output.txt
    python hook_validator.py test
"""

import argparse
import re
import sys
from dataclasses import dataclass
from typing import List, Tuple

sys.stdout.reconfigure(encoding='utf-8')

# Parole vietate assolute (Guru/Introduzioni vuote)
BLACKLIST_WORDS = [
    "ciao", "hey", "in questo video", "oggi vi parlo",
    "sfrutta al massimo", "next level", "potenziale",
    "cambia le regole del gioco", "scopri come", "ragazzi",
    "è fondamentale considerare"
]

@dataclass
class ValidationResult:
    is_valid: bool
    errors: List[str]
    feedback_prompt: str


class HookValidator:
    """Valida i testi degli script secondo il manifesto di Skill.md."""

    def __init__(self):
        self.blacklist = [word.lower() for word in BLACKLIST_WORDS]

    def _extract_hook(self, script_text: str) -> str:
        """Estrae la primissima frase (fino al primo punto, punto interrogativo o a capo)."""
        # Prendiamo la prima riga non vuota
        lines = [l.strip() for l in script_text.split('\n') if l.strip()]
        if not lines:
            return ""
        
        first_line = lines[0]
        # Cerchiamo il primo punto fermo o punto interrogativo
        match = re.split(r'[.?\n]', first_line)
        return match[0].strip() if match else first_line

    def validate_script(self, script_text: str) -> ValidationResult:
        """
        Esegue i controlli formali:
        1. Lunghezza Hook (max 12 parole).
        2. Assenza di Blacklist nel testo generale.
        3. Nessun saluto inziale.
        """
        errors = []
        
        if not script_text.strip():
            return ValidationResult(False, ["Script vuoto."], "Genera uno script valido.")
            
        script_lower = script_text.lower()
        hook = self._extract_hook(script_text)
        
        # 1. Check Hook Length
        words_in_hook = len(hook.split())
        if words_in_hook > 12:
            errors.append(f"Hook troppo lungo ({words_in_hook} parole). Massimo consentito: 12.")
            
        # 2. Check Greetings all'inizio
        for word in ["ciao", "hey", "ragazzi", "in questo video", "oggi"]:
            if script_lower.startswith(word):
                errors.append(f"Apertura vietata: inizia direttamente senza esplorare convenevoli o dire '{word}'.")
                
        # 3. Check Blacklist Terms (Guru-words) ovunque nello script
        for word in self.blacklist:
            if word in script_lower:
                errors.append(f"Termine vietato (guru/fuffa) rilevato: '{word}'")

        # Esito
        is_valid = len(errors) == 0
        
        # Genera un prompt per l'Agente precedente (Claude) se ci sono errori
        feedback_prompt = ""
        if not is_valid:
            feedback_prompt = "Lo script è stato rifiutato per le seguenti violazioni delle linee guida:\n"
            for err in errors:
                feedback_prompt += f"- {err}\n"
            feedback_prompt += "\nRiscrivi lo script risolvendo ESATTAMENTE questi punti. Mantieni alta la specificità tecnica (nomi file, comandi)."
            
        return ValidationResult(
            is_valid=is_valid,
            errors=errors,
            feedback_prompt=feedback_prompt
        )

def run_tests():
    """Effettua test su script dummy per verificare il validatore."""
    validator = HookValidator()
    
    print("--- Test 1: Script Valido Empire Style ---")
    script_1 = "C'è un file che Claude legge automaticamente ad ogni avvio. Si chiama CLAUDE.md ed evita di farti sprecare token."
    r1 = validator.validate_script(script_1)
    print(f"Esito: {'✅ PASSATO' if r1.is_valid else '❌ FALLITO'}")
    
    print("\n--- Test 2: Script Invalido (Guru Words) ---")
    script_2 = "Ciao ragazzi, in questo video ti spiego come sfruttare al massimo il potenziale di Claude."
    r2 = validator.validate_script(script_2)
    print(f"Esito: {'✅ PASSATO' if r2.is_valid else '❌ FALLITO'}")
    for err in r2.errors:
        print(f"  -> {err}")

    print("\n--- Test 3: Hook troppo lungo ---")
    script_3 = "Oggi volevo farti vedere che c'è una funzione che praticamente nessuno usa perché probabilmente nessuno l'ha ancora scoperta in modo accurato. Vai su Google."
    r3 = validator.validate_script(script_3)
    print(f"Esito: {'✅ PASSATO' if r3.is_valid else '❌ FALLITO'}")
    for err in r3.errors:
         print(f"  -> {err}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Hook & Script Validator")
    parser.add_argument("command", choices=["test", "check_script"], help="Comando da eseguire")
    parser.add_argument("--file", help="Path del file di testo dello script da validare")
    
    args = parser.parse_args()
    
    if args.command == "test":
        run_tests()
    elif args.command == "check_script":
        if not args.file:
            print("Errore: specifica un file con --file")
            exit(1)
        try:
            with open(args.file, "r", encoding="utf-8") as f:
                content = f.read()
            validator = HookValidator()
            res = validator.validate_script(content)
            
            if res.is_valid:
                print("✅ SCRIPT APPROVATO. Perfetto per la pubblicazione.")
            else:
                print("❌ SCRIPT RIFIUTATO. Restituisci questo feedback al copywriter:")
                print("---------------------------------------------------------")
                print(res.feedback_prompt)
        except Exception as e:
            print(f"Errore nella lettura del file: {e}")
