"""
Instagram DM Repair — Digital Empire
======================================
Trova i DM sbagliati di oggi, li rimuove (unsend) e ne manda di nuovi corretti.

Uso:
    python repair_instagram.py

Il script identifica automaticamente i lead con dm_sent oggi il cui messaggio
è problematico (non inizia con "Ciao", contiene meta-commentary, ecc.).
Log: Instagram Automation/repair_log.txt
"""

import asyncio
import json
import os
import sys
import random
import logging
from datetime import date, datetime

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

BASE     = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE, "repair_log.txt")
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
from config import SESSION_FILE, LEADS_FILE, DELAY_MIN_SECONDS, DELAY_MAX_SECONDS
from personalize import generate_dm

SESSION_PATH = os.path.join(BASE, SESSION_FILE)
LEADS_PATH   = os.path.join(BASE, LEADS_FILE)

UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/124.0.0.0 Safari/537.36"
)


# ── HELPERS ───────────────────────────────────────────────────────────────────

def load_leads() -> list:
    with open(LEADS_PATH, encoding="utf-8-sig") as f:
        return json.load(f)


def save_leads(leads: list):
    with open(LEADS_PATH, "w", encoding="utf-8") as f:
        json.dump(leads, f, ensure_ascii=False, indent=2)


def is_broken_message(dm_text: str | None) -> bool:
    """Identifica messaggi chiaramente rotti."""
    if not dm_text:
        return False
    t = dm_text.strip()
    lower = t.lower()
    # Non inizia con Ciao
    if not lower.startswith("ciao"):
        return True
    # Contiene meta-commentary AI
    meta_signals = [
        "ecco un'opzione", "ecco una possibile", "possibile revisione",
        "questa versione mantiene", "questa versione", "i 4 pilastri",
        "meno di 50 parole", "non contiene link", "non contiene esclamativi",
        "aiutare a catturare", "più conciso", "revisione del messaggio",
    ]
    if any(s in lower for s in meta_signals):
        return True
    # Contiene virgolette iniziali (AI ha wrappato in quotes)
    if t[0] in ('"', '"', '"', "'", "'"):
        return True
    return False


async def hdelay(a: float = None, b: float = None):
    mn = a if a is not None else DELAY_MIN_SECONDS
    mx = b if b is not None else DELAY_MAX_SECONDS
    await asyncio.sleep(random.uniform(mn, mx))


async def save_screenshot(page, label: str):
    try:
        path = os.path.join(BASE, f"repair_{label}_{datetime.now().strftime('%H%M%S')}.png")
        await page.screenshot(path=path)
        log.info(f"  Screenshot: {path}")
    except Exception:
        pass


async def dismiss_popups(page):
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
    try:
        body_text = await page.evaluate("() => document.body.innerText")
        signals = [
            "We restrict certain activity", "Limitiamo alcune attività",
            "Try again later", "Riprova più tardi",
            "Action Blocked", "Azione bloccata",
            "Please wait a few minutes", "Attendi qualche minuto",
        ]
        for signal in signals:
            if signal.lower() in body_text.lower():
                log.warning(f"  [WARN] RATE LIMIT: '{signal}'")
                await save_screenshot(page, "rate_limit")
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
    try:
        await page.goto("https://www.instagram.com/", wait_until="domcontentloaded")
        await asyncio.sleep(3)
        await dismiss_popups(page)
        current_url = page.url
        if "accounts/login" in current_url or "accounts/suspended" in current_url:
            return False
        logged_in = await page.evaluate("""
            () => !!document.querySelector('svg[aria-label="Home"]')
               || !!document.querySelector('svg[aria-label="Casa"]')
               || !!document.querySelector('a[href="/direct/inbox/"]')
               || !!document.querySelector('a[href^="/direct/"]')
        """)
        return bool(logged_in)
    except Exception:
        return False


# ── APRI CONVERSAZIONE DM ─────────────────────────────────────────────────────

async def open_dm_conversation(page, username: str) -> bool:
    """
    Naviga al profilo @username e clicca Messaggio per aprire il thread DM.
    Ritorna True se il thread è aperto correttamente.
    """
    await page.goto(
        f"https://www.instagram.com/{username}/",
        wait_until="domcontentloaded",
    )
    await asyncio.sleep(random.uniform(2.5, 3.5))
    await dismiss_popups(page)

    if await check_rate_limited(page):
        return False

    # Strategia 1: get_by_role per vari testi
    for btn_text in ["Messaggio", "Message", "Invia messaggio", "Send message"]:
        try:
            loc = page.get_by_role("button", name=btn_text)
            if await loc.is_visible():
                await loc.click()
                await asyncio.sleep(4)
                await dismiss_popups(page)
                return True
        except Exception:
            pass
        try:
            loc = page.get_by_role("link", name=btn_text)
            if await loc.is_visible():
                await loc.click()
                await asyncio.sleep(4)
                await dismiss_popups(page)
                return True
        except Exception:
            pass

    # Strategia 2: JavaScript click
    found = await page.evaluate("""
        () => {
            const texts = ['Messaggio', 'Message', 'Invia messaggio', 'Send message'];
            const els = document.querySelectorAll(
                'div[role="button"], button, a[role="button"]'
            );
            for (const el of els) {
                if (el.offsetWidth === 0 && el.offsetHeight === 0) continue;
                const t = (el.innerText || el.textContent || '').trim();
                if (texts.includes(t)) { el.click(); return true; }
            }
            return false;
        }
    """)
    if found:
        await asyncio.sleep(4)
        await dismiss_popups(page)
        return True

    log.warning(f"  @{username}: bottone Messaggio non trovato")
    await save_screenshot(page, f"no_btn_{username[:12]}")
    return False


# ── SCROLL BOTTOM DM ──────────────────────────────────────────────────────────

async def scroll_to_bottom_dm(page):
    """Scrolla fino all'ultimo messaggio nella conversazione."""
    await page.evaluate("""
        () => {
            // Trova il contenitore scrollabile principale (messages area)
            const candidates = Array.from(document.querySelectorAll('*'));
            const scrollable = candidates.find(el => {
                const s = getComputedStyle(el);
                return el.scrollHeight > el.clientHeight + 50
                    && ['auto', 'scroll', 'overlay'].includes(s.overflowY)
                    && el.clientHeight > 200;
            });
            if (scrollable) {
                scrollable.scrollTop = scrollable.scrollHeight + 99999;
            } else {
                window.scrollTo(0, document.body.scrollHeight + 99999);
            }
        }
    """)
    await asyncio.sleep(2)


# ── TROVA MESSAGGIO NEL DOM ───────────────────────────────────────────────────

async def find_message_position(page, dm_text: str) -> dict | None:
    """
    Cerca il nostro messaggio nel DOM tramite il testo.
    Ritorna {x, y} del centro dell'elemento, o None.
    """
    # Hint: prendi la parte significativa del testo (dopo eventuali virgolette)
    text = dm_text.strip()
    if text and text[0] in ('"', '"', '"', "'", "'"):
        text = text[1:].strip()

    # Usa 25 caratteri come hint (abbastanza unici, non troppo lunghi)
    hint = text[:25].strip()
    if not hint:
        return None

    pos = await page.evaluate(
        """(hint) => {
            function searchNode(node) {
                if (node.nodeType === 3) {
                    if (node.textContent.includes(hint)) {
                        const parent = node.parentElement;
                        if (!parent) return null;
                        const rect = parent.getBoundingClientRect();
                        if (rect.width > 30 && rect.height > 8
                            && rect.top > 50 && rect.top < window.innerHeight) {
                            return {
                                x: rect.left + rect.width / 2,
                                y: rect.top + rect.height / 2
                            };
                        }
                    }
                    return null;
                }
                for (const child of node.childNodes) {
                    const r = searchNode(child);
                    if (r) return r;
                }
                return null;
            }
            return searchNode(document.body);
        }""",
        hint,
    )
    return pos


async def find_any_right_message(page) -> dict | None:
    """
    Fallback: trova un qualsiasi messaggio nostro (allineato a destra).
    Prende l'ULTIMO visibile (il più recente).
    """
    pos = await page.evaluate("""
        () => {
            const vw = window.innerWidth;
            let last = null;
            const all = Array.from(document.querySelectorAll('div, span'));
            for (const el of all) {
                const rect = el.getBoundingClientRect();
                // Messaggio nostro: posizionato a destra, larghezza media, ha testo
                if (rect.left > vw * 0.42
                    && rect.width > 40 && rect.width < vw * 0.58
                    && rect.height > 12 && rect.height < 200
                    && el.childElementCount <= 3
                    && el.innerText && el.innerText.trim().length > 10
                    && rect.top > 0 && rect.top < window.innerHeight) {
                    last = {x: rect.left + rect.width / 2, y: rect.top + rect.height / 2};
                }
            }
            return last;
        }
    """)
    return pos


# ── UNSEND MESSAGGIO ──────────────────────────────────────────────────────────

async def unsend_at_position(page, x: float, y: float) -> bool:
    """
    Hover sul messaggio → opzioni → Rimuovi per tutti.
    Ritorna True se operazione completata.
    """
    # Hover sopra il messaggio
    await page.mouse.move(x, y)
    await asyncio.sleep(1.8)

    # Cerca bottone opzioni (appare dopo hover)
    options_btn = None
    option_selectors = [
        'button[aria-label="Opzioni messaggio"]',
        'button[aria-label="Message options"]',
        'button[aria-label="More options"]',
        'button[aria-label="Opzioni"]',
        'div[aria-label="Opzioni messaggio"]',
        'div[aria-label="Message options"]',
    ]
    for sel in option_selectors:
        try:
            el = await page.query_selector(sel)
            if el and await el.is_visible():
                options_btn = el
                break
        except Exception:
            pass

    # Se non trovato, prova spostando leggermente il cursore
    if not options_btn:
        for offset_x in [40, -40, 60, -60]:
            await page.mouse.move(x + offset_x, y)
            await asyncio.sleep(1)
            for sel in option_selectors:
                try:
                    el = await page.query_selector(sel)
                    if el and await el.is_visible():
                        options_btn = el
                        break
                except Exception:
                    pass
            if options_btn:
                break

    if not options_btn:
        log.warning("  Bottone opzioni messaggio non trovato dopo hover")
        return False

    await options_btn.click()
    await asyncio.sleep(1.2)

    # Cerca "Rimuovi" nel menu aperto
    remove_found = False
    for remove_text in ["Rimuovi", "Remove", "Unsend", "Annulla invio"]:
        try:
            btn = page.get_by_role("button", name=remove_text)
            if await btn.is_visible():
                await btn.click()
                await asyncio.sleep(1.5)
                remove_found = True
                break
        except Exception:
            pass

    if not remove_found:
        # Fallback JS
        remove_found = await page.evaluate("""
            () => {
                const texts = ['Rimuovi', 'Remove', 'Unsend', 'Annulla invio'];
                const els = document.querySelectorAll(
                    'div[role="button"], button, a[role="button"]'
                );
                for (const el of els) {
                    const t = (el.innerText || '').trim();
                    if (texts.includes(t)) { el.click(); return true; }
                }
                return false;
            }
        """)
        if remove_found:
            await asyncio.sleep(1.5)

    if not remove_found:
        log.warning("  Opzione Rimuovi non trovata nel menu")
        await page.keyboard.press("Escape")
        return False

    # Potrebbe apparire un dialog di conferma "Rimuovi per tutti"
    for confirm_text in ["Rimuovi per tutti", "Remove for everyone", "Rimuovi", "Remove", "Sì", "OK"]:
        try:
            conf = page.get_by_role("button", name=confirm_text)
            if await conf.is_visible():
                await conf.click()
                await asyncio.sleep(2)
                log.info("  Messaggio rimosso (con dialog di conferma)")
                return True
        except Exception:
            pass

    # Nessun dialog → l'operazione era già completata al click
    await asyncio.sleep(2)
    log.info("  Messaggio rimosso")
    return True


# ── INVIA NUOVO MESSAGGIO ─────────────────────────────────────────────────────

async def send_in_conversation(page, username: str, message: str) -> bool:
    """
    Invia un DM nella conversazione già aperta.
    Non naviga — presuppone che siamo nel thread DM.
    """
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
        log.warning(f"  @{username}: campo input DM non trovato")
        await save_screenshot(page, f"noinput_{username[:10]}")
        return False

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

    # Invia: bottone submit o Enter
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
    return True


# ── REPAIR SINGOLO LEAD ───────────────────────────────────────────────────────

async def repair_lead(page, lead: dict) -> str:
    """
    Per un singolo lead:
      1. Apre il thread DM
      2. Trova il messaggio sbagliato
      3. Lo rimuove (unsend)
      4. Genera nuovo messaggio corretto
      5. Lo invia
    Ritorna: "ok" / "unsend_failed" / "send_failed" / "error"
    """
    username  = lead["username"]
    wrong_txt = lead.get("dm_text", "")

    log.info(f"  Apro DM con @{username}...")
    opened = await open_dm_conversation(page, username)
    if not opened:
        log.warning(f"  @{username}: impossibile aprire la conversazione")
        return "error"

    await scroll_to_bottom_dm(page)
    await asyncio.sleep(1.5)

    # Trova il messaggio sbagliato tramite testo
    pos = await find_message_position(page, wrong_txt)

    if pos:
        log.info(f"  Messaggio sbagliato trovato @ ({pos['x']:.0f}, {pos['y']:.0f})")
    else:
        log.warning(f"  @{username}: testo non trovato nel DOM — provo con msg generico a destra")
        pos = await find_any_right_message(page)
        if pos:
            log.info(f"  Trovato msg generico destra @ ({pos['x']:.0f}, {pos['y']:.0f})")
        else:
            await save_screenshot(page, f"nomsg_{username[:12]}")
            log.warning(f"  @{username}: nessun messaggio trovato nel DOM")

    # Prova unsend
    unsent = False
    if pos:
        unsent = await unsend_at_position(page, pos["x"], pos["y"])

    if not unsent:
        log.warning(f"  @{username}: unsend fallito — invio comunque il nuovo messaggio")
    else:
        log.info(f"  @{username}: messaggio sbagliato rimosso [OK]")
        await asyncio.sleep(random.uniform(2, 4))

    # Genera nuovo messaggio corretto con personalize.py aggiornato
    new_msg = generate_dm(lead)
    log.info(f"  Nuovo msg ({len(new_msg.split())} parole): {new_msg[:70]!r}...")

    # Verifica che il nuovo messaggio sia corretto prima di inviarlo
    if not new_msg.strip().lower().startswith("ciao"):
        log.error(f"  @{username}: generate_dm ha prodotto messaggio senza Ciao — SKIP invio")
        return "send_failed"

    # Invia il nuovo messaggio nella conversazione già aperta
    ok = await send_in_conversation(page, username, new_msg)
    if ok:
        lead["dm_text"] = new_msg
        lead["dm_sent"] = datetime.now().isoformat()
        lead["_repaired"] = True
        log.info(f"  @{username}: nuovo DM inviato [OK]")
        return "ok"
    else:
        log.warning(f"  @{username}: invio nuovo DM fallito")
        return "send_failed"


# ── MAIN ─────────────────────────────────────────────────────────────────────

async def main():
    from playwright.async_api import async_playwright

    if not os.path.exists(SESSION_PATH):
        print("\n❌  Sessione Instagram non trovata.")
        print("    Esegui prima:  python refresh_session.py")
        sys.exit(1)

    log.info("=" * 60)
    log.info(f"INSTAGRAM REPAIR RUN  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    log.info("=" * 60)

    leads = load_leads()
    today = str(date.today())

    # Identifica lead da riparare: DM inviati oggi + messaggio rotto
    to_repair = [
        l for l in leads
        if l.get("status") == "dm_sent"
        and (l.get("dm_sent") or "").startswith(today)
        and is_broken_message(l.get("dm_text"))
        and not l.get("_repaired")  # evita doppia riparazione
    ]

    log.info(f"Lead con DM sbagliati da riparare: {len(to_repair)}")
    for l in to_repair:
        preview = (l.get("dm_text") or "")[:60].replace("\n", " ")
        log.info(f"  @{l['username']}: {preview!r}...")

    if not to_repair:
        log.info("Nessun lead da riparare. Fine.")
        return

    async with async_playwright() as pw:
        browser, ctx = await new_browser(pw)
        page = await ctx.new_page()

        log.info("Verifica sessione Instagram...")
        if not await validate_session(page):
            log.error("[ERRORE] Sessione scaduta. Riesegui: python refresh_session.py")
            await browser.close()
            sys.exit(1)
        log.info("  Sessione valida [OK]")

        repaired   = 0
        unsend_ko  = 0
        send_ko    = 0
        errors     = 0

        for i, lead in enumerate(to_repair):
            username = lead["username"]
            log.info(f"\n[{i+1}/{len(to_repair)}] Riparazione @{username}")

            if await check_rate_limited(page):
                log.error("Rate limit Instagram — fermato. Riprova domani.")
                break

            try:
                result = await repair_lead(page, lead)
                if result == "ok":
                    repaired += 1
                elif result == "unsend_failed":
                    unsend_ko += 1
                elif result == "send_failed":
                    send_ko += 1
                else:
                    errors += 1

                save_leads(leads)

                # Pausa umana tra riparazioni (25-45s)
                if i < len(to_repair) - 1:
                    await hdelay(25, 45)

            except Exception as e:
                log.error(f"  Errore grave @{username}: {e}")
                errors += 1
                await save_screenshot(page, f"grave_{username[:10]}")
                await hdelay(10, 20)

        await browser.close()

    log.info("\n" + "=" * 60)
    log.info("REPAIR COMPLETATO")
    log.info(f"  Riparati correttamente:  {repaired}")
    log.info(f"  Unsend fallito (inviato nuovo):  {unsend_ko}")
    log.info(f"  Invio nuovo fallito:     {send_ko}")
    log.info(f"  Errori gravi:            {errors}")
    log.info("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())
