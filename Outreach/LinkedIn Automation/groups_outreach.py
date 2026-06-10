"""
LinkedIn Groups Direct Messaging — Digital Empire
Strategia: entrare nei gruppi professionali italiani → inviare DM diretti ai membri
SENZA richiesta di connessione — i membri del gruppo si possono messaggiare liberamente.

Gruppi target:
- Avvocati Italiani, Commercialisti, Fisioterapisti, Psicologi, Dentisti, ecc.
"""
import asyncio
import json
import os
import random
import logging
from datetime import datetime, date

BASE = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE, "groups_log.txt")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler(),
    ]
)
log = logging.getLogger()

import sys
sys.path.insert(0, BASE)
from config import SESSION_FILE, LEADS_FILE, DAILY_MESSAGE_LIMIT
from personalize import generate_message

SESSION_PATH = os.path.join(BASE, SESSION_FILE)
LEADS_PATH   = os.path.join(BASE, LEADS_FILE)
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"

# ── GRUPPI PROFESSIONALI ITALIANI ─────────────────────────────────────────────
# Questi URL vanno verificati/aggiornati — LinkedIn cambia gli ID dei gruppi
# Il formato è: linkedin.com/groups/[ID]/
GRUPPI_TARGET = [
    # Avvocati
    {"url": "https://www.linkedin.com/groups/63947/",   "nicchia": "avvocato",       "nome": "Avvocati Italiani"},
    {"url": "https://www.linkedin.com/groups/2259681/", "nicchia": "avvocato",       "nome": "Diritto e Legge Italia"},
    # Commercialisti
    {"url": "https://www.linkedin.com/groups/3753556/", "nicchia": "commercialista", "nome": "Commercialisti e Consulenti Fiscali"},
    {"url": "https://www.linkedin.com/groups/1841698/", "nicchia": "commercialista", "nome": "Dottori Commercialisti"},
    # Fisioterapisti
    {"url": "https://www.linkedin.com/groups/3989682/", "nicchia": "fisioterapista", "nome": "Fisioterapisti Italia"},
    {"url": "https://www.linkedin.com/groups/6519539/", "nicchia": "fisioterapista", "nome": "Riabilitazione e Fisioterapia"},
    # Psicologi
    {"url": "https://www.linkedin.com/groups/2187747/", "nicchia": "psicologo",      "nome": "Psicologi Italiani"},
    {"url": "https://www.linkedin.com/groups/4221878/", "nicchia": "psicologo",      "nome": "Psicologia Clinica Italia"},
    # Dentisti
    {"url": "https://www.linkedin.com/groups/3156498/", "nicchia": "dentista",       "nome": "Odontoiatri Italiani"},
    {"url": "https://www.linkedin.com/groups/135288/",  "nicchia": "dentista",       "nome": "Dental Network Italia"},
    # Medici
    {"url": "https://www.linkedin.com/groups/1835433/", "nicchia": "medico",         "nome": "Medici Italiani"},
    # Estetisti / Beauty
    {"url": "https://www.linkedin.com/groups/4387456/", "nicchia": "estetica",       "nome": "Estetica e Benessere Italia"},
    # Palestre / Personal Trainer
    {"url": "https://www.linkedin.com/groups/4054841/", "nicchia": "palestra",       "nome": "Personal Trainer Italia"},
]


def load_leads():
    if not os.path.exists(LEADS_PATH):
        return []
    with open(LEADS_PATH, encoding="utf-8") as f:
        return json.load(f)


def save_leads(leads):
    with open(LEADS_PATH, "w", encoding="utf-8") as f:
        json.dump(leads, f, ensure_ascii=False, indent=2)


async def hdelay(a=8, b=20):
    await asyncio.sleep(random.uniform(a, b))


async def new_page(playwright):
    browser = await playwright.chromium.launch(headless=False, args=["--start-maximized"])
    ctx = await browser.new_context(
        storage_state=SESSION_PATH,
        viewport={"width": 1280, "height": 800},
        user_agent=UA,
    )
    ctx.set_default_timeout(20000)
    return browser, ctx


# ── FASE A: TROVA E UNISCITI AI GRUPPI ────────────────────────────────────────

async def find_and_join_groups(page):
    """Cerca gruppi LinkedIn professionali italiani e unisciti."""
    log.info("FASE A — Ricerca e join gruppi professionali italiani")

    joined = []
    for gruppo in GRUPPI_TARGET:
        try:
            log.info(f"  Navigando: {gruppo['nome']}")
            await page.goto(gruppo["url"], wait_until="domcontentloaded")
            await asyncio.sleep(3)

            # Controlla se già membro o se c'è pulsante per unirsi
            stato = await page.evaluate("""
                () => {
                    const btns = Array.from(document.querySelectorAll('button, a'));
                    const joined = btns.find(b => {
                        const t = (b.innerText || '').toLowerCase();
                        return t.includes('membro') || t.includes('member') || t.includes('lascia');
                    });
                    if (joined) return 'already_member';
                    const joinBtn = btns.find(b => {
                        const t = (b.innerText || '').toLowerCase();
                        const a = (b.getAttribute('aria-label') || '').toLowerCase();
                        return t.includes('unisciti') || t.includes('join') || a.includes('join');
                    });
                    if (joinBtn) { joinBtn.click(); return 'join_clicked'; }
                    return 'not_found';
                }
            """)
            log.info(f"    → {stato}")
            if stato in ("already_member", "join_clicked"):
                joined.append(gruppo)
            await asyncio.sleep(2)
        except Exception as e:
            log.warning(f"  Errore gruppo {gruppo['nome']}: {e}")

    log.info(f"FASE A completata — {len(joined)} gruppi accessibili")
    return joined


# ── FASE B: ESTRAI MEMBRI DAL GRUPPO ──────────────────────────────────────────

async def get_group_members(page, gruppo_url: str, max_members: int = 30) -> list[str]:
    """Estrae URL profili dei membri dal gruppo."""
    members_url = gruppo_url.rstrip("/") + "/members/"
    await page.goto(members_url, wait_until="domcontentloaded")
    await asyncio.sleep(4)

    # Scroll per caricare più membri
    for _ in range(3):
        await page.evaluate("window.scrollBy(0, window.innerHeight * 2)")
        await asyncio.sleep(1.5)

    urls = await page.evaluate("""
        () => Array.from(document.querySelectorAll('a[href*="/in/"]'))
             .map(a => a.href.split('?')[0].replace(/\\/$/, '') + '/')
             .filter(h => /\\/in\\/[a-zA-Z0-9_-]+\\/$/.test(h))
    """)
    unique = list(dict.fromkeys(urls))
    log.info(f"    Trovati {len(unique)} profili nel gruppo")
    return unique[:max_members]


# ── FASE C: INVIA DM DIRETTO (senza connessione) ──────────────────────────────

async def send_direct_message(page, profile_url: str, message: str) -> str:
    """
    Naviga al profilo di un membro del gruppo e invia DM diretto.
    I membri del gruppo possono scriversi senza essere connessi.
    Ritorna: 'sent' / 'no_button' / 'error'
    """
    try:
        await page.goto(profile_url, wait_until="domcontentloaded")
        await asyncio.sleep(3)

        # Leggi nome per personalizzare e verificare che è nella pagina giusta
        name_el = await page.query_selector("h1")
        name = (await name_el.inner_text()).strip() if name_el else "Utente"
        title_el = await page.query_selector(".text-body-medium")
        title = (await title_el.inner_text()).strip() if title_el else ""
        loc_el = await page.query_selector(".text-body-small.inline")
        loc = (await loc_el.inner_text()).strip() if loc_el else ""

        # Cerca pulsante "Messaggio" / "Message" (disponibile per membri stesso gruppo)
        msg_btn = await page.evaluate("""
            () => {
                const all = Array.from(document.querySelectorAll('a, button'));
                const btn = all.find(el => {
                    if (el.offsetWidth === 0) return false;
                    const aria = (el.getAttribute('aria-label') || '').toLowerCase();
                    const txt = (el.innerText || '').toLowerCase().trim();
                    return (aria.includes('messaggio') || aria.includes('message') ||
                            txt === 'messaggio' || txt === 'message');
                });
                if (btn) { btn.click(); return 'clicked'; }
                return 'not_found';
            }
        """)

        if msg_btn == "not_found":
            log.info(f"    No messaggio diretto per {name[:30]} (non stesso gruppo o connessione richiesta)")
            return "no_button"

        await asyncio.sleep(2)

        # Trova textarea del messaggio
        ta = await page.query_selector('.msg-form__contenteditable, [data-placeholder*="messaggio"], [data-placeholder*="message"], [role="textbox"]')
        if not ta:
            log.warning(f"    Textarea non trovata per {name[:30]}")
            return "no_textarea"

        await ta.click()
        # Digita carattere per carattere con delay umano
        for char in message:
            await ta.type(char, delay=random.uniform(15, 45))

        await asyncio.sleep(1)

        # Invia
        send_btn = await page.query_selector('button[aria-label*="Invia"], button[aria-label*="Send"]')
        if send_btn:
            await send_btn.click()
        else:
            await ta.press("Enter")

        await asyncio.sleep(2)

        log.info(f"    DM inviato → {name[:30]} ({title[:30]})")
        return "sent", name, title, loc

    except Exception as e:
        log.warning(f"    send_direct_message errore: {e}")
        return "error", "", "", ""


# ── MAIN ──────────────────────────────────────────────────────────────────────

async def main():
    from playwright.async_api import async_playwright

    log.info("=" * 60)
    log.info(f"GROUPS OUTREACH  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    log.info("=" * 60)

    leads = load_leads()
    existing_urls = {l["profile_url"] for l in leads}

    # Conta messaggi già inviati oggi
    sent_today = sum(
        1 for l in leads
        if (l.get("group_dm_sent") or "").startswith(str(date.today()))
    )
    remaining = DAILY_MESSAGE_LIMIT - sent_today
    log.info(f"DM diretti da inviare oggi: {remaining} (limite: {DAILY_MESSAGE_LIMIT})")

    if remaining <= 0:
        log.info("Limite giornaliero raggiunto. Fine.")
        return

    async with async_playwright() as pw:
        browser, ctx = await new_page(pw)
        page = await ctx.new_page()

        total_sent = 0

        for gruppo in GRUPPI_TARGET:
            if total_sent >= remaining:
                break

            log.info(f"\nGruppo: {gruppo['nome']} ({gruppo['nicchia']})")

            try:
                member_urls = await get_group_members(page, gruppo["url"], max_members=40)
                new_urls = [u for u in member_urls if u not in existing_urls]
                log.info(f"  Nuovi profili: {len(new_urls)}")

                for purl in new_urls:
                    if total_sent >= remaining:
                        break

                    # Naviga al profilo e genera messaggio personalizzato
                    await page.goto(purl, wait_until="domcontentloaded")
                    await asyncio.sleep(3)

                    name_el = await page.query_selector("h1")
                    name = (await name_el.inner_text()).strip() if name_el else "Professionista"
                    title_el = await page.query_selector(".text-body-medium")
                    title = (await title_el.inner_text()).strip() if title_el else gruppo["nicchia"]
                    loc_el = await page.query_selector(".text-body-small.inline")
                    loc = (await loc_el.inner_text()).strip() if loc_el else ""

                    lead_tmp = {"name": name, "title": title, "location": loc,
                                "profile_url": purl, "search_query": gruppo["nome"]}

                    msg = generate_message(lead_tmp)

                    result = await send_direct_message(page, purl, msg)
                    r_status = result[0] if isinstance(result, tuple) else result
                    r_name   = result[1] if isinstance(result, tuple) and len(result) > 1 else name
                    r_title  = result[2] if isinstance(result, tuple) and len(result) > 2 else title
                    r_loc    = result[3] if isinstance(result, tuple) and len(result) > 3 else loc

                    lead_record = {
                        "name": r_name,
                        "title": r_title,
                        "location": r_loc,
                        "profile_url": purl.split("?")[0].rstrip("/") + "/",
                        "search_query": gruppo["nome"],
                        "nicchia": gruppo["nicchia"],
                        "source": "group_dm",
                        "status": "group_dm_sent" if r_status == "sent" else r_status,
                        "scraped_date": str(date.today()),
                        "group_dm_sent": datetime.now().isoformat() if r_status == "sent" else None,
                        "group_dm_text": msg if r_status == "sent" else None,
                        "connect_sent": None,
                        "connect_accepted": False,
                        "message_sent": None,
                        "followup1_sent": None,
                        "followup2_sent": None,
                    }
                    leads.append(lead_record)
                    existing_urls.add(lead_record["profile_url"])

                    if r_status == "sent":
                        total_sent += 1
                        log.info(f"  DM [{total_sent}/{remaining}]: {r_name[:30]} — {r_title[:30]}")

                    save_leads(leads)
                    await hdelay(20, 40)  # delay più lungo per DM diretti (meno aggressivo)

            except Exception as e:
                log.warning(f"  Errore gruppo {gruppo['nome']}: {e}")

        log.info(f"\nGROUPS OUTREACH COMPLETATO — DM inviati: {total_sent}")
        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
