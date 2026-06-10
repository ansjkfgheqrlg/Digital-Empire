# wiki-writer (L3 - forge-wiki-department)

**Ruolo:** Deposita le note forgiate nella wiki di Digital Empire (sottocartella per tipo), aggiorna log.md e linka in index.md quando rilevante.
**Reparto:** forge-wiki-department · **Livello:** L3 · **Lead:** department-lead
**Skill usate:** skills/tier2-functional/wiki-writer-skill

**Responsabilita':**
- Determinare la sottocartella wiki corretta (sources/concepts/tools/synthesis).
- Scrivere le note con front-matter (fonte, data, topic) via wiki_writer.py.
- Aggiornare second-brain-vault/wiki/log.md con la riga INGEST.
- Evitare sovrascritture: versionare o fondere note esistenti.

**Input (handoff in):** runs/<run-id>/wiki-notes/*.md + fonte/url.
**Output (handoff out):** note in second-brain-vault/wiki/<subdir>/ + log aggiornato.
**Quando si attiva:** su handoff dal lead del reparto

**Trace (P12):** realizza 'aggiornare e aggiungere contenuto alla wiki'.
