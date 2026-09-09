---
Type: SYNTHESIS
Status: Active
Tags: #competitor #andrei-pascu #lanci #funnel #offerta #documentazione-ufficiale
Created: 2026-09-09
Last updated: 2026-09-09
---

# ANATOMIA DEI LANCI — come lancia Andrei Pascu, smontato pezzo per pezzo

**Documento ufficiale.** Forma originale: questo file Markdown. Forma eseguibile:
`anatomia_lanci.py`. Forma da consegnare: il PDF in `documentazione Empire/Lanci/`.
Destinatario: **la sessione che costruisce l'ecosistema LANCI** (ADR-025) — vedi
`company/Memory/tasks/TASK-LANCI-20260908-ANATOMIA-ANDREI-PASCU.md`.

**Su cosa si fonda.** 52 pagine catturate su 7 domini fra il 7 e il 9 settembre 2026, oltre
100.000 parole di rapporti, **un lancio vivo colto mentre girava**. Ogni numero qui dentro è
misurato sul disco. Dove c'è un'inferenza, è scritto che è un'inferenza.

---

## PARTE I — IL FATTO

Abbiamo catturato **un lancio in corso**, non il ricordo di un lancio: `armageddon.bsns.it`,
pagina madre più quattro pagine figlie, con il pagamento attivo.

| Misura | Valore |
|---|---|
| Prodotti nel pacchetto | 4 (outEmail, outFunnel, outHeadline, outViral) |
| Listino sommato | **585 €** |
| Voucher aggiunto | **199 €** |
| Valore dichiarato | **784 €** |
| Prezzo di vendita | **199 €** |
| Sconto dichiarato | «Risparmi €585» |
| Link di pagamento | **uno solo**, Stripe, identico su tutte e cinque le pagine |
| Costruzione | artigianale, vanilla, zero piattaforma |

**Il primo insegnamento è già qui: il pacchetto costa quanto il voucher.** Il cliente paga 199 € e
riceve un buono da 199 € più quattro prodotti. L'ancora non è un numero inventato: è la somma dei
listini che esistono davvero sul negozio, verificabile da chiunque in trenta secondi.

---

## PARTE II — COME COSTRUISCE UN LANCIO: sei mosse

### Mossa 1 — Non scrive pagine nuove. Specchia quelle che ha.

Le quattro pagine figlie **non sono state scritte per il lancio**: sono le pagine prodotto del
negozio, copiate e ripulite. Il commento dentro `mirror.js` lo dichiara, identico su tutte e
quattro (stesso MD5):

> *«The pages are the originals from andrei-copy.com with every Squarespace script removed.»*

**Costo del lancio in ore di scrittura: quasi zero.** È la ragione per cui può lanciare spesso.

### Mossa 2 — Spoglia la piattaforma

Dal mirror sparisce ogni script di Squarespace. Restano HTML e CSS. Nessun carrello, nessuna
sessione, nessun tracciamento della piattaforma: **una pagina statica che non può rompersi**.

### Mossa 3 — Ripunta tutto a una cassa sola

Tutte e cinque le pagine portano allo **stesso identico link Stripe**. Non c'è un carrello, non c'è
una scelta: c'è un pulsante e una destinazione.

### Mossa 4 — Sostituisce il prezzo con l'appartenenza

Dove la pagina originale mostrava il bottone-prezzo del prodotto singolo, il mirror mette un badge:

> **«INCLUSO NEL PACCHETTO ARMAGEDDON»** — `#bc0807`, maiuscolo, 15,2 px, peso 700

Quel colore **non compare da nessun'altra parte nella pagina tranne che sulla barra d'acquisto**: è
un filo rosso deliberato fra «questo è incluso» e «compra qui». Il prodotto singolo smette di essere
comprabile: esiste solo dentro il pacchetto.

### Mossa 5 — Mantiene il mirror, non lo congela

Prova diretta: l'originale sul negozio dice *«E adesso, nel **2025**…»*; la copia di lancio,
catturata **lo stesso giorno**, dice *«nel **2026**»*. Qualcuno ha aperto l'editor e ha aggiornato
**solo la copia**.

**Conseguenza per noi:** un mirror di lancio è un artefatto vivo, e va messo in manutenzione come
tale. Se non lo si fa, invecchia **il negozio**, che è quello che vende tutto l'anno.

### Mossa 6 — Tiene l'offerta su una pagina sola

La pagina madre è **corta**: 5.103 px, 4 sezioni, 53 blocchi di testo, 7 CTA. Confronto: le sue
pagine di vendita normali stanno fra 10.000 e 27.000 px. **Un lancio non si spiega, si annuncia** —
la spiegazione è già nelle quattro pagine figlie.

---

## PARTE III — IL FUNNEL INTERO, GRADINO PER GRADINO

Il funnel non è un imbuto disegnato: sono pagine vere, con URL, che abbiamo aperto una per una.

### Il percorso freddo — dall'ignaro al prodotto

```
/define                    →   /asa                    →   /copy-base
«Cos'è il copywriting?»        «Come si monetizza»          la pagina prodotto
1.802 px · 1 sezione           1.936 px · 1 sezione
1 video · 1 bottone            1 video · 1 bottone
zero prezzo, zero prova        zero prezzo, zero prova
```

**Due domande in fila**: prima *cos'è* il mestiere, poi *come ci si guadagna*. Il prodotto compare
al terzo passo. Ogni pagina-ponte ha **una sola decisione possibile**.

E porta dentro la riga che vale il viaggio — `/asa`, un `h3` da 38,4 px, il secondo testo più grande
della pagina:

> **«Ti consiglio di vedere e finire il video prima di cliccare il pulsante per capirne i contenuti.»**

Non è cortesia: è **controllo del consumo**. Chi arriva al bottone ha già visto il video, quindi
clicca sapendo cosa compra. Meno rimborsi, meno assistenza, click di qualità più alta.

### Il percorso caldo — dalla pagina di vendita alla cassa

Fra la pagina che convince e il pagamento c'è **sempre un gradino**. Ne abbiamo catturati **nove**,
ed è **un unico stampo**: cornice identica al pixel, cambia solo il riquadro centrale.

**Lo stampo della pre-cassa — sei elementi, in quest'ordine:**

| # | Elemento | Esempio misurato |
|---|---|---|
| 1 | occhiello in corsivo | *«Stai acquistando…»* |
| 2 | nome del prodotto, grande | «out**Funnel**», 68,3 px |
| 3 | istruzione + **codice sconto** | «Ricorda di usare il codice sconto "CWSHOP" per avere il 20% di sconto.» |
| 4 | la cifra, isolata | «98,00 €», 35,2 px |
| 5 | la condizione, attaccata | «Una tantum» |
| 6 | il bottone | «Acquista outFunnel» |

**Sei variabili in tutto**: nome, prezzo, colore, porzione colorata del nome, codice sconto
(opzionale), testo del bottone. Tutto il resto è fisso. **È un generatore, non una pagina.**

### Le tre decisioni dentro lo stampo

1. **Lo sconto sta dopo la decisione.** «CWSHOP» compare **solo** nella pre-cassa: 98 € diventano
   78,40 € mentre il cliente inserisce i dati, non mentre valuta. Uno sconto messo prima abbassa il
   prezzo percepito nel momento in cui il lettore sta ancora scegliendo.
2. **«Stai acquistando…» in corsivo, prima del nome.** Riafferma l'atto invece di ricominciare a
   vendere. È l'anti-ripensamento più economico che esista: due parole e tre puntini.
3. **«Una tantum» attaccato alla cifra.** Uccide il sospetto dell'abbonamento nel punto esatto in
   cui nasce, senza una riga di spiegazione.

### Il costo del percorso, in parole

**86 parole** di contenuto vero portano dall'apertura di `/define` al clic d'acquisto. Una singola
pagina di vendita ne usa **1.140-1.560**. Il funnel è **tredici-diciotto volte più economico** in
parole della pagina che convince.

### E i gradini che non sono casse

`/presto-disponibile`, `/ricevi-email-di-andrei-pascu`, `/aps-assistenza`: pagine di parcheggio.
Notevole: il link «Recensioni» nel piede di **tutte e quattro** le pagine-ponte punta a
`/presto-disponibile`. **La prova sociale non manca per scelta: manca perché la pagina non esiste
ancora**, e il link è stato lasciato lì.

---

## PARTE IV — COME COSTRUISCE L'OFFERTA

| Leva | Come la usa | Misura |
|---|---|---|
| **Ancora** | somma dei listini reali, verificabile | 585 € |
| **Regalo che vale quanto il prezzo** | voucher | 199 € su 199 € pagati |
| **Sconto dichiarato** | in grande, sopra tutto | «Risparmi €585» a **81,6 px** |
| **Prezzo pagato** | in piccolo | **14,88 px** |
| **Scarsità** | solo tempo, nessun limite di posti | dichiarata e verificabile |
| **Bundle contro singolo** | il singolo sparisce dietro il badge | `#bc0807` |

**Il rapporto 81,6 : 14,88 è la scelta tipografica più aggressiva di tutto l'ecosistema.** La cifra
che eccita è **5,5 volte** quella che addebita, ed è più piccola perfino del corpo delle FAQ
(16,5 px). Funziona, ed è esattamente ciò che **noi non faremo**: è diventato il controllo 7 del
nostro gate.

### La scala dei prezzi, e cosa cambia salendo

| Prodotto | Prezzo | Fonti esterne citate | Prova sociale vera |
|---|---|---|---|
| outHeadline | 98 € | 0 | no |
| Vendita101 | 400 € | 2 | sì |
| Copy Mentorship | 999 € | 5 | sì, doppio registro |

**Il prezzo che sale non porta più obiezioni gestite: porta più fonti.** E la prova sociale vera
compare **solo sopra i 349 €**. Citazione dal teardown della mentorship:

> *«Più sale il prezzo, meno regge l'argomento "non ho testimonianze ma ho i dati". A 98 € puoi
> permetterti di posare; a 999 € ti servono facce.»*

---

## PARTE V — COSA HANNO IN COMUNE I SUOI LANCI

Il modello ripetibile, distillato in **otto costanti**:

1. **Un lancio è un pacchetto di cose che esistono già.** Nessun prodotto nuovo.
2. **Le pagine si specchiano, non si scrivono.**
3. **Una sola cassa, un solo link.**
4. **Il singolo sparisce dietro il badge di inclusione.**
5. **L'ancora è verificabile**, perché è la somma di listini pubblici.
6. **Il regalo vale quanto il prezzo** — il voucher pareggia la cifra pagata.
7. **La scarsità è di tempo, mai di posti.** Un limite di posti su un prodotto digitale è una bugia
   che il cliente può smontare; una finestra temporale no.
8. **La pagina madre annuncia, le figlie spiegano.** 5.103 px contro 26.000.

---

## PARTE VI — COME RAGIONA: quattro principi che non ha mai scritto

Ricavati dal comportamento, non da dichiarazioni. Sono inferenze, e come tali vanno lette — ma ognuna
poggia su una misura.

1. **La piattaforma si sceglie dalla vita del pezzo.** Negozio permanente → Squarespace (44 pagine).
   Lancio con una finestra → a mano (7 pagine). Agenzia B2B → a mano con kit condiviso.
2. **Non personalizza dove non conta.** Il `custom.css` del negozio pesa **1.183 byte su 3,6-8,2 MB**
   scaricati — lo 0,02% — e di sei regole **solo due sono vive**. Il valore delle sue 44 pagine di
   negozio non è nel codice: è nel copy e nella sequenza.
3. **Tutto ciò che si ripete diventa uno stampo.** La pre-cassa è un generatore a sei variabili; i
   blocchi di copy attraversano prodotti diversi identici carattere per carattere (*«La speranza non
   è una strategia.»*, *«Lavori da solo? Vale lo stesso. Al posto del team, il vincolo sei tu.»*).
4. **Lucida dove si convince, lascia i difetti dove si transita.** È la regola che spiega tutti i
   suoi difetti in una riga sola.

---

## PARTE VII — COSA NON FA MAI

- **Non chiede i soldi nella pagina che fa desiderare.** Il prezzo definitivo vive nella pre-cassa.
- **Non mette lo sconto prima della decisione.**
- **Non usa limiti di posti** su prodotti digitali.
- **Non spiega il pacchetto nella pagina madre.**
- **Non dichiara un carattere tipografico** sul negozio (38 pagine su 52 a `sans-serif`).
- **Non nomina mai l'obiezione più ovvia del suo corso su Claude** («lo imparo gratis dalla
  documentazione»): non compare né nel copy né nelle FAQ.

---

## PARTE VIII — I DIFETTI, CHE PER NOI VALGONO QUANTO I PREGI

Sette difetti misurati addosso a lui. **Sei sono diventati controlli automatici del nostro gate**
(ADR-024, controlli 3-8).

| # | Difetto | Misura | Nostro controllo |
|---|---|---|---|
| 1 | **La cassa non risolve** | `/vendita` manda a `/acquista-v101`: **404**. La cassa vera (`/vendita101-pre`, 400 €) **non è linkata da nessuna parte** | **Controllo 8 — primo gate obbligatorio di LANCI** |
| 2 | Il prezzo è un'immagine con `alt` vuoto | outEmail 139 €, outFunnel 98 €, outHeadline | Controllo 6 |
| 3 | La cifra pagata è il testo più piccolo | 14,88 px contro FAQ a 16,5 | Controllo 7 |
| 4 | Anni scritti a mano | «nel 2025» sul negozio vivo | Controllo 5 |
| 5 | `og:image` placeholder identico su 3 pagine | targato `lovable.app` | Controllo 3 |
| 6 | Un campo del calcolatore non entra nel calcolo | `apsales.eu/landing-page` | Controllo 4 |
| 7 | Il codice sconto è pubblico e permanente | «CWSHOP» su pagina indicizzabile: il listino vero è 78,40 €, e 98,00 € è decorazione | il nostro pattern `pre-cassa` nasce con codice a scadenza e `noindex` |

**Il difetto 1 vale da solo tutto lo studio.** Un lancio con la pagina di vendita viva e la cassa
irraggiungibile **perde ogni euro che il copy ha guadagnato**, e nessuno se ne accorge, perché la
pagina di vendita funziona benissimo.

---

## PARTE IX — IL MODELLO PER DIGITAL EMPIRE

Non «facciamo come lui»: **facciamo il suo modello senza i suoi difetti.** Dodici passi, in ordine.

| # | Passo | Regola nostra |
|---|---|---|
| 1 | Scegli i pezzi che esistono già | mai costruire prodotto nuovo per un lancio |
| 2 | Somma i listini **pubblici** | l'ancora dev'essere verificabile da un estraneo |
| 3 | Aggiungi un regalo che valga quanto il prezzo | il voucher pareggia la cifra |
| 4 | Fissa una finestra di **tempo** | mai limiti di posti su prodotti digitali |
| 5 | Specchia le pagine prodotto | pattern `mirror-di-lancio` |
| 6 | Sostituisci i bottoni-prezzo col badge di inclusione | un accento, due punti, zero dispersione |
| 7 | Punta tutto a **una** cassa | un solo link di pagamento |
| 8 | Costruisci la pagina madre corta | annuncia, non spiegare |
| 9 | Metti il gradino di pre-cassa | pattern `pre-cassa`, sei elementi in ordine |
| 10 | Codice sconto **a scadenza**, nella pre-cassa, con `noindex` | mai pubblico e permanente |
| 11 | **Prezzo pagabile ≥ corpo del testo di servizio**, e mai dentro un'immagine | controlli 6 e 7 |
| 12 | **Percorri la catena a macchina prima di aprire** | controllo 8: ogni CTA risolve 200, ogni cassa ha almeno un link che ci arriva |

**Il passo 12 non è l'ultimo per caso: è il solo che, se salta, annulla gli altri undici.**

---

## PARTE X — COSA CONSEGNIAMO A LANCI

1. **Questo documento**, nelle tre forme.
2. **Lo stampo di pre-cassa già costruito**: `.claude/skills/fabbrica-siti/pattern/pre-cassa/`
   (HTML vanilla, zero JavaScript, codice a scadenza, `noindex`).
3. **Il pattern `pagina-ponte`**: `.claude/skills/fabbrica-siti/pattern/pagina-ponte/`.
4. **Otto controlli di gate**, di cui il numero 8 è il primo gate obbligatorio di LANCI.
5. **Un funnel nostro già scritto e mai lanciato**: `chiamata-formazione.netlify.app` — call 1:1
   gratuita verso «Claude Code Mastery» a 397 €, 18.770 px, 25 sezioni, 506 blocchi, ferma su uno
   staging. **Era censita per errore fra le pagine del concorrente.**

---

## Connessioni
- [[SINTESI-METODO]] · [[SINTESI-SISTEMA-VISIVO]] · [[SINTESI-SISTEMA-COPY]] — le tre sintesi
- [[ECOSISTEMA]] — l'elenco vero e le correzioni
- `company/Memory/tasks/TASK-LANCI-20260908-ANATOMIA-ANDREI-PASCU.md` — la consegna
- `company/Memory/decisions/ADR-025-ecosistema-lanci.md` · `ADR-024-canone-v2-primo-strato.md`
- `PIANO-MAESTRO/29-ECOSISTEMA-LANCI/` — il piano che riceve
