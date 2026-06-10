"""
Step 1: Scraping lead da LinkedIn Search.
Cerca professionisti per nicchia, estrae nome + URL profilo + titolo.
Salva in linkedin_leads.json con status='new'.

Tecnica di Ben AI: scrape chi interagisce con post di settore.
Tecnica di Oleg: usa LinkedIn search per nicchia specifica.

Run: python 01_scrape_leads.py
Run: python 01_scrape_leads.py --search "avvocato Milano" --max 50
"""
import json
import asyncio
import random
import sys
import time
from datetime import date
from playwright.async_api import async_playwright
from config import SESSION_FILE, LEADS_FILE, DELAY_MIN_SECONDS, DELAY_MAX_SECONDS, TARGET_SEARCHES


def load_leads():
    try:
        with open(LEADS_FILE, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_leads(leads):
    with open(LEADS_FILE, "w", encoding="utf-8") as f:
        json.dump(leads, f, ensure_ascii=False, indent=2)


def already_scraped_urls(leads):
    return {l["profile_url"] for l in leads}


async def human_delay(min_s=None, max_s=None):
    d = random.uniform(
        min_s or DELAY_MIN_SECONDS,
        max_s or DELAY_MAX_SECONDS
    )
    await asyncio.sleep(d)


async def scrape_search(page, query: str, max_results: int = 40) -> list:
    """Cerca profili LinkedIn per query e ritorna lista di lead."""
    results = []
    search_url = f"https://www.linkedin.com/search/results/people/?keywords={query.replace(' ', '%20')}&origin=GLOBAL_SEARCH_HEADER"

    print(f"\nScraping: '{query}'")
    await page.goto(search_url)
    await page.wait_for_load_state("networkidle")
    await human_delay(3, 6)

    page_num = 1
    while len(results) < max_results:
        # Estrai tutti i profili visibili sulla pagina
        profiles = await page.query_selector_all(".reusable-search__result-container")

        for profile in profiles:
            try:
                name_el = await profile.query_selector(".entity-result__title-text a")
                title_el = await profile.query_selector(".entity-result__primary-subtitle")
                loc_el   = await profile.query_selector(".entity-result__secondary-subtitle")

                if not name_el:
                    continue

                name = (await name_el.inner_text()).strip().split("\n")[0]
                href = await name_el.get_attribute("href")
                title = (await title_el.inner_text()).strip() if title_el else ""
                location = (await loc_el.inner_text()).strip() if loc_el else ""

                if href and "/in/" in href:
                    profile_url = href.split("?")[0]
                    results.append({
                        "name": name,
                        "title": title,
                        "location": location,
                        "profile_url": profile_url,
                        "search_query": query,
                        "status": "new",
                        "scraped_date": str(date.today()),
                        "connect_sent": None,
                        "connect_accepted": False,
                        "message_sent": None,
                        "followup1_sent": None,
                        "followup2_sent": None,
                    })
            except Exception:
                continue

        print(f"  Pagina {page_num}: trovati {len(results)} profili totali")

        if len(results) >= max_results:
            break

        # Vai alla pagina successiva
        next_btn = await page.query_selector('[aria-label="Avanti"]')
        if not next_btn:
            next_btn = await page.query_selector('[aria-label="Next"]')
        if not next_btn:
            print("  Nessuna pagina successiva.")
            break

        await next_btn.click()
        await page.wait_for_load_state("networkidle")
        await human_delay(4, 8)
        page_num += 1

    return results[:max_results]


async def main():
    # Parse argomenti
    max_per_search = 30
    custom_search = None

    for i, arg in enumerate(sys.argv[1:]):
        if arg == "--search" and i + 1 < len(sys.argv) - 1:
            custom_search = sys.argv[i + 2]
        if arg == "--max" and i + 1 < len(sys.argv) - 1:
            max_per_search = int(sys.argv[i + 2])

    searches = [custom_search] if custom_search else TARGET_SEARCHES

    existing_leads = load_leads()
    existing_urls = already_scraped_urls(existing_leads)
    new_leads = []

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(
            storage_state=SESSION_FILE,
            viewport={"width": 1280, "height": 800},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        )
        page = await context.new_page()

        for query in searches:
            results = await scrape_search(page, query, max_per_search)
            for r in results:
                if r["profile_url"] not in existing_urls:
                    new_leads.append(r)
                    existing_urls.add(r["profile_url"])
            await human_delay(5, 12)

        await browser.close()

    all_leads = existing_leads + new_leads
    save_leads(all_leads)

    print(f"\n{'='*50}")
    print(f"Nuovi lead aggiunti: {len(new_leads)}")
    print(f"Totale lead nel database: {len(all_leads)}")
    print(f"Salvati in: {LEADS_FILE}")
    print(f"{'='*50}")


if __name__ == "__main__":
    asyncio.run(main())
