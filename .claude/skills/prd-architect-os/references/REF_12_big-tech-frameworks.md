# REF_12 — Big Tech PRD Frameworks
## Framework di Prodotto delle Migliori Aziende Tech Adattati al Sistema

Questa reference documenta i framework PRD usati internamente dalle top tech companies, con adattamenti pratici per il PRD Architect OS. Non sono framework da seguire ciecamente — sono lenti attraverso cui guardare il tuo prodotto.

---

## 1. AMAZON — Working Backwards (PR/FAQ)

### Origine e Filosofia
Amazon usa il processo "Working Backwards" dal 2004. Prima di scrivere una sola riga di codice, il PM scrive il **comunicato stampa del lancio** come se il prodotto fosse già uscito. Se il comunicato non suona eccitante, il prodotto probabilmente non vale la pena di essere costruito.

### Struttura PR/FAQ Amazon

```markdown
## COMUNICATO STAMPA — [Titolo Prodotto]
### [Città], [Data] — [Nome Azienda] annuncia [Prodotto]

**Paragrafo 1 — Summary Hook** (massimo 3 righe)
[Nome Prodotto] permette a [tipo utente] di [beneficio principale] 
senza [pain point principale che elimina]. Disponibile da [data] 
a [prezzo/modello].

**Paragrafo 2 — Il Problema** (contesto e scala)
[Quanti utenti hanno questo problema]. Oggi, [come cercano di 
risolverlo] — ma questo richiede [quanto tempo/denaro/effort] 
e spesso porta a [outcome negativo].

**Paragrafo 3 — La Soluzione** (come funziona)
Con [Prodotto], [utente tipo] può ora [azione principale] in 
[tempo/semplificazione]. [Funzionalità chiave 1], [funzionalità 
chiave 2], e [funzionalità chiave 3] lavorano insieme per [outcome].

**Paragrafo 4 — Quote CEO/VP** (aspirazionale)
"[Nome], CEO di [Azienda]: '[Prodotto] rappresenta [visione ampia]. 
Crediamo che [affermazione sul futuro del mercato].'"

**Paragrafo 5 — Quote Cliente** (specifico e concreto)
"[Nome], [Ruolo] di [Azienda Cliente]: 'Prima usavo [soluzione attuale] 
e ci volevano [X ore/giorni]. Con [Prodotto] ottengo [risultato] 
in [Y minuti]. Ho già [beneficio concreto misurabile].'"

**Paragrafo 6 — Chiamata all'Azione**
[Prodotto] è disponibile [dove/come]. Per iniziare: [URL/azione].
Per saperne di più: [URL media kit / pagina prodotto].

---

## FAQ CLIENTI (5-7 domande)

**D1: Quanto costa?**
R: [risposta precisa con modello pricing]

**D2: Come funziona [feature principale]?**
R: [spiegazione in linguaggio cliente, senza jargon tecnico]

**D3: I miei dati sono al sicuro?**
R: [risposta compliance e sicurezza]

**D4: Funziona con [tool/sistema già in uso]?**
R: [integrazioni supportate]

**D5: Cosa succede se non sono soddisfatto?**
R: [garanzia / trial / rimborso]

---

## FAQ INTERNE (4-6 domande)

**D1: Perché adesso? Perché non aspettare?**
R: [urgenza di mercato, window of opportunity]

**D2: Cosa succederebbe se non lo costruissimo?**
R: [alternativa concorrente, perdita di mercato]

**D3: Qual è il nostro unfair advantage?**
R: [cosa abbiamo noi che i concorrenti non hanno]

**D4: Chi è il nostro cliente reale? Chi stiamo escludendo?**
R: [definizione precisa ICP + chi esplicitamente fuori scope]

**D5: Come si monetizza?**
R: [modello revenue con numeri specifici]

**D6: Quali metriche indicano successo nei primi 90 giorni?**
R: [KPI con target]
```

### Quando usarlo nel PRD Architect OS
- PRD Tipo E (PR/FAQ) → questo è il template nativo
- Fase di validazione idea: scrivilo prima del PRD completo
- Stakeholder exec che non leggono PRD lunghi → summary perfetto

### Vantaggi e Limiti
| Vantaggi | Limiti |
|----------|--------|
| Forza chiarezza sul "perché" | Non adatto a feature incremental |
| Ottimo per executive alignment | Manca specifica tecnica |
| Testa la narrativa del prodotto | Difficile per prodotti B2B complessi |
| Svela se il prodotto è confuso | |

---

## 2. GOOGLE — Product Spec (Gonzo Doc)

### Origine e Filosofia
Google usa i "Product Specs" — noti informalmente come "Gonzo Docs" — che uniscono visione strategica, specifiche funzionali e dati in un unico documento ad alta densità. La cultura Google valorizza la velocità di iterazione e la chiarezza tecnica.

### Struttura Google Product Spec

```markdown
# [Feature Name] — Product Spec
**Status**: [DRAFT / IN REVIEW / APPROVED / SHIPPED]
**DRI** (Directly Responsible Individual): [Nome]
**Stakeholders**: [Lista]
**Ultima revisione**: [Data]

---

## TL;DR
[3 bullet. Chiunque deve capire cosa stiamo costruendo e perché in 30 secondi]
- Stiamo costruendo: [cosa]
- Per: [chi]
- Perché: [motivazione business con dato]

---

## Problema e Contesto
### Cosa sta succedendo nel mercato?
[Dato di mercato + trend]

### Come lo sappiamo?
- User research: [N interviste, data]
- Analytics: [metrica attuale vs target]
- Feedback support: [% ticket su questo problema]

### Perché ora?
[Window of opportunity / urgenza competitiva]

---

## Obiettivi e Non-Obiettivi

**Obiettivi** (cosa deve fare questa feature):
1. [Obiettivo 1 — misurabile]
2. [Obiettivo 2 — misurabile]

**Non-Obiettivi** (cosa NON deve fare — importante):
1. [Non-obiettivo 1 — con motivazione]
2. [Non-obiettivo 2]

---

## Proposta di Soluzione

### Opzione A — [Nome Opzione] (RACCOMANDATA)
[Descrizione soluzione A]
**Pro**: [lista]
**Contro**: [lista]
**Effort**: [S/M/L]

### Opzione B — [Nome Opzione]
[Descrizione soluzione B]
**Pro**: [lista]
**Contro**: [lista]
**Effort**: [S/M/L]

### Perché A e non B?
[Ragionamento decisionale esplicito]

---

## User Experience — Key Scenarios

**Scenario 1 — [Nome scenario]**
Attore: [Persona]
Before: [situazione attuale, dolorosa]
After: [situazione con la feature, migliorata]
Flusso:
  1. [step 1]
  2. [step 2]
  3. [step 3 — outcome]

---

## Specifiche Funzionali

### [Feature/Componente 1]
**Comportamento**: [descrizione precisa]
**Edge cases**:
- SE [condizione X] → [comportamento atteso]
- SE [condizione Y] → [comportamento atteso]

---

## Metriche e Guardrail
**Metrica primaria**: [nome] — target: [X] entro [data]
**Metrica secondaria**: [nome] — target: [Y]
**Guardrail**: [cosa non deve peggiorare] — soglia: [Z]

---

## Rischi

| Rischio | Probabilità | Impatto | Mitigazione |
|---------|-------------|---------|-------------|
| [Rischio 1] | Alta | Alto | [Piano B] |
| [Rischio 2] | Bassa | Medio | [Monitoraggio] |

---

## Piano di Lancio
**M0** [Data]: Specifiche approvate
**M1** [Data]: Alpha interna (5% utenti)
**M2** [Data]: Beta (20% utenti)
**M3** [Data]: GA (100%)
**M4** [Data]: Post-launch review
```

### Quando usarlo
- Feature grandi in prodotto esistente (→ PRD Tipo C Enterprise)
- Team distribuiti che hanno bisogno di maximum clarity
- Quando ci sono opzioni alternative da valutare esplicitamente

---

## 3. AIRBNB — Feature Story

### Origine e Filosofia
Airbnb usa il concetto di "Feature Story" — il PRD inizia sempre da un racconto di un utente reale in una situazione specifica. Non "un utente generico", ma "Valentina, 34 anni, host a Milano, che ha avuto questo problema esatto mercoledì scorso".

### Struttura Feature Story

```markdown
# Feature Story: [Nome Feature]

## La Storia

*È mercoledì mattina. [Nome], [ruolo], [città].*

*[Descrizione vivida della situazione: cosa sta cercando di fare, 
perché è importante, cosa succede oggi che è frustrante/lento/rotto]*

*[Momento di svolta: trova/usa la nuova feature]*

*[Outcome: come cambia la sua giornata/risultato]*

---

## Perché Questa Storia Conta

**Quanti Valentina ci sono?** [N utenti con questo pattern]
**Frequenza**: [quante volte/settimana/mese accade]
**Impatto business**: [revenue / retention / NPS correlato]

---

## La Feature

### Cosa costruiamo
[Descrizione funzionale pulita — 1 paragrafo]

### Come si integra nel prodotto esistente
[Dove vive nella navigazione, come si accede]

---

## Principi di Design della Feature

1. **[Principio 1]**: [Spiegazione + esempio concreto]
2. **[Principio 2]**: [Spiegazione + esempio]
3. **[Principio 3]**: [Spiegazione + esempio]

---

## User Stories Core

**[Nome Feature] — Happy Path**
Come [persona], quando [contesto specifico], voglio [azione], 
in modo da [beneficio].

**Acceptance Criteria**:
- PASSA SE: [condizione verificabile 1]
- PASSA SE: [condizione verificabile 2]
- FALLISCE SE: [condizione negativa]

---

## Anti-Stories (cosa NON facciamo)

Come design team, NON vogliamo che [persona] debba [azione frustrante],
perché [motivazione].

**Vincolo di design resultante**: [cosa non costruiamo + perché]
```

### Quando usarlo
- Feature con forte componente UX/design
- Team dove designer e PM devono allinearsi
- Presentazione a leadership non tecnica

---

## 4. SPOTIFY — Opportunity Assessment

### Origine e Filosofia
Spotify usa un "Opportunity Assessment" come gate prima del PRD completo. È un documento di 1 pagina che risponde a 4 domande fondamentali. Solo se supera l'assessment si procede al PRD esteso.

### Template Opportunity Assessment

```markdown
# Opportunity Assessment: [Nome Feature/Prodotto]
**Data**: [Data]
**Team**: [Squad/Team]
**DRI**: [Nome]

---

## Le 4 Domande (risposte brevi, max 3 righe ciascuna)

### 1. Qual è l'esatto problema che stiamo risolvendo?
[Problema specifico, non soluzione. Con dato quantitativo se disponibile]

### 2. Per chi lo stiamo risolvendo?
[Persona specifica con contesto. Non "tutti gli utenti".]

### 3. Come sappiamo che questo problema esiste?
[Evidenza: dato analytics / interviste / support ticket / ricerca]

### 4. Come valutiamo il successo?
[1-2 metriche. Con target numerico. Con timeframe.]

---

## Opportunity Sizing
**TAM nel nostro prodotto**: [N utenti che hanno questo problema]
**Frequenza**: [quante volte/mese per utente]
**Willingness to pay / engage**: [proxy o dato]

---

## Livello di Confidenza
□ Alta — abbiamo dati diretti (interviste + analytics)
□ Media — abbiamo dati indiretti (analytics o interviste, non entrambi)
□ Bassa — ipotesi da validare (richiede discovery prima del PRD)

---

## Raccomandazione
□ Procedi con PRD completo
□ Fai discovery prima (specifica cosa validare)
□ Depriorizza (motivazione)
```

### Quando usarlo nel PRD Architect OS
- Come pre-PRD per tutti i Tipi A e B
- Quando il cliente non è sicuro se la feature valga la pena
- Discovery phase prima dell'engagement completo

---

## 5. INTERCOM — Jobs to Be Done Framework

### Origine e Filosofia
Intercom usa esplicitamente la teoria JTBD (Jobs to Be Done) di Clayton Christensen nei loro PRD. Ogni feature parte dalla domanda: "Quale lavoro sta cercando di completare l'utente?"

### Template JTBD Intercom-style

```markdown
## Jobs to Be Done Analysis

### Job Statement Principale
"Quando [situazione specifica], voglio [motivazione/goal], 
in modo da [outcome desiderato]."

Esempio corretto:
✅ "Quando ricevo un messaggio dal supporto durante una demo con un cliente,
    voglio sapere immediatamente se è urgente,
    in modo da non interrompere inutilmente la demo."

Esempio sbagliato (descrive soluzione, non job):
❌ "Voglio ricevere notifiche push per i messaggi."

---

### Job Map (sequenza di micro-job)

| Step | Micro-Job | Outcome atteso | Pain attuali |
|------|-----------|----------------|--------------|
| 1. Define | L'utente decide di [iniziare task] | Sa dove andare | [Lista friction] |
| 2. Locate | Trova gli strumenti necessari | Accesso rapido | [Lista friction] |
| 3. Prepare | Configura/setup | Pronto in <1 min | [Lista friction] |
| 4. Execute | Completa il task principale | Risultato corretto | [Lista friction] |
| 5. Monitor | Verifica che sia andato bene | Conferma visiva | [Lista friction] |
| 6. Resolve | Gestisce eccezioni | Recovery rapido | [Lista friction] |
| 7. Conclude | Chiude/archivia | Tutto tracciato | [Lista friction] |

---

### Desired Outcomes (da user interviews)
Usando la scala importanza/soddisfazione di Ulwick:

| Outcome | Importanza (1-10) | Soddisfazione attuale (1-10) | Opportunity Score |
|---------|-------------------|------------------------------|-------------------|
| [Outcome 1] | 9 | 3 | 15 → 🔥 HIGH |
| [Outcome 2] | 7 | 6 | 8 → MEDIUM |
| [Outcome 3] | 4 | 7 | 1 → LOW |

*Opportunity Score = Importanza + max(Importanza - Soddisfazione, 0)*
*Score >10 = opportunità di mercato alta*
```

---

## 6. MICROSOFT — Functional Specification

### Origine e Filosofia
Microsoft usa "Functional Specs" ad altissima densità tecnica. Il documento risponde alla domanda di un developer: "Cosa devo costruire esattamente?" Non lascia spazio a interpretazione.

### Elementi Chiave Functional Spec

```markdown
## Functional Spec: [Feature Name]

### Behavioral Requirements

**FR-001**: Il sistema DEVE [comportamento obbligatorio]
**FR-002**: Il sistema DOVREBBE [comportamento raccomandato]
**FR-003**: Il sistema PUÒ [comportamento opzionale]
**FR-004**: Il sistema NON DEVE MAI [comportamento proibito]

*Usa linguaggio modale RFC 2119: MUST / SHOULD / MAY / MUST NOT*

---

### State Machine

```
                    [evento trigger]
[Stato A] ─────────────────────────────► [Stato B]
    │                                        │
    │ [evento X]                [evento Y]   │
    ▼                                        ▼
[Stato C] ◄──────────────────────────── [Stato D]
                 [evento Z]
```

**Invarianti di stato** (sempre veri in ogni stato):
- [Invariante 1]
- [Invariante 2]

---

### Error Catalog

| Error Code | Situazione | Messaggio utente | Azione sistema | Azione utente |
|------------|-----------|------------------|----------------|---------------|
| ERR_AUTH_001 | Token scaduto | "Sessione scaduta. Accedi di nuovo." | Invalida sessione | Redirect /login |
| ERR_VAL_001 | Email malformata | "Email non valida. Controlla e riprova." | Blocca form submit | Correggi campo |
| ERR_SRV_001 | Database timeout | "Servizio temporaneamente non disponibile." | Retry 3x poi fail | Riprova tra 5 min |

---

### Performance Requirements

| Operazione | Target P50 | Target P95 | Target P99 | Max Accettabile |
|-----------|-----------|-----------|-----------|-----------------|
| Page load | 800ms | 1.5s | 2.5s | 4s |
| API response | 200ms | 500ms | 1s | 3s |
| Search query | 300ms | 800ms | 1.5s | 3s |
| File upload 1MB | 2s | 4s | 8s | 15s |
```

---

## Quando Usare Quale Framework

| Situazione | Framework Consigliato | PRD Tipo |
|-----------|----------------------|----------|
| Nuovo prodotto da lanciare | Amazon PR/FAQ | E → poi B |
| Feature grande su prodotto esistente | Google Product Spec | A o C |
| Feature UX-heavy, team design-led | Airbnb Feature Story | C |
| Idea da validare prima di committarsi | Spotify Opportunity Assessment | Pre-PRD |
| Prodotto consumer con forte emotional driver | Intercom JTBD | B o A |
| Feature tecnica complessa, team engineering-led | Microsoft Functional Spec | A |
| App AI-built, Cursor/Lovable | Vibecoding Constraints | D |

---

## Elementi Universali (presenti in tutti i framework)

Indipendentemente dal framework scelto, questi elementi NON sono mai assenti:

1. **Problem Statement con dato** — tutti i framework iniziano dal problema, non dalla soluzione
2. **Target utente specifico** — nessun framework usa "tutti gli utenti"
3. **Success metric misurabile** — ogni framework ha almeno 1 KPI con target numerico
4. **Scope esplicito (IN e OUT)** — ogni framework chiarisce cosa non fa
5. **Timeline realistica** — ogni framework ha una data o milestone

Questi 5 elementi sono il minimo comune denominatore di ogni PRD eccellente, qualunque sia il framework usato.
