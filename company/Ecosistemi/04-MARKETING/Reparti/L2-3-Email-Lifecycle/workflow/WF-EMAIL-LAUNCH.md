---
Type: WORKFLOW
Status: Active
Tags: #workflow #email #lancio #infobusiness #L2-3
Created: 2026-06-18
Last updated: 2026-06-18
---

# WF-EMAIL-LAUNCH — Sequenza Lancio Email

> **Reparto:** L2.3 Email & Lifecycle · **Committente tipico:** 02-INFO-BUSINESS
> **Durata target:** 48-72h dal brief al pacchetto pronto
> **Gate di uscita:** WF-COPY-EMAIL A8 ≥80 su ogni email; E2 deliverability PASS; G2 brand gate PASS; review umana obbligatoria nelle prime fasi (Art.4.4 Mandato)

---

## Scopo

Produrre la sequenza email completa per un lancio prodotto (corso, ebook, community):
dalla fase di pre-lancio all'email di chiusura carrello. La sequenza copre l'intero arco
narrativo APSOC su più email, costruendo fiducia, prova, gestione obiezioni e urgenza reale.

---

## Input richiesto

```json
{
  "committente": "02-INFO",
  "prodotto": "nome prodotto + descrizione breve",
  "icp": "avatar target + awareness level di ingresso",
  "lista": "n. contatti + fonte + storico acquisti",
  "data_lancio": "YYYY-MM-DD (data apertura carrello)",
  "prezzo": "valore numerico (per urgenza reale negli ultimi giorni)",
  "proof_disponibili": ["testimonianza 1", "case study 2"],
  "brand_kit": "DE (default) | cliente-X",
  "deadline_consegna": "YYYY-MM-DD"
}
```

---

## Passi del workflow

### Passo 1 — Segmentazione lista (E3)
- E3 analizza la lista: segmenta per awareness level, storico acquisti, comportamento recente.
- Output: mappa segmenti con n per segmento, awareness level, branch necessari.
- **Gate passo 1:** mappa segmenti consegnata a EMAIL-LEAD e validata prima di procedere.

### Passo 2 — Architettura sequenza (E1)
- E1 riceve brief + segmentazione E3.
- Progetta la struttura narrativa del lancio:
  - Pre-lancio (T-14 a T-8): valore, curiosità, anticipazione
  - Apertura proposta (T-7 a T-5): claim + proof iniziale
  - Proof + obiezioni (T-4 a T-2): testimonianze + A6
  - Scarcity + chiusura (T-1 a T+0): urgenza reale, ultime ore
- Branch condizionali per segmenti identificati da E3.
- **Gate passo 2:** mappa sequenza validata da EMAIL-LEAD (n email, timing, obiettivi per email, branch).

### Passo 3 — Produzione copy (L2.1 WF-COPY-EMAIL)
- EMAIL-LEAD invia contratto di richiesta a L2.1 per ogni email (obiettivo + awareness_level + icp + vincoli).
- L2.1 esegue WF-COPY-EMAIL: A3 (headline/oggetto), A4 (problema), A5 (soluzione), A6 (obiezioni), A7 (CTA).
- A8 verifica ogni email: score ≥80 richiesto. Email sotto soglia → revisione; score <70 → rifacimento.
- **Gate passo 3:** A8 score ≥80 su OGNI email della sequenza. Nessuna eccezione.

### Passo 4 — Review umana (Art.4.4 Mandato)
- Le prime 2 email (T-14 e T-7) vengono sottoposte a review umana prima di procedere.
- Il committente (Max o referente 02-INFO) legge e approva tono, promise, proof.
- Questo passo è obbligatorio nelle prime fasi di ogni lancio — non si automatizza la prima sequenza.
- **Gate passo 4:** approvazione umana documentata (sì/no/modifiche richieste).

### Passo 5 — Deliverability check (E2)
- E2 riceve il batch di email + lista (campione pseudonimizzato) + dominio mittente.
- PII check obbligatorio: `aidefence_has_pii` prima di qualsiasi elaborazione lista.
- Verifica spam score per ogni email (target ≤3/10).
- Verifica autenticazione dominio (SPF/DKIM/DMARC).
- **Gate passo 5:** E2 report PASS su deliverability. Se FAIL → blocca, azioni correttive, rilancio E2.

### Passo 6 — Gate E-QA finale
- E-QA riceve il batch completo con A8 scores + report E2.
- Verifica ogni email: A8 ≥80 + brand gate G2 + deliverability.
- Verifica coerenza della sequenza come flusso narrativo.
- **Gate passo 6 (uscita definitiva):** E-QA PASS su TUTTE le email. Se FAIL → revisione mirata + re-submit.

### Passo 7 — Consegna e archiviazione
- EMAIL-LEAD assembla il pacchetto finale: sequenze email + mappa sequenza + report E2 + report E-QA.
- Salva in `marketing/email/sequences/launch/{sequence_id}/`.
- Consegna al committente con istruzioni di caricamento ESP.
- **Output finale:** pacchetto completo pronto per invio su ESP del committente.

---

## Output del workflow

```json
{
  "sequence_id": "SEQ-2026-NNN",
  "prodotto": "nome prodotto",
  "n_email_totali": "campo popolato a runtime",
  "segmenti": "n segmenti e branch",
  "qa_report": "E-QA PASS — A8 min: valore a runtime; brand gate: PASS",
  "deliverability_report": "E2 PASS — spam score medio: valore a runtime",
  "review_umana": "APPROVATO da committente (nome a runtime)",
  "path_namespace": "marketing/email/sequences/launch/SEQ-2026-NNN/",
  "pronto_per_invio": true
}
```

---

## Gate di uscita (riepilogo)

| Gate | Agente | Soglia | Bloccante |
|---|---|---|---|
| Mappa segmenti | E3 | completa e validata da EMAIL-LEAD | SÌ |
| Mappa sequenza | E1 | ogni email con timing + obiettivo dichiarato | SÌ |
| Score APSOC email | A8 (L2.1) | ≥80 su ogni email | SÌ |
| Review umana prime email | committente | approvazione documentata (Art.4.4) | SÌ |
| Deliverability | E2 | PASS (spam ≤3; SPF/DKIM/DMARC; PII OK) | SÌ |
| QA finale | E-QA | PASS su tutte le email + coerenza sequenza | SÌ |

---

## Connessioni

- [[email-lead]] · `agenti/email-lead.md` — coordina l'esecuzione
- [[e1-lifecycle-architect]] · `agenti/e1-lifecycle-architect.md` — Passo 2
- [[e2-deliverability-guard]] · `agenti/e2-deliverability-guard.md` — Passo 5
- [[e-qa-email-verifier]] · `agenti/e-qa-email-verifier.md` — Passo 6
- [[04-ECOSISTEMA-MARKETING-V2]] · `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md §L2.3`
