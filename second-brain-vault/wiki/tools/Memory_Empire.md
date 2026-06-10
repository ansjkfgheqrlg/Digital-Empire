---
Type: TOOL
Status: Active
Tags: #memoria #router #skill #digital-empire #orchestrazione #always-on
Created: 2026-06-08
Last updated: 2026-06-08
---

# Memory Empire

## Overview
Skill ufficiale **always-on** di Digital Empire: e' la memoria viva + il router
che attiva il workflow giusto. Si attiva (in modo naturale, senza comandi) quasi
ogni volta che si lavora dentro Digital Empire o quando l'utente passa un
contenuto da ingerire (video, canale, sito, repo).

## Dettagli
- **Posizione:** `~/.claude/skills/memory-empire/` (skill globale auto-attivante).
- **4 funzioni:** (1) memoria viva — carica contesto da wiki + `knowledge/`; (2)
  router — instrada e **attiva il workflow giusto** (rete di sicurezza); (3)
  archivio — salva ogni contenuto **per intero** (mai riassunto) in `knowledge/`
  E nella wiki; (4) **arricchitore** — aggiunge i principi/regole/esempi nuovi alle
  **altre skill** pertinenti (es. marketing da un video → skill `market-*`), in
  sicurezza (backup + append + log + rollback).
- **11 agenti in 4 categorie:** *operativi* (workflow-router, knowledge-keeper,
  skill-enricher, wiki-syncer), *analizzatori* (relevance-analyzer, gap-analyzer),
  *studiosi* (digital-empire-context, knowledge-cartographer), *controllori*
  (permission-guard, change-auditor, integrity-verifier).
- **4 script reali** (testati): `enrich_skill.py` (modifica sicura di altre skill),
  `relevance_scan.py` (trova le skill pertinenti), `audit_log.py` (log + rollback),
  `me_agent_factory.py`. Permessi ampi ma sicuri: vedi `PERMISSIONS.md`.
- **Regole (principi content-forge):** mai riassunti/compattazione; il video va
  visto; content-forge usato **tramite gli agenti di Empire Studio**, non a mano.
- **Collegamento operativo:** quando arriva un link, il router attiva
  [[Empire_Studio]], che guarda il video, forgia e scrive in wiki + Memory Empire
  (script reale `save_to_memory_empire.py`).

## Connessioni
- [[Empire_Studio]]
- [[Map - Agenti]]
- [[Map - Skill_And_Agenti]]
- [[Map - Progetti_Claude]]
