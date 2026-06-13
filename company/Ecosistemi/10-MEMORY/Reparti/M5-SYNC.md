# M5 — Sync & Integrità
## Ecosistema 10-MEMORY

## Missione
I 3 strati della conoscenza operativa (file Memory ↔ wiki ↔ AgentDB) non divergono mai.
Tutto è recuperabile. Il reparto M5 è l'organo circolatorio di MEMORY: propaga ogni evento
rilevante verso la vista umana (wiki/log.md) e verso il recall semantico degli agenti
(AgentDB namespace memory/), e verifica periodicamente che i tre strati siano allineati.

Principio: **un dato scritto in company/Memory/ e non propagato agli altri strati è un
dato parzialmente perso**. M5 elimina questa perdita strutturalmente.

---

## Handoff Contract

**Input — trigger di sync:**
- Ogni CP scritto da ME-A03 (M2)
- Ogni ADR registrato da ME-A05 (M3)
- Ogni aggiornamento state.json da ME-A08 (M4)
- Ogni apertura/chiusura sessione da ME-A04 (M2)
- Richiesta audit manuale o automatica (scheduler periodico)

**Output (per ogni evento):**
- Entry in `second-brain-vault/wiki/log.md` (vista umana)
- `memory_store` su AgentDB namespace `memory/<tipo>` (recall semantico)
- Audit report in `company/Memory/audit/audit-YYYYMMDD.md` (se audit completo)

**Acceptance criteria:**
- Ogni CP/ADR ha corrispondente entry wiki/log.md entro 60s dalla scrittura
- Ogni CP/ADR ha corrispondente vettore in AgentDB entro 60s
- Divergenza rilevata da audit → alert immediato a ME-Conductor + log in audit/
- 0 CP orfani (scritti in checkpoints/ ma non in INDEX o AgentDB)

---

## Team agenti

| Codice | Agente | Livello | Ruolo |
|---|---|---|---|
| ME-A09 | wiki-syncer (sync-agent) | L3 Worker | Propaga eventi a wiki/log.md e AgentDB namespace memory/ |
| ME-A10 | memory-sentinel (integrity-auditor) | L4 Worker | Audit trail, CP orfani, backup/rollback, verifica integrità 3 strati |

---

## Workflow

### Sync ordinario (post ogni evento)
```
evento (CP/ADR/state/session) ricevuto da M5
  → ME-A09: compone entry wiki/log.md (formato: data, tipo evento, id, summary)
  → ME-A09: appende entry a second-brain-vault/wiki/log.md
  → ME-A09: chiama memory_store(namespace=memory/<tipo>, id=<id>, content=<contenuto>)
  → ME-A09: conferma sync completato a ME-Conductor
```

### Audit periodico (settimanale o su richiesta)
```
trigger audit
  → ME-A10: legge tutti i CP in checkpoints/ → lista CP-ids
  → ME-A10: legge INDEX.md → lista CP-ids indicizzati
  → ME-A10: chiama memory_search(namespace=memory/checkpoints) → lista vettori
  → ME-A10: diff tre liste → trova orfani e gap
  → risultato OK → log verde in audit/
  → risultato GAP → alert ME-Conductor + entry audit/ con lista gap
  → ME-A10: verifica backup (pattern backup→append→log→rollback)
```

---

## Come funziona (flusso dettagliato)

1. **Ricezione evento:** ME-A09 riceve notifica da qualsiasi agente M2/M3/M4 che ha
   scritto in company/Memory/ (o da ME-Conductor via broadcast)
2. **Composizione entry wiki:** ME-A09 formatta l'evento per la vista umana:
   `## YYYY-MM-DD — [tipo]: [id] — [summary una riga]`
3. **Append wiki/log.md:** ME-A09 fa solo append al file (mai overwrite) —
   pattern backup→append→log di Memory Empire
4. **Store AgentDB:** ME-A09 chiama `memory_store` con namespace appropriato
   (`memory/checkpoints`, `memory/decisions`, `memory/state`, `memory/sessions`)
5. **Audit trail:** ME-A10 mantiene `company/Memory/audit/` con un file per ogni
   audit settimanale; ogni entry include hash del file originale per verifica integrità
6. **CP orfani:** ME-A10 confronta: (a) file in checkpoints/, (b) voci in INDEX.md,
   (c) vettori in AgentDB — qualsiasi discrepanza è un orfano → alert
7. **Rollback:** in caso di corruzione, ME-A10 usa la trace.jsonl e i backup in audit/
   per ricostruire lo stato precedente (mai distrugge, sempre append)

---

## Confini netti (cosa M5 NON fa)

- M5 **non scrive** in company/Memory/ (lo fanno M2/M3/M4) — M5 solo propaga
- M5 **non interpreta** il contenuto dei CP/ADR — li propaga as-is
- M5 **non è INTELLIGENCE**: wiki/log.md riceve eventi operativi, non conoscenza esterna
  (quella è dominio Memory Empire skill / Empire Studio)
- La direzione del sync è **unidirezionale** per wiki: Memory → wiki, mai wiki → Memory

---

## Namespace AgentDB

| Namespace | Contenuto | Agente |
|---|---|---|
| `memory/checkpoints` | ogni CP con summary + path | ME-A09 |
| `memory/decisions` | ogni ADR con decisione + stato | ME-A09 |
| `memory/state` | snapshot state.json per progetto | ME-A09 |
| `memory/sessions` | apertura/chiusura sessioni | ME-A09 |
| `patterns` | lezioni distillate → ReasoningBank | ME-A09 (relay) |

---

## Gate

- **G-ME4:** audit integrità settimanale verde (0 CP orfani, 0 divergenze)
- Sync considerato completato solo quando TUTTI e 3 i target ricevono l'evento
- ME-A10 ha diritto di veto su operazioni che violerebbero il pattern no-overwrite

---

## KPI

| KPI | Target |
|---|---|
| Divergenza file ↔ wiki ↔ AgentDB | 0 rilevate da audit |
| CP orfani | 0 |
| Latenza sync post-evento | ≤ 60s |
| Audit settimanale completato | 100% |
| File con overwrite (vs append) | 0 |

---

## Connessioni
- [[09-ECOSISTEMA-MEMORY]] — dossier madre
- [[INDEX]] — indice maestro (verificato da ME-A10 nel diff)
- [[STATO-EMPIRE]] — principale documento di stato (verificato da audit)
- [[M2-CHECKPOINT-SESSIONI]] — fonte primaria di eventi per ME-A09
- [[M3-ADR]] — fonte ADR per sync
- [[M4-PIANI-STATO]] — fonte aggiornamenti state.json per sync
- [[07-BACKBONE-RUFLO-SKILLS]] — AgentDB (infrastruttura usata da ME-A09)
- [[Memory_Empire]] — partner pattern backup→append→log→rollback
