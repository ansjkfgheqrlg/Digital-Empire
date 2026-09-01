import os
import sys
import time

root_dir = os.path.dirname(os.path.abspath(__file__))
if root_dir not in sys.path:
    sys.path.append(root_dir)

from Core.browser_manager import BrowserManager

def search_chatgpt():
    print("[*] Avvio BrowserManager per cercare modelli chatgpt...")
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
            time.sleep(3)
            
            # Cerca tra tutti gli elementi del menu
            print("\n--- MODELLI CHE CONTENGONO 'chatgpt' ---")
            found = False
            for opt in page.locator("[role='option'], button, span, p, div").all():
                try:
                    if opt.is_visible():
                        text = opt.inner_text().strip()
                        if "chatgpt" in text.lower() or "gpt" in text.lower():
                            print(f"Modello: '{text}' (Tag: {opt.evaluate('e => e.tagName')})")
                            found = True
                except:
                    pass
            if not found:
                print("Nessun modello trovato contenente 'chatgpt'!")
        else:
            print("Dropdown modello non trovato!")
            
    except Exception as e:
        print(f"Errore: {e}")
    finally:
        manager.close()

if __name__ == "__main__":
    search_chatgpt()
