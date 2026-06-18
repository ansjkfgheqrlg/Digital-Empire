---
Type: WORKFLOW
Status: Active
Tags: #workflow #email #winback #churn #dunning #L2-3
Created: 2026-06-18
Last updated: 2026-06-18
---

# WF-EMAIL-WINBACK — Post-Cancel / Churn Prevention / Dunning

> **Reparto:** L2.3 Email & Lifecycle · **Committenti:** 05-MB (SaaS), 02-INFO (community), 01-AGENCY (clienti inattivi)
> **Durata target:** 24-36h dal trigger al pacchetto pronto
> **Gate di uscita:** E5 + A6; exit survey → insight → AN4 → pattern "motivi di churn per ICP"

---

## Scopo

Produrre la sequenza win-back per utenti cancellati, inattivi o in churn prevention,
e la sequenza dunning per pagamenti falliti (SaaS). Il churn è un'obiezione non gestita
in tempo: questo workflow la affronta post-evento con CPB mirati. L'insight da exit survey
alimenta la ReasoningBank per migliorare le sequenze di onboarding e nurture future.

---

## Input richiesto

```json
{
  "committente": "05-MB | 02-INFO | 01-AGENCY",
  "tipo_winback": "post-cancel | churn-prevention | dunning",
  "prodotto": "nome + tipo",
  "trigger_evento": "cancel SaaS | inattività 45gg | pagamento fallito",
  "cluster_churn": {
    "n": "numero contatti nel cluster",
    "segmento": "descrizione segmento",
    "motivo_stimato": "da E3 o dichiarato dal committente"
  },
  "exit_survey": true,
  "deadline_consegna": "YYYY-MM-DD"
}
```

---

## Passi del workflow

### Passo 1 — Identificazione cluster churn (E5 + E3)
- E5 riceve il trigger dal committente: cancel, inattività, pagamento fallito.
- E3 analizza il cluster: chi sono? Da quanto tempo sono nel prodotto? Segmento (Free/Pro)?
  Storico comportamento (hanno mai raggiunto il first aha moment? hanno aperto le email di onboarding?).
- Il profilo del cluster orienta la strategia win-back.
- **Gate passo 1:** cluster definito con n, segmento, storico comportamento.

### Passo 2 — Exit survey design (E5)
- E5 progetta il form exit survey: max 2 domande chiuse + 1 aperta breve.
  - Domanda 1 (chiusa): "Cosa ti ha spinto a cancellarti?" con 4-5 opzioni.
  - Domanda 2 (opzionale, aperta): "Cosa avremmo potuto fare diversamente?"
- La brevità è la regola: survey più lunga = tasso completamento più basso.
- E5 progetta anche l'email di invio survey (1 email, tono diretto non giudicante).
- **Gate passo 2:** survey validata da EMAIL-LEAD (lunghezza, tono, opzioni plausibili per ICP).

### Passo 3 — Attesa risultati survey (async)
- La survey viene inviata (via ESP del committente) e si aspettano 24-48h per le risposte.
- Se tasso risposta <30%: E5 usa il motivo stimato da E3 come base della sequenza (non si aspetta all'infinito).
- **Gate passo 3:** motivo di churn identificato (da survey o da stima documentata).

### Passo 4 — Progettazione sequenza win-back (E5 + A6)
- E5 progetta la sequenza (max 3 email per non esaurire il credito relazionale residuo):
  - Email 1 (T+4 dalla survey): CPB per obiezione principale identificata (A6 produce il CPB).
  - Email 2 (T+7): offerta win-back con incentivo reale (es. sessione guidata, sconto reale, estensione prova).
  - Email 3 (T+10, opzionale): "ultima email da noi — vuoi che ti rimuoviamo dalla lista?"
- Per dunning: sequenza separata, tono empatico, focus sulla soluzione tecnica del pagamento.
  3 email: T+1 (notifica tecnica), T+4 (reminder con link aggiornamento metodo), T+7 (ultima chance).
- A6 produce il CPB per ogni email win-back che affronta un'obiezione.
- **Gate passo 4:** sequenza progettata e validata da EMAIL-LEAD.

### Passo 5 — Produzione copy (L2.1 WF-COPY-EMAIL)
- EMAIL-LEAD richiede copy a L2.1 per ogni email.
- A6 è l'agente principale per le email win-back (obiezioni = CPB).
- A7 per la CTA finale.
- A8 verifica score ≥80 su ogni email.
- **Gate passo 5:** A8 ≥80 su ogni email.

### Passo 6 — Deliverability check (E2)
- E2 verifica il cluster (spam score, PII check, dominio mittente).
- Attenzione: il cluster churn è per definizione disengaggiato — E2 verifica che l'invio
  non rischi la reputazione del dominio (invio a lista disengaggiata abbassa la reputazione).
- Se il cluster è >90gg inattivo: E2 raccomanda invio progressivo (non blast).
- **Gate passo 6:** E2 report PASS.

### Passo 7 — Gate E-QA finale
- E-QA verifica sequenza: A8 ≥80 + brand gate + deliverability.
- Verifica speciale per win-back: il tono è empatico e non aggressivo? La CTA è reale
  (nessuna scarcity falsa — Mandato Art.2.3)?
- **Gate passo 7:** E-QA PASS.

### Passo 8 — Distillazione insight (AN4) e consegna
- Dopo l'invio della sequenza e raccolta dei risultati (4-14 giorni), E5 produce il report churn:
  - Motivi di churn per ICP (da survey + comportamento).
  - Win-back rate: % recuperati.
  - Pattern: quale email ha avuto il maggiore impatto sul recovery?
- AN4 distilla i pattern in ReasoningBank: `marketing/email/sequences/winback/patterns/{icp}.json`.
- Questi pattern diventano input per E4 (migliorare l'onboarding) e E1 (anticipare l'obiezione in nurture).
- **Output finale:** sequenza + report E2 + report E-QA + pattern churn per AN4.

---

## Output del workflow

```json
{
  "sequence_id": "SEQ-WB-2026-NNN",
  "tipo": "post-cancel | dunning | churn-prevention",
  "n_email": "campo popolato a runtime",
  "motivo_churn_identificato": "campo popolato a runtime (da survey o stima)",
  "a6_cpb_usati": "n. CPB prodotti da A6",
  "qa_report": "E-QA PASS",
  "deliverability_report": "E2 PASS",
  "pattern_churn_path": "marketing/email/sequences/winback/patterns/{icp}.json",
  "win_back_rate": "campo popolato a runtime post-invio"
}
```

---

## Gate di uscita (riepilogo)

| Gate | Agente | Soglia | Bloccante |
|---|---|---|---|
| Cluster churn definito | E5 + E3 | n, segmento, motivo stimato | SÌ |
| Survey design | E5 | max 2 domande chiuse + 1 aperta | SÌ |
| Motivo churn identificato | E5 | da survey (≥30% risposta) o stima documentata | SÌ |
| Sequenza win-back | E5 + A6 | max 3 email; CPB per obiezione principale | SÌ |
| Score APSOC | A8 (L2.1) | ≥80 su ogni email | SÌ |
| Deliverability | E2 | PASS + raccomandazione invio progressivo se lista >90gg | SÌ |
| QA finale | E-QA | PASS; verifica tono empatico + no scarcity falsa | SÌ |
| Pattern AN4 | AN4 | da eseguire post-invio | NO (obbligatorio dopo) |

---

## Connessioni

- [[e5-winback-specialist]] · `agenti/e5-winback-specialist.md` — agente principale
- [[e3-segmentation-analyst]] · `agenti/e3-segmentation-analyst.md` — Passo 1
- [[e2-deliverability-guard]] · `agenti/e2-deliverability-guard.md` — Passo 6
- [[e-qa-email-verifier]] · `agenti/e-qa-email-verifier.md` — Passo 7
- [[ARCHITETTURA]] · `ARCHITETTURA.md` — §2.4 win-back e §4 namespace
