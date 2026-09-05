# Report — A4/L04 · «Editing Video Automatico con AI All in One»

> Le sei voci obbligatorie del piano (§6.2). Appunti integrali in `appunti.md`, schermate in
> `frame-scelti.md`.

---

## 1. Cosa insegna

Come si trasforma un testo in un **video montato** senza toccare un editor: si sceglie il
formato, si sceglie la voce, si incolla il testo, e la piattaforma spezza in scene, pesca le
clip, sincronizza i sottotitoli e monta. Lo strumento è **Fliki** — cioè **il nostro strumento di
produzione**, mostrato dal di dentro.

Le leve che la lezione insegna, tutte lette a schermo:

1. **Il formato è una destinazione**, non un default: Portrait (TikTok/Shorts/IG), Square
   (IG/Twitter/LinkedIn), Landscape (YouTube). «Per YouTube dobbiamo mettere landscape.»
2. **La voce si filtra su quattro assi** — lingua, dialetto/accento, genere, *voice style* — e si
   può applicare **a tutto il file** in un colpo.
3. **Il movimento va lasciato acceso**: Ken Burns fra le sezioni e zoom sulle immagini, «perché
   sembra un video e non sembra un'immagine».
4. **La musica è una funzione della piattaforma**, cercabile per genere, col volume regolabile e
   **l'abbassamento automatico sotto la voce**.
5. **Quattro leve fini sul parlato**, tutte sulla selezione del testo: pronuncia (l'accento
   grafico che corregge `iscrivìti` → `iscrìviti`), pausa (0,2 s fra parole; 1-3 s a fine clip),
   velocità (Tune → Rate, −7 / −11), intonazione.
6. **Idea to video**: dalla sola idea (o da un link, un PowerPoint, un tweet) esce un video
   intero — con l'avvertenza dichiarata che «lo script non è perfetto, qualche immagine non è
   perfetta».

## 2. Cosa facciamo oggi (verificato sul disco, non ricordato)

| Pezzo | Dove | Stato reale |
|---|---|---|
| Formato del video | `fliki_client.py:258` | **`"aspectRatio": "16:9"` scritto a mano nel payload.** Nessun parametro, nessun override per canale: verticale e quadrato sono irraggiungibili |
| Voce | `fliki_client.py:95-116` | filtra per **genere soltanto** e prende `candidates[0]`. Lingua e dialetto risolti via API; *voice style* mai usato (debito già aperto: `A4-L03-01/02`) |
| Movimento sulle immagini | `fliki_client.py:178-180`, `303-312` | **facciamo più della lezione**: `aiVideoModel` + `aiVideoClipPercentage=100` (tutte le scene come clip in movimento) + `imageAnimationPreset="Mix"` |
| Sottotitoli | `fliki_client.py:291-292` | **sempre attivi**, con `subtitlePresetId` per canale e `highlightSubtitles=True` (effetto karaoke, voluto da Gael) |
| Divisione in scene | `fliki_client.py:119-140`, `267` | `sceneBreakdown: lineBreak` + `MAX_WORDS_PER_SCENE=130` (nato da un blocco da 594 parole che aveva bloccato un job per un'ora) |
| **Musica di sottofondo** | — | **nessun campo nel payload.** Cercati `backgroundMusic`, `musicId`, `audioTrack` in `02-AUTOMAZIONI-E-SCRIPTS/`: zero occorrenze |
| **Pausa, velocità, pronuncia** | — | **nessun campo nel payload.** Le tre leve fini della lezione vivono solo nell'interfaccia |
| Chi monta il video | `video-producer.md:20` | l'agente dichiara: «Non "monti" tu il video (**lo fa l'utente in Fliki**)» |
| Cosa l'agente ordina | `video-producer.md:26-31` | musica col volume bilanciato · transizioni fra scene · **anteprima obbligatoria** · «non chiudere il browser durante il rendering» |
| Cosa il gate controlla | `qa-audio-video.md:21,35` | boccia il video se «il volume della musica è troppo alto rispetto alla narrazione», e prescrive «ridurre volume musica al 10%» |

## 3. Delta

**Il delta di questa lezione non è una tecnica che ci manca. È uno scollamento: metà del nostro
apparato descrive un lavoro che nessuno fa più da mesi.**

**a) `video-producer` istruisce un essere umano che non esiste.**
L'agente dice, testualmente, che il video lo monta *l'utente in Fliki*. Non è vero da quando la
produzione passa per `fliki_client.py`: il payload parte, `shouldExport: True`, e il file torna
già esportato. Nessun umano apre un browser, nessuno guarda un'anteprima, nessuno bilancia un
volume. Quattro dei sei ordini dell'agente (**musica**, **transizioni**, **anteprima
obbligatoria**, **non chiudere il browser**) sono **ineseguibili dalla catena che li dovrebbe
eseguire**. Un agente che ordina cose impossibili non è severo: è rumore, e insegna a ignorarlo.

Lo stesso vale per le due schede che l'agente legge: `fliki-produzione.md` descrive la
registrazione via email e i clic nell'interfaccia; `fliki-avanzato.md` §2 dice di aggiungere le
pronunce «nella sezione Pronunciation delle impostazioni vocali del progetto» — un pannello che
la nostra catena non apre mai. **Questo difetto era già stato trovato in L03 e dichiarato
minore.** L04 mostra che non era minore: è sistemico, e riguarda tre file su tre.

**b) Il gate controlla una cosa che potrebbe non esistere.**
`qa-audio-video` è un gate **bloccante** e ha fra i criteri il volume della musica. Ma nel nostro
payload la musica non c'è. Delle due l'una: o Fliki ne aggiunge una di default — e allora la
stiamo lasciando scegliere alla piattaforma, senza deciderla — o non c'è, e il gate ha un criterio
che non può fallire mai. **Non lo so, e non lo scrivo come se lo sapessi**: si accerta ascoltando
un MP4 reale già prodotto. Finché non è accertato, quel criterio non è un controllo, è una
formula.

**c) Il formato è murato a 16:9.**
`aspectRatio` è una stringa fissa dentro il payload. Finché la fabbrica fa solo video lunghi per
YouTube va bene — ma è una decisione presa **una volta e mai più dichiarata**, e il giorno che
serve uno Short non c'è un parametro da cambiare: c'è una riga di codice da modificare, cioè un
intervento sul motore in produzione. La lezione mette in fila le tre destinazioni con i social
scritti accanto: è la prova che nello strumento il formato è **un campo**, non una costante.

**d) Dove siamo avanti (e va scritto, perché non venga "semplificato").**
Sul movimento la lezione consiglia di lasciare acceso il Ken Burns «così sembra un video e non
un'immagine». Noi facciamo un passo oltre: `aiVideoClipPercentage=100` genera **clip vere in
movimento** per tutte le scene, con `imageAnimationPreset="Mix"` sulle immagini residue. È una
scelta pagata cara (il campo veniva ignorato senza `aiVideoModel`: il video v10 era uscito tutto
fermo). Questa lezione la **conferma da fuori** — e conferma anche i sottotitoli sempre accesi.

**Quello che NON prendo da questa lezione:**
- **`Idea to video`** — la scorciatoia dall'idea al video. È l'opposto della nostra catena: noi
  passiamo per ricerca, script e regolatori perché il contenuto sia nostro e difendibile. La
  lezione stessa ammette che «lo script non è perfetto». Porta chiusa, con motivo.
- **Le immagini prese da Google Immagini** — nella lezione si salva la foto di una persona reale
  da una ricerca e la si mette nel video. Per noi è materiale di terzi su una persona reale:
  porta chiusa, come le voci dei personaggi famosi di L03.
- **Il flusso a mano** (clic, anteprima, download): è esattamente ciò che dobbiamo smettere di
  descrivere nei nostri agenti.

## 4. Conflitti col nostro modo di fare

**Nessun conflitto di merito con la lezione** — insegna lo strumento che usiamo, e ciò che
consiglia (movimento acceso, sottotitoli accesi, formato scelto per la destinazione) o lo facciamo
già o è giusto.

**Il conflitto è di nuovo tutto in casa nostra, ed è più grave di quello di L03:**

| chi dice cosa | contro |
|---|---|
| `video-producer.md` — «lo monta l'utente in Fliki», anteprima obbligatoria, non chiudere il browser | `fliki_client.py` — payload API, `shouldExport: True`, nessun browser |
| `fliki-avanzato.md` §3 — «volume musica al 10-15%» | payload senza alcun campo musica |
| `qa-audio-video.md` — gate bloccante sul volume della musica | idem |
| `fliki-produzione.md` — «≥1080p, MP4, non chiudere il browser» | `resolution: "1080p"` fisso nel payload: giusto il valore, sbagliato chi lo imposta |

**Arbitrato:** vince **il codice**, perché è ciò che produce i video veri. Le schede e l'agente si
riscrivono su di lui. Ma la parte della lezione che il codice **non** copre (musica, pronuncia,
velocità, formato) non si cancella: si sposta nella colonna «non raggiungibile via API», scritta
nero su bianco, così che nessuno la prescriva più come se fosse un'operazione nostra.

Nessun conflitto fra lezioni: `CONFLITTI.md` resta non necessario.

## 5. Regole estratte

Cinque, nel registro: `regole/A4-metodo-ai-tube/L04_editing_automatico.py`.

| id | regola in una riga | tocca | binario |
|---|---|---|---|
| `A4-L04-01` | `video-producer` descrive **ciò che la catena fa davvero**: produce la spec del payload API, non le istruzioni per un umano che monta a mano | `video-producer.md` | **A** |
| `A4-L04-02` | Il **formato è una decisione di destinazione**, dichiarata per canale, non una costante nel payload | `fliki_client.py` / `apex7_orchestrator.py` | **B** |
| `A4-L04-03` | Ogni scheda su Fliki dichiara **cosa è raggiungibile via API e cosa no**: musica, pronuncia, velocità, pause e anteprima stanno nell'interfaccia, e la nostra catena non le tocca | `fliki-produzione.md` · `fliki-avanzato.md` | **A** |
| `A4-L04-04` | Un **gate bloccante controlla solo ciò che esiste**: il criterio sulla musica resta sospeso finché non è accertato su un MP4 reale se i nostri video ne hanno una | `qa-audio-video.md` | **A** |
| `A4-L04-05` | Le scene **si muovono sempre**: clip AI al 100% con animazione sulle immagini residue. Tornare alle immagini ferme è una regressione, non una semplificazione | `video-producer.md` | **A** |

## 6. Applicabilità alla nostra fabbrica

- **A4-L04-01, -03, -04, -05 applicate subito** (binario A): un agente e tre schede. Nessuna riga
  del motore toccata, nessun rischio sulla produzione in corso.
- **A4-L04-02 registrata e in attesa del gate A4** (binario B): rendere `aspectRatio` un parametro
  tocca `fliki_client.py` e `apex7_orchestrator.py`. Al gate serve: campo in `CANALI`, default
  `16:9` per entrambi i canali (comportamento invariato), e **un video di prova** in verticale
  prima di dichiararlo funzionante.
- **Verifica aperta, assegnata al gate A4:** ascoltare un MP4 già prodotto e stabilire se contiene
  musica. Da quella risposta dipende se `A4-L04-04` si chiude togliendo il criterio o rendendolo
  reale.
- **Debito dichiarato:** finché `A4-L04-02` non entra, la fabbrica **non può produrre Shorts**.
  Non è un rischio creato dalla regola — è un limite che esisteva e che nessun documento diceva.

**Valore netto della lezione: alto, e non per ciò che insegna.** Tecnicamente ci ha dato poco che
non avessimo (anzi: su movimento e sottotitoli siamo avanti). Ci ha dato il **catalogo completo
delle leve dello strumento che usiamo**, e con quello in mano si vede che tre documenti su tre
descrivono un flusso manuale che la fabbrica ha abbandonato mesi fa. **Il valore di specchio è
altissimo:** è la seconda lezione di fila che ci trova in contraddizione con noi stessi, e questa
volta la contraddizione arriva fino a un gate bloccante.
