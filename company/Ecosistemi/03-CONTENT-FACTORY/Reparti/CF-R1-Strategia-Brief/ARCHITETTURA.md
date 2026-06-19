---
Type: ARCHITETTURA
Status: Active
Tags: #architettura #content-factory #CF-R1 #pre-produzione #workflow
Created: 2026-06-19
Last updated: 2026-06-19
---

# ARCHITETTURA — CF-R1 Strategia & Brief

> **Ecosistema:** 03-CONTENT-FACTORY · **Area:** Pre-Produzione · **Reparto:** CF-R1

---

## Posizione nella gerarchia CF-DE

```
CF-DIRECTOR (CF-D-LEAD)
│
└── L1-PRE — CAPO AREA PRE-PRODUZIONE
    │
    ├── CF-R1 — STRATEGIA & BRIEF  ← questo reparto
    │         CF-R1-COORD riporta a L1-PRE
    │
    └── CF-R2 — BRAND-KIT & TENANT REGISTRY
              (fornitore brand_kit per CF-R1)
```

CF-R1-COORD è il punto di contatto verso L1-PRE per ogni escalation, aggiornamento
di stato e report di reparto. Non riporta mai direttamente al CF-Director: passa sempre
per L1-PRE (separazione di livello, pattern gerarchia MEGA-REPARTO ADR-007).

---

## Flussi dei 3 workflow

### WF-BRIEF — flusso principale

```
[IN] Ordine validato da CF-D-DISPATCH
  → orders/<id>/order.json
        │
        ▼
CF-R1-COORD
  Verifica: brand_kit + icp presenti nel contratto
  Se mancanti → BLOCCO + escalation CF-D-DISPATCH
        │
        ▼
CF-R1-ANALYST
  Carica: brand_kit/<slug>.json + brands/<slug>/icp.json
  Identifica: vincoli per formato (parole_vietate, canali, CTA richiesta, tier_max engine)
  Output: context.json → arricchisce l'ordine
        │
        ▼
CF-R1-ANGLE
  Input: context.json + libreria formule (cf/patterns) + trend INTELLIGENCE
  Output: 3 angle alternativi (angle_A, angle_B, angle_C) con rationale
        │
        ▼
CF-R1-HOOK
  Input: icp + tipo formato + 3 angle
  Output: hook_type selezionato da libreria formule (es. "domanda-provocatoria",
          "dato-sorprendente", "contro-intuizione") + hook draft per il brief
        │
        ▼
CF-R1-QA  ← GATE BLOCCANTE
  Verifica presenza obbligatoria:
  [ ] angle (uno dei 3, confermato o scelto dal committente se ordine lo richiede)
  [ ] hook_type (dalla libreria, non inventato)
  [ ] struttura_formato (slide-deck / script / outline / prompt-set)
  [ ] canali (array non vuoto)
  [ ] vincoli_brand (dall'analyst, anche se array vuoto — deve essere esplicito)
  [ ] word_count o durata_stimata (per formato)
  PASS → brief.json scritto in orders/<id>/01-brief/
  FAIL → lista campi mancanti → CF-R1-COORD → rework
        │
        ▼
[OUT] orders/<id>/01-brief/brief.json
      orders/<id>/state.json aggiornato: fase "01-brief" completata con timestamp + owner
```

**Dry-run:** produce `brief-draft.json` in `orders/<id>/01-brief/` senza scrivere
`state.json` fase completata e senza assegnare slot di produzione. Zero impatto coda.

### WF-CALENDAR — flusso pianificazione

```
[IN] Richiesta piano editoriale: brand_kit_slugs[] + periodo (settimana/mese) + mix_formati
        │
        ▼
CF-R1-CAL
  Carica: brand_kit per ogni slug → identifica canali attivi + cadenza richiesta
  Calcola: slot settimanali per brand (es. 3 caroselli + 1 video per Mentalità Brutale)
        │
        ▼
CF-R1-TREND
  Aggiunge: finestre trend al piano (slot "trend-priority" segnalati da 08-INTELLIGENCE)
        │
        ▼
CF-R1-CAL
  Integra: finestre trend + slot fissi + slot variabili
  Verifica: nessun slot senza brand_kit validato (via CF-R2)
  Output: piano settimanale in cf/calendars/<brand>/settimana-YYYY-WW.json
        │
        ▼
[OUT] cf/calendars/<brand>/settimana-YYYY-WW.json
      Piano inoltrato anche a 04-MARKETING L2.2 per coordinamento calendario ads/organico
```

**Gate:** piano consegnato entro venerdì per la settimana successiva.
Nessun slot senza brand_kit validato da CF-R2.

### WF-TREND-BRIEF — flusso accelerato

```
[IN] Brief trend da 08-INTELLIGENCE: {topic, brand_slug, urgenza, data_trend}
        │
        ▼
CF-R1-TREND
  Verifica: data_trend → se >48h dalla ricezione → SCARTA con motivo strutturato
  Se valido → aggiunge il trend alla libreria cf/patterns per brand/nicchia
        │
        ▼
CF-R1-ANGLE
  Produce: 1 angle virale urgente (non 3 — modalità accelerata)
  Il secondo angle è prodotto solo se la latenza lo permette
        │
        ▼
CF-R1-QA ← GATE ACCELERATO (≤30 min dall'avvio)
  Stessi criteri di WF-BRIEF ma con deadline interna stringente
  FAIL → motivo strutturato → CF-R1-COORD decide: scarta o rielabora
        │
        ▼
[OUT] brief.json con priorità "trend" → coda produzione CF-Director (priorità alta)
      Latenza totale intake→brief ≤1h
```

---

## Handoff verso le aree di produzione

CF-R1 produce `brief.json` e lo deposita in `orders/<id>/01-brief/`. Le aree di
produzione (R3, R4, R5) lo leggono da lì — nessun passaggio diretto agente-agente:
il bus di handoff è il filesystem degli ordini.

| Area di produzione | Cosa legge dal brief |
|---|---|
| R3 — Produzione Video | `struttura_formato: script`, `durata_stimata`, `hook_type`, `angle`, `vincoli_brand.soul_id` |
| R4 — Produzione Testuale | `struttura_formato: outline`, `word_count`, `hook_type`, `angle`, `vincoli_brand.parole_vietate` |
| R5 — Visual & Design | `struttura_formato: slide-deck`, `hook_type`, `angle`, `vincoli_brand.palette`, `icp.dolori` |

---

## Input trend da 08-INTELLIGENCE

Il flusso `intel→cf` è unidirezionale: 08-INTELLIGENCE produce il brief trend
(topic, data, brand_slug, urgenza) e lo deposita nel namespace `cf/briefs/trend/`.
CF-R1-TREND lo legge e avvia WF-TREND-BRIEF. Il flusso inverso (cf→wiki) è gestito
da CF-R1-COORD che logga in `wiki/log.md` ogni brief trend processato.

---

## Connessioni

- [[03-ECOSISTEMA-CONTENT-FACTORY-V2]] · `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY-V2.md §CF-R1`
- [[CF-R2-Brand-Kit-Tenant-Registry]] · fornitore brand_kit validati via WF-BRAND-ONBOARDING
- [[08-INTELLIGENCE]] · flusso `intel→cf` per trend
- [[WF-BRIEF]] · `workflow/WF-BRIEF.md`
