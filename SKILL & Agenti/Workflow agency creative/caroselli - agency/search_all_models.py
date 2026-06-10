import os
import sys
import time

root_dir = os.path.dirname(os.path.abspath(__file__))
if root_dir not in sys.path:
    sys.path.append(root_dir)

from Core.browser_manager import BrowserManager

def search_models():
    print("[*] Avvio BrowserManager per cercare modelli...")
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
            
        # 1. Seleziona Direct
        menu_trigger = None
        for btn in page.locator("button, p, span").all():
            try:
                if btn.is_visible():
                    text = btn.inner_text().strip()
                    if text in ["Battle Mode", "Side by Side", "Direct"]:
                        menu_trigger = btn
                        break
            except: pass
            
        if menu_trigger:
            current_mode = menu_trigger.inner_text().strip()
            if current_mode != "Direct":
                menu_trigger.click(force=True)
                time.sleep(2)
                direct_option = page.locator("*:has-text('Chat with 1 model at a time')").last
                direct_option.click(force=True)
                time.sleep(4)
                
        # 2. Modalità Immagine
        image_btn = page.locator("button[aria-label='Image'], button[title='Image']").first
        if image_btn.is_visible():
            image_btn.click(force=True)
            time.sleep(3)
        else:
            image_btn2 = page.locator("button[data-modality-button='true']").first
            if image_btn2.is_visible():
                image_btn2.click(force=True)
                time.sleep(3)
                
        # 3. Trova il dropdown del modello
        model_btn = None
        for btn in page.locator("button").all():
            try:
                if btn.is_visible():
                    text = btn.inner_text().strip()
                    box = btn.bounding_box()
                    if box and box['y'] < 100 and ("Max" in text or "gpt-image-2" in text.lower() or "medium" in text.lower() or "chatgpt" in text.lower()):
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
            
            # Stampa tutti gli elementi del menu
            print("\n--- TUTTE LE OPZIONI DEL POPUP ---")
            options = page.locator("div, li, span, button").all()
            for opt in options:
                try:
                    if opt.is_visible():
                        txt = opt.inner_text().strip()
                        if txt and len(txt) < 80 and not txt.startswith("Add files"):
                            # Filtriamo le scritte irrilevanti
                            if any(x in txt.lower() for x in ["gpt", "flux", "dall", "llama", "gemini", "claude", "stable", "recraft", "fast", "medium", "slow"]):
                                print(f"  Opzione: '{txt}'")
                except: pass
        else:
            print("[X] Dropdown modello non trovato!")
            
    except Exception as e:
        print(f"Errore: {e}")
    finally:
        manager.close()

if __name__ == "__main__":
    search_models()
