import os
import sys
import time
import glob
import re
from playwright_recaptcha import recaptchav2

root_dir = os.path.dirname(os.path.dirname(__file__))
if root_dir not in sys.path:
    sys.path.append(root_dir)

from Core.browser_manager import BrowserManager
import config

def solve_arena_captcha(page):
    """Rileva e risolve i CAPTCHA su Arena.ai, anche se dentro dialoghi."""
    try:
        # Cerca i vari possibili frame di reCAPTCHA
        frames = page.frames
        for frame in frames:
            if "recaptcha" in frame.url.lower():
                anchor = frame.locator("#recaptcha-anchor")
                if anchor.is_visible(timeout=1000):
                    print("[ArenaAI] [!] CAPTCHA rilevato in frame. Risoluzione...")
                    with recaptchav2.SyncSolver(page) as solver:
                        solver.solve_recaptcha()
                    print("[ArenaAI] [V] CAPTCHA risolto.")
                    return True
        
        if page.locator("iframe[title*='reCAPTCHA']").is_visible(timeout=1000):
             print("[ArenaAI] [!] CAPTCHA visibile (iframe). Risoluzione...")
             with recaptchav2.SyncSolver(page) as solver:
                 solver.solve_recaptcha()
             print("[ArenaAI] [V] CAPTCHA risolto.")
             return True
             
    except Exception as e:
        if "closed" not in str(e).lower():
            print(f"[ArenaAI] Nota CAPTCHA: {e}")
    return False

def upload_files_robust(page, file_paths):
    """Caricamento file con fallback e gestione CAPTCHA."""
    print(f"[ArenaAI] Caricamento {len(file_paths)} file...")
    solve_arena_captcha(page)
    try:
        page.set_input_files("input[type='file']", file_paths)
        time.sleep(4)
        return True
    except Exception as e:
        print(f"[ArenaAI] Errore upload: {e}")
        return False

def setup_arena_chat(page):
    """Configura la modalità Direct e Immagine con click forzati."""
    print("[ArenaAI] Configurazione sessione...")
    solve_arena_captcha(page)
    
    # 1. Forza Direct Mode
    try:
        mode_btn = page.locator("button").filter(has_text=re.compile(r"Battle Mode|Side by Side|Direct", re.I)).first
        if mode_btn.is_visible(timeout=5000):
            if "Direct" not in mode_btn.inner_text():
                mode_btn.click(force=True)
                time.sleep(2)
                direct_opt = page.locator("button, div").filter(has_text="Direct").filter(has_text="Chat with 1 model").last
                if direct_opt.is_visible():
                    direct_opt.click(force=True)
                    time.sleep(2)
    except: pass
    
    # 2. Modalità Immagine
    try:
        image_btn = page.locator("button[aria-label='Image'], button[title='Image']").first
        if image_btn.is_visible(timeout=3000):
            image_btn.click(force=True)
            time.sleep(2)
    except: pass
            
    # 3. Modello GPT Medium
    try:
        model_dropdown = page.locator("button").filter(has_text=re.compile(r"Max|GPT|Claude|Medium", re.I)).first
        if model_dropdown.is_visible(timeout=3000):
            if "medium" not in model_dropdown.inner_text().lower():
                model_dropdown.click(force=True)
                time.sleep(2)
                search = page.locator("input[placeholder*='Search']").first
                if search.is_visible():
                    search.fill("chatgpt medium")
                    time.sleep(1)
                    target = page.locator("div[role='option'], li[role='option']").filter(has_text="medium").first
                    if target.is_visible():
                        target.click(force=True)
                        time.sleep(2)
    except: pass
    return True

def generate_carousel_visuals(slides_plan, topic_name, headless=False):
    """Genera le slide reali."""
    print(f"\n[ArenaAI] Avvio Generazione Carosello: {topic_name}")
    manager = BrowserManager('ArenaAI', headless=headless)
    local_topic_dir = os.path.join(config.LOCAL_DOWNLOAD_DIR, topic_name)
    os.makedirs(local_topic_dir, exist_ok=True)
    
    try:
        context = manager.get_context()
        page = manager.new_page(context)
        
        allegati_files = []
        if os.path.exists(config.ALLEGATI_DIR):
            allegati_files = glob.glob(os.path.join(config.ALLEGATI_DIR, "*.*"))

        known_srcs = set()

        for index, slide in enumerate(slides_plan):
            n_slide = slide['slide_numero']
            testo_slide = slide['testo_esatto']
            success = False
            
            print(f"\n>>> Generazione Slide {n_slide}: {testo_slide[:40]}...")
            
            for attempt in range(3):
                try:
                    page.goto("https://arena.ai/", timeout=60000)
                    time.sleep(5)
                    
                    if page.locator("button:has-text('Log In')").is_visible(timeout=2000):
                        print("[ArenaAI] [!] ATTENZIONE: Sessione non autenticata.")
                    
                    setup_arena_chat(page)
                    
                    if index == 0:
                        if allegati_files: upload_files_robust(page, allegati_files)
                    else:
                        prev_path = os.path.join(local_topic_dir, f"slide_{index}.png")
                        if os.path.exists(prev_path): upload_files_robust(page, [prev_path])

                    regole = "Regole: grafica perfetta, gradiente #062155/#edeebe, font elegante, NO testo eccessivo."
                    prompt = f"Genera la slide {n_slide}. Testo: '{testo_slide}'. {regole}"
                    if index > 0: prompt += " Mantieni lo STESSO IDENTICO stile dell'allegato."

                    print(f"[ArenaAI] Scrittura prompt...")
                    textarea = page.locator("textarea").first
                    solve_arena_captcha(page) 
                    
                    textarea.click(force=True)
                    textarea.fill("") 
                    textarea.type(prompt, delay=30)
                    time.sleep(2)
                    
                    submit_btn = page.locator("button[type='submit'], button:has(svg path[d*='M6 12L3.269 3.126'])").last
                    submit_btn.click(force=True)
                    
                    print("[ArenaAI] Prompt inviato. Attesa generazione...")
                    
                    found = False
                    for poll in range(80): # 4 minuti
                        time.sleep(3)
                        solve_arena_captcha(page)
                        
                        elements = page.locator("img, canvas").all()
                        for el in elements:
                            try:
                                box = el.bounding_box()
                                if box and box['width'] > 300 and box['height'] > 300:
                                    src = el.get_attribute("src") or ""
                                    if "blob:" in src or src not in known_srcs:
                                        print(f"[ArenaAI] [V] Slide {n_slide} rilevata! Salvataggio...")
                                        time.sleep(5) 
                                        dest = os.path.join(local_topic_dir, f"slide_{n_slide}.png")
                                        el.screenshot(path=dest)
                                        
                                        if os.path.getsize(dest) > 30000:
                                            known_srcs.add(src)
                                            success = True
                                            found = True
                                            break
                            except: pass
                        if found: break
                    
                    if success: break
                    else: print(f"[ArenaAI] Tentativo {attempt+1} fallito. Riprovo...")
                except Exception as e:
                    print(f"[ArenaAI] Errore nel tentativo: {e}")
                    solve_arena_captcha(page)
            
            if not success:
                print(f"[ArenaAI] [X] IMPOSSIBILE generare Slide {n_slide}.")

        print(f"\n[ArenaAI] Workflow completato. Cartella: {local_topic_dir}")
        return local_topic_dir if any(glob.glob(os.path.join(local_topic_dir, "slide_*.png"))) else None

    except Exception as e:
        print(f"[ArenaAI] Errore critico: {e}")
        return None
    finally:
        manager.close()

if __name__ == "__main__":
    generate_carousel_visuals([{"slide_numero": 1, "testo_esatto": "Test"}], "Emergency_Test")
