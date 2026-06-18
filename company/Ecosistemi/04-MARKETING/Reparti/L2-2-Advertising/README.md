---
Type: REPARTO
Status: Active
Tags: #reparto #marketing #advertising #paid #campagne #L2-2
Created: 2026-06-18
Last updated: 2026-06-18
---

# L2.2 — Advertising

> **Ecosistema:** 04-MARKETING · **Livello:** L2 Reparto · **Dossier:** `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md §L2.2`
> **Standard:** CF-grade (ADR-007) · **Reparto ampliato v2 — da 4 a 8 agenti**

---

## Missione

Gestire campagne paid end-to-end (strategia → creative → setup → monitoraggio → iterazione)
su Meta, Google, LinkedIn, TikTok.

**Il copy delle ads viene SEMPRE da L2.1 (WF-COPY-AD). Mai scritto qui.**
Advertising possiede: targeting, budget, struttura campagna, testing creativo, compliance piattaforma.

Il confine è netto e non negoziabile: L2.2 non scrive copy (viene da L2.1), non analizza
dati aggregati di marketing (viene da L2.4), non produce visual (viene da 03-CF via L2.5/BR3).
ADS-LEAD coordina il reparto, riceve brief da MKT-Conductor, risponde dei KPI paid.

**Vincolo globale assoluto (Mandato Art.4.3):** nessuna spesa ads reale senza ok esplicito
di Max. Dry-run default per ogni setup campagna. AD3 non può lanciare in produzione senza
approvazione umana esplicita registrata nel contratto.

---

## Roster del reparto (8 agenti)

| ID | Agente | File | Tipo | Tier | Ruolo |
|---|---|---|---|---|---|
| `ADS-LEAD` | Advertising Lead | `agenti/ads-lead.md` | coordinator | opus | Coordina reparto; riceve brief da MKT-Conductor; assegna workflow; risponde KPI paid |
| `AD1` | Audience Analyst | `agenti/ad1-audience-analyst.md` | worker | sonnet | Ricerca audience, segmenti, lookalike per piattaforma; input da 08-INTELLIGENCE |
| `AD2` | Creative Iterator | `agenti/ad2-creative-iterator.md` | worker | sonnet | Varianti creative a scala dal winner; fan-out swarm; skill `ad-creative` |
| `AD3` | Media Buyer | `agenti/ad3-media-buyer.md` | worker | sonnet | Struttura campagna, budget, bid, pacing (dry-run default Art.4.3, sotto Cost-Sentinel) |
| `AD4` | Ad Compliance Checker | `agenti/ad4-compliance-checker.md` | verifier | sonnet | Policy Meta/Google/LinkedIn/TikTok pre-flight — blocca se non conforme (gate G3) |
| `AD5` | Platform Specialist | `agenti/ad5-platform-specialist.md` | worker | sonnet | Specialista per piattaforma: differenze formato/algoritmo/policy tra Meta/Google/LinkedIn/TikTok |
| `AD6` | Creative Analyst | `agenti/ad6-creative-analyst.md` | worker | sonnet | Analizza performance creative (CTR, heatmap formati); identifica pattern per AD2 |
| `AD-QA` | Ads QA Verifier | `agenti/ad-qa-ads-verifier.md` | verifier | sonnet | Verifica brand_kit/pricing/vincoli legali su ogni campagna prima del lancio |

---

## Workflow del reparto (3 workflow CF-grade)

| ID | File | Scopo | Gate di uscita |
|---|---|---|---|
| **WF-ADS-CAMPAIGN** | `workflow/WF-ADS-CAMPAIGN.md` | Brief → S3 strategia → AD1 audience → WF-COPY-AD copy → creative → setup → dry-run | G1 copy ≥80; G3 compliance; ok umano spesa (Art.4.3) |
| **WF-CREATIVE-TEST** | `workflow/WF-CREATIVE-TEST.md` | Fan-out varianti → matrice copy × visual × audience → verdetto statistico | Soglia minima campione raggiunta; verdetto predefinito; no forzatura |
| **WF-ADS-PERFORMANCE** | `workflow/WF-ADS-PERFORMANCE.md` | Loop monitoraggio → diagnosi → AD2 itera dal winner → update `marketing/ads/experiments` | Dati minimi per verdetto; pattern consolidati solo con evidenza ripetuta |

---

## Skill del reparto

| Skill | Priorità | Riferimento |
|---|---|---|
| `ads-compliance` (nuova, P2) | P2 | `skills/SKILLS.md` — pre-flight Meta/Google/LinkedIn/TikTok |
| `ads` (esistente, mappata) | — | Strategia campagna, targeting, bidding |
| `ad-creative` (esistente, mappata) | — | Generazione varianti creative a scala |
| `market-ads` (esistente, ausiliaria) | — | Ausiliaria di T-CREATIVE-BATCH |

---

## KPI del reparto

| KPI | Owner | Definizione |
|---|---|---|
| CTR per campagna e piattaforma | ADS-LEAD | Click-through rate: confronto variante vs variante (mai vs benchmark esterni) |
| CPC per campagna e piattaforma | ADS-LEAD | Costo per click: confronto variante vs variante; [DM] nessuna baseline storica esistente |
| CPA per campagna | AD3 | Costo per acquisizione/conversione; baseline da primo run reale |
| G3 compliance PASS rate | AD4 | % campagne che passano compliance pre-flight al primo tentativo |
| Ad-QA PASS rate | AD-QA | % campagne verificate senza rework su brand_kit/pricing/vincoli legali |
| Varianti testate per ciclo | AD2 | N. varianti creative generate e testate in WF-CREATIVE-TEST per ciclo |
| Esperimenti chiusi con verdetto | AN3 | N. test con verdetto statisticamente valido nel periodo (in coordinamento con L2.4) |
| Gate bypass rate | AD4/AD-QA | Deve essere 0 — ogni bypass è un incidente da loggare |

---

## Handoff e connessioni inter-reparto

| Direzione | Reparto/Ecosistema | Cosa transita |
|---|---|---|
| ← riceve da | MKT-Conductor | Brief campagna con BUDGET OK ESPLICITO di Max (campo obbligatorio nel contratto) |
| ← riceve da | L2.1 Copywriting | Copy ads gated (WF-COPY-AD: 3+ varianti APSOC ≥80) — mai scritto qui |
| ← riceve da | L2.5 Brand/Creative | Creative brief BR3 (tone ads, mood, regole visuali) + visual via 03-CF |
| ← riceve da | 08-INTELLIGENCE | Audience data, competitor insight per AD1 e AD5 |
| ← riceve da | L2.4 Analytics | Performance dati per diagnosi in WF-ADS-PERFORMANCE (AN2, AN3) |
| → consegna a | AD3 → Cost-Sentinel | Budget allocation + struttura campagna per approvazione spend |
| → consegna a | L2.4 Analytics | Matrice test e dati esperimenti in `marketing/ads/experiments` |
| → consegna a | MKT-Conductor | Risultato campagna: varianti, KPI, pattern AD6 per ReasoningBank |

---

## Escalation

- Spesa ads superiore all'envelope approvato → ADS-LEAD blocca e porta a CFO/Cost-Sentinel prima di procedere.
- Campagna che non passa G3 dopo 2 iterazioni compliance → ADS-LEAD escalation a MKT-Conductor + analisi radice.
- Conflitto tra policy piattaforma e claim di copy → AD4 blocca; ADS-LEAD coordina con L2.1 per riscrittura claim.
- Lancio reale senza ok umano esplicito → blocco assoluto, AD3 non procede, log dell'incidente in state.

---

## Principi e regole

- Principi operativi → `principi/PRINCIPI.md`
- Regole non negoziabili → `regole/REGOLE.md`

---

## Connessioni

- [[04-ECOSISTEMA-MARKETING-V2]] · `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md §L2.2`
- [[L2-1-Copywriting]] · fornitore copy ads: mai scritto in questo reparto
- [[L2-4-Analytics]] · AN2/AN3 partner analitici per test e performance
- [[L2-5-Brand-Creative-Strategy]] · BR3 fornitore creative brief e direction visuale
- [[WF-ADS-CAMPAIGN]] · `workflow/WF-ADS-CAMPAIGN.md`
- [[WF-CREATIVE-TEST]] · `workflow/WF-CREATIVE-TEST.md`
- [[WF-ADS-PERFORMANCE]] · `workflow/WF-ADS-PERFORMANCE.md`
- [[MANDATO-EMPIRE]] · `company/Mandato/MANDATO-EMPIRE.md` (Art.4.3 — vincolo spesa)
