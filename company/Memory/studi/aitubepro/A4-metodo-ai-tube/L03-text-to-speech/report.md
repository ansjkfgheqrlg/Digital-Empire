# Report — A4/L03 · «Text to speech: cosa è, e come funziona»

> Le sei voci obbligatorie del piano (§6.2). Appunti integrali in `appunti.md`, schermate in
> `frame-scelti.md`.

---

## 1. Cosa insegna

Come si trasforma un testo in voce e — soprattutto — **quali leve esistono su una voce
sintetica**. Non insegna uno strumento (lo dice apertamente: «questo è l'unico video dove non vi
posso far vedere uno strumento specifico»), insegna un pannello di comandi:

1. **La scelta della voce ha cinque leve**, non una: genere, lingua+accento, **età percepita**
   (bambino / giovane adulto / matura), **uso previsto** (audiolibri, educazione, intrattenimento,
   marketing, news), **emozione**.
2. **La punteggiatura è una direzione di regia**: aggiungere una virgola cambia la lettura, e lo
   dimostra a orecchio sullo stesso testo.
3. **La velocità va regolata** finché il ritmo non è quello giusto, non lasciata di default.
4. **Le pause si mettono su una parola scelta**, con la durata in secondi.
5. **Gli accenti sono l'unica cosa che l'AI sbaglia sistematicamente** — «iscrivìti» invece di
   «iscrìviti» — e la contromisura è un **dizionario di pronunce** che il programma applica in
   automatico ogni volta che quella parola compare. La regola operativa detta a voce:
   «ve le salvate su un file».

## 2. Cosa facciamo oggi (verificato sul disco, non ricordato)

| Pezzo | Dove | Stato reale |
|---|---|---|
| Scelta della voce | `fliki_client.py:95-117` (`find_italian_voice`) | **filtra solo per genere e prende `candidates[0]`** — la prima della lista che l'API restituisce. Nessun criterio di età, uso, emozione |
| Voce fissata per canale | `apex7_orchestrator.py:84-119` (`CANALI`) | **NON esiste**: la configurazione ha `voice_gender` («male» per dosementale, «female» per legamidiamore) ma **nessun `voice_id`**. La voce viene ri-risolta a ogni generazione |
| Cosa chiede l'agente | `voice-caster.md` §2 | «serve una voce **maschile, calma, di qualità**, non la prima disponibile» |
| Pause, enfasi, velocità | `04-SKILLS-E-REFERENCE/references/fliki-avanzato.md` §1 | **c'è**: `[pause: 0.5s]` dopo i concetti complessi, velocità al 90-95% se la voce corre |
| Dizionario delle pronunce | `fliki-avanzato.md` §2 | **c'è come scheda**: 5 trascrizioni consigliate (`Cash Cow`→`Cescau`, `VPH`→`Viu per ora`, `SEO`, `Automation`→`Automescion`, `Fliki`→`Flichi`) |
| Il dizionario che cresce | `qa-audio-video.md` §7 | **sulla carta sì, nei fatti no**: l'agente deve registrare gli errori di pronuncia in `memory/decisions`. Contate le decisioni reali: **125, di cui 0 sulla pronuncia o sulla voce** (solo `DEC-nicchia` e `DEC-video`) |

## 3. Delta

**Due buchi, e il primo è quello che si vede e si sente.**

**a) La voce del canale non è fissata da nessuna parte.**
`voice-caster` chiede «una voce calma, di qualità, non la prima disponibile». Il codice che
esegue quell'ordine prende **letteralmente la prima** voce del genere richiesto. L'agente e
l'implementazione dicono due cose opposte, e comanda il codice.

Il costo non è estetico: `candidates[0]` dipende dall'ordine in cui l'API restituisce le voci.
Se quell'ordine cambia — una voce nuova, un riordino a monte — **il canale cambia voce da un
video all'altro senza che nessuno l'abbia deciso**. Per un canale che pubblica a nastro, la voce
è la faccia: cambiarla in silenzio è come cambiare il logo fra un video e il successivo.
Oggi non ce ne accorgeremmo: `memory/decisions` non contiene una sola riga sulla voce usata,
malgrado `voice-caster` §7 dica di annotarla per ogni video.

**b) Il dizionario delle pronunce non impara.**
Abbiamo la scheda con cinque parole, scritta una volta. Abbiamo un agente che deve segnalare le
pronunce sbagliate. Ma in **125 decisioni registrate non ce n'è nessuna sulla pronuncia**: il
giro si interrompe fra chi ascolta e chi scrive. Ogni errore trovato in un video muore lì, e alla
prossima occorrenza della stessa parola si sbaglia di nuovo.

La lezione ha esattamente la contromisura, ed è banale: **un file**. Non serve un sistema — serve
un posto dove la parola sbagliata e la sua correzione restino scritte, e un agente che quel posto
lo legga prima di generare.

**Quello che NON prendo da questa lezione:** Genny/LOVO come strumento (usiamo Fliki, e la
lezione stessa dice di non affezionarsi), l'AI Writer integrato (il nostro script nasce da un
processo con regolatori, non da un modulo a cinque campi), e **gli strumenti che imitano la voce
di personaggi famosi** — mostrati con leggerezza a 02:50, per noi porta chiusa: sono diritti di
immagine e di voce di persone vere.

## 4. Conflitti col nostro modo di fare

**Nessun conflitto di merito.** Un solo conflitto interno alla casa nostra, portato a galla da
questa lezione: `voice-caster.md` chiede una cosa e `fliki_client.py` ne fa un'altra. Non è la
lezione a contraddirci, siamo noi a contraddirci da soli — e ci voleva una lezione base per
accorgersene.

Difetto minore: `fliki-avanzato.md` §2 dice di aggiungere le pronunce «nella sezione
Pronunciation delle impostazioni vocali del progetto Fliki» — un'operazione **a mano dentro
l'interfaccia**, che una fabbrica che genera via API non compie mai. La scheda descrive una
procedura che la nostra catena non esegue: va detto e va risolto nel testo dello script (dove la
grafia si può correggere) invece che in un pannello che non tocchiamo.

## 5. Regole estratte

Quattro, nel registro: `regole/A4-metodo-ai-tube/L03_text_to_speech.py`.

| id | regola in una riga | tocca | binario |
|---|---|---|---|
| `A4-L03-01` | La voce di un canale si sceglie **una volta con criteri dichiarati** (genere, età percepita, uso, ritmo) e poi si **fissa**: ogni cambio è una decisione scritta, mai un effetto dell'ordine di una lista | `voice-caster.md` | **A** |
| `A4-L03-02` | `voice_id` fisso nella configurazione del canale; `find_italian_voice` serve a **risolverlo la prima volta**, non a riscegliere ad ogni generazione | `fliki_client.py` / `apex7_orchestrator.py` | **B** |
| `A4-L03-03` | Il **lessico di pronuncia** è un file vivo: ogni parola letta male trovata in QA ci finisce dentro con la grafia che la fa leggere bene, e chi scrive lo applica prima di generare | nuovo `references/lessico-pronuncia.md` + `qa-audio-video.md` | **A** |
| `A4-L03-04` | Conferma di `A4-L00-01` su un caso concreto: davanti a 52 strumenti equivalenti si sceglie per **realismo, costo, lingua e controllo fine** (pause, velocità, pronuncia), mai per novità | `references/scelta-strumenti.md` | **A** |

## 6. Applicabilità alla nostra fabbrica

- **A4-L03-01, A4-L03-03, A4-L03-04 applicate subito** (binario A): agenti e schede, nessuna riga
  del motore toccata.
- **A4-L03-02 registrata e in attesa del gate A4**: fissare il `voice_id` in configurazione tocca
  `fliki_client.py` e `apex7_orchestrator.py`, cioè la catena che sta producendo video veri.
  Al gate serve: risolvere la voce una volta con i criteri di `A4-L03-01`, scriverla in `CANALI`,
  e generare un video di prova per sentirla prima di fissarla per sempre.
- **Debito dichiarato:** finché `A4-L03-02` non entra, ogni video generato può uscire con una voce
  diversa dal precedente. Il rischio esiste **oggi**, non è creato dalla regola: la regola lo
  rende visibile.

**Valore netto della lezione:** una lezione introduttiva che ci ha fatto trovare una
contraddizione fra un nostro agente e il nostro codice, e un giro di miglioramento che esisteva
solo sulla carta. Il contenuto nuovo per noi è poco; **il valore di specchio è alto**.
