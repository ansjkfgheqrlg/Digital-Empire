---
Type: WORKFLOW
Status: Active
Tags: #workflow #email #onboarding #saas #attivazione #L2-3
Created: 2026-06-18
Last updated: 2026-06-18
---

# WF-EMAIL-ONBOARDING — Onboarding Attivazione

> **Reparto:** L2.3 Email & Lifecycle · **Committenti:** 05-MULTI-BUSINESS (SaaS) + 02-INFO-BUSINESS (corsi/community)
> **Durata target:** 24-36h dal brief al pacchetto pronto
> **Gate di uscita:** E4 progetta; E2 verifica; pattern salvati in `marketing/email/sequences/onboarding/`

---

## Scopo

Produrre la sequenza di onboarding attivazione per nuovi utenti di prodotti SaaS o acquirenti
di prodotti Info. L'obiettivo è portare il nuovo utente al "first aha moment" entro 7 giorni.
Ogni email ha 1 sola CTA. Il tasso di attivazione (% completamento primo passo entro 7gg)
è il KPI principale del workflow.

---

## Input richiesto

```json
{
  "committente": "05-MB | 02-INFO",
  "prodotto": "nome + tipo (SaaS | corso | community)",
  "first_aha_moment": "azione specifica che genera valore percepito entro 7gg",
  "segmenti": "da E3 (es. Free / Pro / acquirenti base / acquirenti advanced)",
  "n_utenti": "volume nuovo batch da onboardare",
  "vincoli_esp": "ESP in uso + trigger automatici disponibili",
  "deadline_consegna": "YYYY-MM-DD"
}
```

---

## Passi del workflow

### Passo 1 — Identificazione first aha moment (E4 + committente)
- E4 chiede al committente: qual è l'azione che, se completata nei primi 7 giorni, predice
  la ritenzione a 30 giorni? Se il committente non sa rispondere → E4 propone 3 candidati
  basati sulla struttura del prodotto e chiede conferma.
- Il first aha moment diventa il centro di gravità dell'intera sequenza.
- **Gate passo 1:** first aha moment dichiarato e accettato dal committente.

### Passo 2 — Segmentazione (E3)
- E3 analizza il batch: quanti segmenti richiedono onboarding diversi (es. Free vs Pro)?
  Per ogni segmento: obiettivo di attivazione specifico, punto di partenza (setup completato?
  mai acceduto? ha già usato prodotti simili?).
- E4 usa i segmenti per progettare varianti di sequenza.
- **Gate passo 2:** mappa segmenti validata; n. sequenze da produrre dichiarato.

### Passo 3 — Progettazione sequenza (E4)
- E4 progetta ogni sequenza per segmento:
  - 1 sola CTA per email (regola non derogabile).
  - Email T+0: accesso + prima azione immediata (non welcome generico).
  - Email T+1/T+2: check-in (completato il primo passo?).
  - Branch condizionale: completato → avanza al secondo step; non completato → supporto/tutorial.
  - Email T+5/T+7: first aha moment → celebrazione + passo successivo.
- **Gate passo 3:** mappa sequenza per ogni segmento validata da EMAIL-LEAD.

### Passo 4 — Produzione copy (L2.1 WF-COPY-EMAIL)
- EMAIL-LEAD invia contratto a L2.1 per ogni email di ogni segmento.
- Ogni email ha awareness_level specifico per il momento (nuovo utente: problema-aware →
  solution-aware; after first aha: product-aware).
- A8 verifica score ≥80 su ogni email.
- **Gate passo 4:** A8 ≥80 su ogni email di ogni variante di sequenza.

### Passo 5 — Deliverability check (E2)
- E2 verifica il batch (spam score, PII check, dominio mittente).
- Per onboarding: il dominio mittente è tipicamente quello del prodotto (es. hello@second-brain.io);
  E2 verifica la configurazione.
- **Gate passo 5:** E2 report PASS.

### Passo 6 — Gate E-QA finale
- E-QA verifica tutte le sequenze per tutti i segmenti.
- Verifica anche la logica dei branch condizionali: ha senso il percorso "completato" vs "non completato"?
- **Gate passo 6:** E-QA PASS su tutte le email e tutti i segmenti.

### Passo 7 — Archiviazione template e consegna
- EMAIL-LEAD assembla il pacchetto: sequenze + report E2 + report E-QA + istruzioni ESP.
- E4 salva il template base del tipo di prodotto/segmento in `marketing/email/sequences/onboarding/`.
- Consegna al committente con istruzioni di setup trigger su ESP.
- **Output finale:** pacchetto completo con template riutilizzabile per future onboarding dello stesso tipo.

---

## Output del workflow

```json
{
  "sequence_id": "SEQ-ONB-2026-NNN",
  "prodotto": "campo popolato a runtime",
  "n_segmenti": "campo popolato a runtime",
  "first_aha_moment": "dichiarato e accettato",
  "qa_report": "E-QA PASS su tutte le sequenze",
  "deliverability_report": "E2 PASS",
  "template_salvato": "marketing/email/sequences/onboarding/{prodotto}-template.json",
  "path_namespace": "marketing/email/sequences/onboarding/SEQ-ONB-2026-NNN/"
}
```

---

## Gate di uscita (riepilogo)

| Gate | Agente | Soglia | Bloccante |
|---|---|---|---|
| First aha moment dichiarato | E4 + committente | approvato dal committente | SÌ |
| Segmentazione | E3 | n. sequenze dichiarato | SÌ |
| Mappa sequenze | E4 | 1 CTA per email; branch condizionali espliciti | SÌ |
| Score APSOC | A8 (L2.1) | ≥80 su ogni email di ogni variante | SÌ |
| Deliverability | E2 | PASS | SÌ |
| QA finale | E-QA | PASS su tutte le sequenze | SÌ |

---

## Connessioni

- [[e4-onboarding-specialist]] · `agenti/e4-onboarding-specialist.md` — agente principale
- [[e3-segmentation-analyst]] · `agenti/e3-segmentation-analyst.md` — Passo 2
- [[e2-deliverability-guard]] · `agenti/e2-deliverability-guard.md` — Passo 5
- [[e-qa-email-verifier]] · `agenti/e-qa-email-verifier.md` — Passo 6
- [[ARCHITETTURA]] · `ARCHITETTURA.md` — §2.3 logica onboarding e namespace
