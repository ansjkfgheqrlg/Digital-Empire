---
Type: CONCEPT
Status: Active
Tags: #regole #account-management #customer-success #gate #bloccante #A7
Created: 2026-07-11
Last updated: 2026-07-11
---

# REGOLE — A7 Account Management & Customer Success

> **Tutte le regole di questo documento sono BLOCCANTI.** Non sono linee guida, non sono
> raccomandazioni. Una violazione non è un warning: è un FAIL di gate. AG-A7-QA è l'agente che le
> applica; il bypass non esiste (R8).

---

## R1 — Nessun cliente senza KAM

**Regola:** ogni record in `agency/a7/clients/{client_id}` DEVE avere il campo `kam` popolato.
Un cliente senza KAM è un'anomalia bloccante.

- **Chi la applica:** AG-A7-QA (verifica a ogni gate) · AG-A7-HEALTH (rilevazione in monitoraggio)
- **Chi la subisce:** AG-A7-COORD
- **Se violata:** ogni altra azione sul cliente si **ferma**. AG-A7-COORD assegna il KAM prima di
  qualsiasi task. Il cliente non passa di fase, non riceve comunicazioni, non entra nei KPI.
- **Perché:** P1. Un cliente orfano è il gap che il v1 aveva e che A7 esiste per colmare.

---

## R2 — Alert churn entro 24h, azione registrata

**Regola:** ogni segnale di rischio rilevato da AG-A7-HEALTH DEVE generare un alert entro 24h, e
l'azione correttiva scelta da AG-A7-COORD DEVE essere **registrata** in `agency/a7/alerts/{alert_id}`
entro 24h dall'alert.

- **Chi la applica:** AG-A7-QA (gate alert) · AG-A7-HEALTH (escalation automatica a scadenza)
- **Chi la subisce:** AG-A7-COORD
- **Se violata:** l'alert **resta aperto** ed escala automaticamente ad **AG-DIR**. Non si chiude
  per decorrenza dei termini. Il cliente resta contrassegnato a rischio.
- **Perché:** P3. Un rischio osservato ma non registrato non è stato intercettato.

---

## R3 — Un touchpoint non loggato non è avvenuto

**Regola:** ogni touchpoint (kickoff, mid-review, check call, richiesta NPS, chiusura) DEVE essere
loggato in `agency/a7/touchpoints/{client_id}` con data, tipo ed esito.

- **Chi la applica:** AG-A7-QA (gate di fase)
- **Chi la subisce:** AG-A7-ONBOARD · AG-A7-MID · AG-A7-CLOSE · AG-A7-COMM
- **Se violata:** il gate di fase **FAIL**. La fase non si chiude finché il log non esiste.
- **Perché:** senza log non c'è ripartibilità a freddo (test amnesia, ARCHITETTURA §6). Un KAM che
  rientra dopo un'amnesia di sessione deve ricostruire la relazione **dallo state**, non dai ricordi.

---

## R4 — Nessuna promessa non coperta

**Regola:** nessun agente di A7 comunica al cliente date non confermate da A4-Delivery, risultati
non misurati, o impegni non presenti nel contratto chiuso da A3-Preventivi.

- **Chi la applica:** AG-A7-QA (gate sui draft di AG-A7-COMM)
- **Chi la subisce:** tutti gli agenti del reparto, AG-A7-COMM in particolare
- **Se violata:** il draft è **non inviabile**. Se la promessa è già uscita → escalation immediata
  ad AG-DIR e a Max: il danno è contrattuale, non relazionale.
- **Perché:** P4. Ogni fatto comunicato deve avere una fonte tracciabile nello state.

---

## R5 — Nessuna closure senza NPS

**Regola:** la closure a G+90 NON si chiude se `nps` è `[DM]`. Il valore si **raccoglie**: non si
stima, non si deduce dal clima, non si media dai cicli precedenti.

- **Chi la applica:** AG-A7-QA (gate closure — il più stringente del reparto)
- **Chi la subisce:** AG-A7-CLOSE · AG-A7-COORD
- **Se violata:** closure **bloccata**. Dopo 2 follow-up senza risposta, l'esito è
  `chiuso_con_riserva` con `nps: [DM]` e causale registrata + escalation AG-DIR. **Non è un PASS
  mascherato: è un FAIL documentato.** Gli handoff di upsell/referral **non partono**.
- **Perché:** P5. Un NPS inventato propaga il falso a due reparti a valle (A3 e A6).

---

## R6 — Nessuna leva commerciale autonoma

**Regola:** sconti, rimborsi, estensioni gratuite, lavoro extra fuori contratto — **nessun agente
di A7 li concede**. La decisione è di **Max**, sempre.

- **Chi la applica:** AG-A7-QA (gate draft e gate di fase)
- **Chi la subisce:** AG-A7-COORD · AG-A7-MID · AG-A7-CLOSE · AG-A7-COMM
- **Se violata:** FAIL bloccante + escalation ad AG-DIR e Max. La concessione non è ratificabile
  a posteriori dal reparto.
- **Perché:** un agente sotto pressione relazionale tenderà sempre a "salvare il rapporto" regalando
  margine. È esattamente il comportamento che distrugge l'economia dell'agenzia un cliente alla volta.

---

## R7 — Nessun PII nello state

**Regola:** `agency/a7/*` contiene **solo** nome e ruolo del contatto. Email, telefono, indirizzi,
dati di pagamento e qualsiasi altro recapito vivono nel **CRM**, mai nello state e mai nei draft
archiviati.

- **Chi la applica:** AG-A7-QA (gate su ogni scrittura di state) · tutti gli agenti in autocontrollo
- **Chi la subisce:** AG-A7-COMM (principale rischio: incorpora recapiti nei draft) · AG-A7-COORD
- **Se violata:** la scrittura viene **rifiutata**; il dato PII già scritto viene rimosso e l'evento
  registrato. Nessun segreto (API key, credenziale, token) entra mai nello state.
- **Perché:** lo state è versionato e sincronizzato tra sedi. Un PII nello state è un PII in git.

---

## R8 — Il gate non si bypassa

**Regola:** nessun agente di A7 può aggirare, posticipare o "chiudere con riserva" un gate di
AG-A7-QA per rispettare una scadenza. Un FAIL si **risolve**, non si aggira. Il referral e il case
study richiedono `consenso_case_study: confermato`: senza consenso esplicito del cliente, nessuna
pubblicazione.

- **Chi la applica:** AG-A7-QA · AG-DIR in ultima istanza
- **Chi la subisce:** tutti gli agenti del reparto, incluso AG-A7-COORD
- **Se violata:** escalation immediata ad **AG-DIR**. Un gate bypassato è un incidente di processo,
  non un errore di merito: va in `company/Memory/` come errore da non ripetere.
- **Perché:** un gate che si può bypassare sotto pressione non è un gate — è un suggerimento. E un
  case study pubblicato senza consenso è un danno legale e reputazionale, non un'ottimizzazione.

---

## Sintesi applicativa

| Regola | Applica | Gate | Effetto della violazione |
|---|---|---|---|
| R1 KAM obbligatorio | AG-A7-QA | tutti | Blocco totale sul cliente |
| R2 Alert entro 24h | AG-A7-QA · AG-A7-HEALTH | alert churn | Alert aperto + AG-DIR |
| R3 Touchpoint loggato | AG-A7-QA | fase | Fase non chiudibile |
| R4 Nessuna promessa scoperta | AG-A7-QA | draft | Draft non inviabile |
| R5 Nessuna closure senza NPS | AG-A7-QA | closure 90gg | Closure bloccata, handoff fermi |
| R6 Nessuna leva commerciale | AG-A7-QA | draft · fase | FAIL + AG-DIR + Max |
| R7 Nessun PII nello state | AG-A7-QA | scrittura state | Scrittura rifiutata |
| R8 Gate non bypassabile | AG-A7-QA · AG-DIR | tutti | Incidente di processo → Memory |

---

## Connessioni

- [[PRINCIPI]] · `principi/PRINCIPI.md` — il razionale dietro ogni regola
- [[ag-a7-qa]] · `agenti/ag-a7-qa.md` — l'agente che applica tutte le R
- [[WF-RETENTION-ALERT]] · `workflow/WF-RETENTION-ALERT.md` — dove R2 è operativa
- [[WF-CUSTOMER-LIFECYCLE]] · `workflow/WF-CUSTOMER-LIFECYCLE.md` — dove R1, R3, R5 sono operative
