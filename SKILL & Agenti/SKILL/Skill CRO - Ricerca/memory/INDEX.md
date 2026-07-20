# 🧠 MEMORY — skill-cro-ricerca / Client Research Engine (indice locale, ADR-002)

## Stato
- **2026-07-20: RETROFIT MIR-5 sprint 2** — wrap canonico aggiunto: spec/tools/playbook/evals/failure-modes
  + memory locale (questo file). Master `SKILL.md` (1.625r) e i 7 knowledge **intoccati** (ADR-003, diff=0).
- Registrata in `company/skills-map.yaml` fin dal censimento v1.0 (`skill-cro-ricerca`, 01-AGENCY/Acquisizione)
  → NON orfana; v1.6 aggiorna la nota (alias + riferimento retrofit). REGISTRO-IMPRESA §3 idem.
- MKD/piano in `FORGE-AGENT-SKILL/memory/{mkd,plans}/` (MKD-retrofit-… e PLAN-retrofit-client-research-engine).

## Puntatori operativi
- **Manifest fantasma** (spec §debito 1): i 5 template del §KNOWLEDGE_FILES non sono file; i contenuti
  sono inline nel master. Regola: **il corpo dello SKILL.md vince sul manifest**.
- Nessun tool eseguibile (by design, `tools: []`): guida utente → utente raccoglie → skill compila.
- Gate qualità = §STANDARD del master (13 complete / 7 minimum) — riassunto operativo in tools.md.
- Deleghe: copy/obiezioni-gestione → CRO Copy Architect (knowledge dir non censita); monte → Briefing
  Master Pro (assente dal repo al 2026-07-20 — dichiarato, STEP 0 copre con dati minimi).
- Uso W7: ricerca → hook/obiezioni/TOV per `youtube-script-factory` (playbook S4).

## Backlog
- Se Max approva una v2 ripulita del manifest (5 template referenziati → inventario allineato):
  progetto separato, validazione nuova-vs-vecchia PRIMA dello switch (ADR-003). Mai edit diretto del master.
- Eventuale censimento/retrofit di CRO Copy Architect → candidato MIR-5 sprint 3 (vedi PLAN).
