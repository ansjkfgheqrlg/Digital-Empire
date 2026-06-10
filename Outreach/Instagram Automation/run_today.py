"""
Instagram Daily Runner — Digital Empire
========================================
Esegui ogni mattina feriale.

Fasi:
  FASE 0 — Sub-agents: Scout massivo (10 hashtag × 25 profili) +
            Qualifier (pre-screening bio) + Similar Scout (account simili)
  FASE 1 — Scoperta legacy hashtag (backup, 8 hashtag × 20 profili)
  FASE 2 — Invia DM ai lead qualificati/nuovi (max 15/giorno)
  FASE 3 — Follow-up F1 (giorno 2-3 senza risposta)
  FASE 4 — Follow-up F2 (giorno 6-7, break-up con link)

Log: Instagram Automation/run_today_log.txt

v3: FASE 0 sub-agents garantisce pool 200+ candidati → 15 DM certi.
     max_profiles 5→20, hashtags[:4]→[:8], keyword bio estese.
"""
import asyncio
import json
import os
import re
import random
import sys
import logging
from datetime import datetime, date

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

BASE     = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE, "run_today_log.txt")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler(sys.stdout),
    ],
)
log = logging.getLogger()

sys.path.insert(0, BASE)
from config import (
    SESSION_FILE, LEADS_FILE, AGENCY_URL,
    DAILY_DM_LIMIT, DAILY_FOLLOWUP_LIMIT,
    DELAY_MIN_SECONDS, DELAY_MAX_SECONDS,
    TARGET_HASHTAGS, TARGET_KEYWORDS,
)
from personalize import generate_dm, generate_followup1, generate_followup2, get_nicchia
from agents.hashtag_scout import run_scout
from agents.profile_qualifier import run_qualifier, _score_bio
from agents.similar_accounts_scout import run_similar_scout

SESSION_PATH = os.path.join(BASE, SESSION_FILE)
LEADS_PATH   = os.path.join(BASE, LEADS_FILE)

UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/124.0.0.0 Safari/537.36"
)

SKIP_USERNAMES = {
    "instagram", "shop.instagram", "creators", "meta",
    "digitalempireagency", "digitalempireagency.e", "agency_empire", "about",
}


# ── HELPERS ───────────────────────────────────────────────────────────────────

def load_leads() -> list:
    if not os.path.exists(LEADS_PATH):
        return []
    with open(LEADS_PATH, encoding="utf-8-sig") as f:
        return json.load(f)


def save_leads(leads: list):
    with open(LEADS_PATH, "w", encoding="utf-8") as f:
        json.dump(leads, f, ensure_ascii=False, indent=2)


def days_since(date_str: str | None) -> int:
    if not date_str:
        return 999
    try:
        d = datetime.fromisoformat(date_str).date()
        return (date.today() - d).days
    except Exception:
        return 999


def is_target_profession(bio: str) -> bool:
    if not bio:
        return False
    bl = bio.lower()
    return any(kw in bl for kw in TARGET_KEYWORDS)


async def hdelay(a: float | None = None, b: float | None = None):
    mn = a if a is not None else DELAY_MIN_SECONDS
    mx = b if b is not None else DELAY_MAX_SECONDS
    await asyncio.sleep(random.uniform(mn, mx))


async def save_debug_screenshot(page, label: str):
    """Salva screenshot di debug quando qualcosa va storto."""
    try:
        path = os.path.join(BASE, f"debug_{label}_{datetime.now().strftime('%H%M%S')}.png")
        await page.screenshot(path=path)
        log.info(f"  Screenshot debug: {path}")
    except Exception:
        pass


async def dismiss_popups(page):
    """Chiude popup comuni di Instagram."""
    for selector in [
        'button:has-text("Not Now")',
        'button:has-text("Non ora")',
        'button:has-text("Rifiuta tutto")',
        'button:has-text("Consenti tutti i cookie")',
        'button:has-text("Allow All")',
        'button[aria-label="Close"]',
        'button[aria-label="Chiudi"]',
    ]:
        try:
            btn = await page.query_selector(selector)
            if btn and await btn.is_visible():
                await btn.click()
                await asyncio.sleep(0.8)
        except Exception:
            pass


async def check_rate_limited(page) -> bool:
    """
    Rileva se Instagram ha mostrato un messaggio di rate limit o blocco.
    Restituisce True se siamo bloccati.
    """
    try:
        body_text = await page.evaluate("() => document.body.innerText")
        signals = [
            "We restrict certain activity",
            "Limitiamo alcune attività",
            "Try again later",
            "Riprova più tardi",
            "Action Blocked",
            "Azione bloccata",
            "Something went wrong",
            "Si è verificato un errore",
            "Please wait a few minutes",
            "Attendi qualche minuto",
        ]
        for signal in signals:
            if signal.lower() in body_text.lower():
                log.warning(f"  [WARN] RATE LIMIT rilevato: '{signal}' — fermando le azioni")
                await save_debug_screenshot(page, "rate_limit")
                return True
    except Exception:
        pass
    return False


# ── BROWSER ──────────────────────────────────────────────────────────────────

async def new_browser(playwright):
    browser = await playwright.chromium.launch(
        headless=False,
        args=["--start-maximized"],
    )
    ctx = await browser.new_context(
        storage_state=SESSION_PATH,
        viewport={"width": 1280, "height": 800},
        user_agent=UA,
    )
    ctx.set_default_timeout(20000)
    return browser, ctx


async def validate_session(page) -> bool:
    """
    Verifica che la sessione Instagram sia ancora valida.
    Ritorna True se loggato, False se scaduta.
    """
    try:
        await page.goto("https://www.instagram.com/", wait_until="domcontentloaded")
        await asyncio.sleep(3)
        await dismiss_popups(page)

        current_url = page.url
        if "accounts/login" in current_url or "accounts/suspended" in current_url:
            return False

        # Verifica presenza elementi UI loggata
        logged_in = await page.evaluate("""
            () => !!document.querySelector('svg[aria-label="Home"]')
               || !!document.querySelector('svg[aria-label="Casa"]')
               || !!document.querySelector('a[href="/direct/inbox/"]')
               || !!document.querySelector('a[href^="/direct/"]')
        """)
        return bool(logged_in)
    except Exception:
        return False


# ── ESTRAI INFO PROFILO ───────────────────────────────────────────────────────

async def extract_profile_info(page) -> dict:
    """
    Estrae bio e nome da una pagina profilo Instagram già caricata.

    FIX v2:
    - Usa split('\\n') corretto (era split('\\\\n') — bug critico)
    - Rileva profili non trovati (404)
    - Rileva testo italiano per profili privati
    """
    info = {"name": "", "bio": "", "is_private": False, "not_found": False}
    try:
        await asyncio.sleep(2)

        body_text = await page.evaluate("() => document.body.innerText")

        # Profilo non trovato
        not_found_signals = [
            "Sorry, this page isn't available",
            "Spiacenti, questa pagina non è disponibile",
            "Page Not Found",
            "Pagina non trovata",
        ]
        for sig in not_found_signals:
            if sig in body_text:
                info["not_found"] = True
                return info

        # Profilo privato (EN + IT)
        private_signals = [
            "This Account is Private",
            "Questo account è privato",
            "Account is private",
        ]
        for sig in private_signals:
            if sig in body_text:
                info["is_private"] = True
                return info

        # Estrai testo header
        header_text = await page.evaluate("""
            () => {
                const header = document.querySelector('header');
                return header ? header.innerText : document.body.innerText.slice(0, 600);
            }
        """)

        # FIX: split('\n') — carattere newline reale, non '\\n' letterale
        lines = [l.strip() for l in header_text.split('\n') if l.strip()]

        if lines:
            info["name"] = lines[0]

        # Bio: prima riga che sembra descrittiva (non numeri, non "follower", non URL)
        skip_words = [
            "follower", "seguac", "post", "seguendo", "following",
            "modifica profilo", "edit profile", "message", "messaggio",
        ]
        for line in lines[1:]:
            # Salta righe di soli numeri/punteggiatura
            if sum(1 for c in line if c.isdigit()) > len(line) * 0.5:
                continue
            # Salta linee con keyword interfaccia
            if any(w in line.lower() for w in skip_words):
                continue
            # Salta righe troppo corte
            if len(line) < 4:
                continue
            # Salta URL
            if line.startswith("http") or line.startswith("www."):
                continue
            info["bio"] = line
            break

    except Exception as e:
        log.debug(f"  extract_profile_info errore: {e}")
    return info


# ── RICERCA PROFILI DA HASHTAG ────────────────────────────────────────────────

async def scrape_hashtag(page, hashtag: str, existing_usernames: set, max_profiles: int = 6) -> list[str]:
    """
    Estrae username degli autori dalla pagina hashtag.

    Strategia v4 — 4 metodi in cascata:
    1. Network interception: cattura risposte JSON API (GraphQL) prima ancora del DOM
    2. Script/JSON embedded: cerca "username":"VALUE" negli script della pagina
    3. URL fast-path: username nei post link se formato /USERNAME/p/ID
    4. Modal click: clicca thumbnail → overlay con username nell'header
    """
    _GENERIC = {
        'instagram', 'meta', 'about', 'help', 'legal', 'privacy', 'security',
        'explore', 'direct', 'stories', 'reels', 'shop', 'creator', 'business',
        'accounts', 'p', 'reel', 'tv', 'ar', 'web', 'api', 'graphql',
    }

    # ── METODO 1: network interception (prima della navigazione) ──────────────
    api_usernames: list[str] = []

    async def on_response(response):
        try:
            ct = response.headers.get("content-type", "")
            if "json" not in ct:
                return
            text = await response.text()
            matches = re.findall(r'"username"\s*:\s*"([a-zA-Z0-9_.]{2,30})"', text)
            for m in matches:
                if m not in api_usernames:
                    api_usernames.append(m)
        except Exception:
            pass

    page.on("response", on_response)

    url = f"https://www.instagram.com/explore/tags/{hashtag}/"
    try:
        await page.goto(url, wait_until="domcontentloaded")
        await asyncio.sleep(6)
        await dismiss_popups(page)

        if await check_rate_limited(page):
            return []

        page_text = await page.evaluate("() => document.body.innerText")
        if "non è disponibile" in page_text.lower() or "not available" in page_text.lower():
            log.info(f"  #{hashtag}: hashtag non disponibile")
            return []

        # Scroll aggressivo per triggerare API calls lazy
        for _ in range(4):
            await page.evaluate("window.scrollBy(0, window.innerHeight * 2)")
            await asyncio.sleep(2)

        log.info(f"  #{hashtag}: {len(api_usernames)} username da API network")

        # ── METODO 2: script/JSON embedded ────────────────────────────────────
        script_usernames: list[str] = await page.evaluate(r"""
            () => {
                var found = new Set();
                function extract(text) {
                    if (!text || text.length < 10) return;
                    var re = /"username"\s*:\s*"([a-zA-Z0-9_.]{2,30})"/g;
                    var m;
                    while ((m = re.exec(text)) !== null) found.add(m[1]);
                }
                try { extract(JSON.stringify(window.__additionalData)); } catch(e) {}
                try { extract(JSON.stringify(window._sharedData)); } catch(e) {}
                document.querySelectorAll('script').forEach(function(s) {
                    try { extract(s.textContent); } catch(e) {}
                });
                ['__RELAY_STORE__', '__NEXT_DATA__', '__NUXT_DATA__'].forEach(function(id) {
                    var el = document.getElementById(id);
                    if (el) { try { extract(el.textContent); } catch(e) {} }
                });
                return Array.from(found);
            }
        """) or []
        log.info(f"  #{hashtag}: {len(script_usernames)} username da script embedded")

        # ── METODO 3: username dall'URL del post (se /USERNAME/p/ID) ──────────
        post_links: list[str] = await page.evaluate(r"""
            () => Array.from(document.querySelectorAll('a[href*="/p/"]'))
                .map(function(a) { return a.href; })
                .filter(function(v, i, arr) { return arr.indexOf(v) === i; })
                .slice(0, 30)
        """) or []
        url_usernames: list[str] = []
        for purl in post_links:
            m = re.search(r'instagram\.com/([a-zA-Z0-9_.]{2,30})/p/', purl)
            if m:
                url_usernames.append(m.group(1))
        log.info(f"  #{hashtag}: {len(url_usernames)} username da URL, {len(post_links)} post link")

        # ── METODO 4: click thumbnail → modal overlay ─────────────────────────
        modal_usernames: list[str] = []
        all_so_far = api_usernames + script_usernames + url_usernames
        if not all_so_far and post_links:
            log.info(f"  #{hashtag}: 0 da API/script/URL — provo modal click...")
            await page.evaluate("window.scrollTo(0, 0)")
            await asyncio.sleep(1)
            thumbnails = await page.query_selector_all('a[href*="/p/"]')
            clicked_ok = 0
            for thumb in thumbnails[:8]:
                if clicked_ok >= 5:
                    break
                try:
                    await thumb.hover()
                    await asyncio.sleep(0.5)
                    await thumb.click()
                    await asyncio.sleep(3.5)

                    uname = await page.evaluate(r"""
                        () => {
                            // Link profilo nell'header del modal/post
                            var candidates = document.querySelectorAll(
                                'article header a[href], div[role="dialog"] header a[href], ' +
                                'div[role="dialog"] a[href^="/"][href$="/"]'
                            );
                            for (var a of candidates) {
                                var h = (a.getAttribute('href') || '');
                                var m = h.match(/^\/([a-zA-Z0-9_.]{2,30})\/?$/);
                                if (m && m[1] !== 'p' && m[1] !== 'explore') return m[1];
                            }
                            // Alt immagine profilo: "foto profilo di USERNAME"
                            var imgs = document.querySelectorAll(
                                'article img[alt], div[role="dialog"] img[alt]'
                            );
                            for (var img of imgs) {
                                var alt = (img.getAttribute('alt') || '').toLowerCase();
                                var m2 = alt.match(/^([a-zA-Z0-9_.]{2,30})[\s']/);
                                if (m2) return m2[1];
                            }
                            return null;
                        }
                    """)
                    if uname and len(uname) >= 3:
                        modal_usernames.append(uname)
                        clicked_ok += 1
                        log.info(f"  #{hashtag}: modal -> @{uname}")

                    await page.keyboard.press("Escape")
                    await asyncio.sleep(1.5)
                except Exception as e:
                    log.debug(f"  modal click err: {e}")
                    try:
                        await page.keyboard.press("Escape")
                        await asyncio.sleep(1)
                    except Exception:
                        pass
            log.info(f"  #{hashtag}: {len(modal_usernames)} username da modal click")

        # ── Filtra e restituisce ───────────────────────────────────────────────
        all_candidates = api_usernames + script_usernames + url_usernames + modal_usernames

        def is_valid(u: str) -> bool:
            return (
                u and len(u) >= 3
                and u.lower() not in SKIP_USERNAMES
                and u.lower() not in _GENERIC
                and u not in existing_usernames
                and not u.isdigit()
            )

        usernames: list[str] = []
        seen: set[str] = set()
        for uname in all_candidates:
            if len(usernames) >= max_profiles:
                break
            if uname not in seen and is_valid(uname):
                seen.add(uname)
                usernames.append(uname)
                log.info(f"  #{hashtag}: @{uname}")

        log.info(f"  #{hashtag}: {len(usernames)} profili validi (candidati: {len(set(all_candidates))})")
        if not usernames:
            log.info(f"  #{hashtag}: 0 trovati — rate limit o struttura IG aggiornata")
        return usernames

    except Exception as e:
        log.warning(f"  Errore hashtag #{hashtag}: {e}")
        return []
    finally:
        try:
            page.remove_listener("response", on_response)
        except Exception:
            pass


# ── INVIA DM ─────────────────────────────────────────────────────────────────

async def send_dm(page, username: str, message: str, already_on_profile: bool = False) -> str:
    """
    Naviga al profilo @username (se non già lì) e invia un DM.

    FIX v2:
    - Parametro already_on_profile evita doppia navigazione
    - Usa wait_for_selector invece di sleep cieco dopo click
    - Rilevamento profilo non trovato / privato / rate limit
    - Usa page.locator() per trovare il bottone Messaggio (più robusto)

    Ritorna: "sent" / "no_button" / "no_input" / "private" / "not_found" /
             "rate_limited" / "error"
    """
    try:
        if not already_on_profile:
            await page.goto(
                f"https://www.instagram.com/{username}/",
                wait_until="domcontentloaded",
            )
            await asyncio.sleep(random.uniform(3, 4.5))
            await dismiss_popups(page)

        if await check_rate_limited(page):
            return "rate_limited"

        body_text = await page.evaluate("() => document.body.innerText")

        # Profilo non trovato
        if any(s in body_text for s in [
            "Sorry, this page", "Spiacenti, questa pagina",
            "Page Not Found", "Pagina non trovata",
        ]):
            return "not_found"

        # Profilo privato
        if any(s in body_text for s in [
            "This Account is Private",
            "Questo account è privato",
        ]):
            return "private"

        # Cerca il bottone Messaggio con più strategie
        # Strategia 1: get_by_role (più stabile per testo variabile IT/EN)
        msg_btn = None
        for btn_text in ["Messaggio", "Message", "Invia messaggio", "Send message"]:
            try:
                loc = page.get_by_role("button", name=btn_text)
                if await loc.is_visible():
                    msg_btn = loc
                    break
            except Exception:
                pass
            try:
                # Anche link con role=link (Instagram usa <a> o <div>)
                loc = page.get_by_role("link", name=btn_text)
                if await loc.is_visible():
                    msg_btn = loc
                    break
            except Exception:
                pass

        # Strategia 2: cerca div[role="button"] che contenga il testo
        if not msg_btn:
            found = await page.evaluate("""
                () => {
                    const texts = ['Messaggio', 'Message', 'Invia messaggio'];
                    const els = document.querySelectorAll(
                        'div[role="button"], button, a[role="button"]'
                    );
                    for (const el of els) {
                        if (el.offsetWidth === 0 && el.offsetHeight === 0) continue;
                        const t = (el.innerText || el.textContent || '').trim();
                        if (texts.includes(t)) {
                            el.click();
                            return true;
                        }
                    }
                    return false;
                }
            """)
            if found:
                # Già cliccato via JS — salta il click del locator
                await asyncio.sleep(3.5)
                await dismiss_popups(page)
                msg_btn = None  # Gestito sotto
            else:
                log.info(f"  @{username}: bottone Messaggio non trovato")
                await save_debug_screenshot(page, f"no_btn_{username[:15]}")
                return "no_button"
        else:
            await msg_btn.click()
            await asyncio.sleep(3.5)
            await dismiss_popups(page)

        if await check_rate_limited(page):
            return "rate_limited"

        # Aspetta che l'input DM appaia (più robusto di sleep fisso)
        input_selectors = [
            'div[aria-label="Messaggio"]',
            'div[aria-label="Message"]',
            'div[contenteditable="true"]',
            'textarea[placeholder*="mess" i]',
        ]
        msg_input = None
        for sel in input_selectors:
            try:
                await page.wait_for_selector(sel, timeout=6000)
                el = await page.query_selector(sel)
                if el and await el.is_visible():
                    msg_input = el
                    break
            except Exception:
                continue

        if not msg_input:
            log.info(f"  @{username}: campo testo DM non trovato")
            await save_debug_screenshot(page, f"no_input_{username[:15]}")
            return "no_input"

        # Clicca il campo e digita il messaggio carattere per carattere
        await msg_input.click()
        await asyncio.sleep(0.5)

        for char in message:
            if char == '\n':
                # Su Instagram Enter invia — usa Shift+Enter per andare a capo
                await page.keyboard.down("Shift")
                await page.keyboard.press("Enter")
                await page.keyboard.up("Shift")
                await asyncio.sleep(random.uniform(0.08, 0.20))
            else:
                await msg_input.type(char, delay=random.uniform(18, 45))

        await asyncio.sleep(random.uniform(1, 2))

        # Invia: prima prova bottone Send/Invia, poi Enter
        sent = False
        for send_sel in [
            'button[type="submit"]',
            'div[role="button"]:has-text("Invia")',
            'div[role="button"]:has-text("Send")',
            'button:has-text("Invia")',
        ]:
            try:
                sb = await page.query_selector(send_sel)
                if sb and await sb.is_visible():
                    await sb.click()
                    sent = True
                    break
            except Exception:
                continue

        if not sent:
            await page.keyboard.press("Enter")

        await asyncio.sleep(2)
        return "sent"

    except Exception as e:
        log.warning(f"  @{username}: errore send_dm — {e}")
        await save_debug_screenshot(page, f"err_{username[:15]}")
        return "error"


# ── MAIN ─────────────────────────────────────────────────────────────────────

async def main():
    from playwright.async_api import async_playwright

    if not os.path.exists(SESSION_PATH):
        print("\n❌  Sessione Instagram non trovata.")
        print("    Esegui prima:  python refresh_session.py")
        sys.exit(1)

    log.info("=" * 60)
    log.info(f"INSTAGRAM DAILY RUN  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    log.info("=" * 60)

    async with async_playwright() as pw:
        browser, ctx = await new_browser(pw)
        page = await ctx.new_page()

        # ── Verifica sessione valida prima di fare qualsiasi cosa ──────────
        log.info("Verifica sessione Instagram...")
        if not await validate_session(page):
            log.error("[ERRORE] Sessione scaduta o non valida.")
            log.error("    Riesegui: python refresh_session.py")
            await browser.close()
            sys.exit(1)
        log.info("  Sessione valida [OK]")

        leads = load_leads()
        existing_usernames = {l["username"] for l in leads}

        dm_sent_today = sum(
            1 for l in leads
            if (l.get("dm_sent") or "").startswith(str(date.today()))
        )
        fu_sent_today = sum(
            1 for l in leads
            if (l.get("f1_sent") or l.get("f2_sent") or "").startswith(str(date.today()))
        )

        remaining_dm = DAILY_DM_LIMIT - dm_sent_today
        remaining_fu = DAILY_FOLLOWUP_LIMIT - fu_sent_today

        log.info(f"DM oggi: {dm_sent_today}/{DAILY_DM_LIMIT} (rimangono: {remaining_dm})")
        log.info(f"Follow-up oggi: {fu_sent_today}/{DAILY_FOLLOWUP_LIMIT} (rimangono: {remaining_fu})")

        rate_limited = False  # flag globale per blocco Instagram

        # ── FASE 0: SUB-AGENTS — SCOPERTA MASSIVA + PRE-QUALIFICA ──────────
        log.info("FASE 0 — Sub-agents: Scout massivo + Qualifier + Similar Scout")

        # Sub-Agent 1: Scout 10 hashtag × 25 profili = ~250 candidati
        log.info("  [A] Hashtag Scout (10 hashtag × 25 profili)...")
        scout_candidates = await run_scout(
            page,
            TARGET_HASHTAGS,
            existing_usernames,
            max_per_hashtag=25,
            max_hashtags=10,
            delay_between=(3, 6),
        )
        log.info(f"  [A] Scout completato: {len(scout_candidates)} candidati grezzi")

        # Sub-Agent 2: Qualifier — visita profili e pre-screena bio + DM button
        pre_qualified: list[dict] = []
        if scout_candidates:
            log.info(f"  [B] Profile Qualifier (max 60 profili)...")
            pre_qualified = await run_qualifier(
                page,
                scout_candidates,
                max_qualify=60,
                delay_between=(1.5, 3.0),
            )
            log.info(f"  [B] Qualificati: {len(pre_qualified)} pronti per DM")

            # Aggiungi al DB con status "qualified"
            for q in pre_qualified:
                uname = q["username"]
                if uname not in existing_usernames:
                    leads.append({
                        "username":          uname,
                        "bio":               q.get("bio", ""),
                        "name":              q.get("name", ""),
                        "nicchia":           get_nicchia(q.get("bio", "")),
                        "status":            "qualified",
                        "scraped_date":      str(date.today()),
                        "dm_sent":           None,
                        "dm_text":           None,
                        "f1_sent":           None,
                        "f1_text":           None,
                        "f2_sent":           None,
                        "f2_text":           None,
                        "risposta_ricevuta": None,
                    })
                    existing_usernames.add(uname)
            save_leads(leads)

        # Sub-Agent 3: Similar Scout — account simili dai top lead qualificati
        if pre_qualified:
            log.info(f"  [C] Similar Accounts Scout (top 5 profili qualificati)...")
            similar_candidates = await run_similar_scout(
                page,
                pre_qualified,
                existing_usernames,
                max_profiles_to_visit=5,
                max_similar_per_profile=10,
                delay_between=(3, 5),
            )
            log.info(f"  [C] Account simili trovati: {len(similar_candidates)}")
            # Aggiungi come candidati da qualificare nel ciclo DM (status "new")
            for uname in similar_candidates:
                if uname not in existing_usernames:
                    leads.append({
                        "username":          uname,
                        "bio":               "",
                        "name":              "",
                        "nicchia":           "default",
                        "status":            "new",
                        "scraped_date":      str(date.today()),
                        "dm_sent":           None,
                        "dm_text":           None,
                        "f1_sent":           None,
                        "f1_text":           None,
                        "f2_sent":           None,
                        "f2_text":           None,
                        "risposta_ricevuta": None,
                    })
                    existing_usernames.add(uname)
            save_leads(leads)
        else:
            similar_candidates = []

        qualified_today = len(pre_qualified) + len(similar_candidates if pre_qualified else [])
        log.info(f"FASE 0 completata — {qualified_today} lead pronti nel pool")

        # ── FASE 1: SCOPERTA LEGACY (backup se FASE 0 produce poco) ───────
        log.info("FASE 1 — Ricerca legacy da hashtag (backup)")

        hashtags = TARGET_HASHTAGS.copy()
        random.shuffle(hashtags)

        new_found = 0
        for hashtag in hashtags[:8]:
            if rate_limited:
                break
            new_usernames = await scrape_hashtag(
                page, hashtag, existing_usernames, max_profiles=20
            )
            for uname in new_usernames:
                leads.append({
                    "username":         uname,
                    "bio":              "",
                    "name":             "",
                    "nicchia":          "default",
                    "status":           "new",
                    "scraped_date":     str(date.today()),
                    "dm_sent":          None,
                    "dm_text":          None,
                    "f1_sent":          None,
                    "f1_text":          None,
                    "f2_sent":          None,
                    "f2_text":          None,
                    "risposta_ricevuta": None,
                })
                existing_usernames.add(uname)
                new_found += 1
            save_leads(leads)
            await hdelay(5, 10)

        log.info(f"  Nuovi lead trovati: {new_found} | Totale DB: {len(leads)}")

        # ── FASE 2: INVIA DM (qualified prima, poi new) ────────────────────
        log.info(f"FASE 2 — Invio DM (rimangono: {remaining_dm})")

        # Priorità: "qualified" (già pre-screenati, bio confermata) poi "new"
        qualified_leads_dm = [l for l in leads if l.get("status") == "qualified"]
        new_leads_dm       = [l for l in leads if l.get("status") == "new"]
        new_leads          = qualified_leads_dm + new_leads_dm
        log.info(
            f"  Lead da processare: {len(new_leads)} "
            f"({len(qualified_leads_dm)} qualified + {len(new_leads_dm)} new)"
        )

        dm_count = 0
        for lead in new_leads:
            if dm_count >= remaining_dm or rate_limited:
                break

            uname = lead["username"]
            try:
                # Naviga al profilo UNA SOLA VOLTA — poi passa already_on_profile=True a send_dm
                await page.goto(
                    f"https://www.instagram.com/{uname}/",
                    wait_until="domcontentloaded",
                )
                await asyncio.sleep(random.uniform(3, 4.5))
                await dismiss_popups(page)

                if await check_rate_limited(page):
                    rate_limited = True
                    log.warning("  Rate limit in FASE 2 — stop DM")
                    break

                # Estrai info dal profilo già caricato
                info = await extract_profile_info(page)

                if info.get("not_found"):
                    lead["status"] = "not_found"
                    save_leads(leads)
                    await hdelay(2, 4)
                    continue

                if info.get("is_private"):
                    lead["status"] = "private"
                    save_leads(leads)
                    log.info(f"  @{uname}: profilo privato — skip")
                    await hdelay(2, 4)
                    continue

                bio  = info.get("bio", "")
                name = info.get("name", "")
                lead["bio"]  = bio
                lead["name"] = name

                # Determina nicchia
                nicchia = get_nicchia(bio)
                lead["nicchia"] = nicchia

                # Filtra profili non-target — i "qualified" saltano questo check
                # (sono già stati pre-screenati dal Profile Qualifier)
                was_qualified = lead.get("status") == "qualified"
                if not was_qualified and bio and nicchia == "default" and not is_target_profession(bio):
                    lead["status"] = "skip_no_target"
                    save_leads(leads)
                    log.info(f"  @{uname}: non target (bio: {bio[:45]!r})")
                    await hdelay(2, 4)
                    continue

                # Genera DM (ritorna dict {corpo, link_msg})
                dm_dict = generate_dm(lead)
                corpo = dm_dict.get("corpo", "")
                link_msg = dm_dict.get("link_msg", "")

                # Invia prima il corpo del messaggio
                result = await send_dm(page, uname, corpo, already_on_profile=True)

                if result == "sent":
                    # Invia subito il link agency come SECONDO messaggio (niente firma, solo link)
                    if link_msg:
                        await send_dm(page, uname, link_msg, already_on_profile=True)

                    lead["status"]  = "dm_sent"
                    lead["dm_sent"] = datetime.now().isoformat()
                    lead["dm_text"] = f"{corpo}\n\n---\n{link_msg}"
                    dm_count += 1
                    log.info(f"  DM [{dm_count}/{remaining_dm}]: @{uname} ({nicchia})")
                elif result == "rate_limited":
                    rate_limited = True
                    log.warning("  Rate limit durante invio DM — stop")
                    break
                elif result == "private":
                    lead["status"] = "private"
                elif result == "not_found":
                    lead["status"] = "not_found"
                elif result == "no_button":
                    lead["status"] = "no_dm_button"
                    log.info(f"  @{uname}: nessun bottone Messaggio")
                else:
                    lead["status"] = f"errore_{result}"
                    log.warning(f"  @{uname}: {result}")

                save_leads(leads)
                await hdelay()  # pausa umana 15-45s tra DM

            except Exception as e:
                log.warning(f"  Errore @{uname}: {e}")
                await hdelay(8, 15)

        log.info(f"FASE 2 completata — DM inviati oggi: {dm_count}")

        # ── FASE 3: FOLLOW-UP F1 (giorno 2-3) ──────────────────────────────
        if not rate_limited:
            log.info("FASE 3 — Follow-up F1 (giorno 2-3)")

            f1_candidates = [
                l for l in leads
                if l.get("status") == "dm_sent"
                and not l.get("f1_sent")
                and not l.get("risposta_ricevuta")
                and days_since(l.get("dm_sent")) >= 2
            ]
            log.info(f"  Candidati F1: {len(f1_candidates)}")

            f1_count = 0
            for lead in f1_candidates[:remaining_fu]:
                if rate_limited:
                    break
                uname = lead["username"]
                try:
                    f1_dict = generate_followup1(lead)
                    corpo   = f1_dict.get("corpo", "")
                    link_msg = f1_dict.get("link_msg", "")
                    result  = await send_dm(page, uname, corpo)
                    if result == "sent":
                        if link_msg:
                            await send_dm(page, uname, link_msg)
                        lead["status"]  = "f1_sent"
                        lead["f1_sent"] = datetime.now().isoformat()
                        lead["f1_text"] = f"{corpo}\n\n---\n{link_msg}"
                        f1_count += 1
                        log.info(f"  F1 OK: @{uname}")
                    elif result == "rate_limited":
                        rate_limited = True
                    save_leads(leads)
                    await hdelay(30, 60)
                except Exception as e:
                    log.warning(f"  F1 errore @{uname}: {e}")

            log.info(f"  F1 inviati: {f1_count}")
        else:
            f1_count = 0
            log.info("FASE 3 saltata — rate limit attivo")

        # ── FASE 4: FOLLOW-UP F2 (giorno 6-7, break-up) ────────────────────
        if not rate_limited:
            log.info("FASE 4 — Follow-up F2 (giorno 6-7, break-up)")

            f2_candidates = [
                l for l in leads
                if l.get("status") == "f1_sent"
                and not l.get("f2_sent")
                and not l.get("risposta_ricevuta")
                and days_since(l.get("f1_sent")) >= 4
            ]
            log.info(f"  Candidati F2: {len(f2_candidates)}")

            f2_count = 0
            slots_left = remaining_fu - f1_count
            for lead in f2_candidates[:slots_left]:
                if rate_limited:
                    break
                uname = lead["username"]
                try:
                    f2_dict = generate_followup2(lead, AGENCY_URL)
                    corpo   = f2_dict.get("corpo", "")
                    link_msg = f2_dict.get("link_msg", "")
                    result  = await send_dm(page, uname, corpo)
                    if result == "sent":
                        if link_msg:
                            await send_dm(page, uname, link_msg)
                        lead["status"]  = "f2_sent"
                        lead["f2_sent"] = datetime.now().isoformat()
                        lead["f2_text"] = f"{corpo}\n\n---\n{link_msg}"
                        f2_count += 1
                        log.info(f"  F2 OK: @{uname}")
                    elif result == "rate_limited":
                        rate_limited = True
                    save_leads(leads)
                    await hdelay(30, 60)
                except Exception as e:
                    log.warning(f"  F2 errore @{uname}: {e}")

            log.info(f"  F2 inviati: {f2_count}")
        else:
            f2_count = 0
            log.info("FASE 4 saltata — rate limit attivo")

        await browser.close()

    log.info("=" * 60)
    log.info("INSTAGRAM DAILY COMPLETATO")
    log.info(f"  DM primo contatto: {dm_count}")
    log.info(f"  Follow-up F1:      {f1_count}")
    log.info(f"  Follow-up F2:      {f2_count}")
    log.info(f"  Lead totali in DB: {len(leads)}")
    if rate_limited:
        log.warning("  ⚠ Rate limit Instagram rilevato — domani riprova con calma")
    log.info("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())
