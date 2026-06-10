"""
Digital Empire — LinkedIn Only
================================
Lancia SOLO le operazioni LinkedIn:
  [COMMENTI]    → commenti sui post LinkedIn
  [CONNESSIONI] → connection requests + messaggi

Uso: python run_linkedin_only.py
"""

import subprocess
import threading
import os
import sys
from datetime import datetime

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HERE    = os.path.dirname(os.path.abspath(__file__))
BASE_LI = os.path.join(HERE, "LinkedIn Automation")

_print_lock = threading.Lock()

_AZ  = "\033[96m"
_BLD = "\033[1m"
_RS  = "\033[0m"

LABELS = {
    "COMMENTI":    f"{_AZ}[COMMENTI]   {_RS}",
    "CONNESSIONI": f"{_AZ}[CONNESSIONI]{_RS}",
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
    li_session = os.path.join(BASE_LI, "linkedin_session.json")

    if not os.path.exists(li_session):
        print("❌  Sessione LinkedIn non trovata.")
        print("    Esegui:  python \"LinkedIn Automation\\refresh_session.py\"")
        print("    Poi rilancia questo script.")
        sys.exit(1)

    results = {}

    print()
    print("=" * 60)
    print(f"  LINKEDIN ONLY  {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"  Lancia: COMMENTI + CONNESSIONI")
    print(f"  Email / Instagram: NON toccati")
    print("=" * 60)
    print()

    log("ORCH", "Avvio COMMENTI + CONNESSIONI in parallelo...")

    t_commenti = threading.Thread(
        target=worker,
        args=("COMMENTI", BASE_LI, "python comment_posts.py", results),
    )
    t_connessioni = threading.Thread(
        target=worker,
        args=("CONNESSIONI", BASE_LI, "python run_today.py", results),
    )

    t_commenti.start()
    t_connessioni.start()

    t_commenti.join()
    t_connessioni.join()

    print()
    print("=" * 60)
    print("  LINKEDIN COMPLETATO")
    for label, status in results.items():
        print(f"    {label:<14} → {status}")
    print("=" * 60)


if __name__ == "__main__":
    main()
