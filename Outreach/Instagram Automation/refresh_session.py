"""
Instagram — Salva sessione browser
===================================
Apre il browser con la sessione salvata.
Se già loggato → risalva e chiude.
Se non loggato → aspetta login manuale, poi salva.

(Stesso comportamento del LinkedIn refresh_session.py)

Uso:
    cd "c:\\Users\\Utente\\Desktop\\qui tutto\\Digital Empire\\Outreach"
    python "Instagram Automation\\refresh_session.py"
"""
import asyncio
import os

BASE         = os.path.dirname(os.path.abspath(__file__))
SESSION_FILE = os.path.join(BASE, "instagram_session.json")

UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/124.0.0.0 Safari/537.36"
)


async def main():
    from playwright.async_api import async_playwright

    print()
    print("=" * 60)
    print("  INSTAGRAM — REFRESH SESSIONE")
    print("=" * 60)

    async with async_playwright() as pw:
        browser = await pw.chromium.launch(
            headless=False,
            args=["--start-maximized"],
        )

        # Carica sessione esistente se disponibile
        ctx_kwargs = {
            "viewport":   {"width": 1280, "height": 800},
            "user_agent": UA,
        }
        if os.path.exists(SESSION_FILE):
            ctx_kwargs["storage_state"] = SESSION_FILE
            print(f"  Sessione trovata: {SESSION_FILE}")
        else:
            print("  Nessuna sessione salvata — login manuale richiesto.")

        ctx  = await browser.new_context(**ctx_kwargs)
        page = await ctx.new_page()

        print("  Apro Instagram...")
        await page.goto("https://www.instagram.com/", wait_until="domcontentloaded")
        await asyncio.sleep(4)

        current_url = page.url

        # Controlla se siamo già loggati
        is_logged_in = (
            "instagram.com" in current_url
            and "accounts/login" not in current_url
            and "accounts/suspended" not in current_url
        )

        # Verifica più precisa: cerca elementi dell'interfaccia loggata
        if is_logged_in:
            nav_check = await page.evaluate("""
                () => !!document.querySelector('svg[aria-label="Home"], svg[aria-label="Casa"]')
                   || !!document.querySelector('[aria-label="Direct"], [aria-label="Messaggi diretti"]')
            """)
            is_logged_in = nav_check

        if is_logged_in:
            print("  Sessione valida — sei già loggato.")
        else:
            print()
            print("  Non sei loggato.")
            print("  1. Fai login con le tue credenziali nel browser")
            print("  2. Completa eventuale verifica 2FA / captcha")
            print("  3. Quando sei nella HOME di Instagram, torna qui e premi INVIO")
            print()
            loop = asyncio.get_event_loop()
            await loop.run_in_executor(None, lambda: input("  >> Premi INVIO dopo il login...\n"))

        # Salva sessione aggiornata
        await ctx.storage_state(path=SESSION_FILE)
        print(f"\n  ✓ Sessione salvata: {SESSION_FILE}")
        await browser.close()

    print()
    print("  Ora puoi lanciare: python run_parallel.py")
    print()


if __name__ == "__main__":
    asyncio.run(main())
