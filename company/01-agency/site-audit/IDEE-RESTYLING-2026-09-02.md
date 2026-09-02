---
Type: PROJECT
Status: Active
Tags: #agency #landing #restyling #cro #idee #digital-empire
Created: 2026-09-02
Last updated: 2026-09-02
---

# IDEE PER IL SITO AGENCY — grezzo per il piano

Base: [AUDIT-2026-09-02.md](AUDIT-2026-09-02.md) (misure sul nostro sito) + i 9 report dello studio Andrei Pascu (`competitor/Andrei Pascu/site-study/reports/`).
Ogni idea ha: **cosa · dove · perché (con la fonte misurata) · costo**.
Costo: **S** = meno di 1h · **M** = mezza giornata · **L** = 1-2 giorni · **XL** = più di 2 giorni.

---

## A. SEZIONI NUOVE DA AGGIUNGERE

### A1 · Riga di qualificazione sotto la CTA dell'hero — **S**
**Dove:** `hero.tsx`, subito sotto il bottone principale, 15px opacità 50%.
**Cosa:** *"Lavoriamo con chi fattura già e perde ore in operatività manuale. Se stai ancora validando il prodotto, non siamo noi."*
**Perché:** `apsales.eu` mette *"Solo per B2B e B2B SaaS che investono da €5.000 a €100.000 al mese in ads"* esattamente lì. Fa tre cose insieme: squalifica, dichiara il livello di prezzo senza dirlo, e prova che esistono clienti in quella fascia. Noi oggi non filtriamo nessuno e bruciamo mezz'ora di call su ogni curioso.

### A2 · Tabella comparativa a 4 colonne — **M**
**Dove:** sezione nuova, subito dopo `Competitors` (y≈5.000).
**Cosa:** righe = criteri d'acquisto; colonne = **Digital Empire · SaaS a canone · Freelancer · Assumere in casa**. Simboli `✓ / ✕ / ~`.
Righe proposte: *Il codice è tuo* · *Funziona se smetti di pagare* · *Tempo al primo output* · *Chi ti risponde quando si rompe* · *Costo a 24 mesi* · *Serve un tecnico interno* · *Personalizzato sul tuo brand*.
**Perché:** è la sezione più forte di `apsales.eu`. Non confronta con concorrenti nominati ma **con le alternative reali di acquisto** — che è la decisione che il cliente sta davvero prendendo.
**Dettaglio che la rende credibile:** concedere **un** ✓ a un'alternativa (es. *Costo iniziale → Freelancer: ✓ più basso*). Un punto regalato converte la tabella da propaganda a confronto.

### A3 · Caso studio unico, misurato — **L** (contenuto, non codice)
**Dove:** `results.tsx`, che è già pronto ad accoglierlo (gli array sono vuoti per scelta).
**Cosa:** un solo caso, formato fisso: **Situazione → Cosa abbiamo installato → Baseline → Risultato misurato → Tempo**. Anche interno (Digital Empire come cliente di se stessa), dichiarato come tale.
**Perché:** è l'unico buco che ha anche `apsales.eu`. Chi pubblica per primo un numero verificabile vince il confronto sull'asse su cui entrambi promettiamo metodo. **Questa è la singola cosa a più alto impatto di tutta la lista.**

### A4 · "Il sistema, dal vivo" — demo registrata al posto del placeholder — **M**
**Dove:** sostituisce il riquadro `16:9 · PLACEHOLDER` in `results.tsx`.
**Cosa:** 3-5 minuti di schermo reale: lead che entra → qualificazione → notifica Slack → carosello generato → file su Drive. Nessuna slide, nessuna voce impostata.
**Perché:** il copy accanto promette già *"in chiamata ti mostriamo il sistema che gira in 5 minuti"*. Mostrarlo prima della chiamata sposta la prova dove serve. E oggi al suo posto c'è la parola "PLACEHOLDER", che dice al visitatore che la pagina non è finita.

### A5 · Campione gratuito: "Mappa dei tuoi colli di bottiglia" — **L**
**Dove:** nuova sezione a ~40% pagina + un secondo punto di ingresso nel footer.
**Cosa:** un form a **un solo campo** (email) che consegna un audit breve dell'operatività: 5 domande, output un PDF di 2 pagine con i 3 task più costosi e cosa automatizzerebbe un sistema. Micro-copy: *"Dimmi la mail, te la mando adesso."*
**Perché:** dal `manuale-del-copywriter` di Andrei: quando non hai prova sociale, **il campione del prodotto è la prova**. Lui vende un ebook regalando pagine vere, e per questo la sua pagina è lunga la metà delle altre. Noi oggi abbiamo un unico gradino: chiamata o niente. Questo apre il gradino intermedio e ci costruisce una lista.

### A6 · "Cosa NON facciamo" — **S**
**Dove:** dopo `NoFluff`.
**Cosa:** tre righe secche: *non facciamo ads · non facciamo social media management · non facciamo consulenza a ore*. E il perché in una riga: *facciamo una cosa sola e la facciamo per intero*.
**Perché:** `apsales.eu` ha *"Facciamo solo due cose. Per scelta."* e una FAQ intera (*"Fate anche ads, social, SEO?"*) che esiste **per dire di no**. La restrizione di scopo è la prova di competenza più economica che esista.

### A7 · Blocco "Il rischio, scritto per intero" — **S**
**Dove:** accanto alla garanzia.
**Cosa:** cosa succede se il sistema non regge, chi paga cosa, in quanti giorni, e i due limiti veri (serve un VPS tuo, servono gli accessi). Con i numeri: 30 giorni, rimedio, poi rimborso.
**Perché:** la nostra garanzia è **già più forte** di quella di AP Sales (due gradini contro uno) ma è raccontata di sfuggita. Scritta per intero diventa un argomento di vendita, non una rassicurazione.

### A8 · Prezzo: "Cosa costa NON farlo" — **S**
**Dove:** dentro `pricing-roi`, accanto alla matematica dei 20 mesi.
**Cosa:** tre righe: *2-3 ore al giorno di outreach a mano = X ore/anno* · *ogni lancio 2-3 settimane di copy* · *quanto vale la tua ora*. Con i numeri lasciati calcolare al lettore.
**Perché:** la matematica contro il SaaS c'è già ed è il pezzo più solido della pagina. Manca il confronto con **il costo del tuo tempo**, che è quello che il compratore sente davvero.

### A9 · Micro-sezione "Come lavoriamo con te" (il tuo tempo) — **S**
**Dove:** dentro `Clarity`/roadmap.
**Cosa:** *"Ti servono 2 ore in tutto: 30 minuti di call, 1 ora di brief, 30 minuti di formazione. Il resto lo facciamo noi."*
**Perché:** `apsales.eu` ha la FAQ *"Quanto tempo devo dedicarci io?"* ed è quella che chiude i clienti B2B già oberati. Il costo non monetario è l'obiezione silenziosa numero uno.

### A10 · Blocco "Chi c'è dietro" con volti veri — **M**
**Dove:** sezione team, già esistente ma senza foto.
**Cosa:** tre ritratti veri, stesso formato, stesso trattamento (b/n o grana coerente).
**Perché:** su `apsales.eu` l'unica foto reale della pagina è il ritratto del founder, ed è piazzata nell'unica sezione a fondo chiaro. Noi abbiamo tre nomi e zero facce: su un servizio da €8.000 le facce contano.

### A11 · Barra "Loro / Noi" a fine hero — **S**
**Dove:** subito sotto l'hero, prima della sezione tre sistemi.
**Cosa:** una riga sola, tre coppie: *Canone mensile → Pagamento unico* · *Codice loro → Codice tuo* · *Mesi → 7 giorni*.
**Perché:** ancoraggio immediato in una riga, prima che la pagina cominci a spiegare. Costa 20 righe di JSX.

---

## B. SEZIONI DA MODIFICARE

### B1 · Hero: mettere in sicurezza l'H1 — **S**
`clamp(82px, 13.5vw, 148px)` → `clamp(46px, 13.5vw, 148px)`. Oggi "operatività" esce dallo schermo a 390px: **verificato sullo screenshot `mobile-01.png`**. Stesso controllo sulle altre due righe e sui numeri a 130px.

### B2 · "Tre sistemi": rendere leggibile il testo sul fondo — **S/M**
Il PNG `vsl-bg.png` (3,1 MB) mangia occhiello, riga di rassicurazione e barra "ALL SYSTEMS ONLINE". Due strade: velo scuro `rgba(10,10,10,.72)` sopra l'immagine, oppure togliere l'immagine e tenere solo la grana. **In più:** convertire in WebP (da 3,1 MB a ~200 KB).

### B3 · Stack tecnico: da 12 card gradiente a griglia sobria — **M**
Oggi 12 card con gradiente arancione-rosso e testo nero sopra: contrasto sotto soglia, e tutte identiche. Nuova forma: **griglia di etichette monospaziate** (`CLAUDE` `GMAIL API` `PLAYWRIGHT` `PROXY` `n8n` `SUPABASE`…) su fondo neutro, con la descrizione che appare all'hover o in un accordion.
**Perché:** su `apsales.eu` il font più usato è **DM Mono, 240 volte**, tutto in micro-etichette tecniche. Il monospaziato dice "qui si misura" senza scriverlo. E 12 chip pesano meno di 12 card, sia visivamente sia in scroll.

### B4 · Tavolozza: da 77 colori a uno + opacità — **M/L**
Oggi: 77 colori di testo, 42 sfondi, 5 famiglie cromatiche (i deliverable sono rosso/blu/verde, il Second Brain blu/viola, i sistemi rosso/ambra/blu). Il design system ne dichiara **uno**.
Regola nuova: **arancione `#fb4604` + argento + bianco a 12 livelli di opacità**. Il colore distingue i prodotti solo se ogni prodotto ne ha **uno stabile su tutta la pagina** — altrimenti è rumore.
**Perché:** `apsales.eu` costruisce tutta la gerarchia con **un colore e 19 opacità**. È il modo più economico di sembrare un sistema.

### B5 · Raggi: da 19 a 2 — **S**
Tenere `12px` (card) e `9999px` (pill). Eliminare gli altri 17, compreso il `3.35544e+07px` che Tailwind genera da `calc(infinity*1px)`.

### B6 · Le due CTA gemelle a y=1943 — **S**
Oggi due bottoni affiancati, stessa destinazione, stili diversi. Tenerne **uno**: arancione pieno, con la riga di rassicurazione sotto (`30 min · gratuita · zero impegno`) invece che dentro il bottone.

### B7 · CTA con testo che cambia in base alla sezione — **S**
Oggi 8 CTA quasi identiche (*Prenota una Chiamata Gratuita*). Nuove:
- dopo il problema → **"Voglio smettere di farlo a mano"**
- dopo i prezzi → **"Installa il sistema"**
- dopo il team/storia → **"Voglio parlare con chi lo costruisce"**
- finale → **"Vediamo se ha senso lavorare insieme"**
**Perché:** dal `manuale-del-copywriter`: le CTA non si ripetono mai uguali, e dopo il blocco biografico parlano del **rapporto**, non del prodotto (là: *"Voglio imparare da te"*). L'ultima è la CTA condizionale e bilaterale di `apsales.eu`: ammettere che il no è possibile abbassa il rischio percepito più di uno sconto.

### B8 · Sticky CTA: alleggerire su mobile — **S**
Oggi copre una fascia fissa su 390px e il link "Prezzi" al suo interno è nascosto proprio lì (`hidden sm:inline-flex`). Renderla più bassa su mobile, o farla comparire solo dopo la sezione prezzi.

### B9 · Togliere la scarsità inventata — **S**
*"La finestra è aperta per altri 12 mesi. Dopo è chiusa."* → sostituire con la posizione opposta: **"Nessun countdown, nessuna finta scadenza. Il prezzo è quello."**
**Perché:** `apsales.eu` chiude la pagina con *"Nessun impegno. Niente countdown finti."* e mette *"Timer finti, recensioni finte, dark pattern → Mai"* dentro la tabella comparativa. **Stiamo perdendo su un terreno che potremmo vincere, e per una riga sola.** Un'affermazione morale non verificabile diventa una specifica verificabile: apri la pagina e guarda se c'è un countdown.

### B10 · Rendere coerenti i numeri su di noi — **S**
Convivono *"50+ sistemi reali"*, *"agenzia nata a Gennaio 2026"*, *"su decine di implementazioni non è mai successo"*. Lette di fila non tornano. Una formulazione sola, vera e verificabile, ripetuta identica ovunque.
**Perché:** nell'ecosistema Andrei ho misurato **otto cifre diverse per quattro metriche** — è il difetto che gli ho contato addosso. Non possiamo averlo anche noi.

### B11 · Footer: togliere il disclaimer Facebook — **S**
*"Questo sito non fa parte di Facebook…"* è copiato dai funnel info-prodotto americani. Su una pagina B2B che vende infrastruttura segnala "funnel", non "fornitore tecnico". Sostituire con P.IVA, sede, contatto reale — come fa `apsales.eu`, che nel footer mette dati fiscali e link legali veri.

### B12 · Un colore intero per una parola sola — **S**
Scegliere **la** parola che decide il click (es. *gratuita* nella CTA, o *tuo* in "il codice è tuo") e darle un colore che non compare da nessun'altra parte.
**Perché:** sul `manuale-del-copywriter` il verde `#51b216` compare **una volta sola in 11.067px**, sulla parola *"gratuita"*. È la mossa cromatica più efficiente che abbia misurato in tutto l'ecosistema.

### B13 · Il paragrafo "Ascolta bene" va accorciato — **S**
È forte ma dura troppo. Tenere le tre righe che colpiscono (*"Ti svegli già in ritardo sul lavoro che conta davvero"*, *"Loro hanno qualcosa che lavora mentre dormono"*, *"Non è fortuna. È un sistema."*) e tagliare il resto.

### B14 · Sezione Competitor: citare il cliente, non descriverlo — **S**
Riscrivere le tre righe del problema come **frasi tra virgolette che il cliente ha già detto**: *"lo faccio a mano perché nessuno lo fa come voglio io"*, *"ci ho provato con Zapier, si è rotto"*, *"non ho tempo di seguirlo".*
**Perché:** `apsales.eu` scrive *"la risposta di tutti è «spendi di più»"* e *"le modifiche si decidono con «a me piace il blu»"*. Citare invece di descrivere è ciò che separa un copy scritto dopo le call da uno scritto a tavolino.

---

## C. SEZIONI DA TAGLIARE O FONDERE

### C1 · I tre sistemi sono raccontati cinque volte — **M**
`systems-showcase` → `service-deep` → `outreach-inside` / `content-output` / `second-brain-inside` → `pricing` → `about-story`. Fondere in **due** livelli: una vetrina (cosa fa) + un approfondimento espandibile (cosa c'è dentro).
**Guadagno stimato:** da 38.683px a ~24.000px senza perdere una singola informazione.

### C2 · Cancellare le 4 sezioni morte — **S**
`mastery-map.tsx`, `power-pillars.tsx`, `roadmap.tsx`, `service-cards.tsx`: **829 righe** mai renderizzate. O si usano o si eliminano.

### C3 · Ridurre le parole da 6.666 a ~3.500 — **L**
33 minuti di lettura sono fuori scala: `apsales.eu` ne ha un quarto e vende lo stesso ticket. Il taglio esce quasi tutto da C1.

---

## D. GRAFICA — idee che alzano il livello

### D1 · Diagramma del flusso animato (INPUT → SISTEMA → OUTPUT) — **L**
Sostituisce le tre card statiche della vetrina: una linea che si accende, i nodi che si illuminano in sequenza, i tre output che compaiono. GSAP è già installato.

### D2 · Heatmap/wireframe come oggetto grafico — **M**
`apsales.eu` mostra un wireframe con heatmap blu luminescente per dire "noi guardiamo i dati". La nostra versione: **la dashboard vera** in mockup, con i lead che entrano.

### D3 · Card verticali collassate — **M**
Una card aperta e due chiuse a 64px con il titolo ruotato a 90° (è il componente della sezione team di `apsales.eu`): densità alta in orizzontale, zero carosello, zero JS.

### D4 · Etichette monospaziate ovunque ci sia un dato — **S**
`312 MSG/GIORNO`, `99.8% UPTIME`, `7 GG`, `€0`. Tutte in mono, tutte con lo stesso trattamento.

### D5 · Una sola sezione a fondo chiaro, nel punto giusto — **S**
Oggi l'alternanza nero/argento è frequente. `apsales.eu` usa **una sola** inversione in tutta la pagina, ed è quella del team. Ridurre le inversioni a 2-3 rende ognuna un evento.

### D6 · Divisori con un'idea, non solo un filetto — **S**
I `divider-silver-orange` attuali sono decorativi. Farne dei **respiri con una riga di testo** (un numero, una frase secca) — così ogni divisore vende invece di separare e basta.

### D7 · Grana: tenerla, ma alleggerirla dove c'è testo piccolo — **S**
`grain-fine` a opacità 0.55 + hard-light su tutta la pagina rende faticoso il testo a 12-14px. Ridurla nelle sezioni dense.

### D8 · Anteprima social (Open Graph) — **S**
Oggi manca del tutto: chi condivide il link vede un rettangolo vuoto. Immagine 1200×630 con headline + `#fb4604`.

---

## E. FUNNEL E CONVERSIONE

### E1 · Pagina di prenotazione dedicata all'agenzia — **M**
Oggi tutte le CTA vanno su una pagina intitolata **"Call Strategica 1:1 | Claude Code Mastery"**. Serve una pagina con il brand giusto, che ripeta l'offerta e mostri l'agenda.

### E2 · Tracciamento, prima di ogni altra cosa — **S**
GA4 + Microsoft Clarity (heatmap e registrazioni). Oggi **non sappiamo quanti arrivano né dove si fermano**: la prossima analisi la devono fare i dati, non io.
**Perché fa ridere:** vendiamo sistemi che misurano, su una pagina che non misura niente.

### E3 · Eventi sulle CTA — **S**
Un evento per ogni CTA con il nome della sezione. Serve a sapere **quale sezione converte**, non quante conversioni ci sono.

### E4 · Uscita dal `noindex` + sitemap + robots — **S**
`layout.tsx:26` dichiara `index: false, follow: false` ed è nel build di produzione.

### E5 · Secondo gradino di conversione — **M**
Oggi l'unica azione possibile è la chiamata. Aggiungere il campione (A5) e un terzo: **"mandami la proposta senza call"** per chi odia le chiamate.

### E6 · Prezzo visibile anche nell'hero — **S**
*"Da €2.500. Pagamento unico."* sotto la CTA. Squalifica in anticipo e alza la qualità delle call.

---

## F. TECNICO

### F1 · `vsl-bg.png` 3,1 MB → WebP — **S**
Unico asset pesante, servito senza ottimizzazione (`images: { unoptimized: true }`).
### F2 · Open Graph, Twitter card, `sitemap.xml`, `robots.txt`, dati strutturati `Organization` — **S**
### F3 · Contrasto: audit WCAG sulle sezioni con testo su gradiente — **M**
### F4 · Lazy-load delle sezioni sotto la piega — **M** (38.000px di DOM montati tutti insieme)
### F5 · Test mobile reale a 390 / 414 / 360px — **S** (l'H1 è solo il primo di probabili overflow)

---

## G. LE 8 CHE FAREI PER PRIME

| # | Idea | Perché prima |
|---|---|---|
| 1 | **E4** togliere il `noindex` | ogni giorno in più è traffico perso per sempre |
| 2 | **B1** fixare l'H1 mobile | il primo elemento è rotto sul dispositivo maggioritario |
| 3 | **E1** pagina di prenotazione giusta | lo strappo peggiore, e succede quando hanno già deciso |
| 4 | **E2** tracciamento | senza, ogni modifica successiva è un'opinione |
| 5 | **A3** un caso studio misurato | l'unico buco che ha anche il concorrente |
| 6 | **A2** tabella comparativa | la sezione più forte del competitor, e noi non ce l'abbiamo |
| 7 | **B9** togliere la scarsità finta | perdiamo un terreno che potremmo vincere, per una riga |
| 8 | **A1** riga di qualificazione | smette di bruciare call sbagliate da subito |
