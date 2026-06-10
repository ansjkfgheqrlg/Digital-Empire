"""
Script per salvare la sessione di Arena.ai in modo che l'automazione possa usarla.
Questo script utilizza lo stesso BrowserManager dell'automazione, 
quindi tutti i cookie e i dati di login vengono salvati automaticamente.

Istruzioni:
1. Esegui questo script
2. Fai il login ad Arena.ai
3. Vai NELLA CHAT CORRETTA
4. Torna qui e premi INVIO per chiudere e salvare.
"""

import sys
import os
import time

root_dir = os.path.dirname(os.path.dirname(__file__))
if root_dir not in sys.path:
    sys.path.append(root_dir)

import config
from Core.browser_manager import BrowserManager

def main():
    print("\n========================================================")
    print("  ARENA AI — SETUP SESSIONE (MANUALE)")
    print("========================================================\n")

    # Inizializza il manager in modalità non-headless
    manager = BrowserManager('ArenaAI', headless=False)
    
    try:
        context = manager.get_context()
        page = manager.new_page(context)

        chat_url = getattr(config, 'ARENA_CHAT_URL', "https://arena.ai/")
        print(f"[*] Sto aprendo il link della chat: {chat_url}")
        
        page.goto(chat_url)

        print("\n========================================================")
        print(" AZIONE RICHIESTA:")
        print(" 1. Fai il login se non sei ancora loggato.")
        print(" 2. Assicurati di essere DENTRO LA CHAT CORRETTA in cui l'AI deve scrivere.")
        print(" 3. Se non sei nella chat corretta, naviga fino ad essa.")
        print(" 4. QUANDO SEI NELLA CHAT CORRETTA, torna in questo terminale e premi INVIO.")
        print("========================================================\n")
        
        input(">> Premi INVIO per chiudere e salvare la sessione...\n")

        print("\n[V] Sessione salvata con successo!")
        print(f"[V] I dati di sessione sono stati aggiornati nella cartella ArenaAI/session_data")

    finally:
        manager.close()

if __name__ == "__main__":
    main()
