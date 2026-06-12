> Fonte: PIANO-MAESTRO/09-ECOSISTEMA-MEMORY.md sez. 3 M2

# L2 — M2 · CHECKPOINT & SESSIONI

**Ecosistema:** 10-MEMORY · **Direttore:** ME-Conductor
**Workflow L3:** T-M2.1 Checkpoint Writer · T-M2.2 Session Logger
**Connessione:** [[../ECOSISTEMA.md]] · [[../BACKBONE.md]]

## Missione

Ogni task chiuso lascia una traccia; ogni sessione ha apertura e chiusura formale.
M2 implementa il lato "DOPO ogni task" del memory-first (pattern #13):
senza il checkpoint, il task NON è considerato completato. È M2 che permette
la "ripresa a freddo": una sessione nuova trova tutto quello che serve in Memory.

**Regola d'oro:** un handoff HC-ME-POST senza CP-id restituito è INVALIDO.
L'ecosistema committente deve ricevere il CP-id per considerare il proprio task chiuso.

## Template CP (obbligatorio — da usare sempre)

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

Template fisico: `company/Memory/templates/CP-template.md`

## Sessioni di lavoro

Ogni sessione di lavoro (una conversazione con Claude) ha:

**Apertura (SessionStart hook):**
- ME-A01 serve: STATO-EMPIRE.md + "RIPRESA DA:" della sessione precedente
- Questo garantisce che ogni sessione parta con il contesto completo

**Chiusura (a fine lavoro):**
- T-M2.2 Session Logger compila `company/Memory/sessions/session-YYYYMMDD[-n].md`
- Aggiorna il campo "RIPRESA DA:" in STATO-EMPIRE.md per la sessione successiva

## Funzioni L4

| Team L4 | Funzione | Trigger |
|---|---|---|
| T-M2.1 Checkpoint Writer | scrive CP da template + aggiorna INDEX + aggiorna STATO | HC-ME-POST da qualsiasi ecosistema |
| T-M2.2 Session Logger | apre/chiude session-log; compila "RIPRESA DA:" | hook SessionStart/Stop |

## Come si attiva

**Handoff HC-ME-POST (inbound, post-task):**
```json
{
  "task_id": "T-YYYYMMDD-NNN",
  "ecosistema": "01-AGENCY",
  "esito": "completato",
  "output_paths": ["path/reale/1", "path/reale/2"],
  "lezioni": "...",
  "costi": { "token": 0, "usd": 0.00 },
  "prossimo_passo": "..."
}
```

**Risposta:**
```json
{
  "cp_id": "CP-20260611-005",
  "cp_path": "company/Memory/checkpoints/CP-20260611-005.md",
  "index_aggiornato": true,
  "stato_aggiornato": true
}
```

## KPI

| Metrica | Target |
|---|---|
| Task chiusi con CP | 100% (gate, non KPI) |
| Sessioni senza log di apertura/chiusura | 0 |
| CP scritto entro SLA dal task chiuso | ≤ 5 min |
| "RIPRESA DA:" aggiornato a ogni chiusura sessione | 100% |

## Escalation / Failure handling

- Handoff HC-ME-POST senza output_paths o esito → Checkpoint Writer chiede chiarimento;
  non scrive un CP "vuoto".
- Memory-Sentinel rileva task chiusi senza CP (confrontando task log con checkpoint) →
  escalation all'ecosistema committente: "task X risulta aperto, CP mancante".
