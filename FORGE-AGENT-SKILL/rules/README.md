# ⚖️ REGOLE DEL REPARTO (R1-R4) — bloccanti, ereditate dai motori + lezioni impero

## R1 — MAI RIASSUNTI (invariante content-forge #1)
Ogni output ≥ sorgente in informazione utile. Espansione con esempi/schemi/cross-ref; invenzioni `➕`.
Violazione tipica: "documento finale più corto del transcript" → FAIL al gate automaticamente.

## R2 — 7 FILE CANONICI, SEMPRE (invariante master-build-architecture #5)
Agente senza i 7 file (spec/system-prompt/tools/playbook/evals/failure-modes/memory) è un abbozzo,
non un agente. Skill senza kernel ≤550r + references + evals è una pagina wiki, non una skill.

## R2-bis — TEAM SENZA TOPOLOGY.MD = NON ESISTE (MIR-9, 2026-07-20)
Se il deliverable è un **team (≥2 agenti coordinati)**, oltre ai 7-file di ogni agente serve
`topology.md` nella cartella team, compilato da `templates/TOPOLOGY-TEMPLATE.md` (tipo, nodi reali,
entry point, edges con contratti input→output, escalation, memory touchpoints, observability,
kill-criteria). La topologia è UNA pagina di puntatori: se non ci sta, il design è troppo complesso.
Nodi evocati ma non costruiti = agenti fantasma = FAIL gate (qa-gate checklist p.1).
Esempio vivente: `TOPOLOGY.md` del reparto stesso (dogfooding).

## R3 — FAILURE-MODES DI PRIMA CLASSE (invariante #6)
Ogni agente dichiara COME fallisce (tabella 5 colonne). Il gate conta le righe: <5 → FAIL.
Anti-recidiva: difetto ripetuto 2 volte → nuova regola qui (Ispettorato, dossier 15).

## R4 — NIENTE ORFANI: INTESTAZIONE ADR-008 (ADR-008 + direttiva Max 2026-07-20)
L'impero è una holding di workflow: ogni artefatto forgiato ha proprietario + controllore + origine +
governo REALI in testa, e viene registrato (REGISTRO-IMPRESA + skills-map). Artefatto non registrato
= artefatto abusivo (FORGE garantisce la registrazione come ultimo passo di ogni WF).
