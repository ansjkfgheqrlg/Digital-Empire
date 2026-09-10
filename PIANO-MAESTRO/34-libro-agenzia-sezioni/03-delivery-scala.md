# Capitolo 3 — Consegna, Servizio e Scala

*Nota per il lettore: questo capitolo fa parte della Parte 2 del libro — la formazione esterna
da cui il metodo di Digital Empire nasce. Tutto ciò che segue riporta cosa insegnano tre fonti
esterne (due video di Giovanni Beggiato, fondatore dell'agenzia Gentes AI, e un video di
Riccardo Belli Contarini, fondatore dell'agenzia Martes AI), non cosa fa Digital Empire. Dove le
fonti stesse confrontano il proprio insegnamento con pratiche di agenzia già diffuse, lo si segnala
restando chiaro che il confronto appartiene alla fonte, non a una dichiarazione aziendale.*

## 3.1 Tre fonti, tre livelli dello stesso problema

Il Capitolo 1 e il Capitolo 2 di questa Parte hanno coperto come un'agenzia trova un cliente. Ma
un lead che paga non è ancora un cliente servito bene, ed è qui che la maggior parte delle agenzie
— comprese quelle AI-native, dove il ciclo di vendita può essere rapidissimo — comincia a
scricchiolare. Una delle fonti di questo capitolo lo dice con una frase che vale come cerniera fra
i due momenti:

> "Voi avete un cliente se solo se c'è stato un movimento di denaro." [apertura sezione
> fulfillment, Giovanni Beggiato, *Come Avviare Un'Agenzia AI da 10.000€/Mese*, video ID
> `rvpRQD43wdY`]

Prima di quel movimento di denaro, tutto è acquisizione. Dopo, comincia un problema diverso: come
si consegna lo stesso livello di qualità al cliente numero 50 che si è promesso al cliente numero
1, senza che il fondatore diventi il collo di bottiglia di ogni progetto. La stessa fonte
riassume lo scheletro operativo di un'agenzia in **7 fasi** — Lead Generation → Sales Funnel →
Sales Call → Onboarding → CRM Management → Delivery/Fulfillment → Upselling — e in **3 pilastri**
che reggono l'intera struttura: **Promozione** (acquisizione, coperta nei capitoli precedenti),
**Prodotto** (la consegna vera e propria) e **Daily Ops** (la gestione quotidiana che tiene tutto
in piedi). Il punto sottolineato dalla fonte è che la competenza sui *processi* — non sugli
strumenti, che cambiano ogni pochi mesi — è ciò che sopravvive.

Questo capitolo copre la fase Prodotto/Delivery da tre angolazioni diverse, offerte da tre fonti
distinte:

1. **Prezzo e processo** (Giovanni Beggiato, *Come Avviare Un'Agenzia AI da 10.000€/Mese*,
   `rvpRQD43wdY`, 4h17m00s) — come si prezza un servizio AI, e come si struttura il flusso di
   consegna dal kickoff alla chiusura del progetto, fino a quando e come assumere.
2. **Il servizio reso scalabile** (Giovanni Beggiato, *Ho creato un intero team di marketing AI
   con Claude Code in 20 minuti*, `yJOCyyP77bA`, 19m54s) — un esempio concreto e mostrato dal vivo
   di cosa significa "scalare la consegna senza scalare le ore umane": un team di 6 agenti AI
   specialisti che produce in 20 minuti un audit di marketing completo, deliverable incluso.
3. **Il controllo indipendente della qualità** (Riccardo Belli Contarini, *Claude Code + Codex: Il
   Setup di cui NESSUNO Parla*, `T7PPX5M6Puo`, 30m52s) — perché un lavoro dichiarato "pronto" da
   chi lo ha costruito può non esserlo affatto, e cosa succede quando lo si fa controllare da
   qualcuno — o qualcosa — che non condivide gli stessi punti ciechi.

Tre livelli dello stesso problema: **quanto** far pagare, **come** consegnarlo in modo ripetibile,
**chi** verifica che sia davvero pronto prima che il cliente lo veda.

---

## 3.2 Prezzo e pacchetti

### La matrice DIY / DWY / DFY × Tempo / Unità / Risultato

Beggiato presenta — e la disegna dal vivo, verificata a schermo in `frame-0451.png` — una matrice
3×3 che incrocia **come** il cliente riceve il servizio con **su cosa** viene prezzato:

| | Tempo | Unità | Risultato |
|---|---|---|---|
| **Do It Yourself (DIY)** | il cliente compra tempo del tuo prodotto/strumento | il cliente compra un pacchetto di unità da usare da solo | il cliente paga per un risultato che raggiunge da solo con il tuo strumento |
| **Done With You (DWY)** | consulenza a ore/sessioni | pacchetti di unità con supporto | risultato garantito con coaching incluso |
| **Done For You (DFY)** | retainer a tempo (ore/mese dell'agenzia) | **"vendo N automazioni a X€"** | risultato garantito, l'agenzia fa tutto |

Le soluzioni AI, nota la fonte, si collocano quasi sempre nel quadrante **DFY-Unità**: vendere un
numero definito di automazioni a un prezzo fisso. È il quadrante più scalabile della matrice
perché è l'unico **disaccoppiato dal tempo dell'operatore** — un'automazione consegnata al
cliente 1 non costa più ore all'agenzia del cliente 50, mentre ogni altro quadrante lega il
fatturato a un tempo umano che non si moltiplica.

Sopra questa matrice, la fonte sovrappone **tre modelli contrattuali**, che possono convivere
sullo stesso cliente:

- **Pay in full** — pagamento anticipato dell'intero progetto.
- **Pay on performance** — il cliente paga solo, ad esempio, l'ad-spend; l'agenzia rischia sul
  resto del compenso, scommettendo sulla propria capacità di generare risultato.
- **Retainer misto** — una quota fissa mensile più una componente variabile.

### Perché il quadrante DFY-Unità funziona: la "released capacity"

Un elemento centrale per capire *perché* un cliente paga per un'automazione — e quindi perché il
prezzo del quadrante DFY-Unità regge — è il concetto di **released capacity** (capacità
produttiva liberata), che la fonte pone al centro dell'intera proposta di valore dell'agenzia AI:
non si vende un software, si vende tempo umano restituito all'azienda. L'esempio numerico dato:

```
100 dipendenti × 5 ore risparmiate/settimana = 500 ore/settimana
500 ore × €10/ora                            = €5.000/settimana di "released capacity"
```

La fonte è esplicita su un punto che rischia di perdersi in qualsiasi rielaborazione superficiale
di questo materiale: quelle non sono ore diventate automaticamente soldi in tasca
all'imprenditore — sono soldi **potenzialmente** cash, che si materializzano solo se qualcuno
decide cosa fare con le 500 ore liberate. Da qui il salto di ruolo che la fonte attribuisce
all'agenzia AI matura: da fornitore di uno strumento a **partner di change management**. Se
l'agenzia non aiuta il cliente a decidere cosa fare col tempo liberato, il valore percepito
dell'automazione resta basso, quanto sia tecnicamente elegante lo strumento.

### La golden rule del close rate: 30%

Il criterio con cui la fonte suggerisce di sapere se il prezzo fissato è quello giusto non è un
calcolo sui costi, ma una lettura a posteriori del comportamento dei lead in sales call. Il testo
esatto, verificato sulla trascrizione grezza del video (con correzione di una lettura precedente
che schiacciava le tre soglie in una sola):

> "se il vostro close rate e' piu' alto quindi ipotizziamo che il vostro close rate sia del 60%
> significa che il vostro prezzo e' troppo basso rispetto all'offerta se invece ipotizziamo questo
> sia del 20% vuol dire che o siete delle scarpe a vendere o che il prezzo e' troppo alto [...]
> golden rule per service business dovreste essere sul 30%" [sezione pricing, `rvpRQD43wdY`]

Le tre soglie:

| Close rate | Lettura secondo la fonte |
|---|---|
| **60%** | prezzo **troppo basso** rispetto all'offerta |
| **30%** | **golden rule** per un service business — l'equilibrio giusto |
| **20%** | prezzo troppo alto **oppure** "siete delle scarpe a vendere" |

La fonte precisa anche che questo benchmark non è universale: per un modello a **community**, il
close rate atteso e considerato sano è del **2-4%**, non del 30% — la logica di un servizio
one-to-one (dove ogni lead in call viene qualificato a fondo prima di arrivarci) non si applica a
un'offerta aperta a un pubblico ampio.

### Le sei metodologie di acquisizione — solo il ranking

Il dettaglio operativo delle sei metodologie di acquisizione clienti indicate da questa stessa
fonte — Warm Network, Upwork, Strategie Cold, Ads, Fiverr, Social Media Posting — è trattato per
intero nel Capitolo 1 di questa Parte. Qui interessa solo la loro collocazione nella scala di
difficoltà crescente su cui la fonte le ordina (elenco confermato a schermo in `frame-0631.png`,
1:24:00 del video):

1. Warm Network (rubrica personale)
2. Upwork (bootstrap)
3. Strategie Cold (email, DM, call)
4. Ads (solo su contenuto organico già validato)
5. Fiverr (inbound, richiede brand già riconosciuto)
6. Social Media Posting / Organico (curva lenta, nessun plateau precoce)

Il motivo per cui questo ranking appartiene anche al capitolo sulla consegna, e non solo a quello
sull'acquisizione, è che il pricing e il canale di acquisizione **non sono indipendenti**: un
canale che porta lead poco qualificati (es. Ads su contenuto non testato) può far scendere il
close rate sotto il 20% anche con un prezzo corretto, mentre un canale che porta lead già caldi
(Warm Network) può reggere un prezzo più alto con lo stesso close rate — la matrice di pricing
va sempre letta insieme al canale che ha generato quel lead specifico.

---

## 3.3 Fulfillment: dal kickoff alla consegna ripetibile

### Il flowchart Whimsical

La fonte mostra a schermo (verificato in `frame-1401.png` e `frame-1440.png`, URL
`whimsical.com/beggiato-media/how-to-service-your-first-automation-client-in-2026-...`) un
flowchart di fulfillment completo, costruito su Whimsical, che copre l'intero ciclo da "hai già
fatto questo progetto prima?" fino a "test end-to-end + rafforza i casi limite". È il documento
di processo che trasforma la consegna da artigianale (ogni progetto reinventato da zero) a
ripetibile (ogni progetto segue lo stesso schema, con varianti sui dettagli).

### I cinque punti obbligatori della kickoff call

Il nodo più densamente istruttivo del flowchart è la kickoff call, per cui la fonte elenca cinque
elementi che devono essere coperti **sempre**, senza eccezioni:

1. **Timeline con under-promise-and-overdeliver** — la data comunicata al cliente è
   deliberatamente più larga di quella realisticamente attesa internamente, per lasciare margine
   e consegnare in anticipo invece che in ritardo.
2. **Reperibilità esplicita** — si dichiara al cliente quando e come l'agenzia è raggiungibile,
   invece di lasciarlo intuire o scoprire per tentativi.
3. **Definizione scritta del successo** — cosa significa "progetto completato" viene messo per
   iscritto prima di iniziare, proprio per prevenire lo **scope creep**: senza una definizione
   scritta, ogni richiesta successiva del cliente rischia di essere trattata come "compresa" nel
   progetto originale, anche quando non lo è.
4. **Registrazione delle piattaforme in call** — le credenziali e gli accessi necessari vengono
   raccolti mentre si è in videochiamata con il cliente, non rincorsi via email nei giorni
   successivi.
5. **Tracciamento (opzionale)** — un sistema di monitoraggio dello stato di avanzamento, quando
   il progetto lo richiede.

### La policy delle credenziali: sempre del cliente

Un punto di processo dichiarato esplicitamente dalla fonte, e non negoziabile nel suo racconto:
**le credenziali di ogni piattaforma usata nel progetto sono sempre intestate al cliente**, mai
all'agenzia. La ragione dichiarata è evitare il **vendor lock-in**: se l'agenzia possiede gli
account su cui gira l'automazione del cliente, il cliente non può mai davvero lasciare l'agenzia
senza perdere il proprio sistema — una dipendenza che nel racconto della fonte è vista come un
rischio reputazionale e commerciale, non come una leva di ritenzione legittima.

### GoHighLevel come esempio di piattaforma di servizio

Per rendere concreto cosa significhi "fulfillment" in pratica, la fonte fa una demo dal vivo di
**GoHighLevel**, un CRM all-in-one per agenzie, sul dominio reale `gentes.ai` (dashboard
verificata a schermo in `frame-1511.png`). I dati confermati a schermo:

- Costo: **~97$/mese**
- **3 sub-account** inclusi nel piano base
- Programma di affiliazione: fino al **50% ricorrente**

La distinzione tecnica che la fonte segnala come chiave per **templetizzare** un funnel — cioè
costruirlo una volta e rivenderlo a più clienti senza ricostruirlo da zero — è quella fra:

- **custom values**: legate al sub-account/cliente (es. il nome della città in cui opera quel
  cliente specifico)
- **custom fields**: legate al singolo lead (es. la fonte di provenienza, il consenso dato)

La demo copre anche il funnel builder, la pipeline "Opportunities", il calendario, e i workflow di
automazione — mostrando in particolare la tecnica del **"taking in charge"**: un messaggio
automatico di presa in carico inviato al lead prima ancora che un umano lo richiami, con
l'obiettivo dichiarato di alzare il pickup-rate della chiamata umana successiva. La demo si
chiude su Meta Ads Manager, con una campagna reale in bozza — budget **€20,00**, verificato a
schermo, non un dato sintetico di esempio come altre schermate del video.

### Hiring & Scaling: quando e chi assumere

L'ultima sezione della fonte riguarda il momento in cui un'agenzia smette di essere un solo
fondatore e comincia ad assumere. La regola centrale: si assume **a capacità**, non per avere più
tempo libero, e **per bisogno**, non per crescita — soprattutto nella fase iniziale. Prerequisito
esplicito prima di qualunque assunzione: le **SOP** (procedure operative standard) devono essere
già documentate, altrimenti si assume qualcuno senza dargli un processo da seguire.

Il primo ruolo da assumere, secondo la fonte, non è il commerciale ma il **CTO** — la logica è che
un CTO libera l'imprenditore dal lavoro tecnico per concentrarlo sulle vendite, che restano
l'unica leva capace di far crescere il fatturato in prima persona. Un grafico disegnato a mano
durante il video (`frame-1875.png`) mostra il salario dell'imprenditore **scendere
temporaneamente** subito dopo l'assunzione del CTO, prima di risalire quando il fatturato comincia
a scalare grazie al tempo liberato — un costo iniziale dichiarato esplicitamente, non nascosto.

La fonte chiude l'intero video con una nota che ridimensiona l'ambizione stessa del percorso
appena descritto:

> "Voi letteralmente imparate a gestire un business... l'agenzia AI sarà probabilmente l'ultimo
> business che farete? Assolutamente no." [chiusura, sezione hiring & scaling, `rvpRQD43wdY`]

L'agenzia AI, nella lettura della fonte, è quasi sempre uno **step intermedio** verso business più
scalabili — SaaS, community, prodotto digitale — non il punto di arrivo.

---

## 3.4 Il servizio come prodotto: un team di agenti scala la consegna

Se la sezione precedente descrive il *processo* di fulfillment, questa sezione ne mostra
un'applicazione concreta e filmata dal vivo: come lo stesso autore, nella sua agenzia Gentes AI,
ha trasformato un servizio che normalmente richiederebbe ore di lavoro umano — un audit di
marketing completo per una PMI — in un output di 20 minuti prodotto da un team di agenti Claude
Code.

### Il sistema: 6 specialisti + 1 orchestratore

Da un singolo URL e un solo prompt in linguaggio naturale ("attiva il mio marketing team su
questo URL"), il sistema attiva sei agenti specialisti in parallelo più un orchestratore:

```
01 STRATEGA            -> vota Messaggio e Crescita: "prova dei 5 secondi",
                           fonti di traffico (Search/Instagram/LinkedIn/YouTube)
02 ANALISTA CONCORRENZA -> vota Concorrenza: recensioni vs concorrenti reali
                           (P.IVA -> Registro Imprese -> ATECO -> concorrenti)
03 SPECIALISTA SEO      -> vota Trovabilità: titoli pagina, posizione SERP
04 COPYWRITER           -> senza voto, dimostra: 3 testi più deboli, prima/dopo
05 ESPERTO CONVERSIONI  -> vota Conversione: percorso cliente click-per-click
06 MEDIA BUYER          -> senza voto, verdetto: ads di oggi sono soldi buttati?
```

L'architettura sul filesystem è organizzata in una cartella con 11 skill (una per ogni
deliverable — `marketing-ads`, `marketing-seo`, `marketing-funnel`, ecc.) e una sottocartella
`squadra/` con i file `.md` di ogni agente reale (frontmatter `name/description/tools` più il
corpo delle istruzioni). L'autore descrive il pattern con una frase che riassume bene l'approccio:
*"ho creato un sacco di skill e poi ho fatto qui una mini squadra."*

### La regola di squadra: tre righe

Tre regole, esplicitamente dichiarate a schermo in un banner ("OGNI VOTO HA DIETRO UNO
SPECIALISTA"), governano ogni output del team:

```
1. Ogni voto cita il sito
2. Mai numeri inventati
3. Difetti provati nel browser vero
```

> "Ogni voto cita il sito, mai numeri inventati, difetti provati nel browser vero." [banner di
> squadra, `yJOCyyP77bA`]

### Il pattern riusabile: verifica dal vivo contro il fetch statico

L'elemento più interessante, dal punto di vista del *processo* di controllo qualità, è che il
sistema non si accontenta dei dati raccolti da una lettura statica del sito (fetch), ma esegue un
passaggio di verifica in un browser realmente renderizzato (Chrome via MCP) prima di dichiarare
qualunque difetto. Il video mostra cinque casi in cui questo passaggio **cambia il risultato**:

| Claim dal fetch statico | Verifica nel browser renderizzato |
|---|---|
| "hreflang assenti" | **SMENTITO**: it/en/x-default presenti nel DOM |
| "categorie non tradotte" | **SMENTITO**: tradotte via JS, invisibili al fetch |
| "spedizioni solo Italia" | **SMENTITO**: "SHIPMENTS IN ITALY AND EU" nel checkout |
| zero widget recensioni | **CONFERMATO** dal vivo (home/collezione/2 schede) |
| telefono non cliccabile | **CONFERMATO** dal vivo |

Il test è stato eseguito interamente: click, aggiunta al carrello, checkout raggiunto e abbandonato
prima del pagamento — sull'e-commerce reale del cliente usato come caso nel video. Il risultato
pratico di questa verifica non è cosmetico: il voto sulla Conversione è stato **ricalcolato
dentro lo stesso deliverable**, da 6.0 a 6.5, dopo che il passaggio dal vivo ha scoperto elementi
che il fetch statico non poteva vedere — ritiro in negozio, checkout ospite con pagamento express,
opzione "richiedi la taglia".

### La regola "mai concorrenti inventati"

La seconda regola riusabile riguarda la ricerca competitor, e segue una catena di verifica
tracciabile:

```
URL cliente -> scraping P.IVA -> Registro Imprese -> codice ATECO
            -> concorrenti REALI nella stessa nicchia/città (mai inventati)
            -> confronto recensioni (numero E contenuto, non solo stelle)
```

Applicata al caso reale mostrato nel video, questa catena ha prodotto **6 concorrenti reali con
fonte citata** (Google Places + ricerca web), incluso un concorrente — Musto Calzature —
sconosciuto persino all'autore del video, che commenta:

> "Onestamente non ho idea di chi siano, ma a quanto pare va meglio di noi su quasi tutto." [sul
> concorrente Musto Calzature, `yJOCyyP77bA`]

Questo dettaglio ha valore probatorio nel racconto della fonte: dimostra che il sistema non si è
limitato a confermare ciò che l'operatore umano già sapeva, ma ha trovato qualcosa che l'operatore
stesso non conosceva.

### L'output: un deliverable doppio, pronto per il cliente

Il processo produce due artefatti distinti:

- **HTML aggregato** (`TUTTI-I-DELIVERABLE.html`, uso interno) — 8 tab: Pagella, Mappa
  Opportunità, Campagne Ads, Funnel, Piano SEO, Sequenza Email, Calendario Social, Piano 90
  giorni.
- **PDF cliente** (`REPORT-CLIENTE.pdf`) — cover con voto complessivo (5.6/10), radar chart a 5
  assi contro il concorrente principale, confronto testa a testa con 4 concorrenti, matrice di
  priorità 2×2, e una pagina finale dedicata a "Il primo passo": una sola azione da fare per
  prima, non una lista indistinta di raccomandazioni.

### I numeri del caso mostrato

- Tempo totale dal link incollato al piano completo: **20 minuti**
- Voto finale del caso (calzature): **5.6/10** — scomposto in Messaggio 6.0, Trovabilità 5.0,
  Conversione 6.5, Concorrenza **3.5 (rosso)**, Crescita 7.0
- 6 concorrenti reali con fonte: Turci (4.9/1176 recensioni), Velasca (4.8/542), Musto (4.8/406),
  GHIGO (4.4/476), Walter (4.6/299), Pepperina (4.8/187)
- Volumi di ricerca mensili non intercettati dal cliente, trovati dal piano SEO: sneakers donna
  90.500, ballerine donna 60.500, sandali donna 40.500
- Budget ads raccomandato nel piano: **1.200 €/mese** (40 €/giorno)

Due frasi dell'autore riassumono l'intento dietro il sistema, al di là del singolo caso mostrato:

> "Basta incollare il sito di una piccola impresa e in un paio di minuti sei agenti restituiscono
> un'analisi completa." [`yJOCyyP77bA`]

> "Il nostro obiettivo non è mai fare one shot, ma è avvicinarci quanto più possibile ad un output
> di qualità." [`yJOCyyP77bA`]

Questa seconda frase è importante da leggere insieme alla Sezione 3.5: la fonte stessa dichiara
che il processo normale prevede iterazioni, non un colpo unico — un'ammissione che rende ancora
più rilevante la domanda del prossimo blocco, cioè chi controlla che l'output di un run "pulito"
come quello mostrato nel video sia davvero pronto per il cliente.

---

## 3.5 Chi giudica il lavoro non è chi lo fa

### Il principio cardine

La terza fonte di questo capitolo parte da un problema diverso, ma collegato: anche un team ben
costruito — umano o di agenti — può dichiarare pronto un lavoro che non lo è, semplicemente
perché chi ha costruito e chi ha verificato condividono lo stesso punto di vista. La fonte lo
scrive a lavagna, in maiuscolo, come principio cardine dell'intero video:

```
CHI COSTRUISCE ≠ CHI GIUDICA
```

Il meccanismo mostrato: il piano (o il codice) lo scrive Claude, un secondo modello di famiglia
diversa lo contesta con una revisione avversariale, Claude produce una versione 2, il ciclo si
ripete finché il secondo modello non ha più obiezioni — sempre con una revisione umana nel mezzo,
non come sostituto di essa:

> "non vogliamo essere pipecoder seriali... altrimenti quello che abbiamo costruito diventa un
> mostro incontrollabile." [`T7PPX5M6Puo`]

### Lo strumento mostrato: il plugin Codex dentro Claude Code

La fonte dimostra il principio con un plugin ufficiale OpenAI ("Codex Plugin") installato dentro
Claude Code, che espone cinque comandi:

| Comando | Cosa fa | Flag |
|---|---|---|
| `/codex:review` | Legge solo le modifiche non committate su Git, non indirizzabile | — |
| `/codex:adversarial-review` | Come review, ma puntabile su un target (codice o piano) | `--background` |
| `/codex:rescue` | Indaga/corregge un'app o un bug, anche già committata | `--background` `--wait` `--resume` `--fresh` `--model` `--effort` |
| `/codex:transfer` | Porta la conversazione Claude Code dentro Codex, continuando da dove si era | — |
| `/codex:status` / `/codex:result` | Stato dei job in background / report completo a fine job | richiede ID task |

Due pattern d'uso emergono dal video:

- **Pattern 1** — l'app è pronta → `/codex:review` (o `/codex:rescue` se già committata) → un
  umano revisiona i finding → Claude sistema → si va online.
- **Pattern 2** — il piano è scritto con Claude → `/codex:adversarial-review` sul piano → le
  critiche tornano a Claude → piano v2 → il ciclo continua fino a convergenza → **solo allora** si
  comincia a scrivere codice.

### I tre casi reali

Il cuore probatorio della fonte sono tre casi reali dell'agenzia dell'autore (Martes AI, 65+
aziende clienti e 75+ soluzioni AI in produzione al momento del video), in cui Claude Code aveva
già dato un giudizio positivo — sul codice o sul piano — prima che Codex trovasse il problema:

| Caso | Cosa aveva già dichiarato Claude | Cosa ha trovato Codex |
|---|---|---|
| **MaReply** (clone ManyChat, gestisce account Instagram di clienti) | "pronta per essere mandata in produzione" | **2 falle Alte**: autenticazione via email/password senza verifica email (account dirottabile tramite invito); DM duplicati per assenza di un claim atomico (spam, doppio consumo di budget Meta, rischio phishing) |
| **Form candidature** (Cloudflare + Airtable, dati personali di candidati) | nessun audit di sicurezza eseguito prima | **4 finding Alti** (endpoint pubblico senza rate limiting/CAPTCHA, upload completamente fidato lato server, nessun limite alla dimensione dei campi, librerie di terze parti senza SRI/CSP) più 10 medi e 1 informativo |
| **Piano clone Bitly** (Cloudflare Workers + D1, prima ancora di scrivere codice) | piano scritto e presentato come pronto per lo sviluppo | **1 critical** (le API di statistiche/cancellazione non verificano la proprietà del link: chiunque può cancellare link altrui) più **2 high** (redirect 301 cachato che rompe il tracciamento dopo una cancellazione; contatore gonfiato da eventi duplicati) |

Sul caso Bitly, in particolare, Claude — ri-interrogato dopo le obiezioni di Codex — riconosce di
aver ripetuto un errore già noto nella storia di quel prodotto: aveva proposto un redirect
**301** (permanente, cachato indefinitamente dai browser), lo stesso errore che **Bitly stesso
aveva corretto passando a 302 nel 2016**. Riconosce inoltre la fondatezza della maggioranza delle
obiezioni ricevute:

> "4 obiezioni su 5 hanno un nucleo valido." [Claude, ri-interrogato sulle obiezioni Codex al
> piano Bitly, `T7PPX5M6Puo`]

E sul caso MaReply, l'autore commenta con una frase che riassume il rischio concreto di fidarsi di
un solo giudice:

> "Considerate che Claude Code mi aveva detto che questa applicazione era pronta per essere
> mandata in produzione... meno male che ho chiamato Codex." [`T7PPX5M6Puo`]

### Il costo del secondo giudice

La fonte affronta anche la domanda più ovvia — quanto costa aggiungere un secondo modello che
legge tutto ma scrive raramente:

- Solo Claude ($200/mese): "nessuno che lo controlla"
- Solo Codex ($200/mese): "nessuno che serve bene"
- Combo consigliata: Claude Max $100 + Codex/ChatGPT Plus $20 = **$120/mese**
- Alternativa gratuita per testare: piano ChatGPT Free (Codex incluso, con limiti stretti)
- Requisito minimo lato Claude per la combo: piano Pro $20/mese

> "Venti dollari in più. Non il doppio. Perché qui Codex legge e critica, e scrive quasi mai.
> L'auditor costa molto meno che generare." [lavagna finale sui costi, `T7PPX5M6Puo`]

### Il limite dichiarato dalla fonte stessa

La fonte non presenta questo pattern come una legge universale, e lo dichiara esplicitamente:
tre casi aneddotici di una sola agenzia, nessun benchmark quantitativo aggregato su un campione
più ampio, nessun tasso di falsi positivi misurato. `/codex:review` non viene mai eseguito dal
vivo nel video (solo `rescue` e `adversarial-review`), e non viene mostrata alcuna gestione del
disaccordo oltre il caso Bitly (dove 4 obiezioni su 5 vengono accettate) — resta aperta la domanda
di cosa succeda se i due modelli restano in disaccordo per più cicli consecutivi. La dimostrazione
è inoltre limitata a un solo ambiente (Mac + VS Code).

Un'ultima nota di raffronto, che la fonte stessa registra: un'agenzia che ha già un passaggio di
revisione indipendente nel proprio ciclo di lavoro — un secondo controllo dopo chi produce, prima
che il lavoro raggiunga il cliente — non è per questo esente dal problema dimostrato nei tre casi,
se quel secondo controllo gira sulla **stessa famiglia di modello** di chi ha prodotto il lavoro.
Il principio dimostrato non riguarda "quale IA scrive meglio", ma il fatto che un giudice della
stessa famiglia tende a condividere i punti ciechi dell'autore — a prescindere dal tier o dal
livello di reasoning usato per il controllo.

---

## 3.6 Chiusura: tre livelli dello stesso problema

Le tre fonti di questo capitolo, lette insieme, coprono tre domande che un'agenzia deve rispondere
in sequenza dopo aver chiuso un cliente, e che restano valide indipendentemente da quanto lavoro
venga effettivamente svolto da agenti AI invece che da persone:

- **Quanto far pagare, e su cosa** — la matrice DIY/DWY/DFY × Tempo/Unità/Risultato e la golden
  rule del 30% danno un modo per capire se il prezzo fissato è quello giusto, guardando al
  comportamento reale dei lead invece che a un numero scelto a tavolino.
- **Come consegnarlo in modo ripetibile** — il flowchart di fulfillment, i cinque punti
  obbligatori della kickoff call, la policy sulle credenziali e la regola di assunzione
  "CTO prima del commerciale" trasformano la consegna da un'esperienza diversa per ogni cliente a
  un processo che regge la scala. Il team di 6 agenti marketing mostra concretamente cosa
  significa "scalare la consegna senza scalare le ore umane": lo stesso output di qualità in 20
  minuti invece che in giorni, con regole esplicite ("mai numeri inventati", "mai concorrenti
  inventati", "difetti provati nel browser vero") che sostituiscono la supervisione umana
  costante con vincoli scritti nel sistema stesso.
- **Chi verifica che sia davvero pronto** — il principio "chi costruisce non è chi giudica"
  chiude il cerchio: un processo di consegna ripetibile e un prezzo corretto non bastano se
  l'ultimo controllo di qualità condivide gli stessi punti ciechi di chi ha prodotto il lavoro.
  Nei tre casi mostrati dalla fonte, un secondo giudice di famiglia diversa ha trovato falle di
  gravità alta o critica su lavoro già dichiarato pronto — non una volta, ma tre su tre.

Nessuna delle tre fonti, presa da sola, risolve il problema della scala. Un prezzo corretto senza
un processo di consegna ripetibile produce un'agenzia che vende bene ma consegna in modo
inconsistente. Un processo di consegna ripetibile senza un controllo qualità indipendente produce
un'agenzia efficiente che consegna comunque, di tanto in tanto, un lavoro difettoso dichiarato
pronto. E un controllo qualità indipendente, da solo, non genera né il prezzo né il processo su
cui esercitarsi. È la combinazione delle tre leve — prezzo, processo, controllo — a rendere
un'agenzia capace di crescere senza rompersi, coerentemente con la nota di chiusura della prima
fonte di questo capitolo: l'agenzia AI, quasi sempre, non è il punto di arrivo ma lo step che
insegna a costruire ogni pezzo di questo sistema.
