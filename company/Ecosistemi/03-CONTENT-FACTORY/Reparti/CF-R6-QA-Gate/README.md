---
Type: REPARTO
Status: Active
Tags: #reparto #content-factory #qa #gate #CF-R6 #post-produzione #indipendenza
Created: 2026-06-23
Last updated: 2026-06-23
---

# CF-R6 — QA & Gate

> **Ecosistema:** 03-CONTENT-FACTORY · **Area:** Post-Produzione · **Livello:** L2 Reparto
> **Dossier:** `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY-V2.md §CF-R6`
> **Standard:** CF-grade (ADR-007) · **INVARIANT CARDINALE:** indipendente da tutti i reparti di produzione

---

## Missione

Garantire che nessun asset esca da CF-DE senza aver superato i 3 gate sequenziali: FORMATO,
BRAND, COPY — più il Mandato compliance trasversale. CF-R6 è il gatekeeping indipendente
dell'intera Content Factory: chi produce non si auto-valuta. Il capo area Post-Produzione
(L1-POST) garantisce questa separazione; è bypassabile solo da una decisione esplicita del Board.

CF-R6-COORD riporta esclusivamente a L1-POST — MAI a L1-PROD. Nessun agente di
produzione (CF-R3, CF-R4, CF-R5) può influenzare né bypassare i gate.

---

## Cosa fa il reparto

1. **Esegue il GATE-FORMATO** (automatizzabile 100%) su ogni deliverable: dimensioni, peso,
   codec, loudness, struttura — criteri oggettivi, nessuna discrezionalità.
2. **Esegue il GATE-BRAND** parametrico sul brand_kit dell'ordine: palette HEX, font,
   logo, tone of voice campionato vs esempi si/no del brand_kit.voice.
3. **Esegue il GATE-COPY APSOC**: hook presente, problema+promessa coerenti con icp,
   social proof esclusivamente reale e verificabile, CTA unica e misurabile.
4. **Esegue il Mandato compliance** (invariant non-parametrici): "prove non promesse",
   zero claim non verificabili, zero genericità — trasversale su ogni formato.
5. **Gestisce il ciclo rework**: motivo strutturato → rinvio al reparto corretto; traccia
   il contatore rework per pezzo; 2 rework falliti → escalation + entry `cf/failures`.
6. **Coordina QA batch** (≥5 pezzi): parallelismo controllato, report aggregato,
   first-pass rate per batch.
7. **Alimenta il ReasoningBank**: pattern di gate falliti → `cf/failures`; report mensile
   a CF-Director e 07-FORGE per chiudere il loop di miglioramento strutturale.

## Cosa NON fa

- Non suggerisce miglioramenti creativi: il verdetto è PASS o FAIL con motivo, mai "potrebbe
  andare meglio".
- Non riscrive, non corregge, non produce asset: rinvia sempre al reparto produttore con specifica.
- Non riceve ordini da L1-PROD né da reparti di produzione: il flusso è unidirezionale
  (produzione → CF-R6), mai bidirezionale come gerarchia.
- Non bypassa gate: i 3 gate sono sequenziali e non comprimibili; un ROSSO ferma il pezzo.
- Non emette giudizi qualitativi soggettivi: valuta conformità a criteri espliciti e misurabili.

---

## Roster del reparto (8 agenti)

| ID | Agente | File | Tipo | Tier | Ruolo |
|---|---|---|---|---|---|
| `CF-R6-COORD` | QA Lead | `agenti/cf-r6-coord.md` | coordinator | opus | Assegna revisore; riporta a L1-POST; escalation finale |
| `CF-R6-FORMAT` | Gate Formato Verificatore | `agenti/cf-r6-format.md` | verifier | haiku | GATE-FORMATO: dimensioni/peso/codec/loudness/struttura |
| `CF-R6-BRAND` | Gate Brand Verificatore | `agenti/cf-r6-brand.md` | verifier | sonnet | GATE-BRAND: palette/font/logo/tone vs brand_kit |
| `CF-R6-COPY` | Gate Copy Verificatore | `agenti/cf-r6-copy.md` | verifier | sonnet | GATE-COPY APSOC: hook/promessa/social proof/CTA |
| `CF-R6-MANDATO` | Mandato Compliance Verificatore | `agenti/cf-r6-mandato.md` | verifier | sonnet | Invariant Mandato Empire: no claim, no genericità |
| `CF-R6-REWORK` | Rework Coordinator | `agenti/cf-r6-rework.md` | coordinator | haiku | Gestisce ciclo rework; traccia contatore; rinvia |
| `CF-R6-BATCH` | Batch QA Coordinator | `agenti/cf-r6-batch.md` | coordinator | sonnet | QA parallelo batch ≥5; report aggregato; first-pass rate |
| `CF-R6-LEARN` | QA Pattern Analyst | `agenti/cf-r6-learn.md` | analyst | sonnet | Pattern gate falliti → `cf/failures`; report mensile |

---

## Workflow del reparto (3 workflow CF-grade)

| ID | File | Scopo | Gate |
|---|---|---|---|
| **WF-QA-SINGOLO** | `workflow/WF-QA-SINGOLO.md` | Review completa singolo deliverable: 3 gate sequenziali + Mandato | FORMAT→BRAND→COPY→MANDATO; 1 rosso ferma; 2 rework → escalation |
| **WF-QA-BATCH** | `workflow/WF-QA-BATCH.md` | QA parallelo batch ≥5; report aggregato | WF-QA-SINGOLO su ogni pezzo; nessuna abbreviazione per batch |
| **WF-QUALITY-AUDIT** | `workflow/WF-QUALITY-AUDIT.md` | Audit mensile pattern falliti → CF-Director + 07-FORGE | ≥3 casi per pattern; cadenza mensile obbligatoria |

---

## Namespace memoria

| Namespace | Contenuto |
|---|---|
| `cf/qa` | Stato QA per ordine: `{order_id, gate, esito, motivo, n_rework, ts}` |
| `cf/failures` | ReasoningBank: pattern gate falliti per tipo, brand, formato; distillati da CF-R6-LEARN |

---

## KPI del reparto

| KPI | Owner | Definizione |
|---|---|---|
| First-pass rate per formato | CF-R6-COORD | % deliverable che superano tutti e 3 i gate al primo giro; [DM] baseline |
| GATE-FORMATO pass rate | CF-R6-FORMAT | % pezzi con GATE-FORMATO PASS al primo giro; [DM] |
| GATE-BRAND pass rate | CF-R6-BRAND | % pezzi con GATE-BRAND PASS al primo giro; [DM] |
| GATE-COPY pass rate | CF-R6-COPY | % pezzi con GATE-COPY PASS al primo giro; [DM] |
| N. rework per ciclo | CF-R6-REWORK | Rework aperti nel periodo; monitorare per trend; [DM] |
| Latenza QA per pezzo | CF-R6-COORD | Tempo medio dal ricevimento deliverable al verdetto; [DM] |

---

## Handoff e connessioni inter-reparto

| Direzione | Reparto/Ecosistema | Cosa transita |
|---|---|---|
| ← riceve da | CF-R3 (Produzione Video) | Video montato in `orders/<id>/04-render/video/` |
| ← riceve da | CF-R4 (Produzione Testuale) | Testo/articolo/script in `orders/<id>/02-copy/` |
| ← riceve da | CF-R5 (Visual & Design) | PNG caroselli/thumbnail in `orders/<id>/04-render/PNG/` |
| ← riceve da | CF-R2 | `brand_kit.json` validato per GATE-BRAND parametrico |
| → restituisce a | CF-R3/R4/R5 via CF-R6-REWORK | Specifica rework strutturata con gate fallito e motivo |
| → consegna a | CF-R7 (Pubblicazione) | Deliverable con gate verdi in `orders/<id>/05-qa/verdict.json` |
| → alimenta | `cf/failures` + 07-FORGE | Pattern gate falliti; richieste miglioramento a FORGE |
| → riporta a | L1-POST (Capo Area Post-Produzione) | KPI, escalation, report mensile |

---

## Connessioni

- [[03-ECOSISTEMA-CONTENT-FACTORY-V2]] · `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY-V2.md §CF-R6`
- [[CF-R3-Produzione-Video]] · fornitore principale deliverable video
- [[CF-R7-Pubblicazione-Distribuzione]] · destinatario dopo gate verdi
- [[principi/PRINCIPI]] · `principi/PRINCIPI.md` — regole non negoziabili del reparto
