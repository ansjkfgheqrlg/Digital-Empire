# WF-ADR-REGISTER
## Handoff: HC-ME-ADR

## Trigger
- Qualsiasi team o Board prende una decisione architetturale o strategica rilevante
- Segnali tipici: "abbiamo deciso di…", "la scelta definitiva è…", "cambiamo approccio…",
  "adottiamo il pattern…", "dismissiamo il componente…"
- Chiamata diretta `empire-adr` skill da un agente o operatore
- ME-A06 rileva che un CP include decisioni non registrate come ADR

**Natura:** OBBLIGATORIO per decisioni architetturali/strategiche. Decisioni operative
minori (come formattare un file) non richiedono ADR.

---

## Input

```json
{
  "decisione": "la scelta presa in modo chiaro e inequivocabile",
  "contesto": "perché questa decisione si è resa necessaria",
  "alternative": [
    "opzione A: descrizione — scartata perché motivo",
    "opzione B: descrizione — scartata perché motivo"
  ],
  "conseguenze": "impatto atteso — positivo e negativo",
  "richiedente": "Board | ecosistema | agente",
  "priorita": "P0 | P1 | P2"
}
```

---

## Passi

```
1. RICEZIONE E VALIDAZIONE
   └── ME-A00 riceve HC-ME-ADR
   └── Valida campi obbligatori: decisione, contesto, alternative, conseguenze
   └── Se incompleto → richiede integrazione, non procede

2. DRAFT ADR (ME-A05 — ADR Registrar)
   ├── Lista ADR-*.md esistenti in decisions/ → trova ultimo NNN
   ├── Assegna ADR-(NNN+1)
   ├── Compila template ADR completo
   └── Stato iniziale: "proposto" (non ancora "attivo")

3. CONTRADICTION CHECK (ME-A06 — Contradiction Checker)
   ├── Carica tutti gli ADR con stato=attivo
   ├── skill-contradiction-analyzer(draft ADR, ogni ADR attivo)
   ├── Classifica: OK | WARNING | CONFLITTO
   └── Produce report strutturato

4. BRANCH DECISIONALE
   ├── OK:
   │   ME-A05: aggiorna stato → "attivo"
   │   Salva ADR-NNN.md
   │   Aggiorna INDEX.md con voce ADR
   │   ME-A09: sync wiki/log.md + AgentDB memory/decisions
   │   Restituisce ADR-id a richiedente
   │
   ├── WARNING:
   │   ME-A05: aggiorna stato → "attivo" con nota ⚠️
   │   Salva ADR-NNN.md (include sezione warning)
   │   Log warning in audit/
   │   Stessa procedura OK per sync/INDEX
   │
   └── CONFLITTO:
       ADR rimane in stato "proposto" (NON salvato come attivo)
       ME-A00 notifica Board con:
         - ADR draft
         - ADR con cui è in conflitto
         - descrizione del conflitto
       Task richiedente messo in pausa
       Attende risoluzione Board prima di procedere

5. CONFERMA
   └── ADR-id restituito al richiedente (o escalation Board se CONFLITTO)
```

---

## Gate

- **G-ME3:** contradiction-check obbligatorio — nessun ADR passa a "attivo" senza di esso
- **Conflitto:** blocca sia l'ADR che il task che lo ha generato (no workaround)
- **Template completo:** ADR con sezioni vuote non viene registrato

---

## Output

```json
{
  "adr_id": "ADR-NNN",
  "stato": "attivo | proposto (se conflitto)",
  "contradiction_check": "OK | WARNING | CONFLITTO",
  "conflitto_con": "ADR-X (se CONFLITTO)",
  "timestamp": "ISO8601"
}
```

---

## Criteri per "questa decisione richiede un ADR?"

| Tipo decisione | ADR richiesto? |
|---|---|
| Adozione di un pattern architetturale | SI |
| Scelta di stack tecnologico | SI |
| Cambio di struttura filesystem | SI |
| Politica operativa (es. "no overwrite") | SI |
| Decisione strategica (pricing, positioning) | SI |
| Formattazione di un singolo file | NO |
| Scelta di nome variabile | NO |
| Fix di bug ovvio | NO |

---

## Note

- Skill da creare: `empire-adr` (P1 — da ordinare a FORGE)
- Un task che genera decisioni senza HC-ME-ADR: ME-A10 rileverà CP con campo
  "decisioni_prese" non vuoto ma senza ADR corrispondente → alert

---

## Connessioni
- [[09-ECOSISTEMA-MEMORY]] — workflow definito in §5 (WF-DECISION)
- [[ME-A05-adr-registrar]] — passo 2
- [[ME-A06-contradiction-checker]] — passo 3
- [[ME-A00-memory-conductor]] — entry point e destinatario escalation
- [[M3-ADR]] — reparto che esegue questo workflow
- [[WF-POST-TASK-COMMIT]] — il CP del task include il campo "decisioni_prese → ADR-NNN"
