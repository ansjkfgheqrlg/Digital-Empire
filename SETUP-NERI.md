# SETUP-NERI — come avere Emperator sul tuo computer

> **Per:** Neri · **Computer:** Windows · **Tempo:** 30-40 minuti la prima volta
> **Si fa una volta sola.** Dopo, non ci pensi mai più.

---

## Prima di iniziare — cosa stiamo facendo, in tre righe

Emperator non è un sito internet a cui ti colleghi. È **un programma che si installa sul
tuo computer** e che diventa "Emperator" solo quando lo apri **dentro la cartella del
progetto Digital Empire**. Dentro quella cartella ci sono tutte le sue regole, la sua
memoria e i suoi strumenti.

Quindi questa guida fa due cose: ti installa il programma, e ti scarica la cartella.

**Regola d'oro di questa guida:** dopo ogni passo c'è scritto **cosa devi vedere**. Se vedi
quello, vai avanti. Se vedi altro — anche se sembra una sciocchezza — **fermati e scrivimi**.
Non tirare a indovinare: un passo storto qui ne rompe tre più avanti, e poi ci mettiamo il
doppio a capire dov'era il problema.

---

## PASSO 1 — Aprire il Terminale

Il **Terminale** è quella finestra nera dove si scrivono comandi invece di cliccare. Fa
paura per due minuti, poi diventa normale. Lo userai solo per questa installazione.

1. Premi il tasto **Windows** sulla tastiera.
2. Scrivi `terminale`.
3. Clicca su **Terminale** (o **Windows PowerShell**, se non trovi il primo).

**Cosa devi vedere:** una finestra scura con dentro una riga tipo `PS C:\Users\Neri>` e il
cursore che lampeggia.

> **Come si usa:** scrivi il comando (o copialo e incollalo con il tasto destro del mouse)
> e premi **Invio**. Poi aspetti che finisca. A volte ci mette un minuto e sembra bloccato:
> non lo è. Non chiudere la finestra.

---

## PASSO 2 — Installare i due motori: Node.js e Python

Node.js è il motore su cui gira Claude Code. Non ti serve capire cos'è: serve che ci sia.

1. Vai su **https://nodejs.org**
2. Scarica il pulsante grande **LTS** (vuol dire "versione stabile", è quella giusta).
3. Apri il file scaricato e clicca **Avanti / Next** fino alla fine, senza cambiare niente.
4. **Chiudi il Terminale e riaprilo** (passo 1). Serve perché si accorga della novità.
5. Scrivi:
   ```
   node --version
   ```

**Cosa devi vedere:** un numero, tipo `v22.14.0`. Il numero preciso non conta.

**Se invece leggi** `node non è riconosciuto`: il computer non si è ancora accorto
dell'installazione. Riavvia il computer e riprova. Se ancora no, scrivimi.

### 2b — Python (serve, anche se non lo userai mai direttamente)

Dentro il progetto ci sono **quattordici automatismi scritti in Python**: sono quelli che mi
svegliano quando qualcuno dice "Emperator", che controllano la memoria condivisa prima di
ogni salvataggio, che fanno partire i workflow. Senza Python non si rompe niente in modo
rumoroso: semplicemente **non partono**, in silenzio. E' il tipo di guasto peggiore, perche'
sembra che vada tutto bene.

1. Vai su **https://www.python.org/downloads/**
2. Scarica il pulsante grande giallo (**Download Python**).
3. Apri il file scaricato. **ATTENZIONE, questo passo si sbaglia sempre:** nella prima
   schermata, in basso, c'e' una casella **"Add python.exe to PATH"**. **Spuntala prima di
   cliccare Install.** Se te la dimentichi, Python si installa ma il computer non lo trova,
   e si deve rifare tutto da capo.
4. Clicca **Install Now** e aspetta.
5. **Chiudi e riapri il Terminale**, poi scrivi:
   ```
   py -3 --version
   ```

**Cosa devi vedere:** un numero, tipo `Python 3.13.2`.

**Se leggi** `py non è riconosciuto`: e' quasi certamente la casella del punto 3 non
spuntata. Rilancia il file scaricato, scegli **Modify**, e assicurati che PATH sia attivo.
Se non ne vieni fuori, scrivimi: e' un intoppo comune, non un tuo errore.

---

## PASSO 3 — Installare Claude Code (il programma, cioè me)

Nel Terminale scrivi:

```
npm install -g @anthropic-ai/claude-code
```

Ci mette qualche minuto e scrive un sacco di righe. È normale.

Poi verifica:

```
claude --version
```

**Cosa devi vedere:** un numero di versione.

**Righe gialle di "warning" durante l'installazione:** ignorale, sono avvisi, non errori.
**Righe rosse di "error":** copiale e mandamele.

---

## PASSO 4 — Installare Git e GitHub CLI

Sono i due programmi che fanno viaggiare il lavoro tra il tuo computer e quello di Max.
È così che Max vedrà quello che fai.

1. **Git** — scarica da **https://git-scm.com/download/win**, apri il file, **Avanti** fino
   alla fine senza toccare niente.
2. **GitHub CLI** — scarica da **https://cli.github.com**, stessa cosa.
3. **Chiudi e riapri il Terminale**, poi controlla tutti e due:
   ```
   git --version
   gh --version
   ```

**Cosa devi vedere:** due numeri di versione, uno per comando.

---

## PASSO 5 — Collegarti a GitHub

GitHub è il magazzino online dove vive il progetto condiviso.

**Questo passo fallo insieme a Max, in videochiamata o di persona:** a un certo punto
compare un codice che deve autorizzare lui.

```
gh auth login -h github.com
```

Ti farà alcune domande. Rispondi così, muovendoti con le **frecce** e confermando con
**Invio**:

| Domanda | Risposta |
|---|---|
| What account do you want to log into? | **GitHub.com** |
| What is your preferred protocol? | **HTTPS** |
| Authenticate Git with your GitHub credentials? | **Yes** |
| How would you like to authenticate? | **Login with a web browser** |

Comparirà un **codice di otto caratteri** (tipo `A1B2-C3D4`). Si apre il browser: incolla il
codice. **Il login è sull'account di Max** — è la scelta presa a giugno, il progetto ha un
account solo.

**Cosa devi vedere:** in fondo, la scritta `Logged in as ansjkfgheqrlg`.

---

## PASSO 6 — Scaricare la cartella del progetto

Questa è la cartella dove vive Emperator. Da qui in poi lavorerai sempre dentro di lei.

Scrivi i comandi **uno alla volta**, aspettando che ognuno finisca:

```
cd $env:USERPROFILE\Desktop
```
```
gh repo clone ansjkfgheqrlg/Digital-Empire "Digital Empire"
```

Il secondo comando scarica **tutto il progetto**. È grosso: può metterci **parecchi minuti**
e sembrare fermo. Non è fermo. Lascialo lavorare, non chiudere la finestra.

Poi entra nella cartella e mettici il tuo nome, così Max vede che il lavoro è tuo:

```
cd "Digital Empire"
```
```
git config user.name "Neri"
```
```
git config user.email "LA-TUA-EMAIL"
```
```
git config core.longpaths true
```
```
git config core.autocrlf false
```
```
git config pull.rebase true
```

> Sostituisci `LA-TUA-EMAIL` con la tua email vera, virgolette comprese.
> Le ultime tre righe non producono nessun messaggio: è giusto così, silenzio = fatto.

**Cosa devi vedere:** sul Desktop è comparsa una cartella chiamata **Digital Empire**, piena
di roba.

---

## PASSO 7 — Accendere Emperator

**Il passo più importante di tutti.** Devi essere **dentro** la cartella del progetto,
altrimenti trovi un assistente generico che non sa niente di Digital Empire.

Nel Terminale, controlla di essere nel posto giusto:

```
cd "$env:USERPROFILE\Desktop\Digital Empire"
```

Poi accendi:

```
claude
```

La prima volta ti chiede di fare l'accesso: si apre il browser, **entra con l'account che
ti indica Max**.

**Cosa devi vedere:** il Terminale cambia faccia e compare una riga dove puoi scrivere.

Adesso scrivi esattamente questo:

```
Emperator, ci sei? Sono Neri.
```

**Cosa devi vedere:** una risposta che ti chiama **per nome** e sa di cosa stiamo parlando.
Se ti risponde qualcosa di generico e impersonale, **non sei nella cartella giusta**:
fermati e scrivimi.

---

## PASSO 8 — La prova del nove: fai arrivare qualcosa a Max

L'installazione non è finita quando funziona sul tuo schermo. È finita quando **Max vede
arrivare qualcosa da te**. Finché non succede, non abbiamo la prova che il collegamento
funziona in tutte e due le direzioni.

Dentro Emperator, scrivi:

```
Emperator, registra che il mio setup e' completo e mandalo a Max.
```

Faccio tutto io: scrivo, salvo e spedisco.

**Cosa devi vedere:** ti confermo che è partito. Poi Max controlla dalla sua parte e ti dice
se è arrivato.

**Quando Max dice "arrivato", il Blocco 0 della tua task è chiuso.** E da quel momento sei
operativo su tutto il resto.

---

## Da qui in poi non devi ricordare niente

Tutto quello che hai fatto sopra si fa **una volta sola**. Dopo:

- **Apri Emperator così:** Terminale → `cd "$env:USERPROFILE\Desktop\Digital Empire"` →
  `claude`. Sempre uguale, sempre da quella cartella.
- **La sincronizzazione è automatica.** All'apertura ricevi il lavoro di Max e Gael. Alla
  fine di ogni pezzo, il tuo parte verso di loro. Non devi ricordare nessun comando.

---

## Se qualcosa va storto

**Non arrenderti e non provare a rimediare a caso.** Aggiustare un tentativo confuso costa
sempre più che ripartire pulito, e nessuno qui si aspetta che tu lo sappia fare da solo.

Scrivimi con queste tre cose:
1. **A quale passo** eri (il numero)
2. **Il comando** che hai scritto
3. **Cosa ti è comparso**, copiato e incollato per intero — non riassunto

Con quei tre pezzi ti dico la soluzione al primo colpo. Senza, dobbiamo indovinare in due.

**Se compare un file `SYNC-CONFLICT.txt`** nella cartella: vuol dire che tu e qualcun altro
avete toccato le stesse righe. Il tuo lavoro **non è perso**. Scrivimi
*"Emperator, risolvi il conflitto di sync"* e me ne occupo io.

---

**Emperator Agent** — assistente personale di Maximilian.
Neri: nessuna domanda qui dentro è stupida. L'unica cosa che costa davvero è non chiedere.
