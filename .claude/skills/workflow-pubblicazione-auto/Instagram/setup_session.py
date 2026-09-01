import sys
import os

# Aggiungi il percorso root al sys.path
root_dir = os.path.dirname(os.path.dirname(__file__))
if root_dir not in sys.path:
    sys.path.append(root_dir)

from Core.browser_manager import BrowserManager
import config

def setup():
    print(f"\n--- SETUP INSTAGRAM ---")
    print("Si aprirà una finestra del browser. EFFETTUA IL LOGIN MANUALMENTE.")
    print("Dopo aver completato il login, torna qui e premi INVIO.")
    
    manager = BrowserManager('Instagram', headless=False)
    context = manager.get_context()
    page = context.new_page()
    
    # Se abbiamo configurato email e password, potremmo usarle qui,
    # ma il login manuale la prima volta evita i captcha.
    page.goto('https://www.instagram.com/')
    
    input("\n[PREMI INVIO QUANDO HAI FATTO IL LOGIN E SEI NELLA HOME PAGE]...")
    
    manager.close()
    print("Sessione Instagram salvata con successo in Instagram/session_data/")

if __name__ == "__main__":
    setup()
