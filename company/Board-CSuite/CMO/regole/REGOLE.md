---
Type: CONCEPT
Status: Active
Tags: #cmo #regole #operativo #gate #mandato #marketing
Created: 2026-06-17
Last updated: 2026-06-17
---

# REGOLE — CMO (Chief Marketing Officer)

> Regole operative del team CMO. Derivano dai PRINCIPI e dal Mandato (LX). Dove un
> principio dice "perché", una regola dice "come" e "quando". Violazioni di regola → log
> al conductor. Violazioni di principio → escalation.

---

## Regola 1 — Ogni brief richiede brand_kit + icp (obbligatorio)

Nessun brief viene accettato e trasmesso a 04-MARKETING o 03-CONTENT-FACTORY senza:
- `brand_kit` dichiarato (DE o cliente-X con kit caricato)
- `icp` dichiarato con awareness level

I liaison verificano questa regola prima di fare qualsiasi handoff. Brief incompleti vengono
rimandati al conductor, non gestiti in autonomia con valori inventati.

---

## Regola 2 — Score APSOC registrato per ogni output

Ogni output di conversione che esce dal gate `cmo-brand-voice-warden` deve avere uno
`score_apsoc` registrato in `board/cmo/brand-gate-log/`. Non si pubblica output senza log.
Un output senza score non è "approvato": è non verificato, e viene trattato come FAIL.

---

## Regola 3 — Sales page e proposte: soglia ≥85

La soglia APSOC per sales page e proposte commerciali è **85/100**, non 80.
Ogni agente del team conosce questa differenza. Se un output è classificato erroneamente
come "standard" quando è in realtà una sales page → il gate si applica a soglia ≥85.
In caso di dubbio sulla classificazione: soglia più alta.

---

## Regola 4 — Dry-run prima di ogni spesa variabile

Prima di attivare qualsiasi canale con budget variabile (ads Meta/Google, crediti email
tool, API):
1. Stima costi prodotta da `cmo-campaign-strategist`
2. Presentata al conductor
3. Ok umano esplicito ricevuto e loggato

Ordine obbligatorio, non invertibile. Nessuna spesa senza ok.

---

## Regola 5 — Lancio info-business: prezzo approvato prima del via

Un prodotto info-business non si lancia senza prezzo approvato da team prezzi + Max
(Mandato Art.3.3). Se il brief di lancio arriva senza prezzo approvato: il workflow
WF-LANCIO-COORD non parte. Il launch-coordinator comunica al conductor il blocco con
motivazione esplicita ("attesa approvazione prezzo da team prezzi").

---

## Regola 6 — Monitoraggio 72h obbligatorio per ogni lancio

Ogni lancio (campagna o info-business) ha un piano di monitoraggio delle prime 72 ore.
- Check ore 4: anomalie tecniche (0 conversioni con traffico → problema tecnico)
- Check ore 24: metriche iniziali vs target
- Check ore 48: aggiustamenti se necessario
- Check ore 72: report completo al conductor

Il monitoraggio non è opzionale: è parte del workflow, non un'opzione post-lancio.

---

## Regola 7 — Feedback APSOC = specifico, non generico

Quando `cmo-brand-voice-warden` emette un FAIL, il feedback che arriva a 04-MARKETING o
03-CONTENT-FACTORY deve specificare:
- Quale sezione ha il problema (A, P, S, O, C)
- Quale claim specifico non ha proof (se CPB violato)
- Quale fix è richiesto (non "migliora il copy": "aggiungi dato numerico in sezione P")

Un FAIL con feedback generico viene rigettato dal conductor: il feedback deve essere
abbastanza preciso da produrre un fix senza ulteriori chiarimenti.

---

## Regola 8 — Pattern vincenti → cmo-memoria entro 24h dal PASS

Ogni output PASS con score ≥83 e metriche di campagna positive viene segnalato a
`cmo-memoria` entro 24h dal PASS o dall'arrivo delle metriche di conferma. Non aspettare
fine campagna: i pattern si codificano mentre i dati sono freschi.

---

## Regola 9 — ICP aggiornato ogni 90 giorni o al cambio di segnale

Il profilo ICP non è statico. `cmo-audience-intel` verifica ogni 90 giorni se il profilo
attivo è ancora allineato con i segnali di mercato. Se arriva un segnale di drift prima dei
90 giorni (es. 3+ discovery call con pain point diverso dall'ICP attivo) → aggiornamento
immediato + alert al conductor per le campagne in corso.

---

## Regola 10 — Nessun lancio senza allineamento CMO ↔ CRO

Per ogni lancio (WF-LANCIO-COORD), il `cmo-launch-coordinator` deve avere conferma scritta
(output JSON) dell'allineamento con il CRO su:
- Offerta (cosa si vende esattamente)
- Pricing (importo, modalità, nessun canone implicito)
- CTA della sales page (unica, chiara, bassa frizione)

Il lancio non procede al STEP 8 (live) senza questa conferma nel file `allineamento-cro.json`.

---

## Connessioni

- [[principi/PRINCIPI.md]] — i principi da cui derivano queste regole
- [[WF-BRAND-GATE]] · `workflow/WF-BRAND-GATE.md`
- [[WF-CAMPAGNA]] · `workflow/WF-CAMPAGNA.md`
- [[WF-LANCIO-COORD]] · `workflow/WF-LANCIO-COORD.md`
- [[cmo-brand-voice-warden]] · `agenti/cmo-brand-voice-warden.md`
- [[MANDATO-EMPIRE]] Art.2 + Art.3.3 + Art.4 + Art.6
