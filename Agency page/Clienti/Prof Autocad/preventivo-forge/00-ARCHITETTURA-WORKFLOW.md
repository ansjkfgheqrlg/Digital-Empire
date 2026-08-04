---
Type: PROJECT
Status: Experimental
Tags: #workflow #multi-agente #automotive #mobile-de #pdf #CF-grade
Created: 2026-06-30
Last updated: 2026-06-30
Method: architect-agent (RBI) + content-forge (agenti 7-file) + master-build-architecture (swarm/memory)
---

# PreventivoForge — Architettura Workflow

> **Skill principale (regia):** `/preventivo-auto <url-mobile.de>` → avvia l'intera pipeline.
> **CLI equivalente:** `python run.py <url-mobile.de>`
> Codename interno: **PreventivoForge**. Cliente: **Prof Autocad** (vedi `../README.md`).

---

## FASE 1 — COMPRENSIONE (architect-agent)

- **Business value:** il concessionario importa auto dalla Germania. Oggi ricreare ogni
  annuncio (tradurre, riscrivere il copy, ricalcolare il prezzo, impaginare) è lavoro
  manuale lento. PreventivoForge lo rende **automatico**: 1 URL → 1 PDF pronto.
- **Utente finale:** il cliente (concessionario). Deve poter dare un link e ottenere il PDF.
  → Vincolo Max 2026-06-30: **deve girare completamente automatico** (consegna al cliente).
- **Sistemi esterni:** mobile.de (scraping, anti-bot forte), CDN immagini mobile.de.
  Nessun'API ufficiale → si usa **Playwright**.
- **Trigger:** manuale per ora (URL in input). Predisposto per batch/coda in futuro.
- **Output atteso:** `runs/<id>/preventivo_<marca-modello>.pdf` + `listing_it.json` + log.

---

## FASE 2 — PIANO

### 2.1 Workflow diagram

```
INPUT: URL annuncio mobile.de
  STEP 1  SCRAPING        op-scraper      → scraper.py      Tool: Playwright (headless+stealth, persistent ctx, retry)
                          Estrae __NEXT_DATA__/DOM + scarica TUTTE le foto.
                          OUT: runs/<id>/raw.json + runs/<id>/foto/*.jpg
  STEP 2  PARSING         op-parser       → parser.py       Tool: Python (json/regex)
                          Normalizza raw → schema canonico.
                          OUT: runs/<id>/listing.json   (== schema/listing.schema.json)
  GATE A  qa-extraction-verifier — foto tutte scaricate? campi obbligatori? prezzo numerico? → BLOCCA
  STEP 3  TRANSLATE+COPY  op-translator-copy → translate_copy.py  Tool: Claude (content-forge/copywriting) + glossario auto DE→IT
                          DE→IT fedele + copy migliorato (no invenzione fatti).
                          OUT: runs/<id>/listing_it.json
  GATE B  qa-translation-verifier — zero tedesco residuo? optional tradotti? numeri/specifiche invariati? tono ok?
  STEP 4  PRICING         op-pricer       → pricer.py       Tool: Python (deterministico)
                          prezzo_finale = round(prezzo_esposto×1.03 + 1500 + 1500); genera titolo.
                          OUT: aggiorna listing_it.json (price_final_eur, price_breakdown, final_title)
  GATE C  qa-price-verifier — ricalcola INDIPENDENTE, assert formula + formato titolo
  STEP 5  PDF RENDER      op-pdf-renderer → render_pdf.py   Tool: HTML template → PDF (WeasyPrint o Playwright print)
                          Foto embeddate LOCALI (no hotlink). Stile pulito/professionale.
                          OUT: runs/<id>/preventivo_<marca-modello>.pdf
  GATE D  qa-output-reviewer — tutte le sezioni? foto caricate? nessun placeholder? prezzo nel titolo?
OUTPUT: runs/<id>/preventivo_<marca-modello>.pdf
```

### 2.2 Analisi dei rischi

| Step | Cosa va storto | Gestione | Costo max |
|---|---|---|---|
| 1 | mobile.de blocca (anti-bot) | Playwright stealth + persistent context + UA realistico + retry/backoff; **FALLBACK manuale** (HTML salvato + cartella foto) | 0 (1 auto, retry) |
| 1 | foto CDN 403 | retry con header `Referer`; Gate A blocca se mancano | basso |
| 2 | prezzo "€ 28.900" mal parsato (punto migliaia) | parser robusto numeri DE; Gate C ricalcolo indipendente | nullo (gate) |
| 3 | terminologia auto sbagliata | glossario DE→IT (`Allrad`=integrale, `Schaltgetriebe`=cambio manuale, `Standheizung`=riscald. autonomo…) + Gate B | nullo (gate) |
| 3 | copy inventa optional non presenti | invariante "no invenzione fatti" (content-forge) + Gate B confronta con `equipment_de[]` | nullo (gate) |
| 5 | foto rotte nel PDF | embed locale dalle foto già scaricate, mai hotlink; Gate D | nullo (gate) |

### 2.3 Struttura file

```
preventivo-forge/
├── README.md                       # come si usa
├── 00-ARCHITETTURA-WORKFLOW.md     # questo doc (SPEC + piano + split)
├── CLAUDE.md                       # BRAIN (RBI): identità progetto + workflow attivi
├── .env.example  .gitignore  requirements.txt
├── run.py                          # CLI: python run.py <url>
├── schema/
│   ├── listing.schema.json         # 🔑 DATA CONTRACT (cucitura 50/50) — listing raw normalizzato
│   └── listing_it.schema.json      # listing arricchito IT (+prezzo, +titolo)
├── rules/  R1-scraping..R6-qa-gate # RULES (RBI): 1 md per stage, operabile a freddo
├── agents/                         # CF-grade, 7 file ciascuno
│   ├── CATALOG.md
│   ├── conductor/                  # regia del run (sequenza + gate + retry/fallback)
│   ├── operativi/  op-scraper · op-parser · op-translator-copy · op-pricer · op-pdf-renderer
│   └── verifica/   qa-extraction · qa-translation · qa-price · qa-output
├── implementation/  scraper.py parser.py translate_copy.py pricer.py render_pdf.py qa_gate.py
├── orchestration/   supervisor.md routing.md registry.json policies.md
├── templates/       annuncio.html  # template PDF pulito
├── runs/            <id>/ (raw.json, foto/, listing.json, listing_it.json, *.pdf, state.json, trace.jsonl)
└── logs/
```
Skill principale fuori dal progetto: `.claude/skills/preventivo-auto/SKILL.md` (la regia che lancia il workflow).

---

## FASE 3 — ARCHITETTURA RBI + TEAM (CF-grade)

### RULES (`rules/`) — RBI
Un file per stage (R1..R6). Ogni regola: OBIETTIVO · TRIGGER · INPUT (tabella) · OUTPUT ·
STEP-BY-STEP · TEMPLATE · GESTIONE ERRORI · CASI LIMITE · LOG. Operabile da un operatore
intermedio che non ha mai visto il sistema.

### BRAIN (`CLAUDE.md`)
Identità progetto + lista workflow attivi (trigger→file) + regole operative (self-healing,
sicurezza credenziali .env, logging) + naming.

### IMPLEMENTATION (`implementation/`)
Script Python: 1 cosa ciascuno, I/O dichiarati, credenziali solo da `.env`, try/except su ogni
operazione esterna, logging, docstring.

### TEAM — agenti CF-grade (7 file: `agent.md` + `system_prompt.md` + `tools.md` + `playbook.md` + `failure_modes.md` + `evals.md` + `memory.md`)

**Conductor (regia):** `conductor` — sequenzia gli stage, applica i 4 gate, gestisce retry/fallback, scrive `state.json`+`trace.jsonl`. È il cervello del run.

**Team OPERATIVO (fa il lavoro):**
| Agente | Stage | Script | Ruolo |
|---|---|---|---|
| `op-scraper` | 1 | scraper.py | guida Playwright, estrae dati+foto da mobile.de |
| `op-parser` | 2 | parser.py | normalizza raw → `listing.schema.json` |
| `op-translator-copy` | 3 | translate_copy.py | DE→IT + copy migliorato (content-forge/copywriting) |
| `op-pricer` | 4 | pricer.py | formula prezzo + titolo |
| `op-pdf-renderer` | 5 | render_pdf.py | HTML pulito → PDF con gallery |

**Team VERIFICA (controlla, blocca):**
| Agente | Gate | Controlla |
|---|---|---|
| `qa-extraction-verifier` | A | completezza estrazione (foto+campi+prezzo) |
| `qa-translation-verifier` | B | qualità/fedeltà traduzione, no DE residuo, no fatti inventati |
| `qa-price-verifier` | C | ricalcolo prezzo indipendente + formato titolo |
| `qa-output-reviewer` | D | PDF finale completo e corretto |

**Orchestration layer** (`orchestration/`): supervisor + routing + registry.json + policies (retry/escalation/budget).

---

## FASE 4 — FILE DI SUPPORTO
`.env.example` (no segreti hardcoded), `.gitignore` (`.env`, `runs/*/foto`, `__pycache__`, `*.pyc`,
sessioni browser), `requirements.txt` (playwright, beautifulsoup4, requests, weasyprint|playwright-print, pillow, jsonschema), `logs/`.

---

## FASE 5 — VALIDAZIONE (gate di fine build)
Dry-run mentale input→output coperto; ogni script referenzia solo var del `.env`; ogni regola
mappa uno script esistente; `CLAUDE.md` elenca tutti i workflow; agenti = 7 file 0 stub;
`listing.json` valida contro schema; test end-to-end su 1 URL reale (l'annuncio Mercedes GLA fornito).

---

## 🔑 DATA CONTRACT — la cucitura del 50/50
`schema/listing.schema.json` (raw normalizzato) e `schema/listing_it.schema.json` (arricchito IT)
sono il **confine** tra le due metà. **Max li definisce e li congela**; entrambe le metà li rispettano.
Half A produce `listing.json`; Half B lo consuma e produce `listing_it.json` → PDF.

## 👥 SPLIT 50/50 (Max ↔ Gael)
**MAX — Half A «Acquisizione · Dati · Regia»**
- STEP 1 scraper · STEP 2 parser · STEP 4 pricer
- conductor + orchestration + `run.py` + `schema/` (data contract) + `.env`/`requirements`/`.gitignore`
- regole R1, R2, R4 · **skill principale `preventivo-auto`**

**GAEL — Half B «Contenuto · Output · Qualità»**
- STEP 3 translate+copy (content-forge/copywriting/cro-copy-architect) · STEP 5 PDF renderer + `templates/annuncio.html`
- **tutti e 4** gli agenti QA + `qa_gate.py`
- regole R3, R5, R6

Seam congelato = `listing.schema.json`. Coordinamento in `company/Memory/STATO-EMPIRE.md`.

## 🛠 Skill/motori usati (selezione)
`architect-agent` (architettura, questo doc) · `content-forge` (agenti 7-file + motore copy) ·
`master-build-architecture` (swarm/memory ref) · `copywriting` + `cro-copy-architect` + `copy-editing` (STEP 3) ·
`playwright-dev` (STEP 1) · `verification-quality` + `agent-reviewer` + `agent-tester` (QA + test) ·
`sparc-methodology` + `agent-planner` (metodo) · `swarm-orchestration` (se build in swarm).
