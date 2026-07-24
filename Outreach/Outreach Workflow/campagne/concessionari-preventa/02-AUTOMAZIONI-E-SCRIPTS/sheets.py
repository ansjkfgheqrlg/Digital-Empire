# -*- coding: utf-8 -*-
"""
Owner: 01-AGENCY · Controllore: A2-QA · Origine: FORGE
Governo: MANDATO Art.8 + ADR-008

Google Sheets integration and deduplication logic.
"""
from __future__ import annotations

import logging
import os
import re
import time
from pathlib import Path
from typing import List, Dict

log = logging.getLogger("preventa-pw.sheets")

def normalize_phone(p: str) -> str:
    return re.sub(r'\s+', '', p or '').replace('-', '').replace('(', '').replace(')', '')

def upload_to_google_sheets(leads: List[Dict], sheet_id: str, creds_path: str, push_only_alta: bool = False, worksheet_name: str = "Foglio1"):
    """
    Push leads su Google Sheets con deduplica per telefono.
    """
    if not sheet_id:
        log.warning("Sheet ID mancante, skip upload Sheets")
        return

    if push_only_alta:
        leads_to_push = [r for r in leads if r.get("priorita_lead") == "ALTA"]
        log.info(f"Filtro Sheets: solo ALTA -> {len(leads_to_push)} su {len(leads)}")
    else:
        leads_to_push = leads

    if not leads_to_push:
        log.warning("Nessun lead da pushare su Sheets")
        return

    try:
        import gspread
        from google.oauth2.service_account import Credentials
    except ImportError:
        log.error("Librerie Sheets mancanti. Installa: pip install gspread google-auth")
        log.error("Poi ripeti comando con --sheet-id")
        return

    creds_path = creds_path or os.getenv("GOOGLE_SHEETS_CREDS_PATH", "credentials.json")
    if not Path(creds_path).exists():
        log.error(f"File credenziali non trovato: {creds_path}")
        return

    try:
        log.info(f"Connessione a Google Sheets ID={sheet_id[:10]}... con creds {creds_path}")
        scopes = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
        creds = Credentials.from_service_account_file(creds_path, scopes=scopes)
        client = gspread.authorize(creds)
        sheet = client.open_by_key(sheet_id)

        try:
            ws = sheet.worksheet(worksheet_name)
        except Exception:
            log.info(f"Worksheet '{worksheet_name}' non trovato, uso primo foglio")
            ws = sheet.get_worksheet(0)

        existing_phones = set()
        try:
            records = ws.get_all_records()
            for rec in records:
                tel = normalize_phone(rec.get("telefono","") or rec.get("Telefono",""))
                if tel:
                    existing_phones.add(tel)
            log.info(f"Sheet esistente: {len(records)} righe, {len(existing_phones)} telefoni già presenti")
        except Exception as e:
            log.info(f"Sheet vuoto o errore lettura esistenti (normale se nuovo): {e}")
            if ws.row_count == 0 or ws.acell('A1').value is None:
                header = ["nome_attivita","indirizzo","telefono","sito_web","ha_sito","numero_recensioni","media_recensioni","ha_ads_attive","priorita_lead","citta_ricerca","categoria","note_qualifica","maps_url","data_estrazione"]
                ws.append_row(header)

        new_rows = []
        skipped = 0
        for lead in leads_to_push:
            phone_norm = normalize_phone(lead.get("telefono",""))
            if phone_norm and phone_norm in existing_phones:
                skipped += 1
                continue
            if not lead.get("nome_attivita"):
                continue
            row = [
                lead.get("nome_attivita",""),
                lead.get("indirizzo",""),
                lead.get("telefono",""),
                lead.get("sito_web",""),
                str(lead.get("ha_sito","")),
                lead.get("numero_recensioni",0),
                lead.get("media_recensioni",0),
                str(lead.get("ha_ads_attive","")),
                lead.get("priorita_lead",""),
                lead.get("citta_ricerca",""),
                lead.get("categoria",""),
                lead.get("note_qualifica",""),
                lead.get("maps_url",""),
                lead.get("data_estrazione",""),
            ]
            new_rows.append(row)
            if phone_norm:
                existing_phones.add(phone_norm)

        if not new_rows:
            log.info(f"Nessun nuovo lead da aggiungere (skippati {skipped} duplicati)")
            return

        batch_size = 50
        for i in range(0, len(new_rows), batch_size):
            batch = new_rows[i:i+batch_size]
            ws.append_rows(batch, value_input_option="USER_ENTERED")
            log.info(f"Sheets: pushate {len(batch)} righe batch {i//batch_size+1} / {(len(new_rows)-1)//batch_size+1}")
            time.sleep(1)

        log.info(f"✅ Sheets upload completo: {len(new_rows)} nuovi lead aggiunti, {skipped} duplicati saltati")

    except Exception as e:
        log.error(f"Errore upload Google Sheets: {e}")
