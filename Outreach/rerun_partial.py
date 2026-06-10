"""
Digital Empire — Rerun Partial
================================
Rilancia SOLO quello che ha fallito oggi:
  [COMMENTI]    → 100 commenti LinkedIn (quota residua dalla giornata)
  [CONNESSIONI] → 50 connection requests LinkedIn
  [IG-DM]       → 15 DM Instagram + follow-up
  [IG-REPLIES]  → check risposte Instagram (dopo IG-DM)

NON tocca email (potrebbe essere ancora in corso nel terminale principale).

Uso: python rerun_partial.py
"""

import subprocess
import threading
import os
import sys
from datetime import datetime

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HERE    = os.path.dirname(os.path.abspath(__file__))
BASE_LI = os.path.join(HERE, "LinkedIn Automation")
BASE_IG = os.path.join(HERE, "Instagram Automation")

_print_lock = threading.Lock()

_AZ  = "\033[96m"
_OR  = "\033[38;5;208m"
_BLD = "\033[1m"
_RS  = "\033[0m"

LABELS = {
    "COMMENTI":    f"{_AZ}[COMMENTI]   {_RS}",
    "CONNESSIONI": f"{_AZ}[CONNESSIONI]{_RS}",
    "IG-DM":       f"{_OR}[IG-DM]      {_RS}",
    "IG-REPLIES":  f"{_OR}[IG-REPLIES] {_RS}",
    "ORCH":        f"{_BLD}[ORCH]       {_RS}",
}


def log(label, msg):
    ts = datetime.now().strftime("%H:%M:%S")
    with _print_lock:
        prefix = LABELS.get(label, f"[{label}]")
        print(f"{ts}  {prefix}  {msg.rstrip()}", flush=True)


_NOISE = (
    "Traceback (most recent call last)",
    "--- Logging error ---",
    "Call stack:",
    "Message: ",
    "Arguments: (",
    "NoneType: None",
    "During handling of the above",
    "super().run_forever()",
    "self._run_once()",
    "handle._run()",
    "self._context.run(",
    "return codecs.",
    "stream.write(",
    "UnicodeEncodeError",
    "UnicodeDecodeError",
    "charmap' codec",
    "^^^^^^^",
)

def _is_useful(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return False
    for pattern in _NOISE:
        if pattern in line:
            return False
    if stripped.startswith('File "') and '.py"' in stripped:
        return False
    return True


def worker(label: str, cwd: str, cmd: str, results: dict):
    log(label, f"START: {cmd}")
    try:
        proc = subprocess.Popen(
            cmd,
            cwd=cwd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            encoding="utf-8",
            errors="replace",
        )
        for line in proc.stdout:
            line = line.rstrip()
            if _is_useful(line):
                log(label, line)
        proc.wait()
        rc = proc.returncode
        if rc == 0:
            results[label] = "OK"
            log(label, f"\033[92mFINE → OK\033[0m")
        else:
            results[label] = f"ERRORE (exit {rc})"
            log(label, f"FINE → ERRORE (exit {rc})")
    except Exception as e:
        results[label] = f"ECCEZIONE: {e}"
        log(label, f"FINE → ECCEZIONE: {e}")


def main():
    # Verifica sessioni
    li_session = os.path.join(BASE_LI, "linkedin_session.json")
    ig_session = os.path.join(BASE_IG, "instagram_session.json")

    if not os.path.exists(li_session):
        print("❌  Sessione LinkedIn non trovata.")
        print("    Esegui:  python \"LinkedIn Automation\\refresh_session.py\"")
        print("    Poi rilancia questo script.")
        sys.exit(1)

    ig_enabled = os.path.exists(ig_session)
    if not ig_enabled:
        print("⚠   Sessione Instagram non trovata — IG saltato.")

    results = {}

    print()
    print("=" * 60)
    print(f"  RERUN PARTIAL  {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"  Rilancia: COMMENTI + CONNESSIONI + IG-DM")
    print(f"  Email: NON toccata (usa terminale principale)")
    print("=" * 60)
    print()

    # ── Avvia COMMENTI + CONNESSIONI in parallelo ────────────────────────
    log("ORCH", "Avvio COMMENTI + CONNESSIONI in parallelo...")

    r_li = {}
    t_commenti = threading.Thread(
        target=worker,
        args=("COMMENTI", BASE_LI, "python comment_posts.py", r_li),
    )
    t_connessioni = threading.Thread(
        target=worker,
        args=("CONNESSIONI", BASE_LI, "python run_today.py", r_li),
    )

    t_commenti.start()
    t_connessioni.start()

    # ── Avvia IG-DM in parallelo ─────────────────────────────────────────
    r_ig = {}
    if ig_enabled:
        log("ORCH", "Avvio IG-DM in parallelo...")
        t_ig = threading.Thread(
            target=worker,
            args=("IG-DM", BASE_IG, "python run_today.py", r_ig),
        )
        t_ig.start()
    else:
        t_ig = None

    # ── Aspetta IG-DM → lancia IG-REPLIES ────────────────────────────────
    if t_ig:
        t_ig.join()
        log("ORCH", "IG-DM completato → avvio IG-REPLIES...")
        worker("IG-REPLIES", BASE_IG, "python check_replies.py", r_ig)

    # ── Aspetta LinkedIn ──────────────────────────────────────────────────
    t_commenti.join()
    t_connessioni.join()

    # ── Riepilogo ─────────────────────────────────────────────────────────
    print()
    print("=" * 60)
    print("  RERUN COMPLETATO")
    for label, status in {**r_li, **r_ig}.items():
        print(f"    {label:<14} → {status}")
    print("=" * 60)


if __name__ == "__main__":
    main()
