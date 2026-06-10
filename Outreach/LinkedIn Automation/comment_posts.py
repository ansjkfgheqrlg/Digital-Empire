"""
LinkedIn Comment Warmer — Digital Empire
Strategia: People Search per keyword → visita /recent-activity/all/ → commenta primo post.
Non usa il Content Search (inaffidabile per account nuovi, selettori cambiano spesso).

Piano: 30 commenti/giorno su professionisti italiani target.
"""
import asyncio
import json
import os
import random
import sys
import logging
from datetime import datetime, date

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

BASE = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE, "comments_log.txt")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler(),
    ],
)
log = logging.getLogger()

import sys
sys.path.insert(0, BASE)
from config import SESSION_FILE, LEADS_FILE, DAILY_COMMENT_LIMIT
from personalize import generate_comment

SESSION_PATH = os.path.join(BASE, SESSION_FILE)
LEADS_PATH   = os.path.join(BASE, LEADS_FILE)
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"

# People Search keyword → nicchia (deve corrispondere alle nicchie in personalize.py)
PEOPLE_SEARCHES = [
    # Info product / corsi online — chi vende corsi, ebook, membership
    {"keyword": "formatore corsi online",         "nicchia": "info_product"},
    {"keyword": "creatore corsi online Italia",   "nicchia": "info_product"},
    {"keyword": "info product creator",           "nicchia": "info_product"},
    {"keyword": "digital creator corsi",          "nicchia": "info_product"},
    {"keyword": "online course creator",          "nicchia": "info_product"},
    # Coach e mentor — alto ticket, programmi 1:1
    {"keyword": "business coach Italia",          "nicchia": "coach_mentor"},
    {"keyword": "life coach online",              "nicchia": "coach_mentor"},
    {"keyword": "executive coach",                "nicchia": "coach_mentor"},
    {"keyword": "business mentor Italia",         "nicchia": "coach_mentor"},
    {"keyword": "mindset coach",                  "nicchia": "coach_mentor"},
    {"keyword": "coach professionista",           "nicchia": "coach_mentor"},
    # Marketing freelance — SMM, copywriter, ads specialist
    {"keyword": "social media manager freelance", "nicchia": "marketing_freelance"},
    {"keyword": "copywriter freelance Italia",    "nicchia": "marketing_freelance"},
    {"keyword": "facebook ads specialist",        "nicchia": "marketing_freelance"},
    {"keyword": "meta ads specialist",            "nicchia": "marketing_freelance"},
    {"keyword": "consulente marketing digitale",  "nicchia": "marketing_freelance"},
    {"keyword": "performance marketing specialist","nicchia": "marketing_freelance"},
    {"keyword": "google ads specialist Italia",   "nicchia": "marketing_freelance"},
    # Agenzie di marketing digitale
    {"keyword": "agenzia marketing digitale",     "nicchia": "agenzia_marketing"},
    {"keyword": "digital agency founder",         "nicchia": "agenzia_marketing"},
    {"keyword": "agenzia social media",           "nicchia": "agenzia_marketing"},
    {"keyword": "marketing agency owner",         "nicchia": "agenzia_marketing"},
    {"keyword": "digital marketing agency Italia","nicchia": "agenzia_marketing"},
    # E-commerce / dropshipping / Shopify
    {"keyword": "ecommerce entrepreneur Italia",  "nicchia": "ecommerce"},
    {"keyword": "dropshipping Italia",            "nicchia": "ecommerce"},
    {"keyword": "shopify store owner",            "nicchia": "ecommerce"},
    {"keyword": "ecommerce manager",              "nicchia": "ecommerce"},
    {"keyword": "negozio online imprenditore",    "nicchia": "ecommerce"},
    # Consulenti che vendono servizi B2B
    {"keyword": "consulente aziendale freelance", "nicchia": "consulente_servizi"},
    {"keyword": "business consultant Italia",     "nicchia": "consulente_servizi"},
    {"keyword": "consulente strategico",          "nicchia": "consulente_servizi"},
    {"keyword": "consulente finanziario indipendente", "nicchia": "consulente_servizi"},
]


def load_leads():
    if not os.path.exists(LEADS_PATH):
        return []
    with open(LEADS_PATH, encoding="utf-8-sig") as f:
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
    ctx.set_default_timeout(25000)
    return browser, ctx


async def validate_session(page) -> bool:
    """Verifica che la sessione LinkedIn sia ancora valida."""
    try:
        await page.goto("https://www.linkedin.com/feed/", wait_until="domcontentloaded")
        await asyncio.sleep(3)
        url = page.url
        if any(s in url for s in ["login", "authwall", "checkpoint", "signup"]):
            return False
        logged_in = await page.evaluate("""
            () => !!document.querySelector('.global-nav__primary-link')
               || !!document.querySelector('a[href="/feed/"]')
               || document.title.toLowerCase().includes('feed')
        """)
        return bool(logged_in)
    except Exception:
        return False


async def search_people_by_keyword(page, keyword: str, existing_urls: set, max_results: int = 8) -> list[str]:
    """
    Cerca profili LinkedIn via People Search — restituisce lista di URL.
    Estrazione flat di tutti i link /in/ dalla pagina (robusto ai cambi DOM).
    """
    url = (
        "https://www.linkedin.com/search/results/people/"
        f"?keywords={keyword.replace(' ', '%20')}"
        "&origin=GLOBAL_SEARCH_HEADER"
    )
    log.info(f"  Ricerca persone: '{keyword}'")
    try:
        await page.goto(url, wait_until="domcontentloaded")
        await asyncio.sleep(3)

        for _ in range(3):
            await page.evaluate("window.scrollBy(0, window.innerHeight * 2)")
            await asyncio.sleep(1.2)

        all_links = await page.evaluate("""
            () => Array.from(document.querySelectorAll('a[href*="/in/"]'))
                 .map(function(a) { return a.href.split('?')[0].replace(/\\/$/, '') + '/'; })
                 .filter(function(h) { return /\\/in\\/[a-zA-Z0-9_-]+\\/$/.test(h); })
        """)

        seen = set()
        new_urls = []
        for u in all_links:
            if u not in existing_urls and u not in seen:
                seen.add(u)
                new_urls.append(u)

        log.info(f"    {len(new_urls)} profili nuovi (link totali: {len(all_links)})")
        return new_urls[:max_results]

    except Exception as e:
        log.warning(f"  Errore ricerca '{keyword}': {e}")
        return []


async def type_and_submit_comment(page, comment_text: str) -> bool:
    try:
        editors = await page.query_selector_all('.ql-editor[contenteditable="true"]')
        ta = editors[-1] if editors else None
        if not ta:
            ta = await page.query_selector('[role="textbox"][contenteditable="true"]')
        if not ta:
            log.warning("    Textarea commento non trovata")
            return False

        await ta.click()
        await asyncio.sleep(0.5)

        for char in comment_text:
            await ta.type(char, delay=random.uniform(18, 48))

        await asyncio.sleep(1)

        submit = await page.query_selector(
            'button.comments-comment-box__submit-button, '
            'button[aria-label*="Pubblica commento"], '
            'button[aria-label*="Post comment"], '
            'form.comments-comment-box button[type="submit"]'
        )
        if submit:
            await submit.click()
        else:
            await ta.press("Control+Enter")

        await asyncio.sleep(2)
        return True

    except Exception as e:
        log.warning(f"    type_and_submit_comment errore: {e}")
        return False


async def comment_on_activity(page, profile_url: str, nicchia: str, author_name: str = "") -> tuple[str | None, str]:
    """
    Visita /recent-activity/all/ del profilo e commenta il primo post visibile.
    Ritorna (testo_commento, nome_autore) se riuscito, (None, name) altrimenti.
    """
    activity_url = profile_url.rstrip("/") + "/recent-activity/all/"
    try:
        await page.goto(activity_url, wait_until="domcontentloaded")
        await asyncio.sleep(3)

        for _ in range(2):
            await page.evaluate("window.scrollBy(0, window.innerHeight)")
            await asyncio.sleep(1)

        # Estrai nome autore dalla pagina se non fornito
        if not author_name:
            author_name = await page.evaluate("""
                () => {
                    var h1 = document.querySelector('h1');
                    return h1 ? h1.innerText.trim().split('\\n')[0] : '';
                }
            """) or "Professionista"

        # Estrai testo del primo post per commento contestuale
        post_text = await page.evaluate("""
            () => {
                var spans = Array.from(document.querySelectorAll(
                    'span[dir="ltr"], .break-words span, .feed-shared-update-v2__description span, p'
                ));
                var best = '';
                for (var i = 0; i < spans.length; i++) {
                    var t = (spans[i].innerText || '').trim();
                    if (t.length > best.length && t.length < 500) best = t;
                }
                return best.slice(0, 300);
            }
        """)

        comment = generate_comment(post_text, nicchia, author_name)
        if not comment:
            return None

        # Clicca il primo pulsante "Commenta" visibile
        clicked = await page.evaluate("""
            () => {
                var btns = Array.from(document.querySelectorAll('button'));
                var btn = btns.find(function(b) {
                    if (b.offsetWidth === 0) return false;
                    var aria = (b.getAttribute('aria-label') || '').toLowerCase();
                    var txt  = (b.innerText || '').toLowerCase().trim();
                    return aria.includes('commenta') || aria.includes('comment') ||
                           txt === 'commenta'        || txt === 'comment';
                });
                if (btn) {
                    btn.scrollIntoView({ behavior: 'instant', block: 'center' });
                    btn.click();
                    return true;
                }
                return false;
            }
        """)

        if not clicked:
            log.info(f"    No comment button: {author_name[:30]}")
            return None, author_name

        await asyncio.sleep(2)
        success = await type_and_submit_comment(page, comment)
        if success:
            return comment, author_name
        return None, author_name

    except Exception as e:
        log.warning(f"    Errore attività {profile_url[-40:]}: {e}")
        return None, author_name


async def main():
    from playwright.async_api import async_playwright

    log.info("=" * 60)
    log.info(f"COMMENT WARMER  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    log.info("=" * 60)

    leads = load_leads()
    existing_urls = {l["profile_url"] for l in leads}

    commented_today = sum(
        1 for l in leads
        if (l.get("commented_date") or "").startswith(str(date.today()))
    )
    remaining = DAILY_COMMENT_LIMIT - commented_today
    log.info(f"Commenti da fare oggi: {remaining} (limite: {DAILY_COMMENT_LIMIT})")

    if remaining <= 0:
        log.info("Limite commenti giornaliero raggiunto. Fine.")
        return

    already_commented = {
        l["profile_url"] for l in leads if l.get("commented_date")
    }

    async with async_playwright() as pw:
        browser, ctx = await new_page(pw)
        page = await ctx.new_page()

        log.info("Verifica sessione LinkedIn...")
        if not await validate_session(page):
            log.error("[ERRORE] Sessione LinkedIn scaduta. Esegui: python refresh_session.py")
            await browser.close()
            sys.exit(1)
        log.info("  Sessione valida [OK]")

        total_commented = 0
        searches = PEOPLE_SEARCHES.copy()
        random.shuffle(searches)

        for search_info in searches:
            if total_commented >= remaining:
                break

            max_this = min(4, remaining - total_commented)
            profile_urls = await search_people_by_keyword(
                page, search_info["keyword"], already_commented | existing_urls, max_results=max_this
            )
            nicchia = search_info["nicchia"]

            for purl in profile_urls:
                if total_commented >= remaining:
                    break
                if purl in already_commented:
                    continue

                comment_text, name = await comment_on_activity(page, purl, nicchia)
                if comment_text:
                    already_commented.add(purl)
                    total_commented += 1

                    existing = next((l for l in leads if l["profile_url"] == purl), None)
                    if existing:
                        existing["commented_date"] = str(date.today())
                        existing["comment_text"]   = comment_text
                        existing["status"] = existing.get("status") or "commented"
                    else:
                        leads.append({
                            "name":             name,
                            "title":            "",
                            "location":         "",
                            "profile_url":      purl,
                            "search_query":     search_info["keyword"],
                            "nicchia":          nicchia,
                            "source":           "comment_warmer",
                            "status":           "commented",
                            "scraped_date":     str(date.today()),
                            "commented_date":   str(date.today()),
                            "comment_text":     comment_text,
                            "connect_sent":     None,
                            "connect_accepted": False,
                            "message_sent":     None,
                            "followup1_sent":   None,
                            "followup2_sent":   None,
                        })
                        existing_urls.add(purl)

                    save_leads(leads)
                    log.info(f"  COMMENT OK [{total_commented}/{remaining}]: {name[:30]} ({nicchia}) — '{comment_text[:55]}'")
                    await hdelay(30, 55)
                else:
                    await hdelay(5, 10)

            await hdelay(15, 25)  # pausa tra keyword diverse

        log.info(f"\nCOMMENT WARMER COMPLETATO — Commenti inviati: {total_commented}")
        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
