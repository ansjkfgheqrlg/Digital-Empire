"""
STEP 2 del workflow — scrittura del libro con Claude Code, modello HAIKU (2026-08-12).

Scelta di Gael, esplicita: il testo si scrive con **Haiku**, non Sonnet, non Opus, non
Fable. Il motivo e' economico e va detto chiaro: l'obiettivo del catalogo e' il VOLUME —
tanti titoli che vendono — e Haiku costa una frazione degli altri modelli. Su 24 capitoli
per libro e molti libri, la differenza di costo e' l'intero margine.

COME FUNZIONA: si invoca il CLI di Claude Code in modalita' non interattiva
(`claude -p "<prompt>" --model haiku`), che usa i crediti del piano gia' pagato invece di
una API key separata. Ogni capitolo e' una chiamata indipendente: il contesto necessario
(outline + riassunto dei capitoli precedenti) viaggia nel prompt, non nella memoria di una
sessione — cosi' un capitolo che fallisce si rilancia da solo senza rifare gli altri.

DIFESE, tutte nate da problemi REALI gia' incontrati su questo progetto:
- capitolo troppo corto o vuoto -> si rigenera, non si accetta;
- capitolo identico al precedente -> si rigenera (bug realmente visto: 3 capitoli uguali);
- CLI assente o non autenticato -> errore che dice esattamente cosa fare, mai un fallimento
  oscuro a meta' libro.

I TRE DIFETTI TROVATI AL PRIMO GIRO END-TO-END (2026-08-13), tutti corretti qui:

1. **MAI passare da `claude.CMD`** (2026-08-13, il piu' grave). Il CLI installato da npm su
   Windows e' un wrapper batch che rilancia l'eseguibile con `%*`. Un argomento che contiene
   A CAPO viene troncato da cmd.exe alla PRIMA RIGA, e gli argomenti successivi spariscono.
   Misurato con una sonda su argv, stesso prompt di 11 righe:
       via .CMD  -> ARGC=2, prompt = solo 'Sei uno scrittore di narrativa di genere.'
       via .exe  -> ARGC=4, prompt intero, --model haiku presente
   Due conseguenze, entrambe viste in produzione: il modello riceveva solo la riga del ruolo
   e rispondeva "il tuo messaggio imposta il ruolo ma non il task"; e **`--model haiku` non
   arrivava**, quindi si pagava il modello di default. Cioe' l'esatto contrario della scelta
   di Gael, in silenzio. Tutti i prompt di questo modulo sono multiriga: si chiama SEMPRE
   l'eseguibile nativo.

2. **cwd fuori dal repo.** `claude` e' un agente, non un generatore di testo: dalla cartella
   di lavoro risale l'albero e carica i `CLAUDE.md` che trova. Lanciato dentro il progetto
   caricava le regole di Digital Empire, leggeva lo stato del disco e rispondeva da assistente
   ("riprendo The Ninth Winter o ne apro uno nuovo?"). Si lancia da una cartella neutra fuori
   dall'albero, con un system prompt proprio e i tool negati.

3. **stdin chiuso.** Senza, il CLI aspetta 3 secondi di stdin a ogni chiamata e stampa un
   warning: su 25 chiamate per libro e' piu' di un minuto buttato per niente.
"""
from __future__ import annotations

import os
import shutil
import subprocess
import tempfile
from pathlib import Path

from . import config

MODELLO = "haiku"          # scelta vincolante di Gael, non cambiare senza dirglielo
TIMEOUT_CAPITOLO_S = 600   # un capitolo lungo puo' richiedere qualche minuto
PAROLE_MINIME_CAPITOLO = 800   # sotto questa soglia il capitolo non e' utilizzabile

# Il CLI e' un AGENTE: senza un system prompt proprio si comporta da assistente e fa
# domande invece di scrivere. Questo lo riduce a generatore di testo.
SYSTEM_PROMPT = (
    "You are a professional genre-fiction ghostwriter. You output only the requested "
    "creative text, in the exact format requested. You never ask questions, never add "
    "commentary, never mention files, projects or tools, and never use tools."
)

# Negati esplicitamente: il modulo genera prosa, non deve poter toccare il disco.
TOOL_NEGATI = "Bash Read Write Edit Glob Grep WebFetch WebSearch Task TodoWrite NotebookEdit"


class ClaudeNonDisponibile(RuntimeError):
    """Il CLI di Claude Code non e' installato o non e' autenticato."""


class LimiteSpesaRaggiunto(RuntimeError):
    """Il piano ha esaurito il budget: nessun capitolo si puo' scrivere finche' non si alza."""


def _cartella_neutra() -> Path:
    """Una cartella di lavoro FUORI dall'albero del repo (vedi punto 2 del docstring).

    Serve perche' `claude` risale l'albero dalla cwd e carica i CLAUDE.md che trova: lanciato
    dentro il progetto si mette a fare l'assistente di Digital Empire invece di scrivere."""
    d = Path(tempfile.gettempdir()) / "kdp_scrittore_cwd"
    d.mkdir(parents=True, exist_ok=True)
    return d


def _eseguibile() -> str:
    """Trova l'ESEGUIBILE NATIVO del CLI, mai il wrapper `.cmd`/`.bat`.

    Il wrapper batch tronca alla prima riga qualunque argomento contenga un a capo e perde
    quelli successivi (punto 1 del docstring, misurato): siccome ogni prompt di questo modulo
    e' multiriga, passare di li' significa mandare un prompt mutilato SENZA `--model haiku`
    e non accorgersene, perche' il CLI risponde comunque con successo."""
    candidati = [
        Path(os.environ.get("APPDATA", "")) / "npm" / "node_modules" / "@anthropic-ai"
        / "claude-code" / "bin" / "claude.exe",
        Path(os.environ.get("LOCALAPPDATA", "")) / "Programs" / "claude" / "claude.exe",
    ]
    trovato = shutil.which("claude")
    if trovato and Path(trovato).suffix.lower() not in (".cmd", ".bat"):
        candidati.insert(0, Path(trovato))

    for c in candidati:
        if c.exists():
            return str(c)

    # Su Windows `which` trova quasi sempre solo il wrapper: se esiste, l'eseguibile nativo
    # e' accanto ad esso e va cercato li' invece di arrendersi.
    wrapper = shutil.which("claude.cmd") or shutil.which("claude")
    if wrapper:
        accanto = (Path(wrapper).parent / "node_modules" / "@anthropic-ai" / "claude-code"
                   / "bin" / "claude.exe")
        if accanto.exists():
            return str(accanto)
        raise ClaudeNonDisponibile(
            f"Trovato solo il wrapper batch ({wrapper}) e non l'eseguibile nativo accanto.\n"
            f"Il wrapper NON e' utilizzabile: tronca i prompt multiriga alla prima riga e "
            f"perde --model, quindi scriverebbe libri sbagliati pagando il modello sbagliato.\n"
            f"Reinstalla con:  npm install -g @anthropic-ai/claude-code --include=optional"
        )

    raise ClaudeNonDisponibile(
        "CLI di Claude Code non trovato. Installalo con:\n"
        "  npm install -g @anthropic-ai/claude-code --include=optional\n"
        "poi autenticalo lanciando `claude` una volta e seguendo il login."
    )


def genera(prompt: str, timeout_s: int = TIMEOUT_CAPITOLO_S) -> str:
    """Una chiamata a Claude Code con Haiku. Ritorna il testo prodotto."""
    esito = subprocess.run(
        [_eseguibile(), "-p", prompt,
         "--model", MODELLO,
         "--system-prompt", SYSTEM_PROMPT,
         "--disallowed-tools", TOOL_NEGATI],
        capture_output=True, text=True, timeout=timeout_s,
        cwd=str(_cartella_neutra()),          # mai dentro il repo: caricherebbe i CLAUDE.md
        stdin=subprocess.DEVNULL,             # senza, aspetta 3s di stdin a ogni chiamata
        encoding="utf-8", errors="replace",
    )
    uscita = ((esito.stdout or "") + "\n" + (esito.stderr or "")).strip()

    # Il limite di spesa arriva come messaggio normale, non come errore di autenticazione:
    # senza questo controllo un libro intero fallirebbe capitolo per capitolo con 24
    # messaggi oscuri invece di uno chiaro.
    if "spend limit" in uscita.lower() or "limite di spesa" in uscita.lower():
        raise LimiteSpesaRaggiunto(
            "Il piano Claude ha raggiunto il limite di spesa mensile: nessun capitolo puo' "
            "essere scritto finche' non viene alzato su claude.ai/settings/usage. "
            f"Messaggio del CLI: {uscita[:200]}"
        )

    if esito.returncode != 0:
        errore = (esito.stderr or "").strip()[:400] or uscita[:400]
        if "auth" in errore.lower() or "login" in errore.lower():
            raise ClaudeNonDisponibile(
                f"Claude Code non e' autenticato. Lancia `claude` da terminale una volta "
                f"e completa il login, poi rilancia. Dettaglio: {errore}"
            )
        raise RuntimeError(f"Claude Code ha risposto con errore {esito.returncode}: {errore}")

    testo = (esito.stdout or "").strip()
    if not testo:
        raise RuntimeError("Claude Code non ha restituito testo.")
    return testo


# --------------------------------------------------------------------------- #
# Prompt
# --------------------------------------------------------------------------- #

def prompt_outline(nicchia: str, titolo: str, competitor: list[str]) -> str:
    riferimenti = "\n".join(f"- {t}" for t in competitor[:5]) or "- (nessuno)"
    return f"""Sei uno scrittore di narrativa di genere per il mercato Amazon KDP.

Genere/nicchia: {nicchia}
Titolo del libro: {titolo}

Libri di successo nella stessa nicchia (per capire cosa cerca il lettore — NON copiarli,
il testo deve essere completamente originale):
{riferimenti}

Scrivi l'IMPIANTO del romanzo, in inglese, in questo formato esatto:

TITLE: <titolo definitivo, commerciale, chiaro sul genere>
CHARACTERS: <4-5 personaggi, uno per riga: nome, età, ruolo nella storia>
ACT1: <impianto, 3-4 frasi>
ACT2: <sviluppo e complicazione, 3-4 frasi>
ACT3: <risoluzione, incluso il colpo di scena finale, 3-4 frasi>
CHAPTERS:
1. <cosa succede nel capitolo 1, una riga>
2. <...>
(fino a 24)

Regole: nessuna violenza esplicita, nessun contenuto sessuale esplicito. Ogni capitolo
deve chiudere su un gancio che spinge a leggere il successivo. Rispondi SOLO con il
formato sopra, senza commenti."""


def prompt_capitolo(titolo: str, nicchia: str, outline: str, numero: int,
                     totale: int, riassunto: str, parole: int) -> str:
    continuita = (f"Riassunto di quanto accaduto finora:\n{riassunto}"
                  if riassunto else
                  "Questo e' il PRIMO capitolo: presenta ambientazione e personaggi.")
    return f"""Stai scrivendo il romanzo "{titolo}" (genere: {nicchia}), in inglese.

IMPIANTO DEL LIBRO:
{outline}

{continuita}

Scrivi il CAPITOLO {numero} di {totale}, di circa {parole} parole.

Regole vincolanti:
- Comincia con una riga "# <titolo del capitolo>", poi il testo in paragrafi separati da
  riga vuota.
- Solo prosa narrativa: niente riassunti, niente commenti, niente note.
- Coerente con personaggi e trama dell'impianto.
- Chiudi il capitolo su un gancio.
- Nessuna violenza esplicita, nessun contenuto sessuale esplicito.
- NON ripetere scene o frasi dei capitoli precedenti.

Dopo il testo del capitolo, aggiungi una riga esattamente cosi':
---RIASSUNTO---
seguita da 2-3 frasi che riassumono cosa e' successo in QUESTO capitolo."""


# --------------------------------------------------------------------------- #
# Scrittura
# --------------------------------------------------------------------------- #

def _dividi_capitolo_e_riassunto(testo: str) -> tuple[str, str]:
    if "---RIASSUNTO---" not in testo:
        raise ValueError("risposta senza marcatore ---RIASSUNTO---")
    corpo, _, riassunto = testo.partition("---RIASSUNTO---")
    corpo, riassunto = corpo.strip(), riassunto.strip()
    if not corpo or not riassunto:
        raise ValueError("capitolo o riassunto vuoto")
    return corpo, riassunto


def scrivi_capitolo(titolo: str, nicchia: str, outline: str, numero: int, totale: int,
                     riassunto: str, parole: int, gia_scritti: list[str],
                     tentativi: int = 3) -> tuple[str, str]:
    """Genera un capitolo, riprovando se torna corto, malformato o uguale a uno precedente."""
    ultimo_errore = ""
    for tentativo in range(1, tentativi + 1):
        testo = genera(prompt_capitolo(titolo, nicchia, outline, numero, totale, riassunto, parole))
        try:
            corpo, nuovo_riassunto = _dividi_capitolo_e_riassunto(testo)
        except ValueError as e:
            ultimo_errore = str(e)
            print(f"  [cap {numero}] tentativo {tentativo}: {e} — rigenero")
            continue

        n_parole = len(corpo.split())
        if n_parole < PAROLE_MINIME_CAPITOLO:
            ultimo_errore = f"troppo corto ({n_parole} parole)"
            print(f"  [cap {numero}] tentativo {tentativo}: {ultimo_errore} — rigenero")
            continue

        normalizzato = " ".join(corpo.split()).lower()
        if any(normalizzato == " ".join(p.split()).lower() for p in gia_scritti):
            ultimo_errore = "identico a un capitolo precedente"
            print(f"  [cap {numero}] tentativo {tentativo}: {ultimo_errore} — rigenero")
            continue

        return corpo, nuovo_riassunto

    raise RuntimeError(f"Capitolo {numero} non riuscito dopo {tentativi} tentativi: {ultimo_errore}")
