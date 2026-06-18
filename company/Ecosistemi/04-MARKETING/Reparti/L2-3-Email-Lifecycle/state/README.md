---
Type: STATE
Status: Active
Tags: #state #namespace #email #lifecycle #memoria #L2-3
Created: 2026-06-18
Last updated: 2026-06-18
---

# State & Namespace — L2.3 Email & Lifecycle

> Definisce il namespace AgentDB del reparto, gli schemi JSON di stato, le regole di integrità
> e la policy PII per il sistema di memoria di L2.3.

---

## Namespace AgentDB

**Namespace principale:** `marketing/email/sequences`

Struttura completa:

```
marketing/email/sequences/
├── launch/
│   └── {sequence_id}/
│       ├── sequence_map.json       ← output E1 (struttura completa)
│       ├── emails/                 ← copy gated (file .md per email)
│       │   ├── email_01.md
│       │   └── ...
│       ├── deliverability_report.json  ← output E2
│       ├── qa_report.json          ← output E-QA
│       └── script_log.json         ← log esecuzioni script
├── nurture/
│   └── {lista_id}/
│       └── (stessa struttura)
├── onboarding/
│   ├── {prodotto_id}/
│   │   └── (stessa struttura)
│   └── templates/
│       └── {tipo_prodotto}-template.json  ← template riutilizzabili (output E4)
└── winback/
    ├── {sequence_id}/
    │   └── (stessa struttura)
    └── patterns/
        └── {icp_id}.json           ← pattern motivi churn per ICP (output E5 → AN4)
```

---

## Schema JSON: sequence_map (output E1)

```json
{
  "sequence_id": "SEQ-YYYY-NNN",
  "tipo_sequenza": "lancio | nurture | onboarding | winback",
  "n_email_totali": 7,
  "icp": "id ICP",
  "segmenti": "riferimento a segmenti E3",
  "emails": [
    {
      "n": 1,
      "trigger": "trigger evento o T+N giorni",
      "timing": "T+0",
      "awareness_target": "livello awareness target per questa email",
      "obiettivo": "micro-obiettivo misurabile",
      "cta": "testo CTA principale",
      "branch": false,
      "note_copy": "campo popolato a runtime con output L2.1"
    }
  ],
  "creato_da": "E1",
  "validato_da": "EMAIL-LEAD",
  "timestamp": "YYYY-MM-DDTHH:MM:SSZ"
}
```

---

## Schema JSON: deliverability_report (output E2)

```json
{
  "sequence_id": "SEQ-YYYY-NNN",
  "gate_g3": "PASS | FAIL",
  "spam_score": {
    "media_sequenza": 0.0,
    "max_singola_email": 0.0,
    "email_con_issues": []
  },
  "autenticazione_dominio": {
    "spf": "PRESENTE | ASSENTE",
    "dkim": "PRESENTE | ASSENTE",
    "dmarc": "PRESENTE | ASSENTE"
  },
  "igiene_lista": {
    "bounces_sospetti": 0,
    "lista_acquistata": false,
    "raccomandazione": "campo popolato a runtime"
  },
  "pii_check": {
    "eseguito": true,
    "esito": "PASS | FAIL",
    "tool_usato": "aidefence_has_pii",
    "dati_sensibili_rilevati": false
  },
  "warm_up_necessario": false,
  "azioni_richieste": [],
  "timestamp": "YYYY-MM-DDTHH:MM:SSZ"
}
```

---

## Schema JSON: qa_report (output E-QA)

```json
{
  "sequence_id": "SEQ-YYYY-NNN",
  "gate_eqa": "PASS | FAIL",
  "n_email_verificate": 0,
  "a8_score_minimo": 0,
  "a8_score_medio": 0.0,
  "brand_gate_g2": "PASS | FAIL",
  "e2_deliverability": "PASS | FAIL (da report E2)",
  "coerenza_sequenza": "PASS | FAIL",
  "esito_per_email": [
    {
      "n": 1,
      "a8_score": 0,
      "a8_gate": "PASS | FAIL",
      "brand_gate_g2": "PASS | FAIL",
      "e2_deliverability": "PASS | FAIL",
      "esito": "PASS | FAIL",
      "feedback": "campo popolato a runtime in caso di FAIL"
    }
  ],
  "sequenza_pronta_per_invio": false,
  "timestamp": "YYYY-MM-DDTHH:MM:SSZ"
}
```

---

## Regole integrità namespace

1. **sequence_id univoco** — formato `SEQ-YYYY-NNN` (onboarding: `SEQ-ONB-YYYY-NNN`; winback: `SEQ-WB-YYYY-NNN`).
2. **Completezza obbligatoria** — una sequenza è "completa" nel namespace solo se ha:
   `sequence_map.json` + `deliverability_report.json` (E2 PASS) + `qa_report.json` (E-QA PASS).
   Sequenze parziali restano nella cartella ma non sono marcat come "pronte per invio".
3. **Email non-gated escluse** — email con A8 <80 non entrano nella cartella `emails/`.
   Rientrano solo dopo correzione e re-gate.
4. **Immutabilità dei report** — i report E2 e E-QA non si modificano post-approvazione.
   Se è necessaria una nuova verifica → si crea un nuovo file con versione (`deliverability_report_v2.json`).
5. **Lifecycle dei pattern winback** — i pattern in `winback/patterns/{icp}.json` si aggiornano
   (non si sovrascrivono): ogni entry aggiunge una data e i nuovi dati; le entry precedenti restano.

---

## PII policy (Mandato Art.7.2)

- **Nessun dato anagrafico raw** entra nel namespace. Solo pseudonimizzati o aggregati.
- Placeholder consentiti: `{nome}`, `{email}`, `{prodotto}`, `{data}`.
- I campioni lista passati a E2 per igiene sono pseudonimizzati prima dell'elaborazione.
- Il report PII di E2 logga l'esito ma non registra i dati sensibili rilevati.
- In caso di violazione: blocco immediato + escalation a MKT-Conductor + committente.

---

## Connessioni

- [[ARCHITETTURA]] · `ARCHITETTURA.md` — §4 namespace completo; §5 PII policy
- [[e2-deliverability-guard]] · `agenti/e2-deliverability-guard.md` — owner deliverability_report
- [[e-qa-email-verifier]] · `agenti/e-qa-email-verifier.md` — owner qa_report
- [[e1-lifecycle-architect]] · `agenti/e1-lifecycle-architect.md` — owner sequence_map
