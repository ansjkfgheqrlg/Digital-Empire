> Fonte: PIANO-MAESTRO/06-ECOSISTEMI-CORE.md sez. 07 L2 SKILL-WORKS · L4 T-description-optimizer

# T-description-optimizer — Funzione L4: Ottimizzazione Trigger Description

**Ecosistema:** 07-FORGE · **Reparto:** SKILL-WORKS (L2.1) · **Workflow:** WF-SKILL-NEW

Collega: [[07-FORGE/ECOSISTEMA.md]] · [[07-FORGE/BACKBONE.md]]

---

## Missione

Produrre una **trigger description** per la skill che minimizza i falsi positivi e i falsi
negativi di attivazione. La description è il campo `description:` del frontmatter YAML del
SKILL.md — è ciò che il modello LLM legge per decidere se e quando invocare la skill.

---

## Il problema dei falsi positivi/negativi

- **Falso positivo**: la skill si attiva su richieste che non dovrebbe gestire → rumore
- **Falso negativo**: la skill NON si attiva su richieste che dovrebbe gestire → skill invisibile

Una skill con trigger description ambigua è inutile anche se il contenuto è perfetto.

---

## Processo di ottimizzazione

| Passo | Azione | Output |
|---|---|---|
| **1. Analisi eval cases** | Legge i casi falliti del T-eval-runner, specialmente i negativi | lista falsi positivi/negativi osservati |
| **2. Draft description** | Scrive descrizione che include: cosa fa, quando sì, quando NO | description draft |
| **3. Test mentale** | 5 scenari "trigger o non trigger?" verificati sulla description | scenari annotati |
| **4. Versione finale** | Description ottimizzata, max 2 righe | description pronta per il SKILL.md |
| **5. Aggiornamento SKILL.md** | Sostituisce il campo `description:` nel frontmatter | SKILL.md aggiornato |

---

## Formula della buona trigger description

La description efficace risponde a queste domande in ≤2 righe:
1. **COSA FA** la skill (in termini di azione, non di tecnologia)
2. **QUANDO si attiva** (segnali linguistici/contestuali che la triggerano)
3. **QUANDO NON si attiva** (almeno 1 anti-trigger esplicito, se la skill è specializzata)

---

## Esempi (da casi DE reali)

**Ambigua (non ottimizzata):**
> "Skill per gestire skill e agenti."

**Ottimizzata:**
> "Crea o migliora skill Claude Code: usa quando l'utente chiede di costruire/aggiornare
> una skill, definire un trigger, fare eval. NON usare per domande generali su come
> funzionano le skill."

---

## Agente operatore

`frg-skill-smith` (Sonnet) — è la stessa persona che ha scritto il draft (T-draft):
conosce la skill nel dettaglio, può ottimizzare con cognizione di causa.

---

## KPI

| Metrica | Target |
|---|---|
| Skill con falsi positivi segnalati in produzione | < 5% |
| Descrizioni trigger con anti-trigger esplicito (quando specializzate) | 100% |
| Lunghezza description oltre 2 righe | 0 |
