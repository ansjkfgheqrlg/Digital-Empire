# 27 — ARENA → WORKFLOW COMPLETO: metodo per costruire agenti/skill/flussi/automazioni con APEX-7

> Risponde alla richiesta di Max (2026-08-03): usare Arena per creare un **workflow completo**
> — agenti, skill, flussi, automazioni — basato sulla skill di architettura perfetta
> (`master-build-architecture`) e sul sistema di ragionamento APEX-7, integrato obbligatoriamente.
> Questo è il **metodo riusabile**, non un workflow specifico per un prodotto — si applica a
> qualsiasi nuovo workflow tu voglia costruire (Content Factory, Preventa, YouTube, ecc).

---

## §0 — Le 3 fondamenta su cui questo piano è costruito (già esistenti, non da reinventare)

| Fondamenta | Cosa fa | Dove vive |
|---|---|---|
| **Arena** (LMArena.ai) | Cervello di progettazione: analisi, prompt ampi, gate, review indipendente. **Non esegue, non tocca credenziali, non pubblica.** | Contratto in dossier [26](26-ARENA-COSA-COSTRUIAMO-INSIEME.md) (recuperabile da git: `git show 027bf6e6:PIANO-MAESTRO/26-ARENA-COSA-COSTRUIAMO-INSIEME.md` — perso dal disco in un rebase, mai ripristinato) |
| **master-build-architecture** (skill) | Progetta architetture multi-agente "bulletproof": MKD (Master Knowledge Document) → PLAN-v1 → ASK → BUILD → CRITIQUE → ITERATE. 7 file canonici per agente, memory ecosystem da subito, swarm 25+ agenti | `.agents/skills/master-build-architecture/` |
| **APEX-7** | Sistema nervoso/ragionamento: quality gate, event bus, memory. Motore unico dopo ADR-010 (fusione con backbone Ruflo) | `.agents/skills/apex-7/` (definizione skill) + `company/Ecosistemi/11-APEX-7-CORE/` (motore runtime) |

**Vincolo non negoziabile (Regola APEX, `company/Ecosistemi/13-ARENA-APEX/ECOSISTEMA.md`):**
*"Nessun agente esce da questa Arena senza aver integrato e testato la Skill APEX-7 nel proprio
ciclo vitale."* Questo piano rispetta il vincolo end-to-end: APEX-7 non è un'aggiunta finale, è
il gate che ogni pezzo deve passare prima di essere considerato "consegnato".

---

## §1 — Il contratto dei ruoli (chi fa cosa, ripreso e aggiornato da dossier 26)

| | **Arena** | **Claude Code (locale) + Max/Gael** |
|---|---|---|
| Ruolo | Progetta: MKD, spec agenti, prompt di build, criteri di accettazione | Costruisce: file reali, test, integrazione APEX-7, commit |
| Produce | Prompt ampi via `master-build-architecture` (interattivo: PLAN-v1→ASK→BUILD→CRITIQUE) | Codice che gira, test verdi, ADR/CP, registro aggiornato |
| Review | **Passo 5 del ciclo 9 (ADR-006)** — review indipendente di quello che Claude Code ha costruito | Non si autoapprova mai (regola "chi costruisce non si approva da solo") |
| Non fa | Non ha le tue credenziali, non esegue in produzione | — |

**Il loop (identico a dossier 26 §0, riapplicato al workflow specifico):**
```
1. TU (Max)  → dai l'obiettivo del workflow ad Arena ("costruisci il workflow per X")
2. ARENA     → produce MKD + PLAN-v1 (via master-build-architecture) + prompt di build ampio
3. TU/CLAUDE → esegui il prompt in locale con Claude Code → build reale, APEX-7 integrato/testato
4. ARENA     → review indipendente (passo 5) → verdetto: via libera o correzione
5. CLAUDE    → CP + STATO-EMPIRE + registro (ADR-008) → push
```

---

## §2 — Fase A: cosa fai TU in Arena.ai (progettazione)

### A1. Prompt di apertura da incollare in Arena

```
Sei l'architetto di un workflow completo per Digital Empire (agenzia AI multi-business).
Usa il metodo master-build-architecture: produci prima un Master Knowledge Document (MKD)
del workflow [NOME WORKFLOW], poi PLAN-v1.

Il workflow deve includere:
- N agenti specializzati (agent swarm, non un monolite) con 7 file canonici ciascuno:
  spec.md, system-prompt.md, tools.md, playbook.md, evals.md, failure-modes.md, memory.md
- Skill eseguibili (non solo prompt) per ogni step ripetibile
- Flussi/automazioni (event-driven, non a chiamata manuale dove possibile)
- Memory ecosystem da subito: checkpoints/, decisions/, sessions/, plans/, MEMORY-INDEX.md
- OBBLIGATORIO: integrazione APEX-7 come layer di ragionamento/quality-gate — ogni agente
  deve avere un gate APEX-7 nel suo ciclo vitale prima di essere considerato operativo
  (non "in seguito", da subito nel PLAN-v1)

Segui il ciclo Empire a 9 passi (RECALL→SPEC→PRE-MORTEM→BUILD→GATE→REVIEW→TEST→COMMIT→RETRO,
dossier 10-METODO-CICLO-FASE.md) — tu (Arena) fai review indipendente al passo 5, io/Claude
Code costruiamo.

Contesto del workflow: [DESCRIVI QUI L'OBIETTIVO CONCRETO — quale ecosistema, quale problema
risolve, quali dati/input reali esistono già su disco — Arena lavora su prove, non inventa]
```

### A2. Cosa Arena ti restituisce (output atteso)
1. **MKD** — documento che espande (mai riassume) ogni pezzo di contesto che gli dai
2. **PLAN-v1** — architettura completa: N agenti, ruoli, dipendenze, memory ecosystem, gate APEX-7
3. **Prompt di build** — pronto da incollare in Claude Code locale, con criteri di accettazione misurabili (numeri, non aggettivi — coerente con REGOLA UNO)
4. **Pre-mortem** — 3+ modi concreti in cui il workflow fallisce + contromisura (passo 2 del ciclo 9)

### A3. Iterazione (se il PLAN-v1 non convince)
`ASK` (Arena fa domande di chiarimento) → `CRITIQUE` (tuo feedback) → `PLAN-v2` — non accettare
il primo output se manca concretezza: stesso standard di onestà verificabile già in uso nel
resto del repo (niente claim senza fonte, niente "operativo" senza test verde).

---

## §3 — Fase B: cosa fa Claude Code in locale (costruzione)

Quando incolli il prompt di build di Arena, il ciclo 9 passi (ADR-006) parte da qui:

1. **RECALL** — Claude legge `STATO-EMPIRE.md` + INDEX + ADR rilevanti prima di scrivere una riga
2. **SPEC** — micro-spec 10 righe: DONE WHEN misurabile, out-of-scope esplicito
3. **PRE-MORTEM** — ripreso dall'output di Arena (§A2.4), non riscritto da zero
4. **BUILD** — swarm obbligatorio se il workflow copre ≥2 aree disgiunte (es. agenti + skill +
   integrazione APEX-7 = 3 aree → agenti paralleli in background, prompt idempotenti). Blocco
   ⚠️ COORDINAMENTO in STATO-EMPIRE + push PRIMA di iniziare, se Gael/Neri lavorano in parallelo
5. **GATE AUTOMATICO** — deterministico: 0 cartelle vuote, 0 file <15 righe, 0 stub/TODO, JSON/YAML
   validi, **test APEX-7 verdi** (vedi §4)
6. **REVIEW INDIPENDENTE** — torna ad Arena: incolli l'output, Arena fa review (passo 5 del
   ciclo). Se boccia → torna al passo 3 BUILD, non si insiste sullo stesso errore
7. **TEST FUNZIONALE** — esecuzione end-to-end (dry-run prima, poi reale piccola): il workflow
   fa quello che deve, non solo "esiste"
8. **COMMIT** — CP in `company/Memory/checkpoints/` → STATO-EMPIRE aggiornato → wiki/log.md →
   registro (`company/REGISTRO-IMPRESA.md`, ADR-008: proprietario/controllore/origine/governo)
   → push
9. **RETRO** — lezioni nel CP, BACKLOG aggiornato, solo ora si apre il workflow successivo

---

## §4 — Fase C: APEX-7 come gate obbligatorio (il vincolo non negoziabile)

Per ogni agente/skill prodotto in Fase B, prima di segnarlo "operativo":

1. **Integrazione**: l'agente pubblica/consuma eventi sull'EventBus di `11-APEX-7-CORE`
   (`orchestrator/ruflo_core.py`) invece di essere chiamato a mano
2. **Memoria**: usa `APEX7Memory(domain="<nome-workflow>")` — dominio dedicato, isolato dagli
   altri workflow (multi-tenancy già costruita, ADR-010, testata 4/4 in `test_multi_tenant.py`)
3. **Test**: uno unittest analogo a `test_youtube_apex7.py`/`test_multi_tenant.py` che verifica
   l'agente risponde a un evento reale, non mock permanente
4. **Gate di qualità**: definisci soglie concrete per il tuo dominio (es. per YouTube: SEO score
   ≥70, per Preventa: score lead ≥7) — mai un gate che ritorna sempre "PASS" (è il difetto già
   trovato e corretto in APEX-7 YouTube: critic fisso, vedi ADR-010 contesto)

**Solo quando questi 4 punti sono verdi l'agente "esce dall'Arena"** (Regola APEX) ed entra in
produzione.

---

## §5 — Checklist di accettazione del workflow completo

- [ ] MKD prodotto da Arena, espande (non riassume) il contesto reale del dominio
- [ ] N agenti con 7 file canonici ciascuno (spec/system-prompt/tools/playbook/evals/failure-modes/memory)
- [ ] Memory ecosystem presente da subito (checkpoints/decisions/sessions/plans/MEMORY-INDEX.md)
- [ ] Ogni agente integrato su EventBus APEX-7 (`11-APEX-7-CORE`), dominio memoria dedicato
- [ ] Test uniti verdi (unità + almeno 1 E2E) per ogni agente
- [ ] Review indipendente di Arena superata (passo 5), non auto-approvato da chi ha costruito
- [ ] CP scritto, STATO-EMPIRE aggiornato, registro ADR-008 aggiornato, push fatto
- [ ] Nessun claim "operativo" senza numero/test a supporto (standard onestà del repo)

---

## §6 — Nota su cosa NON fare (errori già visti in questo repo)

- **Non ricostruire un motore APEX-7 nuovo per questo workflow** — usa quello consolidato in
  `11-APEX-7-CORE` (ADR-010). Il repo ha già pagato il costo di 4 implementazioni APEX-7
  divergenti create senza saperlo — non aggiungerne una quinta.
- **Non saltare la review di Arena** per far prima — è il passo che oggi manca di più nel repo
  (dossier 26: "build e review cadono spesso sulla stessa sessione").
- **Non dichiarare un agente "operativo" perché il codice esiste** — il precedente più grave
  (CP-20260727-007) ha trovato uno scaffolding APEX-7 reale ma con dati hardcoded ovunque:
  "non manca da costruire, manca di far girare" (dossier 26 §1) resta la diagnosi di fondo.

---

## Connessioni
- [[26-ARENA-COSA-COSTRUIAMO-INSIEME]] — contratto Arena originale (recuperabile da git)
- [[10-METODO-CICLO-FASE]] — ciclo 9 passi applicato qui
- `company/Memory/decisions/ADR-010-fusione-ruflo-apex7.md` — motore APEX-7 consolidato
- `company/Ecosistemi/13-ARENA-APEX/ECOSISTEMA.md` — Regola APEX (vincolo non negoziabile)
- `.agents/skills/master-build-architecture/SKILL.md` — skill di architettura usata in Fase A
