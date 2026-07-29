"""
WhatsApp — Invio messaggio reale via profilo persistente
===========================================================
Usa web.whatsapp.com/send?phone=...&text=... dentro il PROFILO CHROMIUM
PERSISTENTE creato da refresh_session.py (whatsapp-profile/) per aprire la
chat gia' precompilata e premere Invio. Non usa storage_state (WhatsApp Web
tiene le chiavi di sessione in IndexedDB, storage_state non le cattura).

Pensato per essere importato (funzione invia_async / invia_sync) dall'orchestratore
giornaliero (outreach_giornaliero.py), non solo lanciato da CLI.

Uso CLI:
    python "send_message.py" --phone 393927609928 --message "Ciao..."
    python "send_message.py" --phone 393927609928 --message "Ciao..." --dry-run
"""
import argparse
import asyncio
import os
import re
import sys
from urllib.parse import quote

BASE        = os.path.dirname(os.path.abspath(__file__))
PROFILE_DIR = os.path.join(BASE, "whatsapp-profile")

UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/124.0.0.0 Safari/537.36"
)

# Segnali noti di blocco/limitazione account WhatsApp — se compaiono, FERMA subito
# il batch del giorno (non ha senso continuare a mandare se l'account e' segnalato).
SEGNALI_BAN = [
    "account e' stato limitato", "account è stato limitato",
    "account has been temporarily banned", "account temporarily banned",
    "your account is banned", "account is not allowed to use whatsapp",
    "non puoi inviare messaggi", "hai raggiunto il limite",
    "you can no longer send messages", "message not sent due to abuse",
    "spam", "temporarily blocked",
]


def normalizza_numero(numero: str) -> str:
    """
    Numeri italiani locali (10 cifre, es. cellulare che inizia per 3xx) NON hanno il
    prefisso internazionale — controllare 'startswith 39' e' un falso positivo perche'
    molti prefissi mobili italiani (392, 393...) iniziano proprio per '39'. Si decide
    dalla LUNGHEZZA: 10 cifre = locale (prepend 39), 12 cifre gia' iniziate per 39 = ok cosi'.
    """
    n = re.sub(r"[^\d+]", "", numero or "")
    n = n.lstrip("+")
    if n.startswith("39") and len(n) == 12:
        return n
    if len(n) == 10:
        return "39" + n
    return n


def _rileva_ban(body_text: str) -> bool:
    bt = (body_text or "").lower()
    return any(s in bt for s in SEGNALI_BAN)


async def invia_async(phone: str, message: str, dry_run: bool = False) -> dict:
    """
    Ritorna {"esito": str, "dettaglio": str} — esiti possibili:
    inviato, dry_run_ok, numero_non_valido, chat_non_caricata, account_limitato,
    profilo_in_uso, errore
    """
    from playwright.async_api import async_playwright

    if not os.path.isdir(PROFILE_DIR):
        return {"esito": "profilo_mancante", "dettaglio": "Esegui prima refresh_session.py"}

    numero = normalizza_numero(phone)
    url = f"https://web.whatsapp.com/send?phone={numero}&text={quote(message)}"

    async with async_playwright() as pw:
        try:
            ctx = await pw.chromium.launch_persistent_context(
                PROFILE_DIR,
                headless=False,
                args=["--start-maximized"],
                viewport={"width": 1280, "height": 800},
                user_agent=UA,
                timeout=30000,
            )
        except Exception as e:
            msg = str(e)
            if "ProcessSingleton" in msg or "SingletonLock" in msg or "already running" in msg.lower():
                return {"esito": "profilo_in_uso", "dettaglio": "Chiudi la finestra Chrome/WhatsApp gia' aperta su questo profilo e riprova."}
            return {"esito": "errore", "dettaglio": f"Impossibile aprire il profilo: {e}"}

        try:
            page = ctx.pages[0] if ctx.pages else await ctx.new_page()

            await page.goto(url, wait_until="domcontentloaded")
            await asyncio.sleep(6)

            body_text = await page.evaluate("() => document.body.innerText")

            if _rileva_ban(body_text):
                return {"esito": "account_limitato", "dettaglio": body_text[:300]}

            if "Numero di telefono non valido" in body_text or "Phone number shared via url is invalid" in body_text:
                return {"esito": "numero_non_valido", "dettaglio": ""}

            # Alcuni flussi mostrano un bottone "Continua in chat" prima di aprire la conversazione
            for sel in ['a:has-text("Continua in chat")', 'a:has-text("Continue to Chat")',
                        'button:has-text("Continua")', 'button:has-text("Continue")']:
                try:
                    btn = await page.query_selector(sel)
                    if btn and await btn.is_visible():
                        await btn.click()
                        await asyncio.sleep(3)
                        break
                except Exception:
                    pass

            # Aspetta il campo di testo della chat — piu' selettori, WhatsApp cambia spesso il DOM
            input_sel = None
            candidati = [
                'footer div[contenteditable="true"]',
                'div[contenteditable="true"][data-tab]',
                'div[aria-label="Digita un messaggio"]',
                'div[aria-label="Type a message"]',
                '[contenteditable="true"]',
            ]
            for sel in candidati:
                try:
                    await page.wait_for_selector(sel, timeout=8000)
                    input_sel = sel
                    break
                except Exception:
                    continue

            if not input_sel:
                debug_path = os.path.join(BASE, f"debug_chat_non_caricata_{numero}.png")
                try:
                    await page.screenshot(path=debug_path)
                except Exception:
                    debug_path = None
                return {"esito": "chat_non_caricata", "dettaglio": f"screenshot: {debug_path}" if debug_path else body_text[:300]}

            await asyncio.sleep(2)  # il testo precompilato arriva via query string, lascialo assestare

            if dry_run:
                await asyncio.sleep(3)
                return {"esito": "dry_run_ok", "dettaglio": ""}

            input_el = await page.query_selector(input_sel)
            await input_el.click()
            await asyncio.sleep(0.5)
            await page.keyboard.press("Enter")
            await asyncio.sleep(2)

            # Ricontrolla eventuali segnali di ban apparsi DOPO l'invio (WhatsApp a volte
            # mostra il blocco solo dopo aver tentato di mandare, non prima)
            post_text = await page.evaluate("() => document.body.innerText")
            if _rileva_ban(post_text):
                return {"esito": "account_limitato", "dettaglio": post_text[:300]}

            return {"esito": "inviato", "dettaglio": ""}

        except Exception as e:
            return {"esito": "errore", "dettaglio": str(e)}
        finally:
            try:
                await ctx.close()
            except Exception:
                pass


def invia_sync(phone: str, message: str, dry_run: bool = False) -> dict:
    """Wrapper sincrono comodo per chiamare da script non-async (es. orchestratore)."""
    return asyncio.run(invia_async(phone, message, dry_run))


def main():
    parser = argparse.ArgumentParser(description="Invia messaggio WhatsApp via profilo persistente")
    parser.add_argument("--phone", required=True, help="Numero (con o senza prefisso 39)")
    parser.add_argument("--message", required=True, help="Testo del messaggio")
    parser.add_argument("--dry-run", action="store_true", help="Apre la chat e precompila, non invia")
    args = parser.parse_args()

    esito = invia_sync(args.phone, args.message, args.dry_run)
    print(f"\nESITO: {esito['esito']}")
    if esito.get("dettaglio"):
        print(f"DETTAGLIO: {esito['dettaglio']}")
    if esito["esito"] not in ("inviato", "dry_run_ok"):
        sys.exit(1)


if __name__ == "__main__":
    main()
