---
Type: CONCEPT
Status: Active
Tags: #regole #advertising #marketing #gate #L2-2
Created: 2026-06-18
Last updated: 2026-06-18
---

# REGOLE — L2.2 Advertising

> Regole non negoziabili del reparto. A differenza dei principi (orientativi), queste
> regole sono BLOCCANTI: la loro violazione produce uno stop del workflow e un log di incidente.
> Fonte: `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md §L2.2` + Mandato Empire Art.4

---

## REGOLA 1 — MAI spesa ads reale senza ok esplicito di Max (Art.4.3 Mandato)

**BLOCCANTE. ASSOLUTA. SENZA ECCEZIONI.**

Nessuna campagna ads — nemmeno un "piccolo test" — va in produzione senza approvazione
esplicita di Max registrata in state.json con `approval_timestamp` e `approver`.
Il campo `production` di ogni campaign_plan.json è `false` per default.
Chiunque modifichi questo campo senza approvazione registrata commette un incidente da
loggare e segnalare al CMO e al CFO.

---

## REGOLA 2 — Il copy viene da L2.1, MAI scritto in Advertising

**BLOCCANTE.**

Se un agente di questo reparto produce copy persuasivo da zero, l'output è invalido.
Il copy arriva sempre da L2.1/WF-COPY-AD con score APSOC ≥80 certificato.
Advertising può indicare la direzione del copy richiesto (brief), ma non lo produce.

---

## REGOLA 3 — AD4 (G3) e AD-QA sono gate bloccanti, non opzionali

**BLOCCANTE.**

Nessuna campagna raggiunge AD3 (media buyer) senza aver passato AD4 (compliance G3).
Nessuna campagna raggiunge la richiesta di approvazione senza aver passato AD-QA.
Se ADS-LEAD o MKT-Conductor richiedono il bypass di un gate per urgenza → ADS-LEAD documenta
la pressione nel log e rifiuta il bypass. L'urgenza non esiste di fronte a un gate bloccante.

---

## REGOLA 4 — Dry-run di default per ogni piano campagna (Art.4.3)

**BLOCCANTE.**

AD3 produce `campaign_plan.json` con `dry_run: true` per default.
Il campo `dry_run` non si imposta a `false` localmente: lo fa solo ADS-LEAD dopo aver
ricevuto l'approvazione esplicita di Max. Non esiste "modalità veloce" che salti il dry-run.

---

## REGOLA 5 — Budget rispetta sempre l'envelope Cost-Sentinel

**BLOCCANTE.**

Il piano campagna non può allocare budget superiore all'envelope approvato da CFO/Cost-Sentinel.
Se il brief richiede più budget: ADS-LEAD blocca il workflow, porta la richiesta a CFO,
riprende solo dopo l'aggiornamento formale dell'envelope. Non si "testa" con budget non approvato.

---

## REGOLA 6 — Nessun verdetto senza campione minimo validato da AN3

**BLOCCANTE.**

AN3 (L2.4) valida la dimensione campione PRIMA del lancio del test.
AD6 non dichiara winner se il campione non è stato raggiunto.
Un test con verdetto su dati insufficienti non vale come test chiuso: va nel registro come
"inconclusivo" in `marketing/ads/experiments`.

---

## REGOLA 7 — PII proibita nel copy e nei brief (Art.7.2 Mandato)

**BLOCCANTE.**

Nessun dato personale identificabile entra nel copy delle ads o nei brief di targeting.
`aidefence_has_pii` viene chiamato su ogni input che potrebbe contenere dati personali
(liste email, brief con nomi clienti) prima dell'elaborazione. Se rilevato PII → blocco.

---

## REGOLA 8 — Log obbligatorio per ogni gate (PASS e FAIL)

**NON DEROGABILE.**

Ogni esecuzione di AD4 (G3) e AD-QA produce un record in `marketing/ads/compliance-log/`
e `marketing/ads/qa-log/` rispettivamente, con campaign_id, creative_id, esito, timestamp.
Il log non si può saltare neanche per le campagne interne. La tracciabilità è un requisito
operativo, non opzionale.

---

## Connessioni

- [[PRINCIPI]] · `principi/PRINCIPI.md`
- [[04-ECOSISTEMA-MARKETING-V2]] · `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md §7.1`
- [[MANDATO-EMPIRE]] · `company/Mandato/MANDATO-EMPIRE.md` (Art.4 gate + Art.4.3 spesa)
