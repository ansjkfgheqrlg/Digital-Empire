"""
Step 4: Invia il primo messaggio alle connessioni accettate.
Messaggio personalizzato via Claude API (Barnum Effect + valore gratis).

Regola deliverability LinkedIn:
- ZERO link nel primo messaggio (stesso principio email fredda)
- Max 90 parole
- Aspetta 24h dall'accettazione prima di inviare

Run: python 04_send_messages.py
Run: python 04_send_messages.py --dry-run
"""
import json
import asyncio
import random
import sys
from datetime import date, datetime, timedelta
from playwright.async_api import async_playwright
from config import SESSION_FILE, LEADS_FILE, DAILY_MESSAGE_LIMIT, DELAY_MIN_SECONDS, DELAY_MAX_SECONDS
from personalize import generate_message


def load_leads():
    with open(LEADS_FILE, encoding="utf-8") as f:
        return json.load(f)


def save_leads(leads):
    with open(LEADS_FILE, "w", encoding="utf-8") as f:
        json.dump(leads, f, ensure_ascii=False, indent=2)


def is_ready_for_message(lead: dict) -> bool:
    if lead.get("status") != "connected":
        return False
    if lead.get("message_sent"):
        return False
    # Aspetta almeno 24h dall'accettazione
    connected_date = lead.get("connected_date")
    if connected_date:
        delta = date.today() - date.fromisoformat(connected_date)
        if delta.days < 1:
            return False
    return True


async def send_linkedin_message(page, profile_url: str, message: str) -> str:
    """Apre il profilo e invia un messaggio. Ritorna 'sent' o 'error'."""
    await page.goto(profile_url)
    await page.wait_for_load_state("networkidle")
    await asyncio.sleep(random.uniform(3, 6))

    msg_btn = None
    selectors = [
        'button[aria-label*="Messaggio"], button[aria-label*="Message"]',
        '.pvs-profile-actions button:has-text("Messaggio")',
        '.pvs-profile-actions button:has-text("Message")',
    ]
    for sel in selectors:
        try:
            btn = await page.query_selector(sel)
            if btn:
                msg_btn = btn
                break
        except Exception:
            continue

    if not msg_btn:
        return "error_no_button"

    await msg_btn.click()
    await asyncio.sleep(random.uniform(2, 4))

    # Trova la textarea del messaggio
    textarea = await page.query_selector('.msg-form__contenteditable')
    if not textarea:
        textarea = await page.query_selector('[data-placeholder="Scrivi un messaggio…"], [data-placeholder="Write a message…"]')
    if not textarea:
        return "error_no_textarea"

    await textarea.click()
    # Digita il messaggio carattere per carattere per sembrare umano
    for char in message:
        await textarea.type(char, delay=random.uniform(20, 60))

    await asyncio.sleep(random.uniform(1, 3))

    send_btn = await page.query_selector('button[aria-label*="Invia"], button[aria-label*="Send"]')
    if send_btn:
        await send_btn.click()
        await asyncio.sleep(random.uniform(2, 4))
        return "sent"
    else:
        # Prova Enter
        await textarea.press("Enter")
        return "sent"


async def main():
    dry_run = "--dry-run" in sys.argv

    leads = load_leads()
    to_message = [l for l in leads if is_ready_for_message(l)][:DAILY_MESSAGE_LIMIT]

    print(f"\n{'='*55}")
    print(f"  04_send_messages.py — primo messaggio")
    print(f"{'='*55}")
    print(f"  Connessi pronti per messaggio: {len(to_message)}")
    print(f"  Limite giornaliero: {DAILY_MESSAGE_LIMIT}")
    print(f"{'='*55}\n")

    if not to_message:
        print("Nessun contatto pronto. Esegui prima 03_check_accepted.py.")
        return

    # Genera messaggi in anticipo
    print("Genero messaggi personalizzati...")
    for lead in to_message:
        lead["_msg_preview"] = generate_message(lead)
        print(f"  {lead['name'][:40]}: {lead['_msg_preview'][:80]}...")

    if dry_run:
        print("\nDRY-RUN — nessun messaggio inviato.")
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

        for i, lead in enumerate(to_message, 1):
            msg = lead.pop("_msg_preview")
            print(f"[{i:02d}/{len(to_message)}] {lead['name'][:45]}")
            print(f"         Msg: {msg[:80]}...")

            result = await send_linkedin_message(page, lead["profile_url"], msg)

            if result == "sent":
                lead["status"] = "message_sent"
                lead["message_sent"] = datetime.now().isoformat()
                lead["message_text"] = msg
                inviati += 1
                print(f"         OK Messaggio inviato")
            else:
                errori += 1
                print(f"         ERRORE: {result}")

            save_leads(leads)

            if i < len(to_message):
                delay = random.uniform(30, 90)
                print(f"         Attendo {delay:.0f}s...")
                await asyncio.sleep(delay)

        await browser.close()

    print(f"\n{'='*55}")
    print(f"RISULTATO: {inviati} messaggi inviati | {errori} errori")
    print(f"Esegui 05_send_followups.py dopo 3-4 giorni")
    print(f"{'='*55}\n")


if __name__ == "__main__":
    asyncio.run(main())
