> Fonte: PIANO-MAESTRO/06-ECOSISTEMI-CORE.md sez. 08 L2 SECOND-BRAIN

# Reparto L2.3 — SECOND-BRAIN (Wiki Operations)

**Ecosistema:** 08-INTELLIGENCE · **Livello:** L2 · **Owner:** `int-librarian`

Collega: [[08-INTELLIGENCE/ECOSISTEMA.md]] · [[08-INTELLIGENCE/BACKBONE.md]]

---

## Cosa fa

SECOND-BRAIN custodisce e mantiene la **wiki `second-brain-vault/`** — la fonte di verità
umana di Digital Empire (pattern #12 wiki-first). Non è un repository passivo: è un sistema
vivente che viene aggiornato ad ogni operazione, mantenuto con cross-link, tenuto sincronizzato
con l'AgentDB, e purgato di pagine orfane periodicamente.

**Tre linee di lavoro:**
1. **WF-WIKI-CONTEXT** — context pack loader: un comando → `{pagine wiki rilevanti, memorie, pattern}` per qualsiasi ecosistema prima di un task
2. **WF-WIKI-SYNC** — bridge wiki ↔ AgentDB (anti-divergenza) + log.md enforcement
3. **WF-WIKI-GARDEN** — manutenzione: cross-link (≥2-3 per pagina), index.md, pagine orfane

---

## Struttura wiki (intoccabile)

```
second-brain-vault/wiki/
├── concepts/     → Framework, metodologie, principi
├── entities/     → Prodotti, persone, aziende
├── projects/     → Progetti attivi (Clienti/, Formazione/, Publishing/, Agency/)
├── tools/        → Agenti AI, tool, sistemi
├── sources/      → Risorse esterne, articoli, video
├── synthesis/    → Confronti, analisi cross-domain
├── index.md      → Catalogo master (aggiornato sempre)
└── log.md        → Registro operazioni (aggiornato sempre — mai saltare)
```

---

## Come si collega

| Con | Relazione |
|---|---|
| INGESTION | ogni ingestione produce pagine wiki → arrivano a SECOND-BRAIN per curation e cross-link |
| LEARNING / ReasoningBank | pattern con ≥3 conferme → promossi a pagina wiki in concepts/ o synthesis/ |
| FORGE | ogni artefatto FORGE produce pagina wiki tools/ (via int-librarian) |
| OPERATIONS | WF-WIKI-GARDEN schedulato da OPERATIONS/WF-CRON |
| Tutti gli ecosistemi | WF-WIKI-CONTEXT è il servizio più usato: context pack pre-task |

---

## Regola wiki-first (pattern #12)

Ogni operazione LOGGA in `wiki/log.md`:
```
## [Data]
- INGEST: [cosa] → [N] pagine create/aggiornate
- CREATE: [pagina] → [ecosistema/progetto]
- UPDATE: [pagina] → [cosa è cambiato]
```

Nessuna operazione su INTELLIGENCE è valida senza entry in log.md.

---

## Regola cross-link (gate G-LINK)

Ogni pagina nuova deve linkare almeno 2-3 pagine esistenti. Pagine senza cross-link →
rilevate da WF-WIKI-GARDEN → corrette entro 7 giorni.

---

## KPI

| Metrica | Target |
|---|---|
| Pagine nuove con ≥2 cross-link | 100% |
| Log.md aggiornato ad ogni operazione | 100% |
| Pagine orfane aperte > 7 giorni | 0 |
| Lag sync wiki ↔ AgentDB | < 24h |
| Index.md aggiornato dopo nuove pagine | 100% |
