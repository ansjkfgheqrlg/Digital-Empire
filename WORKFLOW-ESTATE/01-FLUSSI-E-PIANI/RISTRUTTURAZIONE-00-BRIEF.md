---
Owner: Max
Controllore: Claude
Origine: brainstorming Max↔Claude 2026-07-24
Governo: company/Mandato/MANDATO-EMPIRE.md
---

# 🧭 RISTRUTTURAZIONE EMPIRE — BRIEF 00 (base dei 7 piani)
> 2026-07-24 · **Stato: ✅ SERIE COMPLETA — i 7 piani sono scritti.** (CP-20260724-007)
>
> | # | Piano | Dimensione | Score |
> |---|---|---|---|
> | 1 | [FONDAMENTA](RISTRUTTURAZIONE-01-FONDAMENTA.md) | la verità verificabile | 8.5 |
> | 2 | [CICLI](RISTRUTTURAZIONE-02-CICLI.md) | l'esecuzione che si registra | 8.8 |
> | 3 | [WORKFLOW](RISTRUTTURAZIONE-03-WORKFLOW.md) | il lavoro diventa eseguibile | **9.0** |
> | 4 | [GERARCHIA](RISTRUTTURAZIONE-04-GERARCHIA.md) | l'autorità | 8.7 |
> | 5 | [SESSIONI](RISTRUTTURAZIONE-05-SESSIONI.md) | la continuità | **9.1** |
> | 6 | [AUTONOMIA](RISTRUTTURAZIONE-06-AUTONOMIA.md) | l'iniziativa | 8.9 |
> | 7 | [APEX](RISTRUTTURAZIONE-07-APEX.md) | l'autocritica | 8.6 |
>
> **Prossimo passo: Max legge e approva. Non si costruisce nulla prima (suo ordine).**
> Ordine di esecuzione consigliato in [APEX §5](RISTRUTTURAZIONE-07-APEX.md).
> Questo file resta la base: contiene le parole di Max, le 8 risposte e la diagnosi.

---

## 1. L'ordine di Max (parole sue, non parafrasate)

> "La struttura ancora non è perfetta. Vedo ancora tantissime cartelle vuote. Ristrutturare tutto,
> architettare tutto perfettamente e ampliare tutto. Deve essere tutto ancora più perfetto,
> complesso, performante."
>
> "Ogni fase è un workflow, che deve avere skill, agenti, ecc. Il tutto deve essere estremamente
> strutturato, devono esserci reparti, gerarchie, flussi, sessioni, debug ed ecosistemi interni."
>
> "Non crei niente: studia, analizza e pianifica. Poi crea un plan1, poi il plan2 che è il
> miglioramento, e così fino al 7. Ogni miglioramento deve seguire un flusso completo di
> miglioramenti, non un miglioramento casuale."

**Riferimento di qualità fornito da Max:** documento `APEX-7 DEEP REFINEMENT` (Quality Gate System,
Gate Agent con state machine, Memory Query Interface, Event Bus con catalogo eventi, RuFLO
Integration Map). È il livello di profondità atteso: ogni pezzo con autocritica e score, non descrizioni.

---

## 2. ⛔ VINCOLO SOVRANO (correzione esplicita di Max, vale su tutto)

> "Che sia chiaro: **tu non devi cancellare tutto e rifare da capo. Non devi ricostruire.**
> Devi soltanto **migliorare, aggiungere, migliorare, aggiungere, perfezionare.**"

**Conseguenze operative, non negoziabili:**
- Nessuna riscrittura, nessuna grande cancellazione, nessuno spostamento di massa.
- Ogni piano è **additivo**: si costruisce SOPRA ciò che esiste (coerente con ADR-003: i motori vivi
  si avvolgono, mai si riscrivono).
- Anche la spazzatura tecnica **non si tocca di iniziativa**: si segnala a Max e decide lui.
- Se un piano propone di rimuovere qualcosa, deve chiedere prima. Sempre.

---

## 3. Risposte di Max al brainstorming (sono i requisiti di progetto)

| Domanda | Risposta di Max |
|---|---|
| Perimetro | **Non cancellare/ricostruire — solo migliorare, aggiungere, perfezionare** |
| Cartelle vuote | **Accendere i cicli che le riempiono da sole** (non riempirle a mano, non svuotarle) |
| "Ogni fase è un workflow" | **Vale da ora, E si rimettono in forma i 6 stream estate esistenti** |
| Agenti vs solo Claude | **Deve funzionare anche con Claude da solo** — gli agenti acceleratore, mai condizione |
| Cosa vuole poter fare in 10 secondi | **(1) sapere cosa fare adesso · (2) vedere lo stato vero di tutto · (3) lanciare un lavoro e fidarsi** |
| Autonomia | **"Fa tutto e mi riporta alla fine"** — massima autonomia |
| Gerarchia | **Come un'azienda vera**: direttori, capi reparto, specialisti, controllori |
| Se sbaglia | **Riprova, poi si ferma e spiega in parole semplici** |

### ⚠️ Tensione dichiarata e come va risolta nei piani
Max ha scelto **massima autonomia** ("fa tutto e riporta alla fine"). Questo NON può estendersi alle
azioni verso l'esterno: mandare email a concessionari veri, incassare, pubblicare su un canale.
**Regola di progetto:** autonomia piena *dentro* la costruzione, mano di Max *sulla porta d'uscita*.
È già il comportamento in vigore (invio outreach gated G-A4, gate umani con evidenza calcolata).
I piani devono renderlo esplicito, non ereditato per caso.

---

## 4. Analisi già fatta — diagnosi delle "cartelle vuote"

**398 cartelle vuote totali.** Non sono un problema solo: sono tre problemi diversi.

### Tipo 1 — Spazzatura tecnica (~250) · NON è struttura
`EmpireDesk/chrome-profile/**` (profilo Chrome intero nel repo) · `.git.bak/` · `.venv/` ·
`dist/` `out/` `.next/` · `node_modules/` · `.netlify/`.
→ **Proposta: `.gitignore`, non cancellazione.** Decide Max.

### ✅ Tipo 1-bis — VERIFICA DI SICUREZZA: FATTA, ESITO BUONO
`EmpireDesk/chrome-profile/` è un profilo Chrome completo, e questi profili contengono cookie e
sessioni di login. Verificato il 2026-07-24:
```
git ls-files EmpireDesk/chrome-profile | wc -l   ->  0
```
**Non è tracciato da git: nessuna credenziale è mai finita nel repo o su GitHub.** Resta solo
ingombro locale. Consigliata una riga in `.gitignore` per sicurezza futura (additivo, non
cancella nulla) — decide Max. **Verifica chiusa, non va rifatta.**

### Tipo 2 — Lavoro mai partito (~100)
`Agenti/Agency/output/run_01_Milano_ristoranti/{emails,leads,reports}` … 11 run preparate, zero output.
`Clienti/EXPONIUM/content-factory/{output,knowledge,input/images}`.
→ Cartelle che aspettano un lavoro mai eseguito.

### 🎯 Tipo 3 — I SENSORI SPENTI (~25) · **è qui il problema vero**
```
WORKFLOW-ESTATE/02-AUTOMAZIONI-E-SCRIPTS/   -> 11 su 11 VUOTE
   architectures · brainstorms · checkpoints · decisions · errors
   feedback · metrics · performances · plans · reasoning-bank · sessions
company/Memory/tasks/01-agency … 10-memory   -> 10 su 10 VUOTE
company/Memory/audit · company/Ispettorato/report/escalation -> VUOTE
SKILL & Agenti/Empire Studio Suite/empire-studio/memory/{agent-state,architectures} · evals -> VUOTE
```
Sono le cartelle dove il sistema dovrebbe scrivere **cosa decide, cosa sbaglia, cosa impara,
quanto ci mette**. Sono vuote perché **nessun agente ci scrive dentro**.

**Prova incrociata (misurata il 24/07, non ipotizzata):** le 6 metriche di telemetria di
`empire inspect` restituiscono tutte `0` con nota *"nessun record PERF registrato"*. Non perché il
codice sia rotto — l'ho costruito e testato — ma perché **non esiste un solo record**.

### 💡 Diagnosi che regge tutto il resto
**Non è un problema di ordine, è un problema di cicli di vita.**
L'azienda ha gli organi di senso (cartelle, schema, moduli) ma non ha i nervi che li collegano:
nessun ciclo di lavoro produce tracce. Riempire le cartelle a mano non risolve niente — vanno
accesi i cicli che le riempiono lavorando. È esattamente il punto del documento APEX-7: gate,
eventi e memoria non sono decorazioni, sono **ciò che produce le tracce**.

Questo è anche il filo che unisce i 3 difetti trovati ieri (CP-20260724-001): controlli che
rassicurano invece di misurare. Stessa radice: **niente veniva mai eseguito davvero.**

---

## 5. Struttura reale rilevata (base di partenza, da NON rifare)

```
company/
  Board-CSuite/   CEO · COO · CTO · CMO · CRO · CFO · Chief-Forge
  Ecosistemi/     14 cartelle (ADR-009 ne ammette 13 — 08-STREAM-S7-BOT compare DUE volte:
                  `08-STREAM-S7-BOT` e `12-STREAM-S7-BOT` -> DA VERIFICARE, possibile residuo)
  Gerarchia/ · Guilds/ · Sentinels/ · MAXIMILIAN/ · Mandato/ · Genesi-Core/
  Ispettorato/    11 agenti + 5 workflow (M1/M3 fatti, M2/M4/M5 no)
  Memory/         INDEX · STATO-EMPIRE · checkpoints (98+) · decisions (9 ADR) · tasks/ (VUOTE)
empire/           runtime: paths config schema conform cli loader index flow memory inspect
                  registry dash tools estate  (207 test verdi)
WORKFLOW-ESTATE/  6 pilastri Art.8 + 07-VIDEO-RUN
```
- **Reparti già censiti:** A1–A10 (01-AGENCY), IB-L2 ×5 (02-INFO-BUSINESS), CF-R0…R6 (03-CONTENT-FACTORY), ecc.
- **439 agenti progettati** (`empire agents`), **0 CF-grade** secondo la dashboard → da capire perché.
- **`empire status`:** 44 alias, 0 rotti.

**Nota da verificare:** `08-STREAM-S7-BOT` e `12-STREAM-S7-BOT` sembrano lo stesso ecosistema
duplicato. Non toccato: è materia di Max (ADR-009).

---

## 6. Come saranno fatti i 7 piani (deciso, da eseguire)

Max chiede: *"ogni miglioramento deve seguire un flusso completo, non un miglioramento casuale"*.
Quindi ogni piano da 1 a 7 ha **la stessa struttura obbligatoria**:

```
PIANO N
  §0  AUTOCRITICA DEL PIANO N-1   cosa manca, dichiarato per punti (non generico)
  §1  DIMENSIONE MIGLIORATA       UNA sola, dichiarata in apertura
  §2  IL CONTENUTO                reparti, agenti, workflow, skill, gate del livello
  §3  GATE DI PASSAGGIO N→N+1     criteri oggettivi, soglia, cosa fare se fallisce
  §4  AUTOCRITICA DEL PIANO N     cosa ho migliorato / cosa manca ancora / SCORE su 10
```

### Progressione dei 7 livelli (non 7 revisioni a caso: una scala)
| # | Livello | Domanda a cui risponde |
|---|---|---|
| 1 | **Fondamenta oneste** | Cosa esiste davvero, chi possiede cosa, cosa è vuoto e perché |
| 2 | **Cicli che lasciano traccia** | Come ogni lavoro scrive da solo decisioni, errori, tempi (accende i sensori) |
| 3 | **Fase = workflow completo** | Ogni fase con i suoi agenti, skill, gate — applicato ai 6 stream estate |
| 4 | **Reparti e gerarchia vera** | Chi comanda chi, chi controlla chi, come si passano il lavoro |
| 5 | **Sessioni, debug, ripresa** | Come si riprende dopo un'interruzione e si capisce cosa è andato storto |
| 6 | **Autonomia sorvegliata** | "Fa tutto e riporta alla fine", con la porta d'uscita in mano a Max |
| 7 | **APEX: si migliora da solo** | Il sistema misura sé stesso e propone le proprie correzioni |

**Vincolo trasversale a tutti e 7:** additivo. Nessun piano può prevedere di cancellare o riscrivere.
Ogni piano deve funzionare anche con Claude da solo, senza swarm.

---

## 7. RIPRESA DA (prossima sessione — leggere questo file per primo)

1. ~~Verifica sicurezza chrome-profile~~ **FATTA il 24/07: non tracciato, nessuna esposizione.**
2. Completare l'analisi: come sono fatti oggi i 6 stream estate (WF-S1…S6) e quali agenti/skill
   hanno già — serve al PIANO 3.
3. Scrivere **PIANO 1 → PIANO 7** con la struttura di §6, in
   `WORKFLOW-ESTATE/01-FLUSSI-E-PIANI/RISTRUTTURAZIONE-0N-*.md`.
4. Non costruire nulla finché Max non approva i piani.

**Contesto operativo:** i subagenti falliscono con `You've hit your monthly spend limit` finché Max
non alza il limite. Tutto va progettato per funzionare senza.

---
⛓️ P12: `RISTR-BRIEF-00#empire` · fonte: brainstorming 2026-07-24 · CP-20260724-002
