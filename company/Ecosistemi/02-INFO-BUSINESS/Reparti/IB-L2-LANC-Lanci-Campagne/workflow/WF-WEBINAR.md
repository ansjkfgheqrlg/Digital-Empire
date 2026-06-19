---
Type: CONCEPT
Status: Active
Tags: #workflow #infobusiness #lanci #webinar #replay #IB-L2-LANC
Created: 2026-06-18
Last updated: 2026-06-18
---

# WF-WEBINAR — Webinar di Vendita (asset di lancio)

> **Workflow:** WF-WEBINAR · **Reparto:** IB-L2-LANC Lanci & Campagne
> **Trigger:** lancio con webinar schedulato nel calendario WF-LANCIO
> **Output:** webinar registrato + replay funnel live + metriche registrati/partecipanti
> **Gate di uscita:** script APSOC PASS + prova tecnica superata + replay con scarcity reale

---

## Trigger

WF-LANCIO ha schedulato un webinar nel calendario (`webinar: true`). IB-COORD-LANCI attiva
IB-LANC-WEBINAR a partire da circa T-14 per costruire la struttura, in parallelo al flusso copy.
Il webinar è un asset di lancio, non un evento isolato: la sua produzione si integra nei gate
del lancio (lo script passa il gate APSOC come ogni altro copy).

---

## Input JSON

```json
{
  "lancio_id": "lancio-X-202607",
  "prodotto": {"id": "corso-X", "offer_stack": ["core", "bonus_webinar"], "icp": "info-producer"},
  "data_webinar": "2026-07-15T18:00",
  "durata_min": 75,
  "template_apertura": "InfoBusiness/Webinar/script-2-storytelling.pdf",
  "replay_window_h": 72,
  "brand_kit": "DE"
}
```

---

## Pipeline + owner

```
[1] IB-LANC-WEBINAR — struttura webinar
    apertura storytelling (template Webinar/) + contenuto valore + pitch APSOC + Q&A + CTA
    durata 60-90 min, una sola offerta, scarcity REALE nel pitch
    owner: IB-LANC-WEBINAR

[2] GATE — IB-LANC-QA
    script conforme APSOC + brand voice; CTA chiara; zero promesse senza prova (Mandato Art.2)
    PASS → step 3 · FAIL → rework struttura/pitch (step 1)
    owner: IB-LANC-QA

[3] Produzione tecnica — coordinamento 03-CONTENT-FACTORY
    setup video/audio, slide, timer per blocco, copione chat
    prova tecnica pre-evento obbligatoria
    owner: IB-LANC-WEBINAR + 03-CF

[4] Esecuzione — live o registrazione
    Max prende il microfono; gli agenti preparano slide, timer, chat (link checkout pinnato)
    owner: Max (esecuzione) + IB-LANC-WEBINAR (regia)

[5] Replay funnel — IB-LANC-WEBINAR
    link protetto → opt-in → accesso replay → scarcity REALE sulla disponibilità (es. 72h reali)
    owner: IB-LANC-WEBINAR

[6] Metriche — IB-LANC-WEBINAR
    registrati, partecipanti (show-up), permanenza, conversione pitch, conversione replay
    feed a IB-LANC-TRACKER (cart open) e IB-LANC-DEBRIEF (post)
```

---

## Gate

| # | Gate | Owner | Criterio | Se FAIL |
|---|---|---|---|---|
| 1 | Script APSOC + voce | IB-LANC-QA | pitch APSOC, CTA chiara, zero promesse senza prova | rework struttura/pitch |
| 2 | Prova tecnica | IB-LANC-WEBINAR + 03-CF | audio/video/slide verificati pre-evento | non va live, fix tecnico |
| 3 | Scarcity replay reale | IB-LANC-QA | finestra replay verificabile (non finta) | riformulare la disponibilità |

---

## Output JSON

```json
{
  "lancio_id": "lancio-X-202607",
  "webinar": {
    "registrato": true,
    "registrati": 210,
    "partecipanti": 96,
    "show_up_%": 45.7,
    "permanenza_media_%": 62,
    "conversione_pitch_%": 9.4
  },
  "replay_funnel": {"live": true, "scarcity_replay": "72h reali", "accessi_replay": 88, "conversione_replay_%": 5.7},
  "gate": {"script_apsoc": "PASS", "prova_tecnica": "PASS", "scarcity_replay": "PASS"}
}
```

---

## Handoff

| Quando | Da → A | Payload |
|---|---|---|
| produzione | IB-LANC-WEBINAR → 03-CF | brief setup tecnico (video/audio/slide) |
| post-evento | IB-LANC-WEBINAR → IB-LANC-TRACKER | metriche conversione pitch (feed cart open) |
| post-lancio | IB-LANC-WEBINAR → IB-LANC-DEBRIEF | metriche webinar + replay per il debrief |

---

## Dry-run

Il replay funnel rientra nel dry-run end-to-end di IB-LANC-DRY a T-1: il percorso
opt-in → accesso replay → checkout viene simulato come parte del funnel del lancio.
La prova tecnica del webinar (step 2) è il dry-run specifico dell'esecuzione live.

---

## Esempio operativo

**Scenario:** webinar di vendita per "Vendi la Skill", 210 registrati.

- Struttura: apertura storytelling (template-2) 10', valore 35', pitch APSOC 15' con bonus a
  scadenza reale (+48h), Q&A 15'.
- GATE: primo script a 79/100 (CTA debole, due CTA concorrenti) → rework a CTA singola → 87/100 PASS.
- Prova tecnica: audio ok, slide ok → live.
- Esecuzione: 96 partecipanti (show-up 45.7%), permanenza 62%, 9 acquisti dal pitch.
- Replay: finestra 72h reali, 88 accessi, 5 acquisti dal replay.
- DEBRIEF: la fascia oraria 18:00 ha basso show-up → pattern "testare 21:00" in ReasoningBank.

---

## Connessioni

- [[IB-LANC-WEBINAR]] · `agenti/IB-LANC-WEBINAR.md`
- [[IB-LANC-QA]] · `agenti/IB-LANC-QA.md`
- [[IB-COORD-LANCI]] · `agenti/IB-COORD-LANCI.md`
- [[WF-LANCIO]] · `workflow/WF-LANCIO.md`
- [[MANDATO-EMPIRE]] · `company/Mandato/MANDATO-EMPIRE.md` (Art.2 — scarcity reale, prove non promesse)
