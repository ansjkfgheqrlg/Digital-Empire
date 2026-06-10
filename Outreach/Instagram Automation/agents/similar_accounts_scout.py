"""
Similar Accounts Scout Agent — Profili Simili da Lead Esistenti
Digital Empire — Instagram Outreach

Visita profili di lead già qualificati e raccoglie gli account suggeriti
da Instagram ("Profili simili" / "Suggeriti per te").
Questi sono lead ad altissima qualità perché algoritmicamente simili.

Usa anche la sezione "Esplora" per profili simili via API intercept.

Uso autonomo:
    python agents/similar_accounts_scout.py --input qualified_leads.json [--max-each 10]

Come modulo:
    from agents.similar_accounts_scout import run_similar_scout
    new_candidates = await run_similar_scout(page, qualified_leads, existing_usernames)
"""
import asyncio
import re
import random
import os
import sys
import json
import argparse
import logging

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

log = logging.getLogger(__name__)

_GENERIC_SKIP = {
    "instagram", "meta", "about", "help", "legal", "privacy", "security",
    "explore", "direct", "stories", "reels", "shop", "creator", "business",
    "accounts", "p", "reel", "tv", "ar", "web", "api", "graphql", "null",
    "undefined", "true", "false",
}


async def _dismiss_popups(page):
    for selector in [
        'button:has-text("Not Now")',
        'button:has-text("Non ora")',
        'button:has-text("Consenti tutti i cookie")',
        'button[aria-label="Close"]',
    ]:
        try:
            btn = await page.query_selector(selector)
            if btn and await btn.is_visible():
                await btn.click()
                await asyncio.sleep(0.5)
        except Exception:
            pass


async def scrape_similar_from_profile(
    page,
    username: str,
    existing_usernames: set,
    max_similar: int = 10,
) -> list[str]:
    """
    Visita il profilo @username e raccoglie account suggeriti/simili.

    Strategie (in cascata):
    1. API intercept: cattura risposte JSON con "edge_follow_suggestions"
       o "suggested_users" che Instagram carica nel profilo
    2. DOM: link nella sezione "Profili simili" / "Suggeriti per te"
    3. DOM: tutti i link profilo nella pagina (esclusi elementi UI)

    Restituisce lista di username suggeriti non già presenti nel DB.
    """
    api_suggested: list[str] = []

    async def _on_response(response):
        try:
            ct = response.headers.get("content-type", "")
            if "json" not in ct:
                return
            text = await response.text()
            # Cerca suggeriti nelle risposte JSON
            for pattern in [
                r'"username"\s*:\s*"([a-zA-Z0-9_.]{2,30})"',
            ]:
                for m in re.findall(pattern, text):
                    if m not in api_suggested:
                        api_suggested.append(m)
        except Exception:
            pass

    page.on("response", _on_response)

    similar: list[str] = []
    try:
        await page.goto(
            f"https://www.instagram.com/{username}/",
            wait_until="domcontentloaded",
        )
        await asyncio.sleep(4)
        await _dismiss_popups(page)

        # Scroll verso il basso per caricare la sezione "Profili simili"
        for _ in range(5):
            await page.evaluate("window.scrollBy(0, window.innerHeight * 1.5)")
            await asyncio.sleep(1.5)

        # Attendi ancora per API calls lazy
        await asyncio.sleep(2)

        # Estrai dal DOM: sezione suggeriti
        dom_candidates: list[str] = await page.evaluate(r"""
            () => {
                var links = new Set();

                // Cerca sezioni con testo "Profili simili" / "Suggeriti" / "Similar accounts"
                var headings = document.querySelectorAll('span, h2, h3, div');
                var suggestedSection = null;
                for (var el of headings) {
                    var txt = (el.innerText || el.textContent || '').trim().toLowerCase();
                    if (txt.includes('profili simili') || txt.includes('suggeriti') ||
                        txt.includes('similar accounts') || txt.includes('suggested')) {
                        suggestedSection = el.closest('section') || el.closest('div[class]') || el.parentElement;
                        break;
                    }
                }

                // Se trovata sezione specifica, prendi link da lì
                if (suggestedSection) {
                    var anchors = suggestedSection.querySelectorAll('a[href^="/"][href$="/"]');
                    for (var a of anchors) {
                        var href = a.getAttribute('href') || '';
                        var m = href.match(/^\/([a-zA-Z0-9_.]{3,30})\/?$/);
                        if (m) links.add(m[1]);
                    }
                }

                // Fallback: tutti i link profilo della pagina (escludi noti elementi UI)
                if (links.size < 3) {
                    var allAnchors = document.querySelectorAll('a[href^="/"][href$="/"]');
                    for (var a2 of allAnchors) {
                        var href2 = a2.getAttribute('href') || '';
                        var m2 = href2.match(/^\/([a-zA-Z0-9_.]{3,30})\/?$/);
                        if (m2) links.add(m2[1]);
                    }
                }

                return Array.from(links).slice(0, 40);
            }
        """) or []

        # Filtra username validi
        _SKIP = _GENERIC_SKIP | {username}

        seen: set[str] = set(existing_usernames)
        all_candidates = api_suggested + dom_candidates

        for uname in all_candidates:
            if len(similar) >= max_similar:
                break
            if (
                uname not in seen
                and uname.lower() not in _SKIP
                and len(uname) >= 3
                and not uname.isdigit()
            ):
                seen.add(uname)
                similar.append(uname)

        log.info(
            f"  [SIMILAR] @{username}: {len(api_suggested)} API + {len(dom_candidates)} DOM "
            f"→ {len(similar)} nuovi suggeriti"
        )

    except Exception as e:
        log.debug(f"  [SIMILAR] @{username}: errore — {e}")
    finally:
        try:
            page.remove_listener("response", _on_response)
        except Exception:
            pass

    return similar


async def run_similar_scout(
    page,
    qualified_leads: list[dict],
    existing_usernames: set,
    max_profiles_to_visit: int = 5,
    max_similar_per_profile: int = 10,
    delay_between: tuple = (3, 6),
) -> list[str]:
    """
    Visita i lead qualificati con score più alto e raccoglie account simili.

    Args:
        page:                     pagina Playwright con sessione valida
        qualified_leads:          lista di dict con chiave "username" (ordinata per score)
        existing_usernames:       set username già nel DB
        max_profiles_to_visit:    quanti lead visitare (default 5, prende i top per score)
        max_similar_per_profile:  suggeriti da raccogliere per profilo (default 10)
        delay_between:            (min, max) secondi tra visite

    Returns:
        Lista di username candidati nuovi (non in existing_usernames).
    """
    new_candidates: list[str] = []
    seen: set[str] = set(existing_usernames)

    # Visita i profili con bio_score più alto (già ordinati dal qualifier)
    top_leads = qualified_leads[:max_profiles_to_visit]

    for lead in top_leads:
        username = lead.get("username", "")
        if not username:
            continue

        candidates = await scrape_similar_from_profile(
            page, username, seen, max_similar_per_profile
        )
        for uname in candidates:
            if uname not in seen:
                seen.add(uname)
                new_candidates.append(uname)

        await asyncio.sleep(random.uniform(*delay_between))

    log.info(f"[SIMILAR] Completato — {len(new_candidates)} nuovi candidati da {len(top_leads)} profili visitati")
    return new_candidates


# ── Esecuzione standalone ──────────────────────────────────────────────────────

async def _standalone_main():
    import sys as _sys
    _sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s  %(message)s",
        handlers=[logging.StreamHandler()],
    )

    parser = argparse.ArgumentParser(description="Similar Accounts Scout — account simili da lead")
    parser.add_argument("--input", default="qualified_leads.json", help="JSON con lead qualificati")
    parser.add_argument("--max-each", type=int, default=10, help="Suggeriti per profilo")
    parser.add_argument("--max-profiles", type=int, default=5, help="Profili da visitare")
    parser.add_argument("--output", default="similar_candidates.json", help="Output JSON")
    args = parser.parse_args()

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    input_path = os.path.join(base_dir, args.input)
    if not os.path.exists(input_path):
        print(f"File input non trovato: {input_path}")
        return

    with open(input_path, encoding="utf-8") as f:
        qualified_leads = json.load(f)

    from config import SESSION_FILE
    session_path = os.path.join(base_dir, SESSION_FILE)
    if not os.path.exists(session_path):
        print("Sessione non trovata. Esegui prima: python refresh_session.py")
        return

    existing_usernames = {l["username"] for l in qualified_leads}

    from playwright.async_api import async_playwright
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=False, args=["--start-maximized"])
        ctx = await browser.new_context(
            storage_state=session_path,
            viewport={"width": 1280, "height": 800},
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
            ),
        )
        ctx.set_default_timeout(20000)
        page = await ctx.new_page()

        candidates = await run_similar_scout(
            page, qualified_leads, existing_usernames,
            max_profiles_to_visit=args.max_profiles,
            max_similar_per_profile=args.max_each,
        )

        output_path = os.path.join(base_dir, args.output)
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(candidates, f, ensure_ascii=False, indent=2)

        print(f"\nNuovi candidati: {len(candidates)}")
        print(f"Salvati in: {output_path}")
        await browser.close()


if __name__ == "__main__":
    asyncio.run(_standalone_main())
