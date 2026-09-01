# REF_04 — Edge Cases Matrix

## Matrice Completa degli Edge Cases per SaaS e Web App

---

## Introduzione: Perché gli Edge Cases Non Sono Opzionali

Un PRD scritto per un developer umano esperto può permettersi alcune lacune. Il developer sa per esperienza cosa fare quando una lista è vuota, quando la rete cade, quando un'API risponde con un errore 500. Colma i gap con buon senso e convenzioni di settore.

Un PRD scritto per un agente AI non può permettersi questa latitudine.

L'AI non ha "buon senso". Esegue letteralmente ciò che è scritto. Se il PRD descrive solo il happy path — l'utente che inserisce dati validi, la rete sempre disponibile, l'API sempre responsive — l'AI costruirà esattamente quello. E il prodotto risultante avrà buchi enormi nelle situazioni limite, che sono proprio quelle dove gli utenti abbandonano l'app o perdono fiducia.

**Gli edge cases non sono casi rari.** Sono eventi quotidiani:
- Un utente apre l'app per la prima volta → empty state (succede al 100% degli utenti)
- Un utente con connessione mobile lenta → loading state prolungato (succede frequentemente)
- Un server risponde lentamente → error state (succede ogni giorno in produzione)
- Un utente free prova una feature premium → permission denied (funzione critica di monetizzazione)

Se questi scenari non sono documentati nel PRD, non verranno implementati correttamente. Questo file fornisce la matrice completa per identificarli, documentarli e verificarli prima di consegnare qualsiasi PRD.

---

## Le 8 Categorie Universali

### 1. EMPTY STATE

**Definizione**
Lo stato in cui una componente (lista, tabella, dashboard, feed) non ha dati da mostrare. Può essere perché l'utente non ha ancora creato nulla (empty state "vergine"), perché ha cancellato tutto, o perché un filtro/ricerca non ha prodotto risultati.

**Trigger — quando si applica**
- Qualsiasi lista, tabella, griglia, feed
- Dashboard con metriche (zero transazioni, zero clienti)
- Risultati di ricerca o filtro
- Notifiche, messaggi, commenti
- Prima sessione utente su qualsiasi sezione

**Domanda di verifica**
"Cosa vede l'utente se questo componente non ha dati da mostrare?"

**Esempio compilato — SaaS generico (CRM)**
```
EMPTY STATE — Lista Contatti

Trigger: L'utente accede alla sezione Contatti senza averne ancora importati.

Comportamento atteso:
- Illustrazione (non solo testo)
- Headline: "Ancora nessun contatto"
- Sottotitolo: "Aggiungi il tuo primo contatto manualmente o importa da CSV"
- CTA primario: [+ Aggiungi contatto]
- CTA secondario: [Importa da CSV]

Variante — filtro attivo senza risultati:
- Headline: "Nessun contatto corrisponde ai filtri"
- Sottotitolo: "Prova a modificare i criteri di ricerca"
- CTA: [Rimuovi filtri]
- NON mostrare la CTA "Aggiungi contatto" — sarebbe confusa

Variante — ricerca testuale senza risultati:
- Headline: "Nessun risultato per '[query]'"
- Sottotitolo: "Controlla l'ortografia o prova parole chiave diverse"
- CTA: [Cancella ricerca]
```

**Segnali che mancano nel PRD**
- Il PRD descrive la lista ma non dice cosa mostra quando è vuota
- Il PRD usa frasi come "mostra la lista dei [X]" senza menzionare il caso zero elementi
- Non c'è distinzione tra "mai avuto dati" e "dati filtrati/non trovati"
- Manca specificazione se l'empty state deve avere CTA o meno

---

### 2. LOADING STATE

**Definizione**
Lo stato transitorio mentre i dati vengono caricati, un'azione viene processata, o un'operazione è in corso. Diversi pattern rispondono a esigenze diverse: skeleton screen per contenuto atteso, spinner per operazioni brevi, progress bar per operazioni con avanzamento misurabile.

**Trigger — quando si applica**
- Ogni richiesta HTTP/API che può richiedere >200ms
- Ogni submit di form che triggera elaborazione server-side
- Ogni operazione di upload/download
- Navigazione tra pagine con caricamento dati
- Operazioni AI (spesso 2-15 secondi)

**Domanda di verifica**
"Cosa vede l'utente mentre aspetta? Per quanto tempo prima che l'attesa diventi percepita come errore?"

**Quando usare quale pattern**

| Pattern | Quando | Durata tipica | Esempio |
|---------|--------|---------------|---------|
| **Skeleton screen** | Contenuto con struttura prevedibile | 0.3-3s | Feed post, lista utenti, dashboard |
| **Spinner inline** | Azione su un singolo elemento | 0.5-2s | Like, follow, toggle switch |
| **Full-page spinner** | Navigazione, autenticazione | 0.5-1.5s | Login, redirect OAuth |
| **Progress bar** | Upload file, elaborazione batch | >2s con step misurabili | Upload CSV, export report |
| **Skeleton + progress** | Operazioni AI o long-running | >3s | Generazione AI, analisi documento |
| **Optimistic update** | Azioni reversibili a bassa criticità | N/A (immediato) | Toggle preferito, archivia email |

**Esempio compilato — SaaS generico (Dashboard Analytics)**
```
LOADING STATE — Dashboard principale

Trigger: Utente naviga su /dashboard, dati in caricamento da API.

Comportamento atteso:
- Skeleton screen che replica il layout delle card metriche
  - 4 card metriche: placeholder grigio animato 40x40px + barra testo 60% width
  - Grafico principale: placeholder rettangolare 100% x 200px animato
  - Tabella transazioni: 5 righe skeleton con colonne simulate
- Animazione: fade pulse (opacity 0.4→1 loop 1.2s ease-in-out)
- Timeout: se dopo 8s i dati non arrivano → mostra error state con retry

Comportamento NON accettabile:
- Pagina bianca
- Testo "Loading..." senza struttura visiva
- Spinner centrato su pagina (solo per navigazione, non per dashboard)
```

**Segnali che mancano nel PRD**
- Il PRD non specifica il tipo di loading (skeleton vs spinner vs progress)
- Non c'è timeout definito per quando il loading diventa un errore
- Le operazioni AI non hanno loading state esplicito nonostante latenza elevata
- Forms senza indicazione di "submitting" state sul bottone

---

### 3. ERROR STATE

**Definizione**
Qualsiasi condizione in cui un'operazione non riesce. Le categorie di errore richiedono UX diverse: gli errori di validazione richiedono guida contestuale, gli errori di rete richiedono retry, gli errori di auth richiedono redirect, gli errori server richiedono escalation.

**Trigger — quando si applica**
- Qualsiasi chiamata API (può fallire)
- Qualsiasi form submission (validazione + errori server)
- Auth token scaduto durante una sessione attiva
- Errori di business logic (es: "non puoi fare questo con il tuo piano")
- Errori di sistema (500, timeout, rate limit)

**Domanda di verifica**
"Se questa operazione fallisce, l'utente capisce cosa è andato storto e cosa fare?"

**Tipologia errori e comportamento atteso**

| Tipo errore | HTTP | Messaggio all'utente | Azione suggerita |
|-------------|------|---------------------|-----------------|
| Validazione input | 400/422 | Specifico: "L'email non è valida" | Highlight campo, non resettare form |
| Non autenticato | 401 | "Sessione scaduta" | Redirect a login, preserva URL destinazione |
| Non autorizzato | 403 | "Non hai accesso a questa funzione" | Link upgrade o info su permessi |
| Non trovato | 404 | "Questa risorsa non esiste" | Link back o ricerca alternativa |
| Rate limit | 429 | "Hai raggiunto il limite. Riprova tra X minuti" | Timer countdown |
| Server error | 500 | "Errore temporaneo. I nostri tecnici sono avvisati" | Retry button |
| Network error | N/A | "Controlla la connessione internet" | Retry button |
| Timeout | N/A | "La richiesta sta impiegando troppo tempo" | Retry + report bug |

**Esempio compilato — SaaS generico (Form di pagamento)**
```
ERROR STATE — Form di pagamento (Stripe)

Scenario A — Carta rifiutata:
- Non resettare il form
- Mostrare banner error sopra il form: "Pagamento rifiutato: fondi insufficienti"
- Highlight del campo carta con bordo rosso
- Suggerimento: "Prova un altro metodo di pagamento"
- CTA: [Prova altra carta] | [Contatta supporto]

Scenario B — Errore di rete durante submit:
- Spinner si trasforma in icona errore
- Messaggio: "Connessione interrotta. Il tuo pagamento NON è stato addebitato."
- CTA prominente: [Riprova]
- Link secondario: "Contatta il supporto se il problema persiste"
- NON mostrare messaggi tecnici (codici errore Stripe, stack trace)

Scenario C — Sessione scaduta durante checkout:
- Modale: "La tua sessione è scaduta"
- Opzioni: [Accedi di nuovo] | [Continua come ospite]
- Preservare i dati del carrello/form dopo il re-login
```

**Segnali che mancano nel PRD**
- Il PRD gestisce solo il caso "submit va a buon fine"
- Non c'è distinzione tra tipi di errore
- I messaggi di errore non sono specificati (solo "mostra errore")
- Non è chiaro se il form si resetta o mantiene i dati dopo un errore
- Auth expiry durante flussi critici non è documentato

---

### 4. SUCCESS STATE

**Definizione**
Il feedback che conferma all'utente che un'azione è stata completata con successo. Spesso sottovalutato, è critico per la trust e il retention: gli utenti che non ricevono conferma eseguono l'azione due volte o pensano che sia andata storta.

**Trigger — quando si applica**
- Submit di qualsiasi form
- Completamento di qualsiasi azione con effetti persistenti (salva, pubblica, invia, cancella)
- Fine di un processo multi-step
- Completamento di un'operazione lunga (upload, export, elaborazione)

**Domanda di verifica**
"Come sa l'utente che l'azione è andata a buon fine? Il feedback è proporzionale all'importanza dell'azione?"

**Livelli di feedback per importanza**

| Importanza azione | Pattern | Durata |
|-------------------|---------|--------|
| Bassa (auto-save, toggle) | Nessun feedback o micro-animation | Immediato |
| Media (salvataggio manuale, aggiunta item) | Toast notification | 3-4s auto-dismiss |
| Alta (submit form, invio email) | Toast persistente + stato UI aggiornato | 5s o click-to-dismiss |
| Critica (pagamento, cancellazione account, invio contratto) | Pagina/modale di conferma dedicata | Rimane fino a navigazione esplicita |

**Esempio compilato — QuickInvoice (app preventivi freelance)**
```
SUCCESS STATE — Invio preventivo al cliente

Azione: Utente clicca "Invia preventivo" dopo composizione.

Comportamento atteso:
- Redirect immediato a pagina /invoices/[id]/sent
- Header: "Preventivo inviato con successo"
- Riepilogo: destinatario, importo, data di scadenza
- Status badge: "In attesa di risposta" (giallo)
- Timeline: "Inviato il [data ora] — Email consegnata"
- CTA primari: [Crea nuovo preventivo] | [Torna alla lista]
- CTA secondario: [Invia promemoria] (disponibile dopo 48h)
- Email di conferma inviata all'utente (non solo al cliente)

Comportamento NON accettabile:
- Toast "Preventivo inviato" da solo senza cambio di stato/pagina
- Ritorno alla lista senza conferma che l'invio è avvenuto
- Nessuna indicazione dell'email di destinazione
```

**Segnali che mancano nel PRD**
- Solo "mostra toast di successo" senza specificare contenuto
- Nessuna distinzione tra azioni di importanza diversa
- Non è documentato il cambio di stato dell'UI dopo il successo
- Manca la comunicazione email/notifica di conferma per azioni critiche

---

### 5. OFFLINE STATE

**Definizione**
Lo stato in cui l'app rileva che l'utente non ha connessione internet. Rilevante per mobile app, PWA e qualsiasi app usata in contesti mobili. Richiede strategie di caching e sincronizzazione.

**Trigger — quando si applica**
- App mobile nativa
- Progressive Web App (PWA)
- Qualsiasi web app con Service Worker
- App usate in contesti a bassa connettività (field workers, trasporti)

**Domanda di verifica**
"Cosa può fare l'utente senza connessione? Cosa succede ai dati inseriti offline quando la connessione ritorna?"

**Strategie offline per tipo di operazione**

| Operazione | Strategia consigliata |
|------------|----------------------|
| Lettura dati | Cache (stale-while-revalidate), mostra banner "Dati non aggiornati" |
| Scrittura dati | Queue offline, sync automatica al ripristino connessione |
| Operazioni critiche (pagamenti) | Blocca e informa chiaramente, non tentare offline |
| Media upload | Queue con indicatore di "in attesa di connessione" |

**Esempio compilato — FocusBoard (task manager con AI)**
```
OFFLINE STATE — FocusBoard app mobile

Trigger: Dispositivo perde connessione mentre utente è nell'app.

Banner persistente (non bloccante) in cima: 
"Sei offline — le modifiche verranno salvate quando torni online"

Funzionalità disponibili offline:
- Visualizzazione task esistenti (da cache locale)
- Creazione nuovi task (con sync pending indicator: icona cloud con slash)
- Completamento task (con sync pending)
- Modifica note task

Funzionalità NON disponibili offline:
- Analisi AI task
- Collaborazione team (real-time)
- Sincronizzazione con calendario esterno

Al ripristino connessione:
- Banner: "Di nuovo online — sincronizzazione in corso..."
- Progress indicator per n task in coda
- Conflict resolution: se stesso task modificato da altro utente → morale con diff
- Banner verde "Tutto sincronizzato" per 3s poi scompare
```

**Segnali che mancano nel PRD**
- App mobile senza menzione di offline state
- PWA senza strategia di caching documentata
- Nessuna indicazione su quali dati vengono cachati
- Conflict resolution non documentato per sync offline→online

---

### 6. PERMISSION DENIED

**Definizione**
Lo stato in cui un utente tenta di accedere a una funzionalità a cui non ha diritto — perché è su un piano inferiore, perché non ha il ruolo appropriato, o perché la feature è in beta/non disponibile nella sua area geografica.

**Trigger — quando si applica**
- App con feature gating (free/pro/enterprise)
- App con ruoli utente (admin/member/viewer)
- Feature in beta riservata a utenti specifici
- Dati di altri utenti in contesti multi-tenant
- Azioni che richiedono verifica (email, 2FA)

**Domanda di verifica**
"Quando l'utente raggiunge un limite del suo piano o dei suoi permessi, come viene comunicato e cosa gli viene offerto?"

**Pattern per permission denied**

| Contesto | Pattern UX | Note |
|----------|------------|------|
| Feature premium visibile nella nav | Mostra feature con lock icon + tooltip | Non nascondere — crea desiderio |
| Feature premium in azione | Modale upgrade inline | Non redirect a pricing page |
| Ruolo insufficiente | Banner informativo + contatta admin | Non mostrare come errore generico |
| Dati di altri utenti | 404 (non 403) | Non rivelare esistenza risorse |
| Email non verificata | Banner persistente + resend CTA | |
| 2FA richiesta | Step obbligatorio prima dell'azione | |

**Esempio compilato — SaaS B2B (piano free vs pro)**
```
PERMISSION DENIED — Export report (feature pro)

Scenario: Utente piano Free clicca su "Esporta CSV" nella sezione Reports.

Comportamento atteso:
- Il bottone "Esporta CSV" è visibile ma con badge "PRO"
- Al click: modale inline (non redirect)
  - Headline: "Export CSV è disponibile nel piano Pro"
  - Benefit: "Con Pro puoi esportare report illimitati in CSV, Excel e PDF"
  - CTA primario: [Passa a Pro — €29/mese]
  - CTA secondario: [Vedi tutti i benefici del Pro]
  - Link: [Rimanda per ora] (dismiss)
- NON mostrare errore 403 o messaggio tecnico
- NON redirigere a /pricing (interrompe il flusso)

Scenario: Utente "Member" tenta operazione admin:
- Modale: "Questa operazione richiede permessi di Admin"
- Info: "Chiedi al tuo Admin [nome admin] di eseguire questa operazione"
- CTA: [Invia richiesta all'Admin] (notifica email all'admin)
```

**Segnali che mancano nel PRD**
- Feature premium non documentate come gated
- Ruoli utente definiti ma comportamento "non autorizzato" non specificato
- Nessun upsell funnel documentato per feature premium
- Il PRD assume tutti gli utenti abbiano gli stessi permessi

---

### 7. RATE LIMIT

**Definizione**
Lo stato in cui l'utente ha superato i limiti di utilizzo imposti dal piano, dall'API esterna, o dalle politiche anti-abuse. Critico da documentare perché impatta sia la monetizzazione che l'esperienza utente.

**Trigger — quando si applica**
- App con limiti per piano (es: 100 email/mese nel piano free)
- Integrazione con API esterne che hanno rate limit (OpenAI, Twilio, SendGrid)
- Azioni ad alta frequenza potenzialmente abusive (login attempts, form submit)
- Feature AI con costo per utilizzo

**Domanda di verifica**
"L'utente sa quanti utilizzi gli restano? Cosa succede quando li finisce? Come si sblocca?"

**Esempio compilato — AI Tool (generazione testi)**
```
RATE LIMIT — Generazioni AI (piano Free: 10/giorno)

Visualizzazione utilizzo:
- Indicatore persistente in header: "7/10 generazioni usate oggi"
- Barra progressiva con cambio colore: verde→giallo→rosso
- Al raggiungimento di 8/10: banner warning "Stai per raggiungere il limite"

Quando limite raggiunto (10/10):
- Bottone "Genera" disabilitato con tooltip: "Limite giornaliero raggiunto"
- Banner: "Hai usato tutte le 10 generazioni gratuite di oggi"
- Opzioni:
  1. [Passa a Pro — generazioni illimitate] → modale pricing
  2. "Il tuo limite si resetta domani alle 00:00"
  3. [Invita un amico per +5 generazioni] (referral)

Rate limit da API esterna (OpenAI):
- NON mostrare errore OpenAI all'utente
- Tradurre in: "Il servizio è momentaneamente occupato. Riprova tra 30 secondi."
- Retry automatico silenzioso dopo 30s se l'utente è ancora sulla pagina
- Log interno dell'evento per monitoring
```

**Segnali che mancano nel PRD**
- Limiti di piano non documentati con UX associata
- Nessun indicatore di utilizzo corrente
- Dipendenze da API esterne senza documentazione del comportamento in caso di rate limit
- Nessuna strategia di retry per rate limit temporanei

---

### 8. DATA CORRUPTED

**Definizione**
Lo stato in cui i dati ricevuti (da API, da input utente, da database) sono malformati, incompleti, o in formato inatteso. Questo edge case è spesso ignorato perché si assume che i dati siano sempre corretti — in produzione non è così.

**Trigger — quando si applica**
- Integrazione con API esterne che possono cambiare formato
- Import di file (CSV, Excel, JSON) da utenti
- Risposta AI malformata o troncata
- Migrazione dati legacy
- Race condition in operazioni concorrenti
- Utenti che manipolano URL o payload direttamente

**Domanda di verifica**
"Cosa succede se un'API risponde con un formato inatteso, o se un file importato contiene dati sporchi?"

**Esempio compilato — QuickInvoice (import clienti da CSV)**
```
DATA CORRUPTED — Import clienti da CSV

Fase validazione (pre-import):
- Parsing del CSV lato client prima dell'upload
- Preview delle prime 5 righe con mapping colonne
- Highlight in giallo: campi opzionali mancanti (es: telefono)
- Highlight in rosso: campi obbligatori mancanti o invalidi (es: email malformata)
- Conteggio: "23 righe valide, 3 righe con errori"

Opzioni all'utente:
- [Importa solo le righe valide (23)]
- [Scarica CSV errori] per correzione manuale
- [Annulla]

Non fare:
- Import cieco → dati corrotti in database
- Blocco totale se anche solo 1 riga è invalida
- Importare email invalide che faranno bouncing

Risposta API esterna malformata (es: campo atteso mancante):
- Non crashare il rendering del componente
- Mostrare il componente in stato degradato: campo mancante → "—" o "N/D"
- Log dell'anomalia con payload ricevuto per debugging
- Se critico: mostrare banner "Dati parzialmente non disponibili"
```

**Segnali che mancano nel PRD**
- Import file senza processo di validazione documentato
- Dipendenze da API esterne senza gestione di risposta malformata
- Rendering di dati da API senza fallback per campi mancanti
- Nessuna strategia di graceful degradation per dati incompleti

---

## Matrix per Tipo di Prodotto

La tabella mostra la criticità di ogni edge case per tipo di prodotto.  
**C** = Critico (mancante = bug grave), **I** = Importante (mancante = UX scadente), **O** = Opzionale (nice-to-have).

| Edge Case | SaaS B2B | SaaS Consumer | Mobile App | Marketplace | AI Tool |
|-----------|----------|---------------|------------|-------------|---------|
| **Empty State** | C | C | C | C | C |
| **Loading State — skeleton** | C | C | I | C | I |
| **Loading State — progress** | I | I | C | I | C |
| **Error — validazione** | C | C | C | C | C |
| **Error — network** | I | C | C | I | C |
| **Error — auth expiry** | C | C | C | C | C |
| **Error — server 500** | C | C | C | C | C |
| **Success State** | C | C | C | C | C |
| **Offline State** | O | I | C | I | I |
| **Permission — piano** | C | C | I | I | C |
| **Permission — ruolo** | C | O | O | C | O |
| **Rate Limit — piano** | C | C | I | I | C |
| **Rate Limit — API esterna** | I | I | I | I | C |
| **Data Corrupted — import** | C | I | I | C | I |
| **Data Corrupted — API** | C | C | C | C | C |

### Note per tipo di prodotto

**SaaS B2B (dashboard, report, team features)**
Priorità assoluta: permission denied con ruoli (admin/member/viewer), empty state di dashboard/report, data corrupted su import dati da sistemi legacy.

**SaaS Consumer (onboarding, payments, notifications)**
Priorità assoluta: error state nei pagamenti (mai perdere una transazione), success state per azioni critiche, offline state se ha app mobile correlata.

**Mobile App**
Offline state è obbligatorio, non opzionale. Loading states con feedback tattile (haptic). Progress bar per qualsiasi upload. Error states con action button — non solo testo.

**Marketplace (2 lati: buyer + seller)**
Empty state diverso per buyer ("nessun prodotto disponibile") e seller ("non hai ancora listato nulla"). Permission denied per azioni riservate a seller verificati. Rate limit su listing se anti-spam necessario.

**AI Tool (latenza alta, fallback quando AI fallisce)**
Loading state per generazione AI è il più critico — utenti abbandonano se non c'è feedback di progresso. Fallback quando AI fallisce (timeout, content policy, error) — deve essere documentato esplicitamente nel PRD. Rate limit con visibilità dell'utilizzo rimasto.

---

## Esempi Compilati per Prodotto di Riferimento

### QuickInvoice — App Preventivi Freelance

**Empty State — Dashboard**
```markdown
## Empty State — Dashboard QuickInvoice

Trigger: Utente nuovo, zero preventivi creati.

Layout:
- Illustrazione centrale: disegnatore alla scrivania (SVG, no foto stock)
- Headline: "Crea il tuo primo preventivo in 2 minuti"
- Body: "QuickInvoice ti aiuta a creare preventivi professionali 
  e inviarli ai tuoi clienti in pochi click"
- CTA primario: [+ Crea preventivo] → /invoices/new
- Link secondario: [Guarda come funziona →] → video tutorial 90s

Variante — zero clienti (se sezione Clienti è vuota):
- Headline: "Aggiungi i tuoi clienti per velocizzare la creazione preventivi"
- CTA: [+ Aggiungi cliente] | [Importa da CSV]
```

**Error State — Invio preventivo fallito**
```markdown
## Error State — Email preventivo non consegnata

Trigger: API email (es. SendGrid) restituisce errore di delivery.

Comportamento:
- Status del preventivo aggiornato a "Errore di invio" (icona warning)
- Toast persistente: "Impossibile inviare l'email al cliente"
- Dettaglio: "Email [cliente@email.com] non raggiungibile"
- CTA: [Riprova invio] | [Copia link diretto al preventivo]
- Link: [Contatta supporto]

NON fare:
- Mostrare "Preventivo inviato" anche se l'email è fallita
- Lasciare il preventivo in stato "In attesa" senza segnalare l'errore
```

**Loading State — Generazione preventivo AI**
```markdown
## Loading State — AI Draft Generation

Trigger: Utente ha descritto il lavoro in linguaggio naturale, 
l'AI sta generando le voci del preventivo.

Comportamento:
- Overlay semitrasparente sulla form preventivo
- Spinner con messaggio progressivo ogni 3s:
  - "Sto analizzando la tua descrizione..."
  - "Sto strutturando le voci di costo..."
  - "Quasi pronto..."
- Durata stimata: 5-12s
- Timeout: se dopo 20s non risponde → 
  "La generazione AI sta impiegando troppo. [Riprova] o [Inserisci manualmente]"
```

**Permission Denied — Export clienti (feature Pro)**
```markdown
## Permission Denied — Export clienti CSV

Trigger: Utente piano Starter clicca "Esporta clienti" 

Comportamento:
- Modale inline (non redirect):
  Headline: "Esporta i tuoi clienti con QuickInvoice Pro"
  Body: "Esporta tutti i tuoi clienti in CSV in un click. 
         Integra con il tuo CRM o crea backup automatici."
  Prezzo: "QuickInvoice Pro — €9/mese"
  CTA: [Attiva Pro] | [Scopri tutti i benefici]
  Link: [Ora no]
- NON mostrare errore generico
- NON disabilitare il bottone senza spiegazione
```

---

### FocusBoard — Task Manager con AI

**Empty State — Nessun task**
```markdown
## Empty State — Lista task (vuota)

Trigger A: Nuovo utente, primo accesso, zero task.
Comportamento:
- Illustrazione minimalista con mood "focus mattutino"
- Headline: "Inizia la tua giornata con chiarezza"
- Body: "Aggiungi il tuo primo task o lascia che l'AI organizzi 
         la tua lista dalle note di ieri"
- CTA primario: [+ Aggiungi task]
- CTA AI: [Genera task da note] (se note precedenti esistono)

Trigger B: Tutti i task completati per oggi.
Comportamento (diverso da "mai avuto task"):
- Illustrazione celebrativa (non stessa del trigger A)
- Headline: "Tutto completato! Ottimo lavoro."
- Body: "Hai completato tutti i task di oggi."
- CTA: [Pianifica domani] | [Vedi il riepilogo]
```

**Loading State — AI task prioritization**
```markdown
## Loading State — AI Task Prioritization

Trigger: Utente clicca "Lascia che l'AI organizzi la mia lista"

Fase 1 (0-2s): "Sto leggendo i tuoi task..."
Fase 2 (2-5s): "Sto valutando urgenza e importanza..."
Fase 3 (5-8s): "Sto applicando la matrice di priorità..."

UI durante loading:
- Lista task sfumata (opacity 0.5)
- Barra progress lineare in cima alla lista con % avanzamento
- Testo fase corrente sotto la barra
- Bottone "Annulla" disponibile sempre

Al completamento:
- Animazione: task che si riordinano con motion fluido (slide)
- Badge "AI" su ogni task con il ragionamento (tooltip on hover)
```

**Offline State — FocusBoard PWA**
```markdown
## Offline State — FocusBoard

Trigger: Service Worker rileva assenza connessione.

Banner persistente non-bloccante (bottom of screen):
"Offline — le modifiche vengono salvate localmente"

Disponibile offline:
- Visualizzazione tutti i task (da IndexedDB cache)
- Creazione task (con indicatore pending sync: icona nuvola/freccia)
- Completamento task
- Timer Pomodoro (funzione locale)
- Note task

Non disponibile offline (bottoni disabilitati con tooltip):
- Analisi AI task ("Richiede connessione")
- Sync calendario ("Richiede connessione")
- Condivisione task con team

Al ripristino connessione (banner 3s):
"Connesso — sincronizzazione in corso (3 task)"
→ "Tutto sincronizzato ✓"
```

---

### E-commerce Generico

**Empty State — Carrello vuoto**
```markdown
## Empty State — Carrello

Trigger: Utente accede a /cart con zero prodotti.

Layout:
- Icona carrello vuoto (non illustrazione generica)
- Headline: "Il tuo carrello è vuoto"
- CTA primario: [Torna allo shopping]
- Sezione: "Potrebbe interessarti" (4 prodotti raccomandati basati su browsing)
- Se utente loggato con wishlist: "Hai X prodotti nella tua wishlist" + [Vedi wishlist]
```

**Error State — Pagamento fallito**
```markdown
## Error State — Pagamento rifiutato

Trigger: Stripe restituisce payment_intent.payment_failed

Comportamento:
- NON fare redirect a pagina errore
- Rimane sulla checkout page
- Banner rosso sopra form pagamento:
  "Pagamento non riuscito: [motivo specifico Stripe tradotto]"
  Esempi:
  - card_declined → "Carta rifiutata dalla banca emittente"
  - insufficient_funds → "Fondi insufficienti"
  - expired_card → "Carta scaduta — inserisci una carta valida"
- Form pagamento resettato (solo i dati carta, non indirizzo)
- CTA: [Prova con un altro metodo] | [PayPal] | [Contatta supporto]
- NON perdi i prodotti nel carrello
- NON reinserire indirizzo di spedizione
```

**Rate Limit — Coupon promo**
```markdown
## Rate Limit — Tentativi codice sconto

Trigger: Utente ha inserito 5 codici sconto errati (anti-abuse).

Comportamento:
- Campo coupon disabilitato per 10 minuti
- Messaggio: "Troppi tentativi. Riprova tra [timer conto alla rovescia]"
- Log dell'evento per review anti-frode
- Se IP sospetto dopo terzo episodio: flag account per review manuale
```

---

## Checklist Rapida Edge Cases

Per ogni feature con interazione utente, verifica questi 10 punti prima di finalizzare la sezione PRD:

```
EDGE CASE CHECKLIST — [Nome Feature]

□ 1. EMPTY STATE
   L'interfaccia ha dati da mostrare? → documentato cosa succede se è vuota?
   Il vuoto "mai avuto dati" è diverso da "filtro/ricerca senza risultati"?

□ 2. LOADING STATE
   Questa feature fa richieste async? → tipo di loading specificato (skeleton/spinner/progress)?
   C'è un timeout definito dopo il quale il loading diventa un errore?

□ 3. ERROR STATE
   Tipo di errore specificato (validazione / network / server / auth)?
   Il messaggio di errore è comprensibile da un utente non tecnico?
   Dopo l'errore, i dati inseriti vengono preservati o persi?

□ 4. SUCCESS STATE
   Il feedback è proporzionale all'importanza dell'azione?
   Per azioni critiche (pagamento, invio, cancellazione): c'è una pagina/modale dedicata?

□ 5. OFFLINE STATE (se mobile/PWA)
   Questa feature funziona offline? Se no, è documentato?
   I dati offline vengono sincronizzati al ripristino connessione?

□ 6. PERMISSION DENIED
   Questa feature è gatata per piano o ruolo?
   L'utente senza accesso vede un upsell o solo un errore?

□ 7. RATE LIMIT
   Questa feature ha limiti di utilizzo?
   L'utente può vedere quanti utilizzi gli restano?

□ 8. DATA CORRUPTED
   Questa feature accetta input da utente (file, testo libero)?
   Questa feature dipende da API esterne? → documentato il fallback se risposta malformata?

□ 9. PARTIAL DATA
   Il componente funziona se alcuni campi opzionali sono null/undefined?
   Valori estremi testati: stringa molto lunga, numero negativo, caratteri speciali?

□ 10. CONCURRENT ACTIONS
   Cosa succede se lo stesso utente apre la feature in due tab?
   Cosa succede se due utenti modificano lo stesso record simultaneamente?
```

---

## Template Sezione Edge Cases per PRD

Questo blocco markdown va inserito alla fine di ogni sezione feature del PRD:

```markdown
### Edge Cases — [Nome Feature]

#### Empty State
**Trigger:** [quando si applica]
**Comportamento atteso:** 
- [descrizione UI]
- CTA: [azione disponibile]

#### Loading State
**Tipo:** [skeleton / spinner / progress bar]
**Timeout:** [Xs → error state]
**Comportamento:**
- [descrizione animazione/skeleton]

#### Error States
| Scenario | Messaggio Utente | Azione Disponibile |
|----------|-----------------|-------------------|
| [tipo errore] | "[testo messaggio]" | [CTA o link] |
| [tipo errore] | "[testo messaggio]" | [CTA o link] |

#### Success State
**Tipo feedback:** [toast / pagina dedicata / inline]
**Contenuto:** [cosa viene mostrato]
**Durata:** [auto-dismiss Xs / persiste fino a navigazione]

#### Permission / Plan Gating
**Chi può accedere:** [piano/ruolo]
**Comportamento per utenti non autorizzati:** 
- [descrizione modale/messaggio]
- Upsell: [sì/no — tipo]

#### Rate Limits
**Limite:** [N azioni per [periodo]]
**Indicatore utilizzo:** [dove/come viene mostrato]
**Comportamento al raggiungimento limite:** [descrizione]

#### Validazione Input / Data Integrity
**Regole di validazione:**
- [campo]: [regola] → errore: "[messaggio]"
**Fallback dati malformati da API:** [comportamento]
```

---

*Fine REF_04 — Edge Cases Matrix*  
*Versione 1.0 — PRD Architect OS Knowledge Base*
