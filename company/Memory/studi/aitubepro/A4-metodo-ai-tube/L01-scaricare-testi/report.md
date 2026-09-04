# Report — A4/L01 · «Scaricare testi già pronti per generare video in 3 click»

> Le sei voci obbligatorie del piano (§6.2). Gli appunti integrali stanno in `appunti.md`,
> le schermate in `frame-scelti.md`; qui c'è **solo** quanto vale per Digital Empire.

---

## 1. Cosa insegna

Come procurarsi la **materia prima testuale** di un video senza scriverla: si prende il video
di un canale concorrente, se ne scarica la trascrizione automatica di YouTube con un servizio
gratuito (DownSub, riserva SaveSubs), e la si porta nel piano editoriale insieme al link della
fonte.

Tre passaggi che la lezione mostra e che vanno tenuti distinti, perché hanno valore diverso:

1. **La scelta della sorgente si fa sul VPH** — visualizzazioni orarie, lette con vidIQ. Non sul
   titolo, non sul gusto.
2. **L'estrazione del testo** — DownSub, con la coda velenosa della **traduzione automatica in
   decine di lingue**: lo stesso video sorgente può alimentare un canale in un'altra lingua.
3. **L'arricchimento con una seconda fonte** — quando il video sorgente è corto, si cerca il tema
   su Google, si apre un articolo di testata, e **si salva il link nella colonna NOTE del piano
   editoriale**. Il pacchetto di lavoro non è il transcript: è transcript + fonti.

Il primo passaggio noi lo facciamo già meglio. Il secondo lo facciamo già meglio. **Il terzo non
lo facciamo affatto**, ed è quello che vale.

## 2. Cosa facciamo oggi (verificato sul disco, non ricordato)

| Pezzo | Dove | Stato reale |
|---|---|---|
| Scelta sorgente per VPH | `02-AUTOMAZIONI-E-SCRIPTS/build_candidate_pool.py:125-138` | **c'è**: calcola `views / età` e ordina per VPH decrescente. `MIN_VPH=20.0` di `cashcow_check.py` è dichiarato **non applicabile** a questa nicchia (top reale ~10-11 vph) — annotato nel codice, non nascosto |
| Scarico transcript | `03-AGENTI-E-RUOLI/operatori/transcript-collector.md` + `apex7_orchestrator.py:394` | **c'è, ed è superiore alla lezione**: `yt-dlp --write-auto-sub --sub-lang it,en`, pulizia `.vtt`, file conservati in `transcripts/` come prova di provenienza. Automatico, senza aprire un browser |
| Pacchetto per chi scrive | `apex7_orchestrator.py:1189-1214` (`<videoId>.DA-SCRIVERE.md`) | **c'è**: titolo sorgente, URL, punteggio SEO, debolezze, durata obbligatoria, struttura HOOK/INTRO/CORPO/CTA, obbligo di riscrittura, schemi di copy misurati, **e il transcript integrale** |
| Controllo che non sia una copia | `02-AUTOMAZIONI-E-SCRIPTS/regolatori.py:153` (`verifica_originalita`) | **c'è**: confronto a n-grammi script↔transcript, blocca se trova sequenze identiche; dichiara da sé il proprio punto cieco (lingue diverse ⇒ sovrapposizione zero che non prova nulla) |
| **Seconda fonte / arricchimento** | — | **NON ESISTE.** `grep` su `script-writer.md` per `fonte/fonti/articolo/approfond`: **zero risultati**. Il pacchetto di lavoro contiene una sola fonte al mondo: il transcript del video copiato |
| **Colonna per le fonti nel piano** | `assemble_piano_editoriale.py:654` | **NON ESISTE.** 13 colonne (`giorno, data_pubblicazione, orario_pubblicazione, strategia, canale_sorgente, url_sorgente_reale, titolo_originale, vph_sorgente, titolo_adattato, hook_3_secondi, caption_descrizione, hashtag_set, comando_cli`): nessuna per note o materiale di supporto |
| Cosa si fa se il transcript manca | `transcript-collector.md` §Playbook 3 | **ci si ferma e si passa al candidato B.** Nessuna via di riserva |

## 3. Delta

**C'è, ed è un buco strutturale, non un dettaglio.**

La nostra fabbrica chiede a chi scrive **2.220 parole** (`apex7_orchestrator.py:146`,
`PAROLE_MINIME_SCRIPT = 12 × 185`) partendo da un pacchetto che contiene **una sola fonte**: il
transcript del video sorgente. Un video di notizie da 5 minuti ne porta ~700. Nessuno misura
quel divario, e nessuno lo dichiara: il brief scritto dalla macchina dice «servono ~2.000 parole»
e poi allega quello che c'è, senza contare le parole né avvisare che non bastano.

Chi scrive si trova davanti a un ordine impossibile e ha tre strade: allungare con aria, ripetere,
o **inventare**. Nessuna delle tre è accettabile su un video di cronaca, dove le informazioni
false hanno un nome e un cognome dentro.

La lezione — che è un corso base del 2023 — questo problema lo ha visto e lo ha risolto con la
cosa più ovvia del mondo: **se il video è corto, vai a prendere l'articolo di giornale**. Noi, che
abbiamo regolatori, gate e n-grammi, quella riga non ce l'abbiamo.

Secondo pezzo del delta, più piccolo: quando i sottotitoli non escono **noi ci fermiamo**. La
lezione mostra che esistono altre strade (SaveSubs e simili). Per noi non è un sostituto di
yt-dlp — yt-dlp è meglio — ma è la differenza fra «candidato scartato» e «candidato recuperato»
in un caso su cui oggi non proviamo nemmeno.

**Quello che NON prendo da questa lezione:** il metodo di scelta della sorgente (già nostro e
automatico), DownSub e SaveSubs come strumenti (yt-dlp li batte: nessun browser, nessun sito di
terzi, nessuna pubblicità, provenienza tracciata), e l'idea che la traduzione automatica basti ad
aprire un canale in un'altra lingua — è vera come possibilità, ma è una decisione di strategia
multicanale che non si prende dentro una lezione di scaricamento testi.

## 4. Conflitti col nostro modo di fare

**Uno, ed è di sostanza, non di metodo.**

La lezione insegna a pubblicare partendo dal transcript di un altro canale e in **7 minuti e 25
non pronuncia mai la parola «riscrivere»**. La riscrittura è rimandata alla lezione successiva:
chi guarda solo questa esce convinto che il lavoro sia prendere il testo e usarlo.

Il nostro `regolatore-originalita` blocca esattamente quel comportamento, e il brief della
fabbrica lo scrive a chiare lettere: *«Va RISCRITTO, non copiato: stesso argomento e stesse
informazioni reali, parole proprie»*. **Il conflitto si risolve a favore nostro senza discussione**
— e la seconda fonte, che è la cosa che prendiamo da qui, va nella stessa direzione: più materiale
proprio, meno dipendenza dal testo copiato.

Difetto minore trovato per strada, da annotare: il brief scritto dalla macchina dice «servono
~2.000 parole», il codice ne pretende **2.220** (`PAROLE_MINIME_SCRIPT`). Due numeri diversi per
lo stesso vincolo, nello stesso file. Va allineato al gate di categoria, insieme a **D-1**
(`DURATA_MASSIMA_S=600` contro 2.220 parole ≈ 720 s) che è già aperto in `BASELINE.md`.

## 5. Regole estratte

Quattro, nel registro: `regole/A4-metodo-ai-tube/L01_scaricare_testi.py`.

| id | regola in una riga | tocca | binario |
|---|---|---|---|
| `A4-L01-01` | Il pacchetto `DA-SCRIVERE` deve **contare le parole** del transcript e, se sotto la soglia, pretendere **≥2 fonti testuali esterne** con link e data | `transcript-collector.md` | **A** |
| `A4-L01-02` | Quando i sottotitoli automatici non escono, prima di scartare il candidato si prova **la via di riserva** (servizi terzi tipo SaveSubs) e, se fallisce anche quella, si dichiara il motivo | `transcript-collector.md` | **A** |
| `A4-L01-03` | Il piano editoriale deve avere una colonna **`fonti_extra`**: il materiale di supporto senza un posto dove stare non esiste | `assemble_piano_editoriale.py` | **B** |
| `A4-L01-04` | Lo stesso video sorgente può alimentare **un canale in un'altra lingua**: è una leva di scala da valutare in sede di strategia, non un'automazione da accendere | `capi/capo-strategia.md` | **A** |

## 6. Applicabilità alla nostra fabbrica

- **A4-L01-01 e A4-L01-02 applicate subito** (binario A): riguardano un agente, non il motore in
  produzione. `transcript-collector.md` cambia da «raccogli il transcript» a «raccogli e
  **dichiara se basta**».
- **A4-L01-03 registrata e NON applicata**: tocca `assemble_piano_editoriale.py`, che è motore in
  produzione. Entra al gate della categoria A4, con test verdi e un video di prova (ADR-024,
  doppio binario). Applicarla oggi vorrebbe dire cambiare lo schema del piano mentre la fabbrica
  ci sta pubblicando sopra.
- **A4-L01-04 applicata come nota di strategia**, non come automazione: `capo-strategia` deve
  sapere che la leva esiste; accenderla è una decisione di Max, non di una lezione.

**Valore netto della lezione:** una lezione base, vecchia di due anni e mezzo, su strumenti che
noi abbiamo già superati — che però contiene **la sola riga di questo studio che tappa un buco
capace di far scrivere il falso** ai nostri video. Il valore non stava dove il titolo prometteva.
