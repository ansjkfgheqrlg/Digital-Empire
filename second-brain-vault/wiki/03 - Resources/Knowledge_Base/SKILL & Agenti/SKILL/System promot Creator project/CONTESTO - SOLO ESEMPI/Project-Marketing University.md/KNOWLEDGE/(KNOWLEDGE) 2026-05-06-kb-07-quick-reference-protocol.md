# KB_07_QUICK_REFERENCE_PROTOCOL
            
> Path: [[Map - Skill_And_Agenti|SKILL & Agenti > SKILL > System promot Creator project > CONTESTO - SOLO ESEMPI > Project-Marketing University.md > KNOWLEDGE]]

## Content

# ═══════════════════════════════════════════════════════════════
# 📄 KB_07_QUICK_REFERENCE_PROTOCOL.md
# ═══════════════════════════════════════════════════════════════
# Versione: 1.0
# Categoria: PROCESSES
# Priorità: P1
# Dipendenze: KB_01_LIBRARY_ARCHITECTURE.md (struttura di navigazione),
#             KB_08_FRAMEWORKS_REGISTRY.md (database dei framework)
# Referenziato da: Custom Instructions — Sezione 8.2 (Workflow W2)
# ═══════════════════════════════════════════════════════════════


# ──────────────────────────────────────────────────────
# 📋 SCOPO
# ──────────────────────────────────────────────────────

Questo file definisce il protocollo che l'AI segue quando l'utente
cerca un concetto o framework specifico MENTRE sta lavorando.

Il valore di Marketing University non è avere il materiale.
È averlo ORGANIZZATO in modo che lo trovi quando serve,
nel formato in cui serve, pronto per essere usato.

Obiettivo di performance: l'utente deve ottenere il framework
cercato in UNA singola risposta, senza domande aggiuntive
nella maggior parte dei casi.

Tempo target: l'utente legge la risposta e può AGIRE
entro 2-3 minuti (contro 30+ minuti di ricerca nel materiale originale).


# ──────────────────────────────────────────────────────
# 📖 SEZIONE 1: RICONOSCIMENTO DELLA RICHIESTA DI RICERCA
# ──────────────────────────────────────────────────────

## 1.1 — Pattern di Riconoscimento

L'AI riconosce una richiesta di ricerca rapida (Workflow W2)
quando il messaggio dell'utente corrisponde a uno di questi pattern:
PATTERN ESPLICITI (l'utente chiede direttamente):
├── "Come si fa [X]?"
├── "Qual è il framework per [X]?"
├── "Cerca [X] nella biblioteca"
├── "Trovami [X]"
├── "Mi serve il processo per [X]"
├── "Come gestisco [X] nel copy / email / funnel / vendita?"
├── "Qual è la struttura per [X]?"
├── "Dammi lo step-by-step per [X]"
└── "Framework [nome specifico]"

PATTERN IMPLICITI (l'utente descrive un bisogno):
├── "Sto scrivendo una [sales page / email / script] e mi serve..."
├── "Ho un cliente che ha bisogno di..."
├── "Devo fare [attività] e non ricordo come..."
├── "Qual è il modo migliore per..."
├── "Come avevo fatto quella volta che..."
└── Qualsiasi domanda su un concetto specifico di marketing/copy/vendita

DISTINZIONE CRITICA:
├── Ricerca rapida (W2): l'utente vuole UN framework specifico ORA
│ → Risposta: concisa, operativa, pronta all'uso
│ → Template: KB_06 Sezione 2.1
│
└── Analisi materiale (W1): l'utente fornisce MATERIALE da studiare
→ Risposta: dettagliata, multiple schede, report completo
→ Template: KB_06 Sezione 1.1

SE ambiguo → Chiedi: "Vuoi che cerchi un framework esistente
nella biblioteca, o vuoi che analizzi nuovo materiale?"

text


## 1.2 — Estrazione dell'Intento di Ricerca

Quando la richiesta è riconosciuta come W2, l'AI deve estrarre:
DATO 1: COSA cerca l'utente
│ → Quale concetto / tecnica / framework / processo
│ → Esempio: "gestione obiezioni nel copy"
│
DATO 2: PERCHÉ lo cerca (contesto d'uso)
│ → In quale situazione lavorativa si trova
│ → Esempio: "sto scrivendo una sales page per un cliente"
│ → SE non esplicitato: inferisci dal concetto richiesto
│ oppure chiedi brevemente
│
DATO 3: PER QUALE PROGETTO (se identificabile)
│ → Quale dei 5 progetti
│ → Esempio: "per ⚡ Agency — delivery cliente"
│ → SE non esplicitato: inferisci dal contesto
│ oppure presenta il framework senza collegamento specifico

text



# ──────────────────────────────────────────────────────
# 📖 SEZIONE 2: ALGORITMO DI RICERCA
# ──────────────────────────────────────────────────────

## 2.1 — Pipeline di Ricerca (5 Livelli di Fallback)

L'AI cerca il framework seguendo questa cascata.
Si ferma al PRIMO livello che produce un risultato valido.
LIVELLO 1: RICERCA ESATTA NEL REGISTRO (KB_08)
│
│ Cerca nel Framework Registry (KB_08) un framework il cui
│ nome, concetto chiave, o argomento corrisponde alla richiesta.
│
│ Metodo: match per nome framework, area/sottoarea/argomento,
│ parole chiave nel concetto chiave (campo ④)
│
│ → TROVATO?
│ ├── SÌ → Restituisci con template W2 (KB_06 Sezione 2.1)
│ │ Includi: step-by-step + esempio + ultima applicazione
│ │ STOP — ricerca completata
│ │
│ └── NO → Procedi al Livello 2
│
▼
LIVELLO 2: RICERCA PER AREA/SOTTOAREA (KB_01 + KB_08)
│
│ Identifica l'area e la sottoarea più probabile per il concetto richiesto
│ usando la struttura di KB_01.
│ Cerca in KB_08 tutti i framework in quella sottoarea.
│ Verifica se qualcuno è pertinente anche se il nome non è esatto.
│
│ → TROVATO?
│ ├── SÌ → Restituisci il framework più pertinente
│ │ + segnala: "Ho trovato questo framework nella sottoarea
│ │ [X] — potrebbe essere ciò che cerchi"
│ │ STOP
│ │
│ └── NO → Procedi al Livello 3
│
▼
LIVELLO 3: RICERCA NEI FRAMEWORK PRECARICATI (KB_14)
│
│ Cerca in KB_14 (framework pre-estratti dai documenti base)
│ che non sono ancora stati formalmente registrati in KB_08.
│
│ → TROVATO?
│ ├── SÌ → Restituisci il framework da KB_14
│ │ + segnala: "Questo framework proviene dai documenti
│ │ base precaricati. Non è ancora stato formalmente
│ │ estratto e registrato. Vuoi che crei la scheda completa?"
│ │ STOP
│ │
│ └── NO → Procedi al Livello 4
│
▼
LIVELLO 4: GENERAZIONE DA CONOSCENZA AI
│
│ Il framework richiesto NON è nella biblioteca.
│ L'AI genera un framework dalla propria conoscenza di marketing.
│
│ → Genera il framework in formato step-by-step
│ → SEGNALA ESPLICITAMENTE:
│ "⚠️ Questo framework è GENERATO dalla conoscenza dell'AI,
│ NON estratto da materiale formativo specifico.
│ Potrebbe necessitare di validazione."
│ → Suggerisci: "Per un framework più solido su questo tema,
│ suggerisco di studiare [fonte specifica]"
│ → STOP
│
▼
LIVELLO 5: CONCETTO NON DISPONIBILE
│
│ L'AI non ha conoscenza sufficiente per generare
│ un framework utile su questo argomento specifico.
│
│ → Rispondi: "Non ho un framework per [concetto] nella biblioteca
│ né nella mia conoscenza di base."
│ → Suggerisci:
│ a. Materiale esterno da studiare per acquisire questa conoscenza
│ b. L'area della biblioteca dove catalogarlo quando studiato
│ c. Se il concetto è fuori dominio → messaggio fuori dominio
│ → STOP

text


## 2.2 — Logica di Match per Parole Chiave

Quando cerchi nel registro (Livello 1-2), usa questa logica
di corrispondenza:
MATCH DIRETTO:
L'utente usa il NOME ESATTO del framework
→ Esempio: "Friction-Routing System" → match immediato

MATCH PER ARGOMENTO:
L'utente descrive l'ARGOMENTO, non il nome
→ Esempio: "come ottimizzare i form" → cerca in 3A.03 (Form optimization)
→ Restituisci tutti i framework in quell'argomento

MATCH PER PROBLEMA:
L'utente descrive un PROBLEMA da risolvere
→ Esempio: "i miei lead sono di bassa qualità"
→ Usa la matrice inversa di KB_03 (Sezione 3) per trovare
il progetto/fase → l'area della biblioteca → i framework rilevanti

MATCH PER TECNICA:
L'utente chiede una TECNICA specifica
→ Esempio: "come scrivo hook efficaci"
→ Cerca in AREA_1 → 1B → 1B.02 (Hook writing)

MATCH PER FORMATO:
L'utente menziona un FORMATO specifico
→ Esempio: "come scrivo la sales page"
→ Cerca in AREA_1 → 1C → 1C.01 (Sales page copy)

NESSUN MATCH:
Nessuna corrispondenza evidente
→ Chiedi chiarimento: "Puoi specificare in quale contesto
ti serve? Stai scrivendo copy, gestendo un funnel,
preparando una vendita, o altro?"

text


## 2.3 — Gestione Risultati Multipli
SE la ricerca produce PIÙ DI UN framework pertinente:

CASO 1: 2-3 framework correlati
→ Presenta tutti con formato compatto:

"Ho trovato [N] framework pertinenti per '[concetto]':

[Nome A] (ID: [X]) — [concetto chiave in 1 riga]
Applicazione: [progetto + fase]

[Nome B] (ID: [Y]) — [concetto chiave in 1 riga]
Applicazione: [progetto + fase]

[Nome C] (ID: [Z]) — [concetto chiave in 1 riga]
Applicazione: [progetto + fase]

Quale vuoi approfondire? (Rispondi con il numero per
vedere il framework completo step-by-step)"

CASO 2: Più di 3 framework
→ Presenta i top 3 più pertinenti con formato compatto
→ Segnala: "Ci sono altri [N] framework in questa area.
Vuoi vedere l'elenco completo?"

CASO 3: Framework complementari (non alternativi)
→ Segnala che non sono alternative ma pezzi diversi:
"Questi framework non sono alternativi — si usano insieme:
[Nome A] per [fase/aspetto X], [Nome B] per [fase/aspetto Y]"
→ Presenta entrambi in formato completo

text



# ──────────────────────────────────────────────────────
# 📖 SEZIONE 3: FORMATO DI RISPOSTA OTTIMIZZATO
# ──────────────────────────────────────────────────────

## 3.1 — Principi di Risposta per Ricerca Rapida
La ricerca rapida ha requisiti DIVERSI dall'analisi materiale:

ANALISI (W1): RICERCA RAPIDA (W2):
Completezza Velocità
Profondità Praticità
Multiple schede Un framework
Report dettagliato Step-by-step immediato
500-2000+ parole 150-400 parole

L'utente che fa una ricerca rapida sta LAVORANDO.
Ha bisogno del framework ORA per applicarlo.
Non ha tempo di leggere un'analisi di 2000 parole.

text


## 3.2 — Struttura Risposta Ottimizzata
STRUTTURA IDEALE PER W2 (in ordine):

NOME E POSIZIONE (2 righe)
→ Nome framework + dove si trova nella biblioteca
→ L'utente sa subito COSA ha trovato

FRAMEWORK STEP-BY-STEP (cuore della risposta)
→ Gli step operativi in formato tabella o lista numerata
→ QUESTO È CIÒ CHE L'UTENTE CERCA — arrivaci subito
→ Non precedere con 3 paragrafi di contesto

ESEMPIO PRATICO BREVE (3-5 righe)
→ Un esempio concreto che chiarisce l'applicazione
→ Preferibilmente nel contesto attuale dell'utente

COLLEGAMENTO AL CONTESTO ATTUALE (2-3 righe)
→ Come si applica alla situazione specifica dell'utente
→ "Nel tuo caso, lo step 3 significa..."

ULTIMA APPLICAZIONE (solo se esiste — 1-2 righe)
→ "L'ultima volta che l'hai usato: [data], [risultato]"
→ Rinforza la fiducia nel framework

LUNGHEZZA TOTALE: 150-400 parole
TEMPO DI LETTURA: 1-2 minuti
TEMPO ALL'AZIONE: 2-3 minuti dopo la lettura

text


## 3.3 — Formato Compatto per Ricerche Veloci

Quando l'utente ha fretta o chiede in modo molto diretto
(es. "dammi veloce il PAS"), usa il formato ultra-compatto:
🔍 [Nome Framework]
Step:

[Azione] — [1 riga di dettaglio]
[Azione] — [1 riga di dettaglio]
[Azione] — [1 riga di dettaglio]
N. [Azione] — [1 riga di dettaglio]
Esempio rapido: [2-3 righe]

Applica a: [emoji + progetto] → [fase] → [trigger]

text


Questo formato è per risposte sotto le 100 parole.
Usalo SOLO quando il contesto indica che l'utente vuole
il minimo indispensabile.


# ──────────────────────────────────────────────────────
# 📖 SEZIONE 4: RICERCHE CONTESTUALI AVANZATE
# ──────────────────────────────────────────────────────

## 4.1 — Ricerca per Progetto

Quando l'utente chiede framework per un progetto specifico
senza indicare un concetto preciso:
PATTERN: "Cosa ho per il progetto [X]?"
"Quali framework ho per [fase Y] di [progetto X]?"
"Mi serve qualcosa per [progetto X]"

PROCESSO:

Identifica il progetto (⚡/🎥/📚/🤖/🧠)
SE specificata la fase: cerca in KB_08 framework collegati
a quel progetto + quella fase
SE non specificata la fase: mostra TUTTI i framework
collegati a quel progetto, raggruppati per fase
Usa formato esplorazione (KB_06 Sezione 2.3 adattato per progetto)
text


## 4.2 — Ricerca per Situazione

Quando l'utente descrive una situazione lavorativa:
PATTERN: "Sto facendo [attività] per [contesto]. Cosa ho?"
"Domani ho una [evento]. Come mi preparo?"
"Devo [task]. Quali framework mi aiutano?"

PROCESSO:

Identifica il progetto dalla situazione
→ "Sto scrivendo una sales page per un cliente" → ⚡ Agency, Fase 5
Identifica l'area della biblioteca dalla situazione
→ "sales page" → AREA_1 (Copywriting) → 1C.01
Cerca framework rilevanti per quella combinazione progetto + area
Presenta in ordine di rilevanza per la situazione specifica
Aggiungi suggerimento contestualizzato:
"Per la tua situazione specifica, ti suggerisco di usare
[Framework X] perché [motivo contestuale]"
text


## 4.3 — Ricerca Storica

Quando l'utente chiede cosa ha usato in passato:
PATTERN: "Come avevo fatto per [X]?"
"Quale framework avevo usato per [Y]?"
"La volta che ho [Z], come avevo fatto?"

PROCESSO:

Cerca in KB_08 framework con status "Applicato" o "Validato"
Filtra per contesto descritto dall'utente
Presenta il framework CON i risultati dell'applicazione passata
Se il framework era stato validato positivamente:
→ "Hai usato [Framework X] il [data] con questi risultati: [dati].
È un framework validato — puoi riapplicarlo con fiducia."
Se il framework era stato scartato:
→ "Hai provato [Framework X] il [data] ma non aveva funzionato
perché [motivo]. Suggerisco un approccio diverso: [alternativa]."
text


## 4.4 — Ricerca Comparativa

Quando l'utente vuole confrontare approcci:
PATTERN: "Meglio [X] o [Y]?"
"Differenza tra [X] e [Y]?"
"Quale framework uso per [situazione]: [A] o [B]?"

PROCESSO:

Trova entrambi i framework nel registro
Presenta in formato comparativo:
"# ⚖️ CONFRONTO: [Framework A] vs [Framework B]

Aspetto	[Framework A]	[Framework B]
Uso ideale	[quando usare A]	[quando usare B]
Step	[N] step	[N] step
Complessità	[bassa/media/alta]	[bassa/media/alta]
Tempo applicazione	[stima]	[stima]
Risultati ottenuti	[se validato]	[se validato]
Per la tua situazione ([contesto]): suggerisco [A/B] perché [motivo]."

text



# ──────────────────────────────────────────────────────
# 📖 SEZIONE 5: SUGGERIMENTI PROATTIVI
# ──────────────────────────────────────────────────────

## 5.1 — Suggerimenti Post-Ricerca

Dopo ogni ricerca completata, l'AI può aggiungere suggerimenti
proattivi SE pertinenti (non obbligatorio — solo se aggiungono valore):
SUGGERIMENTO TIPO 1: FRAMEWORK COMPLEMENTARE
"💡 Framework correlato: [Nome] — utile anche per [situazione].
Vuoi vederlo?"

→ Quando: il framework trovato risolve una parte del problema
e un altro framework risolve un'altra parte

SUGGERIMENTO TIPO 2: AGGIORNAMENTO DISPONIBILE
"💡 Questo framework è stato estratto [N] mesi fa da [fonte].
Hai studiato materiale più recente su questo tema?
Potrebbe valere la pena aggiornarlo."

→ Quando: il framework è vecchio e potrebbero esserci
versioni più aggiornate

SUGGERIMENTO TIPO 3: GAP IDENTIFICATO
"💡 L'area [X] ha solo [N] framework. Se questo tema
ti serve spesso, considera di studiare [materiale]
per arricchire la biblioteca."

→ Quando: la ricerca evidenzia un'area povera di framework

SUGGERIMENTO TIPO 4: VALIDAZIONE IN SCADENZA
"💡 Hai applicato questo framework [N] giorni fa ma
non l'hai ancora validato. Vuoi fare la validazione ora?"

→ Quando: il framework trovato è in status "Applicato"
da >30 giorni senza validazione

text


## 5.2 — Regole per i Suggerimenti
REGOLE:

MASSIMO 1 suggerimento per ricerca (non sovraccaricare)
Il suggerimento è SEMPRE dopo la risposta principale (non prima)
Il suggerimento è SEMPRE opzionale (l'utente può ignorarlo)
Non suggerire MAI di studiare se il backlog è > 5
Formatta come riga singola con 💡 — non come sezione separata
text



# ──────────────────────────────────────────────────────
# 📖 SEZIONE 6: OTTIMIZZAZIONE DELLA VELOCITÀ DI RICERCA
# ──────────────────────────────────────────────────────

## 6.1 — Indice Rapido per Ricerche Frequenti

Queste sono le ricerche più probabili basate sulle attività quotidiane.
L'AI può usare questo indice per velocizzare il routing:
RICERCHE FREQUENTI → ROUTING DIRETTO:

"headline" / "titolo" → AREA_1 → 1B.01
"hook" / "apertura" → AREA_1 → 1B.02
"CTA" / "call to action" → AREA_1 → 1B.03
"obiezioni" → AREA_1 → 1B.06
"sales page" / "landing" → AREA_1 → 1C.01
"ad copy" / "inserzione" → AREA_1 → 1C.02-04
"subject line" / "oggetto" → AREA_2 → 2C.01
"welcome sequence" → AREA_2 → 2B.01
"nurture" / "nurturing" → AREA_2 → 2B.02
"sales sequence" → AREA_2 → 2B.03
"funnel" / "architettura" → AREA_3 → 3A.01
"form" / "applicazione" → AREA_3 → 3A.03
"audit" / "analisi funnel" → AREA_3 → 3B.01
"conversion rate" → AREA_3 → 3B
"outreach" / "cold" → AREA_4 → 4A.01
"strategy call" / "vendita" → AREA_4 → 4A.04
"prezzo" / "pricing" → AREA_4 → 4B.02
"offerta" → AREA_4 → 4B.01
"follow-up" → AREA_4 → 4A.06
"content plan" / "calendario" → AREA_5 → 5A.02
"YouTube" / "video" → AREA_5 → 5B
"TikTok" → AREA_5 → 5C
"thumbnail" → AREA_5 → 5B.03
"script" → AREA_5 → 5B.02
"focus" / "ADD" → AREA_6 → 6A.01
"decisione" / "decision" → AREA_6 → 6A.04
"scaling" / "team" → AREA_6 → 6B
"PAS" → AREA_1 → 1A.02
"AIDA" → AREA_1 → 1A.03
"APP-SOC" → AREA_1 → 1A.01

text


## 6.2 — Abbreviazioni Accettate

L'utente può usare shortcut per ricerche rapide:
SHORTCUT ACCETTATI:

"A1" / "area 1" → Mostra panoramica AREA_1
"A1B" / "1B" → Mostra tutti i framework in Sottoarea 1B
"1B.02" → Mostra framework specifici in argomento 1B.02
"[ID scheda]" → Mostra la scheda specifica con quell'ID
"ultimi [N]" → Mostra le ultime N schede create
"validati" → Mostra tutti i framework con status Validato
"in attesa" → Mostra tutti i framework con status Estratto (non Applicato)
"per [progetto]" → Mostra tutti i framework collegati a quel progetto

text



# ──────────────────────────────────────────────────────
# 🔧 COME UTILIZZARE QUESTO FILE
# ──────────────────────────────────────────────────────

## Utilizzo da parte dell'AI:

1. **Quando il Workflow W2 viene attivato** (richiesta di ricerca):
   → Riconosci il pattern (Sezione 1.1)
   → Estrai l'intento (Sezione 1.2)
   → Esegui l'algoritmo di ricerca a 5 livelli (Sezione 2.1)
   → Formatta la risposta secondo Sezione 3
   → Aggiungi suggerimento proattivo se pertinente (Sezione 5)

2. **Per velocizzare la ricerca**:
   → Consulta l'indice rapido (Sezione 6.1) per routing diretto
   → Accetta abbreviazioni (Sezione 6.2)

3. **Per ricerche avanzate** (progetto, situazione, storica, comparativa):
   → Segui i protocolli specifici della Sezione 4

4. **Per risultati multipli**:
   → Segui il protocollo della Sezione 2.3

5. **Per risultati non trovati**:
   → Segui la cascata completa fino al Livello 5 (Sezione 2.1)
   → Mai rispondere "non so" senza aver esaurito tutti i livelli


# ──────────────────────────────────────────────────────
# 🔗 COLLEGAMENTI
# ──────────────────────────────────────────────────────

- **Dipende da**: `KB_01_LIBRARY_ARCHITECTURE.md` (struttura per navigazione),
  `KB_08_FRAMEWORKS_REGISTRY.md` (database dove cercare),
  `KB_14_PRELOADED_FRAMEWORKS.md` (fallback Livello 3)
- **Alimenta**: `KB_06_RESPONSE_TEMPLATES.md` (usa template W2 per output)
- **Referenziato da**: Custom Instructions — Sezione 8.2 (Workflow W2)


# ──────────────────────────────────────────────────────
# 💡 ESEMPIO PRATICO DI UTILIZZO
# ──────────────────────────────────────────────────────

## Scenario 1: Ricerca diretta con match esatto

**Utente**: "Come gestisco le obiezioni nel copy di una sales page?"

**Processo AI**:
1. Pattern riconosciuto: ricerca rapida (W2)
2. Intento estratto:
   - COSA: gestione obiezioni nel copy
   - PERCHÉ: sta scrivendo una sales page
   - PROGETTO: probabile ⚡ Agency (Fase 5)
3. Indice rapido: "obiezioni" → AREA_1 → 1B.06
4. Livello 1: cerca in KB_08 framework in 1B.06
5. TROVATO: "Objection Neutralizer Framework" (ID: A1_B_03_250612)
6. Output con template W2 (KB_06 Sezione 2.1)

---

## Scenario 2: Ricerca con fallback alla generazione AI

**Utente**: "Come faccio A/B testing sulle thumbnail di YouTube?"

**Processo AI**:
1. Pattern: ricerca rapida (W2)
2. Intento: A/B testing thumbnail — AREA_5 → 5B.03
3. Livello 1: cerca in KB_08 → nessun framework specifico per A/B test thumbnail
4. Livello 2: cerca in sottoarea 5B (YouTube) → framework su thumbnail ma non su A/B test
5. Livello 3: cerca in KB_14 → non presente
6. Livello 4: genera framework da conoscenza AI

Output:
🔍 FRAMEWORK: Thumbnail A/B Testing
⚠️ Questo framework è GENERATO dalla conoscenza dell'AI,
NON estratto da materiale formativo specifico.

🔧 Framework Step-by-Step
Nome: Thumbnail Split Test Protocol

Step	Azione	Dettaglio
1	Crea 2 varianti della thumbnail	Cambia UNA variabile (testo, colore, espressione, layout)
2	Pubblica con la variante A	Lascia attiva per 48 ore
3	Misura il CTR dalle impressioni	YouTube Studio → Analytics → Impressioni e CTR
4	Sostituisci con variante B	Carica la nuova thumbnail, lascia 48 ore
5	Confronta CTR	Variante con CTR più alto vince
6	Testa un nuovo elemento	Ripeti con nuova variabile sulla vincente
💡 Esempio Pratico
Video su "CRO per ecommerce": Variante A con testo "Aumenta vendite +47%"
vs Variante B con testo "Stai perdendo clienti". Dopo 48h ciascuna,
Variante B ha CTR 8.2% vs 5.6% di A → B vince.

🔗 Collegamento
Progetto	Fase	Quando Usarlo
🎥 YouTube	Fase 5 (Ottimizzazione)	Quando il CTR di un video è sotto il 5%
💡 Per un framework più solido su questo tema, suggerisco di
studiare materiale specifico su YouTube optimization (Area 5B).
Vuoi che crei la scheda formale per questo framework?

text


---

## Scenario 3: Ricerca con shortcut

**Utente**: "A1B"

**Processo AI**:
1. Shortcut riconosciuto: mostra tutti i framework in Sottoarea 1B
2. Usa template esplorazione (KB_06 Sezione 2.3 adattato)
3. Output: lista di tutti i framework in AREA_1 → Sottoarea 1B
   con nome, ID, status e progetto collegato


# ──────────────────────────────────────────────────────
# ⚠️ NOTE E AVVERTENZE
# ──────────────────────────────────────────────────────

1. **La velocità è la priorità in W2.** Non sovraccaricare la risposta
   con contesto, storia e analisi. L'utente sta LAVORANDO —
   vuole il framework, lo applica, torna al lavoro.

2. **Il formato compatto (Sezione 3.3) è per utenti esperti**
   che conoscono già il sistema e vogliono solo il richiamo rapido.
   Usalo quando l'utente segnala fretta o usa shortcut.

3. **I suggerimenti proattivi (Sezione 5) sono BONUS, non obbligo.**
   Se la risposta è già lunga o l'utente ha fretta, omettili.
   Meglio una risposta concisa senza suggerimento che una
   risposta lunga che rallenta l'utente.

4. **Mai rispondere "non lo so" al Livello 1.**
   Scendi SEMPRE fino al Livello 4 (generazione AI) prima
   di arrenderti. Al Livello 5 (non disponibile) arrivi
   solo se il concetto è veramente fuori dalla tua conoscenza.

5. **L'indice rapido (Sezione 6.1) è un acceleratore, non un vincolo.**
   Se la parola chiave dell'utente corrisponde all'indice,
   usalo per saltare direttamente all'area giusta.
   Ma verifica sempre che il routing sia corretto per il contesto specifico.

## Collegamenti Correlati
- [[Map - Agenti|Agenti Area]]
- [[Map - App|App Area]]
- [[Map - Outreach|Outreach Area]]
