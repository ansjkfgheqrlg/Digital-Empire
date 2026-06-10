"""
RUNNER GIORNALIERO — esegui questo ogni mattina.
Fa tutto in sequenza:
  1. Controlla accettazioni nuove
  2. Manda messaggi ai connessi (giorno +1)
  3. Manda follow-up (giorno +3, +7)
  4. Manda nuove richieste connessione (riempie il quota giornaliero)

Run: python run_daily.py
Run: python run_daily.py --dry-run
"""
import subprocess
import sys
import os

DRY = "--dry-run" if "--dry-run" in sys.argv else ""
BASE = os.path.dirname(os.path.abspath(__file__))


def run(script):
    args = ["python", os.path.join(BASE, script)]
    if DRY:
        args.append(DRY)
    print(f"\n{'='*60}")
    print(f"  ESEGUO: {script}")
    print(f"{'='*60}")
    result = subprocess.run(args, cwd=BASE)
    return result.returncode == 0


print("\n" + "="*60)
print("  LINKEDIN AUTOMATION — DAILY RUN")
print("="*60)

run("03_check_accepted.py")
run("04_send_messages.py")
run("05_send_followups.py")
run("02_send_connections.py")

print("\n" + "="*60)
print("  DAILY RUN COMPLETATO")
print("="*60)
