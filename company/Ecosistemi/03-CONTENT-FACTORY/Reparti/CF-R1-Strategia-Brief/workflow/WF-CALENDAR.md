---
Type: WORKFLOW
Status: Active
Tags: #workflow #content-factory #CF-R1 #calendario #multi-brand #pianificazione
Created: 2026-06-19
Last updated: 2026-06-19
---

# WF-CALENDAR — Piano Editoriale Multi-Brand

> **ID:** WF-R1-002 · **Owner:** `cf-r1-coord` · **Reparto:** CF-R1 Strategia & Brief
> **Trigger:** richiesta piano editoriale da committente con ordini ricorrenti, o
> avvio automatico ogni venerdì per la settimana successiva

---

## Scopo

Produrre il piano editoriale settimanale per tutti i brand attivi con ordini ricorrenti:
slot (data + ora), formato, brand, owner reparto di produzione. Il piano coordina la
capacità produttiva (R3/R4/R5) e si integra con il calendario ads/organico di
04-MARKETING L2.2 per evitare conflitti. Ogni slot del piano è ancorato a un
brand_kit validato da CF-R2.

**Gate d'uscita:** piano consegnato entro venerdì per la settimana successiva;
ogni slot ha brand_kit validato; slot trend-priority posizionati entro la scadenza
del trend; coordinamento inviato a 04-MARKETING L2.2.

---

## Attori

| Step | Agente | Funzione |
|---|---|---|
| Coordinamento | `cf-r1-coord` | Avvia il workflow, gestisce escalation capacità |
| Pianificazione | `cf-r1-cal` | Costruisce il piano slot per slot, integra mix formati |
| Trend | `cf-r1-trend` | Fornisce trend-attivi per slot trend-priority |
| Gate e coordinamento MKT | `cf-r1-cal` + `cf-r1-coord` | Verifica slot e invia a 04-MARKETING |

---

## Flusso passo-passo

```
[TRIGGER]
Richiesta piano editoriale — trigger: venerdì automatico o richiesta committente
        │
        ▼
[STEP 1] CF-R1-COORD — raccolta dati
  → identifica brand_slugs attivi con ordini ricorrenti (da CF-D-DISPATCH registry)
  → legge vincoli capacità da CF-D-SCHED: slot R3 e R5 disponibili la settimana prossima
  → legge mix_formati richiesti per ogni brand (dal committente o dai default)
  → GATE-0: almeno 1 brand_slug con brand_kit validato? Se 0 → piano vuoto + segnalazione
        │
        ▼
[STEP 2] CF-R1-TREND — recupero trend attivi
  → legge cf/patterns/<brand_slug>/trend-attivi.json per ogni brand
  → filtra: solo trend con scadenza > (oggi + 2 giorni) → trend ancora utili questa settimana
  → produce lista: [{brand_slug, trend_id, scadenza, urgenza}]
        │
        ▼
[STEP 3] CF-R1-CAL — costruzione piano
  → per ogni brand_slug:
    a. carica brand_kit.canali → identifica canali attivi e finestre di pubblicazione ottimali
    b. applica mix formati (default o override dell'ordine)
    c. distribuisce slot nella settimana: alterna formati, rispetta finestre orarie per canale
    d. aggiunge 1 slot trend-priority per brand con trend valido (posizionato entro scadenza)
  → verifica vincoli capacità: tot slot R5 ≤ R5_disponibili; tot slot R3 ≤ R3_disponibili
  → se eccedenza: riduci formati opzionali (non quelli già ordinati) e segnala
  → produce piano_bozza con tutti gli slot
        │
        ▼
[STEP 4] CF-R1-COORD — verifica gate
  → nessun slot con brand_slug senza brand_kit validato da CF-R2?
  → nessun slot trend-priority con scadenza già passata?
  → capacità rispettata?
  → GATE-1: tutte e 3 le condizioni soddisfatte → PASS; anche 1 fallita → aggiusta e rirverifica
        │
        ▼
[STEP 5] CF-R1-CAL — coordinamento 04-MARKETING
  → invia piano_bozza a 04-MARKETING L2.2 (Advertising) via namespace handoff
  → attende risposta (SLA: entro fine giornata del venerdì per non bloccare il piano)
  → se L2.2 segnala conflitti con slot ads: CF-R1-CAL sposta gli slot organici conflittuali
  → se L2.2 non risponde entro SLA: CF-R1-COORD segnala a L1-PRE; piano inviato alla produzione
    senza coordinamento ads (sub-ottimale ma non bloccante)
        │
        ▼
[STEP 6] CF-R1-CAL — finalizzazione e scrittura
  → scrive piano definitivo: cf/calendars/<brand_slug>/settimana-YYYY-WW.json (uno per brand)
  → aggiorna cf/calendars/index.json con riferimento al piano della settimana
  → notifica CF-R1-COORD: piano pronto e disponibile per CF-D-DISPATCH
```

---

## Gate bloccanti

| Gate | Condizione PASS | Owner | Blocca |
|---|---|---|---|
| G0 — Brand attivi | Almeno 1 brand_slug con brand_kit validato presente | CF-R1-COORD | Avvio workflow |
| G1 — Qualità piano | No slot senza brand_kit; no trend scaduti; capacità rispettata | CF-R1-COORD | Scrittura piano |
| G2 — Consegna entro venerdì | Piano scritto entro venerdì per settimana successiva | CF-R1-CAL | Segnalazione ritardo a L1-PRE |

---

## Input / Output del workflow

**Input trigger:**
```json
{
  "richiesta_id": "CAL-2026-W26",
  "tipo": "settimanale_automatico",
  "settimana": "2026-W26",
  "brand_slugs": ["mentalita-brutale", "brand-agency", "brand-education"],
  "mix_override": {
    "brand-education": {"newsletter": 1, "caroselli": 2, "video": 0}
  },
  "vincoli_capacita": {
    "R5_slot": 10,
    "R3_slot": 3,
    "R4_slot": 5
  }
}
```

**Output finale:**
```json
{
  "piano_id": "CAL-2026-W26",
  "settimana": "2026-W26",
  "generato_il": "2026-06-20",
  "brand_coperti": 3,
  "slot_totali": 13,
  "slot_trend_priority": 1,
  "coordinamento_mkt_inviato": true,
  "conflitti_mkt_risolti": 0,
  "piano_path": "cf/calendars/settimana-2026-W26.json",
  "gate_g1": "PASS",
  "consegnato_entro_venerdi": true
}
```

---

## Schema slot piano (struttura)

```json
{
  "slot_id": "W26-01",
  "data": "2026-06-23",
  "ora_pubblicazione": "18:30",
  "brand_slug": "mentalita-brutale",
  "formato": "carosello-ig",
  "owner_reparto": "CF-R5",
  "tipo": "standard | trend-priority | lancio",
  "ordine_ref": "CF-2026-0042 | null",
  "note": ""
}
```

---

## Integrazione con WF-BRIEF

Il piano editoriale è il contenitore di slot; i brief sono il contenuto di ogni slot.
Quando un brief viene completato con gate PASS (WF-BRIEF), CF-R1-COORD associa il
`brief_path` al corrispondente slot del piano (campo `ordine_ref`). I slot senza
brief_path associato alla data di inizio settimana produzione sono segnalati come
"slot orfani" e avviano WF-BRIEF per quell'ordine in modalità prioritaria.

---

## State

File: `cf/calendars/<brand_slug>/settimana-YYYY-WW.json` (uno per brand)
File: `cf/calendars/index.json` (indice tutti i piani attivi)

---

## Connessioni

- [[cf-r1-cal]] · `agenti/cf-r1-cal.md`
- [[cf-r1-trend]] · `agenti/cf-r1-trend.md`
- [[cf-r1-coord]] · `agenti/cf-r1-coord.md`
- [[WF-BRIEF]] · `workflow/WF-BRIEF.md` — popola i brief.json per ogni slot del piano
- [[WF-TREND-BRIEF]] · `workflow/WF-TREND-BRIEF.md` — gestisce i slot trend-priority
- [[04-MARKETING L2-2-Advertising]] · coordinamento calendario ads/organico
