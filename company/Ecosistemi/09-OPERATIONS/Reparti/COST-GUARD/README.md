# L2 — COST-GUARD (Il Guardiano dei Costi della Holding Intera)

> **Ecosistema:** 09-OPERATIONS · **Coordinator:** `ops-cost-sentinel` · **Direttore:** `ops-director`
> **Workflow L3:** `Workflow/WF-BUDGET/` · `Workflow/WF-ATTRIBUTION/` · `Workflow/WF-TIER-ROUTING/`
> **Supervisione C-Suite:** CFO (invariante: "dry-run prima di spendere", pattern #3)

## Cosa fa

COST-GUARD è il reparto più importante di OPERATIONS e uno dei più importanti della
holding: **nessun workflow di NESSUN ecosistema può spendere senza passare di qui.**
Implementa il pattern #9 (cost guard) e l'OUT-OF-SCOPE #1 del Piano Maestro
(zero spese API/crediti senza ok esplicito).

Tre workflow:
1. **WF-BUDGET** — ogni workflow/ecosistema dichiara un budget; il blocco scatta
   PRIMA dello sforo (proiezione, non constatazione); spese nuove → ok umano.
2. **WF-ATTRIBUTION** — ogni run emette evento `{ecosistema, workflow, agente, commessa,
   costo, durata, esito}` → ledger unico; run senza evento = run non valida (G-ATTRIBUTION).
3. **WF-TIER-ROUTING** — enforcement 3-tier (WASM/Haiku/Sonnet-Opus): il modello giusto
   per il task giusto, con Thompson Sampling via Ruflo. Target: ≥70% dei task su tier economico.

## Come si collega

| Con chi | Direzione | Cosa passa |
|---|---|---|
| TUTTI gli ecosistemi | inbound | dichiarazioni budget, eventi costo, richieste approvazione spesa |
| TUTTI gli ecosistemi | outbound | alert 80%, blocchi pre-sforo, verdetti tier |
| CFO (L0) | outbound | report settimanale costi per ecosistema; richieste ok per spese fuori budget |
| FORGE | inbound | ogni nuovo agente arriva con tier+costo stimato → entra nel cost model |
| Cost-Sentinel LX (`company/Sentinels/Cost-Sentinel/`) | outbound | il ledger e gli alert alimentano la sentinella di livello holding |
| RUNTIME / SCHEDULING | bidirezionale | approvazione pre-run; potere di STOP sugli swarm in corsa |
| 10-MEMORY | outbound | sforamenti evitati e decisioni di spesa → CP/ADR |

## 🧠 Come si ATTIVA e RAGIONA

**Attivazione.** Tre canali, tutti always-on (per questo il coordinator è una sentinel):
(a) richiesta di approvazione pre-run (sincrona, bloccante);
(b) flusso eventi costo durante le run (asincrono, mesh);
(c) scansione periodica del ledger per drift (run che costano più della media storica).

**Ragionamento del coordinator (`ops-cost-sentinel`):**
1. Pre-run: `stima = dry-run cost`. Confronta con budget residuo del workflow E
   dell'ecosistema. `stima > residuo` → BLOCCO con tre opzioni: riduci scope, scendi
   di tier, chiedi ok umano. Mai un blocco senza alternativa proposta.
2. In-run: somma incrementale. Al 70% → warning al proprietario. All'80% → alert
   formale + proiezione ("a questo ritmo sfori tra N item"). Al 100% previsto → STOP
   dello swarm (l'unico reparto con potere di kill su run altrui).
3. Tier routing: classifica il task (ripetitivo/schematico → Haiku o WASM; produzione
   standard → Sonnet; strategia/architettura → Opus, solo con giustificazione).
   Thompson Sampling aggiorna le probabilità su esiti reali: se Haiku fallisce 2 volte
   su un tipo di task, promuove il tier e lo memorizza.
4. Spesa nuova mai vista (nuova API, nuovo servizio) → NESSUNA autonomia: handoff al
   CFO con stima e motivazione, attende ok umano di Max.

**Principio:** il guardiano non fa risparmiare tagliando il lavoro — fa spendere il
minimo necessario per il risultato richiesto, e rende ogni euro attribuibile.

*Fonte: dossier 06 §09 L2 COST GUARD · Aggiornato: 2026-06-11*
