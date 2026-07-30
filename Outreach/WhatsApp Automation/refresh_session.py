"""
WhatsApp — Login sessione (profilo persistente)
===================================================
Apre WhatsApp Web dentro un PROFILO CHROMIUM DEDICATO E PERSISTENTE (non il tuo
WhatsApp Desktop personale, non storage_state). WhatsApp Web tiene le chiavi di
sessione in IndexedDB, non nei cookie: storage_state Playwright NON le cattura,
serve un profilo persistente su disco (stesso pattern gia' usato per YouTube in
questo repo: launch_persistent_context su un profile_dir).

Uso:
    cd "c:\\Users\\Utente\\Desktop\\qui tutto\\Digital Empire\\Outreach"
    python "WhatsApp Automation\\refresh_session.py"
"""
import asyncio
import os

BASE        = os.path.dirname(os.path.abspath(__file__))
PROFILE_DIR = os.path.join(BASE, "whatsapp-profile")

UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/124.0.0.0 Safari/537.36"
)


async def is_logged_in(page) -> bool:
    try:
        chat_list = await page.query_selector('div[id="pane-side"]')
        return chat_list is not None
    except Exception:
        return False


async def main():
    from playwright.async_api import async_playwright

    print()
    print("=" * 60)
    print("  WHATSAPP WEB — LOGIN SESSIONE (profilo persistente)")
    print("=" * 60)
    print(f"  Profilo: {PROFILE_DIR}")

    async with async_playwright() as pw:
        ctx = await pw.chromium.launch_persistent_context(
            PROFILE_DIR,
            headless=False,
            args=["--start-maximized"],
            viewport={"width": 1280, "height": 800},
            user_agent=UA,
        )
        page = ctx.pages[0] if ctx.pages else await ctx.new_page()

        print("  Apro WhatsApp Web...")
        await page.goto("https://web.whatsapp.com/", wait_until="domcontentloaded")
        await asyncio.sleep(5)

        if await is_logged_in(page):
            print("  Sessione valida — sei gia' loggato.")
        else:
            print()
            print("  Non sei loggato.")
            print("  1. Apri WhatsApp sul telefono")
            print("  2. Impostazioni -> Dispositivi collegati -> Collega un dispositivo")
            print("  3. Inquadra il QR code mostrato nella finestra del browser")
            print("  4. Quando vedi le tue chat, torna qui e premi INVIO")
            print()
            loop = asyncio.get_event_loop()
            await loop.run_in_executor(None, lambda: input("  >> Premi INVIO dopo aver scansionato il QR...\n"))
            await asyncio.sleep(3)
            if await is_logged_in(page):
                print("  Login confermato.")
            else:
                print("  [ATTENZIONE] Non vedo ancora la lista chat. Il profilo e' comunque salvato su disco:")
                print("  se il login e' andato a buon fine sul telefono, dovrebbe persistere lo stesso.")

        await ctx.close()

    print()
    print(f"  OK - Profilo persistente salvato in: {PROFILE_DIR}")
    print("  Sessione WhatsApp pronta per l'invio automatico.")
    print()


if __name__ == "__main__":
    asyncio.run(main())
