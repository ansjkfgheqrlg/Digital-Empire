#!/usr/bin/env python3
"""
app.py — EMPIRE DESK (Gael, dossier PIANO-MAESTRO/17-EMPIRE-DESK-APP.md).

Un solo .exe = la plancia di comando di Digital Empire. Ogni tile lancia via subprocess
un runtime ESISTENTE (ADR-003: launcher/wrapper, mai riscrittura dei motori).

Stack (identico pattern PreventivoForge, con la lezione WebView2 già applicata):
ordine motori GUI = Chrome-app (server locale + finestra `chrome --app`) -> pywebview -> Tkinter.
Motivo: su alcuni PC WebView2 manca e pywebview fallisce IN SILENZIO (bug reale trovato in
PreventivoForge, CP-20260715-001) -> qui si parte già col motore che NON dipende da WebView2.

Uso dev:      python app.py
Selftest:     python app.py --selftest   (verifica che ogni tile sia lanciabile, NON lancia nulla)
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import threading
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


# --------------------------------------------------------------------------- #
# Percorsi (dev + frozen PyInstaller) — l'exe gira da qualsiasi cartella
# --------------------------------------------------------------------------- #
def _base_dir() -> Path:
    if getattr(sys, "frozen", False):
        return Path(sys.executable).resolve().parent
    return Path(__file__).resolve().parent


BASE_DIR = _base_dir()


def _find_repo_root() -> Path:
    """Risale da BASE_DIR cercando la radice del monorepo (marcatore: PIANO-MAESTRO/ + company/).
    Robusto anche se l'exe viene spostato/rinominato, finché resta dentro il repo."""
    cur = BASE_DIR
    for _ in range(6):
        if (cur / "PIANO-MAESTRO").is_dir() and (cur / "company").is_dir():
            return cur
        if cur.parent == cur:
            break
        cur = cur.parent
    return BASE_DIR.parent  # fallback: EmpireDesk/ è sempre 1 livello sotto la radice


REPO_ROOT = _find_repo_root()
PROFILE_DIR = BASE_DIR / "chrome-profile"


# --------------------------------------------------------------------------- #
# Registro tile — v0.1 (8 automazioni reali, path relativi a REPO_ROOT)
# --------------------------------------------------------------------------- #
TILES = [
    {
        "id": "email", "icon": "\U0001F4E7", "name": "Outreach Email",
        "desc": "Flusso invio email outreach (300+/gg)",
        "kind": "proc", "cmd": ["Outreach/AVVIA-EMAIL-LIVE.bat"],
        "cwd": "Outreach", "input": None,
    },
    {
        "id": "ig", "icon": "\U0001F4F8", "name": "Outreach Instagram",
        "desc": "Flusso outreach Instagram",
        "kind": "proc", "cmd": ["Outreach/Instagram Automation/_avvia_ig.bat"],
        "cwd": "Outreach/Instagram Automation", "input": None,
    },
    {
        "id": "linkedin", "icon": "\U0001F4BC", "name": "LinkedIn",
        "desc": "Flusso giornaliero LinkedIn (scrape+connect+follow-up)",
        "kind": "proc", "cmd": ["Outreach/LinkedIn Automation/run_daily.bat"],
        "cwd": "Outreach/LinkedIn Automation", "input": None,
    },
    {
        "id": "scraper", "icon": "\U0001F50E", "name": "Scraper Lead",
        "desc": "Scraping lead (scrape_only.py)",
        "kind": "proc", "cmd": [sys.executable or "python", "Outreach/Outreach Workflow/scrape_only.py"],
        "cwd": "Outreach/Outreach Workflow", "input": None,
    },
    {
        "id": "preventivi", "icon": "\U0001F697", "name": "PreventivoForge",
        "desc": "App preventivi Novacar (annuncio mobile.de -> PDF)",
        "kind": "proc", "cmd": ["Clienti/Prof Autocad/preventivo-forge/avvia-app.bat"],
        "cwd": "Clienti/Prof Autocad/preventivo-forge", "input": None,
    },
    {
        "id": "caroselli", "icon": "\U0001F3A8", "name": "Caroselli",
        "desc": "Batch caroselli (carousel-factory)",
        "kind": "proc", "cmd": ["node", "scripts/generate.js"],
        "cwd": "Workfolw crea caroselli à/carousel-factory", "input": None,
    },
    {
        "id": "studio", "icon": "\U0001F3AC", "name": "Empire Studio",
        "desc": "Ingest video (incolla URL YouTube)",
        "kind": "proc",
        "cmd": [sys.executable or "python",
                "SKILL & Agenti/Empire Studio Suite/empire-studio/scripts/yt_ingest.py"],
        "cwd": "SKILL & Agenti/Empire Studio Suite/empire-studio", "input": "url",
    },
    {
        "id": "stato", "icon": "\U0001F4CA", "name": "STATO Empire",
        "desc": "Stato corrente dell'Impero (sola lettura)",
        "kind": "readonly", "path": "company/Memory/STATO-EMPIRE.md",
    },
]
_TILE_BY_ID = {t["id"]: t for t in TILES}


# --------------------------------------------------------------------------- #
# TileManager — lancia/monitora i subprocess reali (SOLO wrapper, ADR-003)
# --------------------------------------------------------------------------- #
class _Job:
    __slots__ = ("proc", "lines", "pos", "running", "exit_code", "error")

    def __init__(self):
        self.proc = None
        self.lines: list[str] = []
        self.pos = 0
        self.running = False
        self.exit_code: int | None = None
        self.error: str | None = None


class TileManager:
    def __init__(self):
        self.jobs: dict[str, _Job] = {}
        self._lock = threading.Lock()

    def list_tiles(self) -> list[dict]:
        out = []
        for t in TILES:
            job = self.jobs.get(t["id"])
            out.append({
                "id": t["id"], "icon": t["icon"], "name": t["name"], "desc": t["desc"],
                "kind": t["kind"], "input": t.get("input"),
                "running": bool(job and job.running),
                "exit_code": job.exit_code if job else None,
            })
        return out

    def _resolve_check(self, tile: dict) -> tuple[bool, str]:
        """Verifica che il comando sia LANCIABILE senza eseguirlo (path esiste, eseguibile trovato)."""
        if tile["kind"] == "readonly":
            p = REPO_ROOT / tile["path"]
            return (p.exists(), "" if p.exists() else f"file non trovato: {p}")
        cmd = tile["cmd"]
        cwd = REPO_ROOT / tile["cwd"]
        if not cwd.exists():
            return False, f"cartella non trovata: {cwd}"
        # il primo argomento eseguibile: se è un path relativo dentro il repo, verifica che esista;
        # se è un binario (python/node), verifica che sia raggiungibile.
        first = cmd[0]
        first_path = REPO_ROOT / first if not Path(first).is_absolute() else Path(first)
        if first_path.exists():
            # se il comando ha un secondo argomento che è uno script, verificalo anche
            if len(cmd) > 1:
                script = REPO_ROOT / cmd[1]
                if not script.exists():
                    return False, f"script non trovato: {script}"
            return True, ""
        # binario su PATH (python/node/ecc.)
        import shutil
        exe = shutil.which(first) or shutil.which(Path(first).name)
        if not exe:
            return False, f"eseguibile non trovato: {first}"
        if len(cmd) > 1:
            script = REPO_ROOT / cmd[1]
            if not script.exists():
                return False, f"script non trovato: {script}"
        return True, ""

    def selftest(self) -> list[dict]:
        out = []
        for t in TILES:
            ok, detail = self._resolve_check(t)
            out.append({"id": t["id"], "name": t["name"], "ok": ok, "detail": detail})
        return out

    def launch(self, tile_id: str, user_input: str | None) -> dict:
        tile = _TILE_BY_ID.get(tile_id)
        if not tile:
            return {"ok": False, "error": "tile sconosciuta"}
        if tile["kind"] == "readonly":
            return {"ok": False, "error": "tile di sola lettura: usa stato()"}
        with self._lock:
            job = self.jobs.get(tile_id)
            if job and job.running:
                return {"ok": False, "error": "già in corso"}
            ok, detail = self._resolve_check(tile)
            if not ok:
                return {"ok": False, "error": f"non lanciabile: {detail}"}
            if tile.get("input") == "url" and not (user_input or "").strip():
                return {"ok": False, "error": "serve un URL"}
            cmd = list(tile["cmd"])
            if tile.get("input") == "url":
                cmd = cmd + [user_input.strip()]
            cwd = str(REPO_ROOT / tile["cwd"])
            job = _Job()
            job.running = True
            self.jobs[tile_id] = job
            try:
                creationflags = subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0
                job.proc = subprocess.Popen(
                    cmd, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                    text=True, bufsize=1, encoding="utf-8", errors="replace",
                    creationflags=creationflags,
                )
            except Exception as exc:  # noqa: BLE001
                job.running = False
                job.error = str(exc)
                return {"ok": False, "error": f"avvio fallito: {exc}"}
            threading.Thread(target=self._reader, args=(tile_id, job), daemon=True).start()
            return {"ok": True}

    def _reader(self, tile_id: str, job: _Job) -> None:
        try:
            assert job.proc is not None and job.proc.stdout is not None
            for line in job.proc.stdout:
                job.lines.append(line.rstrip("\n"))
                if len(job.lines) > 2000:
                    job.lines = job.lines[-2000:]
                    job.pos = max(0, job.pos - 1)
            job.exit_code = job.proc.wait()
        except Exception as exc:  # noqa: BLE001
            job.error = str(exc)
        finally:
            job.running = False

    def poll(self, tile_id: str) -> dict:
        job = self.jobs.get(tile_id)
        if not job:
            return {"lines": [], "running": False, "exit_code": None, "error": None}
        new_lines = job.lines[job.pos:]
        job.pos = len(job.lines)
        return {"lines": new_lines, "running": job.running, "exit_code": job.exit_code, "error": job.error}

    def stato(self) -> dict:
        p = REPO_ROOT / "company/Memory/STATO-EMPIRE.md"
        try:
            return {"ok": True, "content": p.read_text(encoding="utf-8")}
        except Exception as exc:  # noqa: BLE001
            return {"ok": False, "content": "", "error": str(exc)}


MANAGER = TileManager()


# --------------------------------------------------------------------------- #
# Bridge HTTP locale (usato dal motore Chrome-app; pywebview usa gli stessi
# metodi esposti direttamente come js_api, senza passare dall'HTTP)
# --------------------------------------------------------------------------- #
def _ui_html() -> str:
    for base in (BASE_DIR, Path(getattr(sys, "_MEIPASS", BASE_DIR))):
        p = base / "ui" / "index.html"
        if p.exists():
            return p.read_text(encoding="utf-8")
    return "<html><body>ui/index.html mancante</body></html>"


class _Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):  # silenzia il log HTTP di default
        pass

    def _send_json(self, obj: dict, code: int = 200) -> None:
        body = json.dumps(obj).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):  # noqa: N802
        if self.path in ("/", "/index.html"):
            body = _ui_html().encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        self.send_response(404)
        self.end_headers()

    def do_POST(self):  # noqa: N802
        length = int(self.headers.get("Content-Length") or 0)
        raw = self.rfile.read(length) if length else b"{}"
        try:
            payload = json.loads(raw or b"{}")
        except Exception:
            payload = {}
        route = self.path.strip("/")
        if route == "api/tiles":
            self._send_json({"tiles": MANAGER.list_tiles()})
        elif route == "api/launch":
            self._send_json(MANAGER.launch(payload.get("id", ""), payload.get("input")))
        elif route == "api/poll":
            self._send_json(MANAGER.poll(payload.get("id", "")))
        elif route == "api/stato":
            self._send_json(MANAGER.stato())
        elif route == "api/selftest":
            self._send_json({"results": MANAGER.selftest()})
        else:
            self._send_json({"error": "route sconosciuta"}, 404)


def _start_server() -> int:
    server = ThreadingHTTPServer(("127.0.0.1", 0), _Handler)
    port = server.server_address[1]
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return port


# --------------------------------------------------------------------------- #
# Motore 1: Chrome-app (nessuna dipendenza da WebView2, pattern CP-20260715-001)
# --------------------------------------------------------------------------- #
def _find_chrome() -> str | None:
    import shutil
    candidates = [
        os.environ.get("ProgramFiles", "") + r"\Google\Chrome\Application\chrome.exe",
        os.environ.get("ProgramFiles(x86)", "") + r"\Google\Chrome\Application\chrome.exe",
        os.environ.get("LocalAppData", "") + r"\Google\Chrome\Application\chrome.exe",
    ]
    for c in candidates:
        if c and Path(c).exists():
            return c
    return shutil.which("chrome") or shutil.which("chrome.exe")


def main_chrome_app() -> int:
    chrome = _find_chrome()
    if not chrome:
        raise RuntimeError("Google Chrome non trovato")
    port = _start_server()
    PROFILE_DIR.mkdir(parents=True, exist_ok=True)
    cmd = [
        chrome, f"--app=http://127.0.0.1:{port}/",
        f"--user-data-dir={PROFILE_DIR}",
        "--window-size=1180,800",
    ]
    proc = subprocess.Popen(cmd)
    proc.wait()
    return 0


# --------------------------------------------------------------------------- #
# Motore 2: pywebview (fallback se Chrome non c'è)
# --------------------------------------------------------------------------- #
class _WebApi:
    def tiles(self):
        return MANAGER.list_tiles()

    def launch(self, tile_id, user_input=None):
        return MANAGER.launch(tile_id, user_input)

    def poll(self, tile_id):
        return MANAGER.poll(tile_id)

    def stato(self):
        return MANAGER.stato()

    def selftest(self):
        return MANAGER.selftest()


def main_webview() -> int:
    import webview  # richiede pywebview + Edge WebView2 runtime

    api = _WebApi()
    webview.create_window(
        "Empire Desk", html=_ui_html(), js_api=api,
        width=1180, height=800, min_size=(980, 680),
        background_color="#1c2329",
    )
    webview.start()
    return 0


# --------------------------------------------------------------------------- #
# Motore 3: Tkinter (fallback finale — nessun PC resta senza app)
# --------------------------------------------------------------------------- #
def main_tk() -> int:
    import tkinter as tk
    from tkinter import scrolledtext

    root = tk.Tk()
    root.title("Empire Desk")
    root.configure(bg="#1c2329")
    root.geometry("880x640")

    tk.Label(root, text="EMPIRE DESK", bg="#1c2329", fg="#ffffff",
             font=("Segoe UI Semibold", 18)).pack(anchor="w", padx=20, pady=(16, 0))
    tk.Label(root, text="Modalità compatibilità (Chrome/WebView2 non disponibili)",
             bg="#1c2329", fg="#9fb0bb", font=("Segoe UI", 10)).pack(anchor="w", padx=20, pady=(0, 12))

    log = scrolledtext.ScrolledText(root, bg="#212a30", fg="#d7e0e6", font=("Consolas", 9))
    log.pack(fill="both", expand=True, padx=20, pady=(0, 10))

    def _log(msg):
        log.insert("end", msg + "\n")
        log.see("end")

    def _launch(tile_id):
        r = MANAGER.launch(tile_id, None)
        _log(f"[{tile_id}] " + ("avviato" if r.get("ok") else "ERRORE: " + str(r.get("error"))))

    btnbar = tk.Frame(root, bg="#1c2329")
    btnbar.pack(fill="x", padx=20, pady=(0, 16))
    for t in TILES:
        if t["kind"] == "readonly":
            continue
        b = tk.Button(btnbar, text=f"{t['name']}", command=lambda i=t["id"]: _launch(i),
                      bg="#3f4f5a", fg="#ffffff", relief="flat", padx=10, pady=6)
        b.pack(side="left", padx=(0, 8), pady=4)

    def _poll_all():
        for t in TILES:
            if t["kind"] == "readonly":
                continue
            r = MANAGER.poll(t["id"])
            for line in r["lines"]:
                _log(f"[{t['id']}] {line}")
        root.after(500, _poll_all)

    root.after(500, _poll_all)
    root.mainloop()
    return 0


# --------------------------------------------------------------------------- #
# Entry point
# --------------------------------------------------------------------------- #
def _run_selftest() -> int:
    results = MANAGER.selftest()
    ok_all = True
    for r in results:
        status = "OK " if r["ok"] else "FAIL"
        print(f"[{status}] {r['id']:<11} {r['name']:<20} {r['detail']}")
        ok_all = ok_all and r["ok"]
    print(f"\nREPO_ROOT = {REPO_ROOT}")
    print("SELFTEST " + ("PASS" if ok_all else "FAIL") + f" ({sum(1 for r in results if r['ok'])}/{len(results)})")
    return 0 if ok_all else 1


if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1] == "--selftest":
        raise SystemExit(_run_selftest())
    # ordine motori: Chrome-app -> pywebview -> Tkinter (mai un PC senza app)
    _code = None
    try:
        _code = main_chrome_app()
    except Exception:
        try:
            _code = main_webview()
        except Exception:
            _code = main_tk()
    raise SystemExit(_code)
