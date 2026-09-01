import os
from playwright.sync_api import sync_playwright

class BrowserManager:
    def __init__(self, headless=False):
        self.headless = headless
        self.session_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'session_data')
        
        # Crea la cartella per le sessioni se non esiste
        if not os.path.exists(self.session_dir):
            os.makedirs(self.session_dir)

    def get_context(self, platform_name):
        """Restituisce un context del browser persistente per la piattaforma specificata (es. 'instagram' o 'tiktok')"""
        user_data_dir = os.path.join(self.session_dir, platform_name)
        
        # Avvia playwright
        self.playwright = sync_playwright().start()
        
        # Usa un context persistente. I cookie e i dati locali vengono salvati qui.
        self.browser_context = self.playwright.chromium.launch_persistent_context(
            user_data_dir=user_data_dir,
            headless=self.headless,
            viewport={'width': 1280, 'height': 720},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        
        return self.browser_context

    def close(self):
        """Chiude il context e playwright"""
        if hasattr(self, 'browser_context'):
            self.browser_context.close()
        if hasattr(self, 'playwright'):
            self.playwright.stop()
