import time
import os
from browser_manager import BrowserManager

def setup_platform(platform_name, url):
    print(f"\n--- SETUP {platform_name.upper()} ---")
    print(f"Si aprirà una finestra del browser su {url}.")
    print("EFFETTUA IL LOGIN MANUALMENTE.")
    print("Dopo aver completato il login e salvato le credenziali, torna qui e premi INVIO.")
    
    # Per il setup, usiamo headless=False in modo che l'utente veda il browser
    manager = BrowserManager(headless=False)
    context = manager.get_context(platform_name)
    page = context.new_page()
    
    page.goto(url)
    
    # Aspetta l'input dell'utente nella console
    input("\n[PREMI INVIO QUANDO HAI FATTO IL LOGIN E SEI NELLA HOME PAGE]...")
    
    manager.close()
    print(f"Sessione per {platform_name} salvata con successo!")

if __name__ == "__main__":
    print("=== TOOL DI SETUP SESSIONI SOCIAL ===")
    print("Questo tool serve a salvare i cookie per non dover fare login ogni volta.")
    
    # Instagram Setup
    setup_platform('instagram', 'https://www.instagram.com/')
    
    # TikTok Setup
    setup_platform('tiktok', 'https://www.tiktok.com/login')
    
    print("\nTutte le sessioni sono state configurate. Ora puoi usare gli script di pubblicazione in modalità invisibile!")
