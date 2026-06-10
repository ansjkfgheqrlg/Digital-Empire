import csv
import dns.resolver
from email_validator import validate_email, EmailNotValidError
import os
import time

def check_mx(email):
    """Verifica se il dominio dell'email ha record MX validi."""
    try:
        domain = email.split('@')[-1]
        records = dns.resolver.resolve(domain, 'MX')
        return True if records else False
    except Exception:
        return False

def verify_leads(input_file, output_file):
    if not os.path.exists(input_file):
        print(f"Errore: {input_file} non trovato.")
        return

    leads = []
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            leads.append(row)

    print(f"Analisi di {len(leads)} lead...")
    
    validated_leads = []
    seen_emails = set()
    counts = {"total": 0, "valid": 0, "invalid_format": 0, "no_mx": 0, "duplicate": 0}

    for lead in leads:
        counts["total"] += 1
        email = lead.get('email', '').strip().lower()

        if not email:
            continue

        if email in seen_emails:
            counts["duplicate"] += 1
            continue
        
        seen_emails.add(email)

        # 1. Validazione formato
        try:
            validate_email(email, check_deliverability=False)
        except EmailNotValidError:
            counts["invalid_format"] += 1
            print(f" [!] Formato non valido: {email}")
            continue

        # 2. Validazione MX (DNS)
        if not check_mx(email):
            counts["no_mx"] += 1
            print(f" [!] Dominio/MX inesistente: {email}")
            continue

        # Se passa tutto
        counts["valid"] += 1
        validated_leads.append(lead)
        
        if counts["valid"] % 50 == 0:
            print(f" ... processati {counts['total']} lead, {counts['valid']} validi finora")

    # Scrittura output
    if validated_leads:
        keys = validated_leads[0].keys()
        with open(output_file, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(validated_leads)

    print("\n" + "="*30)
    print(f"REPORT VALIDAZIONE:")
    print(f"Totale analizzati: {counts['total']}")
    print(f"Validi (REALI)   : {counts['valid']}")
    print(f"Duplicati        : {counts['duplicate']}")
    print(f"Formato errato   : {counts['invalid_format']}")
    print(f"Dominio/MX morto : {counts['no_mx']}")
    print(f"Salvati in       : {output_file}")
    print("="*30)

if __name__ == "__main__":
    input_csv = 'leads_freschi_full.csv'
    output_csv = 'leads_freschi_validated.csv'
    verify_leads(input_csv, output_csv)
