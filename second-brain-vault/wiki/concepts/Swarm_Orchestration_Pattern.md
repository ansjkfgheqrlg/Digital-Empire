---
Type: CONCEPT
Status: Active
Tags: #ai #multi-agent #swarm #parallelismo #architettura
Created: 2026-05-29
Last updated: 2026-05-29
---

# Swarm Orchestration Pattern — Multi-Agent Coordination

## Overview
Il pattern swarm coordina più agenti AI specializzati che lavorano in parallelo o in sequenza.
Estratto da Claude-Flow V3. Applicazione immediata: Exponium Cap.6+ (scrapers paralleli).
Applicazione futura: Agency Digital Empire (team virtuale per clienti).

## Principio Core
```
Un coordinator dirige → agenti specializzati eseguono → risultati aggregati
```
**Non un agent che fa tutto** → più agent, ognuno esperto nel suo ruolo.

## Tipi di Agenti

| Agente | Ruolo |
|--------|-------|
| `coordinator` | Dirige, assegna task, traccia progresso |
| `architect` | Progetta sistema, definisce interfacce |
| `researcher` | Analizza requisiti, esplora codice esistente |
| `coder` | Scrive codice di produzione |
| `tester` | Scrive test, verifica comportamento |
| `reviewer` | Code review, quality check, security scan |
| `security-architect` | Threat modeling, validazione input |
| `performance-engineer` | Profiling, ottimizzazione |

## Topologie

### Hierarchical (default — anti-drift)
```
coordinator
├── architect
├── coder-1 (modulo A)
├── coder-2 (modulo B) ← parallel
├── tester
└── reviewer
```
Usa per: implementazioni feature strutturate.

### Parallel Workers (Exponium scraper swarm)
```
coordinator
├── scraper-google-maps   → 100 lead/giorno
├── scraper-facebook      → 100 lead/giorno  ← tutti parallel
├── scraper-linkedin      → 100 lead/giorno
├── scraper-youtube       → 100 lead/giorno
└── dedup-aggregator      → merge + deduplica
                               ↓
                          500 lead/giorno totali
```
Usa per: Cap.6+ Outreach Platform.

### Pipeline (processing sequenziale)
```
researcher → architect → coder → tester → reviewer
```
Usa per: SPARC methodology phases.

## Applicazione Exponium (Cap.6+)

### Swarm Scraping giornaliero
```python
async def daily_scrape(target: int = 500) -> list[Lead]:
    per_source = target // 4  # 125 per source
    
    tasks = await asyncio.gather(
        GoogleMapsScraper().run(limit=per_source),
        FacebookScraper().run(limit=per_source),
        LinkedInScraper().run(limit=per_source),
        YouTubeScraper().run(limit=per_source),
    )
    
    all_leads = [lead for batch in tasks for lead in batch]
    return deduplicate(all_leads)  # coordinator's job
```

### Swarm Content Factory (Max + Gael collaboration)
```
Max's swarm:           Gael's swarm:
ai-copy-generator  →   canva-login
                        canva-open-template
                        canva-fill-texts (uses Max's copy)
                        canva-download
                        hitsfield-upload
```

## Consensus Algorithms

| Algoritmo | Uso |
|-----------|-----|
| `raft` | Decision making su task assignment (default) |
| `byzantine` | Validazione cross-agent (sicurezza critica) |
| `gossip` | Propagazione stato tra agenti distribuiti |

## Swarm per Digital Empire Agency

Mapping per future client engagements:
```
Client Project Swarm:
├── coordinator (Max / account manager)
├── researcher (analizza brief cliente)
├── architect (progetta soluzione CRO)
├── copywriter-agent (genera copy AI)
├── designer-agent (landing page)
└── qa-reviewer (CRO check pre-lancio)
```

Con memory condivisa: ogni pattern appreso da un cliente viene usato per i successivi.

## Anti-patterns
- **God agent**: un solo agent che fa tutto → sessione lenta, scope immenso
- **No coordinator**: agenti paralleli senza merge step → conflitti di dati
- **Premature parallelism**: dipendenze non rispettate → broken integrations
- **No checkpoints**: swarm di 2h senza save → lavoro perso al blocco

## Connessioni
- [[Tool_ClaudeFlow_Orchestration]] — fonte di questo pattern
- [[AgentDB_Memory_System]] — memoria condivisa tra agenti swarm
- [[SPARC_Methodology]] — SPARC Phase 3 usa architettura swarm
- [[Exponium_Outreach_Platform]] — implementazione concreta Cap.6+
