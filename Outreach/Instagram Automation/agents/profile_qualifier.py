"""
Profile Qualifier Agent — Bulk Bio Screener & DM Readiness Check
Digital Empire — Instagram Outreach

Visita profili candidati in batch, analizza bio con keyword matching esteso,
verifica presenza bottone Messaggio (account pubblico con DM aperto).
Restituisce solo lead "pronti" con bio target + DM disponibile.

Uso autonomo:
    python agents/profile_qualifier.py --input scout_results.json [--max 60]

Come modulo:
    from agents.profile_qualifier import run_qualifier
    qualified = await run_qualifier(page, candidate_usernames)
"""
import asyncio
import random
import os
import sys
import json
import argparse
import logging

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import TARGET_KEYWORDS

log = logging.getLogger(__name__)

# Keywords estese: forme femminili, varianti, categorie aggiuntive
EXTENDED_KEYWORDS = list(TARGET_KEYWORDS) + [
    # Forme femminili di professioni
    "formatrice", "consulente", "imprenditrice", "libera professionista",
    "esperta", "educatrice", "formatrice", "docente",
    # Varianti ortografiche / anglicismi
    "freelancer", "entrepreneur", "digital nomad",
    "content creator", "ugc creator", "ugc",
    "strategist", "growth hacker", "funnel",
    "ads specialist", "media buyer", "performance",
    "prodotto digitale", "online course",
    "accademia", "academy", "mentore",
    "personal brand", "brand identity",
    # Business online
    "reddito online", "lavoro da casa", "lavoro online",
    "guadagna online", "guadagnare", "rendita",
    "passive income", "financial freedom",
    # E-commerce varianti
    "seller", "store owner", "boutique online",
    "dropshipper", "print on demand",
]

# Keyword che indicano NON target (falsi positivi)
NEGATIVE_KEYWORDS = [
    "ristorante", "pizzeria", "trattoria", "osteria", "bar ", "caffè",
    "parrucchiere", "estetista", "barbiere", "nail ",
    "sezione ", "associazione ", "comune di", "municipio",
    "calcio ", "basket ", "tennis ", "pallavolo ",
    "moda ", "fashion ", "abbigliamento", "gioielleria",
    "casa editrice", "giornale", "quotidiano", "redazione",
    "scuola ", "istituto ", "università ", "liceo ",
    "arbite", "arbitro", "aia ",
    # Professionisti locali: fuori target dopo il pivot a implementazioni AI
    "avvocato", "avvocata", "commercialista", "notaio",
    "dentista", "odontoiatra", "fisioterapista", "osteopata",
    "psicolog", "nutrizionista", "personal trainer", "fotograf",
]


def _score_bio(bio: str) -> int:
    """
    Punteggio 0-10 per la bio.
    ≥ 1 → target; 0 → non target.
    """
    if not bio:
        return 0
    bl = bio.lower()

    # Penalità per keyword negative
    for neg in NEGATIVE_KEYWORDS:
        if neg in bl:
            return 0

    # Score per keyword positive
    score = 0
    for kw in EXTENDED_KEYWORDS:
        if kw.lower() in bl:
            score += 1
    return score


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


async def qualify_profile(page, username: str) -> dict:
    """
    Visita il profilo e restituisce il risultato di qualificazione.

    Campi ritornati:
        username, bio, name, bio_score, is_target, has_dm, is_private, not_found
    """
    result = {
        "username":  username,
        "bio":       "",
        "name":      "",
        "bio_score": 0,
        "is_target": False,
        "has_dm":    False,
        "is_private": False,
        "not_found": False,
    }

    try:
        await page.goto(
            f"https://www.instagram.com/{username}/",
            wait_until="domcontentloaded",
        )
        await asyncio.sleep(random.uniform(2.5, 4))
        await _dismiss_popups(page)

        body_text = await page.evaluate("() => document.body.innerText")

        # Profilo non trovato
        if any(s in body_text for s in [
            "Sorry, this page", "Spiacenti, questa pagina",
            "Page Not Found", "Pagina non trovata",
        ]):
            result["not_found"] = True
            return result

        # Profilo privato
        if any(s in body_text for s in [
            "This Account is Private", "Questo account è privato",
        ]):
            result["is_private"] = True
            return result

        # Estrai nome e bio dall'header
        header_text = await page.evaluate("""
            () => {
                const header = document.querySelector('header');
                return header ? header.innerText : document.body.innerText.slice(0, 600);
            }
        """)

        skip_words = [
            "follower", "seguac", "post", "seguendo", "following",
            "modifica profilo", "edit profile", "message", "messaggio",
        ]
        lines = [l.strip() for l in header_text.split("\n") if l.strip()]

        if lines:
            result["name"] = lines[0]

        for line in lines[1:]:
            if sum(1 for c in line if c.isdigit()) > len(line) * 0.5:
                continue
            if any(w in line.lower() for w in skip_words):
                continue
            if len(line) < 4:
                continue
            if line.startswith("http") or line.startswith("www."):
                continue
            result["bio"] = line
            break

        # Scoring bio
        result["bio_score"] = _score_bio(result["bio"])
        result["is_target"] = result["bio_score"] >= 1

        # Controlla bottone Messaggio solo per profili target (risparmia tempo)
        if result["is_target"]:
            has_msg: bool = await page.evaluate("""
                () => {
                    const texts = ['Messaggio', 'Message', 'Invia messaggio', 'Send message'];
                    const els = document.querySelectorAll(
                        'div[role="button"], button, a[role="button"]'
                    );
                    for (const el of els) {
                        if (el.offsetWidth === 0 && el.offsetHeight === 0) continue;
                        const t = (el.innerText || el.textContent || '').trim();
                        if (texts.includes(t)) return true;
                    }
                    return false;
                }
            """)
            result["has_dm"] = bool(has_msg)

        log.info(
            f"  [QUAL] @{username}: bio_score={result['bio_score']} "
            f"target={result['is_target']} dm={result['has_dm']} "
            f"bio={result['bio'][:40]!r}"
        )

    except Exception as e:
        log.debug(f"  [QUAL] @{username}: errore — {e}")

    return result


async def run_qualifier(
    page,
    candidate_usernames: list[str],
    max_qualify: int = 60,
    delay_between: tuple = (1.5, 3.0),
) -> list[dict]:
    """
    Qualifica un batch di candidati.

    Args:
        page:                pagina Playwright con sessione valida
        candidate_usernames: lista username da visitare
        max_qualify:         max profili da visitare (default 60)
        delay_between:       (min, max) secondi tra visite

    Returns:
        Lista di dict per profili is_target=True AND has_dm=True.
        Ordinata per bio_score decrescente (qualità migliore prima).
    """
    qualified: list[dict] = []
    checked = 0

    for username in candidate_usernames[:max_qualify]:
        result = await qualify_profile(page, username)
        checked += 1

        if result["is_target"] and result["has_dm"] and not result["is_private"]:
            qualified.append(result)
            log.info(f"  [QUAL] QUALIFICATO @{username} (score {result['bio_score']})")

        # Stop anticipato: se abbiamo già 30+ qualificati è più che sufficiente
        if len(qualified) >= 30:
            log.info(f"  [QUAL] 30 qualificati raggiunti dopo {checked} visite — stop anticipato")
            break

        await asyncio.sleep(random.uniform(*delay_between))

    # Ordina per bio_score decrescente — i migliori prima
    qualified.sort(key=lambda x: x["bio_score"], reverse=True)

    log.info(
        f"[QUAL] Completato — {len(qualified)} qualificati "
        f"su {checked} visitati ({checked}/{min(len(candidate_usernames), max_qualify)})"
    )
    return qualified


# ── Esecuzione standalone ──────────────────────────────────────────────────────

async def _standalone_main():
    import sys as _sys
    _sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s  %(message)s",
        handlers=[logging.StreamHandler()],
    )

    parser = argparse.ArgumentParser(description="Profile Qualifier — pre-screening bulk")
    parser.add_argument("--input", default="scout_results.json", help="JSON con lista username")
    parser.add_argument("--max", type=int, default=60, help="Max profili da visitare")
    parser.add_argument("--output", default="qualified_leads.json", help="File output JSON")
    args = parser.parse_args()

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    input_path = os.path.join(base_dir, args.input)
    if not os.path.exists(input_path):
        print(f"File input non trovato: {input_path}")
        return

    with open(input_path, encoding="utf-8") as f:
        candidates = json.load(f)

    from config import SESSION_FILE
    session_path = os.path.join(base_dir, SESSION_FILE)
    if not os.path.exists(session_path):
        print("Sessione non trovata. Esegui prima: python refresh_session.py")
        return

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

        qualified = await run_qualifier(page, candidates, max_qualify=args.max)

        output_path = os.path.join(base_dir, args.output)
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(qualified, f, ensure_ascii=False, indent=2)

        print(f"\nQualificati: {len(qualified)}")
        print(f"Salvati in: {output_path}")
        await browser.close()


if __name__ == "__main__":
    asyncio.run(_standalone_main())
