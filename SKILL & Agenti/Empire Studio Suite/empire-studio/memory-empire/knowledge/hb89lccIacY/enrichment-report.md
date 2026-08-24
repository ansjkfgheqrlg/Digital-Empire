# Enrichment Report — hb89lccIacY
## Stage D/E/F/G — Memory Empire

**Video:** 10 strategie PROVATE per EMAIL copywriting per vendere sempre
**Data:** 2026-08-23

---

## Stage D — Connessioni Knowledge Base

| Questo video | Concetto esistente | Connessione |
|-------------|-------------------|-------------|
| Checklist anti-clichè oggetto (KA-04, KA-08) | `Concept_Hook_Anti_Cliche_Checklist` (video 11) | Stesso principio applicato al canale email invece che al copy generico: clickbait ed emoji-clichè sono varianti del "hook riconosciuto come formula" già catalogato. |
| CTR vs CR (KA-05/06/07) | `ab-testing` skill locale, `sample-size-guide.md` | Il video non aggiunge nulla di statisticamente nuovo rispetto alla guida esistente (già rigorosa), ma la distinzione CR/CTR e il caveat "click totali vs per-link" NON erano documentati nella skill `emails` — gap reale colmato. |
| Email lunghe fino a 500 parole (KA-14) | `emails/references/copy-guidelines.md` → sezione "Length" | Il numero (300-500 parole per "story-driven") era già presente nella skill — nessuna modifica necessaria, solo conferma indipendente della soglia. |
| Email reminder di promozione (KA-16) | `emails/references/email-types.md` → "Seasonal Promotions" | Nessun sottotipo esplicito "Promotion Ending Reminder" nella skill — gap segnalato, non ancora colmato (vedi Stage F). |

---

## Stage D — Nuovi Concetti Identificati

1. **CR vs CTR come trappola di lettura metriche** — la stessa cifra di click racconta storie diverse a seconda della base di calcolo; generalizzabile a qualsiasi canale con "sent vs opened vs clicked" (non solo email).
2. **Click totali vs click per-destinazione** — un CTA secondario/distrattivo (link social, video) può gonfiare il CTR complessivo mascherando la sotto-performance del CTA che conta davvero.
3. **"Proof by demonstration" nella CTA finale** — insegnare una tecnica (urgency di fine promo) e applicarla nello stesso respiro alla propria offerta, senza dichiararlo esplicitamente (Pattern P4 in video-analysis.md).

---

## Stage D — Applicazioni DE (dove usare QUESTO contenuto)

| Concetto | Applicazione Digital Empire | Azione |
|----------|------------------------------|--------|
| Subject line rules (KA-02/03/04/08/09) | `emails` (skill locale) — nessuna guida sull'oggetto esisteva nella skill | **FATTO IN QUESTA SESSIONE**: aggiunta sezione "Subject Lines" in `copy-guidelines.md` (limite 50 caratteri, no merge-field iniziale, no clickbait, emoji solo se non clichè). |
| CR vs CTR + click per-link (KA-05/06/07) | `emails` (skill locale) — sezione "Metrics to Track" non distingueva le due basi | **FATTO IN QUESTA SESSIONE**: aggiunta la distinzione CR/CTR e il caveat sul breakdown per-link in `copy-guidelines.md`. |
| Email reminder fine-promo (KA-16) | `emails/references/email-types.md` | **PROPOSTO, non fatto**: aggiungere un sottotipo "Promotion Ending Reminder" sotto "Campaign Emails" (accanto a "Seasonal Promotions") con la regola "ultimi ~5 giorni, aggiungibile a sequenza esistente". Richiede editing più esteso di email-types.md, rimandato per non rallentare l'ingestione sistematica. |
| Checklist anti-clichè subject (KA-04, KA-08) | `Bibbia dei Messaggi Outreach` / `rule_keeper_lint.py` | **PROPOSTA GIA' SEGNALATA in video 11**, questo video la rinforza con l'angolo email specifico (oggetto, non solo hook generico). Ancora non implementata. |

---

## Stage E — Gate di Qualità

| Check | Status | Note |
|-------|--------|------|
| NO-FINTO | PASS | 13/13 frame descritti letti nativamente (campionamento giustificato: formato uniforme verificato) |
| P12 traceability | PASS | Ogni KA ha source video#timestamp + frame |
| Coverage sezioni | PASS | 11 sezioni (10 capitoli + outro), tutte rappresentate nei KA |
| Quote dirette VTT | PASS | Trascrizione integrale in contenuto-integrale.md |
| Pattern estratti | PASS | 4 pattern operativi in video-analysis.md |
| Connessioni KB | PASS | 4 connessioni documentate |
| Nuovi concetti | PASS | 3 nuovi concetti, 1 pagina wiki concept creata |
| Applicazioni DE | PASS | 4 applicazioni, 2 già implementate (skill `emails` patchata 2 volte) |

**GATE: PASS**

---

## Stage F — Applicazione

**Fatto in questa sessione:**
1. Sezione "Subject Lines" aggiunta a `emails/references/copy-guidelines.md`.
2. Distinzione CR/CTR + caveat click-per-link aggiunta alla stessa sezione "Metrics to Track".

**Priorità prossima sessione (non fatto):**
1. Sottotipo "Promotion Ending Reminder" in `emails/references/email-types.md`.
2. Estendere il gate anti-clichè (già in `cro-copy-architect`) con la variante subject-line specifica per email.

---

## Stage G — Audit

**Lacune:**
- Video quasi interamente teorico/parlato, un solo esempio numerico concreto (worked example CR/CTR) e un solo overlay riassuntivo — meno "visivo" degli altri video del run, coerente col fatto che il topic (metriche, regole di oggetto) si presta più al parlato che alla dimostrazione schermo.
- Il capitolo 8 (A/B testing) è il più lungo (149s) e denso — 4 KA solo da questo capitolo, giustificato dalla quantità reale di sotto-regole indipendenti (cosa testare, sample size, stesso orario).
- Nessuna skill `analytics` toccata in questa sessione nonostante la pertinenza di CR/CTR — valutare in una sessione dedicata se `analytics` merita lo stesso tipo di sezione "Email CR vs CTR" per chi arriva da quella skill invece che da `emails`.

**Cross-reference:**
- Video 11 (nRm7JLsP1bc) = clichè di hook/apertura copy generico.
- Video 12 (questo) = stesso principio applicato canale-specifico (email: oggetto, non solo hook) + livello metriche (CR/CTR) mai toccato prima nel run.

**WATCH-001:** Al completamento Stage H → N_video=12, N_MemoryEmpire=12. Verificato post-update MASTER-RUN-TRACKER.

---

## Prossimo Video

**Video 13/29:** `fGpz-uOgr4k` — "email marketing povero, email marketing ricco"
