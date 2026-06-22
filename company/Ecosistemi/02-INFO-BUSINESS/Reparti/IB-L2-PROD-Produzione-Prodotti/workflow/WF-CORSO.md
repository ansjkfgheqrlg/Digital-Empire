---
Type: WORKFLOW
Status: Active
Tags: #workflow #infobusiness #corso #mkd #curriculum #platform #IB-L2-PROD
Created: 2026-06-21
Last updated: 2026-06-21
---

# WF-CORSO — Corso Live End-to-End

> **ID:** WF-IB-PROD-002 · **Owner:** `IB-COORD-PRODOTTO`
> **Reparto:** IB-L2-PROD Produzione Prodotti
> **Trigger:** brief validato (WF-VALIDAZIONE PASS) + cartella raw (es. `Formazzione/Claude code/`)

---

## Scopo

Produrre un corso completo da materiale raw già posseduto fino a un corso live sulla piattaforma
reale, pronto al lancio. La pipeline trasforma raw → MKD (100% atomi) → curriculum (outcome
verificabili) → script → video (03-CONTENT-FACTORY) → corso su Supabase+Next.js (PLATFORM) → asset.
"Vendi la Skill" è il primo banco di prova; gli agenti `formazione-*` esistenti sono wrappati come
team L3 del workflow.

**Regola fondamentale:** nessuno step avanza senza gate QA verde di IB-PROD-QA. Nessun corso si
consegna a IB-L2-VEND prima dello smoke test "studente fantasma" verde sul modulo 1 (R6 — no lancio di ombre).

---

## Attori

| Step | Agente IB-L2-PROD | Agente/Reparto esterno |
|---|---|---|
| MKD | `IB-PROD-MKD` | skill `content-forge` (motore raw → MKD) |
| Gate atomi | `IB-PROD-QA` | — |
| Curriculum | `IB-PROD-CURRIC` | skill `course-architect` (P1) + `prd-architect-os` |
| Gate outcome | `IB-PROD-QA` | — |
| Script lezioni | `IB-PROD-WRITER` | — (voce DE, Mandato Empire) |
| Gate brand voice | `IB-PROD-QA` | — |
| Video | `IB-PROD-WRITER` (brief) | 03-CONTENT-FACTORY (`HC-CF-IB-01`) |
| Deploy piattaforma | `IB-PROD-PLATFORM` (coord.) | PLATFORM: formazione-orchestrator/admin/design/student (`HC-PL-IB-01`) |
| Gate smoke test | `IB-PROD-QA` | studente fantasma |
| Asset | `IB-PROD-DESIGN` | 03-CF (grafiche) |
| Pattern di ciclo | `IB-PROD-LEARN` | — |

---

## Flusso passo-passo

```
[TRIGGER]
WF-VALIDAZIONE PASS → brief validato + cartella raw
         │
         ▼
[STEP 1] IB-PROD-MKD — content-forge sull'intera cartella raw → MKD
  → content_forge_runner.py [WRAPPA] produce MKD + atomi-check.json
  → l'MKD ESPANDE la fonte (rapporto ≥1), non sintetizza
  → GATE QA-1 (atomi): copertura = 100% atomi fonte (checklist quantitativa)?
    PASS → prosegui; FAIL → IB-PROD-MKD recupera atomi mancanti, non si avanza
         │
         ▼
[STEP 2] IB-PROD-CURRIC — MKD → curriculum
  → course-architect: moduli, lezioni, outcome misurabile/lezione, esercizio, prerequisiti, durata
  → GATE QA-2 (outcome): ogni lezione ha 1 outcome verificabile + esercizio + durata stimata?
    PASS → prosegui; FAIL → lezioni senza outcome riprogettate (R5)
         │
         ▼
[STEP 3] IB-PROD-WRITER — script lezione per lezione
  → testo/script dal curriculum; voce DE; zero contenuto generico
  → GATE QA-3 (brand voice + prove): brand voice OK + nessun claim senza prova (Mandato Art.2)?
    PASS → prosegui; FAIL → script riscritto sulle sezioni non conformi (R7)
         │
         ▼
[STEP 4] HANDOFF HC-CF-IB-01 → 03-CONTENT-FACTORY
  → IB-PROD-WRITER consegna script + brief visivo: {prodotto_id, lezione_id[], script_path, durata_target, brief_visivo}
  → Acceptance: MP4, audio ≥44kHz, durata da brief, thumbnail inclusa
  → GATE-4 (handoff CF): 03-CF accetta i criteri → moduli video montati ritornano
    asset video mancanti → IB-PROD-PLATFORM blocca deploy, escalation a IB-COORD-PRODOTTO
         │
         ▼
[STEP 5] IB-PROD-PLATFORM — deploy su piattaforma (HC-PL-IB-01)
  → coordina i 4 formazione-*: orchestrator (schema+contenuti su Supabase), admin (accessi/iscrizioni),
    design (UI corso), student (percorso + progress tracking)
  → GATE QA-4 (smoke test): studente fantasma completa modulo 1 end-to-end, zero errori 500?
    PASS → prosegui; FAIL → difetti registrati in smoke-test.json, IB-PROD-PLATFORM coordina fix
         │
         ▼
[STEP 6] IB-PROD-DESIGN — asset prodotto
  → copertina, workbook, certificato; brief grafiche a 03-CF
  → GATE QA-5 (asset): brand conforme + zero placeholder + link funzionanti?
    PASS → prosegui; FAIL → asset rifatto (R6)
         │
         ▼
[STEP 7] HANDOFF HC-IB-VEND-01 → IB-L2-VEND
  → corso live + asset vendita preliminari: {prodotto_id, url_corso, outcome_per_modulo[], asset_path[], prezzo_stimato}
  → corso in stato_finale: "live"
         │
         ▼
[STEP 8] IB-PROD-LEARN — pattern di ciclo
  → cosa ha rallentato, quale gate ha iterato di più, formato che funziona
  → infobusiness/prod/reasoning/pattern-{YYYYMMDD}.md
```

---

## Gate bloccanti

| Gate | Condizione PASS | Owner | Blocca |
|---|---|---|---|
| QA-1 — Atomi 100% | MKD copre il 100% atomi fonte; rapporto espansione ≥1 | IB-PROD-QA | Curriculum |
| QA-2 — Outcome | 1 outcome verificabile + esercizio + durata per lezione | IB-PROD-QA | Scrittura script |
| QA-3 — Brand voice + prove | Voce DE OK + zero claim senza prova | IB-PROD-QA | Handoff CF |
| QA-4 — Smoke test | Studente fantasma completa modulo 1, zero errori 500 | IB-PROD-QA | Asset + consegna |
| QA-5 — Asset | Brand conforme + zero placeholder + link ok | IB-PROD-QA | Consegna IB-L2-VEND |

---

## Input / Output del workflow

**Input trigger:**
```json
{
  "trigger": "WF-VALIDAZIONE PASS",
  "prodotto_id": "CORSO-001",
  "titolo": "Vendi la Skill",
  "raw_folder": "Formazzione/Claude code/",
  "brief_validato": true,
  "icp": "...",
  "durata_target_h": 0
}
```

**Output finale:**
```json
{
  "prodotto_id": "CORSO-001",
  "url_corso": "https://piattaforma/corsi/vendi-la-skill",
  "outcome_per_modulo": ["M1: configura X e mostra che funziona", "M2: ..."],
  "asset_path": ["copertina.png", "workbook.pdf", "certificato.pdf"],
  "smoke_test": "PASS",
  "gate_qa_tutti": "PASS",
  "prezzo_stimato": "[DM] — da brief / team-prezzi",
  "stato_finale": "live",
  "handoff": "HC-IB-VEND-01",
  "namespace": "infobusiness/prod/corso/state.json"
}
```

---

## State

File: `infobusiness/prod/corso/state.json` (+ `MKD-{prodotto}.md`, `CURRIC-{prodotto}.md`, `smoke-test-{prodotto}.json`)
- Creato all'avvio del workflow su brief validato.
- `fase_corrente` aggiornato ad ogni step; `gate_qa` traccia ogni gate (PASS/FAIL).
- `stato_finale: "live"` solo con tutti i gate QA a PASS, incluso smoke test (R4/R6).

---

## Connessioni

- [[ib-coord-prodotto]] · `agenti/ib-coord-prodotto.md` — orchestra il workflow
- [[ib-prod-mkd]] · `agenti/ib-prod-mkd.md` — produce il MKD (Step 1)
- [[ib-prod-qa]] · `agenti/ib-prod-qa.md` — presidia i 5 gate bloccanti
- [[WF-VALIDAZIONE]] · `workflow/WF-VALIDAZIONE.md` — trigger del workflow (brief validato)
- [[WF-EBOOK]] · `workflow/WF-EBOOK.md` — pipeline gemella per formato ebook
- [[02-ECOSISTEMA-INFOBUSINESS-V2]] · `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS-V2.md §IB-L2-PROD WF-CORSO`
