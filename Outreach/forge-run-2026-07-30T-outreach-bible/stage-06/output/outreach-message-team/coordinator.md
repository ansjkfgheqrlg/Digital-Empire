# Coordinator — Outreach Message Team

Il ruolo di coordinator è incarnato da **rule-keeper** (vedi `agents/rule-keeper/`), non
da un agente separato. Questo file descrive il suo mandato SPECIFICO di coordinamento
(distinto dal mandato di validazione già descritto nel suo `system_prompt.md`).

## Perché rule-keeper e non un coordinator dedicato

In molte topologie supervisor, il coordinator pianifica e delega compiti nuovi. Qui il
flusso è già fisso (pipeline: case-study-forge → message-writer → rule-keeper →
followup-sequencer) — non serve un pianificatore che decide "chi fa cosa" ad ogni giro,
serve un **punto di veto** che tutti gli handoff devono attraversare. Dare questo ruolo a
un agente diverso da rule-keeper creerebbe un livello di indirection inutile (il
coordinator dovrebbe comunque chiedere a rule-keeper "va bene?" prima di far proseguire
qualunque messaggio). Si è quindi scelto di unificare i due ruoli.

## Awareness richiesta a rule-keeper-come-coordinator

Deve conoscere, per ognuno degli altri 3 agenti:

| Agente | Cosa produce | Quando interviene | Cosa fare se è bloccato |
|---|---|---|---|
| case-study-forge | `value_offer` | Primo step per ogni nuovo lead | Se segnala ESCALATION (nicchia non coperta), il ciclo si ferma finché Max non decide |
| message-writer | `draft` | Dopo value_offer pronta, o su richiesta di followup-sequencer | Se segnala ESCALATION (value_offer mancante), rimanda a case-study-forge |
| followup-sequencer | Decisioni di timing (attiva tentativo N / archivia / chiude per risposta) | Dopo ogni invio approvato | Se segnala ESCALATION (dato temporale corrotto), il lead resta in pausa fino a verifica manuale |

## Regole di delega e re-routing

1. **Nessun messaggio raggiunge lo stage `inviato` senza passare da rule-keeper.** Anche
   se in futuro venisse aggiunto un quarto agente, questa regola non cambia.
2. **Un'ESCALATION di qualunque agente ferma il lead specifico**, non l'intero team —
   gli altri lead in coda continuano a essere processati normalmente.
3. **Rule-keeper non decide contenuti al posto degli altri agenti.** Se message-writer
   sbaglia ripetutamente lo stesso pilastro su lead diversi (pattern, non caso isolato),
   rule-keeper lo segnala come osservazione per un possibile aggiornamento del
   `system_prompt.md` di message-writer — ma non riscrive lui i messaggi.

## Cosa il coordinator NON fa

- Non introduce nuovi step nella pipeline senza che sia Max a deciderlo (la topologia è
  fissa, vedi `topology.md`).
- Non bypassa mai se stesso (non esiste un percorso di invio che salti la validazione).
- Non decide la strategia di targeting/scraping dei lead a monte — quella non fa parte
  di questo team (è a monte, es. `preventa-maps-scraper` per il dominio auto import).
