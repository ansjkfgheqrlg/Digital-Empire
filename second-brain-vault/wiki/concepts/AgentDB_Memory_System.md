---
Type: CONCEPT
Status: Active
Tags: #ai #memoria #second-brain #vector-search #hnsw #cap9
Created: 2026-05-29
Last updated: 2026-05-29
---

# AgentDB Memory System — Sistema di Memoria Persistente AI

## Overview
AgentDB è il sistema di memoria di Claude-Flow: pattern storage con ricerca semantica HNSW.
**Questo è l'architettura esatta da implementare nel Cap.9-10 di Exponium** (Second Brain).
Velocità: 150x-12.500x più rapida del linear scan per pattern retrieval.

## Principio Core
```
Prima di ogni task: SEARCH → "ho già risolto qualcosa di simile?"
Dopo ogni task:     STORE  → "salva il pattern per il futuro"
```

## Architettura del Memory System

```
AgentDB
├── Vector Index (HNSW)
│   ├── scraper-patterns/    ← soluzioni scraper funzionanti
│   ├── email-patterns/      ← template email + sequenze che convertono
│   ├── db-patterns/         ← schemi SQLite, query patterns
│   ├── ui-patterns/         ← componenti React/Tailwind
│   ├── ai-patterns/         ← prompt che funzionano, catene AI
│   ├── error-patterns/      ← errori comuni + fix
│   └── canva-patterns/      ← Gael: selettori Canva, flussi automation
├── Relational Store
│   ├── decisions.db         ← perché certi approcci scelti
│   └── sessions.db          ← log sessioni con link ai pattern
└── Search Engine
    ├── semantic search       ← "come scraping google maps?"
    ├── key-value retrieval   ← "dammi scraper-gmaps-v2"
    └── namespace filtering   ← "cerca solo in scraper-patterns"
```

## HNSW Vector Search (Hierarchical Navigable Small World)

```python
# Parametri ottimali per Exponium
hnsw_config = {
    "m": 16,                  # connections per node (16 = buon bilanciamento)
    "ef_construction": 200,   # quality dell'indice (più alto = migliore)
    "ef_search": 100,         # quality della ricerca (più alto = più precisa)
}

# Score interpretation:
# > 0.7  = match forte → usa il pattern direttamente
# 0.5-0.7 = match parziale → adatta il pattern
# < 0.5  = nessun match → crea soluzione nuova, poi storea
```

## Implementazione nel Second Brain di Exponium (Cap.9)

### File Structure
```
second-brain/
├── memory/
│   ├── __init__.py
│   ├── agentdb.py              ← core store/search engine
│   ├── embeddings.py           ← text → vector (OpenAI ada-002 o local)
│   ├── hnsw_index.py           ← HNSW implementation (hnswlib)
│   └── namespaces/
│       ├── scraper_patterns.db
│       ├── email_patterns.db
│       ├── error_patterns.db
│       └── canva_patterns.db
├── wiki/
│   ├── index.md
│   └── ... (wiki esistente)
├── search_cli.py               ← `python search.py "come scraping maps?"` 
└── CLAUDE.md                   ← istruzioni per Claude in questa wiki
```

### Core API
```python
class AgentDB:
    def store(self, key: str, value: str, namespace: str, tags: list[str] = []) -> bool:
        """Salva un pattern con embedding vettoriale"""
        embedding = self.embed(f"{key}: {value}")
        self.index[namespace].add(embedding, metadata={"key": key, "value": value, "tags": tags})
        return True
    
    def search(self, query: str, namespace: str, top_k: int = 5) -> list[dict]:
        """Ricerca semantica — restituisce i pattern più simili"""
        q_embedding = self.embed(query)
        results = self.index[namespace].search(q_embedding, k=top_k)
        return [{"key": r.key, "value": r.value, "score": r.score} for r in results]
    
    def get(self, key: str, namespace: str) -> str | None:
        """Recupero esatto per chiave"""
        return self.store[namespace].get(key)
```

### Dipendenze Python
```txt
hnswlib==0.8.0      # HNSW vector index
sentence-transformers==3.0.0  # embeddings locali (no API cost)
# oppure:
openai==1.35.0      # ada-002 embeddings (più accurati, costo API)
```

## Workflow di utilizzo (sessione Claude Code)

```
SESSION START:
1. search("task keywords") → trova pattern simili da sessioni passate
2. score > 0.7? → usa quel pattern come starting point
3. Implementa il task

SESSION END:
4. store("pattern-name", "what worked: approach + gotchas", namespace)
5. Le sessioni future trovano questa soluzione automaticamente
```

## Valore per Exponium

### Scrapers (scraper-patterns namespace)
- "Google Maps blocca dopo 50 requests" → stored, retrieved the next time
- "Selector #search-results cambiato in #results-container" → stored per Gael e Max
- "Headful mode bypassa CAPTCHA su Facebook" → pattern riusabile

### Email (email-patterns namespace)  
- "Subject con domanda aumenta open rate 40%" → stored con tag "A/B-test-result"
- "Sequenza 3 email: curiosità → prova → offerta" → template riusabile
- "Personalizzazione con nome azienda aumenta click" → insight persistente

### Canva (canva-patterns namespace — Gael)
- "Selector del campo titolo: [data-testid='text-input-0']" → stored, retrieved ogni sessione
- "Login via Google fallisce → usa email/password direct" → fallback noto

## Connessioni
- [[Tool_ClaudeFlow_Orchestration]] — fonte di questa architettura
- [[SPARC_Methodology]] — Phase 2: search memory before every implementation
- [[Swarm_Orchestration_Pattern]] — agenti condividono lo stesso memory store
- [[Exponium_Second_Brain]] — questo IS il Second Brain di Exponium
