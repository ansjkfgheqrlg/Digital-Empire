# agent-forge

> Source: File system (`SKILL & Agenti\SKILL\Agente Max\skills\agent-forge.md`)
> Collected: 2026-05-06
> Published: Unknown

# AGENT-FORGE — Protocollo Creazione Agenti

Usa questo protocollo quando devi creare un nuovo agente Claude Code completo, con frontmatter corretto e system prompt strutturato e professionale.

---

## FASE 1 — INTAKE

Prima di procedere, raccogli queste informazioni (se non già presenti nel prompt):

**Domanda 1 — Dominio specialistico:**
"Di cosa è esperto questo agente? Qual è il suo campo di specializzazione? Es: 'esperto di email marketing', 'analista finanziario', 'reviewer di codice Python'."

**Domanda 2 — Trigger e routing:**
"Quando vuoi che questo agente si attivi? Elenca 3-5 situazioni o frasi che devono triggerarlo. Cosa NON deve gestire (per delimitare il confine con altri agenti)?"

**Domanda 3 — Strumenti e modello:**
"L'agente deve creare file? Navigare il web? Eseguire comandi? Ha bisogno di ragionamento profondo (opus) o è sufficiente velocità (sonnet)? Colore preferito per l'UI?"

---

## FASE 2 — ANATOMIA DELL'AGENTE

### Differenza fondamentale Agente vs Skill:

| | Agente | Skill |
|--|--------|-------|
| Prospettiva | Seconda persona ("you are") | Forma imperativa ("analizza") |
| Attivazione | Automatica tramite description routing | Invocata esplicitamente |
| Persistenza | Mantiene identità attraverso la sessione | Procedura one-shot |
| Sistema prompt | Lungo, identità + processo + vincoli | Istruzioni operative |

### Struttura file agente (nome-agente.md):

```
--- [YAML FRONTMATTER] ---
name: nome-agente
description: [routing description — vedi FASE 3]
model: [sonnet | opus | haiku]
color: [magenta | blue | green | yellow | red | cyan]
tools: ["Read", "Write", "Edit", ...lista minima necessaria]
---

## IDENTITY
[Chi sei, cosa NON sei, principio fondamentale]

## MISSION
[Obiettivo primario in 2-3 frasi]

## PROCESS
[Steps numerati: cosa fai, in quale ordine, con quali gate]

## OUTPUT CONTRACT
[Cosa produci, in quale formato, con quale qualità]

## CONSTRAINTS
Never: [lista vincoli negativi]
Always: [lista vincoli positivi]
```

---

## FASE 3 — DESCRIPTION ENGINEERING PER AGENTI

La description è il meccanismo di routing di Claude Code. Deve rispondere alla domanda: "Quando devo attivare questo agente invece di rispondere direttamente?"

### Struttura obbligatoria:

```
Use this agent when [CONDIZIONI SPECIFICHE]. Also activate when the user says
"[trigger1]", "[trigger2]", "[trigger3]" or any variation.

<example>
Context: [situazione specifica che triggera l'agente]
user: "[messaggio tipico dell'utente]"
assistant: "[come l'agente presenta se stesso o annuncia l'attivazione]"
<commentary>
[spiegazione perché questo caso triggera l'agente]
</commentary>
</example>

<example>
Context: [secondo caso d'uso]
user: "[secondo messaggio tipico]"
assistant: "[risposta dell'agente]"
<commentary>
[perché questo secondo caso è rilevante]
</commentary>
</example>
```

### Regole per la description:

1. **Inizia sempre con "Use this agent when..."** — è il pattern standard Claude Code
2. **Includi le trigger phrases in italiano** (il tuo ecosistema è in italiano)
3. **Minimum 2 esempi** con tag `<example>`, `<commentary>`
4. **Delimita** cosa l'agente NON gestisce per evitare conflitti con altri agenti
5. **Gli esempi devono essere realistici** — usa frasi che l'utente direbbe davvero

---

## FASE 4 — SYSTEM PROMPT ARCHITECTURE

### IDENTITY section:

```markdown
## IDENTITY

You are [nome-agente], [ruolo specifico] for [contesto/azienda].
You are not a general assistant — you are a specialized expert in [dominio].

Your fundamental principle: [principio cardine in una frase].
```

**Regole:**
- Seconda persona ("you are", "you must", "your")
- Stabilisci immediatamente cosa NON sei (delimita per evitare drift)
- Il principio fondamentale deve essere memorabile e specifico

### MISSION section:

```markdown
## MISSION

[2-3 frasi che descrivono l'obiettivo primario dell'agente. Cosa trasforma?
Da cosa a cosa? Per chi? Con quale risultato atteso?]
```

### PROCESS section:

```markdown
## PROCESS

1. **[STEP 1 — nome]** — [descrizione azione concreta]
2. **[STEP 2 — nome]** — [descrizione azione concreta]
3. **[STEP 3 — nome]** — [descrizione azione concreta]
   → Gate: [condizione che deve essere vera prima di procedere]
4. **[STEP 4 — nome]** — [descrizione azione concreta]
5. **[STEP 5 — VERIFY]** — [checklist di verifica pre-output]
```

**Regole del PROCESS:**
- Numerato sequenzialmente
- Ogni step ha un nome in maiuscolo (ACTION)
- I gate obbligatori sono esplicitati con "→ Gate:"
- L'ultimo step è sempre VERIFY con una checklist

### OUTPUT CONTRACT section:

```markdown
## OUTPUT CONTRACT

For [tipo di output 1]: [formato esatto, lunghezza, struttura]
For [tipo di output 2]: [formato esatto, lunghezza, struttura]
For [tipo di output 3]: [formato esatto, lunghezza, struttura]

Before delivering any output, verify:
- [ ] [criterio 1]
- [ ] [criterio 2]
- [ ] [criterio 3]
```

### CONSTRAINTS section:

```markdown
## CONSTRAINTS

Never:
- [vincolo negativo 1]
- [vincolo negativo 2]
- [vincolo negativo 3]

Always:
- [vincolo positivo 1]
- [vincolo positivo 2]
- [vincolo positivo 3]
```

---

## FASE 5 — TOOL SELECTION GUIDE

### Principio: minimo necessario

Non aggiungere tool non usati. Ogni tool aggiunto consuma contesto e aumenta la superficie di rischio.

```
Read           → L'agente deve leggere file esistenti
Write          → L'agente deve creare nuovi file
Edit           → L'agente deve modificare file esistenti
Glob           → L'agente deve trovare file per pattern
Grep           → L'agente deve cercare testo nei file
Bash           → L'agente deve eseguire comandi (ATTENZIONE: rischio alto)
WebSearch      → L'agente deve cercare informazioni online
WebFetch       → L'agente deve leggere pagine web specifiche
TodoWrite      → L'agente gestisce task multi-step
```

**Per agenti di analisi/risposta:** Read, Glob, Grep
**Per agenti di creazione:** Read, Write, Edit
**Per agenti operativi completi:** Read, Write, Edit, Glob, Grep, Bash, TodoWrite
**Per agenti di ricerca:** WebSearch, WebFetch, Read

---

## FASE 6 — PROCESSO DI CREAZIONE

1. **Raccogli le 3 risposte INTAKE**

2. **Scegli il modello:**
   - `opus` → ragionamento profondo, pianificazione strategica, output complessi
   - `sonnet` → operazioni veloci, creazione file, task strutturati (default)
   - `haiku` → task semplici, risposte rapide, bassa complessità

3. **Scrivi la description** con il pattern "Use this agent when..." + 2 esempi

4. **Crea il file `nome-agente.md`** con il frontmatter completo

5. **Scrivi il system prompt** con tutte e 5 le sezioni: IDENTITY, MISSION, PROCESS, OUTPUT CONTRACT, CONSTRAINTS

6. **Esegui il QUALITY CHECKLIST**

---

## QUALITY CHECKLIST PRE-DELIVERY

- [ ] `name` è lowercase con hyphens
- [ ] `description` inizia con "Use this agent when..."
- [ ] `description` contiene trigger phrases in italiano
- [ ] Almeno 2 `<example>` blocks nella description
- [ ] `model` è uno di: opus, sonnet, haiku
- [ ] `color` è uno dei colori validi
- [ ] `tools` è una lista di stringhe valide (non stringa singola)
- [ ] System prompt è interamente in seconda persona
- [ ] Ha tutte le 5 sezioni: IDENTITY, MISSION, PROCESS, OUTPUT CONTRACT, CONSTRAINTS
- [ ] PROCESS ha almeno 3 step numerati
- [ ] OUTPUT CONTRACT specifica il formato di ogni tipo di output
- [ ] CONSTRAINTS ha sia "Never:" che "Always:"

---

## INSTALLAZIONE AGENTE

Al termine della creazione, fornisci queste istruzioni:

```
INSTALLAZIONE:

Copia il file nome-agente.md in:

Globale (disponibile in tutti i progetti):
  C:\Users\Utente\.claude\agents\

Locale (solo questo progetto):
  .claude\agents\   ← nella root del progetto

Riavvia Claude Code. L'agente sarà disponibile automaticamente.
Per invocarlo manualmente: scrivi @nome-agente nel prompt.
```
