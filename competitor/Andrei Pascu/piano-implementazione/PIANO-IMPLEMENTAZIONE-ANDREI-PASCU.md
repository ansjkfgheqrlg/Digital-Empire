# PIANO DI IMPLEMENTAZIONE — ANDREI PASCU

**Stato:** DOCUMENTO FINALE (P3). Chiuso da Emperator il 2026-09-10.
**Codice ripresa:** `EMP-APPLAN1`.

**Come è nato:** il piano è stato criticato tre volte, e ogni giro ha attaccato il giro prima, mai
l'originale. **P0** — 2 Doom Bot (opus) hanno scritto i due draft. **P1** — 3 Sentinelle indipendenti
li hanno demoliti (governo/coerenza/collisione; denaro e verità, due volte, senza sapere l'una
dell'altra). **P2** — Fable ha attaccato le critiche e ha detto quali colpi reggono e quali crollano.
**Assemblaggio** — uno Scagnozzo ha fuso i sei documenti senza decidere nulla. **P3** — le decisioni
qui sotto sono mie, Emperator, non delegate.

**La missione, in una riga:** trasformare lo studio Andrei Pascu in un piano che **fa incassare
Digital Empire**, non in altra documentazione. Il giudizio su questo documento è uno solo: se fra
un mese non è entrato un euro e il documento è ancora bello, è fallito (ADR-016, ULTIMO METRO).

**Fonti (tutte su disco, in questa cartella):** `DRAFT-V1-A-lanci.md` · `DRAFT-V1-B-capacita.md` ·
`P1-CRITICA-S1-governo.md` · `P1-CRITICA-S2-denaro.md` · `P1-CRITICA-sentinella-verita.md` ·
`P2-FABLE-critica-della-critica.md` · `ASSEMBLAGGIO-V2.md`.

---

## 1. La pagina che conta

Se leggi solo questa pagina, hai il piano. **Le altre 34 azioni vengono dopo queste cinque, non
prima** — e la ragione è un fatto verificato sul disco, non un'opinione: Digital Empire possiede
già il codice per incassare, e non l'ha mai acceso.

`empire/tools/checkout.py` (13.819 byte, scritto il 25/07) legge
`Crea siti/Siti CCM/checkout.config.json`, dove il prezzo del Manuale è **già impostato a 67 €
di lancio / 97 di listino / 27 di bump**. Quattro rail di pagamento sono previsti e **tutti spenti**,
tranne l'ordine via email. Il campo del primo dice, testuale: `"richiede": "MAX: crea Payment Link
su Stripe"`. E `KDP - prodottti digitali/Leanding Page/email-agent/main.py` è un webhook FastAPI
funzionante che verifica la firma Stripe e consegna il PDF via Gmail, già usato per un altro ebook.

Manca un gesto da dieci minuti, non una build da quaranta ore.

| # | Azione | Chi | Costo | Quale euro sblocca | Blocca esattamente |
|---|---|---|---|---|---|
| **1** | Aprire il **Payment Link Stripe** del Manuale a 67 € (e quello del bump a 27) e incollare i due URL | **Solo Max** | 10 min | **Il primo euro dell'Impero.** Senza questo non esiste una cassa | Le azioni 2 e 3 di questa tabella. Nient'altro nel piano |
| **2** | Accendere il rail: URL nel `checkout.config.json`, `"attivo": true`, e spostare `scadenza_lancio` — oggi è **31/07/2026, già scaduta** | Una sessione | 15 min | Rende la cassa raggiungibile da una pagina | L'azione 3 |
| **3** | Adattare `email-agent/main.py` (81 righe, già vive) alla consegna del Manuale: prodotto, PDF, testo dell'email | Una sessione | 2-3h | Consegna automatica dopo il pagamento: chiude il ciclo euro→prodotto | Niente. Fino ad allora si consegna a mano |
| **4** | **Ruotare la chiave Brevo** esposta in chiaro sul repo (B-020, da mesi, marcata rossa) | **Solo Max** | 10 min | Nessuno. Non è un incasso, è un rischio aperto | Niente del piano. È urgente da solo (ADR-028) |
| **5** | **Contare il pubblico vero**: quante persone verificate vedranno la pagina il giorno 1, e da quale canale (il canale previsto è spento dal 29/07) | Emperator + Max | 1h | Nessuno — ma decide se gli altri quattro valgono qualcosa | **La data del lancio, non la costruzione.** Con pubblico zero si costruisce pubblico prima, come impone `04-COSTRUZIONE.md` riga 251 |

**Perché `catena.py` non è più il rango 1.** Era la prima azione del Draft A. La Sentinella 1 ha
verificato riga per riga che `GATE-FNL-1` in `dati/registro.yaml` **non nomina né lo script né gli
otto controlli di ADR-024**: costruirlo così produce un pezzo che nessun gate invoca — lo stesso
difetto che il piano rimprovera al concorrente. Scende sotto queste cinque, e quando si farà si
farà **nella versione minima** (2-4h, il controllo 8 più i due banali) **e nello stesso commit
della riga che lo collega al gate**. Mai separati.

---

## 2. Cosa cambia davvero in Digital Empire

Dieci righe. Sono la sostanza di tutto lo studio guardato insieme, non lezione per lezione.

1. **Non si scrivono pagine nuove per lanciare: si specchia e si rilancia.** È il vantaggio vero di
   Andrei — non un funnel più pulito, ma il costo di produzione vicino a zero
   (`SINTESI-METODO.md` §3). Applicato al nostro magazzino vuol dire una cosa sola: i **25 pezzi
   finiti e mai usciti** (il più vecchio da oltre 142 giorni) sono materiale di lancio, non archivio.
2. **Prima si accende ciò che esiste, poi si costruisce.** ADR-003 (wrap, mai riscrittura) vale
   anche per il denaro: `checkout.py` ed `email-agent` erano già lì mentre scrivevamo 1.352 righe
   di specifica.
3. **Nessuna azione è fatta finché non nomina chi la consuma.** Regola della Sentinella 1,
   promossa qui a legge del piano: uno script senza un gate che lo invochi è un pezzo per ULTIMO METRO.
4. **Nessun numero senza fonte.** Tre cifre del piano erano inventate (150 €, 100 €, «massimo 3
   rami»); una quarta, 400, era vera ma sostituiva silenziosamente 349. Da qui in poi ogni cifra o
   porta la fonte o porta la marca STIMA.
5. **Il prezzo del Manuale era già deciso e nessuno lo sapeva.** `DEC-EST-001`, attiva dal 21/07 per
   silenzio-assenso: 67/97. Quattro documenti hanno discusso fasce di prezzo alternative per settimane.
   Una decisione presa e dimenticata costa quanto una decisione mai presa.
6. **Un impedimento ferma solo se stesso** (ADR-028). Per questo ogni azione porta la colonna
   «blocca esattamente», e per questo i due gesti di Max non fermano le altre 32 azioni.
7. **Le tre critiche non concordavano, e va bene così.** Due Sentinelle sullo stesso angolo, che non
   si conoscevano, hanno prodotto conteggi e classificazioni diverse: è la prova che una critica
   sola non basta, non che il metodo sia rotto.
8. **La disciplina si aggiunge dove passa il denaro, non ovunque.** Su 34 azioni, zero producevano un
   euro diretto e l'82% era governo o documento. La proporzione si inverte: prima la cassa, poi le
   griglie.
9. **Il gate si chiude collegandolo, non costruendolo.** Vale per `catena.py` e per ogni controllo
   futuro: il commit che crea lo strumento contiene anche la riga che lo rende obbligatorio.
10. **Il piano stesso è soggetto al proprio esame.** Se fra un mese è ancora un bel documento senza
    un euro dietro, è il pezzo 26 di ULTIMO METRO — e va detto, non nascosto.

---

## 2-bis. Le decisioni di P3 — le sei contraddizioni sciolte

L'assemblaggio ha lasciato aperte sei divergenze fra le fonti, come doveva. Le chiudo io, qui, una
per una. Da adesso valgono queste, e le versioni perdenti non si ridiscutono.

| # | La divergenza | **DECISIONE** | Perché |
|---|---|---|---|
| **D1** | Quante azioni sono: 33 (Sentinella-verità) o 34 (S2 e assemblaggio) | **34, contate per ID distinto** — i tre suffissi `b` contano tre | Un ID è un'unità di lavoro assegnabile. Raggrupparli nasconde lavoro |
| **D2** | Classe di AP-046b e AP-047b: INFRASTRUTTURA (S2) o ABILITA UN EURO (Verità) | **ABILITA UN EURO** | Scomporre il prezzo in pagina e legare ogni prova a una fonte agiscono sulla pagina che incassa, non sull'apparato. Vince la Verità |
| **D3** | Prezzo del Manuale: fascia 27-47 € dei draft, o altro | **67 lancio / 97 listino / 27 bump** — `DEC-EST-001`, già viva nel `checkout.config.json` | Non è una scelta, è una decisione già presa e mai eseguita. La fascia 27-47 veniva da un piano `_v3-superata`, cioè demolito. **Muore qui** |
| **D4** | Scala prezzi: 98→434→999 (già in esecuzione da Gael) o 98→400→999 | **98 → 400 → 999**, e la soglia «prova sociale con faccia e nome» resta **349** | 400 e 349 sono punti misurati; 434 e 150 non coincidono con nessuna fonte. **Da correggere nella TASK-GAEL-20260908, righe 144-146, prima che diventi codice** |
| **D5** | Corsia di AP-038: C1 secca come dichiarata, o altro | **C2 (cartella) + C1 (contenuto)**, identico ad AP-037 | Scrive dentro il perimetro riservato a Gael. Due azioni sulla stessa cartella non possono avere due regole |
| **D6** | Campo di AP-041: riusare `soglia_rapporto_minima` o crearne uno | **Campo nuovo: `soglia_fonti_esterne_minima`** | Il campo esistente ha già un'altra semantica (valore/prezzo per `GATE-OFF-1`). Stesso nome, due significati, è il guasto che si paga fra sei mesi |

**Settima decisione, non una divergenza ma un ordine:** `AP-034` (`catena.py`) **scende dal rango 1**
e si esegue solo in versione minima e solo insieme alla riga che la collega a `GATE-FNL-1`.

---

## 3. Le azioni — tabella unica

**Nota di conteggio, non risolta qui (⚖️ DA DECIDERE IN P3):** contando le azioni per ID distinto
(compresi i tre suffissi `b`) risultano **34 ID** in tutto (29 di Draft A + 5 di Draft B: AP-006,
AP-012, AP-018, AP-019, AP-020). **P1-S2** conta **34** azioni-riga raggruppando AP-046b/047b/048b
in un'unica riga e sommando 7 righe eseguibili di Draft B. **P1-Sentinella-verità** conta **33**
azioni, classificando AP-046b e AP-047b come righe separate dentro la casella ABILITA UN EURO
(diverso sia dal conteggio sia dalla classe di S2, che li mette insieme sotto INFRASTRUTTURA). Le
due letture sono riportate integralmente nella tabella sotto, alla riga di ciascuna azione toccata,
e non decise.

Legenda **Stato dopo P1/P2**: REGGE = colpo confermato da Fable (P2) · CROLLA = colpo respinto da
Fable, azione torna viva · PARZIALE = in parte regge in parte crolla, entrambe le note · N/E = non
esaminato in P2, resta come dichiarato in P1 · ⚖️ = contraddizione fra fonti 4 (S2) e 5 (Verità),
da decidere in P3.

| ID | Azione | Corsia | Classe | Effort | Blocca esattamente | Stato dopo P1/P2 |
|---|---|---|---|---|---|---|
| **AP-004** | Ancoraggio tripwire: Manuale (fascia proposta 27-47€) → Mastery (397€), due lanci incatenati, zero amendment | C2 | ABILITA UN EURO (S2) | T1 (3 campi testo) + T4 (firma prezzo) | «Non blocca niente» (Draft A §3.4). Il valore prezzo resta `PU-PREZZO`, 14gg, nessun default | Colpo S2-2 **REGGE**: fascia «27-47€» dichiarata senza fonte citata nel testo dell'azione. Precisazione Fable: la fonte esiste — `_v3-superata/04-WF-OFFERTA.md:146-169`, un documento **dichiarato superato** — quindi non inventata dal nulla ma pescata da un piano demolito senza dirlo (Fable: «peggio, ma è un'altra accusa»). Colpo S2-1(c) **PARZIALE**: Fable corregge che «nessuna azione tocca i 5 gesti umani» è falso alla lettera — AP-004 §3.5 porta attivamente `PU-RUOLO`/`PU-PREZZO` a Max lo stesso giorno. ⚖️ **DA DECIDERE IN P3**: esiste una sesta cifra di prezzo mai riconciliata dai due draft — DEC-EST-001 (67€ lancio / 97€ listino, firmata 2026-07-21 per silenzio-assenso, già live in `Crea siti/Siti CCM/checkout.config.json`, con `scadenza_lancio: 2026-07-31` **scaduta** — trovato da Sentinella-verità e confermato da Fable §3.C) |
| **AP-005** | Ads dinamiche a countdown (variabile `[GIORNI_RIMANENTI]`) + 3 versioni sequenziali della pagina di vendita, con riparazione del gate sulla v3 mai riverificata | C2 | ABILITA UN EURO, ma il draft stesso dichiara «prima della firma [data_apertura] è aria» (rango 9, §8) | T2 | «Nulla oggi. Se `catena.py` non esiste al momento di S3, la riga di calendario si scrive lo stesso con `stato: da-fare` e la verifica è manuale» (Draft A §3.7) | N/E — nessuna delle tre critiche la attacca direttamente |
| **AP-006** | Automazione AI preventivi (cs2online Bonus 6) — **verdetto principale NO-GO sull'automazione**, va in Sezione 6. Due patch GO separate, vedi righe sotto | — | — | — | — | vedi AP-006 patch A/B sotto |
| ↳ **AP-006 patch A** (= converge con **AP-020a**) | Contratto d'ingresso obbligatorio in `beast-preventivi/SKILL.md`: rifiuto categorico di produrre il documento se mancano brief/prezzo/problema-cliente | C1 (fuori perimetro LANCI, nessuna collisione dichiarata) | INFRASTRUTTURA (S2) | ~30 min | Non dichiarato nel formato ADR-028 dal draft (che usa «condizione di riapertura» invece di «blocca») — **DA DECIDERE IN P3** | Colpo S2 (declassamento implicito per throughput ≈0/mese) **CROLLA** — Fable §2.3 la salva esplicitamente: «il throughput zero è l'argomento giusto contro l'automazione... non contro le ~30 righe di contratto d'ingresso... non è ULTIMO METRO, è la ruota di scorta» |
| ↳ **AP-006 patch B** | Chiusura tensione breakdown-prezzi: il breakdown non entra mai nel documento scritto, può uscire a voce in call dopo il silenzio post-prezzo | C1 | DOCUMENTO | ~30 min | Non dichiarato — **DA DECIDERE IN P3** | N/E. Nota dell'autore stesso (Draft B §10 pt.4): è una decisione di Max presa da Doom Bot B invocando ADR-026/028, dichiarata esplicitamente «ribaltabile in dieci secondi» |
| **AP-008** | Checklist 7 fattori diagnostici fra gli step → campo obbligatorio `transizioni[]` in `funnel.schema.json`, estensione `GATE-FNL-1.criterio_eseguibile`, test rosso nuovo | C2 | INFRASTRUTTURA | T3 | «Blocca solo `GATE-FNL-1`, e solo dopo che lo schema è modificato... Non è una precondizione di nessuna micro-task di `TASK-LANCI-BUILD-W3`» (Draft A §3.10) | Colpo S1-4 **PARZIALE**: metà su ADR-024 REGGE (titolo dice «quattro controlli», corpo ne elenca otto — fonte: `ADR-024-canone-v2-primo-strato.md` righe 101-144/167, **non** `ADR-024-canone-v2-onde-a-b.md` come S1 l'aveva citata per errore); metà «falso allarme» **NON regge intera** — il rosso di AP-008 è davvero assegnato a `MT-4GNU` dalla riga CHI del draft, e il gate di chiusura di quella micro-task è un conteggio letterale «sei su sei» — eseguito alla lettera il conteggio salta davvero. **Salvataggio Fable §2.1**: non si toglie la nota §3.11 (come S1 chiedeva), si corregge la riga CHI/QUANDO assegnando il rosso a `MT-GEKH`/S3, non a `MT-4GNU` — a quel punto la nota diventa un commento di una riga, non un problema |
| **AP-012** (Draft B) | Ramificazione comportamentale email: convenzione nome tag, regola di esistenza, 3 ramificazioni canoniche, riuso soglia MQL di `revops`, freno anti-personalizzazione | C1 (fuori perimetro LANCI; unico rischio dichiarato: 6 righe in `emails/SKILL.md`, basso) | DOCUMENTO (S2: «nessuna campagna email attiva lo consuma oggi») | 1,5-2h | Non dichiarato — **DA DECIDERE IN P3** | Colpo S2-2 **REGGE**: «massimo 3 rami per sequenza» attribuito a KA-07, ma KA-07 nella fonte (`lezione-15/lesson-analysis.md` riga 29) contiene solo un avvertimento qualitativo, **nessun numero** — inventato, e Draft B non lo marca con il proprio simbolo `➕` per le aggiunte fuori fonte come fa altrove. Nota di fusione S1 (non riesaminata da P2, N/E): da cross-linkare con AP-059 (vocabolario leve LANCI di Draft A) — due vocabolari nascenti nello stesso ecosistema, mai dichiarati distinti né uniti |
| ↳ **AP-012 correzione callout** | `revops/SKILL.md` righe 202-206: il callout «non documentato in nessuna skill» è falso — corretto in cross-link onesto verso `emails/references/behavioral-branching.md` | C1 | DOCUMENTO | 10 min | Non dichiarato | N/E |
| **AP-018** | Framework 10 livelli maturità AI come tool d'agenzia — **verdetto NO-GO netto**, va in Sezione 6 | — | — | — | — | — |
| **AP-019** | Budget di sforzo segue il riuso, non la dimensione (content-forge): massimo sforzo su artefatti riusati indefinitamente, dentro un task sullo step che valida | C1 (fuori perimetro LANCI) | DOCUMENTO | 20-30 min | Non dichiarato — **DA DECIDERE IN P3** | N/E dalle tre critiche. Autocritica dell'autore stesso (Draft B §6.2): «il GO più debole», fallisce parzialmente T3 — nessun incidente misurato dietro |
| **AP-020** | Rifiuto se mancano dati obbligatori: patch (a) = converge con AP-006 patch A; patch (b) = validazione a monte in `market-report-pdf/SKILL.md` prima di generare il PDF | (a) C1 · (b) C1 | INFRASTRUTTURA | (a) inclusa in 30 min patch A · (b) 15 min | Non dichiarato — **DA DECIDERE IN P3** | N/E |
| **AP-033** | Nona costante: opzione futura (sconto bloccato su prodotto non ancora a listino), campo opzionale `struttura.opzione_futura`, esclusa dal calcolo `valore_dichiarato` | C2 | ABILITA UN EURO (S2) | T2 (schema) + T1 (righe) | «Il campo è opzionale... Blocca zero. Il nuovo criterio blocca solo l'uso disonesto del campo» (Draft A §3.13) | Colpo S2-2 **REGGE**: valore «100€» dichiarato come «candidato ovvio» senza esserlo — la fonte reale (`ANATOMIA-DEI-LANCI.md` righe 308-312) misura **199€** di sconto su Funnel Operator; il draft non deriva 100€ da quel numero né da alcun calcolo |
| **AP-034** | `catena.py`: gli otto controlli di ADR-024 §4 come script (`.claude/skills/fabbrica-siti/scripts/catena.py`) | C1 | INFRASTRUTTURA | Dichiarato T3 (4-8h) | Dichiarato «Niente. Oggi il controllo 8 non esiste; domani esiste... La sua assenza blocca esattamente una riga: la possibilità di dichiarare VE-1 completo con il controllo 8 incluso» (Draft A) — **CONTESTATO**, vedi colpo S1-1 | Colpo S1-1 **REGGE** (verificato da Fable su `registro.yaml` righe 359-368): `GATE-FNL-1.criterio_eseguibile` non nomina mai `catena.py` né gli otto controlli; nessuna delle 34 azioni propone la riga `AND catena.py exit 0`. La sua etichetta di «rango 1» / «primo gate obbligatorio di LANCI» resta contestata finché quella riga non esiste — S1 chiede di ucciderla, Fable conferma il colpo pieno. Colpo S2-3 **PARZIALE**: stima 4-8h dichiarata insufficiente — S2 ricalcola **18-30h**, Sentinella-verità **8-16h**; Fable non sceglie fra le due ma introduce una terza risposta: la variabile è il **perimetro**, non la stima — una `catena.py` ridotta al solo controllo 8(+3+5) costa **2-4h** e collegherebbe subito il gate mancante del colpo S1-1; la versione completa a 13 controlli (con AP-044) resta nell'ordine 18-30h perché la taratura anti-falsi-positivi sulle 52 pagine (chiesta da Draft A stesso, §10.4) non è mai stata messa nelle ore |
| **AP-035** | Generatore `pre_cassa.py` a sei variabili (nome, prezzo, colore, porzione colorata, codice sconto con finestra, testo bottone), sempre `noindex,nofollow` | C1 | INFRASTRUTTURA | T2 | «Niente. Senza generatore la pre-cassa si scrive a mano dal pattern, come oggi» | N/E diretto. Nota di fusione S1 (non riesaminata in P2): S1 propone di fonderla con AP-041/AP-053/AP-058 in un digest unico per `MT-GEKH`, perché `TASK-GAEL-20260908-SETTIMANA-03` istruisce già Gael a leggere direttamente lo studio — Colpo #5 di S1, non ripreso nella tabella numerata di Fable |
| **AP-036** | Pattern nuovo `cassa-corso-a-livelli`: due card affiancate, checklist quasi identica, nessuno sconto | C1 | INFRASTRUTTURA | T2 | «Niente» | N/E |
| **AP-037** | Cartella condivisa `copy/libreria/` (fuori da `lanci/<id>/`) per frasi riusabili fra lanci | C2 (cartella) + C1 (contenuto) | DOCUMENTO | T2 | «Niente. `ART-CPY` non la richiede» | N/E. Trattamento di corsia preso a modello dal colpo S1-2 (vedi AP-038) |
| **AP-038** | 22 formule retoriche già scritte, travasate in `company/Ecosistemi/15-LANCI/copy/libreria/formule/01..22.md` | Dichiarata **C1** nel draft originale — **CONTESTATA** | DOCUMENTO | T2 | Non dichiarato nella fonte per questa azione specifica — **DA DECIDERE IN P3** | Colpo S1-2 **REGGE** (confermato da Fable, verificato anche `ls company/Ecosistemi/` oggi: nessun `15-LANCI`): il DOVE sta dentro il perimetro che il piano stesso dichiara C2 riservato a Gael («collisione alta»); AP-037, sulla stessa identica cartella, dichiara correttamente C2(cartella)+C1(contenuto), AP-038 no. **Riparazione dichiarata**: eredita lo stesso trattamento di AP-037 — C2(cartella) + C1(contenuto), non C1 secca |
| **AP-039** | Griglia di punteggio `GATE-CPY-1` = le 11 tappe misurate + la 12ª non persuasiva (`chiusura-legale`, presenza/assenza, FAIL se assente) | C2 | INFRASTRUTTURA | T2 | «Nulla di nuovo. `GATE-CPY-1` blocca già. Questa azione gli dà finalmente qualcosa contro cui misurare» | N/E |
| **AP-040** | Campo obbligatorio `concretezza` (`strumento-tecnico`/`percorso`/`mindset`) in `copy.schema.json`, con regola di prova conseguente in `GATE-CPY-1` | C2 | INFRASTRUTTURA | T2 | «`GATE-CPY-1` soltanto, e solo dopo la modifica» | N/E |
| **AP-041** | Scala prova/prezzo: soglia di fonti esterne richieste per fascia di prezzo, riusando (nel testo del draft) il campo `soglia_rapporto_minima` di `offerta.schema.json` | C2 | INFRASTRUTTURA | T2 | «Niente sul primo lancio, per costruzione: alla fascia tripwire la soglia è zero» | Colpo S1-3 **REGGE**: `soglia_rapporto_minima` esiste già con un significato diverso (soglia del rapporto valore/prezzo per `GATE-OFF-1`, default 3) — AP-041 lo vuole riusare per un'altra soglia (fonti esterne, `GATE-CPY-1`), stesso nome due semantiche. Riparazione dichiarata: serve un campo nuovo dedicato (es. `soglia_fonti_esterne_minima`). Colpo S2-2 **REGGE con precisazione**: **150€ è inventato** (nessun punto misurato coincide — la fonte ha solo tre punti: 98€→0, 400€→2, 999€→5 fonti); **400€ NON è inventato** (è il punto realmente misurato di Vendita101) ma **sostituisce silenziosamente 349€** — la soglia realmente misurata in `ANATOMIA-DEI-LANCI.md` per «prova sociale con faccia e nome» — senza dichiarare la sostituzione. ⚖️ **DA DECIDERE IN P3**: `TASK-GAEL-20260908-SETTIMANA-03.md` righe 144-146, **già in esecuzione da Gael oggi**, istruisce la scala prezzi come «98→**434**→999» — un numero che non coincide con nessun punto misurato in nessuna fonte (dovrebbe essere 400, per ADR-024 riga 135) — trovato da Fable §3.A, non presente né in S2 né in Verità |
| **AP-042** | Articolo §13 di `CLAUDE-SITI.md`: la piattaforma si sceglie dalla vita del pezzo. Richiede ADR-029 (estende ADR-023) | C1 | DOCUMENTO | T1 (articolo) + T2 (ADR) + T4 (firma) | «Niente, e c'è il precedente esatto: ADR-024 §6... La firma di Max non ferma nessuno: si applica intanto, si firma quando si firma» | N/E |
| **AP-043** | Articolo §14 di `CLAUDE-SITI.md`: la temperatura del traffico governa la forma, non il prezzo | C1 | DOCUMENTO | T1 | «Niente, stesso regime di §11/§12» | N/E |
| **AP-044** | Cinque controlli nuovi per `catena.py` (9: densità immagini · 10: bundle scomposto · 11: prova social con fonte/alt · 12: codice sconto in config · 13: naming coerente) | C1 | INFRASTRUTTURA | Dichiarato T2 aggiuntivo (1-3h) | «Niente — non esistono oggi» | Colpo S2-3 **PARZIALE** (stessa verifica di AP-034): i controlli 10/11/13 sono più vicini a un piccolo motore di parsing/fuzzy-matching che a «banale» come dichiarato; il controllo 6 di AP-034 (prezzo dentro un'immagine con `alt` vuoto) è dichiarato da Fable **ineseguibile senza OCR**, non menzionato come problema nel testo originale nonostante sia — per verifica indipendente — il più difficile tecnicamente degli otto |
| **AP-046b** | Il prezzo di un bundle si scompone sempre in pagina (il gate già lo ricalcola, la pagina deve dirlo) | C2 (Gael, S3) | ⚖️ **DA DECIDERE IN P3**: S2 la classifica INFRASTRUTTURA (raggruppata con 047b/048b in una riga); Sentinella-verità la classifica **ABILITA UN EURO**, come riga separata, fra le sei «abilita» del suo conteggio | T1 | «Niente» (riga condivisa con 047b/048b) | N/E oltre alla contraddizione di classe già segnalata |
| **AP-047b** | Ogni prova sociale linka una fonte esterna o è etichettata come interna (`ART-CPY.affermazioni[].riferimento`) | C2 (Gael, S3) | ⚖️ **DA DECIDERE IN P3** — stessa divergenza di AP-046b (S2: INFRASTRUTTURA · Verità: ABILITA UN EURO) | T1 | «Niente» | N/E oltre alla contraddizione di classe |
| **AP-048b** | Ogni codice sconto vive in un solo file di configurazione, mai a mano nel testo (dentro il generatore AP-035) | Qualunque sessione, dentro AP-035 | INFRASTRUTTURA (concorde in entrambe S2 e Verità) | T1 | «Niente» | N/E |
| **AP-050** | Mirror di lancio come artefatto vivo: campo `mirror` in `funnel.json` + riga obbligatoria di riconciliazione nel debrief | C2 | INFRASTRUTTURA | T2 | «Niente — il campo è opzionale, e la riga di debrief è una delle tre già richieste da `GATE-MEM-1`» | N/E diretto. Collegata al «buco» (Sezione 7): AP-029 ha consegnato il pattern mirror-di-lancio su UN asset; nessuno lo applica sistematicamente al magazzino ULTIMO METRO — vedi Sezione 7 |
| **AP-051** | Ancora prima del prezzo: domanda di auto-stima del valore come blocco di libreria, prima del reveal | C2 | ABILITA UN EURO (S2) | T1 | «Niente — il campo è opzionale» | N/E |
| **AP-052** | Il rifiuto esplicito di scarsità finta diventa vincolo di `GATE-OFF-1`: `motivo_per_agire_adesso` deve citare `data_chiusura` reale | C2 | INFRASTRUTTURA | T1 + T1 (rosso) | «`GATE-OFF-1`. Ma solo su un'offerta che dichiari una scarsità falsa — un caso che, se si verifica, *deve* bloccare» | N/E |
| **AP-053** | Qualificazione negativa condizionata: obbligatoria solo se `concretezza == strumento-tecnico` avanzato; **esplicitamente esclusa** dalla configurazione tripwire del Manuale | C2 | DOCUMENTO (dichiarata inapplicabile al primo lancio dallo stesso draft) | T1 | «Niente» | N/E diretto. Nota di fusione S1 (N/E): stessa famiglia di AP-035/041/058 per il digest `MT-GEKH` |
| **AP-054** | L'obiezione mai nominata dal concorrente («lo imparo gratis dalla documentazione») entra in `ricerca.json` e nella griglia copy | C2 | ABILITA UN EURO | T1 | «Niente» | N/E. Presente in entrambe le sequenze correttive di S2 (passo 4) e Sentinella-verità (passo 4) come azione ad alto rendimento economico |
| **AP-055** | Il concorrente diretto (Claude Speedrun 2, 249€) entra in `ricerca.json → concorrenti[]` | C2 | Dichiarata originariamente **DOCUMENTO** (S2) — **CONTESTATA** | T1 | «Niente. `concorrenti[]` non è in `required`» | **Salvata in P2** (Fable §2.2): S2 la classifica «riga di ricerca interna in un JSON» ma la propria sequenza correttiva (passo 2, «portare `PU-PREZZO` a Max oggi») ha bisogno esattamente di questa informazione per essere «istruita» e non «inventata con più pagine» (regola scritta nello stesso `offerta.schema.json` che S2 cita altrove). Fable: «Quattro righe di JSON che alimentano l'azione n.2 di S2 non sono "solo documento"» — dovrebbe entrare dentro il passo 2 della sequenza correttiva, non nel mucchio documento |
| **AP-056** | Recupero (non riscrittura) del funnel di casa già scritto e mai lanciato: `chiamata-formazione.netlify.app`, 18.770px/25 sezioni/506 blocchi, puntato su Mastery 397€ | C2 | ABILITA UN EURO (S2: «l'unica azione vicina a un vero acceleratore di cassa») | T2 | «Niente. Se la pagina non è raggiungibile, si costruisce da zero e la riga va in `BACKLOG.md`» | N/E dalle critiche dirette, ma **elevata a priorità n.1** dalla sequenza di Sentinella-verità (§6 passo 1): «l'asset più vicino a un incasso che l'azienda possiede oggi, non fra tre giri di critica» |
| **AP-057** | Pagina di consegna obbligatoria in `GATE-FNL-1.pagine[]` (`ruolo: consegna`) + regola colore brand su CTA (AP-031) | C2 (criterio) + C1 (controllo) | INFRASTRUTTURA | T1 + T1 | «`GATE-FNL-1` soltanto, e solo dopo la modifica. Attenzione: ... Se [`evento_conversione` è impossibile da leggere dietro login] si dichiara `non_misurato`... invece di rendere il gate insoddisfacibile» | Colpo #7 di S1 (**N/E — non ripreso nella tabella numerata di Fable**, quindi non riesaminato in P2, resta come dichiarato in P1): verificato che `funnel.schema.json` rende `evento_conversione` **obbligatorio** e `prova.origine` un **enum chiuso** senza valore «non misurato» — la scappatoia descritta non è «già gestita dal campo esistente» come l'azione afferma; servirebbe comunque una modifica di schema non dichiarata come necessaria. S1 la mette in lista «azioni da uccidere» (la frase, non l'azione intera) |
| **AP-058** | Percorso freddo: tetto di parole dichiarato (riferimento misurato: 86 parole) come criterio d'uscita di `PA-1` | C2 | INFRASTRUTTURA | T1 | «Niente» | N/E |
| **AP-059** | `VOCABOLARIO-LEVE.md`: nove voci (le otto costanti di Parte V + la nona di Parte XI), con «con cosa non va confusa» | C1 | DOCUMENTO | T2 | «Niente» | N/E diretto. Vedi nota di fusione su AP-012 (due vocabolari nello stesso ecosistema, mai cross-linkati) |
| **AP-060** | Vincolo upsell in `GATE-OFF-1`: attivo solo se il lancio dichiara un lancio precedente nella catena — cioè solo sul secondo lancio (Mastery), non sul primo | C2 | INFRASTRUTTURA (esplicitamente inattiva sul primo lancio) | T1 | «Niente sul primo lancio» | N/E |

---

## 4. Corsia C1 — libera, si esegue subito

Azioni classificate **C1** nella tabella §3, eseguibili da chiunque, zero collisione dichiarata con
`TASK-LANCI-BUILD-W3` — con le eccezioni segnalate dove un colpo ha contestato la corsia stessa.

| ID | Azione | Criterio di «fatto» (dalla fonte) |
|---|---|---|
| AP-034 | `catena.py` esiste ed è eseguibile | `ls .claude/skills/fabbrica-siti/scripts/catena.py` + `python catena.py --help` funzionante |
| AP-035 | Generatore pre-cassa | `genera.py` produce una pagina valida dalle sei variabili, sempre `noindex,nofollow` |
| AP-036 | Pattern `cassa-corso-a-livelli` | File creati + `galleria.py` rilanciato (galleria passa da 8 a 10) |
| AP-038 | 22 formule nella libreria (**corsia contestata**, vedi §3 — se eseguita, va subordinata all'apertura della cartella `copy/libreria/` da parte di Gael, non anticipata da altra sessione) | 22 file in `copy/libreria/formule/01..22.md` |
| AP-042/043 | Articoli §13/§14 + ADR-029 | `grep -c "^## §" CLAUDE-SITI.md` = 14; ADR-029 scritto nella forma «estende ADR-023» |
| AP-044 | Controlli 9-13 | Aggiunti dentro `catena.py`, insieme o subito dopo AP-034 |
| AP-057 (solo la metà «controllo») | Estensione di `catena.py` sul colore brand della pagina di consegna | Il controllo gira su una pagina di consegna di prova |
| AP-059 | `VOCABOLARIO-LEVE.md` | File esiste in `PIANO-MAESTRO/29-ECOSISTEMA-LANCI/09-VOCABOLARIO-LEVE.md` |
| AP-006 patch A/B, AP-012 (+ correzione revops), AP-019, AP-020b (Draft B) | Patch a skill fuori perimetro LANCI | Le 3-6 righe/file dichiarati in ciascuna azione, vedi §3 |

## 5. Corsia C2 — consegnata a Gael

Azioni classificate **C2**: dichiarate qui, non eseguite da altre sessioni. Formato dalla tabella
maestra §5.1 di Draft A (scaglione S0→S5 di `TASK-LANCI-BUILD-W3`):

| Scaglione | Micro-task | Azioni di questo assemblaggio |
|---|---|---|
| S1 | `MT-9ADD` | AP-004 (ancoraggio) · AP-055 (concorrente in ricerca) · AP-054 (obiezione) · AP-051 (ancora prezzo) · AP-033 (opzione futura, se Max la vuole) |
| S2 | `MT-XV6Y`, `MT-3XWC`, `MT-4GNU`, `MT-GHZ6` | AP-033 (schema + criterio `GATE-OFF-1`) · AP-052 (scadenza vera) · AP-060 (vincolo upsell) · i rossi corrispondenti |
| S3 | `MT-GEKH` | AP-005 · AP-008 (**rosso riassegnato qui, non a `MT-4GNU`** — correzione Fable §2.1) · AP-039 · AP-040 · AP-041 · AP-037 (cartella) · AP-050 · AP-056 · AP-057 · AP-058 · AP-053 · AP-046b/047b |
| S4 | `MT-69CE` | AP-033 (riga debrief impegno futuro) · AP-050 (riga riconciliazione mirror) |
| S5 | `MT-RGZ6` | copertine in attesa, impegni futuri scaduti (AP-033), mirror non riconciliati (AP-050) |

**Nota di governo, non modificabile dallo Scagnozzo (riportata da Draft A §6.1):** ogni azione C2
tocca il registro o uno schema; `valida_registro.py` deve tornare a exit 0 nello stesso turno, mai
lasciato a metà — un registro incoerente fermerebbe Gael su qualcosa che non è suo.

---

## 6. I NO-GO, con il motivo

| ID | Cosa NON si fa | Perché | Condizione di riapertura |
|---|---|---|---|
| **AP-006** (automazione) | Automazione AI dei preventivi d'agenzia (cs2online Bonus 6) | Il processo gira ~0 volte/mese (`A3-PREVENTIVI/handoffs/` = un file, di giugno); automatizzare un processo a throughput zero fa risparmiare zero ore e produce un altro macchinario da mantenere (ULTIMO METRO). KA-01 della fonte stessa lo dice: non automatizzare un processo non ripetuto | `A3-PREVENTIVI/handoffs/` registra ≥4 preventivi d'agenzia reali/mese per 2 mesi consecutivi |
| **AP-018** | Framework a 10 livelli di maturità AI come tool/assessment d'agenzia | `market-audit` copre già l'onboarding diagnostico con più profondità; il framework è il dispositivo di posizionamento di un concorrente (P1 dell'analisi: «sei bloccato al 3, il corso ti porta al 5»); anti-posizionato rispetto a «l'agenzia progettata per essere licenziata»; fallisce T1/T2/T3 insieme; `free-tools` ha già il test (lead value × lead attesi > costo) e nessuno ha messo un numero | Manuale Claude Code lanciato con almeno una vendita registrata in `entrate.jsonl` **e** il conto di `free-tools` fatto con numeri veri |
| Ponte `beast-preventivi` ↔ `preventivo-auto` | Non si costruisce | Domini diversi: proposte d'agenzia vs riscrittura annunci auto mobile.de. Condividono una parola, non un problema | Niente. Non va costruito |
| Estensione di AP-020 a «tutte le skill che generano output strutturati» | Non si fa, solo 2 skill patchate | Una regola applicata ovunque diventa una regola che nessuno legge | Un caso reale di output inventato in una terza skill |

---

## 7. Il buco — la lezione non convertita

**Quello che P1-S2 ha trovato:** il vantaggio competitivo reale di Andrei Pascu non è un funnel più
pulito — è che non scrive mai pagine nuove per lanciare (mirror-di-lancio: si specchia il negozio,
lo si spoglia, si punta a una cassa sola — `SINTESI-METODO.md` §3). Digital Empire ha, per
ammissione di ADR-016 (ULTIMO METRO), **25 pezzi finiti e mai usciti** (2.137 MB, il più vecchio da
135 giorni al 2026-09-03 — **142+ giorni** oggi, ricalcolo di Sentinella-verità). Nessuno dei due
draft applica il mirror-di-lancio sistematicamente a quel magazzino: Draft A lo usa su un solo
asset trovato per caso (AP-056), le altre 22 azioni della Famiglia B costruiscono invece l'apparato
di disciplina (schemi, gate, griglie) — l'opposto del metodo che produce volume a basso costo.
Draft B nomina il problema (§7 punto 4: «il caso più puro di ULTIMO METRO applicato a un organo
interno») e lo dichiara nello stesso paragrafo fuori dal proprio perimetro.

**Quello che Sentinella-verità ha trovato ed è più forte** (non citato né da S1 né da S2, confermato
da Fable §3.C come «superiore» al buco di S2): Digital Empire possiede già, sul disco, due pezzi di
codice funzionanti e mai collegati:
- `empire/tools/checkout.py` — 375 righe, legge `Crea siti/Siti CCM/checkout.config.json` (prezzo
  già impostato 67/97€, quattro rail di pagamento previsti, tutti `"attivo": false` tranne il
  fallback email; il campo dice letteralmente `"richiede": "MAX: crea Payment Link su Stripe"` — un
  gesto umano da dieci minuti, non una build).
- `KDP - prodottti digitali/Leanding Page/email-agent/main.py` — 81 righe, webhook FastAPI reale che
  verifica la firma Stripe e consegna un PDF via Gmail SMTP su `checkout.session.completed`. Ha già
  una `STRIPE_SECRET_KEY` **live** nel `.env` (per un ebook diverso).

Collegare questi due pezzi (Payment Link vero + adattare `main.py` per il Manuale) è lavoro di poche
ore, non delle 28-46h del piano combinato. Nessuna delle 34 azioni del piano lo tocca. `ADR-003`
(wrap, mai riscrittura) viene applicato dal Draft A al funnel morto di Mastery (AP-056) ma non a
questo pattern di incasso già vivo.

**Il buco che P2 (Fable) aggiunge, non presente in nessuna delle fonti P1 (§5 del suo documento):**
nessuno dei cinque documenti precedenti chiede *quante persone vedranno la pagina del primo lancio
il giorno dell'apertura, e da quale canale* — mentre `04-COSTRUZIONE.md` riga 230 dà probabilità
«media-alta» che il pubblico sia troppo piccolo (il canale previsto è spento dal 29/07/2026) e la
riga 251 impone che con pubblico verificato zero «si ferma il lancio e si va a costruire pubblico».
Prezzo firmato + Stripe attivo + pagina viva + `catena.py` a exit 0, moltiplicati per zero
visitatori, fanno zero euro.

**Rischio di sicurezza attivo, segnalato da Sentinella-verità e non toccato da nessuna delle 34
azioni:** `BACKLOG.md` righe 42-45, **B-020** — chiave Brevo esposta in chiaro su repo pubblico, non
ruotata da mesi, marcata «🔴 subito» e riconfermata la più urgente nella TASK-GAEL di oggi.

---

## 8. Cosa è già fatto (non rifare)

Dalla «correzione di fatto al briefing» di Draft A §0.2, verificata sul disco: il briefing originale
dice «12 candidati già applicati», ma la tabella 🟢 di `MIGLIORAMENTI-DIGITAL-EMPIRE.md` (righe
25-39) ne contiene **13**: AP-001, 002, 003, 006, 007, 009, 010, 011, 012, 013, 014, 015, **016**.
Più **quattro** marcati 🟢 «consegnato» nell'ultima tabella: AP-029, AP-030, AP-031, AP-032.

**Totale verde reale: 17 candidati.** Nessuno di questi è ri-proposto in questo assemblaggio.
(I codici di checkpoint EMP-APDOC1/EMP-APIMPL1 citati altrove in Memory non compaiono per esteso
nelle 6 fonti assemblate qui — questo elenco riporta solo ciò che le fonti stesse dichiarano già
fatto.)

---

## 9. Numeri: quali sono misurati e quali sono stimati

| Numero | Dove compare | Stato | Fonte / nota |
|---|---|---|---|
| 27-47 € | AP-004, fascia prezzo proposta Manuale | **STIMA non dichiarata come tale nel testo** | Pescata da `_v3-superata/04-WF-OFFERTA.md:146-169` (documento superato), mai citata come fonte nell'azione (trovato da Sentinella-verità, confermato Fable) |
| 100 € | AP-033, valore `opzione_futura` | **INVENTATO** | Nessuna derivazione; la fonte reale misura 199€ (`ANATOMIA-DEI-LANCI.md` righe 308-312) |
| 150 € | AP-041, soglia fonti esterne fascia bassa | **INVENTATO** | Nessun punto misurato coincide (i tre punti reali sono 98/400/999€) |
| 400 € | AP-041, soglia fonti esterne fascia alta | **MISURATO** (Vendita101) ma **sostituisce silenziosamente 349€** | 349€ è la soglia reale per «prova sociale con faccia e nome» in `ANATOMIA-DEI-LANCI.md`; 400€ non è la stessa cosa e la sostituzione non è dichiarata |
| 434 (scala 98→434→999) | `TASK-GAEL-20260908-SETTIMANA-03.md` righe 144-146, **istruzione viva** | **NON coincide con nessun punto misurato in nessuna fonte** — dovrebbe essere 400 | Trovato da Fable §3.A, unico numero sbagliato già in esecuzione |
| 67 € / 97 € / 27 € | DEC-EST-001, già in `checkout.config.json` | **MISURATO/FIRMATO** (silenzio-assenso 2026-07-21) | `scadenza_lancio: 2026-07-31` **già scaduta** al 2026-09-10 |
| 249 € | AP-055, prezzo Claude Speedrun 2 (concorrente diretto) | **MISURATO** | `https://claude-speedrun.com`, citato in AP-055 |
| 397 € | AP-004, prezzo Claude Code Mastery | **MISURATO** («già dato in azienda») | `ANATOMIA-DEI-LANCI.md` Parte X punto 5 |
| «massimo 3 rami per sequenza» | AP-012 (Draft B) | **INVENTATO** | Attribuito a KA-07, che nella fonte non contiene numeri |
| Effort `catena.py` (AP-034) | 4-8h dichiarate | **CONTESTATO — tre stime in circolo**: 18-30h (S2) · 8-16h (Sentinella-verità) · 2-4h se limitato al solo controllo 8+3+5 (Fable) | La variabile è il perimetro (quanti degli 8 controlli), non solo la stima — vedi tabella §3 |
| Effort totale piano combinato | 28-46h (Draft A) + 3h20-4h20 (Draft B) | **STIMA, sottostimata secondo S2/Sentinella-verità** | Nessuna delle due somme include la taratura anti-falsi-positivi di `catena.py` né il tempo di verifica delle patch di Draft B (istruzioni per agenti LLM, non codice deterministico) |
| Numero azioni totali | 27 (Draft A) + 7 (Draft B) = 34 (S2) — vs 33 (Sentinella-verità) — vs 34 per ID distinto (questo assemblaggio, §3) | **⚖️ DA DECIDERE IN P3** | Il disaccordo nasce da come si contano AP-046b/047b/048b (una riga o tre) — vedi nota apertura §3 |
| `entrate.jsonl` / `spese.jsonl` | Tesoreria | **MISURATO: 0 righe, 0 byte, entrambi** | Riverificato da S2, Sentinella-verità e Fable indipendentemente, stesso esito |
| ULTIMO METRO | 25 pezzi, 2.137 MB, pezzo più vecchio | **MISURATO al 2026-09-03** (135 giorni allora) | Ricalcolo Sentinella-verità al 2026-09-10: **142+ giorni** |

---

## 10. Registro delle critiche (P1 → P2 → P3)

### Giro P1 — tre critiche indipendenti sui due DRAFT V1

**P1-S1 (governo/coerenza/collisione), 7 colpi:**
1. AP-034 rango 1 non collegata a nessun gate reale → **REGGE in P2**
2. AP-038 viola la corsia C2 dichiarata dal piano stesso → **REGGE in P2**
3. AP-041 riusa un campo esistente con significato diverso → **REGGE in P2**
4. Nota §3.11 sul «settimo rosso» è falso allarme + ADR-024 internamente incoerente → **PARZIALE in P2** (la metà su ADR-024 regge; la metà «falso allarme» non regge intera — il problema esiste davvero, il rimedio proposto da S1 di *togliere* la nota era sbagliato: va corretta, non tolta — salvataggio Fable §2.1)
5. Canale parallelo non riconciliato con l'istruzione già data a Gael in `TASK-GAEL-20260908-SETTIMANA-03` 4️⃣ → **N/E, non ripreso nella tabella numerata di P2**
6. Numerazione AP-034→060 non torna (dichiarati 23, sono 22 interi + 3 «b») → **N/E diretto**, ma il tema del conteggio è ripreso e ampliato da P2 in altra forma (§3.C, 33 vs 34)
7. Scappatoia `non_misurato` di AP-057 non supportata dallo schema → **N/E, non ripreso nella tabella numerata di P2**

**P1-S2 (denaro/verità), colpi principali:**
- Classificazione 34 azioni, 0% euro diretto, 82% infrastruttura/documento → **PARZIALE in P2** (l'aritmetica interna torna, ma il totale «34» dipende da una scelta arbitraria di conteggio contestata da Sentinella-verità; AP-055 declassata ingiustamente a documento — salvata; «nessuna azione tocca i 5 gesti umani» è falso alla lettera per AP-004)
- 4 numeri inventati (27-47€, 100€, 150/400€, «3 rami») → **REGGE con due precisazioni** (400€ non è inventato, è sostituito senza dichiararlo da 349€; 27-47€ ha una fonte reale, un documento superato, non è dal nulla)
- Stima `catena.py` 18-30h vs 4-8h dichiarate → **PARZIALE — c'è una terza risposta**: il perimetro è la variabile
- Il piano è il pezzo 26 di ULTIMO METRO (magazzino non smaltito col metodo mirror) → confermato e **superato** da un ritrovamento più forte della quinta fonte
- Ordine `catena.py` al rango 1 è sbagliato, sequenza «cassa prima» in 5 passi → ripreso e integrato in P2 (che vi aggiunge la domanda sul pubblico, mai posta da nessuno)

**P1-Sentinella-verità (indipendente, angolo denaro/verità), trovamenti propri non nella S2:**
- Conteggio 33 azioni (diverso da S2: 34) → **⚖️ irrisolto, riportato in P3**
- AP-046b/047b classificate ABILITA UN EURO, non INFRASTRUTTURA come in S2 → **⚖️ irrisolto, riportato in P3**
- `checkout.py` + `email-agent/main.py` + DEC-EST-001 (67/97€, già firmata, già scaduta) — pattern di incasso già funzionante mai collegato → **confermato da P2 come il ritrovamento più forte dell'intero giro P1**, non contestato
- B-020 (chiave Brevo esposta) mai toccata dalle 33/34 azioni → ripreso in Sezione 7 di questo assemblaggio
- Rischio pubblico/traffico non censito → ripreso e **approfondito ulteriormente** da P2 (§5, «la domanda che nessuno ha fatto»)

### Giro P2 — Fable, critica della critica

Oltre ai verdetti sui singoli colpi (sopra), P2 ha aggiunto tre ritrovamenti propri, non presenti in
nessuna delle tre fonti P1:
1. **Il 434 nella TASK-GAEL viva** (§3.A) — un numero sbagliato già in esecuzione, che nessuna delle
   tre critiche precedenti aveva notato pur avendo ciascuna verificato pezzi della stessa scala prezzi.
2. **La tesoreria citata da tutti come accusa e cablata da nessuno** (§3.B) — nessuna delle 34 azioni
   né delle tre sequenze correttive scrive la riga che registra il primo euro in `entrate.jsonl`
   quando arriva.
3. **Il giro P1 stesso non è riconciliato** (§3.C) — due critiche sul denaro (S2 e Sentinella-verità)
   si contraddicono su conteggio e classificazione senza saperlo a vicenda; questo assemblaggio
   eredita quella contraddizione e la marca `⚖️ DA DECIDERE IN P3` ovunque tocchi una singola azione
   (AP-004, AP-041, AP-046b, AP-047b, il conteggio totale in apertura di §3).

**Verdetto finale di P2 sulle due tesi pesanti (S1 e S2):** non si contraddicono, sono la stessa
malattia a due scale — S1 è il caso particolare (un artefatto senza consumatore nominato non esiste
per il sistema), S2 è la generalizzazione (un piano il cui consumatore finale, la cassa, non è
nominato da nessuna azione è il pezzo 26). P2 propone di fondere le due regole in un criterio di
accettazione universale per il documento finale: **nessuna azione è «fatta» finché non nomina, con
path e riga, il consumatore che la invoca** — il gate per gli script, la tesoreria per gli euro, la
micro-task per i test rossi.

### Verso P3 — cosa resta esplicitamente irrisolto

- Il conteggio esatto delle azioni (33 / 34 / 34-per-ID) e la classe di AP-046b/047b (§3, §9)
- La fascia di prezzo del Manuale — quale delle cinque/sei cifre in circolo firma Max (§3 AP-004,
  §9)
- Se `catena.py` va costruita per intero (18-30h) o nella versione minima proposta da Fable (2-4h,
  solo controllo 8+3+5) prima di agganciarla a `GATE-FNL-1`
- La correzione del 434→400 nella `TASK-GAEL-20260908-SETTIMANA-03` viva
- Chi scrive, e quando, la prima riga in `tesoreria/entrate.jsonl`

---

## Connessioni

- `competitor/Andrei Pascu/piano-implementazione/STRUTTURA-DOCUMENTO-FINALE.md` — la legge di questo assemblaggio
- `competitor/Andrei Pascu/piano-implementazione/DRAFT-V1-A-lanci.md`, `DRAFT-V1-B-capacita.md`
- `competitor/Andrei Pascu/piano-implementazione/P1-CRITICA-S1-governo.md`, `P1-CRITICA-S2-denaro.md`, `P1-CRITICA-sentinella-verita.md`
- `competitor/Andrei Pascu/piano-implementazione/P2-FABLE-critica-della-critica.md`
- `company/Memory/decisions/ADR-016-ultimo-metro.md`, `ADR-024-canone-v2-primo-strato.md`, `ADR-025-ecosistema-lanci.md`, `ADR-028-niente-blocca-tutto.md`
