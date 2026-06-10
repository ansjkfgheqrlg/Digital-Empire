# 04_drafta_email
            
> Path: [[Map - Agenti|Agenti > Agency > outreach > rules]]

## Content

# REGOLA 04 — Drafta Email di Outreach

## OBIETTIVO
Generare bozze di email di outreach personalizzate e persuasive per ogni lead qualificato, usando Claude AI per adattare il messaggio al contesto specifico del business. Le bozze vengono salvate per revisione umana — mai inviate automaticamente.

## TRIGGER
- Manuale: operatore seleziona lead da `PRONTO_OUTREACH = "Sì"` e lancia lo script
- Può processare 1 lead specifico o tutti i lead pronti in batch

## INPUT

| Campo | Obbligatorio | Tipo | Descrizione |
|-------|-------------|------|-------------|
| `id_lead` | No* | stringa | ID specifico del lead (`NS-MI-xxx` o `AF-RM-xxx`) |
| `batch` | No* | bool | Se True, processa tutti i lead `PRONTO_OUTREACH=Sì` |
| `max_batch` | No (default: 20) | intero | Massimo email da generare per run |

*Almeno uno tra `id_lead` e `batch=True` deve essere fornito.

## OUTPUT
- File `.txt` per ogni email in `bozze_email/YYYY-MM-DD/[ID_LEAD]_bozza.txt`
- Colonne aggiornate in Google Sheets: `BOZZA_GENERATA=Sì`, `DATA_BOZZA`
- Log in `logs/YYYY-MM-DD_WF-D_email_drafts.log`

---

## STEP-BY-STEP

### Step 1 — Carica lead da Google Sheets
1. Se `id_lead` specificato: carica solo quel lead
2. Se `batch=True`: carica tutti con `PRONTO_OUTREACH="Sì"` e `BOZZA_GENERATA` vuota
3. Limita a `max_batch` lead
4. Log: `"N lead da processare per email"`

### Step 2 — Seleziona Template
In base al tipo di lead:
- ID lead che inizia con `NS-` → **Template A: Business Senza Sito**
- ID lead che inizia con `AF-` → **Template B: Business con Ads e Funnel Scarso**
- ID lead che inizia con `AI-` → **Template C: Prospect AI Implementation**

### Step 3 — Genera Email con Claude AI
Per ogni lead:

1. Prepara il prompt per Claude con:
   - Tipo di template (A o B)
   - Dati del lead: nome, settore, città, score funnel (se disponibile), note
   - Istruzioni di tono e stile (vedi sezione TONO)
2. Chiama Claude API (`claude-sonnet-4-6`)
3. Ricevi testo email completo
4. Valida che contenga: oggetto, corpo email, firma
5. Salva in `bozze_email/YYYY-MM-DD/[ID_LEAD]_bozza.txt`
6. Log: `"Bozza generata per [ID_LEAD]: [NOME_BUSINESS]"`

### Step 4 — Aggiorna Google Sheets
1. Aggiorna riga del lead: `BOZZA_GENERATA=Sì`, `DATA_BOZZA=[timestamp]`
2. Non cambiare `STATO_OUTREACH` — rimane `"nuovo"` fino all'invio effettivo

---

## TONO E STILE DELL'EMAIL

Le email devono essere:
- **Brevi**: max 150-200 parole nel corpo
- **Specifiche**: menzionare qualcosa di specifico sul business del destinatario
- **Senza pressione**: nessuna urgenza artificiale, nessun "ultima possibilità"
- **Con curiosità**: finire con una domanda o proposta di call, non con una vendita
- **Professionali ma umane**: non sembrano automatizzate
- **In italiano**: a meno che il business non sia chiaramente anglofono

**Cosa NON scrivere:**
- "Ho notato che il vostro sito potrebbe essere migliorato" (troppo critico)
- "Posso raddoppiare i vostri clienti" (promessa irrealistica)
- Statistiche generiche non contestualizzate
- Più di 1 CTA

---

## TEMPLATE A: Business Senza Sito Web

### Struttura
```
OGGETTO: [Oggetto_Personalizzato]

Ciao [NOME_REFERENTE o ""],

Ho cercato [NOME_BUSINESS] su Google e ho visto che avete [N_RECENSIONI] recensioni molto positive — complimenti per il lavoro che fate.

Ho notato però che non avete un sito web. Per un [CATEGORIA] come voi, questo significa perdere clienti ogni giorno che cercano online ma non riescono a trovarvi.

Mi occupo di creare siti web e sistemi di acquisizione clienti per [SETTORE] locali — non siti vetrina generici, ma pagine progettate per trasformare le ricerche Google in prenotazioni e telefonate.

Avrebbe senso fare una chiacchierata di 15 minuti per capire se posso esservi utile?

[FIRMA]
```

### Variabili dinamiche
| Variabile | Fonte | Fallback |
|-----------|-------|---------|
| `[NOME_REFERENTE]` | Sheets: REFERENTE | "" (non usare "Titolare") |
| `[NOME_BUSINESS]` | Sheets: NOME_BUSINESS | obbligatorio |
| `[N_RECENSIONI]` | Sheets: N_RECENSIONI | "molte" |
| `[CATEGORIA]` | Sheets: CATEGORIA | "attività" |
| `[SETTORE]` | Sheets: CATEGORIA (tradotto) | "aziende come la vostra" |
| `[FIRMA]` | .env: MITTENTE_FIRMA | "Un saluto," |

### Esempi di oggetto
- "Un'opportunità che [NOME_BUSINESS] sta perdendo ogni giorno"
- "I vostri [N_RECENSIONI] clienti soddisfatti non riescono a trovarvi online"
- "Ho cercato [CATEGORIA] a [CITTÀ] — ecco cosa ho trovato"

---

## TEMPLATE B: Business con Ads e Funnel Scarso

### Struttura
```
OGGETTO: [Oggetto_Personalizzato]

Ciao [NOME_REFERENTE o ""],

Ho visto la vostra pubblicità su Facebook per [NOME_BUSINESS] — state investendo in advertising, ottimo.

Ho però analizzato la pagina su cui portate il traffico e ho identificato [N_PROBLEMI] aree che probabilmente vi stanno costando conversioni: [PROBLEMA_PRINCIPALE].

[Una frase che spiega cosa potrebbe cambiare con un funnel ottimizzato, specifica al loro settore]

Lavoro con [SETTORE] che fanno advertising e voglio aiutarli a trasformare lo stesso budget pubblicitario in più clienti, non in più clic.

Ha senso fare una call veloce per mostrarvi cosa ho trovato?

[FIRMA]
```

### Variabili dinamiche
| Variabile | Fonte | Fallback |
|-----------|-------|---------|
| `[NOME_REFERENTE]` | Sheets: REFERENTE | "" |
| `[NOME_BUSINESS]` | Sheets: NOME_PAGINA | obbligatorio |
| `[N_PROBLEMI]` | Derivato da DETTAGLIO_SCORE | "alcune" |
| `[PROBLEMA_PRINCIPALE]` | Sheets: DETTAGLIO_SCORE | generato da Claude |
| `[SETTORE]` | Sheets: SETTORE | "attività" |
| `[FIRMA]` | .env: MITTENTE_FIRMA | "Un saluto," |

### Esempi di oggetto
- "Ho analizzato la landing page di [NOME_BUSINESS]"
- "Cosa succede dopo che qualcuno clicca sul vostro ads?"
- "Il vostro budget ads merita una pagina migliore"

---

---

## TEMPLATE C: Prospect AI Implementation

### Contesto d'uso
Questo template è per aziende strutturate (10+ dipendenti) con processi manuali identificati. Il tono è **diverso dai Template A e B**: non si parla di "sito web" o "ads", ma di efficienza operativa, risparmio di tempo e scalabilità. Il destinatario ideale è un CEO, COO o responsabile operativo.

La chiave: **non vendere tecnologia, vendere il risultato**. Il prospect non vuole un "agente AI", vuole non dover assumere una quinta persona per gestire il back office, o fare report in automatico invece di 3 ore ogni venerdì.

### Struttura
```
OGGETTO: [Oggetto_Personalizzato]

Ciao [NOME_REFERENTE],

Ho visto che [NOME_AZIENDA] sta [OSSERVAZIONE_SPECIFICA — es. "cercando un addetto al back office" / "gestendo manualmente le prenotazioni" / "inviando preventivi su richiesta"].

Lavoro con aziende nel settore [SETTORE] per automatizzare esattamente quel tipo di processo con agenti AI su misura — non software standard, ma sistemi costruiti attorno al vostro flusso di lavoro specifico.

Nel caso di [PROCESSO_TARGET], il risultato tipico è [BENEFICIO_CONCRETO — es. "eliminare 15-20 ore di lavoro manuale a settimana" / "rispondere ai clienti in meno di 2 minuti, 24/7" / "generare report automaticamente ogni lunedì mattina"].

Vale la pena fare una chiamata di 20 minuti per capire se ha senso per voi?

[FIRMA]
```

### Variabili dinamiche
| Variabile | Fonte | Fallback |
|-----------|-------|---------|
| `[NOME_REFERENTE]` | Sheets: REFERENTE | "buongiorno" |
| `[NOME_AZIENDA]` | Sheets: NOME_AZIENDA | obbligatorio |
| `[OSSERVAZIONE_SPECIFICA]` | Sheets: OFFERTE_LAVORO_TROVATE + SEGNALI_AUTOMAZIONE | generato da Claude |
| `[SETTORE]` | Sheets: SETTORE | "questo settore" |
| `[PROCESSO_TARGET]` | Sheets: PROCESSO_TARGET | generato da Claude |
| `[BENEFICIO_CONCRETO]` | Generato da Claude in base al processo | obbligatorio |
| `[FIRMA]` | .env: MITTENTE_FIRMA | "Un saluto," |

### Istruzioni specifiche per Claude (Template C)
- **Mai usare** la parola "AI" o "Intelligenza Artificiale" nel subject — suona freddo e tecnico
- **Usare invece**: "automatizzare", "sistema su misura", "processo automatico"
- **L'osservazione specifica deve essere reale**: basarsi sempre su OFFERTE_LAVORO_TROVATE o SEGNALI_AUTOMAZIONE dal foglio — se questi campi sono vuoti, usa PROCESSO_TARGET per costruire un'osservazione plausibile
- **Il beneficio concreto deve essere specifico al processo**: non "risparmiare tempo" in astratto, ma "eliminare X ore a settimana di [task specifico]"
- **Nessuna lista di servizi**: questa email ha un focus chirurgico su UN processo specifico

### Esempi di oggetto (Template C)
- "Come [NOME_AZIENDA] potrebbe risparmiare 15h/settimana su [PROCESSO]"
- "Ho visto l'annuncio per [RUOLO_CERCATO] — c'è un'alternativa"
- "Una domanda su come gestite [PROCESSO_TARGET] in [NOME_AZIENDA]"
- "[NOME_AZIENDA]: il [PROCESSO] può girare da solo?"

---

## PROMPT CLAUDE (schema)

```
Sei un copywriter esperto che scrive email di outreach B2B per conto di Digital Empire Team,
uno studio specializzato in CRO/Funnel Strategy e implementazione di agenti AI su misura.

Devi scrivere UNA email per questo lead specifico:
- Nome business/azienda: [NOME_BUSINESS]
- Tipo: [no_sito / funnel_scarso / ai_prospect]
- Settore: [SETTORE]
- Città: [CITTÀ]
- Dati rilevanti: [score funnel / rating Google / n_recensioni / segnali_automazione / processo_target / offerte_lavoro_trovate]

Usa questo template come base, ma personalizzalo in modo che non sembri un'email automatica:
[TEMPLATE A, B o C — in base al tipo di lead]

Requisiti generali:
- Max 150 parole nel corpo
- Scrivi in italiano
- Non promettere risultati specifici
- Finisci con UNA sola domanda o proposta di call
- Genera anche 3 varianti dell'oggetto

Requisiti aggiuntivi per Template C (ai_prospect):
- Non usare mai le parole "AI" o "Intelligenza Artificiale" nell'oggetto
- L'osservazione iniziale deve essere specifica e basata sui dati forniti (offerte lavoro o segnali trovati)
- Il beneficio deve essere concreto e quantificato (ore risparmiate, velocità di risposta, ecc.)

Formato output:
OGGETTO 1: ...
OGGETTO 2: ...
OGGETTO 3: ...
---
CORPO EMAIL:
[testo]
```

---

## GESTIONE ERRORI

| Errore | Causa | Azione |
|--------|-------|--------|
| `Claude API: rate limit` | Troppe richieste | Pausa 30s, riprova x3 |
| `Claude: risposta vuota o malformata` | Errore generazione | Log warning, usa template grezzo senza personalizzazione |
| `Lead senza dati sufficienti` | Dati mancanti | Skip, log: "dati insufficienti per personalizzazione" |
| `Cartella bozze non creabile` | Permessi disco | Usa directory temporanea, log warning |

---

## CASI LIMITE

- **Lead con solo numero di telefono (no email)**: genera comunque la bozza email, l'operatore deciderà se usarla per un cold call invece
- **Business con nome strano o difficile da contestualizzare**: Claude usa il settore come riferimento principale
- **Bozza già esistente** per questo lead: non sovrascrivere, aggiungi suffisso `_v2`, `_v3`

---

## FORMATO FILE DI BOZZA

```
# BOZZA EMAIL — [ID_LEAD]
# Generata: [timestamp]
# Business: [NOME_BUSINESS]
# Città: [CITTÀ]
# Tipo lead: [no_sito / funnel_scarso / ai_prospect]
# Score: [SCORE]
# Email destinatario: [EMAIL]
# Referente: [REFERENTE o "non trovato"]
# ============================================

OGGETTO CONSIGLIATO: [oggetto 1 scelto da Claude]
OGGETTI ALTERNATIVI:
  - [oggetto 2]
  - [oggetto 3]

CORPO:
[testo email]

# ============================================
# ISTRUZIONI PER L'OPERATORE:
# 1. Rivedi il testo e personalizza dove necessario
# 2. Se approvata, usa implementation/send_emails.py --lead-id [ID_LEAD]
# 3. Aggiorna lo stato in Google Sheets
```

---

## LOG

File: `logs/YYYY-MM-DD_WF-D_email_drafts.log`

```
[2025-01-15 16:00:00] START — Generazione email per 15 lead
[2025-01-15 16:00:05] NS-MI-xxx → bozza generata (Template A)
[2025-01-15 16:00:10] AF-RM-xxx → bozza generata (Template B)
...
[2025-01-15 16:02:00] END — 14 bozze generate, 1 skip (dati insufficienti)
```

## Collegamenti Correlati
- [[Map - Agenti|Agenti Area]]
- [[Map - App|App Area]]
- [[Map - General|General Area]]
- [[Map - Outreach|Outreach Area]]
