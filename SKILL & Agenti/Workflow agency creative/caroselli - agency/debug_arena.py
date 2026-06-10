import os
import sys
import time
import glob

root_dir = os.path.dirname(os.path.abspath(__file__))
if root_dir not in sys.path:
    sys.path.append(root_dir)

from Core.browser_manager import BrowserManager
import config

def debug_flow():
    print("[Debug] Avvio test di ispezione su Arena.ai...")
    manager = BrowserManager('ArenaAI', headless=True)
    
    try:
        context = manager.get_context()
        page = context.new_page()
        
        print("[Debug] Navigazione verso https://arena.ai/...")
        page.goto("https://arena.ai/", timeout=60000, wait_until='domcontentloaded')
        time.sleep(5)
        page.screenshot(path="debug_1_home.png")
        print("[Debug] Screenshot home salvato.")
        
        # Clicca su New Chat
        new_chat_btn = page.locator("a:has-text('New Chat'), button:has-text('New Chat')").first
        if new_chat_btn.is_visible():
            new_chat_btn.click(force=True)
            time.sleep(3)
            
        # Seleziona Direct
        visible_btn = None
        for btn in page.locator("button, p, span").all():
            try:
                if btn.is_visible() and btn.inner_text().strip() == "Battle Mode":
                    visible_btn = btn
                    break
            except: pass
        if visible_btn:
            visible_btn.click(force=True)
            time.sleep(2)
            
        for opt in page.locator("[role='option']").all():
            try:
                if opt.is_visible() and opt.inner_text().strip().startswith("Direct"):
                    opt.click(force=True)
                    break
            except: pass
        time.sleep(4)
        
        # Attiva modalità immagine
        image_btn = page.locator("button[aria-label='Image'], button[title='Image']").first
        if image_btn.is_visible():
            image_btn.click(force=True)
        else:
            image_btn2 = page.locator("button[data-modality-button='true']").first
            if image_btn2.is_visible():
                image_btn2.click(force=True)
        time.sleep(3)
        
        # Seleziona modello gpt-image-2 (medium)
        model_btn = None
        comboboxes = page.locator("button[role='combobox']").all()
        if len(comboboxes) > 1:
            model_btn = comboboxes[1]
        if model_btn:
            model_btn.click(force=True)
            time.sleep(2)
            search_input = page.locator("input[placeholder='Search models']").first
            if search_input.is_visible():
                search_input.fill("gpt-image-2")
                time.sleep(2)
                for opt in page.locator("[role='option']").all():
                    try:
                        if opt.is_visible() and "gpt-image-2 (medium)" in opt.inner_text().strip():
                            opt.click(force=True)
                            break
                    except: pass
        time.sleep(3)
        page.screenshot(path="debug_2_setup_completed.png")
        print("[Debug] Screenshot setup completato.")
        
        # Carica gli allegati
        allegati_files = []
        if os.path.exists(config.ALLEGATI_DIR):
            allegati_files = glob.glob(os.path.join(config.ALLEGATI_DIR, "*.*"))
        if allegati_files:
            print(f"[Debug] Caricamento di {len(allegati_files)} file...")
            page.set_input_files("input[type='file']", allegati_files)
            time.sleep(6)
        
        page.screenshot(path="debug_3_files_uploaded.png")
        print("[Debug] Screenshot file caricati.")
        
        # Log di tutte le immagini pre-esistenti
        print("\n--- IMMAGINI RILEVATE PRIMA DELLA GENERAZIONE ---")
        for idx, img in enumerate(page.locator("img").all()):
            try:
                src = img.get_attribute("src") or ""
                box = img.bounding_box()
                print(f"Img {idx}: src='{src[:60]}', box={box}")
            except Exception as e:
                print(f"Img {idx} errore: {e}")
                
        # Scrivi il prompt e invia
        prompt = "Disegna una slide con scritto 'Il tuo Marketing è un buco nero? Trasformalo in un pozzo d'oro'."
        textarea = page.locator("textarea").first
        textarea.fill(prompt)
        time.sleep(1)
        
        submit_btn = page.locator("button[type='submit']").first
        if submit_btn.is_visible():
            submit_btn.click(force=True)
        else:
            textarea.focus()
            page.keyboard.press("Enter")
        print("[Debug] Prompt inviato. Inizio polling di 80 secondi...")
        
        # Polling con salvataggio screenshot ed elencazione immagini
        for cycle in range(8):
            time.sleep(10)
            cycle_time = (cycle + 1) * 10
            page.screenshot(path=f"debug_4_polling_{cycle_time}s.png")
            print(f"\n--- IMMAGINI RILEVATE A {cycle_time}s ---")
            for idx, img in enumerate(page.locator("img").all()):
                try:
                    src = img.get_attribute("src") or ""
                    box = img.bounding_box()
                    print(f"Img {idx}: src='{src[:60]}', box={box}")
                except Exception as e:
                    print(f"Img {idx} errore: {e}")
                    
    except Exception as err:
        print(f"[Debug] Errore: {err}")
    finally:
        manager.close()
        print("[Debug] Browser chiuso.")

if __name__ == "__main__":
    debug_flow()
