"""Debug: estrae dati dal HTML della pagina di ricerca LinkedIn (bpr-guid, script vars)."""
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

        # Intercetta ANCHE la risposta HTML iniziale
        initial_html = []
        async def on_response(resp):
            if "search/results/people" in resp.url and resp.status == 200:
                try:
                    body = await resp.body()
                    initial_html.append(body.decode("utf-8", errors="replace"))
                except Exception as e:
                    print(f"Errore lettura HTML: {e}")

        page.on("response", on_response)
        await page.goto(
            "https://www.linkedin.com/search/results/people/?keywords=avvocato+Milano",
            wait_until="domcontentloaded"
        )
        await asyncio.sleep(8)
        page.remove_listener("response", on_response)

        if initial_html:
            html = initial_html[0]
            print(f"HTML iniziale: {len(html)} caratteri")

            # Cerca slug profilo nell'HTML
            slugs = re.findall(r'"publicIdentifier"\s*:\s*"([a-zA-Z0-9_-]+)"', html)
            print(f"\nSlug 'publicIdentifier' trovati: {len(slugs)}")
            for s in slugs[:10]:
                print(f"  https://www.linkedin.com/in/{s}")

            # Cerca firstName nel HTML
            names = re.findall(r'"firstName"\s*:\s*"([^"]+)"', html)
            print(f"\nfirstName trovati: {names[:5]}")

            # Cerca link /in/ nell'HTML
            in_links = re.findall(r'linkedin\.com/in/([a-zA-Z0-9_-]+)', html)
            print(f"\nLink /in/ trovati: {len(set(in_links))}")
            for s in list(set(in_links))[:10]:
                print(f"  https://www.linkedin.com/in/{s}")

            # Cerca bpr-guid code elements
            bpr = re.findall(r'<code[^>]+id="bpr-guid-[^"]+"[^>]*>([^<]{1,2000})</code>', html)
            print(f"\nbpr-guid code elements: {len(bpr)}")
            for b in bpr[:3]:
                print(f"  {b[:100]}")

            # Salva HTML per analisi
            out = os.path.join(BASE, "debug_search_html.html")
            with open(out, "w", encoding="utf-8") as f:
                f.write(html)
            print(f"\nHTML salvato: {out}")
        else:
            print("HTML non catturato dalla response interceptor. Estraggo dal DOM...")
            # Prova a leggere il DOM HTML direttamente
            dom_html = await page.content()
            print(f"DOM HTML: {len(dom_html)} caratteri")
            slugs = re.findall(r'"publicIdentifier"\s*:\s*"([a-zA-Z0-9_-]+)"', dom_html)
            print(f"Slug trovati nel DOM: {len(slugs)}")
            for s in slugs[:10]:
                print(f"  https://www.linkedin.com/in/{s}")

            # Cerca anche nel contenuto dei window.__* globals
            globals_js = await page.evaluate("""
                () => {
                    const keys = Object.keys(window).filter(k =>
                        k.startsWith('__') && typeof window[k] === 'object'
                    );
                    return keys.slice(0, 10);
                }
            """)
            print(f"\nWindow globals con __: {globals_js}")

        await browser.close()

asyncio.run(main())
