> Fonte: PIANO-MAESTRO/09-ECOSISTEMA-MEMORY.md sez. 3 (Reparto M3 — Decisioni ADR)

# T-M3-ADR-REGISTRAR — Funzione ADR Registrar

> Layer funzione condiviso · Livello: L3 · Usato da: ME-A05 adr-registrar, ME-A06 contradiction-checker
> Ecosistema: `company/Ecosistemi/10-MEMORY/ECOSISTEMA.md`
> Backbone: `company/Ecosistemi/10-MEMORY/BACKBONE.md`

---

## Identità funzione

| Campo | Valore |
|---|---|
| Funzione ID | T-M3-ADR-REGISTRAR |
| Capability servite | adr-draft, adr-register, contradiction-check, adr-supersede |
| Reparto owner | M3 — Decisioni (ADR) |
| Stato | ATTIVO — trigger: HC-ME-ADR da qualsiasi team |
| Tier modello | sonnet (ragionamento su conflitti) |
| Missione | zero decisioni implicite nella holding |

---

## Contratto funzione (non negoziabile)

| Operazione | Input | Output |
|---|---|---|
| `draft_adr(decisione)` | `{decisione, contesto, alternative, conseguenze}` | ADR bozza strutturato |
| `contradiction_check(adr_bozza)` | bozza + lista ADR attivi | `{ok: bool, conflitti: [{adr_id, dettaglio}]}` |
| `register_adr(adr_bozza)` | bozza validata (no conflitti) | `{adr_id, path}` confermato |
| `supersede_adr(old_id, new_id)` | id ADR da superare + id nuovo | ADR vecchio stato → "superato da ADR-X" |

---

## Template ADR obbligatorio (da dossier §2)

```markdown
# ADR-NNN — <titolo decisione>

**Stato:** proposto | attivo | superato da ADR-X

## Contesto
<perché questa decisione era necessaria>

## Decisione
<cosa si è deciso esattamente>

## Alternative scartate
- <opzione A>: scartata perché …
- <opzione B>: scartata perché …

## Conseguenze
- Positive: …
- Negative/trade-off: …

## Collegamento
- Ecosistema: <01-AGENCY | 02-INFO | … | holding>
- CP di riferimento: CP-YYYYMMDD-NNN
```

---

## Flusso operativo (HC-ME-ADR)

```
HC-ME-ADR ricevuto {decisione, contesto, alternative, conseguenze}
  1. ME-A05 drafta ADR con template → bozza ADR-NNN
  2. ME-A06 contradiction_check:
     a. Carica tutti gli ADR con stato = ATTIVO da company/Memory/decisions/
     b. Confronta semanticamente la nuova decisione vs ADR attivi
        (usa skill-contradiction-analyzer o ragionamento su dossier)
     c. Se conflitto rilevato → STOP
        → escalation hive-mind Board (mai registrare ADR in conflitto)
     d. Se nessun conflitto → ok per registrazione
  3. ME-A05 assegna ID sequenziale (legge ultimo ADR-NNN in decisions/ → +1)
  4. Scrive company/Memory/decisions/ADR-NNN-titolo.md
  5. Aggiorna company/Memory/INDEX.md: aggiungi riga ADR-NNN
  6. memory_store(AgentDB "memory/decisions", {adr_id, decisione, keywords})
  7. Ritorna {adr_id, path} al team richiedente
```

---

## Regole operative

1. **Contradiction-check non bypassabile**: nessun ADR viene registrato senza check vs tutti gli ADR ATTIVI. Non c'è eccezione, nemmeno per urgenza.
2. **Escalation al Board, non autodecisione**: in caso di conflitto, ME-A06 non decide chi ha torto — escalation hive-mind e attende istruzione.
3. **Il checker blocca solo ADR ATTIVI**: ADR in stato "proposto" o "superato" generano warning, non blocco.
4. **Supersede esplicito**: quando una nuova decisione sostituisce una precedente → ADR vecchio deve essere aggiornato a "superato da ADR-X", non eliminato.

---

## KPI

| KPI | Target |
|---|---|
| Decisioni senza ADR | 0 (gate, non KPI) |
| Falsi positivi contradiction-check | monitora (segnalare al Board se > 2/settimana) |
| Tempo draft→registrazione | ≤ 5 minuti per decisioni standard |

---

## Connessioni

- `company/Ecosistemi/10-MEMORY/ECOSISTEMA.md` — organigramma completo
- `company/Ecosistemi/10-MEMORY/BACKBONE.md` — namespace AgentDB `memory/decisions`
- `company/Ecosistemi/10-MEMORY/Agenti/ME-A05-adr-registrar.md` — agente registrar
- `company/Ecosistemi/10-MEMORY/Agenti/ME-A06-contradiction-checker.md` — agente checker
- `company/Ecosistemi/10-MEMORY/Workflow/WF-DECISION.md` — workflow che orchestra questa funzione
- `PIANO-MAESTRO/09-ECOSISTEMA-MEMORY.md` §2 (template ADR), §3 (M3), §5

*Fonte: dossier 09 §2 (template ADR), §3 (M3), §5 (WF-DECISION) · Aggiornato: 2026-06-12*
