"""
Digital Empire — Instagram + Email (senza LinkedIn)
====================================================
Avvia solo le due catene indipendenti da LinkedIn:

  CATENA INSTAGRAM: IG-DM → IG-REPLIES
  CATENA EMAIL:     EMAIL-GEN (~30-40 min) → EMAIL-INVIA
"""

import subprocess
import threading
import time
import os
import sys
from datetime import datetime

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HERE    = os.path.dirname(os.path.abspath(__file__))
BASE_OW = os.path.join(HERE, "Outreach Workflow")
BASE_IG = os.path.join(HERE, "Instagram Automation")

EMAIL_TARGET = 100

_print_lock = threading.Lock()

_OR  = "\033[38;5;208m"
_VI  = "\033[95m"
_GR  = "\033[92m"
_BLD = "\033[1m"
_RS  = "\033[0m"

LABELS = {
    "IG-DM":       f"{_OR}[IG-DM]      {_RS}",
    "IG-REPLIES":  f"{_OR}[IG-REPLIES] {_RS}",
    "EMAIL-GEN":   f"{_VI}[EMAIL-GEN]  {_RS}",
    "EMAIL-INVIA": f"{_GR}[EMAIL-INVIA]{_RS}",
    "ORCH":        f"{_BLD}[ORCH]       {_RS}",
}

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


def log(label, msg):
    ts = datetime.now().strftime("%H:%M:%S")
    with _print_lock:
        prefix = LABELS.get(label, f"[{label}]")
        print(f"{ts}  {prefix}  {msg.rstrip()}", flush=True)


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
            log(label, f"\033[92mFINE -> OK\033[0m")
        else:
            results[label] = f"ERRORE (exit {rc})"
            log(label, f"FINE -> ERRORE (exit {rc})")
    except Exception as e:
        results[label] = f"ECCEZIONE: {e}"
        log(label, f"FINE -> ECCEZIONE: {e}")


def main():
    ig_session = os.path.join(BASE_IG, "instagram_session.json")
    ig_enabled = os.path.exists(ig_session)
    if not ig_enabled:
        print("\n[WARN] Sessione Instagram non trovata.")
        print("   Esegui prima: python \"Instagram Automation\\refresh_session.py\"")

    results = {}

    print()
    print("=" * 60)
    print(f"  IG + EMAIL  {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"  CATENA INSTAGRAM: IG-DM -> IG-REPLIES")
    print(f"  CATENA EMAIL:     EMAIL-GEN -> EMAIL-INVIA")
    print(f"  LinkedIn: saltato (sessione in attesa)")
    print("=" * 60)
    print()

    def catena_instagram():
        if not ig_enabled:
            results["IG-DM"]      = "saltato (sessione non trovata)"
            results["IG-REPLIES"] = "saltato (sessione non trovata)"
            return
        r = {}
        worker("IG-DM", BASE_IG, "python run_today.py", r)
        results["IG-DM"] = r.get("IG-DM", "non avviato")
        log("ORCH", "IG-DM completato -> avvio IG-REPLIES...")
        r2 = {}
        worker("IG-REPLIES", BASE_IG, "python check_replies.py", r2)
        results["IG-REPLIES"] = r2.get("IG-REPLIES", "non avviato")

    def catena_email():
        r = {}
        worker("EMAIL-GEN", BASE_OW, f"python run.py --mode genera --target {EMAIL_TARGET}", r)
        results["EMAIL-GEN"] = r.get("EMAIL-GEN", "non avviato")
        if results["EMAIL-GEN"] == "OK":
            log("ORCH", "EMAIL-GEN completato -> avvio EMAIL-INVIA...")
            r2 = {}
            worker("EMAIL-INVIA", BASE_OW, "python run.py --mode invia", r2)
            results["EMAIL-INVIA"] = r2.get("EMAIL-INVIA", "non avviato")
        else:
            log("ORCH", "[WARN] EMAIL-GEN fallita — invio saltato.")
            results["EMAIL-INVIA"] = "saltato (generazione fallita)"

    t_ig    = threading.Thread(target=catena_instagram)
    t_email = threading.Thread(target=catena_email)

    t_ig.start()
    time.sleep(3)
    t_email.start()

    t_ig.join()
    t_email.join()

    print()
    print("=" * 60)
    print(f"  REPORT FINALE  {datetime.now().strftime('%H:%M:%S')}")
    print("=" * 60)
    for label in ["IG-DM", "IG-REPLIES", "EMAIL-GEN", "EMAIL-INVIA"]:
        if label in results:
            s = results[label]
            icon = "[OK] " if s == "OK" else ("[--] " if "saltato" in s else "[ERR]")
            print(f"  {icon}  {label:<15}  {s}")
    print("=" * 60)


if __name__ == "__main__":
    main()
