---
Type: PROJECT
Status: Active
Tags: #agency #sito #solo-aggiunte #fabbrica-siti #piano #adr-030
Created: 2026-09-12
Last updated: 2026-09-12 (sera — P0 → 3 critiche → V4 esecutivo; build su «vai»)
---

# DOSSIER 38 — SITO AGENCY: PIANO «SOLO AGGIUNTE»
## Sito giusto: `agency-empire-landing/` → https://agency-empire-landing.vercel.app · legge: CLAUDE-SITI §13 (ADR-030)

> **Perché questo dossier esiste.** Il Dossier 37 v1 era sul sito sbagliato (`agency-empire`). Il 37 v2 era sul sito
> giusto ma **sostituiva** 37 sezioni con 20: Max lo ha visto online e lo ha bocciato. Questo è il **terzo piano**, con
> i due vincoli finalmente giusti insieme: **il sito è `agency-empire-landing`** (confermato da `.vercel/project.json`
> → `prj_34bLuVZNA8iqh9t2MAaK2j7M9D0c`, `npx vercel project ls`, e dalla frase di Max delle 22:05 dell'11/09) **e non si
> modifica nulla di ciò che è online: si aggiunge soltanto**. Il gate che lo prova è `gate_solo_aggiunte.py`.
>
> Il piano è in quattro giri (P0 → Critica 1 → P1 → Critica 2 → P2 → Critica 3 → P3) più il V4 esecutivo. **Nessuna riga
> di codice parte prima del «vai» di Max su questo dossier.** Artefatto: la pagina pubblicata da questa chat.

---

# §0 — COSA C'È ONLINE ADESSO (il «prima», intoccabile)

| Cosa | Stato al 12/09 sera | Tocco? |
|---|---|---|
| 34 sezioni di giugno in `src/components/sections/` (37 blocchi con i 3 divider) | live da 100 giorni, sorgente `57a0ba0b`, tag `agency-empire-landing-live-20260912` | **mai** |
| Header, sticky CTA (→ `chiamata-formazione.netlify.app`), `call-cta.tsx`, footer `href="#"`, `robots noindex` | com'erano | **mai** (tre decisioni di Max, §7) |
| 3 sezioni nostre: `specchio` (dopo Problems), `prove-vere` (dopo Results), `cosa-ottieni` (prima di FinalCTA) | online dal 12/09, CSS scopato `.vivo` | nostre: si correggono e si estendono per **inserimento** |
| Pagine nostre `/prenota/` (Calendly on demand), `/privacy/`, `/cookie/`; `src/lib/{fatti,listino,contatti,legal}.ts`; `vivo.css` | online dal 12/09 | nostre |
| `og.jpg` + Open Graph in `layout.tsx` (+12 righe); 2 refusi corretti | **build pronta, deploy prod a Max** (CP-20260912-X3A4) | — |

**Misure del live (Dossier 37, Parte I, ancora valide):** 38.683 px desktop / 64.255 mobile · 37 blocchi · 10 CTA (1 ogni
3.870 px) · **0 fotografie** · 186 dimensioni tipografiche · 5 famiglie di gradiente · `results.tsx` con segnaposto
(`IL_TUO_ID_LOOM`, "Frase testuale del cliente") · VSL con "312 · 24 · 1.4k" finti-live · Privacy/Termini `href="#"`.

---

# §1 — DIAGNOSI RIFATTA CON IL VINCOLO GIUSTO: cosa si cura aggiungendo, cosa no

Dei difetti misurati nel Dossier 37, **aggiungere cura solo alcuni**. Gli altri stanno dentro file che non si toccano:
si **segnalano a Max** (§7) e basta. Dirlo prima evita di promettere ciò che il vincolo non permette.

| Difetto del live | Si cura aggiungendo? | Come |
|---|---|---|
| 0 fotografie, nessun volto di un team di tre | **sì** | sezioni nuove con ritratti (composizione A: senza file rendono `null`) |
| La prova più importante è vuota (`results.tsx` segnaposto) | **in parte** | `prove-vere` c'è già; si aggiungono **immagini vere** (PDF PreventivoForge oscurato, dashboard) e un **video del sistema che gira** |
| Ultimo metro in 3 salti col brand del corso | **in parte** | `/prenota/` c'è; si aggiungono **fasce-prenota** dopo le sezioni decisive e lo **stato «prenotato»** nella pagina |
| Nessuna misura (B-043: DE non misura un euro) | **sì** | `@vercel/analytics` + eventi nostri (`?da=`, `calendly.event_scheduled`) |
| Nessuna anteprima quando si condivide il link | **fatto** (X3A4) | `og.jpg` + Open Graph — in attesa del deploy |
| Legale mancante (`TODO(N1)` nel codice) | **sì, con i dati di Max** | sezione «coda legale» prima del footer, renderizza solo con `legal.ts` pieno |
| Pagina non pronta per l'indice (nessun JSON-LD, nessuna sitemap) | **sì** | file nuovi; **valgono** solo quando Max toglie il `noindex` |
| Nessuna vita/movimento sopra il fold | **sì, una** | fascia-lampo dei fatti sotto l'hero (statica con `prefers-reduced-motion`) |
| 38.683 px, 5 gradienti, 186 dimensioni, Barnum, «12 mesi», numeri finti-live, `href="#"`, `noindex`, CTA al corso | **no** | dentro l'esistente → **lista di Max** (§7). Aggiungere non accorcia: **ogni aggiunta deve valere il suo spazio** |

**Il principio del cantiere:** un sito già lungo tollera aggiunte **basse e dense** (fasce, non sezioni), **vere** (nessun
segnaposto, nessuna cornice vuota), **misurate** (ogni aggiunta manda un evento), e **accendibili** (scheletri che restano
`null` finché il pezzo di Max non arriva — così la sua parte non ci ferma, ADR-028).

---

# §2 — P0: CATALOGO DELLE AGGIUNTE (prima stesura)

`▸ dopo <X />` = punto d'inserimento in `page.tsx` (una riga `+`). Tutto in `src/sezioni-aggiunte/` dentro `<div class="vivo">`.

| # | Aggiunta | Dove | Cosa | Input | Non duplica perché |
|---|---|---|---|---|---|
| A1 | **Fascia-lampo dei fatti** | ▸ dopo `<Hero />` | marquee di 5 fatti da `FATTI`: 3 sistemi · 7 giorni · 300 msg/giorno · 0 canoni · 90 giorni supporto; statica se reduced-motion | nostro | `science-stats` ha percentuali finte; qui **fatti con fonte**, e un elemento vivo |
| A2 | **Fasce-prenota** ×3 | ▸ dopo `<Pillars />`, `<PricingROI />`, `<Objections />` | una riga + `BottonePrenota` → `/prenota/?da=…`; ≤ 120 px | nostro | le CTA esistenti vanno al corso; queste sono la **porta nostra** ripetuta dove si decide |
| A3 | **Misura** | `layout.tsx` (+2), `package.json` (+1), `analytics.tsx` nuovo | Vercel Web Analytics + eventi: `cta_click{da}`, `prenota_view{da}`, `call_prenotata{da}`, `scroll_50/90` | nostro + toggle Vercel (Max) | non esiste nulla |
| A4 | **La stanza — tre volti** | ▸ dopo `<WhoGuides />` | 3 ritratti (Max, Gael, Leonardo) + nome + una riga; composizione A | **ritratti (Max)** | `who-guides` ha il testo «chi siete»; qui i **volti**, che non ci sono |
| A5 | **Guardalo girare** | ▸ dopo `<OutreachInside />` | video 60-90 s dell'Outreach Factory che gira (mp4/Loom), poster, `<details>` con cosa si vede | **registrazione (Max)** | `vsl` è il video di vendita; questo è la **prova** del sistema |
| A6 | **Immagini vere in `prove-vere`** | dentro `prove-vere.tsx` (inserimento) | PDF PreventivoForge con nome coperto, screenshot dashboard Preventa | nostro (consenso Novacar per il nome: Max) | estende una sezione **nostra** |
| A7 | **Coda legale** | ▸ prima del `<footer>` | ragione sociale, P.IVA, sede, PEC, link `/privacy/` `/cookie/`; `null` se `legal.ts` vuoto | **dati (Max)** | il footer resta; questa aggiunge i dati che mancano |
| A8 | **Pronto per l'indice** | `layout.tsx` (+JSON-LD), `public/sitemap.xml`, `public/robots.txt` | `Organization` + `Service`×3 + `FAQPage` (domande lette da `faq.tsx`, senza toccarlo) | nostro; **vale dopo il noindex (Max)** | non esiste nulla |
| A9 | **Immagini nelle sezioni nostre** | `specchio`, `cosa-ottieni`, fasce | still generati nel registro AURA (Higgsfield) con riga su banda scura | **acquisto Higgsfield (Max)** | solo sezioni nostre |
| A10 | **`/prenota/` stato «prenotato»** | `prenota/page.tsx` + `calendario.tsx` (inserimenti) | su `calendly.event_scheduled`: blocco «Fatto. Cosa preparare in 3 righe» + evento `call_prenotata` | nostro; slug Calendly 30 min (Max) | pagina nostra |
| A11 | **Anteprima di condivisione** | fatto (X3A4) | `og.jpg` + OG/Twitter | deploy (Max) | — |

---

# §3 — CRITICA 1 → P1 (attacca P0)

**C1.1 — «Undici aggiunte su un sito di 38.683 px: lo allunghi ancora».** Vero. Regola di P1: **budget di altezza**
+3.000 px desktop massimo per tutto il cantiere (−: A2 fasce 3×120, A1 90, A4 ≤ 640, A5 ≤ 560, A7 ≤ 160 → ≈ 1.800 px;
A6/A9 non aggiungono altezza, A3/A8/A10/A11 sono zero px). Misura prima/dopo con `capture` (`MISURA-DOPO.md`). Se
un'aggiunta sfonda il budget, si taglia l'aggiunta, non il budget.

**C1.2 — «Tre fasce-prenota sono spam».** Tre CTA in più portano il sito da 10 a 13 CTA su 40.000 px (1 ogni 3.000):
ancora sotto Pascu (1/844). Ma la fascia va dove **si è appena deciso qualcosa**: dopo i prezzi (sì), dopo le obiezioni
(sì), dopo Pillars (no: è a metà della spiegazione). P1: **due fasce**, testo diverso per ciascuna, `aria-label` diverso.

**C1.3 — «A4 e A5 senza i file di Max sono cornici vuote: la trappola del prototipo».** P1 conferma la composizione A del
Dossier 37: il componente rende **`null`** finché il file non esiste in `public/`; il gate `aura_prep.py --check` fallisce
se un file dichiarato nel manifest manca. Zero cornici vuote online, mai.

**C1.4 — «A3 tocca `package.json`: è una modifica».** È una riga `+` in un file che Max non «vede»; il gate parte B la
conta come aggiunta (0 righe rimosse). P1 lo dichiara nel checkpoint e nel commit, con `npm ci` pulito.

**C1.5 — «A5: chi registra il video? Se è Max, non lo farà domani».** P1 offre l'alternativa: **posso registrarlo io**
(Playwright registra lo schermo del sistema in un `--prova` con numeri e nomi oscurati), Max lo approva in anteprima
prima che vada online. Non blocca (ADR-028): lo scheletro va su, il video quando c'è.

**C1.6 — «A7 duplica il footer».** Il footer resta con `href="#"` (Max). La coda legale non ripete il footer: **aggiunge**
ragione sociale, P.IVA, sede, PEC e i link veri. Senza dati resta `null`. Quando Max deciderà sul footer, si vedrà se
tenerla o se il footer la assorbe (allora sarà una modifica ordinata da lui).

**C1.7 — «A8 con `noindex` è lavoro morto».** No: è **pronto**, e costa 2 ore; il giorno che Max toglie il `noindex` il
sito è indicizzabile in una riga. Ma P1 lo mette **ultimo** fra le cose nostre.

---

# §4 — CRITICA 2 → P2 (attacca P1)

**C2.1 — «Il gate testo non vede il reso: due refusi sono stati online 23 ore».** P2 aggiunge a ogni fase un gate che
non c'era: **screenshot desktop 1440 + mobile 390 di ogni aggiunta, GUARDATO** (non solo prodotto) prima del deploy,
con `qa_live.py` promosso a `fabbrica-siti/scripts/qa_reso.py` (console 0 errori, link 100% 200, ancore esistenti).

**C2.2 — «La fascia-lampo è un'animazione: §7».** P2: `@media (prefers-reduced-motion: reduce)` → fascia statica, i
5 fatti in una riga; nessun JS, solo CSS `@keyframes`. Peso: 0 KB di JS.

**C2.3 — «Misurare cosa? "Analytics" senza domanda è vanità».** P2 fissa **le tre domande** a cui i dati rispondono:
(1) da quale sezione si arriva a `/prenota/` (`?da=`), (2) quanti di quelli prenotano davvero (`call_prenotata`), (3)
dove la gente smette di leggere (`scroll_50/90`). Cinque eventi, non venti. Report letto da Emperator ogni settimana
nel battito (B-043 chiuso quando esce il primo numero vero).

**C2.4 — «Ogni deploy vuole l'anteprima di Max? Allora non ci muoviamo più».** P2 distingue: **aggiunte pure passate
dal gate → produzione diretta** (è la legge §13: il gate prova che nulla è cambiato). **Anteprima obbligatoria** solo
per ciò che Max deve *vedere* perché è suo: i suoi ritratti in pagina (A4), il video (A5), i dati legali (A7).

**C2.5 — «Il deploy prod al bot è negato dal classificatore»** (fatto misurato, 2 tentativi il 12/09). P2: ogni fase
finisce con **build + gate + anteprima Vercel (`npx vercel`) + commit**; il `--prod` lo lancia Max con un comando
copiato dal battito, oppure aggiunge la regola di permesso in `settings.json`. Non è un blocco: è l'ultimo metro suo.

**C2.6 — «A6: il PDF di Novacar è di un cliente».** Nome, targhe, prezzi coperti con banda scura ≥ 7:1 (legge del
11/09); il nome del cliente si scrive solo con consenso scritto (già nel copy di `prove-vere`). Se il consenso non arriva,
il PDF resta anonimo: vale lo stesso come prova del sistema.

**C2.7 — «A10: Calendly gratuito non fa redirect dopo la prenotazione».** Giusto — per questo P2 usa il `postMessage`
`calendly.event_scheduled` (funziona sul piano gratuito) e mostra il blocco «prenotato» **nella nostra pagina**, senza
redirect. Il cambio slug (evento agenzia da 30 min) resta di Max.

---

# §5 — CRITICA 3 → P3 (attacca P2)

**C3.1 — «Metà del piano dipende da Max: se non muove un dito, il cantiere sembra fermo».** P3 separa **due corsie**
esplicite e le stampa nel battito con due percentuali:
- **Corsia nostra (si fa da subito, nessun input):** A1, A2, A3, A6 (anonimo), A8, A10, scheletri di A4/A5/A7 → **≈ 70%**
  del valore del cantiere.
- **Corsia di Max (accende ciò che è già costruito):** ritratti, video, dati legali, consenso, Higgsfield, slug Calendly,
  toggle Analytics, `noindex`, CTA vecchie, footer, deploy → ogni gesto **accende** una parte, nessuno **ferma** nulla.

**C3.2 — «L'ordine di P2 è per comodità nostra, non per risultato».** P3 riordina: prima ciò che **cambia il risultato**
e si vede (misura + ultimo metro: A3, A2, A10), poi la **prova** (A6, scheletro A5), poi la **vita** (A1, scheletro A4),
poi il **pronto** (A7, A8). Se il «vai» arriva e domani il sito deve rendere, i primi tre giorni fanno la differenza.

**C3.3 — «Le sezioni nostre aggiunte il 12/09 non sono state guardate da Max».** Vero: le ha viste online insieme alla
bocciatura del resto. P3 mette in **F0** una riga: *Max, le tre sezioni (specchio, prove-vere, cosa-ottieni) e `/prenota/`
restano?* Se dice di toglierne una, è una **cancellazione ordinata da lui**, l'unica modifica ammessa.

**C3.4 — «Manca il criterio di fine».** P3 lo scrive: il cantiere è chiuso quando (a) tutte le aggiunte della corsia
nostra sono online col gate a exit 0, (b) gli scheletri esistono e rendono `null`, (c) il primo report di misura ha
almeno un numero vero, (d) `LEZIONE.md` ha l'esito, (e) i pattern usati due volte (fascia-prenota, coda-legale) sono
promossi nella Fabbrica. Le accensioni di Max **non** sono nel criterio: arrivano quando arrivano.

**C3.5 — «Chi riprende questo cantiere fra un mese non sa da dove».** P3 fissa la ripresa: `EMP-XR4F` resta il codice,
la cartella del cantiere `fabbrica-siti/cantieri/agency-empire-landing-vivo/` resta la stessa (BRIEF aggiornato con
§0 di questo dossier), ogni fase chiude con un CP che nomina la fase successiva.

---

# §6 — V4 ESECUTIVO (P3 messo in fasi)

Ogni fase: **comandi**, **gate exit 0**, **output**, **chi**, **ore**, **peso nel battito**. Il «vai» di Max apre F0.
Gate comuni a ogni fase (G*): `npm run build` OK · `gate_solo_aggiunte.py --live … --build out/index.html --base
agency-empire-landing-live-20260912 --cartella agency-empire-landing` exit 0 · `gate_fatti.py` sul copy nuovo · screenshot
1440+390 **guardati** · console 0 errori · link 100% 200 · `npx vercel` (anteprima) · commit + push · `--prod` da Max.

| F | Fase | Cosa si fa (comandi/file) | Gate proprio | Chi | h | Peso |
|---|---|---|---|---|---|---|
| F0 | **Apertura** | BRIEF aggiornato (§0, URL + `project.json` + frase di Max); domanda C3.3; baseline: altezza px, Lighthouse mobile del live (`npx serve out` o live), n. CTA; deploy di X3A4 (og.jpg) lanciato da Max | baseline in `MISURA-DOPO.md`; og.jpg 200 sul live | Emperator (+Max: deploy) | 1 | 5% |
| F1 | **Misura (A3)** | `npm i @vercel/analytics`; `src/sezioni-aggiunte/analytics.tsx` (5 eventi, legge `?da=`, ascolta `calendly.event_scheduled`); `layout.tsx` +2 righe | eventi visibili nel `console.debug` in dev; `package.json` +1/−0 | Emperator | 3 | 15% |
| F2 | **Ultimo metro (A2 + A10)** | `fascia-prenota.tsx` ×2 (dopo `<PricingROI />`, dopo `<Objections />`, testo diverso, `aria-label` diverso); `/prenota/` stato «prenotato» via `postMessage`; slug Calendly quando c'è | +2 righe in `page.tsx`; altezza +≤ 240 px; test manuale della prenotazione in anteprima | Emperator | 4 | 15% |
| F3 | **Prova (A6 + scheletro A5)** | immagini in `prove-vere.tsx` (PDF PreventivoForge oscurato: banda ≥ 7:1, `aura_prep.py`), `guardalo-girare.tsx` (video slot, `null` senza `src`, `<details>`); proposta: registrazione mia con `--prova` oscurato → anteprima a Max | `aura_prep.py --check` PASS; testo di `prove-vere` = live (gate parte A: solo `insert`) | Emperator (+Max: video o ok alla mia registrazione) | 4 | 15% |
| F4 | **Vita (A1 + scheletro A4)** | `fascia-lampo.tsx` (CSS only, reduced-motion statica) dopo `<Hero />`; `stanza.tsx` (3 ritratti, `null` senza file) dopo `<WhoGuides />`; `public/aura/manifest.json` con i 3 posti | 0 KB JS aggiunto; §7 verificato con emulazione reduced-motion; altezza +≤ 730 px | Emperator (+Max: ritratti) | 4 | 15% |
| F5 | **Pronto (A7 + A8)** | `coda-legale.tsx` prima del footer (`null` con `legal.ts` vuoto); JSON-LD in `layout.tsx` (+1 `<script type="application/ld+json">`), `public/sitemap.xml`, `public/robots.txt` | validatore schema 0 errori; `sitemap.xml` 200 in anteprima | Emperator (+Max: dati legali, noindex) | 3 | 10% |
| F6 | **Accensioni** | per ogni gesto di Max arrivato: file in `public/`, una riga in `contatti.ts`/`legal.ts`, `aura_prep.py`; **anteprima a Max** prima di `--prod` | manifest `--check` PASS; screenshot guardati da Max | Emperator + Max | 3 | 15% |
| F7 | **Chiusura** | `MISURA-DOPO.md` (px, CTA, Lighthouse, eventi arrivati), `LEZIONE.md` esito, pattern promossi (`fascia-prenota`, `coda-legale`, `fascia-lampo` già c'è), CP, STATO, wiki, chiusura ripresa | criterio C3.4 (a)-(e) | Emperator | 1 | 10% |

**Totale corsia nostra: ≈ 20 h · +≤ 3.000 px · 0 righe rimosse.** Le accensioni (F6) valgono il 15% e arrivano
quando Max muove i suoi pezzi: il battito dice **«nostra X% · Max Y%»**.

## Politica di guasto (ADR-028)
- Gate `gate_solo_aggiunte` FAIL → non si deploya; si cerca la riga, mai `--consenti` su testo di giugno.
- `--prod` negato al bot → comando nel battito, Max lo lancia; il lavoro continua sulla fase dopo.
- Un file di Max non arriva → lo scheletro resta `null`, la fase è chiusa lo stesso; F6 lo accende quando arriva.
- Un'aggiunta sfonda il budget di altezza → si taglia l'aggiunta (fascia al posto di sezione), non il budget.
- Max boccia un'aggiunta vista online → si **toglie** quell'aggiunta (file nostro), si scrive in `LEZIONE.md`, il resto resta.

## Percentuale nel battito
`% = Σ pesi delle fasi chiuse col gate a exit 0`, due numeri: **nostra** (F0-F5, F7 = 85%) e **Max** (F6 = 15%, per
gesto: ritratti 5 · video 4 · legale 3 · Calendly 2 · noindex 1). 100% solo a cantiere chiuso (C3.4), mai a pezzo finito.

---

# §7 — LA LISTA DI MAX (gesti che accendono, nessuno ferma — ADR-026/028)

| Gesto | Cosa accende | Quanto conta | Dove si vede |
|---|---|---|---|
| `cd agency-empire-landing && npx vercel --prod --yes` | og.jpg + refusi corretti (X3A4) e ogni fase successiva | ultimo metro di ogni fase | STATO-EMPIRE, in cima |
| Evento Calendly «Chiamata Digital Empire · 30 min» (slug) | `/prenota/` coerente (oggi apre «90% formazione 10% Peach · 1 h») | alto: è la porta | F2 |
| 3 ritratti (Max, Gael, Leonardo), anche da telefono, luce naturale | la stanza dei tre volti (A4) + hero due composizioni in futuro | alto: 0 volti oggi | F4 → F6 |
| Video 60-90 s del sistema che gira (o «sì» alla mia registrazione oscurata) | Guardalo girare (A5) | alto: la prova che manca | F3 → F6 |
| Ragione sociale, P.IVA, sede, PEC | coda legale (A7), `/privacy/` `/cookie/` completi | medio: fiducia + obbligo | F5 → F6 |
| Consenso scritto Novacar/Preventa al nome | il nome nel caso di `prove-vere` | medio | F3 |
| Higgsfield Plus (dossier 28) | immagini AURA nelle sezioni nostre (A9) | medio | F6 |
| Toggle **Web Analytics** nel progetto Vercel | i 5 eventi arrivano | alto: senza, si costruisce al buio | F1 |
| **Decisione:** togliere `noindex` | A8 vale; il sito esiste per Google | tua | F5 |
| **Decisione:** CTA vecchie → `/prenota/` | fine dei 3 salti col brand del corso (modifica: anteprima prima) | tua | — |
| **Decisione:** footer con link veri | `href="#"` → `/privacy/` `/cookie/` (modifica: anteprima prima) | tua | — |
| **Risposta C3.3:** le 3 sezioni + `/prenota/` del 12/09 restano? | se una va tolta, la tolgo io (cancellazione ordinata) | — | F0 |

---

# §8 — COSA NON SI FARÀ IN QUESTO CANTIERE, anche se sembra ovvio
- Accorciare, riordinare, riscrivere o «migliorare» una delle 34 sezioni di giugno. Nemmeno un `alt`. Nemmeno un refuso.
- Toccare header, sticky, `call-cta.tsx`, footer, `robots`, `globals.css`, `next.config`.
- Aggiungere una sezione il cui copy esiste già in pagina (scala, canone, processo, per-chi, garanzia, obiezioni: misurato).
- Mettere online una cornice vuota, un segnaposto, un numero senza fonte, un contatto inventato, uno still AURA di terzi.
- Un `--prod` senza gate a exit 0 e senza screenshot guardato.

---

## Connessioni
- `37-PIANO-SITO-AGENCY-VIVO.md` (diagnosi misurata, riusata; il piano di sostituzione è **superato** da questo)
- `company/Memory/decisions/ADR-030-sito-online-solo-aggiungere.md` · `.claude/skills/fabbrica-siti/CLAUDE-SITI.md` §13
- `.claude/skills/fabbrica-siti/scripts/gate_solo_aggiunte.py` · `og_stampo.py` · `gate_fatti.py` · `gate_voce.py`
- `.claude/skills/fabbrica-siti/cantieri/agency-empire-landing-vivo/` (BRIEF, VOCE, FATTI, COPY, LEZIONE)
- `company/Memory/checkpoints/CP-20260912-7ZNY.md` (ripristino) · `CP-20260912-X3A4.md` (QA, og, gate) · ripresa `EMP-XR4F`
- wiki: `projects/Agency/Progetto_Sito_Agency_Vivo`, `tools/Tool_Fabbrica_Siti`
