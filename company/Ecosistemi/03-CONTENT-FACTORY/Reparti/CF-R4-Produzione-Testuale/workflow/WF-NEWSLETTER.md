---
Type: WORKFLOW
Status: Active
Tags: #workflow #CF-R4 #newsletter #handoff #marketing #apsoc #HC-MK-CF-01 #pipeline
Created: 2026-06-23
Last updated: 2026-06-23
---

# WF-NEWSLETTER — Pipeline Newsletter con Handoff MARKETING

> **Reparto:** CF-R4 Produzione Testuale · **Area:** Produzione
> **[WRAPPA-ESISTENTE + TARGET-V2] — confine CF/MARKETING non negoziabile**
> **Dipendenza critica:** blocco APSOC richiede 04-MARKETING attivo con Copy Guild disponibile

---

## Scopo

Produrre newsletter complete: CF-R4 scrive il corpo editoriale (contenuto strutturale,
informativo, narrativo) e il testo dell'email (oggetto, preview text); il blocco di
persuasione/CTA (APSOC) è prodotto da 04-MARKETING Copy Guild via handoff `HC-MK-CF-01`.
CF non scrive persuasione. Il corpo CF e il blocco APSOC vengono merged dal coordinatore
solo dopo che entrambi hanno i propri gate verdi.

---

## Passi del workflow

| # | Passo | Agente | Input | Output | Gate |
|---|---|---|---|---|---|
| 0 | Dry-run preview | CF-R4-WRITE | `brief.json` + `brand_kit.voice` | `02-copy/newsletter-outline.json` (struttura corpo, sezioni, CTA direction per MARKETING) | nessun testo scritto; zero costo |
| 1 | Redazione corpo | CF-R4-WRITE | `brief.json` + `brand_kit` | `02-copy/newsletter-corpo.html` | auto-verifica interna CF-R4-WRITE |
| 2 | Oggetto email ×3 + preview text | CF-R4-CAPTION | `brief.json` + corpo bozza | `02-copy/email-meta.json` (3 varianti oggetto, preview text ≤90 char) | lunghezza rispettata; tono brand |
| 3 | Emissione handoff | CF-R4-COORD | `newsletter-corpo.html` + `email-meta.json` + `brand_kit` + `icp` | `HC-MK-CF-01` emesso a 04-MARKETING | HC emesso e loggato in state.json |
| 4 | Attesa blocco APSOC | CF-R4-COORD | — | attesa HC-MK-CF-01 risposta con `gate_copy_guild: PASS` | SLA dichiarato nel HC; alert se supera SLA |
| 5 | Merge corpo + APSOC | CF-R4-COORD | `newsletter-corpo.html` + blocco APSOC da MARKETING | `02-copy/newsletter-merged.html` | coerenza sezioni; nessun gap nel layout |
| 6 | GATE-COPY interno | CF-R4-QA | `newsletter-merged.html` + `brief.json` + `brand_kit.voice` | `05-qa/gate-copy-internal.json` | struttura, hook apertura, claim verificabili, handoff MARKETING PASS presente |
| 7 | GATE-BRAND interno | CF-R4-QA | `newsletter-merged.html` + `brand_kit.voice` | `05-qa/gate-brand-internal.json` | tone campionato vs brand_kit.voice.esempi |
| 8 | Output finale | CF-R4-COORD | `newsletter-merged.html` + gate PASS | `02-copy/newsletter-final.html` + `email-meta.json` | state.json aggiornato; `pronto_per_cf_r6: true` |

---

## Confine CF / MARKETING (non valicabile)

CF-R4 scrive:
- Il corpo editoriale (racconto, problema, contesto, approfondimento, esempi)
- Oggetto email e preview text (identità del testo, non leva di conversione)
- La struttura della newsletter (sezioni, heading, transizioni)

04-MARKETING Copy Guild scrive:
- Il blocco APSOC (Attenzione → Problema → Soluzione → Obiezioni → CTA)
- La CTA con urgency, anchor, call-to-action misurabile
- L'eventuale PS persuasivo

CF-R4-COORD non avvia il passo 5 (merge) finché `HC-MK-CF-01.gate_copy_guild` non
è `PASS`. Se il blocco APSOC non arriva entro SLA: stato `in_attesa_marketing` in
state.json; CF-R4-COORD alerta CF-Director; il corpo newsletter è pronto ma la
newsletter non viene consegnata parziale.

---

## Handoff HC-MK-CF-01 (schema)

```json
{
  "handoff_id": "HC-MK-CF-01-CF2026-0102",
  "emesso_da": "CF-R4-COORD",
  "destinatario": "04-MARKETING/Copy-Guild",
  "order_id": "CF-2026-0102",
  "brand_kit_path": "brands/brand-agency/brand-kit.json",
  "icp_path": "brands/brand-agency/icp.json",
  "corpo_path": "orders/CF-2026-0102/02-copy/newsletter-corpo.html",
  "meta_path": "orders/CF-2026-0102/02-copy/email-meta.json",
  "cta_direction": "iscrizione al corso di punta; azione: landing page corso",
  "awareness_level": "problem-aware",
  "deadline_apsoc": "2026-06-25T18:00:00Z",
  "stato": "in_attesa | ricevuto | in_lavorazione | consegnato",
  "gate_copy_guild": null
}
```

Quando 04-MARKETING consegna il blocco APSOC, aggiorna `stato: "consegnato"` e
`gate_copy_guild: "PASS"`. CF-R4-COORD legge il campo prima di avviare il merge.

---

## Gate di uscita

**GATE-COPY (CF-R4-QA, passo 6 — obbligatorio):**
- Struttura newsletter valida: sezioni complete, hook in apertura del corpo
- handoff_marketing_gate: PASS verificato in state.json (campo non bypassabile)
- Zero claim non verificabili nel corpo CF (il controllo sui claim APSOC è in CF-R6-COPY)
- Zero parole_vietate nel corpo e nel testo dell'oggetto email
- Oggetto email nel range di lunghezza per client email (≤60 caratteri per prima variante)

**GATE-BRAND (CF-R4-QA, passo 7 — obbligatorio):**
- Tone of voice del corpo campionato vs brand_kit.voice.esempi_si e esempi_no (≥5 campioni)
- Coerenza tra tono del corpo CF e tono del blocco APSOC (segnala al coord se divergenti)

---

## State machine (state.json durante il workflow)

```json
{
  "order_id": "CF-2026-0102",
  "workflow": "WF-NEWSLETTER",
  "brand": "brand-agency",
  "avviato_il": "2026-06-23T10:00:00Z",
  "fasi": {
    "00-dry-run": { "stato": "completato", "ts": "2026-06-23T10:01:00Z" },
    "01-corpo": { "stato": "completato", "ts": "2026-06-23T10:14:00Z", "corpo_path": "02-copy/newsletter-corpo.html" },
    "02-email-meta": { "stato": "completato", "ts": "2026-06-23T10:16:00Z" },
    "03-handoff-emesso": { "stato": "completato", "ts": "2026-06-23T10:17:00Z", "handoff_id": "HC-MK-CF-01-CF2026-0102" },
    "04-attesa-marketing": { "stato": "completato", "ts": "2026-06-23T14:30:00Z", "gate_copy_guild": "PASS" },
    "05-merge": { "stato": "completato", "ts": "2026-06-23T14:32:00Z", "merged_path": "02-copy/newsletter-merged.html" },
    "06-gate-copy": { "stato": "completato", "ts": "2026-06-23T14:35:00Z", "esito": "PASS" },
    "07-gate-brand": { "stato": "completato", "ts": "2026-06-23T14:37:00Z", "esito": "PASS" },
    "08-output": { "stato": "completato", "ts": "2026-06-23T14:38:00Z", "final_path": "02-copy/newsletter-final.html" }
  },
  "pronto_per_cf_r6": true,
  "stato_finale": "completato"
}
```

---

## Esempio operativo end-to-end

**Ordine:** CF-2026-0102 · brand: brand-agency · formato: newsletter · 500-700 parole corpo
· argomento: "perché il contenuto organico non basta" · CTA direction: landing page corso

**Passo 0 (dry-run):** CF-R4-WRITE → outline corpo: intro-problema + 2 sezioni corpo +
chiusura narrativa aperta (senza CTA, quella viene da MARKETING). Outline approvato.

**Passo 1 (corpo):** CF-R4-WRITE → 620 parole. Hook apertura: "Ogni settimana pubblichi
contenuto. Ogni settimana aspetti che succeda qualcosa." Corpo: 2 sezioni con esempi
concreti senza dati inventati. Chiusura: "La differenza non è quanto pubblichi."

**Passo 2 (email-meta):** CF-R4-CAPTION → 3 varianti oggetto:
- "Il contenuto che non converte (e perché)"
- "Stai pubblicando nel vuoto?"
- "La trappola del contenuto organico"
Preview text: "Ogni settimana pubblichi. Ogni settimana aspetti. Ecco il problema."

**Passo 3 (handoff):** CF-R4-COORD emette HC-MK-CF-01 a 04-MARKETING con deadline +4h.

**Passo 4 (attesa):** 04-MARKETING Copy Guild consegna blocco APSOC 3h45m dopo. `gate_copy_guild: PASS`.

**Passo 5 (merge):** corpo CF + blocco APSOC → `newsletter-merged.html` (layout: corpo → blocco CTA → footer).

**Passi 6-7 (gate):** CF-R4-QA → GATE-COPY PASS (handoff MARKETING PASS in state.json confermato);
GATE-BRAND PASS (tono coerente in entrambe le sezioni).

**Passo 8 (output):** `newsletter-final.html` + `email-meta.json`. `pronto_per_cf_r6: true`. Lead time: 4h38m.

---

## Connessioni

- [[cf-r4-coord]] · `agenti/cf-r4-coord.md` — orchestra il workflow e gestisce il handoff
- [[cf-r4-write]] · `agenti/cf-r4-write.md` — passi 0 e 1
- [[cf-r4-caption]] · `agenti/cf-r4-caption.md` — passo 2
- [[cf-r4-qa]] · `agenti/cf-r4-qa.md` — passi 6 e 7
- [[04-MARKETING-Copy-Guild]] · destinatario HC-MK-CF-01; fornitore blocco APSOC
- [[03-ECOSISTEMA-CONTENT-FACTORY-V2]] · §3 WF-NEWSLETTER e §1 matrice handoff
