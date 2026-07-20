# ADR-009 — Toolkit esterni ufficiali (copy-workflow · master-build-architecture · content-forge2.0) e istituzione del reparto FORGE-AGENT-SKILL

- **Data:** 2026-07-20 · **Stato:** ATTIVO · **Decidente:** Max (direttiva esplicita in sessione)
- **Supersede:** nessuno · **Correlati:** ADR-001, ADR-002, ADR-003, ADR-006, ADR-008

## Contesto
Max ordina in direttiva 2026-07-20 (testuale, riassunta): usare `gh repo clone ansjkfgheqrlg/copy-workflow`
come workflow per migliorare il copy di tutto; usare `ansjkfgheqrlg/master-build-architecture` per migliorare
l'architettura di tutto ricordando che l'oggetto è **un impero con più workflow, non un workflow**;
creare **un nuovo reparto per la creazione di nuovi agenti e nuove skill** partendo da
`ansjkfgheqrlg/content-forge2.0`.

## Decisione
1. **3 toolkit esterni = asset ufficiali dell'impero**, vendored alla root del monorepo:
   - `copy-workflow/` → motore copy aziendale (orchestration layer APSOC 8 agenti, entry `/copywriting`)
   - `content-forge2.0/` → motore di forgia contenuti→artefatti (entry `/forge`)
   - `master-build-architecture/` → metodo di architettura madre (entry `/master-architect`)
   Regola ADR-003 confermata: **wrap, mai riscrittura**; modifiche ai vendor vietate nei gate
   (diff vendored = 0 è controllo bloccante di `fas-qa-gate`).
2. **Nuovo reparto operativo `FORGE-AGENT-SKILL/`** (officina permanente agenti & skill):
   intestato a 06b-FORGE (L2.1 SKILL-WORKS / L2.2 AGENT-WORKS), controllore `fas-qa-gate`+METHOD-GUARD,
   roster v1 di 4 agenti (fas-conductor, fas-agent-smith, fas-skill-smith, fas-qa-gate), workflow
   WF-AGENT-NEW / WF-SKILL-NEW, regole R1-R4 (mai riassunti, 7 file canonici, failure-modes, intestazione).
3. **Versione di master-build-architecture:** resta quella presente su `main` (più completa del clone
   GitHub: ha agents/meta + OPERATING-REGISTRY + .github). Il clone fresco NON la sovrascrive (scartato).
4. **Copertura skill:** wrapper in `.claude/skills/` per i 3 motori, con intestazione ADR-008 in testa.

## Conseguenze
- Ogni copy dell'impero passa per copy-workflow (regola attiva; QA A8 ≥85 + TOV Brand Voice).
- Ogni nuovo agente/skill nasce da FORGE-AGENT-SKILL (WF dedicati) e viene registrato (ADR-008): il
  mantra "non è un workflow, è un impero con più workflow" diventa regola operativa (R4 del reparto).
- Revisione architetturale di base: `PIANO-MAESTRO/18-ARCHITETTURA-IMPERO-REVISIONE.md` (12 migliorie MIR).
- skills-map.yaml → v1.2; REGISTRO-IMPRESA aggiornato (§3 toolkit + reparto).

## Alternativa scartata
Clonare i toolkit "a lato" senza integrazione (sarebbero rimasti inerti) o riscriverli nel repo
(violati ADR-003 e licenze di fatto del lavoro altrui). Wrapper + reparto = adozione senza duplicazione.
