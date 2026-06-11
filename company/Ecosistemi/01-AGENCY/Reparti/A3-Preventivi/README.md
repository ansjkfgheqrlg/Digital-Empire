# A3 — PREVENTIVI

> Reparto L2 di 01-AGENCY · Coordinatore: `AG-A3-COORD` (opus) · Topologia: `pipeline`
> Fonte vincolante: `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md` §2-A3

## Cosa fa

Trasforma ogni discovery call in una **proposta problem-first inviata entro 48h**, con pricing
a catalogo (**mai sconti improvvisati**), che vende l'autonomia del cliente — non la dipendenza.

| Livello | Team | Flusso / Funzione |
|---|---|---|
| L3 | `WF-PREVENTIVO` | trascrizione/appunti call → brief strutturato → audit problema → outline problem-first → documento completo → Gate Preventivo → invio → follow-up commerciale |
| L4 | `T-discovery-brief` | da call a brief: problema, awareness level (aware/unaware), stack attuale, vincoli server/ambiente (skill `discovery-call-brief`) |
| L4 | `T-problem-audit` | quantifica il problema del cliente (skill `market-audit`, cro_audit) |
| L4 | `T-proposal-writer` | costruisce il preventivo (skill **`beast-preventivi`** + `market-proposal`) |
| L4 | `T-pricing-config` | seleziona prodotto/bundle: Outreach Factory €4.000 / Content Factory €3.500 / Second Brain €2.500 / Engine Room €8.000 — one-time, €0 canoni |
| L4 | `T-proposal-qa` | Gate Preventivo (skill `proposal-gate`) — blocca, non suggerisce |

Agenti L5: `AG-A3-COORD` · `AG-A3-BRIEF-W` · `AG-A3-AUDIT-W` · `AG-A3-PROP-W` (opus) ·
`AG-A3-PRICE-W` · `AG-A3-QA-W` (opus).

In più, A3 prepara il **dossier pre-call** per Max (lead + audit + competitor da A1) — la call
resta umana, ma arriva già istruita. Asset evoluti dentro T-discovery-brief:
`Agenti/Agency/outreach/script_chiamata_freddo.md`, `genera_tabella_chiamate.py`.

## Come si collega

| Direzione | Con chi | Cosa passa |
|---|---|---|
| ← A2 Acquisizione | intra-BUS | call prenotata + thread conversazione completo |
| ← A1 Ricerca | intra-BUS | dossier pre-call (profilo, audit problema, competitor) |
| → UMANO (Max) | — | dossier pre-call PRIMA della call; proposta pronta per invio |
| → A4 Delivery | intra-BUS | contratto firmato + scope congelato + prerequisiti ambiente raccolti in call |
| ← 04 MARKETING | `HC-MK-AG-01` | copy preventivi maggiore (refresh strutturali) |
| ← 08 INTELLIGENCE | `HC-IN-AG-01` | intelligence di nicchia per argomentare il problema |
| Memoria | `agency/proposals` | stato, win/loss, motivi — `memory_search` PRIMA di ogni preventivo nuovo |

## 🧠 Come si ATTIVA e RAGIONA

**Trigger.**
1. Call prenotata in calendario → T-discovery-brief prepara il dossier pre-call (prima della call).
2. Call avvenuta: trascrizione/appunti disponibili → parte `WF-PREVENTIVO` con countdown 48h.
3. Proposta inviata senza risposta → follow-up commerciale a cadenza definita.

**Decomposizione.** `AG-A3-COORD` esegue la pipeline lineare con gate finale:
brief (T-discovery-brief) → audit quantificato (T-problem-audit) → selezione prodotto/bundle
(T-pricing-config: SOLO catalogo) → scrittura problem-first (T-proposal-writer con
beast-preventivi: tutto ruota attorno al problema del cliente, adattato al livello di
consapevolezza aware/unaware) → Gate Preventivo (T-proposal-qa).

**Esecuzione.** Prima di scrivere: `memory_search` su `agency/proposals` (preventivi simili,
motivi di loss) e su `agency/reasoning` (pattern di preventivi persi). Il documento APRE con il
problema del cliente, mai con Digital Empire. Promesse = solo prove verificabili (Mandato Empire).
Clausole obbligatorie: proprietà del codice, €0 canoni, setup ≤7gg, supporto 90gg.

**Handoff.** Proposta passata dal gate → invio (≤48h dalla call) → record in `agency/proposals`.
Firma + pagamento verificato (umano) → handoff ad A4 con scope congelato. Loss → motivo
obbligatorio in `agency/proposals` + pattern in `agency/reasoning`.

**Failure.**
- Gate Preventivo boccia → rework con le note del gate (mai bypass), il countdown 48h resta.
- Brief incompleto (mancano vincoli ambiente) → richiesta integrazione a Max PRIMA di scrivere
  (i prerequisiti ambiente servono ad A4: il countdown delivery 7gg parte ad ambiente conforme).
- Richiesta sconto fuori catalogo → NO automatico; eventuale deroga = decisione Board registrata.
- 2 loss consecutive sulla stessa nicchia → audit pattern + `HC-AG-IN-01` per intelligence aggiornata.

## KPI

| KPI | Vincolo |
|---|---|
| Tempo call→preventivo | target ≤48h |
| Win rate | misurato dal giorno 1, baseline |
| Valore medio preventivo | pricing a catalogo: 4.000/3.500/2.500/8.000 € |

## Connessioni

- `../../Workflow/WF-PREVENTIVO/` — pipeline end-to-end del reparto
- `../../Funzioni/T-discovery-brief/` · `T-proposal-writer/` · `T-proposal-qa/`
- `../A2-Acquisizione/` (fornitore call) · `../A4-Delivery/` (cliente interno) · `../A1-Ricerca/` (dossier pre-call)
