#!/usr/bin/env python3
"""
UN solo motore di sessione browser per Arena (TASK-ARENA-SESSION-W1).

Prima di questo modulo la stessa logica esisteva in tre copie divergenti, e ogni
copia aveva imparato lezioni che le altre due non sapevano:

  * `caroselli - agency/Core/browser_manager.py` — profilo persistente, ma
    NESSUN controllo di login, NESSUNA gestione della modale "Terms of Use",
    e un `import playwright_stealth` obbligatorio che oggi lo fa **morire
    all'import** (verificato 2026-08-27: playwright_stealth non e' installato,
    quindi il ramo Arena dei caroselli non parte proprio).
  * `YOUTUBE-AUTOMATION-FACTORY/.../arena_thumbnail.py` — la copia piu' matura:
    Chrome reale via CDP, ricerca della scheda giusta, attesa del login umano,
    "Agree"/"Accept Cookies", `domcontentloaded` invece di `networkidle`.
    Tutte lezioni pagate con bug reali, e tutte invisibili alle altre due copie.
  * `_archivio_automazione_modelli/lmarena_client.py` — archiviato.

Bug storici causati dalla duplicazione: profilo pieno che causava hang da 180 s
(CP-20260806-006), sessione non autenticata scoperta solo guardando uno
screenshot, modale "Terms of Use" mai gestita, timeout ripetuti per aver preso
`context.pages[0]` invece della scheda arena.ai.

Questo modulo NON e' un motore nuovo: e' la copia matura promossa a unica, con
le lezioni delle altre incorporate.

DUE MODI DI ATTACCARSI AL BROWSER
  - `cdp` (default): lancia il chrome.exe VERO come processo indipendente e ci
    si COLLEGA. La finestra sopravvive allo script, quindi un crash non si porta
    via la sessione di login appena fatta. Richiesta esplicita di Max (2026-08-06).
  - `persistente`: `launch_persistent_context` di Playwright. Piu' semplice, ma
    Playwright possiede la finestra e la chiude con se'. E' quello che usavano i
    caroselli; resta disponibile per non rompere chi lo vuole.

DIPENDENZE: solo `playwright`. `playwright_stealth` e' OPZIONALE e se manca il
modulo continua a funzionare dicendolo — una dipendenza estetica non deve
impedire a un motore di partire (e' esattamente il guasto che ha ucciso il ramo
Arena dei caroselli).
"""
from __future__ import annotations

import os
import subprocess
import sys
import time
import urllib.error
import urllib.request

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

ARENA_URL = "https://arena.ai"

CHROME_EXE_CANDIDATI = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    "/usr/bin/google-chrome",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
]

# Testi delle modali che Arena mostra prima di lasciar lavorare. Erano gestiti
# solo in arena_thumbnail.py: i caroselli ci sbattevano contro senza saperlo.
MODALI = [
    ("button", "Agree"),           # Terms of Use, primo utilizzo
    ("button", "I agree"),
    ("text", "Accept Cookies"),
    ("button", "Accept all"),
]

# Se uno di questi e' visibile, NON siamo autenticati.
SEGNI_LOGIN = [
    ("button", "Continue with Google"),
    ("button", "Sign in"),
    ("button", "Log in"),
]

# Cookie che Arena assegna a un utente ANONIMO: la sua presenza e' la prova
# che non c'e' nessun account collegato (verificato dal vivo il 2026-08-27 su
# due profili appena creati). Vale piu' di qualunque elemento della UI.
COOKIE_ANONIMO = {"provisional_user_id"}

# Frammenti di nome tipici di un cookie di sessione autenticata.
#
# LIMITE DICHIARATO, non nascosto: il ramo "autenticato" NON e' mai stato
# confermato contro un profilo Arena davvero loggato, perche' il 2026-08-27 non
# ne esisteva nessuno su questa macchina. Quello che e' stato verificato e' il
# ramo negativo: `arena-auth-prod-v1` compare ANCHE su un profilo anonimo, quindi
# da solo non prova niente ed e' per questo che COOKIE_ANONIMO ha la precedenza.
# In dubbio questo modulo risponde 'non_autenticato'/'ignoto': sbagliare per
# eccesso di prudenza costa un login inutile, sbagliare al contrario costa un run
# intero che muore a meta' — che e' il bug storico da cui nasce questa task.
COOKIE_SESSIONE = ("session", "jwt", "access_token", "sb-")

# Se uno di questi e' visibile, c'e' un captcha: non si "riprova piu' forte",
# si dice e si aspetta (regola dei REGOLE.md dei caroselli).
SEGNI_CAPTCHA = [
    "iframe[src*='recaptcha']",
    "iframe[title*='reCAPTCHA']",
    "text=Non sono un robot",
    "text=I'm not a robot",
]


class ArenaSession:
    """Sessione Arena condivisa. Un'istanza = un browser + la scheda di arena.ai.

    Uso tipico:
        s = ArenaSession(profilo_dir=..., modo="cdp")
        page = s.apri()
        if s.stato_login() != "autenticato":
            s.attendi_login()          # login umano una tantum
        ...
        s.chiudi()
    """

    def __init__(self, profilo_dir, modo="cdp", headless=False, cdp_port=9333,
                 url=ARENA_URL, stealth=True, log=print):
        self.profilo_dir = os.path.abspath(profilo_dir)
        self.modo = modo
        self.headless = headless
        self.cdp_port = cdp_port
        self.url = url
        self.stealth = stealth
        self.log = log
        self._pw = None
        self._browser = None
        self.context = None
        self.page = None
        os.makedirs(self.profilo_dir, exist_ok=True)

    # ------------------------------------------------------------------ avvio
    def _cdp_attivo(self) -> bool:
        try:
            urllib.request.urlopen(
                "http://localhost:%d/json/version" % self.cdp_port, timeout=2)
            return True
        except (urllib.error.URLError, OSError):
            return False

    def _avvia_chrome_reale(self):
        """Chrome VERO come processo indipendente, non posseduto da Playwright.

        Motivo (Max, 2026-08-06): con Playwright che lancia E chiude Chrome, ogni
        crash dello script si portava via la finestra e la sessione di login
        appena fatta, che non era ancora stata scritta su disco.
        """
        exe = next((p for p in CHROME_EXE_CANDIDATI if os.path.exists(p)), None)
        if not exe:
            raise RuntimeError("chrome.exe non trovato nei percorsi noti: %s"
                               % CHROME_EXE_CANDIDATI)
        args = [exe, "--remote-debugging-port=%d" % self.cdp_port,
                "--user-data-dir=%s" % self.profilo_dir, self.url]
        kwargs = {}
        if os.name == "nt":
            kwargs["creationflags"] = (subprocess.DETACHED_PROCESS
                                       | subprocess.CREATE_NEW_PROCESS_GROUP)
        subprocess.Popen(args, **kwargs)
        for _ in range(30):
            if self._cdp_attivo():
                return
            time.sleep(1)
        raise RuntimeError("Chrome avviato ma la porta di debug %d non risponde entro 30s."
                           % self.cdp_port)

    def avvia(self):
        """Avvia/riattacca SOLO il browser e restituisce il context, senza
        navigare da nessuna parte.

        Separato da `apri()` perche' i caroselli hanno gia' il loro codice di
        navigazione dentro `arena_generator.py`: a loro serve il context, non la
        pagina gia' portata su Arena. Wrappare senza cambiare il comportamento
        del consumatore e' la regola ADR-003.
        """
        if self.context is not None:
            return self.context
        from playwright.sync_api import sync_playwright
        self._pw = sync_playwright().start()

        if self.modo == "cdp":
            if not self._cdp_attivo():
                self.log("[arena] avvio Chrome reale (profilo: %s)" % self.profilo_dir)
                self._avvia_chrome_reale()
            else:
                self.log("[arena] riuso la finestra Chrome gia' aperta sulla porta %d"
                         % self.cdp_port)
            self._browser = self._pw.chromium.connect_over_cdp(
                "http://localhost:%d" % self.cdp_port)
            self.context = (self._browser.contexts[0] if self._browser.contexts
                            else self._browser.new_context())
        else:
            self.context = self._pw.chromium.launch_persistent_context(
                user_data_dir=self.profilo_dir,
                headless=self.headless,
                viewport={"width": 1280, "height": 900},
                channel="chrome",
                args=["--disable-blink-features=AutomationControlled",
                      "--disable-infobars"],
                ignore_default_args=["--enable-automation"],
                accept_downloads=True,
            )
        return self.context

    def apri(self, timeout_s=45):
        """Avvia il browser E porta la sessione sulla pagina di Arena, pronta."""
        self.avvia()
        self.page = self._trova_pagina(timeout_s=15)
        self._applica_stealth(self.page)
        # domcontentloaded, MAI networkidle: arena.ai ha traffico di rete continuo
        # che non si ferma mai: networkidle faceva scadere goto() dopo 30s
        # (bug reale 2026-08-06, stessa forma gia' vista su YouTube Studio).
        try:
            self.page.wait_for_load_state("domcontentloaded", timeout=timeout_s * 1000)
        except Exception:
            pass
        time.sleep(1.5)
        self.gestisci_modali()
        return self.page

    def _trova_pagina(self, timeout_s=15):
        """Cerca la scheda arena.ai fra quelle aperte, invece di assumere pages[0].

        Chrome apre spesso PIU' schede al lancio (una vuota + quella da riga di
        comando): prendere sempre la prima significava a volte guardare la scheda
        sbagliata e rilanciare goto() su una navigazione gia' in corso altrove —
        causa reale dei timeout ripetuti fra il 2026-08-06 e il 2026-08-09.
        """
        dominio = self.url.split("//")[-1].split("/")[0]
        scadenza = time.time() + timeout_s
        while time.time() < scadenza:
            for pg in self.context.pages:
                try:
                    if dominio in pg.url:
                        return pg
                except Exception:
                    continue
            time.sleep(0.5)
        pg = self.context.new_page()
        self._applica_stealth(pg)
        pg.goto(self.url, wait_until="domcontentloaded", timeout=30000)
        return pg

    def _applica_stealth(self, page):
        """Stealth se c'e', avviso se non c'e'. Mai un errore: vedi docstring."""
        if not self.stealth:
            return
        try:
            from playwright_stealth import Stealth
        except ImportError:
            if not getattr(self, "_avvisato_stealth", False):
                self.log("[arena] playwright_stealth non installato: proseguo senza "
                         "(non e' bloccante; per averlo: pip install playwright-stealth)")
                self._avvisato_stealth = True
            return
        try:
            Stealth().apply_stealth_sync(page)
        except Exception as e:
            self.log("[arena] stealth non applicato (%s): proseguo" % type(e).__name__)

    # ------------------------------------------------------- modali e sessione
    def gestisci_modali(self):
        """Chiude Terms of Use / cookie. Silenziosa se non ci sono."""
        chiuse = []
        for tipo, testo in MODALI:
            try:
                loc = (self.page.get_by_role("button", name=testo) if tipo == "button"
                       else self.page.get_by_text(testo, exact=True))
                if loc.first.is_visible(timeout=1200):
                    loc.first.click()
                    chiuse.append(testo)
                    time.sleep(0.8)
            except Exception:
                continue
        if chiuse:
            self.log("[arena] modali chiuse: %s" % ", ".join(chiuse))
        return chiuse

    def captcha_presente(self) -> bool:
        for sel in SEGNI_CAPTCHA:
            try:
                if self.page.locator(sel).first.is_visible(timeout=800):
                    return True
            except Exception:
                continue
        return False

    def evidenza_login(self) -> dict:
        """Le prove grezze su cui si basa il verdetto, cosi' e' controllabile."""
        prove = {"captcha": False, "segno_login_visibile": None,
                 "cookie_anonimo": False, "cookie_sessione": [], "input_chat": False}
        if self.page is None:
            return prove
        prove["captcha"] = self.captcha_presente()
        for tipo, testo in SEGNI_LOGIN:
            try:
                loc = (self.page.get_by_role("button", name=testo) if tipo == "button"
                       else self.page.get_by_text(testo, exact=True))
                if loc.first.is_visible(timeout=800):
                    prove["segno_login_visibile"] = testo
                    break
            except Exception:
                continue
        try:
            for c in self.context.cookies():
                nome = c.get("name", "")
                if nome in COOKIE_ANONIMO:
                    prove["cookie_anonimo"] = True
                elif any(k in nome.lower() for k in COOKIE_SESSIONE):
                    prove["cookie_sessione"].append(nome)
        except Exception:
            pass
        for sel in ["textarea", "div[contenteditable='true']", "[data-testid='chat-input']"]:
            try:
                if self.page.locator(sel).first.is_visible(timeout=800):
                    prove["input_chat"] = True
                    break
            except Exception:
                continue
        return prove

    def stato_login(self) -> str:
        """'autenticato' | 'non_autenticato' | 'login_richiesto' | 'captcha' | 'ignoto'.

        ATTENZIONE, lezione pagata due volte (2026-08-27): su arena.ai la casella
        di chat E' USABILE ANCHE DA SLOGGATI. La prima versione di questo metodo
        concludeva "autenticato" appena vedeva una `textarea`, e ha dichiarato
        autenticati due profili appena creati e vuoti — cioe' ha riprodotto
        esattamente il bug storico che questo modulo doveva impedire ("sessione
        non autenticata scoperta solo via screenshot"). Smascherato guardando lo
        screenshot e i cookie, non il DOM.

        Percio' ora il verdetto sta sui COOKIE, che non mentono:
          - `provisional_user_id` = utente anonimo -> NON autenticato;
          - un cookie di sessione vero -> autenticato;
          - in dubbio si risponde 'ignoto', mai 'autenticato'.
        """
        if self.page is None:
            return "ignoto"
        p = self.evidenza_login()
        if p["captcha"]:
            return "captcha"
        if p["cookie_anonimo"]:
            # DOMINANTE su tutto il resto. Verificato il 2026-08-27: un profilo
            # sloggato ha SIA `provisional_user_id` SIA `arena-auth-prod-v1` —
            # cioe' il cookie che "sembra" di autenticazione c'e' anche da
            # anonimi. L'unico segnale che non mente e' l'identita' provvisoria:
            # se Arena te ne ha assegnata una, non c'e' nessun account collegato.
            return "login_richiesto" if p["segno_login_visibile"] else "non_autenticato"
        if p["cookie_sessione"]:
            return "autenticato"
        if p["segno_login_visibile"]:
            return "login_richiesto"
        return "ignoto"

    def attendi_login(self, timeout_s=900) -> bool:
        """Aspetta che un umano faccia il login nella finestra aperta."""
        self.log("[arena] LOGIN RICHIESTO: fallo nella finestra Chrome aperta. "
                 "Attendo fino a %d minuti." % (timeout_s // 60))
        scadenza = time.time() + timeout_s
        while time.time() < scadenza:
            if self.stato_login() == "autenticato":
                self.log("[arena] login completato.")
                self.gestisci_modali()
                return True
            time.sleep(3)
        self.log("[arena] timeout: login non completato.")
        return False

    def screenshot(self, path) -> str | None:
        """Prova visiva dello stato. Una sessione non autenticata si e' scoperta
        una volta solo cosi': lo screenshot non e' un extra, e' la verifica."""
        try:
            os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
            self.page.screenshot(path=path)
            return path
        except Exception as e:
            self.log("[arena] screenshot non riuscito (%s)" % type(e).__name__)
            return None

    def nuova_chat(self):
        """Nuova chat pulita: e' la reazione giusta a un errore di Arena
        (REGOLE.md caroselli: mai insistere sulla stessa chat in errore)."""
        self.page.goto(self.url, wait_until="domcontentloaded", timeout=30000)
        time.sleep(1.5)
        self.gestisci_modali()
        return self.page

    # ------------------------------------------------------------------ uscita
    def chiudi(self, lascia_aperto=None):
        """In modo `cdp` la finestra resta aperta di proposito (e' di Max, non
        nostra: la chiude lui). In modo `persistente` si chiude tutto."""
        if lascia_aperto is None:
            lascia_aperto = (self.modo == "cdp")
        try:
            if not lascia_aperto and self.context is not None:
                self.context.close()
        except Exception:
            pass
        try:
            if self._pw is not None:
                self._pw.stop()
        except Exception:
            pass

    def __enter__(self):
        self.apri()
        return self

    def __exit__(self, *exc):
        self.chiudi()
        return False


def diagnosi(profilo_dir, modo="cdp", headless=False, screenshot_path=None):
    """Verifica onesta della sessione, senza generare niente.

    Serve ai due consumatori (e a chi debugga) per sapere se il browser parte e
    se la sessione e' autenticata, PRIMA di lanciare un run lungo.
    """
    s = ArenaSession(profilo_dir=profilo_dir, modo=modo, headless=headless)
    esito = {"modo": modo, "profilo": s.profilo_dir}
    try:
        s.apri()
        esito["url"] = s.page.url
        esito["stato"] = s.stato_login()
        if screenshot_path:
            esito["screenshot"] = s.screenshot(screenshot_path)
    except Exception as e:
        esito["stato"] = "errore"
        esito["errore"] = "%s: %s" % (type(e).__name__, str(e)[:200])
    finally:
        s.chiudi()
    return esito


if __name__ == "__main__":
    import argparse
    import json

    ap = argparse.ArgumentParser(description="Diagnosi della sessione Arena condivisa")
    ap.add_argument("--profilo", required=True)
    ap.add_argument("--modo", choices=["cdp", "persistente"], default="cdp")
    ap.add_argument("--headless", action="store_true")
    ap.add_argument("--screenshot")
    a = ap.parse_args()
    print(json.dumps(diagnosi(a.profilo, a.modo, a.headless, a.screenshot),
                     ensure_ascii=False, indent=2))
