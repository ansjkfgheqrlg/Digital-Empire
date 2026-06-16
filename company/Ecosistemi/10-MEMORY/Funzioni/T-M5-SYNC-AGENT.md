> Fonte: PIANO-MAESTRO/09-ECOSISTEMA-MEMORY.md sez. 3 (Reparto M5 — Sync & Integrità)

# T-M5-SYNC-AGENT — Funzione Sync Agent & Integrity Auditor

> Layer funzione condiviso · Livello: L3/L4 · Usato da: ME-A09 sync-agent, ME-A10 integrity-auditor
> Ecosistema: `company/Ecosistemi/10-MEMORY/ECOSISTEMA.md`
> Backbone: `company/Ecosistemi/10-MEMORY/BACKBONE.md`

---

## Identità funzione

| Campo | Valore |
|---|---|
| Funzione ID | T-M5-SYNC-AGENT |
| Capability servite | wiki-sync, agentdb-sync, audit-check, backup-verify, orphan-detect, rollback |
| Reparto owner | M5 — Sync & Integrità |
| Stato | ATTIVO — sync continua; audit settimanale (gate G-ME4) |
| Tier modello | haiku (sync) + sonnet (audit e rollback) |
| Invariante | i 3 strati (file ↔ wiki ↔ AgentDB) non divergono mai |

---

## Contratto funzione (non negoziabile)

| Operazione | Input | Output |
|---|---|---|
| `sync_wiki(evento)` | CP/ADR/evento di interesse umano | entry in `second-brain-vault/wiki/log.md` |
| `sync_agentdb(documento)` | CP o ADR appena scritto | `memory_store` in namespace corretto |
| `audit_integrity()` | nessun input (legge tutto Memory/) | report divergenze + lista CP orfani |
| `detect_orphans()` | scan checkpoints/ + tasks/ | lista task senza CP corrispondente |
| `rollback(cp_id)` | id CP da ripristinare | stato ripristinato (APPEND del rollback, mai delete) |

---

## Flusso sync (dopo ogni WF-POSTTASK)

```
CP scritto + state aggiornato
  → ME-A09 sync:
    1. wiki-sync: costruisci entry 1-riga per wiki/log.md
       formato: "- CP-NNN [esito] <ecosistema>: <titolo> → prossimo: <passo>"
       APPEND a second-brain-vault/wiki/log.md (mai sovrascrivere)
    2. agentdb-sync:
       memory_store(namespace="memory/checkpoints", key=cp_id, value={...})
       Se CP contiene ADR → anche memory_store(namespace="memory/decisions", ...)
    3. Se evento è di interesse per ReasoningBank (lezioni/errori presenti):
       → memory_store(namespace="patterns", key=ecosistema+tipo, value=lezione)
       → propaga a Backbone BRAIN (namespace "patterns")
```

---

## Flusso audit integrità (settimanale — gate G-ME4)

```
ME-A10 integrity-auditor lancia audit:
  1. detect_orphans():
     a. Leggi Memory/tasks/<ecosistema>/ → lista task registrati
     b. Confronta con Memory/checkpoints/ → task senza CP = ORFANO
     c. Segnala lista orfani a Memory-Sentinel per escalation
  2. Verifica INDEX.md: ogni CP/ADR in INDEX esiste fisicamente?
     Se INDEX punta a file inesistente → incoerenza critica
  3. Verifica AgentDB: campione di CP → memory_search → risultato presente?
     Divergenza file↔AgentDB → re-sync immediato
  4. Verifica wiki/log.md: ogni CP importante ha entry in wiki?
     Mancanti → sync retroattivo
  5. Genera report: Memory/audit/audit-YYYYMMDD.md
  6. Se 0 divergenze → gate G-ME4 VERDE
     Se divergenze → gate G-ME4 ROSSO + escalation Board
```

---

## Regole operative

1. **Sync è propagazione, non duplicazione**: wiki/log.md riceve solo ciò che è utile all'umano (evento, esito, prossimo passo) — non copia integrale del CP.
2. **Rollback è append, mai delete**: per ripristinare uno stato precedente → si scrive un nuovo CP di rollback che riporta indietro, non si cancellano record.
3. **Backup→append→log→rollback (pattern Memory Empire)**: ogni scrittura in MEMORY segue questa sequenza. Non esistono overwrite senza backup preventivo.
4. **G-ME4 settimanale non negoziabile**: l'audit settimanale è un gate di governance, non una raccomandazione. Se saltato → Memory-Sentinel escalation al Board.

---

## Namespace AgentDB (da dossier §9)

| Namespace | Contenuto |
|---|---|
| `memory/checkpoints` | ogni CP scritto → indicizzato per recall semantico |
| `memory/decisions` | ogni ADR registrato → recall per keyword/ecosistema |
| `memory/state` | stato corrente per progetto → recall veloce |
| `memory/sessions` | log sessioni → ricostruzione storia di lavoro |
| `patterns` | lezioni distillate → ReasoningBank (Backbone BRAIN) |

---

## Connessioni

- `company/Ecosistemi/10-MEMORY/ECOSISTEMA.md` — organigramma completo
- `company/Ecosistemi/10-MEMORY/BACKBONE.md` — topologia e namespace ruflo
- `company/Ecosistemi/10-MEMORY/Agenti/ME-A09-sync-agent.md` — agente sync
- `company/Ecosistemi/10-MEMORY/Agenti/ME-A10-integrity-auditor.md` — agente audit
- `company/Ecosistemi/10-MEMORY/Agenti/Memory-Sentinel.md` — sentinel che riceve escalation orphan
- `PIANO-MAESTRO/09-ECOSISTEMA-MEMORY.md` §3 (M5), §7 (pattern backup→append→log→rollback), §9 (namespace AgentDB)

*Fonte: dossier 09 §3 (M5), §7, §9 · Aggiornato: 2026-06-12*
