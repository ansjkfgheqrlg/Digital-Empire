🧠 SKILL: PRD ARCHITECT OS
 IDENTITÀ, TRIGGER, RELAZIONI
1️⃣ IDENTITÀ DELLA SKILL
PRD Architect OS è la skill responsabile di:

Trasformare idee vaghe in requisiti strutturati
Eliminare ambiguità prima dello sviluppo
Prevenire scope creep
Strutturare PRD per:
SaaS
Web App
Mobile App
AI Tool
Vibecoding
Feature su prodotto esistente
Progetti agency client
Non è un template.
È un sistema decisionale guidato.

2️⃣ TRIGGER (Quando si attiva)
Questa skill si attiva quando:

✅ Devi costruire un nuovo prodotto digitale
✅ Devi creare un SaaS (MVP o completo)
✅ Devi scrivere un PRD per vibecoding con AI (Cursor, Claude, Bolt, v0)
✅ Devi aggiungere una feature a un SaaS esistente
✅ Devi documentare requisiti per un team di sviluppo
✅ Devi validare un’idea prima di svilupparla
✅ Devi presentare un progetto a un team o a un cliente
✅ Devi ridurre ambiguità prima di scrivere codice

⚠️ NON si attiva per:

Copy marketing
Strategie growth
Landing page
Funnel marketing
3️⃣ RELAZIONE CON ALTRI PROGETTI E SKILL
text

MAPPA DIPENDENZE — PRD ARCHITECT OS
════════════════════════════════════════════════════════════

RICEVE INPUT DA:
┌───────────────────────────────┬───────────────────────────┐
│ Progetto/Skill                │ Cosa riceve               │
├───────────────────────────────┼───────────────────────────┤
│ Strategy Command Center       │ Obiettivi business        │
│                               │ KPI target                │
├───────────────────────────────┼───────────────────────────┤
│ Client Research Engine        │ Pain point reali          │
│                               │ Obiezioni utente          │
│                               │ Linguaggio target         │
├───────────────────────────────┼───────────────────────────┤
│ Marketing University          │ Framework prodotto        │
│                               │ Analisi competitor        │
├───────────────────────────────┼───────────────────────────┤
│ Agency Operations             │ Brief cliente             │
│                               │ Vincoli budget/time       │
├───────────────────────────────┼───────────────────────────┤
│ AI Influencer Lab             │ Se PRD riguarda AI tool   │
└───────────────────────────────┴───────────────────────────┘


PRODUCE OUTPUT PER:
┌───────────────────────────────┬───────────────────────────┐
│ Destinatario                  │ Cosa produce              │
├───────────────────────────────┼───────────────────────────┤
│ Engineering Team              │ PRD strutturato           │
├───────────────────────────────┼───────────────────────────┤
│ Vibecoding AI                 │ PRD Markdown operativo    │
├───────────────────────────────┼───────────────────────────┤
│ Design Team                   │ User flow + Edge cases    │
├───────────────────────────────┼───────────────────────────┤
│ Founder / Stakeholder         │ PR/FAQ Amazon-style       │
├───────────────────────────────┼───────────────────────────┤
│ Jira / Linear                 │ Epic → Story breakdown    │
└───────────────────────────────┴───────────────────────────┘
4️⃣ OUTPUT PRINCIPALI DELLA SKILL
La skill può produrre 5 tipi di output:

PRD COMPLETO (Enterprise)
PRD MVP Lean
FEATURE SPEC
PRD per Vibecoding (AI-ready .md)
PR/FAQ Amazon-style (Validazione strategica)
L’output dipende dal contesto selezionato.

5️⃣ POSIZIONAMENTO NEL DIGITAL EMPIRE OS
PRD Architect OS diventa:

text

IDEA → STRATEGIA → PRD ARCHITECT → DESIGN → BUILD → TEST → SCALE
È il ponte tra strategia e codice.

Senza questa skill:

Le build sono confuse
L’AI entra in loop
Lo scope esplode
Le metriche non sono definite
Il team interpreta diversamente

2️⃣ PREREQUISITI
Prima di attivare questa skill e produrre qualsiasi output, il sistema deve raccogliere un set minimo di informazioni. Senza questi prerequisiti, il PRD generato sarà generico, inutile e pericoloso da passare a un team di sviluppo o a un'AI.

La skill gestisce i prerequisiti in due livelli:

Livello 1 — Prerequisiti Minimi (obbligatori per qualsiasi tipo di PRD)
Livello 2 — Prerequisiti Avanzati (richiesti per PRD completi, SaaS enterprise, o vibecoding)
📋 LIVELLO 1 — PREREQUISITI MINIMI (Obbligatori)
Python

PREREQUISITI_MINIMI = {

    "idea_o_problema": {
        "descrizione": "Descrizione dell'idea, feature o prodotto da costruire",
        "formato_accettato": [
            "Frase libera (anche vaga — la skill la struttura)",
            "Lista di funzionalità desiderate",
            "Problema da risolvere",
            "PR/FAQ grezzo non ancora strutturato"
        ],
        "esempio_accettato": (
            "Voglio costruire un SaaS che permette ai "
            "freelancer di inviare preventivi automatici "
            "basati su template personalizzabili"
        ),
        "perche_serve": (
            "Senza il problema core, il PRD non ha un "
            "centro gravitazionale. Ogni sezione ruota "
            "intorno al problema."
        ),
        "errore_se_manca": (
            "La skill genera un PRD generico che "
            "descrive feature senza un perché"
        )
    },

    "tipo_prd": {
        "descrizione": "Quale tipo di PRD deve essere prodotto",
        "opzioni": [
            "A — PRD Completo Enterprise (10-30 pagine)",
            "B — PRD MVP Lean (3-5 pagine)",
            "C — Feature Spec (1-3 pagine)",
            "D — PRD per Vibecoding AI-ready (.md)",
            "E — PR/FAQ Amazon-style (1 pagina)"
        ],
        "default_se_non_specificato": "B — PRD MVP Lean",
        "perche_serve": (
            "Struttura, lunghezza, sezioni e formato "
            "cambiano radicalmente tra i tipi. "
            "Scegliere il tipo sbagliato = documento "
            "inutilizzabile."
        )
    },

    "target_utente": {
        "descrizione": "Chi usa il prodotto — persona primaria",
        "formato_accettato": [
            "Descrizione libera (es: freelancer italiani 25-40 anni)",
            "Persona già strutturata (nome, ruolo, pain point)",
            "Segmento di mercato (es: PMI del settore healthcare)"
        ],
        "perche_serve": (
            "Ogni user story, ogni acceptance criteria, "
            "ogni edge case è scritto per questa persona. "
            "Senza target, le user stories sono astratte."
        ),
        "errore_se_manca": (
            "La skill usa una persona generica "
            "che non rispecchia la realtà"
        )
    },

    "contesto_sviluppo": {
        "descrizione": "Come verrà sviluppato il prodotto",
        "opzioni": {
            "VIBECODING": (
                "Sviluppo con AI (Cursor, Claude, Bolt, "
                "Lovable, v0, Replit)"
            ),
            "TEAM_UMANO": (
                "Developer/designer umani (freelancer, "
                "team interno, agenzia)"
            ),
            "MISTO": (
                "Combinazione — AI per scaffolding, "
                "umani per logica complessa"
            ),
            "AGENCY_CLIENT": (
                "PRD da consegnare a un cliente "
                "come parte del deliverable"
            )
        },
        "perche_serve": (
            "Cambia il livello di dettaglio tecnico, "
            "il formato, la granularità delle sezioni. "
            "Un PRD per Cursor è strutturato diversamente "
            "da uno per un team enterprise."
        )
    }
}
📋 LIVELLO 2 — PREREQUISITI AVANZATI
Python

PREREQUISITI_AVANZATI = {

    "tech_stack": {
        "obbligatorio_per": [
            "PRD per Vibecoding",
            "PRD per SaaS enterprise",
            "PRD Completo"
        ],
        "opzionale_per": [
            "PRD MVP Lean",
            "PR/FAQ Amazon-style"
        ],
        "componenti_da_specificare": {
            "frontend": [
                "React", "Next.js", "Vue", "Svelte",
                "React Native", "Flutter", "da definire"
            ],
            "backend": [
                "Node.js", "Python/FastAPI", "Go",
                "Ruby on Rails", "Laravel", "da definire"
            ],
            "database": [
                "PostgreSQL", "MySQL", "MongoDB",
                "Supabase", "Firebase", "PlanetScale",
                "da definire"
            ],
            "hosting": [
                "AWS", "GCP", "Vercel", "Railway",
                "Render", "Fly.io", "da definire"
            ],
            "auth": [
                "Supabase Auth", "Auth0", "Clerk",
                "NextAuth", "custom JWT", "da definire"
            ],
            "payments": [
                "Stripe", "Paddle", "Lemon Squeezy",
                "PayPal", "nessuno per MVP", "da definire"
            ],
            "ai_layer": [
                "OpenAI API", "Anthropic Claude API",
                "Groq", "Ollama (local)", "nessuno",
                "da definire"
            ]
        },
        "perche_serve": (
            "Il tech stack vincola ogni decisione "
            "architetturale nel PRD. Un PRD che parla di "
            "real-time features senza specificare se si "
            "usa WebSocket, SSE o polling è inutile."
        )
    },

    "success_metrics_iniziali": {
        "obbligatorio_per": [
            "PRD Completo Enterprise",
            "PRD MVP Lean"
        ],
        "descrizione": (
            "Quali metriche definiranno il successo "
            "del prodotto o della feature"
        ),
        "tipi_accettati": {
            "business": [
                "MRR target",
                "CAC massimo accettabile",
                "Churn rate target",
                "Conversion rate trial→paid"
            ],
            "prodotto": [
                "DAU/MAU",
                "Day-7 retention",
                "Feature adoption rate",
                "Time-to-value (minuti dal signup al primo valore)"
            ],
            "tecnici": [
                "Uptime SLA",
                "Latenza P95",
                "Error rate massimo"
            ]
        },
        "perche_serve": (
            "Senza success metrics definite PRIMA dello "
            "sviluppo, il team non sa quando il prodotto "
            "è 'finito' o 'ha successo'. Cagan: "
            "'Il PRD senza metriche è un wishlist.'"
        )
    },

    "vincoli_noti": {
        "obbligatorio_per": ["tutti i tipi"],
        "tipi_di_vincolo": {
            "budget": "Budget disponibile in €",
            "tempo": "Deadline o time-box (es: 2 settimane)",
            "team": "Numero e tipo di persone disponibili",
            "tecnici": "Vincoli architetturali esistenti",
            "legali": (
                "GDPR, settore regolamentato, "
                "compliance necessaria"
            ),
            "business": (
                "Integrazioni obbligatorie, "
                "sistemi legacy da mantenere"
            )
        },
        "perche_serve": (
            "I vincoli non sono limitazioni — sono "
            "i confini dentro cui la soluzione deve "
            "esistere. Shape Up chiama questo 'appetite'. "
            "Senza vincoli, lo scope esplode sempre."
        )
    },

    "saas_specifico": {
        "obbligatorio_per": [
            "SaaS PRD",
            "PRD Completo Enterprise"
        ],
        "domande": {
            "modello_pricing": [
                "Freemium",
                "Trial gratuito → paid",
                "Solo paid",
                "Usage-based",
                "One-time payment"
            ],
            "multi_tenancy": [
                "Single tenant",
                "Multi-tenant (dati isolati per account)",
                "Multi-tenant (dati condivisi)"
            ],
            "ruoli_utente": (
                "Quali ruoli esistono nel sistema? "
                "(es: Owner, Admin, Member, Viewer)"
            ),
            "integrazioni_necessarie": (
                "Quali integrazioni sono richieste "
                "per il lancio? (es: Slack, Zapier, "
                "Google Calendar)"
            ),
            "compliance": [
                "GDPR richiesto",
                "SOC 2 richiesto",
                "HIPAA richiesto",
                "Nessuna compliance specifica"
            ]
        }
    }
}
🔴 CHECKLIST PREREQUISITI — Cosa Verificare Prima di Procedere
Markdown

## PREREQUISITI VERIFICATI ✅

### LIVELLO 1 (Obbligatori)
- [ ] Idea/problema descritta con sufficiente chiarezza
- [ ] Tipo di PRD selezionato (A/B/C/D/E)
- [ ] Target utente identificato (anche sommariamente)
- [ ] Contesto sviluppo definito (vibecoding / team / misto)

### LIVELLO 2 (Avanzati — se PRD Completo o Vibecoding)
- [ ] Tech stack specificato o "da definire" accettato
- [ ] Success metrics iniziali identificate (anche 1-2)
- [ ] Vincoli noti dichiarati (budget, tempo, team)
- [ ] Configurazione SaaS definita (se applicabile)

### GATE DI QUALITÀ
- [ ] Il problema è descritto come PROBLEMA (non come soluzione)
  ❌ "Voglio un bottone rosso"
  ✅ "Gli utenti abbandonano il checkout al 70%"

- [ ] Il target utente è una PERSONA, non un mercato
  ❌ "PMI italiane"
  ✅ "Marco, 34 anni, founder di una web agency da 5 persone"

- [ ] I vincoli sono REALI, non aspirazionali
  ❌ "Voglio lanciare presto"
  ✅ "Ho 3 settimane e un budget di €2.000"
3️⃣ PRINCIPIO FONDAMENTALE
text

═══════════════════════════════════════════════════════════════

  "UN PRD NON È UN DOCUMENTO.
   È UN SISTEMA DI ELIMINAZIONE DELL'AMBIGUITÀ."

  Il codice scritto su basi ambigue ha un costo:
  - Ogni ora di sviluppo su requisiti sbagliati
    = 3-5 ore di refactor + 2 ore di riunioni
  - Ogni feature costruita senza success metrics
    = impossibile sapere se ha funzionato
  - Ogni edge case non documentato
    = bug in produzione con utenti reali

  Il PRD Architect OS esiste per un solo motivo:
  RENDERE IMPOSSIBILE COSTRUIRE LA COSA SBAGLIATA.

═══════════════════════════════════════════════════════════════
4️⃣ FILOSOFIA OPERATIVA — I 7 ASSIOMI DEL PRD ARCHITECT OS
ASSIOMA 1 — Il Problema Prima di Tutto
Markdown

## ❌ ANTI-PATTERN: Solution-First PRD
"Voglio un dashboard con grafici circolari, 
tabelle filtrabili e un sistema di export CSV."

## ✅ PATTERN CORRETTO: Problem-First PRD
"Il 60% dei nostri utenti abbandona dopo il 
primo login perché non capisce cosa fare. 
Il dashboard attuale mostra dati grezzi senza 
contesto. L'utente non vede il suo progresso."

LA REGOLA:
Se riesci a scrivere il PRD senza menzionare 
il problema dell'utente, il PRD è sbagliato.
ASSIOMA 2 — I Non-Goals sono Obbligatori
Markdown

## PERCHÉ I NON-GOALS SONO OBBLIGATORI

Un PRD senza Non-Goals è un contenitore aperto.
Ogni stakeholder ci metterà dentro ciò che vuole.

Il Non-Goal non è una limitazione.
È una decisione strategica documentata.

## ESEMPIO
### Goals (questa release):
- Utente crea account e si autentica
- Utente pubblica un preventivo in <5 minuti
- Sistema invia email al cliente con PDF allegato

### Non-Goals (esplicitamente esclusi):
- Firma digitale del preventivo (v2)
- Integrazione con software contabili (v3)
- App mobile (dopo validazione web)
- Template marketplace (post-PMF)

LA REGOLA:
Per ogni feature IN-SCOPE, 
definisci almeno una cosa OUT-OF-SCOPE correlata.
ASSIOMA 3 — Le Metriche Si Definiscono Prima, Non Dopo
Markdown

## IL PROBLEMA DEL POST-HOC MEASUREMENT

"Abbiamo lanciato la feature.
Ha funzionato? Boh, gli utenti sembrano contenti."

Questo succede quando le metriche non sono 
nel PRD. Il team non sa cosa misurare, 
quindi non misura niente, quindi non impara niente.

## LA STRUTTURA CORRETTA NEL PRD

### North Star Metric (1 sola):
→ Il numero che, se migliora, tutto il resto migliora

### Primary Metrics (max 3):
→ KPI direttamente impattati dalla feature

### Guardrail Metrics:
→ Cosa NON deve peggiorare (anche se la feature ha successo)

### Measurement Method:
→ Come e dove misuriamo (Mixpanel, Posthog, custom event)

## ESEMPIO COMPILATO

North Star: Time-to-first-value ≤ 5 minuti dal signup

Primary Metrics:
1. Day-7 retention: target ≥ 40% (attuale: 23%)
2. Preventivi inviati per utente nel primo giorno: ≥ 1
3. Conversion trial→paid: target ≥ 8% (attuale: 3%)

Guardrail:
- Crash rate: ≤ 0.5% sessioni
- Email delivery rate: ≥ 98%
- Load time homepage: ≤ 2 secondi P95

Measurement:
- Posthog: evento "invoice_sent" con property {user_id, template_id}
- Stripe: webhook "subscription_created"
- Sentry: error tracking automatico
ASSIOMA 4 — Gli Edge Case Non Sono Opzionali
Markdown

## IL COSTO DEGLI EDGE CASE NON DOCUMENTATI

Un developer umano li intuisce (o chiede).
Un'AI non li intuisce mai. Mai.
Un team di 3 persone li dimentica in sprint.

Gli edge case non documentati = bug in produzione.

## LE 8 CATEGORIE DI EDGE CASE DA COPRIRE SEMPRE

1. EMPTY STATE
   → Cosa vede l'utente quando non ha ancora dati?
   → Primo accesso, lista vuota, zero risultati di ricerca

2. LOADING STATE
   → Cosa succede mentre il sistema elabora?
   → Skeleton screen, spinner, barra di progressione?

3. ERROR STATE (specifico, non generico)
   ❌ "Mostra un errore"
   ✅ "Se la chiamata API fallisce dopo 3 retry,
       mostra: 'Impossibile connettersi al servizio.
       I tuoi dati sono stati salvati localmente.
       Riprova tra qualche minuto.' + bottone 'Riprova'"

4. SUCCESS STATE
   → Cosa succede dopo un'azione completata?
   → Feedback visivo, redirect, email, notifica?

5. OFFLINE STATE
   → Il prodotto funziona senza connessione?
   → Se no, cosa mostra?

6. PERMISSION DENIED
   → Cosa vede un utente che cerca di accedere
     a una feature per cui non ha il piano/ruolo?

7. RATE LIMIT RAGGIUNTO
   → L'utente ha esaurito le API calls, lo storage,
     i preventivi del piano gratuito?
   → Cosa vede? Come viene invitato all'upgrade?

8. DATI CORROTTI / MALFORMATI
   → Input inatteso, file non supportato, 
     risposta API malformata?
ASSIOMA 5 — Il PRD per Vibecoding Ha Regole Proprie
Markdown

## PERCHÉ IL PRD PER AI È DIVERSO

Un developer umano:
- Interpreta l'ambiguità
- Chiede chiarimenti
- Ha esperienza pregressa
- Ragiona sul contesto

Un'AI (Cursor, Claude, Bolt):
- Non interpreta: inventa
- Non chiede: genera qualcosa di plausibile
- Ha zero contesto del tuo progetto specifico
- Perde il contesto dopo 10k token

## LE 6 REGOLE DEL PRD VIBECODING

REGOLA 1: FORMATO MARKDOWN OBBLIGATORIO
→ Il file va in /docs/PRD.md nel repository
→ Mai in PDF, mai in Notion senza export
→ Cursor lo legge come file di progetto

REGOLA 2: TECH STACK ESPLICITO E VINCOLANTE
❌ "Usa un database scalabile"
✅ "PostgreSQL su Supabase. Row Level Security 
    abilitato. Ogni tabella ha colonna tenant_id.
    Usa Prisma come ORM."

REGOLA 3: FASI NUMERATE (non feature list)
❌ Lista di 20 feature da costruire
✅ Fase 1 (giorni 1-3): Auth + schema DB
   Fase 2 (giorni 4-7): Core feature X
   Fase 3 (giorni 8-10): Payments + onboarding
→ Passa all'AI una fase alla volta

REGOLA 4: USER FLOW COME TESTO, NON IMMAGINI
❌ Link a Figma wireframe
✅ "1. Utente visita /pricing
    2. Clicca 'Inizia gratis'
    3. Redirect a /signup
    4. Form: email + password + nome
    5. Submit → POST /api/auth/register
    6. Success → redirect a /onboarding/step-1
    7. Error (email già usata) → inline message
       sotto il campo email: 'Questa email è 
       già registrata. Vuoi fare login?'"

REGOLA 5: ACCEPTANCE CRITERIA TESTABILI
Per ogni feature, scrivi:
"✅ PASSA se: [condizione misurabile]"
"❌ FALLISCE se: [condizione misurabile]"

REGOLA 6: SEZIONE "AI CONSTRAINTS" ESPLICITA
→ Cosa l'AI NON deve fare anche se sembra logico
Esempio:
"Non aggiungere feature non specificate.
Non cambiare il tech stack scelto.
Non usare librerie diverse da quelle elencate.
Se hai dubbi, chiedi prima di implementare."
ASSIOMA 6 — Il PRD è Vivo, Non Statico
Markdown

## IL DOCUMENTO FOSSILE

Un PRD scritto il giorno 1 e mai aggiornato
diventa pericoloso dopo 2 sprint.

Il team prende decisioni che contraddicono il PRD.
Il PRD dice una cosa, il codice ne fa un'altra.
Nessuno sa quale dei due è la "verità".

## IL SISTEMA DI VERSIONAMENTO

### Header del PRD (obbligatorio)
---
Titolo: [Nome Feature/Prodotto]
Versione: 1.3
Status: IN REVIEW | APPROVED | DEPRECATED
Autore: [Nome]
Data creazione: GG/MM/AAAA
Ultima modifica: GG/MM/AAAA
Prossima review: GG/MM/AAAA
---

### Change Log (sezione obbligatoria)
| Versione | Data | Autore | Modifica | Motivo |
|----------|------|--------|----------|--------|
| 1.0 | 01/01 | PM | Draft iniziale | — |
| 1.1 | 05/01 | PM | Aggiunta sezione billing | Feedback eng |
| 1.2 | 10/01 | PM | Rimossa feature X | Out of scope Q1 |

### Trigger per aggiornamento obbligatorio:
- Engineering scopre un vincolo tecnico non previsto
- Un'assunzione del PRD si rivela falsa
- Gli stakeholder cambiano priorità
- Una user story viene modificata durante lo sprint
- Il tech stack cambia
ASSIOMA 7 — La Chiarezza è più Importante della Completezza
Markdown

## LA TRAPPOLA DEL PRD ENCICLOPEDICO

Un PRD da 50 pagine che nessuno legge
è peggio di un PRD da 5 pagine che tutti leggono.

La completezza non è una virtù se sacrifica la chiarezza.

## LE REGOLE DI LUNGHEZZA PER TIPO

| Tipo PRD              | Lunghezza Target | Lunghezza Max |
|-----------------------|-----------------|---------------|
| PR/FAQ Amazon-style   | 1 pagina        | 2 pagine      |
| PRD MVP Lean          | 3-5 pagine      | 7 pagine      |
| Feature Spec          | 1-3 pagine      | 5 pagine      |
| PRD Vibecoding        | 2-4 pagine      | 6 pagine      |
| PRD Completo Enterprise | 10-20 pagine  | 30 pagine     |

## LA REGOLA DELLA FRASE

Ogni frase nel PRD deve rispondere a:
"Se questa frase non c'è, cosa non capisce 
il developer/designer/AI?"

Se la risposta è "niente di critico" → elimina la frase.

---

## 🎯 OVERVIEW DEL FRAMEWORK

Il framework core di PRD Architect OS è diviso in **4 motori**:

- **MOTORE 1 — INTAKE ENGINE**: Il sistema di intervista strutturata
- **MOTORE 2 — CONTEXT ENRICHMENT ENGINE**: Come la skill arricchisce il contesto
- **MOTORE 3 — GENERATION ENGINE**: Come viene costruito il PRD sezione per sezione
- **MOTORE 4 — VALIDATION ENGINE**: Come si valida il PRD prima dell'output finale

Questi 4 motori lavorano in sequenza obbligatoria.
Non si può saltare un motore.
Non si può generare il PRD senza aver completato l'intake.

---

## ⚙️ MOTORE 1 — INTAKE ENGINE
### Il Sistema di Intervista Strutturata

---

### PRINCIPIO DEL MOTORE 1

```python
INTAKE_ENGINE_LOGIC = {

    "obiettivo": (
        "Raccogliere abbastanza contesto per rendere "
        "impossibile generare un PRD generico. "
        "Se l'input è vago, la skill NON genera. "
        "La skill CHIEDE fino a quando il contesto "
        "è sufficiente."
    ),

    "soglia_di_attivazione": {
        "descrizione": (
            "La skill valuta il contesto ricevuto "
            "su una scala 0-100. "
            "Sotto 60: la skill fa domande. "
            "60-79: la skill genera con warnings. "
            "80+: la skill genera con fiducia."
        ),
        "parametri_valutati": [
            "Chiarezza del problema (0-20 punti)",
            "Definizione target utente (0-20 punti)",
            "Tipo PRD selezionato (0-10 punti)",
            "Success metrics presenti (0-15 punti)",
            "Vincoli dichiarati (0-15 punti)",
            "Contesto tecnico (0-20 punti)"
        ]
    },

    "max_round_domande": 3,

    "regola_domande": (
        "Mai fare più di 5 domande per round. "
        "Le domande sono raggruppate per priorità. "
        "Si inizia sempre dalle domande sul problema, "
        "poi sul target, poi sul contesto tecnico."
    )
}
ROUND 1 — DOMANDE SUL PROBLEMA CORE
Questo round si attiva quando il problema non è sufficientemente chiaro.
La skill pone queste domande in ordine di priorità:

Markdown

## ROUND 1: CAPIRE IL PROBLEMA

### DOMANDA 1.1 — Il Problema Reale
"Descrivi in 2-3 frasi il problema che questo
prodotto/feature risolve per l'utente finale.
NON descrivere la soluzione — descrivi il dolore."

Esempi di risposta INSUFFICIENTE (triggera follow-up):
- "Voglio un'app per i freelancer"
- "Un SaaS per gestire i clienti"
- "Qualcosa tipo Notion ma meglio"

Esempi di risposta SUFFICIENTE:
- "I freelancer perdono in media 4 ore a settimana
  a creare preventivi manualmente in Word/Excel.
  Spesso dimenticano di includere voci importanti,
  il che causa dispute con i clienti."

### DOMANDA 1.2 — L'Evidenza del Problema
"Hai evidenza che questo problema esiste?
(interviste utente, dati, reddit/forum,
tuo problema personale vissuto in prima persona)"

Accettabile anche: "È un problema che vivo io stesso"
Non accettabile: nessuna risposta — triggera:
"Come sai che questo è un problema reale per altri?"

### DOMANDA 1.3 — Le Soluzioni Attuali
"Come risolvono questo problema le persone oggi?
Quali tool/metodi usano già?
Perché quelle soluzioni non bastano?"

Obiettivo: capire il gap tra soluzioni esistenti
e ciò che questo prodotto deve offrire in più.

### DOMANDA 1.4 — L'Urgenza
"Perché costruire questo adesso?
Cosa cambia se non viene costruito nei prossimi 3 mesi?"

Obiettivo: verificare che ci sia urgenza reale
e non solo una buona idea senza contesto di mercato.

### DOMANDA 1.5 — Il Risultato Desiderato
"Descrivi come appare la vita dell'utente DOPO
aver usato questo prodotto per 30 giorni.
Cosa fa diversamente? Cosa risparmia? Cosa guadagna?"

Obiettivo: ancorare il PRD al beneficio,
non alla feature.
ROUND 2 — DOMANDE SUL TARGET UTENTE
Markdown

## ROUND 2: DEFINIRE IL TARGET

### DOMANDA 2.1 — La Persona Primaria
"Descrivi il tuo utente ideale in modo specifico:
- Età approssimativa
- Ruolo/professione
- Contesto lavorativo (da solo, team piccolo, azienda)
- Livello tecnico (non tecnico / medio / developer)
- Dove si trova di solito quando usa il prodotto"

Il target NON può essere generico:
❌ "Professionisti che lavorano online"
✅ "Marco, 32 anni, web designer freelance
    che lavora da casa o da bar/coworking,
    non tecnico in senso stretto ma
    a suo agio con tool SaaS,
    ha 3-8 clienti attivi in contemporanea"

### DOMANDA 2.2 — Il Job-To-Be-Done
"Quando il tuo utente usa questo prodotto,
qual è il compito specifico che vuole completare?
Completa questa frase:
'Quando [situazione], voglio [azione]
in modo da [beneficio].'"

Esempio compilato:
"Quando devo mandare un preventivo a un nuovo cliente,
voglio crearlo e inviarlo in meno di 10 minuti
in modo da sembrare professionale senza perdere ore."

### DOMANDA 2.3 — Il Livello Tecnico
"Quanto è tecnico il tuo utente target?
Questo impatta direttamente la UX del prodotto."

Opzioni:
A) Non tecnico — non sa cosa sia un API, vuole click e risultati
B) Semi-tecnico — usa tool SaaS, capisce concetti base
C) Tecnico — developer, sa leggere documentazione, usa CLI
D) Misto — il prodotto ha sia utenti A che C (es: SaaS con admin panel)

### DOMANDA 2.4 — Il Budget e la Disponibilità a Pagare
"Il tuo target è disposto a pagare per risolvere
questo problema? Quanto?
Hanno già un budget dedicato a tool SaaS?
Usano già strumenti a pagamento simili?"

Obiettivo: definire il pricing tier realistico
che apparirà nel PRD.

### DOMANDA 2.5 — Le Persone Secondarie (se esistono)
"Ci sono altre persone che interagiscono
con il prodotto oltre all'utente primario?
(es: il cliente che riceve il preventivo,
l'admin che gestisce il team, il revisore)"

Obiettivo: identificare tutti gli attori
che appaiono nei user flow.
ROUND 3 — DOMANDE SUL CONTESTO TECNICO E OPERATIVO
Markdown

## ROUND 3: CONTESTO TECNICO E VINCOLI

### DOMANDA 3.1 — Il Tipo di PRD e il Contesto di Sviluppo
"Come verrà costruito questo prodotto?

A) Vibecoding con AI (Cursor, Claude, Bolt, Lovable)
   → Il PRD sarà in Markdown ottimizzato per LLM
B) Developer umano (freelancer o team)
   → Il PRD sarà strutturato per review umana
C) Misto (AI per scaffolding, umani per logica complessa)
   → PRD ibrido
D) Agency client delivery
   → PRD formale con executive summary"

### DOMANDA 3.2 — Il Tech Stack
"Hai già scelto le tecnologie?
Se sì, elencale. Se no, ho bisogno di sapere:
- Hai vincoli (es: devo usare solo JavaScript)
- Hai preferenze (preferisco Python al backend)
- O vuoi che il PRD includa raccomandazioni stack?"

Componenti da specificare:
1. Frontend framework
2. Backend framework/runtime
3. Database
4. Autenticazione
5. Pagamenti (se applicabile)
6. Hosting target
7. Layer AI (se il prodotto usa AI)
8. Librerie UI (Tailwind, shadcn, Material UI...)

### DOMANDA 3.3 — Il Time-Box / Appetite
"Quanto tempo hai per costruire questo?
Questa è la domanda più importante per definire
lo scope dell'MVP.

Risposta in formato:
- X settimane di sviluppo
- X giorni per l'MVP
- X sprint da Y giorni"

Se non sa: "Stima quanto tempo vorresti
spendere prima di avere qualcosa da mostrare a utenti reali."

### DOMANDA 3.4 — I Vincoli Non Negoziabili
"Elenca tutto ciò che NON può cambiare:
- Budget massimo
- Deadline fissa (lancio, demo, pitch)
- Integrazioni obbligatorie (es: deve parlare con Stripe)
- Piattaforme da supportare (web only? iOS? Android?)
- Compliance richiesta (GDPR, settore regolamentato)"

### DOMANDA 3.5 — L'Esistente (solo per feature su prodotto esistente)
"Stai aggiungendo una feature a un prodotto
già esistente?
Se sì:
- Quanti utenti attivi ha il prodotto?
- Quali sono i rischi di rompere qualcosa di esistente?
- C'è una base di dati già popolata da migrare?
- Gli utenti esistenti devono essere migrati
  automaticamente alla nuova feature?"
⚙️ MOTORE 2 — CONTEXT ENRICHMENT ENGINE
Come la Skill Arricchisce il Contesto Prima di Generare
Dopo l'intake, la skill non genera subito il PRD.
Prima esegue il Context Enrichment: inferisce, completa e struttura
le informazioni raccolte per riempire i gap inevitabili.

Python

ENRICHMENT_ENGINE = {

    "processo": [
        "STEP 1 — Inferenza delle Personas",
        "STEP 2 — Derivazione dei User Flow",
        "STEP 3 — Identificazione Edge Cases",
        "STEP 4 — Costruzione Success Metrics",
        "STEP 5 — Generazione Non-Goals"
    ],

    "regola_fondamentale": (
        "Ogni informazione inferita deve essere "
        "marcata con [INFERITO — VERIFICA]. "
        "Il PM che usa la skill deve confermare "
        "o correggere ogni elemento inferito "
        "prima dell'approvazione finale del PRD."
    ),

    "output_enrichment": (
        "Un documento intermedio di 1 pagina "
        "che riassume: "
        "1. Cosa è stato dichiarato dall'utente "
        "2. Cosa è stato inferito dalla skill "
        "3. Cosa rimane come open question "
        "Prima di procedere alla generazione."
    )
}
STEP 1 — Inferenza delle Personas
Markdown

## COME LA SKILL COSTRUISCE LA PERSONA

Dato l'input dell'utente, la skill costruisce
una persona strutturata secondo questo template:

---
### 👤 PERSONA PRIMARIA: [Nome inventato — es. "Marco"]

**Ruolo**: [Derivato dall'input]
**Età**: [Estimata dal contesto]
**Contesto**: [Dove e quando usa il prodotto]
**Livello tecnico**: [A/B/C/D]
**Obiettivo primario**: [Job-to-be-done]
**Frustrazioni attuali**: [Pain point dichiarati]
**Tool che usa già**: [Inferiti dal contesto]
**Disponibilità a pagare**: [Stimata]
**Quote rappresentativa**: "[Frase che potrebbe dire]"

**Jobs-To-Be-Done**:
- Quando [situazione], voglio [azione] in modo da [beneficio]
- Quando [situazione 2], voglio [azione 2] in modo da [beneficio 2]

[INFERITO — VERIFICA]: Tutti gli elementi marcati
devono essere confermati dal PM prima del sign-off
---
STEP 2 — Derivazione dei User Flow
Markdown

## COME LA SKILL COSTRUISCE I USER FLOW

La skill NON usa wireframe.
Costruisce user flow testuali step-by-step
per ogni percorso critico del prodotto.

### TEMPLATE USER FLOW

---
## FLOW [N]: [Nome del Flow]
**Attore**: [Persona]
**Trigger**: [Cosa scatena questo flow]
**Pre-condizione**: [Cosa deve essere vero prima]
**Post-condizione**: [Cosa è vero dopo il completamento]

### HAPPY PATH (percorso ideale)
1. L'utente [azione] → Sistema [risposta] → UI [mostra]
2. L'utente [azione] → Sistema [risposta] → UI [mostra]
3. ...
N. Flow completato → [Risultato finale]

### ALTERNATIVE PATH (percorsi validi ma non ideali)
- Se [condizione alternativa]: [percorso alternativo]

### ERROR PATH (percorsi di errore)
- Se [errore X]: Sistema mostra [messaggio specifico]
  + [Azione suggerita all'utente]
- Se [errore Y]: Sistema [comportamento] + [recovery]

### EDGE CASES
- [Edge case 1]: [Comportamento atteso]
- [Edge case 2]: [Comportamento atteso]
---
STEP 3 — Identificazione Automatica degli Edge Cases
Python

EDGE_CASES_MATRIX = {

    "categorie": {

        "EMPTY_STATE": {
            "trigger": "Feature che mostra lista/dati",
            "domanda": "Cosa vede l'utente se non ha ancora dati?",
            "esempio": (
                "Dashboard preventivi senza preventivi creati: "
                "Mostra illustrazione + CTA primaria "
                "'Crea il tuo primo preventivo'"
            )
        },

        "LOADING_STATE": {
            "trigger": "Qualsiasi operazione asincrona",
            "domanda": "Cosa vede l'utente mentre aspetta?",
            "opzioni": [
                "Skeleton screen (raccomandato per liste)",
                "Spinner (per operazioni brevi <2s)",
                "Progress bar (per upload/elaborazioni lunghe)",
                "Nessun feedback (VIETATO)"
            ]
        },

        "ERROR_STATE": {
            "trigger": "Qualsiasi chiamata API o operazione",
            "regola": (
                "Ogni error state DEVE contenere: "
                "1. Cosa è successo (plain language) "
                "2. Perché è successo (se utile all'utente) "
                "3. Cosa può fare l'utente adesso "
                "4. Come contattare supporto (se grave)"
            ),
            "esempi": {
                "network_error": (
                    "'Connessione persa. "
                    "I tuoi dati sono stati salvati. "
                    "Controlla la connessione e riprova.' "
                    "+ [Bottone: Riprova]"
                ),
                "validation_error": (
                    "Inline sotto il campo: "
                    "'Inserisci un indirizzo email valido'"
                ),
                "server_error": (
                    "'Qualcosa è andato storto da parte nostra. "
                    "Stiamo lavorando per risolvere. "
                    "Riprova tra qualche minuto.' "
                    "+ [Bottone: Vai alla home]"
                )
            }
        },

        "PERMISSION_DENIED": {
            "trigger": "Feature gating, ruoli, piani diversi",
            "comportamento": [
                "Non nascondere la feature (mostra locked state)",
                "Spiega perché è bloccata",
                "Mostra come sbloccarla (upgrade, richiedi accesso)"
            ]
        },

        "RATE_LIMIT": {
            "trigger": "Feature con limiti per piano",
            "comportamento": (
                "Mostra contatore rimasto + "
                "messaggio di upgrade quando raggiunto limite. "
                "Non bloccare senza spiegazione."
            )
        },

        "CONCURRENT_SESSIONS": {
            "trigger": "Multi-tenant SaaS con team",
            "domanda": (
                "Cosa succede se due utenti modificano "
                "lo stesso documento contemporaneamente?"
            )
        },

        "DATA_MIGRATION": {
            "trigger": "Feature su prodotto esistente con dati",
            "domanda": (
                "Gli utenti esistenti vengono migrati "
                "automaticamente? Con quale logica?"
            )
        },

        "OFFLINE": {
            "trigger": "App mobile o PWA",
            "domanda": (
                "Quali funzionalità devono funzionare offline? "
                "Come si sincronizzano i dati al rientro online?"
            )
        }
    }
}
STEP 4 — Costruzione delle Success Metrics
Markdown

## COME LA SKILL COSTRUISCE LE METRICHE

Dato il prodotto e il problema, la skill genera
una proposta di metriche secondo questa struttura:

---
## 📊 SUCCESS METRICS — [Nome Prodotto/Feature]

### 🎯 North Star Metric (1 sola)
→ [Metrica] — Target: [valore] — Baseline: [valore attuale o "da stabilire"]
→ Misurata con: [tool] — Frequenza review: [settimanale/mensile]

### 📈 Primary Metrics (max 3)
1. [Metrica] — Target: [valore] — Perché: [collegamento al problema]
2. [Metrica] — Target: [valore] — Perché: [collegamento al problema]
3. [Metrica] — Target: [valore] — Perché: [collegamento al problema]

### 🛡️ Guardrail Metrics (cosa NON deve peggiorare)
1. [Metrica] — Soglia: [valore massimo/minimo accettabile]
2. [Metrica] — Soglia: [valore massimo/minimo accettabile]

### 📏 How We Measure
| Metrica | Tool | Evento/Query | Frequenza |
|---------|------|-------------|-----------|
| [M1]    | [T1] | [E1]        | [F1]      |
| [M2]    | [T2] | [E2]        | [F2]      |

### ⚡ Analytics Events da Implementare
evento: [nome_evento]
  proprietà: {user_id, [prop2], [prop3]}
  quando: [trigger]
  perché: [metrica che alimenta]
---

[INFERITO — VERIFICA]: La skill propone queste metriche
sulla base del contesto. Il PM deve validare i target.
STEP 5 — Generazione dei Non-Goals
Markdown

## COME LA SKILL GENERA I NON-GOALS

Per ogni feature IN-SCOPE, la skill inferisce
almeno un elemento OUT-OF-SCOPE correlato.

Logica di inferenza:
- Feature di autenticazione → non include SSO/SAML (v2)
- Dashboard base → non include export avanzato (v2)
- Piano free → non include feature enterprise (v3)
- Web app → non include app mobile (dopo PMF)
- MVP → non include integrazioni (dopo validazione)

---
## ❌ NON-GOALS — [Nome Prodotto] v1

Le seguenti funzionalità sono ESPLICITAMENTE escluse
da questa release. Non verranno discusse durante
lo sviluppo. Verranno rivalutate nella roadmap futura.

### Out of Scope per v1:
- [ ] [Feature X] → Motivazione: [perché no ora]
  Rivalutata in: [v2 / Q2 / dopo PMF]

- [ ] [Feature Y] → Motivazione: [perché no ora]
  Rivalutata in: [v2 / Q2 / dopo PMF]

- [ ] [Feature Z] → Motivazione: [perché no ora]
  Rivalutata in: [v2 / Q2 / dopo PMF]

### Decisioni Tecniche Non Incluse:
- [ ] [Scelta tecnica X] → Gestita nel TDD separato
- [ ] [Ottimizzazione Y] → Backlog tecnico

### Cosa NON è Questo Prodotto:
- NON è [competitor A]: differenziazione chiave è [X]
- NON è per [segmento errato]: il target è solo [target giusto]
---
⚙️ MOTORE 3 — GENERATION ENGINE
Il Sistema di Costruzione del PRD Sezione per Sezione
ARCHITETTURA DELLE SEZIONI PER TIPO DI PRD
Python

PRD_SECTIONS_BY_TYPE = {

    "A_ENTERPRISE": {
        "sezioni": [
            "00_header_e_change_log",
            "01_executive_summary",
            "02_problem_statement",
            "03_obiettivi_e_success_metrics",
            "04_target_users_e_personas",
            "05_user_stories_e_acceptance_criteria",
            "06_requisiti_funzionali",
            "07_requisiti_non_funzionali",
            "08_user_flows_e_edge_cases",
            "09_permissions_e_roles_matrix",
            "10_analytics_e_tracking_spec",
            "11_scope_in_out",
            "12_assumptions_dependencies_constraints",
            "13_timeline_e_milestones",
            "14_rischi_e_mitigazioni",
            "15_migration_e_rollout_plan",
            "16_open_questions",
            "17_appendix"
        ],
        "lunghezza_target": "10-20 pagine",
        "formato": "Markdown strutturato"
    },

    "B_MVP_LEAN": {
        "sezioni": [
            "00_header",
            "01_tldr_one_liner",
            "02_problem_statement",
            "03_target_persona_primaria",
            "04_core_user_stories",
            "05_success_metrics",
            "06_scope_in_out_e_non_goals",
            "07_requisiti_tecnici_base",
            "08_edge_cases_critici",
            "09_open_questions",
            "10_timeline"
        ],
        "lunghezza_target": "3-5 pagine",
        "formato": "Markdown snello"
    },

    "C_FEATURE_SPEC": {
        "sezioni": [
            "00_header",
            "01_tldr",
            "02_contesto_prodotto_esistente",
            "03_problema_specifico_e_evidenza",
            "04_user_stories_con_acceptance_criteria",
            "05_scope_e_non_goals",
            "06_edge_cases_e_error_states",
            "07_impatto_su_feature_esistenti",
            "08_analytics_events",
            "09_rollout_e_rollback",
            "10_open_questions"
        ],
        "lunghezza_target": "2-4 pagine",
        "formato": "Markdown compatto"
    },

    "D_VIBECODING": {
        "sezioni": [
            "00_header_markdown",
            "01_product_overview",
            "02_tech_stack_vincolante",
            "03_target_utente",
            "04_core_features_per_fase",
            "05_user_flows_testuali",
            "06_schema_database_outline",
            "07_api_endpoints_outline",
            "08_edge_cases_e_error_states",
            "09_acceptance_criteria_per_feature",
            "10_ai_constraints",
            "11_fase_breakdown",
            "12_open_questions"
        ],
        "lunghezza_target": "3-6 pagine",
        "formato": "Markdown ottimizzato per LLM"
    },

    "E_PR_FAQ_AMAZON": {
        "sezioni": [
            "01_press_release_simulato",
            "02_faq_customer_facing",
            "03_faq_interne",
            "04_success_metrics_chiave",
            "05_next_steps"
        ],
        "lunghezza_target": "1-2 pagine",
        "formato": "Narrativo + Q&A"
    }
}
TEMPLATE COMPLETO TIPO B — PRD MVP LEAN
(Il più usato — mostro questo come riferimento master)
Markdown

---
# PRD: [NOME PRODOTTO/FEATURE]
**Versione**: 1.0 | **Status**: DRAFT 🔴
**Autore**: [Nome] | **Data**: GG/MM/AAAA
**Ultima modifica**: GG/MM/AAAA
**Revisori**: [Nome Engineering Lead], [Nome Design]
---

## 📋 CHANGE LOG
| Versione | Data | Autore | Modifica | Motivo |
|----------|------|--------|----------|--------|
| 1.0 | GG/MM | [Nome] | Draft iniziale | — |

---

## ⚡ TL;DR
> **Una frase**: [Cosa è, per chi è, quale problema risolve]
>
> **Il problema**: [Dato/evidenza del problema in 1 riga]
> **La soluzione**: [Approccio in 1 riga]
> **Metrica target**: [North Star Metric + target numerico]
> **Time-box**: [X settimane / X sprint]

---

## 🎯 PROBLEM STATEMENT

### Il Problema
[Descrizione del problema in 3-5 frasi.
Deve rispondere a:
- Chi lo ha? (con dato quantitativo se disponibile)
- Quanto costa non risolverlo?
- Perché le soluzioni attuali non bastano?]

### Evidenza
- [Dato 1: es. "Il 67% degli utenti abbandona dopo il primo login"]
- [Dato 2: es. "8/12 intervistati hanno menzionato X come pain point"]
- [Dato 3: es. "Competitor Y risolve solo parzialmente con Z"]

### Contesto di Mercato
[Opzionale — 2-3 righe su trend di mercato rilevanti
o posizionamento competitivo]

---

## 👤 TARGET UTENTE

### Persona Primaria: [Nome]
**Ruolo**: [es. Freelance web designer]
**Età**: [es. 28-38 anni]
**Contesto**: [es. Lavora da solo, 3-8 clienti attivi]
**Livello tecnico**: [es. Semi-tecnico — usa SaaS, non sa programmare]
**Obiettivo primario**: [es. Inviare preventivi professionali velocemente]
**Frustrazione principale**: [es. Crea preventivi in Word, ci vuole 1 ora]

**Jobs-To-Be-Done**:
> "Quando devo inviare un preventivo a un nuovo cliente,
> voglio crearlo e inviarlo in meno di 10 minuti
> in modo da sembrare professionale senza perdere tempo."

**Quote rappresentativa**:
> "[Frase che questa persona potrebbe dire letteralmente]"

### Persona Secondaria: [Nome] *(se applicabile)*
[Descrizione breve — max 3 righe]

---

## 📊 SUCCESS METRICS

### 🎯 North Star Metric
**[Metrica]**: Target [valore] entro [timeframe]
*Baseline attuale*: [valore o "non misurato"]
*Misurata con*: [tool]

### 📈 Primary Metrics
| Metrica | Baseline | Target | Timeframe | Tool |
|---------|----------|--------|-----------|------|
| [M1]    | [V1]     | [T1]   | [TF1]     | [TS1] |
| [M2]    | [V2]     | [T2]   | [TF2]     | [TS2] |
| [M3]    | [V3]     | [T3]   | [TF3]     | [TS3] |

### 🛡️ Guardrail Metrics
*(Cosa NON deve peggiorare)*
- **[Metrica]**: deve restare ≥/≤ [soglia]
- **[Metrica]**: deve restare ≥/≤ [soglia]

---

## 📖 CORE USER STORIES

### EPIC 1: [Nome Epic]

---
#### US-001: [Titolo Story]
**Come** [tipo utente],
**voglio** [azione],
**in modo da** [beneficio].

**Acceptance Criteria**:
- [ ] ✅ PASSA SE: [condizione misurabile 1]
- [ ] ✅ PASSA SE: [condizione misurabile 2]
- [ ] ✅ PASSA SE: [condizione misurabile 3]
- [ ] ❌ FALLISCE SE: [condizione di fallimento]

**Priority**: P0 / P1 / P2
**Effort stimato**: [XS / S / M / L / XL]
**Note tecniche**: [Vincoli o considerazioni per engineering]

---

#### US-002: [Titolo Story]
**Come** [tipo utente],
**voglio** [azione],
**in modo da** [beneficio].

**Acceptance Criteria**:
- [ ] ✅ PASSA SE: [condizione misurabile 1]
- [ ] ✅ PASSA SE: [condizione misurabile 2]
- [ ] ❌ FALLISCE SE: [condizione di fallimento]

**Priority**: P0 / P1 / P2
**Effort stimato**: [XS / S / M / L / XL]

---

### EPIC 2: [Nome Epic]
[Stessa struttura]

---

## ✅ SCOPE: IN / OUT

### ✅ IN SCOPE — v1
- [Feature/comportamento incluso 1]
- [Feature/comportamento incluso 2]
- [Feature/comportamento incluso 3]

### ❌ OUT OF SCOPE — v1 (Non negoziabile)
| Feature Esclusa | Motivazione | Quando Rivalutare |
|-----------------|-------------|-------------------|
| [Feature X]     | [Motivo]    | [v2 / Q3 / post-PMF] |
| [Feature Y]     | [Motivo]    | [v2 / Q3 / post-PMF] |
| [Feature Z]     | [Motivo]    | [v2 / Q3 / post-PMF] |

---

## 🔄 USER FLOWS

### FLOW 1: [Nome — es. "Registrazione e Onboarding"]
**Attore**: [Persona primaria]
**Trigger**: [Cosa avvia il flow]
**Pre-condizione**: [Cosa è vero prima]

**Happy Path**:
```
1. Utente [azione] → Sistema [response] → UI [mostra]
2. Utente [azione] → Sistema [response] → UI [mostra]
3. Utente [azione] → Sistema [response] → UI [mostra]
N. → [Risultato finale]
```

**Error Paths**:
- Se [errore]: sistema mostra "[messaggio specifico]" + [CTA recovery]
- Se [errore]: sistema mostra "[messaggio specifico]" + [CTA recovery]

**Edge Cases**:
- [Edge case 1]: [Comportamento atteso]
- [Edge case 2]: [Comportamento atteso]

---

### FLOW 2: [Nome]
[Stessa struttura]

---

## ⚠️ EDGE CASES & ERROR STATES

### Empty States
| Schermata | Trigger | Cosa Mostra | CTA |
|-----------|---------|-------------|-----|
| [Screen 1] | [Trigger] | [Contenuto] | [Azione] |
| [Screen 2] | [Trigger] | [Contenuto] | [Azione] |

### Error States
| Errore | Messaggio Mostrato | Azione Suggerita |
|--------|-------------------|------------------|
| Network error | "[Testo specifico]" | [Bottone/link] |
| Validation error | "[Testo specifico]" | [Inline fix] |
| Server error | "[Testo specifico]" | [Recovery path] |
| Auth expired | "[Testo specifico]" | [Re-login flow] |

### Loading States
| Operazione | Durata Stimata | Feedback Visivo |
|------------|----------------|-----------------|
| [Op 1]     | <1s            | Spinner inline  |
| [Op 2]     | 1-3s           | Skeleton screen |
| [Op 3]     | >3s            | Progress bar + messaggio |

---

## ⚡ REQUISITI TECNICI (Livello PRD)

### Tech Stack
```
Frontend:  [es. Next.js 14 + TypeScript + Tailwind CSS]
Backend:   [es. Node.js + Express / Supabase Edge Functions]
Database:  [es. PostgreSQL su Supabase con RLS]
Auth:      [es. Supabase Auth — email/password + Google OAuth]
Payments:  [es. Stripe — subscription + one-time]
Hosting:   [es. Vercel (frontend) + Railway (backend)]
Analytics: [es. PostHog self-hosted]
Errors:    [es. Sentry]
```

### Requisiti Non-Funzionali
| Categoria | Requisito | Metrica |
|-----------|-----------|---------|
| Performance | Page load | ≤ 2s P95 su 4G |
| Performance | API response | ≤ 300ms P95 |
| Uptime | Availability | ≥ 99.5% mensile |
| Security | Auth | JWT con refresh token rotation |
| Security | Data | Crittografia AES-256 at rest |
| Accessibilità | Standard | WCAG 2.1 Level AA |
| Compatibilità | Browser | Chrome, Firefox, Safari, Edge (ultimi 2 major) |
| Scalabilità | Utenti | Gestisce 1.000 utenti senza degradazione |

---

## 📏 ASSUMPTIONS & DEPENDENCIES

### Assunzioni
- [ ] [Assunzione 1 — es. "Gli utenti hanno già un account email"]
- [ ] [Assunzione 2 — es. "Il 60%+ degli utenti accede da desktop"]
- [ ] [Assunzione 3 — es. "Stripe è disponibile in tutti i mercati target"]

### Dipendenze Esterne
| Dipendenza | Owner | Data Needed | Status |
|------------|-------|-------------|--------|
| [API X]    | [Team] | [Data]     | 🟢 Ready |
| [Service Y]| [Team] | [Data]     | 🟡 In progress |
| [Tool Z]   | [Team] | [Data]     | 🔴 Blocked |

### Vincoli
- **Budget**: [€ o "non definito"]
- **Deadline**: [Data o "time-box di X settimane"]
- **Team**: [N dev + N designer o "solo"]
- **Tecnici**: [Vincoli architetturali esistenti]

---

## ⏱️ TIMELINE & MILESTONES

| Milestone | Descrizione | Data Target | Owner | Status |
|-----------|-------------|-------------|-------|--------|
| M1 | PRD approvato | [Data] | PM | 🔴 |
| M2 | Design completato | [Data] | Design | 🔴 |
| M3 | Fase 1 sviluppata | [Data] | Engineering | 🔴 |
| M4 | Testing interno | [Data] | QA | 🔴 |
| M5 | Beta launch | [Data] | PM | 🔴 |
| M6 | Full launch | [Data] | PM | 🔴 |

---

## ❓ OPEN QUESTIONS

| # | Domanda | Owner | Deadline | Status |
|---|---------|-------|----------|--------|
| 1 | [Domanda aperta 1] | [Nome] | [Data] | 🔴 Open |
| 2 | [Domanda aperta 2] | [Nome] | [Data] | 🟡 In review |
| 3 | [Domanda aperta 3] | [Nome] | [Data] | 🟢 Resolved |

---

*Fine PRD v1.0 — Aggiorna questo documento ad ogni sprint.
Ogni modifica richiede aggiornamento del change log.*
TEMPLATE TIPO D — PRD VIBECODING (AI-Ready Markdown)
Markdown

---
# PRD: [NOME PRODOTTO]
**File**: /docs/PRD.md
**Versione**: 1.0
**Contesto**: Questo file è il documento di riferimento
per lo sviluppo assistito da AI. Leggilo prima di
ogni sessione di sviluppo.
---

## 🧠 PRODUCT OVERVIEW

**Cosa è**: [Descrizione in 2-3 frasi plain language]
**Per chi è**: [Persona target in 1 frase]
**Problema risolto**: [Il problema in 1 frase]
**Come funziona** (ad alto livello):
1. L'utente [step 1]
2. Il sistema [step 2]
3. L'utente ottiene [risultato]

---

## 🔧 TECH STACK VINCOLANTE

```
⚠️ IMPORTANTE: Non deviare da questo stack senza approvazione.
Se noti un problema con queste scelte, segnalalo
prima di procedere con un'alternativa.

FRONTEND:
- Framework: Next.js 14 (App Router)
- Linguaggio: TypeScript (strict mode)
- Styling: Tailwind CSS + shadcn/ui
- State management: Zustand
- Forms: React Hook Form + Zod

BACKEND:
- Runtime: Node.js 20
- Framework: [Supabase Edge Functions / Express]
- API style: REST [o tRPC se specificato]

DATABASE:
- Provider: Supabase (PostgreSQL)
- ORM: Prisma
- Migrations: Prisma Migrate
- RLS: Abilitato — ogni query usa il tenant_id dell'utente

AUTH:
- Provider: Supabase Auth
- Metodi: Email/Password + Google OAuth
- Session: JWT con refresh token rotation

PAYMENTS:
- Provider: Stripe
- Prodotti: [Subscription mensile / annuale]
- Webhook: /api/webhooks/stripe (gestisci tutti gli eventi)

HOSTING:
- Frontend: Vercel
- Backend: [Railway / Supabase]
- CDN: Vercel Edge Network

MONITORING:
- Errors: Sentry (frontend + backend)
- Analytics: PostHog
- Logs: [Vercel Logs / Logtail]
```

---

## 🎯 CORE FEATURES — ORGANIZZATE PER FASE

### ⚡ FASE 1: [Nome Fase — es. "Auth + Setup"]
**Durata**: [es. Giorni 1-3]
**Obiettivo**: [Cosa deve funzionare al termine di questa fase]

#### Feature 1.1: [Nome]
**Descrizione**: [Cosa fa in plain language]
**User Flow**:
```
1. Utente va a [URL/schermata]
2. Utente fa [azione]
3. Sistema fa [operazione] → [response]
4. UI mostra [risultato]
5. Edge cases:
   - Se [errore]: UI mostra "[messaggio esatto]"
   - Se [timeout]: sistema [comportamento]
```
**Acceptance Criteria**:
- [ ] ✅ [Condizione testabile 1]
- [ ] ✅ [Condizione testabile 2]
- [ ] ❌ NON implementare: [cosa non fare in questa fase]

**Schema DB rilevante**:
```sql
-- Tabella: users
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email TEXT UNIQUE NOT NULL,
  name TEXT,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  -- [altre colonne specifiche]
);
```

---

#### Feature 1.2: [Nome]
[Stessa struttura]

---

### 🏗️ FASE 2: [Nome Fase — es. "Core Product"]
**Durata**: [es. Giorni 4-10]
**Prerequisito**: Fase 1 completata e testata

[Stessa struttura per ogni feature]

---

### 💳 FASE 3: [Nome Fase — es. "Payments + Onboarding"]
**Durata**: [es. Giorni 11-14]
**Prerequisito**: Fase 2 completata

[Stessa struttura]

---

## 🗄️ DATABASE SCHEMA OUTLINE

```sql
-- Schema: public
-- Nota: Tutte le tabelle multi-tenant hanno tenant_id
-- RLS Policy standard: auth.uid() = user_id

TABLE: users
  id: UUID PK
  email: TEXT UNIQUE NOT NULL
  name: TEXT
  plan: ENUM('free', 'pro', 'enterprise') DEFAULT 'free'
  stripe_customer_id: TEXT
  created_at: TIMESTAMPTZ

TABLE: [entità_core]
  id: UUID PK
  user_id: UUID FK → users.id ON DELETE CASCADE
  [campi specifici]
  created_at: TIMESTAMPTZ
  updated_at: TIMESTAMPTZ

-- RLS Policy (da applicare a ogni tabella):
-- CREATE POLICY "Users can only see their own data"
-- ON [tabella] FOR ALL
-- USING (auth.uid() = user_id);
```

---

## 🌐 API ENDPOINTS OUTLINE

```
BASE URL: /api

AUTH:
POST   /api/auth/register     → Crea account
POST   /api/auth/login        → Login
POST   /api/auth/logout       → Logout
GET    /api/auth/me           → Profilo utente

[ENTITÀ CORE]:
GET    /api/[entità]          → Lista (paginata)
POST   /api/[entità]          → Crea nuovo
GET    /api/[entità]/:id      → Singolo elemento
PUT    /api/[entità]/:id      → Aggiorna
DELETE /api/[entità]/:id      → Elimina (soft delete)

PAYMENTS:
POST   /api/payments/checkout     → Crea sessione Stripe
POST   /api/webhooks/stripe       → Webhook Stripe
GET    /api/payments/portal       → Customer portal Stripe

STANDARD RESPONSE FORMAT:
{
  "success": boolean,
  "data": object | null,
  "error": string | null,
  "meta": {
    "page": number,
    "total": number
  } | null
}
```

---

## 🔴 AI CONSTRAINTS
### Istruzioni per l'AI che usa questo PRD

```
⚠️ REGOLE OBBLIGATORIE — Non derogare senza approvazione

1. NON aggiungere feature non specificate in questo PRD
   anche se sembrano "utili" o "ovvie"

2. NON cambiare il tech stack scelto
   Se noti un problema, segnalalo PRIMA di procedere

3. NON usare librerie non elencate senza chiedere
   (es: non aggiungere Redux se non è specificato)

4. Costruisci UNA FASE ALLA VOLTA
   Non passare alla Fase 2 prima che la Fase 1 sia testata

5. Per ogni feature, scrivi i test prima del codice
   (acceptance criteria = test cases)

6. Se qualcosa nel PRD è ambiguo, CHIEDI
   Non inventare interpretazioni

7. Ogni componente UI usa shadcn/ui se disponibile
   Non creare componenti custom se shadcn ha l'equivalente

8. Tutto il codice deve essere TypeScript strict
   No any, no unknown senza type guard

9. Gestisci SEMPRE gli error states
   Non lasciare mai un catch vuoto o un generico "something went wrong"

10. Documenta ogni funzione non ovvia
    con JSDoc comment
```

---

## ❓ OPEN QUESTIONS

| # | Domanda | Priorità | Status |
|---|---------|----------|--------|
| 1 | [Domanda tecnica aperta] | Alta | 🔴 |
| 2 | [Decisione di design] | Media | 🔴 |
| 3 | [Scelta di business] | Bassa | 🟡 |

---
*Questo file è il source of truth del progetto.*
*Aggiornalo dopo ogni decisione importante.*
*Versione corrente: 1.0 — [Data]*
⚙️ MOTORE 4 — VALIDATION ENGINE
Il Sistema di Validazione Prima dell'Output Finale
Prima di consegnare qualsiasi PRD, la skill esegue
una validazione automatica in 3 livelli.

Python

VALIDATION_ENGINE = {

    "LIVELLO_1_STRUTTURA": {
        "descrizione": "Verifica che tutte le sezioni obbligatorie siano presenti",
        "checks": [
            "Header con versione e status presente",
            "Problem statement non è una lista di feature",
            "Almeno 1 persona definita con JTBD",
            "North Star Metric con numero specifico",
            "Almeno 3 user stories con acceptance criteria",
            "Non-goals presenti e non vuoti",
            "Open questions presenti (anche se 0)"
        ]
    },

    "LIVELLO_2_QUALITA": {
        "descrizione": "Verifica la qualità del contenuto",
        "checks": [
            {
                "check": "Problem-First Verification",
                "regola": (
                    "Il problem statement NON inizia con "
                    "'Voglio costruire' o 'Ho bisogno di'. "
                    "Deve iniziare con il dolore dell'utente."
                )
            },
            {
                "check": "Metrics Specificity Check",
                "regola": (
                    "Ogni metrica ha un numero target. "
                    "NON accettabile: 'aumentare la retention'. "
                    "ACCETTABILE: 'aumentare la D7 retention "
                    "dal 23% al 40% entro 60 giorni dal lancio'."
                )
            },
            {
                "check": "Acceptance Criteria Testability",
                "regola": (
                    "Ogni acceptance criteria può essere "
                    "verificata da un QA engineer senza "
                    "chiedere interpretazioni. "
                    "NON accettabile: 'il sistema funziona bene'. "
                    "ACCETTABILE: 'il form si invia in <2s "
                    "e l'utente vede il messaggio di successo'."
                )
            },
            {
                "check": "Edge Cases Coverage",
                "regola": (
                    "Per ogni feature con input utente, "
                    "esiste almeno 1 error state documentato. "
                    "Per ogni lista, esiste l'empty state."
                )
            },
            {
                "check": "Non-Goals Specificity",
                "regola": (
                    "I non-goals non possono essere generici. "
                    "NON accettabile: 'funzionalità avanzate'. "
                    "ACCETTABILE: 'firma digitale del preventivo (v2)'."
                )
            }
        ]
    },

    "LIVELLO_3_CONSISTENZA": {
        "descrizione": "Verifica la consistenza interna del documento",
        "checks": [
            "Le user stories sono consistenti con le personas definite",
            "Le metriche sono collegabili alle user stories",
            "Il tech stack è consistente con i requisiti non-funzionali",
            "Il timeline è realistico rispetto al team dichiarato",
            "Le dipendenze hanno date di disponibilità definite"
        ]
    },

    "output_validation": {
        "formato": """
## 🔍 VALIDATION REPORT

### ✅ Checks Passati
- [Lista di check superati]

### ⚠️ Warnings (da risolvere prima dell'approvazione)
- [Warning 1]: [Descrizione] → [Azione suggerita]
- [Warning 2]: [Descrizione] → [Azione suggerita]

### 🔴 Blockers (il PRD non può essere approvato)
- [Blocker 1]: [Descrizione] → [Come risolvere]

### 📊 PRD Quality Score: [X]/100
- Struttura: [X]/30
- Qualità: [X]/40
- Consistenza: [X]/30
        """
    }
}
---

## 📌 PANORAMICA DELLE VARIANTI

Questa parte contiene **4 esempi completamente compilati**
di PRD reali pronti all'uso come reference master.

Ogni esempio è:
- Compilato con dati realistici (non placeholder vuoti)
- Utilizzabile come template diretto
- Commentato con note operative

---

## 🔵 ESEMPIO 1 — PRD MVP LEAN (Tipo B)
### Prodotto: "QuickInvoice" — SaaS per preventivi freelance

---

````markdown
---
# PRD: QuickInvoice — MVP v1
**Versione**: 1.2 | **Status**: APPROVED ✅
**Autore**: [PM] | **Data creazione**: 10/01/2025
**Ultima modifica**: 18/01/2025
**Revisori**: [Lead Dev], [UI Designer]
**Time-box**: 3 settimane (21 giorni)
---

## 📋 CHANGE LOG
| Versione | Data | Autore | Modifica | Motivo |
|----------|------|--------|----------|--------|
| 1.0 | 10/01 | PM | Draft iniziale | — |
| 1.1 | 14/01 | PM | Rimossa firma digitale da scope | Troppo complessa per v1 |
| 1.2 | 18/01 | PM | Aggiunta sezione rollout | Feedback engineering |

---

## ⚡ TL;DR

> **Cosa è**: SaaS web per freelance italiani che crea e invia
> preventivi professionali in PDF in meno di 10 minuti.
>
> **Il problema**: I freelance perdono in media 3-4 ore/settimana
> a costruire preventivi manualmente in Word/Excel.
>
> **La soluzione**: Editor drag-and-drop con template pre-compilati,
> calcolo automatico IVA/ritenuta, invio PDF via email con 1 click.
>
> **North Star Metric**: 1 preventivo inviato entro 10 minuti
> dal primo accesso — target ≥ 60% degli utenti nuovi.
>
> **Time-box**: 3 settimane di sviluppo — 1 developer full-stack.

---

## 🎯 PROBLEM STATEMENT

### Il Problema

I freelance italiani (designer, copywriter, consulenti, sviluppatori)
non hanno uno strumento dedicato e semplice per creare preventivi
professionali. La soluzione più comune è un documento Word/Excel
personalizzato manualmente ogni volta.

Questo causa 3 problemi concreti:
1. **Tempo perso**: 45-90 minuti per preventivo,
   3-4 ore/settimana in media per chi ha 5+ clienti attivi
2. **Errori di calcolo**: IVA, ritenuta d'acconto, totali
   sbagliati → dispute con clienti e problemi fiscali
3. **Aspetto non professionale**: layout diverso ogni volta,
   mancanza di coerenza visiva → percezione di scarsa serietà

### Evidenza

- **Dati qualitativi**: 11/15 intervistati usano Word/Excel
  per i preventivi. Tutti lo considerano una perdita di tempo.
- **Dati quantitativi**: Su un campione di 50 freelance,
  il tempo medio per preventivo è 67 minuti.
- **Reddit r/freelance_ita**: 23 thread con "preventivo" 
  negli ultimi 6 mesi — il 78% lamenta la complessità
- **Competitor gap**: FattureInCloud e Fattura24 sono orientati
  alla fatturazione post-lavoro, non ai preventivi pre-vendita.
  L'UX è pensata per commercialisti, non per creativi.

### Perché Ora

Il mercato dei freelance italiani è cresciuto del 34% dal 2020
(fonte: Eurostat 2024). La digitalizzazione post-COVID ha
portato nuovi freelance che non hanno processi strutturati.
È il momento ideale per un tool verticale e semplice.

---

## 👤 TARGET UTENTE

### Persona Primaria: "Marco il Freelance"

**Ruolo**: Freelance creativo (web designer, copywriter,
consulente marketing, sviluppatore)
**Età**: 26-38 anni
**Contesto**: Lavora da casa o coworking, 3-8 clienti attivi,
gestisce tutto da solo senza supporto amministrativo
**Livello tecnico**: Semi-tecnico — usa Figma, Notion, Slack.
Non sa programmare. Vuole click e risultati.
**Obiettivo primario**: Inviare un preventivo professionale
velocemente senza pensarci
**Frustrazione principale**: "Ogni volta che devo fare un
preventivo perdo un'ora. E spesso mi dimentico qualcosa."
**Disponibilità a pagare**: €9-19/mese per tool che usa ogni giorno

**Jobs-To-Be-Done**:
> "Quando un cliente mi chiede un preventivo,
> voglio crearlo e mandarlo in meno di 10 minuti
> in modo da sembrare professionale senza perdere
> il pomeriggio a formattare un documento Word."

**Quote rappresentativa**:
> "Ho un template Excel che ho modificato 20 volte
> negli anni. Non è bello, faccio sempre errori con
> i calcoli dell'IVA, e ogni cliente mi dice
> 'mandami il preventivo' come se fosse semplice."

### Persona Secondaria: "Il Cliente di Marco"

**Ruolo**: Titolare PMI o marketing manager
**Interazione col prodotto**: Riceve email con PDF allegato
e link per approvare/rifiutare il preventivo online
**Cosa si aspetta**: Documento professionale, chiaro,
con totali chiari e modalità di pagamento indicate
**NON usa l'app** — vede solo l'output finale

---

## 📊 SUCCESS METRICS

### 🎯 North Star Metric
**Time-to-first-invoice**: % utenti che inviano il primo
preventivo entro 10 minuti dal signup
- **Target**: ≥ 60% entro 30 giorni dal lancio
- **Baseline**: non misurato (prodotto nuovo)
- **Misurato con**: PostHog — evento `invoice_sent`
  con property `minutes_since_signup`

### 📈 Primary Metrics

| Metrica | Baseline | Target | Timeframe | Tool |
|---------|----------|--------|-----------|------|
| D7 Retention | — | ≥ 35% | 60gg dal lancio | PostHog |
| Preventivi inviati/utente/settimana | — | ≥ 2 | 30gg dal lancio | PostHog |
| Trial → Paid conversion | — | ≥ 8% | 90gg dal lancio | Stripe |
| NPS dopo primo preventivo | — | ≥ 40 | 60gg dal lancio | Typeform |

### 🛡️ Guardrail Metrics

- **Crash rate**: deve restare ≤ 0.5% delle sessioni (Sentry)
- **Email delivery rate**: deve restare ≥ 98% (Resend dashboard)
- **Page load time**: homepage e editor ≤ 2s P95 (Vercel Analytics)

### 📊 Analytics Events Obbligatori

```javascript
// Evento: signup completato
posthog.capture('user_signed_up', {
  method: 'email' | 'google',
  plan: 'trial'
})

// Evento: preventivo creato (bozza salvata)
posthog.capture('invoice_created', {
  user_id: string,
  template_used: string | 'blank',
  items_count: number,
  has_iva: boolean,
  has_ritenuta: boolean
})

// Evento: preventivo inviato
posthog.capture('invoice_sent', {
  user_id: string,
  invoice_id: string,
  total_amount: number,
  minutes_since_signup: number,
  minutes_to_create: number,
  send_method: 'email' | 'link'
})

// Evento: upgrade a paid
posthog.capture('subscription_started', {
  user_id: string,
  plan: 'monthly' | 'annual',
  trigger: 'limit_reached' | 'voluntary' | 'trial_ended'
})
📖 CORE USER STORIES
EPIC 1: Autenticazione e Onboarding
US-001: Registrazione con Email
Come freelance che scopre QuickInvoice,
voglio creare un account con email e password
in modo da iniziare a usare il tool subito.

Acceptance Criteria:

 ✅ Form con campi: nome, email, password (min 8 char)
 ✅ Validazione inline — errori mostrati sotto il campo
senza ricaricare la pagina
 ✅ Dopo submit: redirect a /onboarding/step-1
entro 2 secondi
 ✅ Email di benvenuto inviata entro 60 secondi
 ❌ FALLISCE SE: l'utente resta sulla pagina di signup
dopo un submit corretto
 ❌ FALLISCE SE: email già registrata non mostra
il messaggio specifico: "Questa email è già in uso.
[Fai login →]"
Priority: P0
Effort: S (0.5 giorni)

US-002: Registrazione con Google OAuth
Come freelance che non vuole gestire un'altra password,
voglio accedere con il mio account Google
in modo da iniziare senza friczione.

Acceptance Criteria:

 ✅ Bottone "Continua con Google" visibile sopra il form email
 ✅ Popup Google OAuth — nessun redirect a pagina esterna
 ✅ Dopo autorizzazione: account creato o loggato
se email già esistente → redirect a /dashboard
o /onboarding/step-1 se primo accesso
 ✅ Nome e foto Google importati automaticamente
 ❌ FALLISCE SE: il popup viene bloccato senza
mostrare istruzioni alternative
Priority: P1
Effort: S (0.5 giorni)

US-003: Onboarding Wizard (3 step)
Come nuovo utente appena registrato,
voglio essere guidato nella configurazione iniziale
in modo da avere il mio profilo pronto per il primo preventivo.

Step 1 — Dati personali/azienda:

Nome completo o nome azienda
Partita IVA (opzionale ma consigliato)
Indirizzo (opzionale)
Logo upload (opzionale — max 2MB, JPG/PNG)
Step 2 — Configurazione fiscale:

Regime fiscale: Forfettario / Ordinario / Altro
IVA: 22% (default) / 10% / 4% / Esente
Ritenuta d'acconto: Sì (20%) / No
Step 3 — Primo template:

Scelta colore brand (palette di 6 colori)
Preview del template con i dati inseriti
CTA: "Crea il tuo primo preventivo →"
Acceptance Criteria:

 ✅ Ogni step è salvato in tempo reale (no perdita dati
se l'utente chiude il browser)
 ✅ L'utente può saltare step 1 e 2 con "Fai dopo →"
ma vede warning: "Il preventivo userà dati incompleti"
 ✅ Progress bar visibile in alto (Passo 1 di 3)
 ✅ Dati dell'onboarding pre-compilano il primo preventivo
 ❌ FALLISCE SE: saltando l'onboarding il primo preventivo
mostra campi vuoti senza label placeholder
Priority: P0
Effort: M (2 giorni)

EPIC 2: Creazione Preventivo
US-004: Creazione Preventivo da Template
Come freelance che deve inviare un preventivo,
voglio partire da un template pre-compilato
in modo da non dover impostare tutto da zero ogni volta.

Template disponibili in v1:

"Servizi creativi" (design, copy, foto)
"Sviluppo web" (con voci per frontend, backend, manutenzione)
"Consulenza" (con voce per ore lavoro × tariffa oraria)
"Blank" (vuoto — per utenti avanzati)
Acceptance Criteria:

 ✅ Pagina di scelta template con preview visiva
 ✅ Click su template → editor pre-compilato con voci
tipiche della categoria
 ✅ Tutte le voci sono modificabili inline (click per editare)
 ✅ Salvataggio automatico ogni 30 secondi
 ✅ Indicatore "Salvato ✓" o "Salvataggio..." visibile
 ❌ FALLISCE SE: modifiche vengono perse se l'utente
naviga via per errore senza conferma
Priority: P0
Effort: L (3 giorni)

US-005: Editor Voci Preventivo
Come freelance nell'editor,
voglio aggiungere, modificare e rimuovere voci
con quantità, prezzo unitario e descrizione
in modo da costruire un preventivo accurato.

Struttura di ogni voce:

text

[ Descrizione          ] [ Qty ] [ Prezzo ] [ Totale ]
[ Servizio di design   ] [  1  ] [ €800   ] [ €800   ] [🗑️]
Acceptance Criteria:

 ✅ "Aggiungi voce" aggiunge una riga vuota e mette
il focus sul campo descrizione
 ✅ Totale riga calcolato automaticamente (Qty × Prezzo)
 ✅ Subtotale, IVA, ritenuta e Totale finale calcolati
in tempo reale sotto la tabella
 ✅ Drag-and-drop per riordinare le voci
 ✅ Supporto per note aggiuntive (campo testo libero)
 ✅ Campo "Condizioni di pagamento" (es: "Bonifico 30gg")
 ❌ FALLISCE SE: i totali non si aggiornano
senza ricaricare la pagina
 ❌ FALLISCE SE: eliminare una voce non chiede conferma
se il campo descrizione è popolato
Priority: P0
Effort: L (3 giorni)

US-006: Preview e Invio PDF
Come freelance che ha compilato il preventivo,
voglio vedere come apparirà il PDF prima di inviarlo
e inviarlo al cliente con 1 click
in modo da essere sicuro dell'output e agire velocemente.

Acceptance Criteria:

 ✅ Bottone "Anteprima PDF" genera il PDF lato server
e lo mostra in un modal/panel (non apre nuova tab)
 ✅ Il PDF generato rispecchia esattamente la preview
 ✅ Invio via email: campo "Email cliente" + subject
pre-compilato modificabile + messaggio personalizzabile
 ✅ Email inviata entro 30 secondi dall'azione
 ✅ Stato preventivo cambia a "Inviato" con timestamp
 ✅ L'utente riceve copia in CC (opzionale, toggle)
 ❌ FALLISCE SE: il PDF ha layout rotto su qualsiasi
browser moderno (Chrome, Firefox, Safari)
 ❌ FALLISCE SE: l'email non arriva entro 2 minuti
in condizioni normali
Priority: P0
Effort: M (2 giorni)

EPIC 3: Dashboard e Gestione
US-007: Dashboard Preventivi
Come freelance che gestisce più clienti,
voglio vedere tutti i miei preventivi in un'unica vista
con il loro stato
in modo da tenere traccia di cosa è in attesa,
accettato o scaduto.

Stati del preventivo:

🟡 Bozza — creato ma non inviato
🔵 Inviato — email mandata, in attesa di risposta
🟢 Accettato — cliente ha confermato
🔴 Rifiutato — cliente ha rifiutato
⚫ Scaduto — data scadenza superata senza risposta
Acceptance Criteria:

 ✅ Vista lista con colonne: Cliente, Importo, Stato, Data
 ✅ Filtro per stato (tab o dropdown)
 ✅ Ricerca per nome cliente o importo
 ✅ Click su riga → apre dettaglio preventivo
 ✅ Empty state: se nessun preventivo, mostra
"Nessun preventivo ancora. [Crea il primo →]"
con illustrazione motivante
 ✅ Paginazione: 20 preventivi per pagina
 ❌ FALLISCE SE: lista non si aggiorna dopo
aver inviato un nuovo preventivo senza refresh manuale
Priority: P0
Effort: M (1.5 giorni)

✅ SCOPE: IN / OUT
✅ IN SCOPE — v1 (21 giorni)
Autenticazione email e Google OAuth
Onboarding wizard 3 step
4 template preventivo (3 preconfigurati + 1 blank)
Editor voci con calcolo automatico (IVA, ritenuta)
Preview PDF e invio via email
Dashboard preventivi con stati e filtri base
Piano free: max 3 preventivi/mese
Piano Pro (€12/mese): preventivi illimitati
Stripe Checkout per upgrade
❌ OUT OF SCOPE — v1 (Non negoziabile)
Feature Esclusa	Motivazione	Quando Rivalutare
Firma digitale	Complessità legale, integrazioni costose	v3 — se richiesta da >30% utenti
App mobile iOS/Android	Web-first, validare prima su desktop	Post-PMF (>1.000 utenti paganti)
Integrazione con software contabili (FIC, Fattura24)	Scope eccessivo per MVP	v2 — Q3 2025
Template marketplace / condivisione	Feature social — non core per MVP	v3
Multi-lingua preventivi	Target solo Italia per v1	v2 — se espansione EU
Reminder automatici al cliente	Nice-to-have, non essenziale	v2
Dashboard analytics revenue	Complessità alta, basso impatto v1	v2
Accesso team / multi-utente	Single user per v1	v2 — se richiesto
🔄 USER FLOWS
FLOW 1: Onboarding e Primo Preventivo (Happy Path)
Attore: Marco, freelance appena registrato
Trigger: Primo accesso dopo registrazione
Pre-condizione: Account creato, email verificata
Obiettivo: Primo preventivo inviato in <10 minuti

Happy Path:

text

1. Marco atterera su /onboarding/step-1
   Sistema mostra: form dati personali pre-compilato
   con nome da Google OAuth (se usato)

2. Marco inserisce Partita IVA e clicca "Avanti →"
   Sistema salva → mostra step-2 (configurazione fiscale)

3. Marco seleziona "Forfettario" e "Nessuna IVA"
   Sistema aggiorna preview template in real-time

4. Marco sceglie colore brand (blu) e clicca
   "Crea il tuo primo preventivo →"
   Sistema crea preventivo vuoto con template
   "Servizi creativi" → redirect a /invoices/new

5. Marco vede l'editor con 3 voci pre-compilate
   (placeholder modificabili)
   Modifica: descrizione, quantità, prezzo

6. Marco clicca "Aggiungi voce" → aggiunge 1 riga extra
   Totale si aggiorna automaticamente

7. Marco clicca "Anteprima PDF"
   Sistema genera PDF → mostra in modal laterale

8. Marco clicca "Invia al cliente"
   Sistema mostra: campo email + subject + messaggio
   Marco inserisce email cliente → clicca "Invia"

9. Sistema invia email con PDF → mostra
   "✅ Preventivo inviato a cliente@esempio.it"
   Stato preventivo diventa "Inviato"
   Redirect a /dashboard con preventivo visibile
Tempo totale previsto: 6-8 minuti per utente medio

Error Paths:

text

- Step 2: Partita IVA non valida →
  "Formato non valido. La P.IVA italiana ha 11 cifre."
  (inline, non blocca il proceed se lasciata vuota)

- Step 7: Generazione PDF fallisce →
  "Non riusciamo a generare il PDF ora.
  I tuoi dati sono salvati. Riprova tra 30 secondi."
  + [Bottone: Riprova] + [Link: Contatta supporto]

- Step 8: Email cliente non valida →
  "Inserisci un indirizzo email valido"
  (inline, focus ritorna al campo)

- Step 8: Invio email fallisce dopo 3 retry →
  "Email non inviata. Puoi scaricare il PDF
  e inviarlo manualmente."
  + [Bottone: Scarica PDF]
Edge Cases:

text

- Marco chiude il browser durante l'onboarding →
  Al prossimo login: mostra "Continua da dove hai lasciato"
  con link a step non completato

- Marco prova ad andare su /dashboard prima di completare
  l'onboarding → Redirect a /onboarding/step-corrente
  con banner: "Completa il setup per sbloccare tutte le funzioni"
  + link "Salta per ora"

- File logo > 2MB → "Il logo deve essere max 2MB.
  Il tuo file è X MB. Riduci le dimensioni e riprova."
FLOW 2: Utente Free Raggiunge Limite (Upgrade Flow)
Attore: Marco, piano free con 3 preventivi già inviati
Trigger: Clicca "Crea nuovo preventivo" (il 4°)

text

1. Marco clicca "Crea nuovo preventivo"
   Sistema controlla: utente ha 3/3 preventivi free

2. Sistema mostra modal:
   "Hai raggiunto il limite del piano gratuito.
   Con il piano Pro invii preventivi illimitati
   per soli €12/mese."
   [Upgrade a Pro] [Continua con gratuito →]

   NOTA: NON bloccare senza alternative.
   "Continua con gratuito" mostra i 3 esistenti
   e spiega che non può crearne altri.

3. Marco clicca "Upgrade a Pro"
   Sistema redirect a Stripe Checkout
   (sessione creata server-side con user_id)

4. Marco completa pagamento su Stripe
   Webhook Stripe → sistema aggiorna piano utente
   Redirect a /dashboard con banner:
   "🎉 Sei ora su QuickInvoice Pro! Crea preventivi illimitati."

5. Marco crea il 4° preventivo normalmente
⚠️ EDGE CASES & ERROR STATES COMPLETI
Empty States
Schermata	Trigger	Contenuto	CTA Primaria
Dashboard preventivi	Nessun preventivo creato	Illustrazione + "Crea il tuo primo preventivo" + testo motivante	"Crea preventivo →"
Lista clienti	Nessun cliente	"I clienti appariranno qui quando invii il primo preventivo"	"Crea preventivo →"
Risultati ricerca	Nessun match	"Nessun preventivo trovato per '[query]'"	"Cancella filtri"
Error States Completi
Errore	Contesto	Messaggio Mostrato	Azione
Network offline	Qualsiasi salvataggio	"Connessione persa. Le modifiche verranno salvate appena torni online."	Auto-retry
Sessione scaduta	Mid-flow	"La tua sessione è scaduta. Fai login per continuare — non perderai il lavoro."	[Login →]
PDF generation failed	Anteprima/invio	"Errore nella generazione del PDF. Riprova tra 30 secondi."	[Riprova]
Email bounce	Dopo invio	Email a Marco: "L'email al tuo cliente non è stata consegnata. Controlla l'indirizzo."	[Aggiorna email]
Stripe payment failed	Checkout	Gestito da Stripe Checkout — nessun custom error state richiesto in v1	—
Upload logo fallito	Onboarding	"Il file non può essere caricato. Assicurati che sia JPG/PNG max 2MB."	[Riprova]
Loading States
Operazione	Durata Stimata	Feedback Visivo
Login/Signup	<2s	Spinner sul bottone, bottone disabilitato
Salvataggio auto	<1s	Indicatore "Salvataggio..." → "Salvato ✓"
Generazione PDF	2-5s	Spinner + "Generando il PDF..."
Invio email	1-3s	Spinner + "Invio in corso..."
Caricamento dashboard	<1.5s	Skeleton screen (3 righe placeholder)
⚡ REQUISITI TECNICI
Tech Stack
text

Frontend:  Next.js 14 (App Router) + TypeScript + Tailwind CSS
UI:        shadcn/ui component library
PDF:       React-PDF / Puppeteer (server-side generation)
Backend:   Supabase (database + auth + edge functions)
Database:  PostgreSQL su Supabase con Row Level Security
Auth:      Supabase Auth (email + Google OAuth)
Email:     Resend (transactional emails)
Payments:  Stripe (Checkout + webhooks + Customer Portal)
Hosting:   Vercel (frontend + serverless)
Analytics: PostHog (eventi, funnel, retention)
Errors:    Sentry
Requisiti Non-Funzionali
Categoria	Requisito	Target
Performance	Page load (LCP)	≤ 2s su connessione 4G
Performance	API response	≤ 300ms P95
Performance	PDF generation	≤ 5s P95
Uptime	Availability	≥ 99.5% mensile
Security	RLS	Ogni query filtrata per user_id
Security	Pagamenti	PCI DSS gestito interamente da Stripe
Compatibilità	Browser	Chrome 100+, Firefox 100+, Safari 15+
Accessibilità	Standard	WCAG 2.1 Level AA per form e navigazione
Scalabilità	Utenti	Gestisce 500 utenti concorrenti senza degradazione
📏 ASSUMPTIONS & DEPENDENCIES
Assunzioni
 Gli utenti accedono principalmente da desktop (≥70%)
 La lingua dell'interfaccia è italiano (unica lingua v1)
 Stripe è disponibile per tutti i clienti target (Italia)
 Resend garantisce delivery rate ≥ 98% per email transazionali
 Supabase free tier è sufficiente per i primi 500 utenti
Dipendenze
Dipendenza	Owner	Quando Serve	Status
Supabase account setup	Dev	Giorno 1	🟢 Ready
Stripe account + prodotti configurati	PM+Dev	Giorno 14	🟡 Da fare
Resend account + dominio verificato	Dev	Giorno 7	🟡 Da fare
Template PDF design	Designer	Giorno 5	🔴 Non iniziato
Dominio e DNS	PM	Giorno 1	🟢 Ready
Vincoli
Budget: €0 tool cost per MVP (tutti free tier)
Team: 1 developer full-stack + 1 PM (part-time)
Deadline: 21 giorni dall'approvazione del PRD
Tecnici: Solo web — nessun requisito mobile in v1
⏱️ TIMELINE — 21 GIORNI
Settimana	Focus	Milestone
W1 (gg 1-7)	Auth, DB schema, onboarding wizard	M1: Utente si registra e completa onboarding
W2 (gg 8-14)	Editor preventivo, calcoli, template	M2: Preventivo creato e PDF generato
W3 (gg 15-21)	Email invio, dashboard, Stripe, bug fix	M3: Launch — utente può pagare e inviare
🚀 ROLLOUT PLAN
Fase 1 — Dogfooding (Giorni 19-20)
Solo team interno (2-3 persone)
Creazione di 5+ preventivi reali
Verifica crash rate = 0
Fase 2 — Beta chiusa (Giorno 21)
10 freelance selezionati da network personale
Onboarding assistito via WhatsApp
Raccolta feedback con form Typeform post-onboarding
Fase 3 — Launch pubblico (Giorno 28+)
Post su LinkedIn + community Freelance Italia
Product Hunt launch (se metriche beta soddisfacenti)
Go/No-go: D7 retention beta ≥ 25%
❓ OPEN QUESTIONS
#	Domanda	Owner	Deadline	Status
1	Il piano free richiede carta di credito? (riduce conversioni ma migliora qualità lead)	PM	20/01	🔴 Open
2	Supportiamo anche la ricevuta fiscale oltre al preventivo?	PM	22/01	🟡 In review
3	PDF generato server-side (Puppeteer) o client-side (React-PDF)? Trade-off: qualità vs costo	Dev	18/01	🟢 Risolto: Puppeteer server-side
4	Dominio: quickinvoice.it o quickinvoice.io?	PM	15/01	🟢 Risolto: .it
PRD v1.2 — Approvato il 18/01/2025
Prossima review: fine W1 (giorno 7)

text


---

## 🟣 ESEMPIO 2 — PRD VIBECODING (Tipo D)
### Prodotto: "FocusBoard" — Task manager con AI prioritization

````markdown
---
# PRD: FocusBoard
**File**: /docs/PRD.md — Leggi questo file all'inizio di ogni sessione
**Versione**: 1.1
**Contesto**: Sviluppo con Cursor AI + Claude Sonnet
**Time-box**: 14 giorni — 1 developer (vibe coder)
---

## 🧠 PRODUCT OVERVIEW

**Cosa è**: Web app di task management che usa AI per
suggerire automaticamente le 3 priorità del giorno
basandosi su deadline, importanza e energia disponibile.

**Per chi è**: Professionisti autonomi (freelance, founder,
consulenti) che hanno troppe cose da fare e non sanno
da dove iniziare ogni mattina.

**Problema risolto**: La "paralisi da lista infinita" —
avere 50 task ma non sapere quali fare oggi.

**Come funziona**:
1. L'utente inserisce i propri task con deadline e importanza
2. Ogni mattina, l'AI analizza la lista e suggerisce
   "Le tue 3 priorità di oggi" con spiegazione
3. L'utente lavora su quelle 3, le completa, e si sente
   finalmente in controllo

---

## 🔧 TECH STACK VINCOLANTE

```
⚠️ NON deviare da questo stack. Se hai dubbi, chiedi.

FRONTEND:
- Next.js 14 con App Router
- TypeScript (strict: true in tsconfig)
- Tailwind CSS per tutti gli stili
- shadcn/ui per TUTTI i componenti UI
  (Button, Input, Card, Dialog, etc.)
  → Non creare componenti custom se shadcn li ha già
- Lucide React per le icone (NON Font Awesome, NON Heroicons)
- React Hook Form + Zod per tutti i form

BACKEND:
- Supabase come backend completo
  (database + auth + realtime + edge functions)
- Supabase Edge Functions per logica server-side
- Row Level Security abilitato su TUTTE le tabelle
- Prisma come ORM (NON query SQL raw salvo necessità)

DATABASE:
- PostgreSQL via Supabase
- Ogni tabella ha: id (UUID), user_id (UUID FK),
  created_at (TIMESTAMPTZ), updated_at (TIMESTAMPTZ)
- Soft delete: colonna deleted_at TIMESTAMPTZ nullable
  (NON usare DELETE fisico sui dati utente)

AUTH:
- Supabase Auth
- Solo email/password per v1 (NO OAuth per ora)
- JWT gestito da Supabase — non customizzare

AI LAYER:
- OpenAI API (gpt-4o-mini per cost efficiency)
- Chiamate AI SOLO da server-side (Edge Functions)
  → MAI esporre API key al client
- Implementa retry con exponential backoff (max 3 tentativi)

HOSTING:
- Vercel (auto-deploy da GitHub main branch)

MONITORING:
- Sentry per error tracking (frontend + edge functions)
- PostHog per analytics eventi

ENVIRONMENT VARIABLES RICHIESTE:
- NEXT_PUBLIC_SUPABASE_URL
- NEXT_PUBLIC_SUPABASE_ANON_KEY
- SUPABASE_SERVICE_ROLE_KEY (solo server-side)
- OPENAI_API_KEY (solo server-side)
- SENTRY_DSN
- NEXT_PUBLIC_POSTHOG_KEY
```

---

## 🎯 TARGET UTENTE

**Chi è**: Marco, 34 anni, consulente / freelance
**Problema**: Ha sempre 30-50+ task aperti, non sa
da dove iniziare, finisce la giornata con la sensazione
di aver fatto molto ma non le cose importanti

**Livello tecnico**: Non tecnico — vuole un'app semplice
**Contesto d'uso**: Mattina (8-9) per pianificare la giornata,
sera (17-18) per fare il recap

**Jobs-to-be-done**:
> "Ogni mattina voglio sapere esattamente le 3 cose
> più importanti da fare oggi, senza dover pensarci."

---

## 🏗️ CORE FEATURES — ORGANIZZATE PER FASE

---

### ⚡ FASE 1: Auth + Task CRUD Base
**Durata**: Giorni 1-4
**Obiettivo al termine**: L'utente può registrarsi,
creare task, vederli in lista, completarli, eliminarli.
**Non includere**: AI, prioritizzazione, dashboard avanzata.

---

#### FEATURE 1.1: Autenticazione

**User Flow**:
```
/login:
1. Form: email + password
2. Submit → POST Supabase Auth
3. Success → redirect a /dashboard
4. Error (credenziali errate) → inline message sotto form:
   "Email o password non corretti"
   NON specificare quale dei due è sbagliato (sicurezza)

/register:
1. Form: nome + email + password (min 8 char)
2. Submit → crea utente Supabase Auth + riga in tabella users
3. Success → redirect a /dashboard (NON richiedere
   verifica email in v1 — riduce attrito)
4. Error (email esistente) → "Email già in uso. [Fai login →]"
```

**Acceptance Criteria**:
- [ ] ✅ Login funziona con credenziali corrette → redirect /dashboard
- [ ] ✅ Login con credenziali errate → messaggio errore specifico
- [ ] ✅ Register crea riga in tabella `users` con name, email
- [ ] ✅ Session persiste dopo refresh della pagina
- [ ] ✅ Logout cancella session e redirect a /login
- [ ] ❌ NON implementare "Dimentica password" in Fase 1

**Schema DB**:
```sql
-- Già gestito da Supabase Auth (tabella auth.users)
-- Crea tabella pubblica per dati aggiuntivi:

CREATE TABLE public.users (
  id UUID PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
  name TEXT NOT NULL,
  email TEXT NOT NULL,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- RLS:
ALTER TABLE public.users ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Users see only their own profile"
ON public.users FOR ALL
USING (auth.uid() = id);
```

---

#### FEATURE 1.2: Task CRUD

**Struttura di un Task**:
```typescript
interface Task {
  id: string           // UUID
  user_id: string      // UUID — FK to users
  title: string        // max 200 char — required
  description?: string // max 1000 char — optional
  status: 'todo' | 'in_progress' | 'done'
  priority: 'low' | 'medium' | 'high' | null
  deadline?: Date      // optional
  energy_required: 'low' | 'medium' | 'high' // default: 'medium'
  ai_suggested_today: boolean  // default: false
  created_at: Date
  updated_at: Date
  deleted_at?: Date    // soft delete
}
```

**User Flow — Creare Task**:
```
1. Utente è su /dashboard
2. Clicca "Aggiungi task" (bottone prominente, sempre visibile)
3. Si apre Dialog (shadcn Dialog component) con form:
   - Titolo (required, autofocus)
   - Descrizione (optional, textarea)
   - Deadline (optional, date picker)
   - Energia richiesta (low/medium/high — default medium)
4. Submit → POST /api/tasks
5. Dialog chiude → task appare in cima alla lista
   con animazione slide-in
6. Toast: "Task aggiunto ✓"
```

**User Flow — Completare Task**:
```
1. Utente vede checkbox a sinistra di ogni task
2. Click su checkbox → status diventa 'done'
3. Task si sposta in fondo alla lista o
   nella sezione "Completati" (toggle visibile)
4. Animazione: strikethrough sul titolo + fade
5. PATCH /api/tasks/:id {status: 'done'}
```

**User Flow — Eliminare Task**:
```
1. Hover su task → appare icona cestino (Lucide: Trash2)
2. Click → Dialog conferma: "Eliminare questo task?
   Questa azione non può essere annullata."
   [Elimina] [Annulla]
3. Conferma → soft delete (updated_at + deleted_at = NOW())
   → PATCH /api/tasks/:id {deleted_at: now()}
4. Task sparisce dalla lista con animazione fade-out
5. Toast: "Task eliminato" + [Annulla] (undo entro 5 secondi)
```

**Acceptance Criteria**:
- [ ] ✅ Task creato appare in lista senza refresh
- [ ] ✅ Task completato mostra strikethrough
- [ ] ✅ Task eliminato ha undo di 5 secondi
- [ ] ✅ Lista vuota mostra empty state (non pagina bianca)
- [ ] ✅ RLS: un utente non può vedere task di altri utenti
- [ ] ❌ FALLISCE SE: eliminare un task lo cancella fisicamente
  dal DB (deve essere soft delete)

**Schema DB**:
```sql
CREATE TABLE public.tasks (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES public.users(id) ON DELETE CASCADE,
  title TEXT NOT NULL CHECK (char_length(title) <= 200),
  description TEXT CHECK (char_length(description) <= 1000),
  status TEXT NOT NULL DEFAULT 'todo'
    CHECK (status IN ('todo', 'in_progress', 'done')),
  priority TEXT CHECK (priority IN ('low', 'medium', 'high')),
  deadline TIMESTAMPTZ,
  energy_required TEXT NOT NULL DEFAULT 'medium'
    CHECK (energy_required IN ('low', 'medium', 'high')),
  ai_suggested_today BOOLEAN NOT NULL DEFAULT FALSE,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW(),
  deleted_at TIMESTAMPTZ  -- NULL = not deleted
);

-- Index per performance query comuni:
CREATE INDEX tasks_user_id_idx ON public.tasks(user_id);
CREATE INDEX tasks_status_idx ON public.tasks(status);
CREATE INDEX tasks_deleted_at_idx ON public.tasks(deleted_at);

-- RLS:
ALTER TABLE public.tasks ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Users see only their own tasks"
ON public.tasks FOR ALL
USING (auth.uid() = user_id AND deleted_at IS NULL);

-- Trigger per updated_at automatico:
CREATE OR REPLACE FUNCTION update_updated_at()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = NOW();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER tasks_updated_at
BEFORE UPDATE ON public.tasks
FOR EACH ROW EXECUTE FUNCTION update_updated_at();
```

---

### 🤖 FASE 2: AI Prioritization
**Durata**: Giorni 5-9
**Prerequisito**: Fase 1 completata e testata manualmente
**Obiettivo**: L'AI suggerisce le 3 priorità del giorno

---

#### FEATURE 2.1: Daily AI Briefing

**Logica AI**:
```
Ogni mattina (o quando l'utente clicca "Genera priorità"):
1. Fetch tutti i task dell'utente con status != 'done'
   e deleted_at IS NULL
2. Costruisci prompt per OpenAI (vedi sotto)
3. Ricevi risposta: array di 3 task IDs con spiegazione
4. Marca quei 3 task: ai_suggested_today = true
5. Mostra sezione "Le tue 3 priorità di oggi" in cima
```

**Prompt Template** (Edge Function):
```typescript
const systemPrompt = `Sei un assistente di produttività.
Ricevi una lista di task di un professionista e devi
selezionare le 3 priorità del giorno.

Criteri di selezione (in ordine di importanza):
1. Deadline imminente (oggi o domani = massima priorità)
2. Priorità marcata 'high' dall'utente
3. Energia richiesta 'low' o 'medium' (per le mattine)
4. Task più vecchi (creati prima)

Rispondi SOLO con JSON valido in questo formato:
{
  "priorities": [
    {
      "task_id": "uuid-del-task",
      "reason": "Spiegazione breve in italiano (max 20 parole)"
    }
  ]
}

Non aggiungere testo fuori dal JSON.`;

const userPrompt = `Lista task dell'utente:
${JSON.stringify(tasks.map(t => ({
  id: t.id,
  title: t.title,
  deadline: t.deadline,
  priority: t.priority,
  energy_required: t.energy_required,
  created_at: t.created_at
})))}

Oggi è: ${new Date().toISOString()}`;
```

**Acceptance Criteria**:
- [ ] ✅ Il briefing mostra esattamente 3 task (non di più, non di meno)
- [ ] ✅ Se l'utente ha meno di 3 task, mostra quanti ne ha
- [ ] ✅ Ogni priorità ha una spiegazione leggibile
- [ ] ✅ Se OpenAI fallisce → fallback: ordina per deadline
  e mostra i 3 più urgenti senza spiegazione AI
  con banner: "Suggerimenti AI non disponibili —
  ecco le tue priorità per deadline"
- [ ] ✅ Il briefing può essere rigenerato manualmente
  con bottone "Rigenera priorità"
- [ ] ❌ NON chiamare OpenAI più di 1 volta ogni 30 minuti
  per lo stesso utente (rate limit interno)

**API Endpoint**:
```
POST /api/ai/daily-briefing
Auth: required (JWT header)
Body: {} (nessun body — l'endpoint legge i task dell'utente)
Response:
{
  "success": true,
  "data": {
    "priorities": [
      {
        "task_id": "uuid",
        "title": "Titolo del task",
        "reason": "Scadenza oggi"
      }
    ],
    "generated_at": "ISO timestamp",
    "fallback": false
  }
}
```

---

### 🎨 FASE 3: Dashboard + UX Polish
**Durata**: Giorni 10-14
**Prerequisito**: Fase 2 funzionante e testata
**Obiettivo**: UX completa, responsive, pronta per utenti reali

---

#### FEATURE 3.1: Dashboard Layout

**Layout**:
```
HEADER: Logo | "Ciao Marco 👋" | [Logout]

SEZIONE HERO (solo se briefing generato):
┌─────────────────────────────────────────────┐
│ 🎯 Le tue 3 priorità di oggi                │
│                                             │
│ □ [Task 1] — "Scadenza oggi"               │
│ □ [Task 2] — "Alta priorità"               │
│ □ [Task 3] — "Hai rimandato da 3 giorni"   │
│                           [Rigenera →]      │
└─────────────────────────────────────────────┘

SEZIONE TASK LIST:
Tabs: [Tutti] [Oggi] [Alta priorità] [Completati]

[+ Aggiungi task]

Lista task con:
- Checkbox completamento
- Titolo
- Badge deadline (rosso se scaduta, giallo se oggi)
- Badge energia (🔋 low/medium/high)
- Icona cestino (su hover)
```

**Responsive**:
```
Mobile (< 768px):
- Header collassato (solo logo + hamburger)
- Sezione hero stack verticale
- Lista task full-width
- Bottone "+" floating in basso a destra

Desktop (≥ 768px):
- Layout come descritto sopra
- Sidebar opzionale in v2 (non in scope v1)
```

**Acceptance Criteria**:
- [ ] ✅ Layout funziona su mobile, tablet, desktop
- [ ] ✅ Empty state per ogni tab (non pagine bianche)
- [ ] ✅ Deadline scadute mostrano badge rosso
- [ ] ✅ Loading skeleton durante fetch dei task
- [ ] ✅ Transizioni animate (non flash secco)

---

## 🔴 AI CONSTRAINTS — REGOLE OPERATIVE

```
⚠️ ISTRUZIONI PER CURSOR / CLAUDE — LEGGI PRIMA DI OGNI SESSIONE

COSA FARE:
✅ Costruisci una FASE alla volta
✅ Scrivi TypeScript strict (no 'any')
✅ Usa SEMPRE shadcn/ui se il componente esiste
✅ Gestisci SEMPRE loading, error e empty state
✅ Ogni funzione complessa ha un JSDoc comment
✅ Ogni chiamata API ha error handling con try/catch
✅ Le API key non appaiono MAI nel codice client

COSA NON FARE:
❌ Non aggiungere feature non nel PRD
❌ Non cambiare il tech stack (chiedi prima)
❌ Non usare DELETE fisico sui dati utente
❌ Non esporre SUPABASE_SERVICE_ROLE_KEY al client
❌ Non passare alla Fase 2 prima che la Fase 1 sia testata
❌ Non usare useState per stato globale
   (usa Zustand se serve stato globale)

SE HAI DUBBI:
→ Chiedi sempre prima di interpretare
→ Mostra il codice per review prima di procedere
→ Segnala se un requisito del PRD ti sembra
  tecnicamente problematico
```

---

## ❓ OPEN QUESTIONS

| # | Domanda | Priorità | Status |
|---|---------|----------|--------|
| 1 | Il briefing AI si rigenera automaticamente ogni mattina (cron job) o solo su richiesta dell'utente? | Alta | 🔴 Da decidere |
| 2 | Il piano free include l'AI o è solo per paid? | Alta | 🔴 Da decidere |
| 3 | Vogliamo notifiche push/email per il briefing mattutino? | Media | 🟡 Post-v1 |

---
*Versione 1.1 — Aggiornato il [Data]*
*Source of truth del progetto FocusBoard*
🟠 ESEMPIO 3 — PR/FAQ AMAZON-STYLE (Tipo E)
Prodotto: "ContentCalendar AI" — Pianificatore contenuti con AI
Markdown

---
# PR/FAQ: ContentCalendar AI
**Tipo**: Validazione strategica pre-PRD
**Data**: GG/MM/AAAA
**Autore**: [Nome]
**Status**: DRAFT — Da validare con 5 potenziali utenti
---

## 📰 PRESS RELEASE SIMULATO

**PER RILASCIO IMMEDIATO**

### ContentCalendar AI: Il Primo Pianificatore di Contenuti
### che Pensa Come un Social Media Manager Senior

**[Città], [Data]** — ContentCalendar AI ha annunciato oggi
il lancio della sua piattaforma AI-powered che risolve
il problema numero uno dei creator e delle PMI:
non sapere cosa pubblicare e quando.

Con ContentCalendar AI, i professionisti del marketing
e i creator possono generare un calendario editoriale
completo per 30 giorni in meno di 5 minuti,
con idee di contenuto personalizzate per il loro brand,
il loro tono di voce e i loro obiettivi di business.

"Ogni lunedì mattina perdevo 2 ore a pensare a cosa
pubblicare quella settimana," ha detto [nome utente beta],
social media manager freelance.
"Con ContentCalendar AI ci metto 5 minuti.
E i contenuti sono migliori di quelli che avrei pensato da sola."

ContentCalendar AI si differenzia dai generici tool AI
per tre caratteristiche uniche:
**Brand Memory** (impara il tono di voce del brand
dalle prime interazioni), **Trend Integration**
(integra trend di settore in tempo reale),
e **Multi-Platform Calendar** (genera varianti
native per LinkedIn, Instagram e newsletter
da un'unica idea madre).

ContentCalendar AI è disponibile da oggi su
contentcalendar.ai con un piano gratuito
(7 giorni di calendario/mese) e piano Pro (€29/mese,
calendario illimitato + Brand Memory).

---

## ❓ FAQ CUSTOMER-FACING

**Q: Come fa ContentCalendar AI a conoscere
il mio brand e il mio tono di voce?**

A: Al primo accesso, fai un onboarding di 5 minuti
in cui descrivi il tuo brand, il tuo pubblico target,
i tuoi obiettivi e il tuo stile comunicativo.
Opzionalmente, puoi incollare 3-5 tuoi contenuti
passati che ti sono piaciuti. Il sistema li analizza
e li usa come riferimento per tutti i contenuti futuri.
Con il piano Pro, il Brand Memory migliora nel tempo
in base ai contenuti che approvi o modifichi.

**Q: I contenuti generati sono davvero originali
o sono generici?**

A: I contenuti sono generati specificamente per te,
basandosi su: il tuo settore, il tuo brand personality,
il tuo pubblico target e i trend del momento
nel tuo settore. Non sono template riempiti —
sono idee originali. Detto questo, li presentiamo
sempre come punto di partenza che tu puoi e
dovresti personalizzare.

**Q: Funziona anche per business di nicchia
o settori tecnici?**

A: Sì. Il sistema funziona meglio quando descrivi
il tuo settore in modo specifico durante l'onboarding.
Abbiamo utenti in settori come consulenza legale,
ingegneria civile, fisioterapia e B2B manifatturiero
— tutti con ottimi risultati.

**Q: Posso modificare i contenuti suggeriti?**

A: Assolutamente — è il workflow consigliato.
ContentCalendar AI genera le idee, tu le raffini.
Ogni contenuto è editabile direttamente nel calendario
con un editor semplice. Le modifiche vengono usate
per migliorare i futuri suggerimenti (solo piano Pro).

**Q: Quanto costa rispetto ad assumere
un social media manager?**

A: Un SMM freelance base costa €500-1.500/mese.
ContentCalendar AI Pro costa €29/mese.
Non sostituisce un SMM per la gestione e
l'interazione con il pubblico, ma elimina
il lavoro di pianificazione e ideazione,
che rappresenta il 40-60% del tempo di un SMM.

---

## 🔒 FAQ INTERNE

**Q: Perché un creator dovrebbe scegliere noi
invece di ChatGPT diretto?**

A: ChatGPT richiede di sapere come fare il prompt,
non ha memoria del brand, non genera un calendario
strutturato, non integra trend, e non ha
una UI ottimizzata per questa workflow specifica.
Noi siamo ChatGPT con interfaccia professionale,
Brand Memory, e un output strutturato come calendario.
Il valore è nell'opinionated workflow,
non nel modello AI sottostante.

**Q: Qual è il rischio principale del modello?**

A: Il principale rischio è la commodity trap —
OpenAI o competitor possono lanciare feature simili
integrate nei loro prodotti. La difesa è il Brand Memory
(dati proprietari dell'utente difficili da migrare)
e la specializzazione verticale vs tool generici.

**Q: Come generiamo revenue nei primi 6 mesi?**

A: Piano gratuito (lead magnet) → upgrade a Pro (€29/mese)
dopo aver esaurito i 7 giorni free.
Target: 500 utenti Pro entro mese 6 = €14.500 MRR.
Canale principale: LinkedIn content marketing organico
(il nostro target è già lì).

**Q: Il modello Unit Economics regge?**

A: Costo OpenAI API per utente Pro: ~€2/mese.
Costo Vercel/infrastruttura: ~€0.5/utente/mese.
Margine lordo: ~90%. Break-even: ~200 utenti Pro.

---

## 📊 SUCCESS METRICS

**North Star**: Contenuti generati e approvati per settimana
Target: ≥ 3 per utente attivo

**Primary Metrics**:
- Trial → Pro conversion: target ≥ 12%
- D30 retention Pro: target ≥ 70%
- MRR mese 6: target €14.500 (500 utenti)

---

## 🚀 NEXT STEPS

Se questo PR/FAQ viene validato con 5 interviste utente:
1. Scrivere PRD MVP Lean (Tipo B) — 3 giorni
2. Definire tech stack — 1 giorno
3. Iniziare sviluppo Fase 1 — giorno 5

**Validazione richiesta**: Mostrare questo documento
a 5 social media manager / creator e chiedere:
"Pagheresti €29/mese per questo? Perché sì/no?"
Target: ≥ 3/5 rispondono "sì" con entusiasmo.

---

## ✅ SEZIONE 1 — CHECKLIST DI QUALITÀ COMPLETA

La checklist è divisa in **6 livelli** di verifica.
Ogni livello deve essere superato prima di consegnare il PRD.
Il sistema assegna un punteggio finale (0-100).

---

### 🔴 LIVELLO 0 — GATE DI INGRESSO
### (Se anche uno solo di questi fallisce → il PRD non viene generato)

```python
GATE_CHECKS = {

    "G1_problema_non_soluzione": {
        "descrizione": (
            "Il problem statement descrive il dolore "
            "dell'utente, NON la soluzione tecnica"
        ),
        "test": (
            "Il testo del problem statement NON inizia con: "
            "'Voglio costruire', 'Ho bisogno di', "
            "'L'app deve', 'Il sistema deve'"
        ),
        "esempio_fallimento": (
            "Problem: 'Voglio costruire un dashboard "
            "con grafici circolari e filtri avanzati'"
        ),
        "esempio_successo": (
            "Problem: 'I freelance italiani perdono "
            "3-4 ore/settimana a costruire preventivi "
            "manualmente, con errori di calcolo frequenti'"
        ),
        "peso": "BLOCCANTE"
    },

    "G2_north_star_numerica": {
        "descrizione": (
            "La North Star Metric ha un numero target "
            "specifico e misurabile"
        ),
        "test": (
            "La North Star Metric contiene almeno un numero "
            "e un timeframe specifico"
        ),
        "esempio_fallimento": "North Star: 'Aumentare la retention'",
        "esempio_successo": (
            "North Star: D7 retention ≥ 35% "
            "entro 60 giorni dal lancio"
        ),
        "peso": "BLOCCANTE"
    },

    "G3_almeno_una_user_story": {
        "descrizione": (
            "Il PRD contiene almeno 1 user story "
            "con acceptance criteria"
        ),
        "test": (
            "Esiste almeno 1 blocco nel formato "
            "'Come [X] voglio [Y] in modo da [Z]' "
            "con almeno 2 acceptance criteria"
        ),
        "peso": "BLOCCANTE"
    },

    "G4_non_goals_presenti": {
        "descrizione": "La sezione Non-Goals esiste e non è vuota",
        "test": "La sezione Out-of-Scope ha almeno 2 voci specifiche",
        "esempio_fallimento": "Out of Scope: 'Feature future'",
        "esempio_successo": (
            "Out of Scope: App mobile iOS/Android "
            "(post-PMF, rivalutare dopo 1.000 utenti paganti)"
        ),
        "peso": "BLOCCANTE"
    }
}
🟠 LIVELLO 1 — STRUTTURA (30 punti)
Markdown

## CHECKLIST STRUTTURA

### Header e Metadati (6 punti)
- [ ] Titolo specifico e descrittivo (non "PRD Feature X") — 1pt
- [ ] Versione presente (es: v1.2) — 1pt
- [ ] Status dichiarato (DRAFT/REVIEW/APPROVED) — 1pt
- [ ] Autore e data creazione — 1pt
- [ ] Data ultima modifica — 1pt
- [ ] Change log presente con almeno 1 riga — 1pt

### Sezioni Obbligatorie Presenti (12 punti)
- [ ] TL;DR / Executive Summary — 2pt
- [ ] Problem Statement con evidenza — 2pt
- [ ] Target Utente con persona strutturata — 2pt
- [ ] Success Metrics (North Star + Primary) — 2pt
- [ ] User Stories con Acceptance Criteria — 2pt
- [ ] Scope In/Out con Non-Goals — 2pt

### Sezioni Consigliate Presenti (8 punti)
- [ ] User Flows per almeno 1 percorso critico — 2pt
- [ ] Edge Cases & Error States — 2pt
- [ ] Assumptions & Dependencies — 2pt
- [ ] Open Questions — 2pt

### Formato e Leggibilità (4 punti)
- [ ] Documento in Markdown valido — 1pt
- [ ] Heading gerarchici corretti (H1→H2→H3) — 1pt
- [ ] Nessun muro di testo >5 righe senza struttura — 1pt
- [ ] Tabelle usate dove appropriato — 1pt

PUNTEGGIO STRUTTURA: __/30
🟡 LIVELLO 2 — QUALITÀ DEL CONTENUTO (40 punti)
Markdown

## CHECKLIST QUALITÀ CONTENUTO

### Problem Statement (8 punti)
- [ ] Descrive il dolore dell'utente, non la soluzione — 2pt
- [ ] Include almeno 1 dato quantitativo o evidenza — 2pt
- [ ] Spiega perché le soluzioni attuali non bastano — 2pt
- [ ] Risponde a "perché costruire questo ADESSO?" — 2pt

### Target Utente (6 punti)
- [ ] Persona ha nome, ruolo, contesto specifico — 2pt
- [ ] Job-to-be-done formulato correttamente
  ("Quando X, voglio Y, in modo da Z") — 2pt
- [ ] Quote rappresentativa presente — 2pt

### Success Metrics (8 punti)
- [ ] North Star Metric con numero E timeframe — 2pt
- [ ] Primary Metrics max 3 (non 10+) — 2pt
- [ ] Guardrail Metrics presenti — 2pt
- [ ] Metodo di misurazione specificato (quale tool,
  quale evento, quale query) — 2pt

### User Stories (10 punti)
- [ ] Formato corretto: Come/Voglio/In modo da — 2pt
- [ ] Acceptance criteria testabili senza interpretazione — 3pt
- [ ] Almeno 1 "FALLISCE SE" per story critica — 2pt
- [ ] Priority assegnata (P0/P1/P2) — 1pt
- [ ] Effort stimato presente — 2pt

### Scope (4 punti)
- [ ] In-scope è specifico (non "feature core") — 2pt
- [ ] Out-of-scope include motivazione e timeline
  rivalutazione — 2pt

### Requisiti Tecnici (4 punti)
- [ ] Tech stack specificato (anche a livello alto) — 2pt
- [ ] Almeno 2 requisiti non-funzionali con numeri — 2pt

PUNTEGGIO QUALITÀ: __/40
🟢 LIVELLO 3 — EDGE CASES & ERROR STATES (15 punti)
Markdown

## CHECKLIST EDGE CASES

### Empty States (3 punti)
- [ ] Identificato almeno 1 empty state per feature
  che mostra liste o dashboard — 1pt
- [ ] Ogni empty state ha contenuto specifico
  (non "Nessun elemento trovato") — 1pt
- [ ] Ogni empty state ha CTA primaria — 1pt

### Error States (6 punti)
- [ ] Identificati error states per ogni operazione
  asincrona (API call, upload, pagamento) — 2pt
- [ ] Ogni error state ha messaggio specifico
  in plain language (non "An error occurred") — 2pt
- [ ] Ogni error state ha azione suggerita
  (retry, contatta supporto, alternativa) — 2pt

### Loading States (3 punti)
- [ ] Identificato loading state per ogni operazione
  che può durare >500ms — 1pt
- [ ] Tipo di feedback visivo specificato
  (spinner, skeleton, progress bar) — 1pt
- [ ] Durata stimata specificata per ciascuno — 1pt

### Edge Cases Specifici (3 punti)
- [ ] Comportamento offline o rete degradata — 1pt
- [ ] Sessione scaduta mid-flow — 1pt
- [ ] Utente senza permessi (feature gating,
  piano free, ruolo insufficiente) — 1pt

PUNTEGGIO EDGE CASES: __/15
🔵 LIVELLO 4 — ANALYTICS & TRACKING (10 punti)
Markdown

## CHECKLIST ANALYTICS

### Eventi Core (6 punti)
- [ ] Almeno 1 evento per ogni azione critica
  dell'utente (signup, core action, upgrade) — 3pt
- [ ] Ogni evento ha properties definite
  (non solo il nome dell'evento) — 2pt
- [ ] Tool di tracking specificato
  (PostHog, Mixpanel, custom, etc.) — 1pt

### Connessione Metrics-Events (4 punti)
- [ ] Ogni Primary Metric è collegata
  a un evento specifico — 2pt
- [ ] La North Star Metric è misurabile
  con gli eventi definiti — 2pt

PUNTEGGIO ANALYTICS: __/10
🟣 LIVELLO 5 — CONSISTENZA INTERNA (5 punti)
Python

CONSISTENCY_CHECKS = {

    "C1_stories_persona_allineate": {
        "check": (
            "Le user stories sono scritte per le "
            "personas definite nel documento. "
            "Se la persona è 'Marco il freelance', "
            "non esistono stories per 'l'admin aziendale' "
            "se questa persona non è definita."
        ),
        "peso": 1
    },

    "C2_metrics_problem_allineate": {
        "check": (
            "Le success metrics misurano il problema "
            "dichiarato nel problem statement. "
            "Se il problema è 'gli utenti abbandonano', "
            "la metrica deve essere la retention, "
            "non il numero di signup."
        ),
        "peso": 2
    },

    "C3_tech_nonfunc_allineati": {
        "check": (
            "I requisiti non-funzionali sono compatibili "
            "con il tech stack scelto. "
            "Se si usa Supabase free tier, "
            "non si può dichiarare SLA del 99.99%."
        ),
        "peso": 1
    },

    "C4_timeline_team_realistica": {
        "check": (
            "Il timeline è realistico rispetto al team. "
            "1 developer non può consegnare in 2 settimane "
            "ciò che richiederebbe 3 mesi per un team di 5."
        ),
        "peso": 1
    }
}
📊 SCORE FINALE E INTERPRETAZIONE
Python

PRD_QUALITY_SCORING = {

    "calcolo": {
        "livello_0": "GATE — se fallisce anche 1 check: score = 0, PRD bloccato",
        "livello_1_struttura": "max 30 punti",
        "livello_2_qualita": "max 40 punti",
        "livello_3_edge_cases": "max 15 punti",
        "livello_4_analytics": "max 10 punti",
        "livello_5_consistenza": "max 5 punti",
        "totale": "max 100 punti"
    },

    "interpretazione": {
        "0": "🔴 BLOCCATO — Gate check fallito. Non procedere.",
        "1_49": "🔴 INSUFFICIENTE — PRD troppo incompleto per avviare sviluppo.",
        "50_64": "🟠 BOZZA — Utilizzabile per discussione iniziale, non per sviluppo.",
        "65_79": "🟡 DRAFT APPROVABILE — Può avviare sviluppo con warnings.",
        "80_89": "🟢 BUONO — PRD solido, pronto per review engineering.",
        "90_100": "🔵 ECCELLENTE — PRD production-ready."
    },

    "output_report": """
## 📊 PRD QUALITY REPORT — {nome_prd}

### Score Finale: {score}/100 — {interpretazione}

| Livello | Score | Max | % |
|---------|-------|-----|---|
| Gate Checks | {g}/PASS | PASS | — |
| Struttura | {l1} | 30 | {p1}% |
| Qualità Contenuto | {l2} | 40 | {p2}% |
| Edge Cases | {l3} | 15 | {p3}% |
| Analytics | {l4} | 10 | {p4}% |
| Consistenza | {l5} | 5 | {p5}% |

### ✅ Punti di Forza
{strengths}

### ⚠️ Warnings (risolvi prima dell'approvazione)
{warnings}

### 🔴 Blockers (risolvi prima di procedere)
{blockers}

### 💡 Raccomandazioni Prioritarie
1. {rec1}
2. {rec2}
3. {rec3}
    """
}
🚫 SEZIONE 2 — ANTI-PATTERN COMPLETI
Questa sezione documenta i 15 anti-pattern più comuni
nei PRD. La skill li identifica e li segnala attivamente.

❌ ANTI-PATTERN #1 — "The Feature Wishlist"
Markdown

## DESCRIZIONE
Il PRD è una lista di feature senza problema, senza utente,
senza metriche. Sembra un backlog Jira, non un PRD.

## COME SI MANIFESTA
- Sezione "Requisiti" con 40+ feature elencate
- Nessun problem statement
- Nessuna persona utente
- Metriche assenti o vaghe ("l'app deve funzionare bene")

## ESEMPIO
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

## PERCHÉ È PERICOLOSO
- Engineering costruisce le feature nell'ordine sbagliato
- Nessuno sa cosa è P0 vs P3
- Lo scope esplode ad ogni meeting
- Il prodotto viene lanciato ma non risolve nessun problema

## CORREZIONE
Parti sempre dal problema: chi soffre di cosa, con quale evidenza.
Poi deriva le feature come soluzione a quel problema specifico.
❌ ANTI-PATTERN #2 — "The Vague Metric Trap"
Markdown

## DESCRIZIONE
Le metriche esistono ma sono misurabili quanto
"il meteo sarà bello domani".

## ESEMPI DI METRICHE VAGHE
❌ "Aumentare la retention"
❌ "Migliorare l'engagement"
❌ "Ridurre il churn"
❌ "Crescere organicamente"
❌ "Gli utenti devono essere soddisfatti"

## CORREZIONE IMMEDIATA

Per ogni metrica vaga, applica questo test:
"Tra 60 giorni, come sapremo esattamente se
abbiamo raggiunto questo obiettivo?"

Se la risposta richiede interpretazione → la metrica è vaga.

✅ "D7 retention ≥ 35% misurata con PostHog
    sulla coorte di utenti che si registrano
    a Febbraio 2025. Baseline attuale: 18%."
❌ ANTI-PATTERN #3 — "The Orphan Edge Case"
Markdown

## DESCRIZIONE
Il PRD descrive il happy path perfettamente
ma ignora completamente gli stati di errore,
gli stati vuoti, i loading state.

## IMPATTO SUL VIBECODING
Quando passi il PRD a Cursor o Claude,
l'AI costruisce SOLO il happy path.
Gli error state vengono gestiti con
"console.log(error)" o modali generici.

## CHECKLIST ANTI-ORPHAN
Per ogni feature interattiva, verifica:

□ Cosa vede l'utente se la lista è vuota?
□ Cosa vede l'utente mentre la pagina carica?
□ Cosa vede l'utente se l'API fallisce?
□ Cosa vede l'utente se non ha i permessi?
□ Cosa succede se l'utente preme "back"
  durante un'operazione in corso?
□ Cosa succede se la sessione scade
  mentre compila un form lungo?
❌ ANTI-PATTERN #4 — "The Eternal Draft"
Markdown

## DESCRIZIONE
Il PRD rimane in stato DRAFT per settimane
mentre lo sviluppo è già iniziato.
Nessuno lo aggiorna, nessuno lo legge.
Diventa un documento fantasma.

## SINTOMI
- Ultima modifica: 3+ settimane fa
- Status: DRAFT (mai cambiato)
- Change log: vuoto o con 1 riga
- Il codice ha feature non nel PRD
- Il PRD ha sezioni non ancora sviluppate

## CORREZIONE
Il PRD segue il prodotto, non il contrario.
Regola: se prendi una decisione che cambia
qualcosa nel PRD → aggiorni il PRD entro 24h.
Usa feature flags nel change log per tracciare
cosa è cambiato e perché.
❌ ANTI-PATTERN #5 — "The Everything Is P0"
Markdown

## DESCRIZIONE
Tutte le user stories sono marcate P0.
Tutto è critico. Tutto è urgente.
Engineering non sa da dove iniziare.

## IMPATTO
- Sprint overloaded sistematicamente
- Feature critiche bloccate da feature nice-to-have
- Team frustrato e demotivato
- Nessun senso di progresso

## FRAMEWORK DI PRIORITIZZAZIONE CORRETTO

P0 — MUST HAVE (blocca il lancio)
→ Senza questo, il prodotto non può essere lanciato
→ Max il 20-30% delle feature

P1 — SHOULD HAVE (fortemente consigliato per v1)
→ Importante ma il lancio può avvenire senza
→ 30-40% delle feature

P2 — NICE TO HAVE (backlog)
→ Migliora l'esperienza ma non è essenziale
→ 30-50% delle feature

REGOLA: Se tutto è P0, niente è P0.
❌ ANTI-PATTERN #6 — "The Technical PRD"
Markdown

## DESCRIZIONE
Il PRD è scritto per developer, non per il prodotto.
È pieno di terminologia tecnica, schemi DB dettagliati,
specifiche di implementazione.
Il PM ha scritto il Technical Design Document
mascherato da PRD.

## PERCHÉ È SBAGLIATO
Il PRD dice COSA e PERCHÉ.
Il TDD dice COME.

Se il PRD specifica il tipo di join SQL da usare,
l'indice del database, l'algoritmo di hashing...
→ Stai micro-managing engineering
→ Stai rimuovendo autonomia tecnica al team
→ Il PRD diventerà obsoleto al primo refactor

## LINEA DI DEMARCAZIONE

NEL PRD:
✅ "I dati degli utenti devono essere isolati tra tenant"
✅ "Le query devono rispondere in <300ms al P95"
✅ "Il sistema deve scalare fino a 10.000 utenti"

NEL TDD (non nel PRD):
❌ "Usa Row Level Security in PostgreSQL"
❌ "Aggiungi index su user_id e created_at"
❌ "Usa Redis per caching delle sessioni"
❌ ANTI-PATTERN #7 — "The Missing Persona"
Markdown

## DESCRIZIONE
Il target utente è definito in modo così vago
che chiunque potrebbe essere il cliente.
Nessuna decisione di design può essere presa
con un target così generico.

## ESEMPI DI TARGET VAGHI
❌ "Utenti che vogliono essere più produttivi"
❌ "Professionisti del settore"
❌ "PMI italiane"
❌ "Chiunque abbia bisogno di gestire task"

## PERCHÉ È PERICOLOSO
Quando il target è "tutti":
- L'onboarding cerca di accontentare tutti → confonde tutti
- Le feature vengono aggiunte per segmenti diversi → bloat
- Il copy è generico → non converte
- Il marketing non sa chi targettare → CAC esplode

## CORREZIONE
Una persona primaria, specifica, con un job-to-be-done preciso.
Se hai più segmenti → prioritizza il primario
e considera gli altri come secondary personas.
Costruisci per la persona primaria.
❌ ANTI-PATTERN #8 — "The Scope Creep Enabler"
Markdown

## DESCRIZIONE
La sezione Non-Goals è assente o ha voci vaghe.
Ogni stakeholder interpreta lo scope diversamente.
Ad ogni meeting vengono aggiunte "piccole cose".

## COME PREVENIRLO NEL PRD

La sezione Out-of-Scope deve avere:
1. Feature specifica (non categoria generica)
2. Motivazione esplicita (perché no in v1)
3. Timeline di rivalutazione (quando potrebbe entrare)

❌ SBAGLIATO:
"Out of scope: funzionalità avanzate, integrazioni,
feature enterprise"

✅ CORRETTO:
| Feature | Motivazione | Rivalutare in |
|---------|-------------|---------------|
| Firma digitale preventivi | Complessità legale e costo integrazione (DocuSign ~€30/mese) | v3 se richiesto da >30% utenti |
| App mobile | Web-first: validare prima su desktop | Post-PMF (>500 paganti) |
| Export QuickBooks | Solo 8% target usa QuickBooks | v2 — Q4 2025 |
❌ ANTI-PATTERN #9 — "The PRD Without Evidence"
Markdown

## DESCRIZIONE
Il problem statement esiste ma è basato su assunzioni,
sensazioni o "logica di mercato".
Nessuna evidenza che il problema sia reale,
che il target esista, che le soluzioni attuali non bastino.

## TIPI DI EVIDENZA ACCETTABILE (in ordine di forza)

🥇 User interviews (5+ interviste strutturate)
🥈 Dati quantitativi (analytics, survey, report di settore)
🥉 Osservazione diretta (uso personale del prodotto,
   shadowing utenti)
🏅 Community signals (Reddit, forum, commenti competitor)
🎖️ Competitive analysis (gap nelle soluzioni esistenti)

## COSA NON È EVIDENZA
❌ "Tutti hanno questo problema"
❌ "Io stesso ho questo problema" (da solo non basta)
❌ "Il mercato è grande quindi funzionerà"
❌ "I competitor lo fanno quindi c'è domanda"

## MINIMUM VIABLE EVIDENCE
Almeno 2 fonti di evidenza diverse.
Almeno 1 dato quantitativo (anche stimato con fonte).
❌ ANTI-PATTERN #10 — "The Delegated Design PRD"
Markdown

## DESCRIZIONE
La sezione UX/Design del PRD contiene solo:
"Il designer creerà i wireframe"
"Da definire con il team di design"
"Vedi Figma"

Il PM non ha pensato all'esperienza utente.
Ha delegato completamente al designer.

## PERCHÉ È SBAGLIATO
Il PRD deve contenere il PENSIERO del PM sull'esperienza,
anche se non è un designer.

Il PM deve specificare:
- Il flow dell'utente (testuale, non wireframe)
- Gli stati che ogni schermata deve gestire
- Le decisioni di UX critiche (es: modal vs pagina dedicata)
- I vincoli di UX (es: "l'onboarding non deve superare 3 step")

Il designer poi decide il COME visivo.
Il PM decide il COSA e il PERCHÉ dell'esperienza.

## CORREZIONE
Per ogni feature, scrivi il flow testuale prima
di passarlo al designer. Non è necessario che sia bello —
deve essere logicamente completo.
❌ ANTI-PATTERN #11 — "The Impossible Timeline"
Markdown

## DESCRIZIONE
Il timeline nel PRD è costruito senza coinvolgere
engineering. È aspirazionale, non realistico.
Viene ignorato da tutti dopo la prima settimana.

## SEGNALI DI TIMELINE IMPOSSIBILE
- Nessuna buffer per bug e refactor (almeno 20% del tempo)
- Feature L stimate come S
- Dipendenze esterne non considerate
- "Questa cosa è semplice" → di solito è il contrario
- 1 developer deve fare il lavoro di 3

## REGOLE PER TIMELINE REALISTICHE

REGOLA 1: Moltiplica sempre per 1.5-2x la stima iniziale
REGOLA 2: Aggiungi 20% buffer per QA e bug fixing
REGOLA 3: Le dipendenze esterne hanno sempre delay
REGOLA 4: Coinvolgi engineering nella stima prima di fissare le date
REGOLA 5: Il PRD non decide la sprint capacity —
          il team decide la sprint capacity

## SHAPE UP APPROACH (il migliore)
Non stimare i task. Fissa l'appetite (il tempo disponibile)
e poi chiedi: "Cosa possiamo costruire di valore
in queste 3 settimane?" — non "quanto tempo ci vuole?"
❌ ANTI-PATTERN #12 — "The AI-Unfriendly PRD"
Markdown

## DESCRIZIONE
Il PRD viene passato a Cursor/Claude per il vibecoding
ma è strutturato per essere letto da umani:
- Testo narrativo lungo e non strutturato
- Nessuna distinzione tra fasi di sviluppo
- Tech stack non specificato
- User flow descritti vagamente
- Nessuna acceptance criteria testabile

## RISULTATO
L'AI genera qualcosa che sembra funzionare
ma non rispetta nessun requisito specifico.
Ogni correzione rompe 3 cose diverse.
Il developer entra nel loop del vibe coding senza direzione.

## CORREZIONE PER PRD VIBECODING-READY
Vedi Template Tipo D nella Parte 4.
Le 6 regole fondamentali:
1. Markdown nel repository
2. Tech stack vincolante ed esplicito
3. Fasi numerate — 1 fase alla volta
4. User flow step-by-step testuale
5. Acceptance criteria testabili
6. Sezione AI Constraints esplicita
❌ ANTI-PATTERN #13 — "The Compliance Afterthought"
Markdown

## DESCRIZIONE
GDPR, privacy, sicurezza e compliance vengono
menzionati alla fine del PRD come "da gestire dopo il lancio".
In realtà, impattano ogni decisione architetturale.

## COSTO DELL'AFTERTHOUGHT
Aggiungere GDPR dopo il lancio significa:
- Riscrivere tutta la gestione dei dati utente
- Aggiungere consent management in ogni form
- Implementare right-to-be-forgotten su DB già popolato
- Audit log retroattivi (impossibili)
- Rischio sanzioni fino al 4% del fatturato globale

## SEZIONE COMPLIANCE NEL PRD (obbligatoria per SaaS EU)

### Data & Privacy Requirements
- [ ] Consenso esplicito richiesto per: [lista dati]
- [ ] Dati PII mai nei log applicativi
- [ ] Right-to-be-forgotten: procedura definita
- [ ] Data retention policy: [X giorni per tipo di dato]
- [ ] Crittografia at-rest: AES-256 per dati sensibili
- [ ] Crittografia in-transit: TLS 1.2+ obbligatorio
- [ ] Privacy Policy generata prima del lancio
- [ ] Cookie banner conforme (se analytics/tracking)
❌ ANTI-PATTERN #14 — "The Single Reviewer PRD"
Markdown

## DESCRIZIONE
Il PRD viene scritto dal PM in isolamento
e mai revisionato da engineering, design o sales
prima di essere "approvato".

## COSA SI PERDE SENZA REVISIONE

Engineering avrebbe detto:
→ "Questa feature richiede 3 settimane, non 3 giorni"
→ "Il sistema legacy non supporta questa integrazione"
→ "Abbiamo già questo nel codice — prendiamo quello"

Design avrebbe detto:
→ "Questo flow ha 8 step — gli utenti abbandoneranno"
→ "Questo empty state non ha senso nel contesto"
→ "Abbiamo già questo componente nel design system"

Sales/Customer Success avrebbe detto:
→ "I clienti chiedono questa feature da 6 mesi"
→ "Questa terminologia non è quella che usa il mercato"
→ "Questa feature blocca 3 deal in pipeline"

## PROCESSO MINIMO DI REVIEW

1. PM scrive bozza v1.0
2. Review sincrona con Lead Engineering (30 min)
   → Fattibilità tecnica + stima effort
3. Review sincrona con Design (20 min)
   → UX flow + vincoli design system
4. Review asincrona con Sales/CS (commenti su doc)
   → Validazione con il mercato
5. PM incorpora feedback → v1.1
6. Sign-off formale da tutti i reviewer
❌ ANTI-PATTERN #15 — "The Success Without Measurement"
Markdown

## DESCRIZIONE
Il prodotto viene lanciato, gli utenti lo usano,
ma nessuno sa se "ha funzionato" perché:
- Le metriche non erano definite nel PRD
- Il tracking non era stato implementato
- I success criteria erano vaghi
- Non c'è stato nessun post-launch review

## IMPATTO
- Non si sa se iterare, pivotare o abbandonare
- Non si può imparare da questo lancio per il prossimo
- Non si può giustificare (o no) un secondo round di sviluppo
- Il team non ha senso di closure o di successo

## POST-LAUNCH REVIEW MINIMA

Entro 30 giorni dal lancio, il PM deve produrre:

### 📊 Post-Launch Report — [Nome Feature]

**Data review**: GG/MM/AAAA (30 giorni dal lancio)

**North Star Result**:
Target: [valore] | Actual: [valore] | Delta: [%]

**Primary Metrics**:
| Metrica | Target | Actual | Δ | Valutazione |
|---------|--------|--------|---|-------------|
| [M1] | [T1] | [A1] | [D1] | ✅/⚠️/❌ |
| [M2] | [T2] | [A2] | [D2] | ✅/⚠️/❌ |

**Cosa ha funzionato**:
1. [Insight positivo]

**Cosa non ha funzionato**:
1. [Insight negativo]

**Decisione**:
[ ] ✅ Continuare e scalare
[ ] 🔄 Iterare su [aspetto specifico]
[ ] 🛑 Deprecare — motivo: [ragione]

**Next iteration PRD**: [link o "da creare"]
📋 SEZIONE 3 — CUSTOM INSTRUCTIONS COMPLETE
Questo è il blocco da incollare direttamente
nelle custom instructions del progetto Claude.

Markdown

═══════════════════════════════════════════════════════════════
CUSTOM INSTRUCTIONS — PRD ARCHITECT OS
(Incolla questo blocco nelle istruzioni del progetto Claude)
═══════════════════════════════════════════════════════════════

## IDENTITÀ E RUOLO

Sei PRD Architect OS, il sistema specializzato nella
creazione di Product Requirements Document perfetti
per prodotti SaaS, web app, mobile app e progetti
di sviluppo AI-assisted (vibecoding).

Il tuo obiettivo non è produrre testo — è eliminare
l'ambiguità prima che inizi lo sviluppo.

Non sei un generatore di template.
Sei un sistema di pensiero strutturato che guida
il PM (o il founder, o il vibe coder) attraverso
un processo preciso per produrre il PRD ottimale
per il loro contesto specifico.

---

## PROCESSO OBBLIGATORIO — SEGUI SEMPRE QUESTO ORDINE

### FASE 1 — INTAKE (MAI saltare)
Prima di scrivere una singola riga di PRD,
devi raccogliere il contesto minimo.

Valuta il contesto ricevuto su questa scala:
- Sotto 60 punti → fai domande (max 5 per round)
- 60-79 punti → genera con warnings
- 80+ punti → genera con fiducia

### FASE 2 — CONTEXT ENRICHMENT
Dopo l'intake, prima di generare:
1. Inferisci le personas dal contesto
2. Deriva i user flow dalle feature descritte
3. Identifica gli edge cases ovvi
4. Proponi success metrics coerenti col problema
5. Genera i non-goals correlati alle feature in-scope

Ogni elemento inferito va marcato:
[INFERITO — VERIFICA PRIMA DEL SIGN-OFF]

### FASE 3 — GENERAZIONE
Genera il PRD nel formato corretto per il tipo richiesto.
Mai generare un PRD Tipo A (enterprise) quando
il contesto suggerisce un MVP Lean (Tipo B).

### FASE 4 — VALIDATION REPORT
Dopo la generazione, esegui il validation check
e riporta il PRD Quality Score con i blockers.

---

## TIPI DI PRD CHE SAI PRODURRE
A — PRD COMPLETO ENTERPRISE (10-30 pagine)
→ Per SaaS B2B, prodotti con team >5 persone
→ Tutte le 17 sezioni standard

B — PRD MVP LEAN (3-5 pagine)
→ Per startup in early stage, validazione idea
→ 10 sezioni essenziali

C — FEATURE SPEC (2-4 pagine)
→ Per aggiunta di feature a prodotto esistente
→ Focus su impatto, edge cases, rollout

D — PRD VIBECODING AI-READY (3-6 pagine, Markdown)
→ Per sviluppo con Cursor, Claude, Bolt, Lovable
→ Tech stack vincolante, fasi numerate, AI Constraints

E — PR/FAQ AMAZON-STYLE (1-2 pagine)
→ Per validazione strategica pre-sviluppo
→ Press Release simulato + FAQ cliente + FAQ interne

text


---

## DOMANDE DI INTAKE — USA QUESTE ESATTE

Se il contesto è insufficiente, poni queste domande
raggruppate per priorità. Max 5 per round.

### ROUND 1 — Il Problema
1. "Descrivi in 2-3 frasi il problema che risolvi
   per l'utente. NON la soluzione — il dolore."
2. "Hai evidenza che questo problema esiste?
   (interviste, dati, tuo problema personale)"
3. "Come risolvono questo problema le persone oggi?
   Perché quelle soluzioni non bastano?"
4. "Perché costruire questo ADESSO e non tra 6 mesi?"
5. "Descrivi come appare la vita dell'utente
   30 giorni dopo aver usato il prodotto."

### ROUND 2 — Il Target
1. "Chi è il tuo utente ideale? Sii specifico:
   ruolo, età, contesto, livello tecnico."
2. "Completa questa frase:
   'Quando [situazione], voglio [azione],
   in modo da [beneficio].'"
3. "Quanto è disposto a pagare il tuo target?
   Usa già tool SaaS simili?"

### ROUND 3 — Contesto Tecnico
1. "Come verrà sviluppato?
   (A=Vibecoding AI, B=Team umano, C=Misto, D=Agency)"
2. "Hai già scelto il tech stack?
   (Framework, database, auth, payments)"
3. "Quanto tempo hai? (time-box o deadline)"
4. "Quali vincoli non negoziabili esistono?
   (budget, compliance, integrazioni obbligatorie)"

---

## REGOLE OPERATIVE — NON DEROGARE MAI

### REGOLA 1 — Problem First
Se l'utente inizia descrivendo la soluzione,
FERMATI e chiedi: "Prima dimmi il problema
che questo risolve per l'utente finale."

### REGOLA 2 — Metriche Specifiche
Non accettare metriche vaghe.
Se l'utente scrive "aumentare la retention",
rispondi: "Di quanto? Da quale baseline?
In quale timeframe? Misurata come?"

### REGOLA 3 — Non-Goals Obbligatori
Ogni PRD che generi deve avere una sezione
Out-of-Scope con almeno 2 voci specifiche
con motivazione e timeline di rivalutazione.

### REGOLA 4 — Edge Cases Mai Dimenticati
Per ogni feature con interazione utente che generi,
includi almeno:
- 1 empty state
- 1 loading state  
- 1 error state con messaggio specifico

### REGOLA 5 — Inferito vs Dichiarato
Distingui sempre tra ciò che l'utente ha dichiarato
e ciò che hai inferito.
Usa [INFERITO — VERIFICA] per tutto ciò
che non è stato esplicitamente confermato.

### REGOLA 6 — Formato Markdown
Tutto l'output è in Markdown.
Usa heading gerarchici H1→H2→H3.
Usa tabelle per confronti e matrici.
Usa code blocks per schema DB, API, tech stack.
Usa checklist per acceptance criteria.

### REGOLA 7 — Validation Report Finale
Ogni PRD generato termina con il PRD Quality Score.
Se il score è sotto 65, lista i blockers
e offri di risolvere ciascuno.

---

## FORMATO OUTPUT STANDARD

Ogni PRD generato include:
1. Header con versione, status, autore, date
2. Change log (anche vuoto con la prima riga)
3. TL;DR (3-5 righe max)
4. Tutte le sezioni del tipo richiesto
5. PRD Quality Report finale

---

## TONO E STILE

- Diretto e operativo — niente filosofia
- Specifico sempre — niente genericità
- Esempi compilati — non solo template vuoti
- Quando qualcosa manca → chiedi, non inventare
- Quando qualcosa è ambiguo → segnalalo con [?]

---

## QUANDO RICEVI UNA RICHIESTA, CHIEDI SEMPRE:

- "Che tipo di PRD serve?
  (A=Enterprise, B=MVP, C=Feature, D=Vibecoding, E=PR/FAQ)"
- "È un prodotto nuovo o una feature su prodotto esistente?"
- "Chi svilupperà? (Team umano, AI, misto)"
- "Hai già un tech stack?"
- "Qual è il time-box disponibile?"

Se l'utente fornisce già queste informazioni →
procedi direttamente all'intake del contenuto.

═══════════════════════════════════════════════════════════════
📚 SEZIONE 4 — KNOWLEDGE DA CARICARE
Markdown

## KNOWLEDGE BASE — PRD ARCHITECT OS

### 🔴 PRIORITÀ 1 — Carica Subito

| File | Cosa Contiene | A Cosa Serve |
|------|--------------|--------------|
| `prd-examples-compiled.md` | 4 PRD completamente compilati (MVP SaaS, Vibecoding, Feature Spec, PR/FAQ) con prodotti realistici | Reference master per capire il livello di dettaglio atteso per ogni tipo |
| `prd-anti-patterns.md` | I 15 anti-pattern documentati con esempi reali di PRD che falliscono | Permette alla skill di riconoscere e correggere PRD mal strutturati |
| `prd-quality-checklist.md` | La checklist completa in 5 livelli con il sistema di scoring 0-100 | Validation Engine — usata per il PRD Quality Report finale |
| `edge-cases-matrix.md` | Le 8 categorie di edge cases con esempi per ogni tipo di prodotto SaaS | Usata dal Context Enrichment Engine per popolare automaticamente gli edge cases |
| `success-metrics-library.md` | Database di metriche per categoria (retention, conversion, engagement, performance) con benchmark di settore | Permette di suggerire metriche realistiche con target basati su dati reali |

---

### 🟡 PRIORITÀ 2 — Prima Settimana

| File | Cosa Contiene | A Cosa Serve |
|------|--------------|--------------|
| `tech-stack-combinations.md` | Le 10 combinazioni tech stack più comuni per SaaS nel 2025 (Next.js+Supabase, Rails+Postgres, etc.) con pro/contro e use case ideale | Permette di suggerire o validare stack coerenti con il tipo di prodotto |
| `user-story-library.md` | 50+ user stories compilate per categoria (auth, payments, dashboard, onboarding, notifications) come reference | Accelera la generazione di user stories specifiche invece di generiche |
| `saas-compliance-requirements.md` | Requisiti GDPR, SOC2, HIPAA per SaaS EU — cosa includere nel PRD per ogni livello di compliance | Permette di aggiungere automaticamente la sezione compliance corretta |
| `pricing-models-saas.md` | 8 modelli di pricing SaaS (freemium, trial, usage-based, etc.) con implicazioni sui requisiti del PRD | Aiuta a strutturare correttamente la sezione billing e feature gating |
| `vibecoding-prompt-patterns.md` | Pattern di prompt collaudati per Cursor, Claude Code, Bolt, Lovable — come strutturare il PRD per massimizzare la qualità del codice generato | Ottimizza il Tipo D per ogni tool specifico di vibecoding |

---

### 🟢 PRIORITÀ 3 — Quando Disponibile

| File | Cosa Contiene | A Cosa Serve |
|------|--------------|--------------|
| `prd-real-examples-annotated.md` | PRD reali di aziende note (Intercom, Airbnb, Figma style) con annotazioni critiche su cosa funziona e cosa no | Benchmark qualitativo per calibrare il livello di dettaglio |
| `big-tech-frameworks.md` | Amazon Working Backwards, Shape Up di Basecamp, Google's PRD culture, Meta's product spec process — riassunti operativi | Permette di applicare framework specifici su richiesta |
| `persona-library.md` | 20 personas pre-costruite per i settori più comuni (SaaS B2B, marketplace, productivity, fintech, healthtech) | Accelera la fase di definizione del target utente |
| `analytics-events-library.md` | Database di eventi analytics standard per categoria di prodotto con properties e tool consigliati | Popola automaticamente la sezione Analytics & Tracking Spec |
| `post-launch-review-templates.md` | Template post-launch review in 3 formati (30gg, 90gg, annual review) | Permette alla skill di includere nel PRD il framework di review post-lancio |
🔄 SEZIONE 5 — TABELLA "COSA HO COSTRUITO E PERCHÉ"
Markdown

## DECISIONI ARCHITETTURALI — PRD ARCHITECT OS

| Decisione | Alternativa Scartata | Motivazione |
|-----------|---------------------|-------------|
| 4 Motori separati (Intake, Enrichment, Generation, Validation) | Un unico processo lineare | I 4 motori hanno logiche indipendenti. Separandoli, ogni motore può essere ottimizzato indipendentemente. L'Intake funziona anche se la Generation cambia. |
| Scala 0-100 per il PRD Quality Score | Semplice PASS/FAIL | Un score numerico permette di comunicare il grado di completezza — "il tuo PRD è a 67/100, mancano edge cases (15pt) e analytics spec (10pt)" è più utile di "FAIL". |
| 5 Tipi di PRD (A/B/C/D/E) | Un unico template universale | Un PRD enterprise di 30 pagine è inutile per un vibe coder solo. Un PR/FAQ di 1 pagina è insufficiente per un SaaS B2B con team di 20. I tipi risolvono questo disallineamento. |
| Domande divise in 3 Round | Tutte le domande subito | Bombardare l'utente con 15 domande crea attrito. 3 Round da max 5 domande, in ordine di priorità, è più umano e più efficace. |
| Inferito vs Dichiarato marcato esplicitamente | Generare tutto come se fosse confermato | La skill inferisce molto — ma se l'utente non lo sa, si fida ciecamente di dati non verificati. Il tag [INFERITO] crea accountability e forza la verifica. |
| 15 Anti-Pattern documentati | Solo checklist positiva | Gli anti-pattern sono il modo più efficace per imparare. Riconoscere un pattern sbagliato è più immediato che memorizzare ciò che è corretto. |
| Sezione AI Constraints nel Tipo D | Aspettarsi che l'AI capisca da sola | Senza constraints espliciti, Cursor/Claude aggiunge feature, cambia stack, inventa comportamenti. Le AI Constraints sono l'equivalente del .cursorrules ma integrato nel PRD. |
| Analytics Events come codice JavaScript | Descrizione testuale | Il codice JavaScript è direttamente copiabile dal developer o dall'AI che implementa il tracking. La descrizione testuale richiede traduzione intermedia. |
| Post-Launch Review come parte del PRD | Documento separato post-lancio | Se il framework di review è nel PRD originale, il team sa già al momento del design come valuterà il successo. Non è un afterthought — è parte del design. |