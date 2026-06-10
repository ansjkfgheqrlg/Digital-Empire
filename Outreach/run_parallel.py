"""
Digital Empire — Orchestratore Parallelo v4.0
==============================================
Tre catene indipendenti che partono insieme:

CATENA LINKEDIN (più veloce):
  [COMMENTI]    → 100 commenti warming su LinkedIn
  [CONNESSIONI] → 50 connection requests con nota Barnum/Rainbow
  ↓ appena finiti (non aspetta EMAIL-GEN):
  [FOLLOWUP]    → F1 (giorno 3) + F2 (giorno 7) per chi non ha risposto
  [REPLY-MGR]   → controlla Gmail per risposte, continua conversazione verso call
  [LI-REPLIES]  → legge DM LinkedIn, genera suggerimenti risposta (read-only)
  (FOLLOWUP + REPLY-MGR + LI-REPLIES in parallelo tra loro)

CATENA EMAIL (più lenta, ~30-40 min):
  [EMAIL-GEN]   → genera email con framework 5-Pillar (Barnum/Rainbow/niche_term)
  ↓ appena finito:
  [EMAIL-INVIA] → invia le email generate

CATENA INSTAGRAM:
  [IG-DM]       → trova lead da hashtag, invia DM (Barnum/Rainbow), F1, F2
  [IG-REPLIES]  → legge DM Instagram non letti, genera/invia risposte

Log individuali:
  comments_log.txt           → LinkedIn commenti
  run_today_log.txt          → LinkedIn connessioni
  Outreach Workflow/output/  → Email (genera + invia + followup + reply)
  linkedin_replies_log.txt   → Suggerimenti risposte LinkedIn DM
  Instagram Automation/run_today_log.txt     → Instagram DM + follow-up
  Instagram Automation/instagram_replies_log.txt → Risposte Instagram
"""

import subprocess
import threading
import time
import os
import sys
from datetime import datetime

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# ── PERCORSI ────────────────────────────────────────────────────────────────
HERE    = os.path.dirname(os.path.abspath(__file__))
BASE_LI = os.path.join(HERE, "LinkedIn Automation")
BASE_OW = os.path.join(HERE, "Outreach Workflow")
BASE_IG = os.path.join(HERE, "Instagram Automation")

# Target email giornaliero (lo scraper Apify cerca nuovi lead con i SETTORI aggiornati)
EMAIL_TARGET = 100

# ── LOCK per stampa ordinata ─────────────────────────────────────────────────
_print_lock = threading.Lock()

# Schema colori: LinkedIn=azzurro, Instagram=arancione, Email=viola, Invio/Successo=verde
_AZ  = "\033[96m"          # azzurro  — tutto LinkedIn
_OR  = "\033[38;5;208m"    # arancione — tutto Instagram
_VI  = "\033[95m"          # viola    — email gen/followup/reply
_GR  = "\033[92m"          # verde    — email invio + messaggi di successo
_BLD = "\033[1m"           # bold     — orchestratore
_RS  = "\033[0m"           # reset

LABELS = {
    # LinkedIn — AZZURRO
    "COMMENTI":     f"{_AZ}[COMMENTI]   {_RS}",
    "CONNESSIONI":  f"{_AZ}[CONNESSIONI]{_RS}",
    "LI-REPLIES":   f"{_AZ}[LI-REPLIES] {_RS}",
    "FOLLOWUP":     f"{_VI}[FOLLOWUP]   {_RS}",   # email followup — viola
    "REPLY-MGR":    f"{_VI}[REPLY-MGR]  {_RS}",   # email reply    — viola
    # Instagram — ARANCIONE
    "IG-DM":        f"{_OR}[IG-DM]      {_RS}",
    "IG-REPLIES":   f"{_OR}[IG-REPLIES] {_RS}",
    # Email — VIOLA / invio VERDE
    "EMAIL-GEN":    f"{_VI}[EMAIL-GEN]  {_RS}",
    "EMAIL-INVIA":  f"{_GR}[EMAIL-INVIA]{_RS}",
    # Orchestratore
    "ORCH":         f"{_BLD}[ORCH]       {_RS}",
}


def log(label, msg):
    ts = datetime.now().strftime("%H:%M:%S")
    with _print_lock:
        prefix = LABELS.get(label, f"[{label}]")
        print(f"{ts}  {prefix}  {msg.rstrip()}", flush=True)


# ── FILTRO ANTI-RUMORE ───────────────────────────────────────────────────────

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
    """True se la riga non e' un traceback Python interno o rumore di asyncio."""
    stripped = line.strip()
    if not stripped:
        return False
    for pattern in _NOISE:
        if pattern in line:
            return False
    # Righe di traceback indentate con File "..."
    if stripped.startswith('File "') and '.py"' in stripped:
        return False
    return True


# ── WORKER ───────────────────────────────────────────────────────────────────

def worker(label: str, cwd: str, cmd: str, results: dict):
    """Esegue cmd in cwd, streaming l'output filtrato e prefissato."""
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


# ── ORCHESTRATORE ─────────────────────────────────────────────────────────────

def main():
    # Verifica sessione LinkedIn
    session_file = os.path.join(BASE_LI, "linkedin_session.json")
    if not os.path.exists(session_file):
        print("\n❌  Sessione LinkedIn non trovata.")
        print("    Esegui prima:  python \"LinkedIn Automation\\refresh_session.py\"")
        sys.exit(1)

    # Verifica sessione Instagram (avviso non bloccante)
    ig_session_file = os.path.join(BASE_IG, "instagram_session.json")
    ig_enabled = os.path.exists(ig_session_file)
    if not ig_enabled:
        print("\n⚠   Sessione Instagram non trovata — catena IG saltata.")
        print("    Per attivarla: python \"Instagram Automation\\refresh_session.py\"")

    results = {}

    print()
    print("=" * 65)
    print(f"  DIGITAL EMPIRE — PARALLEL OUTREACH v4.0  {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("=" * 65)
    print(f"  CATENA LINKEDIN: COMMENTI + CONNESSIONI")
    print(f"    → appena finiti: FOLLOWUP + REPLY-MGR + LI-REPLIES")
    print(f"  CATENA EMAIL:    EMAIL-GEN (~30-40 min)")
    print(f"    → appena finito: EMAIL-INVIA")
    ig_status = "OK" if ig_enabled else "sessione mancante"
    print(f"  CATENA INSTAGRAM: IG-DM + IG-REPLIES ({ig_status})")
    print(f"  Email target: {EMAIL_TARGET} (scraper Apify — nuovi target)")
    print("=" * 65)
    print()

    # ── Avvia i 3 processi base tutti insieme ────────────────────────────
    log("ORCH", "Avvio — COMMENTI + CONNESSIONI + EMAIL-GEN in parallelo...")

    t_commenti    = threading.Thread(
        target=worker,
        args=("COMMENTI", BASE_LI, "python comment_posts.py", results),
        daemon=True,
    )
    t_connessioni = threading.Thread(
        target=worker,
        args=("CONNESSIONI", BASE_LI, "python run_today.py", results),
        daemon=True,
    )
    t_email_gen   = threading.Thread(
        target=worker,
        args=(
            "EMAIL-GEN", BASE_OW,
            f"python run.py --mode genera --target {EMAIL_TARGET}",
            results,
        ),
        daemon=True,
    )

    t_commenti.start()
    time.sleep(3)
    t_connessioni.start()
    time.sleep(3)
    t_email_gen.start()

    # ── CATENA LINKEDIN ───────────────────────────────────────────────────
    # Appena COMMENTI + CONNESSIONI finiscono → parte FOLLOWUP + REPLY-MGR + LI-REPLIES

    def catena_linkedin():
        t_commenti.join()
        t_connessioni.join()
        log("ORCH", "COMMENTI + CONNESSIONI completati → avvio FOLLOWUP + REPLY-MGR + LI-REPLIES...")

        r_li = {}
        threads = [
            threading.Thread(
                target=worker,
                args=("FOLLOWUP",   BASE_OW, "python run_followup.py",      r_li),
                daemon=True,
            ),
            threading.Thread(
                target=worker,
                args=("REPLY-MGR",  BASE_OW, "python run_reply_manager.py", r_li),
                daemon=True,
            ),
            threading.Thread(
                target=worker,
                args=("LI-REPLIES", BASE_LI, "python check_replies.py",     r_li),
                daemon=True,
            ),
        ]
        for t in threads:
            t.start()
            time.sleep(2)
        for t in threads:
            t.join()

        results["FOLLOWUP"]   = r_li.get("FOLLOWUP",   "non avviato")
        results["REPLY-MGR"]  = r_li.get("REPLY-MGR",  "non avviato")
        results["LI-REPLIES"] = r_li.get("LI-REPLIES", "non avviato")
        log("ORCH", "CATENA LINKEDIN completata.")

    # ── CATENA EMAIL ──────────────────────────────────────────────────────
    # Appena EMAIL-GEN finisce → parte EMAIL-INVIA

    def catena_email():
        t_email_gen.join()
        if results.get("EMAIL-GEN", "").startswith("OK"):
            log("ORCH", "EMAIL-GEN completato → avvio EMAIL-INVIA...")
            r_e = {}
            t_invia = threading.Thread(
                target=worker,
                args=("EMAIL-INVIA", BASE_OW, "python run.py --mode invia", r_e),
            )
            t_invia.start()
            t_invia.join()
            results["EMAIL-INVIA"] = r_e.get("EMAIL-INVIA", "non avviato")
        else:
            log("ORCH", "[WARN] EMAIL-GEN fallita — invio saltato.")
            results["EMAIL-INVIA"] = "saltato (generazione fallita)"
        log("ORCH", "CATENA EMAIL completata.")

    # ── CATENA INSTAGRAM ─────────────────────────────────────────────────
    # IG-DM (trova lead + invia DM + follow-up) → poi IG-REPLIES in parallelo

    def catena_instagram():
        if not ig_enabled:
            results["IG-DM"]      = "saltato (sessione non trovata)"
            results["IG-REPLIES"] = "saltato (sessione non trovata)"
            return

        log("ORCH", "Avvio CATENA INSTAGRAM: IG-DM...")

        r_ig = {}
        t_ig_dm = threading.Thread(
            target=worker,
            args=("IG-DM", BASE_IG, "python run_today.py", r_ig),
            daemon=True,
        )
        t_ig_dm.start()
        t_ig_dm.join()

        results["IG-DM"] = r_ig.get("IG-DM", "non avviato")
        log("ORCH", "IG-DM completato → avvio IG-REPLIES...")

        r_ig2 = {}
        t_ig_rep = threading.Thread(
            target=worker,
            args=("IG-REPLIES", BASE_IG, "python check_replies.py", r_ig2),
            daemon=True,
        )
        t_ig_rep.start()
        t_ig_rep.join()

        results["IG-REPLIES"] = r_ig2.get("IG-REPLIES", "non avviato")
        log("ORCH", "CATENA INSTAGRAM completata.")

    # ── Lancia le tre catene in parallelo ─────────────────────────────────
    t_catena_li    = threading.Thread(target=catena_linkedin)
    t_catena_email = threading.Thread(target=catena_email)
    t_catena_ig    = threading.Thread(target=catena_instagram)

    t_catena_li.start()
    t_catena_email.start()
    time.sleep(5)  # stagger: Instagram parte 5 sec dopo per non sovraccaricare
    t_catena_ig.start()

    t_catena_li.join()
    t_catena_email.join()
    t_catena_ig.join()

    # ── REPORT FINALE ─────────────────────────────────────────────────────
    print()
    print("=" * 65)
    print(f"  REPORT FINALE  {datetime.now().strftime('%H:%M:%S')}")
    print("=" * 65)
    ordine = ["COMMENTI", "CONNESSIONI", "FOLLOWUP", "REPLY-MGR", "LI-REPLIES",
              "EMAIL-GEN", "EMAIL-INVIA", "IG-DM", "IG-REPLIES"]
    for label in ordine:
        if label in results:
            status = results[label]
            icon = "[OK] " if status == "OK" else ("[--] " if "saltato" in status else "[ERR]")
            print(f"  {icon}  {label:<15}  {status}")
    print()
    print(f"  Log individuali:")
    print(f"    LinkedIn commenti:      LinkedIn Automation/comments_log.txt")
    print(f"    LinkedIn connessioni:   LinkedIn Automation/run_today_log.txt")
    print(f"    LinkedIn DM replies:    LinkedIn Automation/linkedin_replies_log.txt")
    print(f"    Email pipeline:         Outreach Workflow/output/")
    print(f"    Instagram DM:           Instagram Automation/run_today_log.txt")
    print(f"    Instagram replies:      Instagram Automation/instagram_replies_log.txt")
    print("=" * 65)
    print()


if __name__ == "__main__":
    main()
