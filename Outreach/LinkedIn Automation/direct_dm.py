"""
LinkedIn Direct DM — Digital Empire
Strategia: cerca professionisti target → se il profilo ha il tasto "Message" disponibile
(Open Profile / 1° grado) → manda subito il DM personalizzato con framework 5 Pilastri.

NON manda connection request — bypassa completamente il problema dell'accettazione.
Piano: 20-30 DM diretti/giorno su profili con Open Profile o già connessi.

Framework 5 Pilastri (Cold DM — Giovanni, Lussemburgo):
  1. Barnum/Rainbow opener — sembra personalizzato, è universale
  2. Identità + prova — chi sei + risultato concreto in 1 frase
  3. Valore gratuito — offri prima di chiedere
  4. Micro-commitment CTA — domanda sì/no a basso attrito
  5. Anti-AI-Slop — termine tecnico di nicchia hard-coded
"""
import asyncio
import json
import os
import random
import logging
from datetime import datetime, date

BASE = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE, "direct_dm_log.txt")
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
from config import SESSION_FILE, LEADS_FILE
from personalize import generate_message

SESSION_PATH = os.path.join(BASE, SESSION_FILE)
LEADS_PATH   = os.path.join(BASE, LEADS_FILE)
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"

DAILY_DM_LIMIT = 25  # DM diretti al giorno (safe per open profiles)

# Keyword list espansa — variazioni per trovare profili diversi
TARGET_SEARCHES = [
    "avvocato Milano",        "avvocato Roma",          "avvocato Napoli",
    "avvocato Torino",        "avvocato penalista",     "avvocato civilista",
    "commercialista Milano",  "commercialista Roma",    "commercialista Torino",
    "commercialista Bologna", "studio commercialista",  "consulente fiscale",
    "fisioterapista Milano",  "fisioterapista Roma",    "studio fisioterapia",
    "fisioterapia sportiva",  "osteopata Milano",
    "psicologo Milano",       "psicologo Roma",         "psicologo clinico",
    "psicoterapeuta Milano",  "psicologo online",
    "medico estetico Milano", "medico estetico Roma",   "medicina estetica",
    "dermatologo Milano",
    "dentista Milano",        "dentista Roma",          "odontoiatra Milano",
    "studio dentistico",      "odontoiatria estetica",
    "personal trainer Milano","personal trainer Roma",  "coach fitness",
    "estetista Milano",       "centro estetico Milano", "estetista Roma",
    "palestra Milano",        "fitness Milano",
]

# Mapping keyword → nicchia per generate_message()
NICCHIA_MAP = {
    "avvocato":          "avvocato",
    "legale":            "avvocato",
    "commercialista":    "commercialista",
    "fiscale":           "commercialista",
    "fisioterapista":    "fisioterapista",
    "fisioterapia":      "fisioterapista",
    "psicologo":         "psicologo",
    "psicoterapeuta":    "psicologo",
    "medico estetico":   "medico",
    "clinica":           "medico",
    "estetista":         "estetica",
    "estetica":          "estetica",
    "personal trainer":  "palestra",
    "palestra":          "palestra",
    "dentista":          "dentista",
    "odontoiatra":       "dentista",
    "dentistico":        "dentista",
}


def nicchia_from_query(query: str) -> str:
    q = query.lower()
    for kw, n in NICCHIA_MAP.items():
        if kw in q:
            return n
    return "default"


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


async def search_and_dm_from_results(page, query: str, nicchia: str,
                                     existing_urls: set, already_messaged: set,
                                     max_dm: int, leads: list) -> int:
    """
    Cerca profili, cerca il tasto 'Message' nelle card dei risultati di ricerca
    (Open Profile mostrano il bottone inline), invia DM direttamente senza
    visitare il profilo. Più efficace per account nuovi.
    Ritorna il numero di DM inviati.
    """
    url = (
        "https://www.linkedin.com/search/results/people/"
        f"?keywords={query.replace(' ', '%20')}"
        "&origin=GLOBAL_SEARCH_HEADER"
    )
    log.info(f"  Ricerca: '{query}'")
    sent = 0
    try:
        await page.goto(url, wait_until="domcontentloaded")
        await asyncio.sleep(3)
        for _ in range(3):
            await page.evaluate("window.scrollBy(0, window.innerHeight * 2)")
            await asyncio.sleep(1.2)

        # Trova card con tasto Message visibile direttamente nei risultati
        cards_with_msg = await page.evaluate("""
            () => {
                var out = [];
                var btns = Array.from(document.querySelectorAll('button'));
                btns.forEach(function(b) {
                    if (b.offsetWidth === 0) return;
                    var aria = (b.getAttribute('aria-label') || '').toLowerCase();
                    var txt  = (b.innerText || '').toLowerCase().trim();
                    var isMsg = aria.includes('message') || aria.includes('messaggio') ||
                                txt === 'message'        || txt === 'messaggio';
                    if (!isMsg) return;
                    // Risali per trovare l'URL del profilo nella stessa card
                    var el = b;
                    for (var i = 0; i < 12; i++) {
                        if (!el) break;
                        var link = el.querySelector ? el.querySelector('a[href*="/in/"]') : null;
                        if (link) {
                            out.push({
                                profileUrl: link.href.split('?')[0].replace(/\/$/, '') + '/',
                                name: (el.querySelector('[aria-hidden="true"]') || {innerText:''}).innerText.trim()
                            });
                            break;
                        }
                        el = el.parentElement;
                    }
                });
                return out;
            }
        """)

        for card in cards_with_msg:
            if sent >= max_dm:
                break
            purl = card.get("profileUrl", "")
            name = card.get("name", "") or "Professionista"
            if not purl or purl in already_messaged or purl in existing_urls:
                continue

            # Clicca il tasto Message direttamente nella card
            clicked = await page.evaluate(f"""
                () => {{
                    var btns = Array.from(document.querySelectorAll('button'));
                    var btn = btns.find(function(b) {{
                        if (b.offsetWidth === 0) return false;
                        var aria = (b.getAttribute('aria-label') || '').toLowerCase();
                        var txt  = (b.innerText || '').toLowerCase().trim();
                        return (aria.includes('message') || aria.includes('messaggio') ||
                                txt === 'message'        || txt === 'messaggio') &&
                               b.closest('a[href*="/in/"]') === null &&
                               document.querySelector('a[href="{purl.rstrip("/")}"]') !== null;
                    }});
                    if (btn) {{ btn.click(); return true; }}
                    return false;
                }}
            """)

            if not clicked:
                continue

            await asyncio.sleep(2)
            lead_dict = {"name": name, "title": nicchia, "location": ""}
            msg = generate_message(lead_dict)
            if not msg:
                continue

            ta = await page.query_selector('.msg-form__contenteditable, [role="textbox"][contenteditable="true"]')
            if not ta:
                continue
            await ta.click()
            await asyncio.sleep(0.4)
            for char in msg:
                await ta.type(char, delay=random.uniform(15, 40))
            await asyncio.sleep(1)
            send_btn = await page.query_selector(
                'button.msg-form__send-button, button[aria-label*="Invia"], button[aria-label*="Send message"]'
            )
            if send_btn:
                await send_btn.click()
            else:
                await ta.press("Control+Enter")
            await asyncio.sleep(2)

            leads.append({
                "name": name, "title": nicchia, "location": "",
                "profile_url": purl, "search_query": query, "nicchia": nicchia,
                "source": "direct_dm", "status": "dm_sent",
                "scraped_date": str(date.today()), "commented_date": None,
                "comment_text": None, "connect_sent": None, "connect_accepted": False,
                "message_sent": datetime.now().isoformat(), "message_text": msg,
                "followup1_sent": None, "followup2_sent": None,
            })
            already_messaged.add(purl)
            existing_urls.add(purl)
            sent += 1
            log.info(f"  DM OK (search): {name[:35]} — '{msg[:60]}'")
            await hdelay(35, 60)

    except Exception as e:
        log.warning(f"  Errore search DM '{query}': {e}")
    return sent


async def search_people_by_keyword(page, query: str, existing_urls: set, max_results: int = 12) -> list[str]:
    """
    People Search → lista di URL profili da visitare.
    """
    url = (
        "https://www.linkedin.com/search/results/people/"
        f"?keywords={query.replace(' ', '%20')}"
        "&origin=GLOBAL_SEARCH_HEADER"
    )
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
        log.warning(f"  Errore ricerca '{query}': {e}")
        return []


async def extract_profile_info(page) -> tuple:
    """Estrae nome, titolo, location dalla pagina profilo già caricata."""
    try:
        info = await page.evaluate("""
            () => {
                // Nome: primo h1 nella pagina — sempre il nome su profili LinkedIn
                var h1 = document.querySelector('h1');
                var name = h1 ? h1.innerText.trim().split('\\n')[0] : '';

                // Titolo: prendi tutti i paragrafi/span nel top della pagina
                // Il titolo è di solito il secondo blocco di testo dopo l'h1
                var title = '';
                var loc = '';
                var allText = Array.from(document.querySelectorAll('main span, main div, main p'))
                    .filter(function(el) {
                        return el.children.length === 0 && el.offsetWidth > 0 &&
                               (el.innerText || '').trim().length > 5 &&
                               (el.innerText || '').trim().length < 200;
                    })
                    .map(function(el) { return el.innerText.trim(); });
                // Cerca il testo dopo il nome
                var nameIdx = allText.findIndex(function(t) { return t === name; });
                if (nameIdx >= 0 && allText[nameIdx + 1]) title = allText[nameIdx + 1];
                if (nameIdx >= 0 && allText[nameIdx + 2]) loc = allText[nameIdx + 2];
                return { name: name, title: title, location: loc };
            }
        """)
        return info.get("name", ""), info.get("title", ""), info.get("location", "")
    except Exception:
        return "", "", ""


async def check_and_send_dm(page, profile_url: str, name: str, nicchia: str, query: str) -> dict | None:
    """
    Naviga al profilo, controlla se "Message" è disponibile direttamente.
    Se sì → genera DM 5 pilastri → invia.
    Ritorna dict con i dati del lead se DM inviato, None altrimenti.
    """
    try:
        await page.goto(profile_url, wait_until="domcontentloaded")
        await asyncio.sleep(3)

        # Leggi info profilo aggiornate
        real_name, title, location = await extract_profile_info(page)
        if real_name:
            name = real_name
        final_url = page.url.split("?")[0].rstrip("/") + "/"

        # Controlla se esiste il tasto "Message" (senza dover fare Connect prima)
        # Approccio: cerca qualsiasi button/a visibile con testo Message/Messaggio
        # Escludi se dentro un article/feed-post (quelli sono bottoni di post, non profilo)
        has_message_btn = await page.evaluate("""
            () => {
                var btns = Array.from(document.querySelectorAll('button, a'));
                return btns.some(function(b) {
                    if (b.offsetWidth === 0 || b.offsetHeight === 0) return false;
                    var aria = (b.getAttribute('aria-label') || '').toLowerCase();
                    var txt  = (b.innerText || '').toLowerCase().trim();
                    var isMsg = aria.includes('messaggio') || aria.includes('message') ||
                                txt === 'messaggio'        || txt === 'message' ||
                                txt === 'invia un messaggio';
                    if (!isMsg) return false;
                    // Escludi bottoni dentro post/commenti/feed
                    var el = b;
                    for (var i = 0; i < 10; i++) {
                        if (!el) break;
                        if (el.tagName === 'ARTICLE') return false;
                        if (el.tagName === 'LI' && el.getAttribute('data-urn')) return false;
                        el = el.parentElement;
                    }
                    return true;
                });
            }
        """)

        if not has_message_btn:
            log.info(f"    No Message btn: {name[:35]} ({title[:30]})")
            return None

        # Genera il DM con framework 5 pilastri
        # Se il titolo è vuoto, usa la nicchia keyword come fallback so get_nicchia() funzioni
        lead_dict = {"name": name, "title": title or nicchia, "location": location}
        msg = generate_message(lead_dict)
        if not msg:
            log.warning(f"    DM generation failed: {name[:35]}")
            return None

        # Clicca il pulsante "Message"
        clicked = await page.evaluate("""
            () => {
                var btns = Array.from(document.querySelectorAll('button, a'));
                var btn = btns.find(function(b) {
                    if (b.offsetWidth === 0 || b.offsetHeight === 0) return false;
                    var aria = (b.getAttribute('aria-label') || '').toLowerCase();
                    var txt  = (b.innerText || '').toLowerCase().trim();
                    var isMsg = aria.includes('messaggio') || aria.includes('message') ||
                                txt === 'messaggio'        || txt === 'message' ||
                                txt === 'invia un messaggio';
                    if (!isMsg) return false;
                    var el = b;
                    for (var i = 0; i < 10; i++) {
                        if (!el) break;
                        if (el.tagName === 'ARTICLE') return false;
                        if (el.tagName === 'LI' && el.getAttribute('data-urn')) return false;
                        el = el.parentElement;
                    }
                    return true;
                });
                if (btn) { btn.scrollIntoView({ behavior: 'instant', block: 'center' }); btn.click(); return true; }
                return false;
            }
        """)

        if not clicked:
            log.warning(f"    Click Message btn failed: {name[:35]}")
            return None

        await asyncio.sleep(2)

        # Scrivi il messaggio nella chat che si è aperta
        # LinkedIn apre una chat overlay — cerca textarea o contenteditable
        ta = await page.query_selector('.msg-form__contenteditable, [role="textbox"][contenteditable="true"]')
        if not ta:
            log.warning(f"    Textarea messaggi non trovata: {name[:35]}")
            return None

        await ta.click()
        await asyncio.sleep(0.5)
        for char in msg:
            await ta.type(char, delay=random.uniform(15, 40))
        await asyncio.sleep(1)

        # Pulsante invia
        send_btn = await page.query_selector(
            'button.msg-form__send-button, '
            'button[aria-label*="Invia"], '
            'button[aria-label*="Send message"], '
            '.msg-form__send-toggle button'
        )
        if send_btn:
            await send_btn.click()
        else:
            await ta.press("Control+Enter")

        await asyncio.sleep(2)
        log.info(f"  DM OK: {name[:35]} ({title[:30]}) — '{msg[:60]}'")

        return {
            "name":           name,
            "title":          title,
            "location":       location,
            "profile_url":    final_url,
            "search_query":   query,
            "nicchia":        nicchia,
            "source":         "direct_dm",
            "status":         "dm_sent",
            "scraped_date":   str(date.today()),
            "commented_date": None,
            "comment_text":   None,
            "connect_sent":   None,
            "connect_accepted": False,
            "message_sent":   datetime.now().isoformat(),
            "message_text":   msg,
            "followup1_sent": None,
            "followup2_sent": None,
        }

    except Exception as e:
        log.warning(f"  Errore DM {profile_url[-40:]}: {e}")
        return None


async def main():
    from playwright.async_api import async_playwright

    log.info("=" * 60)
    log.info(f"DIRECT DM  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    log.info("=" * 60)

    leads = load_leads()
    existing_urls = {l["profile_url"] for l in leads}

    # Conta DM diretti già inviati oggi
    dm_today = sum(
        1 for l in leads
        if l.get("source") == "direct_dm"
        and (l.get("message_sent") or "").startswith(str(date.today()))
    )
    remaining = DAILY_DM_LIMIT - dm_today
    log.info(f"DM diretti da inviare oggi: {remaining} (limite: {DAILY_DM_LIMIT})")

    if remaining <= 0:
        log.info("Limite DM giornaliero raggiunto. Fine.")
        return

    already_messaged = {
        l["profile_url"] for l in leads if l.get("message_sent")
    }

    async with async_playwright() as pw:
        browser, ctx = await new_page(pw)
        page = await ctx.new_page()

        total_sent = 0
        searches = TARGET_SEARCHES.copy()
        random.shuffle(searches)

        for query in searches:
            if total_sent >= remaining:
                break

            nicchia = nicchia_from_query(query)
            max_this = min(5, remaining - total_sent)

            # Strategia 1: cerca il tasto Message direttamente nelle card dei risultati
            # (Open Profile mostrano il bottone inline senza visitare il profilo)
            sent_from_search = await search_and_dm_from_results(
                page, query, nicchia, existing_urls, already_messaged, max_this, leads
            )
            if sent_from_search:
                total_sent += sent_from_search
                save_leads(leads)
                log.info(f"  '{query}': {sent_from_search} DM da search results")

            if total_sent >= remaining:
                break

            # Strategia 2: visita profili singoli e cerca tasto Message
            profiles = await search_people_by_keyword(
                page, query, existing_urls | already_messaged, max_results=max_this * 2
            )

            for purl in profiles:
                if total_sent >= remaining:
                    break
                if purl in already_messaged or purl in existing_urls:
                    continue

                result = await check_and_send_dm(page, purl, "", nicchia, query)
                if result:
                    leads.append(result)
                    existing_urls.add(purl)
                    already_messaged.add(purl)
                    total_sent += 1
                    save_leads(leads)
                    await hdelay(35, 65)
                else:
                    await hdelay(5, 12)

            await hdelay(15, 25)  # pausa tra keyword

        log.info(f"\nDIRECT DM COMPLETATO — DM inviati: {total_sent}")
        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
