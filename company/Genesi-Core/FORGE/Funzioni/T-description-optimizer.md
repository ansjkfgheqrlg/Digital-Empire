# T-description-optimizer — Funzione L4: Ottimizzazione Trigger Description

> **Ecosistema:** Genesi-Core / FORGE · **Reparto:** SKILL-WORKS (L2.1) · **Workflow:** WF-SKILL-NEW
> **Motore reale:** `skill-creator` (modulo description-optimizer) — vedi `Motori/Mappa-Motori.md` #4
> Collega: [[ECOSISTEMA.md]] · [[BACKBONE.md]] · [[Motori/Mappa-Motori.md]]

---

## Missione
Produrre una **trigger description** che minimizza i falsi positivi e negativi di attivazione. È il campo
`description:` del frontmatter YAML del `SKILL.md` — ciò che l'LLM legge per decidere se e quando invocare
la skill. Una skill con trigger ambigua è inutile anche se il contenuto è perfetto.

---

## Il problema dei falsi positivi/negativi
- **Falso positivo**: la skill si attiva su richieste che non dovrebbe gestire → rumore.
- **Falso negativo**: la skill NON si attiva su richieste che dovrebbe gestire → skill invisibile.

---

## Processo di ottimizzazione
| Passo | Azione | Output |
|---|---|---|
| 1. Analisi eval cases | Legge i casi falliti del T-eval-runner, specie i negativi | lista falsi positivi/negativi |
| 2. Draft description | Scrive: cosa fa, quando sì, quando NO | description draft |
| 3. Test mentale | 5 scenari "trigger o non trigger?" verificati | scenari annotati |
| 4. Versione finale | Description ottimizzata, max 2 righe | description pronta |
| 5. Aggiornamento SKILL.md | Sostituisce il campo `description:` nel frontmatter | SKILL.md aggiornato |

---

## Formula della buona trigger description (≤2 righe)
1. **COSA FA** la skill (azione, non tecnologia).
2. **QUANDO si attiva** (segnali linguistici/contestuali).
3. **QUANDO NON si attiva** (almeno 1 anti-trigger esplicito, se specializzata).

---

## Esempi (da casi DE reali)
**Ambigua:** "Skill per gestire skill e agenti."
**Ottimizzata:** "Crea o migliora skill Claude Code: usa quando l'utente chiede di costruire/aggiornare
una skill, definire un trigger, fare eval. NON usare per domande generali su come funzionano le skill."

---

## Agente operatore
`frg-skill-smith` (Sonnet) — la stessa "persona" che ha scritto il draft (T-draft): conosce la skill nel
dettaglio e ottimizza con cognizione di causa.

## KPI
| Metrica | Target |
|---|---|
| Skill con falsi positivi segnalati in produzione | < 5% |
| Descrizioni con anti-trigger esplicito (quando specializzate) | 100% |
| Lunghezza description oltre 2 righe | 0 |
