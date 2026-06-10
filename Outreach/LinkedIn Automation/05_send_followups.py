"""
Step 5: Invia follow-up nella sequenza corretta.

Sequenza (dal notebook NotebookLM - framework confermato):
- Follow-up 1 (giorno 3-4): nudge breve, ZERO link, tasso risposta 40%
- Follow-up 2 (giorno 7): info dump + PRIMO link, tasso risposta 30%

Run: python 05_send_followups.py
Run: python 05_send_followups.py --dry-run
"""
import json
import asyncio
import random
import sys
from datetime import date, datetime, timedelta
from playwright.async_api import async_playwright
from config import SESSION_FILE, LEADS_FILE, DAILY_MESSAGE_LIMIT, AGENCY_URL
from personalize import generate_followup1, generate_followup2


def load_leads():
    with open(LEADS_FILE, encoding="utf-8") as f:
        return json.load(f)


def save_leads(leads):
    with open(LEADS_FILE, "w", encoding="utf-8") as f:
        json.dump(leads, f, ensure_ascii=False, indent=2)


def days_since(date_str: str) -> int:
    if not date_str:
        return 999
    try:
        sent = datetime.fromisoformat(date_str).date()
        return (date.today() - sent).days
    except Exception:
        return 999


def get_followup_queue(leads) -> list:
    """Ritorna lista di (lead, followup_type) da inviare oggi."""
    queue = []
    for lead in leads:
        if lead.get("status") not in ("message_sent", "followup1_sent"):
            continue
        if lead.get("followup2_sent"):
            continue

        msg_days = days_since(lead.get("message_sent"))
        f1_days = days_since(lead.get("followup1_sent"))

        if not lead.get("followup1_sent") and msg_days >= 3:
            queue.append((lead, "followup1"))
        elif lead.get("followup1_sent") and not lead.get("followup2_sent") and f1_days >= 3:
            queue.append((lead, "followup2"))

    return queue[:DAILY_MESSAGE_LIMIT]


async def send_message_to_conversation(page, profile_url: str, message: str) -> str:
    """Apre conversazione esistente e invia follow-up nello stesso thread."""
    await page.goto(profile_url)
    await page.wait_for_load_state("networkidle")
    await asyncio.sleep(random.uniform(3, 5))

    msg_btn = await page.query_selector('button[aria-label*="Messaggio"], button[aria-label*="Message"]')
    if not msg_btn:
        return "error_no_button"

    await msg_btn.click()
    await asyncio.sleep(random.uniform(2, 3))

    textarea = await page.query_selector('.msg-form__contenteditable')
    if not textarea:
        return "error_no_textarea"

    await textarea.click()
    for char in message:
        await textarea.type(char, delay=random.uniform(20, 60))

    await asyncio.sleep(random.uniform(1, 2))

    send_btn = await page.query_selector('button[aria-label*="Invia"], button[aria-label*="Send"]')
    if send_btn:
        await send_btn.click()
    else:
        await textarea.press("Enter")

    await asyncio.sleep(random.uniform(2, 3))
    return "sent"


async def main():
    dry_run = "--dry-run" in sys.argv

    leads = load_leads()
    queue = get_followup_queue(leads)

    print(f"\n{'='*55}")
    print(f"  05_send_followups.py — follow-up sequenza")
    print(f"{'='*55}")
    f1_count = sum(1 for _, t in queue if t == "followup1")
    f2_count = sum(1 for _, t in queue if t == "followup2")
    print(f"  Follow-up 1 (giorno 3-4, no link): {f1_count}")
    print(f"  Follow-up 2 (giorno 7, CON link):  {f2_count}")
    print(f"{'='*55}\n")

    if not queue:
        print("Nessun follow-up da inviare oggi.")
        return

    # Genera messaggi
    for lead, ftype in queue:
        if ftype == "followup1":
            lead["_msg_preview"] = generate_followup1(lead)
        else:
            lead["_msg_preview"] = generate_followup2(lead, AGENCY_URL)
        name = lead['name'][:35]
        print(f"  [{ftype}] {name}: {lead['_msg_preview'][:70]}...")

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

        for i, (lead, ftype) in enumerate(queue, 1):
            msg = lead.pop("_msg_preview")
            print(f"[{i:02d}/{len(queue)}] [{ftype}] {lead['name'][:40]}")

            result = await send_message_to_conversation(page, lead["profile_url"], msg)

            if result == "sent":
                inviati += 1
                if ftype == "followup1":
                    lead["status"] = "followup1_sent"
                    lead["followup1_sent"] = datetime.now().isoformat()
                else:
                    lead["status"] = "followup2_sent"
                    lead["followup2_sent"] = datetime.now().isoformat()
                print(f"         OK")
            else:
                errori += 1
                print(f"         ERRORE: {result}")

            save_leads(leads)

            if i < len(queue):
                delay = random.uniform(30, 90)
                print(f"         Attendo {delay:.0f}s...")
                await asyncio.sleep(delay)

        await browser.close()

    print(f"\n{'='*55}")
    print(f"RISULTATO: {inviati} follow-up inviati | {errori} errori")
    print(f"{'='*55}\n")


if __name__ == "__main__":
    asyncio.run(main())
