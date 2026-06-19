---
Type: ENTITY
Status: Active
Tags: #reparto #infobusiness #prodotto #produzione #IB-L2-PROD
Created: 2026-06-18
Last updated: 2026-06-18
---

# IB-L2-PROD — Produzione Prodotti

> **Livello:** L2 — Area di 02-INFO-BUSINESS
> **Namespace AgentDB:** `infobusiness/prod`
> **Coordinator:** `IB-COORD-PRODOTTO` (Sonnet)
> **Roster:** 10 agenti · 3 workflow CF-grade
> **Missione-in-una-riga:** trasformare materiale raw già posseduto in prodotti finiti
> (ebook, corsi su piattaforma, guide, webinar) senza mai produrre senza validazione idea.

---

## Missione

IB-L2-PROD e il **cuore operativo** di 02-INFO-BUSINESS: trasforma materiale raw gia
posseduto (registrazioni, PDF, manuali, transcript in `Formazzione/`) in prodotti finiti
vendibili — ebook, corsi su piattaforma, guide, webinar recording. Il materiale grezzo non si
butta mai: si ingesta, si struttura, si valida, poi si produce.

Il v1 aveva un team di 4 funzioni (T-MKD, T-CURRICULUM, T-PIATTAFORMA, T-DESIGN-PRODOTTO)
senza QA dedicato. Il v2 porta l'area a **10 agenti con QA indipendente** (`IB-PROD-QA`),
validazione d'ingresso bloccante (`IB-PROD-VALID`) e un agente di apprendimento di processo
(`IB-PROD-LEARN`). La base v1 e wrappata, non riscritta (ADR-003): `IB-MKD-forger`,
`IB-CURRIC-designer`, `IB-PLATFORM-op` restano la fonte e sono referenziati dai loro
equivalenti v2 di area.

**Prodotti reali DE su cui l'area opera:** Manuale Claude Code (203 pagine, prototipo ebook),
Vendi la Skill (primo banco di prova WF-CORSO), Corso Skill Beast (pilota end-to-end).

---

## Posizione nella gerarchia

```
02-INFO-BUSINESS (L1) — IB-0-conductor
  └── IB-L2-PROD PRODUZIONE PRODOTTI ← questa area
        │
        ├── riceve da: IB-L2-STRA (backlog idee, brief prodotto da roadmap)
        ├── gate d'ingresso: IB-PROD-VALID (WF-VALIDAZIONE — score >=60 + MVP test)
        ├── coordina con: 03-CONTENT-FACTORY (script video → moduli video montati)
        ├── coordina con: PLATFORM (HC-PL-IB-01 → formazione-* su Supabase+Next.js)
        ├── consegna a: IB-L2-VEND (corso live + asset vendita → sales page, funnel)
        └── riporta a: IB-0-conductor (L1) per KPI settimanale ed escalation
```

---

## Roster agenti (10)

| ID | Agente | Tier | Ruolo sintetico |
|---|---|---|---|
| `IB-COORD-PRODOTTO` | Capo Area Prodotto | Sonnet | Coordinator: orchestra i 3 WF, priorita produzione, escalation a IB-0-conductor, KPI settimanale |
| `IB-PROD-QA` | Verificatore Prodotto | Sonnet | QA indipendente: 100% atomi fonte, outcome per lezione, smoke test; blocca, non suggerisce |
| `IB-PROD-VALID` | Product Idea Validator | Sonnet | WF-VALIDAZIONE: scoring /100 su 5 criteri, MVP test 7gg — gate d'ingresso dell'area |
| `IB-PROD-MKD` | MKD Forger | Sonnet | content-forge su cartella raw → MKD; log atomi coperti vs fonte (wrappa IB-MKD-forger) |
| `IB-PROD-CURRIC` | Curriculum Architect | Sonnet | MKD → moduli/lezioni con outcome misurabili, prerequisiti, durata (wrappa IB-CURRIC-designer) |
| `IB-PROD-WRITER` | Lesson Writer | Sonnet | Script lezioni/capitoli dal curriculum; voce DE; consegna a CONTENT-FACTORY per video |
| `IB-PROD-PLATFORM` | Platform Integrator | Sonnet | Coordina HC-PL-IB-01 verso PLATFORM; deploy Supabase+Next.js (wrappa IB-PLATFORM-op) |
| `IB-PROD-DESIGN` | Asset Designer | Sonnet | Copertine ebook, slide, workbook, certificato; brief a CONTENT-FACTORY per grafiche |
| `IB-PROD-EBOOK` | Ebook Specialist | Sonnet | Pipeline ebook: raw → MKD → capitoli → impaginazione → export PDF/ePub |
| `IB-PROD-LEARN` | Product Pattern Learner | Sonnet | Ogni ciclo → pattern: cosa rallenta, quale formato converte, difetti ricorrenti |

---

## Workflow CF-grade (3)

| Workflow | Scopo sintetico | File |
|---|---|---|
| `WF-VALIDAZIONE` | Gate d'ingresso: idea → scoring /100 su 5 criteri + MVP test 7gg → brief validato | `workflow/WF-VALIDAZIONE.md` |
| `WF-CORSO` | Raw → MKD → curriculum → lezioni → video (CF) → corso live su piattaforma | `workflow/WF-CORSO.md` |
| `WF-EBOOK` | Raw → MKD → capitoli → impaginazione → ebook PDF/ePub + pagina download | `workflow/WF-EBOOK.md` |

---

## Principi non negoziabili

1. Zero produzione senza gate WF-VALIDAZIONE passato (idea score >=60 + MVP test).
2. Il MKD copre il 100% degli atomi informativi della fonte: nessun contenuto si perde nella
   trasformazione (verifica quantitativa da parte del QA).
3. Ogni lezione ha 1 outcome verificabile e misurabile dichiarato; nessuna lezione teorica senza esercizio.
4. Il corso esiste sulla piattaforma reale prima di qualsiasi lancio: nessun lancio di ombre.

Dettaglio completo in `principi/PRINCIPI.md`.

---

## KPI presidiati

| KPI | Definizione |
|---|---|
| Lead time corso | Giorni da brief validato → corso live su piattaforma |
| % idee oltre gate validazione | n. idee con score >=60 + MVP test PASS / tot idee valutate |
| % gate QA al primo giro | n. gate QA PASS prima iterazione / tot gate (qualita a monte) |
| Difetti smoke test per corso | n. difetti trovati nello smoke test studente fantasma per corso |
| Rapporto espansione MKD | lunghezza MKD / lunghezza fonte (deve essere >=1, mai sintesi) |

Dettaglio e baseline in `kpi/KPI.md`.

---

## Handoff principali

| Direzione | Ecosistema/Reparto | Payload tipico |
|---|---|---|
| ← IB-L2-STRA | Strategia & Intelligence | brief idea prodotto da roadmap/backlog (input WF-VALIDAZIONE) |
| → 03-CONTENT-FACTORY | Content Factory | `HC-CF-IB-01`: script video → moduli video montati (MP4, audio >=44kHz, thumbnail) |
| → PLATFORM | Piattaforma | `HC-PL-IB-01`: curriculum + asset → corso su Supabase+Next.js (formazione-*) |
| → IB-L2-VEND | Vendite & Funnel | corso live + asset vendita preliminari → sales page, funnel evergreen |
| → IB-0-conductor | Conductor L1 | KPI settimanale, escalation gate falliti, blocco produzione |

**Regola handoff:** nessun prodotto entra in WF-CORSO o WF-EBOOK senza brief validato
(WF-VALIDAZIONE PASS). Se il brief non e validato → IB-PROD-VALID blocca, idea va in BACKLOG.

---

## Escalation

- **Gate QA fallito 2+ volte consecutive sullo stesso prodotto:** IB-PROD-QA non itera
  all'infinito → segnala a IB-COORD-PRODOTTO che riesamina brief/curriculum a monte.
- **Decisione Manuale Claude Code (lead magnet gratuito vs prodotto a pagamento):** ANCORA
  INDECISA → B-002 BACKLOG; la decisione spetta al team-prezzi (B-003, ADR-005). WF-EBOOK
  e pronto ma il routing verso funnel gratuito o a pagamento attende quella decisione.
- **Asset video mancanti da 03-CONTENT-FACTORY:** IB-PROD-PLATFORM blocca il deploy, segnala
  a IB-COORD-PRODOTTO; fallback delivery via link protetti (dichiarato nel dry-run).
- **Budget-guard (<20% risorse sessione):** IB-COORD-PRODOTTO chiude con COMMIT, non apre
  nuovi build (ADR-006).

---

## Connessioni

- [[02-ECOSISTEMA-INFOBUSINESS-V2]] · `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS-V2.md` §3 + §IB-L2-PROD
- [[ARCHITETTURA]] · `company/Ecosistemi/02-INFO-BUSINESS/Reparti/IB-L2-PROD-Produzione-Prodotti/ARCHITETTURA.md`
- [[IB-R1-PRODOTTO]] · `company/Ecosistemi/02-INFO-BUSINESS/Reparti/IB-R1-PRODOTTO.md` (base v1 wrappata)
- [[IB-MKD-forger]] · `company/Ecosistemi/02-INFO-BUSINESS/Agenti/IB-MKD-forger.md` (fonte v1)
- [[MANDATO-EMPIRE]] · `company/Mandato/MANDATO-EMPIRE.md` (Art.2 brand voice + prove non promesse)
