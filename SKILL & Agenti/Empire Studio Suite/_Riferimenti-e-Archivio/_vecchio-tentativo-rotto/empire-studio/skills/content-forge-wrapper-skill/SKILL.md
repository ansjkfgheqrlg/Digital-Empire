---
name: content-forge-wrapper-skill
description: 'L4 Wrapper skill per invocare content-forge2.0 in modo controllato e integrato nell\'ecosistema. Prende materiale grezzo (analysis da video-watcher + metadata) o MKD intermedio, invoca il pipeline content-forge (Stage 1-9 o target specifico come wiki), garantisce memory sync, traceability, e output strutturato per wiki insertion. CLI-only (chiama lo skill content-forge esistente via path/clone o /forge se disponibile). Completo: SKILL.md + references (da content-forge2.0 clone) + scripts (Python wrapper + memory hook) + templates + principles (MKD always, no-summary, coverage, trace) + rules. Per forge-team L2 e L3 content-forge-invoker.'
intent: >-
  Bridge tra Empire Studio e la skill content-forge2.0 (che l\'utente fornirà accesso). Assicura che dopo ogni "guarda" + analysis, il materiale venga forg iato correttamente in MKD + wiki notes atomiche con trace. Gestisce input multi-source, memory update, e handoff a wiki-ingester. Supporta target=wiki (default), doc, custom. Espansione + coverage. CLI wrapper per consistenza.
type: tool
theme: content-forge-integration
best_for:
  - "Forgiare output di video-watcher (transcript + visual analysis) in wiki notes"
  - "Creare MKD da ingest multi-video/canale"
  - "Preparare update proposals per existing workflows"
scenarios:
  - "Dopo aver guardato  video design system, forgia tutto in wiki + MKD"
  - "Ingest canale marketing → batch forge to wiki"
  - "Materiale grezzo + visual → note atomiche con trace per Claude Code"
estimated_time: "Dipende da content-forge (minuti per batch)"
compatibility: "content-forge2.0 clone o skill installata (/forge). Integra con Empire Studio (forge-team) e memory."
---

# content-forge-wrapper-skill — Integrazione con content-forge2.0 (MKD + Wiki Target)

> **"Prendi il materiale (transcript + visual 'passaggi mostrati' + atoms) e forgialo via content-forge in MKD + wiki atomiche pronte per Claude Code. Memory sync e trace garantiti."**

## Invariant
- **MKD Sempre (content-forge Stage 4 + P03)**: Non saltare. Prima di qualsiasi target.
- **Target Wiki Default (User primary goal)**: --target=wiki produce note atomiche Obsidian con MOC, wikilink, trace a video/frame.
- **Trace + Coverage (P12 + content-forge)**: Ogni atomo nel output finale ha trace al sorgente (video ID + ts + frame se visual). Coverage check.
- **Memory Sync (P10)**: Prima e dopo invoke, run memory_manager. Aggiorna shared_state con forge results.
- **CLI Wrapper**: Chiama il content-forge (via path al clone/scripts o comando /forge se nel contesto). Logga tutto.
- **No Summary**: Espansione come da content-forge invariants.

## Come Funziona (Aggiornato Step 5 - legame con Strategy)
**Entry:** `python scripts/forge_invoker.py --source "path/to/analysis-or-mkd" --target "wiki" --name "..." --memory-sync --strategy-manifest "path/to/manifest.json"`

Il wrapper ora legge il Strategy Manifest e adatta l'output:
- Se "Visual-Heavy" → forza template con molti ref a frame.
- Se "Playbook Style" → usa struttura When/How/Examples/Metrics.
- Se "Quick-Reference" → note ultra-atomiche e brevi.

**Internals:**
1. Prepara source (copia analysis.md, frames refs, metadata, atoms).
2. Costruisce comando per content-forge (dal clone /home/user/content-forge2.0 o skill).
3. Invoke (subprocess o direct se Python).
4. Post-process: estrae MKD + wiki/ dir.
5. Memory update + trace append.
6. Output: packaged/wiki-notes/ + report + update-proposals skeleton.

**Supporta:**
- --target=wiki (atomic notes)
- --target=doc (espanso)
- Custom per update existing.

## Scripts
- `scripts/forge_invoker.py`: Wrapper completo con argparse, source prep, call, post, memory hook, error handling.
- `scripts/prepare_forge_input.py`: Helper per multi-video + visual.

## References
- /home/user/content-forge2.0/SKILL.md + references/stages/ + processes/wiki.md (full pipeline, wiki target, 9 stages, MKD, no-summary, depth, SI).
- Empire Studio SKILL.md (forge-team role).
- master-build for traceability in forged outputs.

## Principles & Rules
- Sempre MKD.
- Trace a sorgente video/frame.
- Memory P10 prima/dopo.
- Coverage >= soglia prima di accettare.
- Supporta multi-source (canale = più video).
- Output directly usable da wiki-ingester L3.

**Evals**: "Ingest + watch video design → forge to wiki → verify atomic notes with visual trace + MKD present + memory updated."

**Status**: Full L4 skill. Script wrapper principale. Pronto per L3 content-forge-invoker-agent.

**Trace (P12)**: To user "tutto il contenuto... va portato all'interno della skill content-forge... inserire... all'interno Della wiki... la wiki è connessa a claude code" + content-forge2.0 full + content-ingest forge-team + master-build + our integration.
