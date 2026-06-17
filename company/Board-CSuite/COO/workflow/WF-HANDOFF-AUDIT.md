---
Type: CONCEPT
Status: Active
Tags: #workflow #coo #handoff #audit #hc #contratti #ecosistemi
Created: 2026-06-17
Last updated: 2026-06-17
---

# WF-HANDOFF-AUDIT — Audit Contratti Handoff

> **ID workflow:** WF-COO-03 · **Owner:** coo-handoff-auditor (coordinato da coo-conductor)
> **Trigger:** ogni 2 settimane (scheduled) · post-incident (se INC causato da HC rotto) · on-demand
> **Durata attesa:** ≤20 minuti per una sessione di audit (3-5 HC campionati)
> **Blueprint di riferimento:** `company/Board-CSuite/_BLUEPRINT/BP-COO.md`

---

## Scopo

I contratti HC (Handoff Contract) tra ecosistemi sono il sistema nervoso della holding:
quando si rompono silenziosamente, la produzione si degrada senza un incidente visibile.
Questo workflow campiona periodicamente i contratti HC per rilevare rotture strutturali
(payload non conforme) e rotture funzionali (acceptance criteria non rispettati) prima
che causino problemi operativi. Il campionamento è rotazionale: ogni HC viene auditato
almeno una volta ogni 2 settimane.

---

## Agenti coinvolti

| Agente | Ruolo nel workflow | Fase |
|---|---|---|
| `coo-handoff-auditor` | selezione campione, verifica struttura/acceptance, produzione report | tutto |
| `coo-conductor` | riceve il report, decide le azioni, comunica agli ecosistemi coinvolti | fase 3-4 |
| `coo-incident-handler` | apre INC se un HC rotto ha già causato un problema operativo | fase 3 condizionale |
| `coo-memoria` | aggiorna `board/coo/hc-audit-log` con l'esito dell'audit | fase 4 |

---

## Flusso passo-passo

### Fase 1 — Preparazione e Selezione Campione (≤3 minuti)
**Owner:** `coo-handoff-auditor`

1. Carica il HC registry completo da `board/coo/hc-audit-log`.
2. Ordina i contratti per "data ultima verifica" (crescente: i più vecchi da auditare prima).
3. Seleziona 3-5 HC per questa sessione:
   - In sessione normale: i 3-5 con data ultima verifica più vecchia.
   - In post-incident context: priorità agli HC coinvolti nell'incidente (anche se recentemente auditati).
   - In on-demand: l'HC specificato dall'operatore + i 2 più vecchi della lista.
4. Recupera l'ultima transazione reale per ogni HC selezionato (da AgentDB o dai log disponibili).

**Campione HC prioritari (sempre verificati se non auditati nelle ultime 2 settimane):**
- `HC-CEO-COO-01` (comunicazione CEO→COO: direttive operative)
- `HC-COO-CEO-01` (report stato COO→CEO)
- `HC-COO-CFO-01` (alert costo COO→CFO)
- `HC-CTO-COO-01` (salute tecnica CTO→COO)

---

### Fase 2 — Verifica HC (campionamento)
**Owner:** `coo-handoff-auditor`

Per ogni HC del campione, verifica in sequenza:

**Check A — Struttura payload:**
- L'ultimo payload reale trasmesso corrisponde allo schema definito nel contratto?
- Tutti i campi obbligatori sono presenti? I tipi sono corretti?
- Risultato: `conforme | non-conforme (campi mancanti) | non-conforme (tipo sbagliato) | nessuna transazione recente`

**Check B — Acceptance criteria:**
- Il destinatario ha eseguito l'azione definita negli acceptance criteria?
- Esempio: HC-CEO-COO-01 prevede "COO conferma ricevuta + assegna owner operativo" → c'è traccia di questa azione?
- Risultato: `rispettato | non-rispettato | non-verificabile (nessuna traccia)`

**Check C — Owner aggiornato:**
- L'owner del contratto è ancora il ruolo attuale? (Rotazioni di responsabilità senza aggiornamento HC sono una fonte comune di rottura.)
- Risultato: `aggiornato | obsoleto (owner cambiato)`

**Classificazione finale per HC:**
- `ok` = A conforme + B rispettato + C aggiornato
- `degradato` = A conforme + B non-rispettato (o non-verificabile)
- `rotto` = A non-conforme O C obsoleto

---

### Fase 3 — Report e Decisioni (≤5 minuti)
**Owner:** `coo-handoff-auditor` → `coo-conductor`

Il report viene passato al coo-conductor con:
- Lista HC auditati + esito per ciascuno
- Lista HC rotti/degradati con descrizione anomalia + impatto operativo stimato
- Azioni raccomandate per ogni anomalia

**Il coo-conductor decide:**

| HC rotto/degradato | Azione | Owner |
|---|---|---|
| Schema payload non conforme | Proposta aggiornamento schema HC → ecosistema mittente | coo-conductor → ecosistema |
| Acceptance criteria non rispettato | Notifica all'ecosistema destinatario + verifica causa | coo-conductor → ecosistema |
| Owner obsoleto | Aggiornamento registro HC + notifica nuovo owner | coo-handoff-auditor |
| HC rotto già causa di INC | Apre INC con coo-incident-handler | coo-incident-handler |

**Comunicazione agli ecosistemi:**
Il coo-conductor notifica gli ecosistemi coinvolti in modo diretto: "HC-XYZ risulta [rotto/degradato].
Azione richiesta: [specifica]. Deadline: [data]. Owner: [nome]."
Non si invia una segnalazione vaga: ogni notifica ha azione esplicita + deadline + owner.

---

### Fase 4 — Aggiornamento Registro e Log (≤2 minuti)
**Owner:** `coo-memoria`

1. Aggiorna `board/coo/hc-audit-log` con i risultati della sessione.
2. Aggiorna la data di "ultima verifica" per ogni HC auditato.
3. Se un HC è passato da "rotto" a "ok" (fix applicato) → aggiorna stato nel registry.
4. Aggiunge entry nel cadence log del coo-cadence-keeper: audit HC eseguito + data.

**Struttura log entry:**
```json
{
  "data_audit": "2026-06-17",
  "hc_auditati": ["HC-CEO-COO-01", "HC-COO-CEO-01", "HC-COO-CFO-01"],
  "esiti": {
    "HC-CEO-COO-01": "ok",
    "HC-COO-CEO-01": "degradato — acceptance criteria non rispettato (campo 'azioni' vuoto)",
    "HC-COO-CFO-01": "ok"
  },
  "azioni_avviate": ["notifica coo-conductor su HC-COO-CEO-01 — fix richiesto"]
}
```

---

## State del workflow

| Campo | Valore atteso |
|---|---|
| `fase_corrente` | `1-preparazione | 2-verifica | 3-report | 4-aggiornamento | completato` |
| `hc_nel_campione` | lista HC selezionati |
| `hc_auditati_totali` | n. (da hc-audit-log: running total) |
| `hc_rotti_trovati` | n. (sessione corrente) |
| `azioni_pendenti` | lista azioni con owner e deadline |

---

## Gate di completamento

Il workflow è **COMPLETATO** quando:
- [ ] Almeno 3 HC verificati (struttura + acceptance criteria + owner).
- [ ] Report al coo-conductor consegnato.
- [ ] Azioni decise con owner e deadline espliciti per ogni HC rotto/degradato.
- [ ] `board/coo/hc-audit-log` aggiornato con data e esiti.

---

## Frequenza e copertura

| Periodicità | HC da coprire |
|---|---|
| Ogni 2 settimane | 3-5 HC in campionamento rotazionale |
| Trimestrale | full audit: tutti gli HC nel registry (revisione completa schema) |
| Post-incident | HC coinvolti nell'incidente + 2 correlati |

Copertura target: ogni HC auditato almeno 1 volta ogni 2 settimane. Se il registry cresce
(nuovi HC aggiunti), il campione viene aumentato proporzionalmente.

---

## Connessioni

- [[coo-handoff-auditor]] · `agenti/coo-handoff-auditor.md`
- [[coo-conductor]] · `agenti/coo-conductor.md`
- [[coo-incident-handler]] · `agenti/coo-incident-handler.md`
- [[coo-memoria]] · `agenti/coo-memoria.md`
- [[WF-OPS-DAILY]] · `workflow/WF-OPS-DAILY.md`
- [[WF-INCIDENT]] · `workflow/WF-INCIDENT.md`
- [[BP-COO]] · `company/Board-CSuite/_BLUEPRINT/BP-COO.md`
- [[CEO-Empire-Conductor/ARCHITETTURA]] · `../CEO-Empire-Conductor/ARCHITETTURA.md` (tabella HC Board)
- [[13-DOSSIER-MANDATO-ECOSISTEMA]] · `PIANO-MAESTRO/13-DOSSIER-MANDATO-ECOSISTEMA.md`
