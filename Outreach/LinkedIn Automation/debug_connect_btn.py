"""
Cerca il pulsante ESATTO per inviare una richiesta di collegamento.
Visita 3 profili PYMK non connessi e logga tutto.
"""
import asyncio, sys, os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from config import SESSION_FILE
BASE = os.path.dirname(os.path.abspath(__file__))

# Profili da testare (prendo 3 dal leads file)
PROFILES = [
    "https://www.linkedin.com/in/antonio-crapanzano-533b78259/",
    "https://www.linkedin.com/in/virginia-raggi-2a9167221/",
    "https://www.linkedin.com/in/elisa-lignoli/",
]

async def inspect_profile(page, url):
    print(f"\n{'='*60}")
    print(f"URL: {url}")
    await page.goto(url, wait_until="domcontentloaded")
    await asyncio.sleep(6)

    shot = os.path.join(BASE, f"debug_connect_{url.split('/in/')[1].rstrip('/').split('/')[0]}.png")
    await page.screenshot(path=shot)
    print(f"Screenshot: {shot}")

    # Cerca QUALSIASI elemento cliccabile con testo Collegati/Connetti/Connect/Follow/Segui
    result = await page.evaluate("""
        () => {
            // Cerca in TUTTI i tag possibili
            const all = Array.from(document.querySelectorAll(
                'button, a, span[role="button"], div[role="button"], [tabindex="0"]'
            ));
            const keywords = ['collegat', 'connett', 'connect', 'invit', 'follow', 'segui', 'messag'];
            return all
                .filter(el => {
                    const text = (el.innerText || el.textContent || '').trim().toLowerCase();
                    const aria = (el.getAttribute('aria-label') || '').toLowerCase();
                    return keywords.some(k => text.includes(k) || aria.includes(k));
                })
                .map(el => ({
                    tag: el.tagName,
                    role: el.getAttribute('role') || '',
                    text: (el.innerText || el.textContent || '').trim().substring(0, 60),
                    aria: el.getAttribute('aria-label') || '',
                    class: el.className.substring(0, 100),
                    visible: el.offsetWidth > 0 && el.offsetHeight > 0,
                    disabled: el.disabled || el.getAttribute('disabled') !== null,
                    tabindex: el.getAttribute('tabindex'),
                }));
        }
    """)

    print(f"\nElementi azione trovati: {len(result)}")
    for r in result:
        vis = "VIS" if r['visible'] else "NAC"
        dis = " [DISABLED]" if r['disabled'] else ""
        print(f"  [{vis}]{dis} <{r['tag']} role='{r['role']}'> text='{r['text'][:40]}' | aria='{r['aria'][:60]}'")
        if 'collegat' in (r['text']+r['aria']).lower() or 'connett' in (r['text']+r['aria']).lower():
            print(f"    *** POSSIBILE CONNECT BUTTON *** class: {r['class'][:80]}")

    # Anche cerca il div azioni principale del profilo
    actions = await page.evaluate("""
        () => {
            // Il blocco azioni LinkedIn è tipicamente nella sezione .pv-top-card-v2-ctas
            const ctaSection = document.querySelector(
                '.pv-top-card-v2-ctas, .pvs-profile-actions, .pv-s-profile-actions, [data-view-name="profile-action-bar"]'
            );
            if (!ctaSection) return {found: false, html: ''};
            return {
                found: true,
                html: ctaSection.outerHTML.substring(0, 500),
                buttons: Array.from(ctaSection.querySelectorAll('button, a, [role="button"]'))
                    .map(b => ({
                        tag: b.tagName,
                        text: (b.innerText || '').trim(),
                        aria: b.getAttribute('aria-label') || '',
                        visible: b.offsetWidth > 0,
                    }))
            };
        }
    """)
    print(f"\nSezione CTA trovata: {actions.get('found', False)}")
    if actions.get('found'):
        for b in actions.get('buttons', []):
            print(f"  <{b['tag']}> text='{b['text'][:40]}' | aria='{b['aria'][:60]}' | vis={b['visible']}")
    else:
        print("  CTA section non trovata. HTML partial:")
        # Cerca il contenitore del profilo header
        header_html = await page.evaluate("""
            () => {
                const sections = [
                    '.pv-top-card', '.profile-action-button', '[data-member-id]',
                    '.pv-profile-section', 'section.artdeco-card'
                ];
                for (const sel of sections) {
                    const el = document.querySelector(sel);
                    if (el) return {sel, html: el.outerHTML.substring(0, 300)};
                }
                return {sel: 'none', html: ''};
            }
        """)
        print(f"  Selector trovato: {header_html.get('sel')}")

    return result

async def main():
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        ctx = await browser.new_context(
            storage_state=os.path.join(BASE, SESSION_FILE),
            viewport={"width": 1280, "height": 900},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        )
        ctx.set_default_timeout(20000)
        page = await ctx.new_page()

        for url in PROFILES:
            await inspect_profile(page, url)
            await asyncio.sleep(2)

        print("\n\nFINE DEBUG. Premi INVIO per chiudere...")
        input()
        await browser.close()

asyncio.run(main())
