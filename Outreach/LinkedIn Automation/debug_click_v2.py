"""
Debug v2: clicca 'Visualizza' e usa wait_for_url per attendere la navigazione.
Testa se il click porta a un profilo /in/ se si aspetta abbastanza.
"""
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
        ctx.set_default_timeout(15000)
        page = await ctx.new_page()

        print("1. Vado alla ricerca 'avvocato Milano'...")
        await page.goto(
            "https://www.linkedin.com/search/results/people/?keywords=avvocato+Milano",
            wait_until="domcontentloaded"
        )
        await asyncio.sleep(5)

        print(f"   URL: {page.url}")

        # Trova pulsanti Visualizza
        btns = await page.query_selector_all('a:text("Visualizza"), button:text("Visualizza"), span:text("Visualizza")')
        print(f"2. Pulsanti Visualizza: {len(btns)}")

        if not btns:
            print("   Nessun bottone trovato. Prova con scroll...")
            await page.evaluate("window.scrollBy(0, 400)")
            await asyncio.sleep(3)
            btns = await page.query_selector_all('a:text("Visualizza"), button:text("Visualizza"), span:text("Visualizza")')
            print(f"   Dopo scroll: {len(btns)}")

        results = []
        for i, btn in enumerate(btns[:5]):
            try:
                href = await btn.get_attribute("href")
                print(f"\n3.{i} Button {i}: href={href}")

                # Tenta click + wait_for_url
                try:
                    async with page.expect_navigation(timeout=8000) as nav_info:
                        await btn.click()
                    nav = await nav_info.value
                    await asyncio.sleep(2)
                    final_url = page.url
                    print(f"   Navigato a: {final_url}")
                    if "/in/" in final_url:
                        results.append(final_url.split("?")[0])
                        print(f"   ✓ PROFILO TROVATO: {final_url}")
                except Exception as e:
                    # Fallback: aspetta URL change direttamente
                    await asyncio.sleep(4)
                    final_url = page.url
                    print(f"   URL dopo click (fallback): {final_url}")
                    if "/in/" in final_url:
                        results.append(final_url.split("?")[0])

                # Torna alla ricerca
                await page.go_back()
                await asyncio.sleep(3)

            except Exception as e:
                print(f"   Errore: {e}")
                await page.goto(
                    "https://www.linkedin.com/search/results/people/?keywords=avvocato+Milano",
                    wait_until="domcontentloaded"
                )
                await asyncio.sleep(4)

        print(f"\n=== RISULTATO: {len(results)} profili trovati ===")
        for r in results:
            print(f"  {r}")

        await browser.close()

asyncio.run(main())
