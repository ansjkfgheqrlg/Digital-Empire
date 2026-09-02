# ADR-PROPOSTA — Audit cross-model in fase GATE per i deliverable ad alto rischio

> **STATO: PROPOSTA — da approvare da Max.** Questo file non è un ADR attivo: non modifica ADR-006,
> non tocca skill o agenti, non introduce nulla nel flusso ordinario. È la sintesi di un gap reale
> trovato durante l'ingestione di un video, scritta per essere discussa e decisa, non applicata.

- **Data:** 2026-09-02
- **Stato:** PROPOSTA (non attiva)
- **Origine:** ingestione video `T7PPX5M6Puo` — "Claude Code + Codex: Il Setup di cui NESSUNO Parla"
  (Riccardo Belli Contarini, Martes AI), `memory-empire/knowledge/T7PPX5M6Puo/`
- **Decisori:** nessuno ancora — proposta in attesa di Max

## Contesto

I controlli di qualità e sicurezza di Digital Empire girano su un unico impianto: il **Ciclo di
Fase Empire a 9 passi** (ADR-006), il cui passo 5 — **REVIEW indipendente** — è affidato a un
insieme di sentinel dedicati (`sentinel-security`, `sentinel-drift`, `sentinel-quality`,
`review-and-heal`, `security.agent`). Questi agenti sono "indipendenti" nel senso previsto da
ADR-006: sono agenti diversi da chi costruisce, con ruoli e prompt distinti, e il passo REVIEW è
bloccante prima del COMMIT.

Ma tutti — costruttori e giudici — girano oggi **sullo stesso fornitore di modello** (Claude, con
tier diversi: Haiku per i sentinel leggeri, Sonnet/Opus per i reviewer più profondi). Nessuno dei
controlli attuali di DE usa un modello di famiglia diversa (es. GPT/OpenAI) per rileggere un
deliverable prodotto da Claude.

## Il problema

**Un giudice della stessa famiglia condivide i punti ciechi dell'autore.** Non è una questione di
quale modello sia "più bravo": un reviewer addestrato nella stessa famiglia tende a non vedere le
stesse classi di problemi che il modello che ha scritto il codice non vede, perché condividono
un'origine di addestramento e — verosimilmente — bias di compiacenza simili verso codice "familiare".

**Prova esterna, non teorica.** Il video mostra **3 casi su 3** in cui questo scenario si verifica
concretamente:

1. **MaReply** (clone ManyChat, gestisce account Instagram di clienti): Claude Code aveva
   dichiarato l'app "pronta per essere mandata in produzione". Un audit con Codex (`/codex:rescue`,
   modello di famiglia diversa) ha trovato **2 falle Alte**: autenticazione email/password senza
   verifica email (account dirottabile via invito) e DM duplicati per assenza di claim atomico
   (spam, doppio consumo budget Meta, rischio phishing/reputazionale).
2. **Form candidature** (Cloudflare + Airtable, dati personali di candidati): stesso schema.
   Codex ha trovato **4 findings Alti** (endpoint pubblico senza rate limiting/CAPTCHA, upload
   completamente fidato lato server, nessun limite sulla dimensione dei campi, librerie di terze
   parti senza SRI/CSP) più 10 medi e 1 info — nessuno segnalato in precedenza da Claude Code.
3. **Piano "clone Bitly"** (fase di pianificazione, prima ancora di scrivere codice): un
   `adversarial-review` di Codex sul `PLAN.md` scritto da Claude ha trovato 1 finding **critical**
   (API stats/delete senza verifica ownership — chiunque può cancellare link altrui) e 2 **high**.
   Claude, interrogato di nuovo sulle obiezioni, ha confermato **4 obiezioni su 5 fondate** —
   incluso l'errore di aver proposto redirect 301 invece di 302, lo stesso errore che Bitly aveva
   corretto nel 2016.

In tutti e tre i casi, il "primo giudice" (Claude, stessa famiglia di chi aveva costruito) aveva
già dato il via libera o scritto il piano senza rilevare il problema poi trovato da un modello di
famiglia diversa.

## Proposta

Aggiungere un **secondo passaggio di audit con un modello di famiglia diversa**, con perimetro
volutamente stretto:

- **Solo in fase GATE** (il passo 4/5 del ciclo ADR-006), mai in sostituzione della REVIEW
  indipendente esistente — si aggiunge dopo, non al posto di.
- **Solo per deliverable ad alto rischio dati/credenziali**: sistemi che custodiscono credenziali
  di terzi, dati personali, o accesso a conti/pagamenti. Candidati espliciti in DE oggi:
  - **Preventa Outreach** (credenziali WhatsApp/Areus, dati concessionari)
  - **Formazione Empire** (dati studenti, autenticazione, pagamenti corso)
  - **PreventivoForge** (multi-tenant, kill-switch abbonamento, dati clienti concessionari)
- **Un secondo modello di provider diverso** (es. via API OpenAI o Codex CLI, sul modello dei
  comandi `/codex:rescue` / `/codex:adversarial-review` mostrati nel video) rilegge il deliverable
  o il piano con lo stesso schema di severità già in uso nei sentinel Claude
  (critical/high/medium/low/info), per restare comparabile.
- **L'umano resta nel mezzo**: come nel video (Belli filtra i finding e scarta esplicitamente il
  "doppio DM" come falso problema), i finding del secondo giudice si leggono e si filtrano, non si
  applicano alla cieca.

## Cosa NON propone

- **Non sostituisce ADR-006.** Il ciclo a 9 passi resta invariato per ogni fase normale.
- **Non tocca il flusso ordinario.** La stragrande maggioranza dei deliverable DE non tratta dati
  o credenziali ad alto rischio e continua con la sola REVIEW indipendente Claude-su-Claude.
  Chiedere un secondo modello ovunque sarebbe uno spreco, non un rinforzo.
- **Non introduce un secondo abbonamento per tutta l'organizzazione.** Nessuna proposta di
  installare il plugin Codex, configurare marketplace/plugin di Claude Code, o dotare ogni sessione
  di un secondo provider. Se approvata, l'implementazione andrebbe decisa a parte (probabilmente
  via chiamata API mirata sui soli deliverable in scope, non un secondo CLI persistente).
- **Non è un ADR attivo.** Nessuna skill, agente o ADR esistente viene modificato da questo file.

## Costi e complessità (dichiarati onestamente)

- **Credenziale aggiuntiva da gestire**: un secondo provider (OpenAI/ChatGPT o API key) significa
  un secondo account, una seconda chiave da custodire e ruotare — lo stesso tipo di superficie che
  DE ha già dovuto correggere più volte per credenziali esposte (vedi B-020, B-021, B-023 in
  `company/Memory/BACKLOG.md`). Non è gratis in termini di superficie di gestione, anche se il
  costo mensile diretto è basso (il video stima $20/mese aggiuntivi, o $0 in fase di test con
  ChatGPT Free).
- **Beneficio limitato ai casi ad alto rischio**: il guadagno dimostrato nel video è specifico a
  sicurezza/dati — non c'è prova che un secondo modello aggiunga valore su deliverable a basso
  rischio (copy, contenuti, pagine statiche), dove i sentinel Claude esistenti bastano.
  Estendere la proposta oltre il perimetro "dati/credenziali" non è giustificato dalla prova
  disponibile (una sola fonte, tre casi, un solo autore/agenzia).
- **Un secondo ecosistema da mantenere**: anche limitato a pochi deliverable, un secondo provider
  significa un secondo punto di configurazione, un secondo posto dove qualcosa può rompersi
  silenziosamente, e una seconda cosa da tenere aggiornata nel tempo.
- **Nessun benchmark quantitativo a supporto**: la fonte (un solo video, tre casi aneddotici di
  una sola agenzia) non fornisce un tasso di falsi positivi né una stima di quanto spesso il
  secondo giudice troverebbe davvero qualcosa di nuovo su deliverable DE reali. La proposta va
  trattata come ipotesi da pilotare, non come certezza.

## Alternative scartate (dal video-analysis.md di origine)

- **Costruire una skill nuova dedicata al plugin Codex** — scartata: DE non ha un gap di skill di
  audit (esistono già `security-review`, `verification-quality`, `swarm-advanced`); il gap è di
  diversità di modello nei controlli esistenti, non di skill mancanti.
- **Creare un workflow parallelo nuovo** — scartata: il pattern "piano contestato da un secondo
  giudice prima di scrivere codice" è già concettualmente coperto dai passi SPEC → PRE-MORTEM di
  ADR-006; basterebbe un'estensione mirata, non un intero workflow nuovo.

## Conseguenze se approvata

- ADR-006 riceverebbe una clausola opzionale nel passo REVIEW indipendente: "per fasi a rischio
  alto (dati personali, pagamenti, credenziali di terzi), la REVIEW indipendente include un
  secondo modello di provider diverso."
- Andrebbe definito, in un ADR separato o in questo stesso una volta attivato: quale provider,
  come si gestisce la credenziale, chi decide quali deliverable sono "ad alto rischio" (probabile
  che sia il Sentinel Drift o un criterio esplicito in `company/skills-map.yaml`), e un pilota
  su un solo ecosistema prima di estendere agli altri due candidati.

## Conseguenze se NON approvata

- Nessuna: lo stato attuale (REVIEW indipendente solo su modelli Claude) resta quello vigente.
  Il gap resta documentato in `company/Memory/BACKLOG.md` (B-042) per essere riconsiderato quando
  Max lo ritiene opportuno.

## Contradiction-check

Non contraddice ADR-006 (lo estende con una clausola opzionale, non lo sostituisce), non contraddice
ADR-008 (l'eventuale nuovo passo di audit avrebbe comunque proprietario/controllore/origine/governo
come ogni altro artefatto). Nessun conflitto con ADR attivi.

## Connessioni

- [[ADR-006]] (ciclo 9 passi — il passo che questa proposta vorrebbe estendere)
- [[ADR-008]] (catena di intestazione — se approvata, la clausola nuova erediterebbe le stesse regole)
- `company/Memory/BACKLOG.md` — **B-042**
- `memory-empire/knowledge/T7PPX5M6Puo/` — fonte integrale di questa proposta
- `second-brain-vault/wiki/sources/Source_Riccardo_Belli_Claude_Codex_Setup.md`
