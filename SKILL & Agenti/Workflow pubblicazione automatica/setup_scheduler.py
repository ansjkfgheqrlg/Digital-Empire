"""
Digital Empire — Windows Task Scheduler Setup
Configura la pubblicazione automatica giornaliera.

UTILIZZO:
  python setup_scheduler.py --time 09:30    # pubblica ogni giorno alle 09:30
  python setup_scheduler.py --time 18:00    # cambia orario
  python setup_scheduler.py --list          # vedi stato attuale
  python setup_scheduler.py --remove        # rimuovi task
  python setup_scheduler.py --run-now       # forza esecuzione immediata
"""
import argparse, subprocess, sys
from pathlib import Path

WORKFLOW  = Path(__file__).parent.resolve()
PYTHON    = sys.executable
TASK_NAME = "DigitalEmpire_AutoPublisher"
RUN_DAILY = str(WORKFLOW / "run_daily.py")


def schtask(args, check=False):
    cmd = ["schtasks"] + args
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.stdout.strip():
        print(r.stdout.strip())
    if r.stderr.strip():
        print(r.stderr.strip(), file=sys.stderr)
    return r.returncode == 0


def cmd_create(time_str):
    h, m = time_str.split(":")
    task_cmd = f'"{PYTHON}" "{RUN_DAILY}"'
    print(f"\nCreazione task: {TASK_NAME}")
    print(f"Orario:         {h}:{m} ogni giorno")
    print(f"Comando:        {task_cmd}")
    print()

    ok = schtask([
        "/Create", "/F",
        "/TN", TASK_NAME,
        "/TR", task_cmd,
        "/SC", "DAILY",
        "/ST", f"{h}:{m}",
        "/RL", "HIGHEST",
    ])

    if ok:
        print(f"\nOK — Task schedulato: ogni giorno alle {time_str}")
        print(f"Verifica con: python setup_scheduler.py --list")
    else:
        print("\nERRORE — Riprova come Amministratore (tasto destro su terminale → Esegui come amministratore)")


def cmd_list():
    print(f"\n=== Task: {TASK_NAME} ===\n")
    schtask(["/Query", "/TN", TASK_NAME, "/FO", "LIST", "/V"])


def cmd_remove():
    print(f"\nRimozione task: {TASK_NAME}")
    ok = schtask(["/Delete", "/TN", TASK_NAME, "/F"])
    if ok:
        print(f"Task rimosso.")
    else:
        print("Task non trovato o errore rimozione.")


def cmd_run_now():
    print(f"\nEsecuzione immediata: {TASK_NAME}")
    ok = schtask(["/Run", "/TN", TASK_NAME])
    if ok:
        print("Task avviato. Controlla logs/ per il risultato.")
    else:
        print("Errore avvio. Task esiste? Controlla con --list")


def main():
    ap = argparse.ArgumentParser(
        description="Digital Empire Auto Publisher — Scheduler Setup",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    ap.add_argument("--time",    help="Orario pubblicazione HH:MM (es: 09:30)")
    ap.add_argument("--list",    action="store_true", help="Mostra stato task")
    ap.add_argument("--remove",  action="store_true", help="Rimuovi task")
    ap.add_argument("--run-now", action="store_true", help="Forza esecuzione ora")
    args = ap.parse_args()

    if args.time:
        cmd_create(args.time)
    elif args.list:
        cmd_list()
    elif args.remove:
        cmd_remove()
    elif args.run_now:
        cmd_run_now()
    else:
        ap.print_help()


if __name__ == "__main__":
    main()
