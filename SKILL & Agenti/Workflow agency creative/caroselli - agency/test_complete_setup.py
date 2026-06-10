import os
import sys
import time

root_dir = os.path.dirname(os.path.abspath(__file__))
if root_dir not in sys.path:
    sys.path.append(root_dir)

from Core.browser_manager import BrowserManager

def test_complete_setup():
    print("[*] Avvio BrowserManager per testare la configurazione completa...")
    manager = BrowserManager('ArenaAI', headless=True)
    
    try:
        context = manager.get_context()
        page = context.new_page()
        
        url = "https://arena.ai/"
        print(f"[*] Navigazione verso: {url}")
        page.goto(url, wait_until="domcontentloaded")
        time.sleep(5)
        
        # 1. Forza l'apertura di un Nuovo Chat per sicurezza cliccando "New Chat" sulla sinistra
        print("[*] Clicco su 'New Chat' per iniziare un ciclo pulito...")
        new_chat_btn = page.locator("a:has-text('New Chat'), button:has-text('New Chat')").first
        if new_chat_btn.is_visible():
            new_chat_btn.click(force=True)
            time.sleep(3)
            
        # 2. Clicca Battle Mode e seleziona Direct
        print("[*] Seleziono la modalità Direct...")
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
            
        direct_clicked = False
        for opt in page.locator("[role='option']").all():
            try:
                if opt.is_visible() and opt.inner_text().strip().startswith("Direct"):
                    opt.click(force=True)
                    direct_clicked = True
                    break
            except:
                pass
        if not direct_clicked:
            print("[X] Impossibile selezionare Direct!")
            return
        time.sleep(4)
        
        # 3. Attiva la modalità Immagine in basso
        print("[*] Attivo la modalità Immagine...")
        image_btn = page.locator("button[aria-label='Image'], button[title='Image']").first
        if image_btn.is_visible():
            image_btn.click(force=True)
            time.sleep(3)
        else:
            image_btn2 = page.locator("button[data-modality-button='true']").first
            if image_btn2.is_visible():
                image_btn2.click(force=True)
                time.sleep(3)
                
        # 4. Clicca sul dropdown del modello (che attualmente mostra 'Max' o simile)
        print("[*] Apro il dropdown del modello...")
        model_btn = None
        for btn in page.locator("button").all():
            try:
                if btn.is_visible():
                    text = btn.inner_text().strip()
                    # Cerca il pulsante con 'Max' nell'header
                    box = btn.bounding_box()
                    if box and box['y'] < 100 and ("Max" in text or "gpt-image-2" in text.lower()):
                        model_btn = btn
                        break
            except:
                pass
                
        if not model_btn:
            # Fallback
            comboboxes = page.locator("button[role='combobox']").all()
            if len(comboboxes) > 1:
                model_btn = comboboxes[1]
                
        if model_btn:
            print(f"[V] Clicco sul dropdown: '{model_btn.inner_text().strip()}'")
            model_btn.click(force=True)
            time.sleep(2)
            
            # Cerca e digita 'gpt-image-2'
            search_input = page.locator("input[placeholder='Search models']").first
            if search_input.is_visible():
                print("[V] Digito 'gpt-image-2' nella barra di ricerca del modello...")
                search_input.fill("gpt-image-2")
                time.sleep(2)
                
                # Clicca sull'opzione 'gpt-image-2 (medium)'
                model_selected = False
                for opt in page.locator("[role='option']").all():
                    try:
                        if opt.is_visible():
                            text = opt.inner_text().strip()
                            if "gpt-image-2 (medium)" in text:
                                print(f"[V] Seleziono il modello: '{text}'")
                                opt.click(force=True)
                                model_selected = True
                                break
                    except:
                        pass
                if model_selected:
                    time.sleep(3)
                    print("[V] Setup completato con successo!")
                else:
                    print("[X] Modello 'gpt-image-2 (medium)' non trovato nei risultati di ricerca!")
            else:
                print("[X] Input di ricerca non visibile!")
        else:
            print("[X] Dropdown modello non trovato!")
            
        page.screenshot(path=os.path.join(root_dir, "arena_setup_success.png"))
        print("[V] Screenshot salvato in 'arena_setup_success.png'")
        
    except Exception as e:
        print(f"[X] Errore: {e}")
    finally:
        manager.close()

if __name__ == "__main__":
    test_complete_setup()
