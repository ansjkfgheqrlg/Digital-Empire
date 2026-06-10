"""
Step 0: Login LinkedIn e salva sessione.
Esegui UNA VOLTA. Poi tutti gli altri script riusano la sessione salvata.

Run: python linkedin_session.py
"""
import json
import asyncio
from playwright.async_api import async_playwright
from config import LINKEDIN_EMAIL, LINKEDIN_PASSWORD, SESSION_FILE


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(
            viewport={"width": 1280, "height": 800},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        )
        page = await context.new_page()

        print("Apro LinkedIn login...")
        await page.goto("https://www.linkedin.com/login", wait_until="domcontentloaded")
        await asyncio.sleep(2)

        await page.fill("#username", LINKEDIN_EMAIL)
        await page.fill("#password", LINKEDIN_PASSWORD)
        await page.click('[type="submit"]')
        await page.wait_for_load_state("domcontentloaded", timeout=30000)
        await asyncio.sleep(3)

        # Attende se c'è verifica 2FA
        if "checkpoint" in page.url or "challenge" in page.url:
            print("\n ATTENZIONE: Richiesta verifica 2FA — completala nel browser aperto.")
            print("   Quando sei nella home LinkedIn, premi INVIO qui.")
            input()
        else:
            print(f"Login OK — URL: {page.url}")

        await context.storage_state(path=SESSION_FILE)
        print(f"Sessione salvata in: {SESSION_FILE}")
        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
