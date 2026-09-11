---
Type: PROJECT
Status: Active
Tags: #agency #sito #andrei-pascu #tono #immagini-aura #fabbrica-siti #piano
Created: 2026-09-11
Last updated: 2026-09-12 (v2 chiusa — 3 critiche + V4 esecutivo, in attesa del «vai»)
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

# PARTE IV — LE FASI (ciclo a 9 passi, ADR-006) — P0

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

**Decisioni già prese in bozza (P0):** conferma del sito = frase di Max citata nel BRIEF · VSL condizionata al `src`
reale · dettagli tecnici delle 8 sezioni "inside" nei `<details>` sotto ogni fabbrica · storia in prima persona
visibile per 2 paragrafi · listino in un file solo · **hero a due composizioni** (due colonne col ritratto se
`n1-hero.webp` esiste, una colonna con la parola in due strati se manca: mai un segnaposto nell'hero) · tre sistemi
distinti senza tre colori (deroga a §12 scritta nel CSS, mai in silenzio).

---

# FATTI NUOVI — letti nel codice del sito vero il 2026-09-12 (non erano nella bozza)

| # | Fatto | Dove | Perché pesa |
|---|---|---|---|
| FN1 | **Il sito è NOINDEX** per scelta: `robots: { index: false, follow: false }` | `src/app/layout.tsx:31`, commento `TODO(F1-E4)`: *"indicizzare prima manderebbe traffico su Claude Code Mastery"* | 37 sezioni che Google non vede. `public/robots.txt` dice `Allow: /` — i due file si contraddicono |
| FN2 | **La chiamata si prenota in 3 salti col brand sbagliato**: CTA → `chiamata-formazione.netlify.app` (`<title>` "Call Strategica 1:1 \| **Claude Code Mastery**") → `clinquant-pie-aab8d2.netlify.app` (`<title>` "Ci vediamo il **20 Maggio**! \| Claude Code Mastery") → `calendly.com/max-infoproducer/30min` | `src/components/call-cta.tsx:6` `CALL_URL`; header, hero, about-story, final-cta, final-offer | **L'ultimo metro non esiste** (ADR-016): chi vuole comprare l'agenzia atterra su una pagina del corso con una data di quattro mesi fa |
| FN3 | **Metà delle CTA non prenotano niente**: `BOOKING_URL = "#prenota"` = `id` della sezione listino | `src/lib/constants.ts:1`, `vsl.tsx:6` (ridefinito), `results.tsx`, `systems-showcase.tsx`, sticky | "Prenota una chiamata" che scorre al prezzo |
| FN4 | Sito **statico**: `output: "export"`, `trailingSlash: true`, `basePath` opzionale per l'anteprima GitHub Pages | `next.config.mjs` | i gate girano su `out/`, non su `dist`; la misura si fa servendo `out/`, non con `next dev` (PM6 sparisce) |
| FN5 | Prezzi scritti a mano in **3 file, 11 occorrenze**; `PRICE = "€2.500"` senza dire di cosa | `constants.ts`, `pricing-roi.tsx`, `final-offer.tsx` | un listino che cambia in un posto e non negli altri (lezione Company Brain: *i prezzi vivono SOLO in offerta.md*) |
| FN6 | Nel branch wip esistono già **`/prenota/` con Calendly inline** (`?hide_gdpr_banner=1`, colori nostri, evento `calendly.event_scheduled` letto da `analytics.tsx`), `/privacy/`, `/cookie/` | `agency-empire-vivo-wip:agency-empire/src/app/{prenota,privacy,cookie}/page.tsx` | si copiano: riuso, non costruzione |
| FN7 | Nessun messaggio dell'Outreach linka **alcun** sito (0 URL netlify/vercel/calendly in `Outreach Workflow/`) | grep | la ponte non è urgente; il link al sito nella Bibbia è una riga da BACKLOG |
| FN8 | Ultimo commit sul sito: **2026-09-02** (`84c73c33`); nessun tag `agency-empire-landing-*` | git | F0 deve creare il tag di ritorno |

---

# CRITICA 1 → P1 (attacca P0)

**C1.1 — P0 rifà 37 sezioni e non tocca la porta d'uscita.** Il sito è noindex (FN1) e la chiamata si prenota in
tre salti dentro il brand del corso con "20 Maggio" nel titolo (FN2). Un sito vivo con la voce giusta e 15 foto che
finisce su "Claude Code Mastery" è la ventiseiesima cosa finita mai usata (ADR-016). **Correzione:** N17 è la
sezione-checklist **e** la porta: il bottone a bagliore va a **`/prenota/`**, pagina **nostra**, brand agenzia,
Calendly inline (copiata dal wip, FN6) — **1 salto invece di 3, zero pagine del corso in mezzo**. Tutte e 10 le CTA
puntano lì (`href="/prenota/"`), `#prenota` come ancora sparisce, `CALL_URL`/`BOOKING_URL` diventano **una**
costante in `src/lib/contatti.ts`. Gate F4: `grep -rn "netlify.app\|#prenota" src/` = 0. In F0:
`curl -sI https://calendly.com/max-infoproducer/30min` deve dare 200 (se no, la pagina resta con `mailto:` + numero,
e Calendly va nella lista di Max — non blocca).

**C1.2 — P0 lascia il noindex "a Max" senza dirlo.** Il `TODO(F1-E4)` condiziona l'indicizzazione alla pagina di
prenotazione col brand giusto: con C1.1 quella condizione **si chiude dentro questo cantiere**. **Correzione:** F7
toglie `robots.index:false` **nello stesso commit** del deploy, con gate: `grep -c "netlify.app" out/index.html` = 0
**e** `/prenota/` risponde 200 sul live. `public/robots.txt` e il meta smettono di contraddirsi.

**C1.3 — "`gate_siti.py dist`" e "`site_capture.py` sul dev, porta 3012" sono scritti per un sito che non è
questo.** Il sito è `output: "export"` (FN4): l'HTML finale sta in `out/`, e non serve `next dev` per misurarlo.
**Correzione:** F5 = `npm run build && npx serve out -l 3012` → `gate_siti.py out/` + `site_capture.py
http://localhost:3012 --slug 64-agency-landing-dopo`. Si misura **lo stesso HTML che va in produzione**, e la trappola
PM6 (build che spegne dev) non esiste più perché dev e misura non convivono.

**C1.4 — "Listino in `src/lib/listino.ts` una volta" non dice come si impedisce che torni in tre file.**
Oggi 11 occorrenze in 3 file (FN5). **Correzione:** `listino.ts` esporta `LISTINO = { outreach: 4000, content: 3500,
brain: 2500, engine: 8000, engineListino: 10000, acconto: 0.5 }` + `eur(n)`; `constants.ts` ri-esporta per non
rompere nulla; ogni prezzo in pagina è `{eur(LISTINO.x)}` con `data-prezzo="x"`. **Gate meccanico** in F4 e F5:
`grep -rnE "€ ?[0-9]{1,2}\.[0-9]{3}" src/components src/app` = 0 (l'unica cifra letterale sta in `listino.ts`).
Stessa cosa per i fatti (7 giorni, 90 giorni, 30 giorni, 300/giorno): `src/lib/fatti.ts`, usato dalle sezioni.

**C1.5 — F4 dà 13 sezioni "di struttura" a 3 scagnozzi, ma le due fusioni più difficili (N8 = 8 sezioni → 1,
N14 = 4 → 1) sono lì dentro.** Non sono struttura: sono le due decisioni editoriali del sito (cosa resta delle 8
"inside", cosa resta di power-deck/bonuses). **Correzione:** Emperator scrive **N1, N2, N6, N8, N9, N13, N14, N16,
N17** (9); gli scagnozzi **N3, N5, N7, N10, N11, N12, N15, N18, N19, N20** (10, uno solo per file, con `VOCE.md` +
`COPY.md` della sezione + `canone.json` interi nel prompt); N4 solo se il `src` del video esiste. Header, sticky,
`page.tsx`, `vivo.css`, `listino.ts`: solo Emperator.

**P1 = P0 + `/prenota/` nostra e 10 CTA lì + noindex via in F7 con gate + misura su `out/` servito + listino e
fatti in un file con grep = 0 + riassegnazione di F4. Ore: 34 + 4 = 38.**

---

# CRITICA 2 → P2 (attacca P1)

**C2.1 — P1 mette Calendly su `/prenota/` e non fa i conti col peso: `widget.js` terzo + iframe + cookie di
Calendly.** Sulla home non c'è (bene), ma `/prenota/` non ha un obiettivo di performance e il cookie di terzi tocca
N20 (legale). **Correzione:** `/prenota/` ha gate propri: Lighthouse perf ≥ 70 (non 85: il widget pesa), a11y ≥ 95;
lo script si carica **solo al primo scroll o clic** (`loaded` on demand, già così nel wip); la pagina `/cookie/`
(dal wip) nomina Calendly; il link "cookie" sta nel footer di **tutte** le pagine. Sulla home restano perf ≥ 85.

**C2.2 — Togliere il noindex è un gesto quasi irreversibile: Google indicizza l'H1 di quel giorno.** E l'anteprima
GitHub Pages (`GH_PAGES_BASE`, FN4) diventerebbe **contenuto duplicato** indicizzabile. **Correzione:** `robots` in
`layout.tsx` resta `index:false` **se `GH_PAGES_BASE` è valorizzato** (l'anteprima non si indicizza mai), `index:true`
altrimenti; F7 parte **solo dopo F6 verde** (mai indicizzare una versione che non ha passato i test); `sitemap.xml`
elenca `/`, `/prenota/`, `/privacy/`, `/cookie/` e niente altro.

**C2.3 — N11 "Prove — Novacar, Preventa" nomina due clienti senza dire se abbiamo il permesso.** Un nome senza
consenso scritto è il rovescio di PM9 (risultati che fingono): risultati veri che non possiamo pubblicare.
**Correzione:** N11 a tre livelli, tutti veri: (a) **numeri nostri** che non chiedono permesso a nessuno (l'Outreach
Factory che gira per noi: messaggi/giorno, giorni di setup, 0 € di canone — letti dal DB, non a memoria); (b) nome
del cliente **solo con consenso scritto** (Max lo chiede; **non blocca**: ADR-028); (c) senza consenso → "un
concessionario del Nord Italia" + il numero. Ogni prova ha `data-fonte` sull'elemento (gate PROVE di `gate_siti.py`
lo controlla già). Testimonianze: quelle che esistono con nome/foto/link, anche se sono due; zero stelle finte.

**C2.4 — "VOCE.md dal wip, fatti aggiornati": aggiornati da dove?** Se i fatti li aggiorno "a memoria", il copy
nuovo dice "team di tre" e "sei anni fa" perché li ho letti una volta. **Correzione:** F1 produce
`cantiere/FATTI.md`: una tabella, **ogni numero con la fonte** (file:riga del sito vero, o messaggio di Max con
ora), da cui nascono `fatti.ts` e `listino.ts`. Gate nuovo, piccolo e deterministico:
`gate_fatti.py COPY.md FATTI.md` — estrae ogni cifra da `COPY.md` e fallisce se non sta in `FATTI.md`. Exit 0/1.
Entra in `fabbrica-siti/scripts/` accanto a `gate_voce.py`: vale per ogni sito.

**C2.5 — 38 ore con F4 a 14 ore per 20 sezioni + `/prenota/` + `/privacy/` + `/cookie/` + due fusioni 8→1 e
4→1: no.** Lo stesso errore della v1 (C2.4 di allora, +50%). **Correzione:** F4 = **18 h**, spaccata in **F4a
(N1-N10 + header/sticky)** e **F4b (N11-N20 + `/prenota/` + legali)**: F5 può misurare F4a mentre F4b si scrive.
Budget-guard (ADR-006): sotto il 20% di risorse si chiude con COMMIT della sezione verde, non si apre la prossima.

**P2 = P1 + `/prenota/` con gate propri e cookie dichiarato + noindex legato a `GH_PAGES_BASE` e a F6 + prove a tre
livelli senza nomi non autorizzati + `FATTI.md` con `gate_fatti.py` + F4 in due metà a 18 h. Ore: 38 + 6 = 44.**

---

# CRITICA 3 → P3 (attacca P2)

**C3.1 — P2 costruisce 15 posti-foto, ma il giorno del deploy ne esistono forse 4.** Il casting di Parte III usa
still AURA (22, 16, 30, 14, 21, 01, 35, 36, 25, 29) che **non entrano mai in `public/`** (decisione v1 C2.2:
diritto d'autore/immagine). Senza Higgsfield (dossier 28, gesto di Max) e senza i 3 ritratti, il sito nuovo va
online con **10 buchi** — e P2 non dice cosa si vede in quei buchi. **Correzione:** la regola dell'hero vale per
**tutte** le sezioni con foto: ogni `<Aura posto="n"/>` ha una **composizione B senza immagine** (la colonna
sparisce, il testo prende la larghezza, niente cornice vuota, niente "immagine in arrivo"). Gate F5 doppio:
`gate_siti.py out/` con manifest **pieno** (preview locale, still in `cantiere/aura-preview/` gitignored) **e** con
manifest **vuoto** (quello che va davvero online). Le foto arrivano dopo, senza toccare un componente.

**C3.2 — Gli eventi `cta_click` esistono (wip `analytics.tsx`) ma Vercel Web Analytics si accende dal cruscotto
Vercel: gesto di Max, non nostro.** Senza, tre settimane di zero dati e nessuno se ne accorge. **Correzione:** F0
verifica con `npx vercel project ls` / cruscotto se Analytics è attivo; se no, `analytics.tsx` va comunque in
pagina (è muto finché non si accende) e "accendere Web Analytics su agency-empire-landing" va in cima a
STATO-EMPIRE fra i gesti di Max (ADR-026). In più, indipendente da Vercel: ogni CTA porta `?da=N17` e `/prenota/`
legge il parametro e lo passa all'evento — così quando i dati arrivano si sa **da quale sezione** si prenota.

**C3.3 — `trailingSlash: true` + `basePath` opzionale: un `<a href="/prenota/">` scritto a mano rompe
l'anteprima GitHub Pages, un `<a href="/prenota">` senza slash fa un redirect in più su Vercel.** Dieci CTA
scritte da quattro mani diverse = quattro modi di scriverlo. **Correzione:** tutte le CTA interne usano `<Link>`
di Next (che aggiunge `basePath` da solo) con `href="/prenota/"` da `contatti.ts` — mai `<a href="/…">` grezzo.
Gate F4: `grep -rn '<a href="/' src/` = 0.

**C3.4 — La misura "≤ 24.000 px con 20 sezioni + 15 foto + `<details>`" è stata fissata prima di sapere che 10
foto non ci saranno al deploy (C3.1).** Con la composizione B il sito è **più corto** del previsto e i `<details>`
chiusi non contano: l'obiettivo è facile, quindi non è un obiettivo. **Correzione:** due obiettivi dichiarati, uno
per composizione: **manifest vuoto ≤ 21.000 px**, **manifest pieno ≤ 24.000 px** desktop; mobile 36.000 / 40.000.
Il resto (≤ 12 dimensioni, 3 sfondi + fascia, 0 gradienti-card, 10 CTA, 0 placeholder) vale per entrambe.

**C3.5 — 44 ore senza margine e senza pesi: il battito non può dire una percentuale vera.** **Correzione:** +20%
= **53 h**, dichiarate stima. Pesi per il recap, contati **sul disco** (file esistenti + gate PASS):
F0 5 · F1 20 · F2 5 · F3 15 · F4a 18 · F4b 17 · F5 6 · F6 5 · F7 5 · F8 4 = 100. Una sezione conta solo con
`gate_siti` PASS sul suo file; il 100% è il live con H1 nuovo, noindex tolto e `/prenota/` 200 — non prima.

**P3 = P2 + composizione B su ogni foto e gate doppio pieno/vuoto + analytics che non dipende dal cruscotto per
sapere la sezione + `<Link>` e grep sugli href + due obiettivi di altezza + 53 h con pesi sul disco.**

---

# V4 ESECUTIVO — quello che si esegue, nell'ordine, con i comandi

**Pre-condizione unica:** ordine di Max «vai» + blocco ⚠️ COORDINAMENTO in `STATO-EMPIRE.md` (perimetro:
`agency-empire-landing/`, `fabbrica-siti/scripts/gate_fatti.py`, `fabbrica-siti/cantieri/agency-empire-landing-vivo/`)
+ push. **Non si tocca:** `agency-empire/`, V4 Piano Impero Vivo, EMP-8M9F, Outreach.

Tutti i comandi dalla radice del repo. `$L` = `agency-empire-landing`, `$F` = `.claude/skills/fabbrica-siti`.

| # | Fase | Comandi / file esatti | Gate (condizione → exit 0) | Forze (ADR-015) | Ore | Peso |
|---|---|---|---|---|---|---|
| 0 | **F0 Apertura** | `cat $L/.vercel/project.json` (`projectName` deve essere `agency-empire-landing`) · `cd $L && npx vercel project ls` · `curl -sI https://agency-empire-landing.vercel.app` 200 · `curl -sI https://calendly.com/max-infoproducer/30min` · `git tag agency-empire-landing-v1-20260912 && git push origin --tags` · `git archive -o "$TEMP/agency-empire-landing-v1.zip" HEAD:agency-empire-landing` (zip fuori repo) · `$F/cantieri/agency-empire-landing-vivo/BRIEF.md` con URL **e la frase di Max delle 22:05 citata** · `public/aura/manifest.json` (15 posti, casting Parte III, campo `composizione_b: true`) · `src/components/analytics.tsx` dal wip (`git show agency-empire-vivo-wip:agency-empire/src/components/analytics.tsx > $L/src/components/analytics.tsx`) · Lighthouse baseline mobile su live | `project.json` = landing; tag su origin; BRIEF con URL+frase; manifest 15/15 con `alt`,`sorgente`,`composizione_b`; Analytics: attivo o riga in STATO-EMPIRE (Max) | Emperator | 2 | 5 |
| 1 | **F1 Voce + fatti** | `git show agency-empire-vivo-wip:agency-empire/cantiere/VOCE.md > $F/cantieri/agency-empire-landing-vivo/VOCE.md` (10 regole, lista nera, esempi) · `FATTI.md` (ogni numero con fonte file:riga o "Max, ora") · `COPY.md` N1-N20 + `/prenota/` (le 4 sezioni in prima persona del sito vero restano la base; via Barnum, "12 mesi", finti-live, 99,7%) · `python $F/scripts/gate_voce.py …/COPY.md` · **nuovo** `python $F/scripts/gate_fatti.py …/COPY.md …/FATTI.md` · `grep -c "TODO\|IL_TUO\|Frase testuale\|12 mesi\|se sei qui\|99,7" COPY.md` = 0 · N1 ≤ 30 parole sopra il fold | gate_voce 0; gate_fatti 0; grep 0; APSOC ≥ 80 (`cro-copy-architect`); `sentinel-brandvoice` PASS | Emperator scrive; 1 scagnozzo sonnet fa la bozza delle 10 sezioni di struttura; `apex-critic` legge N1-N20 **di fila**: "è una voce sola?" | 8 | 20 |
| 2 | **F2 Immagini** | `git show agency-empire-vivo-wip:agency-empire/scripts/aura_prep.py > $L/scripts/aura_prep.py` · `python $L/scripts/aura_prep.py --manifest public/aura/manifest.json --preview cantiere/aura-preview --out public/aura --check` · brief Higgsfield ×10 (1 riga per posto in `manifest.json`) · ritratti ×3 + screenshot dashboard **da Max, non bloccano** | `--check` PASS; `ls $L/public/aura` ∩ `manifest[sorgente=originale]` = ∅; `cantiere/` in `.gitignore`; `alt` 15/15 | Emperator (+ Max) | 2 | 5 |
| 3 | **F3 Canone + fondamenta** | `git show agency-empire-vivo-wip:agency-empire/src/app/vivo.css > $L/src/app/vivo.css` (token sui neri del sito: `#1c1c1c`/`#0a0a0a`; 0 gradienti-card; arancione < 10%) · `aura.tsx` dal wip (con composizione B) · `src/lib/listino.ts`, `fatti.ts`, `contatti.ts` (`PRENOTA = "/prenota/"`, `CALENDLY = …/30min`), `legal.ts` (P.IVA/sede/PEC: da Max, segnaposto **vuoto** = riga non renderizzata) · `constants.ts` ri-esporta · **header + sticky + call-cta al canone e a `PRENOTA` PRIMA delle sezioni** · `canone.json` (utility ammesse) · `python $F/scripts/canone_sync.py $L` · commit + tag `canone-v3-landing` | `canone_sync.py` 0 hex fuori canone; `grep -rn "netlify.app\|#prenota" $L/src` = 0 nei 3 componenti condivisi; tag esiste | Emperator | 4 | 15 |
| 4a | **F4a Sezioni N1-N10** | `$L/src/components/sections-vivo/N01-hero.tsx … N10-processo.tsx` · vecchie in `sections/_v1/` (rimosse in commit separato dopo F7) · `page.tsx` nuovo ordine · CTA solo via `<Link href={PRENOTA + "?da=Nxx"}>` · prezzi solo `eur(LISTINO.x)` | `npm run build` verde; per sezione `gate_siti.py out/` PASS; `grep -rnE "€ ?[0-9]{1,2}\.[0-9]{3}" src/components src/app` = 0; `grep -rn '<a href="/' src/` = 0; `grep -rn "netlify.app\|#prenota" src/` = 0 | Emperator: N1, N2, N6, N8, N9 · 2 scagnozzi sonnet: N3+N5+N7 / N10 (+N4 solo con `src` video) | 9 | 18 |
| 4b | **F4b Sezioni N11-N20 + pagine** | `N11-prove.tsx … N20-coda-legale.tsx` · `src/app/prenota/page.tsx`, `privacy/page.tsx`, `cookie/page.tsx` dal wip (brand agenzia, Calendly on demand, `?da=` → evento) · `sitemap.xml` a 4 URL · `layout.tsx`: `robots` = `index:false` **solo se** `GH_PAGES_BASE` | idem F4a; `/prenota/` in `out/prenota/index.html`; footer con privacy/cookie su tutte le pagine (`href="#"` = 0) | Emperator: N13, N14, N16, N17, `/prenota/` · 2 scagnozzi sonnet: N11+N12+N15 / N18+N19+N20+legali | 9 | 17 |
| 5 | **F5 Gate + misura (doppia)** | `cd $L && npm run build && npx serve out -l 3012` · `python $F/scripts/gate_siti.py $L/out` · `python "competitor/Andrei Pascu/site-study/scripts/site_capture.py" http://localhost:3012 --slug 64-agency-landing-dopo` · stesso giro con manifest **vuoto** (`--slug 65-agency-landing-dopo-vuoto`) · `cantieri/…/MISURA-DOPO.md` (tabella Parte I rifatta, due colonne) | pieno ≤ 24.000 px / vuoto ≤ 21.000 desktop; mobile ≤ 40.000 / 36.000; 20 sezioni + coda, 0 divider; ≤ 12 dimensioni; 3 sfondi + fascia; 0 famiglie di gradiente; 10 CTA; 0 placeholder; ogni scarto con deroga scritta | `apex-critic` + `guild-design` | 3 | 6 |
| 6 | **F6 Test** | Playwright 390 px + 1440 px su `/`, `/prenota/` · Lighthouse mobile (home perf ≥ 85, a11y ≥ 95; `/prenota/` perf ≥ 70, a11y ≥ 95) · script `href` → HTTP 200 su tutti i link di `out/**/*.html` · prenotazione di prova su `/prenota/` (evento `call_prenotata` visto) · `reduced-motion` a mano | soglie sopra; 0 link rotti; 1 prenotazione di prova ricevuta e cancellata | `site-qa-mobile`, `site-qa-accessibility`, `site-qa-performance` | 3 | 5 |
| 7 | **F7 Deploy** | `cd $L && npx vercel --prod --yes` · `curl -sL https://agency-empire-landing.vercel.app \| grep -c "<H1 nuovo>"` ≥ 1 · `curl -sL …/prenota/` 200 · `curl -sL … \| grep -c "netlify.app"` = 0 · `curl -sL … \| grep -c 'name="robots"'` = 0 · **`curl -sL https://agency-empire-kohl.vercel.app \| grep -c "Automatizziamo la tua operatività"` ≥ 1 (l'altro sito intatto)** · screenshot del live in `cantieri/…/` · commit separato: rimozione `sections/_v1/` | tutte le 5 curl come sopra | Emperator | 1 | 5 |
| 8 | **F8 Retro** | `$F/cantieri/agency-empire-landing-vivo/LEZIONE.md` · riga in `cantieri/INDICE.md` · `gate_fatti.py` promosso a gate della Fabbrica · wiki (`Progetto_Sito_Agency_Vivo`) · `python scripts/checkpoint.py cp --titolo …` · `python scripts/checkpoint.py chiudi EMP-2AW3` · BACKLOG: riga "link `/prenota/` nella Bibbia dei Messaggi" (FN7) | LEZIONE esiste; CP coniato; ripresa chiusa | Emperator | 2 | 4 |
| | | | | **Totale 44 h · +20% = ≈ 53 h** | | **100** |

## Politica di guasto (per fase, ADR-028: nessun guasto ferma le sezioni intorno)

| Guasto | Chi lo vede | Cosa succede | Mai |
|---|---|---|---|
| Sezione bocciata da `gate_siti.py` / `gate_voce.py` / review "una voce sola" | F1, F4, F5 | torna allo scagnozzo **una** volta col verdetto esatto (riga del gate); alla seconda la riscrive Emperator | riscrivere il gate per farla passare |
| Pattern della Fabbrica che non passa `gate_siti.py` | F3 | la sezione usa il canone piatto; il pattern va in `BACKLOG.md` (ADR-005) | bloccare F4 per un pattern |
| `npm run build` rosso a metà F4 | F4 | `git stash` della sezione rotta; le altre si committano; la rotta si riapre da sola | committare un build rosso |
| Calendly non risponde 200 (F0) | F0 | `/prenota/` esce con `mailto:` + telefono da `contatti.ts`; "riattivare Calendly" in cima a STATO-EMPIRE | inventare un altro strumento di prenotazione |
| Ritratti / screenshot / Higgsfield non arrivano | F2 → F7 | si deploya la **composizione B** (C3.1); i file arrivano dopo senza toccare codice | segnaposto, still AURA in `public/`, "foto in arrivo" |
| P.IVA / sede / PEC non arrivano | F4b | `legal.ts` vuoto = riga non renderizzata; privacy/cookie escono comunque; riga per Max in STATO-EMPIRE | inventare dati legali; `href="#"` |
| Vercel Analytics spento | F0 | `analytics.tsx` in pagina, muto; `?da=` funziona lo stesso; riga per Max | rimandare il deploy per i dati |
| `project.json` ≠ `agency-empire-landing` o Max non conferma l'URL | F0 | **STOP di F0 soltanto** (è l'unica infattibilità: non si sa dove costruire); F1 (copy) e F2 (brief) continuano perché non toccano nessun deploy | dedurre il sito da una cartella (PM0) |
| Deploy su un URL diverso da quello del BRIEF | F7 | `vercel rollback` immediato; il curl sull'altro sito lo scopre | lasciare online un deploy sbagliato |
| Risorse di sessione < 20% | ogni fase | COMMIT della sezione verde + checkpoint + ripresa; la prossima non si apre (ADR-006) | "finisco solo questa" |
| Un'altra sessione tocca `agency-empire-landing/` | tutte | il blocco ⚠️ COORDINAMENTO in STATO-EMPIRE lo vieta; se succede: `git log` sul perimetro prima di ogni commit | rebase alla cieca |

## Percentuale nel battito (C3.5)
`% = Σ peso_fase × (gate PASS della fase / gate totali della fase)`, contata sul disco (file esistenti, exit dei gate).
F4a/F4b: `sezioni con gate_siti PASS / sezioni della metà`. 100% = F7 con le 5 curl verdi + F8 con CP coniato.

---

# PRE-MORTEM — come fallisce, e il gate che lo impedisce

| # | Modo di fallire | Segnale | Gate che lo ferma |
|---|---|---|---|
| PM0 | Cantiere sul sito sbagliato (già successo, 3 ore) | `project.json` ≠ landing; URL non confermato | F0: `project.json` + frase di Max nel BRIEF; F7: curl sull'altro sito |
| PM1 | Il sito nuovo finisce ancora su "Claude Code Mastery" | `netlify.app` nell'HTML | grep = 0 in F3, F4, F7 |
| PM2 | Google indicizza l'anteprima GitHub Pages come duplicato | `GH_PAGES_BASE` senza noindex | `robots` legato a `GH_PAGES_BASE` (C2.2) |
| PM3 | Still AURA sul dominio pubblico | file `sorgente=originale` in `public/` | F2 ∩ = ∅; `cantiere/` gitignored |
| PM4 | Tre voci in 20 sezioni | cambi di registro nella lettura di fila | `VOCE.md` in ogni prompt + `apex-critic` di fila |
| PM5 | Prezzo cambiato in un file e non negli altri | cifra letterale fuori da `listino.ts` | grep `€ x.xxx` = 0 |
| PM6 | ~~`next build` spegne `next dev`~~ | — | sparito: la misura serve `out/`, mai `next dev` |
| PM7 | Numero nel copy che nessuno sa da dove viene | cifra assente da `FATTI.md` | `gate_fatti.py` |
| PM8 | Segnaposto nell'hero o nei posti-foto al deploy | cornice vuota, "in arrivo" | composizione B + gate F5 con manifest vuoto |
| PM9 | Risultati che fingono, o nomi di clienti senza permesso | `TODO`, "Frase testuale", nome senza consenso | grep = 0; N11 a tre livelli; `data-fonte` |
| PM10 | Deploy prima dei test → Google vede la versione rotta | F7 senza F6 verde | ordine F6 → F7 nel V4; `robots` cambia solo nel commit di F7 |
| PM11 | Cookie Calendly senza informativa | `/cookie/` non nomina Calendly | gate F4b |
| PM12 | Le ore finiscono a metà F4 | budget < 20% | budget-guard + F4 in due metà |

---

# DIPENDONO DA MAX — in cima a STATO-EMPIRE quando parte il build (ADR-026), **nessuno blocca** (ADR-028)

1. Il «vai». 2. Ritratto suo (senza → hero a una colonna). 3. Ritratti di Gael e Leonardo (senza → N13 senza volti,
composizione B). 4. Higgsfield Plus (dossier 28) per 10 immagini (senza → composizione B). 5. `src` del video
(senza → N4 non si costruisce). 6. P.IVA / sede / PEC (senza → `legal.ts` vuoto). 7. Consenso scritto di
Novacar/Preventa per il nome in N11 (senza → "un concessionario del Nord Italia"). 8. Accendere Vercel Web Analytics
sul progetto. 9. Calendly attivo (oggi: 200 da verificare in F0).

---

# CONSIGLI — cosa nasce da questo studio oltre al sito (le 4 domande obbligatorie, ADR feedback 2026-09-10)

1. **Manca un agente?** No. Manca un **gesto d'apertura di cantiere**: `scripts/apri_cantiere.py <cartella>` stampa
   `project.json`, `npx vercel project ls`, l'URL live, l'ultimo deploy, l'ultimo commit, **e si ferma** finché nel
   BRIEF non c'è la frase del proprietario. Codice, non agente. Chiude PM0 per ogni sito futuro.
2. **Manca una skill?** No: mancano due **gate** in `fabbrica-siti/scripts/`: `gate_fatti.py` (C2.4) e il controllo
   "porta d'uscita" dentro `gate_siti.py` (ogni pagina con CTA: 0 `href="#"`, 0 domini terzi col brand sbagliato,
   ≥ 1 link a una pagina di prenotazione **nostra**). ADR-016 diventa meccanico.
3. **Un flusso da ridisegnare?** Sì: **"un sito nasce dall'URL live confermato dal proprietario, mai da una
   cartella"** → §13 in `CLAUDE-SITI.md` via ADR (candidata `ADR-030`). E il flusso "prezzo": `listino.ts` per sito è
   un cerotto — il listino DE è copiato in 68 file (studio Beggiato, log wiki 2026-09-10): serve `company/offerta.md`
   canonico da cui i siti generano `listino.ts`. Va in BACKLOG come B-0xx, non in questo cantiere.
4. **Del codice?** `apri_cantiere.py`, `gate_fatti.py`, patch a `gate_siti.py` (porta d'uscita), pattern
   `hero-due-composizioni` e `aura-composizione-b` nella Fabbrica.

## Connessioni
- `37-PIANO-SITO-AGENCY-VIVO-v1-SITO-SBAGLIATO.md` · branch `agency-empire-vivo-wip` · `capture/63-agency-landing-vero/`
- `fabbrica-siti/cantieri/agency-empire-vivo/LEZIONE.md` · SINTESI-SISTEMA-COPY / VISIVO · ANATOMIA-DEI-LANCI
- `28-HIGGSFIELD-ELEVENLABS` (immagini generate) · ADR-016 (ultimo metro) · ADR-028 (niente blocca tutto)
- `company/Memory/riprese/EMP-2AW3.md`
