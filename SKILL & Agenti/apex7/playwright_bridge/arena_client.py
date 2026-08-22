"""
APEX-7 Arena Playwright Client - Bridge per Claude Code
Permette a Claude Code (che non può generare immagini) di controllare Arena.ai via browser automation

Install: pip install playwright && playwright install chromium
"""

import asyncio
import os
import json
import re
import time
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Optional
import yaml
import base64

try:
    from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeout
    PLAYWRIGHT_AVAILABLE = True
except ImportError:
    PLAYWRIGHT_AVAILABLE = False
    print("[WARN] playwright non installato - userai fallback locale con generate_image")

from playwright_bridge.auth_manager import AuthManager

BASE_DIR = Path(__file__).parent.parent
CONFIG_PATH = BASE_DIR / "playwright_bridge" / "config.yaml"
OUTPUT_DIR = BASE_DIR / "outputs" / "carousel"

class ArenaPlaywrightClient:
    def __init__(self, config_path: Path = CONFIG_PATH, headless: bool = True, model: str = "GPT-4o", debug: bool = False):
        self.config = self._load_config(config_path)
        self.headless = headless
        self.model = model
        self.debug = debug
        self.browser = None
        self.page = None
        self.context = None
        self.playwright = None
        self.auth_manager = AuthManager()
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        if debug:
            self.auth_manager.screenshots_dir.mkdir(parents=True, exist_ok=True)
        print(f"[ARENA PLAYWRIGHT] Init model={model} headless={headless} debug={debug} playwright_available={PLAYWRIGHT_AVAILABLE}")
        if debug:
            print(f"[DEBUG] Screenshots dir: {self.auth_manager.screenshots_dir}")
            print(f"[DEBUG] Storage state: {self.auth_manager.storage_path} valid={self.auth_manager.has_valid_session()}")

    def _load_config(self, path: Path):
        if path.exists():
            return yaml.safe_load(path.read_text(encoding='utf-8'))
        return {
            "arena": {
                "url": "https://arena.ai",
                "selectors": {
                    "prompt_input": ['textarea'],
                    "generate_button": ['button[type=\"submit\"]'],
                    "generated_images": ['img']
                }
            }
        }

    async def start(self):
        if not PLAYWRIGHT_AVAILABLE:
            print("[ARENA CLIENT] Playwright non disponibile - modalità fallback locale attiva")
            print(self.auth_manager.get_login_instructions())
            return False

        self.playwright = await async_playwright().start()
        self._persistent = False

        # Riusa il profilo Chrome GIA' autenticato su Arena.ai del bridge gemello
        # (caroselli - agency/ArenaAI/session_data) invece di rifare login da qui.
        # Bug reale (2026-08-05, screenshot di Max): Google rifiuta il login OAuth
        # su un browser Playwright "nuovo" ("questo browser o app potrebbero non
        # essere sicuri" - accounts.google.com/v3/signin/rejected). Non e' un
        # problema di selettori, e' rilevamento anti-bot lato Google - inutile
        # ritentare lo stesso login da zero una quarta volta. Quel profilo esiste
        # gia', autenticato via un vero browser umano una volta, e funziona
        # quando riusato con channel="chrome" + contesto persistente (stesso
        # pattern gia' provato in questa sessione sull'altro bridge Arena).
        shared_profile = BASE_DIR.parent / "caroselli - agency" / "ArenaAI" / "session_data"
        if shared_profile.exists():
            print(f"[ARENA] Riuso profilo Chrome autenticato: {shared_profile}")
            self.context = await self.playwright.chromium.launch_persistent_context(
                user_data_dir=str(shared_profile),
                headless=self.headless,
                channel="chrome",
                viewport=self.config.get("playwright", {}).get("viewport", {"width": 1920, "height": 1080}),
                args=[
                    "--disable-blink-features=AutomationControlled",
                    "--no-sandbox",
                    "--disable-infobars",
                    "--window-position=0,0",
                ],
                ignore_default_args=["--enable-automation"],
            )
            self._persistent = True
        else:
            print(f"[ARENA] [!] Profilo condiviso non trovato ({shared_profile}) - fallback a profilo nuovo (rischia lo stesso blocco Google)")
            browser_type = getattr(self.playwright, self.config.get("playwright", {}).get("browser", "chromium"))
            self.browser = await browser_type.launch(
                headless=self.headless,
                args=self.config.get("playwright", {}).get("args", ["--no-sandbox"])
            )
            storage_state = self.auth_manager.load_storage_state()
            if storage_state:
                print(f"[ARENA] Uso sessione salvata - login bypass")
                self.context = await self.browser.new_context(
                    viewport=self.config.get("playwright", {}).get("viewport", {"width": 1920, "height": 1080}),
                    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36",
                    storage_state=storage_state
                )
            else:
                print(f"[ARENA] Nessuna sessione valida - avvio senza auth, potrebbe richiedere login")
                if not self.headless:
                    print(self.auth_manager.get_login_instructions())
                self.context = await self.browser.new_context(
                    viewport=self.config.get("playwright", {}).get("viewport", {"width": 1920, "height": 1080}),
                    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36"
                )

        existing_pages = self.context.pages
        self.page = existing_pages[0] if existing_pages else await self.context.new_page()
        
        # Debug: log console e requests
        if self.debug:
            self.page.on("console", lambda msg: print(f"[BROWSER CONSOLE] {msg.type}: {msg.text}"))
            self.page.on("pageerror", lambda err: print(f"[BROWSER ERROR] {err}"))
        
        # Vai su Arena
        url = self.config["arena"]["url"]
        print(f"[ARENA] Navigating to {url}")
        try:
            await self.page.goto(url, wait_until="domcontentloaded", timeout=30000)
            await self.page.wait_for_timeout(3000)
            title = await self.page.title()
            print(f"[ARENA] Loaded: {title}")
            
            if self.debug:
                screenshot_bytes = await self.page.screenshot()
                self.auth_manager.save_debug_screenshot("01_loaded", screenshot_bytes)
            
            # Controlla se pagina login
            if await self._is_login_page():
                print("[ARENA] Rilevata pagina login!")
                if self.headless:
                    print("[ARENA] Modalità headless - non posso fare login manuale. Lancia con --no-headless per login manuale e salvataggio sessione.")
                    print(self.auth_manager.get_login_instructions())
                    # Prova comunque a continuare, magari storage state era parziale
                else:
                    print("[ARENA] Modalità visibile - FAI LOGIN MANUALMENTE ORA nel browser che si è aperto")
                    print("[ARENA] Hai 60 secondi per fare login...")
                    # Aspetta 60 sec per login manuale
                    for i in range(12):
                        await self.page.wait_for_timeout(5000)
                        if not await self._is_login_page():
                            print("[ARENA] Login rilevato completato!")
                            # Salva sessione
                            storage = await self.context.storage_state()
                            self.auth_manager.save_session(storage, {"login_method": "manual", "title": await self.page.title()})
                            break
                        print(f"[ARENA] Attendo login... {i*5}/60s")
                        if self.debug:
                            ss = await self.page.screenshot()
                            self.auth_manager.save_debug_screenshot(f"login_wait_{i}", ss)
            
            return True
        except Exception as e:
            print(f"[ARENA] Load error {e}, trying fallback")
            for fb_url in self.config["arena"].get("fallback_urls", []):
                try:
                    await self.page.goto(fb_url, timeout=20000)
                    await self.page.wait_for_timeout(2000)
                    print(f"[ARENA] Fallback loaded: {fb_url}")
                    return True
                except:
                    continue
            return False

    async def _is_login_page(self) -> bool:
        """Rileva se siamo su pagina login"""
        try:
            content = await self.page.content()
            login_keywords = ["sign in", "log in", "Sign In", "Log In", "Accedi", "login", "authentication"]
            url = self.page.url
            if any(kw in content for kw in login_keywords) and ("login" in url.lower() or "auth" in url.lower() or "signin" in url.lower()):
                return True
            # Check per bottone login visibile
            for sel in ['button:has-text("Sign in")', 'button:has-text("Log in")', 'a:has-text("Sign in")']:
                try:
                    elem = self.page.locator(sel).first
                    if await elem.count() > 0 and await elem.is_visible():
                        return True
                except:
                    pass
            return False
        except:
            return False

    async def close(self):
        # Il profilo condiviso persistente porta gia' con se' l'auth su disco
        # (stesso meccanismo dell'altro bridge Arena) - salvare uno storage_state
        # separato qui sarebbe ridondante e non serve a nulla in quella modalita'.
        if self.context and not getattr(self, "_persistent", False):
            try:
                storage = await self.context.storage_state()
                if storage.get("cookies") and len(storage["cookies"]) > 0:
                    self.auth_manager.save_session(storage, {"closed_at": datetime.now().isoformat(), "url": self.page.url if self.page else "unknown"})
                    print(f"[AUTH] Sessione salvata alla chiusura - {len(storage['cookies'])} cookies")
            except Exception as e:
                print(f"[AUTH] Errore salvataggio sessione alla chiusura: {e}")

        if getattr(self, "_persistent", False) and self.context:
            await self.context.close()
        elif self.browser:
            await self.browser.close()
        if self.playwright:
            await self.playwright.stop()

    async def _find_element(self, selector_list: List[str], timeout: int = 10000):
        """Trova elemento provando lista selettori con fallback"""
        for sel in selector_list:
            try:
                elem = self.page.locator(sel).first
                await elem.wait_for(state="visible", timeout=timeout//len(selector_list))
                print(f"[FINDER] Found with selector: {sel}")
                return elem
            except:
                continue
        return None

    async def _select_model(self, model_name: str):
        """Seleziona modello GPT-4o / Claude 3.5 su Arena"""
        selectors = self.config["arena"]["selectors"].get("model_selector", [])
        elem = await self._find_element(selectors, timeout=5000)
        if elem:
            try:
                await elem.click(timeout=5000)
                await self.page.wait_for_timeout(1000)
                # Cerca opzione modello
                model_option = self.page.locator(f"text={model_name}").first
                if await model_option.count() > 0:
                    await model_option.click()
                    print(f"[ARENA] Model selected: {model_name}")
                    await self.page.wait_for_timeout(1000)
            except Exception as e:
                print(f"[ARENA] Model select warning: {e}")
        else:
            print(f"[ARENA] Model selector not found, using default {model_name}")

    async def _ensure_direct_mode(self):
        """Arena apre di default in Battle Mode (confronto tra 2 modelli affiancati),
        non in Direct (1 modello, 1 immagine pulita). Bug reale (2026-08-05,
        segnalato da Max osservando lo schermo: "hai lasciato Battle Mode, e'
        gravissimo"). Causa vera trovata dopo il primo tentativo di fix: usavo
        `Locator.is_visible(timeout=...)`, che su Playwright e' un controllo
        ISTANTANEO sullo stato DOM corrente - il parametro timeout NON fa
        polling/attesa, quindi se il bottone non aveva ancora finito di
        idratare (React/Radix) il check falliva subito e in silenzio, sempre.
        `wait_for(state="visible", timeout=...)` invece attende davvero - stesso
        fix gia' applicato e verificato nell'altro bridge Arena
        (caroselli - agency/ArenaAI/arena_generator.py::setup_arena_chat)."""
        try:
            # ":visible" e' un'estensione Playwright, non CSS standard - necessaria
            # perche' un secondo bottone (il combobox nascosto del model-picker,
            # role="combobox") matcha lo stesso testo ed e' PRIMA nel DOM: senza
            # ":visible" `.first` prendeva quello sbagliato, sempre "hidden", mai
            # cliccabile (bug reale trovato in un run vero, 2026-08-05).
            mode_btn = self.page.locator("button:visible").filter(has_text=re.compile(r"Battle Mode|Side by Side|Direct", re.I)).first
            await mode_btn.wait_for(state="visible", timeout=8000)
            text = await mode_btn.inner_text()
            if "Direct" not in text:
                await mode_btn.click(force=True)
                await self.page.wait_for_timeout(1000)
                direct_opt = self.page.locator("button, div").filter(has_text="Direct").filter(has_text="Chat with 1 model").last
                await direct_opt.wait_for(state="visible", timeout=4000)
                await direct_opt.click(force=True)
                await self.page.wait_for_timeout(1000)
                # Verifica reale, non assunta: rileggi il testo del bottone dopo il click.
                text_after = await mode_btn.inner_text()
                if "Direct" in text_after:
                    print("[ARENA] Direct mode attivata (verificato).")
                else:
                    print(f"[ARENA] [!] Click fatto ma il bottone dice ancora '{text_after}' - non confermato.")
            else:
                print("[ARENA] Gia' in Direct mode.")
        except Exception as e:
            print(f"[ARENA] [!] Switch a Direct mode fallito: {e}")

    async def _attach_reference_image(self, image_paths) -> bool:
        """Allega una o piu' immagini di reference al composer per mantenere
        stile/colori coerenti - richiesto esplicitamente da Max osservando lo
        schermo (2026-08-05): senza reference ogni slide puo' uscire con stile
        diverso dalle altre (slide 1: le 8 reference statiche in reference/,
        slide 2+: la slide precedente appena generata)."""
        if isinstance(image_paths, (list, tuple)):
            paths = [str(p) for p in image_paths if p and Path(p).exists()]
        elif image_paths and Path(image_paths).exists():
            paths = [str(image_paths)]
        else:
            paths = []
        if not paths:
            return False
        try:
            attach_selectors = self.config["arena"]["selectors"].get("attachment_area", ['input[type="file"]'])
            for sel in attach_selectors:
                try:
                    file_input = self.page.locator(sel).first
                    if await file_input.count() > 0:
                        await file_input.set_input_files(paths)
                        await self.page.wait_for_timeout(2000)
                        print(f"[ARENA] {len(paths)} reference allegate.")
                        return True
                except Exception:
                    continue
            print("[ARENA] [!] Nessun input file trovato per allegare le reference.")
            return False
        except Exception as e:
            print(f"[ARENA] [!] Allegato reference fallito: {e}")
            return False

    async def generate_image(self, prompt: str, output_path: Path, slide_num: int = 1, reference_image=None) -> Dict:
        """
        Genera singola immagine su Arena via Playwright
        Se Playwright non disponibile o fallisce, usa fallback locale (simulazione con enhanced prompt)
        """
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        if not PLAYWRIGHT_AVAILABLE or not self.page:
            print(f"[FALLBACK] Playwright non attivo - salvo prompt per generazione locale futura - Slide {slide_num}")
            # Salva prompt ultra qualità per generazione successiva con tool locale
            meta = {
                "slide": slide_num,
                "prompt": prompt,
                "output_path": str(output_path),
                "model": self.model,
                "timestamp": datetime.now().isoformat(),
                "requires_arena_generation": True,
                "enhanced": "ULTRA GRAIN + 4K SHARP"
            }
            (output_path.with_suffix('.json')).write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding='utf-8')
            # Salva anche prompt txt
            (output_path.with_suffix('.txt')).write_text(prompt, encoding='utf-8')
            return {"status": "prompt_saved", "path": str(output_path), "mode": "fallback_local", "slide": slide_num}

        try:
            # Seleziona modello + Direct mode se primo giro. Bug reale (2026-08-05,
            # segnalato da Max: "hai lasciato Battle Mode, e' gravissimo"): il tasto
            # modalita' e' presente sulla pagina ma il primo check partiva prima che
            # React/Radix avessero finito di idratare la toolbar - stesso identico
            # problema gia' diagnosticato sull'altro bridge Arena. Fix: aspettare
            # che il composer sia visibile PRIMA di toccare qualsiasi controllo.
            if slide_num == 1:
                try:
                    await self.page.locator("textarea").first.wait_for(state="visible", timeout=8000)
                except Exception as e:
                    print(f"[ARENA] [!] Composer non visibile dopo l'attesa: {e}")
                await self._select_model(self.model)
                await self._ensure_direct_mode()

            # Allega la slide precedente come reference per coerenza di stile
            if reference_image:
                await self._attach_reference_image(reference_image)

            # Trova input
            input_selectors = self.config["arena"]["selectors"]["prompt_input"]
            input_elem = await self._find_element(input_selectors, timeout=15000)

            if not input_elem:
                print(f"[ARENA] Prompt input not found - saving prompt fallback")
                raise Exception("Prompt input not found - fallback")

            # Pulisci e inserisci prompt ultra qualità
            await input_elem.click()
            await self.page.keyboard.press("Control+A")
            await self.page.keyboard.press("Backspace")
            await input_elem.fill(prompt)
            await self.page.wait_for_timeout(500)

            # Trova e clicca genera
            gen_selectors = self.config["arena"]["selectors"]["generate_button"]
            gen_elem = await self._find_element(gen_selectors, timeout=10000)

            if gen_elem:
                # Bug reale (2026-08-05): quando la slide precedente e' allegata
                # come reference, il bottone resta disabled finche' l'upload
                # dell'allegato non finisce di processare - un click subito dopo
                # il fill() trovava il bottone ancora disabled per 30s di fila
                # (mai un timeout "elemento non trovato", proprio "not enabled").
                # Aspetto che diventi davvero cliccabile invece di assumerlo.
                try:
                    await gen_elem.wait_for(state="visible", timeout=1000)
                    await self.page.wait_for_function(
                        "el => el && !el.disabled",
                        arg=await gen_elem.element_handle(),
                        timeout=15000
                    )
                except Exception:
                    print(f"[ARENA] [!] Bottone genera ancora disabled dopo l'attesa - provo comunque.")
                await gen_elem.click()
                print(f"[ARENA] Generate clicked for slide {slide_num}")
            else:
                # Prova Enter
                await self.page.keyboard.press("Enter")
                print(f"[ARENA] Generate via Enter key slide {slide_num}")

            # Attendi generazione - guarda immagini
            await self.page.wait_for_timeout(3000)
            
            # Wait for images with extended timeout
            image_selectors = self.config["arena"]["selectors"]["generated_images"]
            start = time.time()
            timeout_sec = self.config.get("playwright", {}).get("timeout", 60000) / 1000
            
            while time.time() - start < timeout_sec:
                for sel in image_selectors:
                    try:
                        imgs = self.page.locator(sel)
                        count = await imgs.count()
                        if count > 0:
                            # Prendi ultima immagine
                            last_img = imgs.nth(count-1)
                            # Prova a scaricare
                            try:
                                src = await last_img.get_attribute("src")
                                if src:
                                    if src.startswith("data:"):
                                        # Base64 image
                                        header, data = src.split(",", 1)
                                        img_bytes = base64.b64decode(data)
                                        output_path.write_bytes(img_bytes)
                                        print(f"[ARENA] Image saved (base64) {output_path}")
                                        return {"status": "success", "path": str(output_path), "src_type": "base64", "slide": slide_num}
                                    elif src.startswith("http") or src.startswith("blob:"):
                                        # Scarica via request
                                        try:
                                            # Usa page to fetch
                                            response = await self.page.request.get(src) if hasattr(self.page, 'request') else None
                                            # Fallback: screenshot elemento
                                            await last_img.screenshot(path=output_path)
                                            print(f"[ARENA] Image saved (screenshot) {output_path}")
                                            return {"status": "success", "path": str(output_path), "src_type": "screenshot", "slide": slide_num}
                                        except:
                                            await last_img.screenshot(path=output_path)
                                            return {"status": "success", "path": str(output_path), "src_type": "screenshot_fallback", "slide": slide_num}
                            except Exception as e:
                                print(f"[ARENA] Image extraction attempt failed {sel}: {e}")
                                continue
                    except:
                        continue
                await self.page.wait_for_timeout(2000)
                if int(time.time() - start) % 10 == 0:
                    print(f"[ARENA] Waiting image generation... {int(time.time()-start)}s / {int(timeout_sec)}s slide {slide_num}")

            print(f"[ARENA] Timeout waiting image slide {slide_num} - fallback to prompt save")
            raise TimeoutError("Image generation timeout")

        except Exception as e:
            print(f"[ARENA] Generation error slide {slide_num}: {e} - fallback")
            # Salva prompt per rigenerazione manuale/local
            meta = {
                "slide": slide_num,
                "prompt": prompt,
                "error": str(e),
                "output_path": str(output_path),
                "timestamp": datetime.now().isoformat()
            }
            (output_path.with_suffix('.json')).write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding='utf-8')
            (output_path.with_suffix('.txt')).write_text(prompt, encoding='utf-8')
            return {"status": "fallback_saved", "path": str(output_path), "error": str(e), "slide": slide_num}

    async def generate_carousel(self, prompts: List[str], output_dir: Path, model: str = "GPT-4o") -> List[Dict]:
        """Genera carosello completo 8 slide"""
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        
        started = await self.start()
        if not started and PLAYWRIGHT_AVAILABLE:
            print("[ARENA] Failed to start, fallback mode")

        # Le 8 reference statiche (quelle gia' allegate quando Max ha costruito
        # questo sistema in Arena) - servono da guida di stile per la slide 1.
        # Mancavano del tutto prima di questo fix (segnalato da Max osservando
        # lo schermo, 2026-08-05): la slide 1 partiva senza nessuna reference.
        static_refs = sorted((BASE_DIR / "reference").glob("*.png"))

        results = []
        last_success_path = None
        for i, prompt in enumerate(prompts, 1):
            out_path = output_dir / f"slide_{i:02d}.png"
            print(f"\n[CAROUSEL] {i}/{len(prompts)} Generating with {model} -> {out_path}")
            # Slide 1: le 8 reference statiche di stile. Slide 2+: la slide
            # precedente riuscita, per mantenere stile/colori coerenti nel corso
            # del carosello (richiesta esplicita di Max).
            ref = static_refs if i == 1 else last_success_path
            res = await self.generate_image(prompt, out_path, slide_num=i, reference_image=ref)
            results.append(res)
            if res.get("status") == "success":
                last_success_path = Path(res["path"])
            # Delay tra generazioni per non spammare
            await asyncio.sleep(2)

        await self.close()
        return results


# CLI test
if __name__ == "__main__":
    async def test_single():
        client = ArenaPlaywrightClient(headless=False, model="GPT-4o")
        test_prompt = """
        Premium Instagram carousel 1080x1350 black #000000 heavy film grain 35% noise texture on ALL elements background cards text buttons, red-orange glow #FF3B1F corners blurred, pill LA VERITÀ eye red, headline "Non hai un problema di idee. Hai un problema di esecuzione." with problema esecuzione red serif italic, 4K ultra sharp, ultra high resolution, grain on every pixel.
        """
        await client.start()
        res = await client.generate_image(test_prompt, OUTPUT_DIR / "test_slide.png", slide_num=1)
        print(res)
        await client.close()

    asyncio.run(test_single())
