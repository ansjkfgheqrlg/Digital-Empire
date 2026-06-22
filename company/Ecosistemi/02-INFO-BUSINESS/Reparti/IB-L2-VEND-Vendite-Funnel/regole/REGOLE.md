---
Type: REGOLE
Status: Active
Tags: #regole #non-negoziabili #vendite #funnel #evergreen #IB-L2-VEND
Created: 2026-06-21
Last updated: 2026-06-21
---

# Regole Non Negoziabili — IB-L2-VEND Vendite & Funnel

> Queste regole non hanno eccezioni. Se una situazione sembra richiedere di violarle,
> la risposta è escalation, non violazione.

---

## R1 — Nessun prezzo non approvato da team-prezzi (B-003) in produzione

I valori numerici dei prezzi NON si decidono in questo reparto. IB-VEND-OFFER progetta
l'offer stack (value stack, bonus, garanzia, order bump, upsell, naming) ma recepisce i numeri
dal catalogo approvato di B-003 (ADR-005) via handoff `HC-B003-IB-VEND-01`.

Nessun agente IB pubblica un prezzo — neanche "provvisorio" o placeholder — senza approvazione
B-003. Se il catalogo non è approvato a ridosso del go live, il go live slitta.

**Perché esiste questa regola:** vincolo B-002/B-003. Un prezzo sbagliato in produzione è un
danno diretto al revenue e alla percezione del brand; la responsabilità del pricing è di B-003.

---

## R2 — Questo reparto NON implementa le pagine

Le sales page, le opt-in page, i checkout e i paywall vengono costruiti e deployati da
06-PLATFORM via handoff `HC-PL-IB-01`. IB-VEND-SALESPAGE consegna copy approvato + offer stack;
IB-VEND-CHECKOUT coordina la config; PLATFORM implementa.

Nessun agente di IB-L2-VEND modifica HTML, CSS, layout, codice del checkout o config di deploy.
Questo vale anche per modifiche "piccole" post-lancio: ogni modifica strutturale passa da un
brief approvato e da PLATFORM.

**Perché esiste questa regola:** la responsabilità tecnica e la build premium (skill
`empire-premium-style`) sono di PLATFORM. IB che tocca il codice crea regressioni che nessuno presidia.

---

## R3 — IB-VEND-QA è bloccante su ogni output del reparto (gate G-VEND)

Nessuna sales page, nessuna email della sequenza nurture, nessuna opt-in page, nessun funnel
esce senza gate verde di IB-VEND-QA: APSOC ≥80/100 + "prove non promesse" verificato. Il gate
non ha deroga per urgenza.

Se il committente ha urgenza → IB-COORD-VENDITE può consegnare un parziale con nota di rischio
esplicita SOLO con approvazione di ib-director. Ogni bypass non autorizzato viene documentato
da IB-VEND-QA.

---

## R4 — L'evergreen NON usa scarcity artificiale (Mandato Art.2)

"Permanente" significa senza deadline finte. Nessun contatore farlocco, nessun "ultimi 3 posti"
non veri, nessuna scadenza che si resetta. Se esiste un bonus a scadenza, la scadenza deve essere
reale e applicata davvero.

IB-VEND-QA verifica e blocca ogni scarcity artificiale sull'evergreen. Violazione = FAIL automatico
senza analisi aggiuntiva.

**Perché esiste questa regola:** Mandato Art.2 (prove non promesse). La scarcity falsa è una bugia
al cliente; distrugge fiducia e posizionamento ("l'agenzia progettata per essere licenziata").

---

## R5 — Nessun test A/B "conclusivo" prima del campione minimo statistico

Un test non si dichiara concluso (adottato o scartato) finché non raggiunge il campione minimo
calcolato da IB-VEND-CRO. Una variante "winner" su campione insufficiente è peggio di nessun
verdetto: porta a rollout basati su rumore.

Inoltre: una sola variabile cambiata per test (R6 dei principi), rollout su % traffico, mai su
tutto prima della conclusione. Se il traffico non basta per raggiungere il campione in tempo
ragionevole, il test non si avvia.

---

## R6 — Nessun KPI dichiarato senza dato reale

I KPI del reparto hanno campo [DM] (Da Misurare) ovunque non esista baseline storica. Nessun
agente dichiara "opt-in rate atteso 30%" o "conversione evergreen attesa 2%" senza dato reale
da misurazione precedente. I [DM] si riempiono al primo run reale.

Committente che chiede previsioni di conversione pre-lancio → risposta corretta: "la baseline si
stabilisce al primo funnel live. Possiamo dichiarare la struttura e i punti critici, non i numeri."
(Mandato Art.2.)

---

## R7 — Nessun traffico verso un checkout rotto

Se IB-VEND-CHECKOUT o IB-VEND-TRACK rilevano che il pagamento non procede o un evento critico
(purchase) non scatta, la promozione si blocca immediatamente (P0). Nessun ad, nessuna email,
nessun link spinge traffico verso un checkout che non converte.

Il go live di una sales page richiede checkout testato con transazione reale (acceptance
`HC-PL-IB-01`) + tracking debug verde. Fix prima, traffico dopo.

---

## Connessioni

- [[PRINCIPI]] · `principi/PRINCIPI.md` — il "perché" di queste regole
- [[ib-vend-qa]] · `agenti/ib-vend-qa.md` — esecutore del gate G-VEND (R3, R4)
- [[ARCHITETTURA]] · `ARCHITETTURA.md` — confine B-003 / 06-PLATFORM in dettaglio (R1, R2)
- [[MANDATO-EMPIRE]] · `company/Mandato/MANDATO-EMPIRE.md` — Art.2 come fonte di R4 e R6
