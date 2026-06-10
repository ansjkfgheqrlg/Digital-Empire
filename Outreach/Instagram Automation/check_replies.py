"""
Instagram DM Reply Checker — Digital Empire
=============================================
Controlla se i lead hanno risposto ai nostri DM.

APPROCCIO v2 — Lead-based (molto più affidabile di inbox scanning):
Invece di cercare badge "non letto" nell'inbox (selettori instabili),
naviga direttamente ai profili dei lead con DM inviati e apre il thread
per leggere se ci sono messaggi nuovi.

Logica:
  Per ogni lead con status dm_sent/f1_sent/f2_sent e nessuna risposta:
    1. Naviga al profilo
    2. Clicca "Messaggio" per aprire il thread
    3. Legge gli ultimi messaggi
    4. Se il messaggio più recente NON è il nostro → hanno risposto
    5. Classifica + genera risposta suggerita
    6. Stampa a schermo / opzionalmente invia

MODALITÀ DEFAULT: read-only — stampa suggerimenti.
MODALITÀ AUTO-INVIA: python check_replies.py --autoinvia

Log: Instagram Automation/instagram_replies_log.txt
"""
import asyncio
import json
import os
import random
import sys
import logging
from datetime import datetime, date

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

BASE     = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE, "instagram_replies_log.txt")
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
from config import SESSION_FILE, LEADS_FILE
from personalize import classify_and_reply

SESSION_PATH = os.path.join(BASE, SESSION_FILE)
LEADS_PATH   = os.path.join(BASE, LEADS_FILE)

UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/124.0.0.0 Safari/537.36"
)

STATI_CON_MESSAGGI = {"dm_sent", "f1_sent", "f2_sent"}
MAX_LEADS_DA_CONTROLLARE = 20  # controlla al massimo N profili per sessione


# ── HELPERS ───────────────────────────────────────────────────────────────────

async def dismiss_popups(page):
    for selector in [
        'button:has-text("Not Now")',
        'button:has-text("Non ora")',
        'button[aria-label="Close"]',
        'button[aria-label="Chiudi"]',
        'button:has-text("Consenti tutti i cookie")',
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
        body = await page.evaluate("() => document.body.innerText")
        signals = [
            "We restrict certain activity", "Limitiamo alcune attività",
            "Try again later", "Riprova più tardi",
            "Action Blocked", "Azione bloccata",
        ]
        return any(s.lower() in body.lower() for s in signals)
    except Exception:
        return False


# ── APRI THREAD DM ────────────────────────────────────────────────────────────

async def open_dm_thread(page, username: str) -> bool:
    """
    Naviga al profilo e clicca "Messaggio" per aprire il thread DM.
    Ritorna True se il thread è aperto con successo.
    """
    try:
        await page.goto(
            f"https://www.instagram.com/{username}/",
            wait_until="domcontentloaded",
        )
        await asyncio.sleep(random.uniform(3, 4))
        await dismiss_popups(page)

        if await check_rate_limited(page):
            return False

        # Cerca e clicca il bottone Messaggio
        clicked = False

        # Strategia 1: get_by_role (più stabile)
        for btn_text in ["Messaggio", "Message"]:
            try:
                loc = page.get_by_role("button", name=btn_text)
                if await loc.is_visible():
                    await loc.click()
                    clicked = True
                    break
            except Exception:
                pass

        # Strategia 2: JavaScript click
        if not clicked:
            clicked = await page.evaluate("""
                () => {
                    const texts = ['Messaggio', 'Message'];
                    const els = document.querySelectorAll(
                        'div[role="button"], button, a[role="button"]'
                    );
                    for (const el of els) {
                        if (el.offsetWidth === 0) continue;
                        const t = (el.innerText || '').trim();
                        if (texts.includes(t)) { el.click(); return true; }
                    }
                    return false;
                }
            """)

        if not clicked:
            return False

        await asyncio.sleep(3)
        await dismiss_popups(page)
        return True

    except Exception as e:
        log.debug(f"  open_dm_thread @{username}: {e}")
        return False


# ── LEGGI MESSAGGI DEL THREAD ─────────────────────────────────────────────────

async def leggi_thread(page) -> list[str]:
    """
    Legge i messaggi nella conversazione DM attualmente aperta.

    Approccio: estrae tutti i blocchi di testo visibili nell'area messaggi.
    Non distingue inbound/outbound (troppo fragile) — restituisce tutti
    i testi in ordine, dal più vecchio al più recente.
    """
    try:
        await asyncio.sleep(1.5)

        # Scroll in fondo alla conversazione
        await page.evaluate("""
            () => {
                const containers = document.querySelectorAll(
                    'div[role="main"], div[style*="overflow"]'
                );
                for (const c of containers) {
                    c.scrollTop = c.scrollHeight;
                }
                window.scrollTo(0, document.body.scrollHeight);
            }
        """)
        await asyncio.sleep(1)

        # Estrai testo da tutti i blocchi messaggio
        # Instagram usa div[role="row"] o simili, ma le classi cambiano.
        # Usiamo un approccio testuale: tutti i testi di lunghezza significativa
        messages = await page.evaluate("""
            () => {
                // Cerca il contenitore principale dei messaggi
                const main = document.querySelector('div[role="main"]')
                           || document.querySelector('section main')
                           || document.body;

                const seen = new Set();
                const result = [];

                // Raccoglie tutti i nodi di testo che sembrano messaggi
                const walker = document.createTreeWalker(
                    main,
                    NodeFilter.SHOW_TEXT,
                    null
                );

                let node;
                while ((node = walker.nextNode())) {
                    const text = (node.nodeValue || '').trim();
                    // Filtra: lunghezza utile, non già visto, non UI elements
                    if (text.length > 2
                        && text.length < 1500
                        && !seen.has(text)
                        && !/^\\d+$/.test(text)  // non solo numeri
                        ) {
                        seen.add(text);
                        result.push(text);
                    }
                }
                return result.slice(-30);  // ultimi 30 blocchi
            }
        """)

        return messages or []

    except Exception as e:
        log.debug(f"  leggi_thread errore: {e}")
        return []


# ── CONTROLLA SE IL LEAD HA RISPOSTO ─────────────────────────────────────────

def ha_risposto(messages: list[str], nostro_ultimo_testo: str | None) -> tuple[bool, str]:
    """
    Determina se il lead ha risposto al nostro ultimo messaggio.

    Logica: se il nostro ultimo testo è nell'elenco messaggi, cerca
    qualcosa DOPO di esso che non sia nostro. Altrimenti assume che
    ci sia una risposta se ci sono messaggi che non corrispondono
    ai nostri testi salvati.

    Ritorna (ha_risposto: bool, testo_risposta: str).
    """
    if not messages:
        return False, ""

    # Se non abbiamo il testo del nostro messaggio, usa euristica semplice:
    # se ci sono 2+ messaggi nel thread è probabile ci sia una risposta
    if not nostro_ultimo_testo:
        # Troppo incerto — ritorna False per sicurezza
        return False, ""

    # Cerca il nostro testo (anche come sottostringa, i messaggi lunghi possono essere troncati)
    nostro_idx = -1
    nostro_snip = nostro_ultimo_testo[:60].lower()
    for i, msg in enumerate(messages):
        if nostro_snip in msg.lower() or msg.lower() in nostro_ultimo_testo.lower():
            nostro_idx = i
            # Non break — prendi l'ultimo occorrenza
    if nostro_idx == -1:
        # Non trovato — incerto, ritorna False
        return False, ""

    # Cerca messaggi dopo il nostro che sembrano una risposta reale
    after_ours = messages[nostro_idx + 1:]
    for msg in after_ours:
        # Salta testi che sono chiaramente dell'interfaccia
        ui_skip = [
            "messaggio", "message", "visto", "seen", "invia", "send",
            "inviato", "sent", "reagisci", "react",
        ]
        if any(w == msg.lower() for w in ui_skip):
            continue
        if len(msg) > 5:
            return True, msg

    return False, ""


# ── INVIA RISPOSTA ────────────────────────────────────────────────────────────

async def invia_risposta_nel_thread(page, testo: str) -> bool:
    """Invia una risposta nel thread DM già aperto."""
    try:
        # Trova il campo di input (siamo già nel thread)
        msg_input = None
        for sel in [
            'div[aria-label="Messaggio"]',
            'div[aria-label="Message"]',
            'div[contenteditable="true"]',
        ]:
            try:
                await page.wait_for_selector(sel, timeout=5000)
                el = await page.query_selector(sel)
                if el and await el.is_visible():
                    msg_input = el
                    break
            except Exception:
                continue

        if not msg_input:
            return False

        await msg_input.click()
        await asyncio.sleep(0.5)
        for char in testo:
            await msg_input.type(char, delay=random.uniform(18, 45))
        await asyncio.sleep(random.uniform(1, 2))

        # Invia
        for sel in ['button[type="submit"]', 'div[role="button"]:has-text("Invia")']:
            try:
                sb = await page.query_selector(sel)
                if sb and await sb.is_visible():
                    await sb.click()
                    await asyncio.sleep(2)
                    return True
            except Exception:
                pass
        await page.keyboard.press("Enter")
        await asyncio.sleep(2)
        return True

    except Exception as e:
        log.warning(f"  invia_risposta_nel_thread errore: {e}")
        return False


# ── MAIN ──────────────────────────────────────────────────────────────────────

async def main():
    autoinvia = "--autoinvia" in sys.argv

    log.info("=" * 60)
    log.info(f"INSTAGRAM REPLY CHECK  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    log.info(f"Modalità: {'AUTO-INVIA' if autoinvia else 'SUGGERIMENTI (read-only)'}")
    log.info("=" * 60)

    if not os.path.exists(SESSION_PATH):
        log.error("Sessione Instagram non trovata. Esegui: python refresh_session.py")
        return

    leads = []
    if os.path.exists(LEADS_PATH):
        with open(LEADS_PATH, encoding="utf-8-sig") as f:
            leads = json.load(f)

    # Seleziona i lead da controllare
    leads_da_controllare = [
        l for l in leads
        if l.get("status") in STATI_CON_MESSAGGI
        and not l.get("risposta_ricevuta")
    ][:MAX_LEADS_DA_CONTROLLARE]

    log.info(f"Lead da controllare (max {MAX_LEADS_DA_CONTROLLARE}): {len(leads_da_controllare)}")

    if not leads_da_controllare:
        log.info("Nessun lead da controllare. Fine.")
        return

    from playwright.async_api import async_playwright

    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=False, args=["--start-maximized"])
        ctx = await browser.new_context(
            storage_state=SESSION_PATH,
            viewport={"width": 1280, "height": 800},
            user_agent=UA,
        )
        ctx.set_default_timeout(20000)
        page = await ctx.new_page()

        # Valida sessione
        await page.goto("https://www.instagram.com/", wait_until="domcontentloaded")
        await asyncio.sleep(3)
        await dismiss_popups(page)
        if "accounts/login" in page.url:
            log.error("Sessione scaduta. Esegui: python refresh_session.py")
            await browser.close()
            return

        risposte_trovate = []

        for lead in leads_da_controllare:
            username  = lead["username"]
            nicchia   = lead.get("nicchia", "default")
            status    = lead.get("status", "")

            # Recupera il testo del nostro ultimo messaggio
            if status == "f2_sent":
                nostro_testo = lead.get("f2_text") or lead.get("f1_text") or lead.get("dm_text")
            elif status == "f1_sent":
                nostro_testo = lead.get("f1_text") or lead.get("dm_text")
            else:
                nostro_testo = lead.get("dm_text")

            log.info(f"  Controllo @{username} ({status})...")

            if await check_rate_limited(page):
                log.warning("  Rate limit — stop reply check")
                break

            # Apri il thread DM
            opened = await open_dm_thread(page, username)
            if not opened:
                log.info(f"  @{username}: thread non aperto — skip")
                await asyncio.sleep(random.uniform(3, 6))
                continue

            # Leggi i messaggi
            messages = await leggi_thread(page)

            # Verifica se hanno risposto
            risposto, testo_risposta = ha_risposto(messages, nostro_testo)

            if risposto:
                log.info(f"  @{username}: RISPOSTA trovata -> {testo_risposta[:80]!r}")

                # Genera risposta suggerita
                risposta_ai = classify_and_reply(
                    username=username,
                    nicchia=nicchia,
                    loro_msg=testo_risposta,
                    nostro_msg=nostro_testo or "",
                )

                risposte_trovate.append({
                    "username":   username,
                    "nicchia":    nicchia,
                    "loro_msg":   testo_risposta,
                    "risposta":   risposta_ai,
                    "lead":       lead,
                })

                if autoinvia and risposta_ai["testo"]:
                    ok = await invia_risposta_nel_thread(page, risposta_ai["testo"])
                    if ok:
                        lead["status"]            = "reply_gestita"
                        lead["risposta_ricevuta"] = testo_risposta
                        lead["reply_data"]        = str(date.today())
                        log.info(f"  [OK] Risposta inviata a @{username}")
                        # Salva immediatamente
                        with open(LEADS_PATH, "w", encoding="utf-8") as f:
                            json.dump(leads, f, ensure_ascii=False, indent=2)
                    else:
                        log.warning(f"  ✗ Invio fallito per @{username}")
                    await asyncio.sleep(random.uniform(30, 60))
            else:
                log.info(f"  @{username}: nessuna risposta ancora")

            await asyncio.sleep(random.uniform(5, 10))

        await browser.close()

    # ── STAMPA REPORT ─────────────────────────────────────────────────────────
    print()
    print("=" * 65)
    print(f"  INSTAGRAM REPLIES — {len(risposte_trovate)} risposta/e trovata/e")
    print("=" * 65)

    for item in risposte_trovate:
        print(f"\n{'-'*60}")
        print(f"  DA:        @{item['username']} ({item['nicchia']})")
        print(f"  LORO:      {item['loro_msg'][:120]}")
        print(f"  CATEGORIA: {item['risposta']['categoria']}")
        print(f"\n  ▶ RISPOSTA SUGGERITA:")
        print(f"  {item['risposta']['testo']}")
        print(f"{'-'*60}")

    if not autoinvia and risposte_trovate:
        print()
        print("  Copia-incolla le risposte sopra in Instagram.")
        print("  Per inviare automaticamente: python check_replies.py --autoinvia")

    print("=" * 65)

    # Salva lead aggiornati se non in autoinvia (già salvati sopra in autoinvia)
    if not autoinvia and risposte_trovate:
        for item in risposte_trovate:
            lead = item["lead"]
            lead["risposta_ricevuta"] = item["loro_msg"]
        with open(LEADS_PATH, "w", encoding="utf-8") as f:
            json.dump(leads, f, ensure_ascii=False, indent=2)

    log.info(f"COMPLETATO — {len(risposte_trovate)} risposte gestite")


if __name__ == "__main__":
    asyncio.run(main())
