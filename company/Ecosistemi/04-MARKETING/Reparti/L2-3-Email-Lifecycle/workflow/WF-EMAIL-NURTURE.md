---
Type: WORKFLOW
Status: Active
Tags: #workflow #email #nurture #welcome #reengagement #L2-3
Created: 2026-06-18
Last updated: 2026-06-18
---

# WF-EMAIL-NURTURE — Welcome + Nurture + Re-Engagement

> **Reparto:** L2.3 Email & Lifecycle · **Committente tipico:** tutti gli ecosistemi con lista opt-in
> **Durata target:** 24-48h dal brief al pacchetto pronto
> **Gate di uscita:** A8 ≥80 su ogni email; WF-AB-TEST su subject e CTA (opzionale ma raccomandato); AN4 pattern distillati dopo invio

---

## Scopo

Produrre la sequenza welcome + nurture per nuovi opt-in e la sequenza di re-engagement per
contatti inattivi. Il nurture costruisce fiducia e prepara il terreno per future offerte;
il re-engagement tenta di recuperare contatti "freddi" prima che vengano rimossi dalla lista.

---

## Input richiesto

```json
{
  "committente": "04-MKT | 02-INFO | 01-AGENCY | 05-MB",
  "tipo_nurture": "welcome_new | reengagement_inattivi | full_nurture",
  "icp": "avatar target + awareness level",
  "lista": "n. contatti + stato attività (nuovi / inattivi da X giorni)",
  "brand_kit": "DE | cliente-X",
  "contenuti_disponibili": ["case study 1", "quick win 2", "ebook gratuito 3"],
  "frequenza_target": "email ogni N giorni (es. ogni 2-3 giorni)",
  "deadline_consegna": "YYYY-MM-DD"
}
```

---

## Passi del workflow

### Passo 1 — Segmentazione e analisi lista (E3)
- E3 analizza la lista: distingue i nuovi opt-in dagli inattivi; per gli inattivi, verifica
  da quanti giorni non aprono (30, 60, 90+ giorni → tasso di recupero decrescente).
- Per re-engagement: identifica la soglia di pulizia (lista >90 giorni inattiva → raccomanda
  rimozione sicura piuttosto che invio rischioso).
- **Gate passo 1:** segmentazione validata — lista sana o piano igiene dichiarato.

### Passo 2 — Architettura sequenza (E1)
- E1 progetta la sequenza welcome/nurture:
  - Email 1 (T+0): welcome — chi siamo, cosa aspettarsi, quick win immediato
  - Email 2 (T+2): valore — contenuto educativo per ICP
  - Email 3 (T+5): social proof — case study o storia cliente
  - Email 4 (T+9): approfondimento — problema + approccio parziale
  - Email 5 (T+14): CTA — invito al passo successivo
  - Email 6 (T+30, branch inattivi): re-engagement — "sei ancora con noi?"
- Per re-engagement standalone: sequenza 3 email con subject diretto ("ci manchi",
  "ultima email da noi", "vuoi restare in lista?").
- **Gate passo 2:** mappa sequenza validata da EMAIL-LEAD.

### Passo 3 — Test A/B subject e CTA (L2.4/WF-AB-TEST — raccomandato)
- AN3 progetta test A/B su 2 varianti subject per le email 1 e 5 (maggiore impatto su open rate e conversione).
- Variante A: subject diretto; Variante B: subject curiosità/domanda.
- Dimensione campione minima calcolata da AN3 prima di dichiarare il vincitore.
- Questo passo è raccomandato per sequenze sulla lista principale DE; opzionale per liste
  di test o sequenze brevi.
- **Gate passo 3:** AN3 approva il design del test se eseguito; se saltato, si documenta la decisione.

### Passo 4 — Produzione copy (L2.1 WF-COPY-EMAIL)
- EMAIL-LEAD invia contratto di richiesta copy a L2.1 per ogni email.
- A8 verifica score ≥80 su ogni email.
- Per le email di re-engagement: A6 interviene sull'ultima email (gestisce l'obiezione
  "non ho più interesse" con CPB dell'ultimo momento).
- **Gate passo 4:** A8 ≥80 su ogni email.

### Passo 5 — Deliverability check (E2)
- E2 verifica spam score del batch (target ≤3/10) e stato lista.
- PII check: `aidefence_has_pii` sul campione lista — obbligatorio.
- Per re-engagement su lista inattiva >60gg: E2 raccomanda warm-up (invio progressivo, non blast).
- **Gate passo 5:** E2 report PASS.

### Passo 6 — Gate E-QA finale
- E-QA verifica batch completo: A8 ≥80 + brand gate G2 + deliverability.
- Verifica anche la coerenza narrativa della sequenza welcome: progredisce verso la CTA?
- **Gate passo 6:** E-QA PASS globale.

### Passo 7 — Consegna e setup AN4 post-invio
- EMAIL-LEAD consegna pacchetto al committente.
- Setup AN4: AN4 riceve istruzioni per distillare i pattern dopo il primo ciclo di invio
  (open rate per step, click rate, reply rate se aperta la risposta).
- I pattern vengono salvati in `marketing/copy/patterns/{icp}/email-nurture/`.
- **Output finale:** sequenza nurture + report + setup AN4 per raccolta pattern.

---

## Output del workflow

```json
{
  "sequence_id": "SEQ-NUR-2026-NNN",
  "tipo": "welcome_nurture",
  "n_email": "campo popolato a runtime",
  "test_ab_soggetti": "eseguito | saltato (motivazione: campo a runtime)",
  "qa_report": "E-QA PASS",
  "deliverability_report": "E2 PASS",
  "an4_setup": "attivo — raccolta pattern dopo primo invio",
  "path_namespace": "marketing/email/sequences/nurture/SEQ-NUR-2026-NNN/"
}
```

---

## Gate di uscita (riepilogo)

| Gate | Agente | Soglia | Bloccante |
|---|---|---|---|
| Segmentazione lista | E3 | lista sana o piano igiene dichiarato | SÌ |
| Mappa sequenza | E1 | ogni email con timing + obiettivo | SÌ |
| Test A/B design | AN3 | campione minimo calcolato (se eseguito) | NO (raccomandato) |
| Score APSOC | A8 (L2.1) | ≥80 su ogni email | SÌ |
| Deliverability | E2 | PASS (spam ≤3; PII OK) | SÌ |
| QA finale | E-QA | PASS su tutte le email | SÌ |
| Pattern AN4 | AN4 | setup post-invio documentato | NO (da eseguire post-lancio) |

---

## Connessioni

- [[email-lead]] · `agenti/email-lead.md`
- [[e3-segmentation-analyst]] · `agenti/e3-segmentation-analyst.md`
- [[e1-lifecycle-architect]] · `agenti/e1-lifecycle-architect.md`
- [[e2-deliverability-guard]] · `agenti/e2-deliverability-guard.md`
- [[e-qa-email-verifier]] · `agenti/e-qa-email-verifier.md`
