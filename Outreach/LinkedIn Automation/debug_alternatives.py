"""
Testa 3 alternative per trovare profili con URL /in/ reali:
1. mynetwork/people-you-may-know → persone suggerite da LinkedIn
2. Feed principale → autori dei post
3. HTML search page → URN ACoAA... patterns
"""
import asyncio, sys, os, re
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from config import SESSION_FILE
BASE = os.path.dirname(os.path.abspath(__file__))

async def test_page(page, url, wait=6):
    await page.goto(url, wait_until="domcontentloaded")
    await asyncio.sleep(wait)
    # Scroll per caricare lazy content
    for _ in range(3):
        await page.evaluate("window.scrollBy(0, window.innerHeight)")
        await asyncio.sleep(1.5)
    links = await page.evaluate("""
        () => Array.from(document.querySelectorAll('a[href*="/in/"]'))
             .map(a => a.href.split('?')[0])
             .filter(h => /\/in\/[a-zA-Z0-9_-]+\/?$/.test(h))
    """)
    return list(set(links))

async def main():
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        ctx = await browser.new_context(
            storage_state=os.path.join(BASE, SESSION_FILE),
            viewport={"width": 1280, "height": 800},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        )
        ctx.set_default_timeout(20000)
        page = await ctx.new_page()

        # ── TEST 1: People You May Know ──────────────────────────────
        print("="*50)
        print("TEST 1: /mynetwork/people-you-may-know/")
        links1 = await test_page(page, "https://www.linkedin.com/mynetwork/people-you-may-know/")
        print(f"Link /in/ trovati: {len(links1)}")
        for l in links1[:10]:
            print(f"  {l}")

        # ── TEST 2: Feed principale ──────────────────────────────────
        print("\n" + "="*50)
        print("TEST 2: Feed principale /feed/")
        links2 = await test_page(page, "https://www.linkedin.com/feed/")
        print(f"Link /in/ trovati: {len(links2)}")
        for l in links2[:10]:
            print(f"  {l}")

        # ── TEST 3: Search HTML con URN patterns ─────────────────────
        print("\n" + "="*50)
        print("TEST 3: Search HTML - URN ACoAA patterns")
        await page.goto(
            "https://www.linkedin.com/search/results/people/?keywords=avvocato+Milano",
            wait_until="domcontentloaded"
        )
        await asyncio.sleep(8)
        html = await page.content()
        # Cerca URN di profilo nel HTML renderizzato
        urns = re.findall(r'ACoAA[A-Za-z0-9_-]{10,}', html)
        urns_fsd = re.findall(r'urn:li:fsd_profile:([A-Za-z0-9_-]+)', html)
        print(f"URN ACoAA trovati: {len(set(urns))}")
        print(f"URN fsd_profile trovati: {len(set(urns_fsd))}")

        # Cerca data-member-id attributes
        member_ids = await page.evaluate("""
            () => {
                const els = document.querySelectorAll('[data-member-id], [data-anonymized-url], [data-view-link]');
                return Array.from(els).map(e => ({
                    memberid: e.getAttribute('data-member-id'),
                    anonurl: e.getAttribute('data-anonymized-url'),
                    viewlink: e.getAttribute('data-view-link'),
                    tag: e.tagName
                })).filter(x => x.memberid || x.anonurl || x.viewlink);
            }
        """)
        print(f"data-member-id/anon/view attrs: {len(member_ids)}")
        for m in member_ids[:5]:
            print(f"  {m}")

        await browser.close()
        print("\n=== FINE TEST ===")

asyncio.run(main())
