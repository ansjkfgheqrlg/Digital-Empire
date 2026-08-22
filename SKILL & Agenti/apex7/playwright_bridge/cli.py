#!/usr/bin/env python3
"""
CLI per /inizio-generazione - Entry point per Claude Code

Claude Code user digita: /inizio-generazione
Questo script gestisce flusso conversazionale e genera carosello

Uso diretto:
python -m playwright_bridge.cli --topic "Content Factory per e-commerce"

Uso interattivo (simula comando /inizio-generazione):
python -m playwright_bridge.cli --interactive

Integrazione Claude Code:
- Copia questo file in ~/.claude/commands/ o usa come custom command
- Registra skill in skills/claude-code-bridge/SKILL.md
"""

import argparse
import asyncio
import sys
import os
from pathlib import Path
import json

# Console Windows di default e' cp1252 - crasha su box-drawing/emoji nel banner
# e nei messaggi di stato. Bug reale trovato in un run vero (2026-08-05).
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

# Aggiungi parent path
sys.path.insert(0, str(Path(__file__).parent.parent))

from playwright_bridge.carousel_flow import CarouselFlow

BANNER = """
╔════════════════════════════════════════════════════════════════╗
║                                                                ║
║   Digital Empire - Content Factory Carousel Generator          ║
║   Comando: /inizio-generazione                                 ║
║   Bridge Playwright per Claude Code (Arena.ai)                 ║
║                                                                ║
╚════════════════════════════════════════════════════════════════╝
"""

async def run_interactive(model: str = "GPT-4o", headless: bool = True, use_playwright: bool = True):
    print(BANNER)
    print("🎯 Comando /inizio-generazione attivato\n")
    print("Questo workflow collega Claude Code -> Playwright -> Arena.ai")
    print("per generare caroselli 1080x1350 con grana ultra quality su ogni elemento + 4K nitida.\n")
    
    # Step 1: Chiedi argomento
    print("━" * 70)
    print("👋 Ciao! Sono la Content Factory di Digital Empire.")
    print("   Aspetto che tu mi dica l'argomento del carosello...\n")
    topic = input("📌 Argomento (es. 'Content Factory per coach', 'Sistema AI per concessionari'): ").strip()
    
    if not topic:
        print("❌ Argomento vuoto, uso default 'Content Factory per imprenditori'")
        topic = "Content Factory per imprenditori"
    
    print(f"\n✅ Argomento ricevuto: '{topic}'")
    print(f"   Modello: {model} | Playwright: {'attivo' if use_playwright else 'fallback locale'} | Headless: {headless}\n")
    
    flow = CarouselFlow(model=model, headless=headless, use_playwright=use_playwright)
    
    # Step 2-4: Full flow
    report = await flow.run_full_flow(topic, model=model, use_playwright=use_playwright)
    
    # Step 5: Download ready
    print("\n" + "━" * 70)
    print("📦 CAROSELLO PRONTO PER DOWNLOAD")
    print("━" * 70)
    print(f"Topic: {report['topic']}")
    print(f"Slides: {report['total_slides']} x 1080x1350 (4K source 2160x2700 ultra sharp)")
    print(f"Qualità: {report['quality']}")
    print(f"Output dir: {report['output_dir']}")
    print(f"ZIP: {report['zip_path']}")
    print("\nContenuto ZIP:")
    for slide in report['slides']:
        print(f"  - slide_{slide['slide_num']:02d}.png + prompt + copy")
    print(f"\nScarica: {report['zip_path']}")
    print(f"Poi importa su Claude: il workspace contiene tutto in outputs/carousel/\n")
    print("✨ Fatto! Installa questo workspace su Claude Code e lancia /inizio-generazione per generare altri.\n")

async def run_direct(topic: str, model: str = "GPT-4o", headless: bool = True, use_playwright: bool = True, output_dir: Path = None):
    print(BANNER)
    print(f"🎯 /inizio-generazione - Topic: {topic} Model: {model}\n")
    flow = CarouselFlow(model=model, headless=headless, use_playwright=use_playwright)
    report = await flow.run_full_flow(topic, output_dir=output_dir, model=model, use_playwright=use_playwright)
    print(f"\n✅ Done: {report['zip_path']}")
    return report

def main():
    parser = argparse.ArgumentParser(description="Digital Empire - /inizio-generazione carousel generator via Playwright + Arena.ai")
    parser.add_argument("--topic", type=str, help="Argomento carosello (es. 'Content Factory per coach')")
    parser.add_argument("--model", type=str, default="GPT-4o", choices=["GPT-4o", "Claude 3.5 Sonnet"], help="Modello Arena.ai")
    parser.add_argument("--interactive", action="store_true", help="Modalità interattiva - simula /inizio-generazione con attesa argomento")
    parser.add_argument("--headless", action="store_true", default=True, help="Browser headless (default true)")
    parser.add_argument("--no-headless", action="store_true", help="Mostra browser Playwright per debug")
    parser.add_argument("--no-playwright", action="store_true", help="Disabilita Playwright - genera solo prompt (fallback locale)")
    parser.add_argument("--output", type=str, help="Output dir custom")
    parser.add_argument("--debug", action="store_true", help="Debug mode - screenshot + console log + auth debug")
    parser.add_argument("--login", action="store_true", help="Forza login manuale - apre browser visibile per fare login su Arena.ai e salva sessione")
    parser.add_argument("--clear-auth", action="store_true", help="Cancella sessione salvata (logout)")
    parser.add_argument("--check-auth", action="store_true", help="Verifica se sessione salvata è valida")
    parser.add_argument("command", nargs="?", help="Comando diretto: /inizio-generazione o /inzio-generazione per avviare fase generazione")
    
    args = parser.parse_args()
    
    # Gestione comandi /inizio-generazione e /inzio-generazione (typo supportato)
    if args.command and args.command.strip() in ["/inizio-generazione", "/inzio-generazione", "/inizio-carosello", "/genera-carosello"]:
        print(f"[COMMAND] Rilevato comando {args.command} - avvio fase generazione...")
        args.interactive = True
    
    headless = not args.no_headless
    # Se --login, forza no-headless
    if args.login:
        headless = False
        print("[AUTH] Modalità login forzata - browser visibile per login manuale")
    
    use_playwright = not args.no_playwright
    output_dir = Path(args.output) if args.output else None

    # Gestione auth commands
    if args.clear_auth:
        from playwright_bridge.auth_manager import AuthManager
        AuthManager().clear_session()
        print("[AUTH] Sessione cancellata")
        return
    
    if args.check_auth:
        from playwright_bridge.auth_manager import AuthManager
        auth = AuthManager()
        valid = auth.has_valid_session()
        print(f"[AUTH] Sessione valida: {valid}")
        if valid:
            print(f"[AUTH] Storage: {auth.storage_path}")
            print(f"[AUTH] Meta: {auth.meta_path.read_text(encoding='utf-8') if auth.meta_path.exists() else 'no meta'}")
        else:
            print(auth.get_login_instructions())
        return
    
    if args.login:
        # Login flow dedicato. Bug reale trovato in un run vero (2026-08-05): il
        # vecchio timer fisso a 120s si chiudeva e salvava la sessione a
        # prescindere da un login vero completato o no (2 run, 12 poi 6 cookie
        # salvati = mai autenticato). Ora rileva davvero la fine del login
        # (modal "Log In or Create Account" sparito) invece di aspettare alla
        # cieca, e da' fino a 400s invece di 120 - un login Google con
        # eventuale 2FA puo' richiedere piu' di 2 minuti.
        async def login_flow():
            from playwright_bridge.arena_client import ArenaPlaywrightClient
            client = ArenaPlaywrightClient(headless=False, model=args.model, debug=True)
            await client.start()
            print("[LOGIN] Fai login manualmente nel browser aperto (Google o email).")
            print("[LOGIN] Rilevo da solo quando hai finito - non serve chiudere il browser.")

            timeout_sec = 400
            waited = 0
            poll = 5
            login_done = False
            while waited < timeout_sec:
                if not client.page or client.page.is_closed():
                    print("[LOGIN] Browser chiuso manualmente.")
                    break
                try:
                    modal = client.page.get_by_text("Log In or Create Account", exact=False).first
                    if not await modal.is_visible(timeout=1500):
                        login_done = True
                        break
                except Exception:
                    login_done = True
                    break
                await asyncio.sleep(poll)
                waited += poll
                if waited % 30 == 0:
                    print(f"[LOGIN] In attesa... {waited}/{timeout_sec}s (ancora sulla schermata di login)")

            if login_done:
                print("[LOGIN] Login rilevato (schermata di login sparita).")
            else:
                print(f"[LOGIN] [!] Timeout {timeout_sec}s raggiunto senza rilevare login completato.")

            if client.page and not client.page.is_closed():
                await asyncio.sleep(2)  # lascia respirare eventuali redirect/cookie di sessione
            await client.close()
            print("[LOGIN] Sessione salvata in playwright_bridge/auth/ - verifica con --check-auth")

        asyncio.run(login_flow())
        return
    
    # Debug flag passato a client via env o direttamente
    if args.debug:
        os.environ["DEBUG"] = "1"
    
    if args.interactive or not args.topic:
        asyncio.run(run_interactive(model=args.model, headless=headless, use_playwright=use_playwright))
    else:
        asyncio.run(run_direct(topic=args.topic, model=args.model, headless=headless, use_playwright=use_playwright, output_dir=output_dir))

if __name__ == "__main__":
    main()
