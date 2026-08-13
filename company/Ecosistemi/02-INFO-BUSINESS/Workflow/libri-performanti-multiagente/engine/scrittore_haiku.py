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
"""
from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

from . import config

MODELLO = "haiku"          # scelta vincolante di Gael, non cambiare senza dirglielo
TIMEOUT_CAPITOLO_S = 600   # un capitolo lungo puo' richiedere qualche minuto
PAROLE_MINIME_CAPITOLO = 800   # sotto questa soglia il capitolo non e' utilizzabile


class ClaudeNonDisponibile(RuntimeError):
    """Il CLI di Claude Code non e' installato o non e' autenticato."""


def _eseguibile() -> str:
    """Trova il CLI. Su Windows npm installa `claude.cmd`, che `shutil.which` trova solo
    se la shell ha la cartella npm nel PATH: si controllano anche i percorsi standard."""
    trovato = shutil.which("claude") or shutil.which("claude.cmd")
    if trovato:
        return trovato
    import os
    for candidato in (
        Path(os.environ.get("APPDATA", "")) / "npm" / "claude.cmd",
        Path(os.environ.get("APPDATA", "")) / "npm" / "claude",
        Path(os.environ.get("LOCALAPPDATA", "")) / "Programs" / "claude" / "claude.exe",
    ):
        if candidato.exists():
            return str(candidato)
    raise ClaudeNonDisponibile(
        "CLI di Claude Code non trovato. Installalo con:\n"
        "  npm install -g @anthropic-ai/claude-code\n"
        "poi autenticalo lanciando `claude` una volta e seguendo il login."
    )


def genera(prompt: str, timeout_s: int = TIMEOUT_CAPITOLO_S) -> str:
    """Una chiamata a Claude Code con Haiku. Ritorna il testo prodotto."""
    esito = subprocess.run(
        [_eseguibile(), "-p", prompt, "--model", MODELLO],
        capture_output=True, text=True, timeout=timeout_s,
        cwd=str(config.WORKFLOW_DIR), encoding="utf-8", errors="replace",
    )
    if esito.returncode != 0:
        errore = (esito.stderr or "").strip()[:400]
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
