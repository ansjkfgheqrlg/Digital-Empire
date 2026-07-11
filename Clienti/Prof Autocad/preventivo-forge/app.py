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
import re
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
    ("S1_scraping -> running",  "Scaricamento foto…"),
    ("S2_parsing -> running",   "Lettura dati…"),
    ("S3_translate_copy -> running", "Traduzione in italiano…"),
    ("S4_pricing -> running",   "Calcolo prezzo…"),
    ("S5_pdf_render -> running", "Creazione PDF…"),
    ("GATE_R -> passed",        "Controllo qualità…"),
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
        low = line.lower()
        # retry anti-bot: aggiorna la fase corrente (l'utente vede che sta lavorando)
        if "riprovo tra" in low or ("tentativo" in low and "challenge" in low) or ("anti-bot" in low and "riprovo" in low):
            m = re.search(r"tentativo (\d+)/(\d+)", line)
            tag = f" {m.group(1)}/{m.group(2)}" if m else ""
            try:
                self.q.put(("phase", f"Anti-bot: ritento{tag}…"))
            except Exception:
                pass
            return
        for key, label in _MILESTONES:
            if key in line and label not in self._seen:
                self._seen.add(label)
                try:
                    self.q.put(("phase", label))
                except Exception:
                    pass
                return  # una sola fase per riga, il resto si scarta

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


# --------------------------------------------------------------------------- #
# Batch: fino a 10 link in una volta
# --------------------------------------------------------------------------- #
MAX_LINKS = 10


def _parse_links(text: str) -> tuple[list[str], str]:
    """Estrae i link mobile.de dal testo (uno per riga o separati da spazi).
    Dedup, tiene l'ordine, massimo MAX_LINKS. Ritorna (links, nota)."""
    seen: set[str] = set()
    urls: list[str] = []
    for tok in re.split(r"\s+", (text or "").strip()):
        t = tok.strip().strip(",;")
        if "mobile.de" in t.lower() and t not in seen:
            seen.add(t)
            urls.append(t)
    note = ""
    if len(urls) > MAX_LINKS:
        note = f"Massimo {MAX_LINKS} link: uso i primi {MAX_LINKS} (ne hai messi {len(urls)})."
        urls = urls[:MAX_LINKS]
    return urls, note


def run_batch(urls: list[str], dealer: str, log_queue: "queue.Queue | None" = None) -> tuple[bool, "Path | None", str]:
    """Esegue la pipeline su PIU' link (max 10). Ogni link è isolato: uno fallito NON ferma
    gli altri. I PDF riusciti finiscono in un'unica cartella. Ritorna (ok_globale, out_dir, msg)."""
    import shutil
    from datetime import datetime

    n = len(urls)
    out_dir = BASE_DIR / f"preventivi_{datetime.now():%Y%m%d-%H%M%S}"
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
    except Exception:
        out_dir = BASE_DIR

    done: list[Path] = []
    fail: list[int] = []
    for i, url in enumerate(urls, 1):
        if log_queue is not None:
            log_queue.put(("link", i, n))
        try:
            ok, pdf, msg = run_pipeline(url, dealer, log_queue)
        except Exception as exc:  # noqa: BLE001
            ok, pdf, msg = False, None, f"Errore: {exc}"
        if ok and pdf and Path(pdf).exists():
            # salva SEMPRE nell'archivio (dal PDF originale in runs/<id>/, con foto e dati)
            try:
                import archivio
                archivio.add(pdf)
            except Exception:
                pass
            dst = out_dir / f"{i:02d}_{Path(pdf).name}"
            try:
                shutil.copyfile(str(pdf), str(dst))
            except Exception:
                dst = Path(pdf)
            done.append(dst)
            if log_queue is not None:
                log_queue.put(("linkdone", i, n, True, ""))
        else:
            fail.append(i)
            if log_queue is not None:
                log_queue.put(("linkdone", i, n, False, msg))

    if log_queue is not None and done:
        log_queue.put(("allpath", str(out_dir)))

    # apertura: 1 solo → il PDF; più di uno → la cartella con tutti i PDF
    if n == 1 and done:
        _open_file(done[0])
    elif done:
        _open_file(out_dir)

    if done and not fail:
        msg = f"Fatti tutti i {len(done)} preventivi." if n > 1 else "Preventivo pronto."
    elif done and fail:
        msg = f"Fatti {len(done)} su {n}. Non riusciti: {', '.join('#'+str(i) for i in fail)} (vedi log)."
    else:
        msg = f"Nessun preventivo generato su {n} link. Controlla i link e il log."
    return (len(done) > 0), out_dir, msg


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

        tk.Label(card, text="Link annunci mobile.de (fino a 10, uno per riga)", bg=C_CARD, fg=C_TEXT,
                 font=("Segoe UI Semibold", 11)).grid(row=0, column=0, sticky="w", **pad)
        self.url_txt = tk.Text(card, height=5, font=("Segoe UI", 10), relief="flat",
                               bg=C_LOGBG, fg=C_TEXT, insertbackground=C_TEXT, wrap="none",
                               padx=8, pady=6)
        self.url_txt.grid(row=1, column=0, columnspan=2, sticky="we", padx=18, pady=(0, 10))
        self.url_txt.focus_set()

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
        self.status = tk.Label(body, text="Pronto. Incolla fino a 10 link (uno per riga) e premi «Genera».",
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
        urls, note = _parse_links(self.url_txt.get("1.0", "end"))
        if not urls:
            self._set_status("Incolla almeno un link di mobile.de (uno per riga, max 10).", C_ERR)
            return
        self._busy = True
        self.btn.config(text="Generazione in corso…", bg=C_MUTED, state="disabled")
        self.logbox.config(state="normal"); self.logbox.delete("1.0", "end"); self.logbox.config(state="disabled")
        if note:
            self._log("⚠️  " + note)
        n = len(urls)
        self._set_status(f"Genero {n} preventiv{'o' if n == 1 else 'i'}… (si aprirà Chrome, lascialo lavorare)", C_ACCENT)
        dealer = self.dealer_var.get()
        threading.Thread(target=self._worker, args=(urls, dealer), daemon=True).start()

    def _worker(self, urls: list, dealer: str):
        ok, out, msg = run_batch(urls, dealer, self.q)
        self.q.put(("__DONE__", ok, str(out) if out else "", msg))

    def _drain_queue(self):
        try:
            while True:
                item = self.q.get_nowait()
                if isinstance(item, tuple) and item:
                    tag = item[0]
                    if tag == "__DONE__":
                        self._finish(item[1], item[2], item[3])
                    elif tag == "link":
                        self._log(f"Preventivo {item[1]}/{item[2]}: in corso…")
                    elif tag == "phase":
                        pass  # (fallback Tkinter: non mostra ogni singola fase)
                    elif tag == "linkdone":
                        i, n, ok = item[1], item[2], item[3]
                        self._log(f"Preventivo {i}/{n}: " + ("Pronto" if ok else "Non riuscito"))
                    elif tag == "allpath":
                        self._log("Tutto caricato in: " + str(item[1]))
                    else:
                        self._log(str(item))
                else:
                    self._log(str(item))
        except queue.Empty:
            pass
        self.root.after(120, self._drain_queue)

    def _finish(self, ok: bool, out: str, msg: str):
        self._busy = False
        self.btn.config(text="Genera preventivo", bg=C_ACCENT, state="normal")
        if ok:
            self._set_status("✓ " + msg, C_OK)
            if out:
                self._log("Cartella preventivi: " + out)  # (già aperta in automatico)
        else:
            self._set_status("✗ " + msg, C_ERR)


def main_gui() -> int:
    import tkinter as tk
    root = tk.Tk()
    PreventivoApp(root)
    root.mainloop()
    # finestra chiusa → svuota l'archivio (riparte vuoto alla prossima apertura)
    try:
        import archivio
        archivio.clear()
    except Exception:
        pass
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

    def generate(self, text: str, dealer: str):
        if self._running:
            return {"error": "generazione già in corso"}
        urls, note = _parse_links(text or "")
        if not urls:
            return {"error": "Incolla almeno un link di mobile.de (uno per riga, max 10)."}
        self.q = queue.Queue()
        self._done = self._ok = False
        self._pdf = self._msg = ""
        self._running = True
        n = len(urls)
        threading.Thread(target=self._worker, args=(urls, dealer or "novacar"), daemon=True).start()
        return {"started": True, "count": n, "note": note}

    def _worker(self, urls: list, dealer: str):
        try:
            ok, out, msg = run_batch(urls, dealer, self.q)
        except Exception as exc:  # noqa: BLE001
            ok, out, msg = False, None, f"Errore: {exc}"
        self._ok = ok
        self._pdf = str(out) if out else ""   # cartella coi PDF (o singolo PDF)
        self._msg = msg or ""
        self._done = True
        self._running = False
        # apertura già gestita da run_batch (PDF singolo o cartella)

    def poll(self):
        items = []
        try:
            while True:
                items.append(self.q.get_nowait())
        except queue.Empty:
            pass
        return {"items": items, "done": self._done, "ok": self._ok,
                "pdf": self._pdf, "msg": self._msg, "running": self._running}

    def archive(self):
        """Voci dell'archivio (blocchi con foto/nome/prezzo) per la GUI."""
        try:
            import archivio
            return archivio.entries()
        except Exception:
            return []

    def open_pdf(self, path: str):
        """Apre un PDF dell'archivio nel visualizzatore/browser."""
        try:
            _open_file(Path(path))
            return {"ok": True}
        except Exception as exc:  # noqa: BLE001
            return {"ok": False, "error": str(exc)}


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
    # finestra chiusa → svuota l'archivio (riparte vuoto alla prossima apertura)
    try:
        import archivio
        archivio.clear()
    except Exception:
        pass
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
