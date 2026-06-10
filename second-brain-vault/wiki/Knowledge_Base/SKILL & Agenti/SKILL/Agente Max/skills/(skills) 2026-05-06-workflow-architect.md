# workflow-architect
            
> Path: [[Map - Skill_And_Agenti|SKILL & Agenti > SKILL > Agente Max > skills]]

## Content

# WORKFLOW-ARCHITECT — Protocollo Pianificazione Workflow Complessi

Usa questo protocollo quando devi progettare un workflow multi-step, multi-agente o multi-skill. Non eseguire il workflow — pianificalo, documentalo, e mostra all'utente l'intera architettura prima di costruire qualsiasi componente.

---

## FASE 1 — INTAKE

Raccogli queste informazioni prima di procedere:

**Domanda 1 — Processo da automatizzare:**
"Descrivi il processo che vuoi automatizzare dall'inizio alla fine. Cosa succede oggi manualmente, step per step?"

**Domanda 2 — Input e output:**
"Cosa entra nel processo? (es: un brief del cliente, un URL, un file Excel)
Cosa deve uscire? (es: un documento PDF, una serie di post, un report)"

**Domanda 3 — Risorse disponibili:**
"Quali skill, agenti o MCP hai già installati e funzionanti? Cosa sei disposto a costruire ex-novo?"

**Domanda 4 — Vincoli:**
"Ci sono parti del processo che DEVONO essere confermate da te manualmente prima di procedere? Quali sono le operazioni più rischiose (file critici, invio email, pubblicazione)?"

---

## FASE 2 — CLASSIFICAZIONE DEL WORKFLOW

Classifica il workflow prima di progettarlo:

### Tipo A — LINEARE
```
Step 1 → Step 2 → Step 3 → Output
```
Quando: ogni step dipende dal precedente. Semplice, sequenziale.

### Tipo B — RAMIFICATO
```
Input → Analisi → [Percorso A] o [Percorso B]
                       ↓               ↓
                  Output A         Output B
```
Quando: il percorso cambia in base a condizioni (es: "se il prodotto è B2B → percorso A, se B2C → percorso B").

### Tipo C — PARALLELO
```
Input → ┬→ Task A (sub-agente) ─┐
         ├→ Task B (sub-agente) ─┼→ Aggregazione → Output
         └→ Task C (sub-agente) ─┘
```
Quando: più task indipendenti possono essere eseguiti contemporaneamente. Usa sub-agenti o Agent Tool.

### Tipo D — IBRIDO
Combinazione di A, B, C. Per workflow complessi con fasi diverse.

---

## FASE 3 — DECOMPOSIZIONE IN TASK ATOMICHE

Scomponi il processo in task atomiche — unità minime che:
- Hanno un input chiaro
- Producono un output chiaro
- Possono essere verificate autonomamente
- Possono essere assegnate a un singolo agente/skill

### Metodo di decomposizione:

Per ogni fase del processo, definisci:
```
TASK: [nome breve]
Input: [cosa riceve]
Processo: [cosa fa]
Output: [cosa produce]
Verificabile: [come si verifica che abbia fatto bene]
Agente/Skill: [chi esegue: cc-master | skill esistente | nuovo agente | nuovo agente da creare]
Checkpoint umano: [SI / NO — richiede approvazione dell'utente?]
```

---

## FASE 4 — RESOURCE MAPPING

Per ogni task atomica, mappa la risorsa disponibile:

```
MAPPA RISORSE
═════════════════════════════════════════════════════
Task                 → Risorsa        → Stato
─────────────────────────────────────────────────────
[task 1]             → [skill esistente]  → DISPONIBILE
[task 2]             → [agente esistente] → DISPONIBILE
[task 3]             → [skill da creare]  → DA COSTRUIRE
[task 4]             → [MCP necessario]   → DA INSTALLARE
[task 5]             → [cc-master]        → DISPONIBILE
═════════════════════════════════════════════════════
```

**Regola del minimo necessario:** Prima di creare qualcosa di nuovo, verifica se cc-master o una skill esistente può già gestire quel task.

---

## FASE 5 — RISK ANALYSIS

Identifica e classifica i rischi di ogni task:

### Matrice rischi:

```
TASK              | Reversibile? | Impatto errore | Checkpoint?
──────────────────|──────────────|────────────────|────────────
[task creazione]  | SI           | BASSO          | NO
[task invio email]| NO           | ALTO           | SI ← obbligatorio
[task delete file]| NO           | CRITICO        | SI ← obbligatorio
[task pubblicaz.] | difficile    | ALTO           | SI ← obbligatorio
[task analisi]    | SI           | BASSO          | NO
```

**Regola checkpoint:** Qualsiasi operazione NON reversibile con impatto MEDIO o superiore richiede un checkpoint umano esplicito.

---

## FASE 6 — STIMA COSTI TOKEN

Stima il consumo approssimativo per sessione:

```
STIMA COSTI
═══════════════════════════════════════
Componente            | Token stimati
──────────────────────|──────────────
Agent Teams (se usati)| 10.000-80.000 per sessione
Sub-agenti (ognuno)   | 2.000-20.000 per task
Skill invocata        | 500-2.000 per invocazione
KB module letto       | 7.500-17.000 per lettura
═══════════════════════════════════════
TOTALE STIMATO: [somma]
RACCOMANDAZIONE: [sub-agenti vs agent team vs skill diretta]
```

**Principio ROI (dal Capitolo 26):** Se il workflow sarà ripetuto molte volte, vale investire in una skill dedicata che costerà ~€0.01 per invocazione invece di ~€10-80 per Agent Team.

---

## FASE 7 — OUTPUT DEL WORKFLOW DOCUMENT

Produci un documento Markdown con questa struttura:

```markdown
# WORKFLOW: [Nome Processo]

## Overview
[2-3 frasi che descrivono cosa fa il workflow dall'inizio alla fine]

**Tipo:** [Lineare | Ramificato | Parallelo | Ibrido]
**Input:** [cosa riceve]
**Output finale:** [cosa produce]
**Tempo stimato:** [per esecuzione manuale vs automatizzata]
**Costo token stimato:** [per sessione]

---

## Diagramma del Flusso

```
[INPUT]
    │
    ▼
[TASK 1: nome] ──→ [Output parziale A]
    │
    ▼
[TASK 2: nome]
    │
    ├──(condizione X)──→ [TASK 3a] ──→ [Output B]
    │
    └──(condizione Y)──→ [TASK 3b] ──→ [Output C]
    │
    ▼
[CHECKPOINT UMANO ✋] ← richiede approvazione
    │
    ▼
[OUTPUT FINALE]
```

---

## Task Details

### TASK 1: [nome]
- **Input:** [cosa riceve]
- **Processo:** [cosa fa]
- **Output:** [cosa produce]
- **Eseguito da:** [skill/agente/cc-master]
- **Checkpoint:** NO

### TASK 2: [nome]
[...ripeti per ogni task...]

---

## Componenti da Costruire

| Componente | Tipo | Priorità | Stima effort |
|------------|------|----------|--------------|
| [nome] | skill | ALTA | 30 min |
| [nome] | agente | MEDIA | 1 ora |
| [nome] | MCP | BASSA | 15 min |

---

## Sequenza di Implementazione

1. [ ] Installa [componente prerequisito]
2. [ ] Crea skill [nome] (necessaria per Task X)
3. [ ] Crea agente [nome] (necessario per Task Y)
4. [ ] Testa il workflow end-to-end con input di prova
5. [ ] Ottimizza in base ai risultati del test
```

---

## FASE 8 — SEQUENZA DI IMPLEMENTAZIONE

Dopo che il workflow document è approvato dall'utente, pianifica la costruzione nell'ordine giusto:

**Regola:** Costruisci i prerequisiti prima delle dipendenze. Il componente più fondamentale prima.

**Ordine tipico:**
1. Installa MCP necessari (prerequisiti infrastrutturali)
2. Crea skill di base (componenti riusabili)
3. Crea agenti specializzati (usano le skill come strumenti)
4. Configura CLAUDE.md con le regole del workflow
5. Testa ogni componente singolarmente
6. Testa il workflow end-to-end con input reale (non di produzione)
7. Vai live

---

## QUALITÀ: CRITERI DI UN BUON WORKFLOW DOCUMENT

- [ ] Ogni task ha input e output chiaramente definiti
- [ ] Tutti i checkpoint umani sono esplicitamente segnalati
- [ ] Le operazioni irreversibili hanno checkpoint
- [ ] Il diagramma ASCII è leggibile e completo
- [ ] La stima costi token è presente
- [ ] La lista componenti da costruire è completa con priorità
- [ ] La sequenza di implementazione è ordinata correttamente (prerequisiti prima)

## Collegamenti Correlati
- [[Knowledge_Base/Formazzione/manuale-completo-claude-code-business/parte-delle-volte-gli-hook-garantiscono-questa-affidabilità-per-le-parti-critiche-del-workflow/capitolo-38/(capitolo-38) overview|overview]]
- [[Map - Agenti|Agenti Area]]
- [[Map - App|App Area]]
