---
Owner: Max
Controllore: Claude
Origine: WORKFLOW-ESTATE/01-FLUSSI-E-PIANI/PLANNING-P7-MASTER-PLAN.md
Governo: company/Mandato/MANDATO-EMPIRE.md
---

# PIANO COMPLETAMENTO WORKFLOW-ESTATE — **LIVELLO 1** (inventario grezzo)
> 2026-07-23 · Claude · Scopo: elencare TUTTO ciò che manca perché il Workflow Estate sia finito.
> L1 non ottimizza e non decide: **misura e elenca**. Lo migliora L2, che a sua volta è migliorato da L3.

## 0. Metodo di misura (non opinione)
Stato letto con comandi reali, non dalla prosa dei dossier:
```
python -m empire flow gates          # stato dei 6 gate
python -m empire conform WORKFLOW-ESTATE   # 0 block, 13 info riparabili
grep -c YOUR_STRIPE "Crea siti/Siti CCM/manuale.html"   # 3
cat .env | grep FLIKI                # FLIKI_API_KEY= (VUOTA)
```

## 1. Stato dei 6 gate — verità misurata 2026-07-23

| Gate | Stato reale | Causa |
|---|---|---|
| Gate-DEC | 🔴 | fatto `dec_001_attiva` mai scritto. La decisione È attiva per default (veto scaduto 21/07 h20, ADR-EST-006) ma **nessuno l'ha registrata come dato macchina** |
| Gate-FUNNEL | 🔴 | `Crea siti/Siti CCM/manuale.html` contiene ancora 3× `YOUR_STRIPE`. Checkout **non esiste**: la landing è una vetrina che non incassa |
| Gate-CONTATTI | 🔴 | scaduto 23/07 h12 senza conferma umana. `lead.csv` esiste con 7 righe ma nessuna evidenza collegata al gate |
| Gate-S4 | ⏳ | E2E carousel mai dimostrato |
| Gate-S5 | ⏳ | test Fliki mai fatto — **`FLIKI_API_KEY` è vuota nel `.env`** |
| Gate-REV | ⏳ | `anticipi_chiusi = 0` |

## 2. Inventario per stream — cosa manca

### S1 — CONCESSIONARI (`WF-S1-CONCESSIONARI.md`)
- ✅ Esiste: script WA msg1-2-3, argomentario obiezioni, 5 varianti gancio, follow-up G+2/G+5 (`05-TEMPLATES-E-KIT/`), motore outreach live, 61 lead scrapati.
- ❌ Manca: registrazione dei contatti come dato macchina; follow-up automatico G+2/G+5 cablato; tracking risposte; il gate non ha una fonte di verità.

### S2 — MANUALE (`WF-S2-MANUALE.md`)
- ✅ Esiste: `manuale.html`, `thank-you.html`, cartella `emails/`.
- ❌ Manca: **checkout funzionante** (3 placeholder Stripe); nessun fallback attivo benché la ladder sia scritta nel piano; lead-magnet Parte 1 come download; verifica che le 3 email siano caricate da qualche parte.

### S3 — PAGINE (`WF-S3-S4-PAGINE-MENTALITA.md`)
- ✅ Esiste: `carousel-factory` con `generate.js`/`render.js`/`export-all.js` e 4 brand.
- ❌ Manca: batch 7 caroselli mai prodotto; bio→funnel; pubblicazione. **Nota:** Max ha dichiarato IG `crea.illtuo_impero` a ZERO (D-EST-006) → questo stream è discutibile, L2 deve decidere.

### S4 — MENTALITÀ BRUTALE
- ✅ Esiste: brand `mentalita-brutale` nella carousel-factory.
- ❌ Manca: gate QA automatico, scheduler, report engagement. Regola dura di Max: **solo se 100% automatico, altrimenti STANDBY**.

### S5 — YOUTUBE (`WF-S5-YOUTUBE.md`)
- ✅ Esiste: skill `youtube-automation-factory` completa, pacchetto `youtube-niche-scout-analysis` (mappa canali, pattern, 20 idee video, template SEO).
- ❌ Manca: **la chiave Fliki è vuota** → render ladder obbligatoria; nessuna run mai eseguita; canale YouTube non designato (M-EST-8).

### S6 — PREVENTA (`WF-S6-REBRAND-PROMO.md`)
- ✅ Esiste: `preventa-launch-kit` (copy landing, brochure PDF, palette, headline A/B), `preventa-outreach-pack`, `preventa-maps-scraper` (61 lead), sezione sito `03b-preventa.tsx`, `09b-prove-novacar.tsx`.
- ❌ Manca: **case study Novacar in PDF** (cercato su disco: non esiste); landing Preventa standalone; demo video ≤2 min.

### Layer macchina (WF-MASTER / WF-MEM-* / WF-PERF-LOOP)
- ✅ Esiste: `empire/flow` (motore gate), `empire/mem`, `empire/dash`, `empire/registry`, 118 test verdi.
- ❌ Manca: **modulo `inspect`** — la dashboard stampa `n/d (modulo inspect non ancora implementato)` su 6 KPI su 6 della sezione Telemetria. WF-MEM-EOD e WF-MEM-RETRO non sono eseguibili. WF-PERF-LOOP non registra nulla.

## 3. Elenco grezzo dei lavori (L1, non ordinato)
1. Registrare `dec_001_attiva` + far rispettare il default-plus-veto in automatico.
2. Sostituire i placeholder Stripe / attivare la ladder di checkout.
3. Collegare `lead.csv` al Gate-CONTATTI come evidenza.
4. Cablare follow-up automatico G+2/G+5 + tracking risposte.
5. Produrre il case study Novacar in PDF.
6. Costruire la landing Preventa.
7. Registrare la demo video Preventa.
8. Eseguire 1 video YouTube end-to-end con ladder (Fliki è morta).
9. Batch 7 caroselli + QA automatico + scheduler + report (S3/S4).
10. Implementare il modulo `inspect`.
11. Rendere eseguibili WF-MEM-EOD e WF-MEM-RETRO.
12. Riparare i 13 link info del `conform`.
13. Registrare i nuovi artefatti in `REGISTRO-IMPRESA.md` / `skills-map.yaml` (ADR-008, rimasto aperto da CP-20260723-002).

## 4. Limiti dichiarati di L1
- Non distingue ciò che **posso chiudere io** da ciò che **richiede Max** (Stripe, credenziali YouTube, invio reale).
- Non ordina per valore: mette il carosello IG (pagina a zero follower) allo stesso livello del checkout che incassa.
- I "fatto/non fatto" sono binari senza definizione di finito verificabile a macchina.
- Non prevede cosa fare quando un blocco resta chiuso (nessuna ladder operativa).

➡️ **Questi 4 limiti sono l'input di L2.**

---
⛓️ P12: `PIANO-COMPL-L1#estate-2026` · fonti: flow gates 23/07, conform, PLANNING-P7 · migliorato da: [PIANO-COMPLETAMENTO-L2.md](PIANO-COMPLETAMENTO-L2.md)
