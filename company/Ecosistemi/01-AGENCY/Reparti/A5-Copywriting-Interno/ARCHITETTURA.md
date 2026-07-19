---
Type: ARCHITETTURA
Status: Active
Tags: #architettura #agency #copywriting #apsoc #copy #A5
Created: 2026-06-23
Last updated: 2026-06-23
---

# ARCHITETTURA — A5 Copywriting Interno

> Documento di architettura interna del reparto. Descrive gerarchia, flussi, confini,
> namespace e il riuso del Gate Bibbia (pattern 6, ADR-003 wrap-not-rewrite).

---

## 1. Gerarchia interna

```
01-AGENCY (L1) — AG-DIR
   └── A5 Copywriting Interno
         │
         AG-A5-COORD (coordinatore, sonnet)
         ├── AG-A5-WRITE — APSOC Writer (worker, sonnet)
         │     → scrittura/variazione copy (skill cro-copy-architect, market-copy)
         ├── AG-A5-OBJ — Objection Librarian (worker, sonnet)
         │     → libreria obiezioni reali (da HC-AG-IN-01) → risposte testate con prove
         ├── AG-A5-SCRIPT — Script Writer Call (worker, sonnet)
         │     → script discovery + chiusura per A8-Closing
         ├── AG-A5-LEARN — Copy Performance Analyst (worker, sonnet)
         │     → analizza reply rate per template → suggerisce varianti → alimenta agency/outreach
         └── AG-A5-QA — Verificatore Gate Bibbia (verifier, sonnet)
               → Gate Bibbia RIUSATO da A2 (pattern 6) — BLOCCA, non suggerisce
               → wrappa lo stesso gate di ../A2-Acquisizione/agenti/ag-a2-qa.md
```

**Principio di coordinamento:** AG-A5-COORD riceve il brief (refresh template o richiesta
script call), orchestra il `mesh` piccolo writer ↔ objection ↔ qa, e riporta ad AG-DIR.
AG-A5-QA è bloccante su ogni output: nessun copy esce senza Gate Bibbia verde. Il gate
NON è riscritto qui — è lo stesso gate di A2, riusato via cross-link (pattern 6: una skill,
molti reparti; ADR-003 wrap-not-rewrite).

---

## 2. Flussi principali

### 2.1 WF-COPY-REFRESH (refresh template data-driven)

```
[TRIGGER: reply rate A2 sotto baseline 2 cicli, oppure cadenza periodica]
         │
         ▼
AG-A5-LEARN — analizza reply rate ultimi 30gg per template/canale (legge agency/outreach)
  → identifica template in calo · ipotesi sul perché (sezione APSOC debole)
         │
         ▼
AG-A5-WRITE — produce 3 varianti per canale, ancorate al problema reale del target
  → skill cro-copy-architect (framework APSOC) + market-copy
         │
         ▼
AG-A5-OBJ — verifica che le varianti usino solo risposte a obiezioni con prove reali
         │
         ▼
AG-A5-QA — Gate Bibbia (3 check sequenziali, riusati da A2) su ogni variante
  → FAIL: torna ad AG-A5-WRITE con note specifiche (ciclo mesh)
  → PASS: variante autorizzata al test
         │
         ▼
Rollout graduale su batch 10% leads → confronto A/B → adozione winner o scarto
```

### 2.2 WF-SCRIPT-CALL (script per A8-Closing)

```
[TRIGGER: A8-Closing richiede script discovery o script chiusura per nicchia X]
         │
         ▼
AG-A5-OBJ — estrae obiezioni attese per la nicchia dalla libreria (solo prove reali)
         │
         ▼
AG-A5-SCRIPT — struttura lo script con framework APSOC (apertura → problema → soluzione →
  gestione obiezioni con risposte testate → CTA chiusura)
         │
         ▼
AG-A5-QA — Gate Bibbia: no claim senza proof, no dependency-language, brand voice conforme
  → FAIL: torna ad AG-A5-SCRIPT
  → PASS: consegna ad A8-Closing
```

---

## 3. Confine con 04-MARKETING e A2 — chi possiede cosa

| Aspetto | A5 Copywriting Interno (AGENCY) | Dove vive l'alternativa |
|---|---|---|
| Copy operativo quotidiano (template email/DM, micro-copy preventivi, script call) | Possiede e produce | — |
| Sales page, sequenze lunghe, refresh strutturali grandi | Richiede a 04-MARKETING via HC-AG-MK-01 | 04-MARKETING/L2-1-Copywriting |
| Il Gate Bibbia (motore di qualità) | RIUSA — non possiede | A2-Acquisizione (motore `bibbia_team.py`) |
| Dati reply reali e obiezioni grezze | Consuma — non raccoglie | A2-Acquisizione + 08-INTELLIGENCE (HC-AG-IN-01) |
| Esecuzione invio / cap canali | Non tocca | A2-Acquisizione (AG-A2-SEND) |

**Regola d'oro:** A5 è il consumatore-adattatore locale. I pezzi grandi si chiedono a
04-MARKETING; il gate si riusa da A2; A5 produce solo il copy operativo quotidiano e lo
fa passare dallo stesso gate di A2 prima di rilasciarlo.

---

## 4. Namespace memoria — `agency/a5/...`

| Namespace | Contenuto | Owner scrittura |
|---|---|---|
| `agency/a5/templates` | Template attivi per canale + versione + stato gate | AG-A5-WRITE |
| `agency/a5/performance` | Reply rate per variante, esito A/B, decisione adozione/scarto | AG-A5-LEARN |
| `agency/a5/obiezioni` | Libreria obiezioni reali (anonimizzate) → risposte testate con prove | AG-A5-OBJ |
| `agency/a5/script` | Script discovery + chiusura per nicchia, stato gate, consegna A8 | AG-A5-SCRIPT |

**Regola di integrità:** ogni risposta in `agency/a5/obiezioni` deve avere campo `prova`
popolato (rif. conversazione reale o esito misurato). Risposta senza prova = `non_validata`,
non rilasciabile (Mandato Art.2: prove non promesse).

---

## 5. Integrazione con altri namespace e workflow

| Namespace / Sistema | Relazione |
|---|---|
| `agency/outreach` | AG-A5-LEARN legge performance per variante; AG-A5-WRITE scrive template aggiornati |
| `agency/a2/reply/` | AG-A5-OBJ legge obiezioni grezze (anonimizzate) come input libreria |
| A2 / `ag-a2-qa` | AG-A5-QA riusa lo stesso Gate Bibbia (pattern 6) — invoca, non duplica |
| HC-AG-IN-01 (08-INTELLIGENCE) | fornisce obiezioni raccolte da A2 → libreria testata |
| HC-AG-MK-01 (04-MARKETING) | pezzi grandi (sales page, sequenze lunghe) delegati fuori da A5 |
| A8-Closing | riceve gli script call gated prodotti da WF-SCRIPT-CALL |

---

## 6. State e ripartibilità

Ogni esecuzione di WF-COPY-REFRESH produce uno `state.json` in `agency/a5/templates/`
con i campi:
- `refresh_id` — identificativo del ciclo di refresh
- `canale` — email / linkedin / instagram
- `varianti_status` — per variante: prodotta / gated / in_test / adottata / scartata
- `gate_bibbia` — pass/fail per variante (riusa lo schema del gate A2)
- `ab_status` — non_avviato / in_corso / verdetto
- `last_updated` — timestamp

Questo permette la **ripartibilità a freddo**: un agente rientra nel refresh dal punto
esatto di interruzione senza riestrarre tutto il contesto (test amnesia §6).

---

## Connessioni

- [[README]] · `README.md` — missione, roster, KPI del reparto
- [[ag-a2-qa]] · `../A2-Acquisizione/agenti/ag-a2-qa.md` — Gate Bibbia riusato (pattern 6)
- [[01-ECOSISTEMA-AGENCY-V2]] · `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md §A5`
- [[WF-COPY-REFRESH]] · `workflow/WF-COPY-REFRESH.md`
- [[WF-SCRIPT-CALL]] · `workflow/WF-SCRIPT-CALL.md`
