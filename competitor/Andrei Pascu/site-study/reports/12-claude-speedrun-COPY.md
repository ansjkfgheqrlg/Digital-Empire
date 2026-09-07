---
Type: SYNTHESIS
Status: Active
Tags: #competitor #andrei-pascu #claude-speedrun #copy #teardown #corso-ai #concorrente-diretto #manuale-claude-code
Created: 2026-09-07
Last updated: 2026-09-07
---

# Teardown di copy — claude-speedrun.com

**claude-speedrun.com**, corso di Andrei Pascu su come usare Claude nella propria agenzia, **€249**.
Cattura `12-claude-speedrun-v2`, 33.756px, 34 sezioni (32 distinte), 473 blocchi di copy. Questo è il
**concorrente più diretto** che Digital Empire abbia in tutto l'ecosistema studiato finora: lui vende
un corso su Claude, noi vendiamo il Manuale Claude Code. Stesso pubblico, stesso strumento, prezzo
nello stesso ordine di grandezza.

Contesto già acquisito e non ripetuto qui: lo stack (React+Vite, componenti `SectionN` numerati,
`OfferSection`/`LessonList`/`ReviewsWall`/`SkillsGrid`/`FAQ`/`Disclaimer`), i token colore (il suo
`#fb4604` è il nostro arancione, cifra per cifra), gli effetti (`highlighter-reveal`,
`marquee-scroll`) — tutto in `12-claude-speedrun-STACK-E-TOKEN.md`. Qui si guarda solo il copy: cosa
dice, in che ordine, con quali prove, e come giustifica il prezzo.

---

## DELTA ALLA FABBRICA

**CANONE:** un'offerta a prezzo fisso può reggersi anche **senza prezzo barrato o valore-totale
sommato**, se lo sostituisce con un ancoraggio di costo ricorrente più basso. Qui il ponte al prezzo
non è "valeva X, oggi Y" ma *"avere l'Ai dalla tua parte è tipo avere un team che lavora per te… ma
non lo paghi quasi nulla (€20-30 al mese)"* [y=15876] — il paragone è col costo mensile di un
abbonamento AI, non con un prezzo di listino del corso stesso. Per la Fabbrica: quando il prodotto è
un accesso via abbonamento sottostante (qui: Claude), l'ancora di prezzo può essere quel costo
ricorrente invece del valore-totale sommato dei moduli — un'alternativa in più al pattern
"prezzo barrato", da tenere accanto ad esso, non al suo posto.

**PATTERN:** la "cartella di contesto" come argomento di vendita implicito va salvata come blocco
riusabile. Citazione: *"Non è bastato un messaggio. Mi è servita un'intera cartella con: Strumenti
Strategia Context"* [y=12336-12443]. È l'argomento più vicino a una vera obiezione tecnica
("Claude da solo non basta, serve un sistema attorno") ma resta implicito — non diventa mai una FAQ
esplicita. Per il Manuale Claude Code, lo stesso argomento va reso **esplicito**, non lasciato a
sottotesto: "un prompt non basta, serve un sistema di cartelle/contesto/skill" è esattamente la
differenza tra "sapere che Claude esiste" e "sapere usarlo", ed è un varco che lui stesso apre e non
richiude.

**GATE:** ogni cifra di risultato personale ("+270K follower", "3.600+ ordini", produttività "+66%")
deve portare fonte o essere dichiarata non verificabile — vedi §"LE PROVE" sotto, dove risulta che
**nessuna delle cifre di risultato personale di questa pagina ha una fonte esterna in riga**, e almeno
una di esse (i follower TikTok) **si contraddice con il numero dato dallo stesso autore su un'altra
delle sue pagine**, catturata lo stesso giorno. Per la Fabbrica: se una cifra ricorre su più proprietà
dello stesso brand, deve essere identica ovunque o va giustificata la differenza (mese di
aggiornamento, fonte diversa) — mai lasciata a coincidenza.

---

## LA STRUTTURA

La pagina non segue la formula a 11 tappe della famiglia out* in modo lineare: la esegue **due volte**,
con un primo giro dedicato all'AI in generale e un secondo dedicato ad Andrei/Claude Speedrun nello
specifico. Di seguito le macro-tappe, con sezione sorgente (`i`, altezza `y`, `parole` da
`scheda.json`) e la tappa della formula a cui corrispondono.

| # | Macro-tappa | Sezioni (`i`) | y | Funzione | Tappa formula out* |
|---|---|---|---|---|---|
| 1 | Hero doppio: claim + sottopromessa | 1-2 | 0-1600 | *"Come un titolare d'agenzia usa realmente Claude..."* + *"Corso per marketer che vogliono trasformare Claude in un dipendente che non dorme..."* | 1. Hero |
| 2 | Ticker "Versione 2: fuori ora" + CTA "RUBA WORKFLOW" | 3-4 | 1600-4084 | prova di continuità (è la v2) + primo bottone di conversione, presentissimo (a 4.000px, non a fine pagina) | fuori formula — anticipo di CTA insolito così presto |
| 3 | Agitazione #1 — "non sai usare l'AI", mini-comic ChatGPT | 5-8 | 4084-7193 | umilia l'uso attuale del lettore ("Ciao ChatGPT... daddy 🥺" [y=4930]), poll interattivo "ti ritrovi?" | 2. Agitazione |
| 4 | Prova con fonte — ma **della categoria, non dell'autore** | 8 | 5833-7193 | *"Fonte: Punto Informatico"* [y=6779], round OpenAI $110B, $50B Amazon, $30B Nvidia, $30B SoftBank | 3. Prova con fonte |
| 5 | Metodo #1 — "come io uso l'AI: luglio 2026" + agitazione #2 | 9-12 | 7193-10586 | tre motivi per cui l'AI "sembra" inutile, poi la conversione personale ChatGPT→Claude | 4. Rivelazione del metodo (parziale) |
| 6 | Agitazione #2 — competitor | 13-14 | 10586-11906 | *"Hai COMPETITOR e non lo sai"* [y=10682], *"Negli ultimi 7 giorni sono uscite 18 notizie sull'AI"* [y=11114] (cifra senza fonte) | 2. Agitazione (bis) |
| 7 | Metodo #2 — la cartella, gli strumenti | 15 | 11906-12705 | *"Non è bastato un messaggio... Mi è servita un'intera cartella"* [y=12336-12443] | 4. Rivelazione del metodo |
| 8 | Benefici a blocchi (3) | 16 | 12705-13342 | calendario, ricerca clienti, copy Meta Ads — con cifra unica dell'intera pagina corredata da paragone temporale ("10 minuti invece che in 2 giorni" [y=13161]) | 5. Benefici a blocchi |
| 9 | Curriculum/autorevolezza — bio Andrei | 17 | 13342-14307 | *"3.600+ ordini e 1.500+ studenti"*, *"270K+ follower"* [y=14083-14188] | 9. Autorevolezza |
| 10 | Prodotto + primo prezzo | 18 | 14307-14960 | *"Video corso di 7+ ore"* [y=14514], CTA *"...ti do i miei dannati €249"* [y=14805] | 10. Prezzo — **senza barrato** |
| 11 | Obiezione al prezzo | 19 | 14960-16381 | *"Perché quei €249 sono ancora sulla tua carta???"* [y=15145] — ancoraggio al costo mensile di Claude | 8. Obiezioni (unica esplicita di tutta la pagina) |
| 12 | Qualificazione dello scetticismo | 20 | 16381-17084 | *"Ma chi pensi di essere???"* [y=16622], link alla "storia" | 7. Qualificazione (ma del lettore scettico, non del cliente-tipo) |
| 13 | Offerta + Curriculum esteso | 21-23 | 17084-21900 | CTA Stripe, `LessonList` (21 lezioni + 6 bonus), `SkillsGrid` con **3 skill non rivelate** ("???" [y=21207,21410,21613]) | 6. Curriculum |
| 14 | Prova sociale | 24 | 21900-23024 | *"4,9/5 su 14 recensioni verificate"* [y=22050-22089] | 3bis. Prova (recensioni) |
| 15 | Rilancio + argomento logico | 25-30 | 23024-30549 | ripetizione autorevolezza marketer, formula produttività ("Produttività = robe utili che fai / unità di tempo" [y=27729], "+66%" [y=28838]), differenziazione Claude vs ChatGPT | 4bis. Metodo (logico) |
| 16 | Value stack | 31 | 30549-31590 | 11 voci elenco, **nessuna cifra, nessun totale barrato** | 10bis. Valore (senza prezzo) |
| 17 | FAQ | 32 | 31590-33086 | **17 domande** — più del doppio della media famiglia out* (3-4) | 11. FAQ |
| 18 | Chiusura legale + footer | 33-34 | 33086-33756 | `Disclaimer` come sezione a sé (conferma pattern già registrato nel dossier stack) | Chiusura |

**Cosa cambia rispetto alla formula di riferimento:** la tappa "prova con fonte" (3) qui non prova
*Andrei*, prova che *l'AI in generale* è un fenomeno enorme (i miliardi di OpenAI). È un bersaglio
spostato: il lettore finisce per credere che l'AI sia seria, non che Andrei sappia usarla — le due cose
vengono presentate come se fossero la stessa conclusione, ma non lo sono. La tappa "obiezioni" (8),
di solito un botta-e-risposta puntuale nella famiglia out*, qui è **una sola macro-obiezione**
(il prezzo) trattata per un'intera sezione da 1.421px — non ci sono obiezioni tecniche dirette tipo
"e se sbaglia?" o "non ho tempo per un corso". E la tappa 10 (prezzo) non porta mai un barrato o un
valore-totale sommato, cosa che la famiglia out* fa **sempre** (dossier 14-17): è la prima pagina di
tutto l'ecosistema Andrei Pascu studiato finora a mostrare un prezzo fisso senza alcuna cornice di
sconto.

---

## LA PROMESSA E DOVE STA

La promessa non sta nell'H1. L'H1 [y=234] — *"Come un titolare d'agenzia usa realmente Claude nel suo
lavoro (senza la roba hype)"* — è descrittivo, non un beneficio: promette trasparenza di metodo, non un
risultato per il lettore. Il beneficio compare due frasi dopo, nell'H2 [y=840]: *"Corso per marketer
che vogliono trasformare Claude in un dipendente che non dorme, non beve e non chiede aumenti."* — qui
la promessa è esplicita e concreta: Claude come sostituto di un dipendente, con tre limiti umani
nominati e negati uno a uno.

La promessa più aggressiva, però, arriva molto più in basso, dopo tre agitazioni consecutive:
*"E voglio mostrare pure a te come ho trasformato l'AI nel mio vantaggio competitivo in Claude
Speedrun: corso accelerato di come io lo uso come titolare di un'agenzia di marketing."* [y=3830] —
qui il "vantaggio competitivo" sostituisce il "dipendente che non dorme": due promesse diverse per lo
stesso prodotto, mai riconciliate esplicitamente in una sola frase-sintesi. Il lettore arriva al
prezzo (y=14805) avendo letto tre promesse leggermente diverse (dipendente infaticabile, vantaggio
competitivo, "5x del lavoro" [y=2317]) senza che nessuna delle tre sia mai definita con un numero o un
esempio verificabile a corredo.

---

## COME TRATTA LE OBIEZIONI

| Obiezione | Trattata? | Citazione |
|---|---|---|
| "Perché dovrei pagare 249€?" | sì, esplicita, sezione intera | *"Perché quei €249 sono ancora sulla tua carta???"* [y=15145] |
| "Costa troppo rispetto a un abbonamento AI" | sì, implicita via paragone | *"Avere l'Ai dalla tua parte è tipo avere un team che lavora per te… ma non lo paghi quasi nulla (€20-30 al mese)."* [y=15876] |
| "Sei un guru che non sa niente / sei uno scam" | sì, esplicita | *""Andrei, chiunque tu sia… Senti. Parli tanto. Ma chi pensi di essere???""* [y=16622], poi *"Leggi sta pagina malata e pensi che sono scam. Forse lo sono lol. Dammi €249 e scoprilo."* [y=16736] — l'obiezione viene nominata e poi scherzata via, non smontata con una prova |
| "So già usare l'AI, mi serve ancora?" | nominata in FAQ, **risposta non catturata** | *"So già usare bene l'AI, Claude Speedrun è comunque utile?"* [y=32155] — accordion chiuso nel DOM al momento della cattura, non dichiaro un contenuto che non ho letto |
| "Devo pagare anche Claude separatamente?" | nominata in FAQ, **risposta non catturata** | *"Devo pagare Claude?"* [y=32231] |
| "Posso usare il piano gratuito di Claude?" | nominata in FAQ, **risposta non catturata** | *"Posso usarlo col piano free di Claude?"* [y=32383] |
| "Sei un esperto di AI (tecnico)?" | nominata in FAQ, **risposta non catturata** | *"Tu sei un esperto di AI?"* [y=31852] |
| "Lo imparo gratis dalla documentazione" | **mai nominata, in nessuna forma, né in copy né come domanda FAQ** | — |

**La domanda che vale più del resto** (vedi sezione dedicata sotto) trova qui la sua prima risposta
misurata: quell'obiezione specifica non esiste da nessuna parte in questa pagina, né come frase né come
titolo di FAQ. Le tre FAQ più vicine (*"So già usare bene l'AI..."*, *"Devo pagare Claude?"*, *"Posso
usarlo col piano free?"*) la sfiorano ma la loro risposta è chiusa nell'accordion e non è stata
catturata — quindi anche *se* la pagina la affrontasse lì dentro, non lo farebbe **a vista**, cioè non
farebbe il lavoro persuasivo che una risposta visibile fa prima del click sul prezzo.

---

## LE PROVE E LA LORO VERIFICABILITA'

| Cifra / affermazione | Citazione | Fonte in riga? | Verificabile? |
|---|---|---|---|
| OpenAI ha raccolto $110 miliardi | *"$110 miliardi"* [y=6873], con *"Fonte: Punto Informatico"* [y=6779] | **sì** | Sì, è l'unica cifra sourciata di tutta la pagina — ma prova la scala del mercato AI, non la competenza di Andrei |
| $50B Amazon, $30B Nvidia, $30B SoftBank | [y=6933-6985] | no fonte propria, probabilmente sotto lo stesso "Fonte: Punto Informatico" del blocco | Parziale — attribuzione implicita, non ripetuta riga per riga |
| "Negli ultimi 7 giorni sono uscite 18 notizie sull'AI" | [y=11114] | no | **No** — nessun link, nessun aggregatore nominato |
| "Analisi di mercato e competitor in 10 minuti invece che in 2 giorni" | [y=13161] | no | **No** — nessun cliente, nessun output mostrato, nessuno screenshot corredato nel testo catturato |
| "3.600+ ordini e 1.500+ studenti" (Copywriting Mentorship) | [y=14083] | no | **No** — nessun link a piattaforma di vendita, nessuna dashboard |
| "270K+ follower" su TikTok | [y=14188] | no (solo l'handle `@andrei.bsns`) | **No, e in conflitto**: `apsales.eu` (home, stessa cattura del 2026-09-07) dichiara *"follower organici 250.000"* senza specificare piattaforma — 20.000 di scarto sulla stessa persona, stesso giorno, due proprietà dello stesso brand. Vedi `13-apsales-home-COPY.md` §PROVE per il verso opposto della stessa verifica |
| "4,9/5 su 14 recensioni verificate" | [y=22050-22089] | dichiarato "verificate" ma senza piattaforma nominata (non Trustpilot, non Google) | Parziale — il numero di recensioni (14) è basso per un prodotto che promette di reinventare la produttività del lettore, e "verificate" non è ancorato a un sistema terzo visibile in pagina |
| "Nel giorno 2 sei stato 66% più produttivo" | [y=28838], dentro l'esempio della formula *"Produttività = robe utili che fai / unità di tempo"* [y=27729] | no — è un esempio didattico, non dichiarato come dato reale | Onesto per omissione: non finge di essere un caso reale, ma nemmeno lo dichiara esplicitamente come "esempio ipotetico" — l'ambiguità resta a favore della pagina |

**Il verdetto spietato**: su otto cifre-prova, **una sola** (i $110 miliardi di OpenAI) porta una fonte
verificabile — e non è nemmeno una prova su Andrei, è una prova sul mercato in cui opera. Tutte le
cifre che riguardano *lui* (ordini, studenti, follower, tempo risparmiato dal cliente) sono affermate
senza fonte, e almeno una (i follower) si contraddice misurabilmente con un'altra pagina dello stesso
autore catturata lo stesso giorno.

---

## LA SCALA DI IMPEGNO

La pagina chiede un solo tipo di impegno, ripetuto in tre forme di CTA diverse ma equivalenti: **il
pagamento diretto di €249**, mai un form di qualificazione, mai una chiamata conoscitiva. Le CTA
misurate: *"RUBA WORKFLOW"* [y=2889] (early, a 2.889px, prima ancora dell'agitazione principale —
insolito: normalmente un CTA così aggressivo arriva dopo la costruzione del problema, qui la precede),
*"Entra adesso"* [y=3938], *"...ti do i miei dannati €249"* [y=14805], *"Iscriviti adesso"*
[y=17914, link diretto a Stripe: `https://buy.stripe.com/bJe28s3nc7240S39Ra4Ja1F`], *"Iscriviti
adesso"* [y=31438]. Cinque bottoni, tutti portano allo stesso pagamento — a differenza del sito
gemello `apsales.eu`, dove Servizi fa da router verso due pagine diverse (Landing vs Consulenza) con
impegni diversi, qui **non esiste ramificazione**: un solo prodotto, un solo prezzo, un solo click
finale. La scala di impegno è piatta, non progressiva.

---

## IL PREZZO E LA SUA CORNICE — e la domanda che vale più del resto

**Come giustifica i 249€.** Non con un valore-totale sommato (non esiste nella pagina un calcolo tipo
"21 lezioni x Y€ + skill + bonus = Z€, tu paghi 249€"): la giustificazione è triplice e mai riunita in
un solo argomento:
1. **Paragone al costo ricorrente di un abbonamento AI** — *"Avere l'Ai dalla tua parte è tipo avere un
   team che lavora per te… ma non lo paghi quasi nulla (€20-30 al mese)."* [y=15876]. La logica
   implicita: il corso costa una tantum quanto 8-12 mesi di abbonamento Claude, ma promette di
   sbloccare tutto il valore di quell'abbonamento che altrimenti resterebbe inutilizzato.
2. **Pressione sociale/competitiva** — *"i tuoi competitor usano l'AI oggi. ADESSO."* [y=15218],
   seguito da post social citati a memoria (*"Ho appena fatto €100k con la mia agency"* [y=15468])
   che creano il contrasto emotivo, non economico.
3. **Volume di contenuto** — 21 lezioni + 6 bonus + skill, elencate come *"Cosa ottieni se entri
   adesso"* [y=30645], undici voci in elenco puntato, **senza una sola cifra o prezzo unitario
   accanto**.

Nessuna delle tre argomentazioni fa un confronto diretto e numerico con il prezzo (es. "ogni lezione ti
costa X€"). Il prezzo resta un numero isolato, giustificato per accumulo di motivi diversi più che per
calcolo.

**Che prove porta di saper usare Claude, davvero.** Pochissime, e indirette:
- La sezione "benefici a blocchi" [y=12705-13342] elenca tre usi concreti (*"Il mio calendario"*,
  *"Ricerca per i clienti"*, *"Copy per Meta Ads"*) ma senza mostrare un solo output reale, screenshot
  di chat, o cliente nominato — sono didascalie, non prove.
- La bio [y=14083] prova che Andrei **ha un'agenzia e vende corsi**, non che sappia usare Claude in
  modo specificamente superiore alla media: *"basa letteralmente tutta la sua operatività su Claude"*
  è un'affermazione, non una dimostrazione.
- L'unico dettaglio tecnico reale di tutta la pagina è la menzione della "cartella" di contesto
  [y=12401-12443] ("Strumenti, Strategia, Context") — è un'allusione a un sistema, ma il sistema stesso
  non viene mai mostrato, nemmeno come schermata sfocata.

**Come tratta l'obiezione "lo imparo gratis dalla documentazione".** Non la tratta. È assente — non
compare come frase nel copy, non compare come domanda tra le 17 della FAQ (la più vicina,
*"So già usare bene l'AI, Claude Speedrun è comunque utile?"* [y=32155], la aggira parlando di livello
di partenza del lettore, non di dove il lettore potrebbe imparare gratis). L'argomento più vicino a una
risposta implicita è la storia della cartella [y=12336-12443]: *"Non è bastato un messaggio... Mi è
servita un'intera cartella con: Strumenti Strategia Context"* — il sottotesto è "sapere che Claude
esiste (quello che dà la documentazione) non basta, serve un sistema", ma la pagina non lo dice mai
esplicitamente come contro-argomento a "posso studiarmelo da solo gratis". È un varco aperto e mai
richiuso.

**Cosa dobbiamo dire noi, che lui non dice.** Tre cose, precise:
1. **Numeri di risultato con fonte verificabile in riga** — non "10 minuti invece di 2 giorni" detto a
   memoria, ma un output reale, un cliente nominato (con permesso) o almeno un timestamp di sessione.
   Lui non lo fa su nessuna delle sue pagine studiate finora (né qui, né sulle tre di apsales.eu, dossier
   18-20): è un vuoto strutturale dell'intero ecosistema Andrei Pascu, non solo di questa pagina.
2. **Una risposta esplicita, a vista, a "lo imparo gratis dalla documentazione"** — non dentro un
   accordion chiuso, ma come blocco di testo visibile prima del prezzo: la differenza vera tra
   documentazione ufficiale e un manuale a pagamento è il **contesto pronto all'uso** (prompt, skill,
   struttura di cartelle) — l'argomento che lui stesso sfiora con la "cartella" ma non nomina mai come
   risposta a questa obiezione specifica.
3. **Un'ancora di prezzo esplicita**, barrata o a valore sommato — qui manca del tutto, ed è l'unica
   pagina di tutto l'ecosistema Andrei Pascu studiato a mancarne una (dossier 14-17: la famiglia out*
   la mostra sempre). Il Manuale Claude Code può permettersi di essere l'eccezione che la mostra,
   proprio perché il concorrente diretto non lo fa.

---

## COSA NON DICE MAI

- **Nessun caso cliente con nome, nessun prima/dopo con numeri verificabili** — le tre "cose che
  faccio oggi stesso" [y=12968-13161] restano didascalie generiche.
- **Nessun confronto diretto con il prezzo di corsi concorrenti** — l'obiezione al prezzo è trattata
  per paragone a un abbonamento (Claude), mai per paragone ad altri corsi sull'AI.
- **Nessuna garanzia di rimborso** — su un pagamento diretto via Stripe di €249, non compare mai una
  policy "soddisfatti o rimborsati", né nel copy né nelle 17 domande FAQ (la più vicina riguarda
  l'accesso: *"Per quanto tempo ho accesso?"* [y=32307], non il rimborso).
- **Nessun timer, nessuna scarsità dichiarata** — a differenza della pagina madre "Armageddon" dello
  stesso ecosistema (già segnalata con countdown live nel dossier 14-17), qui non c'è pressione
  temporale artificiale.
- **Nessuna competenza tecnica formale dichiarata** — la FAQ *"Tu sei un esperto di AI?"* [y=31852]
  esiste proprio perché la pagina non lo dichiara mai da sola nel corpo del testo; la risposta non è
  stata catturata (accordion chiuso).
- **Le tre skill bonus non vengono mai descritte prima dell'acquisto** — restano *"???"*
  [y=21207, 21410, 21613] anche nella sezione dedicata a venderle.

---

## LE FORMULE RICORRENTI

**1. Negazione tripla di limiti umani applicata a uno strumento**
Originale: *"Corso per marketer che vogliono trasformare Claude in un dipendente che non dorme, non
beve e non chiede aumenti."* [y=840]
Riusabile: *"[STRUMENTO] come un dipendente che non [LIMITE A], non [LIMITE B] e non [LIMITE C]."*

**2. Falsa causa smentita a favore della causa vera, in prima persona plurale**
Originale: *"Il risultato che ti dà l'AI oggigiorno non ti piace NON perché l'AI non è intelligente.
Bensì perché NON SAI USARE l'AI."* [y=6009-6036]
Riusabile: *"Il risultato che ottieni da [STRUMENTO] non ti piace NON perché [STRUMENTO] è scarso.
Bensì perché non sai usare [STRUMENTO]."*

**3. Rivelazione preceduta da un ostacolo minimizzato**
Originale: *"Non è bastato un messaggio... Mi è servita un'intera cartella con: Strumenti Strategia
Context."* [y=12336-12443]
Riusabile: *"Non è bastato [AZIONE MINIMA]. Mi è servito [SISTEMA COMPLETO] con: [ELEMENTO A]
[ELEMENTO B] [ELEMENTO C]."*

**4. Ancoraggio del prezzo al costo ricorrente di un abbonamento sottostante**
Originale: *"Avere l'Ai dalla tua parte è tipo avere un team che lavora per te… ma non lo paghi quasi
nulla (€20-30 al mese)."* [y=15876]
Riusabile: *"Avere [PRODOTTO] è come avere [RISORSA UMANA EQUIVALENTE]… ma costa solo [CIFRA] al
mese."*

**5. Domanda retorica ostile come apertura di sezione, poi disinnescata**
Originale: *""Andrei, chiunque tu sia… Senti. Parli tanto. Ma chi pensi di essere???""* [y=16622]
Riusabile: *""[NOME], chiunque tu sia… Ma chi pensi di essere???""* seguito da un'ammissione ironica
prima della vera risposta.

**6. Formula pseudo-matematica per rendere "misurabile" un beneficio soggettivo**
Originale: *"Produttività = robe utili che fai / unità di tempo"* [y=27729]
Riusabile: *"[BENEFICIO ASTRATTO] = [AZIONE CONCRETA] / [UNITA' MISURABILE]"*

---

## IL DIFETTO

**Il prezzo non è mai ancorato a un valore-totale né a un barrato, unico caso nell'intero ecosistema
Andrei Pascu studiato finora.** Il dossier 14-17 (famiglia out*) misura che tutte e quattro le pagine
sorelle mostrano sempre un prezzo individuale barrato più l'inclusione nel pacchetto Armageddon; qui,
sull'unica sezione che elenca cosa si ottiene [y=30645-31438], undici voci puntate non portano **una
sola cifra**, né la CTA finale [y=31438] mostra un totale. Il lettore arriva al pagamento avendo letto
tre giustificazioni di prezzo (paragone abbonamento, pressione sociale, volume di contenuto) ma mai un
numero che le riunisca in un calcolo verificabile — è una deviazione misurabile dal proprio stesso
standard di famiglia, non un'opinione di stile.

**Secondo difetto, misurato per contraddizione diretta**: la cifra di follower di Andrei Pascu non
coincide tra le sue due proprietà catturate lo stesso giorno. Qui: *"270K+ follower"* su TikTok
[y=14188]. Su `apsales.eu`, home, stessa data di cattura (2026-09-07): *"follower organici 250.000"*
[vedi `13-apsales-home-COPY.md`, §PROVE]. Uno scarto di 20.000 unità (7,4%) sulla stessa persona, sullo
stesso giorno — o le due cifre misurano cose diverse (piattaforma singola vs. somma di più canali) e
allora andrebbe specificato in entrambi i posti, o una delle due è semplicemente non aggiornata.

---

## Nota di chiusura

Il materiale letto (473 blocchi di copy, l'intero `copy-integrale.md` da y=-174 a y=33756, più la
scheda sezioni con 34 voci) bastava per superare le 2.500 parole richieste con sostanza reale. Conteggio
finale dichiarato in chiusura di lavoro insieme al gemello sulla home di apsales.eu.

## Connessioni

- [12-claude-speedrun-STACK-E-TOKEN.md](12-claude-speedrun-STACK-E-TOKEN.md) — stack, token colore,
  componenti, effetti dello stesso sito
- [14-17-famiglia-out-CONFRONTO.md](14-17-famiglia-out-CONFRONTO.md) — la formula a 11 tappe usata qui
  come riferimento di confronto
- [13-apsales-home-COPY.md](13-apsales-home-COPY.md) — il teardown gemello, con la verifica incrociata
  sui follower di Andrei Pascu
- [18-20-apsales-servizi-COPY.md](18-20-apsales-servizi-COPY.md) — lo stesso standard di forma, sulle
  tre pagine di servizio dell'agenzia
- `PIANO-MAESTRO/33-PIANO-STUDIO-TOTALE-ANDREI-PASCU.md`
