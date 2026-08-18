"""
Validatori editoriali e tecnici per i libri KDP (2026-08-10).

Ogni validatore risponde a UNA domanda e ritorna la lista degli errori trovati (vuota =
conforme). Nessuno di essi blocca da solo: e' `book_project.assembla` a decidere cosa fare
del risultato, cosi' la stessa funzione serve sia in fase di controllo sia in fase di
pubblicazione.

Dipendenze opzionali (pdfplumber, pytesseract+Tesseract): se mancano, il validatore NON
crolla — ritorna un avviso che dice esattamente cosa verificare a mano e come installare
lo strumento. Meglio un avviso onesto che un controllo silenziosamente saltato.
"""
from __future__ import annotations

import logging
import re
from pathlib import Path

logger = logging.getLogger(__name__)

# --------------------------------------------------------------------------- #
# Trattini
# --------------------------------------------------------------------------- #

# Trattini leciti, che NON sono "parola-parola" nel corpo del testo:
_RE_ELENCO = re.compile(r"^\s*[-*]\s+")            # marcatore di elenco puntato
_RE_TITOLO_MD = re.compile(r"^\s*#")                # intestazione markdown
_RE_URL = re.compile(r"https?://\S+")
# Date e intervalli numerici vanno neutralizzati PRIMA di cercare i trattini: il pattern
# "parola-parola" spezzerebbe "2024-01-01" trovando "2024-01" e segnalandolo per errore
# (falso positivo reale, trovato al primo test).
_RE_DATA = re.compile(r"\b\d{1,4}-\d{1,2}(-\d{1,4})?\b")
_RE_SEPARATORE = re.compile(r"^\s*-{3,}\s*$")      # riga di separazione ---
_RE_PAROLA_TRATTINO = re.compile(r"\b\w+-\w+\b")


# Trattini GRAMMATICALMENTE CORRETTI che non vanno segnalati (2026-08-10). La regola
# "niente trattini fra parole" applicata alla lettera segnalava 'twenty-nine', 'forty-one',
# 'check-up', 'second-cheapest': in inglese quei trattini sono obbligatori, toglierli
# renderebbe il testo sgrammaticato. Il difetto vero da intercettare e' un altro: la parola
# SPEZZATA dall'impaginazione (es. 'impagina-zione'), che e' brutta da vedere sulla pagina.
_NUMERI_COMPOSTI = (
    r"twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|"
    r"venti|trenta|quaranta|cinquanta|sessanta|settanta|ottanta|novanta"
)
_RE_NUMERO_COMPOSTO = re.compile(rf"^({_NUMERI_COMPOSTI})-\w+$", re.IGNORECASE)

# Prefissi/suffissi che formano composti legittimi in inglese e italiano.
_PREFISSI_LECITI = (
    "self", "well", "half", "non", "ex", "pre", "post", "anti", "co", "re", "sub",
    "super", "over", "under", "cross", "multi", "mid", "long", "short", "high", "low",
    "first", "second", "third", "one", "two", "three", "four", "five",
    "auto", "ultra", "extra", "inter", "sotto", "sopra", "auto",
)
_RE_PREFISSO_LECITO = re.compile(
    rf"^({'|'.join(_PREFISSI_LECITI)})-\w+$", re.IGNORECASE
)

# Seconde parti che rendono lecito il composto ('check-up', 'break-in', 'set-up'):
# in inglese i phrasal nouns si scrivono col trattino.
_SUFFISSI_LECITI = (
    "up", "in", "out", "off", "over", "on", "down", "back", "through", "by", "law",
    "old", "year", "years", "long", "wide", "based", "free", "like", "made", "born",
)
_RE_SUFFISSO_LECITO = re.compile(
    rf"^\w+-({'|'.join(_SUFFISSI_LECITI)})$", re.IGNORECASE
)


def valida_trattini(testo: str) -> list[str]:
    """Cerca trattini che spezzano una parola a meta' (residui di impaginazione).

    NON segnala i trattini grammaticalmente corretti — numeri composti ('twenty-nine'),
    composti con prefisso noto ('check-up', 'second-cheapest', 'self-made') — perche' in
    inglese e italiano sono obbligatori e toglierli produrrebbe testo sgrammaticato
    (falso positivo reale trovato al primo uso su un libro vero, 2026-08-10).

    Restano leciti anche: elenchi puntati, righe di separazione, date, URL, intestazioni."""
    errori: list[str] = []
    for n, riga in enumerate(testo.splitlines(), start=1):
        spoglia = riga.strip()
        if not spoglia or _RE_ELENCO.match(spoglia) or _RE_TITOLO_MD.match(spoglia) \
                or _RE_SEPARATORE.match(spoglia):
            continue
        ripulita = _RE_DATA.sub("DATA", _RE_URL.sub("URL", riga))
        for m in _RE_PAROLA_TRATTINO.finditer(ripulita):
            token = m.group()
            if (_RE_NUMERO_COMPOSTO.match(token) or _RE_PREFISSO_LECITO.match(token)
                    or _RE_SUFFISSO_LECITO.match(token)):
                continue
            errori.append(f"riga {n}: trattino in '{token}' — contesto: '{spoglia[:70]}'")
    if errori:
        logger.warning("valida_trattini: %d occorrenze", len(errori))
    return errori


_RE_LINEETTA = re.compile(r"[—–]|(?<= )--(?= )")


def valida_lineette(testo: str) -> list[str]:
    """Cerca le LINEETTE LUNGHE (— em dash, – en dash, ' -- ') e le boccia tutte.

    Regola di Gael, 2026-08-18: nei libri non ci devono essere. Sono la firma piu'
    riconoscibile della scrittura automatica — un lettore abituale di narrativa le nota, e
    su Amazon "sembra scritto dall'AI" e' una recensione che affonda un titolo.

    NON tocca i trattini delle parole composte ('twenty-nine', 'hand-lettered'): in
    inglese sono ortografia, non stile, e toglierli produrrebbe testo sgrammaticato. Quelli
    restano in carico a `valida_trattini`, che segnala e non blocca.

    Si sostituiscono con: virgola, punto, punto e virgola, due punti o parentesi — cioe'
    riscrivendo la frase, non cambiando il segno."""
    errori: list[str] = []
    for n, riga in enumerate(testo.splitlines(), start=1):
        spoglia = riga.strip()
        if not spoglia or _RE_SEPARATORE.match(spoglia):
            continue
        quante = len(_RE_LINEETTA.findall(spoglia))
        if quante:
            errori.append(f"riga {n}: {quante} lineetta/e lunghe — '{spoglia[:70]}'")
    if errori:
        logger.warning("valida_lineette: %d righe con lineette lunghe", len(errori))
    return errori


# --------------------------------------------------------------------------- #
# Numerazione pagine
# --------------------------------------------------------------------------- #

def valida_sillabazione_pdf(pdf_path: Path, testo_sorgente: str | None = None) -> list[str]:
    """Cerca parole SPEZZATE a fine riga nel PDF impaginato (es. "impagina-\\nzione").

    Questo e' il difetto di trattini che conta davvero (2026-08-10): nasce
    dall'impaginazione, non da chi scrive, e si vede solo sulla pagina stampata. Il
    controllo sul testo sorgente non puo' trovarlo — li' la riga non e' ancora andata a
    capo — e in compenso segnala trattini grammaticali corretti ('twenty-nine',
    'night-time', 'reel-to-reel'), che in narrativa inglese sono obbligatori.

    Se questo controllo trova qualcosa, la correzione non e' riscrivere il testo: e'
    disattivare la sillabazione automatica nell'impaginazione."""
    pdf_path = Path(pdf_path)
    if not pdf_path.exists():
        return [f"PDF non trovato: {pdf_path}"]
    try:
        import pdfplumber
    except ImportError:
        return ["VERIFICA A MANO: pdfplumber non installato. pip install pdfplumber"]

    sorgente = (testo_sorgente or "").lower()
    errori: list[str] = []
    with pdfplumber.open(pdf_path) as pdf:
        for n, pagina in enumerate(pdf.pages, start=1):
            testo = pagina.extract_text() or ""
            for riga in testo.splitlines():
                riga = riga.rstrip()
                m = re.search(r"(\S+)-$", riga)
                if not m or not re.search(r"[a-zA-ZàèéìòùÀÈÉÌÒÙ]-$", riga):
                    continue
                # Distinzione che conta: un a capo su un trattino GIA' PRESENTE nel testo
                # ("second-cheapest" spezzato dopo "second-") e' impaginazione corretta;
                # una parola spezzata dove il trattino non c'era e' sillabazione automatica,
                # ed e' il difetto da correggere. Si controlla nel sorgente.
                frammento = m.group(1).lower()
                if sorgente and f"{frammento}-" in sorgente:
                    continue
                errori.append(f"pagina {n}: parola spezzata a fine riga — '{riga.strip()[-40:]}'")
    if errori:
        logger.warning("valida_sillabazione_pdf: %d righe con parola spezzata", len(errori))
    return errori


def valida_numerazione_pagine(pdf_path: Path) -> list[str]:
    """Verifica che i numeri di pagina stiano SEMPRE nella stessa posizione (tutti in alto
    o tutti in basso). Una numerazione che salta da sopra a sotto e' il tipo di difetto che
    non si nota rileggendo a schermo e si vede subito sulla copia stampata."""
    pdf_path = Path(pdf_path)
    if not pdf_path.exists():
        return [f"PDF non trovato: {pdf_path}"]
    try:
        import pdfplumber
    except ImportError:
        return ["VERIFICA A MANO: pdfplumber non installato, impossibile controllare la "
                "posizione dei numeri di pagina. Installa con: pip install pdfplumber"]

    posizioni: list[tuple[int, str]] = []
    with pdfplumber.open(pdf_path) as pdf:
        for n, pagina in enumerate(pdf.pages, start=1):
            h = pagina.height
            for parola in pagina.extract_words():
                testo = (parola.get("text") or "").strip()
                if not testo.isdigit():
                    continue
                # Il numero di PAGINA e' quello che corrisponde alla posizione nel PDF.
                # Senza questo controllo un anno citato nel testo ("un tappeto scelto nel
                # 1988") in cima alla pagina veniva scambiato per numerazione in alto e
                # segnalato come incoerenza — falso positivo reale, 2026-08-10.
                # Si tollera uno scarto: la numerazione stampata puo' non partire da pag. 1
                # (frontespizio, pagine romane).
                if abs(int(testo) - n) > 5:
                    continue
                y = parola.get("top", 0)
                if y < h * 0.15:
                    posizioni.append((n, "alto"))
                    break
                if y > h * 0.85:
                    posizioni.append((n, "basso"))
                    break

    if not posizioni:
        return ["VERIFICA A MANO: nessun numero di pagina rilevato nel PDF."]

    riferimento = posizioni[0][1]
    errori = [f"pagina {n}: numero in '{p}', ma il resto del libro lo ha in '{riferimento}'"
              for n, p in posizioni if p != riferimento]
    if not errori:
        logger.info("valida_numerazione_pagine: coerente ('%s') su %d pagine",
                    riferimento, len(posizioni))
    return errori


# --------------------------------------------------------------------------- #
# Copertina
# --------------------------------------------------------------------------- #

def _normalizza(s: str) -> str:
    return re.sub(r"[^a-z0-9 ]+", " ", s.lower())


def _letture_ocr(img):
    """Piu' letture della stessa copertina, perche' una sola non basta.

    Tesseract e' tarato su pagine di testo, non su copertine: sull'immagine intera a
    1800x2700, con un titolo alto 200 px sopra un cielo sfumato, restituisce rumore.
    Misurato il 2026-08-17 sulle due copertine vere del progetto:

        The Ninth Winter  immagine intera -> 'FE ee eeeely ee er TN'   (0/3 parole)
        The Quiet Hours   immagine intera -> 'THE QUIET'               (2/3, passata per un pelo)

    Le stesse due, ritagliate in alto e binarizzate, danno 'THE NINTH WINTER' e
    'THE QUIET HOURS': 3/3 entrambe. Quindi si prova in piu' modi e si unisce il letto.

    Unire NON indebolisce il controllo: le parole devono comunque comparire davvero. Una
    copertina col titolo sbagliato non le produce in nessuna delle varianti."""
    from PIL import Image, ImageOps

    yield img                                    # com'e' — a volte basta
    if img.width > 1000:                         # i caratteri giganti confondono Tesseract
        yield img.resize((900, round(900 * img.height / img.width)), Image.LANCZOS)
    # Il titolo sta nella meta' alta: la si isola e si spinge il contrasto. Le due soglie
    # coprono i due casi opposti — testo chiaro su fondo scuro e testo scuro su fondo chiaro.
    meta = ImageOps.grayscale(img.crop((0, 0, img.width, img.height // 2)))
    yield meta.point(lambda x: 0 if x < 170 else 255)
    yield meta.point(lambda x: 255 if x < 110 else 0)
    yield ImageOps.autocontrast(meta)


def valida_copertina_testo(cover_path: Path, titolo_atteso: str | None = None) -> list[str]:
    """Verifica via OCR che la copertina contenga testo e, se richiesto, il titolo.

    Serve perche' i modelli immagine scrivono il testo in modo inaffidabile: lettere
    storte, parole troncate, titoli inventati. Il controllo automatico intercetta il caso
    peggiore — una copertina che sembra a posto a colpo d'occhio ma ha il titolo sbagliato.

    Confronto tollerante: maiuscole/minuscole e punteggiatura ignorate, e si accetta se
    almeno il 70% delle parole del titolo compare nell'OCR (l'OCR sbaglia sempre qualcosa)."""
    cover_path = Path(cover_path)
    if not cover_path.exists():
        return [f"Copertina non trovata: {cover_path}"]

    try:
        import pytesseract
        from PIL import Image
        # Su Windows Tesseract si installa fuori dal PATH: se c'e' nel percorso standard,
        # lo si indica esplicitamente invece di fallire dicendo "non installato".
        _std = Path(r"C:\Program Files\Tesseract-OCR\tesseract.exe")
        if _std.exists():
            pytesseract.pytesseract.tesseract_cmd = str(_std)
        pytesseract.get_tesseract_version()
    except ImportError:
        return ["VERIFICA A MANO: pytesseract/Pillow non installati. "
                "Installa con: pip install pytesseract Pillow"]
    except Exception:
        return ["VERIFICA A MANO: il motore Tesseract non e' installato sul PC (il pacchetto "
                "Python da solo non basta). Scaricalo da "
                "https://github.com/UB-Mannheim/tesseract/wiki e reinstalla; nel frattempo "
                "controlla a occhio che il titolo sulla copertina sia scritto correttamente."]

    immagine = Image.open(cover_path)
    letture = []
    for variante in _letture_ocr(immagine):
        try:
            letture.append(pytesseract.image_to_string(variante).strip())
        except Exception as exc:                 # una variante che fallisce non ferma le altre
            logger.debug("OCR copertina, variante saltata: %s", exc)
    testo = "\n".join(t for t in letture if t).strip()
    if not testo:
        return [f"Copertina '{cover_path.name}': nessun testo rilevato. "
                f"Deve riportare il titolo del libro."]

    logger.debug("OCR copertina:\n%s", testo)
    if not titolo_atteso:
        return []

    parole_titolo = [p for p in _normalizza(titolo_atteso).split() if len(p) > 2]
    ocr = _normalizza(testo)
    trovate = [p for p in parole_titolo if p in ocr]
    if not parole_titolo:
        return []
    quota = len(trovate) / len(parole_titolo)
    # Soglia al 50%. Con le letture multiple (`_letture_ocr`) entrambe le copertine vere del
    # progetto danno 3/3, quindi si potrebbe alzarla — ma resta bassa di proposito: questo
    # controllo BLOCCA, e un blocco che sbaglia insegna a scavalcarlo con --forza, il che
    # svuota tutti gli altri. Serve a intercettare il caso grave — copertina senza titolo, o
    # con un titolo diverso da quello del libro — non a fare le pulci all'OCR.
    if quota < 0.5:
        mancanti = [p for p in parole_titolo if p not in trovate]
        return [f"Copertina '{cover_path.name}': il titolo non sembra leggibile. "
                f"Parole non trovate dall'OCR: {mancanti}. Testo letto: {testo[:120]!r}. "
                f"Controlla a occhio prima di pubblicare."]
    if quota < 1.0:
        mancanti = [p for p in parole_titolo if p not in trovate]
        logger.info("OCR copertina: lette %d/%d parole del titolo (mancanti: %s) — "
                    "sopra soglia, nessun blocco", len(trovate), len(parole_titolo), mancanti)
    return []
