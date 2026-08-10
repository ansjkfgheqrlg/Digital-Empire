"""
Amazon Research (PIANO-KDP-67, CP2) — naviga Amazon con la sessione reale salvata
(CP1) e estrae dati di libri veri da una ricerca per keyword.

A differenza di tutte le varianti consegnate negli zip analizzati (Playwright sempre
simulato, mai una vera `page.goto`): qui la navigazione è reale, con retry/backoff reali
su timeout o blocco, e i dati estratti sono quelli che Amazon restituisce davvero — se
Amazon cambia la struttura della pagina o blocca la richiesta, questo modulo lo dichiara
esplicitamente (lista vuota + errore loggato), non inventa risultati.
"""
from __future__ import annotations

import re
import time
from dataclasses import dataclass

from playwright.sync_api import Page, Playwright, TimeoutError as PlaywrightTimeoutError

from . import config, session_manager


@dataclass
class BookListing:
    title: str
    author: str | None
    price: str | None
    rating: str | None
    asin: str | None
    url: str | None
    reviews_count: int | None = None


def _extract_listings(page: Page, max_results: int = 20) -> list[BookListing]:
    """Estrae i dati REALI presenti nella pagina di risultati corrente. Selettori basati
    sulla struttura pagina Amazon nota — se Amazon cambia il DOM, questo va aggiornato
    (dichiarato nel piano come rischio reale, non nascosto)."""
    results = page.locator('div[data-component-type="s-search-result"]')
    count = min(results.count(), max_results)
    listings: list[BookListing] = []

    for i in range(count):
        item = results.nth(i)
        asin = item.get_attribute("data-asin") or None

        title = None
        for selector in ["h2 span", "h2 a span"]:
            loc = item.locator(selector).first
            if loc.count() > 0:
                text = loc.inner_text(timeout=2000).strip()
                if text:
                    title = text
                    break
        if not title:
            continue  # niente titolo = non è un vero risultato libro, salta senza inventare

        # Bug reale trovato in CP2 (2026-08-05), diagnosticato sul DOM vero (non un'ipotesi):
        # quando il libro fa parte di una serie, il div `a-row a-size-base a-color-secondary`
        # e' UNICO e contiene ENTRAMBI i link (serie E autore) separati da "|":
        #   <a>Book 3 of 4: Nome Serie</a> | <span>by </span><a>Nome Autore</a> | <data>
        # Prendere il primo <a> del div (fix precedente, sbagliato) prende sempre la serie.
        # Fix reale: individuare lo <span> con testo esatto "by" e prendere il link che lo segue.
        # Un caso residuo (audiolibro multi-autore/narratore): il nome non e' dentro un
        # <a> ma in uno <span> semplice ("by Autore, Narratore, et al.") — accettato anche
        # quel tag, prendendo solo il primo nome (autore principale), non l'intera lista.
        author = None
        author_loc = item.locator(
            'div.a-row.a-size-base.a-color-secondary span:text-is("by") + :is(a, span)'
        ).first
        if author_loc.count() > 0:
            author = author_loc.inner_text(timeout=2000).strip() or None

        price = None
        price_loc = item.locator("span.a-price span.a-offscreen").first
        if price_loc.count() > 0:
            price = price_loc.inner_text(timeout=2000).strip() or None

        rating = None
        rating_loc = item.locator("span.a-icon-alt").first
        if rating_loc.count() > 0:
            rating = rating_loc.inner_text(timeout=2000).strip() or None

        # Numero di recensioni: metrica chiave per valutare quanto e' aggredibile una
        # nicchia (pochi concorrenti con poche recensioni = spazio per entrare). Amazon lo
        # espone come link accanto alle stelle, con l'aria-label che contiene il conteggio.
        reviews_count = None
        for sel in ["a[aria-label*='ratings']", "a[aria-label*='rating']",
                     "span[aria-label*='ratings']", "span.a-size-base.s-underline-text"]:
            loc = item.locator(sel).first
            if loc.count() == 0:
                continue
            raw = (loc.get_attribute("aria-label") or loc.inner_text(timeout=2000) or "").strip()
            digits = re.sub(r"[^\d]", "", raw.split("ratings")[0] if "ratings" in raw else raw)
            if digits:
                reviews_count = int(digits)
                break

        link_loc = item.locator("h2 a").first
        url = None
        if link_loc.count() > 0:
            href = link_loc.get_attribute("href")
            if href:
                url = href if href.startswith("http") else config.AMAZON_BASE_URL + href

        listings.append(BookListing(title=title, author=author, price=price, rating=rating,
                                     asin=asin, url=url, reviews_count=reviews_count))

    return listings


def search_amazon(playwright: Playwright, keyword: str, headless: bool = True) -> list[BookListing]:
    """Cerca `keyword` su Amazon con la sessione reale salvata (CP1) e ritorna i libri
    trovati DAVVERO. Retry reali su timeout (config.MAX_RETRIES), backoff progressivo.
    Solleva l'eccezione originale se tutti i tentativi falliscono — mai un risultato finto."""
    context = session_manager.load_context(playwright, config.AMAZON_SESSION_PATH, headless=headless)
    page = context.new_page()
    url = config.AMAZON_SEARCH_URL_TEMPLATE.format(keyword=keyword.replace(" ", "+"))

    last_error: Exception | None = None
    for attempt in range(1, config.MAX_RETRIES + 1):
        try:
            print(f"[amazon-research] tentativo {attempt}/{config.MAX_RETRIES}: {url}")
            page.goto(url, wait_until="domcontentloaded", timeout=config.DEFAULT_TIMEOUT_MS)
            listings = _extract_listings(page)
            print(f"[amazon-research] trovati {len(listings)} risultati reali per '{keyword}'")
            context.close()
            return listings
        except PlaywrightTimeoutError as e:
            last_error = e
            wait_s = attempt * 2
            print(f"[amazon-research] timeout al tentativo {attempt}, riprovo tra {wait_s}s: {e}")
            time.sleep(wait_s)

    context.close()
    raise RuntimeError(
        f"Ricerca Amazon fallita dopo {config.MAX_RETRIES} tentativi per '{keyword}': {last_error}"
    )


if __name__ == "__main__":
    import sys

    from playwright.sync_api import sync_playwright

    keyword = " ".join(sys.argv[1:]) or "cozy mystery cats"
    print(f"=== CP2 self-test REALE: ricerca Amazon per '{keyword}' (sessione vera) ===\n")

    with sync_playwright() as p:
        listings = search_amazon(p, keyword, headless=True)

    if not listings:
        print("\nNESSUN risultato estratto — o Amazon ha cambiato il DOM, o la sessione "
              "non è valida, o la pagina non ha risultati. Non è un successo silenzioso.")
        sys.exit(1)

    print(f"\n=== {len(listings)} risultati REALI ===")
    for b in listings[:10]:
        print(f"- {b.title!r} | autore={b.author} | prezzo={b.price} | rating={b.rating} | asin={b.asin}")

    sys.exit(0)
