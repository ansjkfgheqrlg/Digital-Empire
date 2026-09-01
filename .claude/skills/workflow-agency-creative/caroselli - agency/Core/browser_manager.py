"""
BrowserManager dei caroselli Agency — ora un ADATTATORE sottile sopra il motore
di sessione condiviso `shared/arena_session.py` (TASK-ARENA-SESSION-W1).

L'API pubblica NON cambia: `BrowserManager(nome, headless)`, `.get_context()`,
`.new_page(context)`, `.close()`. `ArenaAI/arena_generator.py`,
`read_arena_chat.py`, `setup_arena_session.py` e `debug_arena.py` continuano a
funzionare senza una riga modificata (ADR-003: si wrappa, non si riscrive).

COSA CAMBIA DAVVERO, e perche':

1. **Non muore piu' all'import.** Prima qui c'era `from playwright_stealth import
   Stealth` a livello di modulo: `playwright_stealth` NON e' installato su questa
   macchina (verificato 2026-08-27), quindi il ramo Arena dei caroselli falliva
   all'import, prima di eseguire una riga. Ora lo stealth e' opzionale: se c'e'
   si applica, se manca lo dice e prosegue. Una dipendenza estetica non deve
   impedire a un motore di partire.

2. **Eredita le lezioni dell'altra copia.** Gestione della modale "Terms of Use"
   e dei cookie, ricerca della scheda giusta invece di `pages[0]`, controllo di
   login esplicito, rilevamento captcha: tutte cose che esistevano solo in
   `YOUTUBE-AUTOMATION-FACTORY/.../arena_thumbnail.py` e che qui mancavano —
   ed erano bug gia' pagati (CP-20260806-006).

3. **Si puo' chiedere lo stato della sessione** invece di dedurlo: `.stato_login()`.
   Una sessione non autenticata era stata scoperta, una volta, solo guardando uno
   screenshot a mano.

Il default resta `modo="persistente"`, cioe' il comportamento storico di questa
cartella (Playwright possiede la finestra, profilo in `<piattaforma>/session_data`):
consolidare non deve voler dire cambiare di nascosto come gira la produzione.
"""
import os
import sys

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if root_dir not in sys.path:
    sys.path.append(root_dir)

# Radice del monorepo: 5 livelli sopra questo file
#   caroselli - agency/Core/browser_manager.py
#   -> caroselli - agency -> Workflow agency creative -> SKILL & Agenti -> <radice>
_REPO = os.path.abspath(os.path.join(root_dir, "..", "..", ".."))
if _REPO not in sys.path:
    sys.path.insert(0, _REPO)

from shared.arena_session import ArenaSession  # noqa: E402


class BrowserManager:
    """Adattatore: stessa firma di prima, motore condiviso sotto."""

    def __init__(self, platform_name, headless=False, modo="persistente"):
        self.platform_name = platform_name
        self.headless = headless
        self.platform_dir = os.path.join(root_dir, platform_name)
        self.session_dir = os.path.join(self.platform_dir, "session_data")
        self.sessione = ArenaSession(
            profilo_dir=self.session_dir,
            modo=modo,
            headless=headless,
        )

    def get_context(self):
        """Context del browser persistente per la piattaforma (API invariata)."""
        return self.sessione.avvia()

    def new_page(self, context=None):
        """Nuova pagina con stealth applicato se disponibile (API invariata)."""
        ctx = context if context is not None else self.sessione.avvia()
        page = ctx.new_page()
        self.sessione._applica_stealth(page)
        return page

    # -- aggiunte, non sostituzioni: nessun chiamante esistente le usa gia' --
    def stato_login(self, page=None):
        """'autenticato' | 'login_richiesto' | 'captcha' | 'ignoto'."""
        if page is not None:
            self.sessione.page = page
        return self.sessione.stato_login()

    def gestisci_modali(self, page=None):
        """Chiude Terms of Use / cookie di Arena. Prima non lo faceva nessuno qui."""
        if page is not None:
            self.sessione.page = page
        return self.sessione.gestisci_modali()

    def close(self):
        self.sessione.chiudi(lascia_aperto=False)
