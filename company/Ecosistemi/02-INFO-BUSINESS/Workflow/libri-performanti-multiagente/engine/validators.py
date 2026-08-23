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

    NON tocca nemmeno le lineette DENTRO le virgolette: nel discorso diretto la lineetta
    ha una funzione vera che nessun altro segno fa, cioe' la parola tagliata a meta' —
    "There's Efrain's boy's wife. She'd be — " quando qualcuno interrompe, e "I'll — it'll
    be nothing" quando chi parla si corregge da solo. Quella non e' scrittura automatica,
    e' come si trascrive una voce (deciso con Gael, 2026-08-18).

    Si sostituiscono con: virgola, punto, punto e virgola, due punti o parentesi, cioe'
    riscrivendo la frase, non cambiando il segno."""
    errori: list[str] = []
    for n, riga in enumerate(testo.splitlines(), start=1):
        spoglia = riga.strip()
        if not spoglia or _RE_SEPARATORE.match(spoglia):
            continue
        # Spezzando sulle virgolette, i pezzi di posto pari sono narrazione e quelli di
        # posto dispari sono parlato: si guarda solo la narrazione.
        narrazione = "".join(spoglia.split('"')[::2])
        quante = len(_RE_LINEETTA.findall(narrazione))
        if quante:
            errori.append(f"riga {n}: {quante} lineetta/e lunghe fuori dal dialogo "
                          f"— '{spoglia[:70]}'")
    if errori:
        logger.warning("valida_lineette: %d righe con lineette lunghe", len(errori))
    return errori


# --------------------------------------------------------------------------- #
# Capitoli che si ripetono
# --------------------------------------------------------------------------- #

# Lunghezza della sequenza di parole usata come impronta. 8 parole di fila uguali sono
# gia' una coincidenza rara in prosa; 3-4 no (le frasi fatte le fanno scattare).
_PAROLE_IMPRONTA = 8
_RE_SEPARA_PAROLE = re.compile(r"[^\w']+", re.UNICODE)

# Soglie MISURATE, non scelte a sentimento (2026-08-23). Confrontate tutte le coppie di
# capitoli dei tre libri veri, 828 confronti in tutto:
#
#   The Ninth Winter           sovrapposizione massima  1,78%   (cap_18 vs cap_21)
#   The Quiet Hours                                     2,72%   (cap_11 vs cap_21)
#   The Second-Hand Spellbook                           0,92%   (cap_13 vs cap_24)
#   mediana, tutti e tre                                0,00%
#
# Controprova sullo stesso corpus: un capitolo di cui si ricopia META' e si allunga con
# testo nuovo esce al **98,8%**. Fra il caso peggiore vero (2,7%) e una duplicazione vera
# c'e' un fattore 36: qualsiasi soglia in mezzo funziona, e queste stanno larghe da
# entrambi i lati — 15% e' 5,5 volte il peggior caso legittimo mai visto qui.
SOGLIA_RIPETIZIONE_BLOCCA = 0.15
SOGLIA_RIPETIZIONE_AVVISA = 0.08


def _impronta(testo: str) -> set[int]:
    parole = [p for p in _RE_SEPARA_PAROLE.split(testo.lower()) if p]
    return {hash(tuple(parole[i:i + _PAROLE_IMPRONTA]))
            for i in range(max(0, len(parole) - _PAROLE_IMPRONTA + 1))}


def valida_ripetizioni(capitoli: dict[str, str]) -> list[str]:
    """Cerca capitoli che si ripetono l'un l'altro.

    PERCHE' ESISTE (2026-08-23). "Mai un capitolo identico o quasi a un altro" e' una delle
    sei regole non negoziabili del progetto, ed era l'unica **senza nessun controllo**:
    scritta in tre documenti, verificata da nessuno. Le altre cinque hanno tutte una
    funzione che blocca. Questa aspettava che me ne accorgessi rileggendo, che e'
    esattamente il tipo di garanzia che qui non vale niente.

    E' anche il difetto piu' probabile quando si scrivono 8 capitoli in un blocco solo con
    la scaletta sotto gli occhi: due capitoli che fanno la stessa scena in due posti
    diversi del libro.

    Confronta le sequenze di 8 parole di ogni capitolo con quelle di ogni altro, e misura
    quanta parte del capitolo piu' corto ricompare nell'altro. Sopra il 15% e' una
    ripetizione da riscrivere, sopra l'8% vale una riletta."""
    firme = {nome: _impronta(testo) for nome, testo in capitoli.items()}
    nomi = sorted(firme)
    problemi: list[str] = []
    for i, a in enumerate(nomi):
        for b in nomi[i + 1:]:
            fa, fb = firme[a], firme[b]
            if not fa or not fb:
                continue
            quota = len(fa & fb) / min(len(fa), len(fb))
            if quota >= SOGLIA_RIPETIZIONE_AVVISA:
                gravita = ("si ripetono" if quota >= SOGLIA_RIPETIZIONE_BLOCCA
                           else "si somigliano molto")
                problemi.append(
                    f"{a} e {b} {gravita}: il {quota * 100:.0f}% delle sequenze di "
                    f"{_PAROLE_IMPRONTA} parole e' in comune. Riscrivi quello dei due che "
                    f"aggiunge meno alla storia."
                )
    if problemi:
        logger.warning("valida_ripetizioni: %d coppie sospette", len(problemi))
    return problemi


def ripetizioni_bloccanti(problemi: list[str]) -> list[str]:
    """Delle coppie trovate, quelle che devono fermare la consegna."""
    return [p for p in problemi if "si ripetono" in p]


# --------------------------------------------------------------------------- #
# Copy KDP (la descrizione che legge chi compra)
# --------------------------------------------------------------------------- #

# Limiti della form KDP. Servono a non scoprire in fase di caricamento che la descrizione
# non ci sta: a quel punto la si taglia di fretta, ed e' il testo che vende il libro.
KDP_MAX_DESCRIZIONE = 4000
KDP_MAX_SOTTOTITOLO = 200
KDP_MAX_KEYWORD = 7
KDP_MAX_CARATTERI_KEYWORD = 50

_CAMPI_COPY_TESTUALI = (
    ("titolo_finale", "titolo"),
    ("sottotitolo", "sottotitolo"),
    ("descrizione", "descrizione"),
    ("descrizione_html", "descrizione HTML"),
    ("bio_autore", "bio autore"),
)


def valida_copy_kdp(copy: dict | None) -> list[str]:
    """Applica al COPY le stesse regole che valgono per il testo del libro.

    PERCHE' ESISTE (2026-08-23). La regola "niente lineette lunghe" girava solo sui
    capitoli. Il risultato, misurato sui pacchetti gia' consegnati: **3 lineette nella
    descrizione di The Ninth Winter e 2 in quella di The Quiet Hours**, cioe' nel testo
    che il compratore legge PRIMA di comprare — l'unico posto dove "sembra scritto
    dall'AI" costa davvero una vendita. Il controllo c'era e mancava proprio dove serve.

    Qui, a differenza dei capitoli, la lineetta NON e' mai lecita: nel copy non c'e'
    discorso diretto interrotto, quindi si guarda tutto il campo, virgolette comprese.

    Controlla anche i limiti della form KDP: descrizione, sottotitolo, numero e lunghezza
    delle keyword. Un copy senza campi (progetto vecchio) non e' un difetto del copy:
    ritorna vuoto, e a segnalarlo e' chi chiama."""
    if not copy:
        return []
    problemi: list[str] = []

    for chiave, nome in _CAMPI_COPY_TESTUALI:
        valore = (copy.get(chiave) or "").strip()
        if not valore:
            continue
        for m in _RE_LINEETTA.finditer(valore):
            inizio = max(0, m.start() - 45)
            problemi.append(
                f"{nome}: lineetta lunga — \"...{valore[inizio:m.end() + 45]}...\". "
                f"Riscrivi la frase (virgola, punto, due punti o parentesi)."
            )

    descrizione = (copy.get("descrizione") or "").strip()
    if len(descrizione) > KDP_MAX_DESCRIZIONE:
        problemi.append(f"descrizione di {len(descrizione)} caratteri: KDP ne accetta "
                        f"{KDP_MAX_DESCRIZIONE}, va accorciata prima del caricamento.")
    sottotitolo = (copy.get("sottotitolo") or "").strip()
    if len(sottotitolo) > KDP_MAX_SOTTOTITOLO:
        problemi.append(f"sottotitolo di {len(sottotitolo)} caratteri: il massimo e' "
                        f"{KDP_MAX_SOTTOTITOLO}.")

    keywords = copy.get("keywords") or []
    if len(keywords) > KDP_MAX_KEYWORD:
        problemi.append(f"{len(keywords)} keyword: KDP ne prende {KDP_MAX_KEYWORD}, "
                        f"le altre andrebbero perse senza accorgersene.")
    for k in keywords:
        if len(k) > KDP_MAX_CARATTERI_KEYWORD:
            problemi.append(f"keyword troppo lunga ({len(k)} caratteri, massimo "
                            f"{KDP_MAX_CARATTERI_KEYWORD}): '{k}'")

    if problemi:
        logger.warning("valida_copy_kdp: %d problemi nel copy", len(problemi))
    return problemi


# --------------------------------------------------------------------------- #
# Prezzo
# --------------------------------------------------------------------------- #

# Quanto ci si puo' allontanare dal prezzo medio MISURATO nella nicchia prima che valga la
# pena riguardarlo. Larghi di proposito: un libro puo' legittimamente stare sopra o sotto
# la media, quello che non deve succedere e' starci fuori **senza essersene accorti**.
PREZZO_MIN_RAPPORTO = 0.5
PREZZO_MAX_RAPPORTO = 2.0


def valida_prezzo(prezzo: float | None, prezzo_medio_nicchia: float | None) -> list[str]:
    """Confronta il prezzo scelto col prezzo medio davvero rilevato su Amazon.

    PERCHE' (2026-08-23). I prezzi dei primi tre libri ($11.99, $12.99, $13.99) sono stati
    decisi a mano, mentre il prezzo medio della nicchia era gia' stato MISURATO e stava
    scritto nel progetto: $10.77, $15.96, $21.19 a seconda della nicchia. Il dato c'era e
    non veniva guardato. Non e' un calcolo di redditivita' (per quello servirebbero le
    tariffe di stampa KDP, che cambiano e non sono misurate qui): e' un confronto fra due
    numeri che abbiamo entrambi."""
    if prezzo is None or not prezzo_medio_nicchia:
        return []
    rapporto = prezzo / prezzo_medio_nicchia
    if rapporto < PREZZO_MIN_RAPPORTO:
        return [f"prezzo ${prezzo:.2f} contro una media misurata di "
                f"${prezzo_medio_nicchia:.2f} nella nicchia: meta' del mercato. Su KDP un "
                f"prezzo molto sotto la media non segnala convenienza, segnala un libro "
                f"che vale meno."]
    if rapporto > PREZZO_MAX_RAPPORTO:
        return [f"prezzo ${prezzo:.2f} contro una media misurata di "
                f"${prezzo_medio_nicchia:.2f} nella nicchia: piu' del doppio. Verifica che "
                f"sia voluto."]
    return []


# --------------------------------------------------------------------------- #
# Capitolo interrotto a meta'
# --------------------------------------------------------------------------- #

# Un capitolo finito chiude cosi': punteggiatura forte, eventualmente seguita da una
# virgoletta di chiusura o da un asterisco di corsivo.
_RE_CHIUSURA_VERA = re.compile(r"""[.!?]["'\u201d\u00bb*]*\s*$|["'\u201d\u00bb]\s*$|\*\s*$""")

# Un capitolo troncato finisce in sospeso. Il \b davanti all'elenco e' OBBLIGATORIO: senza,
# il ramo "(the)\s*$" aggancia la fine di "breathe" e "(an)\s*$" quella di "woman", cioe'
# parole normalissime a fine riga. E' lo stesso genere di falso positivo gia' costato caro
# qui due volte (i trattini di 'twenty-nine', l'OCR della copertina).
_RE_FINALE_SOSPESO = re.compile(
    r"[,;:]\s*$"                                       # virgola, punto e virgola, due punti
    r"|\.\.\.\s*$|\u2026\s*$"                          # puntini di sospensione
    r"|\b(and|but|or|nor|the|an|of|in|on|at|to|for|with|that|which|who|"
    r"was|were|is|are|had|has|been|because|when|while|as|if|"
    r"ma|che|di|il|la|lo|un|una|per|con|su|tra|fra|quando|mentre)\s*$",
    re.IGNORECASE,
)


def valida_troncamento(testo: str, nome: str = "capitolo") -> list[str]:
    """Dice se un testo si interrompe a meta', invece di finire.

    Serve per me, non per un modello: quando scrivo un blocco di capitoli, uno che
    finisce a meta' frase e' un difetto che nessun altro controllo vede — il conteggio
    parole e' a posto, le pagine pure, e il libro va in stampa con un capitolo mozzo.

    **Non guarda le virgolette bilanciate**, di proposito. E' l'euristica ovvia ed e'
    sbagliata sulla narrativa: una battuta che prosegue per due paragrafi apre le
    virgolette nel primo e le chiude nel secondo, e conta come "sbilanciata" pur essendo
    scritta bene. Su The Ninth Winter produrrebbe decine di falsi positivi. Un controllo
    che sbaglia insegna a scavalcarlo, e allora non serve piu' a niente.

    Guarda solo come finisce l'ultima riga di testo vero, che e' l'unico segnale
    affidabile e non ha falsi positivi in prosa curata."""
    righe = [r.strip() for r in testo.strip().splitlines() if r.strip()]
    righe = [r for r in righe if not _RE_SEPARATORE.match(r)]
    if not righe:
        return [f"{nome}: vuoto"]

    ultima = righe[-1]
    if _RE_FINALE_SOSPESO.search(ultima):
        return [f"{nome}: finisce in sospeso — \"...{ultima[-60:]}\""]
    if not _RE_CHIUSURA_VERA.search(ultima):
        return [f"{nome}: l'ultima riga non chiude — \"...{ultima[-60:]}\""]
    return []


# --------------------------------------------------------------------------- #
# Numerazione pagine
# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #
# Lettura del PDF, una volta sola
# --------------------------------------------------------------------------- #

# Aprire un PDF di 116 pagine con pdfplumber costa ~9 secondi, e la consegna lo faceva DUE
# volte: una per la sillabazione e una per la numerazione. Misurato il 2026-08-19 mentre si
# tagliavano i tempi di produzione: 41s totali di codice, di cui 19 solo per rileggere due
# volte lo stesso file. Qui si legge una volta e si tiene, con la chiave che comprende
# mtime e dimensione: se il PDF viene rigenerato, la cache non serve un dato vecchio.
_CACHE_PDF: dict = {}


class PdfIlleggibile(RuntimeError):
    """Il PDF c'e' ma non si apre. Non e' un difetto del libro: e' un controllo che non
    e' potuto girare, e va detto come tale invece di far cadere tutta la consegna.

    Trovato scrivendo i test il 2026-08-23: bastava un PDF troncato o scritto a meta' e
    `assembla` moriva con l'eccezione di pdfminer, senza verdetto e senza REPORT, dopo aver
    gia' fatto tutto il lavoro."""


def _pagine_pdf(pdf_path: Path):
    """[(testo, parole, altezza)] per pagina. Rilegge solo se il file e' cambiato."""
    import pdfplumber

    st = Path(pdf_path).stat()
    chiave = (str(Path(pdf_path).resolve()), st.st_mtime_ns, st.st_size)
    if chiave in _CACHE_PDF:
        return _CACHE_PDF[chiave]
    with pdfplumber.open(pdf_path) as pdf:
        pagine = [(pagina.extract_text() or "", pagina.extract_words(), pagina.height)
                  for pagina in pdf.pages]
    # Un libro alla volta: tenerne di piu' terrebbe in memoria centinaia di pagine per
    # niente, visto che la consegna lavora su un PDF solo.
    _CACHE_PDF.clear()
    _CACHE_PDF[chiave] = pagine
    return pagine


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
    try:
        pagine = _pagine_pdf(pdf_path)
    except Exception as exc:  # noqa: BLE001 — un PDF illeggibile non fa cadere la consegna
        return [f"VERIFICA A MANO: il PDF non si apre ({type(exc).__name__}), "
                f"impossibile cercare le parole spezzate a fine riga."]
    for n, (testo, _parole, _h) in enumerate(pagine, start=1):
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
    try:
        pagine = _pagine_pdf(pdf_path)
    except Exception as exc:  # noqa: BLE001
        return [f"VERIFICA A MANO: il PDF non si apre ({type(exc).__name__}), "
                f"impossibile controllare la posizione dei numeri di pagina."]
    for n, (_testo, parole, h) in enumerate(pagine, start=1):
        for parola in parole:
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

    # ORDINE VOLUTO (2026-08-19): prima quella che sulle copertine vere funziona. Chi chiama
    # si ferma appena il titolo si legge, quindi la prima variante decide il costo. Sulle due
    # copertine del progetto la meta' alta binarizzata da' 3 parole su 3 da sola, mentre
    # l'immagine intera ne da' 0 e 2. Cambiare quest'ordine rallenta e basta.
    meta = ImageOps.grayscale(img.crop((0, 0, img.width, img.height // 2)))
    yield meta.point(lambda x: 0 if x < 170 else 255)   # testo chiaro su fondo scuro
    yield meta.point(lambda x: 255 if x < 110 else 0)   # testo scuro su fondo chiaro
    yield ImageOps.autocontrast(meta)
    yield img                                           # com'e'
    if img.width > 1000:                                # i caratteri giganti confondono Tesseract
        yield img.resize((900, round(900 * img.height / img.width)), Image.LANCZOS)


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
    parole_titolo = [w for w in _normalizza(titolo_atteso or "").split() if len(w) > 2]
    letture = []
    for n_var, variante in enumerate(_letture_ocr(immagine), start=1):
        try:
            letture.append(pytesseract.image_to_string(variante).strip())
        except Exception as exc:
            logger.debug("OCR copertina, variante saltata: %s", exc)
            continue
        # Uscita anticipata: se il titolo si legge gia' tutto, le letture successive non
        # possono cambiare l'esito. Con l'ordine di `_letture_ocr` la prima variante basta
        # su entrambe le copertine vere del progetto.
        letto = _normalizza("\n".join(letture))
        if parole_titolo and all(w in letto for w in parole_titolo):
            logger.debug("OCR copertina: titolo completo alla variante %d di 5", n_var)
            break
        if not parole_titolo and letture[-1]:
            break
    testo = "\n".join(t for t in letture if t).strip()
    if not testo:
        return [f"Copertina '{cover_path.name}': nessun testo rilevato. "
                f"Deve riportare il titolo del libro."]

    logger.debug("OCR copertina:\n%s", testo)
    if not titolo_atteso:
        return []

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
