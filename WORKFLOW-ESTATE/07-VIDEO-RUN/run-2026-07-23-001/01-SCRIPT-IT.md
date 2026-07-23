# 01 — SCRIPT ITALIANO (scene + timing indicativo)

**Titolo di lavoro:** Come installare e configurare Claude Code in 5 minuti (Tutorial Completo)
**Durata totale indicativa:** ~13:00 (finestra 12-15 min raccomandata da `02_PATTERN_VINCENTI.md` §4)
**Formato:** screencast (terminale) senza volto in camera — pattern "SOS Automazioni" (converte
meglio su pubblico B2B rispetto al volto, per canale senza storico/fiducia pregressa).
**Voce:** narrazione fuori campo (per la sintesi vocale, vedi `02-TTS.txt`).

> Nota timing: i minuti sono indicativi (script parlato, non montaggio finale). La regola dura è
> una sola: la CTA alla risorsa gratuita deve chiudersi **entro 0:78** (10% di 13:00) — chiude a
> 1:10, con margine.

---

## Scena 1 — HOOK / prova tangibile (0:00 – 0:35)
**ON-SCREEN:** terminale con un progetto di test aperto, bug reale nel form di contatto.
**PARLATO:**
> Guarda questo terminale. Un attimo fa c'era un bug che bloccava l'invio del form di contatto di
> un sito vero. Ho scritto un comando, ho premuto invio, e Claude Code ha letto da solo il
> progetto, trovato il file giusto e corretto l'errore. Zero copia e incolla dal browser, zero
> schede aperte con ChatGPT. Oggi ti mostro esattamente come installare Claude Code sul tuo
> computer, passo per passo, anche se non hai mai aperto un terminale in vita tua.

---

## Scena 2 — CTA RISORSA GRATUITA (0:35 – 1:10) ⟵ *entro il primo 10% dello script*
**ON-SCREEN:** copertina "Manuale Claude Code — Parte 1 (gratis)" in sovrimpressione, freccia verso
la descrizione.
**PARLATO:**
> Prima di partire, una cosa sola. Ogni comando che uso in questo video — installazione, primo
> avvio, primo test — lo trovi già scritto, pronto da copiare, nella Parte 1 del Manuale di Claude
> Code in italiano, ed è gratuita: il link è il primo della descrizione qui sotto. Aprila in
> un'altra scheda, seguila in parallelo al video, e se ti blocchi su un comando la soluzione ce
> l'hai già davanti. Terminale alla mano, si comincia davvero.

---

## Scena 3 — PROBLEMA (1:10 – 2:45)
**ON-SCREEN:** browser con ChatGPT aperto, poi editor con codice incollato manualmente (dimostrare
il "passacarte").
**PARLATO:**
> Parliamoci chiaro: ChatGPT resta uno strumento straordinario, ma per chi scrive codice o gestisce
> automazioni per un'azienda ha tre limiti pesanti. Primo: non vede il tuo progetto, quindi ogni
> volta devi incollargli codice e spiegargli la struttura delle cartelle da zero. Secondo: lavora
> solo su quello che gli incolli tu, quindi se dimentichi un file o una variabile, la soluzione che
> ti dà è incompleta. Terzo: ti trasforma nel passacarte tra il browser e il tuo editor, con
> Ctrl+C e Ctrl+V a ripetizione invece che nella logica del lavoro vero. Claude Code cambia questo
> perché è un agente che vive dentro la cartella del tuo progetto: vede i file, li apre, li
> modifica ed esegue comandi direttamente sul tuo terminale.

---

## Scena 4 — REQUISITI DI SISTEMA (2:45 – 3:45)
**ON-SCREEN:** slide con 3 icone (Node.js, account Anthropic, terminale).
**PARLATO:**
> Per installarlo ti servono solo tre cose. Uno: Node.js in versione 18 o superiore — se non sai se
> ce l'hai, tra un attimo controlliamo insieme. Due: un account Anthropic attivo, lo stesso che usi
> per Claude nel browser. Tre: un terminale qualsiasi — su Windows va bene PowerShell o il
> Terminale di Windows, su Mac il Terminale di sistema, su Linux la tua shell abituale. Non serve
> altro: niente ambienti virtuali, niente configurazioni particolari.

---

## Scena 5 — INSTALLAZIONE DEL PACCHETTO (3:45 – 5:00)
**ON-SCREEN:** terminale reale, comandi digitati dal vivo.
**PARLATO:**
> Apriamo il terminale e verifichiamo Node: scriviamo node trattino v e premiamo invio. Se compare
> un numero di versione dalla 18 in su, sei pronto; se il terminale non riconosce il comando,
> installa Node.js dal sito ufficiale e poi torna qui. Fatto questo, un solo comando installa
> Claude Code a livello globale: npm install trattino g, poi at-anthropic-ai slash claude-code. Il
> pacchetto scarica in pochi secondi, non minuti. Quando il terminale ti restituisce il controllo,
> l'installazione è completa.

---

## Scena 6 — AUTENTICAZIONE (5:00 – 6:15)
**ON-SCREEN:** terminale, poi passaggio automatico al browser per l'autorizzazione, poi ritorno al
terminale.
**PARLATO:**
> Ora spostati nella cartella del tuo progetto con il comando cd seguito dal nome della cartella, e
> scrivi semplicemente claude, poi invio. Al primo avvio ti chiede di autenticarti: si apre
> automaticamente il browser sulla pagina di Anthropic, clicchi su Authorize, torni al terminale e
> l'accesso è confermato. Da questo momento quel terminale, in quella cartella specifica, ha un
> assistente che vede i tuoi file e può leggerli e modificarli quando glielo chiedi.

---

## Scena 7 — PRIMO TEST REALE (6:15 – 8:45)
**ON-SCREEN:** terminale, prompt digitato dal vivo, Claude Code che legge i file e propone la
modifica, approvazione con invio, file cambiato in tempo reale.
**PARLATO:**
> Vediamolo lavorare per davvero. Nel mio caso c'era un modulo di contatto che non inviava le
> email. Ho scritto un prompt semplice nel terminale: controlla perché il form di contatto non
> invia l'email. Claude Code ha letto l'intero progetto da solo, trovato il file che gestisce
> l'invio, individuato la variabile mancante, e mi ha proposto la modifica esatta: basta premere
> invio per approvarla e il file cambia all'istante. Nessuna riga incollata a mano, nessuna
> spiegazione della struttura del progetto: l'ha capita da sola leggendo i file. Questo è il salto
> reale rispetto a una chat in un browser: qui il codice vive nel tuo progetto, con la tua
> struttura di cartelle, dal primo secondo.

---

## Scena 8 — ERRORI COMUNI DA EVITARE (8:45 – 10:00)
**ON-SCREEN:** slide con 3 punti numerati, screenshot di un errore di compatibilità Node.
**PARLATO:**
> Tre errori che vedo ripetersi a chi installa Claude Code per la prima volta. Primo: lanciare il
> comando nella cartella sbagliata — Claude Code lavora sulla cartella in cui apri il terminale,
> quindi prima di un progetto vero spostati sempre nella cartella corretta. Secondo: una versione
> di Node troppo vecchia — se l'installazione si blocca con un errore di compatibilità, il più
> delle volte la causa è quella. Terzo, il più costoso per chi lavora con dati aziendali: dare
> accesso a cartelle con informazioni sensibili senza pensarci prima — su questo, tra poco, ti dico
> esattamente cosa impostare.

---

## Scena 9 — OFFERTA & CTA FINALE (10:00 – 12:30)
**ON-SCREEN:** copertina del Manuale completo, elenco puntato dei tre bonus citati, prezzo in
sovrimpressione.
**PARLATO:**
> Quello che hai visto è l'installazione di base, il minimo per partire: cinque minuti reali, non
> di marketing. Ma ecco quello che i tutorial gratuiti di solito non dicono: usato senza
> configurazione, Claude Code può leggere cartelle enormi come node underscore modules o i log e
> farti consumare crediti API inutilmente in poche ore; e se non gli dai le regole giuste, può
> modificare file che non volevi toccare. Per questo esiste il Manuale Completo di Claude Code in
> italiano: dentro trovi il file di esclusione già pronto che taglia i consumi di API, una raccolta
> di oltre cinquanta comandi pronti per automazioni, scraping e script aziendali, e la guida
> completa ai server MCP per collegare Claude in sicurezza al tuo database o ai tuoi strumenti di
> lavoro. Hai già la Parte 1 gratuita per partire; il Manuale completo, a sessantasette euro con
> gli aggiornamenti inclusi, è per chi vuole andare oltre l'installazione. Il link, sempre il
> primo, è in descrizione.

---

## Scena 10 — CHIUSURA (12:30 – 13:00)
**ON-SCREEN:** faccia del canale (bumper) o slide di chiusura con iscriviti + prossimo video.
**PARLATO:**
> Se questo video ti ha fatto risparmiare anche solo dieci minuti di tentativi a vuoto, iscriviti
> al canale: qui continuiamo un video alla volta, sempre con il terminale aperto, senza scorciatoie
> finte. Scrivimi nei commenti quale comando di Claude Code vuoi vedere nel prossimo video. Ci
> vediamo lì.

---

## Checklist struttura (da `references/teoria-script.md`, riusata)
- [x] Hook (prova tangibile) nei primi 5-10s, chiaro e pertinente
- [x] CTA iniziale (risorsa gratuita) entro il primo 10% dello script
- [x] Intro/Problema: presentazione implicita + valore proposto
- [x] Corpo: requisiti → installazione → autenticazione → test → errori, ordine che tiene la
      retention (progressione logica, ogni scena presuppone solo la precedente)
- [x] CTA finale forte e assertiva (Manuale completo)
- [x] Keyword target nel parlato: "installare Claude Code", "Claude Code terminale", "configurare
      Claude Code" (per l'indicizzazione dei sottotitoli, vedi `04-SEO-PACK.md`)
