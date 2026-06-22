---
Type: SCRIPTS
Status: Active (wrappa runtime esistente — ADR-003)
Tags: #scripts #ricerca #scraper #qualifier #competitor #A1
Created: 2026-06-22
Last updated: 2026-06-22
---

# Script — A1 Ricerca & Market Intelligence

> Script del reparto. A1 NON riscrive il runtime live (ADR-003): lo WRAPPA.
> Questa pagina documenta gli script esistenti che A1 orchestra e come li invoca.
> Nessuno script qui descritto va riscritto: si parametrizza, si documenta, si invoca.

---

## Script esistenti wrappati (runtime live — usa-così)

### `scraper/*.py` — runner scraper multi-fonte [WRAPPA-ESISTENTE]

**Dove:** `Outreach/Outreach Workflow/agents/` (maps/apify/outscraper/google).
**Scopo:** raccolta raw multi-fonte. AG-A1-SCRAPE li invoca in parallelo per fonte.
**Input:** `{nicchia, query, fonte, n_target}` · **Output:** raw HTML/JSON per fonte.
**Confine:** A1 orchestra e logga per fonte in `agency/a1/sourcing`. Non modifica il codice.

---

### `extractor.py` — estrazione contatti [WRAPPA-ESISTENTE]

**Dove:** `Outreach/Outreach Workflow/agents/extractor.py`.
**Scopo:** trasforma raw HTML/JSON in schede lead (nome, email, telefono, sito, settore).
**Input:** raw per fonte · **Output:** schede lead strutturate.
**Confine:** AG-A1-EXTRACT lo invoca; scrive le schede in `agency/leads`. Non riscrive il parser.

---

### `qualifier.py` — scoring lead vs ICP [WRAPPA-ESISTENTE]

**Dove:** `Outreach/Outreach Workflow/agents/qualifier.py`.
**Scopo:** scora ogni lead contro l'ICP corrente; triage qualificato / nurture / scarta.
**Input:** schede lead + profilo ICP · **Output:** lead con `score` + `motivo` se scartato.
**Confine:** AG-A1-QUAL lo invoca; il motivo dello scarto va in `agency/reasoning`.

---

### `competitor.py` + `cro_audit.py` — dossier competitor [WRAPPA-ESISTENTE]

**Dove:** `Outreach/Outreach Workflow/agents/competitor.py`, `cro_audit.py`.
**Scopo:** audit competitor + audit CRO del prospect per il dossier pre-call.
**Input:** `{url_prospect, url_competitor[]}` · **Output:** dossier competitor + audit problema.
**Confine:** AG-A1-COMP li invoca insieme alla skill `market-audit`. Citano sempre la fonte.

---

## Convenzioni di wrapping

- A1 invoca gli script via il loro entry-point esistente; non li forka, non li riscrive (R1).
- Ogni invocazione logga input/output in `agency/a1/...` (namespace corretto) — mai fuori.
- Dry-run disponibile dove lo script lo supporta (stima volumi senza run reale).
- Nessuna chiamata API esterna autonoma senza input esplicito dell'operatore.
- Modifica al runtime live → solo via ADR esplicito approvato (ADR-003).

---

## Connessioni

- [[ARCHITETTURA]] · `ARCHITETTURA.md §1` — ADR-003 WRAP-not-rewrite
- [[WF-LEAD-SOURCING]] · `workflow/WF-LEAD-SOURCING.md` — usa scraper/extractor/qualifier
- [[WF-BRIEF-PRE-CALL]] · `workflow/WF-BRIEF-PRE-CALL.md` — usa competitor.py/cro_audit.py
- [[SKILLS]] · `skills/SKILLS.md` — skill `icp-radar`, `market-audit`, `competitor-profiling`
