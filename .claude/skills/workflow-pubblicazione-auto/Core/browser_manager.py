import os
import sys

# Aggiungi il percorso root al sys.path per permettere le importazioni relative
root_dir = os.path.dirname(os.path.dirname(__file__))
if root_dir not in sys.path:
    sys.path.append(root_dir)

from playwright.sync_api import sync_playwright

class BrowserManager:
    def __init__(self, platform_name, headless=False):
        self.headless = headless
        self.platform_name = platform_name
        
        # Le sessioni verranno salvate dentro la cartella della piattaforma specifica
        self.platform_dir = os.path.join(root_dir, platform_name)
        self.session_dir = os.path.join(self.platform_dir, 'session_data')
        
        if not os.path.exists(self.session_dir):
            os.makedirs(self.session_dir)

    def get_context(self):
        """Restituisce un context del browser persistente per la piattaforma"""
        self.playwright = sync_playwright().start()
        
        self.browser_context = self.playwright.chromium.launch_persistent_context(
            user_data_dir=self.session_dir,
            headless=self.headless,
            viewport={'width': 1280, 'height': 720},
            channel="chrome",  # Usa il Chrome reale installato nel PC per bypassare i blocchi
            args=["--disable-blink-features=AutomationControlled"], # Nasconde l'automazione a Google
            ignore_default_args=["--enable-automation"] # Rimuove la scritta "Il browser è controllato da un software automatizzato"
        )
        
        return self.browser_context

    def close(self):
        """Chiude il context e playwright"""
        if hasattr(self, 'browser_context'):
            self.browser_context.close()
        if hasattr(self, 'playwright'):
            self.playwright.stop()
