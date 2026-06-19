---
Type: CONCEPT
Status: Active
Tags: #skills #copywriting #apsoc #L2-1
Created: 2026-06-18
Last updated: 2026-06-18
---

# SKILLS — L2.1 Copywriting

> Le skill del reparto cuore. La maggior parte sono il MOTORE esistente (Copy Workflow) richiamato
> come entry point — non si reinventano. Una sola skill nuova v2 (`awareness-router`).
> Dossier: `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md` §5.2, §6.

---

## Skill MOTORE (esistenti — entry point, NON riscritte — ADR-003)

| Skill | Ruolo | Note |
|---|---|---|
| `copywriting` / `copy-workflow` | **Motore primario** | Entry point del Copy Workflow Orchestration Layer. Restano invocabili così come sono. Sono il sistema che gira. |
| `copy-editing` | QA editoriale | Sub-funzione di T-REVIEW per la revisione editoriale del copy. |

## Skill KNOWLEDGE (Guild trasversale — condivise)

| Skill | Ruolo | Note |
|---|---|---|
| `cro-copy-architect` | Knowledge layer condiviso | Pattern #6: usata da tutti gli ecosistemi che toccano copy. NON è di proprietà esclusiva di L2.1: è della Copy/APSOC Guild. |
| `marketing-psychology` | Reference trasversale | Bias, trigger, principi di persuasione per A3-A7. Reference, non motore. |

## Skill NUOVA v2 (da forgiare via 07-FORGE)

### `awareness-router` (priorità P1)

**Owner:** L2.1 (T-AWARENESS-ROUTER)
**Cosa fa:** adatta la struttura APSOC al livello di awareness del lettore. Un `unaware` richiede
più peso su A/P (far percepire il problema); un `most-aware` richiede più peso su O/C (rimuovere
l'ultimo attrito e chiudere). La skill prende `awareness_level` + `formato` e restituisce il
**dosaggio APSOC** raccomandato (quanto spazio a ciascuna sezione).

**Perché serve:** in v1 il dosaggio era implicito nella testa del writer. In v2 diventa esplicito e
deterministico, così il copy è coerente e il gate può verificarlo.

**Anti-contraddizione:** prima della forgiatura → `skill-contradiction-analyzer` contro `copywriting`
e `cro-copy-architect` (rischio sovrapposizione sul routing). La skill IMPLEMENTA il dosaggio,
non ridefinisce APSOC.

---

## Skill ausiliarie mappate (suite market-*)

`market-copy` (ausiliaria, motore primario resta Copy Workflow), `market-proposal` (in prestito a
01-AGENCY per le proposte). Regola: in conflitto tra suite market-* e Copy Workflow, **vince il
motore** (no doppio standard — pre-mortem §11 dossier).

---

## Connessioni

- [[copy-master]] · `agenti/copy-master.md`
- [[a3-attention-writer]] · `agenti/a3-attention-writer.md`
- [[Tool_Copy_Workflow_Orchestration]] · `second-brain-vault/wiki/tools/Tool_Copy_Workflow_Orchestration.md`
- [[Framework_Cold_Outreach_APSOC]] · `second-brain-vault/wiki/concepts/Framework_Cold_Outreach_APSOC.md`
- [[SKILLS]] (L2.5 Brand) · `company/Ecosistemi/04-MARKETING/Reparti/L2-5-Brand-Creative-Strategy/skills/SKILLS.md`
