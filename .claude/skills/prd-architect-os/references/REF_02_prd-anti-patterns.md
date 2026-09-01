# REF_02 — PRD Anti-Patterns
## I 15 Pattern Sbagliati che Distruggono i PRD

Usa questo file per **identificare e correggere** PRD mal strutturati.
Ogni anti-pattern include: descrizione, come si manifesta, esempio concreto, perché è pericoloso, e la correzione.

---

## ❌ ANTI-PATTERN #1 — "The Feature Wishlist"

### Descrizione
Il PRD è una lista di feature senza problema, senza utente, senza metriche. Sembra un backlog Jira, non un PRD.

### Come Si Manifesta
- Sezione "Requisiti" con 40+ feature elencate
- Nessun problem statement
- Nessuna persona utente
- Metriche assenti o vaghe ("l'app deve funzionare bene")
- Titolo del PRD: "Requisiti Feature Sprint 12"

### Esempio
```
❌ PRD che inizia con:
"L'app deve avere:
- Login con email
- Login con Google
- Dashboard con statistiche
- Export CSV
- Notifiche push
- Dark mode
- Multi-lingua
- API pubblica
..."
(continua per 4 pagine)
```

### Perché È Pericoloso
- Engineering costruisce feature nell'ordine sbagliato
- Nessuno sa cosa è P0 vs P3
- Lo scope esplode ad ogni meeting
- Il prodotto viene lanciato ma non risolve nessun problema reale
- Il team non sa mai quando è "finito"

### Correzione
Parti sempre dal problema: chi soffre di cosa, con quale evidenza.
Poi deriva le feature come soluzione a quel problema specifico.

```
✅ Problem Statement prima:
"Il 60% degli utenti abandona il checkout (dato Hotjar).
Il problema principale: 8 step richiesti vs media settore 3 step.
Evidenza: 45 heatmap sessions, 12 user interviews."

→ Da questo derivano le feature:
- US-001: Checkout 1-step per utenti registrati (P0)
- US-002: Salvataggio carta per riacquisto (P1)
- US-003: Guest checkout senza registrazione (P0)
```

---

## ❌ ANTI-PATTERN #2 — "The Vague Metric Trap"

### Descrizione
Le metriche esistono ma sono misurabili quanto "il meteo sarà bello domani". Sembrano obiettivi ma non danno nessuna indicazione operativa.

### Esempi di Metriche Vaghe
```
❌ "Aumentare la retention"
❌ "Migliorare l'engagement"
❌ "Ridurre il churn"
❌ "Crescere organicamente"
❌ "Gli utenti devono essere soddisfatti"
❌ "Aumentare le conversioni"
❌ "Avere più utenti attivi"
```

### Test di Validità della Metrica
Per ogni metrica, rispondi: **"Tra 60 giorni, come sapremo ESATTAMENTE se l'abbiamo raggiunta?"**

Se la risposta richiede interpretazione → la metrica è vaga.

### Correzione
```
✅ Metrica corretta:
"D7 retention ≥ 35% misurata con PostHog
sulla coorte di utenti che si registrano a Febbraio 2025.
Baseline attuale: 18%.
Measurement window: dal giorno del lancio ai 30 giorni successivi.
Review settimanale ogni lunedì mattina."

✅ Metrica corretta:
"Conversion trial→paid ≥ 8% entro 90 giorni dal lancio.
Misurata su Stripe: (subscription_created / signups) nelle ultime 4 settimane.
Baseline: non misurato (prodotto nuovo).
Se raggiungiamo 5% → considera successo parziale."
```

### Domande di Sfida per Ogni Metrica
Quando un utente ti dà una metrica vaga, chiedi:
1. "Di quanto esattamente?" → trasforma in numero
2. "Da quale baseline?" → anchora alla situazione attuale
3. "In quale timeframe?" → deadline chiara
4. "Come la misurerete?" → strumento specifico
5. "Chi è il proprietario della metrica?" → accountability

---

## ❌ ANTI-PATTERN #3 — "The Orphan Edge Case"

### Descrizione
Il PRD descrive il happy path perfettamente ma ignora completamente gli stati di errore, gli stati vuoti, i loading state.

### Impatto sul Vibecoding
Quando passi il PRD a Cursor o Claude, l'AI costruisce SOLO il happy path.
Gli error state vengono gestiti con `console.log(error)` o modali generici.
Risultato: app che sembra funzionare ma si rompe nel primo scenario reale.

### Esempio
```
❌ Feature spec che descrive:
"L'utente clicca 'Invia', il sistema manda l'email, 
l'utente vede il messaggio di conferma."

NON menziona:
- Cosa succede se il server è offline?
- Cosa vede l'utente mentre l'email viene inviata?
- Cosa succede se l'email del destinatario non è valida?
- Cosa vede l'utente se l'invio fallisce?
- Cosa succede se l'utente clicca "Invia" due volte?
```

### Checklist Anti-Orphan
Per ogni feature interattiva, verifica SEMPRE:
```
□ Cosa vede l'utente se la lista è vuota? (Empty State)
□ Cosa vede l'utente mentre la pagina/operazione carica? (Loading State)
□ Cosa vede l'utente se l'API fallisce? (Error State)
□ Il messaggio di errore è specifico o generico?
□ Cosa vede l'utente se non ha i permessi? (Permission State)
□ Cosa succede se l'utente preme "back" durante un'operazione in corso?
□ Cosa succede se la sessione scade mentre compila un form lungo?
□ Cosa succede se l'utente clicca il bottone due volte?
```

### Standard Error State (NON derogare)
```
❌ "Mostra un errore"
❌ "Gestisci l'errore gracefully"

✅ Standard corretto:
"Se la chiamata API fallisce dopo 3 retry:
Mostra toast: 'Impossibile salvare. I tuoi dati sono al sicuro. Riprova tra qualche minuto.'
+ Bottone [Riprova]
+ Link 'Contatta supporto' (mailto: support@app.com)
L'utente non perde il lavoro (dati in local storage)"
```

---

## ❌ ANTI-PATTERN #4 — "The Eternal Draft"

### Descrizione
Il PRD rimane in stato DRAFT per settimane mentre lo sviluppo è già iniziato. Nessuno lo aggiorna, nessuno lo legge. Diventa un documento fantasma.

### Sintomi
- Ultima modifica: 3+ settimane fa
- Status: DRAFT (mai cambiato)
- Change log: vuoto o con 1 riga
- Il codice ha feature non nel PRD
- Il PRD ha sezioni non ancora sviluppate
- Il team dice "non guardare il PRD, è vecchio"

### Costo del Fantasma
- Il team prende decisioni che contraddicono il PRD
- Il nuovo developer legge il PRD e implementa la versione sbagliata
- Nessuno ricorda perché è stata presa una certa decisione
- Il PRD non è più utile per onboarding

### Correzione
Il PRD segue il prodotto, non il contrario.

**Regola**: Se prendi una decisione che cambia qualcosa nel PRD → aggiorni il PRD entro 24h.

**Sistema di trigger obbligatori**:
```
Aggiorna il PRD SEMPRE quando:
□ Engineering scopre un vincolo tecnico non previsto
□ Un'assunzione del PRD si rivela falsa
□ Gli stakeholder cambiano una priorità
□ Una user story viene modificata durante lo sprint
□ Il tech stack cambia (anche parzialmente)
□ Una feature viene spostata nel backlog
□ Una deadline cambia
```

**Header versionamento obbligatorio**:
```markdown
---
Titolo: [Nome Feature]
Versione: 1.3
Status: DRAFT 🔴 | IN REVIEW 🟡 | APPROVED ✅ | DEPRECATED ⚫
Ultima modifica: GG/MM/AAAA
Prossima review: GG/MM/AAAA
---
```

---

## ❌ ANTI-PATTERN #5 — "The Everything Is P0"

### Descrizione
Tutte le user stories sono marcate P0. Tutto è critico. Tutto è urgente. Engineering non sa da dove iniziare.

### Impatto
- Sprint overloaded sistematicamente
- Feature critiche bloccate da feature nice-to-have
- Team frustrato e demotivato
- Nessun senso di progresso
- "Ci sentiamo in riunione per decidere le priorità" → riunione ogni 2 giorni

### Framework di Prioritizzazione Corretto

```
P0 — MUST HAVE (blocca il lancio)
→ Senza questo, il prodotto non può essere lanciato in nessun senso utile
→ Max il 20-30% delle feature
→ Domanda test: "Se questa feature manca, il lancio è un fallimento?"

P1 — SHOULD HAVE (fortemente consigliato per v1)
→ Importante ma il lancio può avvenire tecnicamente senza
→ 30-40% delle feature
→ Domanda test: "Se questa feature manca, gli utenti si lamentano?"

P2 — NICE TO HAVE (backlog)
→ Migliora l'esperienza ma non è essenziale
→ 30-50% delle feature
→ Domanda test: "Se questa feature manca, nessuno lo nota subito?"
```

**REGOLA**: Se tutto è P0, niente è P0.

**Esercizio di Calibrazione**: Prendi tutte le feature P0 e chiedi: "Se dovessimo togliere il 50% di queste, quale 50% togliamo?" — quelle che puoi togliere non erano davvero P0.

---

## ❌ ANTI-PATTERN #6 — "The Technical PRD"

### Descrizione
Il PRD è scritto per developer, non per il prodotto. È pieno di terminologia tecnica, schemi DB dettagliati, specifiche di implementazione. Il PM ha scritto il TDD (Technical Design Document) mascherato da PRD.

### Perché È Sbagliato
Il PRD dice **COSA e PERCHÉ**. Il TDD dice **COME**.

Se il PRD specifica il tipo di join SQL, l'indice del DB, l'algoritmo di hashing:
- Stai micro-managing l'engineering
- Stai rimuovendo autonomia tecnica al team
- Il PRD diventerà obsoleto al primo refactor

### Linea di Demarcazione

```
✅ NEL PRD (COSA e PERCHÉ):
"I dati degli utenti devono essere isolati tra tenant"
"Le query devono rispondere in <300ms al P95"
"Il sistema deve scalare fino a 10.000 utenti senza degradazione"
"I dati PII non devono mai apparire nei log applicativi"

❌ NEL TDD (non nel PRD):
"Usa Row Level Security in PostgreSQL"
"Aggiungi index su user_id e created_at"
"Usa Redis per caching delle sessioni"
"Usa bcrypt con 12 salt rounds per le password"
```

### Quando il Tech Stack è Accettabile nel PRD
Solo per il PRD Tipo D (Vibecoding): il tech stack è VINCOLANTE e appartiene nel documento perché l'AI che sviluppa deve rispettarlo. In tutti gli altri tipi, il tech stack va nel TDD separato.

---

## ❌ ANTI-PATTERN #7 — "The Missing Persona"

### Descrizione
Il target utente è definito in modo così vago che chiunque potrebbe essere il cliente. Nessuna decisione di design può essere presa con un target così generico.

### Esempi di Target Vaghi
```
❌ "Utenti che vogliono essere più produttivi"
❌ "Professionisti del settore"
❌ "PMI italiane"
❌ "Chiunque abbia bisogno di gestire task"
❌ "Giovani tra i 18 e i 45 anni"
❌ "Aziende di medie dimensioni"
```

### Perché È Pericoloso
Quando il target è "tutti":
- L'onboarding cerca di accontentare tutti → confonde tutti
- Le feature vengono aggiunte per segmenti diversi → product bloat
- Il copy è generico → non converte
- Il marketing non sa chi targettare → CAC esplode
- Il team non sa a chi dare ragione nei trade-off di UX

### Correzione
Una persona primaria, specifica, con un job-to-be-done preciso.

```
✅ Persona corretta:
"Marco, 34 anni, web designer freelance
→ Lavora da casa/coworking, 3-8 clienti attivi in contemporanea
→ Usa Figma, Notion, Slack — non sa programmare
→ Budget tool: €15-25/mese — già paga per 5+ SaaS
→ Problema: perde 1 ora a preventivo in Word/Excel
→ JTBD: 'Quando un cliente chiede un preventivo, voglio mandarlo in 10 min'"

Se hai più segmenti:
→ Scegli il primario (chi paga di più o chi è più urgente)
→ Definisci i secondari come note a margine
→ Costruisci per il primario — non per tutti
```

---

## ❌ ANTI-PATTERN #8 — "The Scope Creep Enabler"

### Descrizione
La sezione Non-Goals è assente o ha voci vaghe. Ogni stakeholder interpreta lo scope diversamente. Ad ogni meeting vengono aggiunte "piccole cose".

### Sintomi
- "Ma questo non ci vuole un'ora?" viene detto ogni sprint
- La feature "semplice" di 1 settimana dura 3 mesi
- Il check-in con il cliente rivela sempre nuovi requisiti "ovvi"
- Le PR Review aggiungono feature invece di rivedere il codice

### Correzione

La sezione Out-of-Scope deve avere:
1. Feature specifica (NON categoria generica)
2. Motivazione esplicita (perché no in v1)
3. Timeline di rivalutazione

```
❌ SBAGLIATO:
"Out of scope: funzionalità avanzate, integrazioni, feature enterprise"

✅ CORRETTO:
| Feature | Motivazione | Rivalutare in |
|---------|-------------|---------------|
| Firma digitale preventivi | Complessità legale e costo integrazione (~€30/mese) | v3 se richiesto da >30% utenti |
| App mobile | Web-first: validare prima su desktop | Post-PMF (>500 paganti) |
| Export QuickBooks | Solo 8% target usa QuickBooks | v2 — Q4 2025 |
| API pubblica | Richiede auth separata e documentazione | v3 |
```

**Regola di comunicazione**: Quando uno stakeholder aggiunge una feature durante lo sprint, hai 3 opzioni:
1. La feature è veramente critica → modifica il PRD formalmente + aggiorna il change log
2. La feature è importante ma non urgente → aggiungila all'Out-of-Scope con timeline
3. La feature è nice-to-have → backlog con spiegazione del perché

Non esiste l'opzione 4 (aggiungerla silenziosamente).

---

## ❌ ANTI-PATTERN #9 — "The PRD Without Evidence"

### Descrizione
Il problem statement esiste ma è basato su assunzioni, sensazioni o "logica di mercato". Nessuna evidenza che il problema sia reale.

### Livelli di Evidenza (in ordine di forza)
```
🥇 User interviews (5+ interviste strutturate con domande aperte)
🥈 Dati quantitativi (analytics, survey, report di settore con fonte)
🥉 Osservazione diretta (uso personale del prodotto, shadowing utenti)
🏅 Community signals (Reddit, forum, commenti competitor con link)
🎖️ Competitive analysis (gap nelle soluzioni esistenti con confronto)
```

### Cosa NON È Evidenza
```
❌ "Tutti hanno questo problema"
❌ "Io stesso ho questo problema" (da solo non basta)
❌ "Il mercato è grande quindi funzionerà"
❌ "I competitor lo fanno quindi c'è domanda"
❌ "Logicamente ha senso che..."
❌ "I nostri investitori credono che..."
```

### Minimum Viable Evidence
- Almeno 2 fonti di evidenza diverse
- Almeno 1 dato quantitativo (anche stimato con fonte)
- Almeno 1 citazione diretta da utente reale (non parafrasata)

```
✅ Esempio di evidence solida:
"Dati qualitativi: 11/15 intervistati usano Word/Excel per preventivi.
Tutti lo considerano perdita di tempo.
Dati quantitativi: tempo medio preventivo = 67 minuti (n=50, survey SurveyMonkey).
Community: Reddit r/freelance_ita — 23 thread con 'preventivo' negli ultimi 6 mesi,
78% lamenta complessità (contato manualmente).
Gap competitor: FattureInCloud e Fattura24 sono per fatturazione, non preventivi pre-vendita."
```

---

## ❌ ANTI-PATTERN #10 — "The Delegated Design PRD"

### Descrizione
La sezione UX/Design del PRD contiene solo: "Il designer creerà i wireframe" / "Da definire con il team di design" / "Vedi Figma".

### Perché È Sbagliato
Il PRD deve contenere il PENSIERO del PM sull'esperienza, anche se non è un designer.

Il PM deve specificare:
- Il flow dell'utente (testuale, non wireframe)
- Gli stati che ogni schermata deve gestire
- Le decisioni di UX critiche (modal vs pagina dedicata)
- I vincoli di UX ("l'onboarding non deve superare 3 step")

Il designer poi decide il COME visivo. Il PM decide il COSA e il PERCHÉ dell'esperienza.

### Correzione

```
❌ "Il designer creerà i wireframe per il checkout."

✅ Flow testuale del PM:
"FLOW: Checkout
1. Utente clicca 'Acquista' sulla sales page
2. Vede: riepilogo ordine (prodotto, prezzo, totale)
   + form pagamento (carta o PayPal)
   + CTA 'Paga €97'
3. Submit → processing indicator (bottone con spinner)
4. Success → redirect a /thank-you con:
   - Conferma acquisto + numero ordine
   - Link per accedere al corso
   - Email di conferma entro 5 min

Decision critica: NON usare pagina Stripe hosted — manteniamo l'utente
sul nostro dominio per evitare abbandono. Checkout embedded.

Vincolo UX: max 2 campi nella pagina + CTA — meno click possibile."
```

---

## ❌ ANTI-PATTERN #11 — "The Impossible Timeline"

### Descrizione
Il timeline nel PRD è costruito senza coinvolgere engineering. È aspirazionale, non realistico. Viene ignorato da tutti dopo la prima settimana.

### Segnali di Timeline Impossibile
- Nessun buffer per bug e refactor (almeno 20% del tempo)
- Feature L stimate come S perché "sembra semplice"
- Dipendenze esterne non considerate nei tempi
- "Questa cosa è semplice" → di solito è il contrario
- 1 developer deve fare il lavoro di 3

### Regole per Timeline Realistiche
```
REGOLA 1: Moltiplica sempre per 1.5-2x la stima iniziale
REGOLA 2: Aggiungi 20% buffer per QA e bug fixing
REGOLA 3: Le dipendenze esterne hanno sempre delay (aggiungi 1 settimana)
REGOLA 4: Coinvolgi engineering PRIMA di fissare le date
REGOLA 5: Il PRD non decide la sprint capacity — il team decide
```

### Shape Up Approach (il migliore)
Non stimare i task. Fissa l'appetite (il tempo disponibile) e chiedi:
> "Cosa possiamo costruire di valore in queste 3 settimane?"
→ NON "Quanto tempo ci vuole per costruire X?"

---

## ❌ ANTI-PATTERN #12 — "The AI-Unfriendly PRD"

### Descrizione
Il PRD viene passato a Cursor/Claude per il vibecoding ma è strutturato per essere letto da umani: testo narrativo lungo, nessuna distinzione tra fasi, tech stack non specificato.

### Risultato
L'AI genera qualcosa che sembra funzionare ma:
- Non rispetta nessun requisito specifico
- Inventa feature non richieste
- Usa il tech stack sbagliato
- Ignora gli edge cases
- Ogni correzione rompe 3 cose diverse

### Correzione: Le 6 Regole del PRD Vibecoding-Ready

```
REGOLA 1: MARKDOWN NEL REPOSITORY
→ /docs/PRD.md — Cursor lo legge come file di progetto
→ Mai PDF, mai Notion, mai Google Docs

REGOLA 2: TECH STACK ESPLICITO E VINCOLANTE
❌ "Usa un database scalabile"
✅ "PostgreSQL su Supabase. Row Level Security abilitato.
    Ogni tabella ha colonna tenant_id.
    Usa Prisma come ORM."

REGOLA 3: FASI NUMERATE (non feature list)
❌ Lista di 20 feature da costruire
✅ Fase 1 (giorni 1-3): Auth + schema DB
   Fase 2 (giorni 4-7): Core feature X
   → Passa all'AI una fase alla volta

REGOLA 4: USER FLOW COME TESTO
❌ Link a Figma wireframe
✅ "1. Utente visita /pricing
    2. Clicca 'Inizia gratis'
    3. Redirect a /signup
    4. Form: email + password + nome
    5. Submit → POST /api/auth/register
    6. Success → redirect /onboarding/step-1
    7. Error (email già usata) → 'Questa email è già registrata.'"

REGOLA 5: ACCEPTANCE CRITERIA TESTABILI
✅ PASSA SE: [condizione misurabile]
❌ FALLISCE SE: [condizione misurabile]

REGOLA 6: SEZIONE AI CONSTRAINTS ESPLICITA
"❌ Non aggiungere feature non in questo PRD
❌ Non cambiare il tech stack
✅ Se qualcosa è ambiguo, chiedi prima di implementare"
```

---

## ❌ ANTI-PATTERN #13 — "The Compliance Afterthought"

### Descrizione
GDPR, privacy, sicurezza vengono menzionati alla fine del PRD come "da gestire dopo il lancio".

### Costo dell'Afterthought
Aggiungere GDPR dopo il lancio significa:
- Riscrivere tutta la gestione dei dati utente
- Aggiungere consent management in ogni form
- Implementare right-to-be-forgotten su DB già popolato
- Audit log retroattivi (impossibili)
- Rischio sanzioni fino al 4% del fatturato globale (GDPR)

### Sezione Compliance Obbligatoria per SaaS EU

```markdown
## 🔒 COMPLIANCE & DATA PRIVACY

### GDPR (obbligatorio per qualsiasi SaaS EU)
- [ ] Consenso esplicito per: [lista dati raccolti]
- [ ] PII mai nei log applicativi (nome, email, IP vanno oscurati)
- [ ] Right-to-be-forgotten: procedura documentata (DELETE su richiesta)
- [ ] Data retention: [X giorni per tipo di dato] poi AUTO-DELETE
- [ ] Privacy Policy generata prima del lancio
- [ ] Cookie banner conforme (se analytics/tracking)

### Sicurezza Base
- [ ] Crittografia at-rest: AES-256 per dati sensibili
- [ ] Crittografia in-transit: TLS 1.2+ obbligatorio
- [ ] Password: bcrypt o argon2 (mai MD5/SHA1)
- [ ] JWT: refresh token rotation abilitata

### Per SaaS con dati medici (HIPAA) o card dati (PCI DSS)
→ Questi richiedono audit separato — non affrontare in questo PRD senza specialista
```

---

## ❌ ANTI-PATTERN #14 — "The Single Reviewer PRD"

### Descrizione
Il PRD viene scritto dal PM in isolamento e mai revisionato da engineering, design o sales prima di essere "approvato".

### Cosa Si Perde Senza Revisione

Engineering avrebbe detto:
- "Questa feature richiede 3 settimane, non 3 giorni"
- "Il sistema legacy non supporta questa integrazione"
- "Abbiamo già questo nel codice — prendiamo quello"

Design avrebbe detto:
- "Questo flow ha 8 step — gli utenti abbandoneranno al 4°"
- "Questo empty state non ha senso nel contesto"
- "Abbiamo già questo componente nel design system"

Sales/Customer Success avrebbe detto:
- "I clienti chiedono questa feature da 6 mesi"
- "Questa terminologia non è quella che usa il mercato"
- "Questa feature blocca 3 deal in pipeline"

### Processo Minimo di Review

```
1. PM scrive bozza v1.0
2. Review sincrona con Lead Engineering (30 min)
   → Fattibilità tecnica + stima effort realistico
3. Review sincrona con Design (20 min)
   → UX flow + vincoli design system + accessibilità
4. Review asincrona con Sales/CS (commenti su doc, 48h)
   → Validazione con il mercato reale
5. PM incorpora feedback → v1.1
6. Sign-off formale da tutti i reviewer → PRD marcato APPROVED
```

**Regola minima per PRD Vibecoding (solo founder)**:
Almeno 1 test manuale del flow su carta o su tool di wireframing.
Non procedere se il flow non è chiaro a una seconda persona esterna.

---

## ❌ ANTI-PATTERN #15 — "The Success Without Measurement"

### Descrizione
Il prodotto viene lanciato, gli utenti lo usano, ma nessuno sa se "ha funzionato" perché le metriche non erano definite nel PRD e il tracking non era stato implementato.

### Impatto
- Non si sa se iterare, pivotare o abbandonare
- Non si può imparare da questo lancio per il prossimo
- Non si può giustificare un secondo round di sviluppo
- Il team non ha senso di closure o di successo
- Il PM non può dimostrare il valore del proprio lavoro

### Correzione: Post-Launch Review Minima

Il framework di review deve essere nel PRD originale — non è un afterthought.

```markdown
## 📊 POST-LAUNCH REVIEW FRAMEWORK

### Review a 30 giorni dal lancio

**North Star Result**:
Target: [X] | Actual: [Y] | Delta: [%] | Status: ✅/⚠️/❌

**Primary Metrics**:
| Metrica | Target | Actual | Δ | Status |
|---------|--------|--------|---|--------|

**Cosa ha funzionato**:
1. [Insight positivo con dato]

**Cosa non ha funzionato**:
1. [Insight negativo con dato]

**Decisione**:
[ ] ✅ Continuare e scalare → prossimo sprint
[ ] 🔄 Iterare su [aspetto] → apri PRD Feature Spec
[ ] 🛑 Deprecare → motivo + piano di sunset

**Next Iteration PRD**: [link o "da creare in base alla decisione"]
```

**Owner obbligatorio**: La review a 30 giorni è bloccante per il prossimo sprint sulla stessa area.

---

## Quick Reference: Come Identificare un Anti-Pattern

| Segnale nel PRD | Anti-Pattern Probabile |
|-----------------|----------------------|
| Lista feature senza problem statement | #1 Feature Wishlist |
| "Aumentare X" senza numero | #2 Vague Metric |
| Solo happy path, nessun error state | #3 Orphan Edge Case |
| PRD non aggiornato da 3+ settimane | #4 Eternal Draft |
| Tutte le stories marcate P0 | #5 Everything Is P0 |
| Sezione tecnica con query SQL specifiche | #6 Technical PRD |
| "Target: professionisti" senza dettagli | #7 Missing Persona |
| Non-Goals assente o vaghi | #8 Scope Creep Enabler |
| Problem statement senza evidenza citata | #9 No Evidence |
| "Il designer definirà il flow" | #10 Delegated Design |
| Timeline senza buffer, senza engineering | #11 Impossible Timeline |
| Nessuna distinzione fasi per vibecoding | #12 AI-Unfriendly |
| GDPR menzionato come "todo" | #13 Compliance Afterthought |
| PRD firmato solo dal PM | #14 Single Reviewer |
| Nessuna sezione metriche post-lancio | #15 No Measurement |
