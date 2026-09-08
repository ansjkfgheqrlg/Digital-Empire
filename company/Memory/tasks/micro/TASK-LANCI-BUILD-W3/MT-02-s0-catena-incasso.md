# MT-02 — S0: cassa, pagamento vero, consegna, rimborso, misura (gesti 1-6)

- **Padre:** TASK-LANCI-BUILD-W3
- **Onda:** 1
- **Stato:** APERTA
- **Data:** 2026-09-08
- **Dipende da:** —
- **Scope (percorsi che tocca — controllo di sovrapposizione):**
  - company/Ecosistemi/15-LANCI/

## Cosa fa

Gesti 1-6 di S0 (`04-COSTRUZIONE.md` §3), **senza scrivere codice**: rendere l'azienda capace
di ricevere un euro vero e restituirlo.

1. Collegare una cassa a una pagina qualunque (esiste un indirizzo dove si può pagare).
2. Pagare davvero, con una carta vera.
3. Farsi arrivare il prodotto senza intervento umano.
4. Rimborsare quel pagamento.
5. Installare la misura e vedere l'evento d'acquisto comparire nello strumento.
6. Annotare le commissioni lette sulla transazione (`02-PREVISIONE-E-DENARO.md` §8, riga 5).

**Se non si chiude in 16 ore-uomo, si ferma tutto** (condizione di abbandono 1, `04-COSTRUZIONE.md` §6).

## Gate di chiusura

Aprire il pannello del fornitore di pagamento e vedere, **sulla stessa transazione**: un
incasso, una consegna, un rimborso. Nello strumento di misura, l'evento corrispondente.

## Output

Transazione di prova con incasso+consegna+rimborso, evento leggibile in un pannello.
