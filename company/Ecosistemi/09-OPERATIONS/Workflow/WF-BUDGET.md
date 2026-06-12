> Fonte: PIANO-MAESTRO/06-ECOSISTEMI-CORE.md sez. 09 §3 L3 WF-BUDGET

# L3 — WF-BUDGET (Dichiarazione Budget e Blocco Pre-Sforo)

**Ecosistema:** 09-OPERATIONS · **Reparto L2:** COST-GUARD
**Coordinator:** `ops-cost-sentinel` · **Direttore:** `ops-director`
**Connessione:** [[ECOSISTEMA.md]] · [[BACKBONE.md]]

## Missione

WF-BUDGET implementa il pattern #9 del Piano Maestro e l'OUT-OF-SCOPE #1:
zero spese API/crediti senza ok esplicito di Max. Il blocco scatta PRIMA dello sforo
(proiezione, non constatazione a danno fatto). Ogni nuova spesa mai vista richiede
approvazione umana — nessuna autonomia di spesa su servizi nuovi.

## Flusso dichiarazione budget

```
Ecosistema dichiara budget →
  WF-BUDGET registra {workflow, budget_per_run, budget_mensile_max} →
  ops-cost-sentinel attiva monitoring →
  ogni run: pre-check (stima ≤ residuo?) →
    SÌ: ok al lancio →
    NO: BLOCCO + 3 opzioni all'ecosistema
```

**Le 3 opzioni al momento del blocco (mai un blocco senza alternativa):**
1. Riduci scope (meno items nel batch)
2. Scendi di tier (Haiku invece di Sonnet)
3. Chiedi ok umano al CFO (Max approva spesa extra)

## Input / Output

**Dichiarazione budget (registrazione workflow):**
```json
{
  "workflow": "WF-OUTREACH-EMAIL",
  "ecosistema": "01-AGENCY",
  "budget_per_run": 0.00,
  "budget_mensile_max": 0.00,
  "tier_default": "Haiku",
  "spesa_nuova_api": false
}
```
**Se `spesa_nuova_api: true` → NESSUNA autonomia: handoff al CFO con stima, attende ok di Max.**

**Risposta pre-run (sincrona, bloccante):**
```json
{
  "approvato": true,
  "stima_costo": 0.00,
  "residuo_mensile": 0.00,
  "warning": null
}
```

## Soglie di allerta

| Soglia | Azione |
|---|---|
| 70% budget mensile consumato | warning al proprietario del workflow |
| 80% budget mensile consumato | alert formale + proiezione data sforo |
| 100% previsto (proiezione durante run) | STOP swarm + escalation ops-director |
| Spesa mai vista (nuova API) | STOP immediato + handoff CFO → ok umano Max |

## Processo decisionale (`ops-cost-sentinel`)

1. Pre-run: `stima = dry-run cost`. Confronta con budget residuo workflow E ecosistema.
2. In-run (stream): somma incrementale per shard. Al 70% → warning; all'80% → alert
   formale. Al 100% proiettato → STOP dell'intera run (unico reparto con potere di kill).
3. Spesa nuova mai vista: NESSUNA autonomia → handoff CFO, attende ok umano. No eccezioni.
4. Thompson Sampling aggiorna le probabilità tier su esiti reali: Haiku che fallisce 2x
   su un tipo di task → promuove tier automaticamente, memorizza su AgentDB.

## Gate di qualità

- `G-DRYRUN` — ogni workflow nuovo gira prima in dry-run con stima costi
- `G-BUDGET` — budget dichiarato PRIMA della prima run
- `G-HUMAN-APPROVAL` — spese nuove richiedono ok umano (Max); no eccezioni

## KPI

| Metrica | Target |
|---|---|
| Sforamenti budget | 0 |
| Blocchi pre-sforo attivati correttamente | 100% |
| Spese nuove approvate senza ok umano | 0 |
| Tempo risposta pre-check (sincrono) | ≤ 5s |
