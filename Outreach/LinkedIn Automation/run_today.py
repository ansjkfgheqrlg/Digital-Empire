"""
Runner giornaliero completo — silenzioso, zero terminali.
Il browser LinkedIn appare (necessario per evitare ban).

Strategia profili (in ordine):
  1. Lead "new" già salvati in database → invia connessione
  2. People You May Know → nuovi profili con URL reali → naviga, controlla titolo, connetti
  3. Connetti a qualunque PYMK se ancora sotto il limite (warmup account)

  Giorno successivo all'accettazione: messaggio AI personalizzato
  Giorno 3-4: follow-up senza link
  Giorno 7: follow-up con link agenzia

Log in: run_today_log.txt
"""
import asyncio
import json
import os
import random
import sys
import logging
from datetime import datetime, date

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# ── LOG ──────────────────────────────────────────────────────────────────────
BASE = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE, "run_today_log.txt")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler(sys.stdout),
    ]
)
log = logging.getLogger()

# ── CONFIG ───────────────────────────────────────────────────────────────────
sys.path.insert(0, BASE)
from config import (
    SESSION_FILE, LEADS_FILE,
    DAILY_CONNECT_LIMIT, DAILY_MESSAGE_LIMIT, AGENCY_URL
)
from personalize import generate_message, generate_followup1, generate_followup2, generate_connection_note

SESSION_PATH = os.path.join(BASE, SESSION_FILE)
LEADS_PATH   = os.path.join(BASE, LEADS_FILE)

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"

# Query keyword per la ricerca profili target (LinkedIn People Search)
TARGET_SEARCHES = [
    "formatore corsi online Italia",
    "creatore corsi online",
    "info product creator",
    "business coach Italia",
    "life coach online",
    "executive coach",
    "business mentor Italia",
    "mindset coach",
    "social media manager freelance",
    "copywriter freelance Italia",
    "facebook ads specialist",
    "meta ads specialist",
    "consulente marketing digitale",
    "performance marketing specialist",
    "agenzia marketing digitale",
    "digital agency founder",
    "agenzia social media",
    "ecommerce entrepreneur Italia",
    "dropshipping Italia",
    "shopify store owner",
    "consulente aziendale freelance",
    "business consultant Italia",
]

# Parole chiave delle nicchie target
TARGET_KEYWORDS = [
    # Info product / corsi
    "corso", "corsi", "formatore", "formazione", "infoprodotto", "ebook",
    "membership", "lancio", "insegno", "programma online",
    # Coach / mentor
    "coach", "coaching", "mentor", "mentoring", "mindset",
    # Marketing freelance
    "social media manager", "smm", "copywriter", "facebook ads", "meta ads",
    "google ads", "ads specialist", "marketing", "consulente", "digital",
    # E-commerce
    "ecommerce", "e-commerce", "shopify", "dropshipping",
    # Agenzia
    "agenzia", "agency",
    # Business / imprenditore
    "imprenditore", "business", "freelance", "venditore",
]


# ── HELPERS ───────────────────────────────────────────────────────────────────

def load_leads():
    if not os.path.exists(LEADS_PATH):
        return []
    with open(LEADS_PATH, encoding="utf-8-sig") as f:
        return json.load(f)


def save_leads(leads):
    with open(LEADS_PATH, "w", encoding="utf-8") as f:
        json.dump(leads, f, ensure_ascii=False, indent=2)


def days_since(date_str):
    if not date_str:
        return 999
    try:
        d = datetime.fromisoformat(date_str).date()
        return (date.today() - d).days
    except Exception:
        return 999


def is_target_profession(title):
    """Controlla se il titolo è nella nostra nicchia target."""
    if not title:
        return False
    tl = title.lower()
    return any(kw in tl for kw in TARGET_KEYWORDS)


async def hdelay(a=8, b=20):
    await asyncio.sleep(random.uniform(a, b))


async def new_browser(playwright):
    browser = await playwright.chromium.launch(headless=False, args=["--start-maximized"])
    ctx = await browser.new_context(
        storage_state=SESSION_PATH,
        viewport={"width": 1280, "height": 800},
        user_agent=UA,
    )
    ctx.set_default_timeout(25000)
    return browser, ctx


async def validate_session(page) -> bool:
    """Verifica che la sessione LinkedIn sia ancora valida. Ritorna False se scaduta."""
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
               || document.title.toLowerCase().includes('linkedin')
        """)
        return bool(logged_in)
    except Exception:
        return False


# ── ESTRAI INFO PROFILO ───────────────────────────────────────────────────────

async def extract_profile_info(page):
    """Estrae nome, titolo e posizione dalla pagina profilo caricata."""
    name, title, loc = "Utente LinkedIn", "", ""
    try:
        h1 = await page.query_selector("h1")
        if h1:
            name = (await h1.inner_text()).strip()
        te = await page.query_selector(".text-body-medium")
        if te:
            title = (await te.inner_text()).strip()
        le = await page.query_selector(".text-body-small.inline")
        if le:
            loc = (await le.inner_text()).strip()
    except Exception:
        pass
    return name, title, loc


# ── INVIO CONNECTION REQUEST ──────────────────────────────────────────────────

async def send_connection(page, profile_url, note: str = ""):
    """
    (La pagina è già caricata su profile_url)
    Invia connection request senza nota.

    SCOPERTA: su LinkedIn italiano il pulsante Connect è un <a> tag,
    non <button>, con aria-label="Invita [Nome] a collegarsi".
    Usa il nome del profilo (H1) per trovare il pulsante specifico
    ed evitare di cliccare i bottoni della sidebar.

    Ritorna: "sent" / "already_connected" / "not_found" / "error"
    """
    try:
        await page.evaluate("window.scrollTo(0, 0)")
        await asyncio.sleep(1.5)  # attesa H1 caricato

        result = await page.evaluate("""
            () => {
                const h1 = document.querySelector('h1');
                const firstName = h1 ? h1.innerText.trim().split(' ')[0].toLowerCase() : '';

                // SICUREZZA: se H1 non è caricato, non cliccare nulla
                if (!firstName) return 'no_h1';

                const allLinks = Array.from(document.querySelectorAll('a, button'));

                // Cerca bottone Connect con nome specifico (evita sidebar)
                const connectEl = allLinks.find(el => {
                    if (el.offsetWidth === 0 && el.offsetHeight === 0) return false;
                    const aria = (el.getAttribute('aria-label') || '').toLowerCase();
                    return aria.includes('a collegarsi') && aria.includes(firstName);
                });

                if (connectEl) {
                    connectEl.click();
                    return 'clicked';
                }

                // Già connesso
                const connected = allLinks.find(el => {
                    if (el.offsetWidth === 0) return false;
                    const aria = (el.getAttribute('aria-label') || '').toLowerCase();
                    return (aria.includes('invia un messaggio') || aria.includes('send a message'))
                           && aria.includes(firstName);
                });
                if (connected) return 'already_connected';

                // Solo Segui → profilo pubblico/ristretto
                const seguiEl = allLinks.find(el => {
                    if (el.offsetWidth === 0) return false;
                    const aria = (el.getAttribute('aria-label') || '').toLowerCase();
                    return aria.startsWith('segui') && aria.includes(firstName);
                });
                if (seguiEl) return 'restricted';

                // Già in sospeso
                const pendingEl = allLinks.find(el => {
                    if (el.offsetWidth === 0) return false;
                    const txt = (el.innerText || '').toLowerCase();
                    const aria = (el.getAttribute('aria-label') || '').toLowerCase();
                    return txt.includes('in sospeso') || txt.includes('pending') ||
                           aria.includes('in sospeso') || aria.includes('pending');
                });
                if (pendingEl) return 'already_pending';

                return 'not_found';
            }
        """)

        if result == 'already_connected':
            return "already_connected"
        if result == 'already_pending':
            return "already_pending"
        if result in ('not_found', 'restricted', 'no_h1'):
            log.info(f"    send_connection skip: {result} su {profile_url[-40:]}")
            return "not_found"

        # Connessione cliccata — attendi il modale
        await asyncio.sleep(2)

        modal_handled = False

        if note:
            # Flusso "Aggiungi nota": Barnum/Rainbow compresso, max 300 char
            try:
                await page.click(
                    'button:has-text("Aggiungi una nota"), button:has-text("Add a note")',
                    timeout=4000
                )
                await asyncio.sleep(1.5)
                ta = await page.query_selector(
                    'textarea[name="message"], textarea#custom-message, '
                    'textarea.connect-button-send-invite__custom-message, '
                    'textarea[placeholder*="nota"], textarea[placeholder*="note"]'
                )
                if ta:
                    await ta.click()
                    await ta.fill(note[:300])
                    await asyncio.sleep(0.5)
                    await page.click(
                        'button:has-text("Invia"), button:has-text("Send")',
                        timeout=3000
                    )
                    modal_handled = True
            except Exception:
                pass

        if not modal_handled:
            # Fallback: invia senza nota
            try:
                await page.click(
                    'button:has-text("Invia senza nota"), button:has-text("Send without a note")',
                    timeout=4000
                )
                modal_handled = True
            except Exception:
                pass

        if not modal_handled:
            # Fallback: modale "Come ti conosci?"
            try:
                await page.click('button:has-text("Altro"), button:has-text("Other")', timeout=2000)
                await asyncio.sleep(0.5)
                await page.click('button:has-text("Invia"), button:has-text("Send")', timeout=2000)
                modal_handled = True
            except Exception:
                pass

        await asyncio.sleep(1.5)

        # VERIFICA REALE: controlla che il bottone sia diventato "In sospeso"
        confirmed = await page.evaluate("""
            () => {
                const allEls = Array.from(document.querySelectorAll('a, button, span'));
                return allEls.some(el => {
                    const txt = (el.innerText || '').toLowerCase();
                    const aria = (el.getAttribute('aria-label') || '').toLowerCase();
                    return txt.includes('in sospeso') || txt.includes('pending') ||
                           aria.includes('in sospeso') || aria.includes('pending');
                });
            }
        """)

        if confirmed:
            return "sent"
        elif modal_handled:
            # Modal gestito ma bottone non trovato → probabilmente inviato
            return "sent"
        else:
            log.warning(f"    send_connection: click fatto ma nessuna conferma su {profile_url[-40:]}")
            return "not_confirmed"

    except Exception as e:
        log.warning(f"    send_connection errore: {e}")
        return "error"


# ── NAVIGA E CONNETTI ─────────────────────────────────────────────────────────

async def navigate_and_connect(page, profile_url, query=""):
    """
    Naviga al profilo, estrae info, invia connessione.
    Ritorna (lead_dict, result_str).
    """
    await page.goto(profile_url, wait_until="domcontentloaded")
    await hdelay(3, 5)

    final_url = page.url.split("?")[0].rstrip("/") + "/"
    name, title, loc = await extract_profile_info(page)
    note = generate_connection_note({"name": name, "title": title, "location": loc})
    result = await send_connection(page, final_url, note=note)

    lead = {
        "name": name,
        "title": title,
        "location": loc,
        "profile_url": final_url,
        "search_query": query,
        "status": "new",
        "scraped_date": str(date.today()),
        "connect_sent": None,
        "connect_accepted": False,
        "message_sent": None,
        "message_text": None,
        "followup1_sent": None,
        "followup2_sent": None,
    }

    if result == "sent":
        lead["status"] = "connect_sent"
        lead["connect_sent"] = datetime.now().isoformat()
    elif result == "already_connected":
        lead["status"] = "already_connected"
    elif result == "not_found":
        lead["status"] = "not_found"

    return lead, result


# ── SCOPERTA PROFILI VIA RICERCA KEYWORD ────────────────────────────────────
# LinkedIn People Search è la fonte più affidabile: cerchi "avvocato Milano"
# e LinkedIn ti restituisce esattamente avvocati a Milano.
# Non dipende da classi CSS (che cambiano) — raccoglie tutti i link /in/ dalla pagina.

async def _extract_in_links(page) -> list[str]:
    return await page.evaluate("""
        () => Array.from(document.querySelectorAll('a[href*="/in/"]'))
             .map(a => a.href.split('?')[0].replace(/\\/$/, '') + '/')
             .filter(h => /\\/in\\/[a-zA-Z0-9_-]+\\/$/.test(h))
    """)


async def search_profiles_by_keyword(page, query: str, existing_urls: set, max_per_query: int = 15) -> list[str]:
    """
    Cerca profili LinkedIn per keyword, restituisce URL nuovi da visitare.
    Usa la pagina /search/results/people/ — tutti i link /in/ sono i profili.
    """
    url = (
        "https://www.linkedin.com/search/results/people/"
        f"?keywords={query.replace(' ', '%20')}"
        "&origin=GLOBAL_SEARCH_HEADER"
    )
    try:
        await page.goto(url, wait_until="domcontentloaded")
        await asyncio.sleep(3)

        # Scroll per caricare più risultati
        for _ in range(4):
            await page.evaluate("window.scrollBy(0, window.innerHeight * 2)")
            await asyncio.sleep(1.2)

        all_links = await _extract_in_links(page)

        seen: set[str] = set()
        new_urls: list[str] = []
        for u in all_links:
            if u not in existing_urls and u not in seen:
                seen.add(u)
                new_urls.append(u)

        log.info(f"  Ricerca '{query}': {len(new_urls)} profili nuovi")
        return new_urls[:max_per_query]

    except Exception as e:
        log.warning(f"  Errore ricerca '{query}': {e}")
        return []


async def get_people_also_viewed(page, existing_urls) -> list[str]:
    """
    Estrae 'People also viewed' dalla sidebar del profilo già caricato.
    Di solito 8-10 profili della stessa nicchia — qualità alta.
    """
    try:
        urls = await page.evaluate("""
            () => {
                var links = [];
                var sections = Array.from(document.querySelectorAll('.pv-browsemap-section, .browsemap-section, aside section'));
                sections.forEach(function(sec) {
                    sec.querySelectorAll('a[href*="/in/"]').forEach(function(a) { links.push(a.href); });
                });
                if (!links.length) {
                    document.querySelectorAll('aside a[href*="/in/"]').forEach(function(a) { links.push(a.href); });
                }
                return links
                    .map(function(h) { return h.split('?')[0].replace(/\\/$/, '') + '/'; })
                    .filter(function(h) { return /\\/in\\/[a-zA-Z0-9_-]+\\/$/.test(h); });
            }
        """)
        new = [u for u in dict.fromkeys(urls) if u not in existing_urls]
        return new[:10]
    except Exception:
        return []


# ── INVIO MESSAGGIO ───────────────────────────────────────────────────────────

async def send_message(page, profile_url, message):
    await page.goto(profile_url, wait_until="domcontentloaded")
    await hdelay(3, 5)

    msg_btn = await page.query_selector(
        'button[aria-label*="Messaggio"], button[aria-label*="Message"]'
    )
    if not msg_btn:
        return "no_button"

    await msg_btn.click()
    await hdelay(2, 4)

    ta = await page.query_selector('.msg-form__contenteditable')
    if not ta:
        ta = await page.query_selector(
            '[data-placeholder*="messaggio"], [data-placeholder*="message"]'
        )
    if not ta:
        return "no_textarea"

    await ta.click()
    for char in message:
        await ta.type(char, delay=random.uniform(20, 55))

    await hdelay(1, 2)
    send_btn = await page.query_selector(
        'button[aria-label*="Invia"], button[aria-label*="Send"]'
    )
    if send_btn:
        await send_btn.click()
    else:
        await ta.press("Enter")
    await hdelay(2, 3)
    return "sent"


# ── MAIN ─────────────────────────────────────────────────────────────────────

async def main():
    from playwright.async_api import async_playwright

    log.info("=" * 60)
    log.info(f"DAILY RUN  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    log.info("=" * 60)

    async with async_playwright() as pw:
        browser, ctx = await new_browser(pw)
        page = await ctx.new_page()

        log.info("Verifica sessione LinkedIn...")
        if not await validate_session(page):
            log.error("[ERRORE] Sessione LinkedIn scaduta o non valida.")
            log.error("    Esegui: python refresh_session.py")
            await browser.close()
            sys.exit(1)
        log.info("  Sessione valida [OK]")

        leads = load_leads()
        existing_urls = {l["profile_url"] for l in leads}

        sent_today = sum(
            1 for l in leads
            if (l.get("connect_sent") or "").startswith(str(date.today()))
        )
        remaining = DAILY_CONNECT_LIMIT - sent_today
        log.info(f"FASE 1 — Connessioni: {remaining} rimaste oggi (limite: {DAILY_CONNECT_LIMIT})")

        total_sent = 0

        # ── 1A. LEAD GIÀ SALVATI STATUS 'new' CON FILTRO PROFESSIONE ──
        saved_new = [l for l in leads if l.get("status") == "new"]
        saved_target = [l for l in saved_new if is_target_profession(l.get("title", ""))]
        saved_skip = [l for l in saved_new if not is_target_profession(l.get("title", ""))]

        # Salta i lead non-target (salvati senza titolo da PYMK)
        for lead in saved_skip:
            lead["status"] = "skip_no_title"
        if saved_skip:
            log.info(f"  Saltati {len(saved_skip)} lead senza titolo target (verranno visitati per profiling)")
            save_leads(leads)

        if saved_target and remaining > 0:
            log.info(f"  Lead target da connettere: {len(saved_target)}")
            for lead in saved_target:
                if total_sent >= remaining:
                    break
                try:
                    await page.goto(lead["profile_url"], wait_until="domcontentloaded")
                    await hdelay(3, 5)
                    # Riestrai titolo dalla pagina se mancante
                    _, live_title, _ = await extract_profile_info(page)
                    if live_title:
                        lead["title"] = live_title
                    if not is_target_profession(lead.get("title", "")):
                        lead["status"] = "skip_wrong_target"
                        log.info(f"  SKIP non-target: {lead['name'][:35]} — {lead['title'][:40]}")
                        save_leads(leads)
                        continue
                    note = generate_connection_note(lead)
                    result = await send_connection(page, lead["profile_url"], note=note)
                    if result == "sent":
                        lead["status"] = "connect_sent"
                        lead["connect_sent"] = datetime.now().isoformat()
                        total_sent += 1
                        log.info(f"  CONN [{total_sent}/{remaining}]: {lead['name'][:35]} — {lead['title'][:30]}")
                    elif result == "already_connected":
                        lead["status"] = "already_connected"
                    elif result == "already_pending":
                        lead["status"] = "connect_sent"
                        lead["connect_sent"] = lead.get("connect_sent") or datetime.now().isoformat()
                    elif result == "not_confirmed":
                        lead["status"] = "not_confirmed"
                    save_leads(leads)
                    await hdelay(12, 25)
                except Exception as e:
                    log.warning(f"  Errore lead salvato: {e}")

        # ── 1B. NUOVI PROFILI DA KEYWORD SEARCH ──────────────────────
        if total_sent < remaining:
            log.info(f"  Keyword search: cerco profili target ({remaining - total_sent} richiesti)")
            searches = TARGET_SEARCHES.copy()
            random.shuffle(searches)

            for query in searches:
                if total_sent >= remaining:
                    break

                max_this = min(5, remaining - total_sent)
                new_urls = await search_profiles_by_keyword(page, query, existing_urls, max_per_query=max_this)

                # Coda profili: keyword results + People Also Viewed raccolti strada facendo
                profile_queue = list(new_urls)

                for purl in profile_queue:
                    if total_sent >= remaining:
                        break
                    if purl in existing_urls:
                        continue
                    try:
                        await page.goto(purl, wait_until="domcontentloaded")
                        await hdelay(3, 5)
                        name, title, loc = await extract_profile_info(page)
                        final_url = page.url.split("?")[0].rstrip("/") + "/"

                        if total_sent < remaining - 3:
                            pav = await get_people_also_viewed(page, existing_urls)
                            new_pav = [u for u in pav if u not in set(profile_queue) and u not in existing_urls]
                            if new_pav:
                                profile_queue.extend(new_pav)
                                log.info(f"    +{len(new_pav)} PAV da {name[:25]}")

                        lead_base = {
                            "name": name, "title": title, "location": loc,
                            "profile_url": final_url, "search_query": query,
                            "status": "new", "scraped_date": str(date.today()),
                            "connect_sent": None, "connect_accepted": False,
                            "message_sent": None, "message_text": None,
                            "followup1_sent": None, "followup2_sent": None,
                        }

                        # Solo salta se il titolo è PRESENTE ma non è nella nostra nicchia.
                        # Titolo vuoto = profilo ristretto (nuovo account) → trustare la keyword.
                        if title and not is_target_profession(title):
                            lead_base["status"] = "skip_wrong_target"
                            log.info(f"    Skip non-target: {name[:30]} — '{title[:40]}'")
                            leads.append(lead_base)
                            existing_urls.add(final_url)
                            save_leads(leads)
                            await hdelay(3, 6)
                            continue

                        if not title:
                            log.info(f"    Profilo ristretto -> connetto su keyword '{query}': {name[:30] or purl[-30:]}")

                        note = generate_connection_note({"name": name, "title": title, "location": loc})
                        result = await send_connection(page, final_url, note=note)
                        if result == "sent":
                            lead_base["status"] = "connect_sent"
                            lead_base["connect_sent"] = datetime.now().isoformat()
                            total_sent += 1
                            log.info(f"  CONN TARGET [{total_sent}/{remaining}]: {name[:30]} — {title[:35]}")
                        elif result == "already_connected":
                            lead_base["status"] = "already_connected"
                        else:
                            lead_base["status"] = result
                        leads.append(lead_base)
                        existing_urls.add(final_url)
                        save_leads(leads)
                        await hdelay(12, 25)
                    except Exception as e:
                        log.warning(f"  Errore profilo {purl}: {e}")

                await hdelay(10, 20)  # pausa tra keyword diverse

        log.info(f"FASE 1 completata — Connessioni inviate oggi: {total_sent}")

        # ── 2. CHECK ACCETTAZIONI ─────────────────────────────────────
        log.info("FASE 2 — Check connessioni accettate")
        try:
            await page.goto(
                "https://www.linkedin.com/mynetwork/invite-connect/connections/",
                wait_until="domcontentloaded"
            )
            await hdelay(3, 5)
            for _ in range(3):
                await page.evaluate("window.scrollBy(0, window.innerHeight * 2)")
                await hdelay(1, 2)
            link_els = await page.query_selector_all('.mn-connection-card__link')
            connected_urls = {
                (await l.get_attribute("href") or "").split("?")[0]
                for l in link_els
            }
            accepted = 0
            for lead in leads:
                if lead.get("status") == "connect_sent":
                    lu = lead["profile_url"].rstrip("/")
                    if any(lu in cu or cu in lu for cu in connected_urls):
                        lead["status"] = "connected"
                        lead["connect_accepted"] = True
                        lead["connected_date"] = str(date.today())
                        accepted += 1
            save_leads(leads)
            log.info(f"  Nuove accettazioni: {accepted}")
        except Exception as e:
            log.warning(f"  Check accettazioni errore: {e}")

        # ── 3. PRIMO MESSAGGIO AI CONNESSI ────────────────────────────
        log.info("FASE 3 — Primo messaggio ai connessi")
        to_msg = [
            l for l in leads
            if l.get("status") == "connected"
            and not l.get("message_sent")
            and days_since(l.get("connected_date")) >= 1
        ][:DAILY_MESSAGE_LIMIT]

        msg_sent = 0
        for lead in to_msg:
            try:
                msg_dict = generate_message(lead)
                corpo = msg_dict.get("corpo", "")
                link_msg = msg_dict.get("link_msg", "")

                # Invia prima il corpo
                r = await send_message(page, lead["profile_url"], corpo)
                if r == "sent":
                    # Invia subito il link message come secondo messaggio
                    if link_msg:
                        await send_message(page, lead["profile_url"], link_msg)

                    lead["status"] = "message_sent"
                    lead["message_sent"] = datetime.now().isoformat()
                    lead["message_text"] = f"{corpo}\n\n---\n{link_msg}"
                    msg_sent += 1
                    log.info(f"  MSG OK: {lead['name'][:40]}")
                save_leads(leads)
                await hdelay(30, 90)
            except Exception as e:
                log.warning(f"  MSG errore {lead.get('name','?')}: {e}")

        log.info(f"  Messaggi inviati: {msg_sent}")

        # ── 4. FOLLOW-UP ──────────────────────────────────────────────
        log.info("FASE 4 — Follow-up")
        followups = []
        for l in leads:
            if not l.get("followup1_sent") and days_since(l.get("message_sent")) >= 3:
                if l.get("status") == "message_sent":
                    followups.append((l, "f1"))
            elif l.get("followup1_sent") and not l.get("followup2_sent"):
                if days_since(l.get("followup1_sent")) >= 3:
                    followups.append((l, "f2"))

        fu_sent = 0
        for lead, ftype in followups[:DAILY_MESSAGE_LIMIT]:
            try:
                msg_dict = (
                    generate_followup1(lead)
                    if ftype == "f1"
                    else generate_followup2(lead, AGENCY_URL)
                )
                corpo = msg_dict.get("corpo", "")
                link_msg = msg_dict.get("link_msg", "")

                r = await send_message(page, lead["profile_url"], corpo)
                if r == "sent":
                    if link_msg:
                        await send_message(page, lead["profile_url"], link_msg)

                    fu_sent += 1
                    if ftype == "f1":
                        lead["status"] = "followup1_sent"
                        lead["followup1_sent"] = datetime.now().isoformat()
                    else:
                        lead["status"] = "followup2_sent"
                        lead["followup2_sent"] = datetime.now().isoformat()
                    log.info(f"  FU {ftype} OK: {lead['name'][:40]}")
                save_leads(leads)
                await hdelay(30, 90)
            except Exception as e:
                log.warning(f"  FU errore {lead.get('name','?')}: {e}")

        log.info(f"  Follow-up inviati: {fu_sent}")

        await browser.close()

    log.info("=" * 60)
    log.info("DAILY RUN COMPLETATO")
    log.info("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())
