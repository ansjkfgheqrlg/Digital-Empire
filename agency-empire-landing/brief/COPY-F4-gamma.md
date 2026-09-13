# COPY-F4-gamma — «La storia dei preventivi» (BLOCCO D, dossier 40)

Scagnozzo γ. Sezione nuova `StoriaPreventivi`, montata prima di `<PrimaDopo />`. Nome del cliente **mai** scritto:
resta «un'azienda che importa auto dalla Germania». Numeri solo da `FATTI.novacar` (65 preventivi, 11 marche, 2 minuti a
PDF) — il resto è parole («ore», «pochi minuti», «decine», «pochi secondi»), mai cifre inventate.

## D1

**[apertura]** Ok, sto andando troppo veloce. Adesso ti faccio un esempio concreto…

**[storia-1]** Un cliente nostro importa auto dalla Germania. Ogni mattina apriva il portale tedesco e ripartiva da zero.

**[storia-2]** Apriva un annuncio. Copiava i dati. Calcolava il prezzo a mano. Impaginava il PDF. Poi il prossimo annuncio. E il prossimo.

**[storia-3]** Decine di preventivi al giorno. Ore della sua giornata, ogni giorno — bruciate su un lavoro che una macchina fa meglio di lui.

**[storia-4]** Allora abbiamo costruito una piccola applicazione privata, solo per loro.

**[storia-5]** Incolli il link dell'annuncio. Esce il PDF: il loro logo, le caratteristiche che ci hanno chiesto, il prezzo già calcolato. In pochi secondi.

**[storia-prova]** In dieci giorni abbiamo prodotto 65 preventivi su 11 marche diverse — circa 2 minuti a PDF, controlli compresi.

**[schema — 4 blocchi con frecce ferme, stile funnel-hero]**
1. Annuncio sul portale — riga mono: «il portale tedesco, ogni mattina»
2. Incolli il link — riga mono: «un click, non un modulo»
3. L'app legge tutto e calcola — riga mono: «dati e prezzo, in automatico»
4. PDF col loro logo, in secondi — riga mono: «pronto da mandare»

**[chat — bolle HTML, nomi generici, nessun dato reale]**
- [Titolare, 19:04] Anche oggi decine di preventivi. E sono ancora qui.
- [Digital Empire, 19:05] Mandami il link di un annuncio.
- [Digital Empire, 19:06] Fatto. Ecco il PDF col vostro logo, prezzo già calcolato. Pochi secondi.
- [Titolare, 19:07] …lo puoi fare per tutti?

**[prima-dopo]** Prima: ore, ogni giorno. Dopo: pochi minuti.

**[chiusura]** Lo stesso lavoro. Fatto da una macchina che è loro. Adesso ti mostro quanto costa — e quanto costerebbe affittarlo.

---

### Autocontrollo gate voce (manuale — l'header `## D1` non entra nella regex `## N\d+` degli script di sezione)
- Lista nera: 0 occorrenze.
- Barnum: 0 occorrenze (nessuna delle formule della lista).
- Prima persona: presente («abbiamo costruito», «ci hanno chiesto», «ti faccio», «ti mostro»).
- Provocazione con numero: l'unica «?» è la battuta del cliente in chat («…lo puoi fare per tutti?»), voce riportata non
  provocazione nostra; il gancio di chiusura («quanto costa») introduce la sezione `PrimaDopo` che segue, dove i numeri
  (listino) arrivano subito.
- Gate fatti: 65, 11, 2 → in `FATTI.novacar`. «Dieci» e ogni altro numero restano parole, non cifre. Gli orari in chat
  (19:04 ecc.) stanno dentro il tag `[Nome, ora]`, fuori dal testo passato al gate — coerente con come `gate_fatti.py`
  tratta i tag `[ruolo]`.
