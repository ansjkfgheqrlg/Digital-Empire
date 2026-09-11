---
Type: PROJECT
Status: Active
Tags: #agency #sito #andrei-pascu #tono #immagini-aura #fabbrica-siti #piano
Created: 2026-09-11
Last updated: 2026-09-11 (v2 — riscritto sul sito giusto, BOZZA da chiudere in chat nuova)
---

# DOSSIER 37 (v2) — SITO AGENCY VIVO
## Il sito dell'Agenzia è `agency-empire-landing` — https://agency-empire-landing.vercel.app

> ## ⛔ L'ERRORE DELLA PRIMA VERSIONE, scritto perché non si ripeta
> La v1 (`37-PIANO-SITO-AGENCY-VIVO-v1-SITO-SBAGLIATO.md`, 11/09 18:00-22:00) ha diagnosticato, pianificato,
> **costruito e deployato** su **`agency-empire/`** (`agency-empire-kohl.vercel.app`): **un altro sito**.
> La memoria di progetto (`agency-empire/memory/MEMORY-INDEX.md`) diceva *«Progetto attivo:
> agency-empire-landing»*: l'ho letta e scartata come "stantia". **Ho preferito la mia deduzione a un
> puntatore scritto, e non ho chiesto a Max quale fosse il sito prima di toccare un deploy.**
>
> **Riparato (22:10-22:20):** `agency-empire/` ripristinato integralmente dal tag `agency-empire-v1-20260911`
> (diff contro il tag: vuoto), ridistribuito sullo stesso URL, commit `9a5cc60e`. Il lavoro fatto vive nel
> branch `agency-empire-vivo-wip` su origin: **prototipo riusabile** (§0).
>
> **Regola nuova (memoria + gate F0):** prima di toccare un cantiere si stampa l'URL live del progetto Vercel
> e lo si scrive nel BRIEF **con la conferma scritta di Max**. Un puntatore in memoria vince sulla deduzione.

**Ordine di Max (22:05):** *«Il sito della Agency era agency-empire-landing.vercel.app. Rifai tutto il piano
completamente.»* Metodo invariato: tono di Pascu in ottica nostra, elementi vivi, immagini AURA col copy,
grana su tutto, scritte su foto sempre leggibili. **Piano, non build: il build parte su «vai».**

**Perimetro:** `agency-empire-landing/` (Next.js 16.2.3, Corsia B), 37 sezioni in `src/components/sections/`,
progetto Vercel `agency-empire-landing`. **Non tocca:** `agency-empire/` (chiuso), V4 Piano Impero Vivo, EMP-8M9F.

---

# §0 — COSA SI RIUSA DAL PROTOTIPO (fatto, passato dai gate)

| Pezzo | Dove | Come rientra |
|---|---|---|
| Voce DE (10 regole, formule, lista nera, fatti) | branch wip `agency-empire/cantiere/VOCE.md` | si copia, si aggiornano i fatti (prezzi veri, team di tre) |
| `gate_voce.py` | `.claude/skills/fabbrica-siti/scripts/` (main) | gate di F1 |
| 8 pattern vanilla + 5 esistenti | `.claude/skills/fabbrica-siti/pattern/` (main, PASS) | F3 li avvolge |
| `vivo.css` (canone v3), `<Aura/>`, manifest, `aura_prep.py`, `build_manifest.py`, `analytics.tsx` | branch wip | identici; token adattati ai neri del sito vero (§4) |
| 19 sezioni React | branch wip `src/sections-vivo/` | **riferimento**, non copia (offerta a listino diversa) |
| Tavola Estetica | https://claude.ai/code/artifact/f3fc31e1-b258-4be6-8074-341c021781c9 | invariata |
| LEZIONE del prototipo (6 trappole) | `fabbrica-siti/cantieri/agency-empire-vivo/LEZIONE.md` | valgono uguali |

Ore risparmiate: F1 −50%, F3 −100%, F2 −70%.

---

# PARTE I — DIAGNOSI MISURATA DEL SITO VERO (live, 22:15, `capture/63-agency-landing-vero/`)

| Misura | **agency-empire-landing** | Speedrun | Cosa dice |
|---|---|---|---|
| Altezza desktop / mobile | **38.683 / 64.255 px** (43 schermate) | 33.756 | 15% più lunga della sua pagina più lunga |
| Sezioni | **37** + 5 divider | 34 | 37 sezioni per una chiamata gratuita |
| CTA | **10** → 1 ogni 3.870 px | 40 (1/844) | — |
| Fotografie | **0** (143 media = icone; 1 sfondo `vsl-bg.webp`) | ~15 | **team di tre, nessun volto in pagina** |
| Dimensioni tipografiche / sfondi / heading / blocchi | **186 / 42 / 120 / 880** | ~14 / 3 / 40 / 473 | nessuna scala; **5 famiglie di gradiente** sulle card (arancio, oro, blu, viola, verde): §12 violato 5 volte |
| Prima persona | 4 sezioni su 37 (listen-up, who-guides, my-promise, about-story) | ovunque | la voce c'è e si perde nelle altre 33 |
| Prove | **placeholder**: `results.tsx` `// TODO: incollare case study REALI`, `"Frase testuale del cliente."`, Loom `IL_TUO_ID_LOOM`; VSL con "312 · 24 · 1.4k" finti-live; "99,7% / 100% / 99,8%" | Trustpilot vero | **la sezione più importante è vuota e finge** |
| Barnum / scarsità | *«se sei qui è perché senti il peso»*; *«la finestra è aperta per altri 12 mesi»* | — | le sue debolezze, copiate |
| Legale | Privacy/Termini `href="#"`, `TODO(N1): P.IVA, sede, PEC` nel codice | firma ovunque | manca, e lo sa |

**Diagnosi:** il sito ha già quasi tutti gli elementi di Pascu (ASCOLTA BENE, "Ok ma chi siete?",
capacity-math, self-check, obiezioni, promessa, storia in prima persona) — **tutti di fila, senza foto,
con cinque colori e 880 blocchi**. Manca la **vita** (volti, un accento, respiro) e la **prova** (risultati
= segnaposto). **Tengono:** le 4 sezioni in prima persona (la storia "sei anni fa ero un ragazzo" è vera e
buona), il listino chiaro, i "cosa NON facciamo".

**Fatti dicibili (dal sito):** Outreach Factory **€4.000**, Content Factory **€3.500**, Second Brain **€2.500**,
Engine Room **€8.000** (vs 10.000), 50/50; 7 giorni lavorativi; 90 giorni supporto; garanzia 30 giorni con
rimborso; VPS €5-20/mese del cliente; team **Maximilian (Max), Gael, Leonardo**; agenzia nata gennaio 2026.

---

# PARTE II — I TRE ASSI SUL SITO VERO
- **A Tono:** V1-V10 identiche. Qui la prima persona **si estende** dalle 4 sezioni alle altre. Via Barnum,
  via "12 mesi", via numeri finti-live/senza fonte → 7 giorni · 300/giorno · 0 € + Novacar/Preventa.
- **B Elementi:** catalogo E1-E23 (v1). Sul sito vero **7 esistono già e si rifanno**: listen-up (E6),
  self-check→voto (E5), hierarchy→asse (E9), capacity-math (E15), objections (E7), who-guides+about-story
  (E12), final-offer→checklist (E17). Cinque famiglie di gradiente → **una**: card ink/carta, arancione su
  CTA/numeri/«No.»; i tre sistemi si distinguono con **etichetta mono + numero romano**, non col colore.
- **C Immagini:** regole e pipeline invariate. **Team di tre → 3 ritratti veri** nella stanza + Max nell'hero.
- **D Look:** invariato (Tavola, grana 4 strati + locale, riga su banda scura, `vivo.css`); si adotta la
  **sua** coppia di neri (`#1c1c1c` / `#0a0a0a`, §4).

---

# PARTE III — DA 37 SEZIONI A 20 + CODA

| N | Sezione nuova | Da (`src/components/sections/`) | Foto (posto) | CTA |
|---|---|---|---|---|
| N1 | Hero due colonne (≤ 30 parole sopra il fold) | `hero` | ritratto Max (1) | 1 |
| N2 | Specchio «Ti voglio bene, ma…» + DM vero + voto | `problems` + `self-check` | 22 (2) | — |
| N3 | Tre numeri veri | `science-stats` (via i finti) | — | — |
| N4 | VSL — **solo se il video esiste**, altrimenti non si costruisce | `vsl` | — | 1 |
| N5 | Fascia-lampo + asse (senza 12 mesi) | `competitors` | 16 (5) | — |
| N6 | ASCOLTA BENE. senza Barnum, con prova | `listen-up` | 30 (7) | 1 |
| N7 | La scala: a mano / SaaS / sistema tuo | `hierarchy` + `pillars` | — | — |
| N8 | Le tre fabbriche: cucitura fotografica, dashboard vera, stack in una riga, dettagli tecnici in `<details>` | `systems-showcase` + `service-deep`×3 + `outreach-inside` + `content-output` + `second-brain-inside` + `tool-stack` (**8→1**) | 14 (3), 21 (4), dashboard | 1 |
| N9 | La formula + ORA/CON + il conto del canone | `capacity-math` + `alternatives` | 01 (8) | — |
| N10 | Il processo: 7 giorni, dopo la chiamata, il tuo tempo | `flow-framework` + `clarity` + `your-time` | 35 (9) | 1 |
| N11 | Prove — solo vere (Novacar, Preventa come "consegniamo sistemi che girano"; testimonianze quando esistono con nome/foto/link) | `results` (segnaposto oggi) | — | — |
| N12 | Per chi / cosa NON facciamo | `audience` + `scope-limits` + `no-fluff` | 36 (11) | 1 |
| N13 | Chi siamo — stanza, 3 volti, storia in prima persona (2 paragrafi visibili + resto apribile) | `who-guides` + `builder-not-trainer` + `about-story` | ritratti ×3 (10) | — |
| N14 | I tre sistemi e il prezzo: 3 card ink con etichetta mono, Engine Room, cosa include, 50/50, `data-prezzo` da `src/lib/listino.ts` **una volta** | `pricing-roi` + `bonuses` + `power-deck` + `final-offer` (**4→1**) | — | 1 |
| N15 | Garanzia — 30 giorni, rimborso, una frase | `my-promise` | 25 (12) | 1 |
| N16 | Obiezioni «No.» | `objections` | 29 (13) | — |
| N17 | Cosa ottieni se prenoti — checklist + bottone a bagliore (**CTA principale**) | nuova | — | 1 |
| N18 | FAQ native | `faq` | — | — |
| N19 | Chiusura — dashboard in filigrana | `final-cta` | dashboard | 1 |
| N20 | Coda legale vera (P.IVA, sede, PEC, privacy, cookie: chiude il `TODO(N1)`) | footer | — | — |

**Obiettivi:** ≤ 24.000 px desktop (−38%) · ≤ 40.000 mobile · 20 sezioni + coda, 0 divider · 10 CTA ·
15 foto (`alt` 15/15) · ≤ 12 dimensioni (header/sticky/call-cta compresi) · 3 sfondi + fascia · **0 famiglie
di gradiente** · **0 placeholder / numeri senza fonte** · 100% link 200 · Lighthouse a11y ≥ 95, perf ≥ 85.

---

# PARTE IV — FASI, CRITICHE, V4 (bozza: da chiudere nella chat nuova con i 3 giri)

| # | Fase | Comandi / file | Gate | Forze | Ore |
|---|---|---|---|---|---|
| 0 | F0 | `cd agency-empire-landing && cat .vercel/project.json && npx vercel project ls` → URL nel BRIEF **con la frase di Max delle 22:05** · tag `agency-empire-landing-v1-<data>` + branch + zip fuori repo · Lighthouse baseline · manifest (casting Parte III) · `analytics.tsx` dal wip | tag su origin; BRIEF con URL+conferma; manifest 44 righe | Emperator | 2 |
| 1 | F1 | `cantiere/VOCE.md` (dal wip, fatti aggiornati) · `cantiere/COPY.md` N1-N20 (le 4 sezioni in prima persona del sito vero restano la base) · `gate_voce.py` · `grep "TODO\|IL_TUO\|Frase testuale\|12 mesi\|se sei qui"` = 0 | gate_voce 0; grep 0; APSOC ≥ 80; hero ≤ 30 parole | Emperator + apex-critic | 6 |
| 2 | F2 | `aura_prep.py`, manifest, brief ×11, ritratti ×3, screenshot dashboard | `--check` PASS; `alt` 15/15 | Emperator (+ Max, non blocca) | 2 |
| 3 | F3 | `vivo.css` sui token del sito · `aura.tsx` · `src/lib/listino.ts` · `legal.ts` · **header/sticky/call-cta al canone PRIMA delle sezioni** · commit + tag `canone-v3-landing` | `canone_sync.py` 0 hex; 0 gradienti-card; tag | Emperator | 4 |
| 4 | F4 | N01…N20 + coda; vecchi in `sections/_v1/` (rimossi in commit separato dopo F7) | build verde; canone; `alt`; una voce | Emperator (7 sezioni di voce: N1, N2, N6, N9, N13, N16, N17) + 3 scagnozzi sonnet (13 di struttura) | 14 |
| 5 | F5 | `gate_siti.py dist` · `site_capture.py` sul dev (**porta 3012, distDir diversa dal build**) · MISURA-DOPO | obiettivi o deroga | apex-critic + guild-design | 2 |
| 6 | F6 | Playwright 390, Lighthouse, link 200, prenotazione di prova | a11y ≥ 95, perf ≥ 85, 0 rotti | site-qa ×3 | 2 |
| 7 | F7 | `npx vercel --prod --yes` **dentro `agency-empire-landing/`** · curl+grep H1 nuovo sul live · **curl+grep H1 v1 su `agency-empire-kohl`: deve essere intatto** | 200 + H1 nuovo; l'altro sito intatto | Emperator | 1 |
| 8 | F8 | LEZIONE, INDICE, wiki, CP | riga in INDICE | Emperator | 1 |
| | | | | **≈ 34 h (+20% = 41)** | |

**Decisioni già prese (dalle critiche abbozzate):** conferma del sito = frase di Max citata nel BRIEF · VSL
condizionata al `src` reale · dettagli tecnici delle 8 sezioni "inside" nei `<details>` sotto ogni fabbrica ·
storia in prima persona visibile per 2 paragrafi · listino in un file solo · **hero a due composizioni**
(due colonne col ritratto se `n1-hero.webp` esiste, una colonna con la parola in due strati se manca: mai
un segnaposto nell'hero del sito principale) · tre sistemi distinti senza tre colori (deroga a §12 solo
scritta nel CSS, mai in silenzio).

**Pre-mortem nuovo:** PM0 sito sbagliato (F0 + F7 controllano anche il sito che NON deve cambiare) ·
PM6 `next build` spegne `next dev` (distDir diversa) · PM8 hero con segnaposto · PM9 risultati che fingono.

**Dipendono da Max, non bloccano:** «vai»; ritratto suo (senza → hero a una colonna); ritratti di Gael e
Leonardo; Higgsfield; `src` del video (senza → N4 non esiste); P.IVA/sede/PEC.

**Consigli:** §13 in `CLAUDE-SITI.md` via ADR (*"il cantiere nasce dall'URL live confermato dal proprietario,
mai da una cartella"*); `scripts/apri_cantiere.py` che stampa URL/progetto/ultimo deploy e si ferma senza
conferma; pattern `listino` + hero a due composizioni in `hero-due-strati`.

## Connessioni
- `37-PIANO-SITO-AGENCY-VIVO-v1-SITO-SBAGLIATO.md` · branch `agency-empire-vivo-wip` · `capture/63-agency-landing-vero/`
- `fabbrica-siti/cantieri/agency-empire-vivo/LEZIONE.md` · SINTESI-SISTEMA-COPY / VISIVO · ANATOMIA-DEI-LANCI
