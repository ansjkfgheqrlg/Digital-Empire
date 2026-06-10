# KB_08_FRAMEWORKS_REGISTRY

> Source: File system (`System OMEGA - Creazione proggetti e skill per Claude\System promot Creator project\CONTESTO - SOLO ESEMPI\Project-Marketing University.md\KNOWLEDGE\KB_08_FRAMEWORKS_REGISTRY.md`)
> Collected: 2026-05-06
> Published: Unknown

# ═══════════════════════════════════════════════════════════════
# 📄 KB_08_FRAMEWORKS_REGISTRY.md
# ═══════════════════════════════════════════════════════════════
# Versione: 1.0
# Categoria: DATA_HANDLING
# Priorità: P0
# Dipendenze: KB_01_LIBRARY_ARCHITECTURE.md (struttura classificazione),
#             KB_02_EXTRACTION_ENGINE.md (processo che genera le schede)
# Referenziato da: Custom Instructions — Sezione 2.2, 5.2,
#                  Workflow W1 (Step 8), W2, W4, W5, W6
# ═══════════════════════════════════════════════════════════════


# ──────────────────────────────────────────────────────
# 📋 SCOPO
# ──────────────────────────────────────────────────────

Questo file è il REGISTRO CENTRALIZZATO di tutti i framework
estratti nel sistema Marketing University.

Funziona come un database: ogni framework estratto viene
registrato qui con il suo ID, stato, classificazione e
collegamento al progetto. L'AI consulta questo file per:

1. RICERCA (W2): trovare framework per l'utente
2. TRACKING (W4/W5): monitorare status e progressi
3. STATISTICHE (W5): calcolare KPI mensili
4. DEDUPLICAZIONE (W1): verificare che un framework non sia già registrato
5. VALIDAZIONE (W6): aggiornare lo status dopo applicazione/validazione

NOTA IMPORTANTE SULLA NATURA DI QUESTO FILE:
Questo file contiene la STRUTTURA e le ISTRUZIONI per il registro.
I dati reali (le schede framework) vengono accumulati nelle
conversazioni del progetto. L'AI mantiene la consapevolezza
delle schede create durante le conversazioni attive e usa
questo file come schema di riferimento per la struttura dei dati.

Quando l'utente carica materiale e l'AI estrae framework,
le schede vengono presentate nel formato definito qui.
Per consultazioni future, l'AI si riferisce alle schede
create nelle conversazioni precedenti e a KB_14 (precaricati).


# ──────────────────────────────────────────────────────
# 📖 SEZIONE 1: STRUTTURA DEL REGISTRO
# ──────────────────────────────────────────────────────

## 1.1 — Schema del Record

Ogni framework nel registro ha questa struttura dati:

```python
class FrameworkRecord:
    """
    Schema di un singolo record nel Framework Registry.
    Ogni framework estratto genera un record con questi campi.
    """

    def __init__(self):
        # IDENTIFICAZIONE
        self.id: str = ""                    # ID univoco (es. A1_B_03_250615)
        self.nome: str = ""                  # Nome del framework
        self.fonte: str = ""                 # Da dove è stato estratto

        # CLASSIFICAZIONE
        self.area: str = ""                  # AREA_1 a AREA_6
        self.area_nome: str = ""             # Nome dell'area
        self.sottoarea: str = ""             # XA a XD
        self.sottoarea_nome: str = ""        # Nome della sottoarea
        self.argomento: str = ""             # Codice argomento (es. 1B.06)
        self.argomento_nome: str = ""        # Nome dell'argomento

        # CONTENUTO
        self.concetto_chiave: str = ""       # 1-2 righe
        self.num_step: int = 0               # Numero di step nel framework
        self.step_list: list = []            # Lista degli step (sintesi)

        # COLLEGAMENTO
        self.progetto_primario: str = ""     # Emoji + nome progetto
        self.fase_primaria: str = ""         # Fase del progetto
        self.trigger: str = ""               # Quando usarlo
        self.progetti_secondari: list = []   # Altri progetti

        # AZIONE
        self.azione_7gg: str = ""            # Azione definita
        self.tempo_stimato: str = ""         # Tempo per l'azione
        self.scadenza_azione: str = ""       # Data scadenza

        # STATUS
        self.status: str = ""               # Studiato/Estratto/Applicato/Validato/Insegnato
        self.data_creazione: str = ""        # GG/MM/AAAA
        self.data_applicazione: str = ""     # GG/MM/AAAA (se applicato)
        self.data_validazione: str = ""      # GG/MM/AAAA (se validato)
        self.risultato_validazione: str = "" # Positivo/Negativo/Esteso
        self.note: str = ""                 # Note libere

        # METADATI
        self.qualita_materiale: str = ""     # Alta/Media/Bassa
        self.derivato: bool = False          # True se teoria trasformata in framework
        self.contraddizioni: list = []       # ID di framework che contraddice
1.2 — Sistema di Generazione ID
text

FORMATO: [AREA]_[SOTTOAREA]_[NUMERO]_[YYMMDD]

COMPONENTI:
- AREA:       A1 / A2 / A3 / A4 / A5 / A6
- SOTTOAREA:  A / B / C / D
- NUMERO:     01, 02, 03... (progressivo dentro area+sottoarea)
- DATA:       YYMMDD (data di creazione)

REGOLE:
1. Il numero è progressivo PER COMBINAZIONE area+sottoarea
   → A1_B potrebbe avere 01, 02, 03...
   → A1_C ha la sua numerazione separata 01, 02...
2. L'ID è PERMANENTE — non cambia mai dopo l'assegnazione
3. Se un framework viene scartato, il suo ID NON viene riassegnato
4. Se un framework viene aggiornato, mantiene lo stesso ID
   con nota "Aggiornato il [data]"

ESEMPI:
A1_A_01_250615  → Area 1, Sottoarea A, primo framework, 15/06/2025
A1_B_03_250618  → Area 1, Sottoarea B, terzo framework, 18/06/2025
A3_A_01_250615  → Area 3, Sottoarea A, primo framework, 15/06/2025
A4_B_02_250620  → Area 4, Sottoarea B, secondo framework, 20/06/2025
1.3 — Indice di Stato
I possibili status e le loro transizioni:

text

DIAGRAMMA TRANSIZIONI DI STATO:

                    ┌──────────────────────┐
                    │                      │
                    ▼                      │
┌──────────┐    ┌──────────┐    ┌──────────┐
│ STUDIATO │───▶│ ESTRATTO │───▶APPLICATO │
└──────────┘    └────┬─────┘    └────┬─────┘
                     │               │
                     │               ├──────────────┐
                     │               │              │
                     │               ▼              ▼
                     │          ┌──────────┐   ┌──────────┐
                     │          │ VALIDATO │   │ SCARTATO │
                     │          └────┬─────┘   └──────────┘
                     │               │
                     │               ▼
                     │          ┌──────────┐
                     │          │INSEGNATO │
                     │          └──────────┘
                     │
                     ├──────────────┐
                     │              │
                     ▼              ▼
                ┌──────────┐  ┌──────────┐
                │ IN PAUSA │  │DA RIVEDERE│
                └──────────┘  └──────────┘

CODICI STATUS:
✅✅□□□  = Studiato + Estratto
✅✅✅□□  = Studiato + Estratto + Applicato
✅✅✅✅□  = Studiato + Estratto + Applicato + Validato
✅✅✅✅✅  = Studiato + Estratto + Applicato + Validato + Insegnato
⏸️       = In Pausa (congelato temporaneamente)
❌       = Scartato (testato, non funziona)
🔄       = Da Rivedere (necessita revisione)
──────────────────────────────────────────────────────
📖 SEZIONE 2: TABELLE DEL REGISTRO
──────────────────────────────────────────────────────
2.1 — Tabella Master (Indice Completo)
Questa è la struttura della tabella master che l'AI mantiene
mentalmente e aggiorna durante le conversazioni:

text

REGISTRO FRAMEWORK — TABELLA MASTER
═══════════════════════════════════════════════════════════════════

| ID | Nome Framework | Area | Sotto | Arg. | Fonte | Progetto | Status | Data | Note |
|----|---------------|------|-------|------|-------|----------|--------|------|------|
| [ID] | [Nome] | A[N] | [X] | [cod] | [fonte] | [emoji] | [status] | [data] | [note] |

═══════════════════════════════════════════════════════════════════
2.2 — Tabelle per Viste Specifiche
L'AI genera viste filtrate della tabella master
a seconda del tipo di richiesta:

Vista per AREA (usata in W2 — esplorazione area):
text

REGISTRO — AREA_[N]: [Nome Area]
═══════════════════════════════════════

SOTTOAREA [XA] — [Nome]
| ID | Nome | Status | Progetto | Data |
|----|------|--------|----------|------|

SOTTOAREA [XB] — [Nome]
| ID | Nome | Status | Progetto | Data |
|----|------|--------|----------|------|

SOTTOAREA [XC] — [Nome]
| ID | Nome | Status | Progetto | Data |
|----|------|--------|----------|------|

SOTTOAREA [XD] — [Nome]
| ID | Nome | Status | Progetto | Data |
|----|------|--------|----------|------|

TOTALE AREA: [N] framework | [N] validati | [N] in attesa
Vista per PROGETTO (usata in W2 — ricerca per progetto):
text

REGISTRO — PROGETTO: [emoji] [Nome Progetto]
═══════════════════════════════════════

| Fase | ID | Nome Framework | Area | Status | Data |
|------|----|---------------|------|--------|------|
| Fase 1 | [ID] | [Nome] | A[N] | [status] | [data] |
| Fase 1 | [ID] | [Nome] | A[N] | [status] | [data] |
| Fase 2 | [ID] | [Nome] | A[N] | [status] | [data] |
| ... | ... | ... | ... | ... | ... |

TOTALE PROGETTO: [N] framework | [N] validati
Vista per STATUS (usata in W4/W5 — review):
text

REGISTRO — FILTRO: [Status]
═══════════════════════════════════════

[SE status = "Estratto non Applicato" (backlog):]
| # | ID | Nome | Progetto | Azione | Scadenza | Giorni Attesa |
|---|----|------|----------|--------|----------|---------------|
| 1 | [ID] | [Nome] | [emoji] | [azione] | [data] | [N] |

TOTALE: [N] framework in attesa
⚠️ Anti-accumulazione: [✅ ≤5 / ⚠️ >5 — BLOCCO STUDIO]

[SE status = "Applicato non Validato" (>30gg):]
| # | ID | Nome | Progetto | Applicato il | Giorni da Applicazione |
|---|----|------|----------|-------------|----------------------|
| 1 | [ID] | [Nome] | [emoji] | [data] | [N] |

TOTALE: [N] framework da validare

[SE status = "Validato":]
| # | ID | Nome | Progetto | Risultato | Processo Standard? |
|---|----|------|----------|-----------|-------------------|
| 1 | [ID] | [Nome] | [emoji] | [positivo/negativo] | [Sì/No] |

TOTALE: [N] framework validati | [N] positivi | [N] negativi
Vista TEMPORALE (usata in W4 — review settimanale):
text

REGISTRO — SETTIMANA DEL [data]
═══════════════════════════════════════

CREATI QUESTA SETTIMANA:
| ID | Nome | Area | Progetto | Azione | Scadenza |
|----|------|------|----------|--------|----------|

APPLICATI QUESTA SETTIMANA:
| ID | Nome | Progetto | Risultato Immediato |
|----|------|----------|---------------------|

VALIDATI QUESTA SETTIMANA:
| ID | Nome | Verdetto | Risultato |
|----|------|----------|-----------|

RISCHEDULATI:
| ID | Nome | Motivo | Nuova Scadenza |
|----|------|--------|----------------|
──────────────────────────────────────────────────────
📖 SEZIONE 3: OPERAZIONI SUL REGISTRO
──────────────────────────────────────────────────────
3.1 — CREATE: Aggiunta Nuovo Framework
text

TRIGGER: Workflow W1, Step 8 (dopo generazione scheda)
PROCESSO:

1. Verifica che l'ID non esista già
   → SE esiste: errore di generazione ID, assegna nuovo numero
2. Verifica che il framework non sia un duplicato
   → Cerca per nome simile + area simile
   → SE trovato framework simile:
     a. È lo stesso? → Non creare, segnala duplicato
     b. È complementare? → Crea con nota "Complementare a [ID]"
     c. È un aggiornamento? → Aggiorna l'esistente, non creare nuovo
3. Registra il nuovo record con tutti i campi
4. Status iniziale: ✅ Studiato ✅ Estratto
5. Conferma: "Framework [Nome] registrato con ID [ID]"
3.2 — READ: Lettura / Ricerca Framework
text

TRIGGER: Workflow W2 (ricerca), W4/W5 (review)
PROCESSO:

PER RICERCA SINGOLA:
1. Ricevi la query di ricerca dall'utente
2. Segui l'algoritmo di ricerca in KB_07 Sezione 2.1
3. Cerca match nel registro per: nome, area, argomento, parole chiave
4. Restituisci con formato appropriato (KB_06)

PER VISTA FILTRATA:
1. Identifica il tipo di vista richiesta (area, progetto, status, temporale)
2. Filtra i record secondo i criteri
3. Presenta nella tabella appropriata (Sezione 2.2)

PER STATISTICHE:
1. Conta i record per status, area, progetto
2. Calcola KPI (KB_04 Sezione 7.1)
3. Presenta nel template review (KB_06 Sezione 5)
3.3 — UPDATE: Aggiornamento Framework Esistente
text

TRIGGER: Workflow W6 (validazione), aggiornamento manuale, applicazione

OPERAZIONI DI UPDATE PERMESSE:

UPDATE STATUS (più comune):
├── Estratto → Applicato
│   Campi aggiornati: status, data_applicazione, note
│   Richiede: Report di Applicazione (KB_04 Sezione 4.3)
│
├── Applicato → Validato
│   Campi aggiornati: status, data_validazione, risultato_validazione, note
│   Richiede: Report di Validazione (KB_04 Sezione 5.3)
│
├── Validato → Insegnato
│   Campi aggiornati: status, note (canale e tipo contenuto)
│   Richiede: Brief per il progetto destinazione
│
├── Qualsiasi → In Pausa
│   Campi aggiornati: status, note (motivo pausa)
│   Richiede: Motivo specifico della pausa
│
├── Qualsiasi → Scartato
│   Campi aggiornati: status, note (motivo scarto, lezione appresa)
│   Richiede: Analisi del fallimento
│
└── Qualsiasi → Da Rivedere
    Campi aggiornati: status, note (cosa rivedere)
    Richiede: Motivo della revisione

UPDATE CONTENUTO (meno comune):
├── Aggiunta step al framework
│   → Quando l'applicazione rivela step mancanti
│   → Nota: "Step [N] aggiunto il [data] — scoperto durante applicazione"
│
├── Modifica esempio
│   → Quando un esempio migliore è disponibile dall'esperienza diretta
│
├── Aggiornamento collegamento progetto
│   → Quando il framework si rivela utile per un progetto diverso
│
└── Correzione classificazione
    → Quando la classificazione originale era errata
    → L'ID NON cambia — solo i campi di classificazione
3.4 — DELETE: Rimozione Framework
text

REGOLA: I framework NON vengono MAI cancellati dal registro.

INVECE DI CANCELLARE:
- Framework che non funziona → Status: ❌ Scartato
  (con nota sul perché — la lezione appresa ha valore)
- Framework ridondante → Status: 🔄 Da Rivedere
  (con nota "Potenzialmente duplicato di [ID]")
- Framework obsoleto → Status: ⏸️ In Pausa
  (con nota "Superato da [ID] / non più rilevante dal [data]")

RAZIONALE:
Anche i framework scartati contengono LEZIONI APPRESE.
Sapere cosa NON funziona è conoscenza preziosa.
Il registro è un archivio COMPLETO della storia di apprendimento.
──────────────────────────────────────────────────────
📖 SEZIONE 4: QUERY PREDEFINITE
──────────────────────────────────────────────────────
4.1 — Query Standard per Review Settimanale (W4)
Python

def review_settimanale(settimana_corrente: str) -> dict:
    """
    Query predefinite per la review settimanale.
    Eseguite automaticamente quando l'utente dice "review settimanale".

    Args:
        settimana_corrente: data di inizio settimana (GG/MM/AAAA)

    Returns:
        Dizionario con tutti i dati necessari per il template W4
    """

    results = {
        # Framework creati questa settimana
        "creati_settimana": query(
            filtro="data_creazione >= settimana_corrente",
            campi=["id", "nome", "area", "progetto", "azione_7gg", "scadenza_azione"]
        ),

        # Framework con azione scaduta (>7gg senza applicazione)
        "azioni_scadute": query(
            filtro="status == 'Estratto' AND scadenza_azione < oggi",
            campi=["id", "nome", "progetto", "azione_7gg", "scadenza_azione", "giorni_ritardo"]
        ),

        # Framework applicati questa settimana
        "applicati_settimana": query(
            filtro="data_applicazione >= settimana_corrente",
            campi=["id", "nome", "progetto", "risultato_immediato"]
        ),

        # Backlog totale
        "backlog": query(
            filtro="status == 'Estratto'",
            conteggio=True
        ),

        # Framework da validare (applicati >30gg fa)
        "da_validare": query(
            filtro="status == 'Applicato' AND data_applicazione < (oggi - 30gg)",
            campi=["id", "nome", "progetto", "data_applicazione", "giorni_da_applicazione"]
        )
    }

    return results
4.2 — Query Standard per Review Mensile (W5)
Python

def review_mensile(mese_corrente: str) -> dict:
    """
    Query predefinite per la review mensile.
    Eseguite automaticamente quando l'utente dice "review mensile".

    Args:
        mese_corrente: mese in formato MM/AAAA

    Returns:
        Dizionario con tutti i dati necessari per il template W5
    """

    results = {
        # STATISTICHE MESE
        "creati_mese": query(
            filtro="data_creazione nel mese_corrente",
            conteggio=True
        ),
        "applicati_mese": query(
            filtro="data_applicazione nel mese_corrente",
            conteggio=True
        ),
        "validati_mese": query(
            filtro="data_validazione nel mese_corrente",
            conteggio=True
        ),
        "validati_positivi_mese": query(
            filtro="data_validazione nel mese_corrente AND risultato == 'Positivo'",
            conteggio=True
        ),
        "scartati_mese": query(
            filtro="status cambiato a 'Scartato' nel mese_corrente",
            conteggio=True
        ),

        # MAPPA BIBLIOTECA
        "distribuzione_per_area": {
            area: {
                "totale": query(filtro=f"area == '{area}'", conteggio=True),
                "validati": query(filtro=f"area == '{area}' AND status == 'Validato'", conteggio=True)
            }
            for area in ["AREA_1", "AREA_2", "AREA_3", "AREA_4", "AREA_5", "AREA_6"]
        },

        "distribuzione_per_progetto": {
            prog: query(filtro=f"progetto_primario contiene '{prog}'", conteggio=True)
            for prog in ["Agency", "YouTube", "KDP", "AI Lab", "Strategy"]
        },

        # BACKLOG
        "backlog_attuale": query(
            filtro="status == 'Estratto'",
            conteggio=True
        ),

        # KPI
        "kpi": {
            "tasso_estrazione": "creati_mese / sessioni_studio_mese",
            "tasso_applicazione": "applicati_mese / creati_mese * 100",
            "tasso_validazione": "validati_mese / applicati_mese * 100",
            "tasso_successo": "validati_positivi_mese / validati_mese * 100"
        },

        # TOP E FLOP
        "top_framework": query(
            filtro="validati_positivi nel mese_corrente",
            ordine="impatto_desc",
            limite=3,
            campi=["id", "nome", "risultato"]
        ),
        "framework_falliti": query(
            filtro="scartati nel mese_corrente",
            campi=["id", "nome", "motivo_scarto", "lezione"]
        )
    }

    return results
4.3 — Query per Ricerca Rapida (W2)
Python

def ricerca_framework(query_utente: str) -> list:
    """
    Query per ricerca rapida nel registro.
    Segue l'algoritmo a 5 livelli di KB_07.

    Args:
        query_utente: testo della richiesta dell'utente

    Returns:
        Lista di framework corrispondenti, ordinati per pertinenza
    """

    # Livello 1: Match esatto per nome
    risultati = query(
        filtro=f"nome LIKE '%{query_utente}%'",
        ordine="data_creazione_desc"
    )
    if risultati:
        return risultati

    # Livello 2: Match per area/sottoarea/argomento
    area_target = identifica_area(query_utente)  # Usa KB_01 + indice rapido KB_07
    risultati = query(
        filtro=f"area == '{area_target}' OR argomento LIKE '%{query_utente}%'",
        ordine="pertinenza_desc"
    )
    if risultati:
        return risultati

    # Livello 3: Match per parole chiave nel concetto
    risultati = query(
        filtro=f"concetto_chiave LIKE '%{parola}%' per ogni parola in query_utente",
        ordine="pertinenza_desc"
    )
    if risultati:
        return risultati

    # Livello 4+: Fallback a KB_14 o generazione AI
    # (gestito in KB_07)
    return []
4.4 — Query Anti-Accumulazione
Python

def check_anti_accumulazione() -> dict:
    """
    Verifica se la regola anti-accumulazione è rispettata.
    Chiamata PRIMA di ogni nuovo studio (W1) e durante review (W4/W5).

    Returns:
        Dizionario con stato anti-accumulazione e azioni suggerite
    """

    backlog = query(filtro="status == 'Estratto'", conteggio=True)

    result = {
        "backlog_count": backlog,
        "limite": 5,
        "bloccato": backlog > 5,
        "alert_level": "OK" if backlog <= 3 else "ATTENZIONE" if backlog <= 5 else "BLOCCO"
    }

    if result["bloccato"]:
        result["schede_in_attesa"] = query(
            filtro="status == 'Estratto'",
            ordine="priorita_desc, scadenza_asc",
            campi=["id", "nome", "progetto", "azione_7gg", "scadenza_azione", "giorni_attesa"]
        )
        result["messaggio"] = (
            f"⚠️ BLOCCO STUDIO: {backlog} schede in attesa (limite: 5). "
            f"Applica almeno {backlog - 4} schede prima di studiare nuovo materiale."
        )

    return result
──────────────────────────────────────────────────────
📖 SEZIONE 5: INTEGRITÀ E MANUTENZIONE DEL REGISTRO
──────────────────────────────────────────────────────
5.1 — Regole di Integrità
text

REGOLA 1: UNICITÀ ID
Ogni ID nel registro è UNICO. Non possono esistere due
framework con lo stesso ID. L'AI verifica l'unicità
prima di ogni inserimento.

REGOLA 2: COMPLETEZZA RECORD
Ogni record DEVE avere TUTTI i campi obbligatori compilati.
Campi obbligatori: id, nome, fonte, area, sottoarea, argomento,
concetto_chiave, num_step, progetto_primario, fase_primaria,
trigger, azione_7gg, status, data_creazione.

REGOLA 3: COERENZA STATUS
Le transizioni di status devono seguire il diagramma della
Sezione 1.3. Non è permesso saltare fasi
(es. da Estratto a Validato senza passare per Applicato).
ECCEZIONE: qualsiasi status può transitare a "In Pausa",
"Scartato" o "Da Rivedere".

REGOLA 4: TRACCIABILITÀ TEMPORALE
Ogni cambio di status deve avere una data associata.
Il campo "note" deve documentare PERCHÉ è avvenuto il cambio.

REGOLA 5: COERENZA CLASSIFICAZIONE
L'area, sottoarea e argomento devono corrispondere a codici
validi in KB_01_LIBRARY_ARCHITECTURE.md. Se un nuovo argomento
è necessario, deve essere creato in KB_01 prima di essere usato qui.
5.2 — Manutenzione Periodica
text

DURANTE REVIEW MENSILE (W5):

1. VERIFICA COERENZA
   → Tutti i record hanno ID unici?
   → Tutti i campi obbligatori sono compilati?
   → Le transizioni di status sono coerenti?

2. IDENTIFICA ANOMALIE
   → Framework in status "Estratto" da >30 giorni
     → Segnala come backlog critico
   → Framework in status "Applicato" da >60 giorni senza validazione
     → Segnala: "Validazione in forte ritardo"
   → Framework in status "In Pausa" da >90 giorni
     → Suggerisci: "Questo framework è in pausa da 3 mesi.
       È ancora rilevante? Considera di scartarlo o riattivarlo."

3. PULIZIA
   → Non cancellare MAI — ma segnala i record potenzialmente obsoleti
   → Suggerisci la revisione di framework molto vecchi
     che non sono mai stati applicati
5.3 — Gestione Duplicati
text

QUANDO L'AI SOSPETTA UN DUPLICATO:

1. Cerca per: nome simile + area simile + concetto simile
2. SE match trovato:

   CASO A: DUPLICATO ESATTO
   → Il nuovo framework è identico a uno esistente
   → NON creare nuovo record
   → Segnala: "Questo framework è già registrato come
     [Nome] (ID: [ID]). Non creo un duplicato."

   CASO B: VERSIONE AGGIORNATA
   → Il nuovo framework è una versione migliorata dell'esistente
   → AGGIORNA il record esistente (non creare nuovo)
   → Nota: "Aggiornato il [data] con nuove info da [fonte]"
   → Mantieni l'ID originale

   CASO C: FRAMEWORK COMPLEMENTARE
   → Il nuovo framework copre lo stesso tema ma da angolazione diversa
   → CREA nuovo record
   → In entrambi i record, aggiungi: "Complementare a [ID_altro]"

   CASO D: FRAMEWORK ALTERNATIVO
   → Il nuovo framework è un'alternativa (approccio diverso allo stesso problema)
   → CREA nuovo record
   → In entrambi: "Alternativo a [ID_altro] — usare [trigger per scegliere]"
──────────────────────────────────────────────────────
📖 SEZIONE 6: CONTATORI E STATISTICHE
──────────────────────────────────────────────────────
6.1 — Contatori Globali
L'AI mantiene mentalmente questi contatori, aggiornandoli
ad ogni operazione sul registro:

Python

class RegistryCounters:
    """
    Contatori globali del registro framework.
    Aggiornati automaticamente ad ogni CREATE/UPDATE.
    """

    def __init__(self):
        # Contatori totali
        self.totale_framework: int = 0
        self.totale_per_area: dict = {
            "AREA_1": 0, "AREA_2": 0, "AREA_3": 0,
            "AREA_4": 0, "AREA_5": 0, "AREA_6": 0
        }
        self.totale_per_progetto: dict = {
            "Agency": 0, "YouTube": 0, "KDP": 0,
            "AI_Lab": 0, "Strategy": 0
        }

        # Contatori per status
        self.estratti_non_applicati: int = 0  # Backlog
        self.applicati_non_validati: int = 0
        self.validati_positivi: int = 0
        self.validati_negativi: int = 0
        self.in_pausa: int = 0
        self.scartati: int = 0
        self.insegnati: int = 0

        # Contatori temporali (mese corrente)
        self.creati_mese: int = 0
        self.applicati_mese: int = 0
        self.validati_mese: int = 0

        # Numerazione progressiva per ID
        self.prossimo_numero: dict = {}
        # Formato: {"A1_A": 1, "A1_B": 4, "A3_A": 2, ...}
6.2 — Dashboard Rapida
Quando l'utente chiede "stato biblioteca" o "dashboard", genera:

text

📊 DASHBOARD MARKETING UNIVERSITY
═══════════════════════════════════════

TOTALE FRAMEWORK: [N]

PER AREA:
├── AREA_1 Copywriting:    [█████████░] [N] ([N] validati)
├── AREA_2 Email Marketing:[████░░░░░░] [N] ([N] validati)
├── AREA_3 Funnel/CRO:     [███████░░░] [N] ([N] validati)
├── AREA_4 Vendita:        [██████░░░░] [N] ([N] validati)
├── AREA_5 Content:        [███░░░░░░░] [N] ([N] validati)
└── AREA_6 Mindset:        [██░░░░░░░░] [N] ([N] validati)

PER STATUS:
├── ✅✅□□□ Estratti (in attesa):  [N]  [⚠️ se >5]
├── ✅✅✅□□ Applicati:             [N]
├── ✅✅✅✅□ Validati (+):          [N]
├── ❌     Scartati:              [N]
├── ⏸️     In Pausa:              [N]
└── 🎓     Insegnati:             [N]

PER PROGETTO:
├── ⚡ Agency:   [N] framework
├── 🎥 YouTube:  [N] framework
├── 📚 KDP:      [N] framework
├── 🤖 AI Lab:   [N] framework
└── 🧠 Strategy: [N] framework

MESE CORRENTE:
├── Creati: [N]
├── Applicati: [N]
└── Validati: [N]

ALERT:
[⚠️ Backlog > 5: BLOCCO STUDIO ATTIVO]
[⚠️ N framework da validare (>30gg)]
[✅ Tutto sotto controllo]
═══════════════════════════════════════
──────────────────────────────────────────────────────
🔧 COME UTILIZZARE QUESTO FILE
──────────────────────────────────────────────────────
Utilizzo da parte dell'AI:
Durante Workflow W1 (Step 8 — Registrazione):
→ Dopo aver generato le schede, registra ogni framework
→ Verifica unicità ID
→ Verifica assenza duplicati
→ Aggiorna contatori globali
→ Verifica anti-accumulazione (Sezione 4.4)

Durante Workflow W2 (Ricerca):
→ Esegui query di ricerca (Sezione 4.3)
→ Usa le viste appropriate (Sezione 2.2)
→ Restituisci risultati con template W2 (KB_06)

Durante Workflow W4 (Review Settimanale):
→ Esegui query settimanali (Sezione 4.1)
→ Genera vista temporale (Sezione 2.2)
→ Verifica backlog e azioni scadute

Durante Workflow W5 (Review Mensile):
→ Esegui query mensili (Sezione 4.2)
→ Calcola KPI completi
→ Genera dashboard (Sezione 6.2)
→ Esegui manutenzione (Sezione 5.2)

Durante Workflow W6 (Validazione):
→ Trova il framework da validare nel registro
→ Esegui UPDATE status (Sezione 3.3)
→ Documenta risultati nel record

In qualsiasi momento — Anti-Accumulazione:
→ Prima di ogni W1: esegui check (Sezione 4.4)
→ Se bloccato: impedisci nuovo studio, mostra backlog

──────────────────────────────────────────────────────
🔗 COLLEGAMENTI
──────────────────────────────────────────────────────
Dipende da: KB_01_LIBRARY_ARCHITECTURE.md (codici classificazione),
KB_02_EXTRACTION_ENGINE.md (processo che genera i record)
Alimenta: KB_07_QUICK_REFERENCE_PROTOCOL.md (cercato durante ricerche),
KB_09_STUDY_PRIORITY_ENGINE.md (dati per suggerimenti),
KB_06_RESPONSE_TEMPLATES.md (dati per compilare template)
Referenziato da: Custom Instructions — Sezione 2.2, 5.2,
e tutti i Workflow (W1-W6)
──────────────────────────────────────────────────────
💡 ESEMPIO PRATICO DI UTILIZZO
──────────────────────────────────────────────────────
Scenario: Registrazione di un nuovo framework (W1 Step 8)
Framework appena estratto dalla "Guida Funnel Acquisizione Clienti":

1. Verifica unicità ID:
Prossimo numero per A3_A: 01 (primo framework in questa combinazione)
ID generato: A3_A_01_250615 ✅ Unico

2. Verifica duplicati:
Ricerca "friction" + "form" + "routing" nel registro → Nessun match ✅

3. Registrazione:
text

NUOVO RECORD:
| Campo | Valore |
|-------|--------|
| ID | A3_A_01_250615 |
| Nome | Friction-Routing System |
| Fonte | Guida Funnel Acquisizione Clienti |
| Area | AREA_3 |
| Sottoarea | 3A |
| Argomento | 3A.03 — Form optimization |
| Concetto | La friction nel form è strategica: aumenta costo per lead ma migliora qualità |
| Step | 5 |
| Progetto | ⚡ Agency Operations |
| Fase | Fase 1 — Acquisizione e Qualificazione |
| Trigger | Setup/ottimizzazione form di applicazione |
| Azione | Aggiungere 3 domande qualificanti al form Digital Empire |
| Status | ✅✅□□□ (Studiato + Estratto) |
| Data | 15/06/2025 |
| Scadenza | 22/06/2025 |
4. Aggiornamento contatori:
totale_framework: 0 → 1
totale_per_area["AREA_3"]: 0 → 1
totale_per_progetto["Agency"]: 0 → 1
estratti_non_applicati: 0 → 1
creati_mese: 0 → 1
prossimo_numero["A3_A"]: 1 → 2
5. Anti-accumulazione: 1 ≤ 5 ✅ OK
──────────────────────────────────────────────────────
⚠️ NOTE E AVVERTENZE
──────────────────────────────────────────────────────
Questo file definisce la STRUTTURA, non i dati.
I dati reali vivono nelle conversazioni del progetto Claude.
L'AI mantiene consapevolezza dei framework creati durante
le sessioni attive. Per framework creati in sessioni precedenti,
l'AI si basa su ciò che l'utente le comunica e su KB_14.

Il registro CRESCE nel tempo. Dopo 6 mesi potrebbe
contenere 50-80+ framework. Dopo 12 mesi, 100-150+.
Le viste filtrate (Sezione 2.2) sono essenziali per
navigare un registro grande.

L'anti-accumulazione è il GUARDIANO del registro.
Senza di essa, il registro si riempirebbe di framework
mai applicati. La Sezione 4.4 deve essere eseguita
rigorosamente prima di ogni nuovo studio.

I contatori (Sezione 6) sono APPROSSIMATIVI.
In un progetto Claude, l'AI non ha memoria persistente
tra sessioni. I contatori vengono ricostruiti dalle
informazioni disponibili nella conversazione attiva
e da ciò che l'utente comunica. Per conteggi precisi,
l'utente può mantenere un foglio esterno con gli ID.

Il pseudocodice Python è LOGICA, non codice eseguibile.
Rappresenta il ragionamento che l'AI deve seguire,
non un programma da eseguire. L'AI usa questa logica
internamente per processare le query e le operazioni.
