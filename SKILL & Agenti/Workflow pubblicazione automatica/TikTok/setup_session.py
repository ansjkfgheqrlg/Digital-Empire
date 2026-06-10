import sys
import os

root_dir = os.path.dirname(os.path.dirname(__file__))
if root_dir not in sys.path:
    sys.path.append(root_dir)

from Core.browser_manager import BrowserManager
import config

def setup():
    print(f"\n--- SETUP TIKTOK ---")
    print("Si aprirà una finestra del browser. EFFETTUA IL LOGIN MANUALMENTE.")
    print("Dopo aver completato il login, torna qui e premi INVIO.")
    
    manager = BrowserManager('TikTok', headless=False)
    context = manager.get_context()
    page = context.new_page()
    
    page.goto('https://www.tiktok.com/login')
    
    input("\n[PREMI INVIO QUANDO HAI FATTO IL LOGIN E SEI NELLA HOME PAGE]...")
    
    manager.close()
    print("Sessione TikTok salvata con successo in TikTok/session_data/")

if __name__ == "__main__":
    setup()
