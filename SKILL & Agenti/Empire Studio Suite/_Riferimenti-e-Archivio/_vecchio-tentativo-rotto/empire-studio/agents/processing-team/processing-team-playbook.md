# Processing Team Playbook — Integrato con Strategy System (Step 3)

**Regola Obbligatoria**: Prima di iniziare qualsiasi video-watching, leggi il Strategy Manifest ricevuto dal Conductor.

## Come applicare il Manifest
- Se il Manifest dice "YouTube + Design System v1.1":
  - Estrai frame su ogni capitolo + export/demo.
  - Descrizioni visive devono essere dettagliate (>60 parole) e focalizzate su UI actions e risultati mostrati.
  - Ogni atomo deve avere trace a frame.

- Se il Manifest dice "TikTok + Automazioni":
  - Frame molto densi (ogni 5-10s o hook visivi).
  - Focus su "micro-passaggi" rapidi e tool output visibili.

## Flusso
1. Ricevi video list + Strategy Manifest.
2. Per ogni video: handoff a video-watcher-agent con vincoli dal Manifest.
3. Dopo output: fai audit interno contro regole Manifest.
4. Log "Strategy applied: [regole rispettate]" in memory.
5. Passa a Verification & Strategy Controller per controllo finale.

**Trace**: Integrazione strategia nei team L2 come richiesto.
