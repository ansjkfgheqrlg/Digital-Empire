---
Type: WORKFLOW
Status: Active
Tags: #workflow #CF-R6 #audit #mensile #pattern #apprendimento #forge #post-produzione
Created: 2026-06-23
Last updated: 2026-06-23
---

# WF-QUALITY-AUDIT — Audit Mensile Qualità CF-DE

> **Reparto:** CF-R6 QA & Gate · **Area:** Post-Produzione
> **Cadenza:** mensile obbligatoria (primo lunedì del mese)
> **Invariant:** ≥3 casi per pattern segnalato; nessuna conclusione su n < 3

---

## Scopo

Distillare i pattern ricorrenti nei gate falliti dell'intero mese, produrre un report
strutturato per CF-Director e 07-FORGE, e chiudere il loop tra fallimenti operativi e
miglioramenti strutturali del processo produttivo CF-DE. Non è una review puntuale:
è un audit aggregato che trasforma i FAIL individuali in apprendimento sistemico.

---

## Passi del workflow

| # | Passo | Agente | Input | Output | Condizione |
|---|---|---|---|---|---|
| 0 | Trigger mensile | CF-R6-COORD | calendario (primo lunedì del mese) | sessione audit aperta | cadenza fissa; non posticipabile |
| 1 | Raccolta FAIL mensili | CF-R6-LEARN | `cf/failures` + tutti i verdict.json del mese | dataset FAIL classificati per gate/brand/formato | tutti i FAIL del mese inclusi |
| 2 | Analisi pattern | CF-R6-LEARN | dataset FAIL | lista pattern (conferma: n ≥ 3; speculativo: n = 1-2) | solo pattern con ≥3 casi vengono segnalati |
| 3 | Analisi escalation | CF-R6-LEARN | lista escalation mese (n_rework ≥ 2) | pattern escalation se ≥3 casi dello stesso tipo | escalation sono segnali più critici dei singoli FAIL |
| 4 | Draft report | CF-R6-LEARN | pattern confermati + escalation pattern | draft `audit-YYYY-MM.json` | struttura fissa: gate, criterio, n, brand, causa ipotizzata, azione proposta |
| 5 | Validazione CF-R6-COORD | CF-R6-COORD | draft audit | audit validato o revisione | nessun pattern segnalato senza validazione CF-R6-COORD |
| 6 | Invio CF-Director | CF-R6-COORD | audit validato | report mensile a CF-Director | via `cf/qa` con flag "audit_mensile" |
| 7 | Invio 07-FORGE | CF-R6-COORD | sezione azioni proposte | richiesta a 07-FORGE per pattern strutturali | solo se azione proposta richiede nuova skill o modifica agente |
| 8 | Archiviazione | CF-R6-LEARN | audit validato | archivio `cf/failures/audits/audit-YYYY-MM.json` | pattern risolti marcati "risolto_in: YYYY-MM" |

---

## Invariant audit (non negoziabili)

1. **Soglia n ≥ 3**: nessun pattern viene segnalato in un report ufficiale se ha < 3 casi
   nel mese. I pattern speculativi (n = 1-2) rimangono in `cf/failures` come osservazioni
   non conclude e vengono rivalutati al mese successivo.
2. **Cadenza fissa**: il primo lunedì del mese, senza eccezioni. Posticipare l'audit
   significa perdere il segnale di apprendimento.
3. **Causa ipotizzata, non affermata**: il report distingue tra "causa ipotizzata"
   (da validare) e "causa confermata" (se l'azione di FORGE ha già risolto il pattern
   in precedenza). Nessuna causa affermata senza evidenza.
4. **Azione proposta, non prescritta**: CF-R6-LEARN propone azioni a CF-Director e 07-FORGE;
   la decisione di implementarle spetta a loro. CF-R6 non modifica workflow né agenti da solo.

---

## Schema audit-YYYY-MM.json

```json
{
  "audit_id": "AUDIT-2026-06",
  "mese": "2026-06",
  "ts_generazione": "2026-07-06T10:00:00Z",
  "totale_deliverable_qa": 47,
  "totale_pass": 38,
  "totale_fail": 9,
  "first_pass_rate_mese": 0.81,
  "pattern_confermati": [
    {
      "pattern_id": "PAT-COPY-HOOK-CAROSELLO-001",
      "gate": "GATE-COPY",
      "criterio": "hook assente o debole nella prima slide",
      "formato": "carosello-ig",
      "brand_coinvolti": ["mentalita-brutale", "brand-education"],
      "n_occorrenze_mese": 5,
      "n_occorrenze_totali": 5,
      "causa_ipotizzata": "CF-R5-SLIDECOPY non riceve hook_type valorizzato obbligatoriamente dal brief.json di CF-R1",
      "azione_proposta": "Aggiungere validazione hook_type obbligatoria in WF-BRIEF (CF-R1); CF-R5-SLIDECOPY blocca se campo assente",
      "destinatario_azione": "07-FORGE",
      "priorita": "alta"
    },
    {
      "pattern_id": "PAT-BRAND-FONT-CAROSELLO-001",
      "gate": "GATE-BRAND",
      "criterio": "font body non conforme al brand_kit (uso di font non autorizzato)",
      "formato": "carosello-ig",
      "brand_coinvolti": ["mentalita-brutale", "brand-agency"],
      "n_occorrenze_mese": 3,
      "n_occorrenze_totali": 3,
      "causa_ipotizzata": "WF-CAROSELLO non include check font pre-export in Canva; CF-R5-CANVA non verifica il font al momento dell'operazione di editing",
      "azione_proposta": "Aggiungere step verifica font in WF-CAROSELLO prima di export; o check in CF-R5-QA pre-CF-R6",
      "destinatario_azione": "07-FORGE",
      "priorita": "media"
    }
  ],
  "pattern_speculativi_non_segnalati": [
    {
      "pattern_id": "PAT-MANDATO-CLAIM-VIDEO-001",
      "n_occorrenze_mese": 2,
      "nota": "sotto soglia (n=2 < 3); rivalutare a luglio 2026"
    }
  ],
  "escalation_mese": [
    {
      "order_id": "CF-2026-0048",
      "tipo": "n_rework ≥ 2",
      "gate": "GATE-COPY",
      "n_rework": 2,
      "risolto": true
    }
  ],
  "anomalie_batch_mese": 0,
  "segnalazioni_cf_director": ["PAT-COPY-HOOK-CAROSELLO-001", "PAT-BRAND-FONT-CAROSELLO-001"],
  "segnalazioni_forge": ["PAT-COPY-HOOK-CAROSELLO-001", "PAT-BRAND-FONT-CAROSELLO-001"]
}
```

---

## Come si legge il report (per CF-Director e 07-FORGE)

**Per CF-Director:**
- `first_pass_rate_mese`: KPI mensile; se < 75% → attenzione sistemica.
- `pattern_confermati`: ogni entry ha una causa ipotizzata e un'azione proposta;
  CF-Director decide se approvare l'azione e prioritizzare con 07-FORGE.
- `escalation_mese`: ogni escalation (n_rework ≥ 2) richiede attenzione; pattern
  di escalation ripetuti = processo produttivo da rivedere.

**Per 07-FORGE:**
- I pattern con `destinatario_azione: "07-FORGE"` richiedono nuova skill, modifica
  di un workflow esistente, o aggiornamento della scheda agente interessata.
- La priorità (alta/media/bassa) orienta il backlog di FORGE.
- CF-R6 non prescrive la soluzione tecnica: propone l'obiettivo; FORGE decide come.

---

## Esempio operativo

**Audit:** 2026-06 · Primo lunedì di luglio 2026 (2026-07-06)

1. Passo 0: CF-R6-COORD apre sessione audit (data da calendario).
2. Passo 1: CF-R6-LEARN legge tutti i verdict.json di giugno da `cf/qa`;
   47 deliverable totali, 9 FAIL.
3. Passo 2: analisi pattern → 2 pattern confermati (n ≥ 3); 1 speculativo (n = 2).
4. Passo 3: 1 escalation nel mese (CF-2026-0048, GATE-COPY, 2 rework, risolto).
5. Passo 4: draft `audit-2026-06.json` con 2 pattern confermati, azioni proposte.
6. Passo 5: CF-R6-COORD valida il draft; nessuna revisione necessaria.
7. Passo 6: report inviato a CF-Director via `cf/qa`.
8. Passo 7: segnalazione a 07-FORGE per i 2 pattern (hook_type obbligatorio + check font).
9. Passo 8: archivio `cf/failures/audits/audit-2026-06.json` salvato.

---

## Connessioni

- [[cf-r6-learn]] · `agenti/cf-r6-learn.md` — esegue l'analisi pattern (passi 1-4)
- [[cf-r6-coord]] · `agenti/cf-r6-coord.md` — orchestra e valida il report (passo 5-8)
- [[state/README]] · `state/README.md` — namespace `cf/failures` dove sono archiviati i pattern
- [[03-ECOSISTEMA-CONTENT-FACTORY-V2]] · §CF-R8 — ecosistema che recepisce i pattern per l'ottimizzazione
