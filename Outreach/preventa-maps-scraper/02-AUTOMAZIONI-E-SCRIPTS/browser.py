# -*- coding: utf-8 -*-
"""
Owner: 01-AGENCY · Controllore: A2-QA · Origine: FORGE
Governo: MANDATO Art.8 + ADR-008

Browser module for Preventa Maps Scraper using Playwright.
Handles page navigation, scrolls, cookie consent, and detail extraction.
"""
from __future__ import annotations

import logging
import random
import re
import time
from datetime import datetime
from typing import List, Dict

from playwright.sync_api import TimeoutError as PWTimeout

from checker import check_website_quality, calcola_priorita

log = logging.getLogger("preventa-pw.browser")

DEFAULT_CITIES = ["Milano", "Bergamo", "Brescia"]
DEFAULT_CATEGORIA = "concessionario auto"

def random_delay(a: float = 1.0, b: float = 3.0):
    time.sleep(random.uniform(a, b))

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
        except Exception:
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
        except Exception: pass
    data["nome_attivita"] = name

    addr_sel = ['button[data-item-id="address"] div.Io6YTe', 'button[data-item-id="address"]', '[data-item-id="address"] div.fontBodyMedium']
    address = ""
    for sel in addr_sel:
        try:
            el = page.locator(sel).first
            if el.count() > 0:
                address = el.inner_text(timeout=1500).strip()
                if address and len(address) > 5: break
        except Exception: pass
    data["indirizzo"] = address

    phone_sel = ['button[data-item-id*="phone:tel"] div.Io6YTe', 'button[data-item-id^="phone"] div.Io6YTe', 'a[href^="tel:"]', '[data-item-id*="phone"]']
    phone = ""
    for sel in phone_sel:
        try:
            el = page.locator(sel).first
            if el.count() > 0:
                phone = el.inner_text(timeout=1500).strip()
                if phone: break
        except Exception: pass
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
        except Exception: pass
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
                except Exception: continue
        except Exception: pass
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
            except Exception: pass

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
            except Exception: continue
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
            except Exception: pass
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
            except Exception: 
                try:
                    page.evaluate("el => el.scrollTop += 2000", feed_locator.element_handle())
                except Exception:
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
        except Exception: pass

    return leads_city
