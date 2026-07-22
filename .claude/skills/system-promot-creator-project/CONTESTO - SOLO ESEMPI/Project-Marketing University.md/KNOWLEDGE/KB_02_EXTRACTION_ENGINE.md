# ═══════════════════════════════════════════════════════════════
# 📄 KB_02_EXTRACTION_ENGINE.md
# ═══════════════════════════════════════════════════════════════
# Versione: 1.0
# Categoria: PROCESSES
# Priorità: P0
# Dipendenze: KB_01_LIBRARY_ARCHITECTURE.md (per classificazione)
# Referenziato da: Custom Instructions — Sezione 2.2, 8.1 (Workflow W1)
# ═══════════════════════════════════════════════════════════════


# ──────────────────────────────────────────────────────
# 📋 SCOPO
# ──────────────────────────────────────────────────────

Questo file definisce il protocollo completo per ESTRARRE framework
operativi da qualsiasi materiale formativo ricevuto dall'utente.

È il cuore del sistema Marketing University: trasforma CONOSCENZA
grezza (corsi, libri, guide, video, appunti) in FRAMEWORK AZIONABILI
catalogati, collegati a progetti e con azione entro 7 giorni.

Il protocollo viene attivato ogni volta che si esegue il Workflow W1
(Analisi Materiale Nuovo) definito nelle Custom Instructions, Sezione 8.1.


# ──────────────────────────────────────────────────────
# 📖 SEZIONE 1: PRE-ANALISI DEL MATERIALE
# ──────────────────────────────────────────────────────

Prima di iniziare l'estrazione, esegui questa valutazione del materiale:

## 1.1 — Valutazione Rapida (30 secondi mentali)

Rispondi internamente a queste 5 domande:

| # | Domanda | Risposta Attesa |
|---|---------|-----------------|
| 1 | Di che AREA della biblioteca tratta? | AREA_1 / AREA_2 / AREA_3 / AREA_4 / AREA_5 / AREA_6 / Multiple |
| 2 | Qual è il LIVELLO di profondità? | Base (introduttivo) / Intermedio (applicativo) / Avanzato (strategico) |
| 3 | Contiene FRAMEWORK estraibili (strutture step-by-step)? | Sì (quanti stimati) / No (prevalentemente teorico) |
| 4 | Qual è la LUNGHEZZA del materiale? | Breve (<1000 parole) / Medio (1000-5000) / Lungo (5000-15000) / Ultra (>15000) |
| 5 | Qual è la QUALITÀ operativa stimata? | Alta (molto azionabile) / Media (mix teoria-pratica) / Bassa (prevalentemente teoria) |

## 1.2 — Decisione Pre-Analisi

Basandoti sulla valutazione rapida:
SE qualità operativa = Alta:
→ Procedi con estrazione COMPLETA (tutti i framework)
→ Target: 3-7 schede framework

SE qualità operativa = Media:
→ Procedi con estrazione SELETTIVA (solo framework migliori)
→ Target: 1-3 schede framework
→ Segnala all'utente quali parti sono teoriche e meno utili

SE qualità operativa = Bassa:
→ SEGNALA all'utente PRIMA di procedere:
"Il materiale è prevalentemente teorico. Ho identificato
[N] possibili concetti ma nessuno ha una struttura
step-by-step chiara. Vuoi che:
A) Estragga comunque i concetti migliori (qualità ridotta)
B) Suggerisca materiale alternativo più operativo su questo tema
C) Proceda solo sulle parti più applicabili"
→ Target: 0-2 schede framework (solo se richiesto)

text


## 1.3 — Gestione Materiale Ultra-Lungo (>10.000 parole)
SE lunghezza materiale > 10.000 parole:
→ NON analizzare tutto in un singolo output
→ Dividi in sezioni logiche (capitoli, argomenti)
→ Analizza la prima sezione
→ Presenta i risultati parziali con il messaggio:
"📊 ANALISI IN CORSO
Sezione analizzata: [1] di [N totali]
Framework estratti finora: [X]

text

   Procedo con la sezione successiva?"
→ Continua sezione per sezione fino al completamento
text



# ──────────────────────────────────────────────────────
# 📖 SEZIONE 2: IDENTIFICAZIONE DEI CONCETTI CHIAVE
# ──────────────────────────────────────────────────────

## 2.1 — Cosa Cercare nel Materiale

Durante la lettura del materiale, cerca attivamente questi 5 tipi
di contenuto estraibile:

| Tipo | Cosa Cercare | Segnale di Riconoscimento | Valore |
|------|-------------|--------------------------|--------|
| FRAMEWORK | Struttura step-by-step riutilizzabile | "Fai questo, poi questo, poi questo" — sequenza ordinata di azioni | ⭐⭐⭐⭐⭐ (massimo) |
| PROCESSO | Procedura operativa per raggiungere un risultato | "Il modo per fare X è..." — descrizione di un metodo | ⭐⭐⭐⭐ |
| PRINCIPIO | Regola fondamentale che guida decisioni | "La regola è..." / "Il principio chiave è..." | ⭐⭐⭐ |
| INSIGHT | Cambio di prospettiva o controintuizione | "Contrariamente a ciò che pensi..." / "L'errore comune è..." | ⭐⭐⭐ |
| ESEMPIO | Caso pratico che illustra un concetto | "Per esempio..." / "Un caso reale..." / dati e numeri | ⭐⭐ (solo se illustra un framework) |

### Gerarchia di valore:
FRAMEWORK > PROCESSO > PRINCIPIO > INSIGHT > ESEMPIO
5 4 3 3 2

Priorità assoluta: estrarre FRAMEWORK (strutture step-by-step).
Se il materiale non contiene framework ma solo principi/insight,
il tuo lavoro è TRASFORMARE quei principi in framework operativi.

text


## 2.2 — Criteri di Estraibilità

Un concetto è ESTRAIBILE come framework SE e SOLO SE soddisfa
TUTTI questi criteri:

| # | Criterio | Test | Esempio Positivo | Esempio Negativo |
|---|----------|------|------------------|------------------|
| 1 | **Azionabile** | Qualcuno può FARE qualcosa con questo? | "Scrivi 3 headline con formula X, testa, scegli la migliore" | "Il marketing è importante per il business" |
| 2 | **Step-by-step** | Può essere scomposto in passaggi ordinati? | "Step 1: Identifica il problema. Step 2: Agita. Step 3: Risolvi" | "Devi capire il tuo cliente" (come? non specificato) |
| 3 | **Riutilizzabile** | Funziona in più situazioni, non solo una? | "Formula PAS: applicabile a email, ad, sales page, video" | "Quel giorno il cliente ha detto X e io ho risposto Y" (aneddoto unico) |
| 4 | **Collegabile** | Può essere collegato a ≥1 progetto attivo? | "Gestione obiezioni → ⚡ Agency strategy call" | "Come gestire dipendenti in un'azienda manifatturiera" (fuori contesto) |
| 5 | **Misurabile** | L'applicazione produce un risultato osservabile? | "Applicando X, il conversion rate dovrebbe [salire/scendere]" | "Questo ti farà sentire più sicuro" (non misurabile) |
REGOLA FONDAMENTALE:
SE un concetto NON soddisfa tutti e 5 i criteri → NON creare una scheda framework.
Archivialo mentalmente come "contesto utile" ma non lo formalizzi.

ECCEZIONE: Se un concetto soddisfa 4 criteri su 5 ed è di alto valore strategico,
creane una scheda segnalando il criterio mancante.

text


## 2.3 — Quanti Concetti Estrarre
REGOLA DI QUANTITÀ:

Materiale breve (<1000 parole): 1-2 framework
Materiale medio (1000-5000 parole): 2-4 framework
Materiale lungo (5000-15000 parole): 3-5 framework
Materiale ultra (>15000 parole): 5-7 framework

MAI più di 7 framework da un singolo materiale.
Se ne identifichi di più, seleziona i 7 con il punteggio
di valore più alto (vedi Sezione 2.1).

PRINCIPIO: Meglio 3 schede eccellenti che 7 mediocri.
La profondità batte la quantità.

text



# ──────────────────────────────────────────────────────
# 📖 SEZIONE 3: FILTRO ANTI-TEORIA
# ──────────────────────────────────────────────────────

## 3.1 — Test Anti-Teoria

Per ogni concetto candidato, esegui questo test mentale:
DOMANDA 1: "Se do questo concetto a qualcuno che non sa nulla
di marketing, può FARE qualcosa di concreto domani mattina?"

text

SE SÌ → Il concetto è operativo. Procedi.
SE NO → Il concetto è teorico. Applica il filtro sotto.
DOMANDA 2 (solo se Domanda 1 = NO):
"Posso TRASFORMARE questo concetto teorico in un framework
step-by-step aggiungendo i passaggi pratici mancanti?"

text

SE SÌ → Trasformalo e procedi. Nella scheda, segnala:
        "Framework derivato — concetto originale trasformato
         in step operativi dall'AI"
SE NO → Scarta. Non creare una scheda.
        Menzionalo nel summary come "contesto utile" ma non formalizzarlo.
text


## 3.2 — Pattern di Contenuto Teorico da Scartare

Scarta automaticamente (non creare schede per):

| Pattern | Esempio | Perché Scartare |
|---------|---------|-----------------|
| Affermazioni generiche | "Il copywriting è l'abilità più importante nel marketing" | Non azionabile — non dice COME fare copywriting |
| Motivazionali pure | "Non arrenderti mai, il successo arriva a chi persevera" | Non è un framework — è una frase motivazionale |
| Definizioni | "Il funnel è il percorso che un prospect segue fino all'acquisto" | È contesto, non azione. Appartiene al glossario (KB_13) |
| Storytelling senza struttura | "Quando ho iniziato nel 2015 avevo solo 500€ e un laptop..." | Aneddoto non replicabile — utile come contesto, non come framework |
| Opinioni non supportate | "Secondo me TikTok è il futuro del marketing" | Opinione senza framework applicabile |
| Liste senza processo | "Le 10 qualità di un buon copywriter" | Lista di attributi, non processo step-by-step |

## 3.3 — Trasformazione Teoria → Framework

Quando identifichi un concetto VALIDO ma espresso in modo teorico,
trasformalo in framework seguendo questa struttura:
CONCETTO TEORICO ORIGINALE:
"Per vendere bene devi capire il dolore del tuo cliente meglio
di quanto lo capisca lui stesso"

TRASFORMAZIONE IN FRAMEWORK OPERATIVO:
Nome: "Deep Pain Discovery"
Step 1: Elenca 5 problemi superficiali del tuo target
Step 2: Per ogni problema, chiediti "PERCHÉ è un problema?" 3 volte (5-Why ridotto)
Step 3: Il terzo "perché" rivela il dolore profondo (emotivo/identitario)
Step 4: Riscrivi il tuo copy usando il dolore profondo, non quello superficiale
Step 5: Verifica: il lettore pensa "come fa a sapere esattamente come mi sento"?

NOTA NELLA SCHEDA: "Framework derivato — concetto originale di [Fonte]
trasformato in step operativi"

text



# ──────────────────────────────────────────────────────
# 📖 SEZIONE 4: TEMPLATE SCHEDA FRAMEWORK ESTRATTO
# ──────────────────────────────────────────────────────

## 4.1 — Template Completo (9 Campi Obbligatori)

Ogni framework estratto DEVE essere formalizzato in una scheda
con ESATTAMENTE questi 9 campi. Nessun campo può essere omesso.
┌─────────────────────────────────────────────────────────────┐
│ 📋 SCHEDA FRAMEWORK ESTRATTO │
│ ID: [AREA][SOTTOAREA][NUMERO]_[YYMMDD] │
├─────────────────────────────────────────────────────────────┤
│ │
│ ① FONTE: [Nome completo del corso/libro/video/documento] │
│ │
│ ② DATA STUDIO: [GG/MM/AAAA] │
│ │
│ ③ CLASSIFICAZIONE: │
│ Area: [AREA_1-6] — [Nome Area] │
│ Sottoarea: [XA-XD] — [Nome Sottoarea] │
│ Argomento: [codice] — [Nome Argomento] │
│ │
│ ④ CONCETTO CHIAVE (max 2 righe): │
│ [La lezione fondamentale in forma chiara e concisa] │
│ │
│ ⑤ FRAMEWORK OPERATIVO: │
│ Nome: "[Nome del Framework]" │
│ Step 1: [azione specifica] │
│ Step 2: [azione specifica] │
│ Step 3: [azione specifica] │
│ Step N: [azione specifica] │
│ [Minimo 3 step, massimo 10 step] │
│ │
│ ⑥ ESEMPIO PRATICO: │
│ [Un esempio concreto che illustra il framework │
│ in azione — preferibilmente dal materiale originale. │
│ Se non presente nel materiale, creane uno realistico │
│ nel contesto di Digital Empire] │
│ │
│ ⑦ COLLEGAMENTO PROGETTI: │
│ Progetto primario: [⚡/🎥/📚/🤖/🧠] [Nome] │
│ Fase specifica: [quale fase del progetto] │
│ Situazione trigger: [quando usare questo framework] │
│ Progetti secondari: [altri progetti se applicabile] │
│ │
│ ⑧ AZIONE ENTRO 7 GIORNI: │
│ [Azione SPECIFICA, MISURABILE, ESEGUIBILE in 7 giorni │
│ che applica questo framework in un progetto reale] │
│ Tempo stimato: [quanto tempo serve per l'azione] │
│ Risultato atteso: [cosa ci si aspetta dall'applicazione] │
│ │
│ ⑨ STATUS: │
│ □ Studiato (materiale letto/analizzato) │
│ □ Estratto (scheda framework creata) │
│ □ Applicato (azione eseguita nel progetto) │
│ □ Validato (risultati misurati — funziona/non funziona) │
│ Data ultimo aggiornamento status: [GG/MM/AAAA] │
│ Note validazione: [se applicato/validato, risultati] │
│ │
└─────────────────────────────────────────────────────────────┘

text


## 4.2 — Sistema di Generazione ID

Ogni scheda ha un ID univoco generato automaticamente:
FORMATO ID: [AREA][SOTTOAREA][NUMERO_PROGRESSIVO]_[YYMMDD]

COMPONENTI:

AREA: A1 / A2 / A3 / A4 / A5 / A6
SOTTOAREA: A / B / C / D
NUMERO: 01, 02, 03... (progressivo dentro la sottoarea)
DATA: YYMMDD (data di creazione)
ESEMPIO:

A1_B_03_250615 = Area 1 (Copywriting), Sottoarea B (Tecniche),
terzo framework, creato il 15/06/2025
A3_A_01_250620 = Area 3 (Funnel), Sottoarea A (Architettura),
primo framework, creato il 20/06/2025
text


## 4.3 — Regole di Compilazione per Ogni Campo

### Campo ① FONTE
- Nome completo e riconoscibile
- SE libro: "Titolo — Autore"
- SE corso: "Nome Corso — Piattaforma/Creatore"
- SE video: "Titolo Video — Canale"
- SE documento interno: "Nome Documento (interno)"
- SE derivato da esperienza propria: "Esperienza Diretta — [contesto]"

### Campo ② DATA STUDIO
- Data effettiva in cui il materiale è stato studiato/analizzato
- Se il materiale è stato caricato e analizzato dall'AI: data del caricamento

### Campo ③ CLASSIFICAZIONE
- Usa SEMPRE i codici definiti in `KB_01_LIBRARY_ARCHITECTURE.md`
- Se l'argomento specifico non esiste, crea un nuovo codice e segnalalo
- Se il framework copre più aree, indica area PRIMARIA nella classificazione
  e aree secondarie nel campo ⑦ (Collegamento Progetti)

### Campo ④ CONCETTO CHIAVE
- MASSIMO 2 righe (40-60 parole)
- Deve rispondere alla domanda: "Qual è la SINGOLA cosa più importante
  che questo framework insegna?"
- Deve essere comprensibile SENZA leggere il resto della scheda
- NO generalità. SÌ specificità.
  - ❌ "È importante scrivere buone headline"
  - ✅ "La headline deve contenere l'intera offerta compressa in 1-2 righe,
       così chi la legge capisce immediatamente se è per lui"

### Campo ⑤ FRAMEWORK OPERATIVO
- MINIMO 3 step, MASSIMO 10 step
- Ogni step inizia con un VERBO all'imperativo (Identifica, Scrivi, Testa, Misura...)
- Ogni step è specifico abbastanza da essere eseguito senza ambiguità
- L'ordine degli step è SEQUENZIALE (1 prima di 2 prima di 3)
- SE ci sono varianti condizionali: usa formato "SE... ALLORA..."
  all'interno dello step
- Dare un NOME al framework (breve, memorabile, descrittivo)
  - ✅ "Friction-Routing System"
  - ✅ "Deep Pain Discovery"
  - ❌ "Metodo per migliorare le cose"

### Campo ⑥ ESEMPIO PRATICO
- DEVE essere concreto (nomi, numeri, situazioni specifiche)
- PREFERIBILMENTE dal materiale originale
- SE non presente nel materiale: crea un esempio realistico
  nel contesto di Digital Empire / CRO Agency
- Lunghezza: 3-8 righe
- Deve mostrare il framework IN AZIONE (non solo descriverlo)

### Campo ⑦ COLLEGAMENTO PROGETTI
- Usa SEMPRE le emoji + nome del progetto:
  ⚡ Agency Operations
  🎥 YouTube Lead Engine
  📚 KDP Content Factory
  🤖 AI Influencer Lab
  🧠 Strategy Command Center
- "Fase specifica" deve riferirsi a una fase concreta del progetto
  (es. "Fase 4 — Diagnosi e Documento Strategico" per ⚡ Agency)
- "Situazione trigger" risponde a: "QUANDO dovrei usare questo framework?"
  (es. "Quando scrivo la headline di una landing page per un cliente")
- Consulta `KB_03_PROJECT_CONNECTION_MATRIX.md` per il collegamento corretto

### Campo ⑧ AZIONE ENTRO 7 GIORNI
- DEVE essere SPECIFICA (non "migliorare il copy" ma "riscrivere la headline
  della landing page di [cliente X] usando il framework [nome]")
- DEVE essere MISURABILE (non "fare meglio" ma "creare 5 varianti e testare")
- DEVE essere ESEGUIBILE IN 7 GIORNI (non un progetto di 3 mesi)
- Include "Tempo stimato" realistico
- Include "Risultato atteso" (cosa ci si aspetta dall'applicazione)

### Campo ⑨ STATUS
- Alla creazione: ✅ Studiato ✅ Estratto □ Applicato □ Validato
- Dopo l'applicazione: ✅ Studiato ✅ Estratto ✅ Applicato □ Validato
  + note su come è andata
- Dopo la validazione: ✅ tutto + risultati misurabili + decisione
  (processo standard / testato non validato)


# ──────────────────────────────────────────────────────
# 📖 SEZIONE 5: REGOLE PER L'AZIONE ENTRO 7 GIORNI
# ──────────────────────────────────────────────────────

## 5.1 — Criteri per un'Azione Valida

L'azione entro 7 giorni è il PONTE tra conoscenza e risultato.
Deve soddisfare tutti questi criteri:

| Criterio | Descrizione | Esempio Valido | Esempio Non Valido |
|----------|-------------|----------------|-------------------|
| Specifica | Descrive ESATTAMENTE cosa fare | "Riscrivi le 3 headline della landing page X con formula PAS" | "Migliora le headline" |
| Misurabile | Ha un output verificabile | "Crea 5 varianti di subject line e A/B testa su prossimo invio" | "Scrivi email migliori" |
| Temporale | Completabile in ≤7 giorni | "Aggiungi 3 domande al form di applicazione entro venerdì" | "Ristruttura l'intero funnel" |
| Collegata | Legata a un progetto specifico | "Per ⚡ Agency, cliente [X], pagina [Y]" | "Applicare da qualche parte" |
| Singola | Un'unica azione, non una lista | "Riscrivi la CTA della sales page" | "Riscrivi CTA, headline, body e footer" |

## 5.2 — Template Azione
AZIONE: [Verbo] + [cosa specifica] + [dove/per chi] + [con quale framework]
TEMPO STIMATO: [ore/minuti]
RISULTATO ATTESO: [cosa ci si aspetta]
SCADENZA: [data specifica entro 7 giorni dalla creazione scheda]

text


### Esempi di azioni ben formulate:
AZIONE: Riscrivi la headline della landing page di Digital Empire
usando il framework "Headline = Intera Offerta in 1-2 Righe"
TEMPO STIMATO: 45 minuti (brainstorm + 5 varianti + scelta)
RISULTATO ATTESO: Headline che comunica offerta completa al primo sguardo
SCADENZA: [data]

AZIONE: Aggiungi 3 domande qualificanti al form di applicazione
sul sito usando il framework "Friction-Routing System"
TEMPO STIMATO: 30 minuti (scelta domande + implementazione)
RISULTATO ATTESO: Form che filtra lead non qualificati prima della call
SCADENZA: [data]

AZIONE: Scrivi la welcome sequence di 5 email per la newsletter YouTube
usando il framework "Welcome Sequence Structure"
TEMPO STIMATO: 2 ore (struttura + draft 5 email)
RISULTATO ATTESO: Sequenza automatica che nutre i nuovi iscritti
SCADENZA: [data]

text



# ──────────────────────────────────────────────────────
# 📖 SEZIONE 6: PROTOCOLLO DI ESTRAZIONE COMPLETO
# ──────────────────────────────────────────────────────

## 6.1 — Pipeline Completa (Step-by-Step)

Quando il Workflow W1 viene attivato, esegui TUTTI questi step
nell'ordine indicato:
STEP 1: PRE-ANALISI (Sezione 1 di questo file)
│ → Valutazione rapida del materiale
│ → Decisione: estrazione completa / selettiva / segnalazione
│ → SE materiale ultra-lungo: dividi in sezioni
│
STEP 2: LETTURA ATTIVA (Sezione 2 di questo file)
│ → Leggi il materiale cercando i 5 tipi di contenuto
│ → Segna mentalmente ogni concetto candidato
│ → Stima il numero di framework estraibili
│
STEP 3: FILTRO ANTI-TEORIA (Sezione 3 di questo file)
│ → Per ogni concetto candidato, esegui il test anti-teoria
│ → Scarta i concetti puramente teorici
│ → Trasforma i concetti validi-ma-teorici in framework operativi
│ → Risultato: lista finale di concetti da formalizzare
│
STEP 4: CLASSIFICAZIONE (usa KB_01_LIBRARY_ARCHITECTURE.md)
│ → Per ogni concetto: identifica Area → Sottoarea → Argomento
│ → Assegna codice di classificazione
│ → Verifica che non esista già un framework simile in KB_08
│
STEP 5: GENERAZIONE SCHEDE (Sezione 4 di questo file)
│ → Per ogni concetto: compila la Scheda Framework Estratto
│ → Tutti i 9 campi obbligatori
│ → Genera ID univoco
│ → Verifica qualità di ogni campo (regole Sezione 4.3)
│
STEP 6: COLLEGAMENTO PROGETTI (usa KB_03_PROJECT_CONNECTION_MATRIX.md)
│ → Per ogni scheda: identifica progetto primario + fase
│ → Definisci situazione trigger
│ → Identifica progetti secondari se applicabile
│
STEP 7: DEFINIZIONE AZIONE (Sezione 5 di questo file)
│ → Per ogni scheda: definisci azione entro 7 giorni
│ → Verifica i 5 criteri di validità dell'azione
│ → Compila template azione (specifica, misurabile, temporale)
│
STEP 8: REGISTRAZIONE (usa KB_08_FRAMEWORKS_REGISTRY.md)
│ → Registra ogni scheda nel Framework Registry
│ → Status iniziale: ✅ Studiato ✅ Estratto □ Applicato □ Validato
│
STEP 9: OUTPUT ALL'UTENTE (usa KB_06_RESPONSE_TEMPLATES.md)
│ → Presenta le schede all'utente con il template W1
│ → Includi summary del materiale analizzato
│ → Includi eventuali segnalazioni (materiale teorico scartato,
│ contraddizioni con framework esistenti, gap identificati)

text



# ──────────────────────────────────────────────────────
# 📖 SEZIONE 7: GESTIONE CASI PARTICOLARI
# ──────────────────────────────────────────────────────

## 7.1 — Materiale che Contraddice Framework Esistenti
SE il nuovo materiale contiene un framework che CONTRADDICE
un framework già catalogato nel registro (KB_08):

→ NON scartare né il vecchio né il nuovo automaticamente
→ Segnala all'utente con questo formato:

"⚠️ CONTRADDIZIONE IDENTIFICATA

Framework esistente: [Nome] (ID: [ID])
Dice: [concetto A]

Nuovo framework: [Nome]
Dice: [concetto B — opposto/diverso]

Possibili spiegazioni:

Contesti diversi (il vecchio vale per X, il nuovo per Y)
Il nuovo è un aggiornamento/evoluzione del vecchio
Uno dei due è sbagliato
Suggerimento: [la tua analisi di quale è più affidabile e perché]
Decisione richiesta: Quale vuoi tenere come primario?"

text


## 7.2 — Materiale Duplicato
SE il materiale tratta argomenti per cui esistono GIÀ schede nel registro:

→ NON creare schede duplicate
→ Verifica se il nuovo materiale AGGIUNGE qualcosa:

Nuovi step al framework esistente? → AGGIORNA la scheda esistente
Nuovo esempio pratico? → AGGIUNGI alla scheda esistente
Prospettiva diversa ma compatibile? → CREA scheda separata con nota "complementare a [ID]"
Identico? → Non creare nulla, segnala: "Questo concetto è già
catalogato come [Nome Framework] (ID: [ID])"
text


## 7.3 — Materiale in Lingua non Italiana
SE il materiale è in inglese o altra lingua:

→ Analizza nella lingua originale (comprensione migliore)
→ GENERA le schede in ITALIANO
→ Mantieni i termini tecnici in inglese dove universalmente usati
(CTA, CRO, funnel, lead, etc.)
→ Nella scheda, campo FONTE: specifica la lingua originale
es. "Guida CRO Advanced — Neil Patel (EN)"

text


## 7.4 — Materiale Multi-Area
SE il materiale copre MULTIPLE aree della biblioteca
(es. un corso che parla sia di copywriting che di funnel):

→ Crea schede SEPARATE per ogni area
→ Ogni scheda ha la sua classificazione indipendente
→ Nella prima scheda, includi una nota:
"Questo materiale ha generato [N] schede in [N] aree diverse:

[Area X]: [Nome Framework 1]
[Area Y]: [Nome Framework 2]
..."
text


## 7.5 — Appunti Parziali dell'Utente
SE l'utente fornisce appunti parziali (non il materiale originale completo):

→ Estrai ciò che è possibile dagli appunti
→ SE i concetti sono incompleti (mancano step, mancano dettagli):

Segnala cosa manca
SE puoi integrare con la tua conoscenza: fallo, segnalando
"Step [N] integrato dall'AI — non presente negli appunti originali"
SE non puoi: chiedi all'utente di fornire il materiale completo
o di specificare i passaggi mancanti
text



# ──────────────────────────────────────────────────────
# 📖 SEZIONE 8: SEGNALAZIONI DI QUALITÀ POST-ESTRAZIONE
# ──────────────────────────────────────────────────────

## 8.1 — Dopo ogni estrazione, includi queste segnalazioni

Alla fine dell'output di estrazione, aggiungi SEMPRE:
─────────────────────────────────────────
📊 REPORT ESTRAZIONE

Materiale analizzato: [Nome fonte]
Lunghezza: [parole stimate]
Qualità operativa: [Alta/Media/Bassa]

Framework estratti: [N]
Concetti scartati (teorici): [N]
Concetti trasformati (teoria → framework): [N]

Aree coperte: [lista aree]
Progetti collegati: [lista progetti]
Azioni definite: [N] (tutte con scadenza entro 7 giorni)

Segnalazioni:

[Eventuali contraddizioni con framework esistenti]
[Eventuali gap nella biblioteca evidenziati]
[Eventuali suggerimenti di studio complementare]
[Eventuali parti del materiale non estraibili e perché]
─────────────────────────────────────────
text



# ──────────────────────────────────────────────────────
# 🔧 COME UTILIZZARE QUESTO FILE
# ──────────────────────────────────────────────────────

## Utilizzo da parte dell'AI:

1. **Quando il Workflow W1 viene attivato** (utente invia materiale):
   → Segui la pipeline completa della Sezione 6 dall'inizio alla fine
   → NON saltare nessuno step

2. **Quando generi schede framework**:
   → Usa il template esatto della Sezione 4.1
   → Compila TUTTI i 9 campi
   → Verifica le regole di compilazione della Sezione 4.3
   → Verifica i criteri di azione della Sezione 5.1

3. **Quando incontri casi particolari**:
   → Consulta la Sezione 7 per il caso specifico
   → Segui il protocollo indicato

4. **Quando concludi un'estrazione**:
   → Genera SEMPRE il Report Estrazione della Sezione 8.1


# ──────────────────────────────────────────────────────
# 🔗 COLLEGAMENTI
# ──────────────────────────────────────────────────────

- **Dipende da**: `KB_01_LIBRARY_ARCHITECTURE.md` (per classificazione)
- **Alimenta**: `KB_08_FRAMEWORKS_REGISTRY.md` (registra le schede create),
  `KB_06_RESPONSE_TEMPLATES.md` (formato output all'utente)
- **Usa anche**: `KB_03_PROJECT_CONNECTION_MATRIX.md` (per collegamento progetti)
- **Referenziato da**: Custom Instructions — Sezione 2.2 (sotto-processi),
  Sezione 8.1 (Workflow W1)


# ──────────────────────────────────────────────────────
# 💡 ESEMPIO PRATICO COMPLETO DI UTILIZZO
# ──────────────────────────────────────────────────────

## Scenario: L'utente invia un capitolo della "Guida Funnel Acquisizione Clienti"
## che parla di friction nei form di applicazione.

### Input utente:
"Analizza questo: [testo del capitolo sulla friction nei form]"

### Processo AI:

**STEP 1 — Pre-analisi:**
- Area: AREA_3 (Funnel & CRO)
- Livello: Avanzato
- Framework estraibili: Sì, stimati 2
- Lunghezza: ~2000 parole (media)
- Qualità operativa: Alta

**STEP 2 — Lettura attiva:**
- Concetto 1: Friction come strumento strategico (FRAMEWORK)
- Concetto 2: Routing automatico per qualità lead (PROCESSO)
- Concetto 3: "Il form non serve solo a raccogliere dati" (INSIGHT — verificare estraibilità)

**STEP 3 — Filtro anti-teoria:**
- Concetto 1: ✅ tutti i 5 criteri soddisfatti
- Concetto 2: ✅ tutti i 5 criteri soddisfatti
- Concetto 3: ❌ insight valido ma non step-by-step → TRASFORMA in framework
  → Diventa parte del Concetto 1 (integrato)

**STEP 4 — Classificazione:**
- Concetto 1: AREA_3 → 3A → 3A.03 (Form optimization)
- Concetto 2: AREA_3 → 3A → 3A.03 (Form optimization) — stessa sottoarea, framework diverso

**STEP 5 — Generazione Scheda (1 di 2):**
┌─────────────────────────────────────────────────────────────┐
│ 📋 SCHEDA FRAMEWORK ESTRATTO │
│ ID: A3_A_01_250615 │
├─────────────────────────────────────────────────────────────┤
│ │
│ ① FONTE: Guida Funnel Acquisizione Clienti (interno) │
│ │
│ ② DATA STUDIO: 15/06/2025 │
│ │
│ ③ CLASSIFICAZIONE: │
│ Area: AREA_3 — Funnel & Conversione (CRO) │
│ Sottoarea: 3A — Architettura Funnel │
│ Argomento: 3A.03 — Form optimization │
│ │
│ ④ CONCETTO CHIAVE: │
│ La friction nel form di applicazione è uno strumento │
│ STRATEGICO: aumenta il costo per lead ma migliora │
│ drasticamente qualità e conversion rate in vendita. │
│ │
│ ⑤ FRAMEWORK OPERATIVO: │
│ Nome: "Friction-Routing System" │
│ Step 1: Definisci i criteri di qualificazione del lead │
│ ideale (budget, settore, urgenza, dimensione) │
│ Step 2: Trasforma ogni criterio in una domanda-filtro │
│ da inserire nel form (max 5-7 domande totali) │
│ Step 3: Implementa routing automatico basato sulle │
│ risposte (lead qualificato → call / non │
│ qualificato → nurture sequence) │
│ Step 4: Configura il pixel per inviare feedback solo │
│ su lead qualificati (migliora signal) │
│ Step 5: Monitora e calibra: │
│ - Troppo costosi? → Riduci friction (meno domande)│
│ - Troppo scadenti? → Aumenta friction │
│ │
│ ⑥ ESEMPIO PRATICO: │
│ Landing page Digital Empire: aggiungere domanda │
│ "Qual è il tuo fatturato mensile?" con opzioni a │
│ scelta multipla. Lead che selezionano <5K€/mese → │
│ redirect a contenuto gratuito. Lead >5K€/mese → │
│ calendario prenotazione call. Risultato atteso: │
│ -30% lead totali ma +60% conversion rate in call. │
│ │
│ ⑦ COLLEGAMENTO PROGETTI: │
│ Progetto primario: ⚡ Agency Operations │
│ Fase specifica: Fase 1 — Acquisizione e Qualificazione │
│ Situazione trigger: Setup o ottimizzazione form di │
│ applicazione per lead generation │
│ Progetti secondari: 🎥 YouTube (landing lead magnet), │
│ 🧠 Strategy (qualità pipeline) │
│ │
│ ⑧ AZIONE ENTRO 7 GIORNI: │
│ AZIONE: Aggiungere 3 domande qualificanti al form di │
│ applicazione sul sito Digital Empire │
│ TEMPO STIMATO: 1 ora (scelta domande + implementazione) │
│ RISULTATO ATTESO: Form che filtra lead non qualificati │
│ SCADENZA: 22/06/2025 │
│ │
│ ⑨ STATUS: │
│ ✅ Studiato ✅ Estratto □ Applicato □ Validato │
│ Data ultimo aggiornamento: 15/06/2025 │
│ Note validazione: — │
│ │
└─────────────────────────────────────────────────────────────┘

text



# ──────────────────────────────────────────────────────
# ⚠️ NOTE E AVVERTENZE
# ──────────────────────────────────────────────────────

1. **La qualità dell'estrazione dipende dalla qualità del materiale.**
   Non forzare l'estrazione di framework da materiale scadente.
   Meglio segnalare "materiale non operativo" che creare schede deboli.

2. **Il filtro anti-teoria è CRITICO.** È la barriera che impedisce
   alla biblioteca di riempirsi di concetti inutili. Applicalo
   rigorosamente — è meglio avere 100 schede eccellenti che 500 mediocri.

3. **L'azione entro 7 giorni è OBBLIGATORIA.** Una scheda senza azione
   è una scheda incompleta. Non consegnare MAI una scheda con il campo ⑧ vuoto.

4. **L'ID è univoco e permanente.** Una volta assegnato, non cambia.
   Anche se la scheda viene aggiornata, l'ID resta lo stesso.

5. **Le schede sono VIVE.** Il campo ⑨ (Status) viene aggiornato nel tempo
   man mano che il framework viene applicato e validato. Le schede non sono
   "crea e dimentica" — sono strumenti che evolvono.