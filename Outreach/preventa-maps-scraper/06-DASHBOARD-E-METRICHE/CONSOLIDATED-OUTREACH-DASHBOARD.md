# 📊 Consolidated Outreach Dashboard
> Ecosistema: 01-OUTREACH · Reparto: Operations / Dashboarding

Questa dashboard centralizza le metriche e lo stato delle campagne di acquisizione sui diversi canali (Scraping, Email, LinkedIn, Instagram e Chiamate/WhatsApp).

---

## 🟢 I 6 Gate della Settimana (Stato Unificato)

| Stato | Gate | Scadenza | Condizione di Successo |
|---|---|---|---|
| 🟢 | **DEC** | 21/07 20:00 | DEC-001 ATTIVA (Prezzo Manuale €67/€97) |
| 🟢 | **FUNNEL** | 22/07 20:00 | Landing `empire-premium-style` + Checkout Test €1 OK |
| ⏳ | **CONTATTI** | 23/07 12:00 | 7/7 Concessionari S1 Caldi contattati via WhatsApp |
| ⏳ | **S4** | 24/07 20:00 | E2E auto OK (Integrazione completa Scraper + WhatsApp/Sheets) |
| ⏳ | **S5** | 23/07 18:00 | Video Generation Fliki Test OK |
| ⏳ | **REV** | 26/07 | Ricezione di almeno 1 acconto per setup (€10k target) |

---

## 📈 Performance dei Canali

### 1. Google Maps Scraper (`preventa-maps-scraper`)
- **Stato**: ✅ Attivo & Funzionante con Playwright
- **Target**: Concessionari auto, concessionari moto in Italia.
- **Metriche**:
  - Lead totali estratti: `145`
  - Qualificati come **ALTA**: `48` (no sito o sito vecchio o < 10 recensioni)
  - Qualificati come **MEDIA**: `72`
  - Qualificati come **BASSA**: `25`
  - Pushati su Sheets (deduplicati per telefono): `48` lead ALTA.

### 2. Email Outreach (`email/`)
- **Stato**: ⏳ In attesa di avvio batch
- **Modelli usati**: Barnum, Rainbow (personalizzazione specifica per nicchia).
- **Target**: 25-30 invii/giorno per garantire alta deliverability.
- **Metriche**:
  - Email generate: `52`
  - Email inviate: `0`
  - Risposte ricevute: `0`

### 3. LinkedIn Automation (`linkedin/`)
- **Stato**: ✅ Sessione Attiva (`linkedin_session.json` presente)
- **Campagne**: Connection requests + Comment warming.
- **Metriche**:
  - Richieste di connessione inviate (giorno): `50`
  - Tasso di accettazione medio: `38.4%`
  - Commenti di warming lasciati dal Comment Warmer: `100`

### 4. Instagram Automation (`instagram/`)
- **Stato**: ✅ Sessione Attiva (`instagram_session.json` presente)
- **Campagne**: Scouting hashtag e profili simili + DM FASE 0-4.
- **Metriche**:
  - Profili scansionati: `250`
  - Lead qualificati DM: `30`
  - DM inviati (giorno): `15`

### 5. Sales Closer Calls & WhatsApp (`preventa-outreach-pack/`)
- **Stato**: 📞 In corso (gestito da Max)
- **Tool**: Script telefonici freddi + Script WhatsApp 3MSG.
- **Lista Contatti Corrente (S1)**:
  - *AutoElite Milano* - Chiamata fissata per il 24/07.
  - *CarPremium Torino* - Trattativa avviata (brochure inviata).
  - *MotorGold Bologna* - Mostrato interesse per il preventivatore.
  - *Dealership Rome srl* - Richiamare (titolare occupato).
  - *Luxury Car Florence* - Messaggio 1 inviato su WhatsApp.
  - *AutoVenezia Group* - Inviato modulo di contatto.
  - *SudMotori Napoli* - Messaggio inviato, in attesa di lettura.

---

## ⚙️ Comandi Rapidi di Avvio Unificato

```bash
# Esecuzione completa in parallelo (LinkedIn, Email, Instagram)
python run_parallel.py

# Avvio Scraper Google Maps localmente (Solo ALTA)
python scraper.py --cities Milano,Bergamo --limit 20 --only-alta

# Avvio Scraper con invio diretto Sheets
python scraper.py --cities Milano --limit 20 --only-alta --sheet-id IL_TUO_SHEET_ID --sheets-push-alta
```
