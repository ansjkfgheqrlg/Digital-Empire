"""
Refresh sessione LinkedIn.
Apre il browser — aspetta finché l'utente è effettivamente nel feed, poi salva.
"""
import asyncio
import os
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE)
from config import SESSION_FILE

SESSION_PATH = os.path.join(BASE, SESSION_FILE)
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"


def is_feed_url(url: str) -> bool:
    """Controlla che l'URL sia DAVVERO il feed, non una pagina di login con 'feed' nel redirect."""
    return (
        url.startswith("https://www.linkedin.com/feed")
        or url.startswith("https://www.linkedin.com/mynetwork")
        or (url.startswith("https://www.linkedin.com/in/") and "login" not in url)
    )


async def main():
    from playwright.async_api import async_playwright

    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=False, args=["--start-maximized"])

        ctx_kwargs = {
            "viewport": {"width": 1280, "height": 800},
            "user_agent": UA,
        }
        if os.path.exists(SESSION_PATH):
            ctx_kwargs["storage_state"] = SESSION_PATH
            print(f"Sessione trovata: {SESSION_PATH}")
        else:
            print("Nessuna sessione salvata — login manuale richiesto.")

        ctx  = await browser.new_context(**ctx_kwargs)
        page = await ctx.new_page()

        print("Apro LinkedIn...")
        await page.goto("https://www.linkedin.com/feed/", wait_until="domcontentloaded")
        await asyncio.sleep(3)

        current_url = page.url
        print(f"URL corrente: {current_url}")

        if is_feed_url(current_url):
            print("Sessione valida — sei nel feed.")
        else:
            print()
            print("======================================================")
            print("  AZIONE RICHIESTA:")
            print("  Fai login LinkedIn nel browser aperto.")
            print("  Aspetta di essere nella HOME (feed con i post).")
            print("  Quando sei nel feed, aspettiamo automaticamente...")
            print("======================================================")

            # Attesa automatica: polling ogni 2s fino a 3 minuti
            for _ in range(90):
                await asyncio.sleep(2)
                current_url = page.url
                print(f"  Attendo... URL: {current_url[:60]}")
                if is_feed_url(current_url):
                    print("  Loggato! Salvo la sessione...")
                    break
            else:
                print("[ERRORE] Timeout — login non completato in 3 minuti.")
                await browser.close()
                sys.exit(1)

        await ctx.storage_state(path=SESSION_PATH)
        print(f"\nSessione salvata in: {SESSION_PATH}")
        await browser.close()
        print("OK — sessione valida. Puoi avviare run_parallel.py")


if __name__ == "__main__":
    asyncio.run(main())
