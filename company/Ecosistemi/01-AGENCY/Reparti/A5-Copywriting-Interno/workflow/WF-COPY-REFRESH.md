---
Type: WORKFLOW
Status: Active
Tags: #workflow #agency #copywriting #refresh #apsoc #ab-test #reply-rate #A5
Created: 2026-06-23
Last updated: 2026-06-23
---

# WF-COPY-REFRESH — Refresh Template Data-Driven

> **ID:** WF-A5-001 · **Owner:** `ag-a5-coord` + `ag-a5-learn`
> **Reparto:** A5 Copywriting Interno (01-AGENCY)
> **Trigger:** reply rate sotto baseline per 2 cicli (segnale AG-A5-LEARN) o cadenza periodica
> **Evolve:** WF-COPY-OUTREACH del v1 [TARGET-V2]

---

## Scopo

Eseguire un ciclo completo di refresh dei template di outreach sui 3 canali (email, LinkedIn,
Instagram) basato su **dati reali di performance**, non su intuizione. Il flusso parte da un
segnale di calo (AG-A5-LEARN), produce varianti APSOC (AG-A5-WRITE), le fa passare dal Gate
Bibbia (AG-A5-QA), e le porta in test A/B graduale prima di qualsiasi adozione universale.

**Regola fondamentale:** nessun rollout universale senza dati A/B. Ogni variante passa il Gate
Bibbia prima del test. Un confronto A/B su campione insufficiente non adotta nulla: si registra
il learning. (Mandato Art.2 + principio "si ottimizza su dati, mai su opinioni".)

---

## Attori

| Step | Agente A5 | Esterno |
|---|---|---|
| Segnale calo | `ag-a5-learn` | dati da `agency/outreach` (A2/AG-A2-SEND) |
| Avvio refresh | `ag-a5-coord` | — |
| Varianti | `ag-a5-write` | skill `cro-copy-architect`, `market-copy` |
| Verifica obiezioni | `ag-a5-obj` | libreria `agency/a5/obiezioni` |
| Gate Bibbia | `ag-a5-qa` | gate riusato da A2 (`../A2-Acquisizione/agenti/ag-a2-qa.md`) |
| Rollout + A/B | `ag-a5-coord` | A2 (run su batch 10% leads) |
| Verdetto A/B | `ag-a5-learn` | dati reali post-rollout |

---

## Flusso passo-passo

```
[TRIGGER]
AG-A5-LEARN → reply rate template X sotto baseline 2 cicli (o cadenza periodica)
  {canale, template, trend, diagnosi_candidata}
         │
         ▼
[STEP 1] AG-A5-LEARN — diagnosi
  → legge agency/outreach; conferma il calo su dati reali (no intuizione)
  → mappa il pattern su sezione APSOC debole (A / P-S / O-CTA)
  → GATE-1: dato reale presente → prosegui; dato assente/incoerente → stop, richiedi dati ad A2

         │
         ▼
[STEP 2] AG-A5-COORD — apertura refresh
  → crea refresh_id; scrive state in agency/a5/templates/{refresh_id}
  → assegna AG-A5-WRITE: canale + elemento da variare (UNO per variante)

         │
         ▼
[STEP 3] AG-A5-WRITE — produzione varianti
  → produce 3 varianti APSOC, ognuna cambia UN solo elemento (anti-deriva)
  → ancora al problema reale del target (never generic)
  → per le obiezioni: attinge solo coppie validate da AG-A5-OBJ

         │
         ▼
[STEP 4] AG-A5-OBJ — verifica obiezioni
  → ogni obiezione gestita ha risposta con prova reale (validata)?
  → claim senza prova → marca non_validata; rimanda ad AG-A5-WRITE
  → GATE-2: tutte le obiezioni usate sono validate → prosegui

         │
         ▼
[STEP 5] AG-A5-QA — Gate Bibbia (riuso A2, pattern 6)
  → 3 check sequenziali: APSOC (P prima di S) · CTA singola · no dependency + prove
  → FAIL: torna ad AG-A5-WRITE con note specifiche (ciclo mesh)
  → GATE-3: tutte le varianti PASS → autorizzate al test

         │
         ▼
[STEP 6] AG-A5-COORD — rollout graduale
  → consegna ad A2 le varianti per il test su batch 10% leads (NON full rollout)
  → controllo (template attuale) vs varianti, split definito

         │
         ▼
[STEP 7] AG-A5-LEARN — confronto A/B
  → raccoglie reply rate reali per variante vs controllo
  → campione sufficiente?
      sì → verdetto winner / controllo
      no → inconclusivo (non si adotta su rumore)

         │
   ┌─────┴───────────┐
WINNER            INCONCLUSIVO
   │                  │
   ▼                  ▼
[STEP 8a]         [STEP 8b]
Adozione winner   Learning registrato:
→ A2 sostituisce  "variante non distinguibile
  il template      con volume Y"
  attuale          Nessuna adozione.
   │               Si attende più volume.
   ▼
AG-A5-COORD chiude refresh:
agency/a5/templates/{refresh_id}
con esito + variante adottata
agency/a5/performance aggiornato
```

---

## Gate bloccanti

| Gate | Condizione PASS | Owner | Blocca |
|---|---|---|---|
| G1 — Dato reale presente | reply rate reale in `agency/outreach`; calo confermato | AG-A5-LEARN | Avvio refresh |
| G2 — Obiezioni validate | ogni obiezione usata ha prova reale (validata) | AG-A5-OBJ | Gate Bibbia |
| G3 — Gate Bibbia PASS | APSOC (P prima di S) + CTA singola + no dependency/claim | AG-A5-QA | Rollout |
| G4 — Campione A/B sufficiente | volume per distinguere segnale da rumore | AG-A5-LEARN | Adozione winner |

---

## Input / Output del workflow

**Input trigger:**
```json
{
  "trigger": "reply_rate_calo",
  "canale": "email",
  "template": "EMAIL-V3",
  "trend": "in_calo_2_cicli",
  "diagnosi_candidata": "sezione O debole"
}
```

**Output finale (winner):**
```json
{
  "refresh_id": "REFRESH-A5-001",
  "canale": "email",
  "varianti_testate": ["V1", "V2", "V3"],
  "gate_bibbia": "tutte PASS",
  "verdetto_ab": "winner V2",
  "variante_adottata": "V2 — sezione obiezioni con risposta provata 'non ho tempo'",
  "delta_reply_rate": "[DM] — da agency/outreach post-adozione",
  "namespace": "agency/a5/templates/REFRESH-A5-001"
}
```

**Output finale (inconclusivo):**
```json
{
  "refresh_id": "REFRESH-A5-001",
  "verdetto_ab": "inconclusivo",
  "motivo": "volume insufficiente per distinguere le varianti",
  "learning": "ritestare V2 su batch maggiore al prossimo ciclo",
  "variante_adottata": null,
  "namespace": "agency/a5/templates/REFRESH-A5-001"
}
```

---

## State

File: `agency/a5/templates/{refresh_id}/state.json`
- Creato all'avvio del refresh (STEP 2).
- Campo `gate_bibbia` per variante OBBLIGATORIO prima del rollout.
- Campo `verdetto_ab` OBBLIGATORIO alla chiusura: winner / controllo / inconclusivo.
- Ripartibilità a freddo: `last_updated` permette di riprendere dallo step esatto.

---

## Connessioni

- [[ag-a5-learn]] · `agenti/ag-a5-learn.md` — segnale di calo + verdetto A/B
- [[ag-a5-write]] · `agenti/ag-a5-write.md` — produce le varianti APSOC
- [[ag-a5-qa]] · `agenti/ag-a5-qa.md` — Gate Bibbia (riuso A2, pattern 6)
- [[ARCHITETTURA]] · `ARCHITETTURA.md §2.1` — flusso del refresh
- [[01-ECOSISTEMA-AGENCY-V2]] · `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md §A5 WF-COPY-REFRESH`
