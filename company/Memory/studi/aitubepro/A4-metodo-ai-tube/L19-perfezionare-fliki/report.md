# Report — A4/L19 · «Perfezionare un video con l'AI All In One»

> Le sei voci obbligatorie del piano (§6.2). Appunti integrali in `appunti.md`, schermate in
> `frame-scelti.md`.

---

## 1. Cosa insegna

Un giro guidato dentro **Fliki** — il nostro strumento di produzione — sui pannelli che L04 non
aveva toccato:

1. **I crediti**: plafond mensile, consumo variabile secondo cosa si aggiunge, e la possibilità
   di **chiedere un piano su misura** scrivendo all'assistenza.
2. **⭐ Il campo `YouTube channel ID(s)` nel profilo**, presentato come «una cosa fondamentale per
   non avere problemi di copyright su YouTube».
3. **Voice cloning**: due minuti di registrazione, solo inglese, in italiano «non sarà il massimo».
4. **Background music**: si sceglie o si carica, e il **volume è una percentuale** (10%).
5. **La divisione delle sezioni** col `+`, **AutoPick video**, **Change image/video**, la
   generazione dell'immagine con l'AI e il caricamento delle proprie clip.
6. **Pronunciation map**: la correzione degli accenti parola per parola.

## 2. Cosa facciamo oggi (verificato sul disco, non ricordato)

| Pezzo | Il nostro stato reale |
|---|---|
| **ID canale registrato in Fliki** | **MAI NOMINATO IN TUTTA LA FABBRICA.** Cercati `channel id`, `channelid`, `whitelist`, `licenza fliki` in `02-AUTOMAZIONI-E-SCRIPTS/`, `03-AGENTI-E-RUOLI/`, `04-SKILLS-E-REFERENCE/`: **zero occorrenze pertinenti** |
| Musica di sottofondo | nessun campo nel payload (già accertato in L04). Il pannello conferma che nell'interfaccia **esiste**, col volume in percentuale |
| Volume consigliato | `fliki-avanzato.md` §3 dice «musica al **10-15%** rispetto alla voce» — **combacia col 10% visto a schermo**: la nostra scheda aveva ragione |
| Mappa delle pronunce | `lessico-pronuncia.md` esiste; l'applicazione avviene **nel testo dello script** |
| Voice cloning | mai usato. `CANALI` non ha `voice_id` fisso (debito `A4-L03-02`, binario B) |
| Divisione in sezioni | `sceneBreakdown: lineBreak` + `MAX_WORDS_PER_SCENE=130` — **facciamo la stessa cosa, in automatico** |
| Scelta delle immagini | `visuals: "ai"` — l'equivalente automatico di *Change image → genera con AI* |

## 3. Delta

**a) ⭐ C'è un'azione concreta che protegge i canali e non l'abbiamo mai fatta.**

Fliki espone nel profilo un campo **`YouTube channel ID(s)`** (due caselle) il cui scopo
dichiarato è **prevenire i reclami di copyright** sui contenuti generati con la piattaforma: si
registra l'ID del canale su cui quei video verranno pubblicati, e in caso di reclamo si dispone
della licenza Fliki da opporre.

**Non compare in nessun file della fabbrica.** Non è un difetto di codice: è **una casella da
compilare a mano nell'account**, gratuita, che riguarda entrambi i canali (`dosementale`,
`legamidiamore`).

**Onestà su cosa fa e cosa non fa** — il docente lo presenta come un interruttore («da questo
momento non avrò più problemi di copyright»), e non lo è:
- **copre** le clip e le musiche che Fliki ci fornisce, perché registra la nostra licenza presso
  il fornitore;
- **non copre** ciò che carichiamo noi, né materiale di terzi.
- Il «**nel 99,9% dei casi non dovreste avere problemi**» è **una stima detta a voce**, non un
  dato: la riporto come sua, non come nostra.

**b) La mappa delle pronunce non è la soluzione che sembrava — e lo dice lo schermo.**

Il docente afferma che le correzioni «rimangono salvate su Fliki». Il pannello dichiara:
«…to apply while generating audio **for this video**». **È per singolo video**: non si eredita fra
progetti e una generazione via API non la vede.

Questo **chiude una speranza e conferma una regola**: il debito aperto in L03 — le correzioni di
pronuncia trovate in QA che non entrano mai in produzione — **non si risolve con una
configurazione**. L'unica via resta quella che abbiamo già scelto: **correggere la grafia nel
testo dello script**, con `lessico-pronuncia.md`, prima di generare. Ora però lo sappiamo su una
prova, non per esclusione.

*(Dettaglio utile: la mappa è **case-sensitive**.)*

**c) Il 10% della musica era giusto, e ora è verificato.**

`fliki-avanzato.md` §3 prescriveva «volume musica al 10-15%». Era una prescrizione senza fonte;
adesso ha una schermata: il pannello Fliki mostra **Volume 10%** nell'esempio del docente. Non
cambia nulla di operativo (la musica non passa dal nostro payload), ma **una scheda che aveva
ragione per caso ora ha ragione per prova**.

**d) Un dato di capacità che non avevamo: i minuti si possono negoziare.**

Se il piano non basta, si chiede un'estensione su misura all'assistenza. Non serve oggi, ma è
un'informazione di **capacità produttiva** da tenere: il tetto dei minuti è il vincolo fisico
della nostra fabbrica, e non è del tutto rigido.

**Quello che NON prendo:** il voice cloning (funziona bene solo in inglese, e i nostri canali sono
italiani — se ne riparla se e quando cambierà), e il caricamento manuale di clip proprie, che
richiede l'interfaccia.

## 4. Conflitti col nostro modo di fare

**Nessun conflitto.** Un solo contrasto, ed è **interno alla lezione stessa**: il parlato dice che
la mappa delle pronunce è permanente, lo schermo dice che vale per un video solo. Arbitrato in
tre parole: **schermo batte parlato** (piano §6.4). Nessuna voce nuova in `CONFLITTI.md` — non è
un conflitto fra il corso e noi, è un errore del corso su sé stesso.

## 5. Regole estratte

Quattro, nel registro: `regole/A4-metodo-ai-tube/L19_perfezionare_fliki.py`.

| id | regola in una riga | tocca | binario |
|---|---|---|---|
| `A4-L19-01` | **Ogni canale che pubblica video generati con Fliki ha il suo ID registrato nel profilo Fliki**, ed è una compilazione a mano da fare una volta e verificare | `fliki-produzione.md` | **A** |
| `A4-L19-02` | La **mappa delle pronunce di Fliki vale per un video solo**: non è una configurazione ereditabile e l'API non la vede. Le pronunce si correggono **nel testo** | `lessico-pronuncia.md` | **A** |
| `A4-L19-03` | Il volume della musica in Fliki è **una percentuale**, e il riferimento visto a schermo è **10%** | `fliki-avanzato.md` | **A** |
| `A4-L19-04` | I minuti del piano sono **un plafond mensile** e si può **chiedere un piano su misura**: il tetto dei minuti è un vincolo di capacità, non una legge | `fliki-produzione.md` | **A** |

## 6. Applicabilità alla nostra fabbrica

- **Tutte e quattro applicate subito** (binario A): schede, nessuna riga di motore.
- **`A4-L19-01` porta con sé un'azione manuale che il codice non può fare al posto nostro**:
  aprire `fliki.ai → Profile`, incollare gli ID dei due canali, salvare. **Assegnata al gate A4**
  insieme alle altre due verifiche già aperte (musica, tempo per video). Finché non è fatta, la
  regola resta scritta e non eseguita — **e va detto**, invece di darla per applicata perché è
  documentata.
- **`A4-L19-02` chiude un debito dichiarandolo non chiudibile per quella via**: è un risultato,
  non un fallimento. Sapere che una strada non esiste vale quanto trovarne una.

**Valore netto della lezione: il più alto dello studio finora, in rapporto alla durata.** Undici
minuti, quattro schermate guardate, e ne escono: un'azione concreta di protezione dei canali mai
eseguita, la chiusura definitiva di una questione aperta da due lezioni, una prescrizione nostra
finalmente verificata, e un dato di capacità produttiva. **Nessuna di queste quattro cose sarebbe
uscita dal parlato da solo.**
