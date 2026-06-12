> Fonte: PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md sez. 2-A2 + sez. 8 (cap reali) + sez. 5 (sender.py)

# T-SENDER — Sender con Rate Limiting

> Funzione L4 di A2-ACQUISIZIONE · Worker · Agente: `AG-A2-SEND-W` (haiku)
> Fonte vincolante: `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md` §2-A2 + §8

## Cosa fa

Invia i messaggi approvati dal Gate Bibbia rispettando i cap reali. Logga ogni invio.
Script: `sender.py`. I cap NON sono negoziabili senza ADR approvato.

## Cap reali (invariati — ADR-003)

| Canale | Cap giornaliero | Cap orario | Note |
|---|---|---|---|
| Email | ≤500/gg | ≤100/h | protezione deliverability |
| LinkedIn connessioni | ≤20/gg | — | limite LinkedIn |
| LinkedIn messaggi | ≤20/gg | — | limite LinkedIn |
| LinkedIn commenti | ≤30/gg | — | limite LinkedIn |
| Instagram DM | ≤30/gg | — | protezione account |

## Comportamento

- Pre-flight: verifica credenziali (sessione LinkedIn, token SMTP, sessione Instagram) prima di ogni run
- Se credenziale scaduta → il canale NON parte; alert su dashboard; gli altri canali proseguono
- Rate limiter: `sender.py` gestisce la distribuzione temporale nell'ora (email: max 100/h → ~1.67/min)
- Log ogni invio: `{messaggio_id, lead_email, canale, timestamp, stato: sent|failed}` in `agency/outreach`
- Evento `run_done` emesso a fine run in `company/metrics/runs.jsonl`

## Dry-run

Con `--dry-run`: simula la run completa (verifica cap, distribuzione temporale, pre-flight
credenziali) senza inviare nulla. Output: anteprima N messaggi che verranno inviati + stima
tempo run. Obbligatorio su ogni batch nuovo (pattern #3).

## Failure

| Evento | Risposta |
|---|---|
| SMTP bounce rate > X% | stop invii email; alert a AG-A2-COORD; pattern in agency/reasoning |
| Credenziale LinkedIn / Instagram scaduta in mid-run | stop quel canale; log parziale; alert dashboard |
| Cap giornaliero raggiunto | stop e log; mai superare il cap anche se ci sono lead in coda |
| Token FB scaduto (blocco noto) | stop Instagram; runbook rinnovo in HC-AG-OP-01 |

## Connessioni

- [`./T-bibbia-qa.md`](./T-bibbia-qa.md) (fornitore: solo messaggi PASS) · [`./T-reply-triage.md`](./T-reply-triage.md) (riprende le risposte)
- [`../Reparti/A2-Acquisizione/`](../Reparti/A2-Acquisizione/)
- [`../../ECOSISTEMA.md`](../ECOSISTEMA.md)
