"""
Hashtag Scout Agent — Deep Discovery
Digital Empire — Instagram Outreach

Scansiona 10+ hashtag, raccoglie 20-30 username per hashtag
tramite API network interception (il metodo più affidabile).

Uso autonomo:
    python agents/hashtag_scout.py [--hashtags h1,h2,h3] [--max 25]

Come modulo:
    from agents.hashtag_scout import run_scout
    candidates = await run_scout(page, hashtags, existing_usernames)
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
    "undefined", "true", "false", "error", "none",
}

RATE_LIMIT_SIGNALS = [
    "We restrict certain activity", "Limitiamo alcune attività",
    "Try again later", "Riprova più tardi",
    "Action Blocked", "Azione bloccata",
    "Please wait a few minutes", "Attendi qualche minuto",
]


async def _dismiss_popups(page):
    for selector in [
        'button:has-text("Not Now")',
        'button:has-text("Non ora")',
        'button:has-text("Consenti tutti i cookie")',
        'button:has-text("Allow All")',
        'button[aria-label="Close"]',
    ]:
        try:
            btn = await page.query_selector(selector)
            if btn and await btn.is_visible():
                await btn.click()
                await asyncio.sleep(0.8)
        except Exception:
            pass


async def _is_rate_limited(page) -> bool:
    try:
        body = await page.evaluate("() => document.body.innerText")
        for s in RATE_LIMIT_SIGNALS:
            if s.lower() in body.lower():
                return True
    except Exception:
        pass
    return False


async def scout_single_hashtag(
    page,
    hashtag: str,
    existing_usernames: set,
    max_profiles: int = 25,
    scroll_rounds: int = 10,
) -> list[str]:
    """
    Scansione profonda di un singolo hashtag.
    - scroll_rounds: numero di scroll per triggerare più API calls lazy
    - max_profiles: username unici da restituire
    Restituisce lista username validi non ancora nel DB.
    """
    api_usernames: list[str] = []

    async def _on_response(response):
        try:
            ct = response.headers.get("content-type", "")
            if "json" not in ct:
                return
            text = await response.text()
            for m in re.findall(r'"username"\s*:\s*"([a-zA-Z0-9_.]{2,30})"', text):
                if m not in api_usernames:
                    api_usernames.append(m)
        except Exception:
            pass

    page.on("response", _on_response)

    try:
        await page.goto(
            f"https://www.instagram.com/explore/tags/{hashtag}/",
            wait_until="domcontentloaded",
        )
        await asyncio.sleep(6)
        await _dismiss_popups(page)

        if await _is_rate_limited(page):
            log.warning(f"  [SCOUT] #{hashtag}: rate limit — skip")
            return []

        body = await page.evaluate("() => document.body.innerText")
        if "non è disponibile" in body.lower() or "not available" in body.lower():
            log.info(f"  [SCOUT] #{hashtag}: hashtag non disponibile")
            return []

        # Scroll aggressivo per triggerare lazy API calls
        for i in range(scroll_rounds):
            await page.evaluate("window.scrollBy(0, window.innerHeight * 2.5)")
            await asyncio.sleep(1.2)
            # Ogni 3 scroll, aspetta un po' di più per la rete
            if i % 3 == 2:
                await asyncio.sleep(1.5)

        # Script embedded come fallback
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
                ['__RELAY_STORE__', '__NEXT_DATA__'].forEach(function(id) {
                    var el = document.getElementById(id);
                    if (el) { try { extract(el.textContent); } catch(e) {} }
                });
                return Array.from(found);
            }
        """) or []

        # URL fast-path: /USERNAME/p/ID
        post_links: list[str] = await page.evaluate(r"""
            () => Array.from(document.querySelectorAll('a[href*="/p/"]'))
                .map(function(a) { return a.href; })
                .filter(function(v, i, arr) { return arr.indexOf(v) === i; })
                .slice(0, 60)
        """) or []
        url_usernames: list[str] = []
        for purl in post_links:
            m = re.search(r"instagram\.com/([a-zA-Z0-9_.]{2,30})/p/", purl)
            if m:
                url_usernames.append(m.group(1))

        all_candidates = api_usernames + script_usernames + url_usernames
        log.info(
            f"  [SCOUT] #{hashtag}: {len(api_usernames)} API + {len(script_usernames)} script "
            f"+ {len(url_usernames)} URL = {len(set(all_candidates))} candidati"
        )

        def _is_valid(u: str) -> bool:
            return (
                bool(u)
                and len(u) >= 3
                and u.lower() not in _GENERIC_SKIP
                and u not in existing_usernames
                and not u.isdigit()
                and "." not in u or len(u) > 4
            )

        result: list[str] = []
        seen: set[str] = set()
        for uname in all_candidates:
            if len(result) >= max_profiles:
                break
            if uname not in seen and _is_valid(uname):
                seen.add(uname)
                result.append(uname)

        log.info(f"  [SCOUT] #{hashtag}: {len(result)} profili selezionati (max {max_profiles})")
        return result

    except Exception as e:
        log.warning(f"  [SCOUT] #{hashtag}: errore — {e}")
        return []
    finally:
        try:
            page.remove_listener("response", _on_response)
        except Exception:
            pass


async def run_scout(
    page,
    hashtags: list[str],
    existing_usernames: set,
    max_per_hashtag: int = 25,
    max_hashtags: int = 10,
    delay_between: tuple = (4, 8),
) -> list[str]:
    """
    Scansiona più hashtag in serie nella stessa sessione browser.

    Args:
        page:               pagina Playwright già aperta con sessione valida
        hashtags:           lista hashtag da scansionare
        existing_usernames: set username già nel DB (evita duplicati)
        max_per_hashtag:    username da prendere per hashtag (default 25)
        max_hashtags:       quanti hashtag scansionare al massimo (default 10)
        delay_between:      (min, max) secondi tra hashtag per sembrare umano

    Returns:
        Lista di username candidati unici, non presenti nel DB.
    """
    all_candidates: list[str] = []
    seen: set[str] = set(existing_usernames)
    shuffled = hashtags.copy()
    random.shuffle(shuffled)

    for hashtag in shuffled[:max_hashtags]:
        candidates = await scout_single_hashtag(
            page, hashtag, seen, max_per_hashtag
        )
        for uname in candidates:
            if uname not in seen:
                seen.add(uname)
                all_candidates.append(uname)

        log.info(f"  [SCOUT] Pool totale: {len(all_candidates)} candidati")
        await asyncio.sleep(random.uniform(*delay_between))

    log.info(f"[SCOUT] Completato — {len(all_candidates)} candidati da {min(len(hashtags), max_hashtags)} hashtag")
    return all_candidates


# ── Esecuzione standalone ──────────────────────────────────────────────────────

async def _standalone_main():
    import sys as _sys
    _sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s  %(message)s",
        handlers=[logging.StreamHandler()],
    )

    parser = argparse.ArgumentParser(description="Hashtag Scout — scoperta massiva lead Instagram")
    parser.add_argument("--hashtags", default="", help="Hashtag separati da virgola")
    parser.add_argument("--max", type=int, default=25, help="Max profili per hashtag")
    parser.add_argument("--num", type=int, default=10, help="Numero hashtag da scansionare")
    parser.add_argument("--output", default="scout_results.json", help="File output JSON")
    args = parser.parse_args()

    from config import TARGET_HASHTAGS, SESSION_FILE

    session_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), SESSION_FILE)
    if not os.path.exists(session_path):
        print("Sessione non trovata. Esegui prima: python refresh_session.py")
        return

    hashtags = [h.strip() for h in args.hashtags.split(",") if h.strip()] or TARGET_HASHTAGS

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

        candidates = await run_scout(
            page, hashtags, set(),
            max_per_hashtag=args.max,
            max_hashtags=args.num,
        )

        output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", args.output)
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(candidates, f, ensure_ascii=False, indent=2)

        print(f"\nRisultati salvati in {output_path}")
        print(f"Totale candidati trovati: {len(candidates)}")
        await browser.close()


if __name__ == "__main__":
    asyncio.run(_standalone_main())
