---
Type: WORKFLOW
Status: Active
Tags: #workflow #CF-R7 #delivery #packager #manifest #committenti #drive #non-social
Created: 2026-06-23
Last updated: 2026-06-23
---

# WF-DELIVERY-PACKAGER — Consegna Committenti Non-Social

> **Reparto:** CF-R7 Pubblicazione & Distribuzione · **Area:** Post-Produzione
> **Canali supportati:** Drive cliente, email (link), WeTransfer/link temporaneo
> **Prerequisito:** gate verdi CF-R6 in state.json obbligatori prima di impacchettare

---

## Scopo

Consegnare asset prodotti dalla pipeline CF-DE a committenti che richiedono i file
direttamente (non pubblicazione social). Tipici casi d'uso: consegna deliverable Content
Factory €3.500 al cliente AGENCY, asset lancio a INFO-BUSINESS, creative ads a MARKETING
per campagne, copertine KDP a MULTI-BUSINESS. Il workflow garantisce tracciabilità completa
tramite manifest.json con checksum SHA-256 e conferma di ricezione.

**Dry-run:** produce il manifest.json e la lista asset senza eseguire il trasferimento.
Utile per review committente prima della consegna.

---

## Passi del workflow

| # | Passo | Agente | Input | Output | Gate |
|---|---|---|---|---|---|
| 0 | DRY-RUN (opzionale) | CF-R7-COORD | order.json + state.json | `delivery-plan.json` senza trasferimento | Lista asset e manifest preview |
| 1 | Pre-check gate | CF-R7-QA | state.json + canale consegna | `pre-delivery-verdict.json` | Gate verdi CF-R6 in state.json: tutti PASS |
| 2 | Raccolta asset | CF-R7-DELIVER | `orders/<id>/06-delivery/` | Lista asset verificata | Ogni file presente su disco; corrispondenza con gate in state.json |
| 3 | Naming convention | CF-R7-DELIVER | Lista asset + brand_kit + order | Asset rinominati `[brand]_[formato]_[YYYYMMDD]_[seq]-[versione].[ext]` | Nessun file con nome generico (slide-1.png non conforme) |
| 4 | Checksum | CF-R7-DELIVER | Asset rinominati | SHA-256 per ogni file | Checksum calcolato e verificabile |
| 5 | Manifest.json | CF-R7-DELIVER | Asset + checksum + state.json | `manifest.json` con lista completa | Manifest completo: lista asset + gate + istruzioni |
| 6 | Compressione | CF-R7-DELIVER | Asset + manifest | `.zip` del pacchetto (se >3 file) | Dimensione zip entro soglia canale (Drive: nessun limite, email: <25MB) |
| 7 | Consegna | CF-R7-DELIVER | Pacchetto + canale dichiarato | URL/link/percorso consegna | Consegna completata; URL/path disponibile |
| 8 | Verifica ricezione | CF-R7-CHECK | URL + committente | Conferma o flag attesa | Conferma ricezione committente documentata in state.json |
| 9 | Chiusura ordine | CF-R7-COORD | conferma_ts | state.json `06-delivery.completato: true` | Conferma ricezione ricevuta |

---

## Dry-run (passo 0)

```json
{
  "order_id": "CF-2026-0077",
  "dry_run": true,
  "brand": "agency-brand",
  "committente": "01-AGENCY",
  "delivery_plan": {
    "asset_trovati": [
      { "file": "slide-01.png", "nome_rinominato": "agency-brand_carosello-ig_20260623_001-v1.png", "kb": 480 },
      { "file": "slide-02.png", "nome_rinominato": "agency-brand_carosello-ig_20260623_002-v1.png", "kb": 510 },
      { "file": "caption.txt", "nome_rinominato": "agency-brand_carosello-ig_20260623_caption-v1.txt", "kb": 2 }
    ],
    "n_asset": 3,
    "peso_totale_kb": 992,
    "canale_consegna": "drive",
    "drive_folder_id": "1xXxXxXxXxXxXxXx",
    "manifest_preview": "manifest.json con 3 asset + gate verdi CF-R6"
  },
  "pre_check": { "gate_verdi": true },
  "decisione": "PRONTO — in attesa conferma per eseguire trasferimento"
}
```

---

## Gate non bypassabili

**GATE PRE-DELIVERY (passo 1):**
- Gate verdi CF-R6 in state.json: `gate_formato + gate_brand + gate_copy + gate_mandato: tutti PASS`.
- Nessuna consegna con asset parziali (file mancante in `06-delivery/`).
- Nessuna consegna senza manifest.json prodotto e verificato.

**GATE MANIFEST (passo 5):**
Il manifest.json deve contenere obbligatoriamente:
- Lista completa di tutti gli asset con nome, checksum SHA-256, dimensioni.
- Riferimento all'ordine (`order_id`, `committente`, `brand_kit`).
- Gate verdi estratti da state.json (prova della qualità CF-R6).
- Istruzioni d'uso (canale target, specifiche tecniche, limiti piattaforma).

**GATE RICEZIONE (passo 8):**
L'ordine non è chiuso finché il committente non conferma la ricezione. Se assente dopo
48h → follow-up; dopo 72h → escalation L1-POST.

---

## I/O JSON completo di esempio

**Output finale state.json:**
```json
{
  "order_id": "CF-2026-0077",
  "workflow": "WF-DELIVERY-PACKAGER",
  "fasi": {
    "01-pre-check":    { "stato": "PASS", "gate_cf_r6": "PASS", "ts": "2026-06-23T10:55:00Z" },
    "02-raccolta":     { "stato": "completato", "n_asset": 3, "ts": "2026-06-23T10:56:00Z" },
    "03-naming":       { "stato": "completato", "ts": "2026-06-23T10:56:30Z" },
    "04-checksum":     { "stato": "completato", "ts": "2026-06-23T10:57:00Z" },
    "05-manifest":     { "stato": "prodotto", "manifest_path": "orders/.../06-delivery/manifest.json", "ts": "2026-06-23T10:57:30Z" },
    "06-zip":          { "stato": "completato", "zip_path": "...", "zip_kb": 1100, "ts": "2026-06-23T10:58:00Z" },
    "07-consegna":     { "stato": "completato", "canale": "drive", "drive_url": "https://drive.google.com/file/...", "ts": "2026-06-23T10:59:00Z" },
    "08-ricezione":    { "stato": "in_attesa", "ts_follow_up": "2026-06-25T10:59:00Z" }
  },
  "06-delivery": {
    "consegnato": true,
    "drive_url": "https://drive.google.com/file/...",
    "conferma_ricezione": "in_attesa",
    "ts_consegna": "2026-06-23T10:59:00Z"
  }
}
```

---

## Naming convention (standard CF-DE)

```
[brand_slug]_[formato]_[YYYYMMDD]_[seq]-[versione].[ext]

Esempi:
  mentalita-brutale_carosello-ig_20260623_001-v1.png   ← slide 1
  mentalita-brutale_carosello-ig_20260623_002-v1.png   ← slide 2
  mentalita-brutale_carosello-ig_20260623_caption-v1.txt
  agency-brand_video-ugc_20260623_001-v1.mp4
  mentalita-brutale_carosello-ig_20260623_PACK-v1.zip  ← pacchetto completo
```

La versione `v1` si incrementa su rework richiesti dal committente (v2, v3...).

---

## Esempio operativo end-to-end

**Ordine:** CF-2026-0077 · committente: 01-AGENCY · formato: carosello-ig · consegna: Drive

**Passo 0 (dry-run):** Piano con 3 asset rinominati + manifest preview → inviato ad AGENCY.

**Passo 1 (pre-check):** Gate CF-R6 PASS → procede.

**Passi 2-4:** 3 asset raccolti da `06-delivery/`; rinominati; SHA-256 calcolato per ognuno.

**Passo 5 (manifest):** manifest.json creato con lista 3 asset + gate verdi + istruzioni uso IG.

**Passo 6 (zip):** Archivio `agency-brand_carosello-ig_20260623_PACK-v1.zip` (992KB).

**Passo 7 (consegna):** Caricato su Drive `1xXxXxXxXxXxXxXx`. URL `https://drive.google.com/file/...`.

**Passo 8:** Follow-up schedulato 48h. Notifica 01-AGENCY via HC-AG-CF-01.

**Passo 9:** Dopo conferma AGENCY → `06-delivery.completato: true`. Ordine chiuso.

---

## Connessioni

- [[cf-r7-coord]] · `agenti/cf-r7-coord.md` — orchestra questo workflow
- [[cf-r7-deliver]] · `agenti/cf-r7-deliver.md` — executor passi 2-7
- [[cf-r7-check]] · `agenti/cf-r7-check.md` — verifica ricezione passo 8
- [[CF-R6-QA-Gate]] · fornitore gate verdi prerequisito per la consegna
