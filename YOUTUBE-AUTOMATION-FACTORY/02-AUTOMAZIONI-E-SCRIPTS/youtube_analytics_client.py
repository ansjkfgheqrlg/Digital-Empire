#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Regola che ordina questo script: A4-RC-15
(company/Memory/studi/aitubepro/regole/A4-metodo-ai-tube/RIPASSO_COSTRUTTIVO.py).

Buco che chiude, misurato sulla fabbrica: 03-AGENTI-E-RUOLI/operatori/channel-performance-
analyst.md dichiara "CTR, retention e ricavi richiedono YouTube Studio, che e' privato" e
scrive sempre `null` in memory/performance_logs.json, usando solo scraping pubblico
(youtube_hunter_playwright.py). Ma il canale e' di proprieta' Digital Empire e la YouTube
Analytics API — autenticata via OAuth sullo stesso canale — espone la retention curve reale
(audienceWatchRatio per elapsedVideoTimeRatio). Non e' un limite fisico, e' un flusso mai
costruito.

NON E' ANCORA AGGANCIATO: nessun file esistente (channel-performance-analyst.md,
apex7_orchestrator.py, fliki_client.py, build_candidate_pool.py,
youtube_uploader_playwright.py) importa o chiama questo script. Sostituire i `null` in
performance_logs.json e' una decisione del gate di categoria (ADR-029), non di questo file.

CREDENZIALI — MAI nel codice o nel repository. Questo repo E' stato pubblico con segreti in
chiaro (company/Memory/BACKLOG.md B-020/B-021/B-023: API key Brevo, password Arena/Instagram
committate e mai piu' davvero al sicuro anche dopo la rimozione, perche' la storia git
pubblica resta leggibile). Questo client legge le credenziali SOLO da:
  1) variabili d'ambiente dirette — YT_ANALYTICS_CLIENT_ID, YT_ANALYTICS_CLIENT_SECRET,
     YT_ANALYTICS_REFRESH_TOKEN (consigliato: nessun file di credenziali su disco), oppure
  2) un file di token JSON FUORI da questo repository, il cui percorso sta nella variabile
     d'ambiente YT_ANALYTICS_TOKEN_FILE (rifiutato esplicitamente se il percorso ricade
     dentro l'albero del repository).
Se nessuna delle due e' disponibile, lo dichiara e si ferma. Non inventa un login
interattivo silenzioso, non salva nulla di suo pugno, non stampa mai il valore dei segreti.

Uso da riga di comando:
  python youtube_analytics_client.py --aiuto
  python youtube_analytics_client.py --video-id dQw4w9WgXcQ

Uso come libreria:
  from youtube_analytics_client import carica_credenziali, costruisci_curva_retention
  creds = carica_credenziali()
  dati = costruisci_curva_retention("dQw4w9WgXcQ", creds)
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys

if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)
    sys.stderr.reconfigure(encoding="utf-8", line_buffering=True)

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
# .../YOUTUBE-AUTOMATION-FACTORY/02-AUTOMAZIONI-E-SCRIPTS -> risale a due livelli -> radice repo
REPO_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", ".."))

SCOPES = [
    "https://www.googleapis.com/auth/yt-analytics.readonly",
    "https://www.googleapis.com/auth/youtube.readonly",
]


class CredenzialiMancanti(RuntimeError):
    """Sollevata quando non esiste nessuna credenziale utilizzabile, ne' in ambiente ne' in un file esterno al repo."""


def _percorso_dentro_repo(percorso: str) -> bool:
    """True se `percorso` ricade dentro la radice del repository (stessa unita' disco)."""
    try:
        assoluto = os.path.abspath(percorso)
        return os.path.commonpath([assoluto, REPO_ROOT]) == REPO_ROOT
    except ValueError:
        # unita' disco diverse su Windows (es. C:\ contro D:\): sicuramente fuori dal repo
        return False


def carica_credenziali():
    """
    Carica le credenziali OAuth per la YouTube Analytics/Data API SOLO da ambiente o da un
    file esterno al repository. Non stampa mai il valore dei segreti. Solleva
    CredenzialiMancanti con un messaggio operativo se non trova nulla di utilizzabile.
    """
    try:
        from google.oauth2.credentials import Credentials
        from google.auth.transport.requests import Request
    except ImportError as e:
        raise CredenzialiMancanti(
            "Librerie Google mancanti: pip install google-auth google-auth-oauthlib "
            "google-api-python-client. Impossibile autenticarsi senza."
        ) from e

    client_id = os.environ.get("YT_ANALYTICS_CLIENT_ID")
    client_secret = os.environ.get("YT_ANALYTICS_CLIENT_SECRET")
    refresh_token = os.environ.get("YT_ANALYTICS_REFRESH_TOKEN")

    if client_id and client_secret and refresh_token:
        creds = Credentials(
            token=None,
            refresh_token=refresh_token,
            client_id=client_id,
            client_secret=client_secret,
            token_uri="https://oauth2.googleapis.com/token",
            scopes=SCOPES,
        )
        creds.refresh(Request())
        return creds

    token_file = os.environ.get("YT_ANALYTICS_TOKEN_FILE")
    if token_file:
        if _percorso_dentro_repo(token_file):
            raise CredenzialiMancanti(
                f"YT_ANALYTICS_TOKEN_FILE punta dentro il repository ({token_file}). Rifiutato: "
                "un file di credenziali qui dentro finisce facilmente in un commit (gia' successo, "
                "vedi company/Memory/BACKLOG.md B-020/B-021/B-023). Spostalo fuori dal repo e "
                "aggiorna la variabile d'ambiente."
            )
        if not os.path.isfile(token_file):
            raise CredenzialiMancanti(f"YT_ANALYTICS_TOKEN_FILE indica un file inesistente: {token_file}")
        creds = Credentials.from_authorized_user_file(token_file, SCOPES)
        if creds.expired and creds.refresh_token:
            creds.refresh(Request())
        return creds

    raise CredenzialiMancanti(
        "Nessuna credenziale trovata. Imposta YT_ANALYTICS_CLIENT_ID + YT_ANALYTICS_CLIENT_SECRET "
        "+ YT_ANALYTICS_REFRESH_TOKEN nell'ambiente, oppure YT_ANALYTICS_TOKEN_FILE con un "
        "percorso FUORI da questo repository. Nessuna credenziale viene mai letta da un file "
        "dentro il repo. Mi fermo qui."
    )


def _durata_iso8601_a_secondi(durata_iso: str) -> float:
    """Converte una durata ISO8601 (es. 'PT4M13S') in secondi, senza dipendenze esterne."""
    m = re.match(r"^PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?$", durata_iso or "")
    if not m:
        return 0.0
    ore, minuti, secondi = (int(x) if x else 0 for x in m.groups())
    return float(ore * 3600 + minuti * 60 + secondi)


def estrai_punto_30s(righe: list, durata_secondi: float, secondo_target: float = 30.0) -> dict | None:
    """
    Isola, dalla retention curve, il punto piu' vicino a `secondo_target` secondi.

    `righe`: lista di coppie [elapsedVideoTimeRatio, audienceWatchRatio] come restituite da
    youtubeAnalytics.reports().query(dimensions="elapsedVideoTimeRatio",
    metrics="audienceWatchRatio"). Ritorna None se non c'e' materiale per calcolarlo.
    """
    if not righe or not durata_secondi or durata_secondi <= 0:
        return None
    ratio_target = min(1.0, secondo_target / durata_secondi)
    migliore = min(righe, key=lambda r: abs(float(r[0]) - ratio_target))
    return {
        "elapsed_video_time_ratio": float(migliore[0]),
        "audience_watch_ratio": float(migliore[1]),
        "secondo_stimato": round(float(migliore[0]) * durata_secondi, 1),
    }


def costruisci_curva_retention(video_id: str, credenziali, secondo_target: float = 30.0) -> dict:
    """
    Interroga la YouTube Data API (per la durata) e la YouTube Analytics API (per
    audienceWatchRatio) sul canale autenticato, e ritorna la curva completa piu' il punto
    isolato a `secondo_target` secondi (default 30, il punto che L14 dell'A4 dichiara
    decisivo per la ritenzione).
    """
    from googleapiclient.discovery import build

    youtube = build("youtube", "v3", credentials=credenziali)
    risposta_video = youtube.videos().list(part="contentDetails", id=video_id).execute()
    items = risposta_video.get("items", [])
    if not items:
        raise ValueError(f"Video {video_id} non trovato sul canale autenticato.")
    durata_iso = items[0]["contentDetails"]["duration"]
    durata_secondi = _durata_iso8601_a_secondi(durata_iso)

    analytics = build("youtubeAnalytics", "v2", credentials=credenziali)
    risposta = analytics.reports().query(
        ids="channel==MINE",
        startDate="2000-01-01",
        endDate="2100-01-01",
        metrics="audienceWatchRatio",
        dimensions="elapsedVideoTimeRatio",
        filters=f"video=={video_id}",
        sort="elapsedVideoTimeRatio",
    ).execute()
    righe = risposta.get("rows", [])

    punto_target = estrai_punto_30s(righe, durata_secondi, secondo_target)

    return {
        "video_id": video_id,
        "durata_secondi": durata_secondi,
        "punto_30s": punto_target,
        "curva": [{"elapsed_video_time_ratio": float(r[0]), "audience_watch_ratio": float(r[1])} for r in righe],
        "n_punti": len(righe),
    }


def main():
    parser = argparse.ArgumentParser(
        prog="youtube_analytics_client.py",
        description=(
            "Scarica la retention curve reale (audienceWatchRatio) di un video del canale via "
            "YouTube Analytics API (A4-RC-15). Richiede credenziali OAuth in ambiente o in un "
            "file esterno al repository."
        ),
        add_help=False,
    )
    parser.add_argument("-h", "--help", "--aiuto", action="help", help="mostra questo messaggio ed esce")
    parser.add_argument("--video-id", required=True)
    parser.add_argument("--secondo-target", type=float, default=30.0, dest="secondo_target")
    parser.add_argument("--out", default=None, help="file JSON di output (default: stampa su stdout)")
    args = parser.parse_args()

    try:
        creds = carica_credenziali()
        risultato = costruisci_curva_retention(args.video_id, creds, secondo_target=args.secondo_target)
    except CredenzialiMancanti as e:
        print(f"[STOP] {e}")
        sys.exit(1)
    except Exception as e:
        print(f"[STOP] Errore chiamando le API YouTube: {e}")
        sys.exit(1)

    testo = json.dumps(risultato, ensure_ascii=False, indent=2)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(testo)
        print(f"[OK] scritto {args.out}")
    else:
        print(testo)


if __name__ == "__main__":
    main()
