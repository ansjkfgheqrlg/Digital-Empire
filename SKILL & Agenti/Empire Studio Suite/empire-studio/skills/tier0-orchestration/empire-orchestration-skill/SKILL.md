---
name: empire-orchestration-skill
tier: tier0-orchestration
description: "Skill di orchestrazione di massimo livello: e' l'entrypoint /empire. Avvia la run, sceglie reparto e strategia, guida la pipeline a 9 stage attraverso tutti i reparti (ruflo swarm quando disponibile, altrimenti Conductor via Task). Governa tutte le altre skill."
controls:
  - tutte le skill tier1 (di reparto)
  - strategy-manifest-skill
  - verification-skill
  - memory-ecosystem-skill
---

# empire-orchestration-skill (tier0-orchestration)

> Il direttore d'orchestra: /empire avvia e coordina l'intero workflow.

## Cosa fa
- Riceve /empire <input> e classifica (video/canale/web/repo).
- Avvia memory bootstrap e chiede il Strategy Manifest.
- Instrada al reparto giusto e guida i 9 stage fino alla wiki + report.
- Orchestra in parallelo Verification e Memory (controllori/archivisti).

## Come si usa
```
/empire <link|path> [--dept=youtube|tiktok|web|projects] [--focus=...]
```

## Invarianti
- Memory-first (bootstrap prima di tutto).
- Strategy-first (Manifest prima dell'instradamento).
- Verifica prima di dichiarare 'fatto'.
- CLI-only, no API; visione = Claude.

## Agenti che la impugnano
- `conductor/conductor`

## Trace
risponde a 'questo e' un workflow intero coordinato da agenti e team'.
