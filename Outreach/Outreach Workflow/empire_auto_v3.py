import os
import subprocess
import time
import sys

def run_command(cmd):
    print(f"\n[RUNNING] {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
    if result.returncode != 0:
        print(f"[ERROR] {result.stderr}")
    else:
        print(result.stdout)
    return result

def main():
    print("="*60)
    print(" DIGITAL EMPIRE — OUTREACH AUTOMATOR V3.0")
    print(" Quality: Extreme (APSOC+V) | Account: Single Gmail")
    print("="*60)

    # 1. VALIDAZIONE LEAD (Pulisce i lead inesistenti)
    print("\n[STEP 1] Validazione Lead...")
    if os.path.exists('leads_freschi_full.csv'):
        run_command(['python', 'verify_leads.py'])
    else:
        print("Errore: leads_freschi_full.csv non trovato. Inserisci i nuovi lead nel file.")
        return

    # 2. GENERAZIONE EMAIL
    print("\n[STEP 2] Generazione Email APSOC+V...")
    if os.path.exists('leads_freschi_validated.csv'):
        # Generiamo per i prossimi 50 lead (limite giornaliero sicuro per 1 account)
        run_command(['python', 'prepare_emails.py', '--csv', 'leads_freschi_validated.csv', '--output', 'emails_daily_ready.json'])
    else:
        print("Errore: nessun lead validato trovato.")
        return

    # 3. PULIZIA CARATTERI
    print("\n[STEP 3] Pulizia Encoding...")
    run_command(['python', 'clean_json.py'])

    # 4. INVIO AUTOMATICO
    print("\n[STEP 4] Invio Email...")
    # Usiamo delay_seconds=60 per massima sicurezza se mandiamo 50+ email
    print("Lancio invio in background...")
    # Nota: su Windows, 'start' è un comando shell. Usiamo shell=True o subprocess.Popen
    subprocess.Popen(['python', 'send_ready.py', '--input', 'emails_daily_ready.json', '--auto'], shell=True)
    
    print("\n" + "="*60)
    print(" PROCESSO COMPLETATO!")
    print(" Le email sono in fase di invio in background.")
    print(" Controlla emails_daily_ready.json per lo stato in tempo reale.")
    print("="*60)

if __name__ == "__main__":
    main()
