---
Type: ARCHITETTURA
Status: Active
Tags: #architettura #advertising #paid #marketing #L2-2
Created: 2026-06-18
Last updated: 2026-06-18
---

# ARCHITETTURA — L2.2 Advertising

> Documento di architettura interna del reparto. Descrive gerarchia, flussi, confini e namespace.
> Standard CF-grade (ADR-007). Dossier sorgente: `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md §L2.2`

---

## 1. Gerarchia interna

```
04-MARKETING (L1) — MKT-Conductor
   └── L2.2 Advertising
         │
         ADS-LEAD (coordinator, opus)
         ├── AD1 Audience Analyst (worker, sonnet)
         │     → ricerca segmenti e lookalike per piattaforma
         │     → input da 08-INTELLIGENCE
         ├── AD2 Creative Iterator (worker, sonnet)
         │     → varianti creative a scala dal winner
         │     → fan-out swarm su matrice copy × visual × audience
         ├── AD3 Media Buyer (worker, sonnet)
         │     → struttura campagna / budget / bid / pacing
         │     → dry-run di default (Art.4.3 Mandato)
         │     → coordina con Cost-Sentinel per spend approvato
         ├── AD5 Platform Specialist (worker, sonnet)
         │     → brief specifico per piattaforma
         │     → differenze formato/algoritmo/policy Meta/Google/LinkedIn/TikTok
         ├── AD6 Creative Analyst (worker, sonnet)
         │     → analisi CTR per creative e heatmap formati
         │     → pattern → feed per AD2 e ReasoningBank
         ├── AD4 Ad Compliance Checker (verifier, sonnet)
         │     → policy pre-flight per piattaforma
         │     → gate G3 — blocca se non conforme
         └── AD-QA Ads QA Verifier (verifier, sonnet)
               → verifica brand_kit / pricing / vincoli legali
               → gate pre-lancio — bloccante
```

**Principio di coordinamento:** ADS-LEAD riceve il brief dal MKT-Conductor e assegna il
workflow. AD4 e AD-QA sono gate bloccanti in serie: nessun output esce senza G3 (compliance)
e senza QA finale. AD3 non procede al lancio senza ok umano esplicito.

---

## 2. Flussi principali

### 2.1 Campagna end-to-end (WF-ADS-CAMPAIGN)

```
[MKT-Conductor]
  Brief campagna + BUDGET OK ESPLICITO Max (campo obbligatorio — Art.4.3)
         │
         ▼
ADS-LEAD — valida brief; coordina con S3 Campaign Strategist (L2.1)
         │
         ▼
S3 Campaign Strategist — obiettivo campagna, canali, struttura, KPI target
         │
         ▼
AD1 Audience Analyst — segmenti per piattaforma (input 08-INTELLIGENCE)
         │ PARALLELO (swarm fan-out)
WF-COPY-AD (L2.1) — 3+ varianti copy APSOC ≥80
BR3 Creative Director → 03-CF — visual brief per piattaforma
         │
         ▼
AD5 Platform Specialist — brief specifico formato/algoritmo/policy per piattaforma
         │
         ▼
AD2 Creative Iterator — assembla matrice copy × visual × audience
         │
         ▼
AD4 Compliance Checker — G3 policy check (per ogni piattaforma inclusa)
  → FAIL: blocco + lista specifiche da correggere → riciclo al copy/visual
  → PASS: continua
         │
         ▼
AD3 Media Buyer — struttura campagna in DRY-RUN (default assoluto)
  → budget allocation, bid strategy, pacing
  → output: campaign_plan.json con stato = "dry-run"
         │
         ▼
AD-QA — verifica brand_kit / pricing / vincoli legali
  → FAIL: blocco → riciclo specifico
  → PASS: campagna pronta al lancio
         │
         ▼
[OK UMANO ESPLICITO DI MAX] — senza questo: nessun lancio
  → approvazione registrata in state.json (campo approval_timestamp + approver)
         │
         ▼
LAUNCH → AN2/AN-OBSERVER monitorano → WF-ADS-PERFORMANCE
  → winner → AD2 itera nuove varianti (loop creativo continuo)
  → AD6 → pattern formato/performance → ReasoningBank
```

### 2.2 Testing creativo (WF-CREATIVE-TEST)

```
[Input] Brief test: obiettivo, piattaforma, budget test approvato
         │
         ▼
ADS-LEAD — definisce matrice: N varianti copy × M visual × K audience
         │
         ▼
AD2 — fan-out swarm: genera N varianti creative (ciascuna = 1 agente parallelo)
  Ogni variante: copy da L2.1 + visual brief per 03-CF + targeting da AD1
         │
         ▼
AD4 — compliance check su ogni variante
AD-QA — QA su ogni variante
         │
         ▼
AD3 — setup test su piattaforma (DRY-RUN)
  → AN3 (L2.4) verifica: dimensione campione sufficiente? Criterio predefinito?
  → senza AN3 PASS: test non parte
         │
         ▼
[OK UMANO] → lancio test
         │
         ▼
AD6 — raccoglie CTR/performance per variante
  → AN3 — verdetto statistico con criterio predefinito
  → salva in `marketing/ads/experiments`
  → winner → feed per AD2 (prossima iterazione)
```

### 2.3 Loop performance (WF-ADS-PERFORMANCE)

```
[Monitoraggio continuo: AN2 traccia per copy_id + campagna]
         │
         ▼
AD6 Creative Analyst — identifica sotto-performance creative
  → CTR in calo su creative specifica? Format che non performa?
         │
         ▼
ADS-LEAD + AD2 — diagnosi:
  - CTR basso = copy debole → riciclo a WF-COPY-AD
  - CTR ok ma CPA alto = targeting o bid → AD1/AD3
  - Formato che performa → AD5 identifica se policy/algoritmo cambiato
         │
         ▼
AD2 — itera dal winner: nuova variante con variazione minima (test incrementale)
         │
         ▼
AD4 + AD-QA — check nuova variante prima del lancio
         │
         ▼
Aggiorna `marketing/ads/experiments` + ReasoningBank
```

---

## 3. Confine con L2.1 Copywriting — il copy NON si scrive qui

| Aspetto | L2.2 Advertising | L2.1 Copywriting |
|---|---|---|
| Copy delle ads | Richiede (WF-COPY-AD) — mai scrive | Produce 3+ varianti APSOC ≥80 |
| Score APSOC | Riceve e verifica che sia ≥80 | Garantisce e certifica lo score |
| Iterazione copy | AD2 chiede nuova variante a L2.1 | L2.1 produce la variante richiesta |
| Brief creatività | AD2 descrive la direzione del test | L2.1 esegue con autonomia creativa |

**Regola d'oro:** se in questo reparto appare testo persuasivo da zero, è un errore.
Il copy arriva già gated da L2.1. Advertising assembla, testa, ottimizza — non scrive.

---

## 4. Confine con Cost-Sentinel — budget e spesa

| Aspetto | L2.2 Advertising | Cost-Sentinel (CFO) |
|---|---|---|
| Budget planning | AD3 propone budget allocation | Cost-Sentinel approva o ridimensiona |
| Soglia spend | AD3 rispetta soglie approvate | Cost-Sentinel monitora real-time |
| Superamento budget | AD3 segnala e blocca | Cost-Sentinel allerta ADS-LEAD + CMO |
| Dry-run forzato | AD3 usa dry-run per default | Cost-Sentinel verifica che dry-run sia attivo |

---

## 5. Topologia agenti per piattaforma (AD5 — Platform Specialist)

| Piattaforma | Formato primario | Lunghezza copy | Algoritmo key | Policy critica |
|---|---|---|---|---|
| Meta (FB/IG) | Feed image/video, Reels, Stories | Headline ≤27 car, testo ≤125 car (preview) | Social proof + engagement | Claims medici/finanziari proibiti; text ratio |
| Google Ads | Search (RSA), Display, YouTube | Headline ≤30 car, desc ≤90 car | Intent matching | Prezzi devono corrispondere alla landing; policy claim |
| LinkedIn | Single image, Carousel, InMail | Intro ≤150 car (visible), headline ≤70 car | B2B professional targeting | No discriminazione lavoro; claim verificabili |
| TikTok | In-Feed video, TopView | Testo video ≤80 car | Native/entertainment | No comparison claim; GDPR age |

AD5 aggiorna questa tabella quando le policy cambiano. Le campagne che usano AD5 ricevono
un brief piattaforma-specifico prima di andare in AD4 compliance.

---

## 6. Namespace memoria — `marketing/ads/...`

| Namespace | Contenuto | Owner scrittura |
|---|---|---|
| `marketing/ads/experiments` | Matrici test, varianti, verdetti, winner | AN3 / AD6 scrivono |
| `marketing/ads/campaigns` | Setup campagne: struttura, budget, pacing, stato | AD3 scrive |
| `marketing/ads/patterns` | Pattern creativi vincenti per ICP/piattaforma | AD6 scrive → AN4 consolida in ReasoningBank |

**Regola di integrità:** ogni record in `marketing/ads/experiments` deve avere campo
`verdetto` con uno tra `winner_id`, `inconclusivo` o `in_corso`. Senza verdetto non è
un esperimento chiuso. Un test senza dimensione campione validata da AN3 non parte.

---

## 7. State e ripartibilità

Ogni esecuzione di WF-ADS-CAMPAIGN produce un `state.json` in `marketing/ads/campaigns/`
con campi:
- `campaign_id` — identificativo univoco
- `committente` — ecosistema richiedente
- `piattaforme` — array delle piattaforme incluse
- `budget_approvato` — importo approvato da Cost-Sentinel + Max
- `approval_timestamp` — campo popolato a runtime (da Max prima del lancio reale)
- `approver` — campo popolato a runtime
- `dry_run` — boolean, default `true`, diventa `false` solo con approvazione registrata
- `g3_compliance` — pending / PASS / FAIL per ogni piattaforma
- `ad_qa_gate` — pending / PASS / FAIL
- `last_updated` — timestamp ultimo aggiornamento

Questo garantisce la ripartibilità a freddo: se l'agente muore durante il setup, si riprende
dall'ultimo campo popolato senza ripartire da zero (test amnesia §6 V2).

---

## Connessioni

- [[README]] · `README.md` — missione, roster, KPI del reparto
- [[04-ECOSISTEMA-MARKETING-V2]] · `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md §L2.2 + §4c`
- [[L2-1-Copywriting]] · fornitore copy ads (WF-COPY-AD) — mai scritto in L2.2
- [[L2-4-Analytics]] · AN2/AN3/AD6 partner analitici per test e performance
- [[L2-5-Brand-Creative-Strategy]] · BR3 fornitore creative brief
- [[WF-ADS-CAMPAIGN]] · `workflow/WF-ADS-CAMPAIGN.md`
- [[WF-CREATIVE-TEST]] · `workflow/WF-CREATIVE-TEST.md`
- [[WF-ADS-PERFORMANCE]] · `workflow/WF-ADS-PERFORMANCE.md`
