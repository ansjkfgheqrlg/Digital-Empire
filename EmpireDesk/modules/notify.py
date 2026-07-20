# -*- coding: utf-8 -*-
"""
B3 — modules/notify.py (Half B, owner: Gael — contratto dossier 17 §5.3).

Notifiche Windows toast quando una tile termina (exit code ricevuto o errore immediato).
L'integrazione con TileManager avviene via polling della coda di completamento
(push_tile_completion in app.py, consumata qui in background).

Zero dipendenze nuove: usa PowerShell integrato in Windows per i toast
(nessun pacchetto pip da installare). Fallback silenzioso se PowerShell manca
o la funzionalità non è disponibile (l'app non dipende dalle notifiche per funzionare).

Il modulo NON lancia automazioni (Mandato Art.4.3).
"""
import json
import os
import subprocess
import threading
import time as _time
from pathlib import Path

STATE_DIR = Path(__file__).resolve().parents[1] / "state"
STATE_FILE = STATE_DIR / "notify.json"

_ENABLED = True          # stato globale notifiche
_SENT_LOG: list = []      # ultimi toast inviati (per debug/UI)
_loop_started = False


# --------------------------------------------------------------------------- #
# Config persistenza
# --------------------------------------------------------------------------- #
def _load_cfg() -> dict:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            pass
    return {"enabled": True}


def _save_cfg(cfg: dict) -> None:
    STATE_FILE.write_text(json.dumps(cfg, ensure_ascii=False, indent=2), encoding="utf-8")


# --------------------------------------------------------------------------- #
# Toast Windows via PowerShell
# --------------------------------------------------------------------------- #
def _send_toast(title: str, body: str) -> bool:
    """Invia un Windows toast notification. Ritorna True se inviato, False altrimenti.
    Non solleva eccezioni (fallback silenzioso)."""
    if os.name != "nt":
        return False

    # PowerShell one-liner per toast: [Windows.UI.Notifications.ToastNotificationManager]
    # Funziona su Windows 10/11 con PowerShell 5.1+ (presente su tutti i PC Windows moderni).
    # Non richiede librerie aggiuntive.
    script = f"""
Add-Type -AssemblyName System.Windows.Forms; [System.Windows.Forms.MessageBox]::Show('{body.replace("'", "''")}', '{title.replace("'", "''")}', 'OK', 'Info')
"""
    try:
        proc = subprocess.run(
            ["powershell", "-NoProfile", "-NonInteractive", "-Command", script],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
            timeout=10,
        )
        return proc.returncode == 0
    except Exception:  # noqa: BLE001
        return False


def _notify_tile_complete(tile_id: str, exit_code: int | None, error: str | None) -> None:
    """Costruisce e invia il toast per un completamento tile."""
    global _ENABLED, _SENT_LOG

    if not _ENABLED:
        return

    # Nome leggibile della tile (mappatura statica — non dipende da app.py)
    _TILE_NAMES = {
        "email": "Outreach Email",
        "ig": "Instagram",
        "linkedin": "LinkedIn",
        "scraper": "Scraper Lead",
        "preventivi": "PreventivoForge",
        "caroselli": "Caroselli",
        "studio": "Empire Studio",
    }
    name = _TILE_NAMES.get(tile_id, tile_id)

    if error:
        title = f"❌ {name}"
        body = f"Avvio fallito: {error[:80]}"
    elif exit_code == 0:
        title = f"✅ {name}"
        body = "Completato con successo."
    else:
        title = f"⚠️ {name}"
        body = f"Terminato con exit code {exit_code}."

    sent = _send_toast(title, body)
    _SENT_LOG.append({"tile": tile_id, "title": title, "body": body, "sent": sent, "ts": _time.strftime("%H:%M:%S")})
    del _SENT_LOG[:-20]  # tiene ultimi 20


# --------------------------------------------------------------------------- #
# Background loop — consuma la coda completamenti
# --------------------------------------------------------------------------- #
def run_background(host) -> None:
    """Chiamato da app.py::start_module_background_tasks() a motore GUI già avviato.
    Polla la coda completamenti e invia toast per ogni tile che termina."""
    global _ENABLED, _loop_started

    cfg = _load_cfg()
    _ENABLED = cfg.get("enabled", True)

    if _loop_started:
        return
    _loop_started = True

    # Importo poll_completions da app.py — è nello stesso package (EmpireDesk/)
    from app import poll_completions

    def _loop():
        while True:
            try:
                for ev in poll_completions():
                    _notify_tile_complete(ev["id"], ev.get("exit_code"), ev.get("error"))
            except Exception:  # noqa: BLE001 — il loop non deve mai fermarsi
                pass
            _time.sleep(2)

    threading.Thread(target=_loop, daemon=True).start()


# --------------------------------------------------------------------------- #
# Routes (opzionali — per UI panel)
# --------------------------------------------------------------------------- #
def stato(payload=None):
    cfg = _load_cfg()
    return {
        "enabled": cfg.get("enabled", True),
        "log": _SENT_LOG[-10:],
        "platform": "windows" if os.name == "nt" else "other",
    }


def toggle(payload=None):
    global _ENABLED
    p = payload or {}
    new_state = p.get("enabled")
    if new_state is None:
        return {"errore": "manca 'enabled'"}
    _ENABLED = bool(new_state)
    cfg = _load_cfg()
    cfg["enabled"] = _ENABLED
    _save_cfg(cfg)
    return {"ok": True, "enabled": _ENABLED}


# --------------------------------------------------------------------------- #
# Contratto modulo (dossier 17 §5.3)
# --------------------------------------------------------------------------- #
MODULE = {
    "id": "notify",
    "tile": None,
    "routes": {
        "notify/stato": stato,
        "notify/toggle": toggle,
    },
    "panel_html": None,
}


def selftest():
    """Probe: Windows + PowerShell disponibile. Non invia notifiche reali (Mandato Art.4.3)."""
    if os.name != "nt":
        return True, "notify: piattaforma non Windows — toast disabilitati"
    try:
        r = subprocess.run(
            ["powershell", "-NoProfile", "-NonInteractive", "-Command", "echo ok"],
            capture_output=True, timeout=10,
        )
        if r.returncode == 0:
            return True, "notify: Windows + PowerShell disponibili, toast attivi"
        return False, f"notify: PowerShell ha restituito exit code {r.returncode}"
    except FileNotFoundError:
        return False, "notify: PowerShell non trovato"
    except Exception as exc:
        return False, f"notify: errore PowerShell — {exc}"
