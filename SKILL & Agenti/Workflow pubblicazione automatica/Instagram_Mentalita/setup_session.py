import time
import sys
import os

root_dir = os.path.dirname(os.path.dirname(__file__))
if root_dir not in sys.path:
    sys.path.append(root_dir)

from Core.browser_manager import BrowserManager
from Instagram_Mentalita import config

def run_setup():
    print("\n--- SETUP INSTAGRAM (MENTALITA' BRUTALE) ---")
    print("Si aprirà una finestra del browser. EFFETTUA IL LOGIN MANUALMENTE con mentalita.brutale.")
    print("Dopo aver completato il login, torna qui e premi INVIO.")
    
    manager = BrowserManager('Instagram_Mentalita', headless=False)
    
    try:
        context = manager.get_context()
        page = context.new_page()
        
        page.goto("https://www.instagram.com/")
        
        input("\n[PREMI INVIO QUANDO HAI FATTO IL LOGIN E SEI NELLA HOME PAGE DI MENTALITA.BRUTALE]...")
        
        print("Sessione Instagram salvata con successo in Instagram_Mentalita/session_data/")
        
    except Exception as e:
        print(f"Errore durante il setup: {e}")
    finally:
        manager.close()

if __name__ == "__main__":
    run_setup()
