# 01_ricerca_no_sito
            
> Path: [[Map - Agenti|Agenti > Agency > outreach > rules]]

## Content

# REGOLA 01 — Ricerca Business Senza Sito Web

## OBIETTIVO
Identificare business locali che non hanno un sito web attivo, i quali rappresentano lead diretti per un copywriter/funnel strategist che può offrire la creazione di una presenza online completa.

## TRIGGER
- Esecuzione manuale dall'operatore
- Schedule settimanale automatico (consigliato: lunedì mattina)

## INPUT

| Campo | Obbligatorio | Tipo | Esempio |
|-------|-------------|------|---------|
| `città` | Sì | stringa | `"Milano"`, `"Roma"` |
| `categoria` | Sì | stringa | `"ristorante"`, `"idraulico"`, `"parrucchiere"` |
| `raggio_km` | No (default: 10) | intero | `5`, `15`, `20` |
| `max_risultati` | No (default: 60) | intero | `50`, `100` |

## OUTPUT
- Riga aggiunta nel foglio Google Sheets `[NOME_SHEET]` → tab `Lead_NoSito`
- Log operazione in `logs/YYYY-MM-DD_WF-A_[città]_[categoria].log`

### Colonne prodotte nel foglio:

| Colonna | Descrizione | Esempio |
|---------|-------------|---------|
| `ID_LEAD` | Identificatore unico | `NS-MI-20250115143022` |
| `DATA_TROVATO` | Timestamp scoperta | `2025-01-15 14:30:22` |
| `NOME_BUSINESS` | Nome attività | `Idraulico Rossi` |
| `CATEGORIA` | Categoria Google | `plumber` |
| `INDIRIZZO` | Indirizzo completo | `Via Roma 12, Milano` |
| `CITTÀ` | Città | `Milano` |
| `TELEFONO` | Numero di telefono | `+39 02 1234567` |
| `EMAIL` | Email se trovata | `info@rosi.it` |
| `RATING_GOOGLE` | Valutazione Google | `4.2` |
| `N_RECENSIONI` | Numero recensioni | `47` |
| `PLACE_ID` | ID Google Places | `ChIJxxx...` |
| `SCORE_PRIORITÀ` | Score 0-100 | `78` |
| `STATO_OUTREACH` | Status pipeline | `nuovo` |
| `NOTE` | Note libere | `` |

---

## STEP-BY-STEP

### Step 1 — Ricerca su Google Maps via Apify
1. Avvia run su Apify actor `APIFY_ACTOR_GOOGLE_MAPS` con input:
   - `searchStringsArray`: `["[categoria] [città]"]`
   - `maxCrawledPlacesPerSearch`: `max_risultati`
   - `language`: `"it"`, `country`: `"IT"`
2. Attendi completamento run (polling ogni 5s, timeout 300s)
3. Scarica dataset: ogni item include `title`, `placeId`, `address`, `phone`, `website`, `rating`, `reviewsCount`
4. Log: `"Apify: N business trovati per [categoria] in [città]"`

### Step 2 — Filtra business senza sito web
1. Per ogni business: controlla il campo `website` dalla risposta Places
2. Se `website` è vuoto o None → **candidato lead**
3. Se `website` è presente → esegui Step 2b prima di scartare

#### Step 2b — Verifica sito esistente (se `website` presente)
1. Fai HTTP GET al sito con timeout 10 secondi
2. Se risposta HTTP >= 400 oppure timeout → sito non funzionante → **candidato lead ugualmente**
3. Se risposta HTTP 200 → verifica se è una pagina reale (>500 caratteri di contenuto)
4. Se pagina praticamente vuota o è solo un domain parking → **candidato lead ugualmente**
5. Log per ogni check: `"[business_name]: sito [URL] → status [OK/BROKEN/EMPTY/NONE]"`

### Step 3 — Estrai contatti aggiuntivi
1. Se `phone` non presente nei dati Apify → cerca nel sito web (se rotto) con scraping diretto
2. Cerca email: visita home page + pagina "contatti" del sito → estrai da `mailto:` e regex
3. Nessuna API esterna: tutto via scraping diretto dal sito
4. Log: `"Contatti per [business_name]: tel=[tel], email=[email]"`

### Step 4 — Calcola Score Priorità
Formula score (0-100):

| Criterio | Punti |
|----------|-------|
| Rating Google >= 4.0 | +20 |
| Rating Google 3.5-3.9 | +10 |
| N. recensioni >= 50 | +20 |
| N. recensioni 20-49 | +10 |
| Telefono trovato | +20 |
| Email trovata | +20 |
| Categoria ad alta domanda (ristorante, dentista, avvocato, ecc.) | +10 |
| Sito completamente assente (vs sito rotto) | +10 |

Soglia minima per inserimento: **score >= 30**

### Step 5 — Deduplicazione
1. Confronta `PLACE_ID` con quelli già presenti nel foglio Google Sheets
2. Se già presente → salta, log: `"[business_name] già in database, skip"`
3. Se nuovo → procedi all'inserimento

### Step 6 — Inserimento in Google Sheets
1. Prepara riga con tutti i campi
2. Aggiungi riga in fondo al tab `Lead_NoSito`
3. Log: `"Lead [ID_LEAD] inserito: [NOME_BUSINESS]"`
4. Alla fine del run: log riepilogo `"Run completato: N candidati trovati, M nuovi lead inseriti, K duplicati saltati"`

---

## GESTIONE ERRORI

> **CORREZIONE APPLICATA (2026-02-28)**: `geocodifica_citta` silenziosamente ignorava le eccezioni con `pass`. Risolto aggiungendo logging esplicito. Rimossa variabile `id_esistenti` inutilizzata (deduplicazione avviene tramite `place_id_esistenti`).

| Errore | Causa probabile | Azione |
|--------|----------------|--------|
| `APIFY_API_TOKEN non valida` | Credenziale mancante/errata | Interrompi, log errore, exit 1 |
| `Run Apify FAILED` | Errore actor o quota esaurita | Retry x3 con backoff, poi interrompi |
| `Timeout HTTP sito web` | Sito lento o down | Considera il sito come "non funzionante", procedi |
| `Run Apify timeout (300s)` | Ricerca troppo ampia | Riduci max_risultati, riprova |
| `Nessun risultato Apify` | Categoria/città senza risultati | Log warning, termina run senza errori |
| `Scrittura CSV fallita` | Permessi disco | Log errore, continua con i lead rimanenti |

---

## CASI LIMITE

- **Business con sito in costruzione** ("coming soon"): trattare come senza sito (score pieno)
- **Business con solo pagina Facebook** (nessun sito): trattare come senza sito
- **Business con più sedi**: inserire ogni sede come lead separato con ID diversi
- **Categoria in inglese vs italiano**: il sistema accetta entrambi (Google Places usa termini inglesi internamente)
- **Città con spazio** (es. "San Giovanni"): codificare con %20 nell'URL API

---

## TEMPLATE EMAIL (usato da WF-D)
Vedi `rules/04_drafta_email.md` → Template A: Business Senza Sito

---

## LOG

Ogni run produce un file di log: `logs/YYYY-MM-DD_WF-A_[città]_[categoria].log`

Contenuto minimo del log:
```
[2025-01-15 14:30:00] START — Ricerca: ristorante in Milano, raggio 10km
[2025-01-15 14:30:02] Google Places: 47 risultati trovati
[2025-01-15 14:30:15] Check siti: 32 senza sito, 15 con sito (di cui 3 rotti)
[2025-01-15 14:30:45] Scoring: 28 lead sopra soglia 30
[2025-01-15 14:30:50] Deduplicazione: 5 già presenti, 23 nuovi
[2025-01-15 14:30:52] Inseriti 23 lead nel foglio Lead_NoSito
[2025-01-15 14:30:52] END — Durata: 52s
```

## Collegamenti Correlati
- [[Map - Agenti|Agenti Area]]
- [[Map - App|App Area]]
- [[Map - Outreach|Outreach Area]]
