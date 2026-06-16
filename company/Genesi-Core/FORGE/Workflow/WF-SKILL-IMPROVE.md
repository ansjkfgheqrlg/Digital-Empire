# WF-SKILL-IMPROVE
## Skill esistente + nuova conoscenza → versione migliorata (eval prima/dopo)

> Organo: FORGE (Genesi Core) · Reparto owner: L2.1 SKILL-WORKS · Stato: DEFINED
> Aggiorna una skill già in produzione con nuova conoscenza misurando il guadagno reale.
> Quando il miglioramento tocca la STRUTTURA (sezioni/references/schema) passa prima da ARCHITETTURA
> (HC-ARCH-FORGE con blueprint del delta); quando tocca solo il CONTENUTO del kernel resta dentro la FORGE.
> Regola ferrea: **backup + diff + eval prima/dopo**. Collega: [[WF-SKILL-NEW]] · [[WF-SKILL-AUDIT]]

---

## Trigger
- Memory Empire segnala un enrichment oltre la soglia safe ma che richiede modifica della skill.
- INTELLIGENCE ha ingerito nuovo materiale rilevante per una skill esistente.
- ReasoningBank ha distillato un pattern di fallimento ricorrente (≥3 conferme) su una skill.
- Eval score scende sotto 85% nel monitor periodico di `frg-eval-runner`, o reject rate in aumento (Quality-Sentinel).
- **Natura:** mai toccare una skill attiva senza backup + diff + non-regressione (G-SAFE-ENRICH ereditato da INTELLIGENCE).

---

## Input (JSON)
```json
{
  "skill_id": "nome-skill da migliorare",
  "blueprint_ref": "architettura/blueprint/ARCH-... | null (solo se cambia la struttura)",
  "nuova_conoscenza": "intelligence/empire-studio/<run> | pattern ReasoningBank | feedback operativi",
  "motivo": "descrizione del gap o fallimento",
  "tocca_struttura": false,
  "committente": "INTELLIGENCE | Quality-Sentinel | <ecosistema>"
}
```
- `tocca_struttura = true` → richiede prima HC-ARCH-FORGE da ARCHITETTURA (blueprint del delta validato).

---

## Pipeline (passi · agente owner)
```
1. SNAPSHOT BACKUP                     (frg-skill-smith)
   └── copia versionata della skill originale PRIMA di qualsiasi modifica (backup obbligatorio)

2. CONTEXT ENRICHMENT → MKD            (frg-mkd-forger · content-forge)
   └── MKD con la nuova conoscenza da integrare — espandere, non riassumere

3. EVAL BASELINE                       (frg-eval-runner)
   └── eval score sulla skill ORIGINALE (baseline) registrato in forge/evals/

4. DIFF PROPOSTO + INTEGRAZIONE        (frg-skill-smith)
   └── diff annotato (cosa cambia e perché) approvato da frg-chief → integra; kernel resta ≤500 righe

5. EVAL POST + CONTRADICTION           (frg-eval-runner → frg-contradiction-gate)   →  G-GAIN
   └── eval post-modifica → contradiction VERDE → confronto post vs baseline

6. ROLLBACK GATE + CONSEGNA            (frg-skill-smith + frg-chief)
   └── post ≥ baseline e ≥85% → deploy + handoff a MAXIMILIAN → Mandato → HR (versione aggiornata)
   └── post < baseline → ROLLBACK automatico al backup + issue causa-radice in forge/evals/
```

---

## Gate
- **G-SAFE-ENRICH:** backup presente + diff approvato + verifica non-regressione PRIMA di toccare la skill attiva.
- **G-ARCH (condizionale):** se `tocca_struttura=true`, blueprint del delta validato da ARCHITETTURA prima di procedere.
- **G-GAIN (non negoziabile):** pass_rate post ≥ baseline E ≥ 85%; un miglioramento che peggiora = bug → rollback immediato.
- **G-KERNEL:** kernel resta ≤500 righe, nessuna regressione di formato.
- **G-CONTRADICTION:** nessuna contraddizione bloccante introdotta vs altre skill.

---

## Output (JSON)
```json
{
  "skill_id": "nome-skill",
  "versione_prima": 0.84,
  "versione_dopo": 0.92,
  "diff_summary": "cosa è cambiato",
  "backup_ref": "forge/backups/<skill>-<data>",
  "contraddizioni": "VERDE",
  "handoff_to": "MAXIMILIAN",
  "stato": "deployed | rolled_back"
}
```

---

## Handoff
- **In ingresso (condizionale):** HC-ARCH-FORGE da `WF-ARCH-DESIGN` solo quando cambia la struttura; altrimenti trigger diretto da INTELLIGENCE/ReasoningBank.
- **In uscita:** se `deployed` → **MAXIMILIAN** (all'altezza?) → **Mandato** (lecita?) → **Identity-HR** (aggiorna versione in skills-map.yaml) → VIVO. Se `rolled_back` → issue causa-radice, nessuna consegna.
- **Confine:** modifiche di solo contenuto restano FORGE; modifiche di struttura tornano ad ARCHITETTURA.

---

## Dry-run
Skill `cold-email` con reject rate in aumento + pattern ReasoningBank (≥3 conferme). Backup, MKD con la
nuova conoscenza, eval baseline 0.84, diff approvato, integrazione (kernel ≤500), eval post 0.92 (> baseline,
>85%), contradiction VERDE → deploy + handoff a MAXIMILIAN, skills-map aggiornato. Caso rollback: eval post
0.80 (< baseline) → rollback automatico al backup + issue in forge/evals/.

---

## Connessioni
- [[WF-SKILL-NEW]] — workflow gemello per skill da zero
- [[WF-SKILL-AUDIT]] — può triggerare un improve quando rileva drift/contraddizioni
- [[WF-ARCH-DESIGN]] — invocato solo se il miglioramento cambia la struttura
- [[frg-skill-smith]] · [[frg-mkd-forger]] · [[frg-eval-runner]] · [[frg-contradiction-gate]] — agenti owner
- [[06-ECOSISTEMI-CORE]] §07 L2.1 SKILL-WORKS — fonte di verità
