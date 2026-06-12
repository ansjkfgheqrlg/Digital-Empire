> Fonte: PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY.md sez. 2 (CF-R3)

# CF-R3 — PRODUZIONE TESTUALE

> Reparto L2 di 03-CONTENT-FACTORY · Coordinatore: `CF-R3-A01-text-lead`
> Fonte: dossier 03 §2 (CF-R3), §4c.

---

## Cosa fa

Produce **articoli, newsletter, script video, descrizioni** — contenuto lungo e
strutturato. CF-R3 è il reparto del contenuto editoriale: informare, educare, costruire
autorevolezza per ogni brand della holding.

**Confine chiaro con 04-MARKETING:** CF-R3 produce contenuto, Marketing produce
persuasione. Il copy di conversione (sales, ads) resta a Marketing. Sui pezzi ibridi
(newsletter con CTA, script VSL) CF scrive il corpo e chiede a Marketing il blocco APSOC
via handoff contract: `CF-R3 → 04-MKT/WF-COPY-EMAIL → blocco CTA → CF-R3 assembla`.

### Org interna

| Livello | Team | Contenuto | Owner |
|---|---|---|---|
| L3 | **WF-ARTICOLO** | brief → outline → draft → SEO/AI-SEO pass → formato output (md/html) | CF-R3-A02-writer |
| L3 | **WF-NEWSLETTER** | brief → corpo → blocco CTA (handoff MKT) → email-ready | CF-R3-A02-writer |
| L3 | **WF-SCRIPT** | script video (YouTube lungo, reel, VSL base) per CF-R2 | CF-R3-A02-writer |
| L4 | T-caption | caption + hashtag per canale (lunghezza, tono, emoji policy per brand) | CF-R3-A04-repurposer |
| L4 | T-headline | varianti titolo (usa hook-formulas di carousel-factory) | CF-R3-A01 |
| L4 | T-repurpose | 1 articolo madre → N pezzi derivati (caption, thread, newsletter, shorts) | CF-R3-A04-repurposer |

### Agenti L5 (schede complete in `../../Agenti/`)

| ID | Ruolo | Tier |
|---|---|---|
| CF-R3-A01-text-lead | coordina produzione testuale, sceglie workflow, verifica qualità | sonnet |
| CF-R3-A02-writer | draft articoli, newsletter, script: segue brief.json e brand_kit.voice | sonnet |
| CF-R3-A03-seo-optimizer | SEO + AI-SEO pass (skill `seo-audit`, `ai-seo`, `schema`) | haiku |
| CF-R3-A04-repurposer | derivati multi-formato da un pezzo madre (skill `content-forge`) | haiku |

---

## Come si collega

**Inbound:**
- `CF-R1` → `brief.json` approvato (topic, keyword, icp, formato, canale, tono richiesto).
- `08-INTELLIGENCE` → brief ricerca: trend, fonti, competitor da citare.
- `04-MARKETING/WF-COPY-EMAIL` → blocco CTA APSOC da inserire in newsletter/VSL.

**Outbound:**
- Articolo/newsletter/script finito → `CF-QA-A01` (GATE-COPY + GATE-BRAND) → CF-R5 o committente.
- Script → CF-R2/WF-VIDEO come input per la produzione video.
- Derivati da T-repurpose → CF-R4 (caption per caroselli, slide copy) o CF-R5 (publish).

**Skill knowledge layer:** `content-forge` (repurposing massivo transcript→derivati),
`seo-audit`, `ai-seo`, `schema` (pass SEO articoli) — referenziate, non duplicate (pattern #6).

---

## Come si ATTIVA e RAGIONA

**Attivazione:** SOLO su brief approvato da CF-R1. Gli script per CF-R2 richiedono anche
il brief video (tipo engine, durata, parametri avatar se VSL).

**Logica di ragionamento (per ogni pezzo):**
1. `memory_search("cf/patterns", brand+formato)` — angoli e formule già validi per questo brand.
2. Carica `brand_kit.json.voice` (tono, esempi sì/no, parole vietate) — ogni frase draft
   viene confrontata mentalmente con i vincoli voice prima di scrivere.
3. Draft strutturato: WF-ARTICOLO segue heading hierarchy; WF-NEWSLETTER apre con hook
   (referenziato da hook-formulas), chiude con CTA placeholder (poi riempito da MKT).
4. SEO pass (WF-ARTICOLO): CF-R3-A03 esegue `seo-optimizer` su keyword, density,
   meta-description, schema — non tocca il tono, solo la struttura tecnica.
5. Gate di uscita da CF-R3: GATE-COPY (struttura, claim verificabili, zero genericità)
   + GATE-BRAND (tone vs brand_kit) prima dell'handoff a QA.

**Failure handling:** brief ambiguo → 1 richiesta strutturata al committente via CF-A00;
draft respinto 2 volte dal gate → escalation CF-R3-A01 + entry `cf/failures`.

## KPI del reparto

| KPI | Definizione | Direzione |
|---|---|---|
| Throughput testuale | articoli/newsletter/script consegnati per settimana | ↑ |
| First-pass rate GATE-COPY | % pezzi che passano senza rework | ↑ |
| Lead time brief→deliverable | ore da brief approvato a testo gate-verde | ↓ |
| Ratio repurposing | pezzi derivati per articolo madre (misura efficienza) | ↑ |

## Connessioni

- [[ECOSISTEMA]] — `company/Ecosistemi/03-CONTENT-FACTORY/ECOSISTEMA.md`
- [[BACKBONE]] — `company/Ecosistemi/03-CONTENT-FACTORY/BACKBONE.md`
- `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY.md` §2, §4c
- `company/Ecosistemi/04-MARKETING/` — handoff blocco APSOC per newsletter/VSL

*Fonte: dossier 03 §2-§4 · Aggiornato: 2026-06-11*
