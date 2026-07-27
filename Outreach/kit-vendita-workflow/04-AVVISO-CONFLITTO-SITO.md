# ✅ RISOLTO — pulizia claim del sito (2026-07-27)

> Segnalazione fatta da Arena il 27/07 mentre scrivevo il kit di vendita.
> **Max ha autorizzato l'intervento diretto** ("mettila tu sul sito, e onestà, poi fai anche
> fatica claim senza situazione nuova"). Eseguito lo stesso giorno.
> **Stato: chiuso.** Questo file resta come registro di cosa è stato cambiato e perché.

---

## 🚨 La cosa più grave, che non era nei 4 punti iniziali

Cercando conferme ho controllato anche `11-testimonial.tsx`. Conteneva **tre testimonianze
complete di nome e cognome, ruolo, azienda e cinque stelle**:

| Nome | Claim |
|---|---|
| Marco Resta — Coach, Skill Beast | *"Ho triplicato i contatti mensili senza toccare niente io"* |
| Sara Conti — Social Media Manager | *"Prima 3 ore al giorno per i post, ora 20 minuti… la mia presence è triplicata"* |
| Luca Pellegrini — Founder, Agenzia Digitale | *"Primo mese: 240 lead qualificati arrivati in automatico"* |

**Ho cercato quei tre nomi in tutto il repository — `.md`, `.json`, `.csv`, `.txt`. Zero
riscontri. Nessuno dei tre esiste in nessun file.** Nemmeno i numeri ("240 lead", "triplicato")
hanno una fonte da nessuna parte.

L'unico cliente documentato su disco è **Novacar**, che è un cliente Preventa.

Questo è di un ordine di gravità diverso dai 4 claim gonfiati: **un numero ottimistico è
marketing aggressivo, una persona inventata con nome e cognome è un'altra cosa.** Ed è anche
il rischio pratico più alto: basta che un potenziale cliente cerchi "Marco Resta Skill Beast"
su LinkedIn e non lo trovi.

**Cosa ho fatto:** rimosse tutte e tre. Al loro posto la sezione ora dice, testualmente:

> *"Non abbiamo ancora una testimonianza firmata da pubblicare. Potremmo scrivere tre
> virgolettati con nomi credibili e cinque stelle, come fanno quasi tutti. Abbiamo preferito
> lasciare lo spazio vuoto."*

E rimanda ai numeri veri di Novacar. C'è anche una riga che gioca contro di noi ed è la più
convincente di tutte:

> *"Se state valutando un fornitore, il consiglio vale anche contro di noi: chiedete sempre di
> parlare con un cliente vero. Una testimonianza che non si può verificare non vale la riga su
> cui è scritta."*

Il file ha in testa un blocco di regole che spiega cosa serve per aggiungerne una vera
(consenso scritto, nome reale, numeri verificabili). L'array è tipizzato e vuoto: **appena
aggiungi una testimonianza reale, la sezione cambia forma da sola** e torna a mostrare le card.

---

## I 4 claim originali — tutti sistemati

### 1. «3-5 clienti nuovi nel primo mese» → sostituito
**Prima:** *"Per la maggior parte dei nostri clienti, l'Outreach Workflow porta 3-5 clienti nuovi nel primo mese. Con un ticket medio di 3.000€…"*
**Ora:** *"Il calcolo lo fai tu, in demo. Non ti diciamo quanti clienti porterà: dipende dal tuo mercato e dalla tua offerta, non da noi. In demo prendiamo i tuoi numeri — ore, costo orario, valore di un cliente — e vediamo insieme in quanto rientra. **Se non rientra, te lo diciamo.**"*

Più forte dell'originale: sposta il calcolo sul cliente (che si fida dei propri numeri più che dei nostri) e l'ultima frase è un segnale di onestà che nessun concorrente scrive.

### 2. «Il 90% di chi vede il sistema vuole iniziare la settimana dopo» → rimosso
**Ora:** *"Se secondo noi non fa per te, te lo diciamo in call: preferiamo perdere una vendita che consegnarti un sistema che non ti serve."*
Non l'ho sostituito con un altro numero: non ne abbiamo. L'ho sostituito con una posizione.

### 3. «In ogni demo mostriamo workflow per clienti del tuo settore» → sostituito con la verità
**Ora:** *"In demo ti mostriamo il sistema costruito per Novacar: 65 preventivi su annunci reali tra il 3 e il 13 luglio 2026, 11 marche, circa due minuti l'uno, 6 controlli automatici. **Non è del tuo settore, e te lo diciamo:** è la prova che quello che costruiamo poi funziona."*
L'ammissione preventiva disinnesca l'obiezione invece di aspettarla in call.

### 4. «Si ripaga al primo cliente» → rimosso dal titolo dell'obiezione
**Ora:** *"Fai il conto con i tuoi numeri, non con i nostri."*

---

## Altri due trovati mentre ero lì

### 5. Le statistiche in cima al sito (`02-stats.tsx`)
**Prima:** `40+` automazioni consegnate · `100%` task automatizzati · **`+300%` produttività media, "Misurata dopo 4 settimane"**

Il terzo era il peggiore: **dichiarava esplicitamente una misurazione che non esiste.** Nessuno
ha mai misurato un +300% di produttività su nessun cliente.

**Ora** — i numeri della macchina Novacar, contati sui file:
`65` documenti prodotti · `~2 min` dal dato grezzo al documento · `6` controlli prima di ogni consegna

Con sotto una riga che vale più dei numeri:
> *"Sono i numeri di una macchina che gira da un cliente vero, contati sui file e non stimati.
> Preferiamo tre numeri veri a dieci impressionanti."*

### 6. «I clienti che lo attivano non se ne pentono mai» → riscritto
Claim su un plurale di clienti che non esiste. Ora: *"Non è obbligatorio e non te lo facciamo
firmare all'inizio: si decide alla fine del mese di supporto, quando sai se ti serve davvero."*

---

## Verifica tecnica

| Controllo | Esito |
|---|---|
| `npx tsc --noEmit` | ✅ **0 errori** |
| `npm run build` | ✅ **Compiled successfully**, TypeScript OK, 4 pagine generate |
| File toccati | solo `02-stats.tsx`, `11-testimonial.tsx`, `15-objections.tsx` |
| `layout.tsx` | intatto (`git diff` vuoto) |

**Nota sul build:** in sandbox `npm run build` fallisce al download dei font Google (Cinzel,
Onest, Playfair) per assenza di rete verso `fonts.googleapis.com`. **Ho verificato che fallisce
identico anche sul codice originale**, quindi non è causato dalle modifiche. Per la prova ho
temporaneamente neutralizzato i font, ottenuto il build verde, e **ripristinato `layout.tsx`
byte-per-byte**. Sulla macchina di Gael, con rete normale, il build passa senza toccare niente.

---

## Cosa NON ho toccato (e perché)

- **La garanzia** (`12-garanzia.tsx`): *"se entro 30 giorni non produce almeno 1 risultato
  misurabile, rimettiamo mano gratis"*. Non è un numero inventato, è una promessa che potete
  mantenere. Ma è **mal calibrata**: "1 risultato misurabile" è così basso da sembrare furbo,
  mentre gli esempi ("lead generati") dipendono dal mercato del cliente, non da noi.
  **Serve una decisione tua**, non una correzione mia: il risultato garantito dovrebbe essere
  un **output del sistema** (email mandate, documenti prodotti), non un **esito di mercato**.
- **I prezzi** €5.000-15.000 e €490/€149: sono decisioni di business tue, e sono coerenti ovunque.
- **`11b-carte-scoperte.tsx`**: già onesta, dice cosa è incluso e cosa no senza gonfiare.

---

## Il punto che resta aperto

Il sito adesso **non promette più niente che non possiamo dimostrare**. Ma resta il fatto che
la sezione testimonianze è vuota e la prova è di un altro settore.

**Si riempie in due modi, entrambi già sul tavolo:**
1. la telefonata di 10 minuti a Novacar (asset a più alto rapporto valore/sforzo del repo);
2. il dogfooding documentato — **P1**.

Fino ad allora il sito è onesto ma nudo. **Meglio nudo che vestito di roba falsa**: se un
cliente scopre "Marco Resta" durante una due diligence, non perdi una trattativa — perdi la
reputazione con cui ne fai altre dieci.
