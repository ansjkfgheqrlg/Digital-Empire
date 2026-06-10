# claude-md-builder

> Source: File system (`SKILL & Agenti\SKILL\Agente Max\skills\claude-md-builder.md`)
> Collected: 2026-05-06
> Published: Unknown

# CLAUDE-MD-BUILDER — Protocollo Creazione e Ottimizzazione CLAUDE.md

Usa questo protocollo quando devi creare un file CLAUDE.md da zero, ottimizzare uno esistente, o scegliere il livello corretto (local/global/enterprise) per un progetto specifico.

**Riferimento KB:** K03-progetti.md per esempi pratici, K05-context.md per ottimizzazione token.

---

## FASE 1 — INTAKE

Raccogli queste informazioni prima di creare o modificare il CLAUDE.md:

**D1 — Livello target:**
"Per quale livello vuoi configurare CLAUDE.md? È per un progetto specifico (local), per tutte le tue sessioni (global), o per tutta l'azienda (enterprise)?"

**D2 — Tipo di progetto:**
"Cosa fa questo progetto? (es: sviluppo sito web, gestione contenuti, automazione business, analisi dati)"

**D3 — Comportamenti specifici:**
"Quali regole specifiche vuoi che Claude rispetti in questo contesto? Elenca i comportamenti che vuoi forzare o proibire."

**D4 — Integrazioni:**
"Ci sono skill, agenti, o MCP che Claude deve sapere di usare in questo progetto?"

---

## FASE 2 — GUIDA AI TRE LIVELLI

### Livello LOCAL (`.claude/CLAUDE.md` nella root del progetto)

**Quando usare:**
- Regole specifiche per un singolo progetto
- Istruzioni che non si applicano ad altri contesti
- Configurazioni di workflow proprie di quel progetto

**Esempi di contenuto:**
- "Questo è un sito e-commerce con stack Next.js + Supabase. Non modificare mai il database schema senza conferma esplicita."
- "Usa sempre il Task-Do-Verify cycle per questo progetto."
- "Il file principale è `src/app/page.tsx`. Non creare nuovi file senza prima leggere la struttura esistente."

**Posizione:** `[root-progetto]\.claude\CLAUDE.md`

---

### Livello GLOBAL (`C:\Users\Utente\.claude\CLAUDE.md`)

**Quando usare:**
- Regole identitarie che si applicano in TUTTE le sessioni
- Preferenze personali di comportamento
- Istruzioni di sicurezza universali

**Esempi di contenuto:**
- "Sei un assistente per Digital Empire. Sei diretto, preciso e professionale."
- "Prima di creare o eliminare file importanti, presenta sempre un piano."
- "Usa sempre percorsi Windows con backslash."
- "Non apportare mai modifiche destructive (rm -rf, drop database) senza conferma esplicita."

**Posizione:** `C:\Users\Utente\.claude\CLAUDE.md`

---

### Livello ENTERPRISE (configurazione organizzazione)

**Quando usare:**
- Regole di compliance aziendale
- Standard di sicurezza condivisi
- Workflow standardizzati per tutto il team

**Esempi di contenuto:**
- Regole su quali tool sono permessi
- Standard di naming e struttura file
- Procedure di sicurezza obbligatorie

---

## FASE 3 — CONTENT GUIDELINES

### Principio fondamentale: ogni regola guadagna il suo posto

Prima di aggiungere una regola, chiediti: "Claude Code rispetterebbe questo comportamento di default senza questa regola?" Se SÌ, non aggiungere la regola — è tokens sprecati.

### Struttura ottimale per un CLAUDE.md efficace:

```markdown
# [Titolo Progetto] — Istruzioni per Claude Code

## Regole Critiche
[INIZIO DEL FILE — primacy bias: queste regole hanno il massimo peso]
- [Regola non negoziabile 1]
- [Regola non negoziabile 2]

## Contesto del Progetto
- Stack tecnologico: [...]
- File chiave: [...]
- Pattern architetturali: [...]

## Workflow Standard
- [Come affrontare certi tipi di task]
- [Quando chiedere conferma]
- [Quali comandi usare]

## Non Fare Mai
- [Operazioni vietate esplicitamente]
- [Antipattern da evitare]

## Reminder Finale
[FINE DEL FILE — recency bias: questo viene riletto con attenzione]
[Istruzione che vuoi venga sempre considerata]
```

### Regole per scrivere regole efficaci:

1. **Concise:** Max 1-2 righe per regola. Se ne servono di più, la regola è troppo complessa.
2. **Specifiche:** "Non modificare il database schema" non "sii attento con il database"
3. **Actionable:** Devono descrivere un comportamento concreto, non un principio astratto
4. **Senza duplicati:** Se una regola è già nel CLAUDE.md globale, non ripeterla nel locale
5. **Senza contraddizioni:** Nessuna regola deve essere in conflitto con un'altra

---

## FASE 4 — CONFIGURAZIONI SPECIALI

### Abilitare il ciclo Task-Do-Verify:

```markdown
## Workflow Obbligatorio
Per ogni task complessa (creazione file, modifica struttura, configurazione):
1. TASK: definisci chiaramente cosa devi fare e il criterio di successo
2. DO: esegui
3. VERIFY: verifica il risultato contro il criterio di successo
4. Se la verifica fallisce: analizza, correggi, riesegui
```

### Configurare lo Screenshot Loop (per progetti frontend):

```markdown
## Frontend Development Protocol
Quando lavori su UI/frontend:
1. Implementa la modifica
2. Fai uno screenshot della pagina con il Chrome Dev Tool MCP
3. Analizza lo screenshot: la UI corrisponde alle aspettative?
4. Se NO: identifica il problema e correggi
5. Ripeti fino a che la UI è corretta visivamente
```

### Configurare Bypass Permission (per workflow autonomo):

```markdown
## Permission Mode
Per task di creazione/modifica file in questo progetto:
- Usa Bypass Permission per operazioni di routine (create, edit file)
- Richiedi conferma esplicita PRIMA di: eliminare file, modificare database, inviare richieste esterne
```

### Configurare sub-agenti specifici:

```markdown
## Sub-agenti Disponibili
In questo progetto sono disponibili e devono essere usati:
- @reviewer: per qualsiasi code review prima del commit
- @qa-tester: per test funzionali dopo modifiche significative
Invoca sempre questi agenti prima di consegnare lavoro finale.
```

---

## FASE 5 — TEMPLATES PRONTI ALL'USO

### Template: Progetto Web/App

```markdown
# [Nome Progetto Web] — Istruzioni Claude Code

## Regole Critiche
- Prima di modificare file esistenti: leggili sempre con Read
- Non eliminare mai file senza conferma esplicita
- Backup checkpoint prima di modifiche strutturali significative

## Stack Tecnologico
- Frontend: [Next.js / React / Vue / altro]
- Backend: [Node.js / Python / altro]
- Database: [Supabase / PostgreSQL / altro]
- Deploy: [Vercel / AWS / altro]

## File e Cartelle Chiave
- Entry point principale: [percorso]
- Configurazione: [percorso]
- Componenti: [percorso]

## Workflow Development
1. Leggi sempre i file esistenti prima di modificarli
2. Usa il ciclo Task-Do-Verify per ogni feature
3. Testa in locale prima di committare

## Vietato
- Modificare il database schema senza conferma
- Push diretto su main (usa sempre branch)
- Installare dipendenze senza discuterne prima

## Reminder Finale
Sei un assistente per Digital Empire. Lavora con precisione e consegna output production-ready.
```

---

### Template: Global CLAUDE.md (identità universale)

```markdown
# Identità e Regole Globali — Digital Empire

## Chi Sei
Sei l'assistente operativo di [Nome Utente] per Digital Empire.
Sei diretto, preciso e professionale. Non essere verbose.

## Regole Universali
- Usa sempre percorsi Windows con backslash (C:\Users\Utente\...)
- Prima di ogni task complessa: presenta un piano e attendi approvazione
- Non eliminare file senza conferma esplicita
- Riferisci sempre i tuoi ragionamenti con precisione

## Stile Comunicativo
- Risposte brevi e dirette
- No filler phrases ("Certamente!", "Ottima domanda!")
- Usa markdown per strutturare output complessi
- Cita sempre i file che stai modificando

## Reminder Finale
Produci sempre output production-ready, non approssimativo.
```

---

## FASE 6 — VALIDAZIONE

Prima di consegnare il CLAUDE.md, verifica:

- [ ] Livello corretto (local/global/enterprise)
- [ ] Regole critiche all'INIZIO del file (primacy bias)
- [ ] Reminder finale alla FINE del file (recency bias)
- [ ] Nessuna regola ridondante (già coperta da default Claude Code)
- [ ] Nessuna contraddizione interna tra regole
- [ ] Nessuna contraddizione con il livello superiore (global vs local)
- [ ] Sotto 50 righe per il global, sotto 80 righe per il local
- [ ] Percorsi Windows con backslash se presenti

---

## INSTALLAZIONE

Fornisci sempre queste istruzioni con il CLAUDE.md prodotto:

```
DOVE SALVARE IL FILE:

Livello Local:   [root-progetto]\.claude\CLAUDE.md
Livello Global:  C:\Users\Utente\.claude\CLAUDE.md

Se il file esiste già: aggiungilo alle sezioni esistenti, non sovrascrivere.
Riavvia Claude Code per applicare le modifiche.
Verifica con /config → sezione CLAUDE.md che il file venga riconosciuto.
```
