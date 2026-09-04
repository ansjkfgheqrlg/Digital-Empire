
# Contenuto Integrale — rvpRQD43wdY
## "Come Avviare Un'Agenzia AI da 10.000€/Mese (Guida COMPLETA)" — Giovanni Beggiato (Gentes AI)

**Fonte:** trascrizione audio integrale (100%, 5.550 righe uniche deduplicate da 44.552 righe grezze del `.vtt`, lette in 12 blocchi) + campione visivo mirato (24/1.928 frame guardati nativamente, 1,2% — campionamento dichiarato, concentrato sulle sezioni a screen-share reale, motivato in `runs/max17-v17-beggiato-agenzia/coverage.md`).
**Durata:** 4h17m00s (15.420s) · **Uploader:** Giovanni Beggiato · **Lingua:** italiano
**Run:** `empire-studio/runs/max17-v17-beggiato-agenzia` (batch max17, il video più lungo del lotto)
**Ingested:** 2026-09-04 · **Archiviato (Memory Empire Stage C):** 2026-09-04

> **Regola applicata:** il video ha formato MISTO, verificato non presunto. I primi ~2h53m
> (capitoli 1-6) sono talking-head + whiteboard Excalidraw disegnata a mano in diretta (i disegni
> restano fissi a schermo fino a 31,5 minuti consecutivi in un caso verificato). Gli ultimi ~80
> minuti (capitoli 7-14) sono screen-share denso reale di tre strumenti esterni (Whimsical,
> GoHighLevel, Meta Ads Manager). Per questo il campione di frame guardati (24/1.928, 1,2%) è
> deliberatamente concentrato nella seconda metà — vedi `coverage.md` per la tabella completa e
> il motivo di ciascuna scelta.

---

## Capitoli ufficiali (da `ingest.json`, confermati a video)

| # | Titolo | Start | Durata |
|---|---|---|---|
| 1 | Intro | 0:00 | 3:37 |
| 2 | Ha senso aprire un'agenzia AI nel 2026? | 3:37 | 12:27 |
| 3 | Sto imparando cose obsolete? | 16:04 | 13:10 |
| 4 | Come scegliere la nicchia | 29:14 | 25:19 |
| 5 | Come prezzare l'offerta | 54:33 | 29:17 |
| 6 | Acquisizione clienti | 1:23:50 | 1:29:24 |
| 7 | Fulfillment: come consegnare il servizio | 2:53:14 | 22:18 |
| 8 | Cos'è GoHighLevel | 3:15:32 | 13:31 |
| 9 | Custom variables & custom fields | 3:29:03 | 5:45 |
| 10 | Funnel | 3:34:48 | 5:03 |
| 11 | Lead & calendario | 3:39:51 | 5:30 |
| 12 | Workflow di automazione | 3:45:21 | 7:02 |
| 13 | Meta Ads overview | 3:52:23 | 4:52 |
| 14 | Hiring & scaling | 3:57:15 | 19:45 |

---

## PARTE 1 — Intro (0:00–3:37)

Apre con un montaggio di clip di notizie/spezzoni ("cambiamento epocale", "lavoratori obsoleti",
timori di sostituzione da parte dell'AI) — **verificato a video**: `frame-0001.png` (0:00) mostra
una clip di repertorio della Presidente del Consiglio Giorgia Meloni a un podio istituzionale
("Presidenza del Consiglio dei Ministri", bandiera italiana + UE), usata come B-roll giornalistico
generico per illustrare il tema "cambiamento epocale in atto", non un contenuto originale del
relatore. Da qui presenta l'indice del video (le 14 tappe: agenzia AI oggi, obsolescenza skill,
definizione, nicchia, pricing, acquisizione clienti con 6 metodologie, sistema end-to-end
Meta-Ads→GoHighLevel→chiamata umana, fulfillment, scaling). Si presenta come fondatore di
un'agenzia AI (**Gentes**, dominio `gentes.ai`, confermato a schermo in più frame successivi) con
clienti da 10.000€/mese fino a "50 milioni di euro all'anno" e una community privata
("Avanguardia Plus").

## PARTE 2 — Ha senso aprire un'agenzia AI nel 2026? (3:37–16:04)

**Frame-0029.png (3:44, guardato)** conferma a schermo: whiteboard Excalidraw con titolo "Ha senso
aprire un'agenzia AI, oggi?" e due grafici a griglia di puntini stile Eurostat — "Europeans who use
generative AI for work" e "...for education", ciascun puntino = 3,2 milioni di persone, bandierine
per paese. Dati citati a voce (non verificati indipendentemente da questa sessione, fonte
dichiarata "Eurostat 2025" leggibile a schermo): mondo, 84% (6,8 miliardi) non ha mai usato l'AI;
16% (1,3 miliardi) usa solo modelli gratuiti; 0,3% (~25 milioni) paga un abbonamento AI; solo
0,04% (2-5 milioni) usa "coding harness" agentici (Claude Code, Codex). Italia: terzultimo posto
in Europa per uso AI generativa sul lavoro (8% contro 92% che non la usa), quintultimo per
educazione (6,4%), penultimo per uso personale (12,8%).

Framework **Blue Ocean vs Red Ocean Strategy** (cita il libro *Blue Ocean Strategy*): Blue Ocean =
mercato libero ma senza "proof of concept" (nessuno ci ha mai venduto nulla — o perché nessuno se
n'è accorto, tipo Facebook/Instagram/Netflix all'epoca, o perché qualcuno ci ha provato ed è
fallito, esempio Tesla vs precedenti tentativi di auto elettriche/idrogeno — **verificato a
schermo**: `frame-0263.png`, 35:04, mostra il disegno a mano con le due frecce "NON AVETE 'POC'
(PROOF OF CONCEPT)" → "libero?" e "ci ha provato ed ha fallito" → bubble "TESLA (877)" più a
destra "99%... ho deciso che è un pessimo mercato"). Red Ocean = mercati saturi (palestre,
dentisti, real estate) dove la proof of concept esiste già — consiglio esplicito dell'autore:
partire in Red Ocean con un'offerta differenziante, non in Blue Ocean, "se non sei milionario e
non puoi permetterti di perdere capitale".

## PARTE 3 — Sto imparando cose obsolete? (16:04–29:14)

Tesi: un'agenzia (qualsiasi, AI o no) è sempre la stessa struttura — lead generation → funnel →
vendita → onboarding → CRM → delivery → upselling — e il tool AI specifico (n8n, Make, Claude
Code, Codex...) è la parte che cambia nel tempo, non lo scheletro di business. Framework delle
"3 figure" che servono a qualsiasi azienda: chi fa promozione, chi fa il prodotto, chi fa le daily
ops. Le persone si bloccano soprattutto sull'acquisizione clienti per timidezza/paura del rifiuto.

## PARTE 4 — Come scegliere la nicchia (29:14–54:33)

Due framework per identificare la nicchia:
1. **Se sai fare qualcosa** → modello delle **3P**: Passion, Profession, Pain (del cliente) — cita
   anche l'**Ikigai** come lettura consigliata (intersezione passione/domanda/pagamento).
2. **Se non sai fare nulla** → evitare nicchie regolamentate (farmaceutico, assicurazioni,
   banking — cicli di verifica troppo lunghi); metodo reale di chi ha successo, non quello
   "logico" (chiedere a ChatGPT le 5 nicchie migliori): **testare 5-6 nicchie in parallelo**,
   contattare ~100 persone per nicchia, misurare i risultati, poi concentrarsi sulle 2-3 che
   convertono meglio (esempio numerico dato a voce: da 6 nicchie testate, 2 a zero clienti
   scartate, focus sulle rimanenti, poi l'80% del fatturato arriva da 2 sole).

Regola esplicita anti-"niche hopping": permanenza minima consigliata di **6 mesi** su una
nicchia prima di scartarla — 30 chiamate a freddo non sono un campione sufficiente per giudicare
una nicchia morta; chi salta nicchia ogni poche settimane resta sotto la soglia dei 3.000€/mese
perché non accumula mai competenza verticale.

## PARTE 5 — Come prezzare l'offerta (54:33–1:23:50)

Matrice di pricing 3×3 **verificata a schermo** (`frame-0451.png`, 60:08): righe **DIY / DWY / DFY**
(Do It Yourself, Done With You, Done For You) × colonne **Tempo / Unità / Risultato** — esempio
mostrato: cella DIY-Unità = "ebook, PDF". A voce vengono riempite le altre celle: DFY-tempo =
consulenza a ore (sconsigliata dall'autore); DWY-unità = formazione/corso con revisione;
DWY-risultato = coaching a percentuale (raro); DFY-unità = "vendo 3 automazioni a X€" (il quadrante
dove l'autore colloca la maggior parte delle soluzioni AI, più scalabile perché disaccoppiato dal
tempo); DFY-risultato = pagamento a risultato ottenuto.

Tre modelli contrattuali: **pay in full** (paga tutto oggi, 3.000-10.000€ upfront, difficile da
vendere senza track record), **pay on performance** (es. paga solo l'ad-spend, 25-200€/giorno, il
resto solo a risultato — permette ticket anche oltre 10.000€ perché il rischio lo prende
l'agenzia), **retainer** (misto: fee di setup iniziale + % variabile per lead/cliente o fee fissa
mensile, es. 250€/mese).

**Regola del close rate al 30%** (golden rule esplicita, ripetuta più volte): percentuale di lead
che arrivano in sales call e pagano. Sopra il 30% → prezzo troppo basso (si sta perdendo margine);
sotto il 30% → prezzo troppo alto o vendita debole. Per community/infoprodotti il benchmark citato
è diverso (2-4%).

## PARTE 6 — Acquisizione clienti (1:23:50–2:53:14, capitolo più lungo, 1h29m)

Elenco a schermo dei **6 metodi ordinati per facilità/costo crescente** — **verificato a video**,
`frame-0631.png` (1:24:00): *"1. Warm Network · 2. Upwork · 3. Strategie Cold (DM, Email, Call) ·
4. Ads · 5. Fiverr · 6. Social Media Posting (Organico)"*.

**1. Warm Network.** Mappare la propria rubrica (amici stretti, familiari, amici di amici,
conoscenti — **verificato**, `frame-0676.png`, 1:30:08) e clusterizzarla per professione
(impiegato/imprenditore/studente). Script di contatto testato dall'autore: *"Ho aperto da poco
un'azienda di AI... sto cercando due clienti a cui implementare questo servizio gratuitamente.
Conosci qualcuno a cui potrebbe interessare? [...] l'unica cosa che chiedo in cambio è un
testimonial e almeno due referral"* — **verificato**, `frame-0751.png` (1:40:08), mostra lo
stesso schema di risposta attesa per amico/studente ("si, conosco genitori di X, ti do il
contatto") vs dipendente. Meccanica di crescita a catena: 1 cliente gratuito → 2 referral → 2
nuovi clienti (a pagamento crescente, es. 250€→500€→1.000€) → altri referral. Osservazione
comportamentale: le persone aiutano molto di più a inizio carriera (quando non c'è ancora
"invidia sociale") che a metà crescita — quindi è il momento migliore per chiedere aiuto, non
quello peggiore come si crede.

**2. Upwork.** Demo dal vivo della piattaforma — **verificato**, `frame-1235.png` (2:44:32): lista
di annunci reali ("Email Flow Creator for Automation", "Notion Workspace Setup for Small Team"),
filtri per parole chiave, connects/costi (~1€ per candidatura). Mostra due skill Claude create
dall'autore (non nel repo DE, solo nella sua community): "vaglia annuncio" (valuta se conviene
investire i connects) e "roast del profilo" (critica il profilo Upwork prima di candidarsi).
Consiglio: prezzi non tondi (es. 13,15$/h, non 15$) per differenziarsi, applicare entro 24 ore
dalla pubblicazione dell'annuncio.

**3. Strategie Cold (email, DM, call).** Framework del funnel con metriche: input (es. 100
email/DM) → open rate (80%) → reply rate (30%) → CTR sui link (20%) → risposte positive (10%) →
conversione a meeting (8% sull'input o 80% sulle risposte positive) → clienti paganti (2%). Ogni
metrica bassa indica un problema diverso da correggere (oggetto scadente → open rate basso;
offerta scadente → reply rate basso; sales call debole → conversione meeting→cliente bassa).
Tecnica "cold reading" per l'apertura del messaggio — **verificato a schermo**,
`frame-0899.png` (1:59:44): schema "oggetto: xy 4 you; domande {{nome}}?" / "body: → COLD READING
=>" — frase generica applicabile a chiunque ma percepita come personalizzata (tecnica attribuita a
"FBI e servizi di profiling"), seguita da credenziale sociale (nome noto nello stesso spazio),
offerta con risk reversal (setup gratuito, paghi solo a risultato). Per il cold calling:
script identifica decision-maker → 2 domande di scoperta del problema → offerta di 10 minuti senza
impegno → CTA a fissare appuntamento; aspettarsi 80-90% di rifiuti.

**Curva cold vs organico vs ads nel tempo** — **verificato a schermo**, `frame-1075.png` (2:23:12):
tre curve colorate (blu, verde, rosso) su asse tempo/guadagno con "plateau" — le strategie cold
danno risultati rapidi ma con plateau presto; il contenuto organico cresce lentamente ma senza
plateau evidente nel breve; gli ads, quando funzionano, salgono ripidi. Dato personale citato:
canale LinkedIn, 54.000 follower in un anno.

**5. Fiverr.** Demo di ricerca servizi (video editing, automation AI, ads) con pacchetti
basic/standard/premium, consigliato solo con un brand già riconosciuto per generare inbound.

**6. Ads + contenuto organico** trattati insieme come "stessa curva nel tempo": il contenuto
organico serve a validare quali messaggi/creatività funzionano (le "pepite d'oro" — un post
virale ripostato più volte, esempio concreto mostrato scorrendo il proprio LinkedIn con numeri di
impressions/like/repost reali) prima di spingerci soldi in ads, altrimenti si spreca budget su
contenuti non validati. Menzione della "200 views cage" (fase iniziale in cui un creator resta
bloccato tra 200 e 2.500 views) e consiglio esplicito: monetizzare prima con outbound, investire
poi nel personal brand — non il contrario.

## PARTE 7 — Fulfillment (2:53:14–3:15:32)

Regola cardine: un cliente esiste **solo se c'è stato un movimento di denaro** (un "sì" via email
non è un cliente). Processo di kickoff call documentato con un flowchart Whimsical reale —
**verificato a schermo**, `frame-1401.png` (3:06:40, URL visibile
`whimsical.com/beggiato-media/how-to-service-your-first-automation-client-in-2026-...`): "Hai già
fatto questo progetto?" → SÌ: "Customizza un template esistente sulla richiesta del cliente" / NO:
"Costruisci un MVP" / "Comincia a costruire" / "Templetizza la soluzione". Punti della kickoff
call: 1) timeline del progetto con under-promise-and-overdeliver (es. dichiarare 6 settimane,
consegnare in 4); 2) reperibilità esplicita (giorni/orari di risposta); 3) definizione del
successo/deliverable per prevenire lo scope creep (richieste aggiuntive non concordate);
4) registrazione del cliente sulle piattaforme necessarie durante la call stessa; 5) tracciamento
in un project management tool (opzionale per il primo cliente). Policy dichiarata sulle
credenziali: l'autore lavora sempre sulle credenziali/abbonamenti del cliente, mai proprie,
per evitare vendor lock-in ("ghigliottina" sul cliente) — preferisce riproporre servizi
aggiuntivi via email/upsell piuttosto che trattenere l'accesso come leva.

Continuazione del flowchart Whimsical — **verificato**, `frame-1440.png` (3:11:52): "Aggiorna sui
progressi" → "Usa dei template per fare speed-up del processo" (link a "Project Update Templates"
e "Project Delivery Templates" nella sua community) → invio ogni due settimane fino a
"Progetto completato" → "Test Style Workflow End-to-End (e2e)" → "Rafforza i check per i casi
limite" (edge cases). Dopo la consegna: SOP (Standard Operating Procedure) in Google Doc + video
di spiegazione custom, poi proposta di upsell mentre l'interesse del cliente è ancora alto.

## PARTE 8 — Cos'è GoHighLevel (3:15:32–3:29:03)

Overview della piattaforma CRM "all-in-one per agenzie": ~97$/mese, piano starter con 3
sub-account, programma di affiliazione fino al 50% ricorrente. **Verificato a schermo**,
`frame-1511.png` (3:21:20): dashboard reale dell'account `gentes.ai` (Vicenza, VI) — "Opportunity
status" 11, "Opportunity value" totale €10,92K / vinto €3,93K, "Conversion rate" 9,09% (coerente
con quanto detto a voce, "10,9... conversion rate del 9%"), funnel "Marketing Pipeline" con stadi
Nuovo lead / Contattato. Spiega il modello sub-account = un cliente = un contenitore isolato
(evita di mischiare dati/messaggi tra clienti diversi).

## PARTE 9 — Custom variables & custom fields (3:29:03–3:34:48)

Distinzione tecnica centrale per la templetizzazione: custom values = dati legati al
sub-account/cliente (es. nome agenzia, città — cambiano quando si rivende il sistema a un nuovo
cliente in un'altra città), custom fields = dati legati al singolo lead (es. origine,
consenso, campagna). Confondere le due categorie è l'errore da evitare per rendere un funnel
davvero riutilizzabile/templetizzabile.

## PARTE 10 — Funnel (3:34:48–3:39:51)

Demo di creazione funnel/landing page in GoHighLevel — **verificato a schermo**,
`frame-1590.png` (3:31:52) e `frame-1651.png` (3:40:00): funnel reale "Valutazione casa -
Vicenza" con 2 step (Valutazione, Grazie), hostato su `demo.gentes.ai`. Spiega la struttura
landing page: form di raccolta dati in alto, sezione di "warming up" del lead freddo (contenuto
esplicativo) più in basso con bottone che riporta al form.

## PARTE 11 — Lead & calendario (3:39:51–3:45:21)

Pipeline Opportunities — **verificato a schermo**, `frame-1687.png` (3:44:48): board
"Immobiliare — dal lead all'in..." con colonne Nuovo lead (5), Chiamato, Appuntamento fissato,
Sopralluogo fatto. Setup calendario (disponibilità, durata slot, buffer) collegato al form —
senza questo collegamento l'automazione di prenotazione non funziona.

## PARTE 12 — Workflow di automazione (3:45:21–3:52:23)

Demo del workflow che parte dalla submission del form Meta: crea opportunità in pipeline → invia
messaggio/email di "presa in carico" (aumenta il pickup-rate delle chiamate successive, tecnica
chiamata "taking in charge") → chiama l'operatore umano (mai l'AI direttamente al lead — evita
"brand impact" negativo) → se l'operatore preme 1, il sistema chiama il lead e mette in contatto
diretto con l'umano → se non risponde, sequenza di nurturing a cicli di 20 minuti con messaggi
alternati (SMS/email) fino a un ultimo messaggio di chiusura.

## PARTE 13 — Meta Ads overview (3:52:23–3:57:15)

Demo di creazione campagna Meta Ads — **verificato a schermo**, `frame-1745.png` (3:52:32): Ads
Manager reale, campagna "Immobiliar Demo - Contatti - corso agenzia AI", budget totale €20,00,
stato "In bozza". Passaggi mostrati: obiettivo contatti, moduli interattivi (lead form) collegati
al CRM, targeting geografico (Vicenza), collegamento del modulo al funnel GoHighLevel già creato.

## PARTE 14 — Hiring & scaling (3:57:15–4:16:58)

**Verificato a schermo**, `frame-1781.png` (3:57:20): titolo Excalidraw "Scaling & Hiring".
Regola: assumere quando si è a capacità (non più tempo per nuovo lavoro), e per bisogno, non
per crescita, specialmente all'inizio — assumere per crescita è una scommessa che, se fallisce,
lascia l'imprenditore in perdita netta. Il primo hire consigliato è un CTO (non un
commerciale), anche se costoso (5.000-6.000€+/mese), perché libera l'imprenditore dalla delivery
per concentrarsi sulle vendite (l'unica attività che fa crescere il fatturato). Prerequisito: SOP
già documentate prima di assumere, altrimenti il nuovo hire "rincorre" l'imprenditore per ogni
informazione mancante. **Verificato a schermo**, `frame-1875.png` (4:09:52): grafico a mano con
due curve "Fatturato" e "Salario" che divergono dopo l'assunzione del CTO (il salario
dell'imprenditore scende temporaneamente), seguito da un secondo grafico dopo l'assunzione del
sales team, e riquadro "SOP = Standard Operating Procedure" con processo numerato. Chiusura:
l'agenzia AI non è quasi mai l'ultimo business — è la "benzina iniziale" (soldi, esperienza,
network) che porta poi a business più scalabili (SaaS, community, digital product); l'errore
comune è scartare l'agenzia perché "cappata" a 1-3 milioni/anno confrontandola con business
teoricamente più scalabili invece che con lo stipendio da dipendente di partenza.

---

## Nota sulla community/prodotti citati (non ingeriti nel dettaglio)

Il video cita più volte contenuti extra disponibili solo nella community privata dell'autore
("Avanguardia Plus"): un PDF di 90 pagine/18 capitoli sulla costruzione dell'offerta, una
masterclass di cold email (60+ pagine), un corso di personal brand su LinkedIn (5-6 ore), un
corso ads. Questi contenuti non sono stati visti né ingeriti in questa sessione — sono dietro
paywall, riportati qui solo come riferimento a ciò che l'autore dichiara di offrire.
