# -*- coding: utf-8 -*-
"""audio_level_check.py — misura il livello audio VERO di un MP4 con ffmpeg, non a orecchio.

REGOLA CHE LO ORDINA: A4-RC-11 (company/Memory/studi/aitubepro/regole/A4-metodo-ai-tube/
RIPASSO_COSTRUTTIVO.py). Il livello audio si misura in dB sul file esportato, non si "ascolta".

IL BUCO CHE CHIUDE, misurato il 2026-09-06 (qa-audio-video.md §4): il gate di QA ordina ad un
agente "Controlla il video tramite l'anteprima" e "Ascolto obbligatorio ad alta fedelta'" — un
metro senza righello, chiesto a un agente che non ha orecchie. `regolatori.verifica_qualita`
(regolatori.py:274) misura durata/risoluzione/codec con ffprobe, MAI il contenuto della traccia
audio: cercati `volumedetect`, `loudnorm`, `mean_volume` in tutta `02-AUTOMAZIONI-E-SCRIPTS/`
prima di scrivere questo file — zero occorrenze.

DUE SOGLIE, dichiarate separatamente perche' la fabbrica le conosce diversamente:
  - MUSICA: oggi i video NON hanno musica (qa-audio-video.md §10, accertato il 2026-09-06:
    nessun campo `backgroundMusic`/`musicId`/`audioTrack` nel payload di fliki_client.py, e
    Fliki non la aggiunge da solo). Il tetto per quando tornera' e' dichiarato nello studio
    (A4-L08-02, lezione L08 @ 44:39-45:06): **-35 dB**. Lo uso qui come default per
    `--tetto-musica`, MAI inventato.
  - VOCE: la fascia NON si inventa. La regola A4-RC-11 dice esplicitamente "da tarare sul primo
    campione reale": questo script la lascia PARAMETRICA (`--fascia-voce MIN MAX`) e, se non
    dichiarata, si limita a MISURARE e riportare senza dare un verdetto passa/BLOCCO sulla voce.

NON E' ANCORA AGGANCIATO. Nessun file della catena di produzione (fliki_client.py,
apex7_orchestrator.py, quality_gate.py, regolatori.py) importa questo modulo — ADR-029, binario
B: aspetta il gate di categoria. Chi lo agganciera' trova pronte `misura_livello()` (misura pura,
via ffmpeg -af volumedetect) e `valuta_livello()` (misura + soglie -> verdetto).

USO
    python audio_level_check.py --aiuto
    python audio_level_check.py --file video.mp4
    python audio_level_check.py --file video.mp4 --fascia-voce -30 -12
    python audio_level_check.py --file video.mp4 --tetto-musica -35
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys

if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)
    sys.stderr.reconfigure(encoding="utf-8", line_buffering=True)


def _esito(regolatore: str, passa: bool, motivo: str, **dettagli) -> dict:
    return {"regolatore": regolatore, "esito": "passa" if passa else "BLOCCO",
            "motivo": motivo, **dettagli}


TETTO_MUSICA_DB_DEFAULT = -35.0  # A4-L08-02: chiuso a -35 dB nella lezione, "ancora troppo alta" a -25.

_MEAN_RE = re.compile(r"mean_volume:\s*(-?\d+(?:\.\d+)?)\s*dB")
_MAX_RE = re.compile(r"max_volume:\s*(-?\d+(?:\.\d+)?)\s*dB")


def misura_livello(percorso_media: str, timeout: int = 60) -> dict:
    """Misura pura: livello medio e di picco (dB) dell'audio del file, via ffmpeg volumedetect.
    Non decide nulla, non applica soglie — ritorna {disponibile, mean_db, max_db} o
    {disponibile: False, errore: ...} se la dipendenza esterna manca o il file non c'e'."""
    if not shutil.which("ffmpeg"):
        return {"disponibile": False, "errore": "ffmpeg non trovato sul PATH: impossibile misurare l'audio."}
    if not percorso_media or not os.path.exists(percorso_media):
        return {"disponibile": False, "errore": f"file inesistente: {percorso_media}"}

    cmd = ["ffmpeg", "-i", percorso_media, "-af", "volumedetect",
           "-vn", "-sn", "-dn", "-f", "null", "-"]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        return {"disponibile": False, "errore": f"ffmpeg oltre il timeout di {timeout}s."}

    # volumedetect scrive le statistiche su stderr, non su stdout: e' il comportamento normale
    # di ffmpeg per i log, non un errore.
    output = res.stderr or ""
    mean_m = _MEAN_RE.search(output)
    max_m = _MAX_RE.search(output)
    if not mean_m or not max_m:
        return {"disponibile": False,
                "errore": "volumedetect non ha prodotto risultati (nessuna traccia audio nel file?).",
                "output_ffmpeg": output[-800:]}

    return {"disponibile": True, "mean_db": float(mean_m.group(1)), "max_db": float(max_m.group(1))}


def valuta_livello(misura: dict, fascia_voce: tuple[float, float] | None = None,
                   tetto_musica_db: float | None = None) -> dict:
    """Applica soglie dichiarate a una misura gia' fatta da `misura_livello()`.

    `fascia_voce`: (min_db, max_db) — se None, la voce viene solo misurata e riportata, mai
    giudicata (nessun numero inventato, A4-RC-11).
    `tetto_musica_db`: se dato, il picco non deve superarlo (oggi il campo non si applica: i
    nostri video non hanno musica, vedi docstring del modulo)."""
    if not misura.get("disponibile"):
        return _esito("audio-level-check", False,
                     misura.get("errore", "misura audio non disponibile."))

    problemi, note = [], []
    if fascia_voce is not None:
        lo, hi = fascia_voce
        if not (lo <= misura["mean_db"] <= hi):
            problemi.append(
                f"livello medio voce {misura['mean_db']} dB fuori dalla fascia dichiarata "
                f"[{lo}, {hi}] dB")
    else:
        note.append("fascia voce non dichiarata a riga di comando: nessuna soglia applicata, "
                     "solo misura (A4-RC-11 — 'da tarare sul primo campione reale', non un "
                     "numero inventato qui).")

    if tetto_musica_db is not None:
        if misura["max_db"] > tetto_musica_db:
            problemi.append(
                f"picco {misura['max_db']} dB sopra il tetto musica {tetto_musica_db} dB "
                f"(A4-L08-02)")
    else:
        note.append("tetto musica non verificato: i video di questa fabbrica non hanno una "
                     "traccia musicale (qa-audio-video.md §10). Passa --tetto-musica per attivare.")

    if problemi:
        return _esito("audio-level-check", False, "Livello audio fuori dalle soglie dichiarate.",
                      problemi=problemi, misure=misura, note=note)
    return _esito("audio-level-check", True,
                 "Livello audio dentro le soglie dichiarate (o nessuna soglia dichiarata: solo "
                 "misura riportata).",
                 misure=misura, note=note)


# --------------------------------------------------------------------------------------
def main() -> int:
    ap = argparse.ArgumentParser(
        add_help=False,
        description="Misura livello medio/di picco dell'audio di un MP4 con ffmpeg e lo "
                    "confronta a una soglia dichiarata. A4-RC-11 — non ancora agganciato al gate.",
    )
    ap.add_argument("--aiuto", "-h", action="help", help="mostra questo aiuto ed esce")
    ap.add_argument("--file", required=True, help="percorso del file MP4/audio da misurare")
    ap.add_argument("--fascia-voce", nargs=2, type=float, default=None, metavar=("MIN_DB", "MAX_DB"),
                    help="fascia dichiarata per il livello medio della voce, es. -30 -12")
    ap.add_argument("--tetto-musica", nargs="?", type=float, const=TETTO_MUSICA_DB_DEFAULT, default=None,
                    help=f"attiva il controllo picco musica; senza valore usa il default "
                         f"{TETTO_MUSICA_DB_DEFAULT} dB (A4-L08-02)")
    ap.add_argument("--json", action="store_true", help="stampa il risultato come JSON")
    args = ap.parse_args()

    misura = misura_livello(args.file)
    fascia_voce = tuple(args.fascia_voce) if args.fascia_voce else None
    risultato = valuta_livello(misura, fascia_voce=fascia_voce, tetto_musica_db=args.tetto_musica)

    if args.json:
        print(json.dumps(risultato, ensure_ascii=False, indent=2))
    else:
        simbolo = "[OK]" if risultato["esito"] == "passa" else "[BLOCCO]"
        print(f"{simbolo} {risultato['regolatore']} — {risultato['motivo']}")
        if "misure" in risultato:
            print(f"      misure: {risultato['misure']}")
        for p in risultato.get("problemi", []):
            print(f"      · {p}")
        for n in risultato.get("note", []):
            print(f"      nota: {n}")

    return 1 if risultato["esito"] == "BLOCCO" else 0


if __name__ == "__main__":
    sys.exit(main())
