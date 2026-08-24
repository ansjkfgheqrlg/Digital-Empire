---
Type: TOOL
Status: Active
Tags: #apex7 #orchestration #quality-gates #multi-tenant #adr-010 #adr-011 #infrastruttura
Created: 2026-08-24
Last updated: 2026-08-24
---

# APEX-7-CORE — Motore di Orchestrazione Condiviso

## Overview
Motore comune di orchestrazione e quality-gate per gli agenti di Digital Empire
(`company/Ecosistemi/11-APEX-7-CORE/`). Nato per curare la frammentazione: prima di
[[ADR-010]] esistevano **6 implementazioni APEX-7-shaped divergenti** nel repo (YouTube,
skill generica, `11-APEX-7-CORE`, `12-STREAM-S7-BOT`, `empire/intelligence/apex7/`, più
uno zip consegnato da Max) — nessuna delle sei parlava con le altre, e ognuna reinventava
gate/memoria/bus a modo suo.

## Decisione (ADR-010, 2026-07-28)
Fondere le linee usando il motore già scritto in `11-APEX-7-CORE` come **motore condiviso**,
con namespacing multi-tenant per dominio (`APEX7Memory(domain=...)`,
`RuFLOOrchestrator(domain=...)`) verificato da `test_multi_tenant.py`. Pilota su 2
ecosistemi: **YouTube** (migrato con successo, F1-F6 tutte sul motore condiviso) e
**Stream-S7-Bot** (valutato e **NON migrato**, con motivazione scritta — vedi sotto).

## ADR-011 — il censimento era incompleto (2026-08-13)
ADR-010 contava 4 linee; ne esistevano 6. La quinta (`empire/intelligence/apex7/`, ~650
righe) separa esplicitamente mock e `LLMBackend` reale ed è risultata "la più onesta del
repo" — entra nel censimento come deprecata-non-cancellata, con i suoi due pezzi mancanti
al motore canonico (seam backend LLM, contratto RuFLO) da promuovere in un ciclo dedicato
(B-015, non ancora eseguito). La Fase 2 di ADR-010 (rollout sui restanti ecosistemi) resta
bloccata finché il motore canonico non sa parlare a un LLM reale — altrimenti il limite si
propaga 13 volte invece di una.

## Perché Stream-S7-Bot NON è stato migrato (decisione motivata, non pigrizia)
Verificato con audit comparativo diretto (non per dimensione dei file): l'implementazione
APEX-7 di `12-STREAM-S7-BOT` è **più matura** del motore condiviso su assi reali — 6 gate a
rubrica con 33 criteri misurabili (il motore condiviso ha solo un router di stage fisso),
Event Bus con priorità P0-P3/DLQ/replay (il condiviso non ha DLQ né replay), memory
interface con lock/checkpoint/restore, gate L6→L7 self-giudicante. Migrare avrebbe
significato un **downgrade funzionale** su un bot che esegue trade reali su Solana
mainnet — l'opposto dello spirito di ADR-010. Raccomandazione aperta per Max: portare le
funzionalità mancanti di Stream-S7-Bot DENTRO `11-APEX-7-CORE`, non il contrario.

## I 7 gate generalizzati (`orchestration/`, 2026-08-13)
Sottopacchetto additivo che innesta un layer di orchestrazione dominio-agnostico sopra il
`RuFLOOrchestrator` esistente, senza toccarlo (`git diff` verificato vuoto):
- `contracts.py` — StateSnapshot Merkle SHA-256, GateCheck/GateResult/GateBlocked
- `dag.py` — ordinamento topologico (Kahn), circuit breaker per nodo
- `bus.py` — `InstrumentedEventBus` (DLQ + registro consegne fallite, via sottoclasse)
- `gates.py` — i 7 gate generalizzati + GateLedger
- `healing.py` / `evolution.py` — self-healing tracciato, guardia sugli invarianti
- `pipeline.py` — `OrchestrationPipeline` che avvolge l'orchestratore esistente

**Regola di casa nata da un difetto reale**: nessun punto viene regalato — un check che non
si applica non viene emesso come "passato". Nato dall'audit di uno zip consegnato da Max che
dichiarava "100% PASS Tolleranza Zero L1-L7" ma aveva il Gate L6 mai chiamato, uno swarm
"RuFLO" che restituiva dizionari scritti a mano, e certificava scenari con capitale finale
negativo — ogni difetto trovato in quello zip ha oggi un test REGRESSIONE dedicato
(`test_orchestration.py`, 46/46 verde).

I tre consumatori di produzione già agganciati ai 7 gate: **skill-forge, carousel-machine,
cold-outreach** (i tre che ADR-010 elenca su `domain="default"`). **YouTube** vi si è
aggiunto tramite il retrofit di `apex7_orchestrator.py` (vedi
[[Concept_YouTube_Automation_Factory]]).

## Calc Layer (2026-08-14)
Secondo layer, `calc/` — 16 moduli di calcolo puro in 4 categorie (base, probabilità,
denaro, guadagni/royalty KDP) dietro un'interfaccia `esegui(dict) -> dict` pensata per
parlare con altri orchestration layer via JSON puro. Tre regole: nessun numero senza fonte
(default non dichiarati finiscono in `assunzioni`), nessuna eccezione oltre il confine,
vincoli rifiutati in ingresso (non arrotondati). Nato correggendo due errori finanziari
reali trovati nello stesso zip di Max (tassava il rendimento reale invece della plusvalenza
nominale; confrontava un valore atteso netto con un benchmark lordo — swing di decine di
migliaia di euro sulla stessa conclusione).

## Bug reali del motore condiviso trovati e gestiti
- `execute_workflow` su console Windows cp1252 andava in `UnicodeEncodeError` sul proprio
  banner — corretto separando libreria (solo ASCII) da entry point (UTF-8 forzato).
- `task_id` non sopravviveva ai restart → il guard-rail dei 3 giri di retry non scattava mai
  (rischio di loop infinito su critic score basso) — corretto.

## Come Impatta DE
È il "sistema nervoso" trasversale citato nella memoria persistente del progetto — la scelta
di curare la frammentazione invece di aggiungere una settima implementazione è il punto
architetturale su cui si regge ogni futuro rollout multi-ecosistema.

## Connessioni
- [[Concept_Decisioni_Architetturali_ADR]] — indice di tutte le decisioni, incl. ADR-010/011
- [[Concept_YouTube_Automation_Factory]] — primo consumatore reale del pilota ADR-010
- [[projects/Piano_Maestro_EMPIRE_OS]] — l'ecosistema 11 (Coordination/APEX-7) nel piano generale

## Status
- First added: 2026-08-24 (backfill wiki storico 06→08/2026, permesso esplicito Max)
- Confidence: Alta — verificato con esecuzione reale (test_apex7.py, test_orchestration.py,
  test_calc.py, test_multi_tenant.py tutti verdi ai checkpoint di origine)
