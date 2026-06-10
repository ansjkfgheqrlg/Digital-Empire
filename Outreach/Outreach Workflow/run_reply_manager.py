"""
Digital Empire — Reply Manager
================================
Controlla Gmail per risposte dai lead, classifica l'intenzione
e risponde automaticamente per portare la conversazione verso la chiamata.

SCHEDULE CONSIGLIATO:
  Ogni giorno alle 09:00  →  python run_reply_manager.py

FLUSSO:
  1. IMAP scan Gmail INBOX → cerca email FROM lead nel DB
  2. Per ogni risposta: ConversationManager classifica + genera risposta
  3. Invia risposta via Gmail SMTP
  4. Aggiorna DB: risposta_ricevuta, conversazione_stato
"""

import os
import sqlite3
import sys
from datetime import datetime
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.stderr.reconfigure(encoding="utf-8", errors="replace")

from dotenv import load_dotenv
load_dotenv(Path(__file__).parent / ".env")

DB_PATH    = Path(__file__).parent / "output" / "leads.db"
OUTPUT_DIR = str(Path(__file__).parent / "output")


def verifica_config() -> dict:
    config = {
        "OPENROUTER_API_KEY": os.getenv("OPENROUTER_API_KEY", ""),
        "GMAIL_USER":         os.getenv("GMAIL_USER", ""),
        "GMAIL_APP_PASSWORD": os.getenv("GMAIL_APP_PASSWORD", ""),
    }
    mancanti = [k for k, v in config.items() if not v]
    if mancanti:
        print(f"\n[REPLY-MGR] ❌ Variabili mancanti nel .env: {', '.join(mancanti)}")
        sys.exit(1)
    return config


def segna_risposta_ricevuta(email: str, reply_text: str, reply_subject: str):
    """Aggiorna DB con la risposta ricevuta."""
    ora = datetime.now().isoformat()
    try:
        with sqlite3.connect(DB_PATH) as conn:
            conn.execute("""
                UPDATE leads_contattati
                SET risposta_ricevuta = ?,
                    risposta_testo = ?,
                    risposta_oggetto = ?,
                    conversazione_stato = 'risposto'
                WHERE email = ?
            """, (ora, reply_text[:2000], reply_subject, email))
    except Exception as e:
        print(f"[REPLY-MGR] Errore DB segna_risposta: {e}")


def segna_risposta_inviata(email: str, categoria: str):
    """Aggiorna stato dopo aver inviato la risposta."""
    stato = "esaurito" if categoria == "NON_INTERESSATO" else "in_conversazione"
    try:
        with sqlite3.connect(DB_PATH) as conn:
            conn.execute("""
                UPDATE leads_contattati
                SET conversazione_stato = ?
                WHERE email = ?
            """, (stato, email))
    except Exception as e:
        print(f"[REPLY-MGR] Errore DB segna_risposta_inviata: {e}")


def main():
    inizio = datetime.now()
    config = verifica_config()

    from agents.reply_monitor import ReplyMonitorAgent
    from agents.conversation_manager import ConversationManagerAgent
    from agents.sender import EmailSenderAgent

    monitor  = ReplyMonitorAgent(config["GMAIL_USER"], config["GMAIL_APP_PASSWORD"], str(DB_PATH))
    conv_mgr = ConversationManagerAgent(config["OPENROUTER_API_KEY"])
    sender   = EmailSenderAgent(config["GMAIL_USER"], config["GMAIL_APP_PASSWORD"])

    print()
    print("=" * 65)
    print(f"  DIGITAL EMPIRE — REPLY MANAGER  {inizio.strftime('%Y-%m-%d %H:%M')}")
    print("=" * 65)

    # ── STEP 1: Controlla risposte ────────────────────────────────────────────
    risposte = monitor.run()

    if not risposte:
        print("\n[REPLY-MGR] Nessuna risposta trovata oggi.")
        print("=" * 65)
        return {"risposte_trovate": 0, "risposte_inviate": 0}

    print(f"\n[REPLY-MGR] {len(risposte)} risposte da gestire.")

    # ── STEP 2: Segna risposte ricevute nel DB ────────────────────────────────
    for r in risposte:
        segna_risposta_ricevuta(r["email"], r["reply_text"], r.get("reply_subject", ""))

    # ── STEP 3: Genera risposte ───────────────────────────────────────────────
    print("\n[REPLY-MGR] Genero risposte...")
    risposte_generate = conv_mgr.run_batch(risposte)

    if not risposte_generate:
        print("[REPLY-MGR] Nessuna risposta da inviare.")
        return {"risposte_trovate": len(risposte), "risposte_inviate": 0}

    # ── STEP 4: Invia risposte ────────────────────────────────────────────────
    print(f"\n[REPLY-MGR] Invio {len(risposte_generate)} risposte...")

    # Separa NON_INTERESSATO dagli altri (i NON_INTERESSATO ricevono comunque risposta cortese)
    emails_da_inviare = [
        {
            "email":     r["email"],
            "page_name": r.get("page_name", ""),
            "settore":   r.get("settore", ""),
            "citta":     r.get("citta", ""),
            "oggetto":   r.get("oggetto", ""),
            "corpo":     r.get("corpo", ""),
            "_categoria": r.get("categoria_risposta", "POSITIVO"),
        }
        for r in risposte_generate
        if r.get("corpo")
    ]

    risultati = sender.run(emails_da_inviare, output_dir=OUTPUT_DIR)

    # ── STEP 5: Aggiorna DB ───────────────────────────────────────────────────
    email_map = {r["email"]: r.get("stato", "errore") for r in risultati}
    inviate = 0
    for r in risposte_generate:
        if email_map.get(r["email"]) == "inviata":
            inviate += 1
            segna_risposta_inviata(r["email"], r.get("categoria_risposta", "POSITIVO"))

    # ── REPORT ────────────────────────────────────────────────────────────────
    fine = datetime.now()
    durata = int((fine - inizio).total_seconds())

    print()
    print("=" * 65)
    print(f"  REPLY MANAGER COMPLETATO  {fine.strftime('%H:%M:%S')} ({durata}s)")
    print("=" * 65)
    print(f"  Risposte trovate:  {len(risposte)}")
    print(f"  Risposte inviate:  {inviate}")

    # Breakdown per categoria
    categorie = {}
    for r in risposte_generate:
        cat = r.get("categoria_risposta", "?")
        categorie[cat] = categorie.get(cat, 0) + 1
    for cat, n in categorie.items():
        print(f"    {cat}: {n}")
    print("=" * 65)

    return {"risposte_trovate": len(risposte), "risposte_inviate": inviate}


if __name__ == "__main__":
    main()
