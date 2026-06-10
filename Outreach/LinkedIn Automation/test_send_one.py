"""Test finale: invia UNA connection request ad Antonio Crapanzano e mostra tutto."""
import asyncio, sys, os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
BASE = os.path.dirname(os.path.abspath(__file__))

PROFILE = "https://www.linkedin.com/in/antonio-crapanzano-533b78259/"

async def main():
    from playwright.async_api import async_playwright
    sys.path.insert(0, BASE)
    from config import SESSION_FILE

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        ctx = await browser.new_context(
            storage_state=os.path.join(BASE, SESSION_FILE),
            viewport={"width": 1280, "height": 900},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        )
        ctx.set_default_timeout(20000)
        page = await ctx.new_page()

        print(f"Navigando a: {PROFILE}")
        await page.goto(PROFILE, wait_until="domcontentloaded")
        await asyncio.sleep(5)

        # Importa send_connection da run_today
        import importlib.util
        spec = importlib.util.spec_from_file_location("run_today", os.path.join(BASE, "run_today.py"))
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)

        print("Tentativo di connessione...")
        result = await mod.send_connection(page, PROFILE)
        print(f"\n=== RISULTATO: {result} ===")

        # Screenshot dopo
        shot = os.path.join(BASE, "test_after_connect.png")
        await page.screenshot(path=shot)
        print(f"Screenshot dopo: {shot}")

        await asyncio.sleep(5)
        await browser.close()

asyncio.run(main())
