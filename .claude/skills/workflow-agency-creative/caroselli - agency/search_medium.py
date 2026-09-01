import os
import sys
import time

root_dir = os.path.dirname(os.path.abspath(__file__))
if root_dir not in sys.path:
    sys.path.append(root_dir)

from Core.browser_manager import BrowserManager

def search_medium():
    print("[*] Avvio BrowserManager per cercare modelli 'medium' in modalità Image...")
    manager = BrowserManager('ArenaAI', headless=True)
    
    try:
        context = manager.get_context()
        page = context.new_page()
        
        url = "https://arena.ai/"
        page.goto(url, wait_until="domcontentloaded")
        time.sleep(5)
        
        # 1. Clicca Battle Mode ed seleziona Direct
        visible_btn = None
        for btn in page.locator("button, p, span").all():
            try:
                if btn.is_visible():
                    text = btn.inner_text().strip()
                    if text == "Battle Mode":
                        visible_btn = btn
                        break
            except:
                pass
        if visible_btn:
            visible_btn.click(force=True)
            time.sleep(2)
            
        for opt in page.locator("[role='option']").all():
            try:
                if opt.is_visible() and opt.inner_text().strip().startswith("Direct"):
                    opt.click(force=True)
                    break
            except:
                pass
        time.sleep(4)
        
        # 2. Clicca sull'icona Image in basso PRIMA di selezionare il modello
        image_btn = page.locator("button[aria-label='Image'], button[title='Image']").first
        if image_btn.is_visible():
            image_btn.click(force=True)
            time.sleep(3)
        else:
            image_btn2 = page.locator("button[data-modality-button='true']").first
            if image_btn2.is_visible():
                image_btn2.click(force=True)
                time.sleep(3)
                
        # 3. Clicca sul dropdown del modello
        model_btn = None
        for btn in page.locator("button").all():
            try:
                if btn.is_visible():
                    text = btn.inner_text().strip()
                    if text == "Max" or "Max" in text:
                        model_btn = btn
                        break
            except:
                pass
                
        if not model_btn:
            comboboxes = page.locator("button[role='combobox']").all()
            if len(comboboxes) > 1:
                model_btn = comboboxes[1]
                
        if model_btn:
            model_btn.click(force=True)
            time.sleep(2)
            
            # Digita "medium" nell'input di ricerca
            search_input = page.locator("input[placeholder='Search models']").first
            if search_input.is_visible():
                search_input.fill("medium")
                time.sleep(2)
                
                print("\n--- RISULTATI DELLA RICERCA PER 'medium' (IMAGE) ---")
                for opt in page.locator("[role='option']").all():
                    try:
                        if opt.is_visible():
                            print(f"  Trovato: '{opt.inner_text().strip()}'")
                    except:
                        pass
                        
                # Proviamo anche con "chatgpt" per vedere tutti i modelli chatgpt in modalità Image
                search_input.fill("")
                time.sleep(0.5)
                search_input.fill("chatgpt")
                time.sleep(2)
                
                print("\n--- RISULTATI DELLA RICERCA PER 'chatgpt' (IMAGE) ---")
                for opt in page.locator("[role='option']").all():
                    try:
                        if opt.is_visible():
                            print(f"  Trovato: '{opt.inner_text().strip()}'")
                    except:
                        pass
    except Exception as e:
        print(f"Errore: {e}")
    finally:
        manager.close()

if __name__ == "__main__":
    search_medium()
