"""Debug: mostra TUTTE le chiamate API che LinkedIn fa durante una ricerca."""
import asyncio, sys, os, json
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

        api_calls = []

        async def on_response(response):
            url = response.url
            if "linkedin.com" in url and response.status == 200:
                if any(x in url for x in ["/api/", "/graphql", "/voyager/", "/feed/", "/search"]):
                    api_calls.append({
                        "url": url[:120],
                        "status": response.status,
                        "content_type": response.headers.get("content-type", ""),
                    })

        page.on("response", on_response)

        print("Navigando alla ricerca LinkedIn...")
        await page.goto(
            "https://www.linkedin.com/search/results/people/?keywords=avvocato+Milano",
            wait_until="domcontentloaded"
        )
        await asyncio.sleep(6)
        await page.evaluate("window.scrollBy(0, 600)")
        await asyncio.sleep(3)

        page.remove_listener("response", on_response)

        print(f"\nTotale API calls catturate: {len(api_calls)}")
        for c in api_calls:
            print(f"  [{c['status']}] {c['url']}")

        # Prova a ottenere il JSON da una delle call di search
        print("\n--- Ricerca call con 'search' nell'URL ---")
        search_calls = [c for c in api_calls if "search" in c["url"].lower()]
        for c in search_calls:
            print(f"  {c['url']}")

        await browser.close()

asyncio.run(main())
