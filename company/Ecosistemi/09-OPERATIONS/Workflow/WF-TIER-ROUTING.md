> Fonte: PIANO-MAESTRO/06-ECOSISTEMI-CORE.md sez. 09 §3 L3 WF-TIER-ROUTING

# L3 — WF-TIER-ROUTING (Enforcement 3-Tier Model Routing)

**Ecosistema:** 09-OPERATIONS · **Reparto L2:** COST-GUARD
**Coordinator:** `ops-tier-router` · **Direttore:** `ops-director`
**Connessione:** [[ECOSISTEMA.md]] · [[BACKBONE.md]]

## Missione

WF-TIER-ROUTING implementa il sistema 3-tier di selezione modello per tutti gli
agenti della holding. Il modello giusto per il task giusto: non si usa Opus dove
basta Haiku, non si usa Haiku dove serve Sonnet. Target: ≥70% dei task sul tier
economico (WASM/Haiku). Thompson Sampling via Ruflo aggiorna le probabilità su dati reali.

## I 3 Tier

| Tier | Modelli | Task adatti | Costo relativo |
|---|---|---|---|
| WASM/Edge | modelli leggeri locali | classificazione, routing, check semplici | ~$0 |
| Haiku | Claude Haiku | scrittura schematica, ledger, scheduling, lookup, notify | basso |
| Sonnet/Opus | Claude Sonnet, Opus | strategia, architettura, copy complesso, coordinamento, decisioni | alto |

## Regole di classificazione task

```
Task ripetitivo e schematico → Haiku (o WASM se non serve LLM)
  Esempi: emettere cost_event, aggiornare ledger, inviare alert, validare schema JSON
Task produzione standard → Sonnet
  Esempi: scrivere carosello, generare email personalizzata, coordinare workflow
Task strategia/architettura/decisione → Opus (con giustificazione scritta)
  Esempi: approvare architettura, deliberare budget, forgiare nuovo ecosistema
Task con Opus senza giustificazione → BLOCCATO da ops-tier-router
```

## Thompson Sampling (via Ruflo)

Il tier routing non è statico: impara dai fallimenti.
- Ogni task ricorda: tier scelto, esito (success/failed), costo.
- Se Haiku fallisce 2 volte sullo stesso tipo di task → promuove al tier superiore.
- Se Sonnet risulta overkill per tipo X (0 fallimenti ma costo alto) → propone downgrade.
- Le probabilità vengono aggiornate su AgentDB `operations/tier-stats`.

## Input / Output

**Richiesta routing (da qualsiasi agente pre-spawn):**
```json
{
  "task_tipo": "ledger-update|copy-carosello|architettura-ecosistema|...",
  "complessità": "semplice|media|alta",
  "contesto": "<descrizione breve del task>"
}
```

**Risposta routing:**
```json
{
  "tier": "Haiku",
  "modello": "claude-haiku-4-5",
  "giustificazione": "task schematico, tier economico sufficiente",
  "costo_stimato": 0.0001
}
```

## Processo decisionale (`ops-tier-router`)

1. Riceve descrizione task + complessità dichiarata dall'agente richiedente.
2. Classifica secondo le regole sopra + storico Thompson Sampling per questo tipo.
3. Se richiesto Opus: richiede giustificazione scritta. Senza → downgrade a Sonnet + log.
4. Restituisce tier + stima costo → l'agente usa il modello assegnato.
5. Post-task: riceve esito, aggiorna distribuzione Thompson Sampling.

## Gate di qualità

- `G-TIER-JUSTIFY` — Opus richiede giustificazione; altrimenti downgrade automatico
- `G-TIER-TARGET` — quota task su tier economico monitorata settimanalmente (target ≥70%)

## KPI

| Metrica | Target |
|---|---|
| Quota task su WASM/Haiku | ≥ 70% |
| Opus usato con giustificazione | 100% |
| Risparmio mese/mese per tier routing | trending positivo |
| Fallimenti per downgrade errato | ≤ 2% |
