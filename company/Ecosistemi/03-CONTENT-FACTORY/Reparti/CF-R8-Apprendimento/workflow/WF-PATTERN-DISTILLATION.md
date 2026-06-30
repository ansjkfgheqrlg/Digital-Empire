---
Type: WORKFLOW
Status: Active
Tags: #workflow #CF-R8 #pattern-distillation #hook #engine #failures #cf-patterns #apprendimento
Created: 2026-06-30
Last updated: 2026-06-30
---

# WF-PATTERN-DISTILLATION — Distillazione Pattern Hook + Failures + Engine

> **Reparto:** CF-R8 Apprendimento & Ottimizzazione · **Area:** Post-Produzione
> **Cadenza:** Settimanale per hook/angle; mensile per engine e failures
> **Gate bloccante:** nessun pattern entra in `cf/patterns` senza ≥3 casi e fonte tracciabile (Mandato Art.2)

---

## Scopo

Distillare dalle sorgenti di dati post-task (metriche di performance CF-R7, gate falliti CF-R6,
qualità engine CF-R5) i pattern operativi che permettono di migliorare la pipeline CF-DE nel tempo.
I pattern validati entrano in `cf/patterns`, aggiornano la libreria formule di CF-R1 e vengono
notificati al CF-Director. Nessuna conclusione viene archiviata senza evidenza a supporto.

---

## Passi del workflow

| # | Passo | Agente | Cadenza | Input | Output | Gate / Condizione |
|---|---|---|---|---|---|---|
| 0 | Trigger avvio | CF-R8-COORD | Sett. (hook) / Mensile (engine+failures) | Calendario ciclo; improvement_attivi | Sessione aperta; controllo idempotenza | Non avvia se ciclo già in corso |
| 1a | Analisi hook/angle | CF-R8-HOOK | Settimanale | feedback_entries CF-R7 del periodo | Lista pattern hook candidati (n ≥ 3 pre-filtrati) | Pre-filtro n ≥ 3 obbligatorio |
| 1b | Distillazione failures | CF-R8-REASONING | Mensile | `cf/failures` entries CONFERMATO del periodo | Lista lezioni strutturate con tipo_fix | Solo failures con status CONFERMATO |
| 1c | Analisi engine | CF-R8-ENGINE | Mensile | Verdetti CF-R6 + metriche CF-R7 del periodo | Lista pattern engine candidati (n ≥ 3 per cella comparabile) | Pre-filtro n ≥ 3 obbligatorio |
| 2 | Gate QA | CF-R8-QA | Ogni ciclo | Tutti i candidati da 1a, 1b, 1c | PASS/FAIL per ogni candidato con motivo strutturato | FAIL → candidato scartato con motivo; nessun "quasi PASS" |
| 3 | Archiviazione | CF-R8-COORD | Post-QA PASS | Pattern validati da CF-R8-QA | `memory_store("cf/patterns", pattern_validato)` per ogni PASS | Solo pattern con esito_qa: "PASS" |
| 4 | Aggiornamento CF-R1 | CF-R8-COORD → CF-R1-LEARN | Post-archiviazione | Pattern hook/angle validati | Proposta aggiornamento libreria formule CF-R1 con `{hook_type, peso, contesto}` | CF-R1-LEARN accetta o rifiuta con motivazione |
| 5 | Ottimizzazione routing CF-R5 | CF-R8-COORD → CF-Director | Post-archiviazione (mensile) | Pattern engine validati | Proposta aggiornamento routing capability→engine | Richiede approvazione CF-Director |
| 6 | Notifica CF-Director | CF-R8-COORD | Fine ciclo | Summary del ciclo | Report: n_validati, n_scartati, pattern di rilievo, anomalie | Obbligatorio a fine ogni ciclo |

---

## Topologia swarm (passi 1a, 1b, 1c in parallelo)

Nelle esecuzioni mensili, i passi 1a, 1b, 1c vengono eseguiti in parallelo (star topology):
CF-R8-HOOK + CF-R8-REASONING + CF-R8-ENGINE operano simultaneamente e confluiscono in CF-R8-QA
per il merge e la validazione. Nelle esecuzioni settimanali, solo 1a è attivo.

```
CF-R8-COORD (trigger)
        │
   ┌────┴────┬──────────┐
   │         │          │
CF-R8-HOOK  CF-R8-REASONING  CF-R8-ENGINE
(sett.+mens.)  (mensile)      (mensile)
   │         │          │
   └────┬────┴──────────┘
        │
   CF-R8-QA
   (gate-N3 + gate-FONTE + gate-CORRELAZIONE + gate-UNICITA)
        │
   ┌────┴────────────┐
   │                 │
PASS → memory_store  FAIL → scartato con motivo
   │
CF-R8-COORD
→ proposta CF-R1 (hook)
→ proposta routing CF-R5 (engine)
→ notifica CF-Director
```

---

## Gate 2: Validazione QA (criteri non negoziabili)

Eseguiti da CF-R8-QA su ogni pattern candidato prima dell'archiviazione.

| Gate | Criterio | Esito FAIL |
|---|---|---|
| Gate-N3 | n_casi ≥ 3 nel campo `esempi[]` | Pattern scartato con motivo "n_casi=[n] < 3 richiesti" |
| Gate-FONTE | Ogni caso ha `{namespace, key, ts}` tracciabile | Pattern scartato con motivo "caso [i] privo di fonte tracciabile" |
| Gate-CORRELAZIONE | Pattern formulato come osservazione, non causalità non dimostrata | Richiesta riformulazione al proponente (max 1 riformulazione per ciclo) |
| Gate-UNICITA | Nessun duplicato sostanziale già in `cf/patterns` | Merge proposto, non entry duplicata |

**Invariant assoluto:** nessun pattern entra in `cf/patterns` senza superare tutti e 4 i gate.
La pressione del tempo, la rilevanza percepita del pattern, o una richiesta del CF-Director
non alterano questa regola (Mandato Art.2 — "prove non promesse" vale anche internamente).

---

## State machine (state.json del ciclo WF-PATTERN-DISTILLATION)

```json
{
  "ciclo_id": "WF-PD-2026-06-30",
  "tipo": "settimanale | mensile",
  "fasi": {
    "00-trigger":     { "stato": "completato", "ts": "2026-06-30T07:00:00Z" },
    "01a-hook":       { "stato": "completato", "ts": "2026-06-30T08:00:00Z", "candidati": 2 },
    "01b-reasoning":  { "stato": "completato", "ts": "2026-06-30T08:30:00Z", "lezioni": 1 },
    "01c-engine":     { "stato": "completato", "ts": "2026-06-30T09:00:00Z", "candidati": 1 },
    "02-qa":          { "stato": "completato", "ts": "2026-06-30T09:30:00Z", "pass": 2, "fail": 2 },
    "03-store":       { "stato": "completato", "ts": "2026-06-30T09:35:00Z", "pattern_ids": ["PAT-R8-HOOK-MB-CAROSELLO-001", "PAT-R8-FAILURE-COPY-HOOK-001"] },
    "04-cf-r1":       { "stato": "completato", "ts": "2026-06-30T09:40:00Z", "proposta_inviata": true },
    "05-routing":     { "stato": "non_applicabile", "ts": null },
    "06-notifica":    { "stato": "completato", "ts": "2026-06-30T09:45:00Z" }
  },
  "pattern_validati_ciclo": 2,
  "pattern_scartati_ciclo": 2
}
```

---

## I/O JSON ciclo completo

**Input di avvio:**
```json
{
  "tipo_ciclo": "settimanale",
  "periodo": "2026-06-23/2026-06-30",
  "feedback_entries_disponibili": 18,
  "failures_confermati_disponibili": 0,
  "verdetti_engine_disponibili": 0,
  "improvement_attivi": 1
}
```

**Output di chiusura (notifica CF-Director):**
```json
{
  "ciclo_id": "WF-PD-2026-06-30",
  "tipo": "settimanale",
  "periodo": "2026-06-23/2026-06-30",
  "pattern_validati": 2,
  "pattern_scartati": 2,
  "pattern_scartati_motivi": [
    "CAND-R8-HOOK-MB-CAROSELLO-002: n_casi=2 < 3",
    "CAND-R8-HOOK-BE-ARTICOLO-001: n_casi=2 < 3"
  ],
  "proposta_cf_r1_inviata": true,
  "proposta_routing_inviata": false,
  "anomalie": [],
  "ts_chiusura": "2026-06-30T09:45:00Z"
}
```

---

## Regole di esecuzione (non negoziabili)

1. **Idempotenza** — il workflow non si avvia se un ciclo dello stesso tipo è già in corso
   (controllo su state.json del ciclo); la riesecuzione è sicura: i pattern già archiviati
   hanno `neural_trained` o `stato` che evita duplicazione.
2. **Pre-filtro n ≥ 3 obbligatorio** — CF-R8-HOOK e CF-R8-ENGINE pre-filtrano i candidati
   prima di inviarli a CF-R8-QA: i candidati con n < 3 non vengono inviati (sarebbero rifiutati);
   vanno nel buffer SPECULATIVO per accumulo.
3. **Nessuna conclusione senza dati** — se le feedback_entries del periodo sono < 5,
   CF-R8-HOOK non produce candidati e lo segnala nel report; il ciclo si chiude con 0 candidati.
4. **Max 3 improvement contemporanei** — CF-R8-COORD verifica `cf/improvements` prima di
   aprire il ciclo; se già 3 attivi: il workflow genera i pattern ma non apre nuovi improvement.
5. **Tracciabilità fonte** — ogni entry in `cf/patterns` deve avere almeno 1 fonte
   `{namespace, key, ts}` tracciabile per ogni caso nell'array `esempi[]`.

---

## Esempio operativo end-to-end (ciclo settimanale 23-30 giugno 2026)

**Passo 0 — Trigger:** CF-R8-COORD verifica calendario → ciclo settimanale in scadenza.
Improvement attivi: 1 (sotto il limite di 3). Sessione aperta.

**Passo 1a — CF-R8-HOOK:** legge 18 feedback_entries CF-R7 per il periodo.
Raggruppamento: hook_type "interrogativo-numerico" → 3 caroselli mentalita-brutale sopra baseline.
hook_type "lista-punti" → 2 articoli brand-education (SPECULATIVO, n=2).
Output: 1 candidato hook (n=3), 1 speculativo in buffer.

**Passo 1b — CF-R8-REASONING:** solo ciclo mensile → non attivo in questo ciclo. Output: vuoto.

**Passo 1c — CF-R8-ENGINE:** solo ciclo mensile → non attivo in questo ciclo. Output: vuoto.

**Passo 2 — CF-R8-QA:** 1 candidato hook ricevuto.
Gate-N3: n=3 → PASS. Gate-FONTE: tutti e 3 con {namespace, key, ts} → PASS.
Gate-CORRELAZIONE: formulato come osservazione → PASS. Gate-UNICITA: nessun duplicato → PASS.
Pattern_id assegnato: PAT-R8-HOOK-MB-CAROSELLO-001. Esito: PASS.

**Passo 3 — Archiviazione:** `memory_store("cf/patterns", PAT-R8-HOOK-MB-CAROSELLO-001)`.

**Passo 4 — CF-R1:** proposta inviata a CF-R1-LEARN: "hook_type 'interrogativo-numerico' +1 peso
per carosello-ig mentalita-brutale". Risposta attesa nel prossimo ciclo.

**Passo 5 — Routing:** non applicabile (ciclo settimanale, routing solo mensile).

**Passo 6 — Notifica:** CF-Director notificato: "1 pattern hook validato, 1 speculativo accumulato".

---

## Connessioni

- [[cf-r8-coord]] · `agenti/cf-r8-coord.md` — orchestra l'intero workflow
- [[cf-r8-qa]] · `agenti/cf-r8-qa.md` — esegue il gate di validazione (passo 2)
- [[WF-IMPROVEMENT-CYCLE]] · `workflow/WF-IMPROVEMENT-CYCLE.md` — usa i pattern validati da questo WF
