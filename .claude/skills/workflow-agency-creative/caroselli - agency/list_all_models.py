import os
import sys
import time

root_dir = os.path.dirname(os.path.abspath(__file__))
if root_dir not in sys.path:
    sys.path.append(root_dir)

from Core.browser_manager import BrowserManager

def list_models():
    print("[*] Avvio BrowserManager per elencare tutti i modelli...")
    manager = BrowserManager('ArenaAI', headless=True)
    
    try:
        context = manager.get_context()
        page = context.new_page()
        
        page.goto("https://arena.ai/", timeout=60000, wait_until='domcontentloaded')
        time.sleep(5)
        
        new_chat_btn = page.locator("a:has-text('New Chat'), button:has-text('New Chat')").first
        if new_chat_btn.is_visible():
            new_chat_btn.click(force=True)
            time.sleep(3)
            
        # Imposta Direct
        menu_trigger = page.locator("button, p, span").filter(has_text="Battle Mode").first
        if menu_trigger.is_visible():
            menu_trigger.click(force=True)
            time.sleep(2)
            direct_opt = page.locator("*:has-text('Chat with 1 model at a time')").last
            direct_opt.click(force=True)
            time.sleep(3)
            
        # Modalità Immagine
        img_btn = page.locator("button[aria-label='Image'], button[title='Image']").first
        if img_btn.is_visible():
            img_btn.click(force=True)
            time.sleep(3)
            
        # Clicca dropdown del modello
        model_btn = None
        for btn in page.locator("button").all():
            try:
                if btn.is_visible():
                    text = btn.inner_text().strip()
                    box = btn.bounding_box()
                    if box and box['y'] < 100 and ("gpt-image" in text.lower() or "medium" in text.lower() or "Max" in text or "chatgpt" in text.lower()):
                        model_btn = btn
                        break
            except: pass
            
        if not model_btn:
            comboboxes = page.locator("button[role='combobox']").all()
            if len(comboboxes) > 1:
                model_btn = comboboxes[1]
                
        if model_btn:
            print(f"[V] Clicco sul dropdown del modello: '{model_btn.inner_text().strip()}'")
            model_btn.click(force=True)
            time.sleep(3)
            
            print("\n--- MODELLI DISPONIBILI ---")
            options = page.locator("div, li, span, button").all()
            found_any = False
            for opt in options:
                try:
                    if opt.is_visible():
                        txt = opt.inner_text().strip()
                        # Stampiamo solo elementi che sembrano nomi di modelli (es. contengono parole chiave o sono corti)
                        if txt and len(txt) < 60 and ("image" in txt.lower() or "flux" in txt.lower() or "dall" in txt.lower() or "midjourney" in txt.lower() or "recraft" in txt.lower() or "stable" in txt.lower() or "gpt" in txt.lower() or "llama" in txt.lower() or "gemini" in txt.lower()):
                            print(f"  Modello: '{txt}'")
                            found_any = True
                except: pass
            if not found_any:
                print("Nessun modello trovato o dropdown vuoto!")
        else:
            print("Dropdown del modello non trovato!")
            
    except Exception as e:
        print(f"Errore: {e}")
    finally:
        manager.close()

if __name__ == "__main__":
    list_models()
