---
Type: SKILLS
Status: Active
Tags: #skills #agency #preventivi #beast-preventivi #proposal-gate #A3
Created: 2026-06-22
Last updated: 2026-06-22
---

# Skill — A3 Preventivi

> Mappa delle skill del reparto: skill esistenti mappate agli agenti + eventuali skill da forgiare.
> ADR-003: dove esiste un asset, si wrappa e si mappa — non si riscrive.

---

## Skill esistenti mappate al reparto

| Skill | Stato | Agente owner | Ruolo in A3 |
|---|---|---|---|
| `beast-preventivi` | Esistente, mappata | AG-A3-PROP | Motore di scrittura problem-first; adatta al livello di consapevolezza (aware/unaware) |
| `market-proposal` | Esistente, mappata | AG-A3-PROP | Struttura commerciale della proposta (value, prove, CTA) — ausiliaria a `beast-preventivi` |
| `discovery-call-brief` | Esistente, mappata | AG-A3-BRIEF | Da trascrizione/appunti call a brief strutturato (problema, awareness, stack, vincoli) |
| `proposal-gate` | Esistente, mappata | AG-A3-QA | Gate Preventivo bloccante: verifica conformità prima dell'invio |
| `market-audit` | Esistente, mappata | AG-A3-AUDIT | Audit di mercato per contestualizzare e quantificare il problema nella nicchia |
| `cro_audit.py` | Esistente, wrappata [WRAPPA] | AG-A3-AUDIT | Audit tecnico deterministico del sito (ADR-003: invocata, non riscritta) — vedi `scripts/README.md` |

---

## Dettaglio skill chiave

### `beast-preventivi` — owner AG-A3-PROP

**Funzione:** costruisce preventivi freelance/agenzia problem-first che vendono. Tutto ruota attorno
al problema del cliente; adatta automaticamente al livello di consapevolezza (aware/unaware); genera
outline → documento completo.
**Quando invocarla:** ogni volta che si scrive un preventivo (anche quando il cliente chiede solo "quanto?").
**Input:** `{problema, audit_quantificato, awareness_level, prodotto_catalogo, pattern_vincenti}`
**Output:** documento problem-first pronto per il Gate Preventivo.
**Vincolo:** non decide prezzi (AG-A3-PRICE/catalogo); promesse = prove (Mandato Art.2).

### `proposal-gate` — owner AG-A3-QA

**Funzione:** Gate Preventivo bloccante. Verifica: problema apre il doc · awareness corretto · solo
pricing catalogo · promesse = prove · scope ≤7gg · clausola proprietà codice + €0 canoni · supporto
90gg · brand voice.
**Quando invocarla:** su OGNI proposta prima dell'invio, senza eccezioni.
**Output:** PASS (abilita invio) o FAIL (diagnosi per item + azione richiesta). **Blocca, non suggerisce.**

### `discovery-call-brief` — owner AG-A3-BRIEF

**Funzione:** trasforma trascrizione/appunti della discovery call in un brief strutturato.
**Output:** problema (parole cliente), awareness level, stack attuale, vincoli ambiente/server.
**Vincolo:** flagga i campi mancanti (specie i vincoli ambiente, che servono ad A4).

---

## Regola anti-contraddizione (se si forgiano skill nuove)

Il reparto oggi opera interamente su skill esistenti mappate. Se in futuro si forgia una skill propria
(es. un orchestratore di pipeline preventivi):
1. Eseguire `skill-contradiction-analyzer` contro `beast-preventivi`, `market-proposal`, `proposal-gate`.
2. Se sovrapposizione: la skill nuova IMPLEMENTA/ESTENDE quella esistente, non la ridefinisce.
3. Gerarchia: skill nuova = orchestratore; skill esistente = motore o knowledge base.

---

## Connessioni

- [[ag-a3-prop]] · `agenti/ag-a3-prop.md` — owner di `beast-preventivi` + `market-proposal`
- [[ag-a3-qa]] · `agenti/ag-a3-qa.md` — owner di `proposal-gate`
- [[scripts/README]] · `scripts/README.md` — wrapper `cro_audit.py` (ADR-003)
- [[01-ECOSISTEMA-AGENCY-V2]] · `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md §A3` — skill del reparto
