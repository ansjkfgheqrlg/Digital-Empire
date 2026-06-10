# CS02 — La Nascita del Team Ox (Phase 9, Depth Architecture)

> **Setting**: Phase 9, post-test reali su sorgenti reali dell'utente
> **Personaggi**: l'utente che ha appena testato la skill v1.0 su contenuto reale + l'agente che riceve i 2 report
> **Esito**: aggiunta di Stage 7 con 5 nuovi agenti optimizer (team Ox), tightening dello schema, builder updates
> **Lezione cardine**: i bug più costosi sono quelli che lo schema permissivo lascia passare. Schema stringente è guardian, non burocrazia.

---

## 1. Il contesto (dove eravamo)

Avevamo appena chiuso Phase 8 — packaging v1.0. La skill era installabile. 199 file. 320 KB. 56 test pytest verdi. Tutto sembrava solido.

L'utente l'aveva installata e l'aveva usata. **Due test reali**:

**Test 1**: aveva passato un transcript reale (4 video YouTube su "come fare preventivi") e chiesto `target=skill`. Output: `beast-preventivi`.

**Test 2**: aveva passato un libro intero (215 pagine sul copywriting) e chiesto `target=orchestration` con sub-skill, sub-agenti, workflow. Output: `copy-workflow`.

Poi mi è arrivato il suo report. Era lungo. Strutturato. Aveva preso il tempo di descrivere cosa funzionava e cosa no, con esempi concreti del filesystem prodotto.

Il tono iniziale era positivo:

> "Devo dire innanzitutto che funziona molto bene, ma va assolutamente posizionata e migliorata molto."

Poi è entrato nel dettaglio. E mi è cascato il sorriso.

## 2. I 3 bug che mi ha riportato (in sequenza)

### Bug A — beast-preventivi senza agenti interni

Mi ha scritto:

> "Come vedi il risultato è una buona skill veramente buona. Però vorrei notare che all'interno di questa skill non ci sono degli agenti. E questo è un problema, soprattutto per una skill come questa, ma in generale per ogni skill deve avere degli agenti che si coordinano e che appunto fanno ognuno il suo lavoro. Insomma i classici agenti che ci devono essere in ogni skill. Gli agenti operativi, gli agenti verificatori che controllano. E ad esempio anche gli agenti formulari, quelli che controllano che tutte le formule siano state rispettate. Poi anche per tutte le skill in cui si deve scrivere copy ci deve essere sicuramente un agente che si occupa di rendere il testo più umano possibile."

Lettura: la skill output funzionava strutturalmente, ma era un **set di reference + script senza nessun agente operativo interno**. Per una skill complessa come "fare preventivi", senza agenti interni l'utente finale non aveva chi orchestrasse la logica.

### Bug B — copy-workflow con sub-skill da 1 solo file

Per il secondo test, il problema era diverso:

> "In questo workflow ci sono sei skill. Adesso parliamoci chiaro, ognuna di quelle skill ha solamente un file .md. Estremamente anche secondo me ridotto. E comunque, parliamoci chiaro, non è normale che in una skill ci sia soltanto un file markdown. Insomma, dove sono i file reference? Mancano tutti. Non ci sono. Poi servono anche altri file reference o script Python. Poi ovviamente dipende a seconda delle varie skill, ma insomma dentro una skill deve essere minimo una cartella con i concetti, con le formule, con gli asset."

Lettura: l'output era 6 sub-skill, ma ognuna era uno **scaffold di un solo file `SKILL.md`**. Niente `references/`, niente `evals/`, niente di sostanziale. La skill validator era passata perché lo schema v0.2 era permissivo (non aveva `references_min_files: 3`).

### Bug C — Agenti corti

Continuando:

> "E inoltre andiamo anche a fondo a vedere ogni singolo agente. Non sono avanzati, anzi sono veramente corti, hanno veramente sono agenti piccoli. Non vedo neanche un agente che abbia una struttura completa, estremamente completa. E questo non va bene."

Per gli 8 agenti dentro `copy-workflow`, ognuno aveva 2/7 file canonici (solo `agent.md` + `system_prompt.md`). Mancavano `tools.md`, `playbook.md`, `failure_modes.md`, `eval_cases.json`, `README.md`.

## 3. Il momento di reazione

Avevo 2 opzioni immediate:

### Opzione difensiva (no)
"Beh la skill funziona, il validator passa, l'utente può espandere a mano..."

Sarebbe stato disastroso. L'utente aveva ragione su ogni punto. Il fatto che il validator passasse era **parte del problema**, non difesa.

### Opzione introspettiva (sì)
Riconoscere: "non è solo che ho fatto qualche bug. C'è qualcosa di sistemico che ha permesso a questi bug di emergere insieme. Quale?"

Ho preso l'opzione 2. Mi sono fermato a pensare cosa avevano in comune i 3 bug.

## 4. La diagnosi profonda (cosa avevano in comune i 3 bug)

I 3 bug sembravano diversi:
- A: skill senza agenti
- B: sub-skill thin
- C: agenti incompleti

Ma erano **lo stesso bug a 3 livelli**: il sistema accettava **scaffold come deliverable**.

Lo schema v0.2 era così permissivo:
- "Una skill è valida se ha SKILL.md" → Bug B (skill con 1 file passa)
- "Un agente è valido se ha agent.md" → Bug C (agente con 2/7 file passa)
- Nessuno schema diceva "skill complessa DEVE avere agenti" → Bug A

E i builder avevano questa permissività interiorizzata: producevano il **minimo necessario per passare il validator**. Né più né meno.

Tradotto in 1 frase: **schema permissivo → builder lazy → utente riceve scaffold**.

## 5. Le alternative di fix considerate

Ho considerato 3 strati di intervento, ognuno con costi/benefici diversi.

### Strato 1 — Fix solo schema (più veloce)

Tightening dello schema: aggiungere `references_min_files: 3`, `playbook_min_conversations: 5`, ecc. Schema diventa stringente. Builder costretti a produrre più ricchezza.

**Pro**: implementation breve (1 giorno), no nuovi agenti.
**Contro**: i builder esistenti non sapevano come produrre output ricco. Avrebbero generato scaffold più grandi (riempitivo), non sostanziosamente migliori. Schema avrebbe avuto false-positive da regression.

### Strato 2 — Fix schema + update builder

Strato 1 + revisione dei system prompt di tutti i builder per insegnare loro a produrre output ricco fin dall'inizio.

**Pro**: builder migliori, schema più rigoroso.
**Contro**: serve riscrivere ~8 SP di builder (B1-B8) in modo coerente. Inoltre, non sempre il builder sa come arricchire (es. quanti esempi per atomo nel playbook?). Manca expertise specializzata.

### Strato 3 — Schema + builder + team optimizer dedicato (la scelta)

Strato 2 + **nuovo Stage 7 con 5 agenti optimizer dedicati** che lavorano sull'output del builder, arricchendolo prima della QA.

**Pro**: separation of concerns. Builder fa struttura, optimizer fa depth. Modulare, estensibile, ogni optimizer specializzato in una dimensione di qualità.
**Contro**: complessità implementation più alta (5 nuovi agenti + 1 nuovo stage). Costo run aumenta 2-3x.

## 6. Perché ho scelto Strato 3

Tre ragioni convergenti:

### 6a. Single-responsibility per agent type

Builder ha già scope ampio (deve conoscere shape canonica, produrre file canonici, fare ASK phase, ecc.). Aggiungere "fai anche arricchimento depth" significava sovraccaricarlo. Builder di 2000 parole di SP → quality degrada.

Separare: Builder fa DRAFT strutturalmente valido. Optimizer fa rifinitura. Ogni agente con SP focused.

### 6b. Estensibilità futura

Strato 1 e 2 sono "fix one-off". Strato 3 crea un **pattern riusabile** (PT03 — Builder then Optimizer). In futuro voglio aggiungere nuovo tipo di depth check? Aggiungo nuovo optimizer in `agents/optimizers/`. Niente touch al builder.

### 6c. Forzava il pensiero su "cos'è qualità completa"

Per definire i 5 optimizer (O1-O5), ho dovuto identificare le 5 dimensioni di qualità:
- O1 skill-depth: struttura skill (refs, evals)
- O2 agent-depth: completezza agenti (7/7 file)
- O3 reference-expander: depth content (50→300 righe)
- O4 humanizer: anti-LLM-speak
- O5 formula-validator: completezza framework

Senza questa divisione, "qualità" rimane vago. Con, è enumerable + verificable.

## 7. La decisione e la roadmap proposta

Ho risposto all'utente con un'analisi articolata. Estratto:

> "**Hai ragione su tutto.** La diagnosi è precisa.
>
> I due problemi che hai trovato sono **reali e gravi** [...]
>
> ## Il problema vero ha 3 strati
>
> ```
> Strato 1 — UPSTREAM (la causa)
>   └─ I builder non producono output abbastanza ricco
>      ↓
> Strato 2 — VALIDATION GAP (cosa lo lascia passare)
>   └─ Gli schema sono troppo permissivi
>      ↓
> Strato 3 — DOWNSTREAM (cosa ottieni alla fine)
>   └─ Output magro, anche se sintatticamente valido
> ```
>
> Il tuo optimizer team è una soluzione allo Strato 3 [...]"

Ho proposto Phase 9 con 3 mosse parallele:

1. **Mossa 1**: 5 agenti optimizer (O1-O5)
2. **Mossa 2**: schema tightening v0.2 → v0.3
3. **Mossa 3**: builder improvements (depth-aware)

Più una mossa 4: regression test sui suoi 2 sorgenti originali per misurare miglioramento prima/dopo.

L'utente ha confermato tutte e 3 le mosse. Poi mi ha dato un input cruciale: voleva 5 optimizer (non 3 core), humanizer condizionale via tag KG.

## 8. Le 9 sub-phase di esecuzione

Phase 9 è diventata la phase più articolata fino a quel momento:

| Sub-phase | Cosa | Tempo stimato |
|---|---|---|
| 9.1 | PLAN-v6 con 3 strati | 30 min |
| 9.2 | 5 agenti optimizer in `agents/optimizers/` | 1h |
| 9.3 | Nuovo stage doc + renumber stages 07→08, 08→09 | 30 min |
| 9.4 | Update conductor per pipeline 9-stage + Depth Conductor | 30 min |
| 9.5 | Schema tightening (5 schemi → v0.3) | 1h |
| 9.6 | Update builder agents (B2-B6) "Depth Awareness" | 1h |
| 9.7 | Update C3 + 13 nuovi test pytest | 30 min |
| 9.8 | Regression test reale sui 2 sorgenti | 1-2h |
| 9.9 | Re-package v1.1 | 30 min |

Totale stimato: 6-8 ore. Realtà: si è dilatato per via di bug emersi (vedi sezione 9).

## 9. I 4 bug REALI scoperti durante implementazione (la parte più istruttiva)

Phase 9 è stata la phase dove ho scoperto più bug **in atto di costruzione**, non in test successivo. Tutti emersi durante il regression test (sub-phase 9.8). Tutti coperti con test pytest dedicati post-fix.

### Bug-9.1 — Schema validator non rilevava agenti con nomi custom

Quando sono andato a validare i miei agenti generati (Discovery Agent, Pricing Agent, ecc.), `schema_validator.py` non li trovava. Cercava file chiamati esattamente `agent.md`, ma gli agenti reali hanno nomi tipo `discovery-agent.md`.

**Fix**: aggiunta heuristic in `run_phase9_checks` che cerca file `.md` dentro cartelle `agents/` (non solo `agent.md` letterale).

### Bug-9.2 — Single-file convention con companions non riconosciuta

Avevo strutturato gli agenti come single-file: `discovery-agent.md` + `discovery-agent.system_prompt.md` + `discovery-agent.tools.md`, ecc. Lo schema cercava i 7 file canonici come pari (es. `system_prompt.md` puro), non come suffix.

**Fix**: nuova funzione `check_agent_canonical_files_single_file()` con suffix matching.

### Bug-9.3 — Filtro path `phase` troppo permissivo

Durante test pytest, il pattern di esclusione `if "phase" in str(path)` catturava per errore percorsi tipo `pytest-1/test_run_phase9_checks_finds_t0/` (perché contengono "phase").

**Fix**: regex più stringente: `r"/(phase\d+-(run|regression)|packaged-final)/"`.

### Bug-9.4 — Mancava check `complex-skill-no-agents`

Test #1 baseline v1.0 (`beast-preventivi`) ha PASSED il validator anche dopo le mie tighten dello schema. Perché? Perché lo schema non aveva un check per "skill complessa senza agenti".

L'utente l'aveva esplicitamente segnalato come bug. Senza check, scaffold-skill complessa passava silently.

**Fix**: nuova funzione `check_complex_skill_has_agents()` che usa heuristic (≥3 stages o ≥2 processes = "complex" → richiede `agents/`).

## 10. I numeri finali del regression test

Sub-phase 9.8 ha confrontato output v1.0 vs v1.1 sui due sorgenti.

### Test #1 — beast-preventivi

| Metrica | v1.0 baseline | v1.1 dopo Phase 9 |
|---|---|---|
| File totali | 12 | **40** (+28) |
| Agenti interni | **0** ❌ | **4** (discovery + pricing + qa + humanizer) ✅ |
| Schema validator | WARN | **PASS** |
| Phase 9 issues | 1 (complex-skill-no-agents) | **0** |

### Test #2 — copy-workflow → preventivi-workflow

| Metrica | v1.0 baseline | v1.1 dopo Phase 9 |
|---|---|---|
| File totali | 24 | **101** (+77) |
| File per sub-skill (6 skills) | 1 ❌ | **5** ✅ |
| File per agent (8 agents) | 2/7 ❌ | **7/7** ✅ |
| Schema validator | FAIL (31 errori) | **PASS** (0 errori) |
| Phase 9 issues | 31 | **0** |

Pytest: da 56 a 69 test verdi (+13 nuovi). Zero regressioni.

## 11. Le 5 lezioni che ho estratto

### Lezione 1 — Il validator permissivo è complice del builder lazy

Quando lo schema dice "qualsiasi cosa è OK", il builder produce il minimo necessario. Non per cattiveria — per ottimizzazione naturale.

**Stringere lo schema è azione di leva massima**. Cambi 1 riga in schema, tutti i builder devono adattarsi. Senza, devi convincere ogni builder uno per uno.

### Lezione 2 — Strato 3 (optimizer team) era over-engineering? No, era investimento

A prima vista, aggiungere 5 nuovi agenti per "rifinire" sembra overhead. Avrei potuto solo fare Strato 1+2 (schema + builder updates) in meno tempo.

Ma Strato 3 ha creato:
- Un **pattern riusabile** (PT03)
- Una **categoria di agenti** che posso estendere in futuro
- **Separation of concerns** chiara tra "struttura" (builder) e "depth" (optimizer)
- Un meccanismo per **auto-fix** di gap

Vale tutti i 6-8 ore di implementation. Senza, ogni futura iterazione di qualità sarebbe rifatta a mano.

### Lezione 3 — Trovare 4 bug reali in implementation è normale (e prezioso)

Phase 9 ha trovato 4 bug reali **mentre costruivo Phase 9 stessa**. Non è fallimento del processo: è il processo che funziona.

I 4 bug sono:
- 2 scoperti durante prima esecuzione del regression test
- 1 trovato durante test pytest (filtro path)
- 1 scoperto a quasi-fine quando ho validato il baseline (manca complex-skill check)

**Senza regression test reale**, sarebbero emersi mesi dopo presso utenti reali. Con, fixati in mezza giornata.

### Lezione 4 — La distinzione "structural" vs "content depth" non è ovvia

Avere `references/` con 3 file vuoti soddisfa "structural completeness". Ma è completezza vera? No.

Phase 9 ha dovuto enforce **due cose separate**:
- Structural (file ci sono?): `required_files`
- Depth (content è ricco?): `references_min_total_lines`, `agent_md_min_words`, `playbook_min_conversations`, ecc.

Solo entrambi insieme = vera completezza. Schema v0.3 ha entrambi.

### Lezione 5 — Quando l'utente dice "questo non va bene", credilo

Tre volte in Phase 9 l'utente ha detto sostanzialmente "questo non va bene" con tono educato. Tre volte avevo l'opzione: liquidare con razionalizzazioni o crederci.

Crederci ha portato a:
- Phase 9 (Stage 7 + Ox team) — questo case study
- Phase 10 self-improvement loop (vedi CS03)
- Refactor schema v0.3

Liquidare avrebbe portato a: skill che "passa i test" ma che nessuno usa.

L'utente è il miglior validator esterno che hai. Costa poco crederlo. Costa molto liquidarlo.

---

## Connessioni con altri principi/pattern

- Esemplifica: **P08** (Depth Over Breadth) — Phase 9 è stata sua incarnazione
- Implementa: **PT03** (Builder then Optimizer) — pattern formalizzato qui
- Implementa: **PT06** (Schema Tightening Loop) — v0.2 → v0.3
- Implementa: **PT11** (Validation with Auto-Fix) — optimizer team è auto-fix layer
- Si ricollega a: **CS01** (MKD Discovery) — entrambe trigger esterno (utente) → cambio strutturale
- Anti-esempio di: **AP01** (Scaffold as Deliverable) — Phase 9 è il fix sistematico di AP01
