# 02_ricerca_ads_funnel_scarsi

> Source: File system (`Agenti\Agency\outreach\rules\02_ricerca_ads_funnel_scarsi.md`)
> Collected: 2026-05-06
> Published: Unknown

# REGOLA 02 — Ricerca Business che Fanno Ads con Funnel Scarsi

## OBIETTIVO
Trovare business che investono in pubblicità a pagamento (Facebook/Instagram/Google Ads) ma hanno landing page o funnel di vendita scadenti, rappresentando lead ideali per un copywriter/funnel strategist che può aumentare il ROI delle loro campagne.

## TRIGGER
- Esecuzione manuale dall'operatore
- Schedule settimanale automatico (consigliato: lunedì mattina, dopo WF-A)

## INPUT

| Campo | Obbligatorio | Tipo | Esempio |
|-------|-------------|------|---------|
| `settore` | Sì | stringa | `"dentista"`, `"palestra"`, `"immobiliare"` |
| `città` | Sì | stringa | `"Milano"`, `"Roma"` |
| `paese` | No (default: IT) | stringa ISO | `"IT"`, `"US"` |
| `max_ads` | No (default: 50) | intero | `30`, `100` |

## OUTPUT
- Riga aggiunta nel foglio Google Sheets → tab `Lead_FunnelScarso`
- Log in `logs/YYYY-MM-DD_WF-B_[settore]_[città].log`

### Colonne prodotte nel foglio:

| Colonna | Descrizione | Esempio |
|---------|-------------|---------|
| `ID_LEAD` | Identificatore unico | `AF-RM-20250115150000` |
| `DATA_TROVATO` | Timestamp | `2025-01-15 15:00:00` |
| `NOME_PAGINA` | Nome pagina Facebook | `Studio Dentistico Bianchi` |
| `SETTORE` | Settore dell'attività | `dentista` |
| `CITTÀ` | Città | `Roma` |
| `URL_PAGINA_FB` | URL pagina Facebook | `https://facebook.com/...` |
| `URL_LANDING` | URL landing page trovata | `https://...` |
| `TELEFONO` | Telefono se trovato | `+39 06 123456` |
| `EMAIL` | Email se trovata | `info@...` |
| `SCORE_FUNNEL` | Score qualità funnel (0-100) | `32` |
| `DETTAGLIO_SCORE` | Breakdown del score | `lentezza:−20, no_optin:−25, ...` |
| `N_ADS_ATTIVI` | Numero di ads attivi | `3` |
| `STATO_OUTREACH` | Status pipeline | `nuovo` |
| `NOTE` | Note libere | `` |

---

## STEP-BY-STEP

### Step 1 — Raccolta Ads da Facebook Ad Library via Apify
1. Avvia run su Apify actor `APIFY_ACTOR_FACEBOOK_ADS` con input:
   - `startUrls`: URL della Facebook Ad Library con query pre-impostata per il settore e paese
   - `searchTerms`: `[settore]`
   - `country`: paese ISO
   - `activeStatus`: `"ACTIVE"`
   - `maxItems`: max_ads
2. Attendi completamento run (polling ogni 5s, timeout 300s)
3. Scarica dataset: ogni item include `pageName`, `pageId`, `adCreativeLinkUrl`, `adBody`, `adTitle`, `pageUrl`
4. Filtra risultati per città (cerca nome città nel testo dell'ad o nome pagina)
5. Log: `"Apify Facebook Ads: N ads trovati per [settore] in [paese]"`

### Step 2 — Analisi Landing Page (Funnel Score)
Per ogni business trovato, analizza la loro landing page. Lo script `utils/website_checker.py` esegue questa analisi.

#### Criteri di analisi e penalità:

**COPY E STRUTTURA (max −40 punti)**
- Nessun headline chiaro (H1 assente o generico) → −15 punti
- Nessun form di contatto o opt-in → −15 punti
- Nessuna CTA (call-to-action) visibile → −10 punti

**CREDIBILITÀ (max −20 punti)**
- Nessuna testimonianza o social proof → −10 punti
- Nessun numero di telefono in evidenza → −5 punti
- Nessuna garanzia o policy → −5 punti

**TRACKING (max −10 punti)**
- Nessun Pixel Facebook installato → −5 punti
- Nessun Google Analytics → −5 punti

**Score iniziale: 100 punti.** Si sottraggono i punti delle penalità.

Soglia per inserire come lead: **score <= 60** (funnel oggettivamente migliorabile)

### Step 3 — Estrai Contatti
1. Dalla pagina Facebook: cerca telefono, email, sito web
2. Dalla landing page: cerca telefono con regex `(\+39|0039)?[\s\-]?0?[0-9]{2,4}[\s\-][0-9]{6,8}`
3. Cerca email con regex `[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+`
4. Se Hunter.io configurato: cerca email tramite dominio del sito
5. Log: `"[nome_pagina]: tel=[tel], email=[email]"`

### Step 4 — Deduplicazione
1. Confronta `URL_PAGINA_FB` con quelli già nel foglio
2. Se già presente → skip + log
3. Se nuovo → inserisci

### Step 5 — Inserimento in Google Sheets
1. Prepara riga con tutti i campi
2. Appendi al tab `Lead_FunnelScarso`
3. Log: `"Lead [ID_LEAD] inserito: [NOME_PAGINA] — Score Funnel: [score]"`

---

## GESTIONE ERRORI

> **CORREZIONE APPLICATA (2026-02-28)**: La funzione `cerca_ads_facebook` aveva un bug di paginazione — i parametri venivano reimpostati ma non passati alla seconda request, causando il fetching in loop della prima pagina. Risolto ristrutturando il loop per usare `url_corrente` che viene aggiornato ad ogni iterazione.

| Errore | Causa probabile | Azione |
|--------|----------------|--------|
| `APIFY_API_TOKEN non valido` | Token mancante o scaduto | Interrompi, log errore, exit 1 |
| `Run Apify FAILED` | Errore actor o quota Apify | Retry x3 con backoff, poi interrompi |
| `Landing page irraggiungibile` | Sito down o bloccato | Score funnel = 0 (è un problema enorme), inserisci comunque |
| `Run Apify timeout (300s)` | Ricerca troppo ampia | Riduci max_ads, riprova |
| `Nessun ad trovato` | Settore/luogo senza ads | Log info, termina senza errori |
| `Landing page in altro paese` | Ad nazionale, non locale | Includi comunque se settore corretto |

---

## CASI LIMITE

- **Business con più landing page** (una per ogni ad): analizza solo la prima trovata, annota nelle NOTE
- **Landing page con redirect** (es. link shortener): segui il redirect fino a 3 hop
- **Pagina Facebook senza sito** (solo form Facebook Lead Ads): score funnel = 10 automatico, ottimo lead
- **Ads senza URL landing** (solo immagine o video): salta questo ad, passa al prossimo
- **Score border-line** (59-61): inserisci con nota "verificare manualmente"

---

## TEMPLATE EMAIL (usato da WF-D)
Vedi `rules/04_drafta_email.md` → Template B: Business con Ads e Funnel Scarso

---

## LOG

File: `logs/YYYY-MM-DD_WF-B_[settore]_[città].log`

```
[2025-01-15 15:00:00] START — Ricerca ads: dentista in IT, filtro città Roma
[2025-01-15 15:00:03] Facebook Ad Library: 38 ads trovati
[2025-01-15 15:00:03] Business unici: 21 pagine diverse
[2025-01-15 15:00:45] Analisi funnel: 21 landing analizzate
[2025-01-15 15:00:45] Risultati: 14 score <= 60 (lead), 7 funnel ok (esclusi)
[2025-01-15 15:01:00] Deduplicazione: 2 già presenti, 12 nuovi lead
[2025-01-15 15:01:02] Inseriti 12 lead nel foglio Lead_FunnelScarso
[2025-01-15 15:01:02] END — Durata: 62s
```
