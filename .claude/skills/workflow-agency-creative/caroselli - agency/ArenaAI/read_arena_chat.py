import os
import sys
import time

root_dir = os.path.dirname(os.path.dirname(__file__))
if root_dir not in sys.path:
    sys.path.append(root_dir)

import config
from Core.browser_manager import BrowserManager

def main():
    print("[*] Avvio browser per leggere la chat di Arena...")
    manager = BrowserManager('ArenaAI', headless=True)
    
    try:
        context = manager.get_context()
        page = context.new_page()

        chat_url = getattr(config, 'ARENA_CHAT_URL', "https://arena.ai/")
        print(f"[*] Navigazione verso: {chat_url}")
        
        page.goto(chat_url, wait_until="networkidle")
        time.sleep(10) # Aspetta che carichi bene tutta la chat
        
        # Facciamo scorrere la pagina verso l'alto per caricare i messaggi precedenti se necessario
        # (Opzionale, proviamo prima a prendere il testo visibile)
        for _ in range(3):
            page.mouse.wheel(0, -5000)
            time.sleep(2)
        
        # Estrai tutto il testo della pagina
        chat_text = page.evaluate("() => document.body.innerText")
        
        output_file = os.path.join(os.path.dirname(__file__), "arena_chat_history.txt")
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(chat_text)
            
        print(f"[V] Testo della chat estratto e salvato in: {output_file}")

    except Exception as e:
        print(f"[X] Errore durante l'estrazione: {e}")
    finally:
        manager.close()

if __name__ == "__main__":
    main()
