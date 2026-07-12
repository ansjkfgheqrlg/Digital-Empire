"""
Digital Empire — Auto Publisher App
Interface per gestire la pubblicazione automatica su Instagram.
"""
import sys, json, subprocess, threading
from pathlib import Path
from datetime import datetime

import customtkinter as ctk
from tkinter import messagebox

# --- Path resolution (funziona sia da .py che da .exe compilato)
if getattr(sys, "frozen", False):
    WORKFLOW = Path(sys.executable).parent
else:
    WORKFLOW = Path(__file__).parent

PUBLISH_SCRIPT = WORKFLOW / "scripts" / "ig_carousel_publish.py"
HEALTH_SCRIPT  = WORKFLOW / "scripts" / "health_check.py"
SETUP_SCRIPT   = WORKFLOW / "setup_scheduler.py"
PUBLISHED_LOG  = WORKFLOW / "published.json"
CAROSELLI_DIR  = Path(r"C:\Users\Utente\Desktop\qui tutto\Digital Empire\Lancio corso skill beast\Page\caroselli - Agency\Nuovi")
PYTHON         = sys.executable if not getattr(sys, "frozen", False) else "python"
VALID_EXT      = {".png", ".jpg", ".jpeg", ".webp"}

# --- Colori Digital Empire
BG     = "#080808"
CARD   = "#111111"
CARD2  = "#181818"
ACCENT = "#FF3D00"
ACCENT2 = "#CC3000"
WHITE  = "#FFFFFF"
GRAY   = "#555555"
LGRAY  = "#888888"
GREEN  = "#22C55E"
RED    = "#EF4444"
BORDER = "#222222"

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


class DEPublisher(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Digital Empire Publisher")
        self.geometry("560x720")
        self.resizable(False, False)
        self.configure(fg_color=BG)

        self._running  = False
        self._carousels = []
        self._pub       = {}

        self._build()
        self.after(300, lambda: threading.Thread(target=self._refresh, daemon=True).start())

    # ── UI BUILD ────────────────────────────────────────────────────────────

    def _build(self):
        # Header
        hdr = ctk.CTkFrame(self, fg_color="#0C0C0C", corner_radius=0, height=64)
        hdr.pack(fill="x")
        hdr.pack_propagate(False)

        ctk.CTkLabel(
            hdr, text="⚡  DIGITAL EMPIRE",
            font=ctk.CTkFont(family="Arial", size=20, weight="bold"),
            text_color=WHITE,
        ).pack(side="left", padx=24)

        ctk.CTkLabel(
            hdr, text="AUTO PUBLISHER",
            font=ctk.CTkFont(size=10),
            text_color=ACCENT,
        ).pack(side="left")

        ver = ctk.CTkLabel(hdr, text="v2.0", font=ctk.CTkFont(size=10), text_color=GRAY)
        ver.pack(side="right", padx=20)

        # Divider
        ctk.CTkFrame(self, fg_color=BORDER, height=1, corner_radius=0).pack(fill="x")

        # Status card
        sc = ctk.CTkFrame(self, fg_color=CARD, corner_radius=12)
        sc.pack(fill="x", padx=18, pady=(16, 0))

        top = ctk.CTkFrame(sc, fg_color="transparent")
        top.pack(fill="x", padx=16, pady=(14, 4))

        self._dot = ctk.CTkLabel(top, text="●", font=ctk.CTkFont(size=20), text_color=GRAY)
        self._dot.pack(side="left")

        self._status_lbl = ctk.CTkLabel(
            top, text="Controllo...",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color=LGRAY,
        )
        self._status_lbl.pack(side="left", padx=10)

        ctk.CTkButton(
            top, text="↻", width=32, height=28, corner_radius=6,
            fg_color=CARD2, hover_color=BORDER, text_color=LGRAY,
            font=ctk.CTkFont(size=14),
            command=lambda: threading.Thread(target=self._refresh, daemon=True).start(),
        ).pack(side="right")

        self._status_sub = ctk.CTkLabel(sc, text="", font=ctk.CTkFont(size=11), text_color=GRAY)
        self._status_sub.pack(anchor="w", padx=18, pady=(0, 14))

        # Next carousel card
        nc = ctk.CTkFrame(self, fg_color=CARD, corner_radius=12)
        nc.pack(fill="x", padx=18, pady=(10, 0))

        ctk.CTkLabel(nc, text="PROSSIMO CAROSELLO", font=ctk.CTkFont(size=9), text_color=GRAY).pack(anchor="w", padx=16, pady=(12, 2))

        nr = ctk.CTkFrame(nc, fg_color="transparent")
        nr.pack(fill="x", padx=16, pady=(0, 12))

        self._next_name = ctk.CTkLabel(nr, text="—", font=ctk.CTkFont(size=15, weight="bold"), text_color=WHITE)
        self._next_name.pack(side="left")

        self._next_sub = ctk.CTkLabel(nr, text="", font=ctk.CTkFont(size=11), text_color=GRAY)
        self._next_sub.pack(side="left", padx=10)

        # Actions
        af = ctk.CTkFrame(self, fg_color="transparent")
        af.pack(fill="x", padx=18, pady=(14, 0))

        self._pub_btn = ctk.CTkButton(
            af, text="🚀   PUBBLICA ORA",
            height=54, corner_radius=10,
            fg_color=ACCENT, hover_color=ACCENT2,
            text_color=WHITE,
            font=ctk.CTkFont(size=16, weight="bold"),
            command=self._on_publish,
        )
        self._pub_btn.pack(fill="x", pady=(0, 10))

        # Schedule row
        sr = ctk.CTkFrame(af, fg_color=CARD, corner_radius=10)
        sr.pack(fill="x", pady=(0, 8))

        ctk.CTkLabel(
            sr, text="📅  Orario automatico",
            font=ctk.CTkFont(size=12), text_color=LGRAY,
        ).pack(side="left", padx=14, pady=12)

        self._time_entry = ctk.CTkEntry(
            sr, width=68, height=32, placeholder_text="18:00",
            font=ctk.CTkFont(size=13, weight="bold"),
            fg_color=CARD2, border_color=BORDER, text_color=WHITE,
            corner_radius=7,
        )
        self._time_entry.pack(side="left", padx=6)

        ctk.CTkButton(
            sr, text="IMPOSTA", width=82, height=32, corner_radius=7,
            fg_color="#1C1C1C", hover_color="#2A2A2A",
            text_color=WHITE, border_width=1, border_color=BORDER,
            font=ctk.CTkFont(size=11, weight="bold"),
            command=self._on_schedule,
        ).pack(side="left", padx=4)

        ctk.CTkButton(
            sr, text="✕", width=32, height=32, corner_radius=7,
            fg_color="#1C1C1C", hover_color="#2A0000",
            text_color=RED, border_width=1, border_color=BORDER,
            font=ctk.CTkFont(size=12),
            command=self._on_remove_sched,
        ).pack(side="left")

        # Lista button
        ctk.CTkButton(
            af, text="📋   LISTA CAROSELLI",
            height=40, corner_radius=9,
            fg_color=CARD, hover_color=CARD2,
            text_color=WHITE, border_width=1, border_color=BORDER,
            font=ctk.CTkFont(size=13),
            command=self._show_list,
        ).pack(fill="x")

        # Log
        ctk.CTkLabel(
            self, text="LOG", font=ctk.CTkFont(size=9), text_color=GRAY,
        ).pack(anchor="w", padx=20, pady=(14, 3))

        self._log = ctk.CTkTextbox(
            self, height=170,
            fg_color="#0A0A0A", text_color="#555",
            font=ctk.CTkFont(family="Courier New", size=10),
            corner_radius=10, border_width=1, border_color=BORDER,
            state="disabled",
        )
        self._log.pack(fill="x", padx=18, pady=(0, 12))

        ctk.CTkLabel(
            self, text="Digital Empire  ·  2026",
            font=ctk.CTkFont(size=9), text_color="#222",
        ).pack(pady=(0, 10))

    # ── HELPERS ─────────────────────────────────────────────────────────────

    def _log_write(self, msg: str):
        self._log.configure(state="normal")
        ts = datetime.now().strftime("%H:%M:%S")
        self._log.insert("end", f"[{ts}] {msg}\n")
        self._log.see("end")
        self._log.configure(state="disabled")

    def _run(self, args, timeout=300):
        return subprocess.run(
            [PYTHON] + [str(a) for a in args],
            capture_output=True, text=True,
            encoding="utf-8", errors="replace",
            timeout=timeout, cwd=str(WORKFLOW),
        )

    def _load_carousels(self):
        self._pub = {}
        if PUBLISHED_LOG.exists():
            try:
                self._pub = json.loads(PUBLISHED_LOG.read_text("utf-8"))
            except Exception:
                pass

        self._carousels = []
        if not CAROSELLI_DIR.exists():
            return
        for f in sorted(CAROSELLI_DIR.iterdir()):
            if not f.is_dir():
                continue
            imgs = [x for x in f.iterdir() if x.suffix.lower() in VALID_EXT]
            cap  = (f / "caption.txt").exists()
            if f.name in self._pub:
                stato = "PUBBLICATO " + self._pub[f.name].get("published_at", "")[:10]
            elif imgs and cap:
                stato = "PRONTO"
            elif not imgs:
                stato = "no immagini"
            else:
                stato = "no caption"
            self._carousels.append({"nome": f.name, "img": len(imgs), "stato": stato})

    # ── REFRESH ─────────────────────────────────────────────────────────────

    def _refresh(self):
        self.after(0, self._log_write, "Controllo sistema...")
        try:
            r = self._run([HEALTH_SCRIPT], timeout=30)
        except Exception as e:
            self.after(0, self._log_write, f"Errore health check: {e}")
            return

        self._load_carousels()
        ok = r.returncode == 0
        n_ready = len([c for c in self._carousels if c["stato"] == "PRONTO"])
        n_pub   = len([c for c in self._carousels if c["stato"].startswith("PUBBLICATO")])

        def _update():
            if ok:
                self._dot.configure(text_color=GREEN)
                self._status_lbl.configure(text="Sistema pronto", text_color=WHITE)
                self._status_sub.configure(text=f"{n_ready} pronti  ·  {n_pub} già pubblicati")
                self._log_write(f"OK — {n_ready} caroselli pronti")
            else:
                self._dot.configure(text_color=RED)
                self._status_lbl.configure(text="Problema rilevato", text_color=RED)
                errs = [l for l in r.stdout.splitlines() if "[ERR]" in l]
                sub  = errs[0].replace("[ERR]", "").strip() if errs else "Controlla il log"
                self._status_sub.configure(text=sub)
                self._log_write("ERRORE: " + sub)

            ready = [c for c in self._carousels if c["stato"] == "PRONTO"]
            if ready:
                self._next_name.configure(text=ready[0]["nome"])
                self._next_sub.configure(text=f"{ready[0]['img']} slide")
            else:
                self._next_name.configure(text="Nessuno")
                self._next_sub.configure(text="Aggiungi caroselli")

        self.after(0, _update)

    # ── PUBLISH ─────────────────────────────────────────────────────────────

    def _on_publish(self):
        if self._running:
            return
        ready = [c for c in self._carousels if c["stato"] == "PRONTO"]
        if not ready:
            messagebox.showwarning("Nessun carosello", "Nessun carosello pronto.", parent=self)
            return
        nome = ready[0]["nome"]
        if not messagebox.askyesno("Conferma pubblicazione", f"Pubblica ora:\n\n«{nome}»", parent=self):
            return
        self._running = True
        self._pub_btn.configure(text="⏳   IN CORSO...", state="disabled", fg_color=CARD2)
        self._log_write(f"Avvio: {nome}")
        threading.Thread(target=self._do_publish, args=(nome,), daemon=True).start()

    def _do_publish(self, nome):
        try:
            r = self._run([PUBLISH_SCRIPT, "--folder", nome, "--visible"], timeout=200)
            success = r.returncode == 0
        except Exception as e:
            success = False
            r = type("R", (), {"stdout": str(e), "stderr": ""})()

        def _done():
            self._running = False
            self._pub_btn.configure(text="🚀   PUBBLICA ORA", state="normal", fg_color=ACCENT)
            if success:
                self._log_write(f"PUBBLICATO: {nome}")
                messagebox.showinfo("Pubblicato!", f"Carosello pubblicato:\n«{nome}»", parent=self)
                threading.Thread(target=self._refresh, daemon=True).start()
            else:
                err = (r.stdout or r.stderr or "Errore sconosciuto")[-200:]
                self._log_write(f"FALLITO: {err[:80]}")
                messagebox.showerror("Errore", f"Pubblicazione fallita.\n\n{err[:200]}", parent=self)

        self.after(0, _done)

    # ── SCHEDULE ────────────────────────────────────────────────────────────

    def _on_schedule(self):
        t = self._time_entry.get().strip()
        if not t or ":" not in t or len(t) != 5:
            messagebox.showwarning("Formato errato", "Formato: HH:MM\nEs: 18:00", parent=self)
            return
        self._log_write(f"Impostazione orario: {t}")
        r = self._run([SETUP_SCRIPT, "--time", t], timeout=20)
        if r.returncode == 0:
            messagebox.showinfo("Schedulato!", f"Pubblicazione automatica ogni giorno alle {t}", parent=self)
            self._log_write(f"Scheduler attivo: {t}")
        else:
            messagebox.showerror("Errore", "Errore Task Scheduler.\nProva come Amministratore.", parent=self)

    def _on_remove_sched(self):
        if not messagebox.askyesno("Conferma", "Rimuovere la pubblicazione automatica?", parent=self):
            return
        self._run([SETUP_SCRIPT, "--remove"], timeout=10)
        self._log_write("Scheduler rimosso")
        messagebox.showinfo("Rimosso", "Pubblicazione automatica disattivata.", parent=self)

    # ── LIST ────────────────────────────────────────────────────────────────

    def _show_list(self):
        win = ctk.CTkToplevel(self)
        win.title("Caroselli")
        win.geometry("480x380")
        win.configure(fg_color=BG)
        win.resizable(False, False)
        win.grab_set()

        ctk.CTkLabel(
            win, text="TUTTI I CAROSELLI",
            font=ctk.CTkFont(size=13, weight="bold"), text_color=WHITE,
        ).pack(pady=(16, 8), padx=16, anchor="w")

        sf = ctk.CTkScrollableFrame(win, fg_color=CARD, corner_radius=10)
        sf.pack(fill="both", expand=True, padx=16, pady=(0, 16))

        for c in self._carousels:
            if c["stato"] == "PRONTO":
                col = GREEN
            elif c["stato"].startswith("PUBBLICATO"):
                col = GRAY
            else:
                col = RED

            row = ctk.CTkFrame(sf, fg_color=CARD2, corner_radius=8)
            row.pack(fill="x", pady=3, padx=3)

            ctk.CTkLabel(row, text="●", text_color=col, font=ctk.CTkFont(size=11)).pack(side="left", padx=(10, 6), pady=10)
            ctk.CTkLabel(row, text=c["nome"], font=ctk.CTkFont(size=12, weight="bold"), text_color=WHITE).pack(side="left")
            ctk.CTkLabel(row, text=f"{c['img']} slide", font=ctk.CTkFont(size=10), text_color=GRAY).pack(side="left", padx=8)
            ctk.CTkLabel(row, text=c["stato"], font=ctk.CTkFont(size=10), text_color=col).pack(side="right", padx=12)


if __name__ == "__main__":
    app = DEPublisher()
    app.mainloop()
