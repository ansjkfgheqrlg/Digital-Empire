import os
import sys
import time

root_dir = os.path.dirname(os.path.abspath(__file__))
if root_dir not in sys.path:
    sys.path.append(root_dir)

from Core.browser_manager import BrowserManager

def test_search_input():
    print("[*] Avvio BrowserManager per testare la ricerca del modello...")
    manager = BrowserManager('ArenaAI', headless=True)
    
    try:
        context = manager.get_context()
        page = context.new_page()
        
        url = "https://arena.ai/"
        page.goto(url, wait_until="domcontentloaded")
        time.sleep(5)
        
        # Clicca Battle Mode
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
        if visible_btn:
            visible_btn.click(force=True)
            time.sleep(2)
            
        # Clicca Direct
        for opt in page.locator("[role='option']").all():
            try:
                if opt.is_visible():
                    text = opt.inner_text().strip()
                    if text.startswith("Direct"):
                        opt.click(force=True)
                        break
            except:
                pass
        time.sleep(4)
        
        # Clicca Max
        model_btn = None
        for btn in page.locator("button").all():
            try:
                if btn.is_visible():
                    text = btn.inner_text().strip()
                    if "Max" in text:
                        model_btn = btn
                        break
            except:
                pass
                
        if model_btn:
            model_btn.click(force=True)
            time.sleep(2)
            
            # Trova l'input di ricerca e digita "chatgpt medium"
            search_input = page.locator("input[placeholder='Search models']").first
            if search_input.is_visible():
                print("[V] Trovato input di ricerca modelli! Digito 'chatgpt medium'...")
                search_input.fill("chatgpt medium")
                time.sleep(3)
                
                # Screenshot dei risultati della ricerca
                page.screenshot(path=os.path.join(root_dir, "arena_search_result.png"))
                print("[V] Screenshot risultati di ricerca salvato!")
                
                # Stampiamo i risultati visibili
                print("\n--- RISULTATI DELLA RICERCA DI MODELLO ---")
                options = page.locator("[role='option'], button, span, p, div").all()
                for idx, opt in enumerate(options):
                    try:
                        if opt.is_visible():
                            text = opt.inner_text().strip()
                            # Se non è vuoto e non è il testo generico dell'interfaccia
                            if text and len(text) < 100 and "search models" not in text.lower():
                                print(f"Opzione {idx}: '{text}'")
                    except:
                        pass
                        
                # Proviamo a cliccare sulla prima opzione che corrisponde a "chatgpt medium"
                clicked = False
                for opt in page.locator("[role='option'], button, span, p").all():
                    try:
                        if opt.is_visible():
                            text = opt.inner_text().strip().lower()
                            if "chatgpt medium" in text or "chatgpt-medium" in text or "gpt medium" in text or "chatgpt_medium" in text:
                                print(f"[V] Clicco sul modello trovato: '{opt.inner_text().strip()}'")
                                opt.click(force=True)
                                clicked = True
                                break
                    except:
                        pass
                if not clicked:
                    print("[X] Impossibile trovare e cliccare 'chatgpt medium' nei risultati!")
            else:
                print("[X] Input di ricerca modelli non visibile!")
        else:
            print("[X] Bottone Max non trovato!")
            
        time.sleep(2)
        # Clicca Image
        image_btn = page.locator("button[aria-label='Image'], button[title='Image']").first
        if image_btn.is_visible():
            image_btn.click(force=True)
            time.sleep(2)
            
        page.screenshot(path=os.path.join(root_dir, "arena_search_final.png"))
        print("[V] Screenshot finale salvato!")
        
    except Exception as e:
        print(f"Errore: {e}")
    finally:
        manager.close()

if __name__ == "__main__":
    test_search_input()
