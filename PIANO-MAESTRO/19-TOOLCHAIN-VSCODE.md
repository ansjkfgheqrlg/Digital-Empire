# 19 — TOOLCHAIN VS CODE: SCANSIONE COMPLETA + DECISIONI PER L'IMPERO

> **Intestazione (ADR-008)**
> - **Proprietario:** 06b-FORGE / L2.4 ECOSYSTEM-WORKS (arena session Claude, committente Max)
> - **Controllore:** METHOD-GUARD · 5-bis MAXIMILIAN (campionabile)
> - **Origine:** ordine Max 2026-07-20 («scansione dettagliata di TUTTI i plugin VSC per gestire e migliorare tutto»), CP-20260720-008
> - **Governo:** ADR-001/002/003/006/008/009 · Mandato Art.2 · regola «impero con più workflow» (mai tool orfani: ogni estensione serve almeno un workflow vivo W1-W10)
> - **Data:** 2026-07-20 · **Stato:** adottato (config `.vscode/` già committata)

---

## 0. SINTESESE (MKD della decisione)

L'impero si tocca da VS Code con Claude Code. La scansione ha coperto **14 categorie del Marketplace**
(agenti AI, Git/GitHub, Python, JS/TS, Markdown/PKM, dati YAML/CSV, web HTML, preview documenti,
produttività, API testing, shell, remote/container, database, Go) valutando i candidati di ogni categoria
contro il **censimento reale del repo** (§1) — non contro liste generiche.

**Decisione in 3 fasce:** 🟢 Tier 1 = installare subito (10) · 🟡 Tier 2 = per area di lavoro (10) ·
⚪ Tier 3 = opzionali/condizionali (12) · 🔴 Sconsigliati/rimossi (8, con motivo).

**Due regole d'oro emerse e già applicate nella config:**
1. **L'agente AI ufficiale è Claude Code** (estensione `anthropic.claude-code`). Copilot/Cline/Continue/Kilo
   sono duplicati dell'agente — si evita il doppio driver (stessa regola anti-collisione di STATO-EMPIRE).
2. **Nessun format-on-save automatico in questo repo**: 7.625 Markdown + vendor intoccabili (ADR-003,
   diff-vendor = 0) → un formatter globale sporca migliaia di file e rompe i vendor. Prettier/Ruff restano
   manuali o per-cartella.

---

## 1. METODO + CENSIMENTO DELLO STACK (perché queste scelte)

**Metodo:** (a) censimento `git ls-files` per estensione → peso reale di ogni linguaggio; (b) scansione
Marketplace aggiornata al 2026-07-20 (top install, stato di manutenzione, deprecazioni); (c) matrice
verdetto per categoria (§2-§5); (d) mappatura ai workflow vivi W1-W10 (§6).

**Censimento reale del monorepo (2026-07-20):**

| Tipo | N° file | Dove sta la massa | Cosa serve in editor |
|---|---:|---|---|
| `.png` | 8.123 | frame video, copertine, vault | preview nativa (basta) |
| **`.md`** | **7.625** | vault, Memory, dossier, 300+ agenti CF-grade | **Markdown All in One + Memo (wikilinks) + spellcheck IT** |
| **`.py`** | **867** | Outreach, PreventivoForge, EmpireDesk, scripts | **Python + Pylance + Ruff** |
| `.json` | 600 | state/, config, handoff | nativo + Error Lens |
| `.tsx` + `.ts` | 596 | Empire Studio Suite, dashboard, landing | ESLint + Prettier (manuale) |
| `.go` | 471 | backend Empire Studio Suite | Go (solo se apri la suite) |
| `.mdx` | 339 | docs toolkit | vscode-mdx (opz.) |
| `.txt` | 327 | formazione, prompt, regole | spellchecker IT |
| **`.yaml`/`yml`** | **181** | skills-map (60 skill), registri, handoff, principi | **redhat.vscode-yaml** |
| `.js`+`.mjs` | 184 | generate.js caroselli, orchestratori | ESLint |
| `.pdf` | 107 | preventivi, manuali | vscode-pdf |
| `.html`+`.css` | 129 | landing, EmpireDesk UI, dashboard | Live Server + HTML CSS |
| `.sh`/`.bat`/`.ps1` | 63 | launcher, sync | ShellCheck / PowerShell (opz.) |

**Due ordini di grandezza dominano: Markdown (7.6k) e Python (867).** La toolchain è scelta di conseguenza:
l'impero è un sistema di *conoscenza scritta* pilotata da *automazioni Python*, non una codebase web.

---

## 2. 🟢 TIER 1 — INSTALLARE SUBITO (10, servono a TUTTI i workflow)

| # | Estensione (ID Marketplace) | Categoria | Perché per l'impero |
|---|---|---|---|
| 1 | **Claude Code** (`anthropic.claude-code`) | Agente AI | **È l'agente ufficiale dell'impero**: è la stessa identità/chiavi/sessioni del CLI (`claude`), con pannello laterale, diff visive, history a tab. Richiede VS Code ≥1.98. Ogni altro agente = duplicato. |
| 2 | **GitLens** (`eamodio.gitlens`) | Git | Blame inline + history per file: nel monorepo multi-owner (Max/Gael/Arena) serve sapere *chi ha toccato cosa* senza `git log` manuale. ~48M install, top-4 globale 2026. |
| 3 | **GitHub Pull Requests & Issues** (`github.vscode-pull-request-github`) | GitHub | Issue/PR nel sidebar; serve quando si apriranno PR da `arena/*` verso `main`. |
| 4 | **Python** (`ms-python.python`) | Python | Base per interpreter/venv/debug di Outreach, PreventivoForge, EmpireDesk, `gen-empire.py`. |
| 5 | **Pylance** (`ms-python.vscode-pylance`) | Python | Type-check + navigation sugli 867 `.py` (Error Lens li rende visibili inline). |
| 6 | **Ruff** (`charliermarsh.ruff`) | Python lint/format | Linter+formatter Python ufficiale Astral, standard 2026 (sostituisce flake8+black+isort). Uso **manuale** (vedi regola oro 2). NB: publisher resta `charliermarsh` per scelta Astral. |
| 7 | **markdownlint**… **NO → Markdown All in One** (`yzhang.markdown-all-in-one`) | Markdown | Shortcut, TOC, preview sync, liste automatiche sulle 7.6k note. (markdownlint escluso: su file legacy produrrebbe migliaia di warning mai chiusi — rumore, §5.) |
| 8 | **Markdown Memo** (`svsool.markdown-memo`) | Markdown/PKM | Abilita i **wikilink `[[...]]`** dentro VS Code: il vault `second-brain-vault/wiki/` è Obsidian-style e senza Memo i link interni sono rotti nell'editor. Più leggero di Foam. |
| 9 | **YAML (Red Hat)** (`redhat.vscode-yaml`) | YAML | Validation + autocompletamento sui 181 yaml (skills-map dei 60 skill, registri, handoff). Errori YAML = backbone rotto: qui si vedono **prima di salvare**. |
| 10 | **Code Spell Checker + Italian** (`streetsidesoftware.code-spell-checker` + `...-italian`) | Qualità testo | Copy dell'impero = italiano (STATO-EMPIRE, dossier, kit YouTube, landing). Segna refusi su `.md`/`.txt` senza falsi positivi su codice. |

**Install one-shot (terminale):**
```powershell
code --install-extension anthropic.claude-code eamodio.gitlens github.vscode-pull-request-github ms-python.python ms-python.vscode-pylance charliermarsh.ruff yzhang.markdown-all-in-one svsool.markdown-memo redhat.vscode-yaml streetsidesoftware.code-spell-checker streetsidesoftware.code-spell-checker-italian
```
*(Lo stesso elenco è in `.vscode/extensions.json` → VS Code li propone automaticamente all'apertura della cartella.)*

---

## 3. 🟡 TIER 2 — PER AREA DI LAVORO (installa quando lavori in quell'area)

| # | Estensione (ID) | Area dell'impero che sblocca | Workflow serviti |
|---|---|---|---|
| 11 | **ESLint** (`dbaeumer.vscode-eslint`) | `carousel-factory`, dashboard, landing TSX | W4, W6, W10 |
| 12 | **Prettier** (`esbenp.prettier-vscode`) | formattazione *manuale* JS/TS/CSS/JSON (mai format-on-save globale — regola oro 2) | W4, W10 |
| 13 | **Error Lens** (`usernamehw.errorlens`) | errori/warning inline su tutto (py, ts, yaml) | tutti |
| 14 | **Thunder Client** (`rangav.vscode-thunder-client`) | test API dentro l'editor: Gist licenze, endpoint EmpireDesk, Groq, Calendly | W1, W3, W6 |
| 15 | **Markdown Preview Mermaid Support** (`bierner.markdown-mermaid`) | diagrammi ` ```mermaid ` nei dossier/ARCHITETTURA.md | W5-W8, PIANO-MAESTRO |
| 16 | **vscode-pdf** (`tomoki1207.pdf`) | apre i 107 PDF (preventivi Novacar, manuali) senza uscire dall'editor | W3, W9 |
| 17 | **Material Icon Theme** (`PKief.material-icon-theme`) | orientamento visivo in un albero da 100+ cartelle | tutti |
| 18 | **Todo Tree** (`gruntfuggly.todo-tree`) | raccoglie TODO/FIXME/[ ] sparsi → vista unica (backlog tecnico) | tutti |
| 19 | **Rainbow CSV** (`mechatroner.rainbow-csv`) | export lead Outreach, liste | W1 |
| 20 | **Live Server** (`ritwickdey.LiveServer`) | preview live delle landing statiche (`Agency page*`, landing funnel) | W10 |
| 21 | **Path Intellisense** (`christian-kohler.path-intellisense`) | autocompletamento path nei doc .md che linkano file | W2, W5, Memory |

## 4. ⚪ TIER 3 — OPZIONALI / CONDIZIONALI (installa solo se serve quel caso)

| # | Estensione (ID) | Quando serve |
|---|---|---|
| 22 | **Go** (`golang.go`) | SOLO se apri il backend Go di Empire Studio Suite (471 file) |
| 23 | **PowerShell** (`ms-vscode.powershell`) | ritocchi ai `verify-empire.ps1`/sync script |
| 24 | **ShellCheck** (`timonwong.shellcheck`) | manutenzione dei 39 `.sh` |
| 25 | **Draw.io Integration** (`hediet.vscode-drawio`) | disegnare architetture editabili in repo (alternativa a Mermaid per diagrammi complessi) |
| 26 | **Excalidraw** (`pomdtr.excalidraw-editor`) | sketch visuali veloci |
| 27 | **Even Better TOML** (`tamasfe.even-better-toml`) | se appaiono `pyproject.toml` (oggi 0) |
| 28 | **HTML CSS Support** (`ecmel.vscode-html-css`) | ritocchi pesanti a landing/UI |
| 29 | **Pretty TS Errors** (`yoavbls.pretty-ts-errors`) | debug TSX della Studio Suite |
| 30 | **Bookmarks** (`alefragnani.bookmarks`) | segnalibri sui 6 file cardine (STATO-EMPIRE, INDEX, REGISTRO-IMPRESA…) |
| 31 | **Better Comments** (`aaron-bond.better-comments`) | commenti colorati `! * ? TODO` nel codice |
| 32 | **Project Manager** (`alefragnani.project-manager`) | switch rapido se tieni più checkout della repo |
| 33 | **vscode-mdx** (`unifiedjs.vscode-mdx`) | se editi i 339 `.mdx` dei toolkit |

## 5. 🔴 SCONSIGLIATI / RIMOSSI (con motivo — non reinstallare senza ADR)

| Estensione | Perché no PER QUESTO IMPERO |
|---|---|
| **GitHub Copilot / Copilot Chat** (`github.copilot`, `github.copilot-chat`) | Agente duplicato: l'agente ufficiale è Claude Code (estr. #1). Due driver = collisioni di edit e contesto divergente (stessa lezione PreventivoForge/EmpireDesk). Inline-completion già coperta da Claude. |
| **Sourcegraph Cody** (`sourcegraph.cody-ai`) | Tier Free/Pro **discontinuati 2025-07-23**: prodotto solo Enterprise → inutile a noi. |
| **Cline / Continue / Kilo Code / Codex / Amp** | Agenti alternativi a Claude Code: stessa regola «un solo agente». Codex/Cline valutabili *solo* come esperimento isolato con ADR dedicato. |
| **Dendron** (`dendron.dendron`) | Progetto **deprecato/abbandonato**; per i wikilink usiamo Memo (#8) che è leggero e attivo. |
| **Foam** (`foam.foam-vscode`) | Sovradimensionata (graph, daily notes, template) per un vault già governato da Obsidian-style + Memory-Impero; duplica Memo. |
| **markdownlint** (`davidanson.vscode-markdownlint`) | Su 7.625 md legacy → migliaia di warning storici mai chiusi = rumore nel pannello Problemi. La qualità md è garantita da spellcheck + review, non dal linter. |
| **Jupyter** (`ms-toolsai.jupyter`) | 0 notebook `.ipynb` nel repo. |
| **Docker / Remote-SSH / Dev Containers / WSL** (`ms-azuretools.*`, `ms-vscode-remote.*`) | L'impero gira locale su Windows + git-sync: nessun container, nessun remote. |

---

## 6. MAPPA WORKFLOW → STACK MINIMO (niente tool orfani)

| Workflow (dossier 18) | Estensioni che usa davvero |
|---|---|
| W1 Outreach | GitLens, Python, Ruff, Pylance, Thunder Client, Rainbow CSV, Error Lens |
| W2 Copy APSOC | Markdown AIO, Memo, Spellcheck IT, Claude Code |
| W3 PreventivoForge | Python, Pylance, Ruff, vscode-pdf, Todo Tree, Error Lens |
| W4 Carousels | ESLint, Prettier (manuale), Error Lens |
| W5 Empire Studio | Markdown AIO, Memo, Mermaid, (Go/TSX → #22/#29 se apri la suite) |
| W6 EmpireDesk | Python, Pylance, Thunder Client, HTML CSS Support, vscode-pdf |
| W7 YouTube Lead Machine | Markdown AIO, Memo, Spellcheck IT, Claude Code, Todo Tree |
| W8 FORGE-AGENT-SKILL | YAML Red Hat, Markdown AIO, Memo, Spellcheck IT, Todo Tree, Claude Code |
| W9 Manuale CC | Markdown AIO, Spellcheck IT, vscode-pdf |
| W10 Landing/agency | HTML CSS Support, Live Server, ESLint, Prettier, Error Lens |
| **Governance trasversale** (Memory, INDEX, REGISTRI, checklist) | Markdown AIO, Memo, Spellcheck IT, YAML, GitLens, Todo Tree |

---

## 7. CONFIG COMMITTATA (già nel repo — cartella `.vscode/`)

| File | Contenuto |
|---|---|
| `.vscode/extensions.json` | `recommendations` = Tier 1 + Tier 2 (VS Code propone «Install all» a chiunque apra la repo, Max o Gael, senza cercare gli ID). `unwantedRecommendations` = Dendron (deprecato) + Cody (free morto). |
| `.vscode/settings.json` | Scelte sicure per QUESTO monorepo: `formatOnSave: false` globale (regola oro 2), telemetry OFF (VS Code/GitLens/Red Hat — privacy impero), spellcheck `it,en` su md/txt/yaml/py/tsx, word wrap ON per markdown, **nessuna associazione automatica che riformatti i vendor** (ADR-003). |

Regola di evoluzione: cambiare Tier/settings = modifica a questo dossier + riga in REGISTRO-IMPRESA + CP
(ciclo a 9 passi, ADR-006). Mai aggiungere estensioni «alla chetichella» divergenti fra Max e Gael:
`.vscode/` è parte dell'SSO (single source of truth) come gli altri header ADR-008.

## 8. GATE DI VERIFICA (eseguito 2026-07-20)

- [x] Censimento reale del repo (tabella §1) — numeri da `git ls-files`, non stime
- [x] Ogni Tier 1-2 mappa ≥1 workflow vivo o un'area di governance (§6) → nessun tool orfano
- [x] Deprecazioni verificate online: Cody Free morto (2025-07), Dendron abbandonato, Ruff publisher confermato `charliermarsh` (scelta Astral), Copilot Chat estensione distinta e volutamente esclusa
- [x] `.vscode/extensions.json` valido JSON, ID nel formato `publisher.name` verificati su Marketplace
- [x] Config anti-rumore: niente format-on-save, niente markdownlint, telemetry off
- [x] Compatibilità Windows (l'ambiente di Max): niente estensioni Linux-only/WSL-only nei Tier

## 9. MANUTENZIONE

- **Review semestre** (gen/lug): ri-verificare deprecazioni e top-install di Tier 2-3; aggiornare questo dossier.
- **Entry-point per nuove aree**: se nasce un workflow su tecnologia nuova (es. decidiamo notebook) → si aggiunge riga in §3/§4 + mappa §6, seguendo il ciclo ADR-006.
- **Anti-bloat**: tetto consigliato ~20 estensioni attive per macchina; ogni nuova entra solo se sostituisce o colma un gap reale (mai «perché è famosa» — la lista del 2026 conferma: produttività = 10-20 estensioni scelte).
