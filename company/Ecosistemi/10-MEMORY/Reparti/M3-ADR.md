# M3 — Decisioni (ADR)
## Ecosistema 10-MEMORY

## Missione
Zero decisioni implicite. Ogni scelta architetturale o strategica che impatta la holding
deve essere registrata, versionata e verificata per contraddizioni con le decisioni attive.
Il reparto M3 è il custode della coerenza decisionale: senza ADR registrato, una decisione
non esiste ufficialmente per la holding.

---

## Handoff Contract

**Input (HC-ME-ADR):**
```json
{
  "decisione": "descrizione della scelta presa",
  "contesto": "perché questa decisione si è resa necessaria",
  "alternative": ["opzione A scartata", "opzione B scartata"],
  "conseguenze": "impatto atteso sulla holding",
  "richiedente": "ecosistema o Board che ha generato la decisione"
}
```

**Output:**
- `company/Memory/decisions/ADR-NNN.md` creato e salvato
- Voce in `company/Memory/INDEX.md` aggiornata
- Contradiction-check log restituito al richiedente
- Se conflitto rilevato: escalation Board con diff ADR-vecchio vs ADR-nuovo

**Acceptance criteria:**
- ADR-NNN numerato progressivamente senza gap
- Contradiction-check completato contro TUTTI gli ADR con stato `attivo`
- Conflitto con ADR attivo → ADR NON registrato fino a risoluzione Board
- Warning (non conflitto duro) → ADR registrato con nota `⚠️ revisione consigliata`

---

## Team agenti

| Codice | Agente | Livello | Ruolo |
|---|---|---|---|
| ME-A05 | adr-registrar | L3 Worker | Riceve HC-ME-ADR, compila template ADR, assegna numero progressivo |
| ME-A06 | contradiction-checker | L4 Worker | Confronta nuovo ADR/piano con ADR attivi, usa skill-contradiction-analyzer |

---

## Workflow

```
HC-ME-ADR ricevuto
  → ME-A05: valida input, assegna ADR-NNN, compila template
  → ME-A06: carica tutti gli ADR con stato=attivo da company/Memory/decisions/
  → ME-A06: skill-contradiction-analyzer (nuovo ADR vs ciascun ADR attivo)
  → risultato OK → ME-A05: salva ADR-NNN.md + aggiorna INDEX
  → risultato CONFLITTO → escalation Board (non si salva, task sospeso)
  → risultato WARNING → ME-A05: salva ADR-NNN.md con nota ⚠️ + log warning
  → ME-A09 (M5): propaga evento a wiki/log.md + AgentDB namespace memory/decisions
```

---

## Come funziona (flusso dettagliato)

1. **Ricezione:** qualsiasi team o Board invia HC-ME-ADR a ME-Conductor (ME-A00)
2. **Draft:** ME-A05 compila il template ADR con i campi obbligatori (contesto, decisione,
   alternative, conseguenze, stato=proposto)
3. **Numerazione:** ME-A05 legge l'ultimo ADR-NNN.md in decisions/ e incrementa di 1
4. **Contradiction-check:** ME-A06 carica l'indice degli ADR attivi, applica
   skill-contradiction-analyzer, produce report con severità (conflitto/warning/ok)
5. **Branch decisionale:**
   - OK o WARNING → ADR salvato, INDEX aggiornato, conferma al richiedente
   - CONFLITTO → ME-A00 notifica Board, task richiedente messo in pausa
6. **Sync:** ME-A09 propaga l'evento ai 3 strati (file ✓ / wiki ✓ / AgentDB ✓)

---

## Gate

- **G-ME3:** contradiction-check obbligatorio su ogni ADR prima della registrazione
- Un handoff che dichiara una decisione senza ADR-id è invalido per contratto di holding

---

## KPI

| KPI | Target |
|---|---|
| Decisioni con ADR registrato | 100% |
| ADR senza contradiction-check | 0 |
| Tempo medio registrazione ADR | ≤ 2 min |
| Conflitti rilevati e bloccati prima del build | misura di efficacia (più è meglio) |

---

## Template ADR (obbligatorio)

```markdown
# ADR-NNN — <titolo decisione>
- Data: YYYY-MM-DD
- Richiedente: <ecosistema/Board>
- Stato: proposto | attivo | superato da ADR-X

## Contesto
## Decisione
## Alternative scartate
## Conseguenze
## Contradiction-check: OK | ⚠️ <nota> | ❌ CONFLITTO con ADR-X
```

---

## Connessioni
- [[09-ECOSISTEMA-MEMORY]] — dossier madre dell'ecosistema MEMORY
- [[STATO-EMPIRE]] — stato corrente della holding (aggiornato a ogni ADR attivo)
- [[INDEX]] — indice maestro (voce ADR aggiunta a ogni registrazione)
- [[M1-RECALL-PRETASK]] — M1 usa gli ADR attivi nel context-pack pre-task
- [[skill-contradiction-analyzer]] — motore usato da ME-A06
