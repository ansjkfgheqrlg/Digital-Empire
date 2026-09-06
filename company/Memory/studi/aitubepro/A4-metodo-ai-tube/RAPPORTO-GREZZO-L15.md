---
Lezione: A4/L15 — «Crea il tuo AVATAR con A.I»
Corso: AI TUBE PRO
Fonte: c0d14096-611a-43ae-8f4a-ed8975d99eb7/parlato.txt
Durata coperta dal parlato: 00:06 → 13:46
Data ingestione: 2026-09-06
Stato: RAPPORTO GREZZO — nessuna proposta, solo materiale verificabile
---

# RAPPORTO GREZZO — A4/L15 «Crea il tuo AVATAR con A.I»

## 1. Cos'è la lezione, davvero

È un tutorial d'interfaccia, quasi per intero, di un unico tool esterno di avatar parlanti generati da AI (verosimilmente **D-ID Studio** — la trascrizione lo storpia sistematicamente in "studio di ID" / "studio d'id"). Il docente clicca dentro l'interfaccia del sito, mostra menu a tendina, pulsanti "genera video", upload di foto, e legge ad alta voce i risultati audio. Non c'è metodo trasferibile a un flusso via API: non viene mai nominato un endpoint, una chiave, un payload o una richiesta programmatica — solo point-and-click nel browser. L'unica parte non puramente dimostrativa è la chiusura sui prezzi (min 12:34-13:41) e il caso reale di deepfake di una persona vera (min 11:27-11:48), che vale come materiale di attenzione/compliance, non come procedura.

## 2. Strumenti nominati

| Strumento | A cosa serve (secondo la lezione) | Prezzo | Minuto |
|---|---|---|---|
| Tool avatar AI, nome trascritto "studio di ID" / "studio d'id" (verosimilmente **D-ID Studio** — trascrizione incerta @01:01-01:04) | Trasforma testo in video con avatar parlante; crea avatar da prompt testuale o da foto propria; text-to-speech multilingua | Vedi tabella Numeri (piani da 5$/mese a Enterprise) | 01:01, 01:13, 01:46 |
| "Sito con tutti i portali" (aggregatore/elenco di tool concorrenti) — nome non detto, solo "link in basso" | Confrontare alternative allo strumento principale | Non detto | 01:30-01:39 |

Nessun secondo software viene nominato esplicitamente per nome in tutta la lezione. Il docente dice più volte "questo è un tool, ce ne sono tantissimi altri" (01:13) senza mai citarne uno per nome.

## 3. Numeri

| Dato | Valore | Minuto |
|---|---|---|
| Risoluzione minima foto per creare avatar da immagine propria | 200×200 px | 06:31-06:35 |
| Requisito inquadratura | Frontale, senza occhiali da sole/coperture sul viso | 06:35-06:44 |
| Crediti gratuiti alla registrazione | Non quantificati ("dei crediti") | 07:03-07:06 |
| Consumo per generazione | 1 credito = 1 video generato | 08:20-08:22 (riferito anche al min 07:03) |
| Tempo di generazione di un video con voce già registrata | "nel giro di un minuto" | 13:24-13:27 |
| Piano base | 5 dollari al mese → fino a 10 minuti di registrazione | 12:44-12:49 |
| Piano intermedio | Non quantificato in prezzo, "un'ora" di registrazione | 12:49-12:52 |
| Piano Enterprise | Per "centinaia e centinaia di video" — prezzo non detto | 12:55-13:02 |
| Piano annuale | Sconto rispetto al mensile — percentuale non detta | 13:02-13:09 |
| Durata della lezione | Fino a 13:46 (~14 minuti dichiarati nel titolo) | 13:46 (chiusura) |

Nessun altro numero (percentuali di crescita, follower, view, CTR, durate di editing) viene menzionato in questa lezione.

## 4. Procedure

1. Aprire il sito del tool e cliccare su **"crea video"** — 02:25-02:29
2. Selezionare un avatar dalla libreria preesistente (tanti modelli disponibili) — 02:29-02:52
3. Impostare qualità alta e colore di sfondo; consigliato sfondo verde se il video è per YouTube, per poter poi "staccare" l'immagine con editing (chroma key) — 02:55-03:22
4. Scegliere il formato inquadratura: wide (consigliato per YouTube), quadrato o verticale — 03:45-03:54
5. Inserire il testo che l'avatar deve leggere, nel campo testo — 03:58-04:15
6. Impostare pause nel parlato, opzionalmente generare il testo con l'AI, selezionare la lingua (es. italiano) — 04:21-04:33
7. Scegliere la voce (maschile/femminile, es. voce "Isabella") e lo stile di narrazione — 04:33-04:56
8. Ascoltare l'anteprima audio prima di generare — 05:00-05:10
9. Cliccare su **"genera video"** per produrre il video finale — 05:19-05:22
10. In alternativa: creare un avatar da zero descrivendolo con un prompt testuale ("voglio un volto che assomigli a...") — 05:29-05:55
11. In alternativa: caricare un file/foto propria cliccando su "Ed" (Edit/upload) — 06:00-06:10
12. Per l'avatar da foto propria: registrarsi al sito con una email, poi caricare la foto (requisiti: min 200×200, frontale, viso scoperto) — 06:46-07:29
13. Cliccare "genera video", attendere il caricamento, poi scaricare il risultato da "Download" — 07:41-08:20
14. Per creare un ritratto interamente generato dall'AI: scegliere un genere di contenuto, scrivere un prompt descrittivo (es. "Dragon Ball", "Goku"), cliccare "genera" — 08:50-09:36
15. Far parlare il ritratto generato: inserire testo, scegliere voce e lingua, generare video — 10:00-10:52
16. Riutilizzare un testo/audio già creato in precedenza selezionando un altro personaggio dalla libreria — 11:05-11:27
17. Consultare la pagina "pricing" per vedere i piani — 12:38-12:40

## 5. Cosa è TRASFERIBILE a una fabbrica che genera via API

**QUASI NULLA.** Motivazione: l'intera lezione (punti 1-17 della sezione 4) è una sequenza di click, menu a tendina, upload manuale di foto e ascolto di anteprime dentro l'interfaccia grafica di un sito terzo. La fabbrica YouTube di Digital Empire lavora esclusivamente per payload/API verso Fliki (testo in ingresso, MP4 in uscita) e non apre mai un editor né un'interfaccia clickable di terzi: per costruzione, "dove si clicca in questo sito" vale zero qui, esattamente come specificato. Non viene mai mostrata né nominata un'API, un endpoint, un formato di richiesta, un token di autenticazione: quindi non c'è nemmeno l'ipotesi di un'integrazione tecnica da valutare.

Le uniche due cose che sopravvivono come materiale non-zero, ma NON sono procedure:
- I dati di prezzo di un concorrente/fornitore alternativo di avatar AI (sezione 3), utilizzabili solo come benchmark di mercato se mai servisse confrontare costi, non come istruzione operativa.
- Il caso concreto di deepfake su persona reale e l'uso di un personaggio protetto da copyright (Dragon Ball) senza alcun avvertimento — materiale utile solo per il registro di compliance/rischio (sezione 6 sotto), non per la produzione.

## 6. Affermazioni da segnare

- **Uso su YouTube senza mostrare il volto vero**: «E noi questo genere di video lo possiamo utilizzare per poter creare contenuti su YouTube senza mettere la faccia.» — 08:01-08:05. Nessuna menzione di eventuali obblighi di disclosure sui contenuti generati da AI.

- **Deepfake di una persona reale con finta notizia**: il docente fa leggere all'avatar un testo che annuncia una notizia luttuosa su un cantante italiano reale (nome trascritto "Roberto Bechioni", verosimilmente Roberto Vecchioni — trascrizione incerta @11:34-11:38): «Questo è un giorno di grande tristezza per il mondo della musica italiana. Il cantatore Roberto Bechioni ha annunciato sulla sua pagina Socialist.» — 11:36-11:43. Segue: «Abbiamo dato anche un volto all'intelligenza artificiale.» — 11:43-11:48. Non viene detta nessuna parola su consenso della persona reale, diritto all'immagine, o rischio di diffondere una fake news con voce/volto sintetico di qualcuno esistente.

- **Uso di IP protetta senza menzione di copyright**: creazione di un ritratto e di un avatar parlante ispirato a "Dragon Ball" e a "Goku" — personaggi di proprietà Toei Animation/Bird Studio — con il prompt «qualcosa che ha che fare con Dragon Ball... e Goku» — 09:08-09:21, poi fatto parlare: «Ciao, sono un personaggio di Dragon Ball che non conoscevi» — 10:03-10:11 e ripetuto 10:41-10:52. Nessuna parola sul rischio di diritto d'autore nel generare e distribuire contenuti con personaggi protetti.

- **Qualità del labiale non garantita** (ammissione onesta, va comunque registrata): «Ok, io ho creato il mio avatar in tempo reale. Ovviamente qui ho utilizzato la mia faccia. E quindi diciamo che la qualità è ottima, ma non è c'è il salsa al cento per cento.» — 08:25-08:39 (trascrizione incerta sulla frase finale, probabile "non è il labiale sincronizzato al cento per cento").

- **Promessa vaga di vantaggio competitivo, senza numeri**: «Ma che voi, grazie all'intelligenza artificiale, grazie al fatto di aver anticipato i tempi, potete [testo incomprensibile] per rispetto agli altri.» — 13:32-13:41 (trascrizione incerta, probabile "potete distaccarvi ampiamente rispetto agli altri"). Nessuna metrica o promessa di guadagno concreta associata.

- Nessuna menzione esplicita di "fair use", "monetizzazione YouTube" o frasi tipo "così non ti reclamano" in tutta la lezione — la si segnala per completezza come assenza, non come citazione.

## 7. Verdetto in una riga

Tutorial d'interfaccia di un tool avatar-AI concorrente (click, upload, menu), zero procedure trasferibili a una fabbrica via API, ma contiene un caso serio di deepfake su persona reale e uso di IP protetta senza alcun avvertimento — da portare al registro compliance, non al metodo di produzione.
