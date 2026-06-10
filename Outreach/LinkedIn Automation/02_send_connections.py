"""
Step 2: Invia richieste di connessione LinkedIn.
SENZA nota allegata — tecnica di Oleg Melnikov per massimizzare l'acceptance rate.

"Quando mandi richiesta senza messaggio, sembra meno 'salesy' e più naturale.
L'acceptance rate sale del 30-40%." — Oleg Melnikov (NotebookLM)

Limite: DAILY_CONNECT_LIMIT richieste/giorno (default 20).
Aspetta 24h prima di inviare messaggi ai connessi.

Run: python 02_send_connections.py
Run: python 02_send_connections.py --dry-run
"""
import json
import asyncio
import random
import sys
from datetime import date, datetime
from playwright.async_api import async_playwright
from config import SESSION_FILE, LEADS_FILE, DAILY_CONNECT_LIMIT, DELAY_MIN_SECONDS, DELAY_MAX_SECONDS


def load_leads():
    with open(LEADS_FILE, encoding="utf-8") as f:
        return json.load(f)


def save_leads(leads):
    with open(LEADS_FILE, "w", encoding="utf-8") as f:
        json.dump(leads, f, ensure_ascii=False, indent=2)


def count_sent_today(leads):
    today = str(date.today())
    return sum(1 for l in leads if l.get("connect_sent") and l["connect_sent"].startswith(today))


async def human_delay(min_s=None, max_s=None):
    d = random.uniform(min_s or DELAY_MIN_SECONDS, max_s or DELAY_MAX_SECONDS)
    await asyncio.sleep(d)


async def send_connection(page, profile_url: str) -> str:
    """
    Apre il profilo e clicca 'Connetti'. Ritorna 'sent', 'already_connected',
    'not_found', o 'error'.
    """
    await page.goto(profile_url)
    await page.wait_for_load_state("networkidle")
    await human_delay(3, 7)

    # Cerca il pulsante Connetti
    connect_btn = None
    selectors = [
        'button[aria-label*="Connetti"]',
        'button[aria-label*="Connect"]',
        '.pvs-profile-actions button:has-text("Connetti")',
        '.pvs-profile-actions button:has-text("Connect")',
    ]
    for sel in selectors:
        try:
            btn = await page.query_selector(sel)
            if btn:
                connect_btn = btn
                break
        except Exception:
            continue

    if not connect_btn:
        # Controlla se già connesso
        msg_btn = await page.query_selector('button[aria-label*="Messaggio"], button[aria-label*="Message"]')
        if msg_btn:
            return "already_connected"
        # Potrebbe essere in "More" dropdown
        try:
            more_btn = await page.query_selector('button[aria-label*="Altro"], button[aria-label*="More"]')
            if more_btn:
                await more_btn.click()
                await human_delay(1, 2)
                connect_dropdown = await page.query_selector('[aria-label*="Connetti"], [aria-label*="Connect"]')
                if connect_dropdown:
                    connect_btn = connect_dropdown
        except Exception:
            pass

    if not connect_btn:
        return "not_found"

    await connect_btn.click()
    await human_delay(1, 3)

    # Se compare modale "Come ti conosci?" clicca "Altro"
    try:
        how_know_modal = await page.query_selector('[data-test-modal]')
        if how_know_modal:
            other_btn = await page.query_selector('button[aria-label*="Altro"], label[for*="Other"]')
            if other_btn:
                await other_btn.click()
                await human_delay(0.5, 1)
            send_btn = await page.query_selector('button[aria-label*="Invia"], button[aria-label*="Send"]')
            if send_btn:
                await send_btn.click()
                await human_delay(1, 2)
    except Exception:
        pass

    # Se compare finestra "Aggiungi nota" — chiudi SENZA nota (tecnica Oleg)
    try:
        send_without_note = await page.query_selector(
            'button[aria-label*="Invia senza nota"], button[aria-label*="Send without a note"]'
        )
        if send_without_note:
            await send_without_note.click()
            await human_delay(1, 2)
    except Exception:
        pass

    return "sent"


async def main():
    dry_run = "--dry-run" in sys.argv

    leads = load_leads()
    sent_today = count_sent_today(leads)
    remaining = DAILY_CONNECT_LIMIT - sent_today

    to_process = [
        l for l in leads
        if l.get("status") == "new" and not l.get("connect_sent")
    ]

    print(f"\n{'='*55}")
    print(f"  02_send_connections.py — richieste di connessione")
    print(f"{'='*55}")
    print(f"  Lead disponibili: {len(to_process)}")
    print(f"  Già inviate oggi: {sent_today}")
    print(f"  Limite rimanente: {remaining}")
    print(f"{'='*55}\n")

    if remaining <= 0:
        print("Limite giornaliero raggiunto. Riprova domani.")
        return

    to_send = to_process[:remaining]

    if dry_run:
        print(f"DRY-RUN: manderei {len(to_send)} richieste:")
        for l in to_send:
            print(f"  {l['name'][:40]} | {l['title'][:40]}")
        return

    inviati = 0
    errori = 0

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(
            storage_state=SESSION_FILE,
            viewport={"width": 1280, "height": 800},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        )
        page = await context.new_page()

        for i, lead in enumerate(to_send, 1):
            print(f"[{i:02d}/{len(to_send)}] {lead['name'][:45]}")
            print(f"         Titolo: {lead['title'][:50]}")
            print(f"         URL: {lead['profile_url']}")

            result = await send_connection(page, lead["profile_url"])

            if result == "sent":
                lead["status"] = "connect_sent"
                lead["connect_sent"] = datetime.now().isoformat()
                inviati += 1
                print(f"         OK Richiesta inviata")
            elif result == "already_connected":
                lead["status"] = "already_connected"
                print(f"         GIA' CONNESSO — marcato")
            else:
                errori += 1
                print(f"         ERRORE: {result}")

            save_leads(leads)

            if i < len(to_send):
                delay = random.uniform(15, 35)
                print(f"         Attendo {delay:.0f}s (anti-bot)...")
                await asyncio.sleep(delay)

        await browser.close()

    print(f"\n{'='*55}")
    print(f"RISULTATO: {inviati} richieste inviate | {errori} errori")
    print(f"Aspetta 24-48h per le accettazioni, poi esegui 03_send_messages.py")
    print(f"{'='*55}\n")


if __name__ == "__main__":
    asyncio.run(main())
