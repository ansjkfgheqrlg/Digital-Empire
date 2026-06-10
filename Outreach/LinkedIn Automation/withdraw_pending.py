"""
Ritira le richieste di connessione sbagliate di oggi.
Script one-shot — da eseguire una volta sola.

Naviga su ogni profilo con status 'wrong_target_sent',
clicca 'In sospeso' → 'Ritira invito', aggiorna il DB.
"""
import asyncio
import json
import os
import random
import logging
from datetime import datetime

BASE = os.path.dirname(os.path.abspath(__file__))
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(message)s",
    handlers=[logging.StreamHandler()],
)
log = logging.getLogger()

import sys
sys.path.insert(0, BASE)
from config import SESSION_FILE, LEADS_FILE

SESSION_PATH = os.path.join(BASE, SESSION_FILE)
LEADS_PATH   = os.path.join(BASE, LEADS_FILE)
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"


def load_leads():
    with open(LEADS_PATH, encoding="utf-8") as f:
        return json.load(f)


def save_leads(leads):
    with open(LEADS_PATH, "w", encoding="utf-8") as f:
        json.dump(leads, f, ensure_ascii=False, indent=2)


async def withdraw_invite(page, profile_url: str) -> str:
    """
    Naviga al profilo, clicca 'In sospeso' → 'Ritira invito'.
    Ritorna: 'withdrawn' / 'not_pending' / 'error'
    """
    try:
        await page.goto(profile_url, wait_until="domcontentloaded")
        await asyncio.sleep(3)

        # Cerca il pulsante "In sospeso" (già cliccato → dropdown con "Ritira")
        pending_result = await page.evaluate("""
            () => {
                const all = Array.from(document.querySelectorAll('a, button'));
                const pendingBtn = all.find(el => {
                    if (el.offsetWidth === 0) return false;
                    const txt  = (el.innerText || '').toLowerCase().trim();
                    const aria = (el.getAttribute('aria-label') || '').toLowerCase();
                    return txt.includes('in sospeso') || txt.includes('pending') ||
                           aria.includes('in sospeso') || aria.includes('pending');
                });
                if (pendingBtn) {
                    pendingBtn.scrollIntoView({ behavior: 'instant', block: 'center' });
                    pendingBtn.click();
                    return 'clicked_pending';
                }
                return 'not_pending';
            }
        """)

        if pending_result == 'not_pending':
            log.info(f"  Non in sospeso: {profile_url[-45:]}")
            return "not_pending"

        await asyncio.sleep(1.5)

        # Cerca "Ritira invito" nel dropdown che appare
        withdrew = await page.evaluate("""
            () => {
                const items = Array.from(document.querySelectorAll(
                    'li, div[role="option"], button, a'
                ));
                const ritira = items.find(el => {
                    if (el.offsetWidth === 0) return false;
                    const txt = (el.innerText || '').toLowerCase();
                    return txt.includes('ritira') || txt.includes('withdraw') ||
                           txt.includes('annulla') && txt.includes('invito');
                });
                if (ritira) {
                    ritira.click();
                    return 'clicked_withdraw';
                }
                return 'no_withdraw_option';
            }
        """)

        await asyncio.sleep(2)

        if withdrew == 'clicked_withdraw':
            # Eventuale conferma modale
            try:
                await page.click(
                    'button:has-text("Ritira"), button:has-text("Withdraw")',
                    timeout=3000
                )
                await asyncio.sleep(1)
            except Exception:
                pass
            log.info(f"  RITIRATO: {profile_url[-45:]}")
            return "withdrawn"
        else:
            log.warning(f"  Opzione Ritira non trovata su {profile_url[-45:]}")
            return "error"

    except Exception as e:
        log.warning(f"  Errore su {profile_url[-45:]}: {e}")
        return "error"


async def main():
    from playwright.async_api import async_playwright

    leads = load_leads()
    wrong = [l for l in leads if l.get("status") == "wrong_target_sent"]

    log.info(f"Richieste da ritirare: {len(wrong)}")
    if not wrong:
        log.info("Nessun 'wrong_target_sent' trovato. Fine.")
        return

    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=False, args=["--start-maximized"])
        ctx = await browser.new_context(
            storage_state=SESSION_PATH,
            viewport={"width": 1280, "height": 800},
            user_agent=UA,
        )
        ctx.set_default_timeout(20000)
        page = await ctx.new_page()

        withdrawn = 0
        for i, lead in enumerate(wrong):
            purl = lead["profile_url"]
            log.info(f"[{i+1}/{len(wrong)}] {purl[-45:]}")
            result = await withdraw_invite(page, purl)
            if result == "withdrawn":
                lead["status"] = "withdrawn"
                lead["withdrawn_date"] = str(datetime.now().date())
                withdrawn += 1
            elif result == "not_pending":
                lead["status"] = "expired_or_accepted"
            save_leads(leads)
            await asyncio.sleep(random.uniform(8, 15))

        log.info(f"\nCompletato — Ritirati: {withdrawn}/{len(wrong)}")
        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
