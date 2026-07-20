# FORGE-PLAN — MIR-5 sprint 2: retrofit canonico di `skill-cro-ricerca` (Client Research Engine)

- **Data:** 2026-07-20 · **Owner:** fas-conductor · **Gate:** fas-qa-gate (verbale in memory/checkpoints/)
- **Trigger MIR-5 (P3 dossier 18):** retrofit formato canonico sui figli pre-impero, 1 figlio/sprint (sprint 1: youtube-script-factory ✅ CP-20260720-014).

## Scelta del secondo figlio (motivata — confronto candidati dal censimento)
| Candidato | Perché sì / perché no |
|---|---|
| **`SKILL & Agenti/SKILL/Skill CRO - Ricerca/`** ✅ SCELTA | ① dominio mio d'uso (04-MARKETING / W7: la ricerca alimenta hook/script video — ricerca ToV/pain/obiezioni = input dello script-factory) ② nessun python → nessun rischio estrazione (lezione s1) ③ non contesa (ultimo tocco: sync Max 2026-07-19, nessuna sessione attiva) ④ **manifest fantasma scoperto** (5 file referenziati assenti) → retrofit a valore diagnostico reale |
| `Skill CRO - call/` | RIMANDATA: 3 file da 4.3-5.2k righe con duplicato sospetto ("(2).md" vs senza estensione) → disambiguazione T1 richiederebbe ASK bloccante di Max; inoltre la decisione agenti-vendita dal MKD brand-offer è ancora in sospeso (ASK aperto) |
| `Skill CRO - Strategy social (Ig-tiktok)/` | RIMANDATA: il canone MKD brand-offer dice "non facciamo contenuti sui social" (servizio venduto ≠ marketing proprio) → richiede decisione Max (T3/T4) prima di canonizzarla |
| `Skill - script video lancio CCM/` | RIMANDATA: asset vivo con state JSON (`storico_script.json`, `social_performance.json`) + possibile contesa col filone Empire Studio (Gael) |
| Empire Studio Suite | VIETATA: Gael ci sta lavorando (ingestione video 11/29+) |

## Diamond (cosa produce lo sprint)
- Satelliti canonici nella cartella dell'asset (wrap ADR-003, `SKILL.md` e i 7 knowledge **mai** modificati):
  spec.md · tools.md (dichiarazione "nessun tool, by design") · playbook.md (4 scenari) · evals.md (7 casi) ·
  failure-modes.md (7 righe) · memory/INDEX.md
- MKD (questo folder `memory/mkd/`) con coverage atomi 26/26=100%.
- **Debiti dichiarati (non fixabili in wrap):** D1 manifest fantasma (5 template referenziati assenti —
  contenuti presenti inline nel master; il fix toccherebbe il master → vietato ADR-003) ·
  D2 deleghe verso skill non censite (CRO Copy Architect knowledge-only, Briefing Master Pro assente dal repo).
- Registrazione: skills-map entry esistente `skill-cro-ricerca` (note+alias, v1.6 — NIENTE duplicati),
  REGISTRO §3, wiki tool page, dossier 18 (MIR-5 avanzamento sprint 2).
- GATE retro-mode con delta dichiarati (manifest fantasma, pseudocodice narrante).

## ASK (MIR-3 — ASK-PROTOCOL)
| # | Domanda (1 decisione) | Opzioni | Raccomandazione | Default [ASSUNZIONE] | Trigger |
|---|---|---|---|---|---|
| Q1 | Id di registro in skills-map: rinumerare al name frontmatter o tenere l'esistente? | A) `client-research-engine` (name nel frontmatter) · B) tenere `skill-cro-ricerca` (entry censita v1.0, active) | **B** — l'entry ESISTE già dal censimento (a differenza di s1 dove era orfana): rinumerare = churn sul registro per zero valore; l'alias "Client Research Engine" va in `note` | B | T1 (naming/registry) |

*(T2-T4 assenti: il contenuto è completo e vivo; il manifest fantasma NON è oggetto di ASK perché l'unica
azione permessa dalle regole è dichiararlo come debito — correggerlo significherebbe toccare il master,
vietato da ADR-003; niente scelte economiche; wrap additivo senza conflitti di ownership.)*

## Handoff
Build inline (conductor). Gate: verbale retro-mode. Registrazione + CP globale `CP-20260720-015`.
**Candidato sprint 3 (proposto):** `📁 Skill — CRO Copy Architect — Knowledge Files/` (valle naturale di
questa ricerca; knowledge-only non censita → stesso protocollo, dimensione da verificare) — conferma nel
prossimo ciclo dopo merge di main.
