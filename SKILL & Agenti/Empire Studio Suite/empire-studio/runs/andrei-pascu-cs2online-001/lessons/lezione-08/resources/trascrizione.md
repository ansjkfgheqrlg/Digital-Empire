# Come ascendere con il Context Engineering

> *Questa trascrizione è stata corretta e sanificata con l'intelligenza artificiale e potrebbe contenere errori. Non è stata verificata da un essere umano.*

---

Spesso si dice: "Non puoi usare l'AI se non sai fare il task che gli affidi, perché non sai giudicare l'output." È vero, ma voglio portarlo a un livello successivo: non puoi usare l'AI se non conosci ciò che gli dai da fare, perché non sai giudicare l'**input**.

Se sei un copywriter e fai scrivere un copy all'AI, sai benissimo se è una merda o no — perché è il tuo lavoro. Se è pessimo, lo correggi. Ma a quel punto: che senso ha usare l'AI, se tanto devi correggerlo?

Questa è la storia quotidiana del 90% degli utenti AI. E porta a una domanda più grande: se l'AI fa il tuo lavoro bene, che senso hai tu? Il tuo valore esiste finché l'output è pessimo — appena diventa buono, non servi più.

Però questo non è il gioco reale.

---

## Il vero problema: l'input, non l'output

L'AI ha creato un output pessimo. Perché? Non perché l'AI non sia capace. Il vero motivo è che l'input che le hai dato — il contesto — faceva schifo.

Il punto è che non sai usarla. E la soluzione non è essere un professionista per giudicare l'output: è essere un professionista per costruire un **buon input**.

Di cosa è composto l'input?

- **Il prompt** — il testo che invii, la richiesta
- **Il contesto** — i file allegati, le informazioni extra che contestualizzano la richiesta. Se chiedi un piano per i prossimi 7 giorni ma non dici cosa vuoi raggiungere nei prossimi 7 mesi, l'AI non può indovinarlo
- **RAG** — contesto tecnico avanzato, oltre lo scopo di questo corso
- **Il training dell'AI** — su quali dati è stata allenata
- **I system prompt** — le istruzioni che Anthropic ha inserito dietro le quinte, che non puoi vedere

---

## Prompt engineering vs. Context engineering

Nel 2022-2023, tutti parlavano di prompt engineering: fare il prompt perfetto, giudicare l'output. Ma anche questo era parziale. Perché se l'output fa schifo e devi rifarlo, che senso ha averlo fatto fare all'AI?

La verità è nel **context engineering**. Il prompt conta, ma è soprattutto il contesto intorno che determina la qualità dell'output. I miei prompt personalmente sono fatti in modo molto informale — accendo la dettatura del Mac, parlo per 10 minuti, invio. È il contesto che fa il lavoro pesante.

**Cos'è il context engineering?** È quando ti concentri nel costruire le informazioni contestuali che accompagnano il tuo messaggio, permettendo all'AI di prendere decisioni migliori.

---

## Le tre spiegazioni

**Per bambini**: con contesto, l'AI sa che vuoi andare dal punto A al punto B e ti ci porta. Senza contesto, è nebbia — probabilmente va da qualche altra parte, e tu devi rifare 50 prompt.

**Per adolescenti**: chiedi a Claude una scheda d'allenamento. Se gli dici che vuoi passare da 85 a 78 kg, che hai 3 giorni liberi a settimana e 150€ al mese di budget, ti dà una scheda precisa. Se gli dici solo "fammi una scheda", ti fa domande — ma l'AI non è progettata per investigare su di te, è tua responsabilità dare il contesto corretto.

**Per adulti**: con contesto, l'AI conosce i tuoi obiettivi finali e le tue sfide attuali, e ti porta al goal nel modo migliore. Senza, deve indovinare.

---

Il context engineering si fa principalmente in **documenti Markdown** per i large language model. Per altri tipi di AI — generatori di immagini come Flux — il contesto sono le immagini stesse.
