# 🧠 BRAIN — Memoria condivisa della holding

> **Backbone component.** Tre livelli di memoria: strutturata (Memory), vettoriale (AgentDB), umana (wiki).

## I 3 livelli

| Livello | Sistema | Stato | Chi lo gestisce |
|---|---|---|---|
| **Strutturata** | `company/Memory/` — checkpoint, ADR, piani, stato | ✅ ATTIVO | Ecosistema 10-MEMORY |
| **Vettoriale** | AgentDB/HNSW (via Ruflo `memory_store/search`) | da init in F2 | 09-OPERATIONS |
| **Umana** | `second-brain-vault/wiki/` — fonte di verità leggibile | ✅ ATTIVO | 08-INTELLIGENCE |

## ReasoningBank

Ogni fallimento viene distillato in pattern e salvato nel ReasoningBank.
Namespace: `reasoningbank/<ecosistema>/<tipo_errore>`.
Da costruire in F2 (task 2.4).

## AgentDB — namespace per ecosistema (da inizializzare in F2)

```
ruflo memory init
ruflo memory init --namespace agency
ruflo memory init --namespace infobusiness
ruflo memory init --namespace content
ruflo memory init --namespace marketing
ruflo memory init --namespace multibusiness
ruflo memory init --namespace platform
ruflo memory init --namespace forge
ruflo memory init --namespace intelligence
ruflo memory init --namespace operations
ruflo memory init --namespace memory
ruflo memory init --namespace board
```

## Wiki bridge

`wiki-sync-guard` (skill da forgiare P0) garantisce che ogni operazione INTELLIGENCE
sincronizzi AgentDB con `wiki/log.md`. Quando la wiki viene aggiornata → AgentDB viene
indicizzato con i nuovi contenuti.

## Stato: parziale — wiki + Memory ATTIVI; AgentDB da init (F2, task 2.4)
