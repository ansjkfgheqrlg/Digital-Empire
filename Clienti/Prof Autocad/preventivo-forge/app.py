#!/usr/bin/env python3
"""
app.py — PreventivoForge Desktop (Half B / Gael).

App Windows con interfaccia grafica (argento, minimal, professionale) attorno al motore
PreventivoForge: incolli il link mobile.de → premi un bottone → esce il PDF (si apre da solo).

Non riscrive la pipeline: orchestra `run.py` (Half A/Max) in un thread, mostrando i passaggi in
diretta e aprendo il PDF finale. Pensata per il packaging in .exe (PyInstaller) → il concessionario
la usa senza installare Python. Serve solo Google Chrome sul PC.

Uso dev:   python app.py
Selftest:  python app.py --selftest <annuncio.html> <foto_dir>   (pipeline headless, senza GUI)
"""
from __future__ import annotations

import logging
import os
import queue
import sys
import threading
from pathlib import Path


# --------------------------------------------------------------------------- #
# Percorsi (dev + frozen PyInstaller)
# --------------------------------------------------------------------------- #
def _base_dir() -> Path:
    """Cartella del progetto (dove stanno run.py, implementation/, templates/, concessionarie/)."""
    if getattr(sys, "frozen", False):
        # .exe: i file di lavoro (runs/, concessionarie/) stanno accanto all'eseguibile
        return Path(sys.executable).resolve().parent
    return Path(__file__).resolve().parent


BASE_DIR = _base_dir()
IMPL_DIR = BASE_DIR / "implementation"
# in frozen onedir i moduli bundlati stanno anche in _MEIPASS
for _p in (IMPL_DIR, Path(getattr(sys, "_MEIPASS", BASE_DIR)) / "implementation", BASE_DIR):
    if _p.exists() and str(_p) not in sys.path:
        sys.path.insert(0, str(_p))


def _fix_frozen_paths() -> None:
    """Nell'.exe (frozen) i dati bundlati stanno in _MEIPASS (sola lettura). Le cartelle
    SCRIVIBILI (runs/, logs/) devono stare ACCANTO all'eseguibile, non nel temp bundle.
    common.py (Half A) le calcola da __file__ → qui le reindirizziamo senza toccare quel file."""
    if not getattr(sys, "frozen", False):
        return
    try:
        import common
        common.RUNS_DIR = BASE_DIR / "runs"
        common.LOGS_DIR = BASE_DIR / "logs"
        common.RUNS_DIR.mkdir(parents=True, exist_ok=True)
        common.LOGS_DIR.mkdir(parents=True, exist_ok=True)
        # concessionari accanto all'exe (app clonata dalla fabbrica): se presente ha priorità
        import dealers
        _cand = BASE_DIR / "concessionarie"
        if _cand.exists():
            dealers.DEALERS_DIR = _cand
        # .env accanto all'exe (chiave riserva AI, ecc.) → in os.environ
        try:
            from dotenv import load_dotenv
            _envf = BASE_DIR / ".env"
            if _envf.exists():
                load_dotenv(_envf)
        except Exception:
            pass
    except Exception:
        pass


_fix_frozen_paths()


# --------------------------------------------------------------------------- #
# Brand (identità della singola app, per-concessionario)
# --------------------------------------------------------------------------- #
def _load_brand() -> dict:
    """Ogni copia dell'app ha un `brand.json` accanto all'exe con il SUO concessionario:
       {"dealer_id": "novacar", "display_name": "Novacar srl"}.
    Assente (sviluppo) → default Novacar, non bloccato (mostra tutti i dealer)."""
    default = {"dealer_id": "novacar", "display_name": "Novacar srl", "locked": False}
    try:
        import json as _json
        p = BASE_DIR / "brand.json"
        if p.exists():
            b = _json.loads(p.read_text(encoding="utf-8"))
            return {
                "dealer_id": (b.get("dealer_id") or "novacar").strip(),
                "display_name": (b.get("display_name") or "Novacar srl").strip(),
                "locked": True,
            }
    except Exception:
        pass
    return default


_BRAND = _load_brand()
BRAND_TITLE = f"PreventivoForge — {_BRAND['display_name']}"


# --------------------------------------------------------------------------- #
# Motore: esegue la pipeline (run.main) in-process
# --------------------------------------------------------------------------- #
class _QueueLogHandler(logging.Handler):
    """Inoltra i log della pipeline a una coda thread-safe (per la GUI)."""

    def __init__(self, q: "queue.Queue[str]"):
        super().__init__()
        self.q = q

    def emit(self, record: logging.LogRecord) -> None:
        try:
            self.q.put(self.format(record))
        except Exception:
            pass


def _newest_pdf() -> Path | None:
    runs = BASE_DIR / "runs"
    if not runs.exists():
        return None
    pdfs = sorted(runs.glob("*/preventivo_*.pdf"), key=lambda p: p.stat().st_mtime, reverse=True)
    return pdfs[0] if pdfs else None


# Frasi PULITE mostrate in GUI (il log tecnico completo resta comunque nei file logs/).
_MILESTONES = [
    ("=== PreventivoForge run", "▶️  Avvio…"),
    ("S1_scraping -> running",  "🔎  Apro l'annuncio e scarico le foto…"),
    ("S2_parsing -> running",   "📋  Leggo i dati dell'auto…"),
    ("S3_translate_copy -> running", "🇮🇹  Traduco in italiano…"),
    ("S4_pricing -> running",   "💶  Calcolo il prezzo…"),
    ("S5_pdf_render -> running", "📄  Creo il preventivo PDF…"),
    ("GATE_R -> passed",        "✅  Controllo qualità superato…"),
]


class _StreamToQueue:
    """File-like che FILTRA ciò che la pipeline stampa: alla GUI arrivano SOLO poche frasi
    chiare (le milestone qui sopra), non il log tecnico (che resta nei file logs/).
    Serve anche sotto pythonw/.exe dove sys.stdout è None (evita il crash delle print())."""

    def __init__(self, q):
        self.q = q
        self._buf = ""
        self._seen = set()

    def write(self, s):
        s = s or ""
        self._buf += s
        while "\n" in self._buf:
            line, self._buf = self._buf.split("\n", 1)
            self._emit(line)
        return len(s)

    def _emit(self, line):
        if self.q is None:
            return
        for key, friendly in _MILESTONES:
            if key in line and friendly not in self._seen:
                self._seen.add(friendly)
                try:
                    self.q.put(friendly)
                except Exception:
                    pass
                return  # una sola frase per riga, il resto si scarta

    def flush(self):
        pass

    def isatty(self):
        return False


# codice uscita run.py → messaggio umano
_CODE_MSG = {
    2: "scraping da mobile.de fallito (anti-bot Akamai o link non valido)",
    3: "estrazione incompleta: mancano dati o foto (Gate A)",
    4: "calcolo del prezzo fallito",
    5: "traduzione non conforme, tedesco residuo (Gate B)",
    6: "prezzo non verificabile (Gate C)",
    7: "PDF non conforme alle regole (Gate D)",
    8: "foto non conformi: mancanti o tagliate (Gate IMG / R-09)",
    9: "PDF non conforme alle REGOLE-SACRE (Gate R)",
    10: "abbonamento sospeso: contatta il fornitore per riattivare il servizio",
}


def run_pipeline(url: str, dealer: str, log_queue: "queue.Queue[str]" | None = None) -> tuple[bool, Path | None, str]:
    """Esegue la pipeline PreventivoForge su un URL. Ritorna (ok, pdf_path, messaggio).
    Reindirizza stdout/stderr sulla coda: mostra i passaggi in diretta E evita il crash
    delle print() quando l'app gira senza console (pythonw / .exe)."""
    os.chdir(BASE_DIR)  # run.py lavora con path relativi al progetto
    # Scraping con Chrome VISIBILE (headful): l'anti-bot Akamai di mobile.de blocca l'headless.
    os.environ["PLAYWRIGHT_HEADLESS"] = "false"
    os.environ["PF_NO_OPEN"] = "1"  # il PDF lo apre la GUI (evita doppia apertura)

    out_bak, err_bak = sys.stdout, sys.stderr
    # redirige se c'è una coda (mostra i passaggi in GUI) O se manca la console
    # (pythonw/.exe: sys.stdout è None → le print() di run.py andrebbero in crash)
    if log_queue is not None or sys.stdout is None or sys.stderr is None:
        sink = _StreamToQueue(log_queue)
        sys.stdout = sink
        sys.stderr = sink
    try:
        import importlib
        # ricarica i moduli Half B (glossario/template/gate) così le correzioni si applicano
        # al prossimo "Genera" senza ricostruire l'app (in .exe frozen il reload è no-op sicuro)
        for _m in ("glossary_de_it", "translate_copy", "render_pdf", "qa_gate"):
            if _m in sys.modules:
                try:
                    importlib.reload(sys.modules[_m])
                except Exception:
                    pass
        import run as run_mod
        importlib.reload(run_mod)  # nuovo RunContext/argv a ogni click
        argv_bak = sys.argv[:]
        sys.argv = ["run.py", url, "--dealer", dealer]
        try:
            code = run_mod.main()
        finally:
            sys.argv = argv_bak
        if code != 0:
            return False, None, "Non riuscito: " + _CODE_MSG.get(code, f"codice {code}") + ". Vedi il dettaglio sotto."
        pdf = _newest_pdf()
        if not pdf or not pdf.exists():
            return False, None, "Pipeline conclusa ma PDF non trovato. Vedi il dettaglio sotto."
        return True, pdf, f"Preventivo pronto: {pdf.name}"
    except Exception as exc:  # noqa: BLE001
        import traceback
        if log_queue is not None:
            try:
                log_queue.put("ERRORE: " + repr(exc))
                log_queue.put(traceback.format_exc())
            except Exception:
                pass
        return False, None, f"Errore: {exc}"
    finally:
        sys.stdout, sys.stderr = out_bak, err_bak


def _open_file(path: Path) -> None:
    try:
        if os.name == "nt":
            os.startfile(str(path))  # type: ignore[attr-defined]
        elif sys.platform == "darwin":
            import subprocess
            subprocess.Popen(["open", str(path)])
        else:
            import subprocess
            subprocess.Popen(["xdg-open", str(path)])
    except Exception:
        pass


def _list_dealers() -> list[str]:
    # app brandizzata (brand.json presente) → mostra SOLO il proprio concessionario
    if _BRAND.get("locked"):
        return [_BRAND["dealer_id"]]
    d = BASE_DIR / "concessionarie"
    if not d.exists():
        return [_BRAND["dealer_id"]]
    out = sorted(p.name for p in d.iterdir() if (p / "config.json").exists())
    return out or [_BRAND["dealer_id"]]


# --------------------------------------------------------------------------- #
# GUI (Tkinter) — tema argento / minimal
# --------------------------------------------------------------------------- #
# Palette
C_BG = "#E9ECEF"       # argento chiaro
C_CARD = "#FFFFFF"
C_HEAD = "#37474F"     # slate scuro (header)
C_ACCENT = "#546E7A"   # slate
C_ACCENT_HOVER = "#455A64"
C_TEXT = "#263238"
C_MUTED = "#78909C"
C_OK = "#2E7D32"
C_ERR = "#C62828"
C_LOGBG = "#F5F6F7"


class PreventivoApp:
    def __init__(self, root):
        import tkinter as tk
        from tkinter import ttk
        self.tk = tk
        self.root = root
        self.q: "queue.Queue[str]" = queue.Queue()
        self._busy = False

        root.title(BRAND_TITLE)
        root.configure(bg=C_BG)
        root.minsize(680, 560)
        try:
            root.geometry("720x600")
        except Exception:
            pass

        # ---- Header ----
        header = tk.Frame(root, bg=C_HEAD, height=76)
        header.pack(fill="x", side="top")
        header.pack_propagate(False)
        tk.Label(header, text="PreventivoForge", bg=C_HEAD, fg="#FFFFFF",
                 font=("Segoe UI Semibold", 20)).pack(anchor="w", padx=24, pady=(14, 0))
        tk.Label(header, text="Da annuncio mobile.de al preventivo PDF in italiano",
                 bg=C_HEAD, fg="#B0BEC5", font=("Segoe UI", 10)).pack(anchor="w", padx=24)

        # ---- Corpo ----
        body = tk.Frame(root, bg=C_BG)
        body.pack(fill="both", expand=True, padx=22, pady=18)

        # Card input
        card = tk.Frame(body, bg=C_CARD, bd=0, highlightbackground="#CFD8DC",
                        highlightthickness=1)
        card.pack(fill="x", pady=(0, 14))
        pad = {"padx": 18, "pady": 6}

        tk.Label(card, text="Link annuncio mobile.de", bg=C_CARD, fg=C_TEXT,
                 font=("Segoe UI Semibold", 11)).grid(row=0, column=0, sticky="w", **pad)
        self.url_var = tk.StringVar()
        self.url_entry = tk.Entry(card, textvariable=self.url_var, font=("Segoe UI", 11),
                                  relief="flat", bg=C_LOGBG, fg=C_TEXT, insertbackground=C_TEXT)
        self.url_entry.grid(row=1, column=0, columnspan=2, sticky="we", padx=18, pady=(0, 10),
                            ipady=7)
        self.url_entry.focus_set()

        tk.Label(card, text="Concessionaria", bg=C_CARD, fg=C_TEXT,
                 font=("Segoe UI Semibold", 11)).grid(row=2, column=0, sticky="w", padx=18)
        self.dealer_var = tk.StringVar(value=_list_dealers()[0])
        self.dealer_menu = ttk.Combobox(card, textvariable=self.dealer_var, state="readonly",
                                        values=_list_dealers(), font=("Segoe UI", 10))
        self.dealer_menu.grid(row=3, column=0, sticky="w", padx=18, pady=(0, 16))

        self.btn = tk.Button(card, text="Genera preventivo", command=self._on_generate,
                             bg=C_ACCENT, fg="#FFFFFF", activebackground=C_ACCENT_HOVER,
                             activeforeground="#FFFFFF", relief="flat", cursor="hand2",
                             font=("Segoe UI Semibold", 11), padx=18, pady=9, bd=0)
        self.btn.grid(row=3, column=1, sticky="e", padx=18, pady=(0, 16))
        card.columnconfigure(0, weight=1)

        # Status
        self.status = tk.Label(body, text="Pronto. Incolla un link e premi «Genera preventivo».",
                               bg=C_BG, fg=C_MUTED, font=("Segoe UI", 10), anchor="w")
        self.status.pack(fill="x", pady=(0, 6))

        # Log
        logframe = tk.Frame(body, bg=C_CARD, highlightbackground="#CFD8DC", highlightthickness=1)
        logframe.pack(fill="both", expand=True)
        tk.Label(logframe, text="Avanzamento", bg=C_CARD, fg=C_MUTED,
                 font=("Segoe UI", 9)).pack(anchor="w", padx=12, pady=(8, 0))
        self.logbox = tk.Text(logframe, height=10, bg=C_LOGBG, fg=C_TEXT, relief="flat",
                              font=("Consolas", 9), wrap="word", state="disabled",
                              padx=10, pady=8)
        self.logbox.pack(fill="both", expand=True, padx=12, pady=10)

        # footer
        tk.Label(root, text="Serve Google Chrome installato · nessun costo per preventivo · "
                            "il PDF si apre da solo", bg=C_BG, fg=C_MUTED,
                 font=("Segoe UI", 8)).pack(side="bottom", pady=(0, 8))

        self._hover_bind()
        self.root.after(120, self._drain_queue)

    # -- interazioni --
    def _hover_bind(self):
        self.btn.bind("<Enter>", lambda e: self.btn.config(bg=C_ACCENT_HOVER) if not self._busy else None)
        self.btn.bind("<Leave>", lambda e: self.btn.config(bg=C_ACCENT) if not self._busy else None)

    def _log(self, line: str, color: str | None = None):
        self.logbox.config(state="normal")
        self.logbox.insert("end", line + "\n")
        self.logbox.see("end")
        self.logbox.config(state="disabled")

    def _set_status(self, text: str, color: str = C_MUTED):
        self.status.config(text=text, fg=color)

    def _on_generate(self):
        if self._busy:
            return
        url = self.url_var.get().strip()
        if not url or "mobile.de" not in url:
            self._set_status("Incolla un link valido di mobile.de.", C_ERR)
            return
        self._busy = True
        self.btn.config(text="Generazione in corso…", bg=C_MUTED, state="disabled")
        self.logbox.config(state="normal"); self.logbox.delete("1.0", "end"); self.logbox.config(state="disabled")
        self._set_status("Sto generando il preventivo… (si aprirà Chrome, lascialo lavorare)", C_ACCENT)
        dealer = self.dealer_var.get()
        threading.Thread(target=self._worker, args=(url, dealer), daemon=True).start()

    def _worker(self, url: str, dealer: str):
        ok, pdf, msg = run_pipeline(url, dealer, self.q)
        self.q.put(("__DONE__", ok, str(pdf) if pdf else "", msg))

    def _drain_queue(self):
        try:
            while True:
                item = self.q.get_nowait()
                if isinstance(item, tuple) and item and item[0] == "__DONE__":
                    _, ok, pdf, msg = item
                    self._finish(ok, pdf, msg)
                else:
                    self._log(str(item))
        except queue.Empty:
            pass
        self.root.after(120, self._drain_queue)

    def _finish(self, ok: bool, pdf: str, msg: str):
        self._busy = False
        self.btn.config(text="Genera preventivo", bg=C_ACCENT, state="normal")
        if ok:
            self._set_status("✓ " + msg, C_OK)
            self._log("PDF: " + pdf)
            if pdf:
                _open_file(Path(pdf))
        else:
            self._set_status("✗ " + msg, C_ERR)


def main_gui() -> int:
    import tkinter as tk
    root = tk.Tk()
    PreventivoApp(root)
    root.mainloop()
    return 0


# --------------------------------------------------------------------------- #
# GUI PREMIUM — pywebview (HTML/CSS luxury) + bridge Python↔JS
# --------------------------------------------------------------------------- #
def _ui_html_path() -> Path | None:
    for base in (BASE_DIR, Path(getattr(sys, "_MEIPASS", BASE_DIR))):
        p = base / "ui" / "index.html"
        if p.exists():
            return p
    return None


class _WebApi:
    """Ponte esposto al JS della finestra premium. La UI chiama generate()/poll()/dealers()."""

    def __init__(self):
        self.q: "queue.Queue[str]" = queue.Queue()
        self._done = False
        self._ok = False
        self._pdf = ""
        self._msg = ""
        self._running = False

    def dealers(self):
        return _list_dealers()

    def generate(self, url: str, dealer: str):
        if self._running:
            return {"error": "generazione già in corso"}
        url = (url or "").strip()
        if not url or "mobile.de" not in url.lower():
            return {"error": "Incolla un link valido di mobile.de."}
        self.q = queue.Queue()
        self._done = self._ok = False
        self._pdf = self._msg = ""
        self._running = True
        threading.Thread(target=self._worker, args=(url, dealer or "novacar"), daemon=True).start()
        return {"started": True}

    def _worker(self, url: str, dealer: str):
        try:
            ok, pdf, msg = run_pipeline(url, dealer, self.q)
        except Exception as exc:  # noqa: BLE001
            ok, pdf, msg = False, None, f"Errore: {exc}"
        self._ok = ok
        self._pdf = str(pdf) if pdf else ""
        self._msg = msg or ""
        self._done = True
        self._running = False
        if ok and pdf:
            _open_file(Path(pdf))

    def poll(self):
        lines = []
        try:
            while True:
                lines.append(self.q.get_nowait())
        except queue.Empty:
            pass
        return {"lines": lines, "done": self._done, "ok": self._ok,
                "pdf": self._pdf, "msg": self._msg, "running": self._running}


def main_webview() -> int:
    """Finestra premium HTML/CSS via pywebview. Alza RuntimeError se non disponibile → fallback Tkinter."""
    import webview  # richiede pywebview + (Windows) Edge WebView2 runtime

    html_path = _ui_html_path()
    if not html_path:
        raise RuntimeError("ui/index.html non trovato")
    html = html_path.read_text(encoding="utf-8")
    api = _WebApi()
    webview.create_window(
        BRAND_TITLE,
        html=html, js_api=api,
        width=800, height=700, min_size=(700, 620),
        background_color="#e7ebee",
    )
    webview.start()
    return 0


# --------------------------------------------------------------------------- #
# Entry point
# --------------------------------------------------------------------------- #
if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1] == "--selftest":
        # pipeline headless via fallback --manual (no GUI): verifica il wiring app→run
        _html = sys.argv[2] if len(sys.argv) > 2 else ""
        _foto = sys.argv[3] if len(sys.argv) > 3 else ""
        os.chdir(BASE_DIR)
        # in .exe windowed sys.stdout è None → le print() di run.py crasherebbero:
        # reindirizza su file così il selftest gira headless e lascia una traccia leggibile.
        if sys.stdout is None or sys.stderr is None:
            _logf = open(BASE_DIR / "selftest.log", "w", encoding="utf-8", buffering=1)
            sys.stdout = _logf
            sys.stderr = _logf
        import run as run_mod
        sys.argv = ["run.py", "--manual", _html, "--foto", _foto, "--dealer", _BRAND["dealer_id"]]
        raise SystemExit(run_mod.main())
    # GUI premium (pywebview); se non disponibile → fallback Tkinter (nessun PC resta senza app)
    try:
        _code = main_webview()
    except Exception:
        _code = main_gui()
    raise SystemExit(_code)
