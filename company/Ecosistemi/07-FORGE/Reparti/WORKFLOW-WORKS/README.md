# Reparto L2.3 — WORKFLOW-WORKS (forgia workflow e orchestrazioni)

> **Ecosistema:** 07-FORGE · **Livello:** L2 · **Owner:** Chief-Forge (`frg-chief`)
> Workflow L3: `../../Workflow/WF-FORGE-PIPELINE/` · `../../Workflow/WF-PRD/`

## Cosa fa

WORKFLOW-WORKS trasforma materia prima e requisiti in **documenti operativi e
orchestrazioni**: è il reparto dove vivono i due strumenti documentali più potenti
della FORGE.

1. **WF-FORGE-PIPELINE** (motore: **content-forge**, `SKILL & Agenti/Content-forge/skill - FINALE/`,
   433 file) — da raw (transcript YouTube, registrazioni workshop, appunti sparsi,
   brief interni, intere cartelle) a uno di 8 target: documento espanso, agente,
   team multi-agente, skill Anthropic, workflow eseguibile, orchestration layer,
   nota wiki Obsidian, injection custom (system prompt n8n/CrewAI/LangGraph, RAG pack,
   template parametrizzato). **Passaggio obbligato: l'MKD** (Master Knowledge Document),
   il "documento perfetto" intermedio. Regola assoluta: **mai riassumere, sempre
   espandere** — ogni atomo informativo della fonte diventa più ricco, strutturato,
   con esempi e cross-reference aggiunti.
2. **WF-PRD** (motore: **prd-architect-os**) — PRD tipo A (Enterprise 10-30 pagine),
   B (MVP Lean), C (Feature Spec), D (Vibecoding AI-Ready), E (PR/FAQ Amazon-style).
   Processo a 4 engine: Intake → Context Enrichment → Generation → Validation.
   Ogni PRD chiude con quality score 0-100; **generazione bloccata se context score <60**.

## Come si collega

| Con | Relazione |
|---|---|
| INTELLIGENCE / Empire Studio | fornitore primario di materia prima: contenuto ingerito INTEGRALE → input di content-forge (fase F2 della build FORGE) |
| SKILL-WORKS | quando il target dell'MKD è una skill → handoff a WF-SKILL-NEW per eval e package |
| AGENT-WORKS | quando il target è agente/team → handoff a WF-AGENT-NEW / WF-TEAM-NEW |
| PLATFORM | i PRD tipo B/D alimentano WF-SAAS-BUILD (PLATFORM costruisce, FORGE specifica) |
| METHOD-GUARD | il PRD/MKD è il deliverable della fase S-P di SPARC: frg-sparc-warden lo esige prima di ogni build |

Agenti: `frg-mkd-forger` (operatore content-forge), `frg-prd-architect`
(operatore prd-architect-os).

## 🧠 Come si ATTIVA e RAGIONA

**Attivazione.** Due strade: (a) ordine di `frg-chief` con materia prima allegata o
referenziata ("trasforma questo materiale in X"); (b) chiamata interna dagli altri
reparti FORGE che hanno bisogno del documento intermedio (G-MKD/PRD). Il principio
di Memory Empire vale anche qui: content-forge **non si invoca mai "a mano"** —
lo usano gli agenti (qui `frg-mkd-forger`; in ingestione, gli agenti di Empire Studio).

**Ragionamento:**
1. **Classifica la fonte** — raw testuale/cartella → content-forge; idea di prodotto /
   requisiti → prd-architect-os. Mai forzare il motore sbagliato.
2. **Context check d'ingresso** — content-forge: la fonte è completa? (se è un riassunto
   di seconda mano → chiedere a INTELLIGENCE l'originale integrale, G-INTEGRAL).
   PRD: context score ≥60 o si torna all'intake.
3. **MKD come contratto** — l'MKD non è un appunto: è la spec completa da cui QUALSIASI
   target può essere costruito. Se l'MKD è debole, ogni artefatto a valle è debole.
4. **Espandere, mai comprimere** — ogni atomo della fonte va arricchito (esempi, schemi,
   collegamenti); un MKD più corto della fonte è un bug.
5. **Un target alla volta** — dall'MKD si forgia il target richiesto; altri target
   restano forgiabili dopo (l'MKD si archivia, namespace `forge/builds`).
6. **Quality score sempre** — PRD <75/100 non si consegna: si itera su Validation.

**Anti-pattern vietati:** saltare l'MKD "perché la fonte è corta"; consegnare PRD con
context score sotto soglia; riassumere; buttare l'MKD dopo la build (è un asset riusabile).

*Fonte: `PIANO-MAESTRO/06-ECOSISTEMI-CORE.md` §07 L2 WORKFLOW-WORKS · Aggiornato: 2026-06-11*
