> Fonte: PIANO-MAESTRO/09-ECOSISTEMA-MEMORY.md sez. 3 (Reparto M4 — Piani & Stato)

# T-M4-STATE-TRACKER — Funzione State Tracker

> Layer funzione condiviso · Livello: L4 · Usato da: ME-A07 plan-keeper, ME-A08 state-tracker
> Ecosistema: `company/Ecosistemi/10-MEMORY/ECOSISTEMA.md`
> Backbone: `company/Ecosistemi/10-MEMORY/BACKBONE.md`

---

## Identità funzione

| Campo | Valore |
|---|---|
| Funzione ID | T-M4-STATE-TRACKER |
| Capability servite | state-read, state-update, plan-version, trace-append, stato-empire-update |
| Reparto owner | M4 — Piani & Stato |
| Stato | ATTIVO — aggiornato a ogni cambio fase di un progetto |
| Tier modello | haiku (lettura/scrittura strutturata) |
| Pattern critico | stato mai dichiarato, sempre letto dal filesystem (pattern catalog_status — Empire Studio) |

---

## Contratto funzione (non negoziabile)

| Operazione | Input | Output |
|---|---|---|
| `read_state(progetto_id)` | id progetto | `state.json` corrente letto da disco |
| `update_state(progetto_id, delta)` | id + campi da aggiornare | `state.json` aggiornato + entry `trace.jsonl` |
| `version_plan(piano_id, nuova_versione)` | id piano + path nuova versione | piano versionato in `Memory/plans/` + diff |
| `update_stato_empire(sezione, contenuto)` | sezione STATO-EMPIRE + valore | STATO-EMPIRE.md aggiornato |

---

## Struttura state.json per progetto

```json
{
  "progetto_id": "SLUG-YYYY-NNN",
  "ecosistema": "01-AGENCY | 02-INFO | ...",
  "fase_corrente": "discovery | build | delivery | chiuso",
  "ultimo_aggiornamento": "YYYY-MM-DDTHH:MM:SSZ",
  "cp_ultimo": "CP-YYYYMMDD-NNN",
  "blocchi_attivi": [],
  "prossimo_passo": "...",
  "handoff_pendenti": []
}
```

---

## Struttura trace.jsonl (append-only)

```jsonl
{"ts": "ISO8601", "agente": "ME-A08", "evento": "state_update", "delta": {...}, "cp_ref": "CP-NNN"}
{"ts": "ISO8601", "agente": "ME-A08", "evento": "fase_cambio", "da": "build", "a": "delivery"}
```

---

## Flusso operativo — aggiornamento stato

```
Trigger: HC-ME-POST (parte di WF-POSTTASK) o cambio fase esplicito
  1. read_state(progetto_id) → carica state.json attuale dal disco
  2. Applica delta (mai merge in memoria senza rileggere prima)
  3. Valida coerenza: fase_corrente coerente con CP/ADR esistenti?
  4. update_state: scrivi state.json aggiornato
  5. trace.jsonl: APPEND entry (mai sovrascrivere righe precedenti)
  6. update_stato_empire: aggiorna sezione corrispondente in STATO-EMPIRE.md
```

---

## Versionamento piani

```
Trigger: HC-ME-PLAN (nuovo piano o revisione da Board/FORGE)
  1. Leggi piano corrente in Memory/plans/
  2. Calcola diff tra versione corrente e nuova
  3. Salva nuova versione: Memory/plans/<id>-v<N+1>.md
  4. Salva diff: Memory/plans/<id>-v<N>-v<N+1>-diff.md
  5. Aggiorna INDEX.md con la nuova versione
  6. MAI cancellare versioni precedenti (storico sempre preservato)
```

---

## Regole operative

1. **Stato letto dal filesystem, mai dichiarato**: ME-A08 non si fida di variabili in memoria — ogni `read_state` legge il file fisico.
2. **trace.jsonl è append-only**: nessuna riga viene modificata o eliminata. È il log immutabile della storia del progetto.
3. **STATO-EMPIRE.md riflette la realtà**: se un task è "in corso" in STATO ma il CP di chiusura esiste → incongruenza da correggere immediatamente (segnala a Memory-Sentinel).
4. **Piano versionato sempre prima di applicarlo**: mai sovrascrivere il piano corrente senza preservare la versione precedente.

---

## Connessioni

- `company/Ecosistemi/10-MEMORY/ECOSISTEMA.md` — organigramma completo
- `company/Ecosistemi/10-MEMORY/BACKBONE.md` — namespace AgentDB `memory/state`
- `company/Ecosistemi/10-MEMORY/Agenti/ME-A07-plan-keeper.md` — agente versionamento piani
- `company/Ecosistemi/10-MEMORY/Agenti/ME-A08-state-tracker.md` — agente state tracker
- `company/Ecosistemi/10-MEMORY/Workflow/WF-POSTTASK.md` — workflow che triggera questo aggiornamento
- `PIANO-MAESTRO/09-ECOSISTEMA-MEMORY.md` §3 (M4), §7 (pattern catalog_status)

*Fonte: dossier 09 §3 (M4), §7 (asset → Empire Studio catalog_status) · Aggiornato: 2026-06-12*
