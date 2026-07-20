# MKD — retrofit skill-cro-ricerca / Client Research Engine (MIR-5 sprint 2)

**Sorgente:** `SKILL & Agenti/SKILL/Skill CRO - Ricerca/` — master `SKILL.md` (1.625 righe) + 7 knowledge
file reali (890 righe). Frontmatter name: **"Client Research Engine"**.
**Metodo:** mappa atomi integrale (R1: niente riassunti — il contenuto resta DOVE È; questo file è l'indice
di copertura del wrap, con riferimenti a righe). ➕ = aggiunta del retrofitta.

## Copertura atomi (coverage target 100% della struttura; il contenuto non si sposta — ADR-003)

| # | Atomo sorgente | Dove (righe) | Mappato nel wrap |
|---|---|---|---|
| 1 | Frontmatter (name, description 5 fasi, model, tools []) | 1-7 | spec §intestazione |
| 2 | Identità + principio fondamentale ("parole esatte del target"; regola d'oro) | 10-38 | spec §ruolo + playbook S1 |
| 3 | Limitazione operativa (TU GUIDI / utente raccoglie / TU ANALIZZI) | 40-46 | spec §ruolo + playbook S1 + failure F2 |
| 4 | Attivazione (FASE 3 Agency Ops, prerequisito CRO Copy Architect) + flow ecosistema | 48-77 | spec §deleghe + playbook S4 |
| 5 | INPUT (briefing completo) / OUTPUT (Report Ricerca 10 sezioni) | 78-86 | spec §ruolo + evals E1 |
| 6 | Mappa KNOWLEDGE_FILES + CONSULTATION_ORDER — **5 file referenziati ASSENTI** | 87-257 | spec §debito 1 (manifest fantasma) + failure F1 |
| 7 | STEP 0-1: prerequisiti (8 campi) + selezione piattaforme (B2B/B2C/IT/INT) | 258-369 | playbook S1 + failure F5 |
| 8 | FASE R1 Audience (YouTube/Reddit/Google/LinkedIn/Amazon/FB/Trustpilot; min 20 frasi) | 370-624 | playbook S1 + spec §mappa + evals E2 |
| 9 | FASE R2 Competitor (3 diretti + 2 indiretti, scheda completa) | 625-735 | playbook S2 + evals E3 |
| 10 | FASE R3 TOV extraction (parallela a R1; tabella USA/EVITA 10+ coppie) | 736-826 | playbook S2 + spec §mappa |
| 11 | FASE R4 Pain points (4 categorie, scoring I×F×A, top 5-7 + leve emotive) | 827-965 | playbook S2 + evals E4 |
| 12 | FASE R5 Obiezioni (5 categorie, scoring F×I, top 5-7; RACCOGLI non gestire) | 966-1120 | playbook S2 + evals E5 + failure F3 |
| 13 | STEP FINALE: compilazione Report 10 sezioni | 1121-1275 | playbook S3 + evals E6 |
| 14 | 9 request handlers (inizia/analizza/genera_query/competitor/pain/obiezioni/report/parziale/non_ricerca) | 1276-1417 | playbook S1-S4 + failure F4 |
| 15 | Tempi (full 5-10h; minima 2.5h) | 1418-1472 | playbook S4 + spec §debito 2 |
| 16 | 10 regole non negoziabili | 1473-1568 | spec §ruolo (richiamo) + evals cross + failure F1/F2/F6 |
| 17 | TOV (comunicazione utente + stile report) | 1569-1590 | playbook S3 + failure F6 |
| 18 | Quality standards (13 voci complete + 7 minimum) | 1591-1625 | evals E6 (gate) + tools.md §nessun-tool |
| 19 | Knowledge reale: FILOSOFIA DELLA RICERCA (come pensare prima di cercare) | file esterno 96r | spec §mappa knowledge |
| 20 | Knowledge reale: YOUTUBE masterclass (commenti = pain puri, contesto apprendimento) | file esterno 310r | spec §mappa knowledge + playbook S1 |
| 21 | Knowledge reale: REDDIT masterclass (anonimato=onestà, threading, upvotes=consenso) | file esterno 256r | spec §mappa knowledge + playbook S1 |
| 22 | Knowledge reale: X TWITTER masterclass (real-time, sintesi tagliente, thread, quote) | file esterno 199r | spec §mappa knowledge |
| 23 | Knowledge reale: PAIN POINTS avanzata (3 livelli di profondità oltre il superficiale) | file esterno 212r | spec §mappa knowledge + playbook S2 |
| 24 | Knowledge reale: TOV avanzato (6 dimensioni oltre formale/informale) | file esterno 137r | spec §mappa knowledge + playbook S2 |
| 25 | Knowledge reale: OBIEZIONI avanzate (esplicite vs implicite → comportamento) | file esterno 135r | spec §mappa knowledge + playbook S2 |
| 26 | Knowledge reale: CROSS-PLATFORM (pattern su 3 piattaforme = pattern di mercato → priorità #1) | file esterno 91r | spec §mappa knowledge + evals E7 |
| ➕27 | Manifest fantasma: 5 template referenziati ma mai presenti in cartella | — | debito D1 dichiarato in spec (fix = toccare master → vietato ADR-003) |
| ➕28 | Zero tool eseguibili (pseudocodice python-narrante, `tools: []` nel frontmatter) | — | tools.md dichiara esplicitamente "nessun tool" (non è debito: è by-design) |
| ➕29 | Deleghe a valle: CRO Copy Architect esiste come cartella knowledge NON censita (`SKILL/📁 Skill — CRO Copy Architect — Knowledge Files/`); Briefing Master Pro NON trovato nel repo | — | spec §deleghe + candidato MIR-5 sprint 3 nel PLAN |
| ➕30 | Registrazione: GIÀ in skills-map (v1.0 censimento, entry `skill-cro-ricerca`) → NON orfana | — | aggiornamento note entry v1.6 (niente duplicati) |

**Coverage: 26/26 atomi strutturali = 100%.** ➕ 27-30 = fatti di sistema aggiunti (manifest/registrazione/
deleghe/design), NON contenuto inventato.
