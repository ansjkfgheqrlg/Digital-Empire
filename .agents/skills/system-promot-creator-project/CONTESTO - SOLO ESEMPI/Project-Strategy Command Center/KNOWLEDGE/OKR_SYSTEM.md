# ═══════════════════════════════════════════════════════════════
# 📄 OKR_SYSTEM.md
# ═══════════════════════════════════════════════════════════════
# Versione: 1.0
# Categoria: CORE_LOGIC
# Priorità: P0 — BLOCCANTE
# Dipendenze: GERARCHIA_PILLAR.md (per la gerarchia delle priorità), DASHBOARD_ENGINE.md (i dati dashboard alimentano la review OKR)
# Referenziato da: Custom Instructions — Sezione 2.2 (OKR), Sezione 5.2, Sezione 8.2 (Step 1), Sezione 8.3 (Step 2, 4), Sezione 8.4 (Step 2, 3)
# ═══════════════════════════════════════════════════════════════

## 📋 SCOPO

Questo file contiene il sistema OKR (Objectives & Key Results) completo di Digital Empire. È il sistema di navigazione strategica che traduce la vision in azioni concrete attraverso 3 livelli gerarchici:

- **LIVELLO 1 — OKR ANNUALE**: La bussola. Dove vuoi arrivare entro fine anno.
- **LIVELLO 2 — OKR TRIMESTRALE**: La mappa. Come arrivi là, 90 giorni alla volta.
- **LIVELLO 3 — SPRINT MENSILE**: Il volante. Cosa fai concretamente questo mese.

Principio fondante: Ogni task che fai deve essere collegato a un Key Result. Se non è collegato a nessun KR → non è una priorità. Mettilo nella Not To Do list o posponilo.

---

## 📖 CONTENUTO PRINCIPALE

### 1. ARCHITETTURA DEL SISTEMA OKR
STRUTTURA GERARCHICA — Come si collegano i 3 livelli
═════════════════════════════════════════════════════

text

┌─────────────────────────────────────────┐
│         OKR ANNUALE (LIVELLO 1)         │
│                                         │
│  1 Objective + 3 Key Results            │
│  PER OGNI PILLAR                        │
│  + 1 OKR Cross-Pollination              │
│                                         │
│  Definito: Gennaio (o quando inizi)     │
│  Review: Ogni trimestre                 │
│  Durata: 12 mesi                        │
└──────────────────┬──────────────────────┘
                   │
        ┌──────────┴──────────┐
        │                     │
        ▼                     ▼
┌───────────────┐    ┌───────────────┐
│  OKR Q1       │    │  OKR Q2       │    (e Q3, Q4)
│  (LIVELLO 2)  │    │  (LIVELLO 2)  │
│               │    │               │
│ 1-2 Obj +     │    │ 1-2 Obj +     │
│ 2-3 KR each   │    │ 2-3 KR each   │
│ per pillar    │    │ per pillar    │
│               │    │               │
│ Max 3 priorità│    │ Max 3 priorità│
│ + Not To Do   │    │ + Not To Do   │
│               │    │               │
│ Def: inizio Q │    │ Def: inizio Q │
│ Rev: mensile  │    │ Rev: mensile  │
└───────┬───────┘    └───────────────┘
        │
┌───────┴───────┐
│               │
▼               ▼
┌────────┐ ┌────────┐ ┌────────┐
│Sprint │ │Sprint │ │Sprint │
│Mese 1 │ │Mese 2 │ │Mese 3 │
│(LIV.3) │ │(LIV.3) │ │(LIV.3) │
│ │ │ │ │ │
│5-7 task│ │5-7 task│ │5-7 task│
│collegati│ │collegati│ │collegati│
│ai KR │ │ai KR │ │ai KR │
│ │ │ │ │ │
│Def: 1° │ │Def: 1° │ │Def: 1° │
│lunedì │ │lunedì │ │lunedì │
│Rev: │ │Rev: │ │Rev: │
│settimanale│ │settimanale│ │settimanale│
└────────┘ └────────┘ └────────┘

text


### 2. REGOLE DEL SISTEMA OKR
7 REGOLE INVIOLABILI
═════════════════════

REGOLA 1: COERENZA VERTICALE
Ogni KR trimestrale deve essere un sotto-insieme
di un KR annuale. Ogni task mensile deve muovere
un KR trimestrale. Se non c'è collegamento →
il task non ha ragione di esistere.

REGOLA 2: LIMITI QUANTITATIVI
├── OKR Annuale: 1 Objective + max 3 KR per pillar
├── OKR Trimestrale: max 2 Objectives + max 3 KR
│ ciascuno per pillar
├── Sprint Mensile: max 7 task totali
└── Priorità trimestrali: max 3

REGOLA 3: MISURABILITÀ
Ogni Key Result DEVE contenere un NUMERO.
❌ "Migliorare il close rate" → vago, non misurabile
✅ "Portare il close rate dal 20% al 35%" → preciso

REGOLA 4: NOT TO DO = TO DO
Per ogni lista di priorità, DEVE esistere una lista
di "Not To Do" di uguale importanza. Decidere cosa
NON fare è importante quanto decidere cosa fare.

REGOLA 5: GERARCHIA DEI PILLAR
La distribuzione dei task nello sprint deve
riflettere la gerarchia da GERARCHIA_PILLAR.md:
├── 3-4 task su 7 → Agenzia CRO
├── 1-2 task su 7 → Info-Business
├── 1 task su 7 → YouTube
└── 0-1 task su 7 → Cross-pollination o Satellite

REGOLA 6: REVIEW CADENZATA
├── Sprint mensile → review SETTIMANALE (ogni lunedì)
├── OKR trimestrale → review MENSILE (primo lunedì)
├── OKR annuale → review TRIMESTRALE
└── MAI saltare una review. Se salti, il sistema muore.

REGOLA 7: TARGET REALISTICO
Il target di completion rate per un trimestre è >70%.
├── SE >90% → I tuoi OKR erano troppo facili.
│ Alza l'asticella il prossimo Q.
├── SE 70-90% → Perfetto. Ambizioso ma raggiungibile.
├── SE 50-69% → Accettabile ma da migliorare.
│ Analizza cosa ha bloccato l'esecuzione.
└── SE <50% → Problema serio. O gli OKR erano
irrealistici, o l'esecuzione era debole.
Diagnostica PRIMA di definire i prossimi.

text


### 3. TEMPLATE OKR ANNUALE (LIVELLO 1)
═══════════════════════════════════════════════════════════
OKR ANNUALE — DIGITAL EMPIRE
Anno: 20[XX]
Definito il: [DATA]
Prossima review: Fine Q[N]
═══════════════════════════════════════════════════════════

VISION ANNUALE (1 frase):
"Entro il 31 dicembre 20[XX], Digital Empire
___________________________________________________________."

───────────────────────────────────────────────────────────
PILLAR 1: AGENZIA CRO
───────────────────────────────────────────────────────────

OBJECTIVE:
[Scrivi l'obiettivo annuale per l'agenzia in 1-2 frasi.
Deve essere ambizioso, chiaro e ispirante.]

KEY RESULTS:

KR1: ________________________________________________
Metrica: [cosa misuri]
Baseline (oggi): [valore attuale]
Target (fine anno): [valore obiettivo]
Progresso:
├── Fine Q1: ___% │ Reale: ___%
├── Fine Q2: ___% │ Reale: ___%
├── Fine Q3: ___% │ Reale: ___%
└── Fine Q4: ___% │ Reale: ___%

KR2: ________________________________________________
Metrica: [cosa misuri]
Baseline (oggi): [valore attuale]
Target (fine anno): [valore obiettivo]
Progresso:
├── Fine Q1: ___% │ Reale: ___%
├── Fine Q2: ___% │ Reale: ___%
├── Fine Q3: ___% │ Reale: ___%
└── Fine Q4: ___% │ Reale: ___%

KR3: ________________________________________________
Metrica: [cosa misuri]
Baseline (oggi): [valore attuale]
Target (fine anno): [valore obiettivo]
Progresso:
├── Fine Q1: ___% │ Reale: ___%
├── Fine Q2: ___% │ Reale: ___%
├── Fine Q3: ___% │ Reale: ___%
└── Fine Q4: ___% │ Reale: ___%

STATUS ANNUALE AGENZIA: [🟢🟡🔴]

───────────────────────────────────────────────────────────
PILLAR 2: INFO-BUSINESS
───────────────────────────────────────────────────────────

OBJECTIVE:
[Obiettivo annuale info-business]

KEY RESULTS:

KR1: ________________________________________________
Metrica: [cosa misuri]
Baseline: [valore attuale]
Target: [valore obiettivo]
Progresso:
├── Fine Q1: ___% │ Reale: ___%
├── Fine Q2: ___% │ Reale: ___%
├── Fine Q3: ___% │ Reale: ___%
└── Fine Q4: ___% │ Reale: ___%

KR2: ________________________________________________
Metrica: [cosa misuri]
Baseline: [valore attuale]
Target: [valore obiettivo]
Progresso:
├── Fine Q1: ___% │ Reale: ___%
├── Fine Q2: ___% │ Reale: ___%
├── Fine Q3: ___% │ Reale: ___%
└── Fine Q4: ___% │ Reale: ___%

KR3: ________________________________________________
Metrica: [cosa misuri]
Baseline: [valore attuale]
Target: [valore obiettivo]
Progresso:
├── Fine Q1: ___% │ Reale: ___%
├── Fine Q2: ___% │ Reale: ___%
├── Fine Q3: ___% │ Reale: ___%
└── Fine Q4: ___% │ Reale: ___%

STATUS ANNUALE INFO-BIZ: [🟢🟡🔴]

───────────────────────────────────────────────────────────
PILLAR 3: YOUTUBE / CONTENT
───────────────────────────────────────────────────────────

OBJECTIVE:
[Obiettivo annuale YouTube]

KEY RESULTS:

KR1: ________________________________________________
Metrica: [cosa misuri]
Baseline: [valore attuale]
Target: [valore obiettivo]
Progresso:
├── Fine Q1: ___% │ Reale: ___%
├── Fine Q2: ___% │ Reale: ___%
├── Fine Q3: ___% │ Reale: ___%
└── Fine Q4: ___% │ Reale: ___%

KR2: ________________________________________________
Metrica: [cosa misuri]
Baseline: [valore attuale]
Target: [valore obiettivo]
Progresso:
├── Fine Q1: ___% │ Reale: ___%
├── Fine Q2: ___% │ Reale: ___%
├── Fine Q3: ___% │ Reale: ___%
└── Fine Q4: ___% │ Reale: ___%

KR3: ________________________________________________
Metrica: [cosa misuri]
Baseline: [valore attuale]
Target: [valore obiettivo]
Progresso:
├── Fine Q1: ___% │ Reale: ___%
├── Fine Q2: ___% │ Reale: ___%
├── Fine Q3: ___% │ Reale: ___%
└── Fine Q4: ___% │ Reale: ___%

STATUS ANNUALE YOUTUBE: [🟢🟡🔴]

───────────────────────────────────────────────────────────
CROSS-POLLINATION ANNUALE
───────────────────────────────────────────────────────────

OBJECTIVE:
"Ogni pillar alimenta gli altri in modo misurabile"

KEY RESULTS:

KR1: ________________________________________________
[Es: "Almeno N% degli studenti info-biz diventa
lead agenzia"]
Baseline: [valore attuale]
Target: [valore obiettivo]
Progresso: Q1___% Q2___% Q3___% Q4___%

KR2: ________________________________________________
[Es: "Almeno N% dei clienti agenzia acquista
un prodotto info"]
Baseline: [valore attuale]
Target: [valore obiettivo]
Progresso: Q1___% Q2___% Q3___% Q4___%

KR3: ________________________________________________
[Es: "Almeno N% dei lead info-biz proviene
da YouTube"]
Baseline: [valore attuale]
Target: [valore obiettivo]
Progresso: Q1___% Q2___% Q3___% Q4___%

STATUS ANNUALE CROSS-POLL: [🟢🟡🔴]

───────────────────────────────────────────────────────────
SATELLITE (monitoraggio leggero, no OKR formali)
───────────────────────────────────────────────────────────

KDP:
├── Obiettivo annuale: [1 frase]
├── Metrica chiave: [cosa misuri]
└── Target: [numero]

AI Influencer:
├── Obiettivo annuale: [1 frase]
├── Metrica chiave: [cosa misuri]
└── Target: [numero]

═══════════════════════════════════════════════════════════

text


**Istruzioni per la compilazione dell'OKR Annuale:**
- La VISION deve essere 1 frase che ispira e dà direzione per 12 mesi
- Ogni OBJECTIVE deve essere qualitativo e ambizioso (il "cosa")
- Ogni KEY RESULT deve essere quantitativo e misurabile (il "come sai che ci sei arrivato")
- La BASELINE è il punto di partenza (dove sei oggi). Senza baseline, non puoi misurare il progresso
- Il TARGET è dove vuoi arrivare. Deve essere ambizioso ma non delirante (regola del 70%)
- Il progresso si aggiorna a fine di ogni trimestre
- I satellite NON hanno OKR formali — solo 1 obiettivo + 1 metrica. Non meritano la complessità OKR

---

### 4. TEMPLATE OKR TRIMESTRALE (LIVELLO 2)
═══════════════════════════════════════════════════════════
OKR TRIMESTRALE — Q[N] 20[XX]
Definito il: [DATA primo lunedì del trimestre]
Review mensile: [DATE dei 3 primi lunedì]
Close-out: [DATA ultimo venerdì del trimestre]
═══════════════════════════════════════════════════════════

CONTESTO DEL TRIMESTRE:
"Questo trimestre è importante perché ________________.
La sfida principale è ________________________________.
Se dovessi ottenere UNA SOLA cosa, sarebbe ___________."

───────────────────────────────────────────────────────────
PILLAR 1: AGENZIA CRO — Q[N]
───────────────────────────────────────────────────────────

OKR ANNUALE DI RIFERIMENTO:
[Copia l'Objective annuale dell'agenzia come promemoria]

OBJECTIVE Q[N]:
[Sotto-obiettivo trimestrale che contribuisce all'OKR
annuale. Più specifico, più tattico.]

KR1: ________________________________________________
Collegato a KR annuale: [quale]
Target Q: [numero]
├── Mese 1: Target ___ │ Reale ___ │ Status [🟢🟡🔴]
├── Mese 2: Target ___ │ Reale ___ │ Status [🟢🟡🔴]
└── Mese 3: Target ___ │ Reale ___ │ Status [🟢🟡🔴]
PROGRESSO COMPLESSIVO: ___%

KR2: ________________________________________________
Collegato a KR annuale: [quale]
Target Q: [numero]
├── Mese 1: Target ___ │ Reale ___ │ Status [🟢🟡🔴]
├── Mese 2: Target ___ │ Reale ___ │ Status [🟢🟡🔴]
└── Mese 3: Target ___ │ Reale ___ │ Status [🟢🟡🔴]
PROGRESSO COMPLESSIVO: ___%

KR3: ________________________________________________
Collegato a KR annuale: [quale]
Target Q: [numero]
├── Mese 1: Target ___ │ Reale ___ │ Status [🟢🟡🔴]
├── Mese 2: Target ___ │ Reale ___ │ Status [🟢🟡🔴]
└── Mese 3: Target ___ │ Reale ___ │ Status [🟢🟡🔴]
PROGRESSO COMPLESSIVO: ___%

STATUS Q AGENZIA: [🟢🟡🔴]

───────────────────────────────────────────────────────────
PILLAR 2: INFO-BUSINESS — Q[N]
───────────────────────────────────────────────────────────

OKR ANNUALE DI RIFERIMENTO:
[Copia l'Objective annuale info-biz]

OBJECTIVE Q[N]:
[Sotto-obiettivo trimestrale]

KR1: ________________________________________________
Collegato a KR annuale: [quale]
Target Q: [numero]
├── Mese 1: Target ___ │ Reale ___ │ Status [🟢🟡🔴]
├── Mese 2: Target ___ │ Reale ___ │ Status [🟢🟡🔴]
└── Mese 3: Target ___ │ Reale ___ │ Status [🟢🟡🔴]
PROGRESSO COMPLESSIVO: ___%

KR2: ________________________________________________
Collegato a KR annuale: [quale]
Target Q: [numero]
├── Mese 1: Target ___ │ Reale ___ │ Status [🟢🟡🔴]
├── Mese 2: Target ___ │ Reale ___ │ Status [🟢🟡🔴]
└── Mese 3: Target ___ │ Reale ___ │ Status [🟢🟡🔴]
PROGRESSO COMPLESSIVO: ___%

STATUS Q INFO-BIZ: [🟢🟡🔴]

───────────────────────────────────────────────────────────
PILLAR 3: YOUTUBE / CONTENT — Q[N]
───────────────────────────────────────────────────────────

OKR ANNUALE DI RIFERIMENTO:
[Copia l'Objective annuale YouTube]

OBJECTIVE Q[N]:
[Sotto-obiettivo trimestrale]

KR1: ________________________________________________
Collegato a KR annuale: [quale]
Target Q: [numero]
├── Mese 1: Target ___ │ Reale ___ │ Status [🟢🟡🔴]
├── Mese 2: Target ___ │ Reale ___ │ Status [🟢🟡🔴]
└── Mese 3: Target ___ │ Reale ___ │ Status [🟢🟡🔴]
PROGRESSO COMPLESSIVO: ___%

KR2: ________________________________________________
Collegato a KR annuale: [quale]
Target Q: [numero]
├── Mese 1: Target ___ │ Reale ___ │ Status [🟢🟡🔴]
├── Mese 2: Target ___ │ Reale ___ │ Status [🟢🟡🔴]
└── Mese 3: Target ___ │ Reale ___ │ Status [🟢🟡🔴]
PROGRESSO COMPLESSIVO: ___%

STATUS Q YOUTUBE: [🟢🟡🔴]

───────────────────────────────────────────────────────────
CROSS-POLLINATION — Q[N]
───────────────────────────────────────────────────────────

OBJECTIVE Q[N]:
[Obiettivo trimestrale per le sinergie]

KR1: ________________________________________________
Target Q: [numero]
├── Mese 1: ___ │ Mese 2: ___ │ Mese 3: ___
PROGRESSO: ___%

KR2: ________________________________________________
Target Q: [numero]
├── Mese 1: ___ │ Mese 2: ___ │ Mese 3: ___
PROGRESSO: ___%

STATUS Q CROSS-POLL: [🟢🟡🔴]

───────────────────────────────────────────────────────────
PRIORITÀ DEL TRIMESTRE (max 3)
───────────────────────────────────────────────────────────

Pillar: [quale] │ KR collegato: [quale]
Perché è #1: [motivazione]

Pillar: [quale] │ KR collegato: [quale]
Perché è #2: [motivazione]

Pillar: [quale] │ KR collegato: [quale]
Perché è #3: [motivazione]

VERIFICA: Almeno 1 delle 3 priorità riguarda l'Agenzia?
├── SÌ → ✅ Corretto
└── NO → ⚠️ Perché? L'agenzia è stabile? Se sì, OK.
Se no, ricalibrare.

───────────────────────────────────────────────────────────
"NOT TO DO" DEL TRIMESTRE
───────────────────────────────────────────────────────────

Cose che SCELGO di NON fare questo trimestre:

Motivo: [perché non ora]

Motivo: [perché non ora]

Motivo: [perché non ora]

───────────────────────────────────────────────────────────
CLOSE-OUT TRIMESTRALE (compilare a fine Q)
───────────────────────────────────────────────────────────

┌────────────┬──────┬────────┬──────────┬────────┬────────┐
│ Pillar │ KR │ Target │ Risultato│ % │Lezione │
├────────────┼──────┼────────┼──────────┼────────┼────────┤
│ Agenzia │ KR1 │ [N] │ [N] │ [N]% │ [testo]│
│ Agenzia │ KR2 │ [N] │ [N] │ [N]% │ │
│ Agenzia │ KR3 │ [N] │ [N] │ [N]% │ │
│ Info-Biz │ KR1 │ [N] │ [N] │ [N]% │ │
│ Info-Biz │ KR2 │ [N] │ [N] │ [N]% │ │
│ YouTube │ KR1 │ [N] │ [N] │ [N]% │ │
│ YouTube │ KR2 │ [N] │ [N] │ [N]% │ │
│ Cross-Poll │ KR1 │ [N] │ [N] │ [N]% │ │
│ Cross-Poll │ KR2 │ [N] │ [N] │ [N]% │ │
└────────────┴──────┴────────┴──────────┴────────┴────────┘

OKR COMPLETION RATE COMPLESSIVO: [N]%
VALUTAZIONE:
├── >90%: OKR troppo facili → alza l'asticella
├── 70-90%: Perfetto → mantieni questo livello di ambizione
├── 50-69%: Accettabile → analizza cosa ha bloccato
└── <50%: Problema → diagnostica prima di definire Q+1

DOMANDA CHIAVE: "Cosa avrei fatto DIVERSAMENTE
sapendo quello che so adesso?"
Risposta: ___________________________________________

═══════════════════════════════════════════════════════════

text


---

### 5. TEMPLATE SPRINT MENSILE (LIVELLO 3)
═══════════════════════════════════════════════════════════
SPRINT MENSILE — [MESE] [ANNO]
Definito il: [DATA primo lunedì del mese]
Review: Ogni lunedì
Close-out: [DATA ultimo venerdì del mese]
═══════════════════════════════════════════════════════════

FOCUS DEL MESE (1 frase):
"Questo mese mi concentro su _________________________."

OKR TRIMESTRALE DI RIFERIMENTO:
├── Priorità Q #1: [copia da OKR trimestrale]
├── Priorità Q #2: [copia]
└── Priorità Q #3: [copia]

───────────────────────────────────────────────────────────
TASK PRIORITARI (max 7)
───────────────────────────────────────────────────────────

┌────┬──────────────────────────┬────────┬───────┬───────┬─────────┐
│ # │ Task specifico │ Pillar │ KR │Settim.│ Status │
│ │ (verbo + oggetto + │ │linked │target │ │
│ │ risultato misurabile) │ │ │ │ │
├────┼──────────────────────────┼────────┼───────┼───────┼─────────┤
│ 1 │ [│ [AGZ/ │ [KR#] │ [S1/ │ ⬜ Todo │
│ │ ]│ IB/YT/ │ │ S2/S3/│ 🔄 WIP │
│ │ │ CROSS/ │ │ S4] │ ✅ Done │
│ │ │ SAT] │ │ │ ❌ Drop │
├────┼──────────────────────────┼────────┼───────┼───────┼─────────┤
│ 2 │ []│ │ │ │ ⬜ │
├────┼──────────────────────────┼────────┼───────┼───────┼─────────┤
│ 3 │ []│ │ │ │ ⬜ │
├────┼──────────────────────────┼────────┼───────┼───────┼─────────┤
│ 4 │ []│ │ │ │ ⬜ │
├────┼──────────────────────────┼────────┼───────┼───────┼─────────┤
│ 5 │ []│ │ │ │ ⬜ │
├────┼──────────────────────────┼────────┼───────┼───────┼─────────┤
│ 6 │ []│ │ │ │ ⬜ │
├────┼──────────────────────────┼────────┼───────┼───────┼─────────┤
│ 7 │ []│ │ │ │ ⬜ │
└────┴──────────────────────────┴────────┴───────┴───────┴─────────┘

LEGENDA STATUS:
⬜ Todo = Non ancora iniziato
🔄 WIP = Work in Progress (in corso)
✅ Done = Completato
❌ Drop = Eliminato/posticipato (con motivo)

───────────────────────────────────────────────────────────
VERIFICA DISTRIBUZIONE
───────────────────────────────────────────────────────────

┌─────────────────┬─────────┬──────────┬─────────────────┐
│ Pillar │ N. Task │ Target │ Status │
├─────────────────┼─────────┼──────────┼─────────────────┤
│ Agenzia CRO │ [N]/7 │ 3-4 task │ [OK / ⚠️ Troppi │
│ │ │ │ pochi / Troppi] │
├─────────────────┼─────────┼──────────┼─────────────────┤
│ Info-Business │ [N]/7 │ 1-2 task │ [OK / ⚠️] │
├─────────────────┼─────────┼──────────┼─────────────────┤
│ YouTube │ [N]/7 │ 1 task │ [OK / ⚠️] │
├─────────────────┼─────────┼──────────┼─────────────────┤
│ Cross-Poll │ [N]/7 │ 0-1 task │ [OK / ⚠️] │
├─────────────────┼─────────┼──────────┼─────────────────┤
│ Satellite │ [N]/7 │ 0-1 task │ [OK / ⚠️] │
└─────────────────┴─────────┴──────────┴─────────────────┘

SE la distribuzione non rispetta la gerarchia:
→ Sposta task finché non è bilanciata.
→ Se hai 3 task YouTube e 1 task Agenzia → INVERTI.

───────────────────────────────────────────────────────────
VERIFICA COLLEGAMENTO KR
───────────────────────────────────────────────────────────

Per ogni task, rispondi:
"Questo task, se completato, muove direttamente il
KR [X] di almeno [N] punti percentuali?"

├── SE SÌ → Il task è legittimo. Mantienilo.
├── SE "non direttamente, ma..." → ⚠️ Rivaluta.
│ Probabilmente è un task di supporto, non prioritario.
└── SE NO → ❌ Rimuovi dallo sprint. Mettilo nella
Not To Do o nel backlog.

───────────────────────────────────────────────────────────
REVIEW SETTIMANALI
───────────────────────────────────────────────────────────

SETTIMANA 1 — [Date]
├── Task completati: ___
├── Task in corso: ___
├── Task bloccati: ___ │ Motivo: ___
├── Azione cross-pollination: [✅/❌] Quale: ___
├── Focus check: "Sto lavorando sui task dello sprint?"
│ [SÌ/NO → se NO, cosa mi ha distratto?]
└── Note: ___

SETTIMANA 2 — [Date]
├── Task completati: ___
├── Task in corso: ___
├── Task bloccati: ___ │ Motivo: ___
├── Azione cross-pollination: [✅/❌] Quale: ___
├── Mid-month check: "Sono a buon punto per completare
│ almeno 5/7 task entro fine mese?"
│ [SÌ → continua / NO → cosa taglio o accelero?]
└── Note: ___

SETTIMANA 3 — [Date]
├── Task completati: ___
├── Task in corso: ___
├── Task bloccati: ___ │ Motivo: ___
├── Azione cross-pollination: [✅/❌] Quale: ___
└── Note: ___

SETTIMANA 4 — [Date]
├── Task completati: ___
├── Task in corso: ___
├── Task bloccati: ___ │ Motivo: ___
├── Azione cross-pollination: [✅/❌] Quale: ___
└── Note: ___

───────────────────────────────────────────────────────────
CLOSE-OUT MENSILE
───────────────────────────────────────────────────────────

┌──────────────────────────┬──────────┐
│ Metrica │ Risultato│
├──────────────────────────┼──────────┤
│ Task completati │ [N] / 7 │
│ Completion rate │ [N]% │
│ Task droppati │ [N] │
│ (motivo per ciascuno) │ │
│ Azioni cross-pollination │ [N] / 4 │
│ KR più mosso questo mese │ [quale] │
│ Ore effettive lavorate │ [N] ore │
│ Distribuzione tempo: │ │
│ Agenzia │ [N]% │
│ Info-Biz │ [N]% │
│ YouTube │ [N]% │
│ Satellite │ [N]% │
├──────────────────────────┼──────────┤
│ Cosa ha funzionato bene │ [testo] │
│ Cosa NON ha funzionato │ [testo] │
│ Cosa cambio il mese │ [testo] │
│ prossimo │ │
└──────────────────────────┴──────────┘

═══════════════════════════════════════════════════════════

text


---

### 6. COME SCRIVERE BUONI KEY RESULTS
FORMULA PER UN BUON KEY RESULT
══════════════════════════════

Struttura: [Verbo] + [Metrica] + [da X] + [a Y] + [entro quando]

ESEMPI BUONI:
✅ "Portare il close rate delle call dal 20% al 35% entro fine Q2"
✅ "Chiudere 4 nuovi clienti agenzia con valore medio >€2.500"
✅ "Costruire la lista email da 50 a 500 lead"
✅ "Pubblicare 12 video YouTube (1/settimana)"
✅ "Generare 20 lead/mese da YouTube verso il funnel info-biz"
✅ "Lanciare 2 prodotti info con revenue >€1.000 ciascuno"
✅ "Ottenere 3 referral da clienti agenzia esistenti"

ESEMPI CATTIVI:
❌ "Migliorare il business" → non misurabile
❌ "Fare più video" → quanto è "più"?
❌ "Essere più costante" → costante come?
❌ "Espandere la lista" → di quanto?
❌ "Lavorare sul brand" → cosa significa concretamente?

TEST DI QUALITÀ:
Per ogni KR chiediti:

"Posso misurarlo con un NUMERO?" → se NO, riscrivi
"Saprò con certezza se l'ho raggiunto?" → se NO, riscrivi
"Contribuisce all'Objective?" → se NO, è il KR sbagliato
"È sotto il mio controllo?" → se NO, scomponi in
qualcosa che controlli
"È raggiungibile nel timeframe?" → se NO, riduci il
target o estendi il tempo
text


---

### 7. COME DEFINIRE LE 3 PRIORITÀ TRIMESTRALI
PROCESSO DI SELEZIONE DELLE 3 PRIORITÀ
═══════════════════════════════════════

STEP 1: Elenca TUTTI i KR del trimestre (tutti i pillar)
Tipicamente 7-9 KR totali.

STEP 2: Per ciascuno, valuta l'IMPATTO con la formula:

text

    IMPATTO = (Dimensione Gap) × (Leva sul Revenue) ×
              (Velocità di Risoluzione)

    Dove:
    ├── Dimensione Gap: quanto sei lontano dal target
    │   (1 = vicino, 5 = lontanissimo)
    ├── Leva sul Revenue: quanto impatta sul revenue
    │   totale se raggiunto
    │   (1 = poco, 5 = moltissimo)
    └── Velocità di Risoluzione: quanto velocemente
        puoi muoverlo
        (1 = lento, 5 = veloce)
STEP 3: Ordina per punteggio IMPATTO (decrescente)

STEP 4: I top 3 sono le tue priorità del trimestre

STEP 5: VERIFICA GERARCHIA
├── Almeno 1 priorità deve riguardare l'Agenzia
│ (a meno che l'Agenzia sia stabile al 🟢)
└── Se nessuna priorità è sull'Agenzia E
l'Agenzia non è 🟢 → ricalibra

STEP 6: Tutto il resto va nella NOT TO DO LIST
Non lo ignori — lo PARCHEGGI consapevolmente.

ESEMPIO:
┌────┬───────────────────────┬─────┬─────┬─────┬───────┐
│ # │ KR │ Gap │ Leva│ Vel │IMPATTO│
├────┼───────────────────────┼─────┼─────┼─────┼───────┤
│ 1 │ Close rate 20%→35% │ 4 │ 5 │ 3 │ 60 │
│ 2 │ Lista email 50→500 │ 5 │ 3 │ 4 │ 60 │
│ 3 │ 12 video YouTube │ 3 │ 3 │ 5 │ 45 │
│ 4 │ 2 referral agenzia │ 3 │ 4 │ 3 │ 36 │
│ 5 │ 1 corso info lanciato │ 4 │ 3 │ 2 │ 24 │
│ 6 │ Bridge info→agenzia 5%│ 4 │ 2 │ 2 │ 16 │
└────┴───────────────────────┴─────┴─────┴─────┴───────┘

PRIORITÀ Q:

Close rate 20%→35% (Agenzia — IMPATTO 60)
Lista email 50→500 (Info-Biz — IMPATTO 60)
12 video YouTube (YouTube — IMPATTO 45)
NOT TO DO Q: Referral, lancio corso, bridge
→ Questi non vengono IGNORATI. Vengono PARCHEGGIATI.
Se rimane tempo e capacità → bonus. Ma non sono focus.

text


---

### 8. PROCESSO DI REVIEW OKR
CADENZA E PROCEDURA DI REVIEW
══════════════════════════════

REVIEW SETTIMANALE (dentro la review settimanale del
Command Center — 20 minuti):
────────────────────────────────────────────────────

Apri lo Sprint Mensile corrente
Per ogni task: è completato, in corso o bloccato?
Se bloccato: qual è il bloccante? Cosa faccio per
rimuoverlo QUESTA settimana?
Focus check: "I task che sto facendo sono quelli
dello sprint?" Se no → riallinea
Aggiorna lo status nella tabella
REVIEW MENSILE (dentro la review mensile del
Command Center — 30 minuti):
────────────────────────────────────────────────────

Close-out dello sprint mensile (compila la tabella)
Aggiorna il progresso % di ogni KR trimestrale
Assegna status 🟢🟡🔴 a ogni KR
SE un KR è 🔴 → "Cosa è andato storto? Cosa cambio?"
Definisci il nuovo sprint mensile (prossimi 5-7 task)
Verifica distribuzione task per pillar
Verifica collegamento task → KR
REVIEW TRIMESTRALE (dentro la review trimestrale del
Command Center — 1 ora e 45 minuti):
────────────────────────────────────────────────────

Close-out OKR trimestrale (compila tabella risultati)
Calcola OKR Completion Rate complessivo
Aggiorna progresso OKR annuali
Rispondi: "Cosa avrei fatto diversamente?"
Definisci OKR del trimestre successivo
Definisci 3 priorità + Not To Do del trimestre
Verifica coerenza verticale (Q+1 → Annuale)
REVIEW ANNUALE (dentro la review annuale — 3 ore):
────────────────────────────────────────────────────

Close-out OKR annuale (risultati finali per ogni KR)
Calcola OKR Completion Rate annuale
Lezioni dell'anno: cosa ha funzionato? Cosa no?
Definisci la nuova VISION per l'anno successivo
Definisci i nuovi OKR annuali
Definisci gli OKR del Q1 del nuovo anno
text


---

## 🔧 COME UTILIZZARE QUESTO FILE

**Quando consultarlo:**
- Quando l'utente chiede di definire obiettivi, priorità, o pianificare (qualsiasi livello)
- Quando l'utente chiede "cosa devo fare questo mese/trimestre/anno"
- Durante ogni review (settimanale per lo sprint, mensile per i KR, trimestrale per gli OKR)
- Quando l'utente ha più di 3 priorità o più di 7 task → usa le regole per forzare la scelta
- Quando l'utente presenta un task scollegato dai KR → segnala e suggerisci di spostarlo nella Not To Do

**Come integrare nella risposta:**
1. Usa il template del livello appropriato (annuale/trimestrale/mensile)
2. Verifica SEMPRE la coerenza verticale (sprint → KR trimestrale → KR annuale)
3. Verifica SEMPRE la distribuzione per pillar (Regola 5)
4. Includi SEMPRE la Not To Do list quando fai planning
5. Quando l'utente propone task → chiedi "Quale KR muove?" Se nessuno → segnala
6. Quando calcoli il progresso → usa la formula semaforo da DASHBOARD_ENGINE.md

---

## 🔗 COLLEGAMENTI

- **Dipende da**: `KB/GERARCHIA_PILLAR.md` (gerarchia pillar per distribuzione task), `KB/DASHBOARD_ENGINE.md` (dati per valutare il progresso)
- **Alimenta**: `KB/DECISION_FRAMEWORK.md` (i gap nei KR alimentano le decisioni), `KB/FILTRO_ANTI_ADD.md` (task scollegati dai KR → Not To Do), `KB/WORKFLOW_CADENZE.md` (le review sono definite qui, le cadenze là)
- **Collegato a**: `KB/CROSS_POLLINATION_ENGINE.md` (gli OKR cross-poll), `KB/RETROSPETTIVA_ENGINE.md` (close-out trimestrale)
- **Custom Instructions**: Sezione 2.2 (OKR), Sezione 5.2, Sezione 6.1 (Scenario 3-4), Sezione 8.2-8.4

---

## 💡 ESEMPI PRATICI

### Esempio: Definizione Sprint Mensile con dati reali

**Situazione:** L'utente dice "Definisci lo sprint di Giugno. OKR Q2: Agenzia - chiudere 3 clienti (1 chiuso finora). Info-Biz - lanciare primo corso. YouTube - pubblicare 8 video (4 fatti)."

**Output generato:**
SPRINT MENSILE — GIUGNO 2025

FOCUS: "Chiudere 2 clienti agenzia e preparare il
lancio del primo corso info-biz"

┌────┬────────────────────────────┬────────┬───────┬──────┬────────┐
│ # │ Task │ Pillar │ KR │ Sett │ Status │
├────┼────────────────────────────┼────────┼───────┼──────┼────────┤
│ 1 │ Inviare 10 outreach/giorno │ AGZ │ KR1 │ S1-4 │ ⬜ │
│ │ per 20 giorni lavorativi │ │ │ │ │
├────┼────────────────────────────┼────────┼───────┼──────┼────────┤
│ 2 │ Follow-up su 5 lead │ AGZ │ KR1 │ S1 │ ⬜ │
│ │ dormienti della pipeline │ │ │ │ │
├────┼────────────────────────────┼────────┼───────┼──────┼────────┤
│ 3 │ Preparare proposta per │ AGZ │ KR1 │ S1-2 │ ⬜ │
│ │ 2 prospect caldi │ │ │ │ │
├────┼────────────────────────────┼────────┼───────┼──────┼────────┤
│ 4 │ Completare contenuto corso │ IB │ KR2 │ S1-3 │ ⬜ │
│ │ (moduli 3-5 di 5) │ │ │ │ │
├────┼────────────────────────────┼────────┼───────┼──────┼────────┤
│ 5 │ Creare sales page corso │ IB │ KR2 │ S3-4 │ ⬜ │
│ │ + email di lancio │ │ │ │ │
├────┼────────────────────────────┼────────┼───────┼──────┼────────┤
│ 6 │ Pubblicare 4 video YT │ YT │ KR3 │ S1-4 │ ⬜ │
│ │ (1/settimana) │ │ │ │ │
├────┼────────────────────────────┼────────┼───────┼──────┼────────┤
│ 7 │ Estrarre 3 clip da webinar │ CROSS │ KR-CP │ S2 │ ⬜ │
│ │ registrato per YouTube │ │ │ │ │
└────┴────────────────────────────┴────────┴───────┴──────┴────────┘

DISTRIBUZIONE: AGZ 3/7 (43%) ✅ │ IB 2/7 (29%) ✅ │
YT 1/7 (14%) ✅ │ CROSS 1/7 (14%) ✅

NOT TO DO GIUGNO:

Non iniziare un secondo corso prima di lanciare il primo
Non esplorare nuovi canali di acquisizione per l'agenzia
(prima ottimizza outreach e follow-up)
Non iniziare a lavorare su KDP o AI Influencer
text


---

## ⚠️ NOTE E AVVERTENZE

1. **Gli OKR non sono una to-do list.** Gli Objectives sono qualitativi (la direzione), i Key Results sono quantitativi (la misura del progresso). I task specifici stanno nello Sprint Mensile.

2. **Se un KR non viene mai mosso per 2 mesi consecutivi**, ha 2 possibilità: o è irrealistico (riducilo), o non è una vera priorità (rimuovilo e mettilo nella Not To Do).

3. **La Not To Do list è un DOCUMENTO ATTIVO**, non un cestino. Le cose nella Not To Do non sono "rifiutate" — sono "congelate consapevolmente". Si rivalutano a ogni review trimestrale.

4. **Non modificare gli OKR a metà trimestre** tranne in casi estremi (allarme 🔴 da SOGLIE_ALLARME.md). Se modifichi continuamente gli OKR, non hai OKR — hai una lista di desideri che cambia ogni settimana.

5. **Il target di completion >70% è calibrato appositamente.** Se raggiungi sempre il 100%, i tuoi OKR sono troppo facili e non ti stai sfidando. Il 70% significa che hai puntato in alto e ci sei arrivato quasi — il che è perfetto.

6. **Lo Sprint Mensile deve essere definito in MAX 30 minuti.** Se ci metti di più, stai over-thinking. 7 task, collegati ai KR, distribuiti per pillar. Fine.