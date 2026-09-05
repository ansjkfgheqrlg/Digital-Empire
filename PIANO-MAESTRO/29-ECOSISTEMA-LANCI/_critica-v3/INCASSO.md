# INCASSO — l'infrastruttura commerciale reale di Digital Empire

Metodo: ricerca su disco (grep + lettura file), nessuna chiamata a API esterne (Brevo/Stripe non
interrogati per non esporre credenziali e non alterare stato). Percorsi assoluti dalla radice
`C:\Users\Utente\Desktop\qui tutto\Digital Empire\`. Nessun file del repository è stato modificato.

---

## 1. PAGAMENTI

**Verdetto: NON ESISTE un modo automatico di incassare online. Esiste solo un fallback manuale
via email, più una infrastruttura Stripe reale ma per un prodotto diverso, mai collegata a un
bottone d'acquisto.**

### Il prodotto pilota (Manuale Claude Code) — SOLO PROGETTATO
- `Crea siti\Siti CCM\checkout.config.json` (righe 7-33): tutti i rail di pagamento —
  `stripe_base`, `stripe_bump`, `paypal_me`, `bonifico` — hanno `"attivo": false` e `"url"`/`"iban"`
  vuoti. L'unico rail con `"attivo": true` è `ordine_email` (riga 29-32): un indirizzo Gmail di Max.
- `empire\tools\checkout.py` (tutto il file, 375 righe): script reale e ben scritto che gestisce
  una "ladder" di pagamento a partire da `checkout.config.json`. Dichiara esplicitamente (righe
  13-21): Tier 1 = Stripe live (non raggiunto), Tier 2 = fallback mailto (quello attivo oggi),
  "non esiste un tier 3: un funnel senza modo di pagare non è un funnel" (riga 241).
- `Crea siti\Siti CCM\CHECKOUT-STATO.md` (generato l'ultima volta il 2026-07-24 da `checkout.py
  --apply`): "Tier attivo: 2 -- fallback ordine attivo (mailto verso ordine_email)". Tutti i 4 rail
  di pagamento reale segnati "NO".
- Verificato sul file vivo: `Crea siti\Siti CCM\manuale.html` righe 310, 338-339 — il bottone
  d'acquisto (`id="checkout-btn"`) punta a `pagamento.html`, non a un link Stripe.
- `Crea siti\Siti CCM\pagamento.html` righe 190, 197, 375: il "checkout" è un link
  `mailto:max.infoproducer@gmail.com?subject=Ordine%20Manuale%20Claude%20Code` — il cliente scrive
  una email, Max chiude l'ordine a mano.
- Nessun placeholder `YOUR_STRIPE_*` residuo in `manuale.html` oggi (rimosso dall'ultimo `--apply`),
  ma questo significa solo che il link è stato sostituito col fallback mailto, non con un vero
  Payment Link.
- Conferma indipendente in `company\Memory\STATO-EMPIRE.md`: righe 4734-4737 (2026-07-23), 5828-5832
  e 8030-8032 (fine luglio), 6948-6949 — tutte ripetono che "Max crea i 2 Payment Link Stripe reali"
  non è mai stato fatto; riga 8043-8045: "Landing non ancora deployata su un dominio reale... nessun
  vercel.json/netlify.toml/CNAME trovato nella cartella" (2026-07-22, confermato anche oggi da me
  con `find` diretto sulla cartella: nessuno di questi file esiste).
- La finestra di lancio dichiarata in `checkout.config.json` riga 6 (`"scadenza_lancio":
  "2026-07-31"`) è scaduta da oltre un mese rispetto a oggi (2026-09-05), senza che il Tier 1 sia
  mai stato raggiunto.

### Un prodotto diverso (ebook KDP "Le 48 Leggi dei Maestri Dimenticati") — ESISTE MA NON PROVATO
- `KDP - prodottti digitali\Leanding Page\email-agent\main.py` (81 righe): webhook FastAPI reale
  (`POST /webhook`, riga 53) che verifica la firma Stripe (`stripe.Webhook.construct_event`, riga
  59), e su `checkout.session.completed` invia l'ebook via Gmail SMTP (`send_ebook`, riga 22).
  Codice funzionante, non un mock.
- `KDP - prodottti digitali\Leanding Page\email-agent\.env`: variabili presenti e valorizzate
  (valori NON riportati per regola) — `STRIPE_SECRET_KEY` (108 caratteri, prefisso confermato
  `sk_live_...`: è una chiave Stripe **live**, non di test), `STRIPE_WEBHOOK_SECRET` (39 caratteri),
  `GMAIL_ADDRESS` (27), `GMAIL_APP_PASSWORD` (20), `EBOOK_DOWNLOAD_URL` (86).
- **Ma**: nessun bottone d'acquisto, Payment Link o riferimento a Stripe/checkout trovato nelle 6
  landing page del prodotto (`KDP - prodottti digitali\Leanding Page\Il Codice dei Potenti\*\index.html`
  — grep su "stripe|checkout|payment" = 0 risultati). Il webhook è pronto a ricevere un evento che,
  per quanto trovato, nessuna pagina del sito genera. Nessun file di deploy (`Procfile` c'è, ma
  nessun `railway.json`/project id) conferma che il servizio sia davvero online su Railway oggi.
- Il libro stesso non risulta mai pubblicato: `company\Memory\STATO-EMPIRE.md` righe 197, 791
  ("`libri_pubblicati/` resta vuoto, **0 ASIN**") — nessun libro KDP dell'azienda, incluso questo,
  è mai arrivato in vendita reale su Amazon.

### Il conto dei fatti (tesoreria interna)
- `company\Memory\tesoreria\entrate.jsonl`: **0 righe** (verificato con `wc -l`).
- `company\Memory\tesoreria\spese.jsonl`: **0 righe**.
- `company\Memory\STATO-EMPIRE.md` righe 9007-9010 (B-043, 2026-09-03, la nota più recente
  sull'argomento in tutta la Memory): *"Digital Empire non misura un solo euro: né ricavi, né
  costi effettivi, né una metrica del percorso di vendita."*

### Non trovato
- Nessuna traccia di account/integrazione reale per gumroad, lemonsqueezy, payhip, sumup,
  satispay, thrivecart, hotmart, kajabi, teachable, podia, systeme.io, woocommerce. "Shopify" e
  simili compaiono solo dentro `Agency page\Clienti\marketingskills-main\` — una libreria di skill
  di terze parti clonata nel repo (materiale di riferimento generico, non uso reale di Digital Empire).

---

## 2. LISTA CONTATTI

**Verdetto: ESISTE un meccanismo di raccolta funzionante (Brevo), ma non è dato sapere quante
persone contenga, ed è esposto pubblicamente da mesi senza essere ruotato.**

- `Landing Page\ccm-empire\src\app\page.tsx` righe 32-34: chiave API Brevo **hardcoded lato
  client** (valore NON riportato) + `LIST_ID = 3`. Componente `BrevoForm` (riga 36) fa `fetch`
  reale a `https://api.brevo.com/v3/contacts` (riga 63) al submit di un form nome+email agganciato
  al bottone "SCARICA IL PDF GRATUITO" (righe 548-551). Questo è codice funzionante, non un mock.
- La stessa chiave è duplicata in almeno 3 altri file (`Crea siti\Siti CCM\index.html`,
  `Lancio corso skill beast\Leanding Page CCM\index.html`,
  `.../icro-empire/src/components/optin-form.tsx`) — vedi `company\Memory\BACKLOG.md` riga 42
  (voce **B-020**, stato **⬜ non chiuso**): la chiave è in chiaro su un repo GitHub confermato
  **pubblico** dal commit iniziale, mai revocata né rigenerata su Brevo.
- **Nessun numero reale trovato da nessuna parte**: cercato esplicitamente "iscritti alla
  lista/newsletter", "lista email...dimensione", "subscriber count" in tutto il repo. Gli unici
  riscontri sono campi-modello vuoti da compilare in workflow generici, es.
  `company\Ecosistemi\04-MARKETING\Workflow\WF-EMAIL-LAUNCH.md` riga 9 ("Lista email disponibile:
  dimensione, attributi...") e `company\Ecosistemi\04-MARKETING\Agenti\E3-segmentation-analyst.md`
  riga 16 — sono template di skill, non dati reali dell'azienda.
- Nessun account Mailchimp/ConvertKit/ActiveCampaign/MailerLite/Klaviyo trovato in uso reale;
  compaiono solo negli stessi file di skill di terze parti citati sopra (`marketingskills-main`).
- I numeri "iscritti" trovati nel resto della Memory sono **iscritti YouTube** (es. "14.793
  iscritti" su Legami d'Amore, "198k" su Dose Mentale — `STATO-EMPIRE.md` righe 2747, 4904-4907),
  non contatti email: non vanno confusi con una lista di contatti scrivibile.

---

## 3. PIATTAFORMA DI CONSEGNA

**Verdetto: ESISTE un progetto reale e parzialmente costruito, ma non è confermato live né
confermato collegato a un acquisto.**

- `Lancio corso skill beast\Sale pag\Siti CCM\formazione-empire\` — progetto Next.js 16 +
  Supabase reale (`package.json`: `next 16.2.3`, `@supabase/supabase-js`, `@supabase/ssr`).
- `src\lib\data.ts` righe 1-3: intestazione esplicita **"MOCK DATA — Formazione Empire /
  Sostituire con dati da Supabase nella Fase 2."** — i contenuti dei corsi (incluso "CCM — Claude
  Code Mastery", riga 54) sono ancora dati finti in questo file.
- `src\lib\data.server.ts` (righe 1-50+): esiste già un livello reale collegato a Supabase
  (`createClient` da `@/lib/supabase/server`, funzioni `mapCourseFromDB`/`mapModuleFromDB`/
  `mapLessonFromDB` che leggono righe vere di database) — quindi il lavoro di "Fase 2" risulta
  in parte già fatto, in parallelo al mock ancora presente in `data.ts`.
- `supabase\migrations\0001_initial_schema.sql`: migrazione reale del database.
- `.env.local`: `NEXT_PUBLIC_SUPABASE_URL`, `NEXT_PUBLIC_SUPABASE_ANON_KEY`,
  `SUPABASE_SERVICE_ROLE_KEY` tutte valorizzate (40/46/41 caratteri — lunghezze coerenti con
  credenziali reali di un progetto Supabase, non placeholder; valori non riportati).
- **Trovato ma non verificato**: `Landing Page\ccm-empire\src\app\page.tsx` riga 31 definisce
  `COURSE_URL = "https://formazione-systemarchitect.netlify.app/"` — un dominio Netlify diverso
  da "formazione-empire", citato nel codice come destinazione dopo l'acquisto. Non ho verificato se
  questo dominio sia oggi online né se corrisponda alla stessa piattaforma trovata sopra.
- **Non verificato in questa sessione**: se `formazione-empire` sia effettivamente deployato
  (nessun file di deploy Vercel/Netlify individuato dentro la sua cartella durante questa ricerca),
  e se il middleware di enrollment (citato nella descrizione dell'agente `formazione-database`)
  blocchi davvero l'accesso a chi non ha pagato.
- Per il Manuale Claude Code specificamente: **nessuna consegna automatica** — il fallback
  `pagamento.html` (sezione 1) si limita a mandare una email a Max, che dovrebbe consegnare a mano;
  non è collegato a `formazione-empire`.
- L'unica consegna automatica di un PDF via email trovata nel repo è quella di `email-agent/main.py`
  (sezione 1), che riguarda l'ebook KDP, non il Manuale.

---

## 4. MISURAZIONE

**Verdetto: NON ESISTE. Nessun tracciamento web installato, e l'azienda stessa dichiara di non
misurare un solo euro.**

- Grep mirato su "googletagmanager|gtag(|clarity.ms|fbq(|G-XXXXXXX" in `Landing Page\*` (incluse
  `ccm-empire`, `porco-dio-empire`, i file `thank-you-*.html`, `ccm-dist\*`) e in
  `agency-empire-landing\*` e `agency-empire\*`: **zero occorrenze reali** di codice di tracciamento
  (i pochi file "trovati" da un grep più largo erano falsi positivi su classi CSS, verificato riga
  per riga).
- Conferma esplicita in `company\Memory\STATO-EMPIRE.md` riga 610 (2026-09-03), sull'unico sito
  aziendale confermato live (`digital-empire-agency.netlify.app`, vedi sezione 5): fra le cose
  "RIPRESA DA / SERVE MAX" c'è **"(2) ID GA4 + Clarity."** — non ancora installati, in attesa che
  Max fornisca gli ID.
- `company\Memory\STATO-EMPIRE.md` righe 9007-9010 (B-043, 2026-09-03 — la dichiarazione più
  recente e più autorevole trovata su questo tema): *"Digital Empire non misura un solo euro: né
  ricavi, né costi effettivi, né una metrica del percorso di vendita."*
- Il nuovo ecosistema TESORERIA (`scripts/tesoreria.py`, ADR-020, nato lo stesso giorno) esiste come
  codice ma i suoi due registri sono vuoti (vedi sezione 1): la misurazione economica è stata
  costruita ma non ancora alimentata con un solo movimento vero.
- Nessuna traccia di Plausible/Umami/PostHog/Matomo/Meta Pixel in uso reale in nessuna landing
  ispezionata.

---

## 5. SITI E PAGINE VIVE

**Verdetto: un solo sito con prova esplicita di essere online oggi; altri progetti collegati a
Vercel ma di stato non confermato o esplicitamente definiti "vecchi/scaduti"; le due pagine più
importanti dal punto di vista commerciale (Manuale, ebook KDP) risultano NON deployate.**

### Confermato live (prova diretta in Memory, con ID di progetto)
- **`https://digital-empire-agency.netlify.app`** — progetto Netlify `digital-empire-agency`
  (id `f4c62358-b3ff-4ef3-ba6d-f1b28f04b695`, team `maxignatovic980`), deploy fatto con
  `netlify deploy --prod --dir out --no-build --site <id>` (`company\Memory\STATO-EMPIRE.md`
  riga 607, 2026-09-03). È il sito dell'agenzia; le sue CTA oggi atterrano su una pagina intitolata
  "Claude Code Mastery" che resta `noindex` (stessa riga, 609-610).

### Esplicitamente scaduto/vecchio (stessa fonte)
- `agency-empire-landing.vercel.app` — Memory dichiara: "token scaduto e `vercel login` è
  interattivo, quindi... serve ancora la versione vecchia" (riga 607). L'URL risponde ma non è
  aggiornato.

### Progetti con collegamento Vercel trovato su disco, stato di pubblicazione odierno non verificato
(prova = file `.vercel\project.json` presente, cioè un deploy è stato fatto in passato)
- `agency-empire\.vercel\project.json` — progetto `agency-empire`.
- `Clienti\presentazione-empire\.vercel\project.json` — progetto `presentazione-empire`.
- `Clienti\preventivo-exponium\.vercel\project.json` — progetto `preventivo-exponium`.
- `Lancio corso skill beast\MJ- classifica\.vercel\project.json` — progetto `mj-classifica-empire`.

### Confermato NON deployato (prova diretta, doppia: Memory + verifica su disco oggi)
- `Crea siti\Siti CCM\manuale.html` / `pagamento.html` (la pagina di vendita del Manuale Claude
  Code): `company\Memory\STATO-EMPIRE.md` righe 8043-8045 dichiara "esiste solo come file locale —
  nessun vercel.json/netlify.toml/CNAME trovato nella cartella"; verificato di nuovo oggi con
  ricerca diretta nella cartella `Crea siti\Siti CCM\`: nessuno di quei file è presente.
- Le 6 landing dell'ebook KDP (`KDP - prodottti digitali\Leanding Page\Il Codice dei Potenti\*\`):
  nessun file di deploy trovato nelle rispettive cartelle.
- `formazione-empire`: nessun file di deploy individuato nella cartella durante questa ricerca
  (vedi sezione 8 — non è stata una ricerca esaustiva).

---

## 6. IL PRODOTTO PILOTA

**Verdetto: il manoscritto ESISTE ED È COMPLETO come file (203 pagine); come prodotto lanciato e
vendibile NON esiste ancora — non è mai passato per un acquisto reale (sezioni 1, 4, 5).**

- File trovato in due copie identiche per dimensione (probabile duplicato):
  - `C:\Users\Utente\Desktop\qui tutto\Digital Empire\MANUALE COMPLETO DI CLAUDE CODE PER IL
    BUSINESS.pdf`
  - `C:\Users\Utente\Desktop\qui tutto\Digital Empire\Formazzione\Claude code\MANUALE COMPLETO DI
    CLAUDE CODE PER IL BUSINESS.pdf`
  - Entrambe: **2.931.882 byte (~2,8 MB)**, data del file 2026-03-05.
- **Conteggio pagine verificato direttamente dalla struttura interna del PDF** (oggetto radice
  `/Pages` con `/Count 203`, letto a livello binario, non stimato): **203 pagine**.
- Esiste anche un manoscritto sorgente in Markdown parallelo:
  `Formazzione\Claude code\MANUALE COMPLETO DI CLAUDE CODE PER IL BUSINESS.md`.
- La pagina wiki (archiviata) `second-brain-vault\wiki\09 - Archives\legacy\entities\
  Manuale_Claude_Code_Product.md` (2026-04-29) conferma indipendentemente "203-page ebook", 10
  parti/~38 capitoli, e registra alla voce Metrics: **"Sales: 0 (not yet launched)"** — coerente
  con quanto trovato oggi nella tesoreria (sezione 1).
- Il prezzo È stato deciso: €67 lancio / €97 listino, `DIGITAL-EMPIRE\00-MEMORY\decisions\
  DEC-EST-001-b-003-prezzo-manuale-claude-code-sblocco.md` riga 15 (decisione del 2026-07-21,
  passata per silenzio-assenso). Coincide con `checkout.config.json`. Ma la finestra di lancio
  dichiarata lì (`2026-07-31`) è scaduta da oltre un mese senza che il pagamento reale (Tier 1)
  sia mai stato attivato.
- **Non verificato in questa sessione**: la completezza capitolo per capitolo del contenuto (non
  ho letto le 203 pagine); ho verificato struttura, dimensione e conteggio pagine, non la qualità
  o l'assenza di segnaposto interni al testo.

---

## 7. VERDETTO SECCO

| # | Voce | Stato |
|---|------|-------|
| 1 | **Pagamenti** | **NON ESISTE** (automatico) — esiste solo un fallback manuale via email per il Manuale; una chiave Stripe live reale esiste ma per un ebook diverso e senza un bottone d'acquisto collegato a nessuna pagina trovata |
| 2 | **Lista contatti** | **ESISTE MA NON PROVATO** — form Brevo funzionante su una landing, ma chiave esposta pubblicamente da mesi (mai ruotata) e nessun numero di iscritti reale reperibile |
| 3 | **Piattaforma di consegna** | **ESISTE MA NON PROVATO** — piattaforma Supabase/Next.js reale e in parte collegata a un DB vero, ma stato di deploy e di gating-pagamento non confermati |
| 4 | **Misurazione** | **NON ESISTE** — nessun tracciamento (GA4/Clarity/Pixel) installato su alcun sito verificato; l'azienda dichiara essa stessa (2026-09-03) di non misurare un euro |
| 5 | **Siti e pagine vive** | **ESISTE (parzialmente)** — 1 sito confermato live (`digital-empire-agency.netlify.app`), altri di stato incerto o esplicitamente scaduti; le pagine di vendita del prodotto pilota NON sono online |
| 6 | **Prodotto pilota (Manuale Claude Code)** | **ESISTE E FUNZIONA** come file (203 pagine, manoscritto completo) — **SOLO PROGETTATO** come prodotto lanciato/vendibile (zero vendite, checkout mai attivato) |

**Sintesi in una frase**: Digital Empire può oggi, al massimo, ricevere un ordine per email e
consegnarlo a mano — non esiste un solo percorso automatico, collaudato e misurato che porti da
"qualcuno vede una pagina" a "un euro è arrivato e il prodotto è stato consegnato".

---

## 8. COSA NON HO POTUTO VERIFICARE

- Non ho chiamato le API di Brevo o Stripe (per non esporre le credenziali trovate e per non
  alterare nulla): non so se le chiavi trovate siano ancora valide/attive, né il numero reale di
  contatti nella lista Brevo, né se ci sia mai stata una transazione Stripe reale sull'account
  legato alla chiave `sk_live_...` di `email-agent`.
- Non ho effettuato richieste web esterne: lo stato "live" di `digital-empire-agency.netlify.app`
  si basa sulla dichiarazione esplicita e circostanziata in Memory (con project id Netlify), non su
  una verifica diretta di raggiungibilità fatta da me oggi. Stesso discorso per
  `formazione-systemarchitect.netlify.app` (trovato nel codice, mai verificato).
- Non ho letto le 203 pagine del Manuale Claude Code: ho verificato struttura, dimensione file e
  conteggio pagine reale (dall'oggetto `/Pages` del PDF), non il contenuto capitolo per capitolo.
- Non ho verificato lo stato di deploy di `formazione-empire`, e dei quattro progetti Vercel
  elencati in sezione 5 (`agency-empire`, `presentazione-empire`, `preventivo-exponium`,
  `mj-classifica-empire`) oltre alla presenza di un `project.json` collegato — non so se il
  contenuto pubblicato oggi su quei domini sia aggiornato, vecchio, o assente.
- Non ho verificato se il servizio FastAPI di `email-agent` sia effettivamente in esecuzione da
  qualche parte (Railway o altrove): ho trovato `Procfile`/`runtime.txt` ma nessuna prova di un
  deploy attivo.
- Il repository ha decine di migliaia di file distribuiti su oltre 50 cartelle di primo livello,
  incluso codice vendorizzato di terze parti (es. `ruflo`, `Agency page\Clienti\marketingskills-main`).
  La ricerca è stata mirata (grep globali sulle parole chiave del task + lettura diretta delle aree
  più rilevanti: `company/Memory`, wiki, `Landing Page`, `Crea siti/Siti CCM`, `KDP - prodottti
  digitali`, `formazione-empire`) — non ho ispezionato ogni file del repo uno per uno.
- Non ho aperto singolarmente tutte e 6 le varianti delle landing "Il Codice dei Potenti".

### Cose trovate fuori perimetro (segnalate, non toccate)
- La chiave API Brevo esposta pubblicamente da mesi (BACKLOG B-020, ancora ⬜ aperta) è un rischio
  di sicurezza attivo, non solo un problema di misurazione — meriterebbe rotazione indipendentemente
  da questo audit.
- `email-agent/.git.bak`: la cartella `.git` di quel sotto-progetto è stata rinominata `.git.bak`
  (repo git annidato disattivato) — segnalo solo perché spiega perché il codice sul disco
  (Gmail SMTP) differisce dall'ultimo commit registrato (Mailjet API), nel caso serva chiarire quale
  versione è quella "vera".
