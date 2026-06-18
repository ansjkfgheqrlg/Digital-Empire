---
Type: WORKFLOW
Status: Active
Tags: #workflow #landing #audit #apsoc #cro #diagnosi #L2.6
Created: 2026-06-18
Last updated: 2026-06-18
---

# WF-LANDING-AUDIT — Audit Landing Esistente

> **ID:** WF-CA-003 · **Owner:** `conv-lead` + `ca-qa-conversion-verifier`
> **Reparto:** L2.6 Conversion Architecture
> **Trigger:** richiesta di audit su landing page esistente (da committente o da CONV-LEAD)

---

## Scopo

Auditare una landing page esistente su 4 dimensioni: struttura APSOC, micro-conversioni,
performance tecnica, mobile. Produrre un report diagnostico strutturato con 3 azioni
prioritarie ordinate per impatto stimato. Il report è il punto di partenza per decidere
se avviare un WF-CRO-SPRINT o se la landing richiede un redesign strutturale.

---

## Attori

| Step | Agente L2.6 | Agente/Reparto esterno |
|---|---|---|
| Ricezione + struttura | `conv-lead` | — |
| Audit APSOC | `ca-qa-conversion-verifier` + `ca2-landing-page-strategist` | — |
| Audit micro-conversioni | `ca3-micro-conversion-analyst` | AN5 (L2.4) — dati se disponibili |
| Performance/mobile | `ca2-landing-page-strategist` | 06-PLATFORM (dati tecnici) |
| Sintesi e priorità | `ca-qa-conversion-verifier` + `conv-lead` | — |
| Salvataggio | `conv-lead` | — |

---

## Flusso passo-passo

```
[TRIGGER]
Richiesta audit: {URL landing, committente, obiettivo originale, dati disponibili}
         │
         ▼
[STEP 1] CONV-LEAD — raccolta dati disponibili
  → legge: struttura attuale della landing (sezioni, headline, CTA, form)
  → raccoglie: dati AN5 se disponibili (drop rate per sezione, tempo medio, scroll depth)
  → identifica: awareness level target e ICP della landing
  → GATE-1: informazioni minime disponibili (URL + obiettivo + ICP) → prosegui

         │
         ▼
[STEP 2] CA-QA + CA2 — audit struttura APSOC (in parallelo con step 3)
  → Dimensione 1 — Struttura APSOC:
    · Le 5 sezioni APSOC sono presenti? (A/P/S/O/CTA)
    · Sono nell'ordine corretto? P prima di S?
    · Ogni sezione svolge il suo ruolo? (es. sezione "proof" è reale o generica?)
    · Above-the-fold: headline chiara? CTA visibile senza scroll su mobile?
    · Message-match: il canale di traffico dichiarato è coerente con l'headline?
  → Risultato: check binario per ogni elemento + note diagnostiche

[STEP 3] CA3 + AN5 (se dati disponibili) — audit micro-conversioni (in parallelo)
  → Dimensione 2 — Micro-conversioni:
    · Scroll depth medio (dove abbandona la maggior parte dei visitatori?)
    · Posizione CTA: sopra o sotto il punto di abbandono medio?
    · Attrito form: quanti campi? Obbligatori necessari?
    · Heatmap click (se disponibili)
  → Se dati AN5 assenti: CA3 stima da struttura della pagina il percorso comportamentale atteso
    e identifica i punti di attrito probabile (diagnosi pre-dati)
  → Risultato: mappa percorso con punti di attrito identificati

         │
         ▼
[STEP 4] CA2 + 06-PLATFORM (se dati tecnici disponibili) — audit performance/mobile
  → Dimensione 3 — Performance tecnica:
    · LCP (Largest Contentful Paint): ≤2.5s su mobile 4G? Se >4s: impatto diretto su bounce.
    · CLS (Cumulative Layout Shift): stabilità visiva durante il caricamento?
    · TTFB (Time to First Byte): risposta server?
  → Dimensione 4 — Mobile:
    · CTA visibile above-the-fold su 375px?
    · Form usabile su mobile (input field size, tap target)?
    · Font leggibile senza zoom?
  → Se dati tecnici non disponibili: CA2 specifica quali strumenti usare per misurarli
    (PageSpeed Insights, Lighthouse) e segnala come "da misurare"

         │
         ▼
[STEP 5] CA-QA — sintesi diagnosi e prioritizzazione
  → Consolida i 4 check in un quadro unico:
    · Issue critiche (bloccano la conversione: CTA non visibile, P assente, velocità >5s)
    · Issue importanti (riducono la conversione: proof generica, message-match debole)
    · Issue minori (margini di miglioramento: form fields, font size)
  → Seleziona 3 azioni prioritarie:
    - Ordinamento per impatto stimato (non inventato: basato su APSOC gap e dati disponibili)
    - Ogni azione ha: elemento da modificare + ipotesi di impatto + tipo di intervento
      (copy da L2.1 / struttura da 06-PLATFORM / sprint CRO via WF-CRO-SPRINT)
  → Raccomandazione: "sprint CRO sufficiente" o "redesign strutturale necessario"

         │
         ▼
[STEP 6] CONV-LEAD — report finale + handoff
  → produce report completo: 4 dimensioni audit + diagnosi + 3 azioni prioritarie
  → salva in marketing/cro/audits/{audit_id}
  → consegna al committente
  → se raccomandazione = sprint CRO → avvia WF-CRO-SPRINT con le azioni come input
  → se raccomandazione = redesign → produce nuovo brief per WF-FUNNEL-DESIGN / CA2
```

---

## Gate bloccanti

| Gate | Condizione PASS | Owner | Blocca |
|---|---|---|---|
| G1 — Dati minimi | URL + obiettivo + ICP disponibili | CONV-LEAD | Avvio audit |
| G2 — 3 azioni prioritarie | Ogni azione ha elemento + impatto + tipo intervento | CA-QA | Consegna report |
| G3 — Raccomandazione esplicita | Sprint CRO O redesign dichiarato con motivazione | CA-QA | Chiusura workflow |

---

## Input / Output del workflow

**Input trigger:**
```json
{
  "audit_trigger": "richiesta committente | proattivo post-funnel-live",
  "url_landing": "https://esempio.com/landing-corso",
  "committente": "02-INFO",
  "obiettivo_originale": "acquisto corso €297",
  "icp": "freelance-digitale-ita",
  "dati_disponibili": {
    "AN5_drop_report": true,
    "heatmap": false,
    "pagespeed_score": "[DM]"
  }
}
```

**Output finale:**
```json
{
  "audit_id": "AUDIT-001",
  "url_landing": "https://esempio.com/landing-corso",
  "sommario_diagnosi": {
    "APSOC_struttura": "P assente come sezione dedicata; integrata nell'hero ma non amplificata",
    "micro_conversioni": "scroll depth medio stimato 45%: drop prima della sezione proof",
    "performance": "LCP [DM] — da misurare con PageSpeed Insights",
    "mobile": "CTA non visibile above-the-fold su 375px"
  },
  "azioni_prioritarie": [
    {
      "priorita": 1,
      "elemento": "CTA above-the-fold su mobile",
      "tipo_intervento": "strutturale — 06-PLATFORM",
      "impatto_stimato": "riduzione bounce immediata (CTA non visibile su mobile = utenti che abbandonano senza interagire)",
      "sprint_necessario": false
    },
    {
      "priorita": 2,
      "elemento": "Sezione P (Problema) dedicata",
      "tipo_intervento": "copy + struttura — L2.1 + 06-PLATFORM",
      "impatto_stimato": "miglioramento scroll depth (il visitatore trova la sezione che amplifica il suo problema prima della soluzione)",
      "sprint_necessario": true
    },
    {
      "priorita": 3,
      "elemento": "Proof specifica con risultati misurabili",
      "tipo_intervento": "copy — L2.1 (testimonial + dati reali richiesti al committente)",
      "impatto_stimato": "riduzione drop nella sezione proof/soluzione",
      "sprint_necessario": true
    }
  ],
  "raccomandazione": "sprint CRO sufficiente per azioni 1+2; azione 3 richiede dati proof dal committente",
  "namespace": "marketing/cro/audits/AUDIT-001"
}
```

---

## State

File: `marketing/cro/audits/{audit_id}.json`
- Creato al completamento dell'audit.
- Include le 3 azioni prioritarie e la raccomandazione.
- Se genera WF-CRO-SPRINT: il riferimento allo sprint è linkato nell'audit.

---

## Connessioni

- [[ca-qa-conversion-verifier]] · `agenti/ca-qa-conversion-verifier.md` — conduce l'audit APSOC
- [[ca2-landing-page-strategist]] · `agenti/ca2-landing-page-strategist.md` — audit struttura/performance
- [[ca3-micro-conversion-analyst]] · `agenti/ca3-micro-conversion-analyst.md` — audit micro-conversioni
- [[WF-CRO-SPRINT]] · `workflow/WF-CRO-SPRINT.md` — workflow successivo se raccomandazione = sprint
- [[WF-FUNNEL-DESIGN]] · `workflow/WF-FUNNEL-DESIGN.md` — workflow successivo se raccomandazione = redesign
- [[L2-4-Analytics]] · AN5 fornisce i dati di drop rate come input
