#!/usr/bin/env python3
"""Continua il polling di un fileId Fliki gia' esistente (generazione gia' avviata), senza
rilanciare la richiesta di generazione. Serve quando il client principale ha raggiunto il suo
timeout interno ma il job e' ancora vivo lato server."""
import sys
import os
import time
import json
import urllib.request
import urllib.error
import http.client

# reconfigure(), non un nuovo io.TextIOWrapper: due wrapper distinti sullo stesso buffer fanno
# chiudere il buffer sottostante al garbage collection del primo ("I/O operation on closed
# file", bug reale trovato il 2026-07-30). reconfigure() e' idempotente e sicuro.
if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)
    sys.stderr.reconfigure(encoding="utf-8", line_buffering=True)

FACTORY_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUT_DIR = os.path.join(FACTORY_DIR, "05-TEMPLATES-E-KIT")
VIDEOS_DIR = os.path.join(FACTORY_DIR, "06-DASHBOARD-E-METRICHE", "video-generati")
LOCK_PATH = os.path.join(FACTORY_DIR, "memory", "fliki_lock.json")
# Prima del 2026-08-20 uno stallo lato Fliki restava invisibile per 1-2h (fino al timeout
# interno): scoperto solo controllando a mano. Con un job realmente bloccato per ore, un
# allarme a 30 min invece che 60-120 accorcia di molto il tempo prima che un umano se ne accorga.
ALERT_QUEUED_THRESHOLD_S = 1800


def _clear_lock_if_ours(file_id: str) -> None:
    if not os.path.exists(LOCK_PATH):
        return
    try:
        lock = json.load(open(LOCK_PATH, encoding="utf-8"))
    except (json.JSONDecodeError, ValueError):
        return
    if lock.get("file_id") == file_id:
        try:
            os.remove(LOCK_PATH)
        except OSError:
            pass


def api_key():
    for line in open(os.path.join(FACTORY_DIR, ".env"), encoding="utf-8"):
        if line.strip().startswith("FLIKI_API_KEY="):
            return line.strip().split("=", 1)[1]
    raise SystemExit("FLIKI_API_KEY non trovata")


def main(file_id: str, out_name: str, max_wait_s: int = 3600):
    key = api_key()
    waited = 0
    alertato = False
    while waited < max_wait_s:
        if not alertato and waited >= ALERT_QUEUED_THRESHOLD_S:
            print(f"[!!! ALLARME] fileId={file_id} ancora in coda dopo {waited//60} minuti senza "
                  f"mai passare a 'processing'. Non e' normale attesa di coda: verifica dashboard "
                  f"Fliki (credito/limite piano) invece di continuare ad aspettare in silenzio.",
                  flush=True)
            alertato = True
        req = urllib.request.Request(
            f"https://api.fliki.ai/v1/generate/status?fileId={file_id}",
            headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
        )
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                res = json.loads(resp.read().decode("utf-8"))
        except (TimeoutError, urllib.error.URLError, ConnectionError, http.client.RemoteDisconnected) as e:
            print(f"[!] timeout rete, ritento: {e}", flush=True)
            time.sleep(10)
            waited += 10
            continue
        status = res.get("status")
        print(f"[status] {status} (progress={res.get('progress')}, {waited}s trascorsi)", flush=True)
        if status == "success":
            download = res["download"]
            # Il nome arriva senza estensione (fliki_client.py la aggiunge da se'):
            # senza questa riga il file finiva sul disco come "nome" invece di "nome.mp4"
            # e nessuno script a valle lo trovava (successo il 2026-09-04 su XABjAjqfUxw).
            if not out_name.lower().endswith(".mp4"):
                out_name += ".mp4"
            out_path = os.path.join(VIDEOS_DIR, out_name)
            r2 = urllib.request.Request(download, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(r2, timeout=120) as resp2:
                with open(out_path, "wb") as f:
                    f.write(resp2.read())
            print(f"[+] Video scaricato: {out_path}", flush=True)
            _clear_lock_if_ours(file_id)
            return
        if status in ("error", "canceled"):
            _clear_lock_if_ours(file_id)
            raise SystemExit(f"Generazione fallita: {res}")
        time.sleep(15)
        waited += 15
    raise SystemExit(f"Timeout dopo {max_wait_s}s")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 3600)
