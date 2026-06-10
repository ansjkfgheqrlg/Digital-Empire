"""
Importa lead esportati dall'Apify Leads Finder (IoSHqwTR9YGhzccez) nel formato
standard dei nostri CSV.

Uso:
    python implementation/import_leads_finder.py --file leads_export.json
    python implementation/import_leads_finder.py --file leads_export.csv
    python implementation/import_leads_finder.py --file leads.json --categoria "ristorante" --citta "Milano"

Input:
    --file: Path al file JSON o CSV esportato dall'UI Apify (obbligatorio)
    --categoria: Categoria da assegnare se non presente nei dati (default: "generico")
    --citta: Città da assegnare se non presente nei dati (default: "Italia")

Output:
    CSV in output/YYYY-MM-DD_lead_nosito_[citta]_[categoria]_import.csv
    File di log in logs/

Note:
    - Solo lead con email validata vengono salvati (REGOLA CRITICA)
    - I campi vengono mappati automaticamente dalle varianti comuni dei nomi
"""

import os
import sys
import csv
import json
import argparse
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from dotenv import load_dotenv
from implementation.utils.logger import get_logger, log_errore_fatale
from implementation.utils.sheets_client import INTESTAZIONI_NO_SITO

load_dotenv()

# Soglia score minima per salvare il lead
SOGLIA_SCORE_MINIMO = 20

# Mappatura campo → varianti possibili nei dati Apify Leads Finder
MAPPA_CAMPI = {
    "nome_persona":     ["name", "full_name", "fullName", "first_name", "firstName"],
    "cognome":          ["last_name", "lastName", "surname"],
    "nome_azienda":     ["company", "organization", "organization_name", "organizationName",
                         "employer", "company_name", "companyName", "business_name"],
    "email":            ["email", "email_address", "emailAddress", "business_email",
                         "work_email", "personal_email"],
    "telefono":         ["phone", "phone_number", "phoneNumber", "mobile", "mobile_phone",
                         "mobilePhone", "direct_phone", "cell"],
    "titolo_lavoro":    ["title", "job_title", "jobTitle", "position", "role"],
    "industria":        ["industry", "sector", "category", "verticalCategory"],
    "citta":            ["city", "location", "locality", "person_city", "headquarter_city"],
    "paese":            ["country", "person_country", "headquarter_country"],
    "sito_web":         ["website", "company_website", "companyWebsite", "url",
                         "organization_website", "domain"],
    "linkedin":         ["linkedin_url", "linkedinUrl", "linkedin", "linkedin_profile"],
    "dipendenti":       ["employees", "num_employees", "numEmployees", "employee_count",
                         "employeeCount", "headcount"],
    "email_status":     ["email_status", "emailStatus", "validation_status"],
}


def _estrai_campo(item: dict, varianti: list) -> str:
    """Restituisce il primo valore non vuoto trovato tra le varianti del campo."""
    for chiave in varianti:
        valore = item.get(chiave)
        if valore and str(valore).strip():
            return str(valore).strip()
    return ""


def _costruisci_nome_business(item: dict) -> str:
    """
    Determina il nome del business a partire dai dati del lead.
    Priorità: azienda > nome persona + azienda.
    """
    azienda = _estrai_campo(item, MAPPA_CAMPI["nome_azienda"])
    nome = _estrai_campo(item, MAPPA_CAMPI["nome_persona"])
    cognome = _estrai_campo(item, MAPPA_CAMPI["cognome"])

    if nome and cognome and not nome.strip().lower().endswith(cognome.strip().lower()):
        nome_completo = f"{nome} {cognome}".strip()
    else:
        nome_completo = nome

    if azienda:
        return azienda
    if nome_completo:
        return nome_completo
    return "Sconosciuto"


def _calcola_score(item: dict, ha_email: bool, ha_telefono: bool, industria: str) -> int:
    """
    Calcola score 0-100 per un lead Leads Finder.

    Criteri:
    - Email validata: +40
    - Telefono presente: +20
    - Industria ad alta domanda: +20
    - LinkedIn presente: +10
    - Sito web presente: +10
    """
    score = 0

    if ha_email:
        score += 40

    if ha_telefono:
        score += 20

    industria_lower = industria.lower()
    settori_alta_domanda = {
        "marketing", "advertising", "retail", "food", "restaurant",
        "health", "medical", "dental", "beauty", "fitness", "legal",
        "accounting", "real estate", "construction", "hospitality",
        "ristorante", "dentista", "avvocato", "commercialista",
        "palestra", "estetista", "idraulico", "elettricista"
    }
    if any(s in industria_lower for s in settori_alta_domanda):
        score += 20

    linkedin = _estrai_campo(item, MAPPA_CAMPI["linkedin"])
    if linkedin:
        score += 10

    sito = _estrai_campo(item, MAPPA_CAMPI["sito_web"])
    if sito:
        score += 10

    return min(score, 100)


def _genera_id_lead(citta: str) -> str:
    """Genera ID univoco per il lead."""
    iniziali = "".join([p[:2].upper() for p in citta.split()[:2]])
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")[:18]
    return f"NS-{iniziali}-{timestamp}"


def _carica_file(path_file: str) -> list:
    """
    Carica il file JSON o CSV esportato dall'Apify UI.

    Returns:
        Lista di dizionari con i dati dei lead
    """
    path = Path(path_file)
    if not path.exists():
        raise FileNotFoundError(f"File non trovato: {path_file}")

    suffisso = path.suffix.lower()

    if suffisso == ".json":
        with open(path, encoding="utf-8") as f:
            dati = json.load(f)
        if isinstance(dati, list):
            return dati
        if isinstance(dati, dict) and "items" in dati:
            return dati["items"]
        raise ValueError("Formato JSON non riconosciuto. Atteso array di oggetti o {'items': [...]}")

    elif suffisso == ".csv":
        with open(path, encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)
            return list(reader)

    else:
        raise ValueError(f"Formato file non supportato: {suffisso}. Usa .json o .csv")


def _salva_csv(righe: list, citta: str, categoria: str) -> str:
    """Salva i lead nel CSV standard."""
    Path("output").mkdir(exist_ok=True)
    nome_file = (
        f"output/{datetime.now().strftime('%Y-%m-%d')}"
        f"_lead_nosito_{citta}_{categoria}_import.csv"
    ).replace(" ", "_").lower()

    file_esiste = Path(nome_file).exists()
    with open(nome_file, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=INTESTAZIONI_NO_SITO)
        if not file_esiste:
            writer.writeheader()
        for riga in righe:
            writer.writerow(riga)

    return nome_file


def _processa_lead(item: dict, categoria_default: str, citta_default: str) -> dict | None:
    """
    Converte un item Leads Finder nel formato standard del nostro CSV.

    Returns:
        Dizionario riga CSV o None se il lead va scartato (es. email assente)
    """
    email = _estrai_campo(item, MAPPA_CAMPI["email"])

    # REGOLA CRITICA: senza email il lead non viene salvato
    if not email:
        return None

    telefono = _estrai_campo(item, MAPPA_CAMPI["telefono"])
    nome_business = _costruisci_nome_business(item)
    industria = _estrai_campo(item, MAPPA_CAMPI["industria"]) or categoria_default
    citta = _estrai_campo(item, MAPPA_CAMPI["citta"]) or citta_default
    sito = _estrai_campo(item, MAPPA_CAMPI["sito_web"])
    titolo = _estrai_campo(item, MAPPA_CAMPI["titolo_lavoro"])
    dipendenti = _estrai_campo(item, MAPPA_CAMPI["dipendenti"])
    linkedin = _estrai_campo(item, MAPPA_CAMPI["linkedin"])

    score = _calcola_score(item, ha_email=True, ha_telefono=bool(telefono), industria=industria)
    fascia = "A" if score >= 70 else "B" if score >= 40 else "C"

    note_parts = []
    if titolo:
        note_parts.append(f"Ruolo: {titolo}")
    if dipendenti:
        note_parts.append(f"Dipendenti: {dipendenti}")
    if linkedin:
        note_parts.append(f"LinkedIn: {linkedin}")
    if sito:
        note_parts.append(f"Sito: {sito}")

    return {
        "ID_LEAD": _genera_id_lead(citta),
        "DATA_TROVATO": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "NOME_BUSINESS": nome_business,
        "CATEGORIA": industria,
        "INDIRIZZO": "",
        "CITTÀ": citta,
        "TELEFONO": telefono,
        "EMAIL": email,
        "RATING_GOOGLE": "",
        "N_RECENSIONI": "",
        "PLACE_ID": "",
        "SCORE_PRIORITÀ": str(score),
        "FASCIA": fascia,
        "PRONTO_OUTREACH": "Sì" if score >= 40 else "No",
        "STATO_OUTREACH": "nuovo",
        "BOZZA_GENERATA": "",
        "DATA_BOZZA": "",
        "DATA_ULTIMO_CONTATTO": "",
        "DATA_RISPOSTA": "",
        "DATA_FOLLOWUP_SCHEDULATO": "",
        "STORICO_STATI": "",
        "NOTE": " | ".join(note_parts),
        "MOTIVO_ESCLUSIONE": "",
    }


def main():
    parser = argparse.ArgumentParser(
        description="Importa lead da export Apify Leads Finder nel formato standard"
    )
    parser.add_argument("--file", required=True, help="Path al file JSON o CSV esportato da Apify")
    parser.add_argument("--categoria", default="generico", help="Categoria default se assente nei dati")
    parser.add_argument("--citta", default="Italia", help="Città default se assente nei dati")
    args = parser.parse_args()

    suffix = f"{args.citta}_{args.categoria}".replace(" ", "_").lower()
    logger = get_logger("WF-A-IMPORT", suffix)
    logger.info(f"START — Import da: {args.file} | Categoria: {args.categoria} | Città: {args.citta}")

    # Carica il file
    try:
        items = _carica_file(args.file)
    except Exception as e:
        log_errore_fatale("WF-A-IMPORT", str(e))
        logger.error(f"ERRORE caricamento file: {e}")
        sys.exit(1)

    logger.info(f"Lead trovati nel file: {len(items)}")

    # Se il file ha 0 item, stampa le chiavi dell'eventuale primo item per debug
    if not items:
        logger.warning("File vuoto o nessun lead trovato")
        print("ATTENZIONE: Nessun lead trovato nel file.")
        sys.exit(0)

    # Mostra le chiavi disponibili nel primo item (per debug)
    chiavi_disponibili = list(items[0].keys()) if items else []
    logger.info(f"Campi disponibili: {chiavi_disponibili}")
    print(f"Campi rilevati nel file: {chiavi_disponibili}")

    # Processa ogni lead
    righe_valide = []
    n_senza_email = 0
    n_score_basso = 0

    for item in items:
        riga = _processa_lead(item, args.categoria, args.citta)

        if riga is None:
            n_senza_email += 1
            continue

        if int(riga["SCORE_PRIORITÀ"]) < SOGLIA_SCORE_MINIMO:
            logger.debug(f"Score basso: {riga['NOME_BUSINESS']} — SKIP")
            n_score_basso += 1
            continue

        righe_valide.append(riga)
        logger.info(f"Lead: {riga['NOME_BUSINESS']} | Email: {riga['EMAIL']} | Score: {riga['SCORE_PRIORITÀ']} ({riga['FASCIA']})")

    # Salva CSV
    if righe_valide:
        nome_file = _salva_csv(righe_valide, args.citta, args.categoria)
        logger.info(f"CSV salvato: {nome_file}")
    else:
        nome_file = None
        logger.warning("Nessun lead valido da salvare")

    # Report finale
    print(f"\n{'='*50}")
    print(f"IMPORT COMPLETATO")
    print(f"  Lead nel file:        {len(items)}")
    print(f"  Senza email (skip):   {n_senza_email}")
    print(f"  Score basso (skip):   {n_score_basso}")
    print(f"  Lead salvati:         {len(righe_valide)}")
    if nome_file:
        print(f"  CSV:                  {nome_file}")
    fascia_a = sum(1 for r in righe_valide if r["FASCIA"] == "A")
    fascia_b = sum(1 for r in righe_valide if r["FASCIA"] == "B")
    print(f"  Fascia A (top):       {fascia_a}")
    print(f"  Fascia B:             {fascia_b}")
    print(f"{'='*50}\n")

    logger.info(
        f"END — Totale: {len(items)} | Senza email: {n_senza_email} | "
        f"Score basso: {n_score_basso} | Salvati: {len(righe_valide)}"
    )


if __name__ == "__main__":
    main()
