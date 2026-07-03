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
    except Exception:
        pass


_fix_frozen_paths()


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


def run_pipeline(url: str, dealer: str, log_queue: "queue.Queue[str]" | None = None) -> tuple[bool, Path | None, str]:
    """Esegue la pipeline PreventivoForge su un URL. Ritorna (ok, pdf_path, messaggio).
    Cattura i log della pipeline nella coda (per mostrare i passaggi in diretta)."""
    os.chdir(BASE_DIR)  # run.py lavora con path relativi al progetto
    # Scraping con Chrome VISIBILE (headful): l'anti-bot Akamai di mobile.de blocca l'headless.
    # Su IP residenziale il browser reale di solito passa; se compare un captcha, l'utente lo risolve
    # nella finestra. (Solo lo scraping S1 lo legge; il render PDF resta headless a parte.)
    os.environ["PLAYWRIGHT_HEADLESS"] = "false"
    handler = None
    if log_queue is not None:
        handler = _QueueLogHandler(log_queue)
        handler.setFormatter(logging.Formatter("%(message)s"))
        logging.getLogger("annuncioforge").addHandler(handler)
        logging.getLogger("annuncioforge").setLevel(logging.INFO)

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
            return False, None, f"La pipeline si è fermata (codice {code}). Controlla il log qui sotto."
        pdf = _newest_pdf()
        if not pdf or not pdf.exists():
            return False, None, "Pipeline conclusa ma PDF non trovato. Controlla il log."
        return True, pdf, f"Preventivo pronto: {pdf.name}"
    except Exception as exc:  # noqa: BLE001
        return False, None, f"Errore: {exc}"
    finally:
        if handler is not None:
            logging.getLogger("annuncioforge").removeHandler(handler)


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
    d = BASE_DIR / "concessionarie"
    if not d.exists():
        return ["novacar"]
    out = sorted(p.name for p in d.iterdir() if (p / "config.json").exists())
    return out or ["novacar"]


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

        root.title("PreventivoForge — Novacar srl")
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
# Entry point
# --------------------------------------------------------------------------- #
if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1] == "--selftest":
        # pipeline headless via fallback --manual (no GUI): verifica il wiring app→run
        html = sys.argv[2] if len(sys.argv) > 2 else ""
        foto = sys.argv[3] if len(sys.argv) > 3 else ""
        os.chdir(BASE_DIR)
        import run as run_mod
        sys.argv = ["run.py", "--manual", html, "--foto", foto, "--dealer", "novacar"]
        raise SystemExit(run_mod.main())
    raise SystemExit(main_gui())
