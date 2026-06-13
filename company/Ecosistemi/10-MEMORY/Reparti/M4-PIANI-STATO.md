# M4 — Piani & Stato
## Ecosistema 10-MEMORY

## Missione
I piani della holding sono versionati e mai persi. Lo stato è VERO: letto sempre dal
filesystem reale, mai dichiarato a memoria. Il reparto M4 garantisce che ogni revisione
di piano sia tracciata con diff, e che STATO-EMPIRE.md rifletta esattamente la realtà
corrente — non quello che qualcuno ricorda o si aspetta.

Principio fondante (da pattern catalog_status di Empire Studio): **lo stato non si
dichiara, si legge**. M4 non accetta "siamo in fase X" — verifica nel filesystem.

---

## Handoff Contract

**Input (HC-ME-PLAN):**
```json
{
  "piano_id": "nome o codice piano",
  "versione": "v1.0 / v1.1 / ...",
  "tipo": "nuovo | revisione",
  "richiedente": "Board | FORGE | ecosistema",
  "contenuto_path": "path al file piano sorgente",
  "motivazione_revisione": "perché si revisa (se revisione)"
}
```

**Output:**
- `company/Memory/plans/<piano-id>-vN.md` salvato
- Diff rispetto alla versione precedente (se revisione)
- `company/Memory/STATO-EMPIRE.md` aggiornato con nuova fase/stato
- `company/Memory/state/<progetto-id>/state.json` aggiornato
- `company/Memory/state/<progetto-id>/trace.jsonl` append con evento

**Acceptance criteria:**
- Ogni revisione genera file versione nuova (no overwrite)
- diff prodotto e allegato alla voce INDEX
- state.json validato: nessun campo dichiarato, ogni campo derivato da filesystem
- STATO-EMPIRE.md coerente con l'ultimo state.json

---

## Team agenti

| Codice | Agente | Livello | Ruolo |
|---|---|---|---|
| ME-A07 | plan-keeper | L3 Worker | Custodisce, versiona piani, produce diff tra versioni |
| ME-A08 | state-tracker | L4 Worker | Mantiene state.json + trace.jsonl, aggiorna STATO-EMPIRE.md |

---

## Workflow

```
HC-ME-PLAN ricevuto
  → ME-A07: legge versione precedente (se esiste) in plans/
  → ME-A07: salva nuova versione plans/<piano-id>-vN.md
  → ME-A07: produce diff (v_prec → v_nuova) e lo allega a INDEX
  → ME-A08: legge stato reale dal filesystem (non dichiarato)
  → ME-A08: aggiorna state/<progetto-id>/state.json
  → ME-A08: appende evento a trace.jsonl
  → ME-A08: riscrive STATO-EMPIRE.md sezione "Fase corrente"
  → ME-A09 (M5): sync a wiki/log.md + AgentDB namespace memory/state
```

---

## Come funziona (flusso dettagliato)

1. **Ricezione piano:** ME-A07 riceve il piano da HC-ME-PLAN o direttamente da FORGE/Board
2. **Versioning:** ME-A07 lista i file `<piano-id>-v*.md` in plans/, determina il numero
   di versione successivo, salva il nuovo file senza toccare le versioni precedenti
3. **Diff:** ME-A07 confronta v_precedente e v_nuova, produce un diff leggibile in formato
   markdown e lo allega come nota nella voce INDEX
4. **State read:** ME-A08 NON si fida di variabili in memoria — legge da filesystem:
   - quali cartelle esistono in company/Ecosistemi/
   - quali CP esistono in checkpoints/ (conta e data-stamma)
   - quali ADR hanno stato=attivo in decisions/
5. **Update state.json:** ME-A08 aggiorna il file JSON con i campi derivati da lettura reale
6. **Trace append:** ME-A08 fa solo append a trace.jsonl (pattern backup→append→log —
   mai overwrite, mai delete)
7. **STATO-EMPIRE.md:** ME-A08 riscrive le sezioni "Fase corrente", "Lavori in corso",
   "Blocchi", "Prossime azioni" con dati freschi dal filesystem

---

## Schema state.json

```json
{
  "progetto_id": "string",
  "fase_corrente": "F1 | F2 | ...",
  "ultimo_aggiornamento": "ISO8601",
  "ecosistemi_completati": ["01-AGENCY", "..."],
  "ecosistemi_in_corso": ["10-MEMORY"],
  "blocchi_attivi": [],
  "ultimo_cp": "CP-20260613-001",
  "ultimo_adr": "ADR-007",
  "prossima_azione": "string"
}
```

---

## Gate

- **Nessun overwrite** di versioni precedenti di piani — solo append/nuova versione
- **State.json** non contiene campi che non possono essere verificati dal filesystem
- Riscrittura STATO-EMPIRE.md richiede lettura reale del filesystem (ME-A08 non "ricorda")

---

## KPI

| KPI | Target |
|---|---|
| Piani versionati senza gap | 100% |
| Overwrite versioni precedenti | 0 |
| Divergenza STATO-EMPIRE vs filesystem | 0 rilevate da audit M5 |
| Tempo aggiornamento state.json post-task | ≤ 60s |

---

## Connessioni
- [[09-ECOSISTEMA-MEMORY]] — dossier madre
- [[STATO-EMPIRE]] — file principale gestito da ME-A08
- [[INDEX]] — indice maestro (voci piani aggiornate da ME-A07)
- [[M2-CHECKPOINT-SESSIONI]] — i CP alimentano lo state.json via ME-A08
- [[M5-SYNC]] — ME-A09 propaga gli aggiornamenti di stato ai 3 strati
- [[PIANO-MAESTRO]] — fonte dei piani principali custoditi da ME-A07
