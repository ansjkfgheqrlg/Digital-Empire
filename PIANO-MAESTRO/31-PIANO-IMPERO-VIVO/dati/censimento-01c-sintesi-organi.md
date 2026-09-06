# Censimento 01c — SINTESI DEGLI ORGANI DI GOVERNO

> Materia prima: `PIANO-MAESTRO/31-PIANO-IMPERO-VIVO/dati/censimento-01b-organi.md` (1.096 righe,
> 14 organi schedati, non modificato da me).
> Questo file contiene le **tre sintesi finali** che mancavano al censimento 01b, più le **tre
> verifiche supplementari** (Mandato · Sentinelle · Ispettorato) rifatte da me sul disco.
> Ogni numero qui viene o da una scheda del 01b, o da un comando che ho lanciato e che riporto.
> Data rilevazione: 2026-09-06.

---

## SINTESI A — LA TABELLA

**Legenda "chi lo chiama oggi":** «nessuno» significa nessun hook, nessuno script, nessun comando
dichiarato, nessun workflow. Un check di **esistenza** dentro `scripts/verify-empire.ps1` o
`scripts/gen-empire.py` **non è una chiamata**: verifica che l'organo ci sia, non lo convoca — e
`verify-empire.ps1` a sua volta non è agganciato ad alcun hook (verificato: `grep -nE
'"(SessionStart|Stop|PreToolUse|UserPromptSubmit)"' .claude/settings.json` → i 5 hook configurati
sono `empire-sync.ps1 pull`, `emperator_boot.py`, `gate_battito_hook.py`, `empire-sync.ps1 push`,
`graphify.exe hook-guard` ×2, `emperator_hook.py`. Nessuno nomina un organo).

| # | Organo | File | Agenti definiti | Invocabili in `.claude/agents/` | Chi lo chiama oggi | Difficoltà |
|---|---|---|---|---|---|---|
| 1 | `company/Board-CSuite/` | 163 (163 .md) | **70** (10 per figura) | **0 su 70** — esistono però le 7 figure con altro nome (`ceo-empire-conductor`, `cfo-empire`, `cmo-empire`, `coo-empire`, `cro-empire`, `cto-empire`, `chief-forge`) | **nessuno.** `gen-empire.py:28-35` ne verifica 8 file; `empire/loader.py:157` ne **legge** i 70 file per il cruscotto (letto ≠ chiamato) | MEDIA |
| 2 | `company/Guilds/` | 6 (6 .md, tutti README) | **5** Guild Master, solo nominati nei README | **5 su 5**, con nomi diversi: `guild-prompt`, `guild-copy-apsoc`, `guild-quality`, `guild-cost`, `guild-design` | **nessuno.** `gen-empire.py:43-48` verifica 6 path. Il "BUS" su cui i README dicono di mandare la `guild_request` non esiste come codice | BASSA |
| 3 | `company/Sentinels/` | 6 (6 .md, tutti README) | **5** | **5 su 5**: `sentinel-brandvoice/cost/drift/quality/security` (319-376 righe l'una) | **nessuno.** Nessun hook, nessun daemon, **0 git hook attivi** (`ls .git/hooks \| grep -v .sample \| wc -l` → 0) | MEDIA (Quality/BrandVoice/Cost) · BASSA (Security/Drift) |
| 4 | `company/Mandato/` | 2 (2 .md) | **0 — per statuto** («nessun agente, nessun codice: solo le leggi») | n/a | **verify-empire.ps1:81-89** (4 check di contenuto) + `empire/empire.toml:8` `root_marker` + `empire/tests/test_seed.py:23,66`. Tutto **solo a mano**: nessun hook lancia lo script | BASSA |
| 5 | `company/Ispettorato/` | 204 (115 .md, 88 .json, 1 .gitkeep) | **11** (`isp-*.md` in `agenti/`) | **0 su 11** (`ls .claude/agents/ \| grep -c "^isp-"` → 0) | **`python -m empire inspect capture\|analyze\|dispatch\|confirm\|report\|status\|backfill`** — comando reale, 30 test verdi, ma **a mano**: nessun hook post-run. `empire/loader.py:158` ne legge gli 11 file | BASSA |
| 6 | `company/MAXIMILIAN/` | 15 (15 .md) | **8** (`MX-PRIME`, `MX-VISION`, `MX-CRITIC`, `MX-CHALLENGE`, `MX-ANTICIPATE`, `MX-STYLE`, `MX-FAST`, `MX-MEMORY`) | **0 su 8** (`ls .claude/agents/ \| grep -ci "^MX-\|^maximilian"` → 0). Le sue 2 skill non sono installate in `.claude/skills/` | **nessuno.** Unico aggancio: `empire/empire.toml:33`, alias di percorso | MEDIA |
| 7 | `company/Gerarchia/` | 1 (1 .md, 79 righe) | 0 — è una mappa | n/a | `verify-empire.ps1:59` (esistenza, PASS) + `gen-empire.py:50` | BASSA |
| 8 | `company/Backbone/` | 10 (7 .md, 1 .yaml, 1 .json, 1 .gitkeep) | **2** | **2 su 2**: `bb-handoff-router`, `bb-memory-writer` | `verify-empire.ps1:117-121` (4 check di esistenza, PASS) + `gen-empire.py:36-42`. **`Bus/handoffs/` è vuota**: non ci è mai passato un messaggio | MEDIA |
| 9 | `company/Genesi-Core/` | 64 (64 .md) | **18** (8 `arch-*` + 10 `frg-*`) | **0 su 18** (`ls .claude/agents/ \| grep -c "^arch-\|^frg-"` → 0) | **nessuno.** Solo `empire/empire.toml:31`. **Unico organo che nemmeno il gate strutturale controlla**: assente da `gen-empire.py` e da `verify-empire.ps1` | ALTA (BASSA con la scorciatoia: 17 `mba-*` + 25 `cf-*` fanno già il mestiere) |
| 10 | `company/org/` | 1 (1 .yaml, 346 righe, 33 asset) | 0 — è un inventario | n/a | `verify-empire.ps1:139-145`: **check di contenuto** (`orfani <= 3`, oggi 2, PASS) | BASSA |
| 11 | `company/Antigravity-Briefs/` | 16 (16 .md, 2.314 righe) | 0 — sono brief | n/a | **nessuno**, ed è per natura umano (si incolla un brief a Gemini). Assente da `gen-empire.py` e `verify-empire.ps1` | BASSA |
| 12 | `company/01-agency/` | 114 (91 .png, 15 .md, 6 .json, 1 .txt, 1 .gitignore) | **7** (`AG-DIR` + `AG-A1..A6-COORD`, senza file-scheda) | **0 su 7** (`ls .claude/agents/ \| grep -c "^AG-"` → 0) | **`verify-empire.ps1:147-196`, ~30 check, tutti PASS** — l'organo più controllato. Comando di scrittura: `scripts/agency-trace.ps1`, che **nessuno chiama** | BASSA (rendimento più alto) |
| 13 | `company/02-info-business/` | 24 (18 .png, 2 .py, 1 .pdf, 1 .md, 1 .html, 1 .gitignore) | 0 | n/a | **nessuno.** `python build_brand_guidelines.py` a mano; non è in `skills-map.yaml`, non è in `verify-empire.ps1` | BASSA |
| 14a | `company/GRUPPO.md` | 1 (136 righe) | 0 — ma **cita 7 nomi-agente C-level** (`empire-conductor`, `empire-coo`, `empire-cto`, `empire-cmo`, `empire-cro`, `empire-cfo`, `empire-chief-forge`) | **0 su 7**: nessuno di quei sette nomi esiste in `.claude/agents/` | `verify-empire.ps1:42` + `gen-empire.py:26` (esistenza) | BASSA |
| 14b | `company/REGISTRO-IMPRESA.md` | 1 (699 righe, 98.577 byte) | 0 — è l'anagrafe | n/a | **nessuno.** Non è in `gen-empire.py` né in `verify-empire.ps1`. Solo `empire/registry/orphans.py:23` lo protegge dalla lista orfani | BASSA |
| 14c | `company/skills-map.yaml` | 1 (3.261 righe, 149.298 byte, 80 skill registrate) | 0 — è il registro | n/a | `verify-empire.ps1:127`: **solo esistenza**, nessun confronto con `.claude/skills/` (172 di progetto + 125 globali) | BASSA |

**Totali di colonna.** Agenti **definiti** dentro il perimetro di governo: **121**
(70 Board + 11 Ispettorato + 18 Genesi-Core + 8 MAXIMILIAN + 7 01-agency + 5 Guild + 5 Sentinel +
2 Backbone). **Invocabili in `.claude/agents/`: 19** — 5 Guild + 5 Sentinel + 2 Backbone + 7 figure
C-level (queste ultime con nomi che non compaiono in nessun documento di governo). **Copertura:
15,7%.** Fuori dal perimetro, `.claude/agents/` contiene in tutto **129 file**
(`ls .claude/agents/*.md | wc -l` → 129).

**Campi che il 01b lasciava scoperti e che ho misurato io.**
1. *Chi legge davvero le schede-agente del governo.* Ho eseguito
   `python -c "from empire.loader import _agent_files; ..."`, che risolve i pattern reali di
   `empire/loader.py:152-161`. Risultato: **443 file agente visti** — `company/Ecosistemi` 339,
   `company/Board-CSuite` **70**, `company/Ispettorato` **11**, fuori da `company/` 23.
   **Guilds, Sentinels, MAXIMILIAN, Genesi-Core e 01-agency non sono in nessuno dei 5 pattern**:
   i loro 43 agenti (5+5+8+18+7) sono invisibili anche alla macchina che conta gli agenti
   dell'azienda. Il cruscotto (`empire/dash/collect.py:26`, KPI `agenti_progettati`) li ignora.
2. *Il conteggio degli agenti invocabili per famiglia*, rifatto file per file:
   `^isp-` 0 · `^arch-` 0 · `^frg-` 0 · `^MX-` 0 · `^maximilian` 0 · `^AG-` 0 · `^guild-` **5** ·
   `^sentinel-` **5** · `^bb-` **2** · `^cf-` 25 · `^mba-` 17.
