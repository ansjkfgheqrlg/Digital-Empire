import os
import sys
import time

root_dir = os.path.dirname(os.path.abspath(__file__))
if root_dir not in sys.path:
    sys.path.append(root_dir)

from Core.browser_manager import BrowserManager

def find_send_button():
    print("[*] Avvio BrowserManager per ispezionare il bottone d'invio...")
    manager = BrowserManager('ArenaAI', headless=True)
    
    try:
        context = manager.get_context()
        page = context.new_page()
        
        url = "https://arena.ai/"
        page.goto(url, wait_until="domcontentloaded")
        time.sleep(5)
        
        # Setup base
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
        
        # Clicca Image Mode
        image_btn = page.locator("button[aria-label='Image'], button[title='Image']").first
        if image_btn.is_visible():
            image_btn.click(force=True)
            time.sleep(3)
            
        # Trova textarea
        textarea = page.locator("textarea").first
        textarea.fill("Test di invio")
        time.sleep(2)
        
        # Trova tutti i bottoni vicino alla textarea
        print("\n--- PULSANTI TROVATI VICINO ALLA TEXTAREA ---")
        parent = textarea.locator("xpath=..")
        # Risaliamo di qualche livello per trovare il container del form
        form_container = textarea.locator("xpath=../..")
        
        for btn in form_container.locator("button").all():
            try:
                if btn.is_visible():
                    box = btn.bounding_box()
                    print(f"Bottone: Text='{btn.inner_text().strip()}', Class='{btn.get_attribute('class')}', Aria-label='{btn.get_attribute('aria-label')}', Box={box}")
            except Exception as e:
                print(f"Errore bottone: {e}")
                
        # Vediamo anche tutti i bottoni con una freccia o submit nella pagina
        print("\n--- ALTRI PULSANTI DI INVIO NELLA PAGINA ---")
        for btn in page.locator("button").all():
            try:
                if btn.is_visible():
                    aria_label = btn.get_attribute('aria-label') or ""
                    title = btn.get_attribute('title') or ""
                    type_attr = btn.get_attribute('type') or ""
                    text = btn.inner_text().strip()
                    
                    if "send" in aria_label.lower() or "submit" in type_attr.lower() or "send" in title.lower() or not text:
                        box = btn.bounding_box()
                        # Filtra per bottoni in basso a destra dello schermo (x > 500, y > 400)
                        if box and box['x'] > 500 and box['y'] > 400:
                            print(f"Candidato: Aria-label='{aria_label}', Title='{title}', Type='{type_attr}', Box={box}")
            except:
                pass
                
    except Exception as e:
        print(f"Errore: {e}")
    finally:
        manager.close()

if __name__ == "__main__":
    find_send_button()
