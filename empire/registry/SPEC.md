---
Owner: Max
Controllore: Claude (gate 5-bis)
Origine: FORGE — pacchetto GEM-04 (Antigravity/Gemini)
Governo: company/Mandato/MANDATO-EMPIRE.md + ADR-008
---

# `empire/registry/SPEC.md` — Specifica e Tassonomia dell'Anagrafe d'Impresa

Questo documento stabilisce la tassonomia ufficiale (`kind`), le regole di estrazione della provenienza (`Provenance`), le esclusioni dei falsi positivi per gli orfani e la logica di severità temporale per il gate `ADR-008`.

---

## 1. Tassonomia Ufficiale (`kind`)

Ogni file censito nel monorepo da `census.py` viene classificato in una delle seguenti categorie (`Artifact.kind`):

| `kind` | Descrizione / Pattern Path | Esempi |
|---|---|---|
| `agent` | Scheda agente o definizione operativo AI (`*.md`, `*.yaml` con frontmatter/ruolo agente) | `DIGITAL-EMPIRE/04-AGENTS/PERFORMANCE-CELL.md`, `company/Ecosistemi/*/Agenti/*.md` |
| `department` | Scheda di reparto L2 (`*-Department.md`, `Dipartimento*.md`) | `company/Board-CSuite/Chief-Forge.md`, `DIGITAL-EMPIRE/04-AGENTS/youtube-department/` |
| `ecosystem` | Scheda ecosistema L1 (`ECOSISTEMA.md`, `dossier-*.md`, `company/Ecosistemi/*`) | `company/Ecosistemi/01-AGENCY/ECOSISTEMA.md` |
| `workflow` | Flussi operativi, piani operativi e sequenze (`WF-*.md`, `PLANNING-*.md`, `workflows.yaml`) | `WORKFLOW-ESTATE/01-FLUSSI-E-PIANI/WF-MASTER.md` |
| `skill` | Specifica di skill o cartella skill (`SKILL.md`, `skill-*.yaml`) | `DIGITAL-EMPIRE/05-SKILLS/*/SKILL.md`, `WORKFLOW-ESTATE/.agents/skills/*` |
| `script` | Codice eseguibile, automazioni e librerie (`*.py`, `*.ps1`, `*.sh`, `*.bat`, `*.cmd`) | `empire/cli.py`, `WORKFLOW-ESTATE/02-AUTOMAZIONI-E-SCRIPTS/memory_manager.py` |
| `dashboard` | Cruscotti e metriche di controllo (`DASHBOARD*.md`, `LISTA-*.md`, `*.html` di cruscotto) | `WORKFLOW-ESTATE/06-DASHBOARD-E-METRICHE/DASHBOARD.md` |
| `template` | Modelli e kit di delivery o outreach (`*-template.*`, `05-TEMPLATES-E-KIT/*`) | `WORKFLOW-ESTATE/05-TEMPLATES-E-KIT/preventivo-template.md` |
| `doc` | Documentazione generale, ADR, checkpoint, Mandato, istruzioni (`*.md` non rientranti negli altri) | `company/Mandato/MANDATO-EMPIRE.md`, `company/Memory/STATO-EMPIRE.md` |
| `asset` | Asset binari, immagini, log, dati grezzi (`*.png`, `*.jpg`, `*.json`, `*.csv`) | `empire/.data/census.json` |
| `vendored` | Repository/framework/skill esterni vendorizzati (`DIGITAL-EMPIRE/05-SKILLS/ruflo/*`, etc.) | `DIGITAL-EMPIRE/05-SKILLS/ruflo/CLAUDE.md` |

---

## 2. Estrazione della Provenienza (`Provenance`)

Secondo `ADR-008`, ogni artefatto interno deve dichiarare 4 campi:
1. `Owner` (o `Proprietario`)
2. `Controllore` (o `Controller`, `QA`)
3. `Origine` (o `Origin`, `Creato da`)
4. `Governo` (o `Governance`, `Mandato`)

### Fonti e Priorità di Estrazione
1. **YAML Frontmatter (Markdown / YAML):**
   Cerca tra i primi marcatori `---` e `---` le chiavi `owner:`, `controllore:`, `origine:`, `governo:` (case-insensitive).
2. **Docstring Iniziale / Commenti (Python / PowerShell / Shell / Batch):**
   Cerca nelle prime 30 righe di commento o docstring (`"""` / `#`) le stesse parole chiave (es. `Owner: Max · Controllore: Claude ...`).
3. **Quote / Header Textual (Markdown legacy):**
   Se manca il frontmatter YAML, cerca nelle prime 20 righe (inclusi `> **Legge:**` o tabelle di intestazione) chiavi o meta-dati.

---

## 3. Esclusioni Falsi-Positivi per `orphans.py`

I seguenti artefatti **NON** sono mai classificati come orfani o bloccati per assenza di intestazione `ADR-008`:
1. **File Indice e Documentazione di Root:** `README.md`, `INDEX.md`, `CHANGELOG.md`, `LICENSE`, `REGISTRO-IMPRESA.md`, `skills-map.yaml`.
2. **Template e Kit:** I file all'interno di `05-TEMPLATES-E-KIT/` o cartelle `templates/` o `assets/` (che acquisiscono l'ownership del modulo padre).
3. **Fixture di Test e Dati Generati:** Cartelle `tests/fixtures/`, file in `.data/`, `logs/`, `checkpoints/` (`CP-*.md`), o file generati dalle run (`forge-run-*`).
4. **Asset Vendorizzati (`vendored`):** Cartelle e file sotto `DIGITAL-EMPIRE/05-SKILLS/ruflo/`, `WORKFLOW-ESTATE/.agents/skills/`, `.claude/skills/`, `node_modules/`, che possiedono un proprio governo di terze parti.

---

## 4. Logica di Severità Temporale (`orphans.py`)

Per evitare che il censimento di un monorepo storico (`1.267 .md` nati prima del 19/07/2026) blocchi il lavoro quotidiano:
- **Tolleranza Storica (Prima del 2026-07-19):** I file creati prima della data di promulgazione dell'ADR-008 che mancano di uno o più campi di `Provenance` generano una finding di severità **`warn`**.
- **Rigore Obbligatorio (Dal 2026-07-19 in poi):** Qualsiasi file creato o modificato significativamente dal 19 luglio 2026 in avanti che sia privo dei 4 campi di `Provenance` genera una finding di severità **`block`** (exit 1 nei gate di conformità).

---

## 5. Campionamento di 15 File del Monorepo (Verifica di Ricognizione)

| Path | `kind` | Frontmatter / Intestazione | Esito ADR-008 |
|---|---|---|---|
| `company/REGISTRO-IMPRESA.md` | `doc` | Root Index/Registry (`> **Legge:**...`) | escluso false-positive (`OK`) |
| `company/Mandato/MANDATO-EMPIRE.md` | `doc` | Root Law (`# MANDATO EMPIRE...`) | storico pre-19/07 (`warn`) |
| `company/Board-CSuite/Chief-Forge.md` | `department` | Body Table Header | storico pre-19/07 (`warn`) |
| `company/Memory/STATO-EMPIRE.md` | `doc` | Body Header + Coordinate | storico pre-19/07 (`warn`) |
| `company/Memory/checkpoints/CP-20260722-005.md` | `doc` | Checkpoint log | escluso false-positive (`OK`) |
| `company/Memory/decisions/ADR-008-catena-intestazione-controllo.md` | `doc` | Header list (`- **Autorità:**...`) | storico (`warn`) |
| `company/Ecosistemi/01-AGENCY/ECOSISTEMA.md` | `ecosystem` | Body Table Header | storico pre-19/07 (`warn`) |
| `WORKFLOW-ESTATE/01-FLUSSI-E-PIANI/WF-MASTER.md` | `workflow` | Metadata in quote | storico pre-19/07 (`warn`) |
| `WORKFLOW-ESTATE/02-AUTOMAZIONI-E-SCRIPTS/memory_manager.py` | `script` | Comment header | storico (`warn`) |
| `DIGITAL-EMPIRE/04-AGENTS/PERFORMANCE-CELL.md` | `agent` | Body header | vendored/import (`warn`) |
| `DIGITAL-EMPIRE/05-SKILLS/SKILL-REGISTRY.md` | `doc` | Root registry index | escluso false-positive (`OK`) |
| `DIGITAL-EMPIRE/05-SKILLS/ruflo/README.md` | `vendored` | External repo | vendored (`OK`) |
| `empire/README.md` | `doc` | YAML Frontmatter (`Owner, Controllore, Origine, Governo`) | completo e conforme (`OK`) |
| `empire/schema.py` | `script` | Python docstring (`Owner: Max · Controllore: Claude...`) | completo e conforme (`OK`) |
| `PIANO-MAESTRO/16-PIANO-ESTATE-REVENUE.md` | `doc` | Body header | storico (`warn`) |
