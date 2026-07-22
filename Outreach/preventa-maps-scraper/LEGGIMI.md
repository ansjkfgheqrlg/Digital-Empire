# Preventa Maps Scraper - Playwright ONLY + Google Sheets + Filtro ALTA - LEGGIMI
### v2.1 - Niente API Key Maps, solo browser reale + push automatico Sheets

---

### 1. COSA FA ORA (aggiornato)

Stesso motore Playwright di prima + 2 novità che hai chiesto:

1.  **Filtro `--only-alta`**: salva CSV con solo priorità ALTA (no sito / sito vecchio / <10 recensioni) + crea automaticamente file `_SOLO_ALTA.csv` pronto per dialer.

2.  **Push automatico Google Sheets** con deduplica per telefono:
    `--sheet-id` + service account JSON → aggiunge solo lead nuovi, salta duplicati già presenti nel foglio.

Flusso completo:

```
Maps (Playwright) -> estrae 25 lead/città -> calcola priorita_lead
-> salva data/leads_concessionari.csv (tutti)
-> se --only-alta: salva anche data/leads_concessionari_SOLO_ALTA.csv (solo ALTA)
-> se --sheet-id: pusha su Sheets (opzione --sheets-push-alta per pushare solo ALTA)
-> import diretto in outreach APSOC
```

---

### 2. INSTALLAZIONE

```bash
cd preventa-maps-scraper

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
playwright install chromium

# Se vuoi anche Sheets:
pip install gspread google-auth

cp .env.example .env
# modifica .env se usi Sheets
```

**Niente API key per Maps.** Playwright gira in Chromium locale.

---

### 3. USO BASE - SOLO PLAYWRIGHT + FILTRO ALTA

#### Solo ALTA nel CSV (consigliato per S1-Freddo)
```bash
python scraper.py --cities Milano,Bergamo,Brescia --limit 25 --only-alta --output data/leads.csv
```
Output:
- `data/leads.csv` = tutti ma ordinati ALTA prima
- `data/leads_SOLO_ALTA.csv` = solo ALTA (quello che dai al closer)

#### Senza filtro (tutti i lead)
```bash
python scraper.py --cities Torino,Verona --limit 20 --output data/leads_torino.csv
```

#### Batch da file
```bash
cp cities.txt.example cities.txt
# modifica cities.txt
python scraper.py --input cities.txt --limit 25 --only-alta
```

---

### 4. USO AVANZATO - PUSH AUTOMATICO SU GOOGLE SHEETS

#### Step A: Crea Service Account (una tantum, 3 min)

1. Vai su https://console.cloud.google.com/ → Crea progetto `Preventa-Sheets`
2. Abilita API: **Google Sheets API** + **Google Drive API**
3. IAM & Admin → Service Accounts → Create Service Account → Nome `preventa-sheets-pusher`
4. Keys → Add Key → Create New Key → JSON → scarica file (es. `credentials.json`)
5. Metti file nella cartella scraper: `cp ~/Downloads/*.json ./credentials.json`
6. Crea Google Sheet vuoto (es. "Preventa Lead S1-Freddo") → copia ID dalla URL:
   `https://docs.google.com/spreadsheets/d/1aBcDeFgHiJkLmNoPqRs.../edit` → ID = `1aBcDe...`
7. **Condividi** il Sheet con l'email del service account (tipo `preventa-sheets-pusher@...iam.gserviceaccount.com`) come **Editor**

#### Step B: Configura .env

```bash
GOOGLE_SHEET_ID=1aBcDeFgHiJkLmNoPqRsTuVw...
GOOGLE_SHEETS_CREDS_PATH=credentials.json
```

#### Step C: Lancia con push

**Push solo ALTA (consigliato per non sporcare sheet):**
```bash
python scraper.py --cities Milano,Bergamo --limit 25 --only-alta --sheet-id 1aBcDeFg... --sheets-push-alta --sheets-creds credentials.json
```

**Push tutti:**
```bash
python scraper.py --input cities.txt --sheet-id 1aBcDeFg... --sheets-creds credentials.json
```

**Cosa succede:**
- Legge righe esistenti nel foglio, prende colonna `telefono` normalizzata
- Salta lead con telefono già presente (deduplica)
- Pusha a batch da 50 righe con 1s di pausa
- Log: `✅ Sheets upload completo: 18 nuovi, 7 duplicati saltati`

**Colonne Sheet:** uguali al CSV: nome_attivita, indirizzo, telefono, sito_web, ha_sito, numero_recensioni, media_recensioni, ha_ads_attive, priorita_lead, citta_ricerca, categoria, note_qualifica, maps_url, data_estrazione

Se Sheet vuoto, crea header automaticamente.

---

### 5. ESEMPI COMBINATI PER MAX

**Workflow giornaliero S1-Freddo consigliato:**

```bash
# 1. Scrapa 5 nuove città, solo ALTA, pusha su Sheets
python scraper.py --cities Como,Lecco,Sondrio,Varese,Novara --limit 30 --only-alta --sheet-id $GOOGLE_SHEET_ID --sheets-push-alta

# 2. Esporta CSV SOLO ALTA per dialer
# File: data/leads_concessionari_SOLO_ALTA.csv

# 3. Dai in pasto a agente outreach APSOC (preventa-outreach-pack)
# L'agente legge CSV, sceglie gancio in base a priorità (ALTA no sito -> Gancio 3)
```

**Automazione cron (ogni lunedì 9:00):**
```bash
crontab -e
# aggiungi:
0 9 * * 1 cd /path/preventa-maps-scraper && .venv/bin/python scraper.py --input cities.txt --only-alta --sheet-id X --sheets-push-alta >> logs/scraper.log 2>&1
```

---

### 6. ARGOMENTI CLI COMPLETI

| Arg | Default | Cosa fa |
|-----|---------|---------|
| `--cities` | - | `Milano,Bergamo` inline |
| `--input` | - | File txt una città per riga |
| `--categoria` | `concessionario auto` | Cambia in `concessionario moto` ecc. |
| `--limit` | 25 | Max risultati per città |
| `--output` | `data/leads_concessionari.csv` | Path CSV |
| `--only-alta` | False | Salva solo ALTA + file `_SOLO_ALTA.csv` |
| `--headless` | False | Headless (più rischio blocco, ma ok su server) |
| `--headed` | default | Visibile (consigliato) |
| `--sheet-id` | env GOOGLE_SHEET_ID | ID Google Sheet |
| `--sheets-creds` | `credentials.json` | Path JSON service account |
| `--sheets-worksheet` | `Foglio1` | Nome worksheet |
| `--sheets-push-alta` | False | Se true, pusha solo ALTA su Sheets |

---

### 7. RATE-LIMITING E ANTI-BLOCCO

Già incluso rispettoso:
- 0.6-1.2s tra click scheda
- 1.2-2.8s tra lead
- 3-6s tra città
- 1 batch Sheets + 1s pausa

Non abbassare. Se vedi `debug_*.png` con captcha, ferma 30-60 min, rilancia con `--headed` da IP residenziale.

---

### 8. INTEGRAZIONE CON OUTREACH PACK

Dopo che Sheets si popola:

1. Agente legge nuove righe con `priorita_lead=ALTA` da Sheets (o da `_SOLO_ALTA.csv`)
2. Sceglie gancio da `04_5_VARIANTI_GANCIO_AB.md`:
   - ALTA no sito → Gancio 3 (PDF brutto)
   - ALTA poche rec → Gancio 2 (cliente perso WA)
   - MEDIA → Gancio 1 (tempo perso)
3. Chiama con `01_SCRIPT_CHIAMATA_FREDDA` → se no answer → WA MSG1 file 02
4. Obiezioni → `03_ARGOMENTARIO`
5. Follow-up → `05_FOLLOW_UP`

---

### 9. TROUBLESHOOTING SHEETS

| Errore | Fix |
|--------|-----|
| `File credenziali non trovato` | Metti `credentials.json` nella cartella o specifica `--sheets-creds /path/file.json` |
| `gspread.exceptions.APIError: PERMISSION_DENIED` | Non hai condiviso Sheet con email service account come Editor |
| `ModuleNotFoundError: gspread` | `pip install gspread google-auth` |
| Duplicati non filtrati | Deduplica è su telefono normalizzato. Se telefono vuoto, non deduplica - normale. Pulisci manuale. |
| Sheet vuoto non scrive header | Cancella prima riga vuota, rilancia. Codice scrive header se A1 vuota. |

---

### 10. QUICKSTART FINALE PER TE

```bash
pip install -r requirements.txt
playwright install chromium

# Test senza Sheets, solo ALTA locale:
python scraper.py --cities Milano,Bergamo --limit 15 --only-alta

# Test con Sheets, solo ALTA pushati:
python scraper.py --cities Milano --limit 10 --only-alta --sheet-id 1TUO_ID --sheets-push-alta --sheets-creds credentials.json
```

Fatto. Motore + filtro + push Sheets automatico.

— v2.1 Playwright + Sheets - 22/07/2026
