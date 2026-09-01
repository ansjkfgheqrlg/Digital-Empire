"""Carousel Factory — UN comando, un argomento, un carosello nell'Arsenale.

    python caroselli.py "<argomento>" [--prodotto Preventa] [--slide 6]

Prima di questo file il flusso esisteva ma era in pezzi: `run_content_factory.py`
apriva un browser su arena.ai e si fermava dopo aver scritto l'argomento,
poi una persona guardava `check_status.py` a mano per capire quando era finito,
eventualmente lanciava `resume_generation.py`, e infine `confirm_and_download.py`
per scaricare uno ZIP il cui nome era scritto a mano dentro il codice. Poi
scompattava a mano e scriveva a mano `copy.json`. Cinque passaggi manuali per un
carosello, piu' un login interattivo e un captcha.

Qui il flusso e' uno solo e non chiede niente a nessuno a meta' strada:

    argomento -> copy (modello via API) -> piano slide -> render locale
              -> Arsenale Caroselli/<Prodotto>/<data>_<slug>/ -> GATE

Il motore di render NON e' riscritto: si richiama `carousel-factory`
(Puppeteer + template HTML, Ramo C di CF-R5) come processo esterno, e il
generatore di copy riusa `Agents/ai_client.py` del progetto Agency via import.
Vale ADR-003: si wrappa, non si duplica.

MOTORE DI IMMAGINE (perche' locale e non Arena)
Il Ramo D (Arena, browser) resta il ramo dichiarato nella task, ma al
2026-08-25 su questa macchina e' fermo per tre motivi verificati, non
ipotizzati: `playwright_stealth` non e' installato (ogni script muore
all'import), `ArenaAI/session_data/` non esiste (serve un login Google
interattivo, ed e' gitignorato quindi non arriva col repo), e anche funzionando
richiede attesa e sorveglianza umana per ogni run. Un comando che chiede un
login e poi 15 minuti di babysitting non e' "nessun passaggio manuale nel
mezzo". Il render locale e' deterministico, gira in secondi e non ha sessioni.
Quando la sessione Arena tornera' viva, `--engine arena` e' il posto dove
agganciarla: la struttura di questo file la prevede gia'.

Exit code: 0 ok | 1 gate fallito (carosello non valido) | 2 parametri/config
errati | 3 errore di sistema.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata
from datetime import date
from pathlib import Path

# Console Windows di default e' cp1252 e crasha sulle emoji, che la caption
# contiene per forza (il prompt le chiede). Stesso bug/fix gia' noto qui
# (orchestrator_preventa.py) e nella fabbrica YouTube, CP-20260731-001.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

OK, GATE_FALLITO, CONFIG_ERRATA, ERRORE_SISTEMA = 0, 1, 2, 3

WORKFLOW_DIR = Path(__file__).resolve().parent
AGENCY_DIR = WORKFLOW_DIR / "caroselli - agency"
ARSENALE_DIR = WORKFLOW_DIR / "Arsenale Caroselli"
PRODOTTI_PATH = WORKFLOW_DIR / "caroselli_prodotti.json"
FACTORY_DIR = (WORKFLOW_DIR.parent.parent / "Workfolw crea caroselli à" / "carousel-factory")

TIPI_SLIDE = {"hook-cover", "quote-block", "list-items", "diagram", "cta-finale"}
LATO_ATTESO = 1080
PESO_MINIMO_PNG = 10 * 1024  # sotto i 10KB e' una slide vuota, non una slide


# --------------------------------------------------------------------------- #
# 1. COPY
# --------------------------------------------------------------------------- #

def _carica_prodotto(nome: str) -> dict:
    if not PRODOTTI_PATH.exists():
        raise FileNotFoundError(f"Anagrafe prodotti non trovata: {PRODOTTI_PATH}")
    anagrafe = json.loads(PRODOTTI_PATH.read_text(encoding="utf-8"))
    if nome not in anagrafe:
        disponibili = [k for k in anagrafe if not k.startswith("_")]
        raise KeyError(
            f"Prodotto '{nome}' non in anagrafe. Disponibili: {', '.join(disponibili)}. "
            f"Aggiungerne uno e' dato, non codice: una voce in {PRODOTTI_PATH.name} "
            f"+ un brand in carousel-factory/brands/."
        )
    return anagrafe[nome]


def _prompt_copy(prodotto: dict, argomento: str, n_slide: int) -> str:
    return f"""Sei il CRO Copy Architect di Digital Empire. Scrivi il copy di un carosello
Instagram di ESATTAMENTE {n_slide} slide, piu' la caption del post.

CONTESTO PRODOTTO
{prodotto['brief']}

REGOLA DI CTA
{prodotto['cta']}

TONO
{prodotto['tono']}

ARGOMENTO DI QUESTO CAROSELLO
{argomento}

REGOLE DI SCRITTURA, NON NEGOZIABILI
- "testo_grande" e' il testo fisico grande sulla slide: TUTTO MINUSCOLO, massimo 7 parole,
  frase compatta. Niente muri di testo, niente due frasi.
- "testo_accent" e' UNA sola parola presa da "testo_grande", quella su cui cade l'accento
  di colore. Deve comparire identica dentro "testo_grande".
- "testo_piccolo" e' l'occhiello sopra: massimo 6 parole, minuscolo.
- MAI lineette lunghe come i caratteri em dash o en dash, e mai il doppio trattino: si
  riscrive la frase con virgola, punto, due punti o parentesi. Sono la firma piu'
  riconoscibile del testo scritto da una macchina.
- Niente superlativi vuoti (rivoluzionario, incredibile, pazzesco): numeri e fatti concreti.

STRUTTURA
- Slide 1: tipo "hook-cover". Il pain point piu' concreto e riconoscibile.
- Slide intermedie: tipo "quote-block" per un'affermazione secca, oppure "list-items" per
  un elenco di 3 punti brevi (in quel caso riempi "items" con 3 stringhe da massimo 5
  parole ciascuna).
- Ultima slide: tipo "cta-finale", secondo la regola di CTA qui sopra.

FORMATO DI USCITA
Restituisci ESCLUSIVAMENTE un oggetto JSON valido, senza testo prima o dopo, senza
commenti, con questa forma esatta:

{{
  "titolo": "titolo breve del carosello, 3-6 parole, minuscolo",
  "caption": "caption Instagram completa con emoji e 5-8 hashtag pertinenti",
  "slides": [
    {{"numero": 1, "tipo": "hook-cover", "testo_piccolo": "...", "testo_grande": "...", "testo_accent": "..."}},
    {{"numero": 2, "tipo": "quote-block", "testo_piccolo": "...", "testo_grande": "...", "testo_accent": "..."}},
    {{"numero": {n_slide}, "tipo": "cta-finale", "testo_piccolo": "...", "testo_grande": "...", "testo_accent": "..."}}
  ]
}}"""


def _estrai_json(testo: str) -> dict:
    """Il modello incornicia spesso il JSON in un blocco markdown."""
    m = re.search(r"```(?:json)?(.*?)```", testo, re.DOTALL)
    grezzo = (m.group(1) if m else testo).strip()
    # Ultimo tentativo: prendi dalla prima graffa all'ultima.
    if not grezzo.startswith("{"):
        i, j = grezzo.find("{"), grezzo.rfind("}")
        if i != -1 and j != -1:
            grezzo = grezzo[i:j + 1]
    return json.loads(grezzo)


def genera_copy(prodotto: dict, argomento: str, n_slide: int, tentativi: int = 4) -> dict:
    """Genera il copy e lo rigenera finche' non passa i controlli.

    IL RITENTATIVO RIPORTA INDIETRO L'ERRORE (2026-08-27). La prima versione
    ritentava a freddo, rimandando lo stesso identico prompt: al secondo run
    reale il comando e' morto perche' il modello ha sforato il limite di parole
    due volte di fila e nessuno gli aveva detto in cosa aveva sbagliato. Un
    tentativo cieco non e' un tentativo, e' la stessa domanda fatta piu' forte.
    Qui l'esito del controllo torna al modello come messaggio, quindi il giro
    dopo sa esattamente quale slide correggere."""
    sys.path.insert(0, str(AGENCY_DIR))
    from Agents.ai_client import call_ai  # noqa: E402 - riuso il client Agency (ADR-003)

    prompt = _prompt_copy(prodotto, argomento, n_slide)
    conversazione = [{"role": "user", "content": prompt}]
    ultimo_errore = None

    for tentativo in range(1, tentativi + 1):
        print(f"[copy] generazione (tentativo {tentativo}/{tentativi})...")
        risposta = call_ai(conversazione, max_tokens=2000, temperature=0.8, label="copy")
        if not risposta:
            ultimo_errore = "nessuna risposta dai modelli"
            continue

        try:
            dati = _estrai_json(risposta)
            problemi = valida_copy(dati, n_slide)
        except json.JSONDecodeError as e:
            dati, problemi = None, [f"la risposta non era JSON valido: {e}"]

        if not problemi:
            return dati

        ultimo_errore = "; ".join(problemi)
        print(f"[copy] copy rifiutato: {ultimo_errore}")
        if tentativo == tentativi:
            break

        # La correzione va chiesta indicando il difetto preciso, non ripetendo
        # la richiesta iniziale. Si tiene solo l'ultimo scambio: rimandare tutta
        # la cronologia a ogni giro gonfia i token senza aggiungere niente.
        conversazione = [
            {"role": "user", "content": prompt},
            {"role": "assistant", "content": risposta[:4000]},
            {"role": "user", "content":
                "Il copy non e' stato accettato. Problemi rilevati dal controllo "
                "automatico:\n- " + "\n- ".join(problemi) +
                "\n\nRiscrivi il carosello COMPLETO correggendo esattamente questi punti e "
                "lasciando invariato il resto. Ricorda: testo_grande al massimo 7 parole, "
                "testo_accent deve essere UNA parola che compare identica dentro "
                "testo_grande. Rispondi solo con il JSON."},
        ]
        print("[copy] rimando l'errore al modello e ritento")

    raise RuntimeError(f"Copy non ottenuto dopo {tentativi} tentativi. Ultimo esito: {ultimo_errore}")


_RE_LINEETTA = re.compile(r"[—–]|--")


def valida_copy(dati: dict, n_slide: int) -> list[str]:
    """Le stesse regole che il prompt dichiara, controllate davvero.

    Un prompt che *chiede* una regola non e' una regola: e' un augurio. Qui il
    copy che non la rispetta viene rifiutato e rigenerato, prima di arrivare al
    render e quindi prima di finire in un PNG."""
    problemi: list[str] = []
    if not isinstance(dati, dict):
        return ["la risposta non e' un oggetto JSON"]
    if not (dati.get("caption") or "").strip():
        problemi.append("caption vuota")
    if not (dati.get("titolo") or "").strip():
        problemi.append("titolo vuoto")

    slides = dati.get("slides")
    if not isinstance(slides, list) or len(slides) != n_slide:
        problemi.append(f"attese {n_slide} slide, ricevute "
                        f"{len(slides) if isinstance(slides, list) else 'nessuna'}")
        return problemi

    for i, s in enumerate(slides, start=1):
        eti = f"slide {i}"
        tipo = s.get("tipo")
        if tipo not in TIPI_SLIDE:
            problemi.append(f"{eti}: tipo '{tipo}' non esiste (validi: {sorted(TIPI_SLIDE)})")
        grande = (s.get("testo_grande") or "").strip()
        if not grande:
            problemi.append(f"{eti}: testo_grande vuoto")
            continue
        if len(grande.split()) > 7:
            problemi.append(f"{eti}: testo_grande di {len(grande.split())} parole (max 7)")
        accent = (s.get("testo_accent") or "").strip()
        if accent and accent.lower() not in grande.lower():
            problemi.append(f"{eti}: testo_accent '{accent}' non compare in testo_grande")
        if s.get("tipo") == "list-items":
            items = s.get("items") or []
            if not (2 <= len(items) <= 4):
                problemi.append(f"{eti}: list-items vuole da 2 a 4 items, ricevuti {len(items)}")

    for campo in ("caption", "titolo"):
        if _RE_LINEETTA.search(dati.get(campo) or ""):
            problemi.append(f"{campo}: contiene una lineetta lunga, va riscritta la frase")
    for i, s in enumerate(slides, start=1):
        for campo in ("testo_grande", "testo_piccolo"):
            if _RE_LINEETTA.search(s.get(campo) or ""):
                problemi.append(f"slide {i} {campo}: contiene una lineetta lunga")
    return problemi


# --------------------------------------------------------------------------- #
# 2. PIANO (copy -> schema di carousel-factory)
# --------------------------------------------------------------------------- #

def slug(testo: str, massimo: int = 40) -> str:
    norm = unicodedata.normalize("NFKD", testo).encode("ascii", "ignore").decode()
    norm = re.sub(r"[^a-zA-Z0-9]+", "-", norm.lower()).strip("-")
    return norm[:massimo].strip("-") or "carosello"


def costruisci_piano(copy: dict, brand: str) -> dict:
    slides = []
    for s in copy["slides"]:
        slide = {
            "numero": int(s.get("numero") or len(slides) + 1),
            "tipo": s["tipo"],
            "testo_piccolo": (s.get("testo_piccolo") or "").strip(),
            "testo_grande": (s.get("testo_grande") or "").strip().lower(),
            "testo_accent": (s.get("testo_accent") or "").strip().lower(),
        }
        if s.get("items"):
            slide["items"] = [str(i).strip() for i in s["items"]]
        slides.append(slide)
    slides.sort(key=lambda x: x["numero"])
    for n, s in enumerate(slides, start=1):
        s["numero"] = n
    return {
        "brand": brand,
        "titolo": copy["titolo"].strip(),
        "caption": copy["caption"].strip(),
        "slides": slides,
    }


# --------------------------------------------------------------------------- #
# 3. RENDER (processo esterno, motore non toccato)
# --------------------------------------------------------------------------- #

def render(piano: dict) -> Path:
    if not FACTORY_DIR.exists():
        raise FileNotFoundError(f"Motore di render non trovato: {FACTORY_DIR}")
    if not (FACTORY_DIR / "node_modules" / "puppeteer" / "package.json").exists():
        raise RuntimeError(
            f"Le dipendenze del render non sono installate (o sono installate a meta': "
            f"un'installazione interrotta lascia node_modules/puppeteer senza package.json "
            f"e Node non lo risolve). Esegui, dentro {FACTORY_DIR}:  npm install"
        )
    brand_cfg = FACTORY_DIR / "brands" / piano["brand"] / "config.json"
    if not brand_cfg.exists():
        raise FileNotFoundError(f"Brand '{piano['brand']}' inesistente: manca {brand_cfg}")

    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False,
                                     encoding="utf-8") as f:
        json.dump(piano, f, ensure_ascii=False)
        piano_path = Path(f.name)

    try:
        print(f"[render] {len(piano['slides'])} slide, brand '{piano['brand']}'...")
        esito = subprocess.run(
            ["node", "scripts/generate.js", str(piano_path)],
            cwd=str(FACTORY_DIR), capture_output=True, text=True,
            encoding="utf-8", errors="replace", timeout=600,
        )
        print(esito.stdout.strip())
        if esito.returncode != 0:
            raise RuntimeError(f"render fallito (exit {esito.returncode}):\n{esito.stderr[-1500:]}")
        # Il motore stampa la cartella che ha creato: la leggiamo da li' invece di
        # ricostruirla, cosi' se cambia la sua regola di naming non ci disallineiamo.
        m = re.search(r"generato in:\s*(.+)", esito.stdout)
        if not m:
            raise RuntimeError("render finito ma non ha dichiarato la cartella di output")
        return Path(m.group(1).strip())
    finally:
        piano_path.unlink(missing_ok=True)


# --------------------------------------------------------------------------- #
# 4. ARSENALE
# --------------------------------------------------------------------------- #

def deposita(sorgente: Path, prodotto_nome: str, cartella_prodotto: str,
             argomento: str, piano: dict) -> Path:
    nome = f"{date.today().isoformat()}_{slug(argomento)}"
    dest = ARSENALE_DIR / cartella_prodotto / nome
    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir(parents=True)

    # Nell'Arsenale le slide si chiamano slide_01.png (schema gia' in uso nella
    # cartella Preventa del 2026-08-06), il motore le chiama slide-01.png.
    for png in sorted(sorgente.glob("slide-*.png")):
        numero = png.stem.split("-")[-1]
        shutil.copy2(png, dest / f"slide_{numero}.png")
    for html in sorted(sorgente.glob("slide-*.html")):
        shutil.copy2(html, dest / html.name)

    (dest / "caption.txt").write_text(piano["caption"], encoding="utf-8")
    (dest / "copy.json").write_text(json.dumps({
        "prodotto": prodotto_nome,
        "argomento": argomento,
        "titolo": piano["titolo"],
        "brand": piano["brand"],
        "caption": piano["caption"],
        "slides": piano["slides"],
        "generato_il": date.today().isoformat(),
        "motore": "carousel-factory (render locale, Ramo C di CF-R5)",
    }, indent=2, ensure_ascii=False), encoding="utf-8")
    return dest


# --------------------------------------------------------------------------- #
# 5. GATE
# --------------------------------------------------------------------------- #

def gate(cartella: Path, n_slide_attese: int) -> list[str]:
    """Il carosello e' valido? Controlla i file veri, non il log del render.

    Regola imparata da questo stesso motore (ArenaAI/KNOWN-ISSUES.md): un run
    puo' chiudersi senza una sola eccezione e non aver prodotto niente di buono.
    Qui si guardano numero, peso e dimensioni reali dei PNG."""
    problemi: list[str] = []
    png = sorted(cartella.glob("slide_*.png"))
    if len(png) != n_slide_attese:
        problemi.append(f"{len(png)} PNG invece di {n_slide_attese}")

    try:
        from PIL import Image
    except ImportError:
        problemi.append("VERIFICA A MANO: Pillow non installato, dimensioni non controllate")
        Image = None  # type: ignore

    for p in png:
        peso = p.stat().st_size
        if peso < PESO_MINIMO_PNG:
            problemi.append(f"{p.name}: {peso} byte, sotto il minimo di {PESO_MINIMO_PNG} "
                            f"(slide probabilmente vuota)")
        if Image is not None:
            # Un PNG troncato non deve far ESPLODERE il gate: il gate esiste
            # apposta per dire che quella slide non va bene. Se qui si lascia
            # salire l'eccezione di Pillow, il difetto che il gate doveva
            # riportare diventa un crash senza verdetto.
            try:
                with Image.open(p) as im:
                    dimensioni = im.size
            except Exception as e:
                problemi.append(f"{p.name}: non e' un'immagine leggibile ({type(e).__name__})")
                continue
            if dimensioni != (LATO_ATTESO, LATO_ATTESO):
                problemi.append(f"{p.name}: {dimensioni[0]}x{dimensioni[1]} invece di "
                                f"{LATO_ATTESO}x{LATO_ATTESO}")

    for atteso in ("copy.json", "caption.txt"):
        if not (cartella / atteso).exists():
            problemi.append(f"manca {atteso}")
    if (cartella / "caption.txt").exists() and not (cartella / "caption.txt").read_text(
            encoding="utf-8").strip():
        problemi.append("caption.txt vuoto")
    return problemi


# --------------------------------------------------------------------------- #

def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description="Un comando, un argomento, un carosello nell'Arsenale.")
    ap.add_argument("argomento", help="il topic del carosello")
    ap.add_argument("--prodotto", default="Preventa",
                    help="prodotto in caroselli_prodotti.json (default: Preventa)")
    ap.add_argument("--slide", type=int, default=6, help="numero di slide (default: 6)")
    ap.add_argument("--engine", choices=["locale", "arena"], default="locale",
                    help="motore immagini. 'arena' non e' agganciato: vedi il docstring")
    args = ap.parse_args(argv)

    if args.engine == "arena":
        print("[X] --engine arena non e' agganciato. Il Ramo D (browser su arena.ai) "
              "richiede playwright_stealth installato e una sessione autenticata in "
              "ArenaAI/session_data/, che su questa macchina non esiste. Vedi il "
              "docstring di questo file.")
        return CONFIG_ERRATA
    if not (3 <= args.slide <= 10):
        print("[X] --slide accetta da 3 a 10.")
        return CONFIG_ERRATA

    try:
        prodotto = _carica_prodotto(args.prodotto)
    except (FileNotFoundError, KeyError) as e:
        print(f"[X] {e}")
        return CONFIG_ERRATA

    try:
        copy = genera_copy(prodotto, args.argomento, args.slide)
        piano = costruisci_piano(copy, prodotto["brand"])
        print(f"[copy] '{piano['titolo']}' — {len(piano['slides'])} slide")
        for s in piano["slides"]:
            print(f"       {s['numero']}. [{s['tipo']}] {s['testo_grande']}")
        sorgente = render(piano)
        cartella = deposita(sorgente, args.prodotto, prodotto["cartella_arsenale"],
                            args.argomento, piano)
    except Exception as e:
        print(f"[X] {type(e).__name__}: {e}")
        return ERRORE_SISTEMA

    problemi = gate(cartella, args.slide)
    print(f"\n[gate] {cartella}")
    if problemi:
        print("[gate] CAROSELLO NON VALIDO:")
        for p in problemi:
            print(f"       - {p}")
        return GATE_FALLITO
    print(f"[gate] OK: {args.slide} slide {LATO_ATTESO}x{LATO_ATTESO}, copy.json e caption presenti.")
    return OK


if __name__ == "__main__":
    sys.exit(main())
