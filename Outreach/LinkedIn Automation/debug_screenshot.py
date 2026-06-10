"""Debug: apre LinkedIn search e fa screenshot per vedere cosa mostra."""
import asyncio
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from config import SESSION_FILE

BASE = os.path.dirname(os.path.abspath(__file__))
SESSION = os.path.join(BASE, SESSION_FILE)
SHOT = os.path.join(BASE, "debug_linkedin.png")

async def main():
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        ctx = await browser.new_context(
            storage_state=SESSION,
            viewport={"width": 1280, "height": 800},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        )
        page = await ctx.new_page()
        print("Apro LinkedIn search...")
        await page.goto("https://www.linkedin.com/search/results/people/?keywords=avvocato+Milano", wait_until="domcontentloaded")
        await asyncio.sleep(5)
        await page.screenshot(path=SHOT, full_page=False)
        print(f"Screenshot salvato: {SHOT}")
        print(f"URL attuale: {page.url}")
        # Conta link /in/ presenti
        links = await page.query_selector_all("a[href*='/in/']")
        print(f"Link /in/ trovati: {len(links)}")
        for l in links[:5]:
            href = await l.get_attribute("href")
            txt = (await l.inner_text()).strip()[:40]
            print(f"  {txt} → {href[:60]}")
        await browser.close()

asyncio.run(main())
