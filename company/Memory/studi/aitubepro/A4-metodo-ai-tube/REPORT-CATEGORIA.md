# REPORT DI CATEGORIA — A4 «Metodo AI Tube»

- **Lezioni:** 21 su 21 · **parlato letto:** ~8 ore, integrale
- **Aperta:** 2026-09-04 · **chiusa:** 2026-09-06
- **Regole prodotte:** **62** (59 binario A · 3 binario B, tutte applicate)
- **Arbitrati:** 7 (`C-001` → `C-007`)
- **Frame estratti e letti:** solo su L00-L05, L19 (le lezioni di metodo). Sulle sette lezioni di
  editor manuali e sulle tre di strumenti a click: **zero frame, dichiarato** (piano §10)

> Sesta voce del contratto di report, applicata alla categoria intera. Le sei voci sono le stesse
> di ogni lezione: cosa insegna · cosa facciamo oggi · delta · conflitti · regole · applicabilità.
> La conoscenza organizzata per argomento sta in [`APPUNTI-CATEGORIA.md`](APPUNTI-CATEGORIA.md).

---

## 1. Cosa insegna la categoria

Il metodo completo di AI TUBE PRO: dagli strumenti (L00) alla generazione del testo (L01-L02),
alla voce (L03), al montaggio automatico (L04-L05), fino a Fliki in profondità (L19, L20). In
mezzo, **nove lezioni** che insegnano un mestiere diverso — rifare i video degli altri (L06-L14,
L16) — e **tre** su strumenti che vivono solo dentro un browser (L15, L17, e in parte L13).

**La divisione che il corso non dichiara mai** è la chiave per leggerlo: metà insegna a
**produrre**, metà a **riprodurre**. Solo la prima metà ci riguarda, e va detto senza girarci
intorno perché è la ragione per cui sette lezioni sono state chiuse in **BRONZO dichiarato**.

## 2. Cosa facevamo, prima

La fabbrica generava via API con un payload che nessuno aveva mai messo in discussione: voce
ri-risolta a ogni generazione, formato `"16:9"` scritto a mano, nessun campo musica, e un gate di
qualità che controllava **il volume di una musica inesistente**. Le schede di riferimento erano
scritte per il montaggio a mano dentro Fliki — cioè per un flusso che la nostra catena **non
esegue**. Nessun criterio scritto per scegliere uno strumento. Nessuna riga su come inizia o come
finisce uno script.

## 3. Delta — cosa è cambiato davvero

**Nel motore (binario B, applicato al gate):**

| prima | dopo |
|---|---|
| la voce si ri-risolveva a ogni generazione: se Fliki cambiava l'ordine del suo elenco, il canale cambiava voce da solo | **`voice_id` fisso per canale**, con l'`_id` reale letto dall'API |
| `aspectRatio` costante `"16:9"`: **Shorts impossibili**, e nessun documento diceva perché | formato **dichiarato dal canale** o da `--formato`, tre valori ammessi, default invariato |
| il piano editoriale non aveva un posto per le fonti di supporto | colonna **`fonti_extra`** |

**Negli agenti e nelle schede (binario A, 59 regole):** cinque criteri di scelta strumenti dove
non ce n'era nessuno · l'apertura come leva di ritenzione e la CTA di chiusura in `script-writer` ·
la sorveglianza settimanale col cronometro in `self-improver` · le due domande di liceità e
riproducibilità in `niche-scout` · intro/outro, sincronia e formato in `video-producer` · sette
miti, tre porte chiuse e la mappa delle vie della musica in `monetizzazione-compliance` · la
soglia contro l'ideale in `qa-audio-video`.

**Nei numeri della baseline** (riletta al gate, `../BASELINE.md`):

| metrica | prima | dopo |
|---|---|---|
| test della fabbrica | 11/11 | **16/16** |
| agenti con almeno una soglia numerica | 12/34 (35%) | **19/34 (56%)** |
| schede di riferimento | 8 | **9** |
| regole a registro | 0 | **62**, tutte con prova, **tutte applicate** |

**⭐ Il risultato singolo più utile** non è una novità imparata, è **una verifica chiusa**: i nostri
video **non hanno musica**, accertato incrociando due fatti indipendenti (in Fliki la musica non è
automatica · nel payload non esiste un campo musica). Il criterio «Bilanciamento Volumi» del gate
bloccante non era *sospeso*: era **inapplicabile**, e lo era da mesi.

## 4. Conflitti

**Sette arbitrati**, e i quattro che contano dicono qualcosa **sulla fonte**, non su una lezione:
il corso si contraddice sulla freschezza del video sorgente (`C-005`), sul tempo che costa il suo
metodo (`C-006`, **fattore 12×**), sulla proprietà della musica generata (`C-007`, **dentro una
lezione sola**), e in piccolo perfino nel titolo di L12.

**La regola generale che ne è nata** è probabilmente il lascito più duraturo della categoria:
*l'apertura dice quello che vende, il dettaglio dice quello che sa — e quando c'è di mezzo una
licenza, non si crede a nessuno dei due: si leggono i termini del fornitore.*

## 5. Regole — la mappa

**62 regole**, così distribuite:

| | | | |
|---|---|---|---|
| **binario** | A = 59 | B = 3 | tutte applicate |
| **rischio** | alto = 26 | medio = 16 | basso = 20 |
| **azione** | nuovo = 27 | modifica = 31 | conferma = 4 |
| **tipo** | vincolo = 25 | procedura = 13 | euristica = 12 · parametro = 8 · strumento = 4 |
| **fonte** | parlato = 44 | schermo = 7 | entrambi = 11 |

**Il dato che va guardato è `rischio alto = 26 su 62`:** quasi metà delle regole di questa
categoria sono **divieti**. Non è un caso e non è un giudizio morale: è la conseguenza del fatto
che metà del corso insegna a lavorare su materiale altrui. Una categoria che produce più divieti
che procedure sta dicendo qualcosa sul materiale da cui è stata ricavata.

**`fonte = schermo` o `entrambi` in 18 casi su 62:** le regole nate da un frame sono state le
migliori (il campo `YouTube channel ID(s)`, la mappa pronunce «for this video», la tendina dei
formati). **Lo schermo batte il parlato** (piano §6.4) non è una regola formale: è ciò che è
successo.

## 6. Applicabilità e stato del gate

### Il gate di categoria — 7 condizioni (piano §9)

| # | condizione | esito |
|---|---|---|
| 1 | `REPORT-CATEGORIA.md` + `APPUNTI-CATEGORIA.md` | ✅ questo file e il suo gemello |
| 2 | ogni lezione a `completata`, nessun «quasi» | ✅ **21 su 21** (verificato su `stato.json`) |
| 3 | `registro.py --verifica` pulito | ✅ **62 regole, tutte a norma, zero senza prova** |
| 4 | regole di binario B applicate, test verdi, **video di prova** | ⚠️ **parziale** — le 3 regole sono applicate e i test sono **16/16 verdi** (5 nuovi, a secco), ma **il video di prova non è stato generato**: costa minuti di piano e va deciso da Max |
| 5 | baseline riletta col delta in chiaro | ✅ `../BASELINE.md`, sezione «Rilettura al gate A4» |
| 6 | verifica a campione indipendente | ⏳ affidata a uno scagnozzo — esito in `VERIFICA-GATE-A4.md` |
| 7 | checkpoint + commit + push | ⏳ ultimo passo |

**Sul punto 4, senza addolcirlo:** la prova a secco dimostra che il payload si assembla come deve
(voce fissa di entrambi i canali, default 16:9 invariato, 9:16 accettato, 4:3 respinto) e i cinque
test nuovi la proteggono da regressioni. **Non dimostra che Fliki restituisca un MP4 verticale
valido.** Quella prova costa minuti di piano e va fatta quando serve un video vero, non per il
gusto di spuntare una casella.

### Cosa resta aperto, dichiarato

- **il tempo per video** non è misurato (`A4-L05-04`);
- **il campo `YouTube channel ID(s)`** va compilato a mano sui due canali (`A4-L19-01`): gratis,
  cinque minuti, mai fatto;
- **tre verifiche contro il payload** da L20 (SFX via API · timing per-media · tetto di 50 scene);
- **D-1 e D-2** restano aperti di proposito fino al gate di **A6**.

---

## Giudizio finale sulla categoria

**A4 non è una categoria fallita: è la categoria che ha pagato lo studio.** 62 regole tutte
applicate, tre correzioni al motore, un gate bloccante rimesso in sesto e cinque difetti nostri
trovati guardando i difetti degli altri.

**E va detta anche la parte scomoda:** metà del materiale non serviva, sette lezioni sono state
declassate dichiarandolo, e il valore più alto non è arrivato dal contenuto delle lezioni ma **dal
metodo** — leggerle tutte, in ordine, tenendo un registro. I sette miti esistono perché sette
lezioni sono state lette di fila; i quattro arbitrati esistono perché qualcuno ha messo accanto
due numeri che il corso teneva a nove lezioni di distanza.

**Prossima categoria: A6 «Viral Mastery» (10 lezioni)**, dove si chiudono anche D-1 e D-2.
