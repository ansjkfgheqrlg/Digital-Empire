import os
import sys
import time

root_dir = os.path.dirname(os.path.abspath(__file__))
if root_dir not in sys.path:
    sys.path.append(root_dir)

from Core.browser_manager import BrowserManager

def test():
    print("[Test] Avvio test gpt-image-2 (medium) senza allegati...")
    manager = BrowserManager('ArenaAI', headless=False)
    
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
                
        # 3. Seleziona gpt-image-2 (medium)
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
            current_model_txt = model_btn.inner_text().strip()
            if "gpt-image-2" in current_model_txt.lower() or "medium" in current_model_txt.lower():
                print("[Test] Modello già gpt-image-2 (medium).")
            else:
                print(f"[Test] Clicco sul dropdown: '{current_model_txt}'")
                model_btn.click(force=True)
                time.sleep(2)
                search = page.locator("input[placeholder='Search models'], input[placeholder*='Search']").first
                search.fill("gpt-image-2")
                time.sleep(2)
                opt = page.locator("div, li, span, button").filter(has_text="gpt-image-2 (medium)").last
                opt.click(force=True)
                time.sleep(3)
            
            # Invia prompt semplice
            textarea = page.locator("textarea").first
            textarea.fill("A beautiful neon green sign that says 'SUCCESS' on a black background, high resolution.")
            time.sleep(1)
            
            submit = page.locator("button[type='submit']").first
            submit.click(force=True)
            print("[Test] Prompt inviato, attendo 60s per vedere se genera...")
            
            for i in range(6):
                time.sleep(10)
                page.screenshot(path=f"test_gpt_image_{i+1}.png")
                print(f"[Test] Screenshot {i+1} salvato (a {(i+1)*10} secondi).")
                
                # Controlliamo se c'è un'immagine caricata
                images = []
                for img in page.locator("img").all():
                    try:
                        box = img.bounding_box()
                        if box and box['width'] >= 130 and box['height'] >= 130:
                            src = img.get_attribute("src") or ""
                            if src and not src.startswith("data:") and "/avatars/" not in src:
                                images.append((img, src))
                    except: pass
                if images:
                    print(f"[Test] [SUCCESS] Trovata immagine generata! src='{images[0][1]}'")
                    break
        else:
            print("[Test] Dropdown modello non trovato!")
            
    except Exception as e:
        print(f"[Test] Errore: {e}")
    finally:
        manager.close()
        print("[Test] Finito.")

if __name__ == "__main__":
    test()
