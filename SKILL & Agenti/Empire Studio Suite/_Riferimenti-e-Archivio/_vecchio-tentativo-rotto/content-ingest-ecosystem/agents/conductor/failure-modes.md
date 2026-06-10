# Conductor Failure-Modes (P09 First-Class)

**Table (Failure | Symptom | Prevention | Detection | Recovery)**

| Failure | Symptom | Prevention (in prompt/playbook/tools) | Detection | Recovery |
|---------|---------|---------------------------------------|-----------|----------|
| No visual watching (only transcript) | Wiki has only audio text, user "non basta la trascrizione" | Mandate L3 video-watcher + L4 skill with playwright frames + "passaggi mostrati" section in every analysis template. Always extract 5+ frames per video. | qa coverage grep "frame-" or "visual desc" in wiki notes < threshold; user feedback "manca la parte visiva". | Re-spawn watcher with more frames or full download + opencv; log FM; iterate forge with visual emphasis. |
| API or paid used (violation) | Logs show openai/yt-api calls or costs | Strict CLI: yt-dlp + playwright only in all tools.md/playbooks/L4 scripts. No import requests to paid. Validator --check-cli-only. | validator.py or grep "api" "openai" "anthropic" in run logs; user "ma hai usato API?". | Immediate stop, rollback to pure CLI alternative (playwright for everything), log FM, update all scripts with comment "CLI ONLY per user". |
| Gerarchia bypassed (flat agents) | Conductor calls L3 directly, no L2 teams | Playbook explicit "sempre spawn L2 team first (ingestion-team etc), then L3 inside". Handoff template requires team. | State.json "spawned_teams" empty or CATALOG check; user "dove sono i team?". | Re-plan with L2, spawn teams, log FM, update playbook. |
| Memory not updated (P10 violation) | No new CPs/DECs/INDEX after steps, like initial master-build ANALYSIS | Mandate in every playbook/handoff "memory update after this". Scripts auto call manager. Conductor checklist. | INDEX last entry old; ls checkpoints/ count low; validator or user "non vedo memory". | Run manager manually for missed, create retro CP, update all agents memory.md with stricter protocol (like CP-013 recovery). |
| Low coverage or no trace (P12) | Wiki notes lack "Trace (P12): video#ts+frame" or atoms from visual missing | KG stage + templates force trace headers. Every atom in analysis has "trace". Forge template includes it. | coverage-verifier <95%; grep "Trace (P12)" count < atoms; user "non so da dove viene". | Re-extract with explicit trace in re-run; add to FM log; update templates. |
| Summary instead of expansion (P03) | Short wiki notes, no MKD, "riassunto" feel | content-forge invariant + this SKILL "SEMPRE MKD + espandi". Templates "no summary, expand with examples ➕". | Length check < source; no MKD file; user "troppo corto". | Re-forge with "no-summary" flag + expand instruction; log FM. |
| Shallow visual (P08) | Frames few or desc generic "video shows UI" | Playwright script: min 8 frames/video or per chapter, detailed visual_analyzer prompt "describe exact UI elements, clicks, results shown, colors, text visible". | visual desc < 50 words or no "mostra click" etc. | Re-watch with denser frames or human prompt in script; depth pass. |
| No update proposal when relevant (user req) | Ingest marketing/skill video but no "aggiorna flussi" output | Stage 9 always: "analyze new knowledge vs known user workflows (from memory/context). If match (e.g. skill creation), generate proposal.md with trace." | No update-proposals.md when focus=skills/automation. | Force in playbook; post-run check. |
| Failure-detector not silent (PT07) | User sees SI noise | SI only if negative signals (QA fail, user negative words, FM count>3). Conductor never surfaces unless asked. | User "perché mi parli di failure?". | Enforce in system-prompt "Stage 10 silenzioso". |
| Large channel overload | 100 videos, timeout or cost | Ingestion screening + --focus + batch (max 20 per run), user warn "canale grande, filtro a 15". | State "files_count">30 without batch. | Split runs, user confirm. |

**Global Log:** All FMs to failure-modes-log/ via SI. Triage/plan for phase improvements.

**Additional from Master-Build CS03/CS04 + User:** CS03 (SI without observer = drift) → always silent-observer in qa-team. CS04 (bugs in real-test) → real-test in QA ( "prova a usare la conoscenza per un mini task").

**Trace (P12):** To P09/PT07 + CS03/CS04 from master + user "video va visto" (FM no visual) + "no api" + "gerarchia" + "memory" + "content-forge" + "aggiornare flussi" + "agenti completi" + our build CPs.

**Status:** Full table 10+ entries. Prevention in all other files.
