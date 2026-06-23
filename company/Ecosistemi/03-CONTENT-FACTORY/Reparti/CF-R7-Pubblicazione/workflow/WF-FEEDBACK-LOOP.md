---
Type: WORKFLOW
Status: Active
Tags: #workflow #CF-R7 #feedback #metriche #patterns #marketing-analytics #apprendimento
Created: 2026-06-23
Last updated: 2026-06-23
---

# WF-FEEDBACK-LOOP — Raccolta Metriche e Loop di Miglioramento

> **Reparto:** CF-R7 Pubblicazione & Distribuzione · **Area:** Post-Produzione
> **Trigger:** automatico dopo check live (CF-R7-CHECK → tutti_attivi: true)
> **Destinatari:** `cf/patterns` (CF-R8) + 04-MARKETING Analytics + CF-R6 (calibrazione soglie)

---

## Scopo

Chiudere il loop tra pubblicazione e miglioramento del processo produttivo raccogliendo
metriche di engagement a 48h e 7gg, archiviandole in `cf/patterns` e producendo il
pacchetto di handoff per 04-MARKETING Analytics. I dati alimentano CF-R8-HOOK (libreria
hook) e la calibrazione delle soglie gate di CF-R6-LEARN.

**Regola invariante:** almeno 2 misurazioni (48h e 7gg) per chiudere il loop. Nessuna
conclusione su n < 5 pezzi dello stesso tipo/brand: i dati si accumulano in attesa di
corpus sufficiente.

---

## Passi del workflow

| # | Passo | Agente | Trigger | Output | Gate |
|---|---|---|---|---|---|
| 0 | Schedulazione | CF-R7-COORD | check live OK | `state.json → ts_48h, ts_7gg` | Timestamp calcolati da ts_publish |
| 1 | Raccolta metriche 48h | CF-R7-FEEDBACK | `now() >= ts_48h` | `metriche_48h.json` per ogni URL | Dati disponibili da API piattaforma |
| 2 | Store pattern 48h | CF-R7-FEEDBACK | metriche_48h raccolte | `cf/patterns` entry (metriche_7gg: null) | Formato JSON conforme schema |
| 3 | Raccolta metriche 7gg | CF-R7-FEEDBACK | `now() >= ts_7gg` | `metriche_7gg.json` per ogni URL | Dati disponibili da API piattaforma |
| 4 | Aggiornamento pattern | CF-R7-FEEDBACK | metriche_7gg raccolte | `cf/patterns` entry completata | metriche_7gg valorizzate |
| 5 | Handoff 04-MARKETING | CF-R7-FEEDBACK | pattern completato | `cf/handoff-marketing/<id>.json` | n ≥ 5 per batch pattern; singoli sempre inviati |
| 6 | Handoff CF-R8 | CF-R7-FEEDBACK | pattern completato | segnalazione CF-R8-HOOK per analisi | Segnalazione + path pattern |
| 7 | Chiusura ordine | CF-R7-COORD | step 6 completato | `state.json → feedback_loop.completato: true` | Entrambe le misurazioni presenti |

---

## Schema pattern (entry in cf/patterns)

```json
{
  "pattern_id": "CF-2026-0088-ig-001",
  "order_id": "CF-2026-0088",
  "brand": "mentalita-brutale",
  "formato": "carosello-ig",
  "hook_type": "problema-soluzione",
  "angle": "disciplina brutale",
  "canale": "instagram",
  "url": "https://www.instagram.com/p/CxXxXxXxX/",
  "ts_publish": "2026-06-23T09:05:00Z",
  "metriche_48h": {
    "reach": "[DM]",
    "impression": "[DM]",
    "like": "[DM]",
    "commenti": "[DM]",
    "salvataggi": "[DM]",
    "condivisioni": "[DM]",
    "ts_raccolta": "2026-06-25T09:05:00Z"
  },
  "metriche_7gg": {
    "reach": "[DM]",
    "impression": "[DM]",
    "like": "[DM]",
    "commenti": "[DM]",
    "salvataggi": "[DM]",
    "condivisioni": "[DM]",
    "ts_raccolta": "2026-06-30T09:05:00Z"
  },
  "n_pezzi_tipo": "[DM]",
  "nota_pattern": "Misurazione completata. Analisi affidata a CF-R8-HOOK."
}
```

---

## Gate non bypassabili

**GATE 2 MISURAZIONI:**
L'ordine non è chiuso nel feedback_loop finché non esistono sia `metriche_48h` che
`metriche_7gg`. Una sola misurazione = entry incompleta = loop non chiuso.

**GATE n ≥ 5 per pattern:**
CF-R7-FEEDBACK non propone pattern e non li segnala come affidabili se il corpus dello
stesso `formato + brand + hook_type` non raggiunge n = 5 pezzi. Registra i dati ma
aggiunge `"nota": "corpus insufficiente per pattern affidabile (n < 5)"`.

**GATE "prove non promesse" (Mandato Art.2):**
Nessuna metrica viene inventata o stimata: solo dati reali dalle API delle piattaforme.
Se l'API non restituisce dati → si registra "non disponibile" con motivo.

---

## I/O JSON completo di esempio

**Input (da state.json passo 0):**
```json
{
  "order_id": "CF-2026-0088",
  "publish_results": [
    { "canale": "instagram", "url": "https://www.instagram.com/p/...", "ts_publish": "2026-06-23T09:05:00Z" }
  ],
  "ts_48h": "2026-06-25T09:05:00Z",
  "ts_7gg": "2026-06-30T09:05:00Z"
}
```

**Output handoff 04-MARKETING (cf/handoff-marketing/CF-2026-0088.json):**
```json
{
  "order_id": "CF-2026-0088",
  "brand": "mentalita-brutale",
  "formato": "carosello-ig",
  "hook_type": "problema-soluzione",
  "canali": ["instagram"],
  "metriche": {
    "instagram": {
      "url": "https://www.instagram.com/p/...",
      "metriche_48h": { "reach": "[DM]", "like": "[DM]", "salvataggi": "[DM]" },
      "metriche_7gg": { "reach": "[DM]", "like": "[DM]", "salvataggi": "[DM]" }
    }
  },
  "note_marketing": "Dati organico Instagram per integrazione con analytics ads campagna brand awareness. N pezzi corpus: [DM].",
  "ts_prodotto": "2026-06-30T09:15:00Z"
}
```

---

## Handoff destinatari

| Destinatario | Cosa riceve | Canale |
|---|---|---|
| `cf/patterns` | Entry JSON completa per ogni post (48h + 7gg) | `memory_store("cf/patterns", ...)` |
| 04-MARKETING Analytics | `cf/handoff-marketing/<order_id>.json` con dati organico | File deposito |
| CF-R8-HOOK | Segnalazione "pattern pronto per analisi" con path | Notifica CF-R8-COORD |
| CF-R6-LEARN | Entry cf/patterns (CF-R6 la legge per calibrare soglie) | Via pattern store |

---

## Gestione dati non disponibili

Se l'API della piattaforma non restituisce metriche:
- Post rimosso dall'utente o account sospeso → nota "metriche non disponibili: post rimosso".
- API rate-limited → retry dopo 6h; max 3 retry; dopo il 3° → "metriche non disponibili: rate-limit API".
- Metriche 48h mancanti dopo 72h → segnalazione CF-R7-COORD; tenta ogni 12h per altri 2 giorni.

In ogni caso: nessuna stima o interpolazione. Solo dati reali o "non disponibile".

---

## Esempio operativo end-to-end

**Ordine:** CF-2026-0088 · brand: mentalita-brutale · IG + LinkedIn · publish 2026-06-23T09:05

**Passo 0 (schedulazione):** ts_48h = 2026-06-25T09:05; ts_7gg = 2026-06-30T09:05. state.json aggiornato.

**Passo 1 (48h — 2026-06-25T09:05):**
- IG: API Instagram Graph → reach/impression/like/salvataggi/commenti/condivisioni.
- LI: API LinkedIn → impression/click/like/commenti.

**Passo 2 (store 48h):** 2 entry in cf/patterns (ig + li) con metriche_7gg: null.

**Passo 3 (7gg — 2026-06-30T09:05):** Stesse metriche raccolte (cumulato a 7 giorni).

**Passo 4 (aggiornamento):** Entry cf/patterns aggiornate con metriche_7gg.

**Passo 5 (handoff MARKETING):** `cf/handoff-marketing/CF-2026-0088.json` prodotto.

**Passo 6 (handoff CF-R8):** Segnalazione CF-R8-COORD → "pattern pronto per analisi".

**Passo 7:** state.json → `feedback_loop.completato: true`. Ordine definitivamente chiuso.

---

## Connessioni

- [[cf-r7-feedback]] · `agenti/cf-r7-feedback.md` — executor di questo workflow
- [[cf-r7-coord]] · `agenti/cf-r7-coord.md` — schedula e chiude il loop
- [[CF-R8-Apprendimento]] · destinatario segnalazione pattern per distillazione
- [[03-ECOSISTEMA-CONTENT-FACTORY-V2]] · `§CF-R7 WF-FEEDBACK-LOOP`
