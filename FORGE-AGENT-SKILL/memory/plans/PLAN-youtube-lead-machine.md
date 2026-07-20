# PLAN — WF-SKILL-NEW «youtube-lead-machine» (MIR-11, backlog reparto)

- **Trigger:** dossier 18 MIR-11 (P1) — la strategia YouTube Lead Machine esiste come conoscenza
  (`Formazzione/Youtube/`, 844 righe: strategia 8 sezioni + kit eseguibile), ma non come METODO
  richiamabile. Serve la skill ufficiale `/youtube-lead-machine`.
- **Owner:** fas-conductor · **Build:** fas-skill-smith · **Gate:** fas-qa-gate (verbale in memory/checkpoints/).

## RECALL (step 1) — asset simili esistenti, decisione anti-doppione
| Asset | Cosa copre | Decisione |
|---|---|---|
| `SKILL & Agenti/SKILL/Skill CRO - Youtube - Lead magnet/Skill-youtube.md` (5166 righe, a.k.a. youtube-script-factory) | SOLO scrittura script (7 componenti, 20 hook, checklist 45pt) | **WRAP, non riscrivere** (ADR-003): la nuova skill delega a lui gli script |
| `copy-workflow/` (ADR-009) | QA copy APSOC, score ≥85 | **delega**: review titoli/CTA/descrizioni |
| `formazione-youtube` (skills-map, knowledge) | sorgente grezza | resta la cantina; la skill è il METODO sopra |
| dossier 16 S5 YouTube-Fliki | automazione TTS/faceless | confine dichiarato nel kernel: questa skill = organico/frontman |
Nessuna collisione di slug: `youtube-lead-machine` libero in skills-map e REGISTRO-IMPRESA.

## Piano struttura (step 3)
- **MKD** (base canonica): `FORGE-AGENT-SKILL/memory/mkd/MKD-youtube-lead-machine.md` — copertura atomi sorgente.
- **Kernel** `SKILL.md` ≤550 righe: loop operativo settimanale, tabelle decisionali (pilastri, funnel TOFU-MOFU-BOFU),
  hook 3/10/30s sintesi, speed-to-lead, 7 errori checklist, deleghe esplicite. Solo puntatori ai references.
- **references/** (progressive disclosure vera, caricate on-demand): STRATEGIA-DIGEST, FUNNEL-OPS,
  BATCH-PROTOCOL, LIBRERIA-HOOK-TITOLI, LEAD-MAGNET-OPS, ANALYTICS-REVIEW.
- **evals/scenarios.md**: 5 scenari reali con atteso (attivazione + livello output).
- **failure-modes.md**: ≥5 righe compilate (come fallisce la skill, non il canale).
- Intestazione ADR-008 in testa al kernel. ADR-003: zero modifiche ai vendor/sorgenti (wrap puro).

## Sorgente verificata (844 righe lette)
STRATEGIA (248r, 8 sezioni) · CLIENTE-DORO (57r) · SETUP-CANALE (61r) · LEAD-MAGNET-01 (88r, gate 3 domande
+ 5 messaggi) · batch-01 (PIANO 46r + 6 script ~340r) · COPY-REVIEW-APSOC (score→90-93).

## Criterio di uscita
Gate 7/7 PASS → registrazione: skills-map v1.3 + REGISTRO-IMPRESA §3 + wiki + STATO-EMPIRE + INDEX + CP globale.
