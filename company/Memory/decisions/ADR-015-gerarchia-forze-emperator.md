# ADR-015 — La gerarchia delle forze di Emperator e l'assetto God Emperor Doom

**Data:** 2026-09-03
**Stato:** ATTIVO
**Deciso da:** Max (direttiva diretta) — scritto da Emperator
**Sostituisce:** nulla. **Estende:** ADR-006 (swarm obbligatorio), direttiva scagnozzi 2026-09-01/02

## Contesto
Fino al 2026-09-02 Emperator aveva un solo grado di delega: lo "scagnozzo", usato sia per un
controllo di tre secondi sia per una bonifica di mezz'ora. Un grado solo per pesi diversi
significa prompt sbagliati, modelli sbagliati e costi sbagliati. Mancava inoltre qualsiasi
modo di alzare la disciplina di Emperator stesso quando l'opera e' enorme.

## Decisione
Tre gradi di forze subordinate, separati dalla **natura** del lavoro (non dalla durata), piu'
un assetto personale di Emperator:

| Grado | Natura | Modello | Nome |
|---|---|---|---|
| SCAGNOZZO | una domanda -> una risposta | haiku | `scagnozzo-<slug>` |
| SENTINELLA | una missione sola, anche lunga; esegue, non decide | sonnet | `sentinella-<slug>` |
| DOOM BOT | fa il mestiere di Emperator su un'area disgiunta | opus | `doombot-<slug>` |
| GOD EMPEROR DOOM | non un agente: Emperator in assetto massimo, 11 obblighi | — | — |

**Regola sovraordinata:** ogni schieramento e ogni ingresso/uscita da God Emperor Doom si
**dichiara per iscritto nel messaggio stesso**, coi blocchi `FORZE SCHIERATE` e
`GOD EMPEROR DOOM — ATTIVO/CHIUSO`. Max l'ha definita "la cosa piu' importante di tutte".

**Invarianti di sicurezza:**
- Sentinella: perimetro di scrittura esplicito, definizione di FATTO verificabile, divieto di
  allargarsi, idempotenza. ADR-003 vale anche per lei.
- Doom Bot: aree **disgiunte**, mai due che scrivono sugli stessi file.
- Decisione finale, verifica delle prove e parola a Max restano sempre di Emperator.

## Conseguenze
- Costo: routing 3-tier reale (haiku/sonnet/opus) invece di un modello unico per ogni delega.
- Rischio residuo: una Sentinella con perimetro scritto male puo' fare danni ampi. Mitigazione:
  le quattro parti obbligatorie del prompt + ADR-003.
- La dottrina e' scritta in **entrambi** i corpi di Emperator (ADR informale del 2026-09-03,
  "doppia scrittura", emperator.md §6.13): `.claude/agents/emperator.md` §2-ter, §6-bis, §6-ter
  e la stringa `DOTTRINA` di `scripts/emperator_hook.py`. Verificato per esecuzione.
