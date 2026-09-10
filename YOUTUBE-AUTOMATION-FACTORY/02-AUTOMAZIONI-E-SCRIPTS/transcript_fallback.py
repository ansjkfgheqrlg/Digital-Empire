# -*- coding: utf-8 -*-
"""transcript_fallback.py — quando yt-dlp non trova sottotitoli, prova una via alternativa e
distingue nel log i due guasti possibili: strumento muto contro video davvero senza sottotitoli.

REGOLA CHE LO ORDINA: A4-RC-06 (company/Memory/studi/aitubepro/regole/A4-metodo-ai-tube/
RIPASSO_COSTRUTTIVO.py). Fonte parlata: L01-scaricare-testi/appunti.md @ 06:01 — "puo' succedere
che DownSub qualche volta non funziona".

IL BUCO CHE CHIUDE, misurato sulla fabbrica: `report L01 §2` dice testualmente "Cosa si fa se il
transcript manca: ci si ferma e si passa al candidato B. Nessuna via di riserva". La stessa cosa
succede in codice: `apex7_orchestrator._fetch_transcript()` (riga 412) prova UNA sola strada
(`--write-auto-sub`, sottotitoli automatici it/en) e se non trova nulla ritorna `None` — lo
stesso identico esito sia che yt-dlp abbia fallito per un problema di rete/strumento, sia che il
video non abbia MAI avuto sottotitoli. Senza distinguerli non si puo' nemmeno misurare quanti
buoni candidati la fabbrica sta scartando per un guasto suo, non del video.

VIA ALTERNATIVA scelta: i sottotitoli MANUALI (`--write-sub`, caricati da un umano), non solo
quelli automatici. Sono spesso assenti, ma quando ci sono sono piu' affidabili — e provarli e'
un secondo tentativo reale, non solo un retry della stessa richiesta.

QUESTO FILE E' INDIPENDENTE: non importa `apex7_orchestrator.py` (ne' lo modifica). Il parsing
del `.vtt` e' una copia locale della stessa logica di `_parse_vtt()` (riga 396), per restare
uno script che nessuno deve toccare quando l'altro cambia — coerente con "un file nuovo mai
importato da nessuno non puo' rompere niente".

NON E' ANCORA AGGANCIATO. Nessun file della catena di produzione chiama questo modulo — ADR-029,
binario B: aspetta il gate di categoria. Chi lo agganciera' trova pronta
`recupera_transcript_fallback()`, da chiamare quando la via primaria ha gia' fallito.

USO
    python transcript_fallback.py --aiuto
    python transcript_fallback.py --video-id mkaNzHTBw1M --url "https://youtube.com/watch?v=mkaNzHTBw1M" --out-dir transcripts
    python transcript_fallback.py --video-id ABC123 --url "..." --out-dir transcripts --log memory/transcript_fallback_log.jsonl
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone

if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)
    sys.stderr.reconfigure(encoding="utf-8", line_buffering=True)


def _esito(regolatore: str, passa: bool, motivo: str, **dettagli) -> dict:
    return {"regolatore": regolatore, "esito": "passa" if passa else "BLOCCO",
            "motivo": motivo, **dettagli}


# --------------------------------------------------------------------------------------
# Parsing .vtt — copia locale di apex7_orchestrator._parse_vtt, non un'importazione
# --------------------------------------------------------------------------------------
def _pulisci_vtt(percorso: str) -> str:
    """Testo parlato reale da un file .vtt: via timestamp, tag di posizione e le righe
    duplicate dell'effetto karaoke di YouTube. Stessa logica di _parse_vtt in
    apex7_orchestrator.py, copiata qui apposta per non creare una dipendenza fra i due file."""
    righe, precedente = [], None
    with open(percorso, encoding="utf-8", errors="ignore") as f:
        for raw in f:
            linea = raw.strip()
            if (not linea or "-->" in linea or linea.startswith(("WEBVTT", "Kind:", "Language:"))
                    or linea.isdigit()):
                continue
            linea = re.sub(r"<[^>]+>", "", linea).strip()
            if linea and linea != precedente:
                righe.append(linea)
                precedente = linea
    return " ".join(righe)


# --------------------------------------------------------------------------------------
# Esecuzione yt-dlp isolata in una funzione sola, cosi' i test la sostituiscono senza rete
# --------------------------------------------------------------------------------------
def _esegui_ytdlp(argomenti: list[str], timeout: int = 180) -> tuple[int | None, str, str, bool, bool]:
    """Ritorna (returncode, stdout, stderr, scaduto, non_trovato). `python -m yt_dlp`, non
    l'eseguibile CLI: stessa scelta di apex7_orchestrator.py (il pacchetto e' importabile ma il
    suo entry-point non e' sempre sul PATH)."""
    try:
        res = subprocess.run([sys.executable, "-m", "yt_dlp"] + argomenti,
                             capture_output=True, text=True, timeout=timeout)
        return res.returncode, res.stdout, res.stderr, False, False
    except subprocess.TimeoutExpired:
        return None, "", "", True, False
    except FileNotFoundError:
        return None, "", "", False, True


# --------------------------------------------------------------------------------------
# Classificazione del guasto — funzione pura, il cuore della regola A4-RC-06
# --------------------------------------------------------------------------------------
_PATTERN_STRUMENTO_MUTO = re.compile(
    r"(unable to download webpage|http error|connection (refused|reset|aborted)|"
    r"timed? ?out|http error 429|http error 403|temporary failure|network is unreachable|"
    r"ssl|certificate verify|max retries exceeded|unable to extract|"
    r"sign in to confirm|nsig extraction failed|urlopen error)",
    re.IGNORECASE,
)
_PATTERN_VIDEO_SENZA_SOTTOTITOLI = re.compile(
    r"(no subtitles? (for|available)|there.?s no subtitles|no automatic captions|"
    r"video doesn.?t have (automatic captions|subtitles))",
    re.IGNORECASE,
)


def classifica_guasto(returncode: int | None, stdout: str, stderr: str,
                      scaduto: bool = False, non_trovato: bool = False) -> dict:
    """Distingue STRUMENTO_MUTO (yt-dlp non ha fatto il suo lavoro: assente, in timeout, o
    fallito per rete/protezioni) da VIDEO_SENZA_SOTTOTITOLI (yt-dlp ha lavorato fino in fondo e
    ha confermato che non c'e' nulla da scaricare). Funzione pura: nessuna chiamata di rete,
    testabile con stringhe sintetiche."""
    testo = f"{stdout}\n{stderr}"

    if non_trovato:
        return {"guasto": "strumento_assente", "certezza": "alta",
                "dettaglio": "yt-dlp (python -m yt_dlp) non e' installato o non e' eseguibile "
                             "in questo ambiente: FileNotFoundError all'avvio del processo."}

    if scaduto:
        return {"guasto": "strumento_muto", "certezza": "media",
                "dettaglio": "yt-dlp e' andato in timeout: non si sa se il video ha sottotitoli, "
                             "lo strumento non ha risposto in tempo."}

    m = _PATTERN_STRUMENTO_MUTO.search(testo)
    if m:
        return {"guasto": "strumento_muto", "certezza": "alta",
                "dettaglio": f"yt-dlp ha fallito per un problema dello strumento/rete "
                             f"(pattern trovato: '{m.group(0)}'), non per assenza di sottotitoli."}

    if _PATTERN_VIDEO_SENZA_SOTTOTITOLI.search(testo):
        return {"guasto": "video_senza_sottotitoli", "certezza": "alta",
                "dettaglio": "yt-dlp ha completato il lavoro e ha dichiarato esplicitamente che "
                             "il video non ha sottotitoli."}

    if returncode == 0:
        return {"guasto": "video_senza_sottotitoli", "certezza": "media",
                "dettaglio": "yt-dlp e' uscito senza errori ma non ha scritto nessun file di "
                             "sottotitoli: probabile assenza reale sul video, non un guasto "
                             "dello strumento."}

    return {"guasto": "strumento_muto", "certezza": "bassa",
            "dettaglio": f"yt-dlp e' uscito con codice di errore {returncode} non riconducibile "
                         f"a un pattern noto: trattato per prudenza come guasto dello strumento "
                         f"(un video senza sottotitoli non fa fallire yt-dlp con un codice "
                         f"di errore, si limita a non scrivere file)."}


# --------------------------------------------------------------------------------------
# Via alternativa: sottotitoli manuali invece che automatici
# --------------------------------------------------------------------------------------
def recupera_transcript_fallback(video_id: str, url: str, out_dir: str,
                                 prefisso: str = "dosementale",
                                 lingue: tuple[str, ...] = ("it", "en")) -> dict:
    """Da chiamare quando la via primaria (sottotitoli AUTOMATICI, vedi
    apex7_orchestrator._fetch_transcript) ha gia' fallito. Prova i sottotitoli MANUALI
    (--write-sub) come seconda strada, e in ogni caso classifica il guasto per il log."""
    os.makedirs(out_dir, exist_ok=True)
    base = os.path.join(out_dir, f"{prefisso}-{video_id}-fallback")

    argomenti = ["--skip-download", "--write-sub", "--sub-lang", ",".join(lingue),
                "--sub-format", "vtt", "-o", base, url]
    returncode, stdout, stderr, scaduto, non_trovato = _esegui_ytdlp(argomenti)
    guasto = classifica_guasto(returncode, stdout, stderr, scaduto, non_trovato)

    trovati = [f"{base}.{lingua}.vtt" for lingua in lingue if os.path.exists(f"{base}.{lingua}.vtt")]
    if trovati:
        testo = _pulisci_vtt(trovati[0])
        return {"video_id": video_id, "esito": "trovato", "via": "sottotitoli_manuali",
               "transcript": testo, "file": trovati[0], "guasto": None}

    return {"video_id": video_id, "esito": "non_trovato", "via": "sottotitoli_manuali",
           "transcript": None, "file": None, "guasto": guasto}


# --------------------------------------------------------------------------------------
# Log — per misurare, non solo dichiarare, quanti candidati si perdono per ciascun guasto
# --------------------------------------------------------------------------------------
def registra_esito(risultato: dict, percorso_log: str) -> None:
    """Aggiunge una riga JSONL al log del fallback. Append-only: mai riscrive il log intero, per
    non perdere la storia se qualcosa si interrompe a meta'."""
    os.makedirs(os.path.dirname(os.path.abspath(percorso_log)) or ".", exist_ok=True)
    riga = {**risultato, "quando": datetime.now(timezone.utc).isoformat()}
    with open(percorso_log, "a", encoding="utf-8") as f:
        f.write(json.dumps(riga, ensure_ascii=False) + "\n")


def main() -> int:
    ap = argparse.ArgumentParser(
        add_help=False,
        description="Via di riserva quando yt-dlp non trova sottotitoli automatici: prova i "
                    "sottotitoli manuali e distingue strumento_muto da video_senza_sottotitoli. "
                    "A4-RC-06 — non ancora agganciato alla catena.",
    )
    ap.add_argument("--aiuto", "-h", action="help", help="mostra questo aiuto ed esce")
    ap.add_argument("--video-id", required=True, help="ID YouTube del video sorgente")
    ap.add_argument("--url", required=True, help="URL completo del video")
    ap.add_argument("--out-dir", required=True, help="cartella dove scrivere i .vtt (es. transcripts/)")
    ap.add_argument("--prefisso", default="dosementale", help="prefisso del canale nel nome file")
    ap.add_argument("--lingue", default="it,en", help="lingue da provare, separate da virgola")
    ap.add_argument("--log", default=None, help="percorso di un file .jsonl dove accodare l'esito")
    ap.add_argument("--json", action="store_true", help="stampa il risultato come JSON")
    args = ap.parse_args()

    lingue = tuple(l.strip() for l in args.lingue.split(",") if l.strip())
    risultato = recupera_transcript_fallback(args.video_id, args.url, args.out_dir,
                                             prefisso=args.prefisso, lingue=lingue)

    if args.log:
        registra_esito(risultato, args.log)

    if args.json:
        print(json.dumps(risultato, ensure_ascii=False, indent=2))
    elif risultato["esito"] == "trovato":
        print(f"[OK] transcript recuperato via {risultato['via']}: {risultato['file']} "
              f"({len(risultato['transcript'])} caratteri)")
    else:
        g = risultato["guasto"]
        print(f"[!] transcript non recuperato — guasto: {g['guasto']} (certezza {g['certezza']})")
        print(f"    {g['dettaglio']}")

    return 0 if risultato["esito"] == "trovato" else 1


if __name__ == "__main__":
    sys.exit(main())
