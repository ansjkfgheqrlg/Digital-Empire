---
intestazione_adr008: { proprietario: 01-AGENCY / Acquisizione (uso); FORGE-AGENT-SKILL (retrofit canonico, MIR-5 sprint 2), controllore: fas-qa-gate + METHOD-GUARD, origine: pre-Impero (Max) → retrofit wrap ADR-003 2026-07-20 (CP-20260720-015), governo: ADR-002/003/008/009 }
stato: legacy-wrapped (asset vivo, MAI toccare `SKILL.md` e i 7 knowledge — vincolo ADR-003)
alias: Client Research Engine (name frontmatter)
---

# SPEC — skill-cro-ricerca (Client Research Engine · Skill CRO Ricerca)

## Ruolo nell'impero
**Il sistema di intelligence prima di ogni copy e di ogni video.** Ricerca profonda nelle conversazioni
REALI del target (commenti YouTube, Reddit, X, recensioni, forum) per estrarre le ESATTE PAROLE, i VERI
PROBLEMI, le REALI OBIEZIONI e il linguaggio autentico — non buyer persona inventate. Produce il **Report
Ricerca a 10 sezioni** (pain scored I×F×A, obiezioni scored F×I, TOV con USA/EVITA, gap competitor, leve
emotive, swipe file 15 frasi) che è il prerequisito non negoziabile del CRO Copy Architect.
Divisione di lavoro strutturale: la skill GUIDA la ricerca (cosa/dove/query esatte), l'utente raccoglie,
la skill analizza e compila. Regola d'oro: *"Se non trovi le parole esatte del target, non hai cercato
abbastanza."* 5 fasi: R1 Audience → R2 Competitor → R3 TOV (parallela a R1) → R4 Pain → R5 Obiezioni →
Report. Tempi: full 5-10h, minima 2.5h. 10 regole non negoziabili (mai inventare dati, frasi esatte >
parafrasi, min 20 frasi, commenti > contenuti, scoring obbligatorio, segnala cosa manca, ogni dato ha
una fonte, top 5 non liste infinite…).

## Chi la usa (deleghe)
- **A monte:** Briefing Master Pro (skill citata dal master — ⚠️ NON trovata nel repo al 2026-07-20,
  vedi debito 2). Prerequisito: briefing cliente; se assente la skill si ferma e chiede.
- **A valle:** **CRO Copy Architect** (consuma il Report Ricerca). Esiste nel repo solo come cartella
  knowledge (`SKILL/📁 Skill — CRO Copy Architect — Knowledge Files/`, frameworks APP-SOC/CPB) NON censita
  in skills-map al 2026-07-20 → candidata MIR-5 sprint 3 (vedi PLAN).
- **Uso W7 YouTube (04-MARKETING):** la ricerca ToV/pain/obiezioni alimenta hook e script di
  `youtube-script-factory` (retrofit sprint 1) e la strategia `/youtube-lead-machine` — il master dichiara
  "YouTube Lead Engine" negli `other_uses`.
- **Confine:** questa skill RACCOGLIE e SCORA, non gestisce le obiezioni né scrive copy o strategia
  (handler esplicito `non_ricerca` nel master: indirizza a Copy Architect / Briefing / Agency Ops).

## Mappa canonica della sorgente (`SKILL.md` 1.625r + 7 knowledge reali — wrap: indice, non rilettura)
| Blocco | Righe | Contenuto | Formato canonico corrispondente |
|---|---|---|---|
| Frontmatter + identità | 1-46 | name "Client Research Engine", principio, limitazione operativa | kernel |
| Attivazione + ecosistema + I/O | 48-86 | FASE 3 Agency Ops, flow, input briefing, output Report 10 sezioni | spec (questo file) |
| KNOWLEDGE_FILES + CONSULTATION_ORDER | 87-257 | **MANIFEST di 5 template NON presenti in cartella** (debito 1) | — (fantasma dichiarato) |
| Processo R0-R5 + Report | 258-1275 | prerequisiti/piattaforme, R1 Audience, R2 Competitor, R3 TOV, R4 Pain (I×F×A), R5 Obiezioni (F×I), compilazione report | references equivalenti |
| Request handlers (9) | 1276-1417 | inizia / analizza_dati / genera_query / competitor / pain / obiezioni / report / parziale / non_ricerca | playbook |
| Tempi + 10 regole + TOV + quality standards | 1418-1625 | full 5-10h/min 2.5h; regole; TOV; 13 standard completi + 7 minimum | evals / failure-modes |
| Knowledge reali (7 file, 890r) | esterno | FILOSOFIA · YOUTUBE/REDDIT/X masterclass · PAIN 3 livelli · TOV 6 dimensioni · OBIEZIONI implicite · CROSS-PLATFORM pattern | references reali |

## Debito documentato (onesto, R2-delta)
1. **Manifest fantasma**: `SKILL.md` §KNOWLEDGE_FILES (r. 87-257) referenzia come prioritarie 5 risorse che
   **non esistono in cartella**: `Template-Report-Ricerca.md` (★★★★★), `Checklist-Query-Piattaforme.md` (★★★★★),
   `Scheda-Analisi-Competitor.md`, `Template-Pain-Points-Scoring.md`, `Template-Obiezioni-Scoring.md`.
   I loro contenuti esistono **inline** nel master (fasi R1-R5 dettagliate + report 10 sezioni + scoring) e
   nei 7 knowledge reali — quindi l'asset FUNZIONA, ma il manifest è desync. **Non fixato** perché richiede
   di toccare il master (vietato ADR-003). Regola operativa del wrap: **il corpo dello SKILL.md vince sul
   manifest**; se Max decide una v2 ripulita → progetto separato con validazione (ADR-003).
2. **Monte non censito**: Briefing Master Pro (skill a monte dichiarata) non presente nel repo al 2026-07-20;
   CRO Copy Architect presente solo come knowledge dir non censita. Non blocca l'uso (STEP 0 gestisce il
   briefing assente chiedendo i dati minimi), ma la catena dichiarata non è completa in anagrafe.
3. **Pseudocodice narrante**: il master usa blocchi ```python non eseguibili come notazione procedurale
   (stile pre-impero; `tools: []` nel frontmatter). Non è debito funzionale — è il formato storico.
   `tools.md` dichiara esplicitamente: nessun tool da installare/estrarre.

## File di questo wrap (retrofit MIR-5 sprint 2)
`spec.md` (questo) · `tools.md` (dichiarazione nessun-tool + standard qualità) · `playbook.md` (4 scenari) ·
`evals.md` (7 casi) · `failure-modes.md` (7 righe) · `memory/INDEX.md` — MKD in
`FORGE-AGENT-SKILL/memory/mkd/MKD-retrofit-client-research-engine.md` · PLAN in `…/memory/plans/PLAN-retrofit-client-research-engine.md`.
