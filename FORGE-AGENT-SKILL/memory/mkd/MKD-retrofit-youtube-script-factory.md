# MKD — retrofit youtube-script-factory (MIR-5 sprint 1)

**Sorgente:** `SKILL & Agenti/SKILL/Skill CRO - Youtube - Lead magnet/Skill-youtube.md` (5.166 righe, 9 sezioni).
**Metodo:** mappa atomi integrale (R1: niente riassunti — il contenuto resta DOVE È; questo file è l'indice
di copertura del wrap, con riferimenti a righe). ➕ = aggiunta del retrofitta.

## Copertura atomi (coverage target 100% della struttura; il contenuto non si sposta — ADR-003)

| # | Atomo sorgente | Dove (righe) | Mappato nel wrap |
|---|---|---|---|
| 1 | Principio fondamentale (script=problema del viewer) | 15-44 | spec §ruolo + playbook S1 |
| 2 | VOCE DE non negoziabile (✅/❌ lista) | 45-67 | spec §ruolo + playbook S1.4 (richiamo operativo) |
| 3 | Relazione col sistema (canale, funnel) | 68-91 | spec §deleghe |
| 4 | Checklist pre-scrittura | 92-110 | playbook S1 |
| 5 | 7 componenti script (elenco+ordine) | 111-138 | spec §ruolo, SEZ 6 quick ref |
| 6 | Tipi video: ANCHOR 70 / SHIFT 20 / CONVERSION+AUDIT 10 | 139-165 | spec §ruolo + tools.md §backlog mix |
| 7 | CTA 3 livelli (Preview/Reminder/Finale + 3 varianti) | 166-177 | playbook S1.4 + evals E1 + failure F2 |
| 8 | Ottimizzazione (6 formule titoli <60c, thumbnail 4-5 parole, description, pinned) | 178-186 | playbook S2 + evals E2 |
| 9 | Quality check (scoring; ⚠️ scala "30+" legacy vs 45pt reale) | 187-196 | spec §debito 2 + failure F3 |
| 10 | Workflow operativo (scrittura + altri scenari) | 197-234 | playbook S1-S4 |
| 11 | Output format | 235-246 | playbook S1.6 + tools.md §output JSON |
| 12 | Componenti dettaglio (hook, setup, credibilità 5 formule, contenuto core…) | 247-1888 | spec §mappa (references equivalenti) |
| 13 | Checklist 45 punti + report template + pesi sezioni + errori top10 | 1889-1988 | tools/checklist_qualita.py (fonte scoring) + failure F3 |
| 14 | Cheat sheet (matrice hook, strutture/tipo, 6 titoli, thumbnail, 5 mantra, scoring, output rapido) | 1989-2204 | spec §debito 1 ("kernel operativo") + evals E7-pratica |
| 15 | `genera_script.py` embedded | 2205-3470 | **tools/genera_script.py** (estrato, py_compile ✅) |
| 16 | `checklist_qualita.py` embedded (45pt/11 sezioni, interattiva) | 3471-4389 | **tools/checklist_qualita.py** (estrato, py_compile ✅) |
| 17 | `backlog_manager.py` embedded (mix 70/20/10, performance, piano settimanale) | 4390-5166 | **tools/backlog_manager.py** (estrato, py_compile ✅) |
| ➕18 | Deleghe cross-skill non dichiarate nel file | — | spec §chi-la-usa (da gate `/youtube-lead-machine` 2026-07-20) |
| ➕19 | Stato registrazione: skill ATTIVA ma assente da skills-map/REGISTRO (orfana ADR-008) | — | risolto sprint 1 (skills-map v1.5 + REGISTRO §3) |
| ➕20 | Tool prima non eseguibili (embed-only) | — | risolto: `tools/` + regola deriva (md vince) |

**Coverage: 17/17 atomi strutturali = 100%.** ➕ 18-20 = fatti di sistema aggiunti (deleghe/registrazione/eseguibilità), NON contenuto inventato.
