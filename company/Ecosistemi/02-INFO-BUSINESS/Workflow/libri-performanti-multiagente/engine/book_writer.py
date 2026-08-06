"""
Book Writer (PIANO-KDP-67, CP5) — genera outline (titolo, personaggi, trama in 3 atti) e
poi il manoscritto capitolo per capitolo via LM Arena (CP4), con continuita' REALE: ogni
prompt di capitolo include un riassunto di quanto scritto finora, non l'intero testo
precedente — scala su libri lunghi senza sforare il contesto o rigenerare tutto ogni volta.

Formato di continuita': ogni capitolo generato termina con un marcatore
'---RIASSUNTO---' seguito da 2-3 frasi di riassunto per il capitolo successivo — UN SOLO
prompt per capitolo (non un giro separato per il riassunto): ogni generazione reale su LM
Arena costa tempo/quota, un giro in piu' a capitolo raddoppierebbe il costo per l'intero libro.

Output: dict nella forma attesa da `orchestrator._phase_writing` /
`kdp_formatter.BookManuscript` — {"title", "author", "chapters": [{"title", "paragraphs"}]}.
"""
from __future__ import annotations

from typing import Callable

from playwright.sync_api import Page

from . import lmarena_client

SUMMARY_MARKER = "---RIASSUNTO---"

OUTLINE_FIELDS = ["TITLE", "CHARACTERS", "ACT 1", "ACT 2", "ACT 3"]


def _parse_outline(raw: str) -> dict:
    """Parsa la risposta strutturata (TITLE/CHARACTERS/ACT 1/ACT 2/ACT 3). Solleva
    ValueError esplicito se manca un campo obbligatorio — mai un outline finto/parziale."""
    lines_by_field: dict[str, list[str]] = {k: [] for k in OUTLINE_FIELDS}
    current: str | None = None
    for line in raw.splitlines():
        matched = None
        for key in OUTLINE_FIELDS:
            prefix = f"{key}:"
            if line.strip().upper().startswith(prefix):
                matched = key
                lines_by_field[key].append(line.strip()[len(prefix):].strip())
                break
        if matched:
            current = matched
        elif current and line.strip():
            lines_by_field[current].append(line.strip())

    missing = [k for k in OUTLINE_FIELDS if not lines_by_field[k]]
    if missing:
        raise ValueError(
            f"Outline incompleto, campi mancanti: {missing}. Risposta grezza: {raw[:500]!r}"
        )

    return {
        "title": " ".join(lines_by_field["TITLE"]),
        "characters": " ".join(lines_by_field["CHARACTERS"]),
        "act1": " ".join(lines_by_field["ACT 1"]),
        "act2": " ".join(lines_by_field["ACT 2"]),
        "act3": " ".join(lines_by_field["ACT 3"]),
    }


def generate_outline(page: Page, research: dict) -> dict:
    """Genera titolo, personaggi, trama in 3 atti (CP5). `research` e' l'output reale
    della fase RESEARCH (CP2/CP9): keyword, titolo di lavoro, descrizione, competitor
    Amazon veri — usati come riferimento di nicchia, non copiati."""
    competitors = research.get("competitors") or []
    competitors_note = ""
    if competitors:
        titles = ", ".join(c.get("title", "") for c in competitors[:5] if c.get("title"))
        if titles:
            competitors_note = f"\nExamples of successful books in this niche: {titles}"

    prompt = (
        f"You are outlining a new {research.get('keyword', 'fiction')} novel. "
        f"Working title/theme: \"{research.get('title', '')}\". "
        f"{research.get('description', '')}{competitors_note}\n\n"
        "Reply in EXACTLY this format, one field per line (no extra commentary before or after):\n"
        "TITLE: <a compelling book title>\n"
        "CHARACTERS: <main characters, one line, comma-separated, each with a short role>\n"
        "ACT 1: <setup, 2-3 sentences>\n"
        "ACT 2: <confrontation/rising action, 2-3 sentences>\n"
        "ACT 3: <resolution, 2-3 sentences>"
    )
    raw = lmarena_client.send_text_prompt(page, prompt)
    outline = _parse_outline(raw)
    outline["keyword"] = research.get("keyword", "")
    return outline


def _split_chapter_and_summary(raw: str) -> tuple[str, str]:
    if SUMMARY_MARKER not in raw:
        raise ValueError(
            f"Risposta capitolo senza marcatore '{SUMMARY_MARKER}' — impossibile estrarre "
            f"il riassunto per il capitolo successivo. Risposta grezza: {raw[:300]!r}"
        )
    body, _, summary = raw.partition(SUMMARY_MARKER)
    body, summary = body.strip(), summary.strip()
    if not body or not summary:
        raise ValueError("Capitolo o riassunto vuoto dopo lo split — generazione incompleta")
    return body, summary


def _chapter_prompt(outline: dict, chapter_number: int, total_chapters: int,
                     running_summary: str, words_per_chapter: int) -> str:
    continuity = (
        f"What has happened so far: {running_summary}"
        if running_summary else
        "This is the FIRST chapter — establish the setting and characters, no prior events."
    )
    return (
        f"Continue writing the novel \"{outline['title']}\".\n"
        f"Characters: {outline['characters']}\n"
        f"Overall plot — Act 1: {outline['act1']} Act 2: {outline['act2']} Act 3: {outline['act3']}\n"
        f"{continuity}\n\n"
        f"Write chapter {chapter_number} of {total_chapters}, approximately {words_per_chapter} "
        "words, prose only (no title heading, no meta-commentary), consistent with the characters "
        "and plot established above.\n\n"
        f"After the chapter text, add a line with EXACTLY '{SUMMARY_MARKER}' followed by a 2-3 "
        "sentence summary of THIS chapter's events, to be used as continuity context for the next one."
    )


def write_chapters(page: Page, outline: dict, total_chapters: int,
                    words_per_chapter: int = 1500) -> dict:
    """Loop capitolo per capitolo con continuita' REALE (CP5): ogni prompt include SOLO il
    riassunto accumulato dei capitoli precedenti, mai il testo intero. Fatto = bozza
    completa, un capitolo per iterazione, nessun capitolo saltato o finto."""
    chapters = []
    running_summary = ""
    for i in range(1, total_chapters + 1):
        prompt = _chapter_prompt(outline, i, total_chapters, running_summary, words_per_chapter)
        raw = lmarena_client.send_text_prompt(page, prompt, timeout_s=300)
        body, summary = _split_chapter_and_summary(raw)
        paragraphs = [p.strip() for p in body.split("\n\n") if p.strip()]
        if not paragraphs:
            raise RuntimeError(f"Capitolo {i}: nessun paragrafo estratto da una risposta non vuota")
        chapters.append({"title": f"Chapter {i}", "paragraphs": paragraphs})
        running_summary = f"{running_summary} {summary}".strip()

    return {
        "title": outline["title"],
        "author": "Digital Empire",
        "chapters": chapters,
    }


def make_real_planning_dep(page: Page) -> Callable[[dict], dict]:
    """Dependency REALE per la fase PLANNING dell'orchestrator (CP9)."""
    def _planning(research: dict) -> dict:
        return generate_outline(page, research)
    return _planning


def make_real_writing_dep(page: Page, total_chapters: int = 12,
                           words_per_chapter: int = 1500) -> Callable[[dict], dict]:
    """Dependency REALE per la fase WRITING dell'orchestrator (CP9)."""
    def _writing(planning: dict) -> dict:
        return write_chapters(page, planning, total_chapters, words_per_chapter)
    return _writing


if __name__ == "__main__":
    import sys

    from playwright.sync_api import sync_playwright

    from . import lmarena_client as _lc

    print("=== CP5 self-test REALE (scala ridotta): outline + 3 capitoli brevi su LM Arena ===\n")

    research = {
        "keyword": "cozy mystery cats",
        "title": "A small-town cozy mystery involving a cat, a bakery, and a missing recipe",
        "description": "cozy mystery, amateur sleuth, small town, light humor, no graphic violence",
        "competitors": [
            {"title": "Murder Past Due (Cat in the Stacks Mystery)"},
            {"title": "Claws of Justice: A Cozy Cat Mystery with Humor and a Murderous Twist"},
        ],
    }

    with sync_playwright() as p:
        session = _lc.open_session(p, headless=True)
        try:
            print("[1/2] genero outline reale...")
            outline = generate_outline(session.page, research)
            print(f"  TITLE: {outline['title']}")
            print(f"  CHARACTERS: {outline['characters']}")
            print(f"  ACT 1: {outline['act1']}")
            print(f"  ACT 2: {outline['act2']}")
            print(f"  ACT 3: {outline['act3']}")
            for field in ("title", "characters", "act1", "act2", "act3"):
                assert outline[field], f"campo outline vuoto: {field}"
            print("  [OK] outline reale completo\n")

            print("[2/2] genero 3 capitoli brevi reali (150 parole, per verificare il "
                  "meccanismo di continuita' senza consumare troppa quota)...")
            book = write_chapters(session.page, outline, total_chapters=3, words_per_chapter=150)
            assert book["title"] == outline["title"]
            assert len(book["chapters"]) == 3, f"attesi 3 capitoli, trovati {len(book['chapters'])}"
            for i, ch in enumerate(book["chapters"], start=1):
                assert ch["paragraphs"], f"capitolo {i} senza paragrafi"
                word_count = sum(len(p.split()) for p in ch["paragraphs"])
                print(f"\n  --- {ch['title']} ({word_count} parole) ---")
                print("  " + " ".join(ch["paragraphs"])[:400] + "...")
            print("\n  [OK] 3 capitoli reali generati con continuita' (leggere sopra per "
                  "verificare a mano coerenza di trama/personaggi, come richiesto da CP5)\n")
        finally:
            session.close()

    print("CP5 self-test (scala ridotta): TUTTO VERIFICATO OK")
    print("NOTA: libro completo a 120 pagine reali (~35000 parole, ~20+ capitoli) non generato "
          "qui per costo/tempo — il meccanismo (outline + continuita' + parsing) e' verificato "
          "reale su scala ridotta. Il run a piena scala e' compito di CP12 (test end-to-end).")
    sys.exit(0)
