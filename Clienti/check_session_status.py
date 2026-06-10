import os
import sys
import time

root_dir = r"c:\Users\Utente\Desktop\qui tutto\Digital Empire\SKILL & Agenti\Workflow agency creative\caroselli - agency"
if root_dir not in sys.path:
    sys.path.append(root_dir)

from Core.browser_manager import BrowserManager

def check_platform(name, url):
    print(f"\n==========================================")
    print(f" VERIFICA SESSIONE: {name}")
    print(f"==========================================")
    manager = BrowserManager(name, headless=True)
    try:
        context = manager.get_context()
        page = context.new_page()
        print(f"[*] Navigazione verso {url}...")
        page.goto(url, timeout=45000, wait_until="domcontentloaded")
        time.sleep(6)
        
        current_url = page.url
        title = page.title()
        print(f"[V] URL caricato: {current_url}")
        print(f"[V] Titolo pagina: {title}")
        
        # Salviamo uno screenshot di diagnostica
        screenshot_name = f"check_{name.lower()}.png"
        screenshot_path = os.path.join(root_dir, screenshot_name)
        page.screenshot(path=screenshot_path)
        print(f"[V] Screenshot salvato in: {screenshot_path}")
        
        # Controlliamo la presenza di pulsanti di login comuni
        login_indicators = [
            "button:has-text('Accedi')", "button:has-text('Sign in')", 
            "a:has-text('Accedi')", "a:has-text('Sign in')",
            "input[type='email']", "input[type='password']"
        ]
        
        is_login_page = False
        for ind in login_indicators:
            try:
                el = page.locator(ind).first
                if el.is_visible():
                    print(f"[!] Rilevato elemento di login: {ind}")
                    is_login_page = True
            except:
                pass
                
        if "accounts.google.com" in current_url or "login" in current_url.lower():
            is_login_page = True
            
        if is_login_page:
            print(f"[!] STATO: sessione NON ATTIVA / Richiede Login")
        else:
            print(f"[V] STATO: sessione ATTIVA / Loggato con successo!")
            
    except Exception as e:
        print(f"[X] Errore durante la verifica: {e}")
    finally:
        manager.close()

if __name__ == "__main__":
    # Verifichiamo sia la sessione 'ArenaAI' (che fa sia Arena che Drive upload) sia 'GoogleDrive'
    check_platform('ArenaAI', 'https://arena.ai/')
    check_platform('ArenaAI', 'https://drive.google.com/drive/folders/1XnzZrj3GFovuXqOGnTy03MoK0cc8d9tq')
