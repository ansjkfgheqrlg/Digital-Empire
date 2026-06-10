"""Debug: lista TUTTI gli href nella pagina search LinkedIn."""
import asyncio, sys, os
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
        await page.goto("https://www.linkedin.com/search/results/people/?keywords=avvocato+Milano", wait_until="domcontentloaded")
        await asyncio.sleep(5)

        # Tutti i link presenti
        all_links = await page.evaluate("""
            () => Array.from(document.querySelectorAll('a[href]'))
                .map(a => ({ href: a.href, text: a.innerText.trim().substring(0,40) }))
                .filter(x => x.href.includes('linkedin.com') && x.href.length > 30)
        """)
        print(f"Totale link LinkedIn: {len(all_links)}")
        for l in all_links[:30]:
            print(f"  {l['text'][:30]:30} → {l['href'][:80]}")
        await browser.close()

asyncio.run(main())
