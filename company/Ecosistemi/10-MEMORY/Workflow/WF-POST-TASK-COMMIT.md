# WF-POST-TASK-COMMIT
## Handoff: HC-ME-POST (commit obbligatorio)

## Trigger
- Task dichiarato chiuso da qualsiasi agente o operatore
- Hook UserPromptSubmit: se Claude Code rileva frase di chiusura task ("fatto", "completato",
  "finito", "consegnato") → reminder automatico per avviare HC-ME-POST
- Reminder esplicito da ME-A10 (Sentinel) se task risulta chiuso senza CP dopo N minuti

**Natura:** OBBLIGATORIO e verificato. Un task è "chiuso" solo quando ha ricevuto
un CP-id confermato da ME-A03. Prima del CP-id, il task è "in attesa di commit".

---

## Input

```json
{
  "task_id": "deve corrispondere al task_id del PRE-GATE precedente",
  "gate_id": "PRE-NNN corrispondente (per verifica accoppiamento)",
  "ecosistema": "string",
  "esito": "completato | parziale | fallito",
  "output_paths": ["path1/file.md", "path2/file.md"],
  "decisioni_prese": ["ADR-NNN se create durante il task"],
  "lezioni": "cosa ha funzionato, cosa no, cosa fare diversamente",
  "costi": "token/crediti/€ se applicabile",
  "prossimo_passo": "primo passo del task successivo"
}
```

---

## Passi

```
1. RICEZIONE
   └── ME-A00 (Conductor) riceve HC-ME-POST
   └── Valida accoppiamento: gate_id PRE-NNN corrisponde a task_id?
   └── Se payload incompleto → richiede integrazione (non scrive CP parziale)

2. SCRITTURA CP (ME-A03 — Checkpoint Writer)
   ├── Determina numero progressivo NNN leggendo ultimo CP in checkpoints/
   ├── Compila template CP completo con tutti i campi
   ├── Salva company/Memory/checkpoints/CP-YYYYMMDD-NNN.md
   ├── Appende voce in INDEX.md
   └── Aggiorna STATO-EMPIRE.md sezione "Ultimo task"
   Output: CP-id confermato (es. "CP-20260613-001")

3. AGGIORNAMENTO STATO (ME-A08 — State Tracker)
   ├── Legge filesystem (non dichiara) → costruisce stato aggiornato
   ├── Aggiorna state/<progetto>/state.json
   └── Appende evento a trace.jsonl

4. SYNC (ME-A09 — Wiki Syncer)
   ├── Entry in wiki/log.md: "CP-NNN: [ecosistema] [esito] [summary]"
   └── memory_store(namespace="memory/checkpoints", id=CP-id, content=CP)

5. LEZIONI A REASONINGBANK
   └── Se CP ha sezione "lezioni" non vuota:
       ME-A09 estrae e propaga su AgentDB namespace "patterns"

6. CONFERMA
   └── ME-A00 restituisce CP-id al richiedente
   └── Task ora ufficialmente CHIUSO
   └── PRE-NNN accoppiato al POST → orfano eliminato dal radar ME-A10
```

---

## Gate

- **CP-id obbligatorio:** nessun handoff downstream è valido senza CP-id
- **Template completo:** CP con sezioni vuote obbligatorie non viene accettato
- **Accoppiamento PRE/POST:** se gate_id mancante, ME-A10 verrà notificato dell'orfano

---

## Output

```json
{
  "cp_id": "CP-YYYYMMDD-NNN",
  "task_id": "echo",
  "stato": "CHIUSO",
  "sync_wiki": "ok | warning",
  "sync_agentdb": "ok | warning | ritentato",
  "timestamp": "ISO8601"
}
```

---

## Nota sull'accoppiamento PRE/POST

```
PRE-20260613-001 → [task X eseguito] → POST con gate_id=PRE-20260613-001
```

ME-A10 lista tutti i PRE senza POST corrispondente → questi sono task "in volo" o
task chiusi senza CP. Se un PRE è orfano da > 2h → alert.

---

## Note

- Skill da creare: `empire-checkpoint` (P0 — da ordinare a FORGE)
- Hook Claude Code: UserPromptSubmit reminder se frase di chiusura task rilevata
- Il costo del CP: target ≤ 30 secondi di overhead sul task (ME-A03 compila il template)

---

## Connessioni
- [[09-ECOSISTEMA-MEMORY]] — workflow definito in §5
- [[ME-A00-memory-conductor]] — entry point
- [[ME-A03-checkpoint-writer]] — passo 2
- [[ME-A08-state-tracker]] — passo 3
- [[ME-A09-wiki-syncer]] — passo 4-5
- [[WF-PRE-TASK-GATE]] — workflow accoppiato (pre-task)
- [[M2-CHECKPOINT-SESSIONI]] — reparto che esegue questo workflow
