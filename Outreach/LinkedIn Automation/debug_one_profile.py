"""
Apre UN profilo LinkedIn, scatta screenshot, logga TUTTI i pulsanti presenti.
Obiettivo: capire esattamente quali aria-label/selettori usare per "Connetti".
"""
import asyncio, sys, os, json
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from config import SESSION_FILE
BASE = os.path.dirname(os.path.abspath(__file__))

PROFILE_URL = "https://www.linkedin.com/in/simone-ragni-53b1aa88/"

async def main():
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        ctx = await browser.new_context(
            storage_state=os.path.join(BASE, SESSION_FILE),
            viewport={"width": 1280, "height": 900},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        )
        page = await ctx.new_page()

        print(f"Navigando a: {PROFILE_URL}")
        await page.goto(PROFILE_URL, wait_until="domcontentloaded")
        await asyncio.sleep(5)

        # Screenshot PRIMA di qualsiasi azione
        shot1 = os.path.join(BASE, "debug_profile_before.png")
        await page.screenshot(path=shot1, full_page=False)
        print(f"Screenshot salvato: {shot1}")

        # Logga TUTTI i pulsanti presenti
        buttons = await page.evaluate("""
            () => Array.from(document.querySelectorAll('button, a[role="button"]'))
                .map(b => ({
                    tag: b.tagName,
                    text: (b.innerText || '').trim().substring(0, 60),
                    ariaLabel: b.getAttribute('aria-label') || '',
                    class: b.className.substring(0, 80),
                    visible: b.offsetWidth > 0 && b.offsetHeight > 0,
                    offsetW: b.offsetWidth,
                    offsetH: b.offsetHeight,
                }))
                .filter(b => b.text || b.ariaLabel)
        """)

        print(f"\n=== PULSANTI TROVATI: {len(buttons)} ===")
        for b in buttons:
            vis = "VISIBILE" if b['visible'] else "nascosto"
            print(f"  [{vis}] tag={b['tag']} | text='{b['text'][:40]}' | aria='{b['ariaLabel'][:60]}'")

        # Cerca specificamente pulsanti che sembrano "connect" / "follow" / "message"
        print("\n=== PULSANTI AZIONE (connect/follow/message/altro) ===")
        action_btns = await page.evaluate("""
            () => {
                const keywords = ['connett', 'connect', 'follow', 'messag', 'invit', 'pend'];
                return Array.from(document.querySelectorAll('button, a[role="button"]'))
                    .filter(b => {
                        const t = (b.innerText + b.getAttribute('aria-label') || '').toLowerCase();
                        return keywords.some(k => t.includes(k));
                    })
                    .map(b => ({
                        text: b.innerText.trim(),
                        ariaLabel: b.getAttribute('aria-label') || '',
                        visible: b.offsetWidth > 0,
                        disabled: b.disabled,
                        outerHTML: b.outerHTML.substring(0, 200),
                    }));
            }
        """)
        for b in action_btns:
            print(f"  text='{b['text'][:50]}' | aria='{b['ariaLabel'][:60]}' | visible={b['visible']}")
            print(f"  HTML: {b['outerHTML'][:150]}")
            print()

        # Aspetta che l'utente veda la pagina
        print("\nPagina aperta. Guarda il browser. Premi INVIO per chiudere...")
        input()

        await browser.close()

asyncio.run(main())
