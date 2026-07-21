# Playbook — chief-forge
## Attivazione task (da workflows.yaml)
1. Leggi PLANNING-P7 §2 corsia di oggi + gate in scadenza (WF-MASTER).
2. Prende il task con €/h più alto non assegnato. Prima di costruire: `checkpoint --task WF-x-start`.
3. Costruisci con i motori esistenti; per contenuto grezzo→artefatto usa 05-SKILLS/content-forge2.0 (/forge).
4. Verifica DoD congelata. Testo reale: checkout → test €1; pipeline → run E2E visibile; video → file pubblicato.
5. Chiudi: `checkpoint --task WF-x` + `metric` se KPI. Aggiorna dashboard se gate.
## Sequenza settimana (corsia Gael): CF-R8 close → audit → funnel S2 → caroselli S3 + test Fliki → gate S4 + kit S6 → WF-YT → RETRO.
## Slittamenti: ordine sacrificio S5→S4→S6→S3; dichiarare con `error --wf ... --note "slitta"`.
