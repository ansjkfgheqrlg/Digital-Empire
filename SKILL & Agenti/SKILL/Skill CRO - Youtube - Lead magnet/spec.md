---
intestazione_adr008: { proprietario: 04-MARKETING / W7 YouTube Lead Machine (uso); FORGE-AGENT-SKILL (retrofit canonico, MIR-5 sprint 1), controllore: fas-qa-gate + METHOD-GUARD, origine: pre-Impero (Max) → retrofit wrap ADR-003 2026-07-20 (CP-20260720-014), governo: ADR-002/003/008/009 }
stato: legacy-wrapped (asset vivo, MAI toccare `Skill-youtube.md` — vincolo ADR-003)
---

# SPEC — youtube-script-factory (Skill CRO YouTube Lead Magnet)

## Ruolo nell'impero
**La fabbrica degli script del canale W7.** Sistema completo di scrittura script YouTube lead-generation
per Digital Empire (agenzia CRO): 7 componenti (Hook, Setup, Credibilità, Contenuto Core, Ricap, CTA,
Retention Hooks), 20 formule hook in 4 categorie, strutture per 4 tipi video (Anchor 70% / Shift 20% /
Conversion 10% / Audit live), sistema CTA a 3 livelli (Preview/Reminder/Finale), 10 pattern retention,
6 formule titolo, checklist qualità 45 punti con scoring, backlog manager contenuti.

## Chi la usa (deleghe attive — dal gate di `/youtube-lead-machine`)
- **`/youtube-lead-machine`** (skill forgiata da FORGE-AGENT-SKILL, 2026-07-20): fornisce strategia canale,
  funnel, batch, analytics. **Delega la SCRITTURA SCRIPT a questa factory** (contratto: output = script
  formato 7-componenti + score qualità ≥30/45 prima di programmare la registrazione).
- **QA copy** resta delegato a `copy-workflow` (APSOC) — questa factory NON fa review APSOC, ha il proprio
  scoring 45-punti interno (due sistemi, non confonderli: 45-pt = qualità script video, APSOC = copy marketing).

## Mappa canonica della sorgente (`Skill-youtube.md`, 5.166 righe — wrap: indice, non rilettura integrale)
| Sezione | Righe | Contenuto | Formato canonico corrispondente |
|---|---|---|---|
| 1 (principi) | 11-246 | Principio fondamentale, VOCE DE non negoziabile, 7 componenti, tipi video, CTA 3L, ottimizzazione, QC, workflow, output format | kernel equivalente |
| 2-5 | 247-1988 | Dettaglio componenti (hook/setup/credibilità/core/…), 20 hook, checklist 45pt, report qualità, errori top10 | references equivalenti |
| 6 | 1989-2204 | Cheat sheet rapido (matrice hook, strutture per tipo, 6 formule titoli, thumbnail, 5 mantra, scoring) | quick reference |
| 7 | 2205-3470 | `genera_script.py` embedded | **estrato → `tools/genera_script.py`** |
| 8 | 3471-4389 | `checklist_qualita.py` embedded (45pt, 11 sezioni) | **estrato → `tools/checklist_qualita.py`** |
| 9 | 4390-5166 | `backlog_manager.py` embedded (mix 70/20/10, priorità, performance, piano settimanale) | **estrato → `tools/backlog_manager.py`** |

## Debito documentato (onesto, R2-delta)
1. **Kernel oversize**: 5.166 righe vs ≤550 del formato skill canonico → l'asset resta com'è (vincolo ADR-003:
   funziona e è vivo). Usare SEZIONE 6 (cheat sheet, ~215 righe) come "kernel operativo" di consulenza rapida
   e l'indice qui sopra per navigare. Eventuale v2 ristrutturata = progetto separato, solo dopo validazione
   (ADR-003: il sostituto deve essere provato PRIMA).
2. **Due scale scoring citate**: §1 QC dice "30+ punti" mentre SEZ 5/8 sono su **45 punti** → la scala
   canonica è 45 (tool `checklist_qualita.py` è la fonte); trattare "30+" del §1 come soglia approssimativa legacy.
3. **Python embed-only (RISOLTO sprint 1)**: fino al 2026-07-20 i 3 script esistevano solo nel markdown
   (comandi `python3 …` non eseguibili) → ora estratti in `tools/` (compilano 3/3). Regola di deriva:
   **il markdown vince** — se `Skill-youtube.md` cambia le sezioni 7-9, ri-estrarre e recompilare.

## File di questo wrap (retrofit MIR-5 sprint 1)
`spec.md` (questo) · `tools.md` (catalogo tool) · `playbook.md` (uso operativo) · `evals.md` ·
`failure-modes.md` · `memory/INDEX.md` · `tools/*.py` (3 estratti) — MKD in
`FORGE-AGENT-SKILL/memory/mkd/MKD-retrofit-youtube-script-factory.md` · PLAN in `…/memory/plans/PLAN-retrofit-youtube-script-factory.md`.
