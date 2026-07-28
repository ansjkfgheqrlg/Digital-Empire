---
Owner: Max (committente) · Esecutore: GAEL · Controllore: Claude (gate APEX-7)
Origine: YOUTUBE-AUTOMATION-FACTORY · Governo: ADR-006 (ciclo 9 passi) + ADR-010 (fusione Ruflo+APEX-7-CORE) + REGOLA ZERO memory-first
Emesso: 2026-07-28 · Priorità: P1 (TASK-YT-001..005), P2 (TASK-YT-006..007)
Riferimenti: CP-20260728-001 (fusione Ruflo+APEX-7 fase 1 pilota) · ADR-010 ·
             company/Memory/STATO-EMPIRE.md (blocco COORDINAMENTO 2026-07-28) ·
             YOUTUBE-AUTOMATION-FACTORY/01-FLUSSI-E-PIANI/implementation_plan.md ·
             YOUTUBE-AUTOMATION-FACTORY/02-AUTOMAZIONI-E-SCRIPTS/test_youtube_apex7.py
---

# 🚨 ORDINE MAX — GAEL: chiudi la fabbrica YouTube, F4-F6 sono ancora finti

## 0. Perché (leggi, sono 10 righe, ti risparmiano un giorno)

F1 Scouting, F2 Selezione, F3 Script sono già reali (dati veri: niche-scout Gemini, video live
da YouTube, 20 idee pre-scritte). F4, F5, F6 e la Dashboard scrivono ancora dati hardcoded
indipendentemente dall'input reale delle fasi precedenti — la fabbrica non ha mai prodotto un
video reale. Claude ha già patchato `execute_critic` (punteggio reale su contenuto invece di
dict fisso 8.5/8.0/7.5/8.0/9.0) come fix interinale, backward-compatible, `test_youtube_apex7.py`
11/11 verde. Non è il retrofit architetturale pianificato in ADR-010 (motore condiviso
`11-APEX-7-CORE`) — quello resta tuo (TASK-YT-001).

Verifica subito che il terreno sia solido:
```bash
cd "<radice monorepo>/YOUTUBE-AUTOMATION-FACTORY/02-AUTOMAZIONI-E-SCRIPTS"
python -m unittest test_youtube_apex7 -v   # deve dare "OK", 11/11 test verdi
```
Se non dà 11/11 verde: `git pull`, il task non è arrivato integro.

---

## 1. Cosa è già fatto e NON devi rifare

| Fase | File / metodo | Stato |
|---|---|---|
| F1 Scouting | `apex7_orchestrator.py::run_phase_1` (riga ~541) | ✅ reale — 20 canali veri, niche-gate bloccante con retry |
| F2 Selezione | `run_phase_2` (riga ~636) | ✅ reale — video live fetch YouTube, cache 7gg |
| F3 Script | `run_phase_3` (riga ~722) | ✅ reale — 20 idee vere Gemini, hook/CTA verbatim |
| Critic (patch interinale) | `execute_critic` (riga ~374) | ✅ reale (locale) — non più dict fisso, ma NON ancora sul motore condiviso |

**FILE CONGELATI** (motore condiviso, fondazione APEX-7 empire-wide — vedi ADR-010):
`company/Ecosistemi/11-APEX-7-CORE/memory/memory_system.py` (`APEX7Memory(domain=...)`),
`company/Ecosistemi/11-APEX-7-CORE/orchestrator/ruflo_core.py` (`RuFLOOrchestrator(domain=...)`).
Puoi **usarli** (istanziare con `domain="youtube"`), non rinominare/cambiare firme senza nota
`⚠️ COORDINAMENTO` in `company/Memory/STATO-EMPIRE.md` + push.

---

## 2. I TUOI 7 LOTTI (ID stabili, usali nei commit/CP)

### 🟣 TASK-YT-001 — Retrofit critic + agenti su motore condiviso (P1, sblocca coerenza architetturale)

`execute_critic` (patch interinale mia) e `agents.py` (hardcoded) vanno collegati al motore
condiviso `11-APEX-7-CORE`, come da ADR-010 (fusione Ruflo+APEX-7-CORE, pilota YouTube+Stream-S7-Bot).

- Istanzia `RuFLOOrchestrator(domain="youtube")` / `APEX7Memory(domain="youtube")` dentro
  `Apex7Orchestrator` (o come layer che lo avvolge)
- Il punteggio critic può restare la logica reale già scritta (lunghezza/sezioni/keyword
  density/CTA) — quello che cambia è che deve passare/persistere attraverso il motore condiviso,
  non restare locale al file YouTube
- Mantieni i call-site già aggiornati in F3 (passa il testo reale dello script, non il titolo)

**Gate TASK-YT-001**: `test_youtube_apex7.py` 11/11 verde dopo il retrofit. Incolla output
`python -m unittest test_youtube_apex7 -v`. Se il motore condiviso non espone ancora un'API
adatta al critic, documenta esattamente cosa manca in `11-APEX-7-CORE` invece di aggirarlo.

### 🟣 TASK-YT-002 — F4 Produzione: spec Fliki reale (P1)

`run_phase_4` (riga ~809) scrive sempre `scene_count: 5` con **1 sola scena reale**
(`"Vuoi installare l'agente IA più veloce?"`), indipendentemente dallo script scritto in F3.

- Leggi `working_memory["script_path"]` (script.md reale di F3) e parsa le sezioni HOOK/INTRO/
  CORPO/CTA in scene multiple (una spec Fliki con più `scenes`, non 1 fissa)
- `video_id`/`title` presi da `working_memory["script_idea_title"]` (reale, cambia per run), non
  hardcoded "claude-code-001"/"Installare Claude Code locale"
- `hook_type` da `working_memory["script_idea_hook_type"]` (già salvato da F3)

**Gate TASK-YT-002**: fai girare F1→F4 due volte con due candidati diversi (o due topic) →
`produzione-spec.json` deve avere `scene_count` e testo scene diversi tra le due run. Schema
`validate_schemas.py produzione-spec` deve restare PASS. Incolla i due JSON a confronto.

### 🟣 TASK-YT-003 — F5 Pubblicazione: metadati reali (P1)

`run_phase_5` (riga ~836) scrive sempre lo stesso titolo/tag ("Installare Claude Code locale",
`["claude code", "antigravity", "digital empire"]`) indipendentemente dal video/script reali.

- Titolo da `working_memory["script_idea_title"]`
- Descrizione costruita da contenuto reale dello script (non placeholder "Ecco come installare...")
- Tag da `learned_rules.json["high_performing_tags"]` + eventuale cluster/niche reale di F1
- `brief-miniatura.json`: `concept`/`text_overlay` derivati dall'HOOK reale dello script, non fissi

**Gate TASK-YT-003**: due run con video/idee diversi → `metadati.json` con titolo/tag diversi.
`seo_score.py` sul metadati reale deve restare `pass_soglia_70: true` (o la fase deve gestire
onestamente il caso sotto soglia, non ignorarlo). Incolla output `seo_score.py --json metadati.json`.

### 🟣 TASK-YT-004 — F6 Audit: gate onesto, niente metriche finte (P1)

`run_phase_6` (riga ~868) scrive sempre `views_per_hour: 35.5` fisso in `performance_logs.json`
— il self-improver impara su rumore inventato, non su performance vere.

- Crea/leggi manifest `memory/published_videos.json`: video REALMENTE pubblicati per una run
  (`run_id`, `video_id`, `url`, `published_at`)
- Se **nessuna voce reale** per la run corrente: F6 ritorna `True` **senza** appendere nulla a
  `performance_logs.json` (non è un errore — significa "non ancora pubblicato")
- Se la voce esiste e `published_at` è abbastanza vecchio (proponi soglia, es. ≥24h): calcola
  `views_per_hour` reale (stesso pattern di fetch pubblico usato in F2, `_fetch_channel_videos_live`)
  invece di inventarlo
- Se la voce esiste ma è troppo recente: log onesto "troppo presto per audit reale", nessuna scrittura

**Gate TASK-YT-004**: (a) run senza manifest → `performance_logs.json` invariato (conta le righe
prima/dopo, incolla il diff — deve essere zero); (b) run con manifest e video reale pubblicato da
te (o da Max) → riga nuova con numeri reali, non `35.5`. Incolla entrambi i casi.

### 🟣 TASK-YT-005 — Dashboard: stato reale della run (P1)

`06-DASHBOARD-E-METRICHE/YOUTUBE-PERFORMANCE-DASHBOARD.md` oggi è scritta SOLO da
`run_youtube_apex7.py` (pipeline separata, fake, hardcoded su canale "Dose Mentale", sempre
tutte e 6 le fasi 🟢 PASS a prescindere).

- Aggiungi un metodo (es. `write_dashboard()`) dentro `Apex7Orchestrator`, chiamato a fine
  `execute_workflow`, che scrive la dashboard leggendo `self.working_memory` reale della run
  corrente (canale scelto, video scelto, esito vero di ogni gate — PASS o FAIL, non sempre PASS)
- Decidi (e documenta la decisione nel checkpoint) se `run_youtube_apex7.py` va ritirato o
  riallineato: oggi è un percorso fantasma che non usa nessuno dei fix reali di F1-F3

**Gate TASK-YT-005**: forza un fallimento reale (es. topic che fa fallire il niche-gate su tutti
i 20 canali, già supportato da F1) → la dashboard deve mostrare 🔴 FAIL su quella fase, non 🟢
PASS. Incolla la dashboard generata nel caso FAIL e nel caso PASS.

### 🟣 TASK-YT-006 — Ritiro reimplementazione APEX-7 indipendente in 12-STREAM-S7-BOT (P2, cross-ecosistema)

Da CP-20260728-001: 4 implementazioni APEX-7-shaped divergenti trovate (YouTube, skill generica,
`11-APEX-7-CORE`, `12-STREAM-S7-BOT`). Questa è quella dentro Stream-S7-Bot — **non correlata al
dominio trading** dei tuoi lotti G-A/G-B/G-C su quell'ecosistema (`TASK-GAEL-20260728-STREAM-S7-BOT.md`),
è pulizia architetturale a valle della fusione Ruflo+APEX-7-CORE. Bassa priorità, non bloccante:
fallo dopo TASK-YT-001..005, quando hai già visto come si collega il motore condiviso in pratica.

**Gate TASK-YT-006**: `company/Ecosistemi/12-STREAM-S7-BOT/test_apex7.py` resta 9/9 verde dopo
la migrazione dei file APEX-7 generici (event_bus/memory_interface/quality_gates/gate_agent/
meta_agent/orchestrator) verso il motore condiviso, o motivazione scritta se decidi di non farlo
in questo giro.

### 🟣 TASK-YT-007 — Documentazione a valle del retrofit (P2)

Aggiorna `company/REGISTRO-IMPRESA.md` e `PIANO-MAESTRO/07-BACKBONE-RUFLO-SKILLS.md` per
riflettere lo stato reale dopo TASK-YT-001..006 (motore condiviso in uso su YouTube, fabbrica
end-to-end reale o stato preciso di cosa resta finto).

**Gate TASK-YT-007**: entrambi i file citano esplicitamente `11-APEX-7-CORE` come motore
condiviso YouTube+Stream-S7-Bot e lo stato vero (non aspirazionale) delle 6 fasi.

---

## 3. Perimetro — cosa NON tocchi senza coordinamento

| Area | Di chi è |
|---|---|
| `company/Ecosistemi/11-APEX-7-CORE/**` | Claude — motore condiviso, puoi usarlo non rinominarlo |
| `12-STREAM-S7-BOT/analysis_engine.py`, `risk_manager.py`, `execution_engine.py`, `position_monitor.py` | Tuoi ma su un TASK diverso (`TASK-GAEL-20260728-STREAM-S7-BOT.md`) — non mischiare i due task nello stesso commit |
| **Tuo, in esclusiva su questo task** | `YOUTUBE-AUTOMATION-FACTORY/02-AUTOMAZIONI-E-SCRIPTS/apex7_orchestrator.py`, `agents.py`, `run_youtube_apex7.py`, `06-DASHBOARD-E-METRICHE/YOUTUBE-PERFORMANCE-DASHBOARD.md` |

---

## 4. Regole operative

1. **Prova, non dichiarazione**: nel checkpoint incolli comando + output reale per ogni gate.
2. **Windows-first**: zero emoji nei `print()` nuovi se toccano path già afflitti da crash cp1252
   (verifica: il file ha già un guard UTF-8 in testa, non aggiungerne un secondo).
3. **ADR-006 ciclo a 9 passi** per ogni lotto: RECALL → SPEC → PRE-MORTEM → BUILD → GATE →
   REVIEW → TEST → COMMIT → RETRO.
4. Prima di ogni lotto e dopo: `python -m unittest test_youtube_apex7 -v` deve restare verde
   (11/11). Se lo rompi, non committi finché non torna verde.
5. **Task chiuso → checkpoint** in `company/Memory/checkpoints/CP-20260728-NNN.md` — prendi il
   primo numero libero al momento in cui parti (oggi liberi da `CP-20260728-006`).
6. **Ogni lotto chiuso → aggiorna lo `stato` in `EmpireDesk/state/taskboard.json`** per il suo
   ID (`TASK-YT-00N`) da `da_fare` a `fatto`, con `note` = riassunto + riferimento al checkpoint.
7. **Item minori → `company/Memory/BACKLOG.md`** (ADR-005), non fermare la costruzione.

---

## 5. Definition of Done complessiva

- [ ] TASK-YT-001: critic+agenti sul motore condiviso `11-APEX-7-CORE`, 11/11 test verdi
- [ ] TASK-YT-002: F4 genera spec Fliki multi-scena reale, diversa per run diverse
- [ ] TASK-YT-003: F5 genera metadati/tag/titolo reali, diversi per run diverse
- [ ] TASK-YT-004: F6 non scrive mai metriche finte; manifest `published_videos.json` funzionante
- [ ] TASK-YT-005: dashboard riflette l'esito vero (PASS/FAIL) di ogni gate della run corrente
- [ ] TASK-YT-006: reimplementazione APEX-7 duplicata in Stream-S7-Bot ritirata o motivata
- [ ] TASK-YT-007: `REGISTRO-IMPRESA.md` + dossier 07 aggiornati allo stato reale
- [ ] `python -m unittest test_youtube_apex7 -v` verde (11/11) a fine lavoro
- [ ] checkpoint con comandi e output reali incollati per ogni gate

---

## 6. Ordine di marcia

1. `git pull` → verifica `test_youtube_apex7.py` 11/11 verde prima di toccare qualunque cosa
2. **TASK-YT-001** (motore condiviso) → gate → commit → taskboard aggiornata
3. **TASK-YT-002** (F4) → gate → commit → taskboard aggiornata
4. **TASK-YT-003** (F5) → gate → commit → taskboard aggiornata
5. **TASK-YT-004** (F6) → gate → commit → taskboard aggiornata
6. **TASK-YT-005** (Dashboard) → gate → commit → taskboard aggiornata
7. **TASK-YT-006** (ritiro doppione Stream-S7-Bot) → gate → commit → taskboard aggiornata
8. **TASK-YT-007** (docs) → commit → taskboard aggiornata
9. checkpoint consolidato + RETRO + push

**Se qualcosa non torna** (un formato dati imprevisto, il motore condiviso non espone ancora
quello che serve, una collisione): **non indovinare**. Scrivi il problema con **comando esatto +
errore esatto** in `STATO-EMPIRE.md` e prosegui sul lotto successivo.
