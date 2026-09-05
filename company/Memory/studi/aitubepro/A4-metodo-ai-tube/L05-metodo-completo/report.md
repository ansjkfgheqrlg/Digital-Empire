# Report — A4/L05 · «Come creare un video da zero con il metodo A.I tube (IL METODO COMPLETO)»

> Le sei voci obbligatorie del piano (§6.2). Appunti integrali in `appunti.md`, schermate in
> `frame-scelti.md`, arbitrati in `../../CONFLITTI.md`.

---

## 1. Cosa insegna

**Il metodo intero, eseguito in diretta col cronometro.** Sette passi, cinque minuti dichiarati:

1. **Home di YouTube** → il video col «numero magico»: 5.700 like, 89.000 viste, **13 ore fa**
2. copia il link — «non so assolutamente nulla di cosa tratta questo video»
3. **DownSub** → scarica i sottotitoli in TXT
4. **ChatGPT (GPT-3.5)** → «riscrivimi questo testo da zero aggiungendo qualche dettaglio… e
   rendilo originale»
5. **Fliki** → nuovo file · italiano · video · **landscape** · incolla
6. voce (**Calimero**) · elimina il blocco del titolo · aggiungi un'immagine propria
7. **Export → Download** (2-3 minuti di macchina)

Le due frasi che valgono più di tutto il resto:
- **sulla durata** (05:53): «potremmo fare un testo della durata anche di **10, 12, 15, 20
  minuti**… se io inserissi **altre parti di testo**, sarebbe ancora meglio» — cioè: la durata si
  costruisce **con più fonti**, non allungando il prompt;
- **sulla gerarchia** (04:00): «se vogliamo lavorare sulla **quantità**, che è fondamentale — poi
  ovviamente anche la qualità deve esserci».

## 2. Cosa facciamo oggi (verificato sul disco, non ricordato)

| Passo del corso | Il nostro equivalente | Stato reale |
|---|---|---|
| Fonte dalla home YouTube, «numero magico» | `video-analyst.md` — classifica per **velocity** = viste / età in ore | **c'è, ed è più rigoroso** — ma con una soglia che boccia il caso del corso: «scarta tutto ciò che è più giovane di 24 ore» (`video-analyst.md:31-32`) |
| Sottotitoli da DownSub | `transcript-collector` + `transcripts/*.vtt` | c'è, e non dipende da un sito terzo |
| «Riscrivimi questo testo» a fonte singola | `transcript-collector` §8-§9 — sotto ~1.500 parole servono **≥2 fonti esterne** | **c'è, ed è l'opposto del corso** (regola `A4-L01-02`) |
| Fliki: landscape, voce, incolla | `fliki_client.py` — `aspectRatio: "16:9"`, `voiceId`, `sceneBreakdown` | c'è, via API |
| Voce «Calimero» | `CANALI['dosementale']` — commento: «Voce Fliki (maschile, "Calimero")» | **la stessa voce del corso**, per coincidenza o per eredità |
| Blocco del titolo da eliminare | `_parse_script_scenes` + `MAX_WORDS_PER_SCENE` | c'è: il titolo non entra mai nel contenuto letto |
| Durata «10-20 minuti» | `PAROLE_MINIME_SCRIPT = 2220` (~12 min) **contro** `DURATA_MASSIMA_S = 600` (10 min) | **il difetto D-1 di `BASELINE.md`**: la fabbrica chiede più parole di quanti secondi consente |
| «5 minuti per video» | — | **non esiste alcuna misura del tempo per video** in `BASELINE.md` né altrove |
| Cosa succede dopo il download | `youtube_uploader.py`, `seo-gate`, WF4/WF5 | c'è, ed è tutta roba che il corso non ha |

## 3. Delta

**Questa lezione non ci insegna un passo che ci manca: ci mette davanti il nostro stesso metodo,
fatto in cinque minuti da una persona sola.** Il delta è in tre punti, e due sono a nostro
sfavore.

**a) La nostra soglia sulla freschezza è scritta male, e lo dimostra il caso del corso.**
`video-analyst` scarta tutto ciò che ha meno di 24 ore, con questa motivazione: *«un video di 2 ore
con 200 viste segna 100 views/ora, un dato che non si manterrà»*. L'esempio è giusto e **smonta la
regola che giustifica**: quel candidato è rumore per le **200 viste**, non per le **2 ore**. Il
video del corso — 89.000 viste in 13 ore — non è rumore per nessuna definizione, e noi lo
butteremmo. Nelle nicchie dove la freschezza *è* il prodotto (notizie, cronaca, gossip) quel
filtro non ci protegge: ci taglia fuori. Arbitrato in `CONFLITTI.md` **C-001**.

**b) Non sappiamo quanto ci costa un video.**
Il corso ha un metro: **5 minuti**. Noi abbiamo tre gate, dei regolatori e uno standard di 2.220
parole — e **nessun numero** sul tempo per video, né in `BASELINE.md` né nella dashboard. È un
buco che pesa il doppio alla luce di `ADR-016`: **25 pezzi finiti e mai pubblicati**, il più
vecchio fermo da 135 giorni. Finché il tempo per video non è misurato, «noi puntiamo sulla
qualità» non è una scelta dichiarata: è una frase che copre la lentezza. Arbitrato in
`CONFLITTI.md` **C-003**.

**c) Sulla fonte singola siamo avanti, e la lezione ce lo conferma senza volerlo.**
Il metodo a un solo video è quello che il corso *mostra*; il metodo a più fonti è quello che il
corso *dichiara migliore* sedici minuti dopo, e non usa. Noi abbiamo già in casa il secondo
(`transcript-collector` §8-§9). E il fatto lo conferma: con una fonte sola il video prodotto in
diretta dura **2:34**, contro i 10-20 minuti annunciati. Arbitrato in `CONFLITTI.md` **C-002**.

**Il dato che serviva a D-1.** Il difetto aperto in `BASELINE.md` — `DURATA_MASSIMA_S=600` contro
`PAROLE_MINIME_SCRIPT=2220` (≈12 min) — trova qui un riferimento esterno: **il metodo del corso
punta a video da 10-20 minuti**. Non è la prova definitiva (la lezione sulla durata ottimale è in
A6), ma sposta l'indizio in una direzione precisa: **è il tetto dei 600 s a essere stretto**, non
il minimo di parole a essere alto. Resta assegnato al gate A6, come deciso.

**Quello che NON prendo da questa lezione:**
- **DownSub** — dipendenza da un sito terzo per una cosa che facciamo già in casa.
- **La fonte singola riscritta** (C-002) e **l'immagine presa dal web** (stessa porta chiusa di
  L04).
- **«Non so nulla di cosa tratta»** — nella nostra catena il tema è deciso in F1 e verificato dal
  `niche-gate`: produrre alla cieca è esattamente ciò che i gate esistono per impedire.
- **GPT-3.5 e il prompt in una riga**: il nostro script nasce da un processo con regolatori.

## 4. Conflitti col nostro modo di fare

**Tre, e sono i primi dello studio.** Aperto `company/Memory/studi/aitubepro/CONFLITTI.md`:

| id | Il conflitto | Esito |
|---|---|---|
| **C-001** | Il corso sceglie un video di **13 ore**; `video-analyst` scarta tutto sotto le **24 ore** | **Vinciamo noi, con correzione**: la soglia temporale diventa condizionale al **volume di viste** |
| **C-002** | Il corso lavora su **una fonte sola** riscritta; noi pretendiamo **≥2 fonti** sotto soglia | **Vinciamo noi, senza attenuanti** — e la ragione più forte è una frase del corso stesso |
| **C-003** | «Prima la quantità»; noi abbiamo tre gate bloccanti | **Vinciamo sulla gerarchia**, ma il corso ci ricorda che **non misuriamo il tempo per video** |

## 5. Regole estratte

Quattro, nel registro: `regole/A4-metodo-ai-tube/L05_metodo_completo.py`.

| id | regola in una riga | tocca | binario |
|---|---|---|---|
| `A4-L05-01` | Un video giovane si scarta per **poche viste**, non per poche ore: sotto le 24 h il candidato entra se il **volume assoluto** rende la velocity credibile | `video-analyst.md` | **A** |
| `A4-L05-02` | La durata di uno script si costruisce **aggiungendo fonti**, mai allungando il prompt: «scrivi più dettagli» gonfia il testo, non lo nutre | `script-writer.md` | **A** |
| `A4-L05-03` | Il metodo **a fonte singola riscritta** è scartato, con la motivazione scritta, perché nessuna lezione successiva lo reintroduca di straforo | `transcript-collector.md` | **A** |
| `A4-L05-04` | Il **tempo per video** è una misura di fabbrica: si cronometra e si scrive, come le altre. Senza, «puntiamo sulla qualità» non è una scelta ma una scusa | `BASELINE.md` (studio) | **A** |

## 6. Applicabilità alla nostra fabbrica

- **Tutte e quattro applicate subito** (binario A): tre agenti e la baseline dello studio. Nessuna
  riga del motore toccata.
- **`A4-L05-01` è la più preziosa dello studio finora**: non viene da ciò che il corso insegna, ma
  dall'attrito fra ciò che il corso fa e ciò che noi vietiamo. Ci sblocca un'intera famiglia di
  nicchie (attualità, cronaca, gossip) che oggi il nostro filtro taglia fuori senza che nessuno lo
  sapesse.
- **`A4-L05-04` apre un buco che va riempito**, non chiuso con una riga: la misura del tempo per
  video richiede di cronometrare una produzione vera. **Assegnata al gate A4**, insieme alla
  verifica sulla musica di `A4-L04-04`.
- **Debito dichiarato:** finché il tempo per video non è misurato, il confronto col metro del
  corso (5 minuti) resta impossibile — e con esso ogni discorso serio su «quantità contro
  qualità».

**Valore netto della lezione: il più alto finora.** È corta (7:49, il 25% di L04) e non insegna
nulla di tecnicamente nuovo, ma è **la prima che ci contraddice**, e da tre conflitti sono nate
tre correzioni vere. Il pezzo migliore — la soglia sulla freschezza scritta come vincolo temporale
invece che di volume — era un difetto nostro che nessuna lettura interna avrebbe trovato: ci
voleva qualcuno che facesse la cosa che noi vietiamo, e la facesse funzionare.
