# WF-SCHEMA-EVOLVE
## Migliora la costituzione delle strutture

> Organo: ARCHITETTURA (Genesi Core) · Reparto owner: L2.3 Schemi Canonici · Stato: DEFINED
> Quando un buco strutturale **ricorrente** emerge dai blueprint/artefatti reali, lo schema canonico
> si aggiorna (nuova versione + diff). Così la "costituzione" delle strutture migliora e la FORGE
> sbaglia meno. Non bloccante per il singolo task; migliorativo per tutti i futuri. Fonte: 14-DOSSIER-ARCHITETTURA §4 nota + §7 (ReasoningBank).
> Collega: [[ECOSISTEMA.md]] · [[BACKBONE.md]]

---

## Trigger
- **WF-STRUCT-VALIDATE** segnala lo **stesso buco** su uno schema in ≥N validazioni (ReasoningBank: "gli agenti dimenticano sempre l'escalation").
- WF-ARCH-DESIGN incontra una richiesta che **nessuno schema esistente copre** → serve una FORMA nuova (schema mancante, bloccante per quel task).
- Un motore reale (architect-agent, agent-factory, skill-creator) evolve e introduce una sezione che lo schema deve riflettere.
- **Natura:** un nuovo schema o una nuova versione = decisione strutturale → genera un ADR (HC-ME-ADR verso 10-MEMORY).

---

## Input (JSON)
```json
{
  "evolve_id": "EVO-2026-0619-007",
  "schema_target": "agente",
  "trigger": "buco-ricorrente | schema-mancante | motore-evoluto",
  "evidenza": [
    "VAL-...-031: campo 'escalation' assente",
    "VAL-...-044: campo 'escalation' assente",
    "VAL-...-058: campo 'escalation' assente"
  ],
  "proposta": "rendere 'escalation' campo OBBLIGATORIO nello schema agente"
}
```

---

## Pipeline (passi · agente owner)
```
1. RACCOLTA EVIDENZA                   (arch-schema-keeper)
   └── raccoglie le validazioni che mostrano lo stesso buco da architettura/validazioni/ (ReasoningBank).
        soglia non raggiunta → BACKLOG (item minore, non si tocca lo schema per un caso singolo).

2. DIAGNOSI FORMA                      (arch-blueprint + arch-schema-keeper)
   ├── è un campo mancante nello schema esistente? → evoluzione di versione.
   └── è una FORMA del tutto nuova (es. "ecosistema" non esisteva)? → nuovo schema canonico.

3. DRAFT NUOVA VERSIONE                (arch-schema-keeper)
   ├── crea schema@vN+1 con il campo/sezione aggiunto + REGOLE di validazione aggiornate.
   └── produce il DIFF vN → vN+1 (cosa cambia, perché, impatto sui blueprint esistenti).

4. CONTRADDIZIONE / RETROCOMPAT        (arch-contradiction)
   └── la nuova versione rompe blueprint già consegnati? marca migrazione (i vecchi restano su vN, i nuovi nascono su vN+1).

5. ADR + PUBBLICAZIONE                 (arch-director → 10-MEMORY)
   ├── decisione strutturale → HC-ME-ADR (WF-ADR-REGISTER) per ADR in company/Memory/decisions/.
   └── schema@vN+1 pubblicato in architettura/schemi/<target>@vN+1 (vN resta per audit/migrazione).
```

---

## Gate
- **G-EVO1 (soglia):** uno schema non si tocca per un caso singolo — serve ricorrenza (evidenza ≥ soglia) o schema mancante. Caso singolo → BACKLOG (ADR-005).
- **G-EVO2 (versionato):** ogni cambiamento = nuova versione `@vN+1` + DIFF esplicito. Mai mutazione in-place silenziosa.
- **G-EVO3 (ADR):** nuovo schema o nuova versione = ADR registrato (la costituzione cambia → tracciato).
- **G-EVO4 (retrocompat):** i blueprint esistenti su `vN` restano validi; solo i nuovi nascono su `vN+1` (migrazione esplicita se serve).
- **G-EVO5 (no-gabbia):** lo schema resta minima-ma-completo — si aggiunge solo ciò che serve, non si gonfia (§1 dossier: la lista NON è una gabbia).

---

## Output (JSON)
```json
{
  "evolve_id": "EVO-2026-0619-007",
  "schema_nuovo": "agente@v2",
  "schema_precedente": "agente@v1",
  "diff": "+ campo OBBLIGATORIO 'escalation' (tabella failure→contromisura); regola: assente => buco BLOCK",
  "adr_id": "ADR-NNN",
  "retrocompat": "blueprint v1 restano validi; nuovi su v2",
  "stato": "PUBBLICATO"
}
```

---

## Handoff
- **→ L2.3 Schemi Canonici:** `arch-schema-keeper` pubblica `schema@vN+1`; da subito WF-ARCH-DESIGN carica la nuova versione.
- **→ 10-MEMORY (HC-ME-ADR / WF-ADR-REGISTER):** registra l'ADR della modifica strutturale.
- **← WF-STRUCT-VALIDATE / WF-ARCH-DESIGN:** sorgenti dei trigger (buco ricorrente / schema mancante).
- Nessun handoff alla FORGE: questo workflow non crea artefatti, **migliora le regole** con cui si creano.

---

## Dry-run
3 validazioni mostrano `escalation` assente negli agenti. Schema-keeper supera la soglia, blueprint diagnostica
"campo mancante", produce `agente@v2` con `escalation` OBBLIGATORIO + DIFF, contradiction conferma retrocompat
(v1 restano validi), director apre ADR e pubblica `agente@v2`. Da qui ogni nuovo blueprint-agente è validato
contro v2 → il buco "escalation dimenticata" sparisce strutturalmente. ReasoningBank chiuso.

---

## Connessioni
- [[WF-STRUCT-VALIDATE]] — sorgente dei buchi ricorrenti (ReasoningBank)
- [[WF-ARCH-DESIGN]] — invoca questo WF quando lo schema manca (bloccante per quel task)
- [[arch-schema-keeper]] — owner degli schemi · [[arch-blueprint]] — diagnosi forma · [[arch-contradiction]] — retrocompat · [[arch-director]] — ADR
- [[14-DOSSIER-ARCHITETTURA]] §4 (nota WF-SCHEMA-EVOLVE) · §7 (ReasoningBank) — fonte di verità
- 10-MEMORY: WF-ADR-REGISTER — registrazione ADR della modifica strutturale · BACKLOG.md — item sotto-soglia
