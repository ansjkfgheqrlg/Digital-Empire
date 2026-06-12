> Fonte: PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY.md sez. 4e (WF-PUBLISH)

# WF-PUBLISH — Workflow Pubblicazione Schedulata Multi-Canale

> Livello: L3 · Reparto: CF-R5 PUBBLICAZIONE & DISTRIBUZIONE · Coordinatore: `CF-R5-A01-publish-lead`
> Fonte: dossier 03 §4e, §6.
> Ecosistema: `company/Ecosistemi/03-CONTENT-FACTORY/ECOSISTEMA.md`

---

## Identità

| Campo | Valore |
|---|---|
| ID workflow | WF-PUBLISH |
| Ecosistema | 03-CONTENT-FACTORY |
| Reparto L2 | CF-R5 PUBBLICAZIONE & DISTRIBUZIONE |
| Motore | orchestratori Python esistenti: `main_orchestrator.py`, `mentalita_orchestrator.py` |
| Stato | SCAFFOLD (token IG/FB scaduti — CF-F4 include rinnovo come step 0) |
| Canali supportati | IG · TikTok · LinkedIn · Drive cliente |
| Sub-workflow | WF-DELIVERY · WF-FEEDBACK |

---

## Cosa fa

Prende deliverable con 3 gate verdi e li porta live sui canali dichiarati nell'ordine.
Review umana obbligatoria prima di ogni pubblicazione (vincolo Piano Maestro — il Board
può rimuoverlo quando il sistema è provato).

---

## Pre-condizioni (non derogabili)

1. `state.json` dell'ordine: tutti e 3 i gate VERDI (GATE-FORMATO + GATE-BRAND + GATE-COPY).
2. Caption presente per ogni canale richiesto (adattata da CF-R5-A02).
3. Token di pubblicazione per il canale: `token-health check` come step 0.
4. Slot calendario disponibile (WF-CALENDAR di CF-R1).

---

## Pipeline end-to-end

```
coda (deliverable gate-verdi) → CF-R1/WF-CALENDAR → slot per ogni canale

  STEP 0 — Token health:
    CF-R5-A03 verifica token IG/FB/TikTok/LinkedIn per il brand
    → scaduto: BLOCCO + alert Conductor + task rinnovo (CF-F4 step 0)
    → valido: procede

  STEP 1 — DRY-RUN (obbligatorio alla prima esecuzione per brand/canale):
    Piano pubblicazione: {asset, canale, slot_orario, caption, hashtag, UTM}
    → output: publish_plan.json in state.json.publish_plan
    → attende review umana esplicita

  STEP 2 — Adattamento per canale (CF-R5-A02):
    IG: caption ≤2200 chr, hashtag 5-10 relevanti, aspect 1:1 o 4:5
    TikTok: caption ≤150 chr, hashtag trend, aspect 9:16
    LinkedIn: caption professionale ≤3000 chr, hashtag 3-5, aspect 1:1 o 4:5
    T-utm: UTM appeso a ogni link ({utm_source=canale, utm_medium=organic, utm_campaign=orderId})

  STEP 3 — Pubblicazione (dopo ok umano):
    CF-R5-A03 → orchestratori Python (wrap ADR-003):
      IG/TikTok: mentalita_orchestrator.py (o main_orchestrator.py per altri brand)
      LinkedIn: modulo LinkedIn in workflow pubblicazione automatica
      Drive: upload + share link a committente non-social

  STEP 4 — Post-check (T-postcheck, +5 minuti):
    Screenshot/verifica live → URL post loggato in state.json.publish[].url
    → fallimento verifica: alert umano + retry manual

  STEP 5 — Log:
    trace.jsonl entry: {ts, agent: CF-R5-A03, event: published, canale, url}
    wiki/log.md entry obbligatoria (pattern wiki-first #12)

  STEP 6 — WF-FEEDBACK (schedulato a +48h e +7gg):
    CF-R5-A05 raccoglie metriche → 04-MARKETING/AN2 + memory_store("cf/patterns", ...)
```

---

## WF-DELIVERY (alternativo a WF-PUBLISH per committenti non-social)

```
handoff da CF-R4 o CF-R3 con gate verdi
  → CF-R5-A04 crea pacchetto:
      manifest.json (lista asset, gate-status, note)
      + asset ordinati in cartelle per formato
      + README operativo per il committente
  → upload su Drive condiviso con committente
  → notifica via BUS al committente: "ordine CF-2026-XXXX pronto"
```

---

## Failure handling

| Evento | Azione |
|---|---|
| token scaduto | → BLOCCO (mai tentativo con token scaduto), alert Conductor, task rinnovo |
| rate limit piattaforma | → posticipa slot di 2h nel calendario; log in trace.jsonl; MAI silenzioso |
| ban/shadow-ban rilevato a post-check | → alert umano immediato, pausa tutta la campagna per quel brand, entry cf/failures |
| asset non conforme alla piattaforma (dimensione/formato) | → CF-R5-A02 ritorna a CF-R4/T-resize per riprocessare |

---

## Connessioni

- `company/Ecosistemi/03-CONTENT-FACTORY/ECOSISTEMA.md` — organigramma completo
- `company/Ecosistemi/03-CONTENT-FACTORY/BACKBONE.md` — namespace memoria, topologia
- `company/Ecosistemi/03-CONTENT-FACTORY/Reparti/Pubblicazione/README.md`
- `SKILL & Agenti/Workflow pubblicazione automatica/` — motore Python (NON riscrivere, ADR-003)
- `company/Ecosistemi/04-MARKETING/Reparti/Analytics/` — destinatario metriche WF-FEEDBACK
- `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY.md` §4e, §6

*Fonte: dossier 03 §4e, §6 · Aggiornato: 2026-06-11*
