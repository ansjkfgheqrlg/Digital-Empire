---
Type: CONCEPT
Status: Active
Tags: #agency #namespace #agentdb #architettura #coerenza
Created: 2026-07-11
Last updated: 2026-07-11
---

# NAMESPACE — Mappa autoritativa dello stato AgentDB (01-AGENCY)

> **Questa è la fonte di verità delle chiavi di stato.** Nessun agente inventa un namespace.
> Prima di scrivere/leggere stato, un agente controlla qui.
> Nato da un difetto reale rilevato al gate del 2026-07-11: due convenzioni convivevano
> (`agency/aN` e `agency/0N-nome`) → gli agenti non si sarebbero trovati le chiavi a vicenda.

---

## Regola canonica

**La chiave AgentDB è `agency/a<N>`** — corta, uniforme, machine-friendly.
La forma lunga del dossier (`agency/02-acquisizione`, ...) è un **alias umano leggibile**:
si usa nella prosa dei documenti, **mai come chiave**.

---

## Namespace per reparto (owner esclusivo della scrittura)

| Reparto | Chiave canonica | Alias leggibile (dossier) | Owner scrittura |
|---|---|---|---|
| A1-Ricerca | `agency/a1` | agency/01-ricerca | AG-A1-* |
| A2-Acquisizione | `agency/a2` | agency/02-acquisizione | AG-A2-* |
| A3-Preventivi | `agency/a3` | agency/03-preventivi | AG-A3-* |
| A4-Delivery | `agency/a4` | agency/04-delivery | AG-A4-* |
| A5-Copywriting-Interno | `agency/a5` | agency/05-copy | AG-A5-* |
| A6-Marketing-Interno | `agency/a6` | agency/06-marketing | AG-A6-* |
| A7-Account-Management | `agency/a7` | agency/07-account | AG-A7-* |
| A8-Closing | `agency/a8` | agency/08-closing | AG-A8-* |
| A9-Partnership-Referral | `agency/a9` | agency/09-partnership | AG-A9-* |
| A10-QA-Cliente | `agency/a10` | agency/10-qa-cliente | AG-A10-* |

---

## Namespace CONDIVISI (trasversali, più reparti leggono)

| Chiave | Owner scrittura | Chi legge | Contenuto |
|---|---|---|---|
| `agency/leads` | A1 (AG-A1-EXTRACT/QUAL) | A2, A9 | Schede lead + score ICP + esito triage |
| `agency/outreach` | A2 (AG-A2-SEND/TRIAGE) | A5, A8 | Messaggi inviati, reply, reply-rate per template |
| `agency/reasoning` | A3, A4 (i *-LEARN) | tutti i COORD | ReasoningBank: win/loss con causa, pattern di delivery |
| `agency/clients` | A4 (AG-A4-HAND) → A7 | A7, A9, A10 | Anagrafica cliente live post-consegna |
| `agency/kpi` | ogni COORD (sola aggiunta) | AG-DIR, Board | KPI aggregati di ecosistema |

---

## Regole di accesso (bloccanti)

1. **Owner unico in scrittura.** Un reparto scrive SOLO sotto la propria chiave `agency/a<N>`
   (+ i condivisi di cui è owner). Scrivere nel namespace di un altro reparto = violazione.
2. **Lettura aperta.** Ogni agente può LEGGERE qualsiasi namespace: gli handoff passano di lì.
3. **A10 non scrive mai fuori da `agency/a10`.** È l'audit indipendente: audita, non costruisce
   (vedi A10 R1/R8 — l'indipendenza del gate dipende da questo).
4. **Append-only** per `agency/reasoning` e per i ledger/log: nessuna riscrittura retroattiva.
5. **Nessun PII** nelle chiavi di stato oltre il minimo necessario (nome/ruolo contatto).
   Mai credenziali, mai segreti. Vedi le REGOLE di ogni reparto.
6. **Nuovo namespace = si aggiorna QUESTO file prima.** Nessuna chiave nasce fuori da qui.

---

## Catena degli handoff (dove passa lo stato)

```
A1 agency/leads ──► A2 agency/outreach ──► A8 agency/a8/calls
                                              │ WIN
        A9 agency/a9 ◄── non-ICP/referral      ▼
                                           A3 agency/a3 (preventivo)
                                              │ firmato
                                              ▼
                                           A4 agency/a4 ──► agency/clients
                                              │                  │
                                              ▼                  ▼
                                    A10 agency/a10          A7 agency/a7
                                    (audit indipendente)    (retention/upsell)
                                                                 │ upsell
                                                                 └──► A3
A5 agency/a5 (copy) alimenta A2 + A8 · A6 agency/a6 (proof) legge agency/clients + agency/a4
```

---

## Connessioni

- [[ARCHITETTURA]] · organo che presidia la coerenza strutturale per-artefatto
- [[01-ECOSISTEMA-AGENCY-V2]] · `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md` — dossier sorgente (alias lunghi)
- [[A10-QA-Cliente]] · `Reparti/A10-QA-Cliente/ARCHITETTURA.md` — audit indipendente, regola 3
- [[A4-Delivery]] · `Reparti/A4-Delivery/state/README.md` — owner di `agency/clients`
