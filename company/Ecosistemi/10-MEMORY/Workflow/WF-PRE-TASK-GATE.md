# WF-PRE-TASK-GATE
## Handoff: HC-ME-PRE (gate bloccante — pattern #13)

## Trigger
- Qualsiasi team o agente sta per iniziare un nuovo task
- Hook UserPromptSubmit (Claude Code) quando viene dichiarata un'intenzione di task
- Chiamata diretta `empire-memory-gate` skill da un agente

**Natura:** BLOCCANTE. Il task NON può partire senza che il context-pack sia stato
consegnato. Se il gate non risponde entro 30s → task in attesa, non in esecuzione.

---

## Input

```json
{
  "task_id": "identificativo univoco del task",
  "ecosistema": "01-AGENCY | 02-FORGE | ... | 10-MEMORY",
  "descrizione": "cosa si sta per fare (1-3 frasi)",
  "keywords": ["keyword1", "keyword2"],
  "richiedente": "nome agente o operatore"
}
```

---

## Passi

```
1. RICEZIONE
   └── ME-A00 (Conductor) riceve HC-ME-PRE
   └── Valida che il payload abbia i campi obbligatori
   └── Se incompleto → restituisce lista campi mancanti (non procede)

2. CARICAMENTO (ME-A01 — Context Loader)
   ├── Legge INDEX.md → mappa completa conoscenza
   ├── Legge STATO-EMPIRE.md → stato corrente
   ├── Legge ultima sessione sessions/ → RIPRESA DA:
   ├── Filtra CP in checkpoints/ per ecosistema + keywords
   ├── Filtra ADR in decisions/ con stato=attivo
   └── Chiama memory_search(AgentDB, query=descrizione) → pattern/CP semantici
   Output: context-pack grezzo

3. SCORING (ME-A02 — Relevance Scorer)
   ├── Ordina CP per rilevanza (ecosistema + keywords + data)
   ├── Filtra ADR per pertinenza al task
   ├── Check contraddizioni leggero: il task viola qualche ADR attivo?
   ├── Taglia a max N item (default: 3 CP, 5 ADR, 5 pattern)
   └── Produce summary 3-5 righe
   Output: context-pack finale

4. GATE DI CONTRADDIZIONE
   ├── Contraddizione leggera → context-pack include warning, task procede
   └── Contraddizione diretta con ADR attivo → STOP:
       ME-A00 notifica Board + richiedente
       task messo in pausa fino a risoluzione Board

5. CONSEGNA
   └── ME-A00 restituisce context-pack finale al richiedente
   └── Timestamp gate registrato (per audit: ogni PRE deve avere POST)
   └── Task può ora partire
```

---

## Gate

- **Tempo massimo:** 30 secondi dall'invio HC-ME-PRE alla ricezione context-pack
- **Bloccante:** nessun task parte senza context-pack consegnato
- **Contraddizione dura:** task sospeso fino a risoluzione Board (non self-service)

---

## Output

```json
{
  "gate_id": "PRE-YYYYMMDD-NNN",
  "task_id": "echo del task_id ricevuto",
  "context_pack": {
    "summary": "3-5 righe stato holding + RIPRESA DA",
    "cp_rilevanti": ["CP-NNN: 1-riga", "..."],
    "adr_attivi": ["ADR-NNN: decisione", "..."],
    "pattern_utili": ["..."],
    "warnings": ["se presenti"]
  },
  "esito_gate": "PASS | WARN | BLOCK",
  "timestamp": "ISO8601"
}
```

---

## Note

- Il `gate_id` (PRE-NNN) viene accoppiato al successivo HC-ME-POST:
  ogni POST deve riferirsi al PRE corrispondente → ME-A10 verifica gli orfani
- Skill da creare: `empire-memory-gate` (P0 — priorità massima, da ordinare a FORGE)
- Hook Claude Code attivo: UserPromptSubmit → reminder pre-task gate

---

## Connessioni
- [[09-ECOSISTEMA-MEMORY]] — workflow definito in §5
- [[ME-A00-memory-conductor]] — entry point del workflow
- [[ME-A01-context-loader]] — passo 2
- [[ME-A02-relevance-scorer]] — passo 3
- [[WF-POST-TASK-COMMIT]] — workflow complementare (post-task)
- [[M1-RECALL-PRETASK]] — reparto che esegue questo workflow
