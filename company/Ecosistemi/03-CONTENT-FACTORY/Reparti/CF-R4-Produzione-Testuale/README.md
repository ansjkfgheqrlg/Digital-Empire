---
Type: REPARTO
Status: Active
Tags: #reparto #content-factory #produzione-testuale #CF-R4 #articoli #newsletter #script #caption
Created: 2026-06-19
Last updated: 2026-06-19
---

# CF-R4 — Produzione Testuale

> **Ecosistema:** 03-CONTENT-FACTORY · **Area:** Produzione · **Livello:** L2 Reparto
> **Dossier:** `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY-V2.md §CF-R4`
> **Standard:** CF-grade (ADR-007) · **Reparto v2 — wrappa funzioni testuali v1 esistenti (ADR-003)**

---

## Missione

Produrre articoli, newsletter, script video, caption e testi strutturati per tutti
i committenti di CF-DE. CF-R4 produce **contenuto**; il copy di conversione (sales,
ads, blocchi APSOC) è dominio di 04-MARKETING.

**Confine non valicabile:** CF-R4 scrive il corpo editoriale; quando un pezzo richiede
persuasione (CTA APSOC, blocco di vendita), CF-R4 si ferma e richiede il blocco a
04-MARKETING via handoff `HC-MK-CF-01`. Il merge avviene solo dopo che il blocco APSOC
ha ricevuto gate verde dalla Copy Guild di MARKETING.

---

## Cosa fa il reparto

1. **Redige articoli** (blog, knowledge base, pillar) con outline → draft → pass SEO.
2. **Scrive newsletter** — corpo editoriale CF; blocco CTA delegato a 04-MARKETING.
3. **Produce script video** per CF-R3 (hook 3s / corpo / CTA strutturale).
4. **Derivati multi-formato** da un pezzo madre (WF-REPURPOSING).
5. **Caption + hashtag** per canale da brand_kit.voice e limiti piattaforma.
6. **Varianti titolo A/B** (n=3) coerenti con hook del brief.
7. **Gate GATE-COPY** su ogni pezzo prima del passaggio a CF-R6.
8. **Apprende** correlando struttura/angolo con engagement testuale.

## Cosa NON fa

- Non scrive copy di conversione, blocchi APSOC, claim di vendita: quello è 04-MARKETING L2.1.
- Non valida il brand_kit: quello è CF-R2 (Brand-Kit & Tenant Registry).
- Non pubblica: quello è CF-R7 (Pubblicazione & Distribuzione).
- Non produce video: quello è CF-R3 (Produzione Video).
- Non progetta caroselli o visual: quello è CF-R5 (Visual & Design).
- Non approva il budget di produzione: quello è CF-SENT-COST.

---

## Roster del reparto (8 agenti)

| ID | Agente | File | Tipo | Tier | Ruolo |
|---|---|---|---|---|---|
| `CF-R4-COORD` | Coordinatore Produzione Testuale | `agenti/cf-r4-coord.md` | coordinator | sonnet | Orchestra i 4 workflow; gestisce handoff MARKETING; riporta a L1-PROD |
| `CF-R4-QA` | Verificatore Gate Copy | `agenti/cf-r4-qa.md` | verifier | sonnet | GATE-COPY: struttura valida, hook+CTA presenti, zero claim non verificabili; BLOCCA |
| `CF-R4-WRITE` | Senior Writer | `agenti/cf-r4-write.md` | worker | sonnet | Draft articoli/newsletter/script da brief; applica brand_kit.voice |
| `CF-R4-SEO` | SEO/AI-SEO Optimizer | `agenti/cf-r4-seo.md` | worker | haiku | Pass SEO e AI-SEO: keyword, heading, meta, schema; skill seo-audit+ai-seo |
| `CF-R4-REPURP` | Repurposing Specialist | `agenti/cf-r4-repurp.md` | worker | haiku | Derivati multi-formato da pezzo madre; skill content-forge |
| `CF-R4-CAPTION` | Caption & Hashtag Writer | `agenti/cf-r4-caption.md` | worker | haiku | Caption+hashtag per canale da brand_kit.voice e limiti piattaforma |
| `CF-R4-HEADLINE` | Headline Variator | `agenti/cf-r4-headline.md` | worker | haiku | 3 varianti titolo A/B; coerenti con hook del brief |
| `CF-R4-LEARN` | Text Performance Analyst | `agenti/cf-r4-learn.md` | worker | sonnet | Correla struttura/angolo con engagement; pattern in `cf/patterns` |

---

## Workflow del reparto (4 workflow CF-grade)

| ID | File | Scopo | Gate di uscita |
|---|---|---|---|
| **WF-ARTICOLO** | `workflow/WF-ARTICOLO.md` | Brief → outline + draft → SEO pass → QA gate → output md/html | GATE-COPY + GATE-BRAND; BLOCCANTI |
| **WF-NEWSLETTER** | `workflow/WF-NEWSLETTER.md` | Corpo CF + blocco CTA via handoff HC-MK-CF-01 a MARKETING | Merge solo con blocco APSOC approvato; confine non valicabile |
| **WF-SCRIPT** | `workflow/WF-SCRIPT.md` | Script video hook-3s/corpo/CTA per CF-R3 | Hook nei 3s; parole_vietate assenti; gate CF-R4-QA |
| **WF-REPURPOSING** | `workflow/WF-REPURPOSING.md` | Pezzo madre → N derivati; ogni derivato gate indipendente | GATE-COPY + GATE-BRAND su ogni derivato |

---

## Namespace memoria

| Namespace | Contenuto |
|---|---|
| `cf/text` | Testi prodotti: articoli, newsletter, script (`orders/<id>/02-copy/`) |
| `cf/scripts` | Script video pronti per CF-R3 (`orders/<id>/02-copy/script.md`) |
| `cf/captions` | Caption + hashtag per canale (`orders/<id>/02-copy/captions.json`) |

---

## KPI del reparto

| KPI | Owner | Definizione |
|---|---|---|
| Lead time brief→draft | CF-R4-COORD | Minuti tra ricezione brief e draft completo; [DM] baseline |
| GATE-COPY first-pass rate | CF-R4-QA | N. pezzi PASS senza rework / tot pezzi valutati; [DM] target >70% |
| Derivati per pezzo madre | CF-R4-REPURP | N. derivati prodotti / N. pezzi madre elaborati nel periodo; [DM] |

---

## Handoff e connessioni inter-reparto

| Direzione | Reparto/Ecosistema | Cosa transita |
|---|---|---|
| ← riceve da | CF-R1 (Strategia & Brief) | `brief.json` con angle, hook_type, struttura, canali, vincoli_brand |
| ← riceve da | CF-R2 (Brand-Kit Registry) | `brand_kit.json` validato per ogni tenant |
| → consegna a | CF-R3 (Produzione Video) | `script.md` via WF-SCRIPT per render avatar/UGC |
| → consegna a | CF-R6 (QA & Gate) | Testo prodotto per gate finale |
| → consegna a | CF-R7 (Pubblicazione) | Testo con gate verdi per distribuzione |
| ↔ handoff | 04-MARKETING (Copy Guild) | HC-MK-CF-01: CF richiede blocco APSOC; MARKETING consegna blocco approvato |

---

## Principi e regole

- Principi operativi → `principi/PRINCIPI.md`
- Confine CF/MARKETING: CF produce contenuto, MARKETING produce persuasione — invariante assoluta.

---

## Connessioni

- [[03-ECOSISTEMA-CONTENT-FACTORY-V2]] · `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY-V2.md §CF-R4`
- [[CF-R1-Strategia-Brief]] · fornitore brief.json
- [[CF-R3-Produzione-Video]] · destinatario script via WF-SCRIPT
- [[WF-ARTICOLO]] · `workflow/WF-ARTICOLO.md`
- [[WF-NEWSLETTER]] · `workflow/WF-NEWSLETTER.md`
