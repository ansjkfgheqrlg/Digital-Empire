"""
Cover Generator (PIANO-KDP-67, CP7) — genera un'immagine di copertina REALE via LM Arena
(CP4), con un prompt costruito dai dettagli reali del libro (titolo, genere/keyword,
personaggi, trama) — mai un prompt fisso copiato da un altro libro. Copiare il prompt
produrrebbe copertine indistinguibili fra libri diversi, lo stesso bug di fondo gia' trovato
nell'audit originale (`genera_nuovo_libro.py` copiava sempre lo stesso file .png).
"""
from __future__ import annotations

from pathlib import Path
from typing import Callable

from playwright.sync_api import Page

from . import book_output_manager, config, lmarena_client


def _build_cover_prompt(book_context: dict) -> str:
    """Costruisce il prompt dai dettagli REALI del libro. `book_context` ha 3 chiavi
    opzionali (research/planning/writing, output delle rispettive fasi orchestrator) — usa
    quello che trova, non richiede tutte e 3 (es. un run con solo `writing`, senza
    planning/research a monte, produce comunque un prompt valido dal titolo)."""
    writing = book_context.get("writing") or {}
    planning = book_context.get("planning") or {}
    research = book_context.get("research") or {}

    title = writing.get("title") or planning.get("title") or research.get("title") or "Untitled"
    genre = research.get("keyword") or planning.get("keyword") or "fiction"
    characters = planning.get("characters", "")
    plot = planning.get("act1", "")

    details = f"Genre: {genre}."
    if characters:
        details += f" Main characters: {characters}."
    if plot:
        details += f" Setting/premise: {plot}"

    return (
        f"Design a professional book cover illustration for a {genre} novel titled "
        f"\"{title}\". {details} No text or typography in the image (title/author are "
        f"added separately during KDP formatting) — illustration only, evocative of the "
        f"genre and story, portrait orientation, high detail, publisher-quality artwork."
    )


def generate_cover(page: Page, book_context: dict, out_path: Path) -> Path:
    """Genera la copertina reale (CP7) via LM Arena e la salva in `out_path`. Fatto = un
    file .png reale su disco, con un prompt diverso per ogni libro diverso (mai lo stesso
    prompt fisso — quello e' il bug che questo checkpoint deve evitare per costruzione)."""
    prompt = _build_cover_prompt(book_context)
    return lmarena_client.send_image_prompt(page, prompt, out_path)


def make_real_cover_dep() -> Callable[[dict], dict]:
    """Dependency REALE per la fase COVER dell'orchestrator (CP9): apre una propria
    sessione LM Arena (non condivisa con planning/writing, stesso principio delle altre
    dependency reali — un resume dopo crash puo' rilanciare COVER da sola in un processo
    diverso), genera e salva la copertina, ritorna il path reale."""
    from playwright.sync_api import sync_playwright

    def _cover(book_context: dict) -> dict:
        writing = book_context.get("writing") or {}
        safe_title = book_output_manager.sanitize_title(writing.get("title", "cover"))
        out_dir = config.LIBRI_DIR / "_wip"
        out_path = out_dir / f"{safe_title}_cover.png"
        with sync_playwright() as p:
            session = lmarena_client.open_session(p, headless=False)
            try:
                cover_path = generate_cover(session.page, book_context, out_path)
            finally:
                session.close()
        print(f"[orchestrator] cover reale generata: {cover_path}")
        return {"cover_path": str(cover_path)}

    return _cover


if __name__ == "__main__":
    import sys
    import tempfile

    from playwright.sync_api import sync_playwright

    print("=== CP7 self-test REALE: 2 copertine per 2 libri diversi, verifica anti-copia ===\n")

    book_a = {
        "writing": {"title": "Knead to Know"},
        "planning": {
            "title": "Knead to Know",
            "characters": "Clara Miller, clumsy bakery owner; Barnaby, a perceptive ginger tabby",
            "act1": "Clara's great-grandmother's secret sourdough starter goes missing before the town bake-off.",
        },
        "research": {"keyword": "cozy mystery cats"},
    }
    book_b = {
        "writing": {"title": "The Last Ember"},
        "planning": {
            "title": "The Last Ember",
            "characters": "Kaelen, a disgraced war medic; Sera, a rogue AI courier drone",
            "act1": "In a frozen post-collapse city, Kaelen finds a signal claiming humanity's last reactor still burns.",
        },
        "research": {"keyword": "post-apocalyptic survival thriller"},
    }

    with sync_playwright() as p:
        session = lmarena_client.open_session(p, headless=False)
        try:
            out_a = Path(tempfile.gettempdir()) / "cp7_selftest_cover_a.png"
            out_b = Path(tempfile.gettempdir()) / "cp7_selftest_cover_b.png"

            print("[1/2] genero copertina reale libro A (cozy mystery)...")
            saved_a = generate_cover(session.page, book_a, out_a)
            size_a = saved_a.stat().st_size
            print(f"  salvata: {saved_a} ({size_a / 1024:.1f} KB)")
            assert size_a > 5 * 1024, f"file sospetto, troppo piccolo: {size_a} bytes"

            print("[2/2] genero copertina reale libro B (thriller post-apocalittico)...")
            saved_b = generate_cover(session.page, book_b, out_b)
            size_b = saved_b.stat().st_size
            print(f"  salvata: {saved_b} ({size_b / 1024:.1f} KB)")
            assert size_b > 5 * 1024, f"file sospetto, troppo piccolo: {size_b} bytes"

            assert size_a != size_b, (
                f"BUG: le due copertine hanno la STESSA dimensione byte ({size_a}) — "
                f"stesso identico test forense usato nell'audit originale per smascherare "
                f"il bug copia-template, qui NON deve riprodursi"
            )
            print(f"\n  [OK] dimensioni diverse ({size_a} vs {size_b} bytes) — non sono copie\n")
        finally:
            session.close()

    print("CP7 self-test: TUTTO VERIFICATO OK (2 copertine reali, diverse, verificate)")
    sys.exit(0)
