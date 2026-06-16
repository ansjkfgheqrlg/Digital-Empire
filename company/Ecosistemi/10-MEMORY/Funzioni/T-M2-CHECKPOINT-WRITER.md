> Fonte: PIANO-MAESTRO/09-ECOSISTEMA-MEMORY.md sez. 3 (Reparto M2 — Checkpoint & Sessioni)

# T-M2-CHECKPOINT-WRITER — Funzione Checkpoint Writer

> Layer funzione condiviso · Livello: L3 · Usato da: ME-A03 checkpoint-writer, ME-A04 session-logger
> Ecosistema: `company/Ecosistemi/10-MEMORY/ECOSISTEMA.md`
> Backbone: `company/Ecosistemi/10-MEMORY/BACKBONE.md`

---

## Identità funzione

| Campo | Valore |
|---|---|
| Funzione ID | T-M2-CHECKPOINT-WRITER |
| Capability servite | checkpoint-write, index-update, stato-update, session-open, session-close |
| Reparto owner | M2 — Checkpoint & Sessioni |
| Stato | ATTIVO — trigger: HC-ME-POST e apertura/chiusura sessione |
| Tier modello | haiku (scrittura strutturata) |
| Pattern critico | backup→append→log→rollback (MAI overwrite — da Memory Empire) |

---

## Contratto funzione (non negoziabile)

| Operazione | Input | Output |
|---|---|---|
| `write_checkpoint(payload)` | HC-ME-POST payload completo | `{cp_id, path}` confermato |
| `update_index(cp_id)` | id e titolo del CP appena scritto | INDEX.md aggiornato con entry 1-riga |
| `update_stato(campo, valore)` | campo STATO-EMPIRE + nuovo valore | STATO-EMPIRE.md aggiornato |
| `open_session()` | data + "RIPRESA DA:" estratto da STATO | session-YYYYMMDD.md creato |
| `close_session(cp_sessione)` | summary sessione + prossimo passo | session log chiuso + STATO aggiornato |

---

## Template CP obbligatorio (da dossier §2)

```markdown
# CP-YYYYMMDD-NNN — <titolo task>
- Ecosistema/Reparto: …
- Task: … (rif. piano/fase)
- Esito: ✅ completato | ⚠️ parziale | ❌ fallito
- Output: <path reali prodotti>
- Decisioni prese: <link ADR se create>
- Lezioni/errori: <per ReasoningBank>
- Costi: <token/crediti/€ se applicabile>
- Prossimo passo: …
```

---

## Flusso operativo (HC-ME-POST)

```
HC-ME-POST ricevuto {task_id, esito, output_paths, lezioni, costi}
  1. Genera CP-id sequenziale: leggi ultimo ID in checkpoints/ → +1
  2. Compila template CP dal payload ricevuto
  3. Scrivi file: company/Memory/checkpoints/CP-YYYYMMDD-NNN.md
     (APPEND, mai sovrascrivere un CP esistente)
  4. Aggiorna company/Memory/INDEX.md: aggiungi riga 1-liner
     formato: | CP-NNN | YYYYMMDD | ecosistema | titolo | esito |
  5. Aggiorna company/Memory/STATO-EMPIRE.md:
     - "ultimo CP:" → nuovo id
     - "RIPRESA DA:" → prossimo passo dal CP
     - "lavori in corso:" → rimuovi il task completato
  6. memory_store(AgentDB "memory/checkpoints", {cp_id, titolo, keywords, path})
  7. Ritorna {cp_id, path} al team committente
     (senza questo ack il task rimane APERTO per la Memory-Sentinel)
```

---

## Regole operative

1. **CP-id è il sigillo di chiusura**: nessun team può dichiarare un task CHIUSO senza CP-id confermato da questa funzione.
2. **MAI overwrite**: se un CP già esiste con lo stesso ID → errore esplicito, genera ID successivo.
3. **Lezioni obbligatorie**: campo `lezioni/errori` non può essere vuoto. Se il team non lo fornisce → richiedere, non omettere.
4. **Session close**: la chiusura sessione include sempre il "RIPRESA DA:" — frase breve che un agente nuovo può leggere per ripartire senza contesto pregresso.

---

## Connessioni

- `company/Ecosistemi/10-MEMORY/ECOSISTEMA.md` — organigramma completo
- `company/Ecosistemi/10-MEMORY/BACKBONE.md` — namespace AgentDB `memory/checkpoints`
- `company/Ecosistemi/10-MEMORY/Agenti/ME-A03-checkpoint-writer.md` — agente che esegue questa funzione
- `company/Ecosistemi/10-MEMORY/Agenti/ME-A04-session-logger.md` — agente sessioni
- `company/Ecosistemi/10-MEMORY/Workflow/WF-POSTTASK.md` — workflow che orchestra questa funzione
- `PIANO-MAESTRO/09-ECOSISTEMA-MEMORY.md` §2 (template CP), §3 (M2), §5

*Fonte: dossier 09 §2 (template CP), §3 (M2), §5 (WF-POSTTASK) · Aggiornato: 2026-06-12*
