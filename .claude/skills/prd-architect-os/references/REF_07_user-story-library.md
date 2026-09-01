# REF_07 — User Story Library (50+ Stories Compilate)

> Documento di riferimento per PRD Architect OS — Libreria user stories pronte all'uso.
> Usato durante la generazione della sezione "User Stories" in tutti i tipi di PRD.

---

## Formato User Story e Standard di Qualità

### Il formato corretto

```
Come [tipo utente specifico e contestualizzato],
voglio [azione specifica e misurabile],
in modo da [beneficio concreto, non generico].
```

**Errori comuni da evitare:**
- ❌ "Come utente voglio fare login" → troppo generico
- ✅ "Come nuovo utente che si registra per la prima volta voglio ricevere un'email di conferma con link one-click in modo da verificare il mio account senza inserire password una seconda volta"

Il tipo utente deve essere contestualizzato al prodotto (non "utente" generico). Il beneficio deve essere specifico e misurabile, non "per usare il prodotto".

---

### Acceptance Criteria: PASSA SE / FALLISCE SE

Ogni story deve avere criteri testabili. Il tester deve poter dire "sì" o "no" a ogni criterio senza interpretazione.

**Struttura:**
```
- [ ] ✅ PASSA SE: [condizione osservabile e misurabile]
- [ ] ✅ PASSA SE: [seconda condizione]
- [ ] ❌ FALLISCE SE: [condizione di fallimento critica]
- [ ] ❌ FALLISCE SE: [secondo caso di fallimento]
```

**Regola:** Almeno 2 PASSA SE e 1 FALLISCE SE per ogni story. Le storie critiche (P0) devono averne di più.

---

### Framework di Prioritizzazione P0 / P1 / P2

| Priorità | Definizione | Impatto se manca |
|---|---|---|
| **P0** | Il prodotto non funziona senza questa feature. Blocca il lancio. | Impossibile usare il prodotto |
| **P1** | Feature importante per la user experience core. Presente al lancio. | Esperienza degradata, utenti si lamentano |
| **P2** | Nice-to-have. Può aspettare la versione 1.1 o 2.0. | Assenza non notata dalla maggioranza degli utenti |

**Regola pratica:** Se ti viene il dubbio se una story è P0 o P1, chiediti: "Se lancio senza questa feature, il prodotto è usabile?" → Sì = P1, No = P0.

### Stime di Effort (T-shirt sizing)

| Size | Giorni stima | Descrizione |
|---|---|---|
| **XS** | < 1 giorno | Modifica UI, copy change, piccolo fix |
| **S** | 1-2 giorni | Feature semplice, 1 endpoint, 1 componente |
| **M** | 3-5 giorni | Feature media, più componenti, logica backend |
| **L** | 1-2 settimane | Feature complessa, integrazioni, stato globale |
| **XL** | > 2 settimane | Epic, richiede breakdown in storie più piccole |

---

## CATEGORIA 1: Autenticazione e Account

> **Epic**: Gli utenti possono creare, accedere e gestire il proprio account in sicurezza.
> **Obiettivo business**: Ridurre attrito all'onboarding e garantire sicurezza dell'identità.

---

#### 1.1 Registrazione via Email

**Come** visitatore non registrato che arriva alla pagina di signup,
**voglio** creare un account inserendo email e password in meno di 60 secondi,
**in modo da** iniziare a usare il prodotto senza barriere tecniche.

**Acceptance Criteria**:
- [ ] ✅ PASSA SE: il form accetta email valida + password min 8 caratteri e crea l'account
- [ ] ✅ PASSA SE: l'utente riceve email di verifica entro 60 secondi dalla registrazione
- [ ] ✅ PASSA SE: email duplicata mostra messaggio di errore chiaro ("email già registrata")
- [ ] ❌ FALLISCE SE: l'account viene creato senza che l'utente riceva l'email di verifica
- [ ] ❌ FALLISCE SE: password deboli (<8 caratteri) vengono accettate senza warning

**Priority**: P0 — Il prodotto non è accessibile senza registrazione
**Effort**: S
**Note**: Considera il double opt-in per ridurre spam accounts. Mostrare indicatore forza password in tempo reale.

---

#### 1.2 Login Email / Password

**Come** utente registrato che ritorna al prodotto,
**voglio** accedere inserendo email e password dalla pagina di login,
**in modo da** riprendere il mio lavoro dal punto in cui mi ero fermato.

**Acceptance Criteria**:
- [ ] ✅ PASSA SE: credenziali corrette portano alla dashboard in meno di 3 secondi
- [ ] ✅ PASSA SE: credenziali errate mostrano messaggio "email o password non corretti" (no specifico su quale)
- [ ] ✅ PASSA SE: dopo 5 tentativi falliti, l'account viene bloccato per 15 minuti
- [ ] ❌ FALLISCE SE: il sistema specifica se è l'email o la password a essere sbagliata (security issue)
- [ ] ❌ FALLISCE SE: la sessione non persiste dopo chiusura e riapertura del browser

**Priority**: P0 — Accesso base al prodotto
**Effort**: S
**Note**: "Remember me" checkbox per sessioni persistenti. Redirect alla pagina originale dopo login (se l'utente era su /dashboard/settings, torna lì).

---

#### 1.3 Google OAuth Login

**Come** utente che preferisce non gestire un'altra password,
**voglio** registrarmi e accedere con il mio account Google in un click,
**in modo da** eliminare l'attrito di creare e ricordare nuove credenziali.

**Acceptance Criteria**:
- [ ] ✅ PASSA SE: click su "Continua con Google" apre popup OAuth di Google e completa login
- [ ] ✅ PASSA SE: primo accesso con Google crea automaticamente un account nel sistema
- [ ] ✅ PASSA SE: se l'email Google coincide con un account esistente, gli account vengono collegati
- [ ] ❌ FALLISCE SE: il popup OAuth viene bloccato dai browser (usare redirect invece di popup)
- [ ] ❌ FALLISCE SE: un utente può creare due account distinti con la stessa email (uno Google, uno email)

**Priority**: P0 — Riduce attrito signup del 40-60%
**Effort**: S
**Note**: Implementare anche GitHub OAuth se il target include developer. Google è sempre P0, GitHub è P1.

---

#### 1.4 Forgot Password

**Come** utente registrato che ha dimenticato la password,
**voglio** ricevere un link per reimpostare la password via email,
**in modo da** recuperare l'accesso al mio account senza contattare il supporto.

**Acceptance Criteria**:
- [ ] ✅ PASSA SE: inserendo l'email arriva email con link reset entro 60 secondi
- [ ] ✅ PASSA SE: il link reset è valido per massimo 1 ora dall'invio
- [ ] ✅ PASSA SE: dopo l'uso, il link reset viene invalidato (non riutilizzabile)
- [ ] ✅ PASSA SE: se l'email non esiste nel sistema, il messaggio è generico (no user enumeration)
- [ ] ❌ FALLISCE SE: il link reset non scade mai
- [ ] ❌ FALLISCE SE: è possibile richiedere più di 3 reset password per la stessa email in 1 ora

**Priority**: P0 — Senza questo il supporto è sommerso di richieste
**Effort**: S
**Note**: Mostrare sempre "Se l'email esiste, riceverai un link" — mai confermare l'esistenza dell'account.

---

#### 1.5 Change Email

**Come** utente con account attivo,
**voglio** cambiare l'email associata al mio account dalle impostazioni,
**in modo da** mantenere il mio account aggiornato se cambio provider email.

**Acceptance Criteria**:
- [ ] ✅ PASSA SE: l'utente inserisce nuova email + conferma password attuale
- [ ] ✅ PASSA SE: viene inviata email di verifica alla nuova email prima che il cambio avvenga
- [ ] ✅ PASSA SE: fino alla verifica della nuova email, si continua ad accedere con quella vecchia
- [ ] ❌ FALLISCE SE: il cambio avviene immediatamente senza verifica della nuova email
- [ ] ❌ FALLISCE SE: si può cambiare email senza confermare la password attuale

**Priority**: P1
**Effort**: M
**Note**: Inviare notifica anche alla vecchia email ("qualcuno ha cambiato la tua email — non eri tu?").

---

#### 1.6 Delete Account

**Come** utente che vuole smettere di usare il prodotto,
**voglio** eliminare definitivamente il mio account e tutti i dati associati,
**in modo da** esercitare il mio diritto alla cancellazione dei dati (GDPR).

**Acceptance Criteria**:
- [ ] ✅ PASSA SE: l'eliminazione richiede conferma esplicita (digitare "ELIMINA" o simile)
- [ ] ✅ PASSA SE: viene mostrato un riepilogo di cosa verrà eliminato prima della conferma
- [ ] ✅ PASSA SE: tutti i dati dell'utente vengono cancellati entro 30 giorni (GDPR)
- [ ] ✅ PASSA SE: l'utente riceve email di conferma avvenuta eliminazione
- [ ] ❌ FALLISCE SE: l'eliminazione è irreversibile senza un periodo di grazia (almeno 7 giorni)
- [ ] ❌ FALLISCE SE: dati dell'utente rimangono nel DB dopo l'eliminazione

**Priority**: P1 — Obbligatorio per compliance GDPR
**Effort**: M
**Note**: Considerare "soft delete" con periodo di grazia di 14-30 giorni prima della cancellazione permanente.

---

#### 1.7 Configurazione 2FA (Two-Factor Authentication)

**Come** utente attento alla sicurezza del proprio account,
**voglio** abilitare l'autenticazione a due fattori tramite app authenticator,
**in modo da** proteggere l'account anche in caso di compromissione della password.

**Acceptance Criteria**:
- [ ] ✅ PASSA SE: viene mostrato QR code da scansionare con Google Authenticator / Authy
- [ ] ✅ PASSA SE: l'attivazione richiede verifica del codice TOTP prima di essere completata
- [ ] ✅ PASSA SE: vengono forniti 10 codici di backup monouso in caso di perdita del dispositivo
- [ ] ❌ FALLISCE SE: si può disabilitare il 2FA senza verificare il codice attuale
- [ ] ❌ FALLISCE SE: i codici di backup non vengono invalidati dopo l'uso

**Priority**: P1 — Obbligatorio per SaaS B2B enterprise
**Effort**: M
**Note**: Per SaaS B2C, P2. Per SaaS B2B con dati sensibili, P0.

---

#### 1.8 Session Management

**Come** utente che accede al prodotto da più dispositivi,
**voglio** vedere e gestire le sessioni attive del mio account,
**in modo da** revocare l'accesso a dispositivi che non riconosco o che ho perso.

**Acceptance Criteria**:
- [ ] ✅ PASSA SE: la lista mostra dispositivo, browser, IP approssimativo e data ultimo accesso
- [ ] ✅ PASSA SE: il pulsante "Disconnetti" su una sessione la invalida immediatamente
- [ ] ✅ PASSA SE: "Disconnetti tutte le altre sessioni" funziona e mostra conferma
- [ ] ❌ FALLISCE SE: la sessione corrente può essere disconnessa accidentalmente dalla lista
- [ ] ❌ FALLISCE SE: la disconnessione non invalida il token lato server (solo lato client)

**Priority**: P1
**Effort**: M
**Note**: Inviare notifica email quando viene rilevato login da nuovo dispositivo/IP.

---

#### 1.9 Aggiornamento Profilo

**Come** utente con account attivo,
**voglio** aggiornare le informazioni del mio profilo (nome, bio, preferenze),
**in modo da** personalizzare la mia identità nel prodotto e nelle comunicazioni.

**Acceptance Criteria**:
- [ ] ✅ PASSA SE: le modifiche vengono salvate e riflesse nell'UI senza reload della pagina
- [ ] ✅ PASSA SE: i campi hanno validazione inline (lunghezza massima, caratteri speciali)
- [ ] ✅ PASSA SE: viene mostrata conferma "Profilo aggiornato" dopo salvataggio
- [ ] ❌ FALLISCE SE: il form resetta i valori se la validazione fallisce su un campo
- [ ] ❌ FALLISCE SE: non esiste un modo per annullare le modifiche non salvate

**Priority**: P1
**Effort**: S

---

#### 1.10 Upload Avatar

**Come** utente che vuole personalizzare il proprio profilo,
**voglio** caricare un'immagine come foto profilo,
**in modo da** essere riconoscibile nei contesti collaborativi e rendere l'esperienza più personale.

**Acceptance Criteria**:
- [ ] ✅ PASSA SE: vengono accettati formati JPG, PNG, WebP fino a 5MB
- [ ] ✅ PASSA SE: l'immagine viene compressa/ottimizzata automaticamente prima dello storage
- [ ] ✅ PASSA SE: viene mostrata anteprima prima del salvataggio definitivo
- [ ] ✅ PASSA SE: esiste un avatar generato automaticamente (iniziali o identicon) come fallback
- [ ] ❌ FALLISCE SE: file troppo grandi causano timeout senza messaggio di errore chiaro
- [ ] ❌ FALLISCE SE: l'avatar vecchio rimane visibile in cache dopo l'aggiornamento

**Priority**: P2
**Effort**: S
**Note**: Implementare crop circolare nel browser prima dell'upload per uniformità.

---

## CATEGORIA 2: Onboarding

> **Epic**: I nuovi utenti raggiungono il primo valore (First Value Moment) entro 5 minuti dalla registrazione.
> **Obiettivo business**: Aumentare activation rate e ridurre il time-to-value.

---

#### 2.1 Welcome Wizard — Step 1: Raccolta Informazioni Base

**Come** nuovo utente che ha appena verificato l'email,
**voglio** completare un setup guidato di 3-5 step che personalizza l'esperienza,
**in modo da** iniziare a usare il prodotto in modo rilevante per il mio caso d'uso specifico.

**Acceptance Criteria**:
- [ ] ✅ PASSA SE: il wizard si avvia automaticamente al primo accesso dopo verifica email
- [ ] ✅ PASSA SE: viene mostrata barra di progresso con numero step ("Step 1 di 4")
- [ ] ✅ PASSA SE: i dati inseriti vengono salvati ad ogni step (no perdita se si chiude il browser)
- [ ] ✅ PASSA SE: l'utente può saltare il wizard e completarlo dopo dalle impostazioni
- [ ] ❌ FALLISCE SE: il wizard si ripresenta ad ogni login anche dopo completamento
- [ ] ❌ FALLISCE SE: non esiste escape route per chi vuole saltare il setup

**Priority**: P0 — Impatto diretto su activation rate
**Effort**: L
**Note**: Non superare 5 step. Ogni step aggiuntivo riduce il completion rate del 15-20%.

---

#### 2.2 Configurazione Iniziale del Workspace

**Come** nuovo utente nel wizard di setup,
**voglio** configurare le impostazioni base del mio workspace (nome, settore, dimensione team),
**in modo da** ricevere contenuti, template e suggerimenti personalizzati.

**Acceptance Criteria**:
- [ ] ✅ PASSA SE: il form richiede solo i campi strettamente necessari (max 4-5 campi)
- [ ] ✅ PASSA SE: le opzioni per "settore" e "dimensione team" sono predefinite (dropdown, non testo libero)
- [ ] ✅ PASSA SE: le scelte fatte qui influenzano visibilmente i contenuti mostrati in dashboard
- [ ] ❌ FALLISCE SE: vengono richiesti dati non necessari per il primo valore (es: numero di telefono obbligatorio)

**Priority**: P0
**Effort**: M

---

#### 2.3 Primo Valore — First Value Moment

**Come** nuovo utente che ha completato il setup base,
**voglio** completare la mia prima azione di valore all'interno del prodotto entro 5 minuti,
**in modo da** capire subito il beneficio concreto che il prodotto mi offre.

**Acceptance Criteria**:
- [ ] ✅ PASSA SE: il wizard guida l'utente verso la prima azione chiave del prodotto
- [ ] ✅ PASSA SE: la prima azione produce un output visibile e tangibile (es: primo documento creato, prima analisi generata)
- [ ] ✅ PASSA SE: dopo la prima azione viene mostrato un messaggio di congratulazioni/celebrazione
- [ ] ❌ FALLISCE SE: il primo accesso porta a una dashboard vuota senza guidance
- [ ] ❌ FALLISCE SE: il primo valore richiede più di 5-7 minuti senza un utente esperto

**Priority**: P0 — Il momento più critico del funnel
**Effort**: L
**Note**: Definire esattamente qual è il "First Value Moment" del prodotto PRIMA di progettare l'onboarding. Tutto il wizard deve puntare a quello.

---

#### 2.4 Tutorial Interattivo In-App

**Come** nuovo utente che ha completato il wizard,
**voglio** ricevere tooltip contestuali e guide interattive mentre esploro le feature principali,
**in modo da** imparare a usare il prodotto senza leggere documentazione esterna.

**Acceptance Criteria**:
- [ ] ✅ PASSA SE: i tooltip appaiono al momento giusto, non tutti insieme al primo accesso
- [ ] ✅ PASSA SE: ogni tooltip ha un pulsante "Capito" o "Salta tutto"
- [ ] ✅ PASSA SE: il progresso del tutorial è persistente (se si chiude, riprende dal punto giusto)
- [ ] ❌ FALLISCE SE: il tutorial non può essere saltato o disabilitato
- [ ] ❌ FALLISCE SE: i tooltip bloccano l'interazione con l'interfaccia

**Priority**: P1
**Effort**: M
**Note**: Usare librerie come Shepherd.js, Intro.js o Joyride. Non costruire da zero.

---

#### 2.5 Import Dati da Competitor

**Come** utente che viene da un tool concorrente,
**voglio** importare i miei dati esistenti (CSV, API, file export) nel nuovo prodotto,
**in modo da** non perdere il lavoro fatto finora e migrare senza attrito.

**Acceptance Criteria**:
- [ ] ✅ PASSA SE: viene fornito un template CSV di esempio da scaricare
- [ ] ✅ PASSA SE: l'import mostra anteprima dei dati prima di confermare
- [ ] ✅ PASSA SE: errori nel file CSV vengono segnalati riga per riga con descrizione chiara
- [ ] ✅ PASSA SE: l'import gira in background e notifica l'utente al completamento
- [ ] ❌ FALLISCE SE: un file con errori parziali viene importato parzialmente senza avviso
- [ ] ❌ FALLISCE SE: non esiste modo per annullare un import appena avviato

**Priority**: P1
**Effort**: L

---

#### 2.6 Invito Membri del Team

**Come** utente admin che ha completato il setup personale,
**voglio** invitare i membri del mio team via email durante l'onboarding,
**in modo da** iniziare a collaborare immediatamente senza dover aspettare che si registrino autonomamente.

**Acceptance Criteria**:
- [ ] ✅ PASSA SE: si possono inserire più email contemporaneamente (campo multiplo o paste da CSV)
- [ ] ✅ PASSA SE: gli invitati ricevono email con link di signup personalizzato entro 2 minuti
- [ ] ✅ PASSA SE: l'admin può impostare il ruolo degli invitati (Admin/Member/Viewer) prima dell'invio
- [ ] ✅ PASSA SE: i link di invito scadono dopo 7 giorni
- [ ] ❌ FALLISCE SE: non esiste modo per reinviare un invito o revocarlo

**Priority**: P1 — Critico per SaaS B2B team
**Effort**: M

---

#### 2.7 Setup Pagamenti e Billing

**Come** nuovo utente che vuole attivare il piano a pagamento,
**voglio** inserire i dati di pagamento e scegliere il piano durante l'onboarding,
**in modo da** sbloccare le feature premium senza interruzione del flusso iniziale.

**Acceptance Criteria**:
- [ ] ✅ PASSA SE: il checkout è embedded nell'onboarding (no redirect a pagina separata)
- [ ] ✅ PASSA SE: vengono mostrati chiaramente: prezzo, cosa include, quando verrà addebitato
- [ ] ✅ PASSA SE: l'utente può procedere su piano free e aggiornare dopo
- [ ] ❌ FALLISCE SE: il billing è obbligatorio prima di poter esplorare il prodotto (no forced paywall)
- [ ] ❌ FALLISCE SE: non viene inviata email di conferma dopo attivazione piano

**Priority**: P1
**Effort**: M
**Note**: Il forced paywall nel primo onboarding riduce la conversion del 30-50%. Mostrare sempre un'opzione free/trial.

---

#### 2.8 Completamento Setup con Progress Bar

**Come** nuovo utente che ha completato solo una parte del setup,
**voglio** vedere una checklist di completamento del profilo/workspace con percentuale,
**in modo da** sapere cosa manca per sfruttare il prodotto al massimo.

**Acceptance Criteria**:
- [ ] ✅ PASSA SE: la progress bar mostra la percentuale di completamento (es: "60% completato")
- [ ] ✅ PASSA SE: ogni item nella checklist è cliccabile e porta direttamente all'azione
- [ ] ✅ PASSA SE: al 100% viene mostrata una celebrazione/messaggio di benvenuto
- [ ] ✅ PASSA SE: la checklist scompare o si minimizza dopo il completamento
- [ ] ❌ FALLISCE SE: la progress bar non si aggiorna in tempo reale quando si completa un'azione

**Priority**: P1
**Effort**: S
**Note**: LinkedIn usa questo pattern con grande efficacia. Aumenta il completamento del profilo del 20-30%.

---

## CATEGORIA 3: Dashboard e Analytics

> **Epic**: Gli utenti hanno una visione chiara delle metriche più importanti e possono agire direttamente dalla dashboard.
> **Obiettivo business**: Aumentare retention e daily active usage.

---

#### 3.1 Vista KPI Principali

**Come** utente che accede alla dashboard,
**voglio** vedere i KPI più importanti per il mio business in un colpo d'occhio,
**in modo da** capire immediatamente lo stato del mio prodotto/account senza navigare tra più pagine.

**Acceptance Criteria**:
- [ ] ✅ PASSA SE: i KPI principali sono visibili above the fold (senza scroll)
- [ ] ✅ PASSA SE: ogni KPI mostra il valore attuale + variazione rispetto al periodo precedente (+/- %)
- [ ] ✅ PASSA SE: i dati si aggiornano automaticamente ogni 5 minuti o al refresh manuale
- [ ] ❌ FALLISCE SE: i dati mostrati nella dashboard non corrispondono ai dati reali del DB
- [ ] ❌ FALLISCE SE: non esiste indicatore di "dati aggiornati al [timestamp]"

**Priority**: P0
**Effort**: M

---

#### 3.2 Filtri per Date Range

**Come** utente analista che studia le performance nel tempo,
**voglio** filtrare tutte le metriche della dashboard per range di date personalizzato,
**in modo da** confrontare periodi specifici (es: questo mese vs mese scorso).

**Acceptance Criteria**:
- [ ] ✅ PASSA SE: esistono opzioni rapide: Oggi, Ieri, Ultimi 7 giorni, Ultimi 30 giorni, Questo mese, Range custom
- [ ] ✅ PASSA SE: il range selezionato persiste durante la navigazione nella dashboard
- [ ] ✅ PASSA SE: tutte le metriche e grafici si aggiornano simultaneamente al cambio del filtro
- [ ] ❌ FALLISCE SE: il filtro data viene resettato al refresh della pagina
- [ ] ❌ FALLISCE SE: le date nel date picker sono in formato ambiguo (MM/DD vs DD/MM)

**Priority**: P1
**Effort**: M

---

#### 3.3 Export CSV / PDF

**Come** utente che deve riportare dati a stakeholder o importarli in altri tool,
**voglio** esportare i dati della dashboard in formato CSV o PDF,
**in modo da** condividere le informazioni con chi non ha accesso al prodotto.

**Acceptance Criteria**:
- [ ] ✅ PASSA SE: il CSV include tutte le colonne visibili nella vista attuale
- [ ] ✅ PASSA SE: il PDF include grafici renderizzati, non solo tabelle di dati
- [ ] ✅ PASSA SE: l'export rispetta i filtri data attivi al momento dell'esportazione
- [ ] ✅ PASSA SE: file grandi vengono generati in background con notifica al completamento
- [ ] ❌ FALLISCE SE: il CSV ha encoding errato (problemi con caratteri speciali/accentati)

**Priority**: P1
**Effort**: S

---

#### 3.4 Grafici Interattivi

**Come** utente che analizza trend nel tempo,
**voglio** interagire con i grafici (hover per dettaglio, click per drill-down),
**in modo da** capire le cause dei picchi e delle anomalie nelle metriche.

**Acceptance Criteria**:
- [ ] ✅ PASSA SE: hover su un punto del grafico mostra tooltip con valore esatto e data
- [ ] ✅ PASSA SE: i grafici sono responsive (funzionano su mobile e tablet)
- [ ] ✅ PASSA SE: il tipo di grafico è appropriato al dato (linea per trend, barre per confronti)
- [ ] ❌ FALLISCE SE: i grafici non si caricano su browser Safari o Firefox (solo Chrome)
- [ ] ❌ FALLISCE SE: dataset grandi causano freeze del browser

**Priority**: P1
**Effort**: M
**Note**: Usare Recharts, Chart.js o Nivo — non costruire grafici da zero.

---

#### 3.5 Notifiche e Alert

**Come** utente che monitora metriche critiche,
**voglio** ricevere una notifica quando una metrica supera una soglia che ho impostato,
**in modo da** reagire prontamente a cambiamenti importanti senza dover controllare manualmente.

**Acceptance Criteria**:
- [ ] ✅ PASSA SE: si può configurare un alert su qualsiasi metrica chiave con soglia personalizzata
- [ ] ✅ PASSA SE: gli alert arrivano via notifica in-app e opzionalmente via email
- [ ] ✅ PASSA SE: esiste una pagina "Storico Alert" con tutti gli alert scattati
- [ ] ❌ FALLISCE SE: gli alert continuano ad arrivare ripetutamente per lo stesso evento (no debouncing)

**Priority**: P1
**Effort**: M

---

#### 3.6 Ricerca Globale

**Come** utente con molta storia nel prodotto,
**voglio** cercare qualsiasi entità (progetto, cliente, documento) tramite barra di ricerca globale,
**in modo da** trovare quello che cerco in meno di 5 secondi senza navigare manualmente.

**Acceptance Criteria**:
- [ ] ✅ PASSA SE: shortcut keyboard (CMD+K / CTRL+K) apre la ricerca globale ovunque nel prodotto
- [ ] ✅ PASSA SE: i risultati appaiono mentre si digita (debounce 200ms)
- [ ] ✅ PASSA SE: i risultati sono categorizzati per tipo (Progetti, Clienti, Documenti, etc.)
- [ ] ❌ FALLISCE SE: la ricerca impiega più di 500ms a mostrare i primi risultati
- [ ] ❌ FALLISCE SE: la ricerca non funziona con typo minori o varianti ortografiche

**Priority**: P1
**Effort**: M

---

#### 3.7 Customizzazione Widget Dashboard

**Come** utente avanzato con necessità specifiche,
**voglio** personalizzare quali widget/KPI compaiono nella mia dashboard e in quale ordine,
**in modo da** vedere immediatamente le metriche più rilevanti per il mio ruolo.

**Acceptance Criteria**:
- [ ] ✅ PASSA SE: i widget sono riordinabili tramite drag-and-drop
- [ ] ✅ PASSA SE: ogni widget può essere nascosto/mostrato da un pannello di configurazione
- [ ] ✅ PASSA SE: le preferenze di layout sono salvate per utente (non per sessione)
- [ ] ❌ FALLISCE SE: non esiste opzione "Ripristina layout default"

**Priority**: P2
**Effort**: L

---

#### 3.8 Report Periodico via Email

**Come** utente manager che vuole monitorare le performance senza accedere ogni giorno,
**voglio** ricevere un report settimanale o mensile con i KPI principali via email,
**in modo da** rimanere aggiornato sullo stato del prodotto senza effort manuale.

**Acceptance Criteria**:
- [ ] ✅ PASSA SE: l'utente può scegliere frequenza (giornaliero/settimanale/mensile) e orario di invio
- [ ] ✅ PASSA SE: l'email contiene i KPI chiave con confronto periodo precedente
- [ ] ✅ PASSA SE: il report può essere disabilitato in un click da qualsiasi email inviata
- [ ] ❌ FALLISCE SE: il report non si può personalizzare per contenuto (tutti ricevono lo stesso)

**Priority**: P2
**Effort**: M

---

## CATEGORIA 4: Billing e Pagamenti

> **Epic**: Gli utenti possono gestire il loro abbonamento in autonomia completa senza contattare il supporto.
> **Obiettivo business**: Ridurre churn e massimizzare lifetime value.

---

#### 4.1 Upgrade Piano

**Come** utente su piano free o tier inferiore,
**voglio** passare a un piano superiore dalle impostazioni del mio account,
**in modo da** sbloccare le feature di cui ho bisogno senza aspettare l'approvazione di nessuno.

**Acceptance Criteria**:
- [ ] ✅ PASSA SE: la pagina di upgrade mostra chiaramente cosa si sblocca con ogni piano
- [ ] ✅ PASSA SE: il cambio piano è immediato senza interruzione del servizio
- [ ] ✅ PASSA SE: viene addebitato solo il pro-rata per i giorni rimanenti del ciclo attuale
- [ ] ✅ PASSA SE: viene inviata email di conferma con ricevuta
- [ ] ❌ FALLISCE SE: l'utente viene rediretto fuori dal prodotto per completare l'upgrade

**Priority**: P0
**Effort**: M

---

#### 4.2 Downgrade Piano

**Come** utente su piano premium che vuole ridurre i costi,
**voglio** passare a un piano inferiore o free senza perdere i dati esistenti,
**in modo da** ridurre la spesa mantenendo accesso ai miei dati storici.

**Acceptance Criteria**:
- [ ] ✅ PASSA SE: prima del downgrade viene mostrato esattamente cosa si perderà
- [ ] ✅ PASSA SE: il downgrade è effettivo alla fine del ciclo di billing corrente (no rimborso immediato)
- [ ] ✅ PASSA SE: i dati creati con il piano premium rimangono accessibili in sola lettura dopo il downgrade
- [ ] ❌ FALLISCE SE: il downgrade elimina dati senza avviso esplicito
- [ ] ❌ FALLISCE SE: non esiste modo per annullare il downgrade prima che sia effettivo

**Priority**: P0
**Effort**: M

---

#### 4.3 Gestione Carta di Credito

**Come** utente con abbonamento attivo,
**voglio** aggiornare o cambiare la carta di credito associata al mio account,
**in modo da** evitare interruzioni del servizio quando la carta scade o viene sostituita.

**Acceptance Criteria**:
- [ ] ✅ PASSA SE: il form di inserimento carta usa Stripe Elements (sicuro, PCI compliant)
- [ ] ✅ PASSA SE: la nuova carta viene verificata con un addebito di €0 o €1 (con rimborso)
- [ ] ✅ PASSA SE: viene notificato via email quando una carta sta per scadere (30 e 7 giorni prima)
- [ ] ❌ FALLISCE SE: i dati della carta vengono mostrati o loggati in chiaro
- [ ] ❌ FALLISCE SE: non è possibile avere più carte salvate (una attiva + una backup)

**Priority**: P0
**Effort**: M

---

#### 4.4 Cancellazione Abbonamento

**Come** utente che vuole disdire il servizio,
**voglio** cancellare il mio abbonamento in autonomia dalle impostazioni,
**in modo da** non continuare a pagare senza dover contattare il supporto (dark pattern illegale in EU).

**Acceptance Criteria**:
- [ ] ✅ PASSA SE: il percorso di cancellazione è raggiungibile in meno di 3 click
- [ ] ✅ PASSA SE: prima della cancellazione viene mostrata un'offerta di retention (pausa, sconto)
- [ ] ✅ PASSA SE: viene chiesto il motivo della cancellazione (survey 1 domanda)
- [ ] ✅ PASSA SE: la cancellazione è effettiva alla fine del ciclo, con accesso garantito fino ad allora
- [ ] ❌ FALLISCE SE: la cancellazione richiede di contattare il supporto (illegale in EU dal 2023)
- [ ] ❌ FALLISCE SE: i dati vengono eliminati immediatamente alla cancellazione (no grace period)

**Priority**: P0 — Requisito legale EU
**Effort**: M

---

#### 4.5 Reattivazione Abbonamento

**Come** ex utente che ha cancellato l'abbonamento e vuole tornare,
**voglio** riattivare il mio account con un click durante il grace period,
**in modo da** riprendere da dove avevo lasciato senza perdere i miei dati.

**Acceptance Criteria**:
- [ ] ✅ PASSA SE: durante il grace period (30 giorni dopo cancellazione) esiste un pulsante "Riattiva"
- [ ] ✅ PASSA SE: la riattivazione usa la carta di credito già salvata (no re-inserimento)
- [ ] ✅ PASSA SE: tutti i dati precedenti sono ripristinati immediatamente
- [ ] ❌ FALLISCE SE: la riattivazione richiede di reinserire i dati di pagamento senza motivo

**Priority**: P1
**Effort**: S

---

#### 4.6 Download Fatture

**Come** utente o responsabile contabilità,
**voglio** scaricare le fatture di tutti i pagamenti effettuati in formato PDF,
**in modo da** riconciliarle con la contabilità aziendale o richiederle per il rimborso spese.

**Acceptance Criteria**:
- [ ] ✅ PASSA SE: tutte le fatture sono elencate con data, importo e numero fattura
- [ ] ✅ PASSA SE: ogni fattura è scaricabile singolarmente in PDF con logo e dati fiscali corretti
- [ ] ✅ PASSA SE: si possono scaricare tutte le fatture di un anno in un unico ZIP
- [ ] ❌ FALLISCE SE: le fatture non includono il numero IVA dell'azienda (obbligatorio per rimborso B2B)

**Priority**: P0 — Requisito legale e contabile
**Effort**: S

---

#### 4.7 Coupon / Promo Code

**Come** utente che ha ricevuto un codice promozionale,
**voglio** inserire il codice durante il checkout o nelle impostazioni per ottenere uno sconto,
**in modo da** beneficiare dell'offerta che mi è stata comunicata.

**Acceptance Criteria**:
- [ ] ✅ PASSA SE: il campo coupon è presente sia nel checkout iniziale che nelle impostazioni
- [ ] ✅ PASSA SE: il codice viene validato in tempo reale mostrando lo sconto applicato prima della conferma
- [ ] ✅ PASSA SE: codici scaduti o già usati mostrano messaggio di errore chiaro
- [ ] ❌ FALLISCE SE: il coupon viene applicato senza mostrare il nuovo prezzo finale

**Priority**: P1
**Effort**: S

---

#### 4.8 Conversione Trial → Paid

**Come** utente in periodo di trial che sta per scadere,
**voglio** ricevere promemoria chiari sulla scadenza del trial e un percorso semplice per convertire,
**in modo da** non perdere l'accesso al prodotto e ai dati che ho creato durante il trial.

**Acceptance Criteria**:
- [ ] ✅ PASSA SE: banner in-app visibile negli ultimi 7 giorni di trial con countdown giorni
- [ ] ✅ PASSA SE: email di promemoria: 7 giorni prima, 3 giorni prima, 1 giorno prima
- [ ] ✅ PASSA SE: al termine del trial, i dati vengono preservati per 14 giorni in attesa di conversione
- [ ] ✅ PASSA SE: l'utente può convertire con un click senza re-inserire informazioni già date
- [ ] ❌ FALLISCE SE: i dati del trial vengono eliminati immediatamente alla scadenza

**Priority**: P0 — Core della monetizzazione
**Effort**: M

---

## CATEGORIA 5: Notifiche

> **Epic**: Gli utenti vengono informati tempestivamente degli eventi rilevanti nel modo e nel momento giusto.
> **Obiettivo business**: Aumentare engagement e ridurre la necessità di polling manuale.

---

#### 5.1 Notifica In-App Real-Time

**Come** utente attivo nel prodotto,
**voglio** ricevere notifiche in-app immediatamente quando accade qualcosa di rilevante,
**in modo da** reagire prontamente senza dover uscire e rientrare nel prodotto.

**Acceptance Criteria**:
- [ ] ✅ PASSA SE: le notifiche appaiono come toast/snackbar in meno di 2 secondi dall'evento
- [ ] ✅ PASSA SE: il badge sul campanellino si aggiorna in tempo reale (senza refresh)
- [ ] ✅ PASSA SE: cliccando la notifica si viene portati direttamente alla risorsa rilevante
- [ ] ❌ FALLISCE SE: le notifiche appaiono anche durante attività che richiedono focus (es: editing)

**Priority**: P1
**Effort**: M

---

#### 5.2 Email Notification Opt-In / Opt-Out

**Come** utente che gestisce le proprie preferenze di comunicazione,
**voglio** scegliere quali tipi di email ricevere e quali no,
**in modo da** ricevere solo comunicazioni che trovo utili senza essere sommerso di email.

**Acceptance Criteria**:
- [ ] ✅ PASSA SE: esiste pagina "Preferenze Notifiche" con lista di tutti i tipi di email
- [ ] ✅ PASSA SE: ogni tipo di email ha toggle on/off indipendente
- [ ] ✅ PASSA SE: ogni email marketing include link "Unsubscribe" in fondo (obbligo legale)
- [ ] ❌ FALLISCE SE: disabilitare tutte le email impedisce di ricevere email transazionali (reset password, fatture)

**Priority**: P1 — Obbligo legale (GDPR + CAN-SPAM)
**Effort**: M

---

#### 5.3 Centro Notifiche

**Come** utente che ha perso delle notifiche,
**voglio** accedere a uno storico di tutte le notifiche ricevute,
**in modo da** recuperare informazioni importanti che potrebbero essere passate inosservate.

**Acceptance Criteria**:
- [ ] ✅ PASSA SE: il pannello notifiche mostra gli ultimi 100 eventi con data e ora
- [ ] ✅ PASSA SE: le notifiche non lette sono visivamente distinte da quelle già lette
- [ ] ✅ PASSA SE: esiste pulsante "Segna tutto come letto"
- [ ] ❌ FALLISCE SE: lo storico notifiche non va oltre i 7 giorni (deve essere almeno 30)

**Priority**: P1
**Effort**: S

---

#### 5.4 Notifica Push Mobile

**Come** utente mobile che ha installato l'app,
**voglio** ricevere notifiche push anche quando non sto usando l'app attivamente,
**in modo da** essere informato di eventi urgenti ovunque mi trovi.

**Acceptance Criteria**:
- [ ] ✅ PASSA SE: la prima apertura dell'app chiede il permesso per le notifiche push
- [ ] ✅ PASSA SE: le notifiche push portano alla schermata giusta all'apertura
- [ ] ✅ PASSA SE: si può disabilitare ogni tipo di notifica push dalle impostazioni app
- [ ] ❌ FALLISCE SE: vengono inviate notifiche push per eventi non critici (spam di notifiche)

**Priority**: P1 — Solo per prodotti con app mobile
**Effort**: M

---

#### 5.5 Digest Settimanale

**Come** utente manager che non accede ogni giorno,
**voglio** ricevere un riepilogo settimanale via email di tutto ciò che è successo nel mio workspace,
**in modo da** rimanere informato senza dover accedere al prodotto ogni giorno.

**Acceptance Criteria**:
- [ ] ✅ PASSA SE: il digest arriva ogni lunedì mattina con il riepilogo della settimana precedente
- [ ] ✅ PASSA SE: il contenuto è personalizzato per ruolo (admin vede tutto, member vede solo il suo)
- [ ] ✅ PASSA SE: il digest può essere disabilitato dalle preferenze notifiche
- [ ] ❌ FALLISCE SE: il digest arriva anche a utenti che si sono loggati ogni giorno (per loro è rumore)

**Priority**: P2
**Effort**: M

---

#### 5.6 @Mention Notification

**Come** utente in un contesto collaborativo,
**voglio** ricevere una notifica quando qualcuno mi menziona con @nome in un commento o documento,
**in modo da** rispondere prontamente alle richieste dirette dei miei colleghi.

**Acceptance Criteria**:
- [ ] ✅ PASSA SE: la notifica arriva sia in-app che via email entro 30 secondi dalla mention
- [ ] ✅ PASSA SE: la notifica include il contesto (chi, dove, cosa ha scritto)
- [ ] ✅ PASSA SE: cliccando la notifica si arriva direttamente al commento con il focus sul reply
- [ ] ❌ FALLISCE SE: le mention funzionano solo in alcuni contesti (devono essere universali)

**Priority**: P1 — Solo per prodotti con feature collaborative
**Effort**: M

---

## CATEGORIA 6: Team e Collaborazione

> **Epic**: I team possono lavorare insieme in modo strutturato con ruoli, permessi e audit trail.
> **Obiettivo business**: Espandere il contratto (più seat) e aumentare lo switching cost.

---

#### 6.1 Invito Membro Team

**Come** admin del workspace,
**voglio** invitare nuove persone a unirsi al team via email,
**in modo da** espandere l'accesso al prodotto ai colleghi senza che creino account separati.

**Acceptance Criteria**:
- [ ] ✅ PASSA SE: l'invito specifica il ruolo che avrà il nuovo membro
- [ ] ✅ PASSA SE: il link di invito funziona per registrarsi direttamente senza passare dalla homepage
- [ ] ✅ PASSA SE: l'admin riceve notifica quando qualcuno accetta l'invito
- [ ] ❌ FALLISCE SE: si possono inviare inviti illimitati su un piano con limite di seat

**Priority**: P0 — Core per SaaS B2B team
**Effort**: M

---

#### 6.2 Ruoli e Permessi (Owner / Admin / Member / Viewer)

**Come** admin che gestisce un team con diversi livelli di accesso,
**voglio** assegnare ruoli granulari a ogni membro del team,
**in modo da** garantire che ognuno abbia accesso solo a ciò che gli serve per il suo ruolo.

**Acceptance Criteria**:
- [ ] ✅ PASSA SE: esiste almeno 4 livelli: Owner (tutto), Admin (gestione team), Member (uso), Viewer (sola lettura)
- [ ] ✅ PASSA SE: la matrice permessi è documentata e visibile agli admin
- [ ] ✅ PASSA SE: l'Owner non può essere rimosso o degradato da un Admin
- [ ] ❌ FALLISCE SE: i permessi non vengono verificati lato server (solo lato client — security issue critico)

**Priority**: P0 — Requisito essenziale SaaS B2B
**Effort**: L
**Note**: Implementare RBAC (Role-Based Access Control) lato server. Non fidarsi mai del ruolo inviato dal client.

---

#### 6.3 Rimozione Membro

**Come** admin del workspace,
**voglio** rimuovere un membro dal team quando lascia l'azienda o il progetto,
**in modo da** revocare immediatamente l'accesso ai dati aziendali.

**Acceptance Criteria**:
- [ ] ✅ PASSA SE: la rimozione invalida immediatamente tutte le sessioni attive del membro
- [ ] ✅ PASSA SE: prima della rimozione viene mostrato cosa succederà ai dati di quel membro
- [ ] ✅ PASSA SE: l'admin può scegliere se trasferire i contenuti del membro a qualcun altro
- [ ] ❌ FALLISCE SE: il membro rimosso può ancora accedere al prodotto se aveva una sessione aperta

**Priority**: P0 — Requisito di sicurezza
**Effort**: M

---

#### 6.4 Transfer Ownership

**Come** Owner del workspace che lascia l'azienda o cede il prodotto,
**voglio** trasferire la proprietà del workspace a un altro membro,
**in modo da** garantire continuità operativa senza perdere accesso al prodotto.

**Acceptance Criteria**:
- [ ] ✅ PASSA SE: solo l'Owner attuale può trasferire la proprietà
- [ ] ✅ PASSA SE: il nuovo Owner deve accettare esplicitamente il trasferimento
- [ ] ✅ PASSA SE: il vecchio Owner diventa automaticamente Admin dopo il trasferimento
- [ ] ❌ FALLISCE SE: il trasferimento è immediato senza conferma da parte del ricevente

**Priority**: P1
**Effort**: S

---

#### 6.5 Activity Log Team

**Come** admin che monitora le azioni del team,
**voglio** vedere un log cronologico di tutte le azioni significative compiute dai membri,
**in modo da** garantire accountability e investigare eventuali problemi.

**Acceptance Criteria**:
- [ ] ✅ PASSA SE: il log registra: chi, cosa, quando, su quale risorsa
- [ ] ✅ PASSA SE: il log è filtrabile per utente, tipo di azione, range di date
- [ ] ✅ PASSA SE: il log è esportabile in CSV
- [ ] ❌ FALLISCE SE: le azioni degli Owner e Admin non vengono loggate (devono esserlo)
- [ ] ❌ FALLISCE SE: il log può essere eliminato da chiunque (deve essere append-only)

**Priority**: P1 — P0 per SaaS enterprise
**Effort**: M

---

#### 6.6 Commenti su Entità Condivise

**Come** membro del team che collabora su una risorsa condivisa,
**voglio** lasciare commenti contestuali su documenti, progetti o altri oggetti condivisi,
**in modo da** comunicare feedback e decisioni direttamente dove è rilevante senza usare chat esterne.

**Acceptance Criteria**:
- [ ] ✅ PASSA SE: i commenti supportano testo ricco, @mention e link
- [ ] ✅ PASSA SE: i commenti possono essere risolti (collapsed dopo risoluzione, non eliminati)
- [ ] ✅ PASSA SE: tutti i membri con accesso alla risorsa ricevono notifica per nuovi commenti
- [ ] ❌ FALLISCE SE: i commenti eliminati scompaiono senza traccia (devono essere preservati nel log)

**Priority**: P1
**Effort**: M

---

## CATEGORIA 7: Integrazioni

> **Epic**: Gli utenti possono connettere il prodotto ai tool che già usano nel loro workflow.
> **Obiettivo business**: Aumentare switching cost e rendere il prodotto sticky nell'ecosystem dell'utente.

---

#### 7.1 Connessione via OAuth (es: Slack, Google Workspace)

**Come** utente che usa Slack e Google nel lavoro quotidiano,
**voglio** connettere il prodotto al mio Slack e Google Workspace tramite OAuth,
**in modo da** ricevere notifiche in Slack e accedere a file Google Drive direttamente nel prodotto.

**Acceptance Criteria**:
- [ ] ✅ PASSA SE: il flow OAuth si completa in meno di 3 click
- [ ] ✅ PASSA SE: vengono richiesti solo i permessi strettamente necessari (principio di least privilege)
- [ ] ✅ PASSA SE: la connessione è testabile con un pulsante "Test connessione"
- [ ] ❌ FALLISCE SE: il token OAuth non viene refreshato automaticamente alla scadenza
- [ ] ❌ FALLISCE SE: revocare il permesso da Slack/Google non disconnette automaticamente l'integrazione

**Priority**: P1 — Dipende dal prodotto
**Effort**: M

---

#### 7.2 Webhook Outbound

**Come** developer o power user che vuole automatizzare workflow,
**voglio** configurare webhook che inviano dati a URL esterni quando accadono eventi specifici,
**in modo da** integrare il prodotto con qualsiasi tool esterno (Zapier, n8n, sistemi custom).

**Acceptance Criteria**:
- [ ] ✅ PASSA SE: si possono creare webhook per almeno 5 eventi principali del prodotto
- [ ] ✅ PASSA SE: il payload del webhook è documentato con esempi
- [ ] ✅ PASSA SE: esiste log di delivery (successi, errori, retry automatici)
- [ ] ✅ PASSA SE: i webhook falliti vengono ritentati con exponential backoff (3 tentativi)
- [ ] ❌ FALLISCE SE: non esiste modo per testare un webhook prima di pubblicarlo in produzione

**Priority**: P1 — P0 per prodotti API-first
**Effort**: M

---

#### 7.3 API Key Management

**Come** developer che vuole integrare il prodotto via API,
**voglio** generare e gestire API key per l'accesso programmatico al mio account,
**in modo da** costruire automazioni e integrazioni custom senza usare le mie credenziali personali.

**Acceptance Criteria**:
- [ ] ✅ PASSA SE: si possono creare API key con scope limitati (es: read-only, write, admin)
- [ ] ✅ PASSA SE: la chiave viene mostrata una sola volta alla creazione (poi hashata nel DB)
- [ ] ✅ PASSA SE: ogni API key ha un nome/descrizione per identificarne l'uso
- [ ] ✅ PASSA SE: si può revocare una chiave immediatamente senza impattare le altre
- [ ] ❌ FALLISCE SE: le API key vengono salvate in chiaro nel database

**Priority**: P1 — P0 per prodotti con API pubblica
**Effort**: M

---

#### 7.4 Disconnect Integration

**Come** utente che ha connesso un'integrazione e vuole rimuoverla,
**voglio** disconnettere un'integrazione esterna in un click,
**in modo da** revocare l'accesso del prodotto ai miei dati esterni quando non mi serve più.

**Acceptance Criteria**:
- [ ] ✅ PASSA SE: il pulsante "Disconnetti" è visibile accanto a ogni integrazione attiva
- [ ] ✅ PASSA SE: la disconnessione mostra un warning su cosa smetterà di funzionare
- [ ] ✅ PASSA SE: dopo la disconnessione il token OAuth viene revocato anche lato provider esterno (se supportato)
- [ ] ❌ FALLISCE SE: non è possibile riconnettere un'integrazione dopo averla disconnessa

**Priority**: P1
**Effort**: S

---

## Epic Template

> Usa questo template per raggruppare le user stories in Epic con obiettivo chiaro.

```markdown
## Epic: [Nome Epic]

**Obiettivo**: [Una frase che descrive il valore business dell'epic]
**KPI di successo**: [Come misuri che l'epic ha raggiunto l'obiettivo]
**Timeline stimata**: [X settimane]
**Owner**: [Ruolo responsabile]

### Stories incluse

| ID | Titolo Story | Priority | Effort | Status |
|---|---|---|---|---|
| 1.1 | [Titolo] | P0 | M | TODO |
| 1.2 | [Titolo] | P1 | S | TODO |
| 1.3 | [Titolo] | P2 | L | TODO |

### Criteri di completamento Epic

L'Epic è completata quando:
- [ ] Tutte le stories P0 sono in produzione
- [ ] [KPI specifico] ha raggiunto [valore target]
- [ ] [Test critico] passa in staging

### Dipendenze

- Dipende da: [Epic o story che deve essere completata prima]
- Richiesta da: [Epic o story che dipende da questa]
```

---

## Come Usare Questa Libreria

### 1. Seleziona le storie rilevanti per il tuo prodotto

Non tutte le storie si applicano a ogni prodotto. Filtra per categoria in base a cosa stai costruendo:
- Prodotto B2C solo app mobile → Categorie 1, 2, 3, 5, 7.1
- SaaS B2B team → Tutte le categorie
- Tool solo → Categorie 1, 2, 3, 4 (billing), 7.3 (API key)

### 2. Adatta il tipo utente al tuo prodotto

Sostituisci il tipo utente generico con quello specifico del tuo prodotto:
- "utente" → "freelancer che gestisce 5+ clienti"
- "admin del workspace" → "responsabile marketing di una PMI"
- "developer" → "CTO di una startup SaaS early stage"

### 3. Contestualizza i benefici

Il beneficio (in modo da...) deve essere specifico al value proposition del tuo prodotto:
- ❌ generico: "in modo da usare il prodotto"
- ✅ specifico: "in modo da ridurre i tempi di reporting mensile da 4 ore a 20 minuti"

### 4. Aggiorna le Acceptance Criteria con metriche reali

Le soglie generiche vanno sostituite con quelle del tuo prodotto:
- "entro X secondi" → definisci X in base al tuo SLA
- "max Y tentativi" → definisci Y in base alla tua policy di sicurezza

### 5. Assegna priorità in base al tuo MVP scope

In un MVP tipico:
- **Includi nel lancio**: tutte le P0 + le P1 core della proposta di valore
- **Post-lancio v1.1**: P1 secondarie
- **Roadmap v2.0**: tutte le P2

### 6. Raggruppa le storie in Epic

Usa l'Epic Template per raggruppare le storie per area funzionale prima di portarle in sprint.

---

*Documento aggiornato: 2026-05-01 | Versione: 1.0 | Parte di PRD Architect OS*
