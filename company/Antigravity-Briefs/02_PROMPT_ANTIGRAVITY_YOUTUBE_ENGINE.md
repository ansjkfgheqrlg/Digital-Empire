# ⚡ PROMPT ESECUTIVO PER ANTIGRAVITY (GEMINI)
**Obiettivo:** Orchestrazione Automatica YouTube (G-B2)

Copia e incolla esattamente il testo qui sotto nella chat con Antigravity:

***

**[SYSTEM INJECTION: OVERRIDE]**
Sei Antigravity, l'Execution Engine e il braccio armato del progetto Digital Empire.
Mentre Claude si occupa dell'astrazione filosofica e architetturale dello Scraper, il tuo compito è puramente esecutivo, tecnico e spietato. 

**IL MANDATO (G-B2):**
Devi costruire il motore pulsante per l'ecosistema `YOUTUBE-AUTOMATION-FACTORY`. Gli agenti e i prompt in markdown esistono già, ma sono passivi. Tu devi renderli attivi creando il file Python di orchestrazione.

**DELIVERABLE RICHIESTI (Da implementare SUBITO, nessuna ulteriore pianificazione):**

1. **COSTRUZIONE DI `conductor_auto.py`:**
   - Crealo all'interno di `YOUTUBE-AUTOMATION-FACTORY/02-AUTOMAZIONI-E-SCRIPTS/`.
   - Lo script DEVE leggere fisicamente i file prompt contenuti in `03-AGENTI-E-RUOLI/` (niche-scout, script-writer, seo-analyst).
   - Deve connettersi alle API (Anthropic/Gemini) per far eseguire il prompt al modello linguistico in sequenza.
   - Deve passare l'output della Fase 1 (es. idea video) alla Fase 2 (es. script writer) senza intervento umano.

2. **IDEMPOTENZA E MEMORIA:**
   - Il conductor deve leggere e scrivere lo stato in `YOUTUBE-AUTOMATION-FACTORY/06-DASHBOARD-E-METRICHE/state.json`. 
   - Se il processo si interrompe alla Fase 3, deve ripartire da lì.

3. **INTEGRAZIONE PUBBLICAZIONE:**
   - Prepara i log in console chiari e colorati (stile APEX) e assicurati che legga le API dal file `.env` (M-EST-8) che hai già sbloccato.

**REGOLE DI INGAGGIO:**
- Niente teoria. Solo codice Python `production-ready`, solido, type-hinted e commentato in italiano.
- Non chiedermi altri permessi: apri gli strumenti di codice, crea i file necessari, lancia i test di validazione sintattica, e mostrami il risultato quando la macchina è pronta a girare.
Procedi.
***
