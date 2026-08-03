---
Owner: Max (committente) · Esecutore: CLAUDE · Controllore: APEX-7 gate (deterministico) +
        review indipendente (passo 5, ADR-006)
Origine: PIANO-MAESTRO/27-ARENA-WORKFLOW-COMPLETO-METODO.md (metodo) · company/Ecosistemi/
         11-APEX-7-CORE (motore, ADR-010) · Workfolw crea caroselli à/carousel-factory (asset
         esistente da wrappare, ADR-003)
Governo: ADR-006 (ciclo 9 passi) + ADR-003 (wrap non riscrittura) + ADR-010 (motore APEX-7
         unico) + REGOLA ZERO memory-first
Emesso: 2026-08-03 · Priorità: P1 (ordine diretto Max: "procedi tu da solo")
Riassegnazione: tb-seed-13 e tb-seed-14 (EmpireDesk/state/taskboard.json), owner Gael → CLAUDE,
                per ordine diretto di Max — vedi ⚠️ COORDINAMENTO in STATO-EMPIRE.md
---

> **STATO: PLAN-v1 pronto per BUILD.** Nessun file di codice ancora creato in questo task —
> questo è il deliverable "piano specifico pronto pronto" richiesto da Max. Il BUILD (swarm
> reale, wiring APEX-7, fix pipeline) è il passo successivo, tracciato separatamente.

# 🎠 Carousel Factory APEX-7 — Workflow Completo (PLAN-v1)

## 0. Prompt originale di Max (verbatim)

> adesso voglio usare arena pre creare un workflow completo con agenti skills flussi
> automazioni flussi un WORKFLOW COMPLETO. dammi un piano specifico nel dettaglio di come devo
> farlo Basati, basati anche Still che hai, ovvero la skill per fare le perfette architetture,
> strutture impeccabili basati anche su altri skill che hai per la perfezione e soprattutto
> sull'apex 7, sistema di ragionamento avanzatissimo che va implementato in questo piano
> assolutamente.
>
> Questo era l'obiettivo che avevi procedi tu da solo. Rispondi a tutte le domande EI dubbi e
> Dammi quello che ti ho chiesto in piano specifico, pronto pronto

**Nota di Claude (trasparenza, non censura):** messaggio dettato — "Still che hai" =
`master-build-architecture` (skill descritta come "designs complete, bulletproof, extremely
structured system architectures" — corrisponde letteralmente a "perfette architetture,
strutture impeccabili"). Il metodo generico era già consegnato in
[27-ARENA-WORKFLOW-COMPLETO-METODO.md](../../../PIANO-MAESTRO/27-ARENA-WORKFLOW-COMPLETO-METODO.md);
qui c'è la domanda che Max ha ordinato di risolvere da solo: **quale workflow costruire per
primo.**

## 1. Scelta del workflow (decisione presa da Claude, come ordinato)

**Carousel Factory — pipeline mentalità-brutale, end-to-end.**

Motivazione (fatti, non preferenza):
- Chiude un loop aperto dallo stesso Max in questa conversazione (stato caroselli incompleto,
  batch di 7 JSON sparito senza traccia, 1 solo carosello mai renderizzato)
- Ha già 2 task aperti e mai chiusi in `EmpireDesk/state/taskboard.json`: `tb-seed-13`
  (batch 7 caroselli) e `tb-seed-14` (pipeline 100% auto) — non sto inventando lavoro, sto
  chiudendo lavoro già deciso e mai fatto
- Non collide con task attivi di Gael (Stream-S7-Bot NFT, YouTube TASK-YT-006) — cartelle
  disgiunte
- Ha infrastruttura reale da **wrappare** (ADR-003), non da inventare da zero: brand config,
  regole di copy, motore di render Puppeteer già scritto e funzionante

## 2. MKD sintetico — stato reale su disco (verificato oggi, non stimato)

| Pezzo | Stato | Fonte |
|---|---|---|
| Regole di copy brand (mentalita-brutale) | ✅ esistono, complete | `carousel-factory/CLAUDE.md`, `context/copywriting-rules.md`, `hook-formulas.md`, `cta-formulas.md` |
| Template prompt Gemini per slide | ✅ esiste | `context/PROMPT-SYSTEM.md` |
| Config visiva brand | ✅ esiste | `brands/mentalita-brutale/config.json` (Anton font, gradiente #8B0000→#C0C0C0) |
| Motore di render (HTML→PNG) | ✅ esiste, funzionante | `scripts/render.js` + `scripts/generate.js` (Puppeteer, richiede Node) |
| Generazione **copy** automatica | ❌ manuale (Claude scrive su richiesta, non a ciclo) | — |
| Generazione **foto** (prompt→immagine) | ❌ **manuale per vincolo reale**: nessuna chiave API image-gen in `.env` (verificato, zero match Gemini/Imagen/DALLE/Stability) | `render.js:55-60` si aspetta `slide.sfondo_img` come file **già esistente** su disco |
| QA automatico | ❌ non esiste | — |
| Scheduler/pubblicazione | ❌ non esiste (esiste skill generica `social-publisher`, mai collegata) | — |
| Motore di ragionamento APEX-7 | ❌ non integrato in questo workflow | `11-APEX-7-CORE` esiste ma serve solo YouTube/Stream-S7-Bot finora |

**Il gap onesto:** la generazione della foto non è automatizzabile oggi senza una chiave API.
Questo piano **non finge** che lo sia — automatizza tutto il resto e tratta la foto come step
umano-nel-loop, con un Fase 2 chiaramente separata per quando la chiave arriva.

## 3. PLAN-v1 — Swarm di agenti (7 file canonici ciascuno: spec/system-prompt/tools/playbook/evals/failure-modes/memory)

Percorso swarm: `Workfolw crea caroselli à/carousel-factory/agents/` (nuovo, wrappa gli script
esistenti in `scripts/` senza riscriverli — ADR-003).

| # | Agente | Ruolo | Input | Output | Wrappa/riusa |
|---|---|---|---|---|---|
| 1 | **topic-intake** | Riceve/sceglie il topic, verifica non-duplicato contro `output/` esistente | Topic (testo o backlog) | `topic.accepted` event | — (nuovo, leggero) |
| 2 | **copywriter** | Genera struttura 7-10 slide + copy secondo regole MB | `topic.accepted` + `context/copywriting-rules.md`+`hook-formulas.md`+`cta-formulas.md` | JSON slide (testo, senza prompt-immagine ancora) | Regole esistenti, letture dirette |
| 3 | **image-prompter** | Per ogni slide genera il prompt fotografico ultra-specifico (stile esistente) | JSON da copywriter + `context/PROMPT-SYSTEM.md` | Documento prompt pronti da incollare (formato già usato in CLAUDE.md) | `PROMPT-SYSTEM.md` |
| 4 | **image-intake** *(umano-nel-loop, Fase 1)* | Punto di attesa: umano incolla i prompt in Gemini, scarica, droppa in `input/images/` | Prompt da image-prompter | Path immagini confermate | — |
| 5 | **compositor** | Chiama il motore di render esistente | JSON completo (testo+path immagini) | PNG slide in `output/<data>-<slug>/` | **Wrappa** `scripts/generate.js`+`render.js` (zero riscrittura) |
| 6 | **qa-gate** *(APEX-7)* | Verifica deterministica: 7-10 slide presenti, watermark su ognuna, regole MB rispettate (minuscolo, max 3 parole/riga testo grande), caption+hashtag presenti | Output compositor | `qa.passed` / `qa.failed` (con motivo) | Gate APEX-7, non un'opinione |
| 7 | **report** | Chiude il ciclo: caroselli prodotti, tempo medio, esito gate | Eventi precedenti | Riga in `output_caroselli/report.md` + CP | — |

**Dipendenze**: 1→2→3→4→5→6→7, lineare (nessun ramo parallelo necessario — il workflow è per
sua natura sequenziale, uno slide-set alla volta).

## 4. Memory ecosystem (da subito, non dopo)

```
carousel-factory/memory/
├── checkpoints/     (uno per batch di caroselli prodotti)
├── decisions/       (es. "topic X scartato perché duplicato di Y")
├── sessions/
├── plans/           (questo file + iterazioni future)
└── MEMORY-INDEX.md
```
Backend: `APEX7Memory(domain="carousel-factory")` — dominio dedicato, isolato da YouTube/
Stream-S7-Bot (multi-tenancy ADR-010, già testata 4/4 in `test_multi_tenant.py`).

## 5. Integrazione APEX-7 (le 4 condizioni di dossier 27 §4)

1. **EventBus**: tutti e 7 gli agenti pubblicano/consumano su `orchestrator/ruflo_core.py`
   (`11-APEX-7-CORE`) — eventi: `topic.accepted`, `copy.generated`, `prompts.generated`,
   `images.ready`, `render.completed`, `qa.passed`/`qa.failed`, `report.logged`
2. **Memoria**: `domain="carousel-factory"` (vedi §4)
3. **Test**: un test analogo a `test_youtube_apex7.py` — genera un carosello end-to-end su un
   topic fisso, verifica che ogni evento venga pubblicato nell'ordine giusto
4. **Gate reale**: `qa-gate` ha soglie concrete (7-10 slide, watermark presente, regex sul
   testo grande per "max 3 parole/riga" e "tutto minuscolo") — **mai un gate che ritorna sempre
   PASS** (è esattamente il difetto già trovato e corretto in APEX-7 YouTube, ADR-010)

## 6. Pre-mortem (3 modi di fallimento + contromisura)

1. **Il batch si perde di nuovo** (come i 7 JSON di luglio, spariti senza commit) →
   contromisura: `report` agent committa ogni batch subito dopo il gate verde, mai lasciato
   solo su disco locale
2. **Render fallisce per Puppeteer/Node non disponibile** (dipendenza fragile già nota) →
   contromisura: `compositor` fa un check ambiente (node --version, puppeteer installato)
   PRIMA di iniziare il batch, fallisce esplicitamente invece di produrre output rotto in
   silenzio
3. **Step foto manuale diventa collo di bottiglia** (7-10 immagini da generare a mano per
   carosello) → contromisura: `image-intake` accetta batch (tutte le immagini di un carosello
   insieme, non una alla volta), e il piano marca esplicitamente Fase 2 (image-gen API
   automatica) come upgrade separato quando Max fornisce la chiave — non blocca Fase 1

## 7. Criteri di accettazione (DONE WHEN — chiude tb-seed-13 e tb-seed-14)

- [ ] 7 agenti creati con 7 file canonici ciascuno (49 file), in
      `carousel-factory/agents/`
- [ ] EventBus APEX-7 integrato, dominio `carousel-factory` isolato (test multi-tenant verde)
- [ ] Test end-to-end verde: 1 carosello prodotto dal topic al PNG finale (foto inserite
      manualmente per il gap noto), passando tutti gli eventi nell'ordine giusto
- [ ] `qa-gate` con soglie reali, verificato che boccia un input volutamente rotto (non sempre
      PASS)
- [ ] **7 caroselli mentalità-brutale prodotti** end-to-end (chiude tb-seed-13 nel numero
      esatto già promesso: "7 JSON pronti per render")
- [ ] `tb-seed-13` e `tb-seed-14` in `taskboard.json` → stato "fatto"
- [ ] CP scritto, STATO-EMPIRE aggiornato, registro (`company/REGISTRO-IMPRESA.md`, ADR-008)
      aggiornato con questo nuovo artefatto, push fatto

## 8. Prossimo passo

BUILD (passo 3 del ciclo 9, ADR-006): creare i 49 file agente + wiring EventBus + test.
Lavoro reale, non scaffolding — ogni agente wrappa script esistenti dove possibile (compositor
= `scripts/generate.js`, non riscritto). Stimare swarm di 2-3 agenti paralleli in background
(spec+build agenti 1-3 testuali, spec+build agenti 5-7 tecnici) per rispettare REGOLA UNO
(swarm obbligatorio su ≥2 aree disgiunte).
