"""
APEX-7 Auth Manager - Gestione login sessioni persistenti per Arena.ai
Salva cookies, localStorage, sessionStorage per evitare login ripetuti
"""

from pathlib import Path
from datetime import datetime, timedelta
import json
import os

BASE_DIR = Path(__file__).parent.parent
AUTH_DIR = BASE_DIR / "playwright_bridge" / "auth"
AUTH_DIR.mkdir(parents=True, exist_ok=True)

STORAGE_STATE_PATH = AUTH_DIR / "arena_storage_state.json"
SESSION_META_PATH = AUTH_DIR / "session_meta.json"
SCREENSHOTS_DIR = AUTH_DIR / "debug_screenshots"
SCREENSHOTS_DIR.mkdir(exist_ok=True)

class AuthManager:
    def __init__(self):
        self.storage_path = STORAGE_STATE_PATH
        self.meta_path = SESSION_META_PATH
        self.screenshots_dir = SCREENSHOTS_DIR

    def has_valid_session(self) -> bool:
        """Controlla se esiste sessione salvata e non scaduta"""
        if not self.storage_path.exists():
            print("[AUTH] Nessuna sessione salvata")
            return False
        
        if not self.meta_path.exists():
            print("[AUTH] Meta sessione mancante - considerata scaduta")
            return False
        
        try:
            meta = json.loads(self.meta_path.read_text(encoding='utf-8'))
            expires_str = meta.get("expires_at")
            if expires_str:
                expires = datetime.fromisoformat(expires_str)
                if datetime.now() > expires:
                    print(f"[AUTH] Sessione scaduta il {expires}")
                    return False
                print(f"[AUTH] Sessione valida fino a {expires} (login: {meta.get('login_at')})")
                return True
            # Se non ha scadenza, considera valida 7 giorni dal file mtime
            mtime = datetime.fromtimestamp(self.storage_path.stat().st_mtime)
            if datetime.now() - mtime > timedelta(days=7):
                print(f"[AUTH] Sessione troppo vecchia ({mtime})")
                return False
            print(f"[AUTH] Sessione valida (mtime {mtime})")
            return True
        except Exception as e:
            print(f"[AUTH] Errore verifica sessione: {e}")
            return False

    def save_session(self, storage_state: dict, user_info: dict = None):
        """Salva storage state di Playwright su disco"""
        self.storage_path.write_text(json.dumps(storage_state, indent=2), encoding='utf-8')
        
        meta = {
            "login_at": datetime.now().isoformat(),
            "expires_at": (datetime.now() + timedelta(days=7)).isoformat(),
            "user_info": user_info or {},
            "storage_path": str(self.storage_path),
            "version": "2.0-ultra-grain"
        }
        self.meta_path.write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding='utf-8')
        print(f"[AUTH] Sessione salvata in {self.storage_path} - valida 7 giorni")

    def load_storage_state(self) -> dict | None:
        """Carica storage state se valido"""
        if not self.has_valid_session():
            return None
        try:
            data = json.loads(self.storage_path.read_text(encoding='utf-8'))
            print(f"[AUTH] Storage state caricato da {self.storage_path}")
            return data
        except Exception as e:
            print(f"[AUTH] Errore caricamento storage: {e}")
            return None

    def clear_session(self):
        """Cancella sessione (logout)"""
        if self.storage_path.exists():
            self.storage_path.unlink()
        if self.meta_path.exists():
            self.meta_path.unlink()
        print("[AUTH] Sessione cancellata - necessario nuovo login")

    def save_debug_screenshot(self, name: str, image_bytes: bytes = None):
        """Salva screenshot debug"""
        path = self.screenshots_dir / f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_{name}.png"
        if image_bytes:
            path.write_bytes(image_bytes)
        return path

    def get_login_instructions(self) -> str:
        return """
[AUTH] LOGIN RICHIESTO PER ARENA.AI

Arena.ai potrebbe richiedere login. Ecco come procedere:

1. MODALITÀ MANUALE (consigliata prima volta):
   - Lancia: python -m playwright_bridge.cli --topic "test login" --no-headless --no-playwright=false
   - Si aprirà browser Chromium visibile
   - Fai login manualmente su Arena.ai (Google, GitHub, etc)
   - Una volta loggato e vedi chat pronta, chiudi browser - la sessione verrà salvata automaticamente in auth/arena_storage_state.json
   - Prossime volte userà sessione salvata, niente più login

2. MODALITÀ AUTO con storage salvato:
   - Se hai già fatto login una volta, la sessione è salvata
   - Prossime esecuzioni: python -m playwright_bridge.cli --topic "..." --headless
   - Carica storage_state.json automaticamente, niente login

3. SE SESSIONE SCADUTA:
   - Cancella: rm playwright_bridge/auth/arena_storage_state.json
   - Rifai login manuale con --no-headless

4. ENV VARS (se Arena usa API key):
   export ARENA_API_KEY=sk-...
   export ARENA_EMAIL=tuo@email.com
   export ARENA_PASSWORD=...

Sessione salvata dura 7 giorni, poi richiede re-login.
Debug screenshots in playwright_bridge/auth/debug_screenshots/
"""

# Test
if __name__ == "__main__":
    auth = AuthManager()
    print(f"Has valid session: {auth.has_valid_session()}")
    print(auth.get_login_instructions())
