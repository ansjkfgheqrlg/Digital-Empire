---
Type: CONCEPT
Status: Active
Tags: #principi #advertising #marketing #L2-2
Created: 2026-06-18
Last updated: 2026-06-18
---

# PRINCIPI — L2.2 Advertising

> Principi operativi che guidano ogni decisione del reparto Advertising.
> Fonte: `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md §L2.2` + Mandato Empire Art.2 + Art.4.3

---

## P1 — Il copy non si scrive qui

Ogni parola di copy ads viene da L2.1 (WF-COPY-AD) con score APSOC ≥80 certificato da A8.
Advertising assembla, testa, ottimizza. Se in questo reparto qualcuno produce copy da zero,
è un errore di processo da segnalare ad ADS-LEAD.

Corollario: una variante "con un hook diverso" non si improvvisa localmente — si richiede
una nuova variante a L2.1 con il brief della variante.

---

## P2 — Dry-run di default, sempre (Art.4.3 Mandato)

Ogni piano campagna esce dal reparto con `dry_run: true` e `production: false`.
Il campo `production` diventa `true` SOLO quando l'approvazione esplicita di Max è registrata
in state.json con `approval_timestamp` e `approver`. Nessuna eccezione, nessuna urgenza,
nessuna "campagna di test piccola" giustifica saltare questo vincolo.

---

## P3 — Una variabile alla volta (test puro)

Nelle iterazioni creative: si modifica una sola variabile per ciclo (solo copy, o solo visual,
o solo audience). Modificare più variabili insieme toglie il segnale causale — non si sa cosa
ha funzionato. Il testing senza segnale causale è spreco di budget.

---

## P4 — Nessun verdetto senza campione sufficiente

AN3 (L2.4) valida la dimensione campione prima del lancio di ogni test. Il verdetto viene
dichiarato SOLO quando il campione predefinito è raggiunto. "Sembra che funzioni" non è un
verdetto. La campagna può essere interrotta per budget ma il verdetto è "inconclusivo", non
winner. I pattern si consolidano solo con evidenza ripetuta.

---

## P5 — Il budget sta sotto l'envelope approvato

AD3 non può andare oltre l'envelope approvato da CFO/Cost-Sentinel. Se il piano richiede
più budget: ADS-LEAD blocca, porta la richiesta a CFO, riprende il workflow solo dopo
l'aggiornamento dell'envelope. La spesa non autorizzata è un incidente da loggare.

---

## P6 — Gate in serie, non in parallelo

G3 (compliance AD4) e AD-QA sono gate in serie, non opzionali. Una campagna non può
bypassare AD4 per andare direttamente ad AD-QA, né viceversa. La sequenza è fissa:
G1 copy → G3 compliance → AD-QA → approvazione Max. Saltare un gate è un incidente.

---

## P7 — Prove non promesse nelle ads (Art.2 Mandato)

Ogni claim nelle ads deve avere una prova verificabile nella landing page.
"I migliori risultati del settore" senza dati reali: non passa AD-QA.
"300 email al giorno — come fa Outreach Factory" con demo nella landing: passa.
Il principio "prove non promesse" non è solo etico: è anche protezione dalla policy Meta
che rifiuta claim non substantiated.

---

## P8 — Pattern si accumulano, non si dimenticano

Ogni ciclo di test chiuso produce pattern in `marketing/ads/patterns/{icp_piattaforma}`.
AD2 legge questi pattern prima di costruire nuove varianti: non si ripetono varianti già
testate perdenti. Il vantaggio competitivo del reparto è la memoria cumulativa dei test.
Senza questa memoria, ogni campagna riparte da zero — è spreco strutturale.

---

## Connessioni

- [[REGOLE]] · `regole/REGOLE.md` — regole non negoziabili (vs principi orientativi)
- [[04-ECOSISTEMA-MARKETING-V2]] · `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md §L2.2`
- [[MANDATO-EMPIRE]] · `company/Mandato/MANDATO-EMPIRE.md` (Art.2 + Art.4.3)
