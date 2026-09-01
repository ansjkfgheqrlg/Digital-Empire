# Failure Modes — enrichment-research / department-lead

## FM-01: atoms.json non generato
**Causa:** ingestion-archive non ha prodotto atoms
**Fix:** Genera manualmente dal video-analysis.md (ogni fatto/regola/prompt = 1 atomo)

## FM-02: Pipeline interrotta a metà
**Causa:** Un agente non produce l'handoff atteso
**Fix:** Timeout 30s per agente; se manca → il dept-lead produce la fase manualmente

## FM-03: Nessun report all'utente
**Causa:** Enrichment finito senza comunicazione
**Fix:** Regola invariante: il dept-lead parla sempre all'utente dopo il pipeline

## FM-04: skill-enricher modifica file sbagliato
**Causa:** Path errato in proposals.json
**Fix:** permission-guard verifica il path prima di ogni esecuzione
