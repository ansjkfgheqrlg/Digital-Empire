import os
import sys
import time

root_dir = os.path.dirname(os.path.abspath(__file__))
if root_dir not in sys.path:
    sys.path.append(root_dir)

from Core.browser_manager import BrowserManager

def test_model_selection():
    print("[*] Avvio BrowserManager per testare Direct + chatgpt medium...")
    manager = BrowserManager('ArenaAI', headless=True)
    
    try:
        context = manager.get_context()
        page = context.new_page()
        
        url = "https://arena.ai/"
        print(f"[*] Navigazione verso: {url}")
        page.goto(url, wait_until="domcontentloaded")
        time.sleep(5)
        
        # 1. Trova ed apre il dropdown Battle Mode
        print("[*] Cerco il dropdown Battle Mode nell'header...")
        visible_btn = None
        for btn in page.locator("button, p, span").all():
            try:
                if btn.is_visible():
                    text = btn.inner_text().strip()
                    if text == "Battle Mode":
                        box = btn.bounding_box()
                        if box and box['width'] > 0 and box['width'] < 300 and box['y'] < 100:
                            visible_btn = btn
                            break
            except:
                pass
                
        if not visible_btn:
            combobox = page.locator("button[role='combobox']").first
            if combobox.is_visible():
                visible_btn = combobox
                
        if visible_btn:
            print("[*] Clicco sul dropdown...")
            visible_btn.click(force=True)
            time.sleep(2)
        else:
            print("[X] Impossibile trovare il dropdown Battle Mode!")
            return
            
        # 2. Clicca su Direct (usando solo role='option' che inizia con Direct)
        print("[*] Cerco l'opzione 'Direct' con role='option'...")
        direct_clicked = False
        for opt in page.locator("[role='option']").all():
            try:
                if opt.is_visible():
                    text = opt.inner_text().strip()
                    if text.startswith("Direct"):
                        print(f"[V] Clicco su option: {text}")
                        opt.click(force=True)
                        direct_clicked = True
                        break
            except:
                pass
                
        if not direct_clicked:
            print("[X] Impossibile cliccare su Direct!")
            return
            
        time.sleep(4)
        
        # Salviamo screenshot per confermare Direct Mode
        page.screenshot(path=os.path.join(root_dir, "arena_direct_mode.png"))
        print("[V] Screenshot Direct Mode salvato!")
        
        # 3. Cerchiamo il model dropdown (è un bottone visibile con il testo "Max" o simile)
        print("\n--- IDENTIFICAZIONE BOTTONE MODELLO ---")
        model_btn = None
        for btn in page.locator("button").all():
            try:
                if btn.is_visible():
                    text = btn.inner_text().strip()
                    # Cerca il bottone che contiene "Max" o che ha un'icona e testo
                    if text == "Max" or "Max" in text:
                        box = btn.bounding_box()
                        if box and box['width'] > 0 and box['y'] < 100:
                            print(f"[V] Trovato bottone modello: Text='{text}', Box={box}")
                            model_btn = btn
                            break
            except:
                pass
                
        if not model_btn:
            # Fallback: se non c'è "Max", prendiamo il secondo combobox
            comboboxes = page.locator("button[role='combobox']").all()
            if len(comboboxes) > 1:
                model_btn = comboboxes[1]
                print(f"[V] Fallback combobox modello: Text='{model_btn.inner_text().strip()}'")

        if model_btn:
            print("[*] Clicco sul dropdown del modello...")
            model_btn.click(force=True)
            time.sleep(2)
            
            # Screenshot delle opzioni del modello
            page.screenshot(path=os.path.join(root_dir, "arena_models_list.png"))
            print("[V] Screenshot lista modelli salvato!")
            
            # Stampiamo le opzioni disponibili
            print("\n--- OPZIONI MODELLO DISPONIBILI ---")
            for idx, opt in enumerate(page.locator("div[role='listbox'] *, div[role='menu'] *, ul *, li, button, [role='option']").all()):
                try:
                    if opt.is_visible():
                        text = opt.inner_text().strip()
                        if text and len(text) < 60:
                            print(f"Opzione {idx}: '{text}'")
                except:
                    pass
                    
            # Clicchiamo su "chatgpt medium"
            print("[*] Cerco 'chatgpt medium'...")
            model_selected = False
            for opt in page.locator("[role='option'], button, span, p").all():
                try:
                    if opt.is_visible():
                        text = opt.inner_text().strip().lower()
                        # Cerchiamo corrispondenza parziale per "chatgpt medium"
                        if "chatgpt medium" in text or "chatgpt-medium" in text or "gpt medium" in text or "chatgpt_medium" in text:
                            print(f"[V] Clicco su opzione modello: '{opt.inner_text().strip()}'")
                            opt.click(force=True)
                            model_selected = True
                            break
                except:
                    pass
            
            if not model_selected:
                print("[X] Modello 'chatgpt medium' non trovato!")
            else:
                time.sleep(2)
        else:
            print("[X] Dropdown modello non trovato!")

            
        # 4. Selezioniamo l'icona dell'immagine in basso
        print("[*] Cerco l'icona dell'immagine in basso...")
        image_btn = page.locator("button[aria-label='Image'], button[title='Image']").first
        if image_btn.is_visible():
            print("[V] Clicco sull'icona Image...")
            image_btn.click(force=True)
            time.sleep(2)
        else:
            # Fallback a data-modality-button
            image_btn2 = page.locator("button[data-modality-button='true']").first
            if image_btn2.is_visible():
                print("[V] Clicco su data-modality-button Image...")
                image_btn2.click(force=True)
                time.sleep(2)
            else:
                print("[X] Icona immagine non trovata!")
                
        # Screenshot finale del setup
        page.screenshot(path=os.path.join(root_dir, "arena_final_setup.png"))
        print("[V] Screenshot setup finale salvato!")

    except Exception as e:
        print(f"[X] Errore: {e}")
    finally:
        manager.close()

if __name__ == "__main__":
    test_model_selection()
