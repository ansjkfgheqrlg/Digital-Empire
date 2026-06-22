---
Type: REGOLE
Status: Active
Tags: #regole #non-negoziabili #lanci #campagne #launch #IB-L2-LANC
Created: 2026-06-21
Last updated: 2026-06-21
---

# Regole Non Negoziabili — IB-L2-LANC Lanci & Campagne

> Queste regole non hanno eccezioni. Se una situazione sembra richiedere di violarle,
> la risposta è escalation, non violazione.

---

## R1 — Nessun lancio senza prodotto a gate PASS e budget approvato

Un lancio non si avvia se mancano i due prerequisiti duri:
1. Prodotto che ha superato il gate qualità prodotto (WF-CORSO o WF-EBOOK con verdetto PASS).
2. Budget approvato da 09-OPERATIONS (stima costi dry-run a T-1, gate Cost-Sentinel).

IB-COORD-LANCI verifica entrambi prima di far partire il calendario T-30. Mancando uno dei due,
il lancio è bloccato — non rinviabile a "lo sistemiamo strada facendo".

**Perché esiste questa regola:** lanciare un prodotto non validato o senza budget approvato
significa bruciare lista e reputazione su qualcosa che non regge. Lo status quo (non lanciare)
è meno costoso del danno.

---

## R2 — Questo reparto NON scrive copy né produce asset

Il copy di ogni email, sales page, ad del lancio viene prodotto da 04-MARKETING (HC-IB-MK-01).
Gli asset creativi (contenuti organici, video, grafiche) da 03-CONTENT-FACTORY (HC-IB-CF-01).

IB-L2-LANC produce brief lancio (offer, ICP, deadline, acceptance criteria, brand kit) e valida
i rientri. Nessun agente di IB-L2-LANC scrive headline, body copy, CTA o email, né realizza asset.

**Perché esiste questa regola:** la qualità del copy è presidiata dal gate APSOC ≥80 di
IB-LANC-QA sui rientri di 04-MARKETING. Se IB-L2-LANC scrivesse copy internamente, il gate
salterebbe e il sistema di qualità si romperebbe.

---

## R3 — Scarcity REALE o nessuna scarcity (Mandato Art.2)

Ogni deadline e ogni bonus a scadenza del lancio deve essere verificabile e rispettato: il
checkout chiude davvero all'ora dichiarata, il bonus a scadenza sparisce davvero.

Sono vietati: timer che si resettano, "ultimi posti" non reali, deadline posticipate dopo
l'annuncio, scarcity inventata per spingere la conversione.

IB-LANC-QA verifica la verificabilità di ogni elemento di scarcity nel gate copy/asset.
Scarcity non verificabile = FAIL automatico, senza analisi aggiuntiva.

---

## R4 — IB-LANC-QA è bloccante su tutti gli output del reparto

Nessun copy entra in produzione, nessun asset si pubblica, nessun dry-run abilita il go senza
gate verde di IB-LANC-QA (APSOC ≥80 / ≥85 sales page · asset-complete · dry-run OK). Il gate
non ha deroga per urgenza.

Se il committente ha urgenza → IB-COORD-LANCI può ripianificare il calendario SOLO con consensus,
mai bypassare il gate. IB-LANC-QA non suggerisce mai copy: ha potere di NO, non di scrittura.

---

## R5 — Dry-run obbligatorio a T-1 prima del go/no-go

Nessun lancio apre il cart senza dry-run completo a T-1: simulazione invii (sequenza email,
link, checkout) + stima costi. Il dry-run produce `dry-run.md` ed è input obbligatorio del
go/no-go.

Un go/no-go senza dry-run è un go cieco: vietato. Se il dry-run rileva un asset rotto (checkout
KO, link morto, email non caricata) → si torna allo step asset, non si forza il go.

---

## R6 — Delta budget dry-run >10% blocca il go/no-go

Se la stima costi del dry-run a T-1 scosta di oltre il 10% dal budget approvato da 09-OPERATIONS,
IB-LANC-DRY blocca il go. IB-COORD-LANCI rinegozia il budget con 09-OPERATIONS o ridefinisce lo
scope del lancio. Non si lancia "sperando" che i costi rientrino.

Il target di qualità è delta reale vs stima <10% anche a consuntivo (verificato nel debrief, P5).

---

## R7 — Go/no-go è consensus a 5 voci, UN solo NO blocca

Il go/no-go a T-0-ε è un hive-mind consensus di 5 voci: ib-director + IB-LANC-QA +
Quality-Sentinel + Brand-Voice-Sentinel + Cost-Sentinel. UN solo NO blocca il lancio — nessun
override, nessuna maggioranza che vince sul NO.

Il verbale `go-nogo.md` registra ogni voce e la motivazione. Un go senza verbale completo non è
un go valido. Questa regola protegge il reparto dalla pressione "lanciamo comunque".

---

## R8 — Nessun lancio è chiuso senza debrief scritto entro T+7

Il cart close non chiude il lancio: il debrief lo chiude. IB-LANC-DEBRIEF scrive `debrief.md`
entro T+7 con piano vs reale (ogni KPI), root cause di ogni scarto ≥10%, ≥3 pattern distillati
in `reasoningbank/`, zero numeri approssimati. Senza debrief, il lancio resta aperto nello state.

**Perché esiste questa regola:** un lancio senza debrief è fatturato senza conoscenza. Il
prossimo lancio ripete gli stessi errori. Il debrief è il meccanismo di apprendimento composto.

---

## Connessioni

- [[PRINCIPI]] · `principi/PRINCIPI.md` — il "perché" di queste regole
- [[IB-LANC-QA]] · `agenti/IB-LANC-QA.md` — esecutore dei gate R3/R4/R5
- [[ARCHITETTURA]] · `ARCHITETTURA.md` — confini IB-L2-LANC vs 04-MARKETING/03-CF in dettaglio
- [[MANDATO-EMPIRE]] · `company/Mandato/MANDATO-EMPIRE.md` (Art.2) come fonte di R3
