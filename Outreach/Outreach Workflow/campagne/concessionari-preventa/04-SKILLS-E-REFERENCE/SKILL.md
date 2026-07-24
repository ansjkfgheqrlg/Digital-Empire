---
name: preventa-maps-scraping
description: Metodologia e comandi operativi per lo scraping e la qualificazione di concessionari auto tramite Playwright e Google Sheets.
---

# Skill: Preventa Maps Scraping

Questa skill definisce la procedura operativa e le linee guida per estrarre e qualificare lead di concessionari da Google Maps.

## Comandi Operativi Primari

### 1. Esecuzione Locale con priorità ALTA
Estrae i lead di determinate città, filtra solo la priorità ALTA e salva il file CSV completo + quello filtrato:
```bash
python scraper.py --cities Milano,Bergamo,Brescia --limit 25 --only-alta --output data/leads.csv
```

### 2. Sincronizzazione automatica su Google Sheets
Esegue lo scraping e carica le nuove righe direttamente su Google Sheets qualificando per priorità ALTA (saltando i duplicati telefonici):
```bash
python scraper.py --cities Milano --limit 30 --only-alta --sheet-id TUO_GOOGLE_SHEETS_ID --sheets-push-alta --sheets-creds credentials.json
```

## Struttura della Qualificazione (Scoring)
Il modulo valuta la presenza e la modernità del sito per classificare la lead:
- **ALTA**: Pitch modernizzazione immediata. Nessun sito, sito vecchio (copyright superato, no HTTPS, markup scarso), o meno di 10 recensioni.
- **MEDIA**: Pitch ottimizzazione o ads. Sito esistente ma senza Pixel FB o Google Tag Manager (probabile assenza di campagne attive), o recensioni basse.
- **BASSA**: Sito moderno, tracciamento attivo, e alto volume di recensioni positive.

## Gestione dei Fogli Google
1. Crea un service account in Google Cloud Console.
2. Scarica la chiave JSON come `credentials.json`.
3. Condividi lo spreadsheet con l'email del service account come **Editor**.
4. Imposta `GOOGLE_SHEET_ID` nel file `.env` locale.
