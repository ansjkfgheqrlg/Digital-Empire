import os
import sys
import time
import glob

root_dir = os.path.dirname(os.path.abspath(__file__))
if root_dir not in sys.path:
    sys.path.append(root_dir)

from Core.browser_manager import BrowserManager
import config

def test_generation_live():
    print("[*] Avvio BrowserManager per test di generazione live...")
    manager = BrowserManager('ArenaAI', headless=True)
    
    try:
        context = manager.get_context()
        page = context.new_page()
        
        url = "https://arena.ai/"
        page.goto(url, wait_until="domcontentloaded")
        time.sleep(5)
        
        # 1. Setup completo
        visible_btn = None
        for btn in page.locator("button, p, span").all():
            try:
                if btn.is_visible() and btn.inner_text().strip() == "Battle Mode":
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
        
        # Attiva Image Modality
        image_btn = page.locator("button[aria-label='Image'], button[title='Image']").first
        if image_btn.is_visible():
            image_btn.click(force=True)
            time.sleep(3)
            
        # Seleziona gpt-image-2 (medium)
        print("[*] Cerco il dropdown del modello...")
        page.locator("button[role='combobox']").first.click()
        time.sleep(1)
        search_input = page.locator("input[placeholder='Search models']").first
        search_input.fill("gpt-image-2")
        time.sleep(2)
        
        option = page.locator("[role='option']").first
        if option.is_visible():
            option.click(force=True)
            print("[V] Selezionato modello gpt-image-2 (medium)")
        time.sleep(3)
        
        # 2. Carica gli allegati
        allegati_files = glob.glob(os.path.join(config.ALLEGATI_DIR, "*.*"))
        print(f"[V] Trovati {len(allegati_files)} file da caricare: {allegati_files}")
        
        with page.expect_file_chooser(timeout=5000) as fc_info:
            add_files_btn = page.locator("button:has-text('Add files'), button[aria-label='Add files and more']").first
            if add_files_btn.is_visible():
                add_files_btn.click(force=True)
            else:
                page.locator("input[type='file']").first.click(force=True)
        fc_info.value.set_files(allegati_files[:3])
        print("[V] Allegati caricati!")
        time.sleep(6)
        
        # 3. Compila e invia il messaggio
        prompt = "Disegna una splendida slide in formato carosello con scritto: 'Clienti persi? Il tuo funnel attuale non converte.'"
        textarea = page.locator("textarea").first
        textarea.fill(prompt)
        time.sleep(1)
        
        submit_btn = page.locator("button[type='submit']").first
        if submit_btn.is_visible():
            print("[*] Clicco su submit...")
            submit_btn.click(force=True)
        else:
            print("[*] Provo tasto Enter...")
            page.keyboard.press("Enter")
            
        # 4. Monitoriamo e scattiamo screenshot ogni 15 secondi per 3 minuti
        print("\n--- MONITORAGGIO GENERAZIONE ---")
        for i in range(12):
            time.sleep(15)
            screenshot_path = os.path.join(root_dir, f"generation_step_{i+1}.png")
            page.screenshot(path=screenshot_path)
            
            # Conta le immagini presenti
            imgs = page.locator("img").all()
            large_imgs = []
            for img in imgs:
                try:
                    box = img.bounding_box()
                    if box and box['width'] > 100:
                        large_imgs.append(img)
                except:
                    pass
            print(f"Step {i+1} ({(i+1)*15}s): Trovate {len(imgs)} immagini totali, {len(large_imgs)} grandi. Screenshot salvato.")
            
    except Exception as e:
        print(f"[X] Errore: {e}")
    finally:
        manager.close()

if __name__ == "__main__":
    test_generation_live()
