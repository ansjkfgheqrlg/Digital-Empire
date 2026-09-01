import os
import sys
import time

root_dir = os.path.dirname(os.path.abspath(__file__))
if root_dir not in sys.path:
    sys.path.append(root_dir)

from Core.browser_manager import BrowserManager

def inspect():
    print("[*] Avvio BrowserManager per ispezionare Arena...")
    manager = BrowserManager('ArenaAI', headless=True)
    
    try:
        context = manager.get_context()
        page = context.new_page()
        
        url_test = "https://www.google.com"
        print(f"[*] Test connettività verso: {url_test}")
        page.goto(url_test, wait_until="domcontentloaded", timeout=15000)
        print("[V] Connessione a Google riuscita!")
        
        url = "https://arena.ai/"
        print(f"[*] Navigazione verso Arena: {url}")
        page.goto(url, wait_until="domcontentloaded", timeout=30000)
        time.sleep(8)
        
        # Salviamo uno screenshot
        screenshot_path = os.path.join(root_dir, "arena_home.png")
        page.screenshot(path=screenshot_path)
        print(f"[V] Screenshot salvato in: {screenshot_path}")
        
        # Dump HTML
        html_path = os.path.join(root_dir, "arena_home.html")
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(page.content())
        print(f"[V] HTML salvato in: {html_path}")
        
        # Stampiamo alcuni elementi significativi
        print("\n--- BOTTONI VISIBILI ---")
        buttons = page.locator("button").all()
        for idx, btn in enumerate(buttons):
            try:
                text = btn.inner_text().strip()
                aria_label = btn.get_attribute("aria-label") or ""
                title = btn.get_attribute("title") or ""
                html_class = btn.get_attribute("class") or ""
                if text or aria_label or title:
                    print(f"Btn {idx}: Text='{text}', AriaLabel='{aria_label}', Title='{title}', Class='{html_class}'")
            except:
                pass
                
        print("\n--- LINK / TAB VISIBILI ---")
        links = page.locator("a").all()
        for idx, link in enumerate(links):
            try:
                text = link.inner_text().strip()
                href = link.get_attribute("href") or ""
                if text or href:
                    print(f"Link {idx}: Text='{text}', Href='{href}'")
            except:
                pass

        print("\n--- INPUT FILE E TEXTAREA ---")
        inputs = page.locator("input").all()
        for idx, inp in enumerate(inputs):
            try:
                inp_type = inp.get_attribute("type") or ""
                inp_class = inp.get_attribute("class") or ""
                print(f"Input {idx}: Type='{inp_type}', Class='{inp_class}'")
            except:
                pass

    except Exception as e:
        print(f"[X] Errore: {e}")
    finally:
        manager.close()


if __name__ == "__main__":
    inspect()
