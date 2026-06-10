"""
Script per salvare la sessione di Google Drive in modo che l'automazione possa usarla.
Questo script utilizza lo stesso BrowserManager dell'automazione GoogleDrive, 
quindi tutti i cookie e i dati di login vengono salvati automaticamente.

Istruzioni:
1. Esegui questo script: python GoogleDrive/setup_drive_session.py
2. Fai il login sul tuo Account Google
3. Assicurati che Google Drive sia visibile e funzionante
4. Torna in questo terminale e premi INVIO per chiudere e salvare la sessione.
"""

import sys
import os
import time

root_dir = os.path.dirname(os.path.dirname(__file__))
if root_dir not in sys.path:
    sys.path.append(root_dir)

from Core.browser_manager import BrowserManager

def main():
    print("\n========================================================")
    print("  GOOGLE DRIVE — SETUP SESSIONE (MANUALE)")
    print("========================================================\n")

    # Inizializza il manager in modalità non-headless (visibile)
    manager = BrowserManager('GoogleDrive', headless=False)
    
    try:
        context = manager.get_context()
        page = manager.new_page(context)

        url = "https://drive.google.com/drive/my-drive"
        print(f"[*] Sto aprendo Google Drive: {url}")
        page.goto(url)

        print("\n========================================================")
        print(" AZIONE RICHIESTA:")
        print(" 1. Fai il login sul tuo account Google.")
        print(" 2. Assicurati che si carichi la home di Google Drive ('Il mio Drive').")
        print(" 3. Torna in questo terminale e premi INVIO per chiudere e salvare la sessione.")
        print("========================================================\n")
        
        input(">> Premi INVIO per chiudere e salvare la sessione...\n")

        print("\n[V] Sessione salvata con successo!")
        print(f"[V] I dati di sessione sono stati aggiornati nella cartella GoogleDrive/session_data")

    finally:
        manager.close()

if __name__ == "__main__":
    main()
