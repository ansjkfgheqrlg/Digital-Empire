"""Debug: estrae dati embedded nella pagina di ricerca LinkedIn (script tags, data attributes)."""
import asyncio, sys, os, json, re
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

        # Intercetta TUTTE le risposte con JSON
        all_responses = []
        async def on_resp(resp):
            url = resp.url
            ct = resp.headers.get("content-type", "")
            if "json" in ct and resp.status == 200:
                all_responses.append((url, resp))

        page.on("response", on_resp)

        print("Carico pagina ricerca...")
        await page.goto(
            "https://www.linkedin.com/search/results/people/?keywords=avvocato+Milano",
            wait_until="domcontentloaded"
        )
        # Aspetta il rendering React
        await asyncio.sleep(10)
        await page.evaluate("window.scrollBy(0, 800)")
        await asyncio.sleep(5)

        # 1. Cerca link /in/ nel DOM dopo attesa lunga
        profile_links = await page.evaluate("""
            () => Array.from(document.querySelectorAll('a[href*="/in/"]'))
                .map(a => ({href: a.href, text: a.innerText.trim().substring(0,50)}))
                .filter(x => x.href.includes('linkedin.com/in/'))
        """)
        print(f"\n1. Link /in/ dopo 15s di attesa: {len(profile_links)}")
        for l in profile_links[:10]:
            print(f"   {l['text'][:30]:30} → {l['href'][:80]}")

        # 2. Script tags con JSON
        script_data = await page.evaluate("""
            () => {
                const scripts = Array.from(document.querySelectorAll('script[type="application/json"], script[type="application/ld+json"], code[id]'));
                return scripts.map(s => ({
                    id: s.id || s.getAttribute('type'),
                    len: s.textContent.length,
                    preview: s.textContent.substring(0, 100)
                }));
            }
        """)
        print(f"\n2. Script/code tags con dati JSON: {len(script_data)}")
        for s in script_data[:5]:
            print(f"   [{s['id']}] len={s['len']} preview: {s['preview'][:80]}")

        # 3. Cerca elemento con publicIdentifier o firstName nel DOM
        person_data = await page.evaluate("""
            () => {
                const html = document.body.innerHTML;
                const matches = [];
                // Cerca pattern di slug profilo
                const re = /linkedin\\.com\\/in\\/([a-zA-Z0-9_-]+)/g;
                let m;
                while ((m = re.exec(html)) !== null) {
                    matches.push(m[1]);
                }
                return [...new Set(matches)];
            }
        """)
        print(f"\n3. Slug /in/... trovati nell'HTML: {len(person_data)}")
        for slug in person_data[:10]:
            print(f"   https://www.linkedin.com/in/{slug}")

        # 4. JSON responses catturate
        print(f"\n4. JSON API responses catturate: {len(all_responses)}")
        search_responses = [(url, r) for url, r in all_responses if "search" in url.lower() or "cluster" in url.lower() or "people" in url.lower()]
        print(f"   Di cui con 'search/cluster/people': {len(search_responses)}")

        for url, resp in all_responses[:5]:
            print(f"   {url[:100]}")

        # 5. Salva la prima JSON response con "search" per analisi
        if search_responses:
            url, resp = search_responses[0]
            try:
                data = await resp.json()
                out = os.path.join(BASE, "debug_search_response.json")
                with open(out, "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                print(f"\n5. Prima search response salvata: {out}")
            except Exception as e:
                print(f"\n5. Errore lettura search response: {e}")

        await browser.close()

asyncio.run(main())
