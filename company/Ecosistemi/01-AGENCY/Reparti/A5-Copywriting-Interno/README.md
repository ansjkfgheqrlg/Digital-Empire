> Fonte: PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md sez. 2-A5 + sez. 6 + sez. 8

# A5 — COPYWRITING-INTERNO

> Reparto L2 di 01-AGENCY · Coordinatore: `AG-A5-COORD` (sonnet) · Topologia: `mesh` piccolo
> Fonte vincolante: `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md` §2-A5

## Cosa fa

Produce il **copy operativo quotidiano** dell'agency con framework APSOC: template email/DM,
micro-copy preventivi, script call. I pezzi grandi (sales page, sequenze lunghe, refresh strutturali)
si chiedono a **04 MARKETING** via `HC-AG-MK-01` — A5 è il consumatore-adattatore locale.
È il custode della **libreria obiezioni reali**, alimentata dalle conversazioni di A2.

| Livello | Team | Flusso / Funzione |
|---|---|---|
| L3 | `WF-COPY-OUTREACH` | refresh periodico template 3 canali: analisi reply reali → varianti APSOC → gate Bibbia → rollout graduale |
| L4 | `T-apsoc-writer` | scrittura/variazione copy con skill `cro-copy-architect` + `market-copy` |
| L4 | `T-objection-handler` | libreria obiezioni reali (da `HC-AG-IN-01`) → risposte testate |
| L4 | `T-copy-qa` | Gate Bibbia di A2 riusato (pattern #6: una skill, molti reparti) — blocca, non suggerisce |

Agenti L5: `AG-A5-COORD` · `AG-A5-COPY-W` · `AG-A5-OBJ-W` (schede in `../../Agenti/`).

## Come si collega

| Direzione | Con chi | Cosa passa |
|---|---|---|
| ← A2 Acquisizione | intra-BUS | dati reply reali: reply rate, motivi, obiezioni → input per refresh template |
| → A2 Acquisizione | intra-BUS | template aggiornati pronti per la run |
| ← 04 MARKETING | `HC-MK-AG-01` | copy maggiore: nuove sequenze, refresh strutturali, copy per preventivi |
| ← 08 INTELLIGENCE | `HC-AG-IN-01` (dati obiezioni) | obiezioni raccolte da A2 → libreria testata |
| Memoria | `agency/outreach` | template attivi + performance per variante per decidere quando refreshare |

Knowledge layer esistente: skill `cold-email`, `agency-scalping`, `cro-copy-architect` (APSOC),
suite `market-*` (15 skill). Il gate Bibbia (`bibbia_team.py`) è CONDIVISO con A2 (pattern #6):
A5 è il secondo consumatore autorizzato del gate.

## Come si ATTIVA e RAGIONA

**Trigger.**
1. Reply rate di A2 scende sotto baseline per 2 cicli → richiesta refresh a A5.
2. Gate Bibbia boccia in serie un template A2 → template ritirato, A5 produce variante.
3. Nuova obiezione ricorrente da `HC-AG-IN-01` → `T-objection-handler` aggiorna la libreria.
4. A3 richiede micro-copy per preventivo specifico → `T-apsoc-writer` produce su brief.

**Decomposizione.** `AG-A5-COORD` gestisce il `mesh` piccolo (writer ↔ objection ↔ qa):
- Brief di refresh arriva con dati reali (reply rate, obiezioni) → `T-apsoc-writer` produce
  variante APSOC ancorata al problema del target (never generic);
- `T-objection-handler` verifica che le varianti usino solo risposte con prove reali;
- `T-copy-qa` passa il Gate Bibbia: se boccia → feedback specifico a `T-apsoc-writer` → ciclo
  iterativo (mesh) fino a gate PASS;
- Template approvato → rollout graduale su A2 (test su batch piccolo prima del full rollout).

**Regola obiezioni.** La libreria contiene SOLO obiezioni raccolte da conversazioni reali (da A2 via
`HC-AG-IN-01`, anonimizzate) con risposte testate su prospect reali. Nessuna risposta inventata
entra nella libreria: "prove non promesse" si applica anche internamente.

**Failure.**
- Copy non passa il Gate Bibbia dopo 3 cicli → escalation a AG-A5-COORD: brief difettoso?
  Target sbagliato? Referenziale a 04 MARKETING.
- Nessun dato reale disponibile per il brief → A5 NON produce senza input da A2; segnala il gap.
- Risposta a obiezione non documentata da prove reali → `T-objection-handler` la blocca;
  la risposta entra in `agency/reasoning` come "non validata" fino a prova reale.

## KPI

| KPI | Definizione |
|---|---|
| % copy passato Gate Bibbia al primo giro | indicatore qualità pipeline interna |
| Tempo brief→copy | per tipi standard (email, DM, preventivo) |

## Connessioni

- [`../../Workflow/WF-COPY-OUTREACH/`](../../Workflow/WF-COPY-OUTREACH/)
- [`../../Funzioni/T-apsoc-writer/`](../../Funzioni/T-apsoc-writer/) · [`T-objection-handler/`](../../Funzioni/T-objection-handler/) · [`T-copy-qa/`](../../Funzioni/T-copy-qa/)
- [`../A2-Acquisizione/`](../A2-Acquisizione/) (cliente e fornitore dati) · [`../A6-Marketing-Interno/`](../A6-Marketing-Interno/) (case study e proof come input copy)
- [`../../BACKBONE.md`](../../BACKBONE.md) · [`../../ECOSISTEMA.md`](../../ECOSISTEMA.md)
