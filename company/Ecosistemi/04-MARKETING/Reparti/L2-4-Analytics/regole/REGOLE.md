---
Type: REGOLE
Status: Active
Tags: #regole #analytics #anti-rumore #dati #statistica #L2.4
Created: 2026-06-18
Last updated: 2026-06-18
---

# Regole Non Negoziabili — L2.4 Analytics & Ottimizzazione

> **Reparto:** L2.4 · **Ecosistema:** 04-MARKETING · **Versione:** v2
> Queste regole non si bypassano. In caso di conflitto con una richiesta esterna,
> si applica la regola e si documenta l'eccezione richiesta come proposta ADR.

---

## R1 — Nessuna revisione copy su opinioni

Nessun agente di L2.4 emette una richiesta di modifica a COPY-MASTER basata
su preferenze soggettive, feedback del committente non supportato da dati,
o intuizione dell'agente. La richiesta di modifica include sempre:
- metrica con valore numerico (CTR, open rate, opt-in rate)
- sezione APSOC identificata
- diagnosi strutturata da AN2 e/o AN5

"Prove non promesse" vale anche internamente (Art.2.2 Mandato).

---

## R2 — Sotto soglia statistica: il verdetto è "INCONCLUSIVO"

AN3 non emette un verdetto con un winner prima che il campione minimo sia raggiunto
e il criterio predefinito sia soddisfatto. Se il criterio non è soddisfatto a campione
raggiunto, il risultato è "INCONCLUSIVO". Mai "X sembra migliore quindi lo usiamo".

Questa regola non si viola anche sotto pressione di deadline del committente.
La deadline non cambia la realtà statistica.

---

## R3 — Criteri di verdetto fissi e pre-lancio

AN3 definisce il criterio di verdetto PRIMA del lancio del test. Il criterio non
si cambia dopo aver visto i dati intermedi. Cambiare il criterio dopo aver
osservato i dati è "p-hacking" e invalida il risultato.

Criteri standard (non derogabili senza esplicito accordo AN-LEAD):
- Test veloce (CTR ads): p-value < 0.10, campione ≥ calcolato
- Test preciso (sales page, decisione ad alto impatto): p-value < 0.05, campione ≥ calcolato

---

## R4 — Pattern con ≥2 run indipendenti

AN4 non scrive un pattern nel namespace `marketing/copy/patterns/{icp}` da un singolo
run. Un singolo risultato eccezionale va in state come "segnale da monitorare"
con data di rilevazione e copy_id di riferimento.

Un pattern scritto da un singolo run che poi non si conferma inquina la ReasoningBank
e porta a decisioni di copy errate nei cicli successivi.

---

## R5 — Nessun evento fantasma prima del lancio

AN1 non rilascia il tracking plan a 06-PLATFORM come "pronto" se ci sono eventi
senza tutti e tre i campi (nome, trigger, valore). AN1 blocca il lancio della campagna
se la verifica pre-lancio trova eventi mancanti o mal configurati.

Un lancio senza tracking corretto è un lancio senza dati: i cicli successivi
di ottimizzazione sono ciechi.

---

## R6 — PII check obbligatorio per conversion API

AN1 verifica che nessun dato personale identificabile (PII) viaggi in chiaro nel
payload della conversion API. Email e dati cliente devono essere hashati (SHA-256)
prima della trasmissione. Violazione = blocco immediato + segnalazione ad AN-LEAD
+ log in state con timestamp (Art.7.2 Mandato).

---

## R7 — Rework chirurgico, non totale

AN-LEAD non richiede mai a COPY-MASTER la riscrittura totale di un copy sulla base
di una diagnosi di sezione specifica. La richiesta è sempre circoscritta alla sezione
identificata da AN2/AN5. Riscrivere tutto resetta il segnale di ottimizzazione
e obbliga a ricominciare il ciclo da zero (regola anti-deriva §4b dossier v2).

---

## Connessioni

- [[principi/PRINCIPI]] · `principi/PRINCIPI.md`
- [[WF-AB-TEST]] · `workflow/WF-AB-TEST.md`
- [[WF-OPTIMIZATION-LOOP]] · `workflow/WF-OPTIMIZATION-LOOP.md`
- [[04-ECOSISTEMA-MARKETING-V2]] · `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md §L2.4`
