#!/usr/bin/env python3
"""
app.py — EMPIRE DESK (Gael, dossier PIANO-MAESTRO/17-EMPIRE-DESK-APP.md, §0-bis PIVOT AREUS).

Un solo .exe = l'app gestionale di Digital Empire. Il server locale serve la piattaforma
**Aureus Agency OS** (React/Vite, grafica di Max — `platform/`, INTOCCABILE) come root, mantenendo
vive le stesse API `/api/*` (tiles/launch/poll/modules/...) per l'operatività di fase 2 (Max, U1).
La vecchia UI launcher (Empire Premium) resta raggiungibile a `/legacy` come fallback temporaneo.

Ogni tile/automazione lanciata resta un subprocess su un runtime ESISTENTE (ADR-003: launcher/
wrapper, mai riscrittura dei motori).

Stack GUI (identico pattern PreventivoForge, con la lezione WebView2 già applicata):
ordine motori = Chrome-app (server locale + finestra `chrome --app`) -> pywebview -> Tkinter.
Motivo: su alcuni PC WebView2 manca e pywebview fallisce IN SILENZIO (bug reale trovato in
PreventivoForge, CP-20260715-001) -> qui si parte già col motore che NON dipende da WebView2.

Uso dev:      python app.py                (richiede EmpireDesk/platform/dist/ già buildata:
                                             dentro platform/ -> npm install && npm run build)
Selftest:     python app.py --selftest   (verifica tile/moduli/build platform, NON lancia nulla)
"""
from __future__ import annotations

import json
import mimetypes
import os
import subprocess
import sys
import threading
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
PLATFORM_DIR = BASE_DIR / "platform"          # Aureus Agency OS (grafica = Max, INTOCCABILE)
PLATFORM_DIST = PLATFORM_DIR / "dist"         # prodotta da `npm run build` dentro platform/


# --------------------------------------------------------------------------- #
# Registro tile — v0.1 (8 automazioni reali, path relativi a REPO_ROOT)
#
# "kind" decide COME si costruisce l'argv al lancio (mai un binario congelato al momento
# dell'import — vedi _python_bin/_node_bin: da frozen, sys.executable è EmpireDesk.exe
# stesso, NON un interprete Python -> l'argv va risolto a runtime, non qui).
#   bat      -> ["cmd.exe", "/c", <script>]   (evita WinError 193 su .bat senza shell)
#   py       -> [_python_bin(), <script>]
#   node     -> [_node_bin(), <script>]
#   readonly -> nessun processo, legge solo "path"
# --------------------------------------------------------------------------- #
_CORE_TILES = [
    {
        "id": "email", "icon": "\U0001F4E7", "name": "Outreach Email",
        "desc": "Flusso invio email outreach (300+/gg)",
        "kind": "bat", "script": "Outreach/AVVIA-EMAIL-LIVE.bat",
        "cwd": "Outreach", "input": None,
    },
    {
        "id": "ig", "icon": "\U0001F4F8", "name": "Outreach Instagram",
        "desc": "Flusso outreach Instagram",
        "kind": "bat", "script": "Outreach/Instagram Automation/_avvia_ig.bat",
        "cwd": "Outreach/Instagram Automation", "input": None,
    },
    {
        "id": "linkedin", "icon": "\U0001F4BC", "name": "LinkedIn",
        "desc": "Flusso giornaliero LinkedIn (scrape+connect+follow-up)",
        "kind": "bat", "script": "Outreach/LinkedIn Automation/run_daily.bat",
        "cwd": "Outreach/LinkedIn Automation", "input": None,
    },
    {
        "id": "scraper", "icon": "\U0001F50E", "name": "Scraper Lead",
        "desc": "Scraping lead (scrape_only.py)",
        "kind": "py", "script": "Outreach/Outreach Workflow/scrape_only.py",
        "cwd": "Outreach/Outreach Workflow", "input": None,
    },
    {
        "id": "preventivi", "icon": "\U0001F697", "name": "PreventivoForge",
        "desc": "App preventivi Novacar (annuncio mobile.de -> PDF)",
        "kind": "bat", "script": "Clienti/Prof Autocad/preventivo-forge/avvia-app.bat",
        "cwd": "Clienti/Prof Autocad/preventivo-forge", "input": None,
    },
    {
        "id": "caroselli", "icon": "\U0001F3A8", "name": "Caroselli",
        "desc": "Genera 1 carosello da un file JSON (brand/titolo/slide)",
        "kind": "node", "script": "Workfolw crea caroselli à/carousel-factory/scripts/generate.js",
        "cwd": "Workfolw crea caroselli à/carousel-factory", "input": "path",
    },
    {
        "id": "studio", "icon": "\U0001F3AC", "name": "Empire Studio",
        "desc": "Ingest video (incolla URL YouTube)",
        "kind": "py", "script": "SKILL & Agenti/Empire Studio Suite/empire-studio/scripts/yt_ingest.py",
        "cwd": "SKILL & Agenti/Empire Studio Suite/empire-studio", "input": "url",
    },
    {
        "id": "stato", "icon": "\U0001F4CA", "name": "STATO Empire",
        "desc": "Stato corrente dell'Impero (sola lettura)",
        "kind": "readonly", "path": "company/Memory/STATO-EMPIRE.md",
    },
]


def _python_bin() -> str:
    """L'interprete Python da usare per lanciare gli script .py delle automazioni.
    In dev è lo stesso interprete che esegue app.py; da .exe (frozen) sys.executable
    e' EmpireDesk.exe -> va cercato un python reale installato sul PC (PreventivoForge
    e le altre automazioni Python richiedono comunque Python installato a parte)."""
    if not getattr(sys, "frozen", False):
        return sys.executable
    import shutil
    for cand in ("python", "python3", "py"):
        found = shutil.which(cand)
        if found:
            return found
    return "python"  # lascia fallire in modo esplicito (selftest lo segnala)


def _node_bin() -> str:
    import shutil
    return shutil.which("node") or "node"


class _Host:
    """Contesto opzionale passato a `run_background(host)` (es. B2 scheduler): permette a un
    modulo di lanciare/pollare altre tile SENZA importare app.py o conoscere TileManager
    (disaccoppiamento — il modulo non tocca mai il core). I metodi leggono `MANAGER`/`all_tiles()`
    a runtime (late-binding): sicuro anche se `_Host` è istanziato PRIMA che `MANAGER` esista più
    sotto nel file, perché `run_background` parte solo a motore GUI avviato (mai prima, mai in
    --selftest — vedi `start_module_background_tasks()`)."""

    def launch(self, tile_id: str, user_input: str | None = None) -> dict:
        return MANAGER.launch(tile_id, user_input)

    def poll(self, tile_id: str) -> dict:
        return MANAGER.poll(tile_id)

    def tile_ids(self) -> list[str]:
        return [t["id"] for t in all_tiles() if t["kind"] != "readonly"]


_HOST = _Host()


# --------------------------------------------------------------------------- #
# B1 — Loader moduli (EmpireDesk/modules/*.py, contratto dossier 17 §5.3)
#
# Dopo B1 il core Python (app.py) va in FREEZE lato business-logic: nuove funzionalità (B2/B3/B4
# di Gael, A1-A4 di Max) entrano SOLO come moduli qui sotto. Eccezione unica e già prevista:
# `_Host`/`run_background()` qui sopra — pura plumbing per permettere a un modulo di richiamare
# TileManager, non logica di business (necessaria per B2, non introduce comportamento nuovo).
# `ui/index.html` è di Max (vedi STATO-EMPIRE 2026-07-19 sera) — non si tocca da qui.
# Un modulo rotto (import fallito, MODULE malformato) NON deve mai far cadere l'intero Empire
# Desk: si isola, si segnala nel selftest, si salta.
# --------------------------------------------------------------------------- #
MODULES_DIR = BASE_DIR / "modules"

_LOADED_MODULES: list[dict] = []   # [{"id","file","routes","tile","panel_html","selftest_fn"}]
_MODULE_LOAD_ERRORS: list[dict] = []  # [{"file","error"}] — moduli scartati, mai fatali
_MODULE_ROUTES: dict[str, "callable"] = {}
_MODULE_TILES: list[dict] = []


def _validate_module_tile(tile: dict) -> tuple[bool, str]:
    """Una tile fornita da un modulo DEVE rispettare lo schema di _CORE_TILES (id/icon/name/desc/kind
    + script/cwd o path) — altrimenti TileManager va in KeyError su un dict a metà (un modulo con
    schema sbagliato non deve mai far crashare selftest/list_tiles per TUTTE le tile, incluse quelle core)."""
    if not isinstance(tile, dict):
        return False, "tile non è un dict"
    required = {"id", "icon", "name", "desc", "kind"}
    missing = required - tile.keys()
    if missing:
        return False, f"campi mancanti: {sorted(missing)}"
    if tile["kind"] == "readonly":
        if "path" not in tile:
            return False, "kind='readonly' richiede 'path'"
    elif tile["kind"] in ("bat", "py", "node"):
        if "script" not in tile or "cwd" not in tile:
            return False, f"kind='{tile['kind']}' richiede 'script' e 'cwd'"
    else:
        return False, f"kind sconosciuto: {tile['kind']}"
    return True, ""


def _load_modules() -> None:
    """Scandisce modules/*.py, importa ognuno in isolamento (try/except per file:
    un modulo rotto si segnala e si salta, non fa crashare Empire Desk)."""
    import importlib.util

    _LOADED_MODULES.clear()
    _MODULE_LOAD_ERRORS.clear()
    _MODULE_ROUTES.clear()
    _MODULE_TILES.clear()

    if not MODULES_DIR.is_dir():
        return
    for f in sorted(MODULES_DIR.glob("*.py")):
        if f.name.startswith("_"):
            continue
        try:
            spec = importlib.util.spec_from_file_location(f"empiredesk_module_{f.stem}", f)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)  # type: ignore[union-attr]
            info = getattr(mod, "MODULE", None)
            if not isinstance(info, dict) or "id" not in info:
                raise ValueError("MODULE mancante o senza 'id' (contratto dossier 17 §5.3)")
            mid = info["id"]
            selftest_fn = getattr(mod, "selftest", None)
            entry = {
                "id": mid, "file": f.name,
                "routes": info.get("routes") or {},
                "tile": info.get("tile"),
                "panel_html": info.get("panel_html"),
                "selftest_fn": selftest_fn if callable(selftest_fn) else None,
                "run_background_fn": getattr(mod, "run_background", None)
                if callable(getattr(mod, "run_background", None)) else None,
            }
            _LOADED_MODULES.append(entry)
            for route_name, fn in entry["routes"].items():
                if route_name in _MODULE_ROUTES:
                    _MODULE_LOAD_ERRORS.append({
                        "file": f.name,
                        "error": f"route '{route_name}' già registrata da un altro modulo — ignorata",
                    })
                    continue
                _MODULE_ROUTES[route_name] = fn
            if entry["tile"]:
                tile_ok, tile_detail = _validate_module_tile(entry["tile"])
                used_ids = {t["id"] for t in _CORE_TILES} | {t["id"] for t in _MODULE_TILES}
                if tile_ok and entry["tile"]["id"] in used_ids:
                    tile_ok, tile_detail = False, f"id '{entry['tile']['id']}' già usato da un'altra tile"
                if tile_ok:
                    _MODULE_TILES.append(entry["tile"])
                else:
                    # tile scartata (schema invalido) MA routes/panel del modulo restano validi:
                    # un modulo rotto su UNA parte non deve buttare via tutto il resto.
                    _MODULE_LOAD_ERRORS.append({"file": f.name, "error": f"tile scartata: {tile_detail}"})
        except Exception as exc:  # noqa: BLE001 — un modulo rotto non deve fermare l'app
            _MODULE_LOAD_ERRORS.append({"file": f.name, "error": str(exc)})


_load_modules()


def all_tiles() -> list[dict]:
    return _CORE_TILES + _MODULE_TILES


def _tile_by_id() -> dict[str, dict]:
    return {t["id"]: t for t in all_tiles()}


def modules_public() -> list[dict]:
    """Elenco moduli per la UI (contratto STATO-EMPIRE 2026-07-19 sera, owner UI Max):
    POST /api/modules -> {"modules": [{id, tile, panel_html}, ...]}."""
    return [{"id": m["id"], "tile": m["tile"], "panel_html": m["panel_html"]} for m in _LOADED_MODULES]


_background_started = False


def start_module_background_tasks() -> None:
    """Avvia i task in background dei moduli (es. B2 scheduler) chiamando `run_background(host)`.
    Va chiamata SOLO dai motori GUI reali (main_chrome_app/main_webview/main_tk), quando sono già
    certi di partire — MAI durante `_load_modules()` (troppo presto: MANAGER non esiste ancora) e
    MAI durante `--selftest` (Mandato Art.4.3: zero lanci/automazioni durante un selftest)."""
    global _background_started
    if _background_started:
        return
    _background_started = True
    for m in _LOADED_MODULES:
        fn = m.get("run_background_fn")
        if not fn:
            continue
        try:
            fn(_HOST)
        except Exception as exc:  # noqa: BLE001 — un modulo rotto non deve impedire l'avvio dell'app
            _MODULE_LOAD_ERRORS.append({"file": m["file"], "error": f"run_background fallito: {exc}"})


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
        for t in all_tiles():
            job = self.jobs.get(t["id"])
            out.append({
                "id": t["id"], "icon": t["icon"], "name": t["name"], "desc": t["desc"],
                "kind": t["kind"], "input": t.get("input"),
                "running": bool(job and job.running),
                "exit_code": job.exit_code if job else None,
            })
        return out

    def _build_argv(self, tile: dict) -> list[str]:
        script_path = str(REPO_ROOT / tile["script"])
        if tile["kind"] == "bat":
            return ["cmd.exe", "/c", script_path]
        if tile["kind"] == "py":
            return [_python_bin(), script_path]
        if tile["kind"] == "node":
            return [_node_bin(), script_path]
        raise ValueError(f"kind sconosciuto: {tile['kind']}")

    def _resolve_check(self, tile: dict) -> tuple[bool, str]:
        """Verifica che il comando sia LANCIABILE senza eseguirlo (path esiste, eseguibile trovato).
        Non esegue mai il processo (Mandato Art.4.3 — dry-run prima di spendere)."""
        if tile["kind"] == "readonly":
            p = REPO_ROOT / tile["path"]
            return (p.exists(), "" if p.exists() else f"file non trovato: {p}")
        cwd = REPO_ROOT / tile["cwd"]
        if not cwd.exists():
            return False, f"cartella non trovata: {cwd}"
        script = REPO_ROOT / tile["script"]
        if not script.exists():
            return False, f"script non trovato: {script}"
        if tile["kind"] == "py":
            exe = _python_bin()
            import shutil
            if not (Path(exe).exists() or shutil.which(exe)):
                return False, "interprete Python non trovato sul PC"
        elif tile["kind"] == "node":
            import shutil
            if not shutil.which("node"):
                return False, "Node.js non trovato sul PC (richiesto da carousel-factory)"
        return True, ""

    def selftest(self) -> list[dict]:
        out = []
        for t in all_tiles():
            ok, detail = self._resolve_check(t)
            out.append({"id": t["id"], "name": t["name"], "ok": ok, "detail": detail})
        return out

    def launch(self, tile_id: str, user_input: str | None) -> dict:
        tile = _tile_by_id().get(tile_id)
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
            if tile.get("input") and not (user_input or "").strip():
                return {"ok": False, "error": "questa tile richiede un input (vedi il campo sulla card)"}
            resolved_input = (user_input or "").strip()
            if tile.get("input") == "path" and resolved_input:
                # accetta assoluto, relativo alla cwd della tile, o relativo alla radice del repo
                candidates = [Path(resolved_input)]
                if not Path(resolved_input).is_absolute():
                    candidates += [REPO_ROOT / tile["cwd"] / resolved_input, REPO_ROOT / resolved_input]
                found = next((c for c in candidates if c.exists()), None)
                if not found:
                    return {"ok": False, "error": f"file non trovato: {resolved_input}"}
                resolved_input = str(found)
            cmd = self._build_argv(tile)
            if tile.get("input"):
                cmd = cmd + [resolved_input]
            cwd = str(REPO_ROOT / tile["cwd"])
            job = _Job()
            job.running = True
            self.jobs[tile_id] = job
            try:
                creationflags = subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0
                job.proc = subprocess.Popen(
                    cmd, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                    stdin=subprocess.DEVNULL,  # alcuni .bat wrappati finiscono con `pause`:
                    # senza stdin chiuso resterebbero appesi in attesa di un tasto per sempre
                    # (tile bloccata su "in corso" a vita) — vedi REGISTRO-ERRORI EDE-1.
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


def global_selftest() -> list[dict]:
    """Selftest completo: tile (core + moduli) + selftest proprio di ogni modulo caricato +
    i moduli scartati per errore di import (un modulo rotto DEVE comparire come FAIL qui,
    non sparire in silenzio — Gate 1, zero bottoni finti / zero difetti nascosti)."""
    out = MANAGER.selftest()
    for m in _LOADED_MODULES:
        if not m["selftest_fn"]:
            continue
        try:
            ok, detail = m["selftest_fn"]()
        except Exception as exc:  # noqa: BLE001 — un selftest di modulo non deve crashare il globale
            ok, detail = False, f"selftest del modulo ha sollevato: {exc}"
        out.append({"id": f"module:{m['id']}", "name": f"Modulo {m['id']}", "ok": bool(ok), "detail": str(detail)})
    for e in _MODULE_LOAD_ERRORS:
        out.append({"id": f"module-error:{e['file']}", "name": f"Modulo {e['file']} (import fallito)",
                    "ok": False, "detail": e["error"]})
    # Aureus buildata? (la home dell'app dipende da platform/dist/index.html)
    idx = PLATFORM_DIST / "index.html"
    out.append({
        "id": "platform", "name": "Aureus (platform/dist)",
        "ok": idx.exists(),
        "detail": "" if idx.exists() else f"build mancante — dentro platform/: npm install && npm run build ({idx})",
    })
    return out


def _call_module_route(route: str, payload: dict) -> dict:
    """Dispatcher condiviso HTTP/pywebview per le routes esposte dai moduli (§5.3).
    Un modulo che solleva un'eccezione NON deve mai far cadere il bridge — si riporta l'errore."""
    fn = _MODULE_ROUTES.get(route)
    if not fn:
        return {"error": f"route modulo sconosciuta: {route}"}
    try:
        return fn(payload or {})
    except Exception as exc:  # noqa: BLE001
        return {"error": f"modulo '{route}' ha sollevato: {exc}"}


# --------------------------------------------------------------------------- #
# Bridge HTTP locale (usato dal motore Chrome-app e da pywebview via url=,
# vedi main_webview) — serve la piattaforma Aureus (platform/dist/) come root,
# la vecchia UI launcher resta raggiungibile a /legacy (§0-bis dossier 17, G1).
# --------------------------------------------------------------------------- #
def _legacy_html() -> str:
    """Vecchia UI launcher 'Empire Premium' — fallback temporaneo a /legacy finché la
    fase 2 (Max, U1) non ricollega le automazioni dentro Aureus."""
    for base in (BASE_DIR, Path(getattr(sys, "_MEIPASS", BASE_DIR))):
        p = base / "ui" / "index.html"
        if p.exists():
            return p.read_text(encoding="utf-8")
    return "<html><body>ui/index.html (legacy) mancante</body></html>"


def _platform_missing_html() -> str:
    """Pagina di aiuto onesta se platform/dist/ non è ancora buildata (mai una pagina
    bianca o un errore criptico — Gate 'zero bottoni finti' vale anche per la home)."""
    return f"""<!doctype html><html lang="it"><head><meta charset="utf-8">
<title>Empire Desk — build mancante</title></head>
<body style="font-family:'Segoe UI',sans-serif;background:#1c2329;color:#eef1f3;
             padding:48px;max-width:640px;margin:0 auto;line-height:1.6">
<h1 style="color:#fb4604">Aureus non è ancora buildata</h1>
<p>Manca <code>{PLATFORM_DIST}</code>.</p>
<p>Esegui, dentro <code>EmpireDesk/platform/</code>:</p>
<pre style="background:#12171b;padding:14px 16px;border-radius:10px">npm install
npm run build</pre>
<p>Poi riavvia Empire Desk.</p>
<p><a href="/legacy" style="color:#fb4604">Apri la vecchia UI launcher (fallback) &rarr;</a></p>
</body></html>"""


def _platform_index_html() -> str | None:
    idx = PLATFORM_DIST / "index.html"
    return idx.read_text(encoding="utf-8") if idx.exists() else None


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

    def _send_html(self, html: str, code: int = 200) -> None:
        body = html.encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _serve_platform_asset(self, path: str) -> bool:
        """Serve un file statico REALE da platform/dist/<path>. False se non esiste
        (o path non valido) -> il chiamante passa al fallback SPA (index.html)."""
        try:
            rel = path.lstrip("/")
            if not rel:
                return False
            dist_root = PLATFORM_DIST.resolve()
            candidate = (PLATFORM_DIST / rel).resolve()
            if not candidate.is_relative_to(dist_root) or not candidate.is_file():
                return False
        except (OSError, ValueError):
            return False
        ctype = mimetypes.guess_type(str(candidate))[0] or "application/octet-stream"
        body = candidate.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)
        return True

    def do_GET(self):  # noqa: N802
        path = self.path.split("?", 1)[0]
        if path in ("/legacy", "/legacy/"):
            self._send_html(_legacy_html())
            return
        if path.startswith("/api/"):
            self.send_response(404)
            self.end_headers()
            return
        if path != "/" and self._serve_platform_asset(path):
            return
        # "/" o route client-side di react-router (es. /kanban): serve sempre index.html
        # (fallback SPA standard) — se platform/dist/ non è buildata, pagina di aiuto onesta.
        html = _platform_index_html()
        self._send_html(html if html is not None else _platform_missing_html())

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
            self._send_json({"results": global_selftest()})
        elif route == "api/modules":
            self._send_json({"modules": modules_public()})
        elif route.startswith("api/") and route[len("api/"):] in _MODULE_ROUTES:
            self._send_json(_call_module_route(route[len("api/"):], payload))
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
    start_module_background_tasks()
    PROFILE_DIR.mkdir(parents=True, exist_ok=True)
    cmd = [
        chrome, f"--app=http://127.0.0.1:{port}/",
        f"--user-data-dir={PROFILE_DIR}",
        "--window-size=1360,860",
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
        return global_selftest()

    def modules(self):
        return modules_public()

    def call(self, route, payload=None):
        return _call_module_route(route, payload)


def main_webview() -> int:
    import webview  # richiede pywebview + Edge WebView2 runtime

    port = _start_server()
    start_module_background_tasks()
    api = _WebApi()
    webview.create_window(
        "Empire Desk", url=f"http://127.0.0.1:{port}/", js_api=api,
        width=1360, height=860, min_size=(1100, 720),
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
    start_module_background_tasks()
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
    for t in all_tiles():
        if t["kind"] == "readonly":
            continue
        b = tk.Button(btnbar, text=f"{t['name']}", command=lambda i=t["id"]: _launch(i),
                      bg="#3f4f5a", fg="#ffffff", relief="flat", padx=10, pady=6)
        b.pack(side="left", padx=(0, 8), pady=4)

    def _poll_all():
        for t in all_tiles():
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
    results = global_selftest()
    ok_all = True
    for r in results:
        status = "OK " if r["ok"] else "FAIL"
        print(f"[{status}] {r['id']:<20} {r['name']:<28} {r['detail']}")
        ok_all = ok_all and r["ok"]
    print(f"\nREPO_ROOT = {REPO_ROOT}")
    if _LOADED_MODULES:
        print(f"Moduli caricati: {', '.join(m['id'] for m in _LOADED_MODULES)}")
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
