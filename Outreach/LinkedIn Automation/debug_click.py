"""Test: clicca il primo 'Visualizza' e logga cosa succede."""
import asyncio, sys, os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from config import SESSION_FILE
BASE = os.path.dirname(os.path.abspath(__file__))

async def main():
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        ctx = await browser.new_context(
            storage_state=os.path.join(BASE, SESSION_FILE),
            viewport={"width": 1280, "height": 800},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        )
        page = await ctx.new_page()

        print("1. Vado alla ricerca...")
        await page.goto("https://www.linkedin.com/search/results/people/?keywords=avvocato+Milano", wait_until="domcontentloaded")
        await asyncio.sleep(4)

        print(f"   URL attuale: {page.url}")

        # Trova pulsanti Visualizza
        btns = await page.query_selector_all('a:text("Visualizza"), button:text("Visualizza")')
        print(f"2. Pulsanti Visualizza trovati: {len(btns)}")

        if btns:
            btn = btns[0]
            # Controlla il suo href PRIMA di cliccare
            href = await btn.get_attribute("href")
            print(f"   href del primo bottone: {href}")

            # Ascolta eventuali nuovi tab
            new_page_future = asyncio.get_event_loop().create_future()
            def on_page(new_p):
                if not new_page_future.done():
                    new_page_future.set_result(new_p)
            ctx.on("page", on_page)

            print("3. Clicco 'Visualizza'...")
            await btn.click()
            await asyncio.sleep(3)

            print(f"   URL dopo click (stessa pagina): {page.url}")

            # Controlla se si è aperto un nuovo tab
            if new_page_future.done():
                new_p = new_page_future.result()
                await asyncio.sleep(2)
                print(f"   NUOVO TAB aperto! URL: {new_p.url}")
                await new_p.screenshot(path=os.path.join(BASE, "debug_newtab.png"))
            else:
                print("   Nessun nuovo tab")
                await page.screenshot(path=os.path.join(BASE, "debug_afterclick.png"))
                print(f"   Screenshot salvato")

        print("4. Test completato")
        await asyncio.sleep(3)
        await browser.close()

asyncio.run(main())
