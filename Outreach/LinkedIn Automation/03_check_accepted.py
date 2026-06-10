"""
Step 3: Controlla quali richieste sono state accettate.
Aggiorna lo status da 'connect_sent' a 'connected' in linkedin_leads.json.

Tecnica: controlla le nuove connessioni nell'ultimo giorno da LinkedIn.

Run: python 03_check_accepted.py
"""
import json
import asyncio
import random
from datetime import date, datetime, timedelta
from playwright.async_api import async_playwright
from config import SESSION_FILE, LEADS_FILE


def load_leads():
    with open(LEADS_FILE, encoding="utf-8") as f:
        return json.load(f)


def save_leads(leads):
    with open(LEADS_FILE, "w", encoding="utf-8") as f:
        json.dump(leads, f, ensure_ascii=False, indent=2)


async def get_new_connections(page) -> set:
    """Estrae URL dei profili delle nuove connessioni (ultimi 7 giorni)."""
    connected_urls = set()

    await page.goto("https://www.linkedin.com/mynetwork/invite-connect/connections/")
    await page.wait_for_load_state("networkidle")
    await asyncio.sleep(random.uniform(3, 6))

    # Scorri per caricare più connessioni
    for _ in range(3):
        await page.evaluate("window.scrollBy(0, window.innerHeight * 2)")
        await asyncio.sleep(random.uniform(1, 2))

    profile_links = await page.query_selector_all('.mn-connection-card__link')
    for link in profile_links:
        href = await link.get_attribute("href")
        if href and "/in/" in href:
            connected_urls.add(href.split("?")[0])

    print(f"Connessioni trovate nella lista: {len(connected_urls)}")
    return connected_urls


async def main():
    leads = load_leads()
    pending = [l for l in leads if l.get("status") == "connect_sent"]

    print(f"\n{'='*55}")
    print(f"  03_check_accepted.py — controlla accettazioni")
    print(f"{'='*55}")
    print(f"  Richieste pendenti: {len(pending)}")
    print(f"{'='*55}\n")

    if not pending:
        print("Nessuna richiesta pendente da controllare.")
        return

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(
            storage_state=SESSION_FILE,
            viewport={"width": 1280, "height": 800},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        )
        page = await context.new_page()

        connected_urls = await get_new_connections(page)
        await browser.close()

    nuove_connessioni = 0
    for lead in leads:
        if lead.get("status") == "connect_sent":
            # Normalizza URL per il confronto
            lead_url = lead["profile_url"].rstrip("/")
            for conn_url in connected_urls:
                if lead_url in conn_url or conn_url in lead_url:
                    lead["status"] = "connected"
                    lead["connect_accepted"] = True
                    lead["connected_date"] = str(date.today())
                    nuove_connessioni += 1
                    print(f"  ACCETTATO: {lead['name']}")
                    break

    save_leads(leads)

    print(f"\n{'='*55}")
    print(f"Nuove connessioni accettate: {nuove_connessioni}")
    print(f"Ora esegui: python 04_send_messages.py")
    print(f"{'='*55}\n")


if __name__ == "__main__":
    asyncio.run(main())
