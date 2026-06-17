---
Type: WORKFLOW
Status: Active
Tags: #workflow #cmo #lancio #info-business #cro #coordinamento
Created: 2026-06-17
Last updated: 2026-06-17
---

# WF-LANCIO-COORD — Workflow Lancio Info-Business Coordinato

> **ID:** WF-CMO-003 · **Owner:** cmo-launch-coordinator · **Trigger:** brief lancio da 02-INFO-BUSINESS
> **Blueprint:** `company/Board-CSuite/_BLUEPRINT/BP-CMO.md`
> **Standard:** CF-grade — gate sales page ≥85 non bypassabile, dry-run obbligatorio, monitoraggio 72h.

---

## Scopo

Coordinare un lancio di prodotto info-business (corso, ebook, community) end-to-end dal lato
marketing: dalla pianificazione alla messa live, con allineamento CRO, gate APSOC ≥85 sulla
sales page, e monitoraggio strutturato delle prime 72 ore post-lancio. Questo workflow garantisce
che nessun lancio parta con materiali non verificati o con un'offerta non allineata tra CMO e CRO.

---

## Pre-condizioni (INPUT obbligatori)

Prima che WF-LANCIO-COORD possa partire:
- `prodotto` — nome e versione del prodotto info-business
- `prezzo` — prezzo approvato da team prezzi + Max (Mandato Art.3.3)
- `data_lancio_target` — data target (realisticamente ≥T+14 dalla ricezione del brief)
- `icp_id` — profilo ICP attivo
- `brand_kit` — DE (per prodotti propri)
- `canali_previsti` — lista canali (email, social, ads)

Un brief senza prezzo approvato NON avvia il workflow: il prodotto non si lancia senza prezzo
confermato (Mandato Art.3.4 — non blocca la costruzione, ma blocca il lancio).

---

## Flusso

```
[STEP 1 — INTAKE E VALIDAZIONE]
  Owner: cmo-launch-coordinator
  Input: brief lancio da 02-INFO-BUSINESS
  Action: valida pre-condizioni; produce timeline inversa dalla data lancio target
  Output: lancio_id + piano lancio (fasi, asset, canali, responsabilità, SLA)
  Gate: prezzo approvato? Se no → BLOCCO. Data realistica? Se no → proposta slittamento.

[STEP 2 — ICP E AUDIENCE]
  Owner: cmo-audience-intel
  Input: icp_id, prodotto
  Action: profila l'audience specifica per questo lancio; identifica il messaggio principale
          (qual è il pain point che risuona di più per questo ICP con questo prodotto?)
  Output: ICP brief lancio + awareness level + obiezioni specifiche per questo prodotto
  Nota: un lancio sbaglia target con la stessa frequenza con cui sbaglia copy.

[STEP 3 — ARCHITETTURA FUNNEL LANCIO]
  Owner: cmo-funnel-architect
  Input: ICP brief lancio, canali previsti
  Action: progetta il funnel dedicato al lancio (pre-lancio → lancio → post-lancio)
          con touch-point, sequenza email, trigger, metriche per nodo
  Output: funnel_lancio_id + APSOC mapping per ogni fase

[STEP 4 — ASSET BRIEF E PRODUZIONE]
  Owner: cmo-launch-coordinator (coordina)
  Sub-step A — via cmo-content-liaison → 03-CONTENT-FACTORY:
    asset visivi (cover, caroselli lancio, grafiche email)
  Sub-step B — via cmo-marketing-liaison → 04-MARKETING:
    copy (sales page draft, sequenza email pre-lancio, email D0, follow-up)
  SLA dichiarata per ogni deliverable con buffer per gate.
  Gate: il copy per la sales page è identificato come sales page? (applica soglia ≥85)

[STEP 5 — ALLINEAMENTO CRO]
  Owner: cmo-launch-coordinator (coordina), CRO (peer)
  Action: allineamento su offerta + pricing + pagina di vendita:
    - Prezzo è dichiarato correttamente? (one-time, nessun canone implicito)
    - CTA è una sola, chiara, a bassa frizione?
    - Garanzia (se presente) è formulata in modo non dependency-language?
    - CRO valida la struttura di conversione tecnica; CMO valida il messaggio.
  Output: allineamento confermato (JSON) | lista discrepanze da risolvere
  Gate: nessun lancio con posizionamento conflittuale tra CMO (messaggio) e CRO (offerta).

[STEP 6 — GATE SALES PAGE (APSOC ≥85)]
  Owner: cmo-brand-voice-warden (via WF-BRAND-GATE)
  Input: sales page copy completa, brand_kit DE, icp_id
  Action: score APSOC + Brand Gate G2
  Gate BLOCCANTE: score <85 → RIFAI (torna a STEP 4B). Nessun bypass. Nessuna eccezione.
  Output: gate_pass: true, score: ≥85 → procede | gate_pass: false → fix e riciclo

[STEP 7 — DRY-RUN E APPROVAZIONE]
  Owner: cmo-launch-coordinator
  Action: per ogni canale con spesa variabile (ads, tool): dry-run costi stimati
          proiezione budget totale, scenario base e scenario con cap
  Gate: OK UMANO su spesa prima di procedere. Non si spende senza conferma.
  Output: dry_run_approvato: true | false (blocco se false)

[STEP 8 — LANCIO]
  Owner: cmo-launch-coordinator
  Pre-condition: gate sales page PASS + allineamento CRO confermato + dry-run approvato
  Action: attiva i canali secondo la sequenza del funnel:
    T-14→T-1: canali pre-lancio (teaser, educazione, urgenza)
    D0: canali lancio (email D0 + social + ads se previste)
  Output: lancio_log.json con timestamp per ogni canale attivato

[STEP 9 — MONITORAGGIO 72H]
  Owner: cmo-performance-analyst + cmo-launch-coordinator
  Timing: ore 4, 24, 48, 72 dal lancio
  Metriche: acquisti (o lead), CVR sales page, open rate email D0, anomalie tecniche
  Gate anomalia: 0 acquisti con traffico attivo nelle prime 4h → alert immediato al conductor
                 (probabile problema tecnico, non di marketing)
  Output: report 72h al conductor + piano post-lancio (follow-up, scarcity se finestra chiude)
```

---

## State (namespace AgentDB)

```
board/cmo/lancio-history/<lancio-id>/
  ├── brief.json              — input iniziale
  ├── piano-lancio.json       — output STEP 1
  ├── icp-brief-lancio.json   — output STEP 2
  ├── funnel-lancio.json      — output STEP 3
  ├── asset-brief/            — brief per 03-CONTENT-FACTORY e 04-MARKETING
  ├── allineamento-cro.json   — output STEP 5
  ├── gate-sales-page.json    — score APSOC + G2 (da WF-BRAND-GATE)
  ├── dry-run.json            — stima costi + flag ok-umano
  ├── lancio-log.json         — timestamp attivazione canali
  └── report-72h.json         — metriche prime 72h
```

---

## Gate non bypassabili

1. **Prezzo approvato** (STEP 1) — nessun lancio senza prezzo firmato da team prezzi + Max.
2. **Gate sales page APSOC ≥85** (STEP 6) — il gate più severo. Mai derogato.
3. **Allineamento CRO** (STEP 5) — nessun messaggio conflittuale tra marketing e offerta.
4. **Dry-run + ok umano** (STEP 7) — nessuna spesa senza approvazione esplicita.

---

## Connessioni

- [[cmo-launch-coordinator]] · `agenti/cmo-launch-coordinator.md`
- [[cmo-conductor]] · `agenti/cmo-conductor.md`
- [[cmo-funnel-architect]] · `agenti/cmo-funnel-architect.md`
- [[cmo-audience-intel]] · `agenti/cmo-audience-intel.md`
- [[cmo-marketing-liaison]] · `agenti/cmo-marketing-liaison.md`
- [[cmo-content-liaison]] · `agenti/cmo-content-liaison.md`
- [[cmo-brand-voice-warden]] · `agenti/cmo-brand-voice-warden.md`
- [[cmo-performance-analyst]] · `agenti/cmo-performance-analyst.md`
- [[WF-BRAND-GATE]] · `workflow/WF-BRAND-GATE.md` (STEP 6 di questo workflow)
- [[02-INFO-BUSINESS]] — ecosistema richiedente
- [[CRO]] — peer di revenue (STEP 5)
- [[MANDATO-EMPIRE]] Art.2 + Art.3.3 (prezzo approvato) + Art.4.1 + Art.4.2 + Art.6.1
