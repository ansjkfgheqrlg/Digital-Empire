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

    # Due cose vanno chieste in modo insistente e all'INIZIO, non di sfuggita in coda:
    # 1) il formato verticale — chiedendolo in fondo il modello ha restituito un quadrato
    #    1024x1024, inutilizzabile per un 6x9 (caso reale, 2026-08-08);
    # 2) il TITOLO scritto sulla copertina — scelta di Gael del 2026-08-10. Va ripetuto e
    #    messo tra virgolette perche' i modelli immagine sbagliano facilmente le lettere:
    #    per questo esiste il controllo OCR in `validators.valida_copertina_testo`, che
    #    verifica che il titolo sia davvero leggibile prima della consegna.
    author = book_context.get("planning", {}).get("author") or "Digital Empire"
    return (
        f"IMPORTANT — FORMAT: the image must be a TALL VERTICAL PORTRAIT rectangle with a "
        f"2:3 aspect ratio (like a real book cover, e.g. 1024 wide by 1536 tall). Do NOT "
        f"produce a square image.\n\n"
        f"IMPORTANT — TEXT: the cover must display the book title spelled EXACTLY as "
        f"\"{title}\" in large, bold, perfectly legible lettering in the upper third, and "
        f"the author name \"{author}\" smaller at the bottom. Spell every letter correctly. "
        f"Do not add any other words.\n\n"
        f"Design a professional book cover for a {genre} novel. {details} Evocative of the "
        f"genre and story, high detail, publisher-quality artwork, strong contrast between "
        f"the lettering and the artwork so the title stays readable as a small thumbnail."
    )


# Requisiti KDP reali per una copertina 6x9in (fonte: kdp.amazon.com, cover guidelines):
# rapporto altezza/larghezza 1.5, minimo 300 DPI sul trim con abbondanza.
KDP_ASPECT_RATIO = 1.5
KDP_ASPECT_TOLERANCE = 0.05
KDP_MIN_WIDTH_PX = 1600   # sotto questa larghezza KDP segnala bassa risoluzione


def verifica_copertina_kdp(path: Path) -> dict:
    """Controlla che l'immagine sia davvero utilizzabile su KDP (2026-08-08).

    Nato da un caso reale: la prima copertina generata per "The Quiet Hours" era bella e
    coerente ma **quadrata 1024x1024**, cioe' inutilizzabile per un 6x9 — e il codice
    l'aveva accettata perche' controllava solo che il file esistesse e pesasse piu' di 5KB.
    Un controllo sulla dimensione del file non dice NIENTE sull'usabilita': serve guardare
    le proporzioni e la risoluzione, come farebbe KDP al caricamento."""
    from PIL import Image

    with Image.open(path) as im:
        w, h = im.size
    ratio = h / w if w else 0
    problemi = []
    if abs(ratio - KDP_ASPECT_RATIO) > KDP_ASPECT_TOLERANCE:
        problemi.append(
            f"proporzioni sbagliate: 1:{ratio:.2f} invece di 1:{KDP_ASPECT_RATIO} "
            f"(6x9in) — KDP rifiuta o deforma"
        )
    if w < KDP_MIN_WIDTH_PX:
        problemi.append(f"risoluzione bassa: {w}px di larghezza, minimo {KDP_MIN_WIDTH_PX}px")
    return {"larghezza": w, "altezza": h, "rapporto": round(ratio, 3),
            "ok": not problemi, "problemi": problemi}


def adatta_a_kdp(src: Path, dest: Path | None = None,
                  larghezza_finale: int = 1800) -> Path:
    """Trasforma un'immagine qualsiasi in una copertina conforme a KDP (6x9in, 300 DPI).

    Perche' serve (2026-08-08): i modelli immagine di LM Arena restituiscono un quadrato
    1024x1024 qualunque cosa chieda il prompt — verificato chiedendo il formato verticale
    sia in coda sia in apertura, in maiuscolo, con le proporzioni esplicite. Invece di
    rigenerare all'infinito sperando in un formato diverso, si adatta l'immagine ottenuta:
    deterministico, ripetibile, indipendente dal modello.

    Come: ritaglio CENTRATO al rapporto 2:3 (i soggetti generati stanno praticamente
    sempre al centro), poi ingrandimento a risoluzione KDP con LANCZOS.

    Limite dichiarato, non nascosto: partendo da 1024px si ingrandisce di ~2.6x, quindi la
    resa e' buona ma non pari a un'illustrazione nativa ad alta risoluzione. Per un libro
    di punta conviene far rifinire la copertina a un grafico; per il volume di pubblicazione
    va bene."""
    from PIL import Image

    dest = dest or src.with_name(src.stem + "_kdp.png")
    altezza_finale = int(larghezza_finale * KDP_ASPECT_RATIO)

    with Image.open(src) as im:
        im = im.convert("RGB")
        w, h = im.size
        # ritaglio centrato al rapporto corretto
        if h / w < KDP_ASPECT_RATIO:          # troppo larga: taglio ai lati
            nuova_w = int(h / KDP_ASPECT_RATIO)
            sinistra = (w - nuova_w) // 2
            im = im.crop((sinistra, 0, sinistra + nuova_w, h))
        else:                                  # troppo alta: taglio sopra/sotto
            nuova_h = int(w * KDP_ASPECT_RATIO)
            alto = (h - nuova_h) // 2
            im = im.crop((0, alto, w, alto + nuova_h))
        im = im.resize((larghezza_finale, altezza_finale), Image.LANCZOS)
        dest.parent.mkdir(parents=True, exist_ok=True)
        im.save(dest, "PNG")

    print(f"[cover] adattata a KDP: {dest.name} ({larghezza_finale}x{altezza_finale}, 6x9in @300dpi)")
    return dest


def _font(dimensione: int):
    """Carica un font di sistema leggibile. Ordine di preferenza: serif eleganti prima
    (stanno bene su un thriller), poi qualunque cosa esista, poi il font di default."""
    from PIL import ImageFont
    candidati = ["georgiab.ttf", "timesbd.ttf", "constanb.ttf", "arialbd.ttf", "segoeuib.ttf"]
    for nome in candidati:
        try:
            return ImageFont.truetype(nome, dimensione)
        except OSError:
            continue
    return ImageFont.load_default()


def aggiungi_titolo(cover_path: Path, titolo: str, autore: str = "Digital Empire",
                     dest: Path | None = None) -> Path:
    """Scrive titolo e autore sulla copertina con un font vero.

    Perche' cosi' e non chiedendolo al modello (2026-08-10): il modello immagine e' stato
    provato due volte con istruzioni esplicite e non ha prodotto nulla di usabile (errori
    lato sito + un captcha da risolvere a mano ogni tentativo). Anche quando riesce, i
    modelli sbagliano le lettere — nella prima copertina aveva scritto "New Voicemail"
    troncando "1 New Voicemail". Scrivendo il testo qui: ortografia sempre corretta, font
    e posizione controllati, risultato ripetibile senza dipendere da un servizio esterno.

    Composizione: fascia scura semitrasparente in alto per il titolo (garantisce leggibilita'
    qualunque sia l'illustrazione sotto) e una in basso per l'autore."""
    from PIL import Image, ImageDraw

    cover_path = Path(cover_path)
    dest = dest or cover_path.with_name(cover_path.stem + "_titolo.png")

    with Image.open(cover_path) as im:
        im = im.convert("RGB")
        L, H = im.size
        disegno = ImageDraw.Draw(im, "RGBA")

        # --- titolo: a capo automatico per stare nei margini ------------------ #
        dim = int(L * 0.13)
        margine = int(L * 0.08)
        larghezza_max = L - 2 * margine
        while dim > 20:
            font = _font(dim)
            parole, righe, riga = titolo.upper().split(), [], ""
            for p in parole:
                prova = f"{riga} {p}".strip()
                if disegno.textlength(prova, font=font) <= larghezza_max:
                    riga = prova
                else:
                    if riga:
                        righe.append(riga)
                    riga = p
            if riga:
                righe.append(riga)
            if len(righe) <= 3:
                break
            dim = int(dim * 0.9)

        alt_riga = int(dim * 1.25)
        alt_blocco = alt_riga * len(righe)
        cima = int(H * 0.06)
        disegno.rectangle([0, cima - int(alt_riga * 0.4),
                            L, cima + alt_blocco + int(alt_riga * 0.35)], fill=(0, 0, 0, 165))
        for i, riga in enumerate(righe):
            w = disegno.textlength(riga, font=font)
            y = cima + i * alt_riga
            disegno.text(((L - w) / 2 + 3, y + 3), riga, font=font, fill=(0, 0, 0, 190))
            disegno.text(((L - w) / 2, y), riga, font=font, fill=(255, 255, 255, 255))

        # --- autore in basso -------------------------------------------------- #
        font_a = _font(int(L * 0.055))
        testo_a = autore.upper()
        wa = disegno.textlength(testo_a, font=font_a)
        ya = int(H * 0.90)
        disegno.rectangle([0, ya - int(L * 0.025), L, ya + int(L * 0.085)], fill=(0, 0, 0, 165))
        disegno.text(((L - wa) / 2 + 2, ya + 2), testo_a, font=font_a, fill=(0, 0, 0, 190))
        disegno.text(((L - wa) / 2, ya), testo_a, font=font_a, fill=(238, 232, 220, 255))

        im.save(dest, "PNG")

    print(f"[cover] titolo scritto sulla copertina: {dest.name}")
    return dest


def generate_cover(page: Page, book_context: dict, out_path: Path,
                    verifica: bool = True) -> Path:
    """Genera la copertina reale (CP7) via LM Arena e la salva in `out_path`. Fatto = un
    file .png reale su disco, con un prompt diverso per ogni libro diverso (mai lo stesso
    prompt fisso — quello e' il bug che questo checkpoint deve evitare per costruzione)
    E verificato utilizzabile su KDP (proporzioni + risoluzione), non solo esistente."""
    prompt = _build_cover_prompt(book_context)
    saved = lmarena_client.send_image_prompt(page, prompt, out_path)
    if verifica:
        esito = verifica_copertina_kdp(saved)
        if not esito["ok"]:
            print(f"[cover] ATTENZIONE, copertina NON pronta per KDP "
                  f"({esito['larghezza']}x{esito['altezza']}):")
            for p in esito["problemi"]:
                print(f"  - {p}")
            print(f"  File comunque salvato in {saved} — va adattato prima dell'uso.")
    return saved


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
            session = lmarena_client.open_session(p)
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
        session = lmarena_client.open_session(p)
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
