import os
import sys
import time

root_dir = os.path.dirname(os.path.abspath(__file__))
if root_dir not in sys.path:
    sys.path.append(root_dir)

from Core.browser_manager import BrowserManager

def test_search_terms():
    print("[*] Avvio BrowserManager per testare termini di ricerca modello...")
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
                if opt.is_visible() and opt.inner_text().strip().startswith("Direct"):
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
            
            search_input = page.locator("input[placeholder='Search models']").first
            if search_input.is_visible():
                terms = ["chatgpt", "chatgpt medium", "gpt-4o", "gpt-4", "4o", "chatgpt-4o", "medium", "gpt-4o-medium"]
                for term in terms:
                    print(f"\n--- CERCO TERMINE: '{term}' ---")
                    # Pulisce e scrive il termine
                    search_input.fill("")
                    time.sleep(0.5)
                    search_input.fill(term)
                    time.sleep(2)
                    
                    # Stampiamo i risultati visibili
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
                        print("  Nessun modello trovato!")
            else:
                print("Search input non trovato!")
        else:
            print("Bottone Max non trovato!")
            
    except Exception as e:
        print(f"Errore: {e}")
    finally:
        manager.close()

if __name__ == "__main__":
    test_search_terms()
