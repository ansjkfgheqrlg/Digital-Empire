import os
import sys
import time

root_dir = os.path.dirname(os.path.abspath(__file__))
if root_dir not in sys.path:
    sys.path.append(root_dir)

from Core.browser_manager import BrowserManager

def test_image_models():
    print("[*] Avvio BrowserManager per testare i modelli in modalità Image...")
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
        print("[*] Clicco sull'icona Image per passare in modalità Immagine...")
        image_btn = page.locator("button[aria-label='Image'], button[title='Image']").first
        if image_btn.is_visible():
            image_btn.click(force=True)
            time.sleep(3)
        else:
            image_btn2 = page.locator("button[data-modality-button='true']").first
            if image_btn2.is_visible():
                image_btn2.click(force=True)
                time.sleep(3)
                
        # 3. Ora clicchiamo sul dropdown del modello (che potrebbe essere cambiato)
        print("[*] Cerco il dropdown del modello in modalità Image...")
        model_btn = None
        for btn in page.locator("button").all():
            try:
                if btn.is_visible():
                    text = btn.inner_text().strip()
                    # Stampa tutti i bottoni visibili nell'header per capire cosa contiene
                    box = btn.bounding_box()
                    if box and box['y'] < 100:
                        print(f"Header Button: Text='{text}', Box={box}")
                        if text == "Max" or "Max" in text or "flux" in text.lower() or "dall" in text.lower() or "gpt" in text.lower():
                            model_btn = btn
            except:
                pass
                
        if not model_btn:
            # Fallback al secondo combobox
            comboboxes = page.locator("button[role='combobox']").all()
            if len(comboboxes) > 1:
                model_btn = comboboxes[1]
                
        if model_btn:
            print(f"[V] Clicco sul dropdown del modello in modalità Image: '{model_btn.inner_text().strip()}'")
            model_btn.click(force=True)
            time.sleep(2)
            
            # Digita "chatgpt medium" nell'input di ricerca se presente
            search_input = page.locator("input[placeholder='Search models']").first
            if search_input.is_visible():
                print("[V] Trovato input di ricerca modelli! Digito 'chatgpt medium'...")
                search_input.fill("chatgpt medium")
                time.sleep(2)
                
                # Stampiamo i risultati visibili
                print("\n--- RISULTATI DELLA RICERCA DI MODELLO (MODALITA' IMAGE) ---")
                results = []
                for opt in page.locator("[role='option']").all():
                    try:
                        if opt.is_visible():
                            text = opt.inner_text().strip()
                            if text and "search models" not in text.lower():
                                results.append(text)
                    except:
                        pass
                if results:
                    for r in results:
                        print(f"  Trovato: '{r}'")
                else:
                    print("  Nessun modello trovato per 'chatgpt medium' in modalità Image!")
                    
                # Proviamo con altri termini se vuoto
                search_input.fill("")
                time.sleep(0.5)
                search_input.fill("gpt")
                time.sleep(2)
                print("\n--- RISULTATI DELLA RICERCA DI MODELLO PER 'gpt' (IMAGE) ---")
                for opt in page.locator("[role='option']").all():
                    try:
                        if opt.is_visible():
                            print(f"  Trovato gpt: '{opt.inner_text().strip()}'")
                    except:
                        pass
            else:
                print("Search input non visibile!")
        else:
            print("Dropdown modello non trovato!")
            
    except Exception as e:
        print(f"Errore: {e}")
    finally:
        manager.close()

if __name__ == "__main__":
    test_image_models()
