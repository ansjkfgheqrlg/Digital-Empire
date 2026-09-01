import os
import sys
import time

root_dir = os.path.dirname(os.path.abspath(__file__))
if root_dir not in sys.path:
    sys.path.append(root_dir)

from Core.browser_manager import BrowserManager

def test_direct():
    print("[*] Avvio BrowserManager per testare la selezione Direct...")
    manager = BrowserManager('ArenaAI', headless=True)
    
    try:
        context = manager.get_context()
        page = context.new_page()
        
        url = "https://arena.ai/"
        print(f"[*] Navigazione verso: {url}")
        page.goto(url, wait_until="domcontentloaded")
        time.sleep(5)
        
        # 1. Trova l'elemento visibile con testo 'Battle Mode'
        print("[*] Cerco l'elemento VISIBILE contenente esattamente 'Battle Mode' nell'header...")
        visible_btn = None
        
        # Cerchiamo tra tutti gli elementi p, button, span che contengono il testo esatto e che sono visibili
        for btn in page.locator("button, p, span").all():
            try:
                if btn.is_visible():
                    text = btn.inner_text().strip()
                    if text == "Battle Mode":
                        box = btn.bounding_box()
                        if box and box['width'] > 0 and box['width'] < 300 and box['y'] < 100: # Deve essere nell'header
                            print(f"[V] Trovato elemento visibile: Tag={btn.evaluate('e => e.tagName')}, Box={box}")
                            visible_btn = btn
                            break
            except:
                pass
                
        # Se non lo trova con l'esatto, prova con combobox
        if not visible_btn:
            combobox = page.locator("button[role='combobox']").first
            if combobox.is_visible():
                box = combobox.bounding_box()
                if box and box['width'] > 0 and box['y'] < 100:
                    print(f"[V] Trovato combobox nell'header: Box={box}")
                    visible_btn = combobox

                
        success = False
        if visible_btn:
            try:
                box = visible_btn.bounding_box()
                # Proviamo a cliccarlo direttamente
                print("[*] Clicco direttamente sull'elemento visibile...")
                visible_btn.click(force=True)
                success = True
            except Exception as e:
                print(f"[X] Click diretto fallito: {e}")
                
            if not success:
                try:
                    # Fallback con coordinate mouse
                    x = box['x'] + box['width']/2
                    y = box['y'] + box['height']/2
                    print(f"[*] Clicco a coordinate mouse ({x}, {y})")
                    page.mouse.click(x, y)
                    success = True
                except Exception as e:
                    print(f"[X] Click mouse fallito: {e}")
        else:
            print("[X] Nessun elemento visibile 'Battle Mode' trovato nell'header!")


        time.sleep(3)
        
        # Stampiamo tutte le opzioni visibili nel menu
        print("\n--- TESTO DI TUTTI GLI ELEMENTI ATTIVI E VISIBILI IN COPERTURA ---")
        # I menu di Radix UI di solito sono portali posizionati in fondo al body
        for idx, el in enumerate(page.locator("div[role='listbox'] *, div[role='menu'] *, ul *, li, button, [role='option']").all()):
            try:
                if el.is_visible():
                    text = el.inner_text().strip()
                    role = el.get_attribute("role") or ""
                    if text and len(text) < 50:
                        print(f"Elemento {idx}: Text='{text}', Role='{role}'")
            except:
                pass

        # Cerca l'opzione "Direct" e cliccala
        print("[*] Cerco l'opzione 'Direct'...")
        direct_clicked = False
        
        # Proviamo prima per testo esatto o parziale
        for opt in page.locator("div, span, button, [role='option']").all():
            try:
                text = opt.inner_text().strip()
                if text == "Direct" and opt.is_visible():
                    print(f"[V] Clicco su elemento 'Direct' esatto! (Tag: {opt.evaluate('e => e.tagName')})")
                    opt.click(force=True)
                    direct_clicked = True
                    break
            except:
                pass
                
        if not direct_clicked:
            for opt in page.locator("div, span, button, [role='option']").all():
                try:
                    text = opt.inner_text().strip()
                    if "direct" in text.lower() and opt.is_visible():
                        print(f"[V] Clicco su elemento con testo contenente 'direct': '{text}'")
                        opt.click(force=True)
                        direct_clicked = True
                        break
                except:
                    pass

        if not direct_clicked:
            print("[X] Impossibile cliccare su Direct!")
        else:
            time.sleep(4)
            page.screenshot(path=os.path.join(root_dir, "arena_direct_selected.png"))
            print("[V] Screenshot Direct selezionato salvato!")
            
            # Ora che siamo in Direct, stampiamo i bottoni e i selettori per il Modello (chatgpt medium) e l'immagine
            print("\n--- ELEMENTI VISIBILI IN DIRECT MODE ---")
            for idx, el in enumerate(page.locator("button, [role='combobox']").all()):
                try:
                    if el.is_visible():
                        text = el.inner_text().strip()
                        aria_label = el.get_attribute("aria-label") or ""
                        print(f"Element {idx}: Text='{text}', AriaLabel='{aria_label}'")
                except:
                    pass


    except Exception as e:
        print(f"[X] Errore: {e}")
    finally:
        manager.close()

if __name__ == "__main__":
    test_direct()
