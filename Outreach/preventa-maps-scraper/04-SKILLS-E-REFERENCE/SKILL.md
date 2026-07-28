---
name: preventa-maps-scraping
description: Metodologia e comandi operativi per lo scraping e la qualificazione di concessionari auto tramite Playwright, con push automatico sul CRM Areus (EmpireDesk).
---

# Skill: Preventa Maps Scraping

Questa skill definisce la procedura operativa e le linee guida per estrarre e qualificare lead di concessionari da Google Maps.

## Comandi Operativi Primari

### 1. Esecuzione Locale con priorità ALTA
Estrae i lead di determinate città, filtra solo la priorità ALTA e salva il file CSV completo + quello filtrato:
```bash
python scraper.py --cities Milano,Bergamo,Brescia --limit 25 --only-alta --output data/leads.csv
```

### 2. Sincronizzazione automatica su Areus (default, nessun setup)
Esegue lo scraping e carica le nuove righe direttamente sul CRM Areus di EmpireDesk qualificando per priorità ALTA (saltando i duplicati telefonici) — attivo di default, nessuna credenziale:
```bash
python scraper.py --cities Milano --limit 30 --only-alta --areus-push-alta
```

## Struttura della Qualificazione (Scoring)
Il modulo valuta la presenza e la modernità del sito per classificare la lead:
- **ALTA**: Pitch modernizzazione immediata. Nessun sito, sito vecchio (copyright superato, no HTTPS, markup scarso), o meno di 10 recensioni.
- **MEDIA**: Pitch ottimizzazione o ads. Sito esistente ma senza Pixel FB o Google Tag Manager (probabile assenza di campagne attive), o recensioni basse.
- **BASSA**: Sito moderno, tracciamento attivo, e alto volume di recensioni positive.

## Gestione lead in Areus
Nessun setup richiesto: i lead entrano in `EmpireDesk/state/preventa_leads.json` e sono visibili
subito nel pannello "Preventa — Outreach Freddo" dentro Areus. Se serve un path non standard,
imposta `AREUS_STATE_PATH` nel file `.env` locale.
