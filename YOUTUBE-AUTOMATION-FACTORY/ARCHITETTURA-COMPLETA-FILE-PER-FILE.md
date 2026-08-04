# ARCHITETTURA COMPLETA — YOUTUBE-AUTOMATION-FACTORY

> Mappa file-per-file di tutto il repository, generata il 2026-08-04 leggendo i file reali
> (docstring, header, contenuto), non i checkpoint. Per la storia/decisioni vedi
> `company/Memory/STATO-EMPIRE.md` (sezioni YOUTUBE-AUTOMATION-FACTORY) e i checkpoint
> `CP-20260728-*` → `CP-20260803-*`. Per la mappa concettuale ad agenti vedi
> [04-SKILLS-E-REFERENCE/ARCHITECTURE.md](04-SKILLS-E-REFERENCE/ARCHITECTURE.md) (complementare,
> non sostituita da questo file).

---

## ⚠️ Attenzione: DUE motori paralleli nello stesso repo

| | **Motore reale** (`02-AUTOMAZIONI-E-SCRIPTS/`) | **Scaffold nuovo** (`youtube_automation_factory/`) |
|---|---|---|
| Stato | ✅ Funzionante, testato, ha prodotto un video reale (Fliki) | ⚠️ Non installato, test falliscono (`pydantic_settings` mancante) |
| Stile | Script procedurali, uno per responsabilità | Package `src/`-layout, Pydantic v2, CLI `yaf`, pip-installabile |
| Fliki | Client reale (`fliki_client.py`, chiamate HTTP vere) | `FlikAdapter` astratto + `MockFlikAdapter`, **nessun client reale** (dichiarato nel README) |
| YouTube scraping | `youtube_hunter_playwright.py`, reale, testato su 36 video | `automation/youtube_playwright.py`, richiede selettori in config, mai eseguito qui |
| Test | `test_youtube_apex7.py`: **11/11 PASS** (verificato 2026-08-04) | `pytest`: **FALLISCE**, dipendenza mancante (verificato 2026-08-04) |
| Nato da | Task formale TASK-YT-001..007 (Gael, 07-28→08-03) | Commit `f4f50f22` "salvataggio lavoro in corso" (08-03), origine/scopo non documentati in un checkpoint dedicato |

Non sono la stessa cosa rifattorizzata: hanno modelli dati diversi, CLI diverse, stato di
maturità opposto. Prima di lavorarci, decidere quale dei due è la strada da seguire — oggi la
fabbrica *in uso* è quella in `02-AUTOMAZIONI-E-SCRIPTS/`.

---

## Struttura root

```
YOUTUBE-AUTOMATION-FACTORY/
├── .claude/                        configurazione permessi Claude Code (locale)
├── .env                            FLIKI_API_KEY (gitignored, aggiunto 2026-08-04)
├── README.md                       descrizione minima del repo
├── 01-FLUSSI-E-PIANI/              workflow narrativi (F1→F6) + storia refactor
├── 02-AUTOMAZIONI-E-SCRIPTS/       ★ MOTORE REALE — tutti gli script Python eseguibili
├── 03-AGENTI-E-RUOLI/              specifiche agenti (33, gerarchia 4 livelli)
├── 04-SKILLS-E-REFERENCE/          skill kernel + riferimenti tecnici (Fliki, SEO, script...)
├── 05-TEMPLATES-E-KIT/             template JSON/MD + output correnti (script, spec, metadati)
├── 06-DASHBOARD-E-METRICHE/        dashboard di stato scritta dal motore reale
├── memory/                         stato persistente del motore reale (decisioni, run, cache)
├── transcripts/                    transcript scaricati (sorgente per gli script adattati)
└── youtube_automation_factory/     ★ SCAFFOLD NUOVO — package pip-installabile, non finito
```

---

## `.claude/`
| File | Cosa fa |
|---|---|
| `settings.json` | Permessi/allowlist condivisi della sessione Claude Code per questa cartella |
| `settings.local.json` | Override locali non versionati per la stessa configurazione |

## Root
| File | Cosa fa |
|---|---|
| `.env` | `FLIKI_API_KEY` reale, copiata dal `.env` root del monorepo il 2026-08-04 per far funzionare `fliki_client.py` (che cerca solo qui, non nella root) — gitignorato |
| `README.md` | Descrizione minima, rimanda alle cartelle numerate |

---

## `01-FLUSSI-E-PIANI/` — workflow narrativi e storia
| File | Cosa fa |
|---|---|
| `WF1-niche-discovery.md` | Fase 1: scelta/validazione nicchia — oggi fissa su @dosementale |
| `WF2-video-selection.md` | Fase 2: selezione video da replicare, "il momento chiave" (gate ≥20 viste/ora) |
| `WF3-production.md` | Fasi 3+4: Script → spec Fliki multi-scena |
| `WF4-publish-seo.md` | Fase 5: metadati, tag, punteggio SEO |
| `WF5-performance-audit.md` | Fase 6: audit performance reale + feedback loop di auto-miglioramento |
| `implementation_plan.md` | Piano originale del refactor verso l'architettura APEX-7 |
| `session_chat_history.md` | Log della sessione di brainstorming del 24/07/2026 (origine del progetto) |

---

## `02-AUTOMAZIONI-E-SCRIPTS/` — ★ motore reale (5.478 righe totali)

### Orchestratore e motore APEX-7
| File | Righe | Cosa fa |
|---|---|---|
| `apex7_orchestrator.py` | 1315 | **Il cuore.** Classe `Apex7Orchestrator`: esegue le 6 fasi (`run_phase_1`…`run_phase_6`), gestisce stato/resume, scrive la dashboard. CLI: `run` (`--phase N` = fase **di arrivo**, non partenza! `--resume` continua da dove salvato), `status`, `memory`. |
| `agents.py` | 408 | Governo APEX-7 Swarm Agents & Conductor. Agenti Planner/Writer/Analyst/Critic/Refiner usati dall'orchestratore |
| `event_bus.py` | 57 | Event Bus Broker APEX-7 — comunicazione tra agenti |
| `memory.py` | 189 | Sistema di memoria a 5 livelli APEX-7 (working memory, decisioni, storico) |
| `meta_agent.py` | 90 | Meta-Agent Supervisor — supervisione del ciclo swarm |
| `gate_agent.py` | 118 | GATE-1 Agent — motore generico di gate a soglia |
| `quality_gate.py` | 141 | Quality Gate Engine — motore condiviso di controllo qualità |
| `ruflo_connector.py` | 35 | Connector verso l'API RuFLO (integrazione esterna dichiarata, non approfondita qui) |
| `conductor_auto.py` | 156 | Orchestratore idempotente alternativo/precedente (`APEX-7 YOUTUBE AUTOMATION CONDUCTOR`) |
| `run_youtube_apex7.py` | 99 | Runner E2E storico — **ritirato** (TASK-YT-005): pipeline fantasma su canale fisso mai collegata alle fasi reali F1-F6, lasciato per riferimento |

### Regolatori (L3 — bloccanti, eseguibili)
| File | Righe | Cosa fa |
|---|---|---|
| `regolatori.py` | 349 | **5 controlli eseguibili**: nicchia (termini fuori tema + CTA commerciali), originalità (n-grammi condivisi col transcript), copy (anglicismi/promesse mediche/emoji), configurazione (confronto campo-per-campo Fliki approvato), qualità (ffprobe sul file reale). Registro delle 3 firme in `memory/firme.json` (mai ancora popolato — nessuna run l'ha attraversato per intero con firme L1). |

### Ricerca / competitor
| File | Righe | Cosa fa |
|---|---|---|
| `youtube_hunter_playwright.py` | 249 | Scraping reale di YouTube via Playwright (profilo dedicato). Estrae titoli/viste per posizione, non per selettore CSS (i selettori storici `a#video-title-link` ecc. non esistono più) |
| `cashcow_check.py` | 131 | Indice Cash Cow (0-100) di un canale da un campione di video — informativo, non bloccante |
| `copy_study_dosementale.py` | 192 | Reparto COPY, agente `copy-researcher`: studia correlazione schema-titolo ↔ velocity, scrive lo studio nel second brain |

### Produzione (Fliki + copertine)
| File | Righe | Cosa fa |
|---|---|---|
| `fliki_client.py` | 312 | **Client reale** API Fliki Enterprise (`api.fliki.ai/v1`). Legge `produzione-spec.json` (F4) + script (F3), genera il video via API, fa polling stato. Cerca `FLIKI_API_KEY` in env poi in `.env` locale a questa cartella |
| `fliki_poll_only.py` | 66 | Rilancia il polling di un job Fliki già avviato, quando il client principale va in timeout ma il job è ancora vivo lato server |
| `fliki_subtitle_presets.py` | 78 | Estrae gli ID reali dei preset sottotitoli Fliki (non esposti da API/HTML — richiede clic reale su "Copy subtitle preset ID" via Playwright) |
| `fliki_youtube_test.py` | 13 | Script minimo di verifica presenza `FLIKI_API_KEY` — solo un check, non genera nulla |
| `arena_thumbnail.py` | 279 | Automazione Playwright reale di Arena.ai (ex LM Arena) per generare la copertina — profilo Chrome persistente, login umano una tantum |
| `thumbnail_analyzer.py` | 92 | Analisi colori/metriche di una copertina. Ha un ramo `analyze_real()` **e** un fallback `analyze_mock()`; anche il ramo "reale" ha l'estrazione colori dominanti dichiarata "mocked per semplicità" |

### Pubblicazione
| File | Righe | Cosa fa |
|---|---|---|
| `seo_score.py` | 200 | Punteggio SEO deterministico dei metadati (title/description/tags/thumbnail/subtitles) |
| `youtube_uploader.py` | 122 | Upload YouTube: `upload_mock()` sempre presente + `upload_real()` (OAuth `client_secrets`) con fallback automatico su mock se le credenziali mancano o la chiamata fallisce |
| `youtube_uploader_playwright.py` | 155 | Stessa logica ma via Playwright invece di API OAuth; fallback su mock identico |

### Qualità / auto-miglioramento / test
| File | Righe | Cosa fa |
|---|---|---|
| `validate_schemas.py` | 157 | Validazione manuale (no libreria JSON-schema) dei file `candidati-video.json`, `produzione-spec.json`, `brief-miniatura.json` |
| `self_improve.py` | 175 | Legge `memory/performance_logs.json`, calcola trend (CTR/retention/keyword), aggiorna `memory/learned_rules.json` |
| `test_youtube_apex7.py` | 300 | Suite di unit test del motore reale — **11/11 PASS** verificato 2026-08-04, nessuna rete richiesta |

---

## `03-AGENTI-E-RUOLI/` — 33 agenti su 4 livelli

`ORGANIGRAMMA.md` è il documento master. `conductor.md` = L0 (direttore di fabbrica, ex
"conductor": coordina i capi, non produce contenuti).

**Principio delle 3 firme**: operatore (L2) esegue → capo reparto (L1) approva → regolatore (L3)
non ha bloccato. Un blocco L3 non è appellabile dai capi né dal direttore — solo Gael deroga, e
la deroga va in memoria.

### L1 — Capi reparto (`capi/`) — *decidono*
| File | Reparto |
|---|---|
| `capo-ricerca.md` | RICERCA — cosa copiamo |
| `capo-copy.md` | COPY — cosa diciamo |
| `capo-produzione.md` | PRODUZIONE — come lo facciamo |
| `capo-strategia.md` | INTELLIGENCE — dove andiamo (**non può** cambiare la nicchia attiva, solo proporre a Gael) |

### L2 — Operatori (`operatori/`) — *eseguono*
| File | Fase/Reparto |
|---|---|
| `niche-scout.md` | Fase 1: scouting nicchia |
| `channel-scout.md` | Reparto INTELLIGENCE: scouting canali |
| `channel-performance-analyst.md` | Reparto INTELLIGENCE: performance canale |
| `competitor-analyst.md` | Reparto INTELLIGENCE: analisi competitor |
| `video-hunter.md` | Fase 2: selezione video (versione base) |
| `video-hunter-playwright.md` | Reparto RICERCA: selezione video via Playwright reale |
| `video-analyst.md` | Reparto RICERCA: analisi video |
| `transcript-collector.md` | Reparto RICERCA: raccolta transcript |
| `seo-analyst.md` | Fase 2: analisi SEO dei candidati |
| `script-writer.md` | Fase 3: scrittura script |
| `copy-researcher.md` | Reparto COPY: studio copy competitor |
| `title-writer.md` | Reparto COPY: titoli |
| `thumbnail-copywriter.md` | Reparto COPY: copy delle copertine |
| `video-producer.md` | Fase 4: produzione |
| `voice-caster.md` | Reparto PRODUZIONE: scelta voce |
| `thumbnail-designer.md` | Fase 5: design miniatura |
| `metadata-optimizer.md` | Fase 5: ottimizzazione metadati |

### L3 — Regolatori (`regolatori/`) — *bloccano, veto su tutti*
| File | Controllo |
|---|---|
| `regolatore-nicchia.md` | fuori tema / CTA commerciali |
| `regolatore-originalita.md` | copia verbatim dal transcript sorgente |
| `regolatore-copy.md` | anglicismi, promesse mediche, emoji |
| `regolatore-configurazione.md` | custodisce la configurazione Fliki approvata da Gael |
| `regolatore-qualita.md` | soglie tecniche (ffprobe) — **non** può bloccare per stile |

### Controllo (gate storici, pre-riorganizzazione — `controllo/`)
| File | Cosa fa |
|---|---|
| `niche-gate.md` | gate bloccante di nicchia |
| `qa-audio-video.md` | gate qualità audio/video |
| `seo-gate.md` | gate bloccante pre-pubblicazione |
| `performance-auditor.md` | Fase 6: audit + feedback |

### Supporto (`supporto/`)
| File | Cosa fa |
|---|---|
| `memory-keeper.md` | gestione memoria dal passo zero |
| `self-improver.md` | auto-miglioramento |

---

## `04-SKILLS-E-REFERENCE/` — skill kernel + riferimenti
| File | Cosa fa |
|---|---|
| `SKILL.md` | Skill kernel `youtube-automation-factory` |
| `ARCHITECTURE.md` | Mappa concettuale ad agenti (topologia 3 livelli MBA) — **complementare** a questo file, non sovrapposta: quella è per orientarsi tra agenti, questa è l'inventario di ogni file |
| `MKD.md` | Master Knowledge Document della fabbrica |
| `references/teoria-script.md` | Teoria dello script: Hook → Intro → CTA → SEO |
| `references/fliki-produzione.md` | Riferimento tecnico: produzione con Fliki (testo → video) |
| `references/fliki-avanzato.md` | Riferimento tecnico: SSML e pronunce avanzate su Fliki |
| `references/seo-certificazione.md` | SEO e certificazione di nicchia |
| `references/monetizzazione-compliance.md` | Linee guida monetizzazione YouTube e contenuto riutilizzato |
| `references/video-iq-analisi.md` | Analisi con Video IQ |

---

## `05-TEMPLATES-E-KIT/` — template e output correnti
| File | Cosa fa |
|---|---|
| `scheda-nicchia.md` | Template scheda nicchia |
| `script.md` | Template script |
| `candidati-video.json` | **Output corrente** F2: candidati video con SEO score (A-upside/B-sicurezza) |
| `produzione-spec.json` | **Output corrente** F4: spec Fliki multi-scena reale |
| `brief-miniatura.json` | **Output corrente** F5: brief copertina |
| `metadati.json` | **Output corrente** F5: titolo/descrizione/tag |
| `seo-report.json` | **Output corrente** F5: report punteggio SEO |
| `script-adattati/mkaNzHTBw1M.md` | Script riscritto integralmente (0% copiato, verificato — era al 21% prima della riscrittura, CP-20260803-003) |
| `source-thumbnail/dosementale-mkaNzHTBw1M-maxres.jpg` | Copertina originale del competitor, riferimento analitico |
| `copertina-arena-candidata-1.png` | Copertina generata via Arena.ai/Playwright |

---

## `06-DASHBOARD-E-METRICHE/`
| File | Cosa fa |
|---|---|
| `YOUTUBE-PERFORMANCE-DASHBOARD.md` | Scritta da `Apex7Orchestrator.write_dashboard()` a fine run, riflette lo stato REALE (PASS/FAIL veri per fase), non una tabella statica |

---

## `memory/` — stato persistente del motore reale
| File | Cosa fa |
|---|---|
| `decision_log.json` / `decision_log_archive.json` | Log storico di ogni decisione presa dall'orchestratore (gate, scelte) |
| `decisions/DEC-*.md` | Decisioni individuali storicizzate in Markdown (una per run/gate) |
| `runs/run_yt-*.json` | Stato salvato di ogni run (per `--resume`) |
| `channel_videos/dosementale.json`, `ciraolone.json` | Cache dei video reali scrapati per canale |
| `learned_rules.json` | Regole apprese da `self_improve.py` — azzerato 2026-07-31 (rimuoveva contaminazione dal vecchio funnel "claude code") |
| `performance_logs.json` | Log performance reali — **vuoto**, nessun video pubblicato ancora |
| `performance_logs.ARCHIVIO-MOCK.json` | Log FINTI del vecchio Conductor simulato — archiviati, non più letti |
| `strategy_store.json` | Strategie APEX-7 con tasso di successo (es. "Piramide Evolutiva", "Critique-Before-Output") |
| `architecture_snapshots.json` | Snapshot versione architetturale APEX-7 |
| `arena_thumbnail_status.json` | Ultimo stato dell'automazione copertina Arena |
| `fliki_subtitle_presets.json` | Cache preset sottotitoli Fliki con ID reali |
| `fliki_subtitle_page.png` | Screenshot della pagina preset Fliki (prova visiva) |
| `firme.json` | **Non ancora creato** — registro delle 3 firme di `regolatori.py`, nessuna run l'ha ancora popolato |

---

## `transcripts/`
| File | Cosa fa |
|---|---|
| `dosementale-mkaNzHTBw1M.it.vtt` / `.en.vtt` | Sottotitoli scaricati del video competitor (IT/EN) |
| `transcript_it.txt` / `transcript_en.txt` | Transcript in testo semplice, usati dal regolatore-originalità per il confronto n-grammi |

---

## `youtube_automation_factory/` — ★ scaffold nuovo (non installato)

Package Python standard (`src/` layout, `pyproject.toml`, CLI `yaf`). Vedi tabella di confronto
in cima al documento.

### Root package
| File | Cosa fa |
|---|---|
| `pyproject.toml` | Definizione pacchetto, dipendenze (`pydantic`, `pydantic-settings`, extra `dev`/`browser`) |
| `.env.example` | Template variabili `YAF_*`, nessun segreto |
| `README.md` | Documentazione d'uso, CLI, limitazioni dichiarate (vedi sezione dedicata sotto) |
| `config/settings.py` | Configurazione via env `YAF_*`/`.env`, mai costanti hardcoded |

### `docs/` (documentazione del package, non del repo)
| File | Cosa fa |
|---|---|
| `architecture.md` | Architettura interna del package |
| `workflow.md` | Macchina a stati del workflow |
| `agent_hierarchy.md` | Gerarchia agenti di questo package (parallela a quella in `03-AGENTI-E-RUOLI/`, non la stessa) |
| `approval_process.md` | Processo di approvazione |

### `src/youtube_automation_factory/core/` — dominio
| File | Cosa fa |
|---|---|
| `models.py` | Modelli Pydantic v2. Regole applicate nel modello: timestamp sempre UTC, asset nasce con `originality_checked=False` |
| `enums.py` | Stati workflow, livelli gerarchici, esiti |
| `exceptions.py` | Un'eccezione dedicata per ogni vincolo violato |
| `approvals.py` | `require_level()` — la gerarchia è applicata qui, non solo documentata |
| `workflow.py` | Macchina a stati: transizioni fuori mappa sollevano `InvalidTransitionError` e restano tracciate |
| `validators.py` | Funzioni pure di validazione, ritornano motivi di blocco, non modificano stato |
| `repositories.py` | Persistenza: implementazione in-memory (test) + JSON su file (CLI demo), dietro `Protocol` |
| `reporting.py` | Generazione report Markdown standardizzati |

### `src/youtube_automation_factory/agents/`
| File | Cosa fa |
|---|---|
| `base.py` | Classe base: ogni agente dichiara `level`, azioni riservate passano da `authorize()` |
| `senior_decision_agent.py` | Unico livello che approva riferimenti, script, nuove nicchie |
| `profitable_niche_agent.py` | Propone nicchie — **non può mai** cambiare `PRIMARY_NICHE` (vincolo in 3 punti: qui, nel modello, in approvals) |
| `niche_channel_scout_agent.py` | Ricerca altri canali dentro la nicchia primaria |
| `research_agent.py` | Agente operativo di ricerca |
| `competitor_analysis_agent.py` | Analisi competitor e performance canale |
| `review_agent.py` | Revisione completezza dati e pertinenza nicchia |
| `script_agent.py` | Brief editoriale e stesura script originale |
| `copywriting_agent.py` | Team copy: produce copy originale, lo manda in revisione |
| `production_agent.py` | Prepara il job di produzione solo per script approvati |
| `thumbnail_agent.py` | Brief copertina + generazione via Arena quando configurata |
| `regulatory_agent.py` | Trasversale, può bloccare; non produce né approva contenuti (separazione applicata da `approvals`) |

### `src/youtube_automation_factory/automation/` — integrazioni browser
| File | Cosa fa |
|---|---|
| `youtube_playwright.py` | Client YouTube: **nessun selettore hardcoded**, senza config solleva `AutomationNotConfiguredError` |
| `arena_playwright.py` | Client Arena: stessi confini, assenza non blocca il workflow |

### `src/youtube_automation_factory/integrations/` e `services/`
| File | Cosa fa |
|---|---|
| `integrations/flik_adapter.py` | Interfaccia astratta `FlikAdapter` + `MockFlikAdapter` — **nessun client HTTP reale** (dichiarato: nessuna API Flik verificata trovata) |
| `services/originality_service.py` | Checklist di **processo** (non certificazione legale): brief proprio presente, nessun flag copy-mode, nessuna derivazione dichiarata |

### `src/youtube_automation_factory/` root
| File | Cosa fa |
|---|---|
| `cli.py` | CLI `yaf`: `check-config`, `init-demo`, `run-demo`, `list-states`, `generate-report`, `validate-workflow`. Exit code 2 = blocco regolatorio |
| `demo.py` | Workflow dimostrativo end-to-end, solo dati locali e mock, nessuna rete |

### `tests/`
7 file (`test_approvals.py`, `test_automation_config.py`, `test_flik_adapter.py`, `test_models.py`,
`test_regulatory_agent.py`, `test_reporting.py`, `test_workflow.py`, `conftest.py`) — **non
eseguibili in questo ambiente**: `ModuleNotFoundError: No module named 'pydantic_settings'`
(dipendenza mai installata, verificato 2026-08-04).

---

## Limitazioni dichiarate nel proprio README (scaffold nuovo)
Dal README del package stesso, non da interpretazione:
- Flik non ha un client reale — solo interfaccia + mock.
- I selettori browser non sono forniti — l'automazione si rifiuta di partire senza.
- Nessun aggiramento di protezioni (login/CAPTCHA/accessi).
- CTR e retention dichiarati "dati mancanti", mai stimati.
- Il quality control verifica stati/coerenza, non la qualità percettiva del video prodotto.

## Cosa manca oggi (dal motore reale, non dallo scaffold)
- Nessun canale YouTube reale posseduto — va comprato già monetizzato (decisione Max/Gael).
- `memory/performance_logs.json` vuoto: F6/auto-miglioramento mai validati su un video davvero pubblicato.
- `memory/firme.json` non esiste: le firme L1 dei capi reparto non sono ancora imposte dal codice, solo i regolatori L3 bloccano davvero.
- Video "dopo-70-anni-v10-DEFINITIVO" citato come in generazione nell'ultimo checkpoint: nessun file locale trovato (Fliki è cloud, non scarica in automatico nel repo).
