---
Type: REPARTO
Status: Active
Tags: #reparto #content-factory #apprendimento #ottimizzazione #CF-R8 #post-produzione #pattern #reasoningbank
Created: 2026-06-23
Last updated: 2026-06-23
---

# CF-R8 — Apprendimento & Ottimizzazione

> **Ecosistema:** 03-CONTENT-FACTORY · **Area:** Post-Produzione · **Livello:** L2 Reparto
> **Dossier:** `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY-V2.md §CF-R8`
> **Standard:** CF-grade (ADR-007) · **INVARIANT CARDINALE:** nessun pattern senza ≥3 casi verificati
> **Nota:** CF-R8 è il NONO e ULTIMO reparto — con il suo completamento l'ecosistema 03-CONTENT-FACTORY è COMPLETO (9/9 reparti).

---

## Missione

Distillare le lezioni dall'intera pipeline CF-DE e tradurle in miglioramenti strutturati, misurati e tracciabili.
CF-R8 è il reparto di chiusura del loop: raccoglie i segnali di performance (hook, engine, fallimenti)
da tutti i reparti, li valida con la soglia ≥3 casi, li archivia nei namespace `cf/patterns` e `cf/failures`,
aggiorna la libreria formule di CF-R1, ottimizza il routing engine in CF-R5, e propone ADR
su pattern strutturali al Board e richieste di nuova skill a 07-FORGE.

CF-R8 non produce contenuto. Produce conoscenza operativa verificata che migliora la pipeline nel tempo.

CF-R8-COORD riporta a L1-POST e opera trasversalmente su tutti i reparti della Content Factory.

---

## Cosa fa il reparto

1. **Distilla pattern hook/angle** (WF-PATTERN-DISTILLATION): ogni settimana analizza le performance
   7gg dei contenuti pubblicati (CF-R7-FEEDBACK) per identificare quali hook e angle hanno performato
   meglio per brand/formato/nicchia → aggiorna la libreria formule di CF-R1.
2. **Distilla fallimenti** (WF-PATTERN-DISTILLATION): ogni post-task, CF-R8-REASONING legge
   `cf/failures` (alimentato da CF-R6-LEARN) e distilla lezioni strutturate → propone fix a reparti
   specifici o richieste a 07-FORGE.
3. **Analizza performance engine** (WF-PATTERN-DISTILLATION): CF-R8-ENGINE valuta qualità output
   per engine (Canva vs Puppeteer vs Higgsfield) per formato/nicchia → ottimizza routing
   capability→engine nel workflow CF-R5.
4. **Valida ogni pattern** (CF-R8-QA): nessun pattern entra in `cf/patterns` senza ≥3 casi,
   fonte tracciabile, nessuna correlazione inventata — invariant Mandato Art.2.
5. **Alimenta il neural trainer** (WF-IMPROVEMENT-CYCLE): CF-R8-NEURAL usa i pattern validati
   da `cf/patterns` per alimentare `neural_train` quando esistono dati reali sufficienti.
6. **Propone e traccia miglioramenti** (WF-IMPROVEMENT-CYCLE): dal pattern distillato
   alla proposta → approvazione CF-Director → implementazione → misurazione effetto 4 settimane.
7. **Propone ADR su pattern strutturali**: se un pattern rivela un difetto architetturale
   ricorrente (≥3 casi confermati), CF-R8-COORD redige una bozza ADR e la sottopone al Board.

## Cosa NON fa

- Non produce asset di nessun tipo: non scrive copy, non genera immagini, non pubblica.
- Non emette pattern su n < 3: invariant non derogabile nemmeno in emergenza.
- Non modifica direttamente workflow, schede agente, o configurazioni di altri reparti:
  propone sempre; CF-Director o 07-FORGE decidono e implementano.
- Non sostituisce CF-R6 nel gatekeeping QA: CF-R8 lavora sui pattern aggregati, non sui verdetti
  singoli (quelli sono di CF-R6).
- Non fa analisi su dati non tracciabili: se la fonte non è citabile in formato `{namespace, key, ts}`,
  il pattern non viene validato.
- Non avvia improvement cycle senza approvazione CF-Director: nessuna modifica strutturale
  senza esplicita autorizzazione.

---

## Roster del reparto (6 agenti)

| ID | Agente | File | Tipo | Tier | Ruolo |
|---|---|---|---|---|---|
| `CF-R8-COORD` | Learning & Optimization Lead | `agenti/cf-r8-coord.md` | coordinator | sonnet | Orchestra WF-PATTERN-DISTILLATION e WF-IMPROVEMENT-CYCLE; aggiorna libreria; propone ADR; riporta a L1-POST |
| `CF-R8-QA` | Pattern Verifier | `agenti/cf-r8-qa.md` | verifier | sonnet | Valida ogni pattern: ≥3 casi, fonte tracciabile, nessuna correlazione inventata |
| `CF-R8-HOOK` | Hook Pattern Analyst | `agenti/cf-r8-hook.md` | analyst | sonnet | Quali hook/angle performano per brand/formato/nicchia → aggiorna libreria formule CF-R1 |
| `CF-R8-ENGINE` | Engine Performance Analyst | `agenti/cf-r8-engine.md` | analyst | sonnet | Qualità output per engine Canva vs Puppeteer vs Higgsfield → ottimizza routing capability→engine |
| `CF-R8-REASONING` | ReasoningBank Distiller | `agenti/cf-r8-reasoning.md` | analyst | sonnet | Distilla `cf/failures` → lezioni strutturate → fix a reparti + richieste 07-FORGE |
| `CF-R8-NEURAL` | Neural Pattern Trainer | `agenti/cf-r8-neural.md` | worker | haiku | Alimenta `neural_train` con pattern validati da `cf/patterns` quando dati reali sufficienti |

---

## Workflow del reparto (2 workflow CF-grade)

| ID | File | Scopo | Cadenza |
|---|---|---|---|
| **WF-PATTERN-DISTILLATION** | `workflow/WF-PATTERN-DISTILLATION.md` | Post-task: distilla pattern hook + failures + engine → QA valida → `memory_store("cf/patterns")` + aggiornamento CF-R1 | Settimanale (hook/angle); mensile (engine e failures) |
| **WF-IMPROVEMENT-CYCLE** | `workflow/WF-IMPROVEMENT-CYCLE.md` | Da pattern distillato a miglioramento implementato e misurato | Mensile (ciclo 4 settimane di osservazione) |

---

## Namespace memoria

| Namespace | Contenuto |
|---|---|
| `cf/patterns` | Pattern validati (≥3 casi, fonte tracciabile): hook, engine, failures distillati |
| `cf/failures` | ReasoningBank: gate falliti classificati per tipo/brand/formato (alimentato da CF-R6-LEARN) |
| `cf/improvements` | Tracking improvement cycle: proposta, stato, effetto misurato |

---

## KPI del reparto

| KPI | Owner | Definizione |
|---|---|---|
| Pattern validati/mese | CF-R8-QA | N. pattern con ≥3 casi entrati in `cf/patterns` nel periodo; [DM] baseline |
| Fix proposti vs implementati | CF-R8-COORD | Ratio fix proposti/approvati/implementati; [DM] |
| Miglioramento first-pass rate nel tempo | CF-R8-COORD | Delta first-pass rate CF-R6 mese M vs M-3 dopo improvement cycle; [DM] |
| Pattern hook aggiornati in CF-R1 | CF-R8-HOOK | N. formule libreria CF-R1 aggiornate per mese; [DM] |
| Latenza pattern→improvement implementato | CF-R8-COORD | Giorni da pattern confermato a improvement live; [DM] |

---

## Handoff e connessioni inter-reparto

| Direzione | Reparto/Ecosistema | Cosa transita |
|---|---|---|
| ← riceve da | CF-R6 (via `cf/failures`) | Pattern gate falliti distillati da CF-R6-LEARN |
| ← riceve da | CF-R7 (via `cf/patterns`) | Metriche 48h e 7gg per hook/angle performance (WF-FEEDBACK-LOOP) |
| ← riceve da | CF-R1 | Libreria formule corrente (hook_type, angle_type per brand) |
| → aggiorna | CF-R1 (libreria formule) | Nuovi hook/angle validati da CF-R8-HOOK |
| → ottimizza | CF-R5 (routing engine) | Aggiornamento routing capability→engine da CF-R8-ENGINE |
| → propone a | 07-FORGE | Richieste nuova skill o modifica agente per pattern strutturali |
| → propone a | Board/CF-Director (ADR bozza) | Pattern architetturali → ADR-bozza per approvazione |
| → riporta a | L1-POST | KPI mensile, improvement cycle status, ADR proposte |
| → alimenta | `neural_train` | Pattern validati da `cf/patterns` via CF-R8-NEURAL |

---

## Connessioni

- [[03-ECOSISTEMA-CONTENT-FACTORY-V2]] · `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY-V2.md §CF-R8`
- [[CF-R6-QA-Gate]] · `company/Ecosistemi/03-CONTENT-FACTORY/Reparti/CF-R6-QA-Gate/README.md` — fonte primaria `cf/failures`
- [[CF-R7-Pubblicazione]] · `company/Ecosistemi/03-CONTENT-FACTORY/Reparti/CF-R7-Pubblicazione/README.md` — fonte metriche performance
- [[principi/PRINCIPI]] · `principi/PRINCIPI.md` — invariant operativi del reparto
