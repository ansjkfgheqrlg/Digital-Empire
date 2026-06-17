---
Type: CONCEPT
Status: Active
Tags: #coo #scripts #automazione #ops #health-check #cron
Created: 2026-06-17
Last updated: 2026-06-17
---

# SCRIPTS — COO (Chief Operating Officer)

> Descrizione degli script operativi del team COO. Questi script non sono ancora implementati
> come eseguibili autonomi (stato: progettati, da implementare in V2-3 con Chief-Forge).
> La descrizione qui è il contratto di cosa devono fare: input, output, trigger.
> Implementazione: richiesta a Chief-Forge o 09-OPERATIONS.

---

## Script 1 — `health-check.sh` (o equivalente in stack scelto)

**Scopo:** Esegue il ciclo di check del WF-OPS-DAILY in modo automatizzato e produce
il report strutturato JSON per il coo-conductor.

**Trigger:** schedulato ogni mattina (cron) + on-demand.

**Logica:**
1. Ping AgentDB (BRAIN): disponibile? Latenza?
2. Check BUS: dimensione DLQ, latenza media messaggi.
3. Check token/credenziali: lista token con expiry < 24h.
4. Check git status (sync Max↔Gael): conflitti? Ultima run sync?
5. Check run schedulate: quali erano previste oggi? Sono partite?
6. Output JSON con stato per componente + anomalie rilevate.

**Output atteso:** JSON strutturato compatibile con il format `ops-dashboard` della skill omonima.
**Owner script:** Chief-Forge per implementazione, coo-conductor per definizione requisiti.
**Dipendenze:** accesso read-only a AgentDB, git, log sistema 09-OPERATIONS.

---

## Script 2 — `sync-guard.py` (o hook Git)

**Scopo:** Hook Git che viene eseguito prima di ogni push/commit su aree critiche del monorepo.
Verifica che non ci siano flag `⚠️ COORDINAMENTO` attivi sull'area che si sta modificando.

**Trigger:** pre-commit hook (lato Max e Gael, configurato in `.git/hooks/`).

**Logica:**
1. Legge STATO-EMPIRE.md: ci sono flag `⚠️ COORDINAMENTO` attivi?
2. Confronta le aree flaggate con i file che si sta per committare.
3. Se c'è sovrapposizione → blocca il commit con messaggio esplicito: quale area è bloccata, chi ha il flag.
4. Se nessuna sovrapposizione → permette il commit.

**Output:** exit 0 (permetti) o exit 1 (blocca) con messaggio human-readable.
**Owner script:** Chief-Forge (implementazione) + coo-sync-keeper (definizione logica).
**Dipendenze:** accesso a STATO-EMPIRE.md, git hooks infrastruttura.

---

## Script 3 — `cron-runner-status.sh`

**Scopo:** Verifica lo stato dei job cron schedulati e produce un report delle run
previste vs. avvenute per la giornata corrente.

**Trigger:** schedulato 2x al giorno (dopo l'orario dell'ultima run pianificata del mattino
e della sera) + on-demand da coo-runtime-marshal.

**Logica:**
1. Carica lo schedule della giornata da `board/coo/run-schedule`.
2. Confronta con i log delle run effettivamente avvenute.
3. Identifica: run completate / run fallite / run mancanti (non avviate).
4. Per le run mancanti: calcola il ritardo (minuti dalla scadenza schedulata).
5. Output: lista run con stato + alert per quelle con ritardo >30min.

**Output atteso:** JSON `{run_completate: [], run_fallite: [], run_mancanti: [{id, ritardo_min}]}`.
**Owner script:** Chief-Forge (implementazione) + coo-runtime-marshal (definizione).
**Dipendenze:** log 09-OPERATIONS, `board/coo/run-schedule` in AgentDB.

---

## Script 4 — `incident-opener.sh`

**Scopo:** Crea automaticamente un INC strutturato con ID univoco quando viene rilevata
un'anomalia dai monitor. Riduce il tempo di apertura INC da manuale a automatico.

**Trigger:** chiamato da health-check.sh o da qualsiasi monitor che rileva un'anomalia.

**Logica:**
1. Riceve come input: fonte, descrizione, severità, componente impattato.
2. Genera ID univoco: `INC-YYYYMMDD-NNN` (NNN incrementale per la giornata).
3. Crea file INC strutturato in `board/coo/incidenti-aperti` in AgentDB.
4. Notifica coo-incident-handler che un nuovo INC è aperto.

**Output:** `{inc_id: "INC-20260617-001", creato: true}`.
**Owner script:** Chief-Forge (implementazione) + coo-incident-handler (definizione).
**Dipendenze:** AgentDB write access, sistema di notifica interna.

---

## Note implementazione

- **Stack:** da decidere in V2-3 con Chief-Forge (bash/Python/Node a seconda del runtime 09-OPERATIONS).
- **Test:** ogni script deve avere uno scenario di test "anomalia reale" prima del deploy in produzione.
- **ADR richiesto:** se i script modificano STATO-EMPIRE.md in modo automatico → ADR per approvazione Max.
- **Nessun script fa git push autonomamente** senza conferma esplicita dell'operatore umano.

---

## Connessioni

- [[coo-conductor]] · `agenti/coo-conductor.md`
- [[coo-backbone-health]] · `agenti/coo-backbone-health.md`
- [[coo-sync-keeper]] · `agenti/coo-sync-keeper.md`
- [[coo-runtime-marshal]] · `agenti/coo-runtime-marshal.md`
- [[coo-incident-handler]] · `agenti/coo-incident-handler.md`
- [[SKILLS]] · `skills/SKILLS.md`
- [[BP-COO]] · `company/Board-CSuite/_BLUEPRINT/BP-COO.md`
- [[14-DOSSIER-ARCHITETTURA]] · `PIANO-MAESTRO/14-DOSSIER-ARCHITETTURA.md`
