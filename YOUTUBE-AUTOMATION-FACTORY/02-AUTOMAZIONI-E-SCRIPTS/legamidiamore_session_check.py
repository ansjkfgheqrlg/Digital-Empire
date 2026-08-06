#!/usr/bin/env python3
"""
Diagnostica: la sessione salvata in chrome-profile-legamidiamore e' ancora valida?

Le sessioni Google scadono (logout remoto, cambio password, "esci da tutti i dispositivi",
inattivita' prolungata). Prima di questo script, l'unico modo per saperlo era lanciare
un'automazione reale e scoprire a meta' che il login e' scaduto — spreco di tempo su un
canale vero. Questo script risponde SOLO alla domanda "posso operare?", headless, in pochi
secondi, senza toccare nulla sul canale.

Uso:
    python legamidiamore_session_check.py            # controllo silenzioso, solo output
    python legamidiamore_session_check.py --visibile  # se FALLITO, riapre la finestra per
                                                        # rifare il login a mano

Codici di uscita: 0 = sessione valida, 1 = sessione scaduta/assente (serve nuovo login),
2 = errore imprevisto (rete, layout cambiato — non e' detto che la sessione sia morta).
"""
import os
import sys
import subprocess

from playwright.sync_api import sync_playwright

if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)
    sys.stderr.reconfigure(encoding="utf-8", line_buffering=True)

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
FACTORY_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
PROFILE_DIR = os.path.join(FACTORY_DIR, "chrome-profile-legamidiamore")

# Bug reale trovato il 2026-08-05: senza uno User-Agent esplicito, il Chromium di Playwright
# si identifica in un modo che YouTube Studio segna come "browser non supportato" e mostra un
# interstiziale ("Improve your experience" + link "SKIP TO YOUTUBE STUDIO") AL POSTO della
# dashboard — anche con sessione perfettamente valida (nessun redirect al login). Il primo
# giro di questo script lo leggeva come sessione scaduta: falso negativo puro, non un problema
# di login. Fix alla radice: uno User-Agent Chrome desktop reale evita l'interstiziale del
# tutto. Click di riserva sotto, nel caso ricompaia su una versione futura di Chromium.
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"


def sessione_valida() -> tuple[bool, str]:
    if not os.path.exists(PROFILE_DIR):
        return False, "Nessun profilo trovato: login mai fatto. Lancia legamidiamore_login.py."

    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir=PROFILE_DIR, headless=True,
            viewport={"width": 1440, "height": 900},
            user_agent=USER_AGENT,
        )
        page = context.pages[0] if context.pages else context.new_page()
        try:
            # domcontentloaded, non networkidle: Studio ha traffico di rete continuo
            # (analytics/polling) che non si ferma mai davvero — "networkidle" ha fatto
            # scadere goto() stesso dopo 30s (Timeout, non un mancato login). Il caricamento
            # del contenuto reale si aspetta DOPO, sul testo, non sulla rete.
            page.goto("https://studio.youtube.com", wait_until="domcontentloaded", timeout=30000)
            # Riserva: se l'interstiziale ricompare comunque, il link "Skip" lo scavalca senza
            # bisogno di un browser diverso.
            try:
                page.get_by_text("SKIP TO YOUTUBE STUDIO", exact=False).click(timeout=3000)
            except Exception:
                pass
            # Se la sessione e' scaduta, Studio reindirizza a accounts.google.com/signin.
            # Se e' valida, la dashboard reale compare entro pochi secondi. Selettore per TESTO
            # visibile ("Channel dashboard"), non per id/classe interna: verificato con
            # screenshot reale che `ytcp-header`/`#entity-name` non esistono piu' nel DOM
            # attuale di Studio (bug reale trovato il 2026-08-05, stesso tipo di selector-rot
            # gia' documentato in youtube_hunter_playwright.py per le pagine pubbliche).
            try:
                page.get_by_text("Channel dashboard", exact=False).first.wait_for(state="visible", timeout=20000)
                return True, f"Sessione valida — {page.title()}"
            except Exception:
                url_attuale = page.url
                if "accounts.google.com" in url_attuale or "signin" in url_attuale:
                    return False, f"Sessione scaduta: reindirizzato al login ({url_attuale[:80]})."
                return False, f"Dashboard non trovata, URL inatteso: {url_attuale[:80]}."
        finally:
            context.close()


def main():
    visibile = "--visibile" in sys.argv
    try:
        valida, motivo = sessione_valida()
    except Exception as e:
        print(f"[!] Errore imprevisto durante il controllo: {e}")
        sys.exit(2)

    simbolo = "🟢" if valida else "🔴"
    print(f"{simbolo} {motivo}")

    if valida:
        sys.exit(0)

    print("[!] Serve un nuovo login. " + ("Rilancio legamidiamore_login.py..." if visibile else
          "Rilancia con --visibile per rifarlo subito, o `python legamidiamore_login.py`."))
    if visibile:
        subprocess.run([sys.executable, os.path.join(SCRIPT_DIR, "legamidiamore_login.py")])
    sys.exit(1)


if __name__ == "__main__":
    main()
