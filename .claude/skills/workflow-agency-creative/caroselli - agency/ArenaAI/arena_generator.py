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

def dismiss_blocking_dialogs(page, timeout_ms=1500):
    """Root cause reale del fallimento 9/9 tentativi del 2026-08-05 (CP-20260805):
    Arena mostra (a) un banner cookie al primo caricamento ("This website uses
    cookies" / Accept Cookies) e (b) un secondo modal "Terms of Use / Agree" la
    prima volta che si attiva la modalita' Image in una sessione. Nessuno dei due
    veniva gestito. Un click force=True su un elemento sotto il modal non da' MAI
    errore (force bypassa il controllo "receives events" di Playwright) - il
    risultato e' un blocco silenzioso di ogni interazione successiva, senza una
    sola riga d'errore nel log. Diagnosticato solo con screenshot reali dopo 2 run
    completi falliti (9 tentativi, 0 immagini, 0 eccezioni).

    Va richiamata ad OGNI punto critico del flusso (dopo ogni cambio di modalita',
    prima di scrivere il prompt, prima di ogni submit) - non basta chiamarla una
    volta sola all'inizio, perche' i due modal compaiono in momenti diversi."""
    try:
        accept_btn = page.locator(
            "button:has-text('Accept Cookies'), button:has-text('Accept all'), "
            "button:has-text('Agree')"
        ).first
        if accept_btn.is_visible(timeout=timeout_ms):
            accept_btn.click(force=True)
            time.sleep(1)
            print("[ArenaAI] Dialog dismesso (Accept/Agree).")
            return True
    except Exception:
        pass
    # Fallback universale: qualunque altro dialog rimasto aperto (es. da una
    # sessione precedente) si chiude con Escape senza dover indovinare il
    # selettore esatto del bottone di chiusura.
    try:
        dialog = page.locator("[role='dialog']").first
        if dialog.is_visible(timeout=timeout_ms):
            page.keyboard.press("Escape")
            time.sleep(1)
            print("[ArenaAI] Dialog residuo chiuso con Escape.")
            return True
    except Exception:
        pass
    return False


def wait_for_login(page, timeout_sec=300):
    """Se la sessione persistente e' scaduta, Arena mostra un modal 'Log In or
    Create Account' che copre tutta la UI. Prima di questo fix lo script non lo
    gestiva: continuava a cercare textarea/bottoni nascosti dal modal per 3
    tentativi x 3 slide, girando a vuoto per 30+ minuti senza mai produrre un
    errore chiaro (bug reale, trovato su un run vero il 2026-08-05 dopo che il
    profilo Arena non veniva usato dal 22 maggio). Ora si ferma, aspetta che
    l'utente faccia login a mano nella finestra aperta, e riprende da solo."""
    try:
        login_modal = page.get_by_text("Log In or Create Account", exact=False).first
        if not login_modal.is_visible(timeout=2000):
            return True  # gia' autenticato
    except Exception:
        return True

    print("[ArenaAI] [!] Sessione non autenticata — fai login nella finestra aperta (Google o email). In attesa...")
    waited = 0
    poll = 5
    while waited < timeout_sec:
        time.sleep(poll)
        waited += poll
        try:
            if not login_modal.is_visible(timeout=1000):
                print("[ArenaAI] [V] Login rilevato, riprendo.")
                return True
        except Exception:
            print("[ArenaAI] [V] Pagina cambiata, riprendo.")
            return True
        if waited % 30 == 0:
            print(f"[ArenaAI] In attesa del login... ({waited}s/{timeout_sec}s)")

    print(f"[ArenaAI] [X] Login non completato entro {timeout_sec}s.")
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
    """Configura la modalità Direct e Immagine con click forzati.

    Nota (debug 2026-08-05, CP-20260805): questa funzione inghiottiva ogni
    errore con `except: pass` - una run reale ha fallito 9/9 tentativi senza
    NESSUNA traccia del perché (0 immagini generate, nessuna eccezione nel
    log). Diagnosticato con screenshot reali: il selettore del bottone Image
    (aria-label='Image') e' corretto e l'elemento e' visibile, ma il bottone
    del mode-switch (Battle Mode -> Direct) e' risultato "not visible" in un
    check isolato subito dopo il page.goto() - probabile race di idratazione
    React/Radix UI. Ora ogni step logga esito reale (fatto/fallito/perché)
    invece di fallire in silenzio, cosi' un fallimento futuro e' diagnosticabile
    dal log invece che richiedere un altro giro di screenshot manuali."""
    print("[ArenaAI] Configurazione sessione...")
    dismiss_blocking_dialogs(page)
    solve_arena_captcha(page)

    # attende che il composer sia davvero pronto prima di toccare la UI
    # (idratazione React puo' richiedere piu' dei 5s fissi del chiamante)
    try:
        page.locator("textarea").first.wait_for(state="visible", timeout=8000)
    except Exception as e:
        print(f"[ArenaAI] [!] Composer non visibile dopo l'attesa: {e}")

    # 1. Forza Direct Mode
    # `button` (senza :visible) matcheva un duplicato NASCOSTO nel DOM (stesso
    # testo "Battle Mode", ma <button ...> con data-state="closed" mai visibile
    # in nessun run) - confermato con `Locator.wait_for` che scade sempre dopo
    # aver risolto ripetutamente sullo stesso elemento hidden. `:visible` forza
    # a prendere il bottone che l'utente vede davvero, in alto a sinistra.
    try:
        mode_btn = page.locator("button:visible").filter(has_text=re.compile(r"Battle Mode|Side by Side|Direct", re.I)).first
        mode_btn.wait_for(state="visible", timeout=6000)
        if "Direct" not in mode_btn.inner_text():
            mode_btn.click(force=True)
            time.sleep(2)
            direct_opt = page.locator("button, div").filter(has_text="Direct").filter(has_text="Chat with 1 model").last
            if direct_opt.is_visible(timeout=3000):
                direct_opt.click(force=True)
                time.sleep(2)
                print("[ArenaAI] Direct mode attivata.")
            else:
                print("[ArenaAI] [!] Opzione 'Direct' non trovata nel menu aperto.")
        else:
            print("[ArenaAI] Gia' in Direct mode.")
    except Exception as e:
        print(f"[ArenaAI] [!] Switch a Direct mode fallito: {e}")

    # 2. Modalità Immagine
    try:
        image_btn = page.locator("button[aria-label='Image'], button[title='Image']").first
        image_btn.wait_for(state="visible", timeout=5000)
        pressed_before = image_btn.get_attribute("aria-pressed") or image_btn.get_attribute("data-state") or ""
        image_btn.click(force=True)
        time.sleep(2)
        pressed_after = image_btn.get_attribute("aria-pressed") or image_btn.get_attribute("data-state") or ""
        print(f"[ArenaAI] Toggle Image cliccato (stato prima='{pressed_before}' dopo='{pressed_after}').")
    except Exception as e:
        print(f"[ArenaAI] [!] Toggle modalita' Image fallito: {e}")

    # La prima attivazione di Image in una sessione fa comparire un secondo modal
    # ("Terms of Use & Privacy Policy" / Agree) - va dismesso qui, non solo
    # all'inizio della funzione (vedi dismiss_blocking_dialogs).
    dismiss_blocking_dialogs(page)

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
                        print("[ArenaAI] Modello 'chatgpt medium' selezionato.")
                    else:
                        print("[ArenaAI] [!] Opzione modello 'medium' non trovata nella ricerca.")
        else:
            print("[ArenaAI] [!] Bottone selezione modello non visibile - resta il default.")
    except Exception as e:
        print(f"[ArenaAI] [!] Selezione modello fallita (resta il default): {e}")
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

                    if not wait_for_login(page):
                        print("[ArenaAI] [X] Interrompo: impossibile procedere senza login.")
                        return None

                    setup_arena_chat(page)
                    
                    if index == 0:
                        if allegati_files: upload_files_robust(page, allegati_files)
                    else:
                        prev_path = os.path.join(local_topic_dir, f"slide_{index}.png")
                        if os.path.exists(prev_path): upload_files_robust(page, [prev_path])

                    regole = "Regole: grafica perfetta, gradiente #062155/#edeebe, font elegante, NO testo eccessivo."
                    prompt = f"Genera la slide {n_slide}. Testo: '{testo_slide}'. {regole}"
                    if index > 0: prompt += " Mantieni lo STESSO IDENTICO stile dell'allegato."

                    dismiss_blocking_dialogs(page)  # rete di sicurezza finale prima del submit

                    print(f"[ArenaAI] Scrittura prompt...")
                    textarea = page.locator("textarea").first
                    solve_arena_captcha(page)

                    textarea.click(force=True)
                    textarea.fill("") 
                    textarea.type(prompt, delay=30)
                    time.sleep(2)
                    
                    submit_btn = page.locator("button[type='submit'], button:has(svg path[d*='M6 12L3.269 3.126'])").last
                    submit_btn.click(force=True)
                    time.sleep(2)

                    # Il PRIMO submit reale di una sessione apre un gate "Terms of Use &
                    # Privacy Policy / Agree" invece di inviare il prompt (root cause vera
                    # del fallimento 9/9 del 2026-08-05, trovata con screenshot: a questo
                    # punto il click precedente viene "assorbito" dal gate, il prompt non
                    # parte mai). Se il gate compare, va accettato e il submit rifatto.
                    if dismiss_blocking_dialogs(page, timeout_ms=2000):
                        print("[ArenaAI] Gate Terms of Use dismesso — reinvio il prompt.")
                        # Il textarea perde il focus quando si apre/chiude il gate - un
                        # secondo click diretto sul bottone submit non basta, va ridato
                        # focus al composer prima, altrimenti il click non fa nulla
                        # (osservato su un run reale: submit "riuscito" senza errori, ma
                        # il prompt restava visibile non-inviato nella textarea).
                        textarea.click(force=True)
                        time.sleep(1)
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
                    if "closed" in str(e).lower():
                        # Bug reale trovato su un run vero (2026-08-05, CP-20260805): il browser
                        # e' morto a meta' (Chrome crash durante una risoluzione captcha) e OGNI
                        # tentativo successivo, per TUTTE le slide rimanenti, falliva all'istante
                        # con lo stesso errore "context/browser has been closed" - il codice
                        # riusava un `page` ormai morto invece di riaprire una sessione. Ora
                        # rileva il caso e riapre browser/contesto/pagina puliti prima di ritentare.
                        print("[ArenaAI] [!] Browser/contesto chiuso inaspettatamente — riapro una sessione pulita.")
                        try:
                            manager.close()
                        except Exception:
                            pass
                        manager = BrowserManager('ArenaAI', headless=headless)
                        context = manager.get_context()
                        page = manager.new_page(context)
                    else:
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
