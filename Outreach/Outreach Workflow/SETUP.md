# SETUP — Digital Empire Outreach Automatico

## In 15 minuti sei operativo. Segui questa guida nell'ordine esatto.

---

## PASSO 1 — Installa le dipendenze (2 minuti)

Apri il terminale nella cartella `Outreach/` e lancia:

```bash
pip install -r requirements.txt
```

Poi copia il file di configurazione:

```bash
cp .env.example .env
```

---

## PASSO 2 — Token Facebook Ad Library (5 minuti)

Il Token Facebook ti permette di cercare gratis tutti i business che fanno ads in Italia.
**GRATUITO. Nessun costo.**

### Come ottenerlo:

1. Vai su **https://developers.facebook.com/tools/explorer**
   (devi essere loggato con il tuo account Facebook)

2. In alto a destra, clicca su **"My Apps"** → se non hai un'app, clicca **"Create New App"**
   - Tipo: **"Consumer"**
   - Nome: qualsiasi (es. "Digital Empire")
   - Clicca "Create App"

3. Torna su **https://developers.facebook.com/tools/explorer**
   - Seleziona la tua app dal menu a tendina in alto
   - Clicca **"Generate Access Token"**
   - Nella lista permessi, spunta **`ads_read`**
   - Clicca "Generate Access Token" e conferma su Facebook

4. Copia il token che appare (inizia con "EAAg...")

5. **IMPORTANTE — token a lunga durata (60 giorni):**
   Il token generato dura solo 1-2 ore. Per ottenerne uno valido 60 giorni:
   
   Vai su: `https://developers.facebook.com/tools/debug/accesstoken`
   - Incolla il token corto
   - Clicca "Debug"
   - Sotto, clicca **"Extend Access Token"**
   - Copia il nuovo token lungo (EAAg... molto più lungo)

6. Incolla il token nel file `.env`:
   ```
   FB_ACCESS_TOKEN=EAAg[...il tuo token...]
   ```

> Il token scade ogni 60 giorni. Imposta un promemoria per rinnovarlo.

---

## PASSO 3 — App Password Gmail (3 minuti)

Devi usare una **App Password**, NON la tua password normale.
È un codice di 16 caratteri che Gmail genera apposta per le app.

### Come ottenerla:

1. Vai su **https://myaccount.google.com/security**
   (devi avere la **verifica in due passaggi attiva** — se non ce l'hai, attivala prima)

2. Scorri fino a **"Come accedi a Google"** → clicca **"Password per le app"**
   (oppure vai direttamente su: **https://myaccount.google.com/apppasswords**)

3. In "Seleziona app" scegli **"Mail"**
   In "Seleziona dispositivo" scegli **"Computer Windows"**

4. Clicca **"Genera"** — appare un codice di 16 caratteri tipo: `abcd efgh ijkl mnop`

5. Copia questo codice **SENZA spazi** nel file `.env`:
   ```
   GMAIL_APP_PASSWORD=abcdefghijklmnop
   ```

> Nota: La password `Max.23.09` nel vecchio .env NON funziona — non è un'App Password.

---

## PASSO 4 — API Key Anthropic (già configurata)

La tua API key Anthropic è già nel file `Agenti/Agency/.env`.
Copiala nel nuovo `.env` della cartella Outreach:

```
ANTHROPIC_API_KEY=sk-ant-api03-AZTq4LM...
```

---

## PASSO 5 — Configura il .env finale

Il file `Outreach/.env` deve avere questi 4 valori:

```env
ANTHROPIC_API_KEY=sk-ant-api03-...    ← da Agenti/Agency/.env
FB_ACCESS_TOKEN=EAAg...               ← dal passo 2
GMAIL_USER=max.infoproducer@gmail.com ← già sai questa
GMAIL_APP_PASSWORD=abcdefghijklmnop   ← dal passo 3
```

---

## PASSO 6 — Test (senza inviare email reali)

Prima di lanciare in produzione, testa il sistema:

```bash
# Dalla cartella Outreach/:
python run.py --target 10 --anteprima
```

Questo comando:
- Cerca 20 business su Facebook Ads
- Trova le loro email
- Genera 10 email personalizzate con Claude
- **NON le invia** — le mostra solo su schermo

Se tutto funziona, vedrai le email generate per 10 business reali.

---

## PASSO 7 — Lancio in produzione

```bash
python run.py
```

Questo invia **500 email al giorno** in automatico.

Oppure personalizza:

```bash
python run.py --target 200    # Solo 200 email
python run.py --target 500    # 500 email (massimo Gmail free)
```

---

## COSTI

| Servizio | Costo |
|----------|-------|
| Facebook Ad Library API | **GRATUITO** |
| Email extractor (scraping) | **GRATUITO** |
| Gmail SMTP | **GRATUITO** (500/giorno) |
| Claude Haiku (500 email) | **~$0.50/giorno** |
| **TOTALE** | **~$15/mese** |

---

## ARCHITETTURA AGENTI

Il sistema segue il pattern **Orchestratore + Worker Agents** di Anthropic:

```
run.py
 └── OutreachOrchestrator (orchestrator.py)
      ├── FacebookScraperAgent  → cerca business da FB Ads (gratis)
      ├── EmailExtractorAgent   → trova email sui siti (gratis)
      ├── EmailWriterAgent      → scrive email con Claude Haiku ($)
      └── EmailSenderAgent      → invia via Gmail SMTP (gratis)
```

Ogni agente:
- Ha una sola responsabilità
- Comunica tramite liste di dizionari Python
- Può fallire senza bloccare gli altri
- Logga tutto in `output/`

---

## STRUTTURA FILE

```
Outreach/
├── SETUP.md              ← questa guida
├── run.py                ← lancia tutto da qui
├── requirements.txt
├── .env.example          ← template configurazione
├── .env                  ← TUA configurazione (non committare!)
│
├── agents/
│   ├── orchestrator.py   ← coordina i 4 agenti
│   ├── scraper.py        ← Facebook Ad Library API
│   ├── extractor.py      ← estrae email dai siti
│   ├── writer.py         ← Claude: scrive email personalizzate
│   └── sender.py         ← Gmail SMTP
│
└── output/
    ├── leads.db                     ← database deduplicazione
    └── YYYY-MM-DD_invio_log.csv     ← log giornaliero invii
```

---

## TROUBLESHOOTING

**"FB_ACCESS_TOKEN non valido"**
→ Il token è scaduto (dura 60 giorni). Rinnova seguendo il Passo 2.

**"ERRORE AUTENTICAZIONE Gmail"**
→ Stai usando la password normale invece dell'App Password. Rileggi Passo 3.

**"Nessuna email trovata"**
→ I siti web trovati non espongono email. Il sistema continuerà a trovarne altri.

**"Rate limit Anthropic"**
→ Aumenta l'intervallo tra le generazioni. Il sistema riprova automaticamente.

**"Nessun business trovato su Facebook"**
→ Il token FB non ha il permesso `ads_read`. Ricrea il token con quel permesso.

---

## RINNOVARE IL TOKEN FACEBOOK (ogni 60 giorni)

1. Vai su `https://developers.facebook.com/tools/explorer`
2. Genera nuovo token con permesso `ads_read`
3. Estendi a 60 giorni su `https://developers.facebook.com/tools/debug/accesstoken`
4. Aggiorna `.env` con il nuovo token

Imposta un promemoria nel calendario tra 55 giorni.
