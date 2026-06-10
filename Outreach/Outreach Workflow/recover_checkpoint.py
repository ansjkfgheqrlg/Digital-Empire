"""
recover_checkpoint.py — Estrai email dai business già trovati nel scrape_checkpoint.json
Uso: python recover_checkpoint.py
"""
import csv, json, sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.stderr.reconfigure(encoding="utf-8", errors="replace")

from dotenv import load_dotenv
load_dotenv(Path(__file__).parent / ".env")

BASE        = Path(__file__).parent
CP_PATH     = BASE / "scrape_checkpoint.json"
OUTPUT_PATH = BASE / "leads_verificati.csv"
DB_PATH     = BASE / "leads.db"

if not CP_PATH.exists():
    print("scrape_checkpoint.json non trovato.")
    sys.exit(1)

# ── Carica business dal checkpoint ───────────────────────────────────────────
businesses = json.loads(CP_PATH.read_text(encoding="utf-8"))
print(f"[RECOVERY] {len(businesses)} business trovati nel checkpoint\n")

# ── Carica memoria: nomi, siti, email già noti ───────────────────────────────
nomi_noti, siti_noti, email_note = set(), set(), set()
if OUTPUT_PATH.exists():
    with open(OUTPUT_PATH, newline="", encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            if row.get("page_name"): nomi_noti.add(row["page_name"].strip().lower())
            if row.get("website"):   siti_noti.add(row["website"].strip().lower().rstrip("/"))
            if row.get("email"):     email_note.add(row["email"].strip().lower())

if DB_PATH.exists():
    import sqlite3
    with sqlite3.connect(DB_PATH) as conn:
        try:
            for (nome, sito, email) in conn.execute(
                "SELECT page_name, website, email FROM leads_contattati"
            ).fetchall():
                if nome:  nomi_noti.add(nome.strip().lower())
                if sito:  siti_noti.add(sito.strip().lower().rstrip("/"))
                if email: email_note.add(email.strip().lower())
        except Exception:
            pass

print(f"[MEMORIA] {len(email_note)} email già note | {len(nomi_noti)} nomi | {len(siti_noti)} siti\n")

# ── Filtra business già noti ─────────────────────────────────────────────────
nuovi = []
for b in businesses:
    nome = (b.get("page_name") or "").strip().lower()
    sito = (b.get("website") or "").strip().lower().rstrip("/")
    if nome and nome in nomi_noti: continue
    if sito and sito in siti_noti: continue
    nuovi.append(b)

print(f"[FILTRO] {len(businesses) - len(nuovi)} già noti saltati → {len(nuovi)} nuovi da estrarre\n")

if not nuovi:
    print("Tutti i business già presenti. Niente da estrarre.")
    sys.exit(0)

# ── Estrazione email ─────────────────────────────────────────────────────────
from agents.extractor import EmailExtractorAgent
extractor = EmailExtractorAgent()

print(f"[EXTRACTOR] Estraggo email da {len(nuovi)} siti...")
leads_con_email = extractor.run(nuovi)

# ── Filtra per email univoca ─────────────────────────────────────────────────
leads_nuovi = []
for lead in leads_con_email:
    email = lead.get("email", "").strip().lower()
    if not email or "@" not in email:
        continue
    if email in email_note:
        continue
    leads_nuovi.append(lead)
    email_note.add(email)

print(f"\n[RISULTATO] {len(leads_nuovi)} email nuove trovate su {len(nuovi)} business\n")

if not leads_nuovi:
    print("Nessuna email nuova trovata.")
    sys.exit(0)

# ── Salva su CSV ─────────────────────────────────────────────────────────────
fields = ["page_name", "email", "settore", "citta", "website"]
file_esiste = OUTPUT_PATH.exists()
with open(OUTPUT_PATH, "a", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
    if not file_esiste:
        writer.writeheader()
    for lead in leads_nuovi:
        writer.writerow({k: lead.get(k, "") for k in fields})

print(f"[SALVATO] {len(leads_nuovi)} email aggiunte → {OUTPUT_PATH.name}")
print(f"\nSe non bastano, lancia: python scrape_only.py --target 300")
