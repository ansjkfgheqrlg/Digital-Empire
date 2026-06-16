# ARCHITETTURA — Organo del Genesi Core (porta d'ingresso)

> Il nucleo strutturale della FORGE. Disegna la **forma al millimetro** di ogni cosa che la holding
> crea, prima che la FORGE ci costruisca dentro il CONTENUTO. Standard: CF-grade.
> Fonte di verità: [[14-DOSSIER-ARCHITETTURA]]. Stato: build STEP 1 del Genesi Core.

---

## Missione
ARCHITETTURA è una **FORGE specializzata SOLO nella struttura**. Prima che la FORGE forgi qualsiasi
artefatto — skill, agente, team, principio, stile, workflow, documento, reparto, ecosistema — ARCHITETTURA
ne **disegna la struttura al millimetro e la valida**. È il fulcro del nucleo di ogni operazione FORGE:
nulla si forgia senza un blueprint architettato e approvato qui. In termini SPARC, ARCHITETTURA possiede
**Specification → Pseudocode → Architecture**; la FORGE possiede **Refinement → Completion**.
*L'architetto disegna, la fabbrica costruisce.*

**Cosa NON è.** Non è l'architettura dell'infrastruttura Empire (quello è il PIANO-MAESTRO). È architettura
**per-artefatto**: la forma di *ogni singola cosa* che nasce dalla FORGE. Non scrive il contenuto finale
(FORGE), non giudica se è "all'altezza di Max" (MAXIMILIAN), non decide se è lecito (Mandato).

---

## Posizione nella gerarchia (§9 dossier)
```
LX  Mandato (legge) · MAXIMILIAN (standard/visione)
 │
GENESI CORE  ┌─ ARCHITETTURA (progetta la struttura) ──┐
             └─ FORGE (costruisce il contenuto) ◄─ blueprint ┘
 │
L0  Board C-Suite (regia)
 │
L1  i 10 ecosistemi (nascono DA Genesi Core)
```
ARCHITETTURA è **gemella della FORGE** dentro il Genesi Core e **multi-tenant per definizione**: ogni
creazione di ogni ecosistema, passando dalla FORGE, passa prima da qui. È la costituzione strutturale della holding.

---

## I 5 reparti (L2) + Guild
- **L2.1 Spec & Requirements** — la richiesta diventa spec precisa (cosa, perché, vincoli, fuori-scope).
- **L2.2 Blueprint & Struttura** — la spec diventa struttura millimetrica dell'artefatto.
- **L2.3 Schemi Canonici** — custodisce/versiona gli schemi-template (la "costituzione" delle strutture).
- **L2.4 Validazione Strutturale** — il gate `struct-gate`: completo/incompleto vs schema (pre e post FORGE).
- **L2.5 Progettazione Ecosistemi** — disegna org chart interi L1→L5 (il livello più grande di design).
- **⊕ Pattern Guild** (trasversale) — libreria di pattern riusabili, anti-reinvenzione.

## Gli 8 agenti (`arch-*`)
`arch-director` (L1, conductor) · `arch-spec-writer` (L2.1) · `arch-blueprint` (L2.2) ·
`arch-schema-keeper` (L2.3) · `arch-validator` (L2.4) · `arch-contradiction` (L2.4) ·
`arch-org-designer` (L2.5) · `arch-pattern-scout` (Guild).

## Le 9 forme / schemi canonici
skill · agente · team · principio · stile · workflow · documento (MKD) · reparto · ecosistema.
Per ogni forma esiste lo **schema canonico** al millimetro. La lista **non è una gabbia**: una forma nuova
si aggiunge con WF-SCHEMA-EVOLVE. **L'ingegno sta nello scegliere la forma minima-ma-completa** (mai gonfiare, mai banalizzare).

## I 4 workflow
- **[[WF-ARCH-DESIGN]]** — il cuore: richiesta `{tipo,scopo,vincoli}` → pattern-scout → spec → schema → blueprint → struct-gate → HANDOFF a FORGE.
- **[[WF-STRUCT-VALIDATE]]** — il gate riusabile `struct-gate`: artefatto → `{COMPLETO|INCOMPLETO, buchi:[…]}` vs schema (pre e post FORGE).
- **[[WF-ECOSYSTEM-DESIGN]]** — mandato Board → org L1→L5 + BACKBONE + namespace → handoff a FORGE (WF-ECOSYSTEM-NEW).
- **[[WF-SCHEMA-EVOLVE]]** — buco strutturale ricorrente → schema canonico aggiornato (versione + diff). Migliora la costituzione.

---

## La catena del Genesi Core (handoff completo)
```
richiesta → ARCHITETTURA (spec + blueprint + struct-gate) → FORGE (costruisce il contenuto)
         → MAXIMILIAN (è all'altezza?) → Mandato (lecito?) → Identity-HR (registra) → VIVO
```
- **FORGE** (gemello): ARCHITETTURA disegna il blueprint, la FORGE ci costruisce dentro. La FORGE non inventa strutture, le chiede qui.
- **MAXIMILIAN** (sopra): ARCHITETTURA garantisce *strutturalmente completo*; MAXIMILIAN che sia *all'altezza di Max*. Due gate in serie.
- **Mandato** (legge): ARCHITETTURA = forma corretta; Mandato = forma lecita.

---

## Confine ferreo: STRUTTURA vs CONTENUTO
**ARCHITETTURA = struttura. FORGE = contenuto.** ARCHITETTURA produce *la forma vuota al millimetro*
(file, sezioni, I/O, handoff, schema rispettato), mai una riga del contenuto finale. La FORGE riempie quella
forma. Questo confine è la regola che impedisce la sovrapposizione tra i due gemelli del Genesi Core.

---

## Navigazione
- Workflow → `Workflow/` (i 4 sopra) · Agenti → `Agenti/` (gli 8 `arch-*`) · Reparti → `Reparti/` (L2.1→L2.5)
- Schemi canonici → `Schemi-Canonici/` (le 9 forme) · Infrastruttura → [[BACKBONE.md]]
- Fonte di verità → [[14-DOSSIER-ARCHITETTURA]] · Gemello → 07-FORGE · Gate a valle → [[12-DOSSIER-MAXIMILIAN]] · [[13-DOSSIER-MANDATO-ECOSISTEMA]]
