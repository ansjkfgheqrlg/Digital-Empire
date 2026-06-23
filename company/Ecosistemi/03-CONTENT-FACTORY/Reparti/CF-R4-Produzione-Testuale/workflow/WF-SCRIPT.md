---
Type: WORKFLOW
Status: Active
Tags: #workflow #CF-R4 #script #video #hook-3s #CF-R3 #gate-copy #pipeline
Created: 2026-06-23
Last updated: 2026-06-23
---

# WF-SCRIPT — Pipeline Script Video per CF-R3

> **Reparto:** CF-R4 Produzione Testuale · **Area:** Produzione
> **[TARGET-V2] — produce script testuale che CF-R3 usa come input per WF-VIDEO-UGC / WF-VIDEO-AVATAR**
> **Gate critico:** hook deve essere operativo nei primi 3 secondi di lettura/recitazione

---

## Scopo

Produrre script video completi e pronti per la pipeline CF-R3: YouTube lungo, reel,
VSL base, tutorial. Lo script è strutturato con marcatori espliciti `[HOOK]`, `[CORPO]`,
`[CTA]` e rispetta i vincoli del brand_kit (parole_vietate, tono) e del formato piattaforma
(durata target, ritmo parole al secondo). Output: `script.md` pronto per handoff a
CF-R3 (WF-VIDEO-UGC o WF-VIDEO-AVATAR).

---

## Passi del workflow

| # | Passo | Agente | Input | Output | Gate |
|---|---|---|---|---|---|
| 0 | Struttura script | CF-R4-WRITE | `brief.json` + `brand_kit.voice` + `formato_video` | `02-copy/script-struttura.json` (sezioni, durata per sezione, parole/min target) | durata totale stimate nel range del formato |
| 1 | Redazione script | CF-R4-WRITE | `script-struttura.json` + `brand_kit` | `02-copy/script-draft.md` con marcatori [HOOK] [CORPO] [CTA] | auto-verifica interna: hook in posizione, CTA unica |
| 2 | Varianti titolo | CF-R4-HEADLINE | `brief.json` + titolo video draft | `02-copy/titolo-varianti.json` (×3 per A/B test) | coerenza con hook e con brand_kit.voice |
| 3 | GATE-COPY interno | CF-R4-QA | `script-draft.md` + `brief.json` + `brand_kit.voice` | `05-qa/gate-copy-script.json` | hook nei primi 3s, CTA unica, parole_vietate assenti |
| 4 | Output + handoff CF-R3 | CF-R4-COORD | `script-draft.md` + gate PASS | `02-copy/script-final.md` + handoff a CF-R3 | state.json aggiornato; `pronto_per_cf_r3: true` |

---

## Struttura obbligatoria dello script

Ogni script prodotto da WF-SCRIPT usa i marcatori standard:

```
[HOOK] — 3-8 secondi (≤20-25 parole a velocità normale di recitazione)
Apertura che agancia: domanda provocatoria, affermazione controcorrente, scenario
riconoscibile. Il marcatore [HOOK] deve coprire la prima frase pronunciabile in ≤3s.

[CORPO] — corpo principale per sezioni
Per reel (≤60s): 1-2 sezioni, ognuna con una sola idea.
Per YouTube lungo: sezioni esplicite con heading di regia (es. [SEZIONE: IL PROBLEMA]).
Per VSL base: struttura Problema → Agitazione → Soluzione (no APSOC pieno: quello è MARKETING).

[CTA] — chiusura unica e misurabile
Una sola CTA. Misurabile: link nella bio, commenta con X, vai su [URL]. Non duplicare la CTA.
```

---

## Gate di uscita

**GATE-COPY script (CF-R4-QA, passo 3 — critico):**

| Campo | Condizione PASS |
|---|---|
| `hook_3s` | Il testo nel marcatore [HOOK] è pronunciabile in ≤3s a 130 parole/min (ritmo naturale italiano); ≤25 parole |
| `cta_unica` | Esattamente 1 marcatore [CTA] nel documento; nessuna CTA intermedia nel corpo |
| `parole_vietate_assenti` | Zero occorrenze delle `brand_kit.voice.parole_vietate` nell'intero script |
| `struttura_marcatori` | I marcatori [HOOK], [CORPO], [CTA] sono presenti nell'ordine corretto |
| `durata_stimata` | Conteggio parole / (velocità_target parole/min) = durata in range ±10% del brief |
| `nessun_claim_non_verificabile` | Zero affermazioni quantitative senza fonte; zero promesse garantite |

Un campo con segnaposto non sostituito (testo del template lasciato non compilato)
conta come FAIL su quel campo specifico.

---

## Calcolo durata (formula deterministica)

```
velocità_default = 130 parole/min (parlato italiano naturale per contenuto formativo)
velocità_reel = 150 parole/min (ritmo più incalzante per short-form)
velocità_vsl = 120 parole/min (ritmo deliberato per sales content)

durata_stimata_s = (n_parole / velocità) × 60

Esempio: script 195 parole × (60/130) = 90s → reel IG: fuori range (limite 60s) → FAIL durata
Esempio: script 195 parole × (60/150) = 78s → reel IG: fuori range → riscrivere con brief ridotto
Esempio: script 130 parole × (60/150) = 52s → reel IG: PASS (≤60s con margine)
```

---

## Dry-run (passo 0 — struttura script)

Prima della redazione, CF-R4-WRITE produce la struttura a costo zero:

```json
{
  "order_id": "CF-2026-0103",
  "tipo_workflow": "WF-SCRIPT",
  "dry_run": true,
  "brand": "mentalita-brutale",
  "formato_video": "reel-60s",
  "velocita_parole_min": 150,
  "struttura_proposta": {
    "HOOK": { "durata_s": 3, "parole_stimate": 8, "tipo": "affermazione-controcorrente" },
    "CORPO": { "durata_s": 45, "n_sezioni": 2, "parole_stimate": 112 },
    "CTA": { "durata_s": 7, "parole_stimate": 17, "azione": "commenta con la tua risposta" }
  },
  "parole_totali_stimate": 137,
  "durata_totale_stimata_s": 55,
  "note": "struttura pronta; nessuno script avviato"
}
```

---

## State machine (state.json durante il workflow)

```json
{
  "order_id": "CF-2026-0103",
  "workflow": "WF-SCRIPT",
  "brand": "mentalita-brutale",
  "formato_video": "reel-60s",
  "avviato_il": "2026-06-23T11:00:00Z",
  "fasi": {
    "00-struttura": { "stato": "completato", "ts": "2026-06-23T11:01:00Z", "struttura_path": "02-copy/script-struttura.json" },
    "01-draft": { "stato": "completato", "ts": "2026-06-23T11:09:00Z", "n_parole": 134, "draft_path": "02-copy/script-draft.md" },
    "02-titolo-varianti": { "stato": "completato", "ts": "2026-06-23T11:11:00Z", "n_varianti": 3 },
    "03-gate-copy": { "stato": "completato", "ts": "2026-06-23T11:13:00Z", "esito": "PASS", "n_rework": 0 },
    "04-output": { "stato": "completato", "ts": "2026-06-23T11:14:00Z", "final_path": "02-copy/script-final.md" }
  },
  "pronto_per_cf_r3": true,
  "cf_r3_workflow_target": "WF-VIDEO-UGC",
  "stato_finale": "completato"
}
```

---

## Esempio operativo end-to-end

**Ordine:** CF-2026-0103 · brand: mentalita-brutale · formato: reel-60s
· angle: "la mente che si autosabota nei momenti chiave" · hook_type: affermazione-controcorrente

**Passo 0 (struttura):** velocità 150 p/min; struttura HOOK(3s/8p) + CORPO(45s/112p×2) + CTA(7s/17p) → totale 55s stimate.

**Passo 1 (draft):**
```
[HOOK]
La motivazione non serve. Serve un sistema.

[CORPO]
Ogni volta che stai per fare la cosa difficile, il cervello ti dà un'uscita.
"Inizierò domani." "Non sono pronto." "Forse non è il momento giusto."
Non è pigrizia. È un meccanismo di protezione che funziona contro di te.
Il problema non è la forza di volontà. È che hai costruito un ambiente
che rende l'uscita più facile dell'azione.

[CTA]
Commenta con la prima uscita che usi di più.
```
Auto-verifica: hook ≤8 parole PASS; CTA unica PASS; nessuna parola_vietata PASS.

**Passo 2 (titolo-varianti):**
- "La Motivazione è una Truffa"
- "Il Cervello che Lavora Contro di Te"
- "Nessuna Forza di Volontà: Solo Sistema"

**Passo 3 (GATE-COPY):** hook_3s: "La motivazione non serve. Serve un sistema." = 8 parole × (60/150) = 3.2s → PASS (≤3s con tolleranza frase completa). Tutti i campi: PASS.

**Passo 4 (output):** `script-final.md` → handoff a CF-R3 per WF-VIDEO-UGC. Lead time: 14 minuti.

---

## Connessioni

- [[cf-r4-coord]] · `agenti/cf-r4-coord.md` — orchestra questo workflow e gestisce handoff CF-R3
- [[cf-r4-write]] · `agenti/cf-r4-write.md` — passi 0 e 1
- [[cf-r4-headline]] · `agenti/cf-r4-headline.md` — passo 2
- [[cf-r4-qa]] · `agenti/cf-r4-qa.md` — passo 3 (GATE-COPY script)
- [[CF-R3-Produzione-Video]] · `../CF-R3-Produzione-Video/` — destinatario dello script (WF-VIDEO-UGC o WF-VIDEO-AVATAR)
- [[03-ECOSISTEMA-CONTENT-FACTORY-V2]] · §3 WF-SCRIPT e §5(b) WF-VIDEO pipeline
