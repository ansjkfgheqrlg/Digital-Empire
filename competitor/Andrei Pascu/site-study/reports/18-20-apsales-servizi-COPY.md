---
Type: SYNTHESIS
Status: Active
Tags: #competitor #andrei-pascu #apsales #copy #teardown #cro #servizi #landing-page #consulenza
Created: 2026-09-07
Last updated: 2026-09-07
---

# Teardown di copy — le tre pagine di servizio di apsales.eu

Le tre pagine studiate: **Servizi** (`/servizi`, cattura `18-apsales-servizi`, 1.228 parole, 4229px,
5 sezioni/4 distinte), **Landing** (`/landing-page`, cattura `19-apsales-landing-page`, 3.894 parole,
16039px, 17 sezioni/17 distinte), **Consulenza** (`/consulenza`, cattura `20-apsales-consulenza`,
3.695 parole, 16832px, 15 sezioni/14 distinte). Ogni citazione qui sotto porta la pagina di
provenienza; dove il testo non era leggibile nel DOM catturato (accordion chiusi) lo dichiaro invece
di completarlo. Contesto già acquisito e non ripetuto qui: stack React + TanStack Start, colore
d'azione `#0062ff` — vedi `13-apsales-STACK-E-TOKEN.md` e `13-apsales-ATLANTE.md` (che studiano però
un'altra cattura, l'homepage `13-apsales-v2`, non le tre pagine di questo teardown).

---

## DELTA ALLA FABBRICA

**CANONE:** l'asimmetria di prezzo tra prodotto standard e prodotto su misura entra come regola
generale per la Fabbrica Siti. Su queste tre pagine il prodotto a prezzo fisso e basso rischio
(Consulenza, €610) mostra il prezzo tre volte, sempre appaiato a "IVA inclusa" (Servizi y=1810,
Consulenza y=845 e y=10664); il prodotto su misura e costoso (Landing page) non mostra mai un numero,
solo "Prezzo Su preventivo, dopo l'audit" (Servizi, y=1354) — confermato dalla FAQ della pagina
Landing: "Che tipo di accordo offrite? Un accordo una tantum, con riduzione del rischio grazie a
operatività basate sulle performance che ti portiamo. Paghi una volta." (Landing, y=12924) — modello
dichiarato, cifra mai. Regola per il canone: *il prodotto a listino mostra il prezzo ovunque appaia;
il prodotto su misura mostra il modello di pagamento ma mai la cifra, e la sposta dietro una call di
preventivo.*

**PATTERN:** il paragrafo "vincolo sei tu" per il cliente solo-fondatore va salvato come blocco
riusabile letterale, perché AP Sales lo ha già riusato identico su due pagine diverse (prova che
loro stessi lo trattano come un pezzo di libreria, non come copy ad hoc): "Lavori da solo? Vale lo
stesso. Al posto del team, il vincolo sei tu." (Servizi, y=2193; Consulenza, y=6578, testo
identico carattere per carattere). Nella Fabbrica va salvato come snippet parametrico (vedi Formula 4
più sotto) da richiamare ogni volta che il funnel/diagnosi ha una tappa "team" e il cliente target
include liberi professionisti.

**GATE:** ogni cifra usata come prova deve portare la propria fonte nella stessa riga, o va segnalata
come non verificabile prima della pubblicazione. Su queste tre pagine ho contato **10 cifre-prova**
(250k follower, 1.500 clienti formazione, 100+ clienti agenzia, 3.900+ ordini processati, "più di 100
imprenditori", "più di 100 consulenze... più di 50", "4,1 milioni di dichiaranti IVA", "da 2 a 3,5%"
di conversione, "+30 acquisti extra al mese"): **una sola** (il +30 acquisti/mese) dichiara
l'assunzione che la genera ("Assunzione: conversion rate 2,75% → 4,13% (+50%), stesso budget.",
Landing y=3997); le altre nove sono affermate senza fonte in riga. Il gate per la Fabbrica: prima di
mandare in produzione un numero-prova, o si allega la fonte (link, nome cliente, metodo di calcolo) o
si riscrive la frase togliendo la cifra — non si pubblica un numero nudo.

---

## LA STRUTTURA

Le tre pagine non hanno la stessa taglia: Servizi è un router corto (4229px, funziona da smistatore
verso le altre due), Landing e Consulenza sono pagine di vendita complete (16-17mila px ciascuna). Di
seguito le tappe che compaiono, in ordine, sulle tre pagine — numerate, con la sezione esatta (id,
heading, altezza y) dove presenti.

| # | Tappa | Servizi | Landing | Consulenza |
|---|---|---|---|---|
| 1 | Header/nav identico (Carriere, Menu) | sì (y=1197) | sì (y=13045) | sì (y=12692) |
| 2 | H1 + sottotitolo/qualificazione | sì, "Facciamo solo due cose. Per scelta." (y=177) | sì, "Il traffico lo paghi con le ads. Ma poi il tuo sito lo perde." (y=193) | sì, "Consulenza di problem solving con Andrei Pascu" (y=319) |
| 3 | CTA a bottone pieno già nell'hero | no — solo due link-teaser ai servizi | sì, "Rifai la tua landing →" (y=557) | sì, "Fai una consulenza adesso →" (y=742) |
| 4 | Barra micro-metriche in hero | no (le metriche sono dentro le due sezioni-servizio) | sì, "Costo ↓ più basso / Risultati ↑ più alti" (y=680) | sì, "Formato / Output / Prezzo" (y=652-845) |
| 5 | Sezione diagnosi/problema | no | sì, sezioni 2-5 (spesa→traffico→conversione) | sì, sezioni 2-3 (processo→vincolo) |
| 6 | Bio/social proof del founder | no | no (solo "Siamo AP Sales...", y=1094, senza foto né numeri) | sì, "Ma chi è Andrei Pascu?" (y=3013), con foto e 4 numeri |
| 7 | Metodo a step numerati | no (3 righe di processo per servizio, non numerate) | sì, "Come lavoriamo." 01-05 (y=4751) | no (ha invece il diagramma Input→Output, y=1214, e la timeline post-pagamento) |
| 8 | Lista puntata di deliverable | sì, breve: "Registrazione + piano in PDF" (y=1990) | sì, 5 bullet in "Landing Page AP Sales" (y=6245) | sì, 4 bullet in "Consulenza con Andrei Pascu." (y=10609-10850) |
| 9 | Tabella comparativa noi/altri | no | sì, "AP Sales, o un'altra agenzia?" (y=7758) | sì, "Andrei Pascu vs consulente medio." (y=12147) |
| 10 | Timeline "cosa succede dopo" | no | sì, 14 step, "Cosa succede dopo che ci contatti." (y=8738) | sì, 5 step, "Cosa succede dopo il pagamento." (y=11299) |
| 11 | FAQ | no | sì, 8 domande con risposta piena (y=12808) | sì, 14 domande, accordion chiuso (y=13244) |
| 12 | CTA di chiusura + footer identico | sì | sì | sì |

**Cosa hanno tutte e tre**: header/nav, H1 con qualificazione, lista deliverable (anche minima),
CTA di chiusura, footer verbatim identico (stessi 8 link, stesso indirizzo P.IVA, stessa formula di
copyright). **Cosa ha solo una pagina**: la bio del founder con foto e numeri esiste solo su
Consulenza; il metodo numerato 01-05 esiste solo su Landing; Servizi è l'unica delle tre a non avere
né diagnosi, né tabella comparativa, né timeline, né FAQ — coerente col suo ruolo di router: non deve
convincere, deve smistare in meno di 5 sezioni verso una delle altre due pagine, che fanno il lavoro
di persuasione vero.

---

## LA PROMESSA E DOVE STA

**Servizi** non ha una promessa di risultato in senso stretto: la sua promessa è posizionale, e sta
nel titolo stesso, in cima alla pagina (y=177): *"Facciamo solo due cose. Per scelta."* — la promessa
è "specializzazione totale", non "più conversioni". La promessa di risultato compare solo dentro le
due sotto-sezioni: *"Rifacciamo la pagina che riceve il tuo traffico."* (sezione Landing page, y=977,
prima riga della sezione) e *"Un'ora di problem solving con Andrei Pascu."* (sezione Consulenza,
y=1822, stessa posizione — prima riga sotto l'heading).

**Landing** apre con un problema, non con una promessa: l'H1 (y=193) è *"Il traffico lo paghi con le
ads. Ma poi il tuo sito lo perde."* — la promessa vera e propria arriva dopo, come h2 di una sezione
successiva (y=2179): *"Il nostro lavoro è aumentare quante persone comprano."* Tra le due c'è uno
scarto di quasi 2000px di scroll: la pagina fa vivere il problema prima di nominare cosa risolve.

**Consulenza** mette la promessa immediatamente sotto l'H1, non altrove: il sottotitolo (y=589, la
riga subito sotto il titolo) è *"Seguendo logica, problem solving e teoria dei vincoli per ricevere
chiare indicazioni su come crescere il prima possibile con meno rischio possibile."* — unica delle tre
pagine a mettere la promessa di risultato nel primo blocco di testo letto, non in una sezione
successiva.

---

## COME TRATTA LE OBIEZIONI

| Obiezione (implicita o esplicita) | Pagina | Frase che la gestisce |
|---|---|---|
| "Basta spendere di più in ads" | Landing | *"Perché «semplicemente spendi di più in ads» non è sempre la risposta."* (y=2331) — obiezione messa tra virgolette caporali e poi smontata dalle due frasi seguenti: *"La maggior parte delle aziende B2B non ha un problema di traffico... Il problema sta nella conversione."* |
| "Fate anche altro marketing oltre a landing/CRO?" | Landing (FAQ) | *"Offrite anche altri servizi di marketing? No, facciamo solo landing e consulenza di conversione (CRO). Trovi i nostri servizi completi nella pagina Servizi."* (y=13415) |
| "E se il lavoro non funziona, ho pagato per niente?" | Servizi + Landing | *"Se le conversioni non salgono, rimettiamo mano alla pagina. Gratis."* (Servizi, y=1273); *"Cosa succede se le conversioni non aumentano? Sulla base di condizioni chiare e semplici, rifacciamo la pagina gratuitamente. Quasi azzeriamo il tuo rischio."* (Landing FAQ, y=13260) |
| "Mi legate alla vostra piattaforma?" | Landing (FAQ) | *"Potete costruire sulla mia piattaforma? Sì, ma preferiamo la nostra... c'è una fee aggiuntiva."* (y=13570) — obiezione non negata, prezzata |
| "Sono un solo-founder, questo servizio è per aziende più strutturate" | Servizi + Consulenza | *"Lavori da solo? Vale lo stesso. Al posto del team, il vincolo sei tu."* (identica sulle due pagine, Servizi y=2193, Consulenza y=6578) |
| "In consulenza mi venderete altri servizi?" | Consulenza (FAQ) | Domanda nominata: *"In questa call mi verranno venduti servizi?"* (y=14005) — risposta non catturata, accordion chiuso nel DOM al momento dello screenshot: dichiaro l'assenza invece di inventarla |
| "Il mio problema non rientra nelle competenze di Andrei" | Consulenza | Nominata due volte: nella sezione sblocco, come limite dichiarato in anticipo — *"Finché rientra in un'area di competenza di Andrei Pascu."* (y=5481) — e come domanda FAQ, *"E se il mio problema non rientra nelle aree di Andrei?"* (y=14581, risposta non catturata) |
| "È un consiglio generato dall'AI, non da una persona vera?" | Consulenza (FAQ) | Nominata due volte: *"Andrei usa l'AI per darmi consigli?"* (y=13716) e *"Il riassunto che ricevo entro 48h è fatto dall'AI?"* (y=13812) — entrambe risposte non catturate, accordion chiuso |
| "Siete disonesti/usate trucchi da agenzia predatoria?" | Landing | Sezione intera dedicata, "Tecniche sostenibili." (y=10738): elenco esplicito di ciò che NON fanno — *"Timer finti"*, *"Numeri aziendali hardcoded"*, *"Recensioni finte"*, *"Testimonianze ingannevoli"* (y=11183-11305) — obiezione anticipata nominando prima loro le tecniche disoneste, poi negandole per sé |
| "Posso pagare in fattura/bonifico?" | Consulenza (FAQ, dato strutturato) | *"Fate fattura? Certamente. Dopo il pagamento troverai un modulo per inserire le tue informazioni fiscali... riceverai la fattura elettronicamente entro 24h dal pagamento."* — testo preso dal FAQPage schema in `scheda.json`, non visibile a schermo (accordion chiuso); la seconda voce, *"Posso pagare con bonifico?"*, è nello stesso schema ma il suo testo di risposta risulta troncato nella cattura e non lo riporto |

**Assenza notevole**: la pagina Servizi non gestisce nessuna obiezione in modo esplicito — non ha
FAQ, non ha sezione "tecniche sostenibili", non ha tabella comparativa. Il suo unico compito difensivo
è la qualificazione in ingresso (vedi sotto), non la gestione del dubbio.

---

## LE PROVE E LA LORO VERIFICABILITA'

| Cifra / affermazione | Pagina | Citazione | Fonte dichiarata in riga? | Verificabile dalla pagina? |
|---|---|---|---|---|
| "da 2 a 3,5%" (percentuale di conversione) | Landing | *"da2a3,5% ... la percentuale di persone che agisce dopo aver visto il tuo sito."* (y=2869-3005) | no | **No** — nessun cliente, nessun caso, nessun link |
| "+30 acquisti extra al mese" | Landing | con *"Assunzione: conversion rate 2,75% → 4,13% (+50%), stesso budget."* (y=3997) | **sì, esplicita** | **Sì, come proiezione dichiarata** — è un calcolatore con assunzione a vista, non uno spot di risultato reale; unico caso onesto delle 10 cifre |
| "250k Follower organici" | Consulenza | (y=3767) | no accanto al numero | Parziale — il profilo Instagram è linkato nel footer (`instagram.com/andrei.bsns`) ma non è agganciato alla cifra stessa: il lettore deve fare il collegamento da solo |
| "1.500 Clienti formazione" | Consulenza | (y=3767) | no | **No** |
| "100+ Clienti agenzia" | Consulenza | (y=3881) | no | **No** — nessun logo, nessun nome, su nessuna delle tre pagine |
| "3.900+ Ordini processati" | Consulenza | (y=3881) | no | **No** |
| "più di 100 imprenditori hanno deciso di investire" | Consulenza | (y=4979) | no | **No** |
| "più di 100 consulenze con imprenditori, e più di 50 consulenze con professionisti" | Consulenza | (y=7644) | no | **No** |
| "4,1 milioni di dichiaranti IVA in Italia" (2024) | Consulenza | (y=7271, con grafico "Distribuzione dei dichiaranti IVA italiani per fatturato, 2024") | no — nessuna fonte (es. Agenzia delle Entrate/ISTAT) citata accanto al grafico | **No** dalla pagina stessa, anche se è verosimilmente un dato pubblico reale |
| "€5.000 a €100.000 al mese in ads" (soglia cliente) | Servizi + Landing (FAQ) | *"Solo per B2B e B2B SaaS che investono da €5.000 a €100.000 al mese in ads."* (Servizi, y=586); ripetuta in Landing FAQ, *"Con che aziende lavorate? Aziende B2B o SaaS B2B che spendono almeno €5.000 in advertising..."* (y=13979) | n/a (è un criterio di ingresso, non una prova di risultato) | Coerente fra le due pagine — stesso numero, stesso ruolo di filtro |

**Il verdetto spietato richiesto dalla regola**: su dieci cifre-prova citate in queste tre pagine, nove
sono ipse dixit — affermate e basta, senza cliente nominato, senza link, senza metodo. L'unica che si
salva è quella del calcolatore interattivo di Landing, perché dichiara da sé l'assunzione che la
genera invece di spacciarla per un risultato osservato.

---

## LA SCALA DI IMPEGNO

Le tre pagine chiedono cose diverse, in ordine diverso, e questo è probabilmente il dato più
importante del teardown:

- **Servizi** non chiede nulla di suo: è un router. Offre solo scelte di percorso — i due link-teaser
  in hero ("Landing page" / "Consulenza"), poi due CTA a bottone dentro le rispettive sezioni
  ("Voglio rifare la pagina →" verso `/landing-page`, "Fai una consulenza →" verso `/consulenza`), poi
  li ripropone identici in chiusura ("Voglio rifare la landing →" / "Voglio una consulenza"). Nessun
  form, nessuna raccolta dati.
- **Landing** chiede un **form di qualificazione**, non un pagamento: dopo aver mostrato il metodo e i
  deliverable, la sezione "Parla con AP Sales subito." (y=6962) fa scegliere il tipo di azienda —
  *"Sono un'azienda B2B"* / *"Sono una SaaS"* / *"Altro"* — e solo dopo compare *"Parla con noi →"*.
  Il prezzo non compare mai in questo percorso: la promessa esplicita è *"Dicci chi sei, ti
  rispondiamo entro 24 ore."* (y=7106) — l'impegno richiesto è basso (un form), il rischio del prezzo
  è rimandato a una fase successiva, confermata dalla timeline "Cosa succede dopo che ci contatti.":
  prima una *"Chiamata conoscitiva"* (24h), poi solo *"se decidi di procedere"* una *"Chiamata di
  preventivo"* (y=8862-9069) — due chiamate prima che un numero venga pronunciato.
- **Consulenza** chiede il massimo impegno, e lo chiede subito: la CTA *"Fai una consulenza adesso →"*
  è già visibile nella prima schermata (y=742), non dopo lo scroll. Non c'è form di qualificazione, non
  c'è chiamata conoscitiva: il percorso è *"Paga, poi scegli data e ora →"* (y=10862) — pagamento
  diretto (€610) prima ancora di scegliere l'orario, confermato dalla nota *"Il modulo si apre qui,
  senza uscire dalla pagina."* (y=10940) e dalla timeline "Cosa succede dopo il pagamento.": il primo
  step è *"Completi il modulo di fatturazione"*, il secondo *"Scegli data e ora della tua
  consulenza"* (y=11439-11534) — si paga prima di prenotare, non il contrario.

La scala coerente sull'intero sito: prodotto a basso prezzo e alto rischio percepito per il cliente
(perché è impegnativo per il tempo di Andrei, non per il costo) → vendita diretta senza filtro umano.
Prodotto ad alto prezzo implicito e costruito su misura → filtro a due chiamate prima di dire un
numero.

---

## IL PREZZO

**Consulenza**: il prezzo esiste, è unico (**€610**) e compare identico su entrambe le pagine che lo
citano — Servizi (y=1810, in caratteri da 60px) e Consulenza stessa, sia nella barra hero (*"Prezzo
€610 IVA inclusa"*, y=845) sia nel blocco di conversione a metà pagina (**€610** in caratteri da
112px, y=10664). Le tre occorrenze sono sempre appaiate a "IVA inclusa" — mai il prezzo compare da
solo, sempre con la rassicurazione fiscale accanto, come se il rischio "poi mi arriva l'IVA sopra"
fosse un'obiezione abbastanza frequente da meritare una risposta automatica ogni volta.

**Landing**: il prezzo **non compare mai**, su nessuna delle tre pagine, come cifra. L'unico
riferimento è *"Prezzo Su preventivo, dopo l'audit"* (Servizi, y=1354) — un'etichetta "Prezzo" seguita
da un non-prezzo. La FAQ di Landing conferma il modello ma non la cifra: *"Che tipo di accordo
offrite? Un accordo una tantum, con riduzione del rischio grazie a operatività basate sulle
performance che ti portiamo. Paghi una volta."* (y=12924) — sappiamo che è un pagamento singolo, mai
quanto. Questo è un fatto rilevante quanto una cifra: la trasparenza di prezzo è riservata al prodotto
standardizzato e a basso costo unitario; il prodotto costoso e su misura resta sempre dietro una
conversazione umana prima di essere quotato.

---

## COSA NON DICE MAI

- **Nessun nome di cliente, nessun logo**, su nessuna delle tre pagine — né in Servizi, né in Landing,
  né in Consulenza. I numeri di traguardo (100+ clienti agenzia, 3.900+ ordini) restano quindi senza
  un solo esempio verificabile a corredo.
- **Nessun case study con numeri prima/dopo legati a un cliente reale**, su nessuna delle tre pagine —
  le uniche cifre di risultato ("da 2 a 3,5%", "+30 acquisti extra al mese") sono generiche o
  dichiaratamente ipotetiche, mai agganciate a un nome.
- **Nessuna testimonianza cliente**: le uniche citazioni in prima persona di tutta la pagina Consulenza
  sono di Andrei stesso (la sezione delle tre citazioni sulla "ghigliottina a 365 centimetri", y=8393-
  9123) — zero voci di clienti soddisfatti.
- **Nessuna descrizione del team**: il footer linka `/lavora-con-noi` e `/carriere` (presenti su tutte
  e tre le pagine), il che implica che un team esista, ma nel corpo di queste tre pagine non viene mai
  nominata una persona diversa da Andrei Pascu.
- **Nessun dettaglio sulle "condizioni chiare"** della garanzia di rilavorazione gratuita: la frase
  *"a condizioni chiare"* ricorre due volte (Servizi implicitamente con *"Gratis"*, Landing y=5628
  *"a condizioni chiare, se non salgono ci rimettiamo mano. Gratis."*) ma le condizioni stesse — quante
  settimane, quante revisioni, cosa succede se il traffico cambia nel frattempo — non sono mai
  elencate su queste tre pagine.
- **Nessuna scarsità artificiale**: coerente con la sezione "Tecniche sostenibili." di Landing, che
  elenca *"Timer finti"* come tecnica Black Hat da evitare (y=11183) — e infatti su nessuna delle tre
  pagine compare un countdown o una scorta limitata finta. L'unica leva di urgenza è reale e verificabile
  in linea di principio: *"Andrei è disponibile oggi stesso... Verificato dal calendario reale e
  aggiornato di Andrei Pascu."* (Consulenza, y=9882-9974).
- **Nessun servizio oltre a landing e consulenza**: dichiarato esplicitamente in negativo — *"No,
  facciamo solo landing e consulenza di conversione (CRO)."* (Landing FAQ, y=13415) — niente SEO, niente
  gestione ads, niente social, mai nominati come offerta.
- **Nessuna politica di rimborso** per il pagamento anticipato dei €610, nonostante esista una FAQ
  dedicata ai pagamenti (*"Fate fattura?"*, *"Posso pagare con bonifico?"*) — il tema del "e se cambio
  idea prima della call" non è mai affrontato nel testo catturato.

---

## LE FORMULE RICORRENTI

**1. Restrizione di scopo come prova di competenza**
Originale: *"Facciamo solo due cose. Per scelta."* (Servizi, y=177)
Riusabile: *"Facciamo solo [N] [COSE]. Per scelta."*

**2. Doppio percorso condizionato sulla diagnosi del lettore**
Originale: *"Se lo sai, si parte dalla pagina. Se non lo sai, si parte dall'ora insieme."* (Servizi,
y=2753)
Riusabile: *"Se [SAI GIA' X], si parte da [OPZIONE A]. Se non lo sai, si parte da [OPZIONE B]."*

**3. Redirezione dalla causa apparente alla causa vera**
Originale: *"La maggior parte delle aziende B2B non ha un problema di traffico... Il problema sta
nella conversione: cosa dici al tuo pubblico per convincerli a contattarti."* (Landing, y=2398-2472)
Riusabile: *"La maggior parte di [SEGMENTO] non ha un problema di [CAUSA APPARENTE]... Il problema
sta in [CAUSA VERA]: [DEFINIZIONE OPERATIVA]."*

**4. Disinnesco dell'obiezione "sono solo, non ho un team"**
Originale: *"Lavori da solo? Vale lo stesso. Al posto del team, il vincolo sei tu."* (identica su
Servizi y=2193 e Consulenza y=6578)
Riusabile: *"[FAI QUESTO] da solo? Vale lo stesso. Al posto di [RISORSA STRUTTURALE], [ELEMENTO]
sei tu."*

**5. Contrasto numerico per rivendicare focalizzazione**
Originale: *"Non dieci problemi. Uno."* (Consulenza, y=2018)
Riusabile: *"Non [N GRANDE] [COSE]. [UNA/UNO]."*

**6. Tripla negazione anaforica per posizionamento anti-fuffa**
Originale: *"No motivazione. No frasi magiche. No cazzate."* (Consulenza, y=10933)
Riusabile: *"No [X]. No [Y]. No [Z]."*

**7. Assunzione dichiarata a fianco del numero calcolato**
Originale: *"Assunzione: conversion rate 2,75% → 4,13% (+50%), stesso budget."* (Landing, y=3997)
Riusabile: *"Assunzione: [METRICA] [VALORE A] → [VALORE B] ([DELTA%]), [VARIABILE] costante."*

---

## Nota di chiusura

Il materiale letto (1.228 + 3.894 + 3.695 parole di copy sorgente, più le due schede JSON di sezioni)
bastava abbondantemente per superare le 2.500 parole richieste con sostanza reale, senza necessità di
aria: questo documento ne conta 3.506 (conteggio `wc -w` sul file, tabelle e frontmatter compresi).

## Connessioni

- [13-apsales-STACK-E-TOKEN.md](13-apsales-STACK-E-TOKEN.md) — stack tecnico e token colore dello
  stesso dominio (cattura diversa, l'homepage)
- [13-apsales-ATLANTE.md](13-apsales-ATLANTE.md) — atlante visivo sezione per sezione dell'homepage
- `PIANO-MAESTRO/33-PIANO-STUDIO-TOTALE-ANDREI-PASCU.md`
