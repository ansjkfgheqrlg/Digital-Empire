# 🧬 CICLO v3 — SELF-HEALING HARDENING (stress-test anti-fragile)
> Ciclo 2 di 3 · Metodo: 5 scenari di failure simulati contro la struttura v2 (post-audit). Regola: la rete deve **guarire da sola**; se serve un umano per guarire, è un bug → patch strutturale (mai nuovo tooling).

## Scenario S1 — "Agente morto" nel momento peggiore
**Setup:** forge-builder muore a metà del build del funnel S2 (22/07, gate alle h20:00).

1. Heartbeat mancato al SYNC → router marca `AWOL` dopo 2 sync saltati.
2. `SLA miss` sul task attivo → router **riassegna automaticamente al backup** (funnel-engineer, già dichiarato nella team map v2).
3. Task continua; TRUTH-CMD logga `ERR` + CP di handover.

**🕳️ Buco trovato:** e se muore ANCHE il backup su un task revenue-critico?
**🩹 Patch H1 — catena 3-deep per ruoli revenue-critici:** closer-a8 → pricing-cell → revenue-ops-dir; funnel-engineer → forge-builder → forge-dir. Sostituzioni SOLO nella catena pre-dichiarata (niente improvvisazioni). ✅ autoguarisce senza umani.

## Scenario S2 — "Regolatore in loop" (falso positivo)
**Setup:** cadence-guard emette RULE-BLOCK su social-ops per una regola interpretata male; social-ops è innocente ma bloccato.

1. Primo RULE-BLOCK valido, social-ops fermo.
2. Al **3° block in 1h dalla stessa (regola, agente)**: circuit-breaker → il regolatore passa in `FROZEN` + ALERT a TRUTH-CMD.
3. **Quorum:** un BLOCK persistente richiede co-firma di un **2° regolatore** (diversa regola-base) entro 1h, altrimenti decade a WARN.
4. constitution-guard arbitra; esito scritto in `errors/` (alimenta mutation del prompt del regolatore, ciclo v4).

**🕳️ Buco trovato:** e se due regolatori colludono per errore (stessa regola letta male entrambi)?
**🩹 Patch H2 — appello con timer (da R8):** OVERRIDE-REQ di BUILD-CMD a Max; se Max non risponde in 4h su task P0-revenue, vale l'eccezione prevista dalla costituzione per quella regola (con log pubblico sulla board). ✅ autoguarisce; mai gridlock >4h.

## Scenario S3 — "Board intasata o down"
**Setup:** giorno di chiusure S1: 60+ messaggi, quota 30/giorno superata alle 15:00.

1. **Load-shedding del router:** P3 → aggregati in digest EOD · P2 → trattenuti 4h · P1/P0 → passano sempre.
2. **Board down/corrotta:** modalità degradata → gli agenti scrivono in `09-BOARD/emergency/` (file flat, stesso schema, id message idempotente).
3. **Ripristino:** replay `emergency/`→`messages/` deduplicato da memory-keeper; heartbeat EC continua su canale emergency.

**🩹 Patch H3:** gli id messaggio sono idempotenti (`MSG-<data>-<from>-<hash>`) — un replay non duplica mai. Il digest Max funziona anche in degraded-mode. ✅ il sistema parla anche da ferito.

## Scenario S4 — "Comando in conflitto"
**Setup:** REVENUE-CMD vuole slittare WF-S5 per dare ore a S1; BUILD-CMD rifiuta (ha promesso il video entro il 25/07).

1. **Matrice di arbitrato:** si applica la tabella €/h di P4 → S1 vince (revenue-first, ADR-EST-001). Conflitto risolto in automatico.
2. Se la matrice pareggia → **timer 4h** → decide EMPIRE-COMMANDER.
3. Se il conflitto COINVOLGE EC → **quorum 3/4** dei comandanti + DECISION-REQ parallela a Max.

**🩹 Patch H4 — default = piano invariato:** finché Max non risponde, si esegue il MASTER PLAN com'è scritto. Il conflitto non può fermare la macchina: **fermo il dibattito, mai il flusso**. ✅

## Scenario S5 — "Max assente 48h+" (ferie, imprevisto)
**Setup:** Max irraggiungibile giovedì-venerdì.

1. Tutte le DECISION-REQ scadono → **default ATTIVI** automaticamente (pattern già attivo, R10 del v2).
2. I gate continuano; le chiusure S1 proseguono a condizioni standard (termini offerta fissi, mai sconti extra).

**🕳️ Buco trovato:** il sistema NON deve poter: spendere soldi >50€, firmare condizioni fuori standard, cambiare la costituzione.
**🩹 Patch H5 — freno secco:** in assenza di Max, queste 3 azioni vanno in `PARKED` (coda congelata, riattivata al ritorno). Regola: **il sistema procede, ma non firma**. TRUTH-CMD certifica al ritorno: log completo di ciò che è stato deciso dai default. ✅

## 3. BOLLETTINO POST-STRESS (v3 = v2 + patch)

| Patch | Cosa aggiunge | Cosa NON aggiunge |
|---|---|---|
| H1 catene 3-deep | mappa successioni ruoli critici | nessun agente (sono i backup/2° backup già esistenti) |
| H2 quorum regolatori + circuit-breaker + appello | regole di arbitrato | nessun regolatore nuovo |
| H3 idempotenza + emergency replay | specifica router | nessun canale nuovo (emergency = cartella della stessa board) |
| H4 arbitrato + plan-as-default | regola decisionale | nessun livello gerarchico |
| H5 freno "procede ma non firma" | policy PARKED | nessun controllo umano aggiuntivo |

**Esito:** tutti i 5 scenari si chiudono senza intervento umano, tranne S5 che si chiude *volontariamente* in attesa dell'umano (by design). Struttura **anti-fragile** certificata a simulazione; da validare al primo self-audit live (F6).

---
⛓️ Trace P12: `CICLO-v3#ecosystem` · input: CICLO-v2 (R1..R10) · patch: H1..H5 · prossimo: CICLO-v4 optimization
