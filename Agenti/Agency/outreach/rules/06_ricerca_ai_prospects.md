# REGOLA 06 — Ricerca Prospect per Implementazione AI

## OBIETTIVO
Trovare aziende strutturate (10+ dipendenti) che hanno processi manuali e ripetitivi nelle loro operazioni quotidiane — processi che possono essere automatizzati con agenti AI custom. Questi sono prospect per il **Servizio 2: AI Implementation**.

Il segnale chiave: l'azienda spende soldi in personale o tool per fare cose che l'AI potrebbe fare meglio, più velocemente e a minor costo.

## TRIGGER
- Esecuzione manuale dall'operatore
- Schedule settimanale automatico (consigliato: martedì mattina)

## INPUT

| Campo | Obbligatorio | Tipo | Esempio |
|-------|-------------|------|---------|
| `settore` | Sì | stringa | `"logistica"`, `"immobiliare"`, `"studi legali"` |
| `città` | Sì | stringa | `"Milano"`, `"Roma"`, `"Torino"` |
| `dimensione_min` | No (default: 10) | intero | `10`, `50` |
| `max_risultati` | No (default: 40) | intero | `20`, `60` |

### Settori ad alta priorità (alto potenziale di automazione)
- Logistica e trasporti (tracking, comunicazioni con clienti, reportistica)
- Studi legali e commercialisti (elaborazione documenti, contratti, fatture)
- Agenzie immobiliari (qualifica lead, follow-up, gestione appuntamenti)
- E-commerce e retail (customer service, gestione ordini, resi)
- Cliniche e studi medici (prenotazioni, follow-up pazienti, documentazione)
- Agenzie marketing (reportistica clienti, analisi dati, brief creativi)
- Aziende manifatturiere (ordini fornitori, qualità, reportistica)

## OUTPUT
- Riga aggiunta nel foglio Google Sheets → tab `Lead_AIProspect`
- Log in `logs/YYYY-MM-DD_WF-F_[settore]_[città].log`

### Colonne prodotte nel foglio:

| Colonna | Descrizione | Esempio |
|---------|-------------|---------|
| `ID_LEAD` | Identificatore unico | `AI-MI-20250115143022` |
| `DATA_TROVATO` | Timestamp scoperta | `2025-01-15 14:30:22` |
| `NOME_AZIENDA` | Nome azienda | `Logistica Rossi Srl` |
| `SETTORE` | Settore di attività | `logistica` |
| `CITTÀ` | Città sede | `Milano` |
| `SITO_WEB` | URL sito aziendale | `https://logistica-rossi.it` |
| `EMAIL` | Email contatto | `info@logistica-rossi.it` |
| `TELEFONO` | Telefono | `+39 02 1234567` |
| `REFERENTE` | Nome decisore (se trovato) | `Marco Rossi` |
| `N_DIPENDENTI_STIMATO` | Dimensione stimata | `20-50` |
| `SEGNALI_AUTOMAZIONE` | Processi manuali rilevati | `data entry, back office, customer service` |
| `OFFERTE_LAVORO_TROVATE` | Annunci che segnalano processi manuali | `"Cercasi segretaria back office"` |
| `TOOL_USATI` | Software aziendali visibili | `Salesforce, Excel, Google Workspace` |
| `SCORE_AI_POTENZIALE` | Score opportunità AI (0-100) | `74` |
| `PROCESSO_TARGET` | Processo principale da automatizzare | `gestione email clienti + reportistica` |
| `STATO_OUTREACH` | Status pipeline | `nuovo` |
| `NOTE` | Note libere | `` |

---

## STEP-BY-STEP

### Step 1 — Ricerca aziende tramite Google
1. Esegui ricerche Google con query mirate:
   - `"[settore] srl" OR "studio [settore]" "[città]" site:linkedin.com/company`
   - `"[settore]" "[città]" "contatti" "about us" -linkedin`
   - `"[settore] [città]" filetype:pdf OR "chi siamo"`
2. Estrai: nome azienda, URL sito, eventuali contatti
3. Log: `"Trovate N aziende candidate per [settore] in [città]"`

### Step 2 — Ricerca offerte di lavoro (segnale di processo manuale)
1. Cerca su LinkedIn Jobs, Indeed e InfoJobs con query:
   - `"[settore]" "[città]" ("back office" OR "data entry" OR "segreteria" OR "amministrativo" OR "customer service" OR "addetto inserimento dati")`
2. Per ogni offerta trovata: estrai nome azienda e tipo di ruolo cercato
3. Il tipo di ruolo è un **segnale diretto** del processo manuale esistente:
   - "Addetto data entry" → inserimento dati manuale
   - "Customer service" → gestione comunicazioni manuali
   - "Segreteria" → scheduling e comunicazioni manuali
   - "Back office amministrativo" → processi documentali manuali
   - "Preventivista" → generazione offerte manuali
4. Log: `"Offerte di lavoro trovate: N annunci, M aziende uniche"`

### Step 3 — Analisi sito aziendale
Per ogni azienda candidata, analizza il sito web per rilevare segnali di automazione potenziale:

#### Segnali positivi (alta opportunità AI):
| Segnale | Punti | Indicatore |
|---------|-------|-----------|
| Pagina "Lavora con noi" con ruoli manuali | +20 | Processi non automatizzati |
| Form di contatto generico (no booking online) | +15 | Gestione appuntamenti manuale |
| Nessun chatbot o widget di supporto | +10 | Customer service manuale |
| Menzione di "team dedicato" o "staff" per processi operativi | +10 | Forza lavoro impiegata in task automatizzabili |
| Più di 2 indirizzi email diversi sul sito | +10 | Routing comunicazioni manuale |
| Nessun portale clienti o area riservata | +10 | Gestione clienti manuale |
| Pagina prezzi assente (preventivi su richiesta) | +10 | Preventivazione manuale |
| Testimonial che citano "rapidità" o "comunicazione" come punti di forza | +5 | Processo comunicativo critico |

#### Segnali negativi (bassa opportunità o azienda non adatta):
| Segnale | Punti |
|---------|-------|
| Già usa chatbot visibile sul sito | −20 |
| Ha portale clienti o app dedicata | −15 |
| Meno di 5 dipendenti (troppo piccola) | −30 |
| Già pubblicizza servizi AI o automazione | −25 |

**Score iniziale: 0.** Si sommano i punti positivi e si sottraggono i negativi.

### Step 4 — Stima dimensione aziendale
1. Cerca su LinkedIn company page: campo "Dimensione aziendale"
2. Se non disponibile: stima da sito web (numero email diverse, pagine team, offerte lavoro)
3. Se < 10 dipendenti stimati → scarta (troppo piccola per Servizio 2)
4. Classi dimensione: `"10-20"`, `"20-50"`, `"50-200"`, `"200+"`

### Step 5 — Estrai contatti decisionali
Il decisore per il Servizio 2 non è il titolare operativo, ma il **responsabile delle operazioni o il CEO/COO**:
1. Cerca su LinkedIn: `[nome azienda] CEO` o `[nome azienda] Operations Manager` o `[nome azienda] Direttore Operativo`
2. Sul sito aziendale: cerca pagina "Team", "Chi siamo", "Management"
3. Se trovato il nome del decisore: salva in `REFERENTE`
4. Cerca email tramite Hunter.io con dominio aziendale + nome trovato
5. Log: `"Referente trovato per [azienda]: [nome] — [email]"`

### Step 6 — Identifica Processo Target
Sulla base dei segnali trovati, identifica il processo principale più automatizzabile:

| Processo | Trigger |
|----------|---------|
| Gestione email e comunicazioni clienti | Nessun chatbot + servizio customer-facing |
| Data entry e inserimento ordini | Offerta lavoro "data entry" trovata |
| Generazione report e analytics | Settore con molti dati (logistica, retail, finance) |
| Qualifica e follow-up lead | Settore con ciclo vendita lungo (immobiliare, B2B) |
| Gestione appuntamenti e calendario | Form contatto generico + nessun booking online |
| Elaborazione documenti e contratti | Settore legale, contabile, assicurativo |
| Customer onboarding | Servizi con processo di attivazione complesso |

Salva il processo identificato in `PROCESSO_TARGET`.

### Step 7 — Deduplicazione
1. Confronta `SITO_WEB` e `NOME_AZIENDA` con quelli già presenti nel foglio
2. Se già presente → salta, log: `"[nome_azienda] già in database, skip"`
3. Se nuovo → procedi all'inserimento

### Step 8 — Inserimento in Google Sheets
1. Prepara riga con tutti i campi
2. Soglia minima per inserimento: **SCORE_AI_POTENZIALE >= 25**
3. Appendi al tab `Lead_AIProspect`
4. Log: `"Lead [ID_LEAD] inserito: [NOME_AZIENDA] — Score AI: [score] — Processo: [PROCESSO_TARGET]"`
5. Fine run: `"Run completato: N candidati trovati, M inseriti (score >= 25), K scartati"`

---

## GESTIONE ERRORI

| Errore | Causa probabile | Azione |
|--------|----------------|--------|
| `Google: nessun risultato` | Query troppo specifica | Allarga query, rimuovi filtri città |
| `Sito aziendale irraggiungibile` | Down o bloccato | Score AI = 0 per assenza sito, segnala in NOTE |
| `LinkedIn: rate limit` | Troppe richieste | Pausa 60s, riprova, poi passa ad altre fonti |
| `Hunter.io: quota esaurita` | Piano scaduto | Salta email search, salva solo nome referente |
| `Dimensione < 10 dipendenti` | Azienda troppo piccola | Scarta, log: "Esclusa [azienda]: troppo piccola" |
| `Google Sheets: 403 Forbidden` | Service account senza permessi | Salva su CSV locale come backup |

---

## CASI LIMITE

- **Azienda già cliente o competitor conosciuto**: salta, aggiungi a lista esclusioni
- **Azienda con sede in più città**: usa sempre la sede principale come `CITTÀ`
- **Multinazionale o grande corporation (500+ dipendenti)**: scarta — fuori target (decision making troppo lento, budget procurement complesso)
- **Startup < 2 anni**: segnala in NOTE "startup giovane", potenzialmente interessante ma meno budget
- **Azienda senza sito web**: salta — non è possibile analizzare i processi senza presenza online

---

## TEMPLATE EMAIL (usato da WF-D)
Vedi `rules/04_drafta_email.md` → Template C: Prospect AI Implementation

---

## LOG

File: `logs/YYYY-MM-DD_WF-F_[settore]_[città].log`

```
[2025-01-15 09:00:00] START — Ricerca AI prospect: logistica in Milano
[2025-01-15 09:00:05] Google search: 28 aziende candidate trovate
[2025-01-15 09:00:05] Job search: 14 offerte di lavoro trovate (8 aziende con ruoli manuali)
[2025-01-15 09:02:30] Analisi siti: 28 siti analizzati
[2025-01-15 09:02:30] Scoring: 19 sopra soglia 25, 9 esclusi
[2025-01-15 09:03:00] Referenti trovati: 11 su 19
[2025-01-15 09:03:05] Deduplicazione: 3 già presenti, 16 nuovi
[2025-01-15 09:03:10] Inseriti 16 lead nel foglio Lead_AIProspect
[2025-01-15 09:03:10] END — Durata: 190s
```
