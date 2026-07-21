# -*- coding: utf-8 -*-
"""
B3 — modules/notify.py (Half B, owner: Gael — contratto dossier 17 §5.3).

Notifica Windows nativa (toast) quando una tile finisce, con l'exit code. Zero dipendenze
pip pesanti (dossier 17 §5.1: "zero dipendenze pesanti"): usa PowerShell + WinRT toast API,
già presente su ogni Windows moderno — nessun pacchetto extra da installare/bundlare.

Osserva le tile via `host.tiles()` (stato read-only, NON consuma il cursore di `poll()`: non
ruba mai righe di log a chi guarda il pannello nella UI — vedi app.py::_Host.tiles()).
"""
import os
import shutil
import subprocess
import threading
import time as _time

_HOST = None            # iniettato da run_background(host)
_last_running: dict = {}  # {tile_id: bool} — stato al giro precedente, per rilevare la transizione
_loop_started = False


def run_background(host) -> None:
    """Chiamato da app.py::start_module_background_tasks() a motore GUI già avviato."""
    global _HOST, _loop_started
    _HOST = host
    if _loop_started:
        return
    _loop_started = True
    threading.Thread(target=_loop, daemon=True).start()


def _loop() -> None:
    while True:
        try:
            _tick()
        except Exception:  # noqa: BLE001 — il loop non deve mai fermarsi da solo
            pass
        _time.sleep(2)


def _tick() -> None:
    if _HOST is None:
        return
    for t in _HOST.tiles():
        tid = t["id"]
        running = bool(t.get("running"))
        was_running = _last_running.get(tid, False)
        if was_running and not running:
            exit_code = t.get("exit_code")
            name = t.get("name", tid)
            if exit_code == 0:
                _toast(f"{name} — completata", "Terminata con successo (exit 0).")
            elif exit_code is not None:
                _toast(f"{name} — errore", f"Terminata con errore (exit {exit_code}).")
        _last_running[tid] = running


def _toast(title: str, body: str) -> None:
    """Notifica Windows via PowerShell/WinRT (fire-and-forget). Non blocca, non solleva:
    una notifica mancata non deve mai impedire il resto dell'app."""
    if os.name != "nt":
        return
    ps_title = title.replace("'", "''")
    ps_body = body.replace("'", "''")
    script = (
        "[Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType=WindowsRuntime] > $null;"
        "$t = [Windows.UI.Notifications.ToastNotificationManager]::GetTemplateContent("
        "[Windows.UI.Notifications.ToastTemplateType]::ToastText02);"
        "$texts = $t.GetElementsByTagName('text');"
        f"$texts.Item(0).AppendChild($t.CreateTextNode('{ps_title}')) > $null;"
        f"$texts.Item(1).AppendChild($t.CreateTextNode('{ps_body}')) > $null;"
        "$toast = [Windows.UI.Notifications.ToastNotification]::new($t);"
        "[Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier('Empire Desk').Show($toast);"
    )
    try:
        subprocess.Popen(
            ["powershell.exe", "-NoProfile", "-NonInteractive", "-WindowStyle", "Hidden", "-Command", script],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL,
            creationflags=subprocess.CREATE_NO_WINDOW,
        )
    except OSError:
        pass


MODULE = {
    "id": "notify",
    "tile": None,
    "routes": {},
    "panel_html": None,
}


def selftest():
    """Probe: piattaforma + powershell.exe disponibili. NESSUNA notifica reale in selftest."""
    if os.name != "nt":
        return True, "notify: piattaforma non Windows, notifiche disattivate (no-op sicuro)"
    if not (shutil.which("powershell") or shutil.which("powershell.exe")):
        return False, "notify: powershell.exe non trovato sul PC"
    return True, "notify: powershell.exe disponibile, loop pronto"
