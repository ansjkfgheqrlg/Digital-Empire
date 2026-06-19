---
Type: ARCHITETTURA
Status: Active
Tags: #architettura #content-factory #gerarchia #cf-r0 #mega-reparto #L0
Created: 2026-06-19
Last updated: 2026-06-19
---

# ARCHITETTURA — CF-DE MEGA-REPARTO

> **Reparto:** CF-R0 · **Ecosistema:** 03-CONTENT-FACTORY · **Versione:** v2
> Dossier di riferimento: `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY-V2.md §2`

---

## 1. Gerarchia a 5 livelli

CF-DE non è un reparto con agenti piatti: è un'organizzazione a gerarchia esplicita,
multi-area, con leader, capo area, coordinatori, verificatori e worker. Ogni livello ha
responsabilità definite e non si sostituisce al livello sotto o sopra.

```
LIVELLO 0 — CF-DIRECTOR (leader ecosistema) — CF-R0
│   Ingresso unico ordini, validazione contratto, smistamento aree,
│   gestione priorità coda, KPI globali, escalation Board.
│   Team: 7 agenti (cf-d-lead opus, cf-d-qa, cf-d-dispatch, cf-d-sched,
│          cf-d-budget, cf-d-status, cf-d-learn)
│
├── LIVELLO 1 — CAPO AREA PRE-PRODUZIONE (L1-PRE)
│   │   Supervisiona R1-Strategia & Brief e R2-Brand-Kit Registry.
│   │   Garantisce che ogni ordine abbia brief valido e brand_kit aggiornato
│   │   prima di entrare in produzione. Nessun ordine in produzione senza brief approvato.
│   │
│   ├── LIVELLO 2 — CF-R1 STRATEGIA & BRIEF
│   │       Trasforma ordini in brief eseguibili: angle, hook type, struttura,
│   │       calendario, assegnazione reparti produzione. 8 agenti, 3 workflow.
│   │
│   └── LIVELLO 2 — CF-R2 BRAND-KIT & TENANT REGISTRY
│           Crea, mantiene e valida brand_kit e icp.json per ogni tenant.
│           Custode identità visiva e vocale. Impedisce brand-drift. 6 agenti, 2 workflow.
│
├── LIVELLO 1 — CAPO AREA PRODUZIONE (L1-PROD)
│   │   Supervisiona R3-Video, R4-Testuale, R5-Visual & Design.
│   │   Orchestra i team di produzione, risolve conflitti di capacità,
│   │   sceglie engine. Nessun asset in QA senza gate produzione verde.
│   │
│   ├── LIVELLO 2 — CF-R3 PRODUZIONE VIDEO
│   │       UGC (Higgsfield), avatar (HeyGen), short-form (ffmpeg+TTS).
│   │       Pipeline Soul ID → Image 4K → Motion → Montaggio. 10 agenti, 4 workflow.
│   │
│   ├── LIVELLO 2 — CF-R4 PRODUZIONE TESTUALE
│   │       Articoli, newsletter, caption social, script, copy strutturale.
│   │       Non produce copy persuasivo (→ 04-MKT L2.1). 8 agenti, 3 workflow.
│   │
│   └── LIVELLO 2 — CF-R5 VISUAL & DESIGN / CAROSELLI
│           Caroselli Instagram, thumbnail, grafiche per ads, landing hero.
│           Layer Canva parametrico per brand_kit. 8 agenti, 4 workflow.
│
└── LIVELLO 1 — CAPO AREA POST-PRODUZIONE (L1-POST)
    │   Supervisiona R6-QA & Gate, R7-Pubblicazione & Distribuzione, R8-Apprendimento.
    │   Garantisce che nessun asset esca senza gate verdi.
    │   Presidia il loop di miglioramento.
    │
    ├── LIVELLO 2 — CF-R6 QA & GATE
    │       Gate qualità parametrico per brand_kit: ogni asset viene verificato
    │       contro il brand_kit del tenant prima di uscire. INDIPENDENTE dalla produzione.
    │       Chi produce non si auto-valuta — invariant cardinale non bypassabile.
    │
    ├── LIVELLO 2 — CF-R7 PUBBLICAZIONE & DISTRIBUZIONE
    │       Publish su canali, scheduling, tracciamento distribuzione per committente.
    │
    └── LIVELLO 2 — CF-R8 APPRENDIMENTO & OTTIMIZZAZIONE
            Aggrega dati di performance per formato+brand; alimenta pattern in `cf/patterns`;
            report ciclico → CF-D-LEARN → Board + 07-FORGE.
```

---

## 2. CF-Director è L0

CF-R0 non è un reparto tra altri: è il livello 0 dell'intera gerarchia CF-DE.
Non entra nel merito della produzione — non decide angoli, non sceglie engine, non approva
copy. Decide solo:
- Se un ordine è valido (gate CF-D-QA)
- A quale area va (dispatch CF-D-DISPATCH)
- In quale slot di carico (scheduling CF-D-SCHED)
- Se il budget è nei limiti (CF-D-BUDGET)
- Qual è lo stato real-time (CF-D-STATUS)
- Cosa imparare dall'aggregato di tutto (CF-D-LEARN)

Le decisioni di produzione appartengono ai capi area L1 e ai coordinatori L2.

---

## 3. Le 3 aree operative

| Area | Capo Area | Reparti L2 | Missione |
|---|---|---|---|
| Pre-Produzione | L1-PRE | CF-R1, CF-R2 | Ogni ordine diventa brief+brand_kit validati prima di produrre |
| Produzione | L1-PROD | CF-R3, CF-R4, CF-R5 | Asset prodotti in formato+qualità del committente |
| Post-Produzione | L1-POST | CF-R6, CF-R7, CF-R8 | Gate QA, pubblicazione, apprendimento |

Il flusso è lineare: Pre → Prod → Post. Non si bypassa una fase.
Un ordine in produzione senza brief di Pre-Produzione è un errore di processo: il capo
area L1-PROD deve bloccare e rimandare a CF-R1.

---

## 4. Regola di precedenza coda

CF-D-LEAD applica la regola di precedenza nell'ordine fisso:

1. **deadline** — la scadenza più vicina vince tra ordini di pari tipo
2. **revenue impact** — ordini Agency (SLA clienti firmati) e lanci Info-Business (data pubblica
   annunciata, Mandato Art.2) hanno precedenza su ordini a revenue potenziale e su ordini interni
3. **interno** — gli ordini DE-interno sono l'ultima priorità; non bloccano mai un ordine cliente

Questa regola è non discrezionale: CF-D-LEAD la applica, non la interpreta. Se due ordini
hanno la stessa deadline e stesso revenue impact, il criterio è il timestamp di ricezione
(il più vecchio va prima). Escalation Board solo se la priorità è fisicamente impossibile
da risolvere con le risorse disponibili.

---

## 5. Multi-tenant: la regola brand_kit+icp

CF-DE è un sistema multi-tenant a ordine. Ogni input porta il proprio `brand_kit` + `icp`.
Nessun contenuto viene prodotto senza questi due input (pattern 11 del Piano Maestro — non
negoziabile). Il gate CF-D-QA blocca qualsiasi ordine che non abbia entrambi.

Il GATE-BRAND in produzione è parametrico: ogni agente di produzione legge il brand_kit
dell'ordine, non un mandato fisso. Questa è la differenza strutturale rispetto a un sistema
mono-brand: aggiungere un tenant richiede solo un brand_kit validato, zero modifica al codice.

---

## Connessioni

- [[03-ECOSISTEMA-CONTENT-FACTORY-V2]] · `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY-V2.md §2`
- [[README]] · `README.md` — roster agenti e workflow CF-R0
- [[CF-R2-Brand-Kit-Registry]] · custode brand_kit che CF-D-QA valida
