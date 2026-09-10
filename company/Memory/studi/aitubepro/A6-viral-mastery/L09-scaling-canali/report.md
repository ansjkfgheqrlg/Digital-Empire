# Report — A6/L09 «Scaling dei canali e dei video YouTube» (07:38)

- **Durata:** 07:38 · ~1.194 parole · **profondità ORO**
- **Letta:** parlato integrale + 6/22 frame unici (talking-head con dashboard reale, numeri presi dallo schermo per la garbugliatura del transcript automatico)
- **Materiale grezzo:** appunti.md nella stessa cartella · frame scelti: frame-scelti.md

---

## 1. Cosa insegna

Scaling per replica di contenuti già vincenti, con un caso reale misurato su due dashboard
Analytics (canale italiano: 2,8M views, +35.891 iscritti, 8.400,38 euro in 12 mesi; stesso canale
tradotto in spagnolo con ChatGPT, a costo di lavoro zero: 2,2M views, +35.021 iscritti, 3.083,10
euro in 4 mesi). Sette leve di scaling in ordine: virali sul canale originale, specializzazione di
nicchia, risposta a tutti i commenti, cross-promotion via Community, replica multi-canale nella
stessa lingua, replica multi-lingua (spagnolo, francese, portoghese fatti; inglese pianificato),
altre leve di monetizzazione oltre le ads (e-commerce, super grazie, chat, abbonamenti,
affiliazioni, non approfondite).

## 2. Cosa facciamo oggi nella fabbrica

Verificato con grep su apex7_orchestrator.py e fliki_client.py: CANALI (apex7_orchestrator.py:84)
è una mappa canale -> configurazione (voce, formato, temi, prefisso file) implicitamente
monolingua: nessun campo lingua, nessuna funzione che prenda uno script gia scritto e lo traduca
per generare un canale gemello in un'altra lingua. Ogni script viene scritto da zero per ogni
produzione (pipeline apex7 -> fliki), mai riusato traducendo un testo gia validato. Le altre due
leve gia coperte da questo giro di studio (rispondere ai commenti, Community/cross-promotion) sono
gia registrate come gap in A6-L08-01/02/03: qui il corso le cita di nuovo, come componenti dello
scaling, confermando trasversalmente la loro importanza.

## 3. Delta

Il delta piu specifico e piu misurabile di questo giro: la fabbrica non ha nessun meccanismo per
fare esattamente cio che il caso reale della lezione dimostra rendere piu redditizio (stessi
risultati, un terzo del tempo, zero lavoro aggiuntivo oltre la traduzione) - prendere uno script
che ha gia superato i gate di qualita (seo_score.py, regolatori.py) su un canale, tradurlo, e
produrne un secondo canale gemello in un'altra lingua. Oggi, per aprire un canale in una nuova
lingua, la fabbrica ripartirebbe dalla ricerca fonte e dalla scrittura scratch - lo stesso costo
di un canale nuovo, mentre il corso mostra che il costo reale dovrebbe essere solo l'API di
traduzione.

Delta secondario: nessuna funzione di "riesumazione" di uno script gia pubblicato per
ripubblicarlo modificato dopo 1-1,5 mesi sullo stesso canale (leva #1 della lezione) - la coda di
produzione (coda_produzione.json) non ha un concetto di "richiuso, candidato a rilancio futuro".

## 4. Conflitti

Nessuno. Gap di costruzione mancante, non scelta contraria - la fabbrica oggi produce solo canali
mono-canale mono-lingua scritti da zero, e non ha mai affrontato la replica multi-lingua come
categoria.

## 5. Regole estratte

Tre regole, tutte costruttive. Le due su commenti/community richiamano (non duplicano)
A6-L08-01/02/03 gia registrate: qui si limita a confermarle come leve di scaling, senza aprire
nuovi id. Dettaglio con prova in regole/A6-viral-mastery/L09_scaling_canali.py.

| id | tipo | regola in una riga | azione | tocca |
|---|---|---|---|---|
| A6-L09-01 | funzione | manca una funzione che traduca uno script gia approvato (passato i gate) per generare un canale gemello in un'altra lingua, invece di riscrivere da zero | costruisci | 02-AUTOMAZIONI-E-SCRIPTS/apex7_orchestrator.py |
| A6-L09-02 | parametro | CANALI dovrebbe portare un campo lingua esplicito, oggi assente, prerequisito tecnico per A6-L09-01 | costruisci | 02-AUTOMAZIONI-E-SCRIPTS/apex7_orchestrator.py (dict CANALI) |
| A6-L09-03 | flusso | manca un concetto di script "richiudibile" nella coda di produzione, per ripubblicare (con modifiche) un contenuto gia virale dopo 1-1,5 mesi sullo stesso canale | costruisci | memory/coda_produzione.json |

## 6. Applicabilità

Alta su A6-L09-01/02: e la leva con il caso reale piu forte di tutto questo giro di quattro
lezioni (numeri su schermo, non solo promessa a voce) e la fabbrica ha gia l'infrastruttura
multi-canale (CANALI) su cui innestarla - manca solo il campo lingua e la funzione di traduzione,
che è un lavoro contenuto (chiamata API di traduzione su un testo che già esiste, non generazione
nuova). Media su A6-L09-03, utile ma meno urgente vista la produzione attuale limitata (8 video
totali, BASELINE.md §4) - riguarda una fase di ottimizzazione che arriva dopo aver risolto Ultimo
Metro (L06), non prima.
