# 🏗️ 11 — PIANO V2: LA DIRETTIVA DI SCALA (revisione maestra, 2026-06-11)

> **Direttiva integrale di Max dopo analisi completa del workspace.** Questo documento
> SUPERA lo standard v1 dei dossier 00-09 dove in conflitto (ADR-007). Non stiamo
> costruendo un reparto o un workflow: **stiamo costruendo un'INTERA AZIENDA.**
> Corpus originale delle parole di Max: `company/Memory/maximilian-corpus/`.

---

## 0. LA NUOVA UNITÀ DI MISURA (il cambio di scala)

**Standard Max: "un workflow fatto bene = il Content Factory di Exponium".**
Quella che in v1 trattavamo come azienda di riferimento è, nella scala v2, **UN SINGOLO
WORKFLOW**. Definizione operativa — un workflow Empire-grade ("CF-grade") ha:

| Componente | Minimo richiesto |
|---|---|
| Gerarchia interna | livelli espliciti (conductor → coordinatori → worker) |
| Agenti | team completi, schede millimetriche (identità, responsabilità, I/O, logica passo-passo, KPI, escalation, esempi) |
| Skill PROPRIE | skill dedicate al workflow (kernel + references/) |
| Principi e regole | invariant cardinali scritti, non negoziabili |
| Script eseguibili | .py/.ps1 reali (orchestrazione, dispatch, QA) — non solo markdown |
| QA a cancelli | gate deterministici + verify dedicato |
| Runtime/state | state.json + trace per ogni esecuzione |
| Memoria | namespace dedicato + lezioni → ReasoningBank |
| Dry-run | modalità a costo zero |

**Tutto ciò che in v1 era "un file .md" in v2 è una STRUTTURA. Vietato consegnare
un ruolo in un markdown e chiamarlo agente/reparto/figura.**

---

## 1. BOARD C-SUITE V2 — ogni figura è un WORKFLOW, non un agente

INACCETTABILE (v1): CEO = 1 file markdown con un ruolo.
STANDARD V2: **ogni figura C-level = un intero workflow CF-grade**:

```
Board-CSuite/CEO-Empire-Conductor/        ← cartella-workflow, non file
├── README.md                              # architettura della figura
├── ARCHITETTURA.md                        # progettata con skill apposite (vedi §8)
├── agenti/                                # MINIMO 10 agenti per figura
│   ├── ceo-conductor.md                   # il decisore principale
│   ├── ceo-analista-strategico.md         # analizza scenari prima delle decisioni
│   ├── ceo-advisor-rischi.md  ceo-advisor-opportunita.md
│   ├── ceo-priorita-arbiter.md            # arbitra conflitti tra ecosistemi
│   ├── ceo-budget-allocator.md  ceo-okr-tracker.md
│   ├── ceo-comunicatore.md                # direttive verso gli ecosistemi
│   ├── ceo-verificatore.md                # controlla che le decisioni siano eseguite
│   └── ceo-memoria.md                     # storico decisioni, pattern, coerenza ADR
├── principi/  regole/                     # come ragiona, cosa non può fare
├── skills/                                # skill PROPRIE della figura
├── scripts/                               # .py/.ps1: raccolta dati, report, dispatch
├── workflow/                              # i flussi operativi della figura (≥2)
│   ├── WF-DECISIONE-STRATEGICA/  WF-REVIEW-TRIMESTRALE/ ...
└── kpi/  state/
```
Stesso schema per: **COO, CTO, CMO, CRO-Revenue, CFO, Chief-Forge** (7 figure × ~10 agenti
= ~70 agenti solo nel Board). Ogni figura: architettura progettata con le skill di
architettura (§8), non improvvisata.

---

## 2. REPARTI V2 — ogni reparto è un'organizzazione

STANDARD V2 per OGNI reparto L2 di OGNI ecosistema:
1. **Team di agenti: minimo 6, tipico 8-10** — con gerarchia interna: 1 lead/coordinatore,
   1 verificatore/QA, specialisti. Schede millimetriche (standard §0).
2. **Da 1 a 5 workflow CF-grade** per reparto (più strade = più workflow). Esempio
   Reparto Ricerca (Agency): team 6-10 agenti + WF-RICERCA-INTENSIVA (entra nei siti,
   scrape, analisi) + collegamento a **Empire Studio** per l'ingestione + WF-COMPETITOR +
   WF-ICP-DISCOVERY.
3. **Più reparti dove servono**: l'Agency non basta con Ricerca/Acquisizione/Preventivi —
   aggiungere (minimo): Delivery/Implementazione, Account Management & Supporto,
   Closing/Sales-call, Partnership, QA-cliente. Ogni ecosistema rivede la propria lista
   reparti al rialzo nel proprio dossier v2.

**MEGA-REPARTI = aziende dentro l'azienda.** Info Business, Content Factory (e altri da
valutare) sono ENORMI: gerarchia solida A LIVELLI propria (leader di reparto → capi area →
coordinatori → verificatori → worker), sempre DENTRO Digital Empire e sotto il Mandato.

---

## 3. MANDATO V2 — da documento a ECOSISTEMA di governo

Il Mandato v1 (un file di Articoli) è più piccolo di un reparto: inaccettabile.
**Il Mandato diventa un GIGANTE — di fatto un ecosistema**: controlla tutto, comanda
anche le Sentinelle.
- **Team custodi** (≥6 agenti): interprete del Mandato, analista di conformità,
  aggiornatore (propone evoluzioni ad ADR), enforcement-lead (comanda le Sentinelle),
  storico, verificatore.
- **Più workflow**: WF-ENFORCEMENT (violazione → blocco → escalation), WF-EVOLUZIONE
  (analisi → proposta → approvazione Max → pubblicazione), WF-AUDIT-PERIODICO.
- Gli Articoli restano il cuore, ma vivono dentro questa struttura con principi/, regole/,
  scripts/ (contradiction-check automatico), skills/ proprie.

## 4. SENTINELLE V2 — ognuna multi-workflow

Ogni Sentinella (Cost, Quality, Drift, Security, Brand-Voice): non un runbook ma una
struttura con **più workflow** (monitoraggio continuo · intervento/blocco · escalation ·
auto-calibrazione soglie) + agenti propri + script di scansione reali + state.
Rispondono al Mandato (§3).

## 5. GUILDS V2 — drasticamente migliorate

Ogni Guild: non un file ma una struttura con playbook completo, libreria di pattern
validati (collegata al Brain), processo di standardizzazione (raccolta→validazione→
pubblicazione→notifica via bus), agenti propri (curatore, validatore), calendario di review.

## 6. MEMORY V2 — al passo con la scala

MEMORY è promosso bene (parola di Max) ma deve reggere la scala v2:
- task log e state per OGNI workflow CF-grade (non solo per fase);
- indici per ecosistema/mega-reparto (INDEX a 2 livelli per non esplodere);
- checkpoint anche per i build interni dei workflow;
- il test "amnesia" si estende: ogni workflow deve essere ripartibile a freddo dal suo state.

## 7. ORGANO MAXIMILIAN — il team che incarna Max (gerarchia massima)

**Nuovo organo, sopra il Board, accanto al Mandato (LX).** Team di agenti che È Max:
carattere, carisma, idee, standard, modo di decidere. Funzione: correggere la rotta,
dire ciò che direbbe Max, pre-approvare al posto suo dove delegato (es. prezzi col
team-prezzi B-003), spingere SEMPRE verso: chirurgico, millimetrico, completo, ampio,
mai fermarsi su minuzie (ADR-005), swarm sempre (ADR-006), tutto visibile nell'Explorer.
- **Composizione (≥8 agenti):** Maximilian-Prime (la voce), Visionario (scala/ambizione),
  Critico-Standard (boccia ciò che Max boccerebbe — "è un file markdown? INACCETTABILE"),
  Decisore-Rapido, Anticipatore (immagina le modifiche che Max vorrebbe PRIMA che le chieda),
  Custode-Stile (come parla/scrive Max), Challenger ("perché ti fermi?"), Memoria-di-Max.
- **Addestramento:** corpus = TUTTI i prompt/direttive di Max — archiviati in
  `company/Memory/maximilian-corpus/` (il primo file è la direttiva integrale di oggi).
  Ogni futura direttiva si appende al corpus.
- **Uso operativo:** ogni fase, al passo 5 (REVIEW indipendente) si aggiunge il
  **passo 5-bis: REVIEW MAXIMILIAN** — "Max approverebbe?" Se no: si rifà.

## 8. ARCHITETTURA CON SKILL APPOSITE (obbligo)

Ogni struttura v2 (figure Board, mega-reparti, workflow CF-grade, Mandato, Maximilian)
si progetta PRIMA con le skill di architettura installate — non si improvvisa:
`architect-agent` (architettura agenti) · `prd-architect-os` (PRD con quality score) ·
`agent-architecture`/`sparc-methodology` (SPARC fase 3) · `Skill Master Architecture` ·
`skill-creator` (per le skill proprie) · `content-forge` (da conoscenza a struttura).
Flusso standard: PRD → architettura → build swarm → gate → review (incl. Maximilian).

## 9. KNOWLEDGE INGESTION — la formazione diventa azienda

Le cartelle del workspace piene di formazione/conoscenza NON ancora usate diventano
organi interni (reparti, workflow, agenti, skill). Mappa di trasformazione (fase dedicata):

| Sorgente | Destinazione v2 |
|---|---|
| `Formazzione/` (Agency Scalping, Claude Code, Outreach, Storytelling, Youtube) | corpus → skill/workflow dei reparti competenti (via content-forge/book-to-skill) |
| `Marketing & Ai/` | ecosistema 04-MARKETING (reparti v2) |
| `SKILL & Agenti/` (tutte le sotto-cartelle non ancora mappate) | FORGE: censimento → ogni asset diventa workflow/skill interna |
| `InfoBusiness/`, `Lancio corso skill beast/`, `Lanco ebook/` | mega-reparto 02-INFO-BUSINESS |
| `MarketMind/`, `Crea siti/`, `SaaS/`, `App/`, `caroselli/`, `Workflow-libri/`, `KDP/` | ecosistemi competenti (03/05/06) |
| Prompt e direttive di Max (questa chat e future) | `maximilian-corpus/` (§7) |
Metodo: Empire Studio/content-forge per l'estrazione INTEGRALE (mai riassunti), poi FORGE
costruisce. Niente cartella resta "morta" nel workspace.

---

## 10. ROADMAP V2 (sostituisce la sequenza corrente da qui in poi)

| Fase | Cosa | Note |
|---|---|---|
| **V2-0** | Questo documento + ADR-007 + corpus Maximilian + handover | fatto in questa sessione |
| **V2-1** | F1-bis di Gael si COMPLETA come previsto (è la BASE, non lavoro sprecato) | in corso ora |
| **V2-2** | Dossier v2: swarm riscrive/amplia i dossier 01-09 + nuovo dossier MAXIMILIAN e MANDATO-ecosistema secondo questa direttiva (architettura con skill §8) | primo swarm disponibile |
| **V2-3** | ORGANO MAXIMILIAN costruito (corpus + 8 agenti + review-gate 5-bis attivo) | priorità alta: da qui in poi corregge tutto il resto |
| **V2-4** | BOARD V2: le 7 figure ricostruite come workflow CF-grade (~70 agenti) | swarm, una figura per agente |
| **V2-5** | MANDATO-ecosistema + SENTINELLE multi-workflow + GUILDS v2 | |
| **V2-6** | REPARTI V2 ecosistema per ecosistema (ordine: 01→04→03→02→05) — team 6-10 + 1-5 workflow CF-grade per reparto; mega-reparti con gerarchia propria | più cicli, uno per ecosistema |
| **V2-7** | KNOWLEDGE INGESTION (§9) — la formazione del workspace diventa organi | sessioni dedicate |
| **V2-8+** | si riaggancia alla roadmap v1 (F5-F12: produzione reale, YouTube, agenti running, auto-miglioramento) con strutture v2 | |

Ogni fase: ciclo a 9 passi (ADR-006) + review Maximilian (da V2-3 in poi). Budget-guard:
MAI due swarm grossi insieme sull'account condiviso (lezione CP-005).

## Connessioni
- ADR-007 (questa direttiva) · [[00-PIANO-MAESTRO]] (v1, base che resta valida dove non in conflitto) · [[10-METODO-CICLO-FASE]] (si aggiunge passo 5-bis) · `maximilian-corpus/`
