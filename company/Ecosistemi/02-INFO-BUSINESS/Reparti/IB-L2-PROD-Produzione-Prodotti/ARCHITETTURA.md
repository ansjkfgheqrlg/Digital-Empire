---
Type: CONCEPT
Status: Active
Tags: #architettura #infobusiness #prodotto #produzione #IB-L2-PROD
Created: 2026-06-18
Last updated: 2026-06-18
---

# ARCHITETTURA — IB-L2-PROD Produzione Prodotti

> Cartella-workflow CF-grade. Standard: Content Factory Exponium (corpus Maximilian).
> Dossier sorgente: `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS-V2.md` §3 + §IB-L2-PROD

---

## Topologia del team

```
                   ┌──────────────────────────────┐
                   │  IB-COORD-PRODOTTO (Sonnet)    │
                   │  capo area, orchestra i 3 WF   │
                   └──────────────┬───────────────-┘
                                  │
        ┌──────────────┬──────────┼───────────┬──────────────┐
        │              │          │           │              │
  ┌─────▼─────┐  ┌─────▼─────┐ ┌──▼──────┐ ┌──▼────────┐ ┌───▼────────┐
  │IB-PROD-   │  │IB-PROD-MKD│ │IB-PROD- │ │IB-PROD-   │ │IB-PROD-    │
  │VALID      │  │(forge)    │ │CURRIC   │ │WRITER     │ │EBOOK       │
  │(gate IN)  │  │           │ │         │ │           │ │            │
  └─────┬─────┘  └─────┬─────┘ └──┬──────┘ └──┬────────┘ └───┬────────┘
        │              │          │           │              │
        │         ┌────▼──────┐ ┌─▼──────────▼┐         ┌────▼────────┐
        │         │IB-PROD-   │ │IB-PROD-     │         │ (handoff    │
        │         │DESIGN     │ │PLATFORM     │         │  03-CF /    │
        │         │           │ │(HC-PL-IB-01)│         │  PLATFORM)  │
        │         └────┬──────┘ └─────┬───────┘         └─────────────┘
        │              │              │
        └──────────────┼──────────────┘ output prodotto
                       │
         ┌─────────────▼──────────────┐   ┌──────────────────────┐
         │ IB-PROD-QA (Sonnet)         │   │ IB-PROD-LEARN (Sonnet)│
         │ gate qualita — bloccante    │   │ pattern di processo   │
         └─────────────────────────────┘   └──────────────────────┘
```

**Topologia:** pipeline lineare governata dal coordinator. `IB-PROD-VALID` e il gate d'ingresso
(nessun prodotto entra senza brief validato). `IB-PROD-QA` opera trasversalmente come gate di
qualita su ogni step chiave (blocca, non suggerisce). `IB-PROD-LEARN` osserva ogni ciclo e
deposita pattern in `infobusiness/reasoning`. La sequenza varia per workflow (vedi flussi).

---

## Livelli gerarchici interni

| Livello | Agente(i) | Tier | Funzione |
|---|---|---|---|
| L0 — Coordinator | `IB-COORD-PRODOTTO` | Sonnet | Orchestra i 3 WF, priorita, escalation, KPI settimanale |
| L1 — Gate ingresso | `IB-PROD-VALID` | Sonnet | WF-VALIDAZIONE: filtra le idee prima della produzione |
| L2 — Produzione | `IB-PROD-MKD` · `IB-PROD-CURRIC` · `IB-PROD-WRITER` · `IB-PROD-EBOOK` | Sonnet | Trasformazione raw → MKD → struttura → testo |
| L3 — Integrazione | `IB-PROD-PLATFORM` · `IB-PROD-DESIGN` | Sonnet | Deploy su piattaforma + asset visivi |
| L4 — Verifica | `IB-PROD-QA` | Sonnet | Gate qualita su ogni step (100% atomi, outcome, smoke test) |
| L5 — Apprendimento | `IB-PROD-LEARN` | Sonnet | Pattern di processo → reasoning |

---

## Flussi principali

### WF-VALIDAZIONE (gate d'ingresso)
```
Trigger: nuova idea prodotto (da IB-L2-STRA, BACKLOG, community, segnale agency)
  → IB-PROD-VALID: scoring /100 su 5 criteri (problema, raw disponibile, ICP, differenziazione, posizionamento)
  → Gate 1: score >=60 → avanza a MVP test
  → Gate 2: MVP test 7gg — 5 "si, lo comprerei" reali da ICP
  → IB-COORD-PRODOTTO: approva avvio produzione (PASS) | idea in BACKLOG (FAIL)
Output: brief validato → input WF-CORSO o WF-EBOOK
Gate di uscita: score >=60 + MVP PASS
```

### WF-CORSO (corso live end-to-end)
```
Trigger: brief validato + cartella raw (es. Formazzione/Claude code/)
  → IB-PROD-MKD: content-forge → MKD     [GATE QA: 100% atomi fonte]
  → IB-PROD-CURRIC: MKD → curriculum      [GATE QA: 1 outcome verificabile/lezione + durata]
  → IB-PROD-WRITER: script lezione/lezione [GATE: brand voice + zero generico + zero claim senza prova]
  → HANDOFF HC-CF-IB-01 → 03-CONTENT-FACTORY: script → moduli video montati
  → IB-PROD-PLATFORM: HC-PL-IB-01 → formazione-* su Supabase [GATE QA: smoke test studente fantasma]
  → IB-PROD-DESIGN: copertina, workbook, certificato [GATE QA: brand conforme, zero placeholder]
Output: corso live + asset vendita preliminari → IB-L2-VEND
Gate di uscita: smoke test verde + tutti i gate QA PASS
```

### WF-EBOOK (ebook pronto vendita/lead magnet)
```
Trigger: brief validato + cartella/file raw
  → IB-PROD-MKD: content-forge → MKD       [GATE QA: 100% atomi fonte]
  → IB-PROD-EBOOK: struttura capitoli       [GATE: 1 CTA/capitolo + esercizio/capitolo]
  → IB-PROD-WRITER: testo capitolo/capitolo [GATE QA: prove non promesse su ogni claim]
  → IB-PROD-DESIGN: impaginazione PDF/ePub + copertina [GATE: leggibile mobile, link ok, zero placeholder]
  → IB-PROD-PLATFORM: storage sicuro + link protetto + checkout se a pagamento
Output: file ebook (PDF+ePub) + pagina download → IB-L2-VEND
Nota: routing free/paid Manuale Claude Code in attesa team-prezzi (B-002/B-003 BACKLOG)
```

---

## Flussi con ecosistemi esterni

### IB-L2-PROD → 03-CONTENT-FACTORY
```
IB-PROD-WRITER produce script video lezione → handoff HC-CF-IB-01 a 03-CF.
Acceptance: durata da brief; formato MP4; qualita audio >=44kHz; thumbnail inclusa.
Schema handoff: {prodotto_id, lezione_id[], script_path, durata_target, brief_visivo}
```

### IB-L2-PROD → PLATFORM (Supabase + Next.js)
```
IB-PROD-PLATFORM coordina HC-PL-IB-01 verso i 4 agenti formazione-*:
  formazione-orchestrator (schema + contenuti), formazione-admin (accessi/iscrizioni),
  formazione-design (UI corso), formazione-student (percorso + progress tracking).
Acceptance: smoke test studente fantasma completa modulo 1 end-to-end, zero errori 500.
```

### IB-L2-PROD → IB-L2-VEND
```
Corso live + asset vendita preliminari (bullet outcome, copertina, prezzo stimato dal brief).
Schema handoff: {prodotto_id, url_corso, outcome_per_modulo[], asset_path[], prezzo_stimato}
```

---

## Handoff contract

| Contract | Da → A | Payload | Acceptance criteria |
|---|---|---|---|
| `HC-STRA-IB-01` | IB-L2-STRA → IB-L2-PROD | brief idea + ICP ipotetico + raw path | brief completo per scoring WF-VALIDAZIONE |
| `HC-CF-IB-01` | IB-L2-PROD → 03-CF | script video + brief visivo | MP4, audio >=44kHz, durata da brief, thumbnail |
| `HC-PL-IB-01` | IB-L2-PROD → PLATFORM | curriculum + asset + schema Supabase | smoke test verde, paywall attivo, tracking ok |
| `HC-IB-VEND-01` | IB-L2-PROD → IB-L2-VEND | corso live + asset vendita | corso accessibile, outcome dichiarati, prezzo stimato |

---

## Namespace memoria

```
infobusiness/prod/
├── validazione/
│   └── state.json            → idea, score /100, breakdown, MVP result, esito, data
├── corso/
│   ├── state.json            → per corso: fase corrente, gate superati, errori bloccanti, log
│   ├── MKD-{prodotto}.md      → Master Knowledge Document (100% atomi)
│   ├── CURRIC-{prodotto}.md   → curriculum con outcome map
│   └── smoke-test-{prodotto}.json → log smoke test studente fantasma
├── ebook/
│   └── state.json            → per ebook: fase, capitoli, gate, export PDF/ePub
└── reasoning/
    └── pattern-{YYYYMMDD}.md  → pattern di processo da IB-PROD-LEARN
```

---

## Skill del reparto

| Skill | File | Funzione |
|---|---|---|
| `course-architect` (P1, nuova) | `skills/SKILLS.md` | MKD → curriculum standardizzato con outcome verificabili |
| `content-forge` (esistente) | mapping skill holding | Motore primario raw → MKD (IB-PROD-MKD) |
| `book-to-skill` (esistente) | mapping skill holding | PDF lunghi → struttura (Manuale Claude Code 203pp) |
| `prd-architect-os` (esistente) | mapping skill holding | Strutturazione gerarchica contenuti (IB-PROD-CURRIC) |

---

## Connessioni

- [[README]] · `company/Ecosistemi/02-INFO-BUSINESS/Reparti/IB-L2-PROD-Produzione-Prodotti/README.md`
- [[02-ECOSISTEMA-INFOBUSINESS-V2]] · `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS-V2.md` §IB-L2-PROD
- [[WF-VALIDAZIONE]] · `workflow/WF-VALIDAZIONE.md`
- [[WF-CORSO]] · `workflow/WF-CORSO.md`
- [[WF-EBOOK]] · `workflow/WF-EBOOK.md`
- [[IB-R1-PRODOTTO]] · `company/Ecosistemi/02-INFO-BUSINESS/Reparti/IB-R1-PRODOTTO.md` (base v1)
- [[MANDATO-EMPIRE]] · `company/Mandato/MANDATO-EMPIRE.md` (Art.2)
