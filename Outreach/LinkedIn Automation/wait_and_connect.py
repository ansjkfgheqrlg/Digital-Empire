"""
Aspetta che scraping finisca (linkedin_leads.json creato con lead),
poi avvia automaticamente 02_send_connections.py.
"""
import json
import os
import subprocess
import sys
import time

LEADS_FILE = "linkedin_leads.json"
MIN_LEADS = 5  # aspetta almeno 5 lead prima di procedere
CHECK_INTERVAL = 10  # controlla ogni 10 secondi

print("Attendo completamento scraping lead...")
print(f"Controllo {LEADS_FILE} ogni {CHECK_INTERVAL}s\n")

while True:
    if os.path.exists(LEADS_FILE):
        try:
            with open(LEADS_FILE, encoding="utf-8") as f:
                leads = json.load(f)
            new_leads = [l for l in leads if l.get("status") == "new"]
            print(f"  Lead trovati: {len(new_leads)} (attendo minimo {MIN_LEADS})...")
            if len(new_leads) >= MIN_LEADS:
                print(f"\nScraping completato — {len(new_leads)} lead pronti.")
                print("Avvio 02_send_connections.py...\n")
                break
        except Exception:
            pass
    time.sleep(CHECK_INTERVAL)

result = subprocess.run([sys.executable, "02_send_connections.py"], cwd=os.path.dirname(os.path.abspath(__file__)))
print(f"\nConnessioni completate (exit code {result.returncode}).")
