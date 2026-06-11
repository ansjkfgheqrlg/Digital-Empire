# A2 — ACQUISIZIONE / OUTREACH

> Reparto L2 di 01-AGENCY · Coordinatore: `AG-A2-COORD` (sonnet — oggi `orchestrator.py`)
> Topologia: `pipeline` (strategist→writer→bibbia→sender) + `star` per i 3 canali
> Fonte vincolante: `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md` §2-A2 · ⚠️ **ADR-003: runtime ATTIVO, si wrappa, non si riscrive**

## Cosa fa

Converte lead qualificati in **discovery call prenotate**, su 3 canali, dentro i cap reali.
CTA standard di ogni canale: **presentazione-empire.vercel.app**.

| Livello | Team | Flusso / Funzione |
|---|---|---|
| L3 | `WF-OUTREACH-EMAIL` | **ESISTENTE, NON SI TOCCA**: scraper → qualifier → strategist → writer (APSOC) → **Bibbia 3-checker QA** → sender. Fino a 500/gg, cap 100/h |
| L3 | `WF-OUTREACH-LINKEDIN` | 20 connessioni + 20 messaggi + 30 commenti/gg (script 01→05 + comment_posts.py) |
| L3 | `WF-OUTREACH-INSTAGRAM` | 30 DM/gg, pattern 2 messaggi (corpo + link), follow-up |
| L3 | `WF-REPLY-FOLLOWUP` | reply_monitor → triage risposta → conversation_manager → follow-up (followup_writer) → booking call |
| L4 | `T-strategist` | angolo di attacco per lead (strategist.py, insight.py) |
| L4 | `T-writer-apsoc` | scrittura messaggio (writer.py, humanizer.py, copy_knowledge.py) |
| L4 | `T-bibbia-qa` | gate qualità 3-checker pre-invio (bibbia_team.py) — **BLOCCA, non suggerisce** |
| L4 | `T-sender` | invio + rate limiting + log (sender.py) |
| L4 | `T-reply-triage` | classificazione risposte: interessato / obiezione / no / out-of-office |
| L4 | `T-followup` | sequenze follow-up multi-touch (run_followup.py, skill `cold-email`) |
| L4 | `T-li-engage` | commenti + connessioni LinkedIn |
| L4 | `T-ig-dm` | DM Instagram + follow-up 2 step |

Agenti L5: `AG-A2-COORD` · `AG-A2-STRAT-W` · `AG-A2-WRITE-W` · `AG-A2-BIBBIA-C1/C2/C3` ·
`AG-A2-SEND-W` · `AG-A2-TRIAGE-W` · `AG-A2-FUP-W` · `AG-A2-LI-W` · `AG-A2-IG-W`.

## Come si collega

| Direzione | Con chi | Cosa passa |
|---|---|---|
| ← A1 Ricerca | intra-BUS | lead qualificati da `leads.db` (score ≥ soglia) |
| → A3 Preventivi | intra-BUS | call prenotata + thread conversazione (contesto per il brief) |
| → A5 Copy-interno | intra-BUS | dati reply reali per il refresh template (`WF-COPY-OUTREACH`) |
| → 08 INTELLIGENCE | `HC-AG-IN-01` | obiezioni reali, motivi rifiuto, domande ricorrenti (anonimizzati) |
| ← 04 MARKETING | `HC-MK-AG-01` | refresh template maggiori (passati da Copy/APSOC Guild + Bibbia) |
| ← 09 OPERATIONS | `HC-OP-AG-01` | scheduling run giornaliere, cost guard, pre-flight credenziali |
| Memoria | `agency/outreach` + `agency/conversations` | template/performance · thread (PII-scan prima dello store) |

Entrypoint operativi (skill installate): `avvia-email`, `avvia-linkedin`, `avvia-ig`,
`avvia-parallel`, `avvia-scraper`. Knowledge layer: skill `cold-email`, `agency-scalping`,
`outreach-reply-triage` (riusabile anche dai clienti Outreach Factory — pattern #11).

## 🧠 Come si ATTIVA e RAGIONA

**Trigger.**
1. Run giornaliera schedulata (email/LI/IG) via 09 OPERATIONS — è il battito cardiaco del reparto.
2. Risposta in ingresso → `WF-REPLY-FOLLOWUP` si attiva in tempo reale (reply_monitor).
3. Template in calo (reply rate sotto baseline 2 cicli) → richiesta refresh ad A5/04-MARKETING.

**Decomposizione.** `AG-A2-COORD` (orchestrator.py) apre la run: pre-flight credenziali
(token FB, sessione LinkedIn) → carica batch lead da `leads.db` → fan-out `star` sui 3 canali,
ciascuno internamente `pipeline`: strategist (angolo) → writer (APSOC) → Bibbia (gate) → sender.

**Esecuzione.** Cap NON negoziabili: email ≤500/gg con cap 100/h · LinkedIn 20 connessioni +
20 messaggi + 30 commenti/gg · Instagram 30 DM/gg. Il sender applica rate limiting e logga ogni
invio. Ogni messaggio passa il Gate Bibbia PRIMA dell'invio: un solo checker boccia → il
messaggio NON parte, torna al writer con note. Dry-run disponibile su ogni canale
(anteprima messaggi + stima volumi senza invio).

**Handoff.** Risposta "interessato" → conversation_manager gestisce il thread fino alla call
prenotata → handoff ad A3 con storico completo. Lead "non ora/budget basso" → `HC-AG-IB-01`
verso 02 INFO-BUSINESS. Obiezioni ricorrenti → `HC-AG-IN-01` verso 08.

**Failure.**
- Bounce/error rate in salita → Sentinel Quality osserva; pattern di bounce distillato in `agency/reasoning`.
- Credenziale scaduta in pre-flight → run del canale NON parte, alert su dashboard, runbook rinnovo.
- Gate Bibbia boccia in serie lo stesso template → template ritirato, richiesta refresh ad A5.
- MAI rispondere a un "no" (regola triage); 2 reject handoff consecutivi → escalation a AG-DIR.

## KPI e cap reali

| KPI | Cap/vincolo reale |
|---|---|
| Inviati/gg per canale | email ≤500/gg cap 100/h · LI 20+20+30/gg · IG 30 DM/gg |
| Reply rate · positive reply rate | baseline dal giorno 1, mai inventata |
| Call prenotate/settimana | output finale del reparto |

I cap non si alzano senza dati (OUT OF SCOPE del dossier §0): proteggono deliverability e account.

## Connessioni

- `../../Workflow/WF-OUTREACH-EMAIL/` · `WF-OUTREACH-LINKEDIN/` · `WF-OUTREACH-INSTAGRAM/` · `WF-REPLY-FOLLOWUP/`
- `../../Funzioni/T-strategist/` · `T-writer-apsoc/` · `T-bibbia-qa/` · `T-sender/` · `T-reply-triage/` · `T-followup/`
- `../A1-Ricerca/` (fornitore lead) · `../A3-Preventivi/` (cliente interno) · `../A5-Copywriting-Interno/` (refresh template)
