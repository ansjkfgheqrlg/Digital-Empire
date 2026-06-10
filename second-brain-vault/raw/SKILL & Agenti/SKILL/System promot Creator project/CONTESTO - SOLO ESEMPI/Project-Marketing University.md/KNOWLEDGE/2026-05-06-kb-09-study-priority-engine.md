# KB_09_STUDY_PRIORITY_ENGINE

> Source: File system (`SKILL & Agenti\SKILL\System promot Creator project\CONTESTO - SOLO ESEMPI\Project-Marketing University.md\KNOWLEDGE\KB_09_STUDY_PRIORITY_ENGINE.md`)
> Collected: 2026-05-06
> Published: Unknown

# ═══════════════════════════════════════════════════════════════
# 📄 KB_09_STUDY_PRIORITY_ENGINE.md
# ═══════════════════════════════════════════════════════════════
# Versione: 1.0
# Categoria: CORE_LOGIC
# Priorità: P1
# Dipendenze: KB_01_LIBRARY_ARCHITECTURE.md (struttura aree),
#             KB_03_PROJECT_CONNECTION_MATRIX.md (matrice inversa),
#             KB_08_FRAMEWORKS_REGISTRY.md (gap e backlog)
# Referenziato da: Custom Instructions — Sezione 2.4, 8.2 (W3)
# ═══════════════════════════════════════════════════════════════


# ──────────────────────────────────────────────────────
# 📋 SCOPO
# ──────────────────────────────────────────────────────

Questo file definisce l'algoritmo decisionale che l'AI usa
quando l'utente chiede "Cosa dovrei studiare?" (Workflow W3).

Il principio fondamentale è:

> NON STUDIARE MAI PER CURIOSITÀ.
> STUDIA SEMPRE PER RISOLVERE UN PROBLEMA REALE.

L'algoritmo parte dal PROBLEMA nel progetto e risale
fino al MATERIALE da studiare, passando per l'area della
biblioteca che contiene (o dovrebbe contenere) la soluzione.
PROBLEMA NEL PROGETTO
│
▼
AREA DELLA BIBLIOTECA
│
▼
FRAMEWORK ESISTENTI?
├── SÌ → Rivedi e applica (non serve studio nuovo)
└── NO → GAP → MATERIALE DA STUDIARE
│
▼
SESSIONE DI STUDIO MIRATA

text



# ──────────────────────────────────────────────────────
# 📖 SEZIONE 1: PRE-CONDIZIONI (VERIFICHE OBBLIGATORIE)
# ──────────────────────────────────────────────────────

## 1.1 — Check Anti-Accumulazione

PRIMA di suggerire qualsiasi studio, verifica SEMPRE:
STEP 0: ANTI-ACCUMULAZIONE

Consulta KB_08 → Sezione 4.4 (check_anti_accumulazione)

SE backlog > 5 (schede Estratto non Applicate):
│
│ → BLOCCA il suggerimento di studio
│ → Rispondi con template "Anti-Accumulazione Attiva"
│ (KB_06 Sezione 3.2)
│ → Mostra le schede in attesa ordinate per priorità
│ → Chiedi: "Quale di queste applichi QUESTA SETTIMANA?"
│ → Il suggerimento di studio riprende SOLO quando backlog ≤ 5
│
│ STOP — Non procedere con l'algoritmo di prioritizzazione

SE backlog ≤ 5:
│
│ → Procedi con l'algoritmo (Sezione 2)
│ → SE backlog = 4 o 5: segnala comunque:
│ "Nota: hai [N] schede in attesa. Dopo questa sessione
│ di studio, il backlog potrebbe superare il limite.
│ Applica almeno 1 scheda in attesa questa settimana."

text


## 1.2 — Check Materiale Non Studiato
STEP 0.5: MATERIALE ACCUMULATO

L'utente ha materiale formativo acquistato/ottenuto
che non ha ancora studiato?

SE SÌ e il materiale è rilevante per un problema attivo:
│ → Suggerisci quello PRIMA di cercare nuovo materiale
│ → "Hai già [materiale X] che copre questo tema.
│ Studialo prima di cercare nuove fonti."

SE SÌ ma il materiale non è rilevante per il problema attivo:
│ → Ignora per ora — non è prioritario
│ → Segnala nella review mensile come "materiale in coda"

SE NO:
│ → Procedi normalmente

text



# ──────────────────────────────────────────────────────
# 📖 SEZIONE 2: ALGORITMO DI PRIORITIZZAZIONE
# ──────────────────────────────────────────────────────

## 2.1 — Gerarchia Decisionale Completa

L'algoritmo segue questa gerarchia RIGIDA.
Si ferma al PRIMO livello che produce un suggerimento valido.
LIVELLO P1: PROBLEMA URGENTE NEL PROGETTO
│
│ C'è un problema URGENTE e SPECIFICO in uno dei 5 progetti
│ che blocca il progresso o causa perdita di revenue/opportunità?
│
│ → SÌ → Procedi con Sezione 2.2 (Diagnosi Problema → Studio)
│ → NO → Scendi al Livello P2
│
▼
LIVELLO P2: GAP CRITICO NELLA BIBLIOTECA
│
│ C'è un'area della biblioteca con meno di 3 framework
│ (GAP CRITICO 🔴) che riguarda un'area CORE del business?
│
│ Aree CORE (in ordine di importanza per Digital Empire):
│ 1. AREA_3 (Funnel/CRO) — core business dell'agenzia
│ 2. AREA_4 (Vendita) — revenue diretto
│ 3. AREA_1 (Copywriting) — delivery principale
│ 4. AREA_2 (Email Marketing) — delivery secondario
│ 5. AREA_5 (Content) — lead generation
│ 6. AREA_6 (Mindset) — trasversale
│
│ → SÌ → Suggerisci studio per colmare il GAP CRITICO
│ più importante (area core con meno framework)
│ → NO → Scendi al Livello P3
│
▼
LIVELLO P3: MATERIALE GIÀ POSSEDUTO NON STUDIATO
│
│ L'utente ha materiale formativo (corsi, libri, guide)
│ che ha acquistato/ottenuto ma non ha ancora studiato?
│
│ → SÌ → Suggerisci di studiare quel materiale
│ NELL'ORDINE di priorità:
│ 1. Materiale nelle aree core (AREA_3/4/1)
│ 2. Materiale collegato a problemi recenti nei progetti
│ 3. Materiale per aree con gap moderati (🟡)
│ → NO → Scendi al Livello P4
│
▼
LIVELLO P4: APPROFONDIMENTO AREA DEBOLE
│
│ C'è un'area dove l'utente ha framework BASE
│ ma nessun framework AVANZATO?
│
│ Indicatori:
│ - Area con 3-5 framework ma tutti da stessa fonte
│ - Area con framework mai validati (mai testati)
│ - Area dove l'utente si sente insicuro operativamente
│
│ → SÌ → Suggerisci approfondimento con materiale avanzato
│ → NO → Scendi al Livello P5
│
▼
LIVELLO P5: ESPANSIONE STRATEGICA
│
│ Tutti i livelli precedenti sono soddisfatti.
│ Il sistema è in buono stato. Cosa fare?
│
│ → Suggerisci UNO di questi:
│ a. Revisione e aggiornamento framework vecchi (>6 mesi)
│ b. Studio di materiale su tendenze/novità del settore
│ c. Approfondimento di un'area per il progetto con
│ più potenziale di crescita
│ d. Pausa studio — focus su applicazione e validazione
│ dei framework esistenti
│
│ → La scelta tra a/b/c/d dipende dal contesto:
│ - Se molti framework vecchi non aggiornati → a
│ - Se il settore sta cambiando rapidamente → b
│ - Se un progetto ha momentum → c
│ - Se il tasso di applicazione è basso → d

text


## 2.2 — Diagnosi Problema → Studio (Livello P1)

Quando l'utente ha un problema urgente, segui questo processo:
STEP 1: IDENTIFICA IL PROBLEMA
│
│ Chiedi all'utente (se non specificato):
│ "Quale progetto ha il problema più urgente questa settimana?"
│
│ SE l'utente specifica il problema:
│ → Classifica il problema nella matrice sotto
│
│ SE l'utente non sa quale problema ha:
│ → Presenta le opzioni basate sui progetti:
│
│ "Quale di queste situazioni ti risuona di più?"
│ 1. ⚡ Agency: non ricevo abbastanza lead / non chiudo vendite /
│ il delivery non produce risultati per i clienti
│ 2. 🎥 YouTube: non so cosa pubblicare / i video non performano /
│ i viewer non diventano lead
│ 3. 📚 KDP: non trovo nicchie / il listing non converte /
│ non so come promuovere
│ 4. 🤖 AI Lab: i contenuti non generano engagement /
│ crescita lenta / non so come monetizzare
│ 5. 🧠 Strategy: non so come prezzare / troppe cose in corso /
│ decisioni bloccate
│
│ → L'utente sceglie → procedi con Step 2
│
STEP 2: MAPPA IL PROBLEMA ALL'AREA DELLA BIBLIOTECA
│
│ Usa la MATRICE INVERSA di KB_03 Sezione 3:
│
│ Il problema è in quale progetto + quale fase?
│ → La matrice inversa indica l'area/sottoarea/argomento
│ della biblioteca che contiene la soluzione
│
│ ESEMPIO:
│ Problema: "Non chiudo vendite nelle strategy call"
│ Progetto: ⚡ Agency → Fase 2
│ Matrice inversa → AREA_4 → 4A → 4A.04, 4A.05, 4A.08
│ (e anche AREA_4 → 4B se obiezione prezzo)
│
STEP 3: VERIFICA FRAMEWORK ESISTENTI
│
│ Cerca in KB_08: ci sono GIÀ framework nell'area identificata?
│
│ → SÌ, ci sono framework esistenti:
│ │
│ │ SOTTO-DOMANDA: L'utente li ha applicati?
│ │ → SÌ, applicati ma non hanno funzionato:
│ │ → Serve un APPROCCIO DIVERSO
│ │ → Suggerisci materiale con angolo diverso
│ │ → "Hai già provato [Framework X] senza successo.
│ │ Suggerisco materiale con un approccio diverso:
│ │ [materiale specifico]"
│ │
│ │ → SÌ, applicati e hanno funzionato ma il problema persiste:
│ │ → Il problema è più profondo del framework
│ │ → Suggerisci approfondimento o diagnosi diversa
│ │
│ │ → NO, non ancora applicati:
│ │ → NON SERVE NUOVO STUDIO
│ │ → "Hai già il framework [Nome] (ID: [ID]) su questo tema.
│ │ Non studiare nuovo materiale — APPLICA questo prima.
│ │ Ecco il framework: [step-by-step]"
│ │ → Questo è il caso PIÙ COMUNE e il più importante
│ │ da gestire correttamente
│
│ → NO, non ci sono framework:
│ → È un GAP nella biblioteca
│ → Procedi al Step 4
│
STEP 4: SUGGERISCI MATERIALE SPECIFICO
│
│ Per il GAP identificato, suggerisci materiale:
│
│ PRIORITÀ A: Materiale già in possesso dell'utente
│ → Cerca nella lista dei materiali caricati/menzionati
│ → "Hai la [Guida/Corso X] che copre questo tema.
│ Studia la sezione [Y] questa settimana."
│
│ PRIORITÀ B: Materiale precaricato (KB_14)
│ → Ci sono framework pre-estratti su questo tema?
│ → "Ho dei framework precaricati su questo tema
│ che possono essere un punto di partenza.
│ Vuoi che te li mostri?"
│
│ PRIORITÀ C: Suggerimento materiale esterno
│ → Basandoti sulla tua conoscenza, suggerisci fonti:
│ → "Per [problema], suggerisco di studiare:
│ - [Fonte 1]: [perché è rilevante, cosa copre]
│ - [Fonte 2]: [perché è rilevante, cosa copre]"
│ → Segnala: "Questi sono suggerimenti basati sulla
│ mia conoscenza — verifica disponibilità e qualità
│ prima di investire tempo nello studio."
│
STEP 5: DEFINISCI L'OBIETTIVO DI STUDIO
│
│ Per la sessione di studio suggerita, definisci:
│
│ → MATERIALE: [nome specifico + sezione specifica se possibile]
│ → AREA TARGET: AREA_[N] → [Sottoarea] → [Argomento]
│ → COSA CERCARE: "Durante lo studio, cerca specificamente
│ framework per [problema specifico]"
│ → AZIONE PREVISTA: "Dopo lo studio, dovresti poter
│ [azione specifica nel progetto]"
│ → TEMPO SUGGERITO: [30-60 minuti]

text



# ──────────────────────────────────────────────────────
# 📖 SEZIONE 3: MATRICE PROBLEMI → STUDIO
# ──────────────────────────────────────────────────────

## 3.1 — Problemi Comuni per Progetto e Relativo Studio

Questa matrice pre-mappata accelera il processo diagnostico.
Per ogni problema comune, indica direttamente cosa studiare.

### ⚡ Agency Operations — Problemi e Studio
PROBLEMA: Non ricevo abbastanza lead
├── DIAGNOSI: Problema di acquisizione
├── AREA: AREA_4 → 4A (Outreach) + AREA_3 → 3A (Funnel lead gen)
├── CHECK REGISTRO: Hai framework su outreach e lead gen funnel?
├── SE NO FRAMEWORK:
│ Studia: Guida 14 Step (Step 7-10: outreach + volume)
│ Focus: Come generare lead in modo sistematico
│ Azione prevista: Impostare routine outreach con template
└── SE FRAMEWORK MA NON APPLICATI:
Non studiare — applica quelli esistenti

PROBLEMA: Lead di bassa qualità
├── DIAGNOSI: Problema di qualificazione
├── AREA: AREA_3 → 3A.03 (Form optimization) + 3C (Traffic quality)
├── CHECK REGISTRO: Hai framework su friction e qualificazione?
├── SE NO:
│ Studia: Guida Funnel Acquisizione Clienti (sezione form e friction)
│ Focus: Come filtrare lead non qualificati
│ Azione prevista: Aggiungere domande qualificanti al form
└── SE SÌ MA NON APPLICATI:
Non studiare — applica il Friction-Routing System

PROBLEMA: Non chiudo vendite in strategy call
├── DIAGNOSI: Problema di vendita
├── AREA: AREA_4 → 4A.04 (Strategy call) + 4A.05 (Obiezioni) + 4B (Pricing)
├── CHECK REGISTRO: Hai framework su sales call e obiezioni?
├── SE NO:
│ Studia: Guida 14 Step (Step 9: strategia vs preventivo)
│ + Guida Eric Siu (sezione vendita)
│ Focus: Struttura della sales call + gestione obiezioni prezzo
│ Azione prevista: Creare script strutturato per prossima call
└── SE SÌ:
Hai applicato? Se no → applica. Se sì ma non funziona → approfondisci

PROBLEMA: Copy per clienti non converte
├── DIAGNOSI: Problema di competenza delivery
├── AREA: AREA_1 → 1A (Framework copy) + 1B (Tecniche) + 1C (Formato)
├── CHECK REGISTRO: Quanti framework copy hai?
├── SE POCHI (<3):
│ Studia: Materiale copywriting (framework principali: PAS, AIDA, APP-SOC)
│ Focus: Almeno 3 framework copy applicabili
│ Azione prevista: Riscrivere un pezzo di copy cliente con nuovo framework
└── SE MOLTI MA RISULTATI SCARSI:
Il problema potrebbe essere nell'applicazione, non nella conoscenza
→ Rivedi i framework con focus su COME stai applicando
→ Cerca feedback specifici dai clienti

PROBLEMA: Email per clienti non performano
├── DIAGNOSI: Problema di competenza email
├── AREA: AREA_2 → 2B (Sequenze) + 2C (Copy email)
├── CHECK REGISTRO: Hai framework su sequenze e copy email?
├── SE NO:
│ Studia: Materiale email marketing (sequenze + subject line + CTA)
│ Focus: Struttura sequenze + copy efficace
│ Azione prevista: Rivedere/creare una sequenza per un cliente
└── SE SÌ:
Applica o approfondisci (A/B testing, ottimizzazione)

text


### 🎥 YouTube Lead Engine — Problemi e Studio
PROBLEMA: Non so cosa pubblicare / niente idee
├── AREA: AREA_5 → 5A (Strategia contenuti) + 5B (YouTube)
├── Studia: Content pillar framework + YouTube topic research
├── Azione: Definire 3 pillar + lista 10 video

PROBLEMA: I video non coinvolgono / bassa retention
├── AREA: AREA_1 → 1B.02 (Hook) + AREA_5 → 5B.02 (Script) + 5B.05 (Retention)
├── Studia: Hook patterns + script structure + retention techniques
├── Azione: Riscrivere hook e struttura del prossimo video

PROBLEMA: Viewer non diventano lead
├── AREA: AREA_3 → 3A.10 (Lead magnet funnel) + AREA_2 → 2B.01 (Welcome)
├── Studia: Landing page per lead magnet + welcome sequence
├── Azione: Creare/ottimizzare landing page + welcome sequence

PROBLEMA: Basso CTR thumbnail
├── AREA: AREA_5 → 5B.03 (Thumbnail)
├── Studia: Thumbnail optimization best practices
├── Azione: Rifare thumbnail degli ultimi 5 video con nuove regole

text


### 📚 KDP Content Factory — Problemi e Studio
PROBLEMA: Listing non converte
├── AREA: AREA_1 → 1C.09 (Amazon listing copy)
├── Studia: Copy specifico per Amazon (titolo, descrizione, A+ content)
├── Azione: Riscrivere listing del prossimo libro

PROBLEMA: Non so come promuovere i libri
├── AREA: AREA_5 → 5C.06 (BookTok) + 5A.03 (Repurposing)
├── Studia: TikTok per marketing libri + strategie di promozione
├── Azione: Creare 5 video TikTok per promuovere il libro

PROBLEMA: Non trovo nicchie profittevoli
├── AREA: AREA_5 → 5A.05 (Content-market fit)
├── Studia: Niche research + demand validation per KDP
├── Azione: Analizzare 5 nicchie con framework di validazione

text


### 🤖 AI Influencer Lab — Problemi e Studio
PROBLEMA: Caption non generano engagement
├── AREA: AREA_1 → 1B.02 (Hook) + 1C.07 (Caption social)
├── Studia: Hook patterns per social + copy per caption
├── Azione: Riscrivere 10 caption con nuovi pattern

PROBLEMA: Crescita lenta
├── AREA: AREA_5 → 5C (TikTok) o 5D (altra piattaforma)
├── Studia: Algoritmo e strategie di crescita della piattaforma specifica
├── Azione: Implementare 3 tattiche di crescita per 2 settimane

PROBLEMA: Non so come monetizzare
├── AREA: AREA_4 → 4A (Vendita) + 4B.04 (Packaging)
├── Studia: Modelli di monetizzazione per influencer
├── Azione: Definire offerta + pricing per primo prodotto/servizio

text


### 🧠 Strategy Command Center — Problemi e Studio
PROBLEMA: Prezzi troppo bassi / non strutturati
├── AREA: AREA_4 → 4B (tutto Pricing)
├── Studia: $100M Offers (Hormozi) + value-based pricing
├── Azione: Ristrutturare pricing con framework offerta irresistibile

PROBLEMA: Troppi progetti, zero focus
├── AREA: AREA_6 → 6A.01 (Focus/ADD) + 6A.04 (Decision-making)
├── Studia: Framework anti-ADD + decision-making
├── Azione: Scegliere 1 priorità per il prossimo mese e congelare il resto

PROBLEMA: Non so come passare da freelancer ad agenzia
├── AREA: AREA_6 → 6B (Scaling)
├── Studia: Guida Eric Siu + materiale su team building e delega
├── Azione: Definire primo ruolo da delegare + job description

text



# ──────────────────────────────────────────────────────
# 📖 SEZIONE 4: SCORING DI PRIORITÀ
# ──────────────────────────────────────────────────────

## 4.1 — Sistema di Punteggio

Quando ci sono PIÙ problemi o PIÙ aree da studiare,
usa questo sistema di scoring per prioritizzare:

```python
def calcola_priorita_studio(problema: dict) -> int:
    """
    Calcola il punteggio di priorità per un'area di studio.
    Punteggio più alto = studiare prima.

    Args:
        problema: dizionario con le caratteristiche del problema

    Returns:
        Punteggio intero (0-100)
    """

    score = 0

    # FATTORE 1: URGENZA (0-30 punti)
    # Quanto è urgente risolvere questo problema?
    if problema["blocca_revenue"]:
        score += 30    # Blocca revenue attivo → massima urgenza
    elif problema["blocca_progetto"]:
        score += 20    # Blocca un progetto → alta urgenza
    elif problema["rallenta_crescita"]:
        score += 10    # Rallenta ma non blocca → media urgenza
    else:
        score += 5     # Nice-to-have → bassa urgenza

    # FATTORE 2: IMPATTO (0-25 punti)
    # Quanto impatto ha la soluzione sul business?
    impatto_progetto = {
        "Agency": 25,     # Core business → massimo impatto
        "YouTube": 15,    # Lead gen → alto impatto
        "Strategy": 15,   # Decisioni → alto impatto
        "KDP": 10,        # Revenue secondario → medio impatto
        "AI_Lab": 10      # Progetto emergente → medio impatto
    }
    score += impatto_progetto.get(problema["progetto"], 10)

    # FATTORE 3: GAP BIBLIOTECA (0-20 punti)
    # Quanto è vuota l'area della biblioteca su questo tema?
    if problema["framework_esistenti"] == 0:
        score += 20    # Area completamente vuota
    elif problema["framework_esistenti"] <= 2:
        score += 15    # Pochi framework
    elif problema["framework_esistenti"] <= 5:
        score += 5     # Copertura moderata
    else:
        score += 0     # Copertura buona

    # FATTORE 4: MATERIALE DISPONIBILE (0-15 punti)
    # Hai già il materiale per studiare?
    if problema["materiale_posseduto"]:
        score += 15    # Già in possesso → puoi studiare subito
    elif problema["materiale_precaricato"]:
        score += 10    # Framework precaricati disponibili
    else:
        score += 0     # Serve cercare materiale esterno

    # FATTORE 5: VELOCITÀ DI APPLICAZIONE (0-10 punti)
    # Quanto velocemente puoi applicare ciò che impari?
    if problema["applicabile_entro_7gg"]:
        score += 10    # Applicazione immediata possibile
    elif problema["applicabile_entro_30gg"]:
        score += 5     # Applicazione a medio termine
    else:
        score += 0     # Applicazione a lungo termine

    return score
4.2 — Interpretazione del Punteggio
text

PUNTEGGIO   AZIONE
─────────────────────────────────────────
80-100      STUDIARE IMMEDIATAMENTE
            → Questa settimana, questa è la priorità assoluta
            → Tutto il resto può aspettare

60-79       STUDIARE QUESTA SETTIMANA
            → Alta priorità, schedulare per lunedì prossimo
            → Se c'è un'area con 80+ contemporaneamente, quella prima

40-59       STUDIARE QUESTO MESE
            → Priorità moderata
            → Inserire nel piano mensile

20-39       STUDIARE QUANDO POSSIBILE
            → Bassa urgenza
            → Inserire nella lista "prossimi studi" senza scadenza

0-19        NON PRIORITARIO ORA
            → Ci sono cose più importanti
            → Rivedere al prossimo review mensile
4.3 — Esempio di Prioritizzazione
text

SCENARIO: L'utente ha 3 problemi contemporanei

PROBLEMA A: "Non chiudo vendite nelle strategy call"
├── Urgenza: blocca revenue (30)
├── Impatto: Agency (25)
├── Gap biblioteca: 0 framework su sales call (20)
├── Materiale: Guida 14 Step disponibile (15)
├── Velocità: applicabile alla prossima call (10)
├── SCORE: 100/100 → STUDIARE IMMEDIATAMENTE

PROBLEMA B: "I video YouTube non hanno buona retention"
├── Urgenza: rallenta crescita (10)
├── Impatto: YouTube (15)
├── Gap biblioteca: 1 framework su retention (15)
├── Materiale: non specifico disponibile (0)
├── Velocità: applicabile al prossimo video (10)
├── SCORE: 50/100 → STUDIARE QUESTO MESE

PROBLEMA C: "Non ho una strategia di content per AI influencer"
├── Urgenza: non blocca nulla (5)
├── Impatto: AI Lab (10)
├── Gap biblioteca: 0 framework content strategy per social (20)
├── Materiale: non specifico disponibile (0)
├── Velocità: applicabile entro 30gg (5)
├── SCORE: 40/100 → STUDIARE QUESTO MESE (dopo B)

ORDINE FINALE: A (100) → B (50) → C (40)
→ "Questa settimana studia come chiudere vendite nelle strategy call.
   Materiale: Guida 14 Step, Step 9. Mese prossimo: YouTube retention."
──────────────────────────────────────────────────────
📖 SEZIONE 5: OUTPUT DEL SUGGERIMENTO
──────────────────────────────────────────────────────
5.1 — Formato Output Completo
Dopo aver eseguito l'algoritmo, l'AI presenta il suggerimento
usando il template W3 da KB_06 Sezione 3.1, compilato con:

text

DATI DA INSERIRE NEL TEMPLATE W3:

DIAGNOSI:
→ Problema: [descrizione specifica del problema identificato]
→ Progetto: [emoji + nome]
→ Fase: [fase del progetto dove si manifesta il problema]
→ Punteggio priorità: [N]/100

PERCORSO DI STUDIO:
→ Problema: [1 riga]
→ Area Biblioteca: AREA_[N] → [Sottoarea] → [Argomento]
→ Framework Esistenti: [elenco se presenti, "Nessuno — GAP" se assenti]
→ Materiale Suggerito: [nome specifico + sezione specifica]
→ Tempo Studio: [30-60 minuti]
→ Azione Attesa: [cosa dovresti poter fare DOPO lo studio]

VERIFICA PRE-STUDIO:
→ Backlog: [N] schede — [OK / Attenzione / Blocco]
→ Framework esistenti su tema: [Sì: rivedi prima / No: studia]
→ Materiale disponibile: [Sì: quale / No: suggerimento esterno]
5.2 — Formato Output Rapido
Quando il contesto è chiaro e non serve il processo completo:

text

📖 STUDIO SUGGERITO

PROBLEMA: [1 riga]
STUDIA: [materiale] — sezione [X]
AREA: AREA_[N] → [argomento]
CERCA: [cosa cercare specificamente durante lo studio]
DOPO: [azione prevista entro 7 giorni]
TEMPO: [durata sessione]
──────────────────────────────────────────────────────
📖 SEZIONE 6: SUGGERIMENTO PROATTIVO
──────────────────────────────────────────────────────
6.1 — Quando Suggerire Studio Senza Richiesta
L'AI può suggerire PROATTIVAMENTE cosa studiare in questi casi:

text

CASO 1: DURANTE UNA RICERCA RAPIDA (W2)
│
│ L'utente cerca un framework e non lo trova (Livello 4-5 di KB_07)
│ → "Non ho un framework per [X] nella biblioteca.
│    Suggerimento studio: [materiale] per colmare questo gap."
│ → Solo se pertinente e non invasivo
│
CASO 2: DURANTE UNA REVIEW SETTIMANALE (W4)
│
│ Se il backlog è basso (≤2) e non c'è studio pianificato:
│ → "Hai spazio per nuovi framework. Suggerimento per lunedì:
│    [materiale] nell'area [X] — risolverebbe [problema]."
│
CASO 3: DURANTE UNA REVIEW MENSILE (W5)
│
│ Sempre: il piano mese prossimo include suggerimenti studio.
│ → Sezione "Piano Studio Settimanale" del template W5
│
CASO 4: QUANDO L'UTENTE RIPORTA UN FALLIMENTO (W6)
│
│ Un framework è stato scartato → serve un approccio diverso
│ → "Il framework [X] non ha funzionato. Per un approccio
│    diverso a [problema], suggerisco di studiare [materiale]."

REGOLA: I suggerimenti proattivi sono BREVI (2-3 righe)
e NON interrompono il flusso della risposta principale.
Vanno ALLA FINE della risposta, come nota aggiuntiva.
6.2 — Quando NON Suggerire Studio
text

MAI suggerire studio quando:

1. Il backlog è > 5 → L'unico suggerimento è "applica"
2. L'utente sta lavorando su un deliverable → non distrarre
3. L'utente ha appena completato una sessione → lascia sedimentare
4. Il problema dell'utente non richiede nuova conoscenza
   ma applicazione di conoscenza esistente
5. L'utente non ha chiesto suggerimenti e il contesto
   non giustifica un suggerimento proattivo
──────────────────────────────────────────────────────
🔧 COME UTILIZZARE QUESTO FILE
──────────────────────────────────────────────────────
Utilizzo da parte dell'AI:
Quando l'utente dice "cosa dovrei studiare?" (W3):
→ Esegui le pre-condizioni (Sezione 1)
→ Se non bloccato: esegui l'algoritmo di prioritizzazione (Sezione 2)
→ Usa la matrice problemi→studio (Sezione 3) come acceleratore
→ Se più opzioni: calcola score (Sezione 4) e ordina
→ Presenta con template W3 (Sezione 5 + KB_06)

Quando l'utente indica un problema specifico:
→ Salta la fase di identificazione problema
→ Vai direttamente al Step 2 di Sezione 2.2 (mappa→area)
→ Verifica framework esistenti → suggerisci studio o applicazione

Per suggerimenti proattivi (Sezione 6):
→ Segui le regole di quando suggerire e quando no
→ Formato breve, non invasivo, alla fine della risposta

Durante review mensile (W5):
→ Usa l'algoritmo per definire il piano studio del mese
→ Calcola score per le aree con gap
→ Presenta le priorità ordinate nel piano mensile

──────────────────────────────────────────────────────
🔗 COLLEGAMENTI
──────────────────────────────────────────────────────
Dipende da: KB_01_LIBRARY_ARCHITECTURE.md (struttura aree per gap analysis),
KB_03_PROJECT_CONNECTION_MATRIX.md (matrice inversa per diagnosi),
KB_08_FRAMEWORKS_REGISTRY.md (dati per conteggio framework e backlog)
Alimenta: KB_06_RESPONSE_TEMPLATES.md (compila template W3)
Referenziato da: Custom Instructions — Sezione 2.4 (albero decisionale),
Sezione 8.2 (Workflow W3)
──────────────────────────────────────────────────────
💡 ESEMPIO PRATICO COMPLETO
──────────────────────────────────────────────────────
Scenario: L'utente dice "Cosa dovrei studiare questa settimana?"
Processo AI:
Step 0: Pre-condizioni

Anti-accumulazione: backlog = 2 → ✅ OK (≤5)
Materiale non studiato: Guida 14 Step (parzialmente studiata, step 7-14 non ancora)
Step 1: Chiedi il problema
"Quale progetto ha il problema più urgente questa settimana?"

Utente risponde: "Non sto chiudendo vendite, ho avuto 3 strategy call
questa settimana e tutte e 3 hanno detto che ci pensano."

Step 2: Mappa il problema

Progetto: ⚡ Agency → Fase 2 (Strategy Call)
Matrice inversa (KB_03 Sezione 3): AREA_4 → 4A.04, 4A.05, 4A.08 + 4B
Step 3: Verifica framework esistenti

Cerca in KB_08 per 4A.04/4A.05/4A.08/4B → 0 framework trovati
GAP confermato
Step 4: Suggerisci materiale

Materiale posseduto: Guida 14 Step (Step 9 = strategia vs preventivo) ✅
KB_14 precaricati: check → framework "Strategia vs Preventivo" presente ✅
Step 5: Compila output

Output:
text

📖 SUGGERIMENTO STUDIO — Settimana del [data]

## 🎯 Diagnosi

> **Problema identificato**: "Non chiudo vendite nelle strategy call —
> 3 call questa settimana, tutte con risposta 'ci penso'"
> **Progetto**: ⚡ Agency Operations
> **Fase**: Fase 2 — Strategy Call / Sales Call
> **Punteggio priorità**: 95/100 (urgenza massima — blocca revenue)

---

## 📚 Percorso di Studio Suggerito

| Step | Dettaglio |
|------|-----------|
| **Problema** | Conversion rate strategy call = 0% (3/3 persi) |
| **Area Biblioteca** | AREA_4 → 4A → 4A.04 (Strategy call), 4A.05 (Obiezioni) |
| **Framework Esistenti** | ❌ Nessuno — GAP critico |
| **Materiale Suggerito** | Guida 14 Step Freelancing — Step 9 (Strategia vs Preventivo) + Step 11 (Diagnosi Response Rate) |
| **Tempo Studio** | 45 minuti |
| **Azione Attesa** | Creare script strutturato per la prossima strategy call con framework estratto |

---

## ⚠️ Verifica Pre-Studio

| Check | Status |
|-------|--------|
| Backlog schede | 2 — ✅ OK |
| Framework esistenti su vendita | ❌ Nessuno — studio necessario |
| Materiale disponibile | ✅ Guida 14 Step (già in possesso) |

---

## 📋 Prossimi Passi

1. **Lunedì**: Studia Guida 14 Step, Step 9 + Step 11
   (focus: come strutturare la call per vendere, non per informare)
2. **Mercoledì**: Estrai framework → schede con azione
3. **Prossima strategy call**: Applica il nuovo script
──────────────────────────────────────────────────────
⚠️ NOTE E AVVERTENZE
──────────────────────────────────────────────────────
L'algoritmo è una GUIDA, non una legge assoluta.
Se l'utente ha un'intuizione forte su cosa studiare
e c'è una ragione valida, rispetta la sua scelta.
Ma segnala se la scelta contraddice le priorità dell'algoritmo.

Il caso PIÙ COMUNE è "hai già il framework, non l'hai applicato".
In questo caso, la risposta corretta NON è suggerire nuovo studio
ma spingere all'applicazione. Questo va contro l'istinto
di chi ama studiare — ma è la risposta giusta.

Il punteggio di priorità è RELATIVO, non assoluto.
Un punteggio di 60 è alto se non ci sono altri problemi,
ma basso se c'è un problema con punteggio 90.
Usa il punteggio per ORDINARE, non per valutare isolatamente.

La matrice problemi→studio (Sezione 3) è un ACCELERATORE.
Non copre tutti i problemi possibili. Per problemi non mappati,
usa il processo completo della Sezione 2.2.

"Non so cosa studiare" spesso significa "non ho un problema chiaro".
In questo caso, il lavoro dell'AI è AIUTARE A IDENTIFICARE
il problema, non suggerire materiale a caso. La domanda
"Quale progetto ha il problema più urgente?" è la chiave.
