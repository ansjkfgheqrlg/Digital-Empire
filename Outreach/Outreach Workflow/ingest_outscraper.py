"""
ingest_outscraper.py — Converte CSV Outscraper in leads puliti

Input:  CSV esportato da Outscraper.com (business italiani)
Output: leads_outscraper_clean.csv

Colonne Outscraper attese (possono variare):
  name, site, phone, full_address, city, state, country, email, category, rating, reviews

Colonne output:
  nicchia, page_name, email, citta, website, telefono, ha_booking_online, note

Run:
  python ingest_outscraper.py outscraper_export.csv
"""

import csv
import glob
import json
import os
import re
import sys
from pathlib import Path

# ─── Mappatura categoria Google Maps → nicchia ───────────────────────────────

CATEGORY_MAP = {
    "fisioterapista": "fisioterapista",
    "physical therapy": "fisioterapista",
    "physiotherapist": "fisioterapista",
    "fisioterapia": "fisioterapista",
    "avvocato": "avvocato",
    "lawyer": "avvocato",
    "attorney": "avvocato",
    "studio legale": "avvocato",
    "law firm": "avvocato",
    "psicologo": "psicologo",
    "psychologist": "psicologo",
    "psicologia": "psicologo",
    "palestra": "palestra",
    "gym": "palestra",
    "fitness center": "palestra",
    "yoga": "yoga",
    "yoga studio": "yoga",
    "estetica": "estetica",
    "beauty salon": "estetica",
    "centro estetico": "estetica",
    "nail salon": "estetica",
    "spa": "spa",
    "day spa": "spa",
    "commercialista": "commercialista",
    "accountant": "commercialista",
    "accounting": "commercialista",
    "studio commercialista": "commercialista",
    "dentist": "dentista",
    "dentista": "dentista",
    "dental clinic": "dentista",
    "studio dentistico": "dentista",
    "doctor": "medico",
    "medico": "medico",
    "clinic": "medico",
    "clinica": "medico",
    "medico di base": "medico",
}


def map_category(raw_category: str) -> str:
    """Mappa la categoria Google Maps alla nicchia corretta.
    Cerca corrispondenza parziale (case-insensitive).
    Default: categoria originale lowercase."""
    if not raw_category:
        return "altro"
    cat_lower = raw_category.strip().lower()
    # Prima cerca corrispondenza esatta
    if cat_lower in CATEGORY_MAP:
        return CATEGORY_MAP[cat_lower]
    # Poi cerca corrispondenza parziale
    for key, nicchia in CATEGORY_MAP.items():
        if key in cat_lower or cat_lower in key:
            return nicchia
    # Default: categoria originale lowercase, spazi → underscore
    return re.sub(r"\s+", "_", cat_lower)


# ─── Filtro email valida ──────────────────────────────────────────────────────

INVALID_EMAIL_PATTERNS = [
    r"noreply",
    r"no-reply",
    r"info@doctolib",
    r"donotreply",
]


def is_valid_email(email: str) -> bool:
    """Restituisce True se l'email è valida e utilizzabile per outreach."""
    if not email or "@" not in email:
        return False
    email_lower = email.strip().lower()
    for pattern in INVALID_EMAIL_PATTERNS:
        if re.search(pattern, email_lower):
            return False
    return True


# ─── Generazione campo note ───────────────────────────────────────────────────

def build_note(site: str) -> str:
    """Genera il campo note in base al sito web."""
    if not site or site.strip() == "":
        return "nessun sito web"
    site_lower = site.strip().lower()
    if "facebook.com" in site_lower or "fb.com" in site_lower:
        return "solo pagina facebook"
    return "sito web presente"


# ─── Caricamento email già processate ────────────────────────────────────────

def load_existing_emails(folder: Path) -> set:
    """Carica tutte le email già presenti in qualsiasi emails_*.json nella cartella."""
    existing = set()
    json_files = list(folder.glob("emails_*.json"))
    for jf in json_files:
        try:
            data = json.loads(jf.read_text(encoding="utf-8"))
            if isinstance(data, list):
                for entry in data:
                    if isinstance(entry, dict) and "email" in entry:
                        existing.add(entry["email"].strip().lower())
            elif isinstance(data, dict):
                for email_key in data:
                    existing.add(email_key.strip().lower())
        except (json.JSONDecodeError, OSError):
            pass
    return existing


# ─── Normalizzazione colonne CSV Outscraper ──────────────────────────────────

# Alcune esportazioni usano nomi colonna leggermente diversi
COLUMN_ALIASES = {
    "name": ["name", "business_name", "title"],
    "email": ["email", "emails", "email_1", "business_email"],
    "site": ["site", "website", "url", "web", "site_web"],
    "city": ["city", "citta", "città", "locality"],
    "category": ["category", "categories", "type", "business_type"],
    "phone": ["phone", "phone_number", "telefono", "tel", "phone_1"],
}


def resolve_columns(headers: list) -> dict:
    """Mappa le colonne trovate nel CSV ai campi canonici."""
    headers_lower = [h.strip().lower() for h in headers]
    mapping = {}
    for canonical, aliases in COLUMN_ALIASES.items():
        for alias in aliases:
            if alias in headers_lower:
                original_idx = headers_lower.index(alias)
                mapping[canonical] = headers[original_idx]
                break
    return mapping


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    if len(sys.argv) < 2:
        print("Uso: python ingest_outscraper.py <outscraper_export.csv>")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    if not input_path.exists():
        print(f"Errore: file non trovato → {input_path}")
        sys.exit(1)

    script_dir = Path(__file__).parent
    output_path = script_dir / "leads_outscraper_clean.csv"

    # Carica email già processate
    existing_emails = load_existing_emails(script_dir)
    print(f"Email già presenti nei file emails_*.json: {len(existing_emails)}")

    # Lettura CSV input
    rows = []
    with open(input_path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        col_map = resolve_columns(list(reader.fieldnames or []))
        for row in reader:
            rows.append(row)

    total_input = len(rows)
    print(f"\nInput: {total_input} righe")

    # Contatori scarti
    discarded_no_email = 0
    discarded_duplicates = 0

    # Set per deduplicazione interna
    seen_emails = set(existing_emails)

    output_rows = []

    for row in rows:
        # Leggi i campi usando la mappatura colonne
        raw_email   = row.get(col_map.get("email", "email"), "").strip()
        raw_name    = row.get(col_map.get("name", "name"), "").strip()
        raw_site    = row.get(col_map.get("site", "site"), "").strip()
        raw_city    = row.get(col_map.get("city", "city"), "").strip()
        raw_cat     = row.get(col_map.get("category", "category"), "").strip()
        raw_phone   = row.get(col_map.get("phone", "phone"), "").strip()

        # Filtro email valida
        if not is_valid_email(raw_email):
            discarded_no_email += 1
            continue

        email_lower = raw_email.lower()

        # Deduplicazione
        if email_lower in seen_emails:
            discarded_duplicates += 1
            continue

        seen_emails.add(email_lower)

        # Costruzione riga output
        nicchia  = map_category(raw_cat)
        note     = build_note(raw_site)
        website  = raw_site if raw_site else ""

        output_rows.append({
            "nicchia":           nicchia,
            "page_name":         raw_name,
            "email":             raw_email,
            "citta":             raw_city,
            "website":           website,
            "telefono":          raw_phone,
            "ha_booking_online": "NO",
            "note":              note,
        })

    # Scrittura CSV output
    fieldnames = ["nicchia", "page_name", "email", "citta", "website", "telefono", "ha_booking_online", "note"]
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(output_rows)

    # Report finale
    total_discarded = discarded_no_email + discarded_duplicates
    print(f"Scartati: {total_discarded} (no email: {discarded_no_email}, duplicati: {discarded_duplicates})")
    print(f"Output: {len(output_rows)} lead → {output_path}")


if __name__ == "__main__":
    main()
