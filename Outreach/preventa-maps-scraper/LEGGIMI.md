# Preventa Maps Scraper - Playwright ONLY + Areus + Filtro ALTA - LEGGIMI
### v3.0 - Niente API Key Maps, solo browser reale + push automatico su Areus (CRM interno)

---

### 1. COSA FA ORA (aggiornato)

Stesso motore Playwright di prima + 2 novità:

1.  **Filtro `--only-alta`**: salva CSV con solo priorità ALTA (no sito / sito vecchio / <10 recensioni) + crea automaticamente file `_SOLO_ALTA.csv` pronto per dialer.

2.  **Push automatico su Areus** (il CRM di EmpireDesk/Aureus Agency OS, la piattaforma unica
    dell'azienda): dedup per telefono, nessuna credenziale da configurare — attivo di default.
    I lead entrano in Areus con stage `NEW` (freddo), e da lì tracci contattato/risposto/non
    risposto nella stessa app, non su un foglio esterno.

Flusso completo:

```
Maps (Playwright) -> estrae 25 lead/città -> calcola priorita_lead
-> salva data/leads_concessionari.csv (tutti)
-> se --only-alta: salva anche data/leads_concessionari_SOLO_ALTA.csv (solo ALTA)
-> push su Areus (default attivo; --no-areus per disattivarlo, --areus-push-alta per solo ALTA)
-> visibile subito in EmpireDesk -> pannello "Preventa"
-> import diretto in outreach APSOC (contact_leads.py aggiorna lo stage a CONTACTED)
```

---

### 2. INSTALLAZIONE

```bash
cd preventa-maps-scraper

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
playwright install chromium

cp .env.example .env
# Areus funziona senza configurare nulla. Modifica .env solo se la struttura cartelle
# Digital Empire/EmpireDesk non e' quella standard (vedi AREUS_STATE_PATH).
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

### 4. USO AVANZATO - PUSH AUTOMATICO SU AREUS

Nessun setup richiesto: il push su Areus è **attivo di default**, scrive un file JSON locale
(`EmpireDesk/state/preventa_leads.json`) che il modulo `EmpireDesk/modules/preventa.py` legge e
serve al pannello "Preventa — Outreach Freddo" dentro Areus.

#### Lancio normale (push automatico incluso)

```bash
python scraper.py --input cities.txt --limit 25 --only-alta
```

**Push solo ALTA (consigliato, per non sporcare il CRM con lead BASSA):**
```bash
python scraper.py --cities Milano,Bergamo --limit 25 --only-alta --areus-push-alta
```

**Disattivare il push (solo CSV locale):**
```bash
python scraper.py --input cities.txt --no-areus
```

**Override path (solo se la struttura cartelle non è quella standard):**
```bash
python scraper.py --input cities.txt --areus-state-path "C:/altro/path/preventa_leads.json"
```

**Cosa succede:**
- Legge i lead già presenti in Areus, confronta per `telefono` normalizzato
- Salta lead con telefono già presente (deduplica)
- Ogni lead nuovo entra con stage `NEW` (freddo, non ancora contattato)
- Log: `✅ Areus: 18 nuovi lead aggiunti (Milano), 7 duplicati saltati`

**Campi salvati:** uguali al CSV (nome_attivita, indirizzo, telefono, sito_web, ha_sito, numero_recensioni, media_recensioni, ha_ads_attive, priorita_lead, citta_ricerca, categoria, note_qualifica, maps_url, data_estrazione) + `stage`, `note`, `aggiunto_il`.

---

### 5. ESEMPI COMBINATI PER MAX

**Workflow giornaliero S1-Freddo consigliato:**

```bash
# 1. Scrapa 5 nuove città, solo ALTA, pusha su Areus (default attivo)
python scraper.py --cities Como,Lecco,Sondrio,Varese,Novara --limit 30 --only-alta --areus-push-alta

# 2. Esporta CSV SOLO ALTA per dialer (backup locale)
# File: data/leads_concessionari_SOLO_ALTA.csv

# 3. Contatti i lead da Areus (pannello "Preventa"), o dai in pasto al runner outreach:
python contact_leads.py
# marca ogni lead contattato come stage=CONTACTED direttamente in Areus
```

**Automazione cron (ogni lunedì 9:00):**
```bash
crontab -e
# aggiungi:
0 9 * * 1 cd /path/preventa-maps-scraper && .venv/bin/python scraper.py --input cities.txt --only-alta --areus-push-alta >> logs/scraper.log 2>&1
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
| `--no-areus` | False | Disattiva il push su Areus (default: attivo, no credenziali) |
| `--areus-state-path` | env `AREUS_STATE_PATH` o auto | Override path JSON condiviso con EmpireDesk |
| `--areus-push-alta` | False | Se true, pusha solo ALTA su Areus |

---

### 7. RATE-LIMITING E ANTI-BLOCCO

Già incluso rispettoso:
- 0.6-1.2s tra click scheda
- 1.2-2.8s tra lead
- 3-6s tra città
- Scrittura Areus istantanea a fine città (nessun batching/rete esterna)

Non abbassare. Se vedi `debug_*.png` con captcha, ferma 30-60 min, rilancia con `--headed` da IP residenziale.

---

### 8. INTEGRAZIONE CON OUTREACH PACK

Dopo che Areus si popola:

1. Agente legge nuove righe con `priorita_lead=ALTA` da Areus (o da `_SOLO_ALTA.csv`)
2. Sceglie gancio da `04_5_VARIANTI_GANCIO_AB.md`:
   - ALTA no sito → Gancio 3 (PDF brutto)
   - ALTA poche rec → Gancio 2 (cliente perso WA)
   - MEDIA → Gancio 1 (tempo perso)
3. Chiama con `01_SCRIPT_CHIAMATA_FREDDA` → se no answer → WA MSG1 file 02
4. Obiezioni → `03_ARGOMENTARIO`
5. Follow-up → `05_FOLLOW_UP`

---

### 9. TROUBLESHOOTING AREUS

| Errore | Fix |
|--------|-----|
| Lead non compaiono in EmpireDesk | Verifica che `EmpireDesk/state/preventa_leads.json` esista e che il path calcolato corrisponda alla tua struttura cartelle (altrimenti usa `--areus-state-path`) |
| Duplicati non filtrati | Deduplica è su telefono normalizzato. Se telefono vuoto, non deduplica - normale. Pulisci manuale. |
| Vuoi solo il CSV locale, niente Areus | `--no-areus` |

---

### 10. QUICKSTART FINALE PER TE

```bash
pip install -r requirements.txt
playwright install chromium

# Test senza push (solo CSV locale):
python scraper.py --cities Milano,Bergamo --limit 15 --only-alta --no-areus

# Uso normale: push su Areus automatico, solo ALTA:
python scraper.py --cities Milano --limit 10 --only-alta --areus-push-alta
```

Fatto. Motore + filtro + push Areus automatico.

— v3.0 Playwright + Areus - 28/07/2026
