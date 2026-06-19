---
Type: REPARTO
Status: Active
Tags: #reparto #content-factory #strategia #brief #pre-produzione #CF-R1
Created: 2026-06-19
Last updated: 2026-06-19
---

# CF-R1 — Strategia & Brief

> **Ecosistema:** 03-CONTENT-FACTORY · **Area:** Pre-Produzione · **Livello:** L2 Reparto
> **Dossier:** `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY-V2.md §CF-R1`
> **Standard:** CF-grade (ADR-007) · **Reparto v2 — wrappa funzioni brief v1 esistenti (ADR-003)**

---

## Missione

Trasformare ogni ordine validato in un **brief eseguibile**: angle, hook type, struttura
per formato, calendario, assegnazione ai reparti di produzione (R3/R4/R5).

**Nessun contenuto si produce senza brief approvato.** Questo è il principio fondante e
il confine operativo del reparto: CF-R1 è il filtro che garantisce che ogni asset abbia
una direzione creativa coerente con il brand_kit del committente, l'icp dichiarato e il
Mandato Empire prima che qualsiasi risorsa di produzione venga impegnata.

---

## Cosa fa il reparto

1. **Analizza ogni ordine validato** — carica brand_kit + icp, identifica vincoli formato.
2. **Produce 3 angle alternativi** — da libreria formule interna + trend da 08-INTELLIGENCE.
3. **Seleziona il hook type** — coerente con l'icp e la libreria hook di CF-DE.
4. **Gate brief** — verifica che tutti i campi obbligatori siano presenti prima di passare
   il brief alla produzione.
5. **Pianifica il calendario editoriale** — slot multi-brand, mix formati, finestre trend.
6. **Impara dalla performance** — correla angle/hook con first-pass rate in produzione.

## Cosa NON fa

- Non produce contenuto: quello è il dominio di R3 (Video), R4 (Testuale), R5 (Visual).
- Non scrive copy di conversione o APSOC: quello è 04-MARKETING L2.1.
- Non valida il brand_kit: quello è CF-R2 (Brand-Kit & Tenant Registry).
- Non pubblica: quello è CF-R7 (Pubblicazione & Distribuzione).
- Non approva il budget di produzione: quello è CF-SENT-COST (CF-Director team).

---

## Roster del reparto (8 agenti)

| ID | Agente | File | Tipo | Tier | Ruolo |
|---|---|---|---|---|---|
| `CF-R1-COORD` | Coordinatore Strategia & Brief | `agenti/cf-r1-coord.md` | coordinator | sonnet | Orchestra i 3 workflow; riporta a L1-PRE; valuta conformità angolo al Mandato |
| `CF-R1-QA` | Verificatore Brief | `agenti/cf-r1-qa.md` | verifier | sonnet | Gate brief: campi obbligatori angle/hook_type/struttura/canali/vincoli; BLOCCA se incompleto |
| `CF-R1-ANALYST` | Brief Analyst | `agenti/cf-r1-analyst.md` | worker | sonnet | Parse ordine; carica brand_kit+icp; identifica vincoli specifici per formato |
| `CF-R1-ANGLE` | Angle Strategist | `agenti/cf-r1-angle.md` | worker | sonnet | 3 angle alternativi per brief da libreria formule + trend 08-INTELLIGENCE |
| `CF-R1-HOOK` | Hook Selector | `agenti/cf-r1-hook.md` | worker | haiku | Seleziona formula hook da libreria coerente con icp |
| `CF-R1-TREND` | Trend Intake Specialist | `agenti/cf-r1-trend.md` | worker | haiku | Riceve brief trend da 08-INTELLIGENCE; aggiorna libreria angle per brand/nicchia |
| `CF-R1-CAL` | Calendar Planner | `agenti/cf-r1-cal.md` | worker | sonnet | Piano editoriale multi-brand: slot, mix formati, ricorrenze |
| `CF-R1-LEARN` | Brief Performance Analyst | `agenti/cf-r1-learn.md` | worker | sonnet | Correla angle/hook con first-pass rate; pattern in `cf/patterns` |

---

## Workflow del reparto (3 workflow CF-grade)

| ID | File | Scopo | Gate di uscita |
|---|---|---|---|
| **WF-BRIEF** | `workflow/WF-BRIEF.md` | Da ordine validato a `brief.json` eseguibile | CF-R1-QA: angle+hook_type+struttura+canali+vincoli presenti; BLOCCANTE |
| **WF-CALENDAR** | `workflow/WF-CALENDAR.md` | Piano editoriale multi-brand settimanale | Piano consegnato con slot per brand_kit validato; nessun slot orfano |
| **WF-TREND-BRIEF** | `workflow/WF-TREND-BRIEF.md` | Brief accelerato ≤1h per contenuti a finestra stretta | Latenza intake→brief ≤1h; trend >48h scartato con motivo |

---

## Namespace memoria

| Namespace | Contenuto |
|---|---|
| `cf/briefs` | brief.json per ordine (`orders/<id>/01-brief/brief.json`) |
| `cf/calendars` | Piani editoriali per brand (`cf/calendars/<brand>/`) |
| `cf/patterns` | Pattern angle/hook validati per brand/nicchia (alimentati da CF-R1-LEARN) |

---

## KPI del reparto

| KPI | Owner | Definizione |
|---|---|---|
| Lead time ordine→brief | CF-R1-COORD | Minuti tra ricezione ordine validato e brief.json approvato; [DM] baseline |
| % brief completi al primo giro | CF-R1-QA | N. brief superati GATE senza rework / tot brief prodotti nel periodo |
| Angle usati vs scartati per brand | CF-R1-ANGLE | N. angle selezionati dal committente / N. angle prodotti; [DM] baseline |

---

## Handoff e connessioni inter-reparto

| Direzione | Reparto/Ecosistema | Cosa transita |
|---|---|---|
| ← riceve da | CF-Director (CF-D-DISPATCH) | Ordine validato con brand_kit+icp+formato+deadline |
| ← riceve da | 08-INTELLIGENCE | Brief trend (`intel→cf`) per WF-TREND-BRIEF |
| ← riceve da | CF-R2 | brand_kit validato per ogni tenant |
| → consegna a | CF-R3 (Produzione Video) | brief.json + slot calendario per formati video |
| → consegna a | CF-R4 (Produzione Testuale) | brief.json + slot calendario per formati testo |
| → consegna a | CF-R5 (Visual & Design) | brief.json + slot calendario per caroselli/visual |
| → consegna a | 04-MARKETING L2.2 | Finestre trend per coordinamento calendario ads |

---

## Principi e regole

- Principi operativi → `principi/PRINCIPI.md`

---

## Connessioni

- [[03-ECOSISTEMA-CONTENT-FACTORY-V2]] · `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY-V2.md §CF-R1`
- [[CF-R2-Brand-Kit-Tenant-Registry]] · fornitore brand_kit validati
- [[08-INTELLIGENCE]] · fornitore brief trend
- [[WF-BRIEF]] · `workflow/WF-BRIEF.md`
- [[WF-CALENDAR]] · `workflow/WF-CALENDAR.md`
- [[WF-TREND-BRIEF]] · `workflow/WF-TREND-BRIEF.md`
