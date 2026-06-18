---
Type: REPARTO
Status: Active
Tags: #reparto #marketing #conversion #funnel #cro #L2.6
Created: 2026-06-18
Last updated: 2026-06-18
---

# L2.6 — Conversion Architecture

> **Ecosistema:** 04-MARKETING · **Livello:** L2 Reparto · **Dossier:** `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md §L2.6`
> **Standard:** CF-grade (ADR-007) · **Reparto NUOVO v2 — greenfield (non esisteva nel v1)**

---

## Missione

Progettare l'architettura completa di conversione — funnel multi-step, landing system,
sequenze di pagine, micro-conversion map — in collaborazione con 06-PLATFORM (che
implementa le pagine tecnicamente).

**Marketing (questo reparto) possiede la STRATEGIA di conversione.**
**06-PLATFORM possiede l'IMPLEMENTAZIONE.**

Il confine è netto e non negoziabile: L2.6 non scrive copy (viene da L2.1), non costruisce
pagine (viene da 06-PLATFORM), non analizza i dati di performance a livello aggregato
(viene da L2.4/AN5). L2.6 trasforma il brief del committente in un'architettura funnel
documentata, con brief tecnico approvato per 06-PLATFORM e copy per stage richiesto a L2.1.

---

## Roster del reparto (6 agenti)

| ID | Agente | File | Tipo | Tier | Ruolo |
|---|---|---|---|---|---|
| `CONV-LEAD` | Conversion Architecture Lead | `agenti/conv-lead.md` | coordinator | opus | Coordina il reparto; disegna architettura conversione per ogni committente; risponde KPI funnel |
| `CA1` | Funnel Strategist | `agenti/ca1-funnel-strategist.md` | worker | opus | Architettura funnel multi-step ToFu→MoFu→BoFu con mapping APSOC per stage |
| `CA2` | Landing Page Strategist | `agenti/ca2-landing-page-strategist.md` | worker | sonnet | Struttura landing hero→proof→offer→objections→CTA; brief tecnico per 06-PLATFORM |
| `CA3` | Micro-Conversion Analyst | `agenti/ca3-micro-conversion-analyst.md` | worker | sonnet | Mappa micro-conversioni scroll/click/opt-in → input per AN5 e ottimizzazione |
| `CA4` | CRO Sprint Lead | `agenti/ca4-cro-sprint-lead.md` | worker | sonnet | Esegue sprint CRO: collo di bottiglia → variante → test → implementazione |
| `CA-QA` | Conversion QA Verifier | `agenti/ca-qa-conversion-verifier.md` | verifier | sonnet | Verifica che ogni funnel rispetti struttura APSOC end-to-end e KPI conversione attesi |

---

## Workflow del reparto (3 workflow CF-grade)

| ID | File | Scopo | Gate di uscita |
|---|---|---|---|
| **WF-FUNNEL-DESIGN** | `workflow/WF-FUNNEL-DESIGN.md` | Design funnel completo: obiettivo → stage map → copy per stage → landing brief → email handoff | CA-QA: coerenza APSOC end-to-end; ogni stage ha copy gated |
| **WF-CRO-SPRINT** | `workflow/WF-CRO-SPRINT.md` | Sprint ottimizzazione: AN5 identifica drop → CA4 variante → WF-AB-TEST → implementazione → misurazione | Verdetto A/B statisticamente valido; implementazione solo dopo gate AN3 |
| **WF-LANDING-AUDIT** | `workflow/WF-LANDING-AUDIT.md` | Audit landing esistente: struttura APSOC + micro-conversion + velocità + mobile → report + 3 azioni prioritarie | CA-QA + AN5; 3 azioni con impatto stimato |

---

## Skill del reparto

| Skill | Priorità | File |
|---|---|---|
| `conversion-funnel-designer` | P2 | `skills/SKILLS.md` |
| `cro-sprint-runner` | P3 | `skills/SKILLS.md` |
| `cro` (esistente, mappata) | — | Wrapper a L2.6/WF-CRO-SPRINT |
| `market-funnel` (esistente, mappata) | — | Ausiliaria CA1 |
| `market-landing` (esistente, mappata) | — | Marketing possiede strategia; Platform implementa |

---

## KPI del reparto

| KPI | Owner | Definizione |
|---|---|---|
| Funnel conversion rate per stage | CONV-LEAD | Drop rate per sezione APSOC (da AN5); baseline da primo funnel live |
| Micro-conversion rate | CA3 | Scroll depth / click CTA / opt-in per stage; [DM] |
| Sprint CRO chiusi con verdetto | CA4 | N. sprint con verdetto A/B statisticamente valido nel periodo |
| Audit landing completati con 3 azioni | CA-QA | N. audit con azioni prioritarie e impatto stimato |

---

## Handoff e connessioni inter-reparto

| Direzione | Reparto/Ecosistema | Cosa transita |
|---|---|---|
| ← riceve da | L2.1 Copywriting | Copy gated per ogni stage del funnel (WF-COPY-FULL / WF-COPY-SALES-PAGE) |
| ← riceve da | L2.3 Email & Lifecycle | Sequenze email per stage MoFu/BoFu (WF-EMAIL-LAUNCH / WF-EMAIL-NURTURE) |
| ← riceve da | L2.4 Analytics (AN5) | Drop rate per sezione APSOC → input diagnosi per WF-CRO-SPRINT |
| → consegna a | 06-PLATFORM | Brief tecnico landing approvato (struttura, sezioni, micro-conversion target) |
| → consegna a | L2.1 Copywriting | Richiesta copy per stage (contratto §1.2 dossier) |
| → consegna a | L2.3 Email | Richiesta sequenze email per stage (obiettivo per stage dichiarato) |
| → consegna a | AN5 (L2.4) | Mappa micro-conversioni attese (CA3 → input per piano di misurazione AN5) |

---

## Escalation

- Sprint CRO con verdetto inconclusivo dopo 2 cicli → CONV-LEAD porta ad AN3 per ricalcolo dimensione campione.
- Conflitto tra strategia L2.6 e implementazione 06-PLATFORM → CONV-LEAD + responsabile 06-PLATFORM; escalation a CMO se non risolto.
- Funnel senza copy gated disponibile da L2.1 → CONV-LEAD non emette brief tecnico; blocca e segnala a MKT-Conductor.
- Qualsiasi ottimizzazione senza verdetto A/B valido → CA-QA blocca; non si implementa su opinione.

---

## Principi e regole

- Principi operativi → `principi/PRINCIPI.md`
- Regole non negoziabili → `regole/REGOLE.md`

---

## Connessioni

- [[04-ECOSISTEMA-MARKETING-V2]] · `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md §L2.6`
- [[06-ECOSISTEMA-PLATFORM]] · partner implementazione landing
- [[L2-1-Copywriting]] · fornitore copy per ogni stage funnel
- [[L2-4-Analytics]] · AN5 fornitore drop rate; AN3 verifica dimensione test
- [[WF-FUNNEL-DESIGN]] · `workflow/WF-FUNNEL-DESIGN.md`
- [[WF-CRO-SPRINT]] · `workflow/WF-CRO-SPRINT.md`
- [[WF-LANDING-AUDIT]] · `workflow/WF-LANDING-AUDIT.md`
