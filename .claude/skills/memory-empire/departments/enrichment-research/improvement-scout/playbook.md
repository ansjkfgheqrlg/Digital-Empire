# Playbook — improvement-scout

## Input richiesto
- `atoms.json` (atomi estratti dall'ingestione)
- `gaps.json` (output di gap-analyzer)
- Lista skill installate (da `~/.claude/skills/`)

## Step 1 — Determina il dominio della nuova conoscenza
Leggi atoms e identifica: è prompting? marketing? AI tools? workflow? copywriting?

## Step 2 — Mappa dominio → skill pertinenti
Oltre alle skill già trovate da relevance-analyzer, cerca:
- Skill con dominio adiacente (es. "marketing" se il video è su copywriting AI)
- Workflow (avvia-*, content-forge, memory-empire stessa)
- Meta-skill (skill-creator, agent-architecture)

## Step 3 — Per ogni skill nella lista pertinenti
a. Leggi SKILL.md
b. Cerca pattern obsoleti o mancanti rispetto agli atoms
c. Valuta impatto del miglioramento

## Step 4 — Genera improvement objects
Per ogni miglioramento trovato:
```json
{
  "id": "IMP-NNN",
  "type": "ADD_CONTENT|UPDATE_APPROACH|RESTRUCTURE_SECTION|NEW_WORKFLOW_STEP|DEPRECATE_PATTERN",
  "target_skill": "nome-skill",
  "target_file": "SKILL.md|references/X.md|...",
  "target_section": "sezione specifica",
  "current_approach": "cosa dice ora la skill (citazione diretta o null)",
  "new_approach": "cosa dovrebbe dire con la nuova conoscenza",
  "evidence": "citazione dall'atom che giustifica il cambiamento",
  "source_atom": "videoID#timestamp+frameNNN",
  "priority": "low|medium|high",
  "confidence": 0.0-1.0
}
```

## Step 5 — Filtra
Rimuovi: confidence < 0.6, rilevanza < 0.5, duplicati di gap-analyzer

## Step 6 — Scrivi handoff
`memory/handoffs/improvements-<timestamp>.json`

## Step 7 — Se 0 miglioramenti trovati
Scrivi comunque il JSON con `improvements: []` e aggiungi:
```json
"scout_notes": "La nuova conoscenza non identifica pattern obsoleti o mancanti nelle skill analizzate. Dominio troppo specifico o skill già aggiornate."
```
