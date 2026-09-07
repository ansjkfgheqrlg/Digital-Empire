---
Type: SYNTHESIS
Status: Active
Tags: #competitor #andrei-pascu #apsales #copy #teardown #cro #home #concorrente-diretto
Created: 2026-09-07
Last updated: 2026-09-07
---

# Teardown di copy — apsales.eu (home)

**apsales.eu**, home dell'agenzia di Conversion Rate Optimization di Andrei Pascu, **concorrente
diretto** dell'agenzia CRO di Digital Empire. Cattura `13-apsales-v2`, 12.565px, 14 sezioni (13
distinte), 537 blocchi di copy. Contesto già acquisito e non ripetuto qui: lo stack (React + TanStack
Start), i token OKLCH→HEX (`--brand-blue` `#0062ff`, `--brand-void` `#0a0a0b` quasi identico al nostro
`--ink-2`), il componente `Ascii`, le 14 tavole visive per sezione — tutto in
`13-apsales-STACK-E-TOKEN.md` e `13-apsales-ATLANTE.md`.

Questo teardown guarda solo il copy della **home**, non delle tre pagine di servizio già smontate in
`18-20-apsales-servizi-COPY.md`. Dove quel rapporto stabilisce una regola generale (l'asimmetria di
prezzo, il paragrafo "vincolo sei tu"), qui la verifico contro la home invece di ripeterla — e la home,
essendo un livello sopra Servizi/Landing/Consulenza nel funnel, offre un test indipendente.

---

## DELTA ALLA FABBRICA

**CANONE:** l'asimmetria di prezzo del report 18-20 (*"il prodotto a listino mostra il prezzo ovunque
appaia; il prodotto su misura mostra il modello ma mai la cifra"*) **si conferma e si estende un
livello più in alto**: sulla home non compare **nessun prezzo**, nemmeno quello della Consulenza
(€610) che le sue stesse pagine figlie mostrano tre volte. L'unica traccia è la domanda FAQ *"Quanto
costa?"* [y=10239], la cui risposta non è stata catturata (accordion chiuso, e il campione `jsonld` di
`scheda.json` espone solo la prima domanda del FAQPage schema, *"Cos'è la CRO?"*, troncando le
successive). Regola aggiornata per la Fabbrica: *più ci si allontana dal prodotto specifico e più si
sale verso la pagina che deve smistare il traffico, più il prezzo sparisce — non solo quando il
prodotto è su misura, ma strutturalmente, a ogni livello sopra la pagina di vendita diretta.*

**PATTERN:** la fila di **10 loghi cliente reali** (Vidiren, LSP, AGL Aste Immobiliari, Autos EU,
Oltreset, Altlife Agency, BM Ecom, Pearl West Brands, Pets are Kids, Lecca Milano, M.P. Edile) compare
a y=1687 [sezione i=3], **prima** che la pagina nomini un solo problema (il problema arriva a y=2559,
quasi 900px dopo). Nella formula a 11 tappe della famiglia out* la prova/autorevolezza è la tappa 9,
molto dopo l'agitazione (tappa 2): qui l'ordine è invertito, la fiducia anticipa il problema invece di
seguirlo. Pattern riusabile per la Fabbrica: *quando la pagina è una home "di ingresso" (non una
landing di prodotto), la fila di loghi cliente può precedere l'agitazione invece di seguirla — funziona
da lasciapassare per continuare a leggere, non da chiusura dell'argomentazione.*

**GATE:** stessa cifra di follower, due numeri diversi sulle due proprietà del brand catturate lo
stesso giorno (2026-09-07). Qui: *"follower organici 250.000"* [y=8482], senza piattaforma
specificata. Su `claude-speedrun.com` (bio di Andrei, vedi `12-claude-speedrun-COPY.md` §LE PROVE):
*"270K+ follower"*, specificato su TikTok. Scarto: 20.000 unità, 7,4%. Il gate per la Fabbrica resta
quello già scritto nel gemello: *se una cifra ricorre su più proprietà dello stesso brand, deve essere
identica o la differenza va giustificata in riga (piattaforma, data di aggiornamento) — mai lasciata a
coincidenza silenziosa.*

---

## LA STRUTTURA

Le 14 sezioni della home, lette attraverso la formula a 11 tappe della famiglia out* (dossier 14-17:
hero, agitazione, prova con fonte, metodo, benefici, curriculum, qualificazione negativa, obiezioni,
autorevolezza, prezzo barrato, FAQ, chiusura). La home non è una landing di prodotto e lo si vede
subito: esegue la formula con **tre tappe assenti** e **tre sezioni in più** che la formula non prevede
affatto.

| # | Sezione (`i`) | y / h | Heading | Funzione | Tappa formula |
|---|---|---|---|---|---|
| 1 | 1 | 65 / 902 | "Il traffico si compra. I clienti si convertono." | promessa nell'H1 stesso + qualificazione cliente al 50% opacità | 1. Hero |
| 2 | 2 | 967 / 720 | (nessuno) — 5 guerrieri in stile ASCII | posizionamento/brand puro, **fuori formula**: nessuna delle 11 tappe prevede una sezione solo atmosferica | — |
| 3 | 3 | 1687 / 309 | (nessuno) — marquee 10 loghi cliente | prova sociale **anticipata** (vedi PATTERN sopra) | 9bis. Autorevolezza, spostata in apertura |
| 4 | 4 | 1996 / 563 | (nessuno) — paragrafo manifesto | estensione della promessa, unico blocco centrato di tutta la pagina | 1bis. Hero (eco) |
| 5 | 5 | 2559 / 1004 | "Il problema" + "La soluzione" | agitazione e rivelazione del metodo **fuse in una sola sezione a specchio** | 2. Agitazione + 4. Metodo insieme |
| 6 | 6 | 3563 / 1482 | "Facciamo solo due cose. Per scelta." | il "curriculum": qui non lezioni ma i due servizi venduti | 6. Curriculum (equivalente) |
| 7 | 7 | 5045 / 1194 | "Metodo statistico. Non opinioni." | processo numerato 01-04 (Tracciamo/Guardiamo/Costruiamo/Misuriamo) | 4bis. Metodo, esplicito e numerato |
| 8 | 8 | 6239 / 692 | "Non facciamo solo pagine. Orchestriamo la conversione." | 3 colonne (Offerta/Coerenza/Fiducia) | 5. Benefici a blocchi |
| 9 | 9 | 6931 / 1034 | "Agenzia generalista, freelancer o assumere? Nessuno dei tre." | tabella comparativa 4 colonne × 6 righe | 9. Autorevolezza (per confronto, non per track record) |
| 10 | 10 | 7965 / 978 | "Piccola agenzia. Standard alti." | bio founder + 3 numeri + team | 9bis. Autorevolezza (per curriculum) |
| 11 | 11 | 8943 / 652 | "Deleghiamo. Ma mai a caso." | ammissione preventiva di outsourcing | 8. Obiezioni (una sola, dedicata) |
| 12 | 12 | 9594 / 1077 | "Domande frequenti." | 7 domande, accordion | 11. FAQ |
| 13 | 13 | 10671 / 712 | "Vediamo se ha senso lavorare insieme." | CTA condizionale + "Nessun impegno" | Chiusura |
| 14 | 14 | 11383 / 1182 | (footer) | link, P.IVA, copyright | Chiusura legale |

**Le tre tappe che mancano del tutto**: **3 (prova del problema con fonte esterna)** — "Il CPL sale
ogni trimestre" [y=2946] è affermato senza una sola statistica o link, a differenza sia della famiglia
out* (che cita HubSpot/Salesforce) sia di `claude-speedrun.com` (che cita Punto Informatico per i
miliardi di OpenAI, vedi il gemello); **10 (prezzo, barrato o no)** — assente per intero, vedi CANONE
sopra; e una vera **qualificazione negativa** ("non è per te se…") in forma di lista esplicita, che
qui non esiste come blocco a sé (la qualificazione c'è ma è positiva e implicita, nella riga
*"Solo per B2B e B2B SaaS che investono da €5.000 a €100.000 al mese in ads."* [y=812], una singola
frase e non una lista).

**Le tre sezioni che la formula non prevede**: le sezioni 2, 3 e 4 (guerrieri ASCII, marquee loghi,
paragrafo manifesto) occupano insieme **1.592px** prima ancora che la pagina nomini un problema — quasi
il doppio dell'hero stesso (902px). Sono investimento di brand puro, non passi di persuasione diretta:
la home si concede uno spazio che nessuna pagina di prodotto della famiglia out* o di `claude-speedrun`
si concede.

---

## LA PROMESSA E DOVE STA

A differenza di `claude-speedrun.com` (promessa sparsa su tre frasi diverse in tre punti della pagina,
vedi il gemello), qui la promessa è **una sola, dichiarata subito, e quantificata nel meccanismo**: l'H1
[y=177] *"Il traffico si compra. I clienti si convertono."* pone il contrasto in due frasi da tre
parole ciascuna. Il sottotitolo, la riga immediatamente sotto [y=532], la rende operativa:
*"Siamo AP Sales, agenzia di Conversion Rate Optimization. Usiamo numeri e persuasione etica per
aumentare quante persone ti contattano e comprano, con la stessa spesa pubblicitaria."* — qui compare
già il meccanismo economico (stessa spesa, più risultati) che nella famiglia out* di solito arriva
molto più tardi. Non c'è mai, in tutta la home, una riformulazione diversa della stessa promessa: le
sezioni successive la argomentano, non la ridefiniscono — un'unica coerenza che manca del tutto al
gemello studiato su Claude Speedrun.

---

## COME TRATTA LE OBIEZIONI

| Obiezione | Trattata? | Citazione |
|---|---|---|
| "Basta spendere di più in ads" | sì, come apertura del problema | *"Il CPL sale ogni trimestre. E la risposta di tutti è "spendi di più"."* [y=2946] |
| "Le vostre scelte sono solo gusto, non dati" | sì, rovesciata contro il mercato in generale | *"Le modifiche al sito si decidono con "a me piace il blu". Zero dati."* [y=3145] |
| "Perché non un'agenzia generalista / un freelancer / assumere?" | sì, tabella comparativa 6 righe | *"Agenzia generalista, freelancer o assumere? Nessuno dei tre."* [y=7075], con confronto riga per riga su specializzazione, dati, dark pattern, garanzia, costo fisso, reperibilità [y=7259-7756] |
| "Siete troppo pochi per seguirmi sul serio" | sì | *"Siamo meno di 10 persone, per scelta. L'AI ci dà la velocità di un team da 100."* [y=8261] |
| "Usate manodopera esterna a basso costo?" | sì, ammessa in anticipo | *"Su parte del lavoro ci appoggiamo a professionisti selezionati fuori dal team. Non è subappalto a basso costo: ognuno lavora dentro i nostri processi e le nostre SOP."* [y=9304] |
| "E se le conversioni non aumentano?" | nominata in FAQ, **risposta non catturata** | [y=10143] |
| "Quanto costa?" | nominata in FAQ, **risposta non catturata** | [y=10239] — l'unica risposta FAQ effettivamente leggibile in questa cattura è quella della prima domanda, *"Cos'è la CRO?"*: *"Conversion Rate Optimization: ottimizzare la percentuale di visitatori che compie un'azione, che sia un contatto, un preventivo o un ordine. Si fa con dati, test e psicologia. Non a sensazione."* (da `scheda.json`, campo `jsonld`) |
| "Fate anche ads, social, SEO oltre alla conversione?" | nominata in FAQ, **risposta non catturata** | [y=10335] |
| "Quanto tempo devo dedicarci io?" | nominata in FAQ, **risposta non catturata** | [y=10431] |
| "Siete un'agenzia che usa trucchi da funnel aggressivo?" | sì, in una riga sola, non in una sezione dedicata (a differenza della pagina Landing, che ha "Tecniche sostenibili.", già segnalato nel report 18-20) | *"Nessun impegno. Niente countdown finti."* [y=11200] |

**Cosa manca rispetto alle pagine di servizio**: Landing dedica una sezione intera al disinnesco delle
tecniche disoneste (dossier 18-20, §Obiezioni); la home la comprime in una riga di nove parole in
fondo alla pagina. È coerente col ruolo di router della home — argomenta meno, rimanda alle pagine
figlie per il lavoro persuasivo pesante.

---

## LE PROVE E LA LORO VERIFICABILITA'

| Cifra / affermazione | Citazione | Fonte in riga? | Verificabile? |
|---|---|---|---|
| "follower organici 250.000" | [y=8482] | no, nessuna piattaforma nominata | **No, e in conflitto**: `claude-speedrun.com` (bio Andrei, stessa data di cattura) dichiara *"270K+ follower"* su TikTok — vedi `12-claude-speedrun-COPY.md` §LE PROVE. 20.000 di scarto, stessa persona, stesso giorno |
| "clienti seguiti 100+" | [y=8546] | no | **Parziale** — la pagina mostra solo **10 loghi distinti** nel marquee [y=1883, sezione i=3]: il 10% del numero dichiarato è nominabile, il resto no |
| "professionisti formati 1.500+" | [y=8611] | no | **Coerente** (raro, positivo) con la bio su `claude-speedrun.com`: *"un corso con 3.600+ ordini e 1.500+ studenti"* — stessa cifra "1.500+", stesso riferimento (Copywriting Mentorship). Unico numero su due proprietà che **non** si contraddice |
| "Il CPL sale ogni trimestre" | [y=2946] | no | **No** — nessuna serie storica, nessun settore specificato, nessun grafico |
| "Ogni modifica confrontata con una baseline. Se non migliora, si cambia." | [y=3145] | n/a (è una descrizione di metodo, non una cifra) | Verificabile solo con accesso diretto al processo, non dalla pagina |
| Dieci loghi cliente (Vidiren, LSP, AGL Aste Immobiliari, ecc.) | [y=1883-2508 nel DOM, sezione i=3] | n/a | **Sì, in linea di principio** — sono nomi reali di aziende verificabili, a differenza di ogni altra prova della pagina. È l'unica prova della home non riconducibile a un ipse dixit — ma nessun logo porta un risultato numerico accanto |

**Il verdetto**: sulle tre cifre di credibilità del founder (follower, clienti, professionisti
formati), una si contraddice tra le due proprietà del brand, una è verificabile solo al 10% dal
materiale in pagina, una sola regge il confronto incrociato. L'unica prova realmente solida — i dieci
loghi cliente — non è quantificata: dimostra che i clienti esistono, non quanto hanno guadagnato.

---

## LA SCALA DI IMPEGNO

La home chiede meno di quanto chieda persino Servizi (che è già, per sua natura, un router — dossier
18-20). Le CTA misurate: in hero, *"Voglio aumentare le conversioni →"* (piena, blu) versus
*"Vedi i servizi"* (fantasma) [y=720-812] — una scelta binaria fra "sono pronto" e "voglio prima
guardare"; a metà pagina, *"Come funziona"* → `/landing-page` e *"Fai una consulenza"* → `/consulenza`
[y=4801]; a fine pagina, *"Parla con noi →"* [y=11119] e, fissa, *"Prenota una chiamata →"* [y=10098].
**Zero form di qualificazione, zero pagamento, zero raccolta dati** in tutta la home: ogni singolo CTA
è un link di navigazione verso un'altra pagina del sito. È un router puro, un livello sopra Servizi
stesso: se Servizi smista fra due prodotti, la home smista fra "guarda i servizi" e "vai già a un
servizio specifico" — l'impegno massimo richiesto qui è un click, mai un'informazione di contatto.

---

## IL PREZZO E LA SUA CORNICE

**Nessun prezzo compare in tutta la home.** L'unica occorrenza del simbolo "€" in tutto il file
sorgente è dentro il criterio di qualificazione del cliente-tipo, non un prezzo del servizio:
*"Solo per B2B e B2B SaaS che investono da €5.000 a €100.000 al mese in ads."* [y=812] — è un filtro
di ingresso, non un'offerta. La parola "prezzo" o "costo" compare una sola volta, come titolo di FAQ
chiusa: *"Quanto costa?"* [y=10239], la cui risposta non è stata catturata in questa cattura statica.

Questo conferma, con una fonte indipendente in più (la home, non ancora esaminata nel report 18-20),
la regola già scritta su quel report: **il prezzo esiste da qualche parte nel sito (Consulenza, €610,
mostrato tre volte) ma non risale mai fino alla pagina più a monte del funnel.** Chi arriva sulla home
non vede un numero prima di aver cliccato almeno una volta — spesso due, se passa da Servizi prima di
arrivare a Consulenza o Landing.

---

## COSA NON DICE MAI

- **Nessun prezzo**, nemmeno quello del prodotto a listino (già discusso sopra).
- **Nessun caso cliente con numeri prima/dopo** — i dieci loghi provano l'esistenza dei clienti, non un
  solo risultato ottenuto per loro.
- **Nessuna testimonianza di un cliente in prima persona** — le uniche citazioni dirette dell'intera
  home sono le etichette dei cinque guerrieri (`design`, `statistica`, `vendita`, `persuasione`,
  `APsales`), non parole di un cliente.
- **Nessun nome di dipendente oltre Andrei Pascu** — il blocco "Team" [y=8109-8702] mostra solo
  *"Meno di 10 persone, per scelta"*, mai un nome, un ruolo o una foto diversa da quella del founder.
- **Nessun dettaglio sulle "SOP" citate** — *"i nostri processi e le nostre SOP"* [y=9304] è nominato
  come garanzia di qualità sul lavoro delegato, ma nessuna SOP viene mostrata nemmeno come esempio.
- **Nessuna scarsità o urgenza**, esplicitamente negata: *"Nessun impegno. Niente countdown finti."*
  [y=11200].
- **Il termine "CRO" non compare mai per esteso nell'hero** — arriva solo nel sottotitolo
  (*"agenzia di Conversion Rate Optimization"*, y=532) e viene definito solo in FAQ, alla prima
  domanda.

---

## LE FORMULE RICORRENTI

**1. Contrasto a specchio fra due verbi diversi per due soggetti diversi**
Originale: *"Il traffico si compra. I clienti si convertono."* [y=177]
Riusabile: *"[AZIONE A] si [VERBO A]. [AZIONE B] si [VERBO B]."*

**2. Negazione del minimo, sostituita da un verbo di scala maggiore**
Originale: *"Non facciamo solo pagine. Orchestriamo la conversione."* [y=6383]
Riusabile: *"Non facciamo solo [ELEMENTO SINGOLO]. [VERBO AMPIO] [SISTEMA INTERO]."*

**3. Triade di alternative note, rifiutate in blocco**
Originale: *"Agenzia generalista, freelancer o assumere? Nessuno dei tre."* [y=7075]
Riusabile: *"[OPZIONE A], [OPZIONE B] o [OPZIONE C]? Nessuno dei tre."*

**4. Metodo + negazione secca dell'alternativa debole**
Originale: *"Numeri e persuasione. Non indovinare."* [y=2836]
Riusabile: *"[METODO A] e [METODO B]. Non [VERBO DA EVITARE]."*

**5. Verbo dichiarato, poi subito ridimensionato da un avverbio di cautela**
Originale: *"Deleghiamo. Ma mai a caso."* [y=9152]
Riusabile: *"[VERBO SCOMODO]. Ma mai a caso."*

**6. Riduzione dimensionale seguita da innalzamento qualitativo, stessa struttura a due frasi**
Originale: *"Piccola agenzia. Standard alti."* [y=8109]
Riusabile: *"[AGGETTIVO RIDUTTIVO] [SOSTANTIVO]. [AGGETTIVO AMPLIFICANTE] [SOSTANTIVO]."*

---

## IL DIFETTO

**Il layout a specchio "Il problema / La soluzione" promette una corrispondenza punto-per-punto che il
testo non mantiene.** Le tre righe del problema [y=2946-3145]:
1. *"Il CPL sale ogni trimestre. E la risposta di tutti è "spendi di più"."*
2. *"La tua pagina parla del tuo prodotto. Ma al cliente interessa il suo problema, non il tuo
   prodotto."*
3. *"Le modifiche al sito si decidono con "a me piace il blu". Zero dati."*

Le tre righe della soluzione, alla stessa identica coordinata `y` nella colonna accanto:
1. *"Prima il tracciamento compliant: GA4, Meta Pixel, Clarity. Poi le opinioni."*
2. *"Copy e design costruiti su psicologia e standard di marketing. Creatività con un perché."*
3. *"Ogni modifica confrontata con una baseline. Se non migliora, si cambia."*

Solo la riga 2 risponde davvero alla riga 2 (prodotto vs cliente → copy/design su psicologia). La
riga 1 della soluzione (tracciamento/dati) risponde meglio alla riga 3 del problema ("zero dati") che
alla propria riga 1 ("spendi di più"); la riga 3 della soluzione (baseline/test) risponde meglio alla
riga 1 del problema (CPL che sale senza verifica) che alla propria riga 3. Il layout — due colonne
allineate riga per riga, bordo comune, bullet nello stesso stile — comunica visivamente una
corrispondenza 1:1 che il contenuto smentisce: chi legge in fretta (il modo in cui la maggior parte
del traffico legge una sezione "problema/soluzione") si porta via un abbinamento sbagliato fra la
propria obiezione e la risposta che la risolve davvero.

**Secondo difetto, per contraddizione incrociata**: la cifra dei follower di Andrei Pascu (vedi
GATE e LE PROVE sopra) non coincide fra questa pagina e `claude-speedrun.com` — 250.000 qui,
270.000+ là, stesso giorno di cattura.

---

## Nota di chiusura

Il materiale letto (537 blocchi di copy, l'intero `copy-integrale.md` da y=65 a y=11119, la scheda
delle 14 sezioni, il campione `jsonld` del FAQPage) bastava per superare le 2.500 parole richieste con
sostanza reale, senza necessità di riempitivo.

## Connessioni

- [13-apsales-STACK-E-TOKEN.md](13-apsales-STACK-E-TOKEN.md) — stack, token OKLCH→HEX, componenti
- [13-apsales-ATLANTE.md](13-apsales-ATLANTE.md) — atlante visivo delle 14 sezioni di questa stessa
  cattura
- [18-20-apsales-servizi-COPY.md](18-20-apsales-servizi-COPY.md) — lo standard di forma seguito qui,
  sulle tre pagine di servizio (Servizi/Landing/Consulenza) — la home ne conferma l'asimmetria di
  prezzo un livello più in alto
- [12-claude-speedrun-COPY.md](12-claude-speedrun-COPY.md) — il teardown gemello, con la verifica
  incrociata sui follower di Andrei Pascu
- `PIANO-MAESTRO/33-PIANO-STUDIO-TOTALE-ANDREI-PASCU.md`
