---
Type: WORKFLOW
Status: Active (TARGET-V2 — evolve WF-REPLY-FOLLOWUP del v1)
Tags: #workflow #agency #acquisizione #outreach #reply #booking #triage #pii #A2
Created: 2026-06-22
Last updated: 2026-06-22
---

# WF-REPLY-BOOKING — Da risposta positiva a call prenotata

> **ID:** WF-A2-REPLY · **Owner:** `ag-a2-coord` · **Reparto:** A2 Acquisizione (01-AGENCY)
> **Trigger:** risposta in ingresso su qualsiasi canale (event-driven, `reply_monitor.py`)
> **ADR-003:** WRAPPA `reply_monitor.py`, `conversation_manager.py`, `run_reply_manager.py`. Zero modifiche al codice.

---

## Scopo

Trasformare una risposta positiva in una **discovery call prenotata e confermata**, poi fare
l'handoff ad A8-Closing. È event-driven: si attiva in tempo reale quando arriva una risposta.
Applica le regole non negoziabili: **mai rispondere a un "no" definitivo** (R5), **PII-scan
prima di ogni store** (R3), **nessun handoff senza slot confermato** (R6). Evolve il
WF-REPLY-FOLLOWUP del v1 aggiungendo lo step booking strutturato e gli handoff verso A8/A7.

---

## Attori

| Step | Agente A2 | Motore wrappato [WRAPPA] / handoff |
|---|---|---|
| Rilevamento risposta | `ag-a2-triage` | `reply_monitor.py` |
| Classificazione | `ag-a2-triage` | skill `outreach-reply-triage` |
| Gestione conversazione / obiezione | `ag-a2-fup` | `followup_writer.py`, `conversation_manager.py` |
| Proposta + conferma slot | `ag-a2-book` | `conversation_manager.py` |
| Handoff finale | `ag-a2-book` | `HC-AG-CL-01` → A8 · `HC-AG-AM-01` → A7 |

---

## Flusso passo-passo

```
[TRIGGER] risposta in ingresso (email / LinkedIn / Instagram)
         │
         ▼
[STEP 1] AG-A2-TRIAGE — rilevamento + classificazione
  → reply_monitor.py rileva la nuova risposta
  → skill outreach-reply-triage classifica in 4 categorie:
       interessato / obiezione / no / out-of-office
  → PII-scan (aidefence_has_pii) PRIMA dello store
  → scrive thread in agency/02-acquisizione/reply/ (no PII)

         │
         ▼
[STEP 2] Routing per categoria
  ├── "no"            → CHIUDE il thread. Nessun follow-up (REGOLE R5). FINE.
  ├── "out-of-office" → ripianifica il contatto dopo la data indicata. FINE (per ora).
  ├── "obiezione"     → AG-A2-FUP gestisce l'obiezione (CPB, no dependency-language)
  └── "interessato"   → AG-A2-FUP gestisce la conversazione

         │  (interessato / obiezione gestita)
         ▼
[STEP 3] AG-A2-FUP — gestione conversazione
  → followup_writer.py / conversation_manager.py portano avanti il thread
  → ogni messaggio in uscita passa per il GATE BIBBIA (AG-A2-QA)
  → quando il lead è pronto per la call → passa ad AG-A2-BOOK

         │
         ▼
[STEP 4] AG-A2-BOOK — proposta slot
  → propone slot concreti (date/ore reali, no scarcity falsa)
  → attende conferma esplicita dello slot

         │
         ▼
[STEP 5] GATE BOOKING (R6) — slot confermato?
  ├── NO  → il lead resta in gestione AG-A2-FUP/BOOK. Nessun handoff. Ri-loop step 4.
  └── SÌ  → prosegui all'handoff

         │
         ▼
[STEP 6] AG-A2-BOOK — handoff finale
  → HC-AG-CL-01 → A8-Closing (thread + slot confermato + contesto)
  → HC-AG-AM-01 → A7 Account (anagrafica cliente aperta)
  → aggiorna state: slot_confermato=true, esito=call_confermata
  → obiezioni ricorrenti (anonimizzate) → HC-AG-IN-01 verso 08-INTELLIGENCE
```

---

## Gate bloccanti

| Gate | Condizione PASS | Owner | Blocca |
|---|---|---|---|
| G1 — PII-scan | pii_scan = passed | AG-A2-TRIAGE | Store del thread |
| G2 — No risposta a "no" | categoria != "no" | AG-A2-TRIAGE/FUP | Qualsiasi follow-up a un "no" (R5) |
| **G3 — Gate Bibbia** | 3 check PASS su ogni messaggio in uscita | AG-A2-QA | Invio nel thread |
| **G4 — Slot confermato** | slot_confermato = true | AG-A2-BOOK | Handoff ad A8 (R6) |

---

## Cap reali nelle risposte

Le risposte nei thread non sono soggette ai cap di prospecting (≤500/gg email, 20+20+30/gg LI,
30 DM/gg IG): quelli valgono per l'outreach a freddo in uscita. La gestione conversazione è
1:1 e reattiva. Resta il vincolo: ogni messaggio in uscita passa il gate Bibbia (G3).

---

## Input / Output del workflow

**Input trigger (risposta rilevata):**
```json
{ "thread_id": "TH-0001", "canale": "email", "testo_risposta": "rif. (PII da scansionare)" }
```

**Output finale (handoff ad A8 + A7):**
```json
{
  "handoff": "HC-AG-CL-01",
  "thread_ref": "agency/02-acquisizione/reply/TH-0001",
  "canale_origine": "email",
  "slot_confermato": "YYYY-MM-DDTHH:MM",
  "stato": "call_confermata",
  "anagrafica": "HC-AG-AM-01 → A7"
}
```

---

## State

File: `agency/02-acquisizione/reply/{thread_id}.json` — thread per lead, stato triage, follow-up
inviati, slot, esito. Nessuna PII (REGOLE R3). Ripartibilità a freddo: lo state riflette lo step
esatto del thread; un agente riprende senza riestrarre la conversazione.

---

## Failure

- PII-scan fallito → store bloccato, segnalazione (rischio sicurezza).
- Lead che rinvia ripetutamente lo slot → resta in gestione FUP; non si forza l'handoff.
- 2 reject handoff consecutivi da A8 → escalation ad AG-DIR; rivedere soglia qualifica con A1.
- Risposta ambigua non classificabile → revisione manuale via AG-A2-COORD.

---

## Connessioni

- [[ag-a2-triage]] · `agenti/ag-a2-triage.md` — classifica le risposte
- [[ag-a2-fup]] · `agenti/ag-a2-fup.md` — gestisce la conversazione
- [[ag-a2-book]] · `agenti/ag-a2-book.md` — proposta slot + handoff ad A8/A7
- [[regole/REGOLE]] · `regole/REGOLE.md` — R3 PII, R5 no risposta a "no", R6 no handoff senza slot
