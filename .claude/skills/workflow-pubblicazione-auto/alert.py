"""
Alert system — notifica Max in caso di errori critici.
Livello 1: Windows balloon tip (taskbar)
Livello 2: File in alerts/ (persistente, monitorabile)
Livello 3: Stampa su stderr
"""
import argparse, sys, subprocess
from pathlib import Path
from datetime import datetime

WORKFLOW  = Path(__file__).parent.resolve()
ALERT_DIR = WORKFLOW / "alerts"
ALERT_DIR.mkdir(exist_ok=True)


def balloon_tip(title, msg):
    script = f"""
Add-Type -AssemblyName System.Windows.Forms
$n = New-Object System.Windows.Forms.NotifyIcon
$n.Icon = [System.Drawing.SystemIcons]::Warning
$n.BalloonTipTitle = "{title}"
$n.BalloonTipText = "{msg}"
$n.Visible = $True
$n.ShowBalloonTip(8000)
Start-Sleep -s 9
$n.Dispose()
""".strip()
    subprocess.Popen(
        ["powershell", "-WindowStyle", "Hidden", "-NonInteractive", "-Command", script],
        creationflags=subprocess.CREATE_NO_WINDOW if hasattr(subprocess, "CREATE_NO_WINDOW") else 0,
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--msg", required=True, help="Messaggio di alert")
    ap.add_argument("--title", default="Digital Empire Publisher", help="Titolo notifica")
    args = ap.parse_args()

    msg   = args.msg
    title = args.title
    ts    = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Livello 1: Windows balloon
    try:
        balloon_tip(title, msg)
        print(f"[ALERT] Balloon tip inviato")
    except Exception as e:
        print(f"[ALERT] Balloon fallito: {e}", file=sys.stderr)

    # Livello 2: File alert persistente
    safe_ts  = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    alert_f  = ALERT_DIR / f"{safe_ts}_ALERT.txt"
    alert_f.write_text(f"[{ts}] {title}\n{msg}\n", encoding="utf-8")
    print(f"[ALERT] Scritto: {alert_f}")

    # Livello 3: stderr
    print(f"[ALERT] {ts} — {title}: {msg}", file=sys.stderr)


if __name__ == "__main__":
    main()
