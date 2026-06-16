# Libreria degli Schemi Canonici — ARCHITETTURA

> Il **cuore dell'organo ARCHITETTURA** (Genesi Core). Per OGNI forma che la FORGE può creare
> esiste qui un **modello al millimetro**: sezioni obbligatorie, template vuoto, checklist di
> completezza (alimenta `struct-gate`), esempio minimo, anti-pattern. Fonte di verità:
> `PIANO-MAESTRO/14-DOSSIER-ARCHITETTURA.md` §1. Custode: `arch-schema-keeper`.

---

## IL PRINCIPIO MADRE — scegli la FORMA GIUSTA con ingegno

**ARCHITETTURA non applica la stessa forma a tutto.** Prima di disegnare, la domanda è sempre:
*"qual è la forma minima-ma-completa che questa cosa richiede?"* — mai gonfiare, mai banalizzare.
È la decisione più importante dell'organo (Max, 2026-06-16).

- Le **forme leggere** (Principio, Stile, Skill) NON ricevono il trattamento pesante di un
  ecosistema: niente org chart, niente KPI di reparto, niente I/O JSON forzato. Sarebbe **spreco**.
- Le **forme con agenti** (Team, Reparto, Ecosistema) seguono lo schema "team-canonico":
  coordinator, I/O espliciti, acceptance, escalation, shared_state.
- Le **forme-conoscenza** (Principio, Stile, Documento/MKD) seguono lo schema del loro tipo.
- La lista NON è una gabbia: se una cosa richiede una forma nuova, `arch-schema-keeper` la aggiunge
  (WF-SCHEMA-EVOLVE) con versione + diff.

**Errare per eccesso (ecosistema su un principio) è grave quanto errare per difetto (skill thin su
un'area che era un ecosistema). L'ingegno sta nel calibrare il peso.**

---

## Le 9 forme (+ questo indice)

| Schema | Peso | Usa quando | Motore reale |
|---|---|---|---|
| [[Schema-Skill]] | leggera-media | capability invocabile, singolo esecutore | `skill-creator`, Skill Master Architecture |
| [[Schema-Agente]] | media | entità autonoma con I/O JSON, escalation, KPI | `architect-agent`, agent-factory |
| [[Schema-Team]] | medio-pesante | ≥2 ruoli che si coordinano con handoff | swarm, T-org-design |
| [[Schema-Principio]] | LEGGERA | una regola-guida (knowledge) | P01..P15 SMA |
| [[Schema-Stile]] | LEGGERA | coerenza visiva/voce di un brand | empire-premium-style |
| [[Schema-Workflow]] | media | processo a passi con gate e owner | SPARC, agent-planner |
| [[Schema-Documento-MKD]] | medio-pesante | conoscenza ampia canonica, mai riassunta | content-forge (MKD) |
| [[Schema-Reparto]] | PESANTE | unità organizzativa permanente (L2) | org-design |
| [[Schema-Ecosistema]] | PIÙ PESANTE | intera area L1→L5 con BACKBONE+namespace | ecosystem-scaffold |

---

## Decision tree — quale forma?

```
La cosa è SAPERE (non si esegue)?
├─ SÌ → è UNA regola? → Principio · è visiva/voce? → Stile · è un corpo ampio? → Documento/MKD
└─ NO (si esegue) →
   ├─ è un PROCESSO a passi con gate/owner? → Workflow
   ├─ è una CAPABILITY invocabile, 1 esecutore, senza stato? → Skill
   ├─ è UN'entità autonoma con I/O JSON? → Agente
   ├─ servono ≥2 ruoli che si coordinano (ad-hoc)? → Team
   ├─ è un'unità organizzativa PERMANENTE (L2)? → Reparto
   └─ è un'intera AREA L1→L5 (BACKBONE+namespace)? → Ecosistema
```

---

## Come si usano questi schemi (nel ciclo ARCHITETTURA)

1. `arch-schema-keeper` carica lo schema della forma richiesta (WF-ARCH-DESIGN, passo schema).
2. `arch-blueprint` costruisce la struttura millimetrica usando "Struttura obbligatoria" + "Template vuoto".
3. `arch-validator` esegue `struct-gate`: scorre la **Checklist di completezza** voce per voce →
   restituisce `{COMPLETO | INCOMPLETO, buchi:[...]}`. Le checklist sono binarie e verificabili
   proprio per essere eseguibili (non descrittive-vaghe).
4. Solo `COMPLETO` passa alla FORGE (regola di blocco: niente costruzione al buio).
5. Se un artefatto reale rivela un buco nello schema → WF-SCHEMA-EVOLVE aggiorna lo schema (versione+diff)
   e la ReasoningBank lo memorizza: la "costituzione" delle strutture migliora nel tempo.

---

## Convenzioni della libreria
- **Naming Title-Case FISSO** (`Schema-<Forma>.md`) — mai mischiare maiuscolo/minuscolo
  (lezione collisione Windows, 2026-06-16).
- Ogni file-schema: ~50–100 righe, stessa anatomia (Quando si usa → Struttura → Template → Checklist
  → Esempio minimo → Anti-pattern → Connessioni).
- Le checklist di completezza sono il contratto verso `struct-gate`: tenute binarie e aggiornate.

## Connessioni
- 14-DOSSIER-ARCHITETTURA §0 (missione), §1 (le forme), §4 (workflow), §5 (skill `canonical-schema`/`struct-gate`)
- [[Schema-Skill]] [[Schema-Agente]] [[Schema-Team]] [[Schema-Principio]] [[Schema-Stile]] [[Schema-Workflow]] [[Schema-Documento-MKD]] [[Schema-Reparto]] [[Schema-Ecosistema]]
