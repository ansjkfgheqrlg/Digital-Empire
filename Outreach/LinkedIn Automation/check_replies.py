"""
LinkedIn DM Reply Checker — Digital Empire
==========================================
Apre LinkedIn Messaggi via Playwright, rileva risposte non lette
dai lead in leads.json, genera suggerimenti di risposta via AI.

MODALITÀ SICURA: legge solo, NON auto-invia.
Il testo suggerito viene stampato a schermo per copia-incolla manuale.

LOGICA:
- Cerca in leads.json chi ha status 'message_sent', 'followup1_sent', 'followup2_sent'
- Apre linkedin.com/messaging — cerca messaggi non letti
- Per ogni risposta: classifica + genera risposta suggerita
- Stampa tutto in linkedin_replies_log.txt
- Opzionale (flag --autoinvia): invia automaticamente le risposte
"""

import asyncio
import json
import os
import random
import sys
import logging
from datetime import datetime, date

BASE = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE, "linkedin_replies_log.txt")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler(sys.stdout),
    ]
)
log = logging.getLogger()

sys.path.insert(0, BASE)
from config import SESSION_FILE, LEADS_FILE, AGENCY_URL
from personalize import get_nicchia, NICCHIE, _ai, _AI_OK

SESSION_PATH = os.path.join(BASE, SESSION_FILE)
LEADS_PATH   = os.path.join(BASE, LEADS_FILE)
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"

STATI_CON_MESSAGGI = {"message_sent", "followup1_sent", "followup2_sent"}


# ── GENERATORI RISPOSTA ───────────────────────────────────────────────────────

def _classifica_e_rispondi(nome: str, titolo: str, messaggio_loro: str, ultimo_nostro: str) -> dict:
    """Classifica la risposta e genera la replica appropriata."""
    if not _AI_OK:
        return _fallback_risposta(nome, titolo, messaggio_loro)

    prompt_classificazione = f"""Classifica questo messaggio LinkedIn ricevuto dopo una nostra proposta di CRO/landing page.

NOSTRO ULTIMO MESSAGGIO: {ultimo_nostro[:200]}
LORO RISPOSTA: {messaggio_loro[:300]}

Categoria (scegli 1):
- POSITIVO: interessato, vuole info, aperto a call
- OBIEZIONE: resistenza (prezzo, tempo, già lo fa qualcuno, ci penso)
- DOMANDA: chiede dettagli, referenze, come funziona
- NON_INTERESSATO: no chiaro

JSON: {{"categoria": "X", "sintesi": "<5 parole sul contenuto>"}}"""

    from openai import OpenAI
    risposta_class = _ai(prompt_classificazione, max_tokens=80)
    categoria = "POSITIVO"
    try:
        if risposta_class:
            data = json.loads(risposta_class.strip().lstrip("```json").rstrip("```"))
            categoria = data.get("categoria", "POSITIVO")
    except Exception:
        pass

    # Genera risposta in base alla categoria
    prompt_risposta = f"""Sei Max Ricci, consulente di Digital Empire su LinkedIn.
Devi rispondere a {nome} ({titolo}) che ha risposto al tuo DM.

LORO MESSAGGIO: {messaggio_loro[:300]}
CATEGORIA: {categoria}

REGOLE:
- Prima persona singolare: io, ho, mi, mio. MAI noi/offriamo.
- MAX 60 parole.
- Zero esclamativi. Zero scuse. Zero "Grazie per la risposta".
- OBIETTIVO: fissare una call gratuita di 20 minuti.
- Per POSITIVO: proponi 2-3 opzioni orario concrete.
- Per OBIEZIONE: riframe, la call è gratuita e dura 20 minuti.
- Per DOMANDA: rispondi brevemente, proponi call per approfondire.
- Per NON_INTERESSATO: max 20 parole, rispettoso, porta aperta.
- ZERO link (siamo su LinkedIn, va messo a voce).

Solo il messaggio da inviare."""

    risposta_testo = _ai(prompt_risposta, max_tokens=150)
    if not risposta_testo:
        risposta_testo = _fallback_risposta(nome, titolo, messaggio_loro)["testo"]

    return {
        "categoria": categoria,
        "testo": risposta_testo.strip(),
    }


def _fallback_risposta(nome: str, titolo: str, messaggio: str) -> dict:
    testo_basso = messaggio.lower()
    if any(w in testo_basso for w in ["no grazie", "non interess", "rimuovi", "tolga"]):
        return {"categoria": "NON_INTERESSATO", "testo": "Capito, nessun problema. Se mai cambia qualcosa, sai dove trovarmi."}
    return {
        "categoria": "POSITIVO",
        "testo": f"Ho disponibilità martedì alle 10, giovedì alle 15 o venerdì alle 11. 20 minuti gratuiti — ti mostro cosa ho trovato, poi scegli tu. Ti va uno di questi?"
    }


# ── PLAYWRIGHT: LEGGI MESSAGGI ────────────────────────────────────────────────

async def leggi_messaggi_non_letti(page) -> list:
    """
    Apre linkedin.com/messaging e raccoglie le conversazioni con messaggi non letti.
    Restituisce lista di {profile_url, nome, messaggio_loro, messaggio_nostro_precedente}.
    """
    conversazioni = []
    try:
        await page.goto("https://www.linkedin.com/messaging/", wait_until="domcontentloaded")
        await asyncio.sleep(4)

        # Scroll per caricare tutte le conversazioni
        for _ in range(3):
            await page.evaluate("window.scrollBy(0, window.innerHeight)")
            await asyncio.sleep(1)

        # Raccoglie le conversazioni con badge "non letto"
        conv_els = await page.query_selector_all(
            '.msg-conversation-listitem, .msg-conversations-container__convo-item'
        )
        log.info(f"  Conversazioni trovate: {len(conv_els)}")

        for conv_el in conv_els[:30]:  # Max 30 conversazioni
            try:
                # Cerca badge non letto
                badge = await conv_el.query_selector('.notification-badge, .msg-conversation-listitem__unread-count')
                if not badge:
                    continue

                # Clicca sulla conversazione
                await conv_el.click()
                await asyncio.sleep(2)

                # Estrai URL profilo dalla conversazione
                profile_link = await page.query_selector('a[href*="/in/"]')
                profile_url = ""
                if profile_link:
                    href = await profile_link.get_attribute("href")
                    if href:
                        profile_url = href.split("?")[0].rstrip("/") + "/"

                # Estrai nome dell'interlocutore
                nome_el = await page.query_selector(
                    '.msg-s-message-group__profile-link, .msg-thread__link-to-profile'
                )
                nome = ""
                if nome_el:
                    nome = (await nome_el.inner_text()).strip()

                # Estrai gli ultimi messaggi (ultimi 3 per contesto)
                msgs = await page.query_selector_all('.msg-s-message-list__event')
                messaggi = []
                for msg_el in msgs[-6:]:
                    try:
                        corpo = await msg_el.query_selector('.msg-s-event-listitem__body, .msg-s-message-list-content')
                        if not corpo:
                            continue
                        testo = (await corpo.inner_text()).strip()
                        # Determina se è nostro o loro
                        is_outbound = await msg_el.query_selector('.msg-s-message-list__event--outbound, .msg-s-event-listitem--self')
                        messaggi.append({"testo": testo, "nostro": bool(is_outbound)})
                    except Exception:
                        continue

                if not messaggi:
                    continue

                # Ultimo messaggio loro = primo non-nostro dalla fine
                loro_msg = ""
                nostro_msg = ""
                for m in reversed(messaggi):
                    if not m["nostro"] and not loro_msg:
                        loro_msg = m["testo"]
                    if m["nostro"] and not nostro_msg:
                        nostro_msg = m["testo"]

                if loro_msg:
                    conversazioni.append({
                        "profile_url": profile_url,
                        "nome":        nome,
                        "messaggio_loro":   loro_msg,
                        "messaggio_nostro": nostro_msg,
                    })
                    log.info(f"  Risposta da {nome[:30]}: {loro_msg[:60]}...")

            except Exception as e:
                log.warning(f"  Errore lettura conversazione: {e}")
                continue

    except Exception as e:
        log.warning(f"  Errore apertura messaggi: {e}")

    return conversazioni


async def invia_dm(page, profile_url: str, testo: str) -> bool:
    """Invia un DM alla conversazione già aperta (o aprendola dal profilo)."""
    try:
        await page.goto(profile_url, wait_until="domcontentloaded")
        await asyncio.sleep(random.uniform(3, 5))

        msg_btn = await page.query_selector('button[aria-label*="Messaggio"], button[aria-label*="Message"]')
        if not msg_btn:
            return False

        await msg_btn.click()
        await asyncio.sleep(2)

        ta = await page.query_selector('.msg-form__contenteditable')
        if not ta:
            return False

        for char in testo:
            await ta.type(char, delay=random.uniform(18, 45))

        await asyncio.sleep(random.uniform(1, 2))
        send_btn = await page.query_selector('button[aria-label*="Invia"], button[aria-label*="Send"]')
        if send_btn:
            await send_btn.click()
            await asyncio.sleep(2)
            return True
    except Exception as e:
        log.warning(f"  Errore invio DM: {e}")
    return False


# ── MAIN ─────────────────────────────────────────────────────────────────────

async def main():
    autoinvia = "--autoinvia" in sys.argv

    log.info("=" * 60)
    log.info(f"LINKEDIN REPLY CHECK  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    log.info(f"Modalità: {'AUTO-INVIA' if autoinvia else 'SUGGERIMENTI (read-only)'}")
    log.info("=" * 60)

    # Carica leads
    if not os.path.exists(LEADS_PATH):
        log.info("Nessun leads.json trovato.")
        return
    with open(LEADS_PATH, encoding="utf-8-sig") as f:
        leads = json.load(f)

    # Lead che hanno ricevuto messaggi
    leads_con_msg = {
        l["profile_url"]: l
        for l in leads
        if l.get("status") in STATI_CON_MESSAGGI
    }
    log.info(f"Lead monitorati (con messaggi inviati): {len(leads_con_msg)}")

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

        # Leggi messaggi non letti
        conversazioni = await leggi_messaggi_non_letti(page)

        log.info(f"\nRisposte non lette trovate: {len(conversazioni)}")
        print()
        print("=" * 65)
        print("  RISPOSTE LINKEDIN — SUGGERIMENTI")
        print("=" * 65)

        risposte_generate = 0
        for conv in conversazioni:
            profile_url = conv["profile_url"]
            nome        = conv["nome"] or "il lead"
            loro_msg    = conv["messaggio_loro"]
            nostro_msg  = conv["messaggio_nostro"]

            # Trova titolo dal DB leads
            lead_db = leads_con_msg.get(profile_url, {})
            titolo  = lead_db.get("title", "professionista")
            nicchia = get_nicchia(titolo)

            # Genera risposta suggerita
            risposta = _classifica_e_rispondi(nome, titolo, loro_msg, nostro_msg)

            print(f"\n{'─'*60}")
            print(f"  DA:       {nome} ({titolo[:40]})")
            print(f"  PROFILO:  {profile_url}")
            print(f"  LORO:     {loro_msg[:120]}")
            print(f"  CATEGORIA: {risposta['categoria']}")
            print(f"\n  ▶ RISPOSTA SUGGERITA:")
            print(f"  {risposta['testo']}")
            print(f"{'─'*60}")

            log.info(f"RISPOSTA [{risposta['categoria']}] per {nome}: {risposta['testo'][:80]}...")
            risposte_generate += 1

            # Auto-invia se flag attivo
            if autoinvia and risposta["testo"] and profile_url:
                ok = await invia_dm(page, profile_url, risposta["testo"])
                if ok:
                    # Aggiorna leads.json
                    for lead in leads:
                        if lead.get("profile_url") == profile_url:
                            lead["status"] = "reply_gestita"
                            lead["reply_gestita_date"] = str(date.today())
                            break
                    log.info(f"  ✓ Risposta inviata automaticamente a {nome}")
                else:
                    log.warning(f"  ✗ Invio fallito per {nome}")
                await asyncio.sleep(random.uniform(30, 60))

        # Salva leads.json se aggiornato
        if autoinvia and risposte_generate > 0:
            with open(LEADS_PATH, "w", encoding="utf-8") as f:
                json.dump(leads, f, ensure_ascii=False, indent=2)

        await browser.close()

    print()
    print("=" * 65)
    print(f"  COMPLETATO — {risposte_generate} risposte gestite")
    if not autoinvia and risposte_generate > 0:
        print()
        print("  Copia-incolla le risposte sopra in LinkedIn.")
        print("  Per inviare automaticamente: python check_replies.py --autoinvia")
    print("=" * 65)
    log.info(f"COMPLETATO — {risposte_generate} risposte generate")


if __name__ == "__main__":
    asyncio.run(main())
