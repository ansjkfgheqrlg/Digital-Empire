#!/usr/bin/env python3
"""
Preventa Maps Scraper - Playwright ONLY + Google Sheets + Filtro ALTA
Versione 2.1 - 22/07/2026 - Build per Max S1-Freddo

Cosa fa:
- Playwright: apre Maps reale, cerca "concessionario auto a {città}", scrolla feed, clicca schede
- Estrae: nome, indirizzo, telefono, sito, recensioni, rating
- Analizza sito per ha_sito / ha_ads_attive / vecchio
- Calcola priorita_lead ALTA/MEDIA/BASSA
- Salva CSV deduplicato
- [NUOVO] Filtro --only-alta: salva solo ALTA priorità
- [NUOVO] Push automatico su Google Sheets con deduplica per telefono

Requisiti:
pip install -r requirements.txt
playwright install chromium
# per sheets opzionale:
# pip install gspread google-auth
"""

import argparse
import csv
import random
import re
import time
import os
import logging
from pathlib import Path
from datetime import datetime
from typing import List, Dict

import requests

from playwright.sync_api import sync_playwright, TimeoutError as PWTimeout

# ---------------- CONFIG ----------------
logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(message)s', datefmt='%H:%M:%S')
log = logging.getLogger("preventa-pw")

HEADERS_WEBSITE = {"User-Agent": "Mozilla/5.0 PreventaBot/1.0"}
DEFAULT_CITIES = ["Milano", "Bergamo", "Brescia"]
DEFAULT_CATEGORIA = "concessionario auto"

try:
    from dotenv import load_dotenv
    load_dotenv()
except:
    pass

def random_delay(a=1.0, b=3.0):
    time.sleep(random.uniform(a, b))

def normalize_key(name, addr, phone):
    phone_n = re.sub(r'\s+', '', (phone or ''))
    if phone_n:
        return f"tel:{phone_n}"
    return f"name:{(name or '').lower().strip()}|{(addr or '').lower().strip()}"

def normalize_phone(p: str) -> str:
    return re.sub(r'\s+', '', p or '').replace('-', '').replace('(', '').replace(')', '')

def check_website_quality(url: str) -> Dict:
    if not url:
        return {"ha_sito": False, "ha_pixel": False, "ha_gtm": False, "vecchio": True, "note": "Nessun sito", "https": False}
    res = {"ha_sito": True, "ha_pixel": False, "ha_gtm": False, "ha_ads": False, "vecchio": False, "https": url.startswith("https://"), "note": ""}
    try:
        t0 = time.time()
        r = requests.get(url, headers=HEADERS_WEBSITE, timeout=10, allow_redirects=True)
        html = r.text.lower()
        if time.time() - t0 > 4:
            res["note"] += "Sito lento. "
        if "fbevents.js" in html or "fbq(" in html or "connect.facebook.net" in html:
            res["ha_pixel"] = True
        if "googletagmanager.com" in html or "gtag(" in html or "google-analytics.com" in html:
            res["ha_gtm"] = True
        if "doubleclick.net" in html or "adsbygoogle" in html:
            res["ha_ads"] = True

        vecchio_score = 0
        if not res["https"]: vecchio_score += 2
        if "copyright 201" in html or "© 201" in html: vecchio_score += 1
        if "joomla" in html or "frontpage" in html: vecchio_score += 1
        if len(html) < 8000: vecchio_score += 1
        if "under construction" in html or "sito in manutenzione" in html or "costruzione" in html: vecchio_score += 2
        if vecchio_score >= 2:
            res["vecchio"] = True
            res["note"] += f"Sito scarso/vecchio score {vecchio_score}. "
        if not res["ha_pixel"] and not res["ha_gtm"]:
            res["note"] += "Nessun pixel/tracking (probabile no campagne). "
    except Exception as e:
        res["note"] += f"Err check sito {e}. "
        res["vecchio"] = True
    return res

def calcola_priorita(row, site_check):
    ha_sito = row.get("ha_sito", False)
    num = int(row.get("numero_recensioni") or 0)
    media = float(row.get("media_recensioni") or 0)

    if not ha_sito:
        return ("ALTA", "Senza sito web - priorità massima. Pitch modernizzazione.")
    if site_check.get("vecchio"):
        return ("ALTA", f"Sito vecchio/scarso. {site_check.get('note','')}")
    if num < 10:
        return ("ALTA", f"Poche recensioni ({num}) - attività poco digitalizzata.")
    if not site_check.get("ha_pixel") and not site_check.get("ha_gtm"):
        return ("MEDIA", "Sito ok ma no pixel/GTM -> probabile no ads attive.")
    if num < 25 or media < 4.0:
        return ("MEDIA", f"Base debole: {num} rec, media {media}.")
    return ("BASSA", "Strutturato: sito moderno + recensioni alte + tracking.")

def accept_cookies_if_any(page):
    selectors = [
        'button:has-text("Accetta tutto")',
        'button:has-text("Accetta")',
        'button:has-text("I agree")',
        'button:has-text("Accept all")',
        'div[jsname="b3VHJd"] button',
        '#L2AGLb',
        'button[aria-label*="Accept"]',
    ]
    for sel in selectors:
        try:
            btn = page.locator(sel).first
            if btn.count() > 0 and btn.is_visible(timeout=1000):
                btn.click(timeout=2000)
                log.info(f"Cookie banner chiuso con {sel}")
                random_delay(0.5, 1.2)
                return
        except:
            continue

def extract_details_from_pane(page) -> Dict:
    data = {}
    name_selectors = ['h1.DUwDvf', 'h1.x3AX1-LfntMc-header-title-title', 'h1']
    name = ""
    for sel in name_selectors:
        try:
            el = page.locator(sel).first
            if el.count() > 0:
                name = el.inner_text(timeout=1500).strip()
                if name: break
        except: pass
    data["nome_attivita"] = name

    addr_sel = ['button[data-item-id="address"] div.Io6YTe', 'button[data-item-id="address"]', '[data-item-id="address"] div.fontBodyMedium']
    address = ""
    for sel in addr_sel:
        try:
            el = page.locator(sel).first
            if el.count() > 0:
                address = el.inner_text(timeout=1500).strip()
                if address and len(address) > 5: break
        except: pass
    data["indirizzo"] = address

    phone_sel = ['button[data-item-id*="phone:tel"] div.Io6YTe', 'button[data-item-id^="phone"] div.Io6YTe', 'a[href^="tel:"]', '[data-item-id*="phone"]']
    phone = ""
    for sel in phone_sel:
        try:
            el = page.locator(sel).first
            if el.count() > 0:
                phone = el.inner_text(timeout=1500).strip()
                if phone: break
        except: pass
    if phone:
        m = re.search(r'(\+?39[\s\d]+|0\d[\s\d]{6,})', phone)
        if m: phone = m.group(1)
    data["telefono"] = phone

    site_sel = ['a[data-item-id="authority"]', 'a[data-item-id="authority"] div', 'a.lcr4fd']
    website = ""
    for sel in site_sel:
        try:
            el = page.locator(sel).first
            if el.count() > 0:
                href = el.get_attribute("href", timeout=1500)
                if href and href.startswith("http"):
                    website = href
                    break
        except: pass
    if not website:
        try:
            links = page.locator('a[href^="http"]').all()
            for l in links:
                try:
                    href = l.get_attribute("href")
                    if href and "google.com" not in href and "maps.google" not in href and len(href) > 10:
                        if any(x in href for x in ["facebook.com", "instagram.com", "google.com/maps"]):
                            continue
                        website = href
                        break
                except: continue
        except: pass
    data["sito_web"] = website

    rating = 0.0
    reviews = 0
    try:
        rating_sel = ['span.MW4etd', 'div.F7nice span[aria-hidden="true"]', 'span.ceNzKf[aria-label*="stelle"]']
        for sel in rating_sel:
            try:
                el = page.locator(sel).first
                if el.count() > 0:
                    txt = el.inner_text(timeout=1000).strip().replace(",", ".")
                    m = re.search(r'([0-5](?:\.\d)?)', txt)
                    if m:
                        rating = float(m.group(1))
                        if rating > 0: break
            except: pass

        review_sel = ['div.F7nice span', 'button:has-text("recensioni")', 'span:has-text("recension")', 'span.UY7F9']
        for sel in review_sel:
            try:
                els = page.locator(sel).all()
                for el in els:
                    txt = el.inner_text(timeout=800) if el else ""
                    if not txt: continue
                    m1 = re.search(r'\((\d+)\)', txt)
                    m2 = re.search(r'(\d+)\s*recension', txt.lower())
                    if m1:
                        reviews = int(m1.group(1))
                        break
                    if m2:
                        reviews = int(m2.group(1))
                        break
                if reviews: break
            except: continue
    except Exception as e:
        log.debug(f"Parse rating/recensioni fallito: {e}")

    data["media_recensioni"] = rating
    data["numero_recensioni"] = reviews
    data["maps_url"] = page.url

    return data

def scrape_city(page, city: str, categoria: str, limit: int) -> List[Dict]:
    query = f"{categoria} a {city}"
    search_url = f"https://www.google.com/maps/search/{query.replace(' ', '+')}/"
    log.info(f"\n=== CERCO: {query} ===")
    log.info(f"URL: {search_url}")

    leads_city = []
    try:
        page.goto(search_url, wait_until="domcontentloaded", timeout=30000)
        random_delay(2, 3)
        accept_cookies_if_any(page)

        try:
            page.wait_for_selector('div[role="feed"]', timeout=15000)
        except PWTimeout:
            log.warning(f"[{city}] Feed non trovato - forse zero risultati o blocco.")
            try:
                page.screenshot(path=f"data/debug_{city}_no_feed.png")
            except: pass
            return []

        feed_locator = page.locator('div[role="feed"]')
        previous_count = 0
        stable_iterations = 0
        scroll_attempts = 0
        max_scroll_attempts = 30

        while scroll_attempts < max_scroll_attempts:
            articles = page.locator('div[role="article"]')
            count = articles.count()
            log.info(f"[{city}] Risultati caricati: {count} / target {limit}")

            if count >= limit:
                break
            if count == previous_count:
                stable_iterations += 1
            else:
                stable_iterations = 0
            if stable_iterations >= 4:
                log.info(f"[{city}] Nessun nuovo risultato dopo scroll, stop.")
                break
            previous_count = count

            try:
                if count > 0:
                    articles.nth(count - 1).scroll_into_view_if_needed(timeout=3000)
                page.mouse.wheel(0, 4000)
            except: 
                try:
                    page.evaluate("el => el.scrollTop += 2000", feed_locator.element_handle())
                except:
                    page.mouse.wheel(0, 4000)

            random_delay(1.0, 2.2)
            scroll_attempts += 1

        articles = page.locator('div[role="article"]')
        total_found = articles.count()
        to_process = min(total_found, limit)
        log.info(f"[{city}] Processo {to_process} schede (trovate {total_found})")

        for idx in range(to_process):
            try:
                log.info(f"[{city}] -> Lead {idx+1}/{to_process}")
                articles = page.locator('div[role="article"]')
                if idx >= articles.count():
                    break
                art = articles.nth(idx)
                art.scroll_into_view_if_needed(timeout=3000)
                random_delay(0.6, 1.2)
                art.click(timeout=5000)
                random_delay(2.0, 3.5)

                try:
                    page.wait_for_selector('h1.DUwDvf', timeout=8000)
                except PWTimeout:
                    log.warning(f"Dettagli non caricati per idx {idx}, skip")
                    continue

                details = extract_details_from_pane(page)
                if not details.get("nome_attivita"):
                    log.warning("Nome vuoto, skip")
                    continue

                details["citta_ricerca"] = city
                details["categoria"] = categoria
                details["data_estrazione"] = datetime.now().strftime("%Y-%m-%d")

                sito = details.get("sito_web", "")
                time.sleep(random.uniform(0.8, 1.8))
                site_check = check_website_quality(sito)

                details["ha_sito"] = bool(sito) and site_check.get("ha_sito", True)
                details["ha_ads_attive"] = bool(site_check.get("ha_pixel") or site_check.get("ha_gtm") or site_check.get("ha_ads"))

                prio, note = calcola_priorita(details, site_check)
                details["priorita_lead"] = prio
                details["note_qualifica"] = note

                log.info(f"   ✓ {details['nome_attivita']} | tel:{details['telefono'][:15]} | sito:{bool(details['ha_sito'])} | rec:{details['numero_recensioni']} | prio:{prio}")
                leads_city.append(details)
                random_delay(1.2, 2.8)

            except Exception as e:
                log.warning(f"Errore estrazione idx {idx} città {city}: {e}")
                random_delay(1, 2)
                continue

    except Exception as e:
        log.error(f"Errore città {city}: {e}")
        try:
            page.screenshot(path=f"data/debug_{city}_error.png")
        except: pass

    return leads_city

def load_cities(args):
    cities = []
    if args.input:
        p = Path(args.input)
        if not p.exists():
            log.error(f"File input non trovato: {args.input}")
            exit(1)
        cities = [l.strip() for l in p.read_text(encoding="utf-8").splitlines() if l.strip() and not l.strip().startswith("#")]
    elif args.cities:
        raw = args.cities
        if "," in raw:
            cities = [c.strip() for c in raw.split(",") if c.strip()]
        else:
            cities = [c.strip() for c in raw.split() if c.strip()]
    else:
        cities = DEFAULT_CITIES
    return cities

def save_csv(leads: List[Dict], output_path: str, only_alta: bool = False):
    if not leads:
        log.warning("Nessun lead da salvare.")
        return [], []

    # deduplica globale
    deduped = {}
    for row in leads:
        key = normalize_key(row.get("nome_attivita",""), row.get("indirizzo",""), row.get("telefono",""))
        if key not in deduped:
            deduped[key] = row
        else:
            existing = deduped[key]
            if len(row.get("sito_web","")) > len(existing.get("sito_web","")):
                deduped[key] = row

    final = list(deduped.values())

    # filtra ALTA se richiesto
    if only_alta:
        final_filtered = [r for r in final if r.get("priorita_lead") == "ALTA"]
        log.info(f"Filtro --only-alta: {len(final_filtered)} ALTA su {len(final)} totali")
    else:
        final_filtered = final

    # ordina ALTA prima
    order = {"ALTA":0, "MEDIA":1, "BASSA":2}
    final_sorted = sorted(final, key=lambda x: (order.get(x.get("priorita_lead","BASSA"),2), x.get("numero_recensioni",0)))
    filtered_sorted = sorted(final_filtered, key=lambda x: (order.get(x.get("priorita_lead","BASSA"),2), x.get("numero_recensioni",0)))

    fieldnames = ["nome_attivita","indirizzo","telefono","sito_web","ha_sito","numero_recensioni","media_recensioni","ha_ads_attive","priorita_lead","citta_ricerca","categoria","note_qualifica","maps_url","data_estrazione"]

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
        w.writeheader()
        w.writerows(final_sorted)

    log.info(f"\n✓ CSV completo salvato: {output_path} | {len(final_sorted)} lead unici (da {len(leads)} estratti)")
    from collections import Counter
    c = Counter([r["priorita_lead"] for r in final_sorted])
    log.info(f"Distribuzione priorità (completo): {dict(c)}")

    # se filtro alta, salva anche file separato _ALTA.csv
    alta_path = None
    if only_alta:
        alta_path = str(Path(output_path).with_name(Path(output_path).stem + "_SOLO_ALTA.csv"))
        with open(alta_path, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
            w.writeheader()
            w.writerows(filtered_sorted)
        log.info(f"✓ CSV SOLO ALTA salvato: {alta_path} | {len(filtered_sorted)} lead")

    return final_sorted, filtered_sorted

# ---------------- GOOGLE SHEETS INTEGRATION ----------------
def upload_to_google_sheets(leads: List[Dict], sheet_id: str, creds_path: str, push_only_alta: bool = False, worksheet_name: str = "Foglio1"):
    """
    Push leads su Google Sheets con deduplica per telefono.
    - sheet_id: ID del Google Sheet (dalla URL: https://docs.google.com/spreadsheets/d/{ID}/edit)
    - creds_path: percorso file JSON service account
    - push_only_alta: se True pusha solo priorita ALTA
    - worksheet_name: nome foglio (default Foglio1)
    """
    if not sheet_id:
        log.warning("Sheet ID mancante, skip upload Sheets")
        return

    if push_only_alta:
        leads_to_push = [r for r in leads if r.get("priorita_lead") == "ALTA"]
        log.info(f"Filtro Sheets: solo ALTA -> {len(leads_to_push)} su {len(leads)}")
    else:
        leads_to_push = leads

    if not leads_to_push:
        log.warning("Nessun lead da pushare su Sheets")
        return

    try:
        import gspread
        from google.oauth2.service_account import Credentials
    except ImportError:
        log.error("Librerie Sheets mancanti. Installa: pip install gspread google-auth")
        log.error("Poi ripeti comando con --sheet-id")
        return

    creds_path = creds_path or os.getenv("GOOGLE_SHEETS_CREDS_PATH", "credentials.json")
    if not Path(creds_path).exists():
        log.error(f"File credenziali non trovato: {creds_path}")
        log.error("Crea Service Account su https://console.cloud.google.com/ -> IAM & Admin -> Service Accounts -> Create -> Keys -> JSON")
        log.error("Poi condividi il Google Sheet con l'email del service account (Editor).")
        return

    try:
        log.info(f"Connessione a Google Sheets ID={sheet_id[:10]}... con creds {creds_path}")
        scopes = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
        creds = Credentials.from_service_account_file(creds_path, scopes=scopes)
        client = gspread.authorize(creds)
        sheet = client.open_by_key(sheet_id)

        try:
            ws = sheet.worksheet(worksheet_name)
        except:
            log.info(f"Worksheet '{worksheet_name}' non trovato, uso primo foglio")
            ws = sheet.get_worksheet(0)

        # Leggi telefoni esistenti per deduplica
        existing_phones = set()
        try:
            records = ws.get_all_records()
            for rec in records:
                tel = normalize_phone(rec.get("telefono","") or rec.get("Telefono",""))
                if tel:
                    existing_phones.add(tel)
            log.info(f"Sheet esistente: {len(records)} righe, {len(existing_phones)} telefoni già presenti")
        except Exception as e:
            log.info(f"Sheet vuoto o errore lettura esistenti (normale se nuovo): {e}")
            # se vuoto, scrivi header
            if ws.row_count == 0 or ws.acell('A1').value is None:
                header = ["nome_attivita","indirizzo","telefono","sito_web","ha_sito","numero_recensioni","media_recensioni","ha_ads_attive","priorita_lead","citta_ricerca","categoria","note_qualifica","maps_url","data_estrazione"]
                ws.append_row(header)

        # Prepara righe nuove non duplicate
        new_rows = []
        skipped = 0
        for lead in leads_to_push:
            phone_norm = normalize_phone(lead.get("telefono",""))
            if phone_norm and phone_norm in existing_phones:
                skipped += 1
                continue
            if not lead.get("nome_attivita"):
                continue
            row = [
                lead.get("nome_attivita",""),
                lead.get("indirizzo",""),
                lead.get("telefono",""),
                lead.get("sito_web",""),
                str(lead.get("ha_sito","")),
                lead.get("numero_recensioni",0),
                lead.get("media_recensioni",0),
                str(lead.get("ha_ads_attive","")),
                lead.get("priorita_lead",""),
                lead.get("citta_ricerca",""),
                lead.get("categoria",""),
                lead.get("note_qualifica",""),
                lead.get("maps_url",""),
                lead.get("data_estrazione",""),
            ]
            new_rows.append(row)
            if phone_norm:
                existing_phones.add(phone_norm)

        if not new_rows:
            log.info(f"Nessun nuovo lead da aggiungere (skippati {skipped} duplicati)")
            return

        # Push a batch da 50 per rispettare limiti API
        batch_size = 50
        for i in range(0, len(new_rows), batch_size):
            batch = new_rows[i:i+batch_size]
            ws.append_rows(batch, value_input_option="USER_ENTERED")
            log.info(f"Sheets: pushate {len(batch)} righe batch {i//batch_size+1} / {(len(new_rows)-1)//batch_size+1}")
            time.sleep(1)

        log.info(f"✅ Sheets upload completo: {len(new_rows)} nuovi lead aggiunti, {skipped} duplicati saltati")

    except Exception as e:
        log.error(f"Errore upload Google Sheets: {e}")
        import traceback
        traceback.print_exc()

def main():
    parser = argparse.ArgumentParser(description="Preventa Maps Scraper - Playwright ONLY + Sheets + Filtro ALTA")
    parser.add_argument("--cities", type=str, help="Lista città separate da virgola: Milano,Bergamo,Brescia")
    parser.add_argument("--input", type=str, help="File txt con una città per riga")
    parser.add_argument("--categoria", type=str, default=DEFAULT_CATEGORIA)
    parser.add_argument("--output", type=str, default="data/leads_concessionari.csv")
    parser.add_argument("--limit", type=int, default=25, help="Max risultati per città")
    parser.add_argument("--headless", action="store_true")
    parser.add_argument("--headed", action="store_true")
    parser.add_argument("--only-alta", action="store_true", help="Salva solo lead priorita ALTA nel CSV (e crea file _SOLO_ALTA.csv)")
    parser.add_argument("--sheet-id", type=str, default=os.getenv("GOOGLE_SHEET_ID",""), help="ID Google Sheet per push auto (dalla URL)")
    parser.add_argument("--sheets-creds", type=str, default=os.getenv("GOOGLE_SHEETS_CREDS_PATH","credentials.json"), help="Path file JSON service account")
    parser.add_argument("--sheets-worksheet", type=str, default="Foglio1", help="Nome worksheet")
    parser.add_argument("--sheets-push-alta", action="store_true", help="Se push su Sheets, pusha solo ALTA (consigliato)")
    args = parser.parse_args()

    cities = load_cities(args)
    log.info(f"Città: {cities} | Categoria: {args.categoria} | Limit: {args.limit} | only-alta={args.only_alta}")

    headless = args.headless and not args.headed
    if not args.headless and not args.headed:
        headless = False
        log.info("Modalità: HEADED visibile (più stabile). Usa --headless per server.")

    all_leads = []

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=headless,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--no-sandbox",
                "--disable-dev-shm-usage",
                "--lang=it-IT,it",
            ]
        )
        context = browser.new_context(
            viewport={"width": 1366, "height": 850},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            locale="it-IT"
        )
        page = context.new_page()

        for i, city in enumerate(cities):
            city_leads = scrape_city(page, city, args.categoria, args.limit)
            all_leads.extend(city_leads)
            if i < len(cities)-1:
                pausa = random.uniform(3.0, 6.0)
                log.info(f"Pausa {pausa:.1f}s prima prossima città...")
                time.sleep(pausa)

        browser.close()

    final_sorted, filtered_sorted = save_csv(all_leads, args.output, only_alta=args.only_alta)

    # Push su Sheets se richiesto
    if args.sheet_id:
        log.info(f"\n=== PUSH GOOGLE SHEETS ===")
        upload_to_google_sheets(
            leads=final_sorted,
            sheet_id=args.sheet_id,
            creds_path=args.sheets_creds,
            push_only_alta=args.sheets_push_alta,
            worksheet_name=args.sheets_worksheet
        )
    else:
        log.info("\nNessun --sheet-id fornito: skip upload Sheets. CSV locale pronto.")

    log.info("\n✅ FATTO. CSV pronto per outreach APSOC.")
    log.info(f"File: {args.output}")
    if args.only_alta:
        log.info(f"File solo ALTA: {Path(args.output).with_name(Path(args.output).stem + '_SOLO_ALTA.csv')}")

if __name__ == "__main__":
    main()
