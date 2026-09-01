"""
Digital Empire — Master Auto Publisher
Avviato da Windows Task Scheduler all'orario configurato.

Flusso: health_check → publish (retry x3 ogni 5min) → alert fallimento
Log: logs/YYYY-MM-DD.log
"""
import sys, subprocess, time, logging
from pathlib import Path
from datetime import datetime

WORKFLOW    = Path(__file__).parent.resolve()
LOG_DIR     = WORKFLOW / "logs"
LOG_DIR.mkdir(exist_ok=True)

log_file = LOG_DIR / f"{datetime.now().strftime('%Y-%m-%d')}.log"
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(str(log_file), encoding="utf-8"),
        logging.StreamHandler(sys.stdout),
    ]
)
log = logging.getLogger("run_daily")

PYTHON      = sys.executable
HEALTH      = str(WORKFLOW / "scripts" / "health_check.py")
PUBLISH     = str(WORKFLOW / "scripts" / "ig_carousel_publish.py")
ALERT       = str(WORKFLOW / "alert.py")
MAX_RETRIES = 3
RETRY_WAIT  = 300  # 5 minuti tra i tentativi


def run_cmd(script_args, timeout=300):
    """Esegue python script_args, logga output, restituisce exit code."""
    cmd = [PYTHON] + script_args
    log.info(f"Eseguo: {' '.join(cmd)}")
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=timeout,
            cwd=str(WORKFLOW),
        )
        if result.stdout.strip():
            for line in result.stdout.strip().splitlines():
                log.info(f"  | {line}")
        if result.stderr.strip():
            for line in result.stderr.strip().splitlines():
                log.warning(f"  ! {line}")
        return result.returncode
    except subprocess.TimeoutExpired:
        log.error(f"TIMEOUT dopo {timeout}s")
        return 99
    except Exception as e:
        log.error(f"Errore subprocess: {e}")
        return -1


def send_alert(msg):
    log.warning(f"ALERT: {msg}")
    try:
        run_cmd([ALERT, "--msg", msg], timeout=15)
    except Exception as e:
        log.error(f"Alert.py fallito: {e}")


def main():
    log.info("=" * 60)
    log.info("AVVIO — Digital Empire Auto Publisher")
    log.info(f"Data: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    log.info("=" * 60)

    # FASE 1 — Health Check
    log.info("[FASE 1] Health Check pre-pubblicazione...")
    code = run_cmd([HEALTH])
    if code != 0:
        msg = "Health check FALLITO — pubblicazione annullata. Controlla logs/"
        log.error(msg)
        send_alert(msg)
        sys.exit(1)
    log.info("[FASE 1] Health Check SUPERATO")

    # FASE 2 — Publish con retry
    log.info("[FASE 2] Avvio pubblicazione automatica...")
    for attempt in range(1, MAX_RETRIES + 1):
        log.info(f"[FASE 2] Tentativo {attempt}/{MAX_RETRIES}...")
        code = run_cmd([PUBLISH, "--auto"], timeout=180)
        if code == 0:
            log.info("[FASE 2] SUCCESSO — carosello pubblicato!")
            log.info("=" * 60)
            sys.exit(0)
        elif code == 1:
            log.warning(f"[FASE 2] Tentativo {attempt} fallito (exit 1 — nessun carosello pronto o errore IG)")
        else:
            log.warning(f"[FASE 2] Tentativo {attempt} fallito (exit code {code})")

        if attempt < MAX_RETRIES:
            log.info(f"[FASE 2] Attendo {RETRY_WAIT}s ({RETRY_WAIT//60} min) prima del prossimo tentativo...")
            time.sleep(RETRY_WAIT)

    # Tutti i tentativi esauriti
    msg = f"FALLITO dopo {MAX_RETRIES} tentativi — intervento manuale necessario"
    log.error(msg)
    send_alert(msg)
    log.info("=" * 60)
    sys.exit(1)


if __name__ == "__main__":
    main()
