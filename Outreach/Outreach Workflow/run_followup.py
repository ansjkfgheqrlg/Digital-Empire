"""
Digital Empire — Email Follow-up Runner
========================================
Controlla il DB ogni mattina e invia follow-up ai lead
che non hanno risposto alla email precedente.

SCHEDULE CONSIGLIATO:
  Ogni giorno alle 10:00  →  python run_followup.py

LOGICA:
  F1 (giorno 3-4):  email inviata 3+ giorni fa, nessuna risposta, F1 non ancora inviata
  F2 (giorno 7-8):  F1 inviata 4+ giorni fa, nessuna risposta, F2 non ancora inviata

STATISTICHE ATTESE:
  F1 tasso risposta aggiuntivo: ~20-25% (cumulativo ~40-45%)
  F2 tasso risposta aggiuntivo: ~8-10%  (cumulativo ~50-55%)
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

# ── CONFIG ────────────────────────────────────────────────────────────────────
DB_PATH     = Path(__file__).parent / "output" / "leads.db"
OUTPUT_DIR  = str(Path(__file__).parent / "output")

GIORNI_F1 = 3    # Invia F1 dopo N giorni senza risposta
GIORNI_F2 = 4    # Invia F2 dopo N giorni senza risposta a F1
MAX_F1_GIORNO = 80   # Max F1 da inviare in un giorno
MAX_F2_GIORNO = 80   # Max F2 da inviare in un giorno


def carica_lead_per_f1() -> list:
    """Lead con email inviata da 3+ giorni, senza risposta, F1 non ancora inviata."""
    if not DB_PATH.exists():
        return []
    try:
        with sqlite3.connect(DB_PATH) as conn:
            rows = conn.execute(f"""
                SELECT email, page_name, settore, citta, website,
                       oggetto, corpo, score, template,
                       COALESCE(settore_calibrato, settore) AS settore_calibrato, data
                FROM leads_contattati
                WHERE stato = 'inviata'
                AND f1_inviata IS NULL
                AND risposta_ricevuta IS NULL
                AND julianday('now') - julianday(data) >= {GIORNI_F1}
                ORDER BY data ASC
                LIMIT {MAX_F1_GIORNO}
            """).fetchall()
        leads = []
        for r in rows:
            leads.append({
                "email": r[0], "page_name": r[1], "settore": r[2],
                "citta": r[3], "website": r[4], "oggetto": r[5],
                "corpo": r[6], "score": r[7], "template": r[8],
                "settore_calibrato": r[9] or r[2], "data": r[10],
            })
        return leads
    except Exception as e:
        print(f"[FOLLOWUP] Errore lettura DB per F1: {e}")
        return []


def carica_lead_per_f2() -> list:
    """Lead con F1 inviata da 4+ giorni, senza risposta, F2 non ancora inviata."""
    if not DB_PATH.exists():
        return []
    try:
        with sqlite3.connect(DB_PATH) as conn:
            rows = conn.execute(f"""
                SELECT email, page_name, settore, citta, website,
                       oggetto, corpo, score, template,
                       COALESCE(settore_calibrato, settore) AS settore_calibrato, f1_inviata, f1_oggetto
                FROM leads_contattati
                WHERE f1_inviata IS NOT NULL
                AND f2_inviata IS NULL
                AND risposta_ricevuta IS NULL
                AND julianday('now') - julianday(f1_inviata) >= {GIORNI_F2}
                ORDER BY f1_inviata ASC
                LIMIT {MAX_F2_GIORNO}
            """).fetchall()
        leads = []
        for r in rows:
            leads.append({
                "email": r[0], "page_name": r[1], "settore": r[2],
                "citta": r[3], "website": r[4], "oggetto": r[5],
                "corpo": r[6], "score": r[7], "template": r[8],
                "settore_calibrato": r[9] or r[2],
                "f1_inviata": r[10],
                "f1_oggetto": r[11] or f"Re: {r[5]}",
            })
        return leads
    except Exception as e:
        print(f"[FOLLOWUP] Errore lettura DB per F2: {e}")
        return []


def salva_f1_inviata(risultati: list):
    """Aggiorna DB: segna F1 come inviata e aggiorna stato."""
    if not risultati:
        return
    ora = datetime.now().isoformat()
    try:
        with sqlite3.connect(DB_PATH) as conn:
            for r in risultati:
                if r.get("stato_invio") == "inviata":
                    conn.execute("""
                        UPDATE leads_contattati
                        SET f1_inviata = ?, f1_oggetto = ?, f1_corpo = ?, stato = 'f1_inviata'
                        WHERE email = ?
                    """, (ora, r.get("f1_oggetto", ""), r.get("f1_corpo", ""), r["email"]))
    except Exception as e:
        print(f"[FOLLOWUP] Errore aggiornamento DB F1: {e}")


def salva_f2_inviata(risultati: list):
    """Aggiorna DB: segna F2 come inviata e aggiorna stato."""
    if not risultati:
        return
    ora = datetime.now().isoformat()
    try:
        with sqlite3.connect(DB_PATH) as conn:
            for r in risultati:
                if r.get("stato_invio") == "inviata":
                    conn.execute("""
                        UPDATE leads_contattati
                        SET f2_inviata = ?, f2_oggetto = ?, f2_corpo = ?, stato = 'f2_inviata'
                        WHERE email = ?
                    """, (ora, r.get("f2_oggetto", ""), r.get("f2_corpo", ""), r["email"]))
    except Exception as e:
        print(f"[FOLLOWUP] Errore aggiornamento DB F2: {e}")


def verifica_config() -> dict:
    config = {
        "OPENROUTER_API_KEY": os.getenv("OPENROUTER_API_KEY", ""),
        "GMAIL_USER":         os.getenv("GMAIL_USER", ""),
        "GMAIL_APP_PASSWORD": os.getenv("GMAIL_APP_PASSWORD", ""),
    }
    mancanti = [k for k, v in config.items() if not v]
    if mancanti:
        print(f"\n[FOLLOWUP] ❌ Variabili mancanti nel .env: {', '.join(mancanti)}")
        sys.exit(1)
    return config


def main():
    inizio = datetime.now()
    config = verifica_config()

    from agents.followup_writer import FollowupWriterAgent
    from agents.sender import EmailSenderAgent

    writer = FollowupWriterAgent(config["OPENROUTER_API_KEY"])
    sender = EmailSenderAgent(config["GMAIL_USER"], config["GMAIL_APP_PASSWORD"])

    # Verifica orario business (lun-ven 8-19)
    giorno = inizio.weekday()
    if giorno >= 5:
        print(f"\n[FOLLOWUP] Weekend — i follow-up non si inviano il weekend.")
        sys.exit(0)
    if not (8 <= inizio.hour < 19):
        print(f"\n[FOLLOWUP] Orario fuori business ({inizio.hour}:00). Riprova tra le 8-19.")
        sys.exit(0)

    print()
    print("=" * 65)
    print(f"  DIGITAL EMPIRE — EMAIL FOLLOW-UP  {inizio.strftime('%Y-%m-%d %H:%M')}")
    print("=" * 65)

    # ── F1 ────────────────────────────────────────────────────────────────────
    lead_f1 = carica_lead_per_f1()
    print(f"\n[FOLLOWUP] Lead eligibili F1 (giorno 3+): {len(lead_f1)}")

    f1_inviati = 0
    if lead_f1:
        lead_con_f1 = writer.run_f1(lead_f1)
        # Prepara per il sender (mappa campi)
        emails_f1 = []
        for lead in lead_con_f1:
            if lead.get("f1_corpo"):
                emails_f1.append({
                    "email":     lead["email"],
                    "page_name": lead.get("page_name", ""),
                    "settore":   lead.get("settore", ""),
                    "citta":     lead.get("citta", ""),
                    "oggetto":   lead.get("f1_oggetto", f"Re: {lead.get('oggetto','')}"),
                    "corpo":     lead["f1_corpo"],
                    # Metadati extra per il salvataggio
                    "f1_oggetto": lead.get("f1_oggetto", ""),
                    "f1_corpo":   lead["f1_corpo"],
                })

        if emails_f1:
            print(f"\n[FOLLOWUP] Invio {len(emails_f1)} F1...")
            risultati = sender.run(emails_f1, output_dir=OUTPUT_DIR)
            # Aggiungi info invio ai lead originali
            email_map = {r["email"]: r.get("stato", "errore") for r in risultati}
            for lead in lead_con_f1:
                lead["stato_invio"] = email_map.get(lead["email"], "errore")
            salva_f1_inviata(lead_con_f1)
            f1_inviati = sum(1 for r in risultati if r.get("stato") == "inviata")

    # ── F2 ────────────────────────────────────────────────────────────────────
    lead_f2 = carica_lead_per_f2()
    print(f"\n[FOLLOWUP] Lead eligibili F2 (giorno 7+): {len(lead_f2)}")

    f2_inviati = 0
    if lead_f2:
        lead_con_f2 = writer.run_f2(lead_f2)
        emails_f2 = []
        for lead in lead_con_f2:
            if lead.get("f2_corpo"):
                emails_f2.append({
                    "email":     lead["email"],
                    "page_name": lead.get("page_name", ""),
                    "settore":   lead.get("settore", ""),
                    "citta":     lead.get("citta", ""),
                    "oggetto":   lead.get("f2_oggetto", f"Re: {lead.get('oggetto','')}"),
                    "corpo":     lead["f2_corpo"],
                    "f2_oggetto": lead.get("f2_oggetto", ""),
                    "f2_corpo":   lead["f2_corpo"],
                })

        if emails_f2:
            print(f"\n[FOLLOWUP] Invio {len(emails_f2)} F2...")
            risultati2 = sender.run(emails_f2, output_dir=OUTPUT_DIR)
            email_map2 = {r["email"]: r.get("stato", "errore") for r in risultati2}
            for lead in lead_con_f2:
                lead["stato_invio"] = email_map2.get(lead["email"], "errore")
            salva_f2_inviata(lead_con_f2)
            f2_inviati = sum(1 for r in risultati2 if r.get("stato") == "inviata")

    # ── REPORT ────────────────────────────────────────────────────────────────
    fine = datetime.now()
    durata = int((fine - inizio).total_seconds())

    print()
    print("=" * 65)
    print(f"  FOLLOW-UP COMPLETATO  {fine.strftime('%H:%M:%S')} (durata: {durata}s)")
    print("=" * 65)
    print(f"  F1 inviati:  {f1_inviati}")
    print(f"  F2 inviati:  {f2_inviati}")
    print(f"  Totale:      {f1_inviati + f2_inviati}")
    print("=" * 65)

    return {"f1_inviati": f1_inviati, "f2_inviati": f2_inviati}


if __name__ == "__main__":
    main()
