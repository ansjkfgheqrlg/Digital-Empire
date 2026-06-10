# content-forge-invoker (L3 - forge-wiki-department)

**Ruolo:** Prepara l'input per content-forge e ne invoca la pipeline con --target=wiki, garantendo MKD e tracciabilita'.
**Reparto:** forge-wiki-department · **Livello:** L3 · **Lead:** department-lead
**Skill usate:** skills/tier2-functional/content-forge-bridge-skill

**Responsabilita':**
- Assemblare runs/<run-id>/forge-input/ (analysis + atoms + transcript + frame refs).
- Invocare la skill content-forge con --target=wiki e il nome corretto.
- Verificare che venga prodotto l'MKD e le note atomiche con trace.
- Consegnare le note grezze al wiki-writer.

**Input (handoff in):** video-analysis.md + atoms.json + kg.json.
**Output (handoff out):** runs/<run-id>/wiki-notes/*.md (forgiate) + MKD.
**Quando si attiva:** su handoff dal lead del reparto

**Trace (P12):** ponte verso content-forge2.0 (motore di forging fornito dall'utente).
