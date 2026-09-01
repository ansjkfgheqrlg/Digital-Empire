import os
import sys
import time

root_dir = os.path.dirname(os.path.abspath(__file__))
if root_dir not in sys.path:
    sys.path.append(root_dir)

from Core.browser_manager import BrowserManager

def inspect_image_button():
    print("[*] Avvio BrowserManager in modalità HEADLESS per ispezionare il pulsante immagine...")
    manager = BrowserManager('ArenaAI', headless=True)
    
    try:
        context = manager.get_context()
        page = context.new_page()
        
        url = "https://arena.ai/"
        print("[*] Navigo su https://arena.ai/...")
        page.goto(url, wait_until="domcontentloaded")
        time.sleep(6)
        
        # Facciamo uno screenshot iniziale
        page.screenshot(path="inspect_1_home.png")
        print("[*] Screenshot iniziale salvato come inspect_1_home.png")
        
        # Elenchiamo tutti i bottoni presenti nella pagina, specialmente quelli vicini alla textarea
        print("\n--- ELENCO DI TUTTI I BOTTONI VISIBILI NELLA PAGINA ---")
        buttons = page.locator("button").all()
        for idx, btn in enumerate(buttons):
            try:
                if btn.is_visible():
                    aria_label = btn.get_attribute("aria-label") or ""
                    title = btn.get_attribute("title") or ""
                    text = btn.inner_text().strip()
                    btn_id = btn.get_attribute("id") or ""
                    btn_class = btn.get_attribute("class") or ""
                    box = btn.bounding_box()
                    
                    # Stampiamo solo bottoni rilevanti (es. che hanno icone, label o posizioni vicine al form di input)
                    if box and box['y'] > 400: # Solitamente l'input bar è in basso
                        print(f"Btn #{idx}: text='{text}', aria-label='{aria_label}', title='{title}', id='{btn_id}', class='{btn_class[:50]}', box={box}")
                        
                        # Esaminiamo se contiene un SVG
                        svgs = btn.locator("svg").all()
                        if svgs:
                            print(f"  -> Contiene {len(svgs)} SVG")
                            for s_idx, svg in enumerate(svgs):
                                paths = svg.locator("path").all()
                                d_attrs = [p.get_attribute("d")[:30] + "..." for p in paths if p.get_attribute("d")]
                                print(f"     SVG #{s_idx}: paths={d_attrs}")
            except Exception as e:
                pass
                
        # Proviamo anche ad elencare i selettori specifici per l'area di input
        print("\n--- ANALISI DEGLI INPUT E CONTENITORI IN BASSO ---")
        for tag in ["textarea", "input", "[contenteditable='true']"]:
            locs = page.locator(tag).all()
            for idx, loc in enumerate(locs):
                try:
                    if loc.is_visible():
                        box = loc.bounding_box()
                        print(f"Input Tag '{tag}' #{idx}: box={box}, placeholder='{loc.get_attribute('placeholder')}'")
                except:
                    pass

        # Clicchiamo su "New Chat" per sicurezza
        new_chat_btn = page.locator("a:has-text('New Chat'), button:has-text('New Chat')").first
        if new_chat_btn.is_visible():
            new_chat_btn.click(force=True)
            time.sleep(3)
            
        # Proviamo a simulare il click sul pulsante dell'immagine usando i selettori trovati o trovandolo per prossimità
        print("\n[*] Provo a localizzare e cliccare il pulsante immagine...")
        
        # Selettore 1: per classe o prossimità dell'icona dell'immagine.
        # Spesso l'icona dell'immagine ha un'immagine o è un bottone con aria-label 'Image' o simile
        # Ma nel DOM moderno potrebbe non avere un'aria-label. Cerchiamo bottoni vicini al pulsante 'Add files' o alla textarea
        # che contengono icone.
        image_btn = None
        
        # Nel screenshot dell'utente, i pulsanti in basso sono: Add files, poi un'icona del mondo (web search), poi l'icona dell'immagine, poi </>
        # Cerchiamo i bottoni vicini alla textarea o all'interno della stessa barra
        input_container = page.locator("textarea").first.locator("xpath=./../..") # Saliamo di livello per trovare il contenitore dell'input
        
        # Se non funziona, cerchiamo tutti i bottoni in basso e proviamo a filtrarli
        candidates = []
        for btn in page.locator("button").all():
            try:
                if btn.is_visible():
                    aria_label = btn.get_attribute("aria-label") or ""
                    title = btn.get_attribute("title") or ""
                    box = btn.bounding_box()
                    if box and box['y'] > 500:
                        # Se è un bottone piccolo e non ha testo lungo
                        text = btn.inner_text().strip()
                        if len(text) < 15:
                            candidates.append(btn)
            except:
                pass
                
        print(f"Trovati {len(candidates)} bottoni candidati nella barra in basso.")
        
        # Facciamo una prova a cliccare quello che potrebbe essere il pulsante immagine
        # Spesso ha aria-label='Image' o contiene un svg con determinate forme o è il terzo bottone dopo 'Add files'
        # Cerchiamo un bottone che abbia aria-label contenente 'image', 'picture', 'photo', 'genera', 'generate' o 'media'
        found_btn = None
        for c in candidates:
            label = (c.get_attribute("aria-label") or "").lower()
            title = (c.get_attribute("title") or "").lower()
            if "image" in label or "image" in title or "picture" in label or "photo" in label:
                found_btn = c
                break
                
        if found_btn:
            print(f"[V] Trovato pulsante immagine tramite attributi: aria-label/title. Clicco...")
            found_btn.click(force=True)
            time.sleep(3)
            page.screenshot(path="inspect_2_clicked_image_btn.png")
        else:
            print("[*] Nessun bottone con label 'image' esplicito. Stampo l'HTML dei candidati...")
            for idx, c in enumerate(candidates):
                try:
                    html = c.inner_html()
                    print(f"Candidato #{idx}: HTML = {html[:150]}...")
                    # Se ha un SVG e non ha testo, proviamo a cliccarlo per vedere l'effetto
                    # Nel screenshot del cliente, ci sono 4 bottoni in basso:
                    # 1. Add files (con testo)
                    # 2. Globe icon (senza testo)
                    # 3. Image icon (senza testo)
                    # 4. </> icon (senza testo)
                    # Quindi l'immagine è l'icona numero 3 in quel gruppo!
                except Exception as e:
                    print(f"Errore candidato #{idx}: {e}")
                    
            # Proviamo a cliccarli uno per uno e salvare screenshot per vedere quale attiva la modalità Immagine!
            for idx, c in enumerate(candidates):
                try:
                    print(f"[*] Clicco candidato #{idx} per test...")
                    c.click(force=True)
                    time.sleep(2)
                    page.screenshot(path=f"inspect_3_candidate_{idx}.png")
                    # Resettiamo cliccando di nuovo (se è un toggle)
                    c.click(force=True)
                    time.sleep(1)
                except Exception as e:
                    print(f"Errore nel cliccare candidato #{idx}: {e}")
                    
    except Exception as e:
        print(f"[X] Errore nell'ispezione: {e}")
    finally:
        manager.close()

if __name__ == "__main__":
    inspect_image_button()
